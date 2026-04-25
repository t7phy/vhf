use super::interpolation::{BasisCache, compute_basis_functions, point_interpolator, interpolator, integration_regions};
use scirs2_integrate::quad::{quad, QuadOptions};
use crate::dis::internal::CoeffFuncs as Cf1D;
use rayon::prelude::*;

use mchep::vegas::{Vegas, VegasResult};
use mchep::integrand::Integrand;
use mchep::vegasplus::VegasPlus;

const EPS_INTEGRATION_BORDER: f64 = 1e-10;

pub struct Conv1DPoint {
    pub x: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf1D,
    pub pid: i32,
    pub pdf_xfxq: fn(i32, f64, f64) -> f64,
}

impl Conv1DPoint {
    pub fn new(x: f64, q: f64, nf: f64, coeff_func: Cf1D, pid: i32, pdf_xfxq: fn(i32, f64, f64) -> f64) -> Self {
        Self {
            x,
            q,
            nf,
            coeff_func,
            pid,
            pdf_xfxq,
        }
    }

    pub fn compute(&self) -> f64 {
        // let has_r = self.coeff_func.r.is_some();
        // let has_s = self.coeff_func.s.is_some();
        // let has_l = self.coeff_func.l.is_some();
        let mut res: f64 = 0.0;

        let quad_options = QuadOptions {
            abs_tol: 1e-11,
            rel_tol: 1e-6,
            max_evals: 1_000_000, 
            use_abs_error: false,
            use_simpson: false,
        };

        let pdf_at_x = (self.pdf_xfxq)(self.pid, self.x, self.q);

        let integration_result = quad(
            |xhat: f64| -> f64{

                let mut val: f64= 0.0;

                if xhat <= 0.0 || xhat >= 1.0 { return 0.0; }

                let pdf_val = (self.pdf_xfxq)(self.pid, self.x / xhat, self.q);
                let term_val = pdf_val / xhat;

                val += self.coeff_func.r(xhat, self.nf) * term_val;

                val += self.coeff_func.s(xhat, self.nf) * (term_val - pdf_at_x);
                val
            },
            self.x, 
            1.0, 
            Some(quad_options) 
        );

        match integration_result {
            Ok(quad_res) => res += quad_res.value,
            Err(e) => eprintln!("Integration failed at pid: {}, x: {}, q: {}: {:?}", self.pid, self.x, self.q, e),
        }   

        res += self.coeff_func.l(self.x, self.nf) * pdf_at_x;
        res        
    }        
}


// pub struct Conv1DBin {
//     pub xmin: f64,
//     pub xmax: f64,
//     pub q: f64,
//     pub nf: f64,
//     pub coeff_func: Cf1D,
//     pub pid: i32,
//     pub pdf_xfxq: fn(i32, f64, f64) -> f64,
// }

// impl Conv1DBin {
//     pub fn new(
//         xmin: f64,
//         xmax: f64,
//         q: f64,
//         nf: f64,
//         coeff_func: Cf1D,
//         pid: i32,
//         pdf_xfxq: fn(i32, f64, f64) -> f64,
//     ) -> Self {
//         Self {
//             xmin,
//             xmax,
//             q,
//             nf,
//             coeff_func,
//             pid,
//             pdf_xfxq,
//         }
//     }

//     pub fn compute(&self) -> f64 {
//         let mut res = 0.0;

//         let outer_options = QuadOptions {
//             abs_tol: 1e-11,
//             rel_tol: 1e-6,
//             max_evals: 100_000,
//             use_abs_error: false,
//             use_simpson: false,
//         };

//         let integration_result = quad(
//             |x: f64| -> f64 {
//                 if x <= 0.0 || x >= 1.0 {
//                     return 0.0;
//                 }

//                 let point = Conv1DPoint::new(
//                     x,
//                     self.q,
//                     self.nf,
//                     self.coeff_func,
//                     self.pid,
//                     self.pdf_xfxq,
//                 );

