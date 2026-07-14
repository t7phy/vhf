//! Cubic spline interpolation of 1-D data.
//!
//! Self-contained equivalent of `scipy.interpolate.CubicSpline` for scalar
//! data: a piecewise cubic, twice continuously differentiable interpolant.
//! Construction follows scipy's algorithm exactly (scipy's version is pure
//! Python + LAPACK; there is no FITPACK involved, unlike the bivariate
//! classes): the C2 continuity conditions are written as a tridiagonal
//! linear system in the first derivatives s[i] at the data sites, the
//! system is solved with partial pivoting (scipy calls LAPACK `dgbsv` via
//! `solve_banded`; the solver below is the tridiagonal equivalent of
//! LAPACK `dgtsv`), and each segment is converted from Hermite form to
//! local power-basis coefficients, scipy's `PPoly` representation. The C2
//! interpolant with given boundary conditions is unique, so the resulting
//! spline is identical to scipy's up to rounding.
//!
//! Boundary conditions map to scipy's `bc_type` as follows:
//! `Boundary::NotAKnot` is `'not-a-knot'` (scipy's default),
//! `Boundary::SecondDeriv(0.0)` is `'natural'`,
//! `Boundary::FirstDeriv(0.0)` is `'clamped'`, and
//! `FirstDeriv(v)` / `SecondDeriv(v)` are the per-end tuples `(1, v)` /
//! `(2, v)`. scipy's `'periodic'` is deliberately not implemented: it needs
//! a separate cyclic solver and only matters for periodic tables; it can be
//! added if ever needed.
//!
//! Out-of-range arguments are extrapolated with the boundary polynomial
//! pieces, which is scipy's default (`extrapolate=True`). Note this is the
//! opposite convention from the companion `RectBivariateSpline` module,
//! which clamps to the grid edge because that is what FITPACK does; here
//! scipy genuinely extrapolates, so this module does too. Clamp the
//! argument at the call site if edge-value behaviour is wanted.

/// Boundary condition at one end of the spline.
#[derive(Clone, Copy, Debug, PartialEq)]
pub enum Boundary {
    /// Third derivative continuous across the first/last interior knot
    /// (scipy's default). With n = 2 this degenerates, as in scipy, to a
    /// straight line; with n = 3 at both ends, to the parabola through the
    /// three points.
    NotAKnot,
    /// Prescribed first derivative at the endpoint; `FirstDeriv(0.0)` is
    /// scipy's `'clamped'`.
    FirstDeriv(f64),
    /// Prescribed second derivative at the endpoint; `SecondDeriv(0.0)` is
    /// scipy's `'natural'`.
    SecondDeriv(f64),
}

/// Piecewise-cubic C2 interpolant through `(x[i], y[i])`.
pub struct CubicSpline {
    x: Vec<f64>,
    /// Per-segment local power-basis coefficients `[a0, a1, a2, a3]`:
    /// `S(u) = a0 + a1*d + a2*d^2 + a3*d^3` with `d = u - x[i]`.
    seg: Vec<[f64; 4]>,
}

impl CubicSpline {
    /// Build with scipy's default boundary conditions (not-a-knot at both
    /// ends).
    pub fn new(x: &[f64], y: &[f64]) -> Self {
        Self::with_bc(x, y, Boundary::NotAKnot, Boundary::NotAKnot)
    }

