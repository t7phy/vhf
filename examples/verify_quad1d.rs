use vhf::dis::CoeffFuncs as Cf1D;
use vhf::core::conv1dquad::{Conv1DPointQuad, Conv1DBinQuad, Conv1DPointGrid};
use vhf::core::interpolation::lambertgrid;


// --- Constants ---
const CF: f64 = 4.0 / 3.0;
const Z2: f64 = 1.644934066;

// --- Coefficient Functions ---

fn r_00(x: f64, _nf: f64) -> f64 {
    let term1 = -2.0 * (1.0 + x) * ((1.0 - x) / x).ln();
    let term2 = -4.0 * x.ln() / (1.0 - x);
    CF * (term1 + term2 + 6.0 + 4.0 * x)
}

fn s_00(x: f64, _nf: f64) -> f64 {
    (-3.0 * CF) / (1.0 - x) + (4.0 * CF) * (1.0 - x).ln() / (1.0 - x)
}

fn l_00(x: f64, _nf: f64) -> f64 {
    let ln_1_x = (1.0 - x).ln();
    let term1 = -CF * (9.0 + 4.0 * Z2);
    let term2 = -3.0 * CF * ln_1_x;
    let term3 = 4.0 * CF * ln_1_x.powi(2) / 2.0;
    term1 + term2 + term3
}

// --- Toy PDF as f(x,Q), not x*f(x,Q) ---

fn fxq(pid: i32, x: f64, _q: f64) -> f64 {
    xfx_q2(pid, x) / x
}

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

fn main() {
    let central_x = 0.2;
    let x_min = 0.199;
    let x_max = 0.201;

    let q = 10.0;
    let nf = 5.0;
    let pid = 1;
    let epsrel = 1e-8;

    let coeffs = Cf1D {
        r_fn: r_00,
        s_fn: s_00,
        l_fn: l_00,
    };

    fn obs_def_func(_x: f64, _q: f64) -> f64 {
        1.0
    }

    let point = Conv1DPointQuad::new(central_x, q, nf, coeffs, pid, fxq, epsrel);
    let bin = Conv1DBinQuad::new(x_min, x_max, q, nf, coeffs, pid, fxq, epsrel);

    let (point_val, point_err) = point.compute_full();
    let (bin_val, bin_err) = bin.compute_full();

    let xgrid_itp = lambertgrid(200, 1e-5, 1.0);
    let mode_log = true; // change if your interpolation setup expects true

    let point_grid = Conv1DPointGrid::new(
        central_x,
        q,
        nf,
        coeffs,
        // obs_def_func,
        xgrid_itp.clone(),
        mode_log,
    );

    let subgrid = point_grid.compute();

    let pdf_on_grid: Vec<f64> = xgrid_itp
        .iter()
        .map(|&x| fxq(pid, x, q))
        .collect();

    let subgrid_result: f64 = subgrid
        .iter()
        .zip(pdf_on_grid.iter())
        .map(|(w, f)| w * f)
        .sum();

    println!("--- Custom quad/nquad Results ---\n");

    println!("Point (x = {}):", central_x);
    println!("  value = {:.12e}", point_val);
    println!("  error = {:.6e}\n", point_err);

    println!("Bin (x_min = {}, x_max = {}):", x_min, x_max);
    println!("  value = {:.12e}", bin_val/0.002);
    println!("  error = {:.6e}", bin_err);

    println!("\n--- Subgrid result ---");
    println!("Point (x = {}):", central_x);
    println!("  value = {:.12e}", subgrid_result);
}