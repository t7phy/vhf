use std::collections::HashMap;
use serde::Serialize;

#[derive(Debug, Clone, Serialize)]
pub struct BasisPiece {
    pub xmin: f64,
    pub xmax: f64,
    pub coeffs: Vec<f64>,
}

/// Solves the inverse relation y = 5(1-x) - ln(x) for x using Newton-Raphson.
fn inverse_relation_solver(y: f64) -> f64 {
    let mut yp = y;
    let mut deltap = f64::INFINITY;

    // Newton-Raphson iteration
    for _ in 0..10 {
        let x = (-yp).exp();
        // delta = f(yp) = 5(1 - e^-yp) - (y - yp)
        let delta = (1.0 - x).mul_add(-5.0, y - yp);
        
        // Check for convergence or precision limit
        if delta == 0.0 || (delta.abs() < 2e-15 && delta.abs() >= deltap.abs()) {
            return x;
        }
        
        // derivative of f(yp)
        let deriv = x.mul_add(-5.0, -1.0);
        yp -= delta / deriv;
        deltap = delta;
    }
    (-yp).exp()
}

pub fn lambertgrid(n_pts: usize, x_min: f64, x_max: f64) -> Vec<f64> {
    let direct_relation = |x: f64| 5.0 * (1.0 - x) - x.ln();

    let y_min = direct_relation(x_min);
    let y_max = direct_relation(x_max);

    let mut grid = Vec::with_capacity(n_pts);
    for i in 0..n_pts {
        // Linear spacing in y-space
        let y = y_min + (y_max - y_min) * (i as f64) / ((n_pts - 1) as f64);
        grid.push(inverse_relation_solver(y));
    }
    grid
}

// ... Keep area_block_map, basis_function, compute_basis_functions, 
// ... interpolator, point_interpolator, and integration_regions as previously defined.

pub fn area_block_map(xgrid: &[f64], poly_deg: usize) -> Vec<(usize, usize)> {
    let num_x = xgrid.len();
    let num_areas = num_x - 1;
    let mut blocks_index = Vec::new();
    
    let po2 = if poly_deg % 2 == 0 {
        poly_deg / 2 - 1
    } else {
        poly_deg / 2
    };

    for i in 0..num_areas {
        let mut kmin = if i > po2 { i - po2 } else { 0 };
        let mut kmax = kmin + poly_deg;
        
        if kmax >= num_x {
            kmax = num_areas;
            kmin = kmax - poly_deg;
        }
        blocks_index.push((kmin, kmax));
    }
    blocks_index
}

pub fn basis_function(
    poly_index: usize,
    xgrid: &[f64],
    blocks_index: &[(usize, usize)],
    mut basis_functions: HashMap<String, Vec<BasisPiece>>,
) -> HashMap<String, Vec<BasisPiece>> {
    let mut bflist = Vec::new();

    for (i, &(kmin, kmax)) in blocks_index.iter().enumerate() {
        if poly_index >= kmin && poly_index <= kmax {
            let xmin = xgrid[i];
            let xmax = xgrid[i + 1];
            
            let mut ref_indices = Vec::new();
            for j in kmin..=kmax {
                if j != poly_index {
                    ref_indices.push(j);
                }
            }

            let xj = xgrid[poly_index];
            let mut denominator = 1.0;
            for &j in &ref_indices {
                denominator *= xj - xgrid[j];
            }

            let mut coeffs = vec![1.0];
            for (s, &k) in ref_indices.iter().enumerate() {
                let xk = xgrid[k];
                
                // Mxk_coeffs = -xk * coeffs
                let mxk_coeffs: Vec<f64> = coeffs.iter().map(|&c| -xk * c).collect();
                
                // coeffs = np.concatenate(([0.0], coeffs))
                let mut next_coeffs = vec![0.0];
                next_coeffs.extend(&coeffs);
                
                // coeffs[:s+1] += Mxk_coeffs
                for idx in 0..=s {
                    next_coeffs[idx] += mxk_coeffs[idx];
                }
                coeffs = next_coeffs;
            }

            let final_coeffs: Vec<f64> = coeffs.into_iter().map(|c| c / denominator).collect();
            bflist.push(BasisPiece { xmin, xmax, coeffs: final_coeffs });
        }
    }
    basis_functions.insert(format!("p_{}", poly_index), bflist);
    basis_functions
}

pub fn compute_basis_functions(xgrid: Vec<f64>, poly_deg: usize, mode_log: bool) -> HashMap<String, Vec<BasisPiece>> {
    let xgrid_transformed = if mode_log {
        xgrid.into_iter().map(|x| x.ln()).collect()
    } else {
        xgrid
    };

    let num_x = xgrid_transformed.len();
    let blocks_index = area_block_map(&xgrid_transformed, poly_deg);
    let mut basis_functions = HashMap::new();

    for i in 0..num_x {
        basis_functions = basis_function(i, &xgrid_transformed, &blocks_index, basis_functions);
    }
    basis_functions
}

pub fn interpolator(ev_point: f64, basis_functions: &HashMap<String, Vec<BasisPiece>>, mode_log: bool) -> Vec<f64> {
    let ev = if mode_log { ev_point.ln() } else { ev_point };
    let mut res_list = Vec::new();
    let num_basis = basis_functions.len();

    for i in 0..num_basis {
        let mut res = 0.0;
        if let Some(pieces) = basis_functions.get(&format!("p_{}", i)) {
            for piece in pieces {
                if ev > piece.xmin && ev <= piece.xmax {
                    for (k, &l) in piece.coeffs.iter().enumerate() {
                        res += l * ev.powi(k as i32);
                    }
                }
            }
        }
        res_list.push(res);
    }
    res_list
}

pub fn point_interpolator(ev_point: f64, basis_functions: &HashMap<String, Vec<BasisPiece>>, i: usize, mode_log: bool) -> f64 {
    let ev = if mode_log { ev_point.ln() } else { ev_point };
    let mut res = 0.0;
    
    if let Some(pieces) = basis_functions.get(&format!("p_{}", i)) {
        for piece in pieces {
            if ev > piece.xmin && ev <= piece.xmax {
                for (k, &l) in piece.coeffs.iter().enumerate() {
                    res += l * ev.powi(k as i32);
                }
            }
        }
    }
    res
}

pub fn integration_regions(x: f64, itp_xgrid: &[f64]) -> Option<Vec<(f64, f64)>> {
    if x <= itp_xgrid[0] || x >= *itp_xgrid.last().unwrap() {
        return None;
    }

    // np.searchsorted(side='right')
    let pos = match itp_xgrid.binary_search_by(|prob| {
        if *prob <= x { std::cmp::Ordering::Less } else { std::cmp::Ordering::Greater }
    }) {
        Ok(idx) => idx,
        Err(idx) => idx,
    };

    let mut region_borders = vec![x];
    region_borders.extend_from_slice(&itp_xgrid[pos..]);

    let mut regions = Vec::new();
    for i in 0..(region_borders.len() - 1) {
        regions.push((region_borders[i], region_borders[i + 1]));
    }
    Some(regions)
}