//                 point.compute()
//             },
//             self.xmin,
//             self.xmax,
//             Some(outer_options),
//         );

//         match integration_result {
//             Ok(quad_res) => res += quad_res.value,
//             Err(e) => eprintln!(
//                 "Bin integration failed at pid: {}, xmin: {}, xmax: {}, q: {}: {:?}",
//                 self.pid, self.xmin, self.xmax, self.q, e
//             ),
//         }

//         res
//     }
// }

pub struct Conv1DPointGrid {
    pub x: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf1D,
    pub obs_def_func: fn(f64, f64) -> f64,
    pub itp_xgrid: Vec<f64>,
    pub mode_log: bool,
    pub basis_functions: BasisCache,
    pub interpolator_at_x: Vec<f64>,
    pub integration_regions: Option<Vec<(f64, f64)>>,
}

impl Conv1DPointGrid {
    pub fn new(x: f64, q: f64, nf: f64, coeff_func: Cf1D, obs_def_func: fn(f64, f64) -> f64, itp_xgrid: Vec<f64>, mode_log: bool) -> Self {
        let basis_functions = compute_basis_functions(itp_xgrid.clone(), 4, mode_log);
        let interpolator_at_x = interpolator(x, &basis_functions);
        let regions = integration_regions(x, &itp_xgrid);

        Self {
            x,
            q,
            nf,
            coeff_func,
            obs_def_func,
            itp_xgrid,
            mode_log,
            basis_functions,
            interpolator_at_x,
            integration_regions: regions,
        }
    }

    pub fn compute(&self) -> Vec<f64> {
        // let has_r = self.coeff_func.r.is_some();
        // let has_s = self.coeff_func.s.is_some();
        // let has_l = self.coeff_func.l.is_some();
        (0..self.itp_xgrid.len()).into_par_iter().map(|xnode| {
            let mut res: f64 = 0.0;
            
            let pieces = &self.basis_functions.functions[xnode];
            let max_xmax_raw = pieces.last().unwrap().xmax;
            let max_xmax = if self.mode_log { max_xmax_raw.exp() } else { max_xmax_raw };

            if self.x >= (1.0 - EPS_INTEGRATION_BORDER) || max_xmax <= self.x {
                return 0.0;
            }

            if let Some(ref regions) = self.integration_regions {
                for i in regions {
                    let a = i.0 * (1.0 + EPS_INTEGRATION_BORDER);
                    let b = i.1 * (1.0 - EPS_INTEGRATION_BORDER);
                    
                    if b <= a { continue; }

                    let quad_options = QuadOptions {
                        abs_tol: 1e-10,
                        rel_tol: 1e-6,
                        max_evals: 1_000_000, 
                        use_abs_error: false,
                        use_simpson: false,
                    };

                    let integration_result = quad(
                        |xhat: f64| -> f64{
                            if xhat <= 0.0 || xhat >= 1.0 { return 0.0; }

                            let interp_val = point_interpolator(self.x / xhat, &self.basis_functions, xnode);
                            let term_val = interp_val / xhat;
                            
                            let mut val: f64= 0.0;
                            val += self.coeff_func.r(xhat, self.nf) * term_val;
                            val += self.coeff_func.s(xhat, self.nf) * (term_val - self.interpolator_at_x[xnode]);
                            val *= (self.obs_def_func)(self.x, self.q);
                            val
                        }, 
                        a, 
                        b, 
                        Some(quad_options) 
                    );
                    match integration_result {
                        Ok(quad_res) => res += quad_res.value,
                        Err(e) => {                            
                            eprintln!("Warning: Integration failed at xnode {} in region {:?}: {:?}", xnode, i, e);
                        }
                    }
                }
            }
            res += self.coeff_func.l(self.x, self.nf) * self.interpolator_at_x[xnode];
            res
        }).collect()        
    }
}
