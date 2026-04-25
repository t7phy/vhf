use crate::dis::CoeffFuncs as Cf1D;
use super::interpolation::{BasisCache, compute_basis_functions, point_interpolator, interpolator, integration_regions};

// Adjust this path to wherever you placed your custom quad function.
use crate::core::quad::{quad, nquad, Bound};

use rayon::prelude::*;


const EPS_INTEGRATION_BORDER: f64 = 1e-10;

/// Pointwise convolution using custom adaptive G7-K15 quadrature.
///
/// Computes
///   ∫_x^1 d xhat [ r(xhat,nf) * term + s(xhat,nf) * (term - pdf(x,q)) ]
///   + l(x,nf) * pdf(x,q)
///
/// with
///   term = pdf(x/xhat, q) / xhat
pub struct Conv1DPointQuad {
    pub x: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf1D,
    pub pid: i32,
    pub fxq: fn(i32, f64, f64) -> f64,
    pub epsrel: f64,
}

impl Conv1DPointQuad {
    pub fn new(
        x: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf1D,
        pid: i32,
        fxq: fn(i32, f64, f64) -> f64,
        epsrel: f64,
    ) -> Self {
        Self {
            x,
            q,
            nf,
            coeff_func,
            pid,
            fxq,
            epsrel,
        }
    }

    /// Returns only the central value.
    pub fn compute(&self) -> f64 {
        self.compute_full().0
    }

    /// Returns (value, estimated_error).
    pub fn compute_full(&self) -> (f64, f64) {
        assert!(self.x > 0.0 && self.x <= 1.0, "x must satisfy 0 < x <= 1");

        let x = self.x;
        let q = self.q;
        let nf = self.nf;
        let pid = self.pid;
        let fxq = self.fxq;
        let coeff_func = self.coeff_func;

        let pdf_at_x = fxq(pid, x, q);

        let (integral_val, integral_err) = quad(
            |xhat: f64| -> f64 {
                // if xhat <= 0.0 || xhat < x || xhat > 1.0 {
                //     return 0.0;
                // }

                let pdf_val = fxq(pid, x / xhat, q);
                let term_val = pdf_val / xhat;

                coeff_func.r(xhat, nf) * term_val
                    + coeff_func.s(xhat, nf) * (term_val - pdf_at_x)
            },
            x,
            1.0,
            self.epsrel,
        );

        let local_term = coeff_func.l(x, nf) * pdf_at_x;

        (integral_val + local_term, integral_err)
    }
}

/// Bin-integrated convolution using custom adaptive G7-K15 quadrature.
///
/// Computes
///   ∫_{xmin}^{xmax} dx [
///       ∫_x^1 d xhat [ r(xhat,nf) * term + s(xhat,nf) * (term - pdf(x,q)) ]
///       + l(x,nf) * pdf(x,q)
///   ]
///
/// with
///   term = pdf(x/xhat, q) / xhat

pub struct Conv1DBinQuad {
    pub xmin: f64,
    pub xmax: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf1D,
    pub pid: i32,
    pub fxq: fn(i32, f64, f64) -> f64,
    pub epsrel: f64,
}

impl Conv1DBinQuad {
    pub fn new(
        xmin: f64,
        xmax: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf1D,
        pid: i32,
        fxq: fn(i32, f64, f64) -> f64,
        epsrel: f64,
    ) -> Self {
        Self {
            xmin,
            xmax,
            q,
            nf,
            coeff_func,
            pid,
            fxq,
            epsrel,
        }
    }

    pub fn compute(&self) -> f64 {
        self.compute_full().0
    }