    /// Build with explicit boundary conditions at the start and end.
    ///
    /// `x` must be finite and strictly increasing with at least 2 points;
    /// `y` must be finite and of the same length. Invalid input panics (a
    /// malformed table is a programming error, and a constructor has no
    /// NaN-like value to return); `ev`/`ev_deriv` never panic.
    pub fn with_bc(x: &[f64], y: &[f64], start: Boundary, end: Boundary) -> Self {
        let n = x.len();
        assert!(n >= 2, "need at least 2 points");
        assert_eq!(y.len(), n, "x and y must have the same length");
        assert!(
            x[0].is_finite() && x.windows(2).all(|w| w[0] < w[1] && w[1].is_finite()),
            "x must be finite and strictly increasing"
        );
        assert!(y.iter().all(|v| v.is_finite()), "y must be finite");

        let dx: Vec<f64> = x.windows(2).map(|w| w[1] - w[0]).collect();
        let slope: Vec<f64> =
            dx.iter().zip(y.windows(2)).map(|(h, w)| (w[1] - w[0]) / h).collect();

        // As in scipy, a not-a-knot condition with n == 2 is replaced by
        // "first derivative equals the slope of the line through the data".
        let fix = |bc| if bc == Boundary::NotAKnot { Boundary::FirstDeriv(slope[0]) } else { bc };
        let (start, end) = if n == 2 { (fix(start), fix(end)) } else { (start, end) };

        // Tridiagonal system for the first derivatives s[i] at the sites:
        // row i (interior):
        //   dx[i]*s[i-1] + 2*(dx[i-1]+dx[i])*s[i] + dx[i-1]*s[i+1]
        //     = 3*(dx[i]*slope[i-1] + dx[i-1]*slope[i])
        // with the first and last rows supplied by the boundary conditions.
        let mut dl = vec![0.0; n]; // dl[i] multiplies s[i-1] in row i
        let mut d = vec![0.0; n];
        let mut du = vec![0.0; n]; // du[i] multiplies s[i+1] in row i
        let mut rhs = vec![0.0; n];

        if n == 3 && start == Boundary::NotAKnot && end == Boundary::NotAKnot {
            // Both not-a-knot conditions fall on the same (single) interior
            // knot; the convention, as in scipy, is the parabola through the
            // three points.
            d[0] = 1.0;
            du[0] = 1.0;
            rhs[0] = 2.0 * slope[0];
            dl[1] = dx[1];
            d[1] = 2.0 * (dx[0] + dx[1]);
            du[1] = dx[0];
            rhs[1] = 3.0 * (dx[1] * slope[0] + dx[0] * slope[1]);
            dl[2] = 1.0;
            d[2] = 1.0;
            rhs[2] = 2.0 * slope[1];
        } else {
            for i in 1..n - 1 {
                dl[i] = dx[i];
                d[i] = 2.0 * (dx[i - 1] + dx[i]);
                du[i] = dx[i - 1];
                rhs[i] = 3.0 * (dx[i] * slope[i - 1] + dx[i - 1] * slope[i]);
            }
            match start {
                Boundary::NotAKnot => {
                    let w = x[2] - x[0];
                    d[0] = dx[1];
                    du[0] = w;
                    rhs[0] =
                        ((dx[0] + 2.0 * w) * dx[1] * slope[0] + dx[0] * dx[0] * slope[1]) / w;
                }
                Boundary::FirstDeriv(v) => {
                    d[0] = 1.0;
                    rhs[0] = v;
                }
                Boundary::SecondDeriv(v) => {
                    d[0] = 2.0 * dx[0];
                    du[0] = dx[0];
                    rhs[0] = -0.5 * v * dx[0] * dx[0] + 3.0 * (y[1] - y[0]);
                }
            }
            match end {
                Boundary::NotAKnot => {
                    let w = x[n - 1] - x[n - 3];
                    d[n - 1] = dx[n - 3];
                    dl[n - 1] = w;
                    rhs[n - 1] = (dx[n - 2] * dx[n - 2] * slope[n - 3]
                        + (2.0 * w + dx[n - 2]) * dx[n - 3] * slope[n - 2])
                        / w;
                }
                Boundary::FirstDeriv(v) => {
                    d[n - 1] = 1.0;
                    rhs[n - 1] = v;
                }
                Boundary::SecondDeriv(v) => {
                    d[n - 1] = 2.0 * dx[n - 2];
                    dl[n - 1] = dx[n - 2];
                    rhs[n - 1] = 0.5 * v * dx[n - 2] * dx[n - 2] + 3.0 * (y[n - 1] - y[n - 2]);
                }
            }
        }

        let s = solve_tridiagonal(&mut dl, &mut d, &mut du, &mut rhs);

        // Hermite form (values + first derivatives) -> local power basis,
        // same formulas as scipy's CubicHermiteSpline.
        let seg = (0..n - 1)
            .map(|i| {
                let t = (s[i] + s[i + 1] - 2.0 * slope[i]) / dx[i];
                [y[i], s[i], (slope[i] - s[i]) / dx[i] - t, t / dx[i]]
            })
            .collect();
        Self { x: x.to_vec(), seg }
    }

