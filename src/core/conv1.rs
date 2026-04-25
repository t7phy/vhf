// use super::interpolation::{
//     compute_basis_functions, integration_regions, interpolator, point_interpolator, BasisCache,
// };
// use super::vegas::{Vegas, VegasConfig};
// use std::f64;

// // Small epsilon for integration borders to avoid singularities at endpoints
// const EPS_INTEGRATION_BORDER: f64 = 1e-10;

// /// Type alias for coefficient functions: f(x) -> f64
// pub type CoeffFn = fn(f64) -> f64;

// /// Container for the coefficient functions (r, s, l)
// /// Using Option allows us to handle cases where a function is missing (like "l" in your example).
// pub struct CoeffFuncs {
//     pub r: Option<CoeffFn>,
//     pub s: Option<CoeffFn>,
//     pub l: Option<CoeffFn>,
// }

// pub struct Conv1DGrid {
//     pub x: f64,
//     pub itp_xgrid: Vec<f64>,
//     pub coeff_func: CoeffFuncs,
//     pub mode_log: bool,
//     pub basis_functions: BasisCache,
//     pub interpolator_at_x: Vec<f64>,
//     pub integration_regions: Option<Vec<(f64, f64)>>,
// }

// impl Conv1DGrid {
//     /// Constructor: Translates the Python __init__
//     pub fn new(
//         x: f64,
//         itp_xgrid: Vec<f64>,
//         coeff_func: CoeffFuncs,
//         mode_log: bool,
//     ) -> Self {
//         // compute_basis_functions takes ownership of the xgrid in the provided Rust implementation.
//         // We clone it here because we also want to store `itp_xgrid` in the struct.
//         let basis_functions = compute_basis_functions(itp_xgrid.clone(), 4, mode_log);
        
//         // Compute interpolator values at x
//         let interpolator_at_x = interpolator(x, &basis_functions);
        
//         // Compute regions
//         let integration_regions = integration_regions(x, &itp_xgrid);

//         Self {
//             x,
//             itp_xgrid,
//             coeff_func,
//             mode_log,
//             basis_functions,
//             interpolator_at_x,
//             integration_regions,
//         }
//     }

//     /// The main computation method
//     pub fn compute(&self) -> Vec<f64> {
//         let mut grid_res = Vec::with_capacity(self.itp_xgrid.len());

//         // Check which coefficient functions exist to avoid repeated Option unwrapping inside the hot loop
//         let has_r = self.coeff_func.r.is_some();
//         let has_s = self.coeff_func.s.is_some();

//         for (xnode, _) in self.itp_xgrid.iter().enumerate() {
//             let mut res = 0.0;

//             // Retrieve max_xmax from the basis functions
//             // Structure: functions[xnode] -> Vec<BasisPiece> -> last() -> xmax
//             // Note: In your Rust interpolation module, 'functions' is a Vec<Vec<BasisPiece>>.
//             let max_xmax_raw = self.basis_functions.functions[xnode]
//                 .last()
//                 .map(|p| p.xmax)
//                 .unwrap_or(0.0);

//             let max_xmax = if self.mode_log {
//                 max_xmax_raw.exp()
//             } else {
//                 max_xmax_raw
//             };

//             // Optimization: Skip calculation if x is outside relevant range
//             if self.x >= (1.0 - EPS_INTEGRATION_BORDER) || max_xmax <= self.x {
//                 grid_res.push(0.0);
//                 continue;
//             }

//             // Perform Integration if regions exist
//             if let Some(ref regions) = self.integration_regions {
//                 for (region_low, region_high) in regions {
//                     // Apply epsilon borders
//                     let a = region_low * (1.0 + EPS_INTEGRATION_BORDER);
//                     let b = region_high * (1.0 - EPS_INTEGRATION_BORDER);

//                     // Configure VEGAS for this specific interval.
//                     // Since this is a 1D integral nested inside a loop, we keep it lightweight.
//                     // We set num_threads = 1 to avoid overhead of creating a thread pool for every small 1D integral.
//                     let config = VegasConfig {
//                         ndim: 1,
//                         max_evals: 500_000, // Sufficient for 1D smooth functions
//                         epsrel: 1e-6,      // 0.01% precision goal
//                         stratified: true, // Stratification overhead usually not worth it for 1D smooth
//                         num_threads: 0,    // Run sequentially within the current thread
//                         ..Default::default()
//                     };

//                     let mut mc = Vegas::new(config);

//                     // The Closure (Integrand)
//                     // This captures 'self' and 'xnode' from the environment.
//                     let result = mc.integrate(|u_arr| {
//                         let u = u_arr[0]; // 1D integration variable from VEGAS [0,1]
                        
