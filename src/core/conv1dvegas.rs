use crate::dis::CoeffFuncs as Cf1D;

use mchep::integrand::Integrand;
use mchep::vegas::VegasResult;
use mchep::vegasplus::VegasPlus;

/// Fixed VEGAS+ settings.
///
/// mchep interprets target_accuracy as a percentage.
/// So 0.001 means 0.001%.
const VEGAS_TARGET_ACCURACY_PERCENT: f64 = 0.001;

// Aggressive fixed defaults.
// These can be tuned later after benchmarking.
const VEGAS_N_ITER: usize = 50;
const VEGAS_N_EVAL: usize = 1_000_000;
const VEGAS_N_BINS: usize = 128;
const VEGAS_ALPHA: f64 = 1.0;
const VEGAS_N_STRAT: usize = 8;
const VEGAS_BETA: f64 = 0.75;

const VEGAS_SEED_POINT: u64 = 13579;
const VEGAS_SEED_BIN_2D: u64 = 24680;
const VEGAS_SEED_BIN_1D: u64 = 24681;

/// Build a VEGAS+ integrator on the unit hypercube [0,1]^dim.
fn make_vegas(dim: usize, seed: u64) -> VegasPlus {
    let boundaries: Vec<(f64, f64)> = vec![(0.0, 1.0); dim];

    let mut vegas = VegasPlus::new(
        VEGAS_N_ITER,
        VEGAS_N_EVAL,
        VEGAS_N_BINS,
        VEGAS_ALPHA,
        VEGAS_N_STRAT,
        VEGAS_BETA,
        &boundaries,
    );

    vegas.set_seed(seed);
    vegas
}

//
// =========================
//  Conv1DPoint using VEGAS+
// =========================
//
// Computes
//   ∫_x^1 d xhat [ r(xhat,nf) * term + s(xhat,nf) * (term - pdf(x,q)) ]
//   + l(x,nf) * pdf(x,q)
//
// with
//   term = pdf(x/xhat, q) / xhat
//
// We map xhat ∈ [x,1] to u ∈ [0,1]:
//   xhat = x + (1 - x) u
//   d xhat = (1 - x) du
//

pub struct Conv1DPointVegas {
    pub x: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf1D,
    pub pid: i32,
    pub fxq: fn(i32, f64, f64) -> f64,
}

impl Conv1DPointVegas {
    pub fn new(
        x: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf1D,
        pid: i32,
        fxq: fn(i32, f64, f64) -> f64,
    ) -> Self {
        Self {
            x,
            q,
            nf,
            coeff_func,
            pid,
            fxq,
        }
    }

    /// Central value only.
    pub fn compute(&self) -> f64 {
        self.compute_full().value
    }

    /// Full VEGAS+ result.
    pub fn compute_full(&self) -> VegasResult {
        assert!(self.x > 0.0 && self.x <= 1.0, "x must satisfy 0 < x <= 1");

        let integrand = PointIntegrand {
            x: self.x,
            q: self.q,
            nf: self.nf,
            coeff_func: self.coeff_func,
            pid: self.pid,
            fxq: self.fxq,
        };

        let mut vegas = make_vegas(1, VEGAS_SEED_POINT);
        let mut result = vegas.integrate(&integrand, Some(VEGAS_TARGET_ACCURACY_PERCENT));

        // Add the local term outside the MC integral.
        let pdf_at_x = (self.fxq)(self.pid, self.x, self.q);
        result.value += self.coeff_func.l(self.x, self.nf) * pdf_at_x;

        result
    }
}

struct PointIntegrand {
    x: f64,
    q: f64,
    nf: f64,
    coeff_func: Cf1D,
    pid: i32,
    fxq: fn(i32, f64, f64) -> f64,
}

impl Integrand for PointIntegrand {
    fn dim(&self) -> usize {
        1
    }

    fn eval(&self, point: &[f64]) -> f64 {
        let u = point[0];

        if !(0.0..=1.0).contains(&u) {
            return 0.0;
        }

        let xhat = self.x + (1.0 - self.x) * u;
        let jac = 1.0 - self.x;

        if xhat <= 0.0 || xhat < self.x || xhat > 1.0 {
            return 0.0;
        }

        let pdf_at_x = (self.fxq)(self.pid, self.x, self.q);
        let pdf_val = (self.fxq)(self.pid, self.x / xhat, self.q);
        let term_val = pdf_val / xhat;

        jac * (
            self.coeff_func.r(xhat, self.nf) * term_val
                + self.coeff_func.s(xhat, self.nf) * (term_val - pdf_at_x)
        )
    }
}

