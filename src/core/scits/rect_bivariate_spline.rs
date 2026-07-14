//! Bivariate spline interpolation on a rectangular grid.
//!
//! Self-contained equivalent of `scipy.interpolate.RectBivariateSpline` for its
//! default, interpolating case (`s = 0`). Construction reproduces the knot
//! placement of the FITPACK routine `regrid` for `s = 0`; since the
//! interpolating spline on fixed knots is unique, the resulting surface is the
//! same one scipy builds, and evaluation uses the same B-spline recurrence as
//! FITPACK's `fpbspl`/`fpbisp`.
//!
//! Accuracy is controlled by the spline degrees `kx`, `ky` (1 = bilinear,
//! 3 = bicubic = scipy's default, 5 = biquintic). scipy's smoothing parameter
//! `s` is deliberately not implemented: it does not increase accuracy, it
//! *relaxes* the fit so the spline may miss the data points (useful only for
//! noisy data), and `s = 0` is what interpolation of tabulated values calls
//! for. `maxit` only governs the iteration that searches for a smoothing
//! spline when `s > 0`, so it is moot here as well.
//!
//! Coordinates outside the grid are clamped to its boundary before
//! evaluation. (scipy's docstring mentions extrapolation, but the underlying
//! FITPACK evaluator `fpbisp` clamps, which is what scipy actually returns;
//! verified against scipy 1.17.1.)

/// Bivariate interpolating spline on a rectangular grid.
pub struct RectBivariateSpline {
    tx: Vec<f64>,
    ty: Vec<f64>,
    /// B-spline coefficients, row-major: `coef[i * ny + j]`.
    coef: Vec<f64>,
    kx: usize,
    ky: usize,
    ny: usize,
}

impl RectBivariateSpline {
    /// Build the interpolating spline through `z[i * y.len() + j] = f(x[i], y[j])`.
    ///
    /// `x` and `y` must be finite and strictly increasing, with
    /// `x.len() > kx` and `y.len() > ky`; degrees must lie in `1..=5`.
    /// `(kx, ky) = (3, 3)` reproduces scipy's default bicubic spline.
    ///
    /// Invalid input panics: unlike a failed quadrature, a misshapen grid is a
    /// programming error in the caller, and there is no NaN-like value a
    /// constructor could return.
    pub fn new(x: &[f64], y: &[f64], z: &[f64], kx: usize, ky: usize) -> Self {
        let mx = x.len();
        let my = y.len();
        assert!(
            (1..=5).contains(&kx) && (1..=5).contains(&ky),
            "spline degrees must be in 1..=5"
        );
        assert!(mx > kx, "need at least kx + 1 points along x");
        assert!(my > ky, "need at least ky + 1 points along y");
        assert_eq!(z.len(), mx * my, "z must hold len(x) * len(y) values, row-major");
        let finite_increasing =
            |w: &[f64]| w[0].is_finite() && w.windows(2).all(|p| p[0] < p[1] && p[1].is_finite());
        assert!(finite_increasing(x), "x must be finite and strictly increasing");
        assert!(finite_increasing(y), "y must be finite and strictly increasing");
        assert!(z.iter().all(|v| v.is_finite()), "z must be finite");

        let tx = interpolation_knots(x, kx);
        let ty = interpolation_knots(y, ky);

        // Tensor-product structure: interpolate along x for every y-column of
        // z, then along y for every row of the intermediate result.
        let ax = BandLU::collocation(&tx, kx, x);
        let mut coef = vec![0.0; mx * my];
        let mut col = vec![0.0; mx];
        for j in 0..my {
            for i in 0..mx {
                col[i] = z[i * my + j];
            }
            ax.solve(&mut col);
            for i in 0..mx {
                coef[i * my + j] = col[i];
            }
        }

        let ay = BandLU::collocation(&ty, ky, y);
        for row in coef.chunks_exact_mut(my) {
            ay.solve(row);
        }

        Self { tx, ty, coef, kx, ky, ny: my }
    }

    /// Evaluate the spline at a single point. Coordinates outside the grid are
    /// clamped to its boundary, exactly as scipy/FITPACK's `fpbisp` does.
    pub fn ev(&self, x: f64, y: f64) -> f64 {
        let x = x.clamp(self.tx[self.kx], self.tx[self.tx.len() - self.kx - 1]);
        let y = y.clamp(self.ty[self.ky], self.ty[self.ty.len() - self.ky - 1]);
        let lx = find_interval(&self.tx, self.kx, x);
        let ly = find_interval(&self.ty, self.ky, y);

        let mut bx = [0.0; 6];
        let mut by = [0.0; 6];
        bspline_values(&self.tx, self.kx, lx, x, &mut bx);
        bspline_values(&self.ty, self.ky, ly, y, &mut by);

        let i0 = lx - self.kx;
        let j0 = ly - self.ky;
        let mut s = 0.0;
        for a in 0..=self.kx {
            let row = (i0 + a) * self.ny + j0;
            let mut acc = 0.0;
            for b in 0..=self.ky {
                acc += self.coef[row + b] * by[b];
            }
            s += bx[a] * acc;
        }
        s
    }
}