    pub fn compute_full(&self) -> (f64, f64) {
        assert!(self.xmin > 0.0, "xmin must be > 0");
        assert!(self.xmax <= 1.0, "xmax must be <= 1");
        assert!(self.xmin < self.xmax, "require xmin < xmax");

        let xmin = self.xmin;
        let xmax = self.xmax;
        let q = self.q;
        let nf = self.nf;
        let pid = self.pid;
        let fxq = self.fxq;
        let coeff_func = self.coeff_func;
        let epsrel = self.epsrel;

        // Double piece:
        // ∫_{xmin}^{xmax} dx ∫_x^1 d xhat [ r(...) * term + s(...) * (term - f(x)) ]
        let bounds = vec![
            Bound::Fixed(xmin, xmax),
            Bound::Dynamic(Box::new(|args: &[f64]| {
                let x = args[0];
                (x, 1.0)
            })),
        ];

        let (double_val, double_err) = nquad(
            |args: &[f64]| -> f64 {
                let x = args[0];
                let xhat = args[1];

                let pdf_at_x = fxq(pid, x, q);
                let pdf_val = fxq(pid, x / xhat, q);
                let term_val = pdf_val / xhat;

                coeff_func.r(xhat, nf) * term_val
                    + coeff_func.s(xhat, nf) * (term_val - pdf_at_x)
            },
            &bounds,
            epsrel,
        );

        // Local term:
        // ∫_{xmin}^{xmax} dx l(x,nf) f(x,q)
        let (local_val, local_err) = quad(
            |x: f64| -> f64 {
                let pdf_at_x = fxq(pid, x, q);
                coeff_func.l(x, nf) * pdf_at_x
            },
            xmin,
            xmax,
            epsrel,
        );

        let total_val = double_val + local_val;
        let total_err = (double_err.powi(2) + local_err.powi(2)).sqrt();

        (total_val, total_err)
    }
}


pub struct Conv1DPointGrid {
    pub x: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf1D,
    // pub obs_def_func: fn(f64, f64) -> f64,
    pub itp_xgrid: Vec<f64>,
    pub mode_log: bool,
    pub basis_functions: BasisCache,
    pub interpolator_at_x: Vec<f64>,
    pub integration_regions: Option<Vec<(f64, f64)>>,
}

impl Conv1DPointGrid {
    pub fn new(
        x: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf1D,
        // obs_def_func: fn(f64, f64) -> f64,
        itp_xgrid: Vec<f64>,
        mode_log: bool,
    ) -> Self {
        let basis_functions = compute_basis_functions(itp_xgrid.clone(), 4, mode_log);
        let interpolator_at_x = interpolator(x, &basis_functions);
        let regions = integration_regions(x, &itp_xgrid);

        Self {
            x,
            q,
            nf,
            coeff_func,
            // obs_def_func,
            itp_xgrid,
            mode_log,
            basis_functions,
            interpolator_at_x,
            integration_regions: regions,
        }
    }

    pub fn compute(&self) -> Vec<f64> {
        (0..self.itp_xgrid.len())
            .into_par_iter()
            .map(|xnode| {
                let mut res: f64 = 0.0;

                let pieces = &self.basis_functions.functions[xnode];
                let max_xmax_raw = pieces.last().unwrap().xmax;
                let max_xmax = if self.mode_log {
                    max_xmax_raw.exp()
                } else {
                    max_xmax_raw
                };

                if self.x >= (1.0 - EPS_INTEGRATION_BORDER) || max_xmax <= self.x {
                    return 0.0;
                }

                if let Some(ref regions) = self.integration_regions {
                    for i in regions {
                        let a = i.0 * (1.0 + EPS_INTEGRATION_BORDER);
                        let b = i.1 * (1.0 - EPS_INTEGRATION_BORDER);

                        if b <= a {
                            continue;
                        }

                        let epsrel = 1e-6;

                        let (quad_val, _quad_err) = quad(
                            |xhat: f64| -> f64 {
                                if xhat <= 0.0 || xhat >= 1.0 {
                                    return 0.0;
                                }

                                let interp_val =
                                    point_interpolator(self.x / xhat, &self.basis_functions, xnode);
                                let term_val = interp_val / xhat;

                                let mut val: f64 = 0.0;
                                val += self.coeff_func.r(xhat, self.nf) * term_val;
                                val += self.coeff_func.s(xhat, self.nf)
                                    * (term_val - self.interpolator_at_x[xnode]);
                                // val *= (self.obs_def_func)(self.x, self.q);
                                val
                            },
                            a,
                            b,
                            epsrel,
                        );

                        res += quad_val;
                    }
                }

                res += self.coeff_func.l(self.x, self.nf) * self.interpolator_at_x[xnode];
                res
            })
            .collect()
    }
}