    /// Index of the polynomial piece used for `u`; out-of-range arguments
    /// select the boundary piece, which yields polynomial extrapolation.
    fn segment(&self, u: f64) -> usize {
        let x = &self.x;
        let last = x.len() - 2;
        if !(u > x[0]) {
            return 0;
        }
        if u >= x[last + 1] {
            return last;
        }
        let (mut lo, mut hi) = (0, last);
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if x[mid] <= u {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }

    /// Evaluate the spline at a single point.
    pub fn ev(&self, u: f64) -> f64 {
        let i = self.segment(u);
        let t = u - self.x[i];
        let [a0, a1, a2, a3] = self.seg[i];
        ((a3 * t + a2) * t + a1) * t + a0
    }

    /// Evaluate the `nu`-th derivative at a single point (`nu = 0` is the
    /// value itself; derivatives of order > 3 are identically zero).
    /// Equivalent to scipy's `cs(u, nu)`.
    pub fn ev_deriv(&self, u: f64, nu: u32) -> f64 {
        let i = self.segment(u);
        let t = u - self.x[i];
        let [a0, a1, a2, a3] = self.seg[i];
        match nu {
            0 => ((a3 * t + a2) * t + a1) * t + a0,
            1 => (3.0 * a3 * t + 2.0 * a2) * t + a1,
            2 => 6.0 * a3 * t + 2.0 * a2,
            3 => 6.0 * a3,
            _ => 0.0,
        }
    }
}

/// Solve a tridiagonal system in place with partial pivoting (the algorithm
/// of LAPACK's `dgtsv`; row interchanges create a second super-diagonal,
/// `du2`). scipy reaches the same solution through `solve_banded`, which
/// calls LAPACK's `dgbsv`. The not-a-knot boundary rows are not diagonally
/// dominant, so a plain Thomas algorithm without pivoting would be the one
/// shortcut too far here.
fn solve_tridiagonal(dl: &mut [f64], d: &mut [f64], du: &mut [f64], rhs: &mut [f64]) -> Vec<f64> {
    let n = d.len();
    let mut du2 = vec![0.0; n];
    for i in 0..n - 1 {
        if d[i].abs() >= dl[i + 1].abs() {
            // No interchange.
            assert!(d[i] != 0.0, "singular spline system");
            let m = dl[i + 1] / d[i];
            d[i + 1] -= m * du[i];
            rhs[i + 1] -= m * rhs[i];
        } else {
            // Interchange rows i and i+1.
            let m = d[i] / dl[i + 1];
            let (dn, dun) = (d[i + 1], du[i + 1]);
            d[i] = dl[i + 1];
            d[i + 1] = du[i] - m * dn;
            du[i] = dn;
            du2[i] = dun;
            du[i + 1] = -m * dun;
            let r = rhs[i];
            rhs[i] = rhs[i + 1];
            rhs[i + 1] = r - m * rhs[i];
        }
    }
    assert!(d[n - 1] != 0.0, "singular spline system");

    let mut sol = vec![0.0; n];
    sol[n - 1] = rhs[n - 1] / d[n - 1];
    if n >= 2 {
        sol[n - 2] = (rhs[n - 2] - du[n - 2] * sol[n - 1]) / d[n - 2];
    }
    for i in (0..n.saturating_sub(2)).rev() {
        sol[i] = (rhs[i] - du[i] * sol[i + 1] - du2[i] * sol[i + 2]) / d[i];
    }
    sol
}

#[cfg(test)]
mod tests {
    use super::*;

    const X: [f64; 7] = [0.0, 0.4, 1.1, 1.9, 2.3, 3.0, 3.8];

    fn ys() -> Vec<f64> {
        X.iter().map(|&x| (1.7 * x).sin() + 0.3 * x * x).collect()
    }

    #[test]
    fn passes_through_data_points() {
        let y = ys();
        let cases = [
            (Boundary::NotAKnot, Boundary::NotAKnot),
            (Boundary::SecondDeriv(0.0), Boundary::SecondDeriv(0.0)),
            (Boundary::FirstDeriv(1.5), Boundary::SecondDeriv(-2.0)),
        ];
        for &(b0, b1) in &cases {
            let s = CubicSpline::with_bc(&X, &y, b0, b1);
            for (i, &xi) in X.iter().enumerate() {
                assert!((s.ev(xi) - y[i]).abs() < 1e-12, "{b0:?},{b1:?} at x={xi}");
            }
        }
    }

    #[test]
    fn not_a_knot_reproduces_a_cubic_exactly() {
        // A single cubic polynomial satisfies the not-a-knot conditions, so
        // the interpolant must reproduce it everywhere, including under
        // extrapolation on both sides.
        let p = |x: f64| 1.0 - 2.0 * x + 0.7 * x * x + 0.31 * x * x * x;
        let y: Vec<f64> = X.iter().map(|&x| p(x)).collect();
        let s = CubicSpline::new(&X, &y);
        for &q in &[-1.0, 0.05, 1.3, 2.71, 3.79, 5.0] {
            assert!((s.ev(q) - p(q)).abs() < 1e-10 * (1.0 + p(q).abs()), "at u={q}");
        }
    }

    #[test]
    fn boundary_conditions_hold() {
        let y = ys();
        let s =
            CubicSpline::with_bc(&X, &y, Boundary::FirstDeriv(0.75), Boundary::SecondDeriv(-1.25));
        assert!((s.ev_deriv(X[0], 1) - 0.75).abs() < 1e-12);
        assert!((s.ev_deriv(X[6], 2) + 1.25).abs() < 1e-12);
        let nat =
            CubicSpline::with_bc(&X, &y, Boundary::SecondDeriv(0.0), Boundary::SecondDeriv(0.0));
        assert!(nat.ev_deriv(X[0], 2).abs() < 1e-12);
        assert!(nat.ev_deriv(X[6], 2).abs() < 1e-12);
    }

