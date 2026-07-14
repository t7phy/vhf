use vhf::core::conv1::{Conv1DGrid, CoeffFuncs};
use vhf::core::interpolation::lambertgrid;
use scirs2_integrate::quad::{quad, QuadOptions};

// --- Constants ---
const CF: f64 = 4.0 / 3.0;
const Z2: f64 = 1.644934066;

// --- Coefficient Functions ---

fn r_00(x: f64) -> f64 {
    // - 2. * (1. + x) * np.log((1. - x) / x) - 4. * np.log(x) / (1. - x) + 6. + 4. * x
    let term1 = -2.0 * (1.0 + x) * ((1.0 - x) / x).ln();
    let term2 = -4.0 * x.ln() / (1.0 - x);
    CF * (term1 + term2 + 6.0 + 4.0 * x)
}

fn s_00(x: f64) -> f64 {
    // (-3. * CF)/(1. - x) + (4. * CF) * np.log(1. - x) / (1. - x)
    (-3.0 * CF) / (1.0 - x) + (4.0 * CF) * (1.0 - x).ln() / (1.0 - x)
}

fn l_00(x: f64) -> f64 {
    // - CF * (9. + 4. * z2) + (-3. * CF) * np.log(1. - x) + (4. * CF) * pow(np.log(1. - x), 2)/2
    let ln_1_x = (1.0 - x).ln();
    let term1 = -CF * (9.0 + 4.0 * Z2);
    let term2 = -3.0 * CF * ln_1_x;
    let term3 = 4.0 * CF * ln_1_x.powi(2) / 2.0;
    term1 + term2 + term3
}

// --- PDF Function (Recursive) ---

fn xfx_q2(pid: i32, x: f64) -> f64 {
    match pid {
        3 | -3 => 0.2 * (xfx_q2(-1, x) + xfx_q2(-2, x)),
        -2 => xfx_q2(-1, x) * (1.0 - x),
        -1 => 0.1939875 * x.powf(-0.1) * (1.0 - x).powi(6),
        0 | 21 => 1.7 * x.powf(-0.1) * (1.0 - x).powi(5),
        1 => 3.064320 * x.powf(0.8) * (1.0 - x).powi(4) + xfx_q2(-1, x),
        2 => 5.107200 * x.powf(0.8) * (1.0 - x).powi(3) + xfx_q2(-2, x),
        _ => panic!("PID {} not implemented", pid),
    }
}

// --- Main Evaluation Logic ---

fn pointwise_hypercube_grid_eval(x: f64, pid: i32, xgrid: &[f64]) -> f64 {
    // 1. Setup Coefficients
    let coeffs = CoeffFuncs {
        r: Some(r_00),
        s: Some(s_00),
        l: Some(l_00),
    };

    // 2. Initialize the Convolution Grid
    // Note: This matches `conv_1d_grid(x, xgrid_itp, c2, mode_log=True)`
    // We clone xgrid because Conv1DGrid takes ownership to store it.
    let conv = Conv1DGrid::new(x, xgrid.to_vec(), coeffs, true);

    // 3. Compute the convolution weights (the "grid" in python)
    let grid_weights = conv.compute();

    // 4. Compute the PDF array: [fxQ2(x_val) for x_val in xgrid_itp]
    // Note: fxQ2(x) = xfxQ2(x) / x
    let pdf_arr: Vec<f64> = xgrid.iter()
        .map(|&x_val| xfx_q2(pid, x_val) / x_val)
        .collect();

    // 5. Dot Product
    // result = np.dot(grid, pdf_arr)
    let result: f64 = grid_weights.iter()
        .zip(pdf_arr.iter())
        .map(|(w, f)| w * f)
        .sum();

    result
}

fn main() {
    // 1. Generate Lambert Grid
    // Matches: lambertgrid(100, 1e-5, 1)
    let xgrid_itp = lambertgrid(100, 1e-5, 1.0);

    // 2. Define Test Points
    // You can change these to match the exact values you tested in Python
    let test_points = vec![0.02];
    let test_pids = vec![2]; // u-quark, d-quark, gluon

    println!("{:<10} {:<10} {:<25}", "PID", "x", "Result");
    println!("{:-<10} {:-<10} {:-<25}", "", "", "");

    for &pid in &test_pids {
        for &x in &test_points {
            let res = pointwise_hypercube_grid_eval(x, pid, &xgrid_itp);
            println!("{:<10} {:<10.4} {:.12e}", pid, x, res);
        }
        println!("{:-<45}", "");
    }
}

// fn fx_q2(pid: i32, x: f64) -> f64 {
//     xfx_q2(pid, x) / x
// }

// fn main() {
//     let x = 0.02;
//     let pid = 2; 

//     let fx_val = fx_q2(pid, x);

//     // Integrand Closure
//     // r_00(xhat) * f(x/xhat)/xhat + s_00(xhat) * (f(x/xhat)/xhat - f(x))
//     let integrand = |xhat: f64| {
//         // Prevent division by zero or log(0) at boundaries if integrator hits them exactly
//         if xhat <= 0.0 || xhat >= 1.0 { return 0.0; }

//         let f_div_xhat = fx_q2(pid, x / xhat) / xhat;
        
//         let term_r = r_00(xhat) * f_div_xhat;
//         let term_s = s_00(xhat) * (f_div_xhat - fx_val);
        
//         term_r + term_s
//     };

//     // Configuration
//     let options = QuadOptions {
//         abs_tol: 1e-12,     // Matches standard precision requirements
//         rel_tol: 1e-6,      // Matches Python epsrel
//         max_evals: 100_000, // INCREASED: Essential for singularities
//         use_abs_error: true,
//         use_simpson: false,
//     };

//     // Perform Integration [x, 1.0]
//     let result = quad(integrand, x, 1.0, Some(options));

//     match result {
//         Ok(quad_res) => {
//             let integral = quad_res.value;
//             let local_term = l_00(x) * fx_val;
//             let total = integral + local_term;

//             println!("Result (Rust): {:.16}", total);
//         }
//         Err(e) => {
//             eprintln!("Integration failed: {:?}", e);
//         }
//     }
// }