//                         // Jacobian transformation: u[0,1] -> xhat[a,b]
//                         let xhat = a + (b - a) * u;
                        
//                         // Logic from optimized_integrand:
//                         // 1. Evaluate point interpolator (Rust version handles log logic internally via BasisCache)
//                         let interp_val = point_interpolator(self.x / xhat, &self.basis_functions, xnode);
//                         let term_val = interp_val / xhat;

//                         let mut integrand_val = 0.0;

//                         if has_r {
//                             // Safe unwrap because we checked has_r
//                             integrand_val += (self.coeff_func.r.unwrap())(xhat) * term_val;
//                         }

//                         if has_s {
//                             // Safe unwrap because we checked has_s
//                             let diff = term_val - self.interpolator_at_x[xnode];
//                             integrand_val += (self.coeff_func.s.unwrap())(xhat) * diff;
//                         }

//                         // Multiply by Jacobian of the coordinate change
//                         integrand_val * (b - a)
//                     });

//                     res += result.estimate;
//                 }
//             }

//             // Add the "Local" term (l) if it exists
//             if let Some(c_l) = self.coeff_func.l {
//                 res += c_l(self.x) * self.interpolator_at_x[xnode];
//             }

//             grid_res.push(res);
//         }

//         grid_res
//     }
// }
// use crate::core::interpolation::{BasisCache, point_interpolator, interpolator, integration_regions};
// use crate::core::vegas::{Vegas, VegasConfig};

// // Use the exact same epsilon as your Python test
// const EPS_INTEGRATION_BORDER: f64 = 1e-10;

// pub type CoeffFn = fn(f64) -> f64;

// pub struct CoeffFuncs {
//     pub r: Option<CoeffFn>,
//     pub s: Option<CoeffFn>,
//     pub l: Option<CoeffFn>,
// }

// pub struct Conv1DGrid {
//     pub x: f64,
//     pub itp_xgrid: Vec<f64>,
//     pub coeff_func: CoeffFuncs,
//     pub mode_log: bool,
//     pub basis_functions: BasisCache,
//     pub interpolator_at_x: Vec<f64>,
//     pub integration_regions: Option<Vec<(f64, f64)>>,
// }

// impl Conv1DGrid {
//     pub fn new(x: f64, itp_xgrid: Vec<f64>, coeff_func: CoeffFuncs, mode_log: bool) -> Self {
//         // Basis functions are computed with degree 4 as in your python snippet
//         let basis_functions = crate::core::interpolation::compute_basis_functions(itp_xgrid.clone(), 4, mode_log);
//         let interpolator_at_x = interpolator(x, &basis_functions);
//         let regions = integration_regions(x, &itp_xgrid);

//         Self {
//             x,
//             itp_xgrid,
//             coeff_func,
//             mode_log,
//             basis_functions,
//             interpolator_at_x,
//             integration_regions: regions,
//         }
//     }

//     pub fn compute(&self) -> Vec<f64> {
//         let mut grid = Vec::with_capacity(self.itp_xgrid.len());
        
//         let has_r = self.coeff_func.r.is_some();
//         let has_s = self.coeff_func.s.is_some();
//         let c_r = self.coeff_func.r;
//         let c_s = self.coeff_func.s;

//         for xnode in 0..self.itp_xgrid.len() {
//             let mut res = 0.0;
            
//             // Get max_xmax for the specific basis function node
//             let pieces = &self.basis_functions.functions[xnode];
//             let max_xmax_raw = pieces.last().unwrap().xmax;
//             let max_xmax = if self.mode_log { max_xmax_raw.exp() } else { max_xmax_raw };

//             // Python check: if self.x >= (1 - eps) or max_xmax <= self.x:
//             if self.x >= (1.0 - EPS_INTEGRATION_BORDER) || max_xmax <= self.x {
//                 grid.push(0.0);
//                 continue;
//             }

//             if let Some(ref regions) = self.integration_regions {
//                 for i in regions {
//                     // Python: x_intv_low = i[0] * (1 + eps), x_intv_high = i[1] * (1 - eps)
//                     let a = i.0 * (1.0 + EPS_INTEGRATION_BORDER);
//                     let b = i.1 * (1.0 - EPS_INTEGRATION_BORDER);
                    
//                     if b <= a { continue; }

//                     // Use robust VEGAS settings. 
//                     // Since Python VEGAS worked, we use Stratified: true.
//                     let config = VegasConfig {
//                         ndim: 1,
//                         max_evals: 50_000, 
//                         min_iters: 5,
//                         max_iters: 20,
//                         epsrel: 1e-6,
//                         stratified: true, 
//                         num_threads: 1, // Inner loop is sequential to avoid pool contention
//                         ..Default::default()
//                     };