    #[test]
    fn c2_continuity_at_interior_knots() {
        let y = ys();
        let s = CubicSpline::new(&X, &y);
        for i in 1..X.len() - 1 {
            let h = X[i] - X[i - 1];
            let [_, _, a2l, a3l] = s.seg[i - 1];
            let [_, _, a2r, _] = s.seg[i];
            let (left, right) = (2.0 * a2l + 6.0 * a3l * h, 2.0 * a2r);
            assert!((left - right).abs() < 1e-9 * (1.0 + right.abs()), "knot {i}");
        }
    }

    #[test]
    fn small_n_special_cases() {
        // n = 2: not-a-knot degenerates to the straight line through the
        // points (and extrapolates linearly).
        let s = CubicSpline::new(&[1.0, 3.0], &[2.0, 8.0]);
        assert!((s.ev(1.5) - 3.5).abs() < 1e-14);
        assert!((s.ev(4.0) - 11.0).abs() < 1e-13);
        // n = 3 with not-a-knot at both ends: the parabola through the points.
        let q = |x: f64| 2.0 + 0.5 * x - 0.75 * x * x;
        let xs = [0.0, 1.0, 2.5];
        let yq: Vec<f64> = xs.iter().map(|&x| q(x)).collect();
        let s = CubicSpline::new(&xs, &yq);
        for &t in &[-0.5, 0.4, 1.9, 3.0] {
            assert!((s.ev(t) - q(t)).abs() < 1e-12, "at u={t}");
        }
    }

    #[test]
    fn matches_scipy_reference_values() {
        // Reference values computed with scipy 1.17.1:
        //   CubicSpline(X, Y, bc_type=(start, end))(q, nu)
        // on the grid above with y = sin(1.7 x) + 0.3 x^2. Boundary encoding:
        // 0 = not-a-knot, 1 = (1, v), 2 = (2, v). A direct comparison over 14
        // randomized cases (840 points, all bc kinds, n = 2..2000, spacing
        // spanning 11 orders of magnitude, derivatives 0..2, out-of-range
        // queries) showed agreement to < 5e-14 relative; these spot values
        // pin that down in CI.
        let bc = |code: usize, v: f64| match code {
            0 => Boundary::NotAKnot,
            1 => Boundary::FirstDeriv(v),
            _ => Boundary::SecondDeriv(v),
        };
        #[rustfmt::skip]
        let reference = [
            (0, 0.0, 0, 0.0, 0.2, 0, 3.5521421644685858e-01),
            (0, 0.0, 0, 0.0, 1.05, 0, 1.3064101514642408e+00),
            (0, 0.0, 0, 0.0, -0.6, 0, -1.1158578809307145e+00),
            (0, 0.0, 0, 0.0, 4.3, 0, 7.0875012629919230e+00),
            (0, 0.0, 0, 0.0, 1.7, 1, -6.1616968367110458e-01),
            (0, 0.0, 0, 0.0, 2.9, 2, 2.9149926852963404e+00),
            (2, 0.0, 2, 0.0, 0.2, 0, 3.5146727418975315e-01),
            (2, 0.0, 2, 0.0, 2.42, 0, 9.3337356227690826e-01),
            (2, 0.0, 2, 0.0, 4.1, 1, 3.6985641943193532e+00),
            (1, 0.75, 2, -1.25, 0.9, 0, 1.2597084355630686e+00),
            (1, 0.75, 2, -1.25, 3.1, 0, 2.0446928925594734e+00),
            (1, 0.75, 2, -1.25, 2.0, 1, -4.3391273661412866e-01),
            (1, 0.75, 2, -1.25, 1.5, 2, -7.4642813148182663e-01),
        ];
        let y = ys();
        let mut cached: Option<((usize, usize), CubicSpline)> = None;
        for &(c0, v0, c1, v1, q, nu, want) in &reference {
            if cached.as_ref().map(|(k, _)| *k) != Some((c0, c1)) {
                cached = Some(((c0, c1), CubicSpline::with_bc(&X, &y, bc(c0, v0), bc(c1, v1))));
            }
            let v = cached.as_ref().unwrap().1.ev_deriv(q, nu);
            assert!(
                (v - want).abs() < 1e-13 * (1.0 + want.abs()),
                "bc=({c0},{c1}) at (u={q}, nu={nu}): {v} vs scipy {want}"
            );
        }
    }
}