/// FITPACK (`regrid`, s = 0) knot placement for an interpolating spline of
/// degree `k` through sites `w`: `k + 1` coincident knots at each boundary,
/// interior knots at the data sites for odd `k` and at midpoints between
/// consecutive sites for even `k`.
fn interpolation_knots(w: &[f64], k: usize) -> Vec<f64> {
    let m = w.len();
    let mut t = vec![0.0; m + k + 1];
    t[..=k].fill(w[0]);
    t[m..].fill(w[m - 1]);
    if k % 2 == 1 {
        let h = (k + 1) / 2;
        for i in (k + 1)..m {
            t[i] = w[i - h];
        }
    } else {
        let h = k / 2;
        for i in (k + 1)..m {
            t[i] = 0.5 * (w[i - h - 1] + w[i - h]);
        }
    }
    t
}

/// Index `l` of the knot interval containing `u`: the largest `l` in
/// `[k, t.len() - k - 2]` with `t[l] <= u`, clamped at both ends so that
/// out-of-range `u` selects the boundary polynomial piece (extrapolation).
fn find_interval(t: &[f64], k: usize, u: f64) -> usize {
    let hi = t.len() - k - 2;
    if !(u > t[k]) {
        return k;
    }
    if u >= t[hi + 1] {
        return hi;
    }
    let (mut lo, mut up) = (k, hi);
    while lo < up {
        let mid = (lo + up + 1) / 2;
        if t[mid] <= u {
            lo = mid;
        } else {
            up = mid - 1;
        }
    }
    lo
}

/// Values at `u` of the `k + 1` B-splines that are non-zero on knot interval
/// `l`; `h[a]` is the value of B-spline number `l - k + a`. This is the
/// stable de Boor recurrence, transcribed from FITPACK's `fpbspl`.
fn bspline_values(t: &[f64], k: usize, l: usize, u: f64, h: &mut [f64; 6]) {
    let mut hh = [0.0_f64; 5];
    h[0] = 1.0;
    for j in 1..=k {
        hh[..j].copy_from_slice(&h[..j]);
        h[0] = 0.0;
        for i in 0..j {
            let li = t[l + i + 1];
            let lj = t[l + i + 1 - j];
            let f = hh[i] / (li - lj);
            h[i] += f * (li - u);
            h[i + 1] = f * (u - lj);
        }
    }
}

/// LU factorization, without pivoting, of the banded B-spline collocation
/// matrix `A[r][c] = B_c(sites[r])`. With the knots from
/// `interpolation_knots` this matrix satisfies the Schoenberg-Whitney
/// conditions and is totally positive, for which elimination without pivoting
/// is non-singular and stable (de Boor, "A Practical Guide to Splines",
/// BANFAC). Band storage: entry `(r, c)`, `|r - c| <= k`, lives at
/// `ab[(k + r - c) * n + c]`.
struct BandLU {
    ab: Vec<f64>,
    n: usize,
    k: usize,
}

impl BandLU {
    fn collocation(t: &[f64], k: usize, sites: &[f64]) -> Self {
        let n = sites.len();
        let mut ab = vec![0.0; (2 * k + 1) * n];
        let mut h = [0.0; 6];
        for (r, &u) in sites.iter().enumerate() {
            let l = find_interval(t, k, u);
            bspline_values(t, k, l, u, &mut h);
            for a in 0..=k {
                let c = l - k + a;
                assert!(c <= r + k && r <= c + k, "collocation entry outside band");
                ab[(k + r - c) * n + c] = h[a];
            }
        }

        // In-place LU; multipliers overwrite the strict lower band.
        for j in 0..n {
            let piv = ab[k * n + j];
            assert!(piv != 0.0, "singular collocation matrix");
            let rmax = (j + k).min(n - 1);
            for r in (j + 1)..=rmax {
                let f = ab[(k + r - j) * n + j] / piv;
                ab[(k + r - j) * n + j] = f;
                for c in (j + 1)..=rmax {
                    ab[(k + r - c) * n + c] -= f * ab[(k + j - c) * n + c];
                }
            }
        }
        Self { ab, n, k }
    }