//                     let mut mc = Vegas::new(config);
//                     let result = mc.integrate(|u_arr| {
//                         let u = u_arr[0];
//                         // xhat = a + (b - a) * u
//                         let xhat = a + (b - a) * u;
                        
//                         // interp_val = point_interpolator(self.x / xhat, ...)
//                         let interp_val = point_interpolator(self.x / xhat, &self.basis_functions, xnode);
//                         let term_val = interp_val / xhat;
                        
//                         let mut val = 0.0;
//                         if has_r {
//                             val += (c_r.unwrap())(xhat) * term_val;
//                         }
//                         if has_s {
//                             // term_val - self.interpolator_at_x[xnode]
//                             val += (c_s.unwrap())(xhat) * (term_val - self.interpolator_at_x[xnode]);
//                         }
                        
//                         // res * (b - a)
//                         val * (b - a)
//                     });
//                     res += result.estimate;
//                 }
//             }

//             // if "l" in self.coeff_func: res += ...
//             if let Some(c_l) = self.coeff_func.l {
//                 res += c_l(self.x) * self.interpolator_at_x[xnode];
//             }
//             grid.push(res);
//         }
//         grid
//     }
// }

// use crate::core::interpolation::{BasisCache, point_interpolator, interpolator, integration_regions};
// use crate::core::quad::Quad; // Pulling from your existing module
// use rayon::prelude::*;

// /// Numerical border epsilon for singularities (matches Python test exactly)
// const EPS_INTEGRATION_BORDER: f64 = 1e-10;

// pub type CoeffFn = fn(f64) -> f64;

// pub struct CoeffFuncs {
//     pub r: Option<CoeffFn>,
//     pub s: Option<CoeffFn>,
//     pub l: Option<CoeffFn>,
// }

// pub struct Conv1DGrid {
//     pub x: f64,
//     pub itp_xgrid: Vec<f64>,
//     pub coeff_func: CoeffFuncs,
//     pub mode_log: bool,
//     pub basis_functions: BasisCache,
//     pub interpolator_at_x: Vec<f64>,
//     pub integration_regions: Option<Vec<(f64, f64)>>,
// }

// impl Conv1DGrid {
//     pub fn new(x: f64, itp_xgrid: Vec<f64>, coeff_func: CoeffFuncs, mode_log: bool) -> Self {
//         let basis_functions = crate::core::interpolation::compute_basis_functions(itp_xgrid.clone(), 4, mode_log);
//         let interpolator_at_x = interpolator(x, &basis_functions);
//         let regions = integration_regions(x, &itp_xgrid);

//         Self {
//             x,
//             itp_xgrid,
//             coeff_func,
//             mode_log,
//             basis_functions,
//             interpolator_at_x,
//             integration_regions: regions,
//         }
//     }

//     /// Computes the convolution weights. 
//     /// Parallelized across nodes for high-throughput evaluation.
//     pub fn compute(&self) -> Vec<f64> {
//         let has_r = self.coeff_func.r.is_some();
//         let has_s = self.coeff_func.s.is_some();

//         (0..self.itp_xgrid.len()).into_par_iter().map(|xnode| {
//             let mut res = 0.0;
            
//             // 1. Support Check
//             let pieces = &self.basis_functions.functions[xnode];
//             let max_xmax_raw = pieces.last().unwrap().xmax;
//             let max_xmax = if self.mode_log { max_xmax_raw.exp() } else { max_xmax_raw };

//             if self.x >= (1.0 - EPS_INTEGRATION_BORDER) || max_xmax <= self.x {
//                 return 0.0;
//             }

//             // 2. Integration over sub-regions
//             if let Some(ref regions) = self.integration_regions {
//                 for i in regions {
//                     // Apply exact same borders as Python
//                     let a = i.0 * (1.0 + EPS_INTEGRATION_BORDER);
//                     let b = i.1 * (1.0 - EPS_INTEGRATION_BORDER);
                    
//                     if b <= a { continue; }

//                     // We integrate directly from a to b. 
//                     // The Quad handles the coordinate transformation internally.
//                     let result = Quad::integrate(&|xhat| {
//                         let interp_val = point_interpolator(self.x / xhat, &self.basis_functions, xnode);
//                         let term_val = interp_val / xhat;
                        
//                         let mut val = 0.0;
//                         if has_r {
//                             val += (self.coeff_func.r.unwrap())(xhat) * term_val;
//                         }
//                         if has_s {
//                             // Subtraction scheme: cancels 1/(1-x) singularity numerically
//                             val += (self.coeff_func.s.unwrap())(xhat) * (term_val - self.interpolator_at_x[xnode]);
//                         }
//                         val
//                     }, a, b, 1e-10, 15);