//
// =======================
//  Conv1DBin using VEGAS+
// =======================
//
// Computes
//   ∫_{xmin}^{xmax} dx ∫_x^1 d xhat [ ... ]
//   + ∫_{xmin}^{xmax} dx l(x,nf) * pdf(x,q)
//
// The double-integral region is triangular:
//   xmin <= x <= xmax
//   x <= xhat <= 1
//
// We map (u,v) ∈ [0,1]^2 to that region by
//   x    = xmin + (xmax - xmin) u
//   xhat = x + (1 - x) v
//
// Jacobian:
//   J = (xmax - xmin) (1 - x)
//
// The local x-only term is computed separately as a 1D integral.
//

pub struct Conv1DBinVegas {
    pub xmin: f64,
    pub xmax: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf1D,
    pub pid: i32,
    pub fxq: fn(i32, f64, f64) -> f64,
}

impl Conv1DBinVegas {
    pub fn new(
        xmin: f64,
        xmax: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf1D,
        pid: i32,
        fxq: fn(i32, f64, f64) -> f64,
    ) -> Self {
        Self {
            xmin,
            xmax,
            q,
            nf,
            coeff_func,
            pid,
            fxq,
        }
    }

    /// Central value only.
    pub fn compute(&self) -> f64 {
        self.compute_full().value
    }

    /// Full VEGAS+ result.
    ///
    /// The error is the quadrature combination of the 2D and 1D MC errors.
    /// The chi2_dof is kept from the 2D piece.
    pub fn compute_full(&self) -> VegasResult {
        assert!(self.xmin > 0.0, "xmin must be > 0");
        assert!(self.xmax <= 1.0, "xmax must be <= 1");
        assert!(self.xmin < self.xmax, "require xmin < xmax");

        // 2D double-integral piece
        let integrand_2d = BinDoubleIntegrand {
            xmin: self.xmin,
            xmax: self.xmax,
            q: self.q,
            nf: self.nf,
            coeff_func: self.coeff_func,
            pid: self.pid,
            fxq: self.fxq,
        };

        let mut vegas_2d = make_vegas(2, VEGAS_SEED_BIN_2D);
        let mut res_2d = vegas_2d.integrate(&integrand_2d, Some(VEGAS_TARGET_ACCURACY_PERCENT));

        // 1D local term piece
        let integrand_1d = BinLocalIntegrand {
            xmin: self.xmin,
            xmax: self.xmax,
            q: self.q,
            nf: self.nf,
            coeff_func: self.coeff_func,
            pid: self.pid,
            fxq: self.fxq,
        };

        let mut vegas_1d = make_vegas(1, VEGAS_SEED_BIN_1D);
        let res_1d = vegas_1d.integrate(&integrand_1d, Some(VEGAS_TARGET_ACCURACY_PERCENT));

        res_2d.value += res_1d.value;
        res_2d.error = (res_2d.error.powi(2) + res_1d.error.powi(2)).sqrt();

        res_2d
    }
}

struct BinDoubleIntegrand {
    xmin: f64,
    xmax: f64,
    q: f64,
    nf: f64,
    coeff_func: Cf1D,
    pid: i32,
    fxq: fn(i32, f64, f64) -> f64,
}

impl Integrand for BinDoubleIntegrand {
    fn dim(&self) -> usize {
        2
    }

    fn eval(&self, point: &[f64]) -> f64 {
        let u = point[0];
        let v = point[1];

        if !(0.0..=1.0).contains(&u) || !(0.0..=1.0).contains(&v) {
            return 0.0;
        }

        let x = self.xmin + (self.xmax - self.xmin) * u;
        let xhat = x + (1.0 - x) * v;
        let jac = (self.xmax - self.xmin) * (1.0 - x);

        if x <= 0.0 || x > 1.0 || xhat <= 0.0 || xhat < x || xhat > 1.0 {
            return 0.0;
        }

        let pdf_at_x = (self.fxq)(self.pid, x, self.q);
        let pdf_val = (self.fxq)(self.pid, x / xhat, self.q);
        let term_val = pdf_val / xhat;

        jac * (
            self.coeff_func.r(xhat, self.nf) * term_val
                + self.coeff_func.s(xhat, self.nf) * (term_val - pdf_at_x)
        )
    }
}

struct BinLocalIntegrand {
    xmin: f64,
    xmax: f64,
    q: f64,
    nf: f64,
    coeff_func: Cf1D,
    pid: i32,
    fxq: fn(i32, f64, f64) -> f64,
}

impl Integrand for BinLocalIntegrand {
    fn dim(&self) -> usize {
        1
    }

    fn eval(&self, point: &[f64]) -> f64 {
        let u = point[0];

        if !(0.0..=1.0).contains(&u) {
            return 0.0;
        }

        let x = self.xmin + (self.xmax - self.xmin) * u;
        let jac = self.xmax - self.xmin;

        let pdf_at_x = (self.fxq)(self.pid, x, self.q);

        jac * self.coeff_func.l(x, self.nf) * pdf_at_x
    }
}