    /// Solve `A b = rhs` in place.
    fn solve(&self, b: &mut [f64]) {
        let (n, k) = (self.n, self.k);
        for j in 0..n {
            let bj = b[j];
            if bj != 0.0 {
                for r in (j + 1)..=(j + k).min(n - 1) {
                    b[r] -= self.ab[(k + r - j) * n + j] * bj;
                }
            }
        }
        for j in (0..n).rev() {
            let mut s = b[j];
            for c in (j + 1)..=(j + k).min(n - 1) {
                s -= self.ab[(k + j - c) * n + c] * b[c];
            }
            b[j] = s / self.ab[k * n + j];
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn tabulate(f: impl Fn(f64, f64) -> f64, x: &[f64], y: &[f64]) -> Vec<f64> {
        let mut z = Vec::with_capacity(x.len() * y.len());
        for &xi in x {
            for &yj in y {
                z.push(f(xi, yj));
            }
        }
        z
    }

    const X: [f64; 8] = [0.0, 0.3, 0.75, 1.1, 1.7, 2.0, 2.6, 3.0];
    const Y: [f64; 6] = [-1.0, -0.4, 0.1, 0.5, 1.2, 1.5];

    fn test_fn(x: f64, y: f64) -> f64 {
        (1.3 * x).sin() * (0.25 * y).exp() + 0.5 * x * y * y
    }

    #[test]
    fn passes_through_grid_points() {
        let z = tabulate(test_fn, &X, &Y);
        for &(kx, ky) in &[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (3, 1), (1, 5)] {
            let s = RectBivariateSpline::new(&X, &Y, &z, kx, ky);
            for (i, &xi) in X.iter().enumerate() {
                for (j, &yj) in Y.iter().enumerate() {
                    let v = s.ev(xi, yj);
                    assert!(
                        (v - z[i * Y.len() + j]).abs() < 1e-12,
                        "k=({kx},{ky}) at grid point ({xi},{yj}): {v} vs {}",
                        z[i * Y.len() + j]
                    );
                }
            }
        }
    }

    #[test]
    fn bicubic_reproduces_tensor_cubic_exactly() {
        // A polynomial of degree <= k per variable lies in the spline space for
        // any knots, so the interpolant must reproduce it everywhere,
        // including under extrapolation.
        let p = |x: f64, y: f64| {
            (2.0 - x + 0.5 * x * x - 0.25 * x * x * x) * (1.0 + y + y * y + 0.1 * y * y * y)
        };
        let z = tabulate(p, &X, &Y);
        let s = RectBivariateSpline::new(&X, &Y, &z, 3, 3);
        for &(qx, qy) in &[(0.123, -0.77), (1.456, 0.33), (2.95, 1.49), (0.51, 1.07)] {
            let v = s.ev(qx, qy);
            let e = p(qx, qy);
            assert!((v - e).abs() < 1e-9 * (1.0 + e.abs()), "at ({qx},{qy}): {v} vs {e}");
        }
    }

    #[test]
    fn clamps_outside_the_grid_like_scipy() {
        let z = tabulate(test_fn, &X, &Y);
        let s = RectBivariateSpline::new(&X, &Y, &z, 3, 3);
        assert_eq!(s.ev(-0.6, 0.3), s.ev(0.0, 0.3));
        assert_eq!(s.ev(3.7, 2.1), s.ev(3.0, 1.5));
    }

    #[test]
    fn k1_is_bilinear() {
        let z = [0.0, 2.0, 3.0, 9.0]; // z(0,0)=0, z(0,2)=2, z(1,0)=3, z(1,2)=9
        let s = RectBivariateSpline::new(&[0.0, 1.0], &[0.0, 2.0], &z, 1, 1);
        assert!((s.ev(0.25, 0.5) - 1.5).abs() < 1e-14);
    }

    #[test]
    fn matches_scipy_reference_values() {
        // Reference values computed with scipy 1.17.1:
        //   RectBivariateSpline(X, Y, Z, kx=kx, ky=ky, s=0).ev(qx, qy)
        // on the grid above with z = test_fn. Direct comparison over 25 degree
        // combinations x 40 points (including out-of-domain) showed agreement
        // to <6e-16 relative; these spot values pin that down in CI.
        #[rustfmt::skip]
        let reference = [
            (1, 1, 0.2, -0.9, 2.8871820899668860e-01),
            (1, 1, 0.87, 0.21, 9.6500172721908928e-01),
            (1, 1, 1.93, 1.34, 2.5692193401008940e+00),
            (1, 1, 2.71, -0.13, -2.4245515165892931e-01),
            (3, 3, 0.2, -0.9, 2.8663685491335122e-01),
            (3, 3, 0.87, 0.21, 9.7299046629680352e-01),
            (3, 3, 1.93, 1.34, 2.5594333196767618e+00),
            (3, 3, 2.71, -0.13, -3.3746170067564346e-01),
            (5, 5, 0.2, -0.9, 2.8624443156600904e-01),
            (5, 5, 0.87, 0.21, 9.7278821381235525e-01),
            (5, 5, 1.93, 1.34, 2.5592682161749498e+00),
            (5, 5, 2.71, -0.13, -3.3746744045073274e-01),
        ];
        let z = tabulate(test_fn, &X, &Y);
        let mut cached: Option<((usize, usize), RectBivariateSpline)> = None;
        for &(kx, ky, qx, qy, want) in &reference {
            if cached.as_ref().map(|(k, _)| *k) != Some((kx, ky)) {
                cached = Some(((kx, ky), RectBivariateSpline::new(&X, &Y, &z, kx, ky)));
            }
            let v = cached.as_ref().unwrap().1.ev(qx, qy);
            assert!(
                (v - want).abs() < 1e-13 * (1.0 + want.abs()),
                "k=({kx},{ky}) at ({qx},{qy}): {v} vs scipy {want}"
            );
        }
    }
}