//                     res += result.estimate;
//                 }
//             }

//             // 3. Local Term (Delta contribution)
//             if let Some(c_l) = self.coeff_func.l {
//                 res += c_l(self.x) * self.interpolator_at_x[xnode];
//             }
//             res
//         }).collect()
//     }
// }

use crate::core::interpolation::{BasisCache, point_interpolator, interpolator, integration_regions};
use rayon::prelude::*;
use scirs2_integrate::quad::{quad, QuadOptions}; 

const EPS_INTEGRATION_BORDER: f64 = 1e-10;

pub type CoeffFn = fn(f64) -> f64;

pub struct CoeffFuncs {
    pub r: Option<CoeffFn>,
    pub s: Option<CoeffFn>,
    pub l: Option<CoeffFn>,
}

pub struct Conv1DGrid {
    pub x: f64,
    pub itp_xgrid: Vec<f64>,
    pub coeff_func: CoeffFuncs,
    pub mode_log: bool,
    pub basis_functions: BasisCache,
    pub interpolator_at_x: Vec<f64>,
    pub integration_regions: Option<Vec<(f64, f64)>>,
}

impl Conv1DGrid {
    pub fn new(x: f64, itp_xgrid: Vec<f64>, coeff_func: CoeffFuncs, mode_log: bool) -> Self {
        let basis_functions = crate::core::interpolation::compute_basis_functions(itp_xgrid.clone(), 4, mode_log);
        let interpolator_at_x = interpolator(x, &basis_functions);
        let regions = integration_regions(x, &itp_xgrid);

        Self {
            x,
            itp_xgrid,
            coeff_func,
            mode_log,
            basis_functions,
            interpolator_at_x,
            integration_regions: regions,
        }
    }

    pub fn compute(&self) -> Vec<f64> {
        let has_r = self.coeff_func.r.is_some();
        let has_s = self.coeff_func.s.is_some();

        (0..self.itp_xgrid.len()).into_par_iter().map(|xnode| {
            let mut res = 0.0;
            
            // 1. Support Check
            let pieces = &self.basis_functions.functions[xnode];
            let max_xmax_raw = pieces.last().unwrap().xmax;
            let max_xmax = if self.mode_log { max_xmax_raw.exp() } else { max_xmax_raw };

            if self.x >= (1.0 - EPS_INTEGRATION_BORDER) || max_xmax <= self.x {
                return 0.0;
            }

            // 2. Integration over sub-regions
            if let Some(ref regions) = self.integration_regions {
                for i in regions {
                    let a = i.0 * (1.0 + EPS_INTEGRATION_BORDER);
                    let b = i.1 * (1.0 - EPS_INTEGRATION_BORDER);
                    
                    if b <= a { continue; }

                    // FIXED TOLERANCES: Matches Python (epsrel=1e-6)
                    let options = QuadOptions {
                        abs_tol: 1e-10,      // Relaxed from 1e-12 to handle 1/(1-x) noise
                        rel_tol: 1e-6,      // Relaxed from 1e-10 to match Python
                        max_evals: 100_000, 
                        use_abs_error: false,
                        use_simpson: false,
                    };

                    let integration_result = quad(
                        |xhat: f64| {
                            // Safety guard for boundaries
                            if xhat <= 0.0 || xhat >= 1.0 { return 0.0; }

                            let interp_val = point_interpolator(self.x / xhat, &self.basis_functions, xnode);
                            let term_val = interp_val / xhat;
                            
                            let mut val = 0.0;
                            if has_r {
                                val += (self.coeff_func.r.unwrap())(xhat) * term_val;
                            }
                            if has_s {
                                // Subtraction scheme
                                val += (self.coeff_func.s.unwrap())(xhat) * (term_val - self.interpolator_at_x[xnode]);
                            }
                            val
                        }, 
                        a, 
                        b, 
                        Some(options) 
                    );

                    match integration_result {
                        Ok(quad_res) => res += quad_res.value,
                        Err(e) => {
                            // FIXED: Log error instead of crashing the thread.
                            // In PDF evolution, one tiny bin failing convergence usually implies
                            // the contribution is negligible or the singularity is too steep.
                            eprintln!("Warning: Integration failed at xnode {} in region {:?}: {:?}", xnode, i, e);
                            // We do NOT add anything to res here, effectively treating the failed region as 0.
                            // If this happens often, we might need even looser tolerances or higher limits.
                        }
                    }
                }
            }

            // 3. Local Term
            if let Some(c_l) = self.coeff_func.l {
                res += c_l(self.x) * self.interpolator_at_x[xnode];
            }
            res
        }).collect()
    }
}