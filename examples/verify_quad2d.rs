use vhf::sidis::CoeffFuncs as Cf2D;
use vhf::core::conv2dquad::{Conv2DPointQuad, Conv2DBinQuad, Conv2DPointGrid};
use vhf::core::interpolation::lambertgrid;

use vhf::sidis::fl::FLC2q2qM::cf;

// --- Toy PDF as f(x,Q), not x*f(x,Q) ---

fn fxq_pdf(pid: i32, x: f64, _q: f64) -> f64 {
    xfx_q2_pdf(pid, x) / x
}

fn xfx_q2_pdf(pid: i32, x: f64) -> f64 {
    match pid {
        3 | -3 => 0.2 * (xfx_q2_pdf(-1, x) + xfx_q2_pdf(-2, x)),
        -2 => xfx_q2_pdf(-1, x) * (1.0 - x),
        -1 => 0.1939875 * x.powf(-0.1) * (1.0 - x).powi(6),
        0 | 21 => 1.7 * x.powf(-0.1) * (1.0 - x).powi(5),
        1 => 3.064320 * x.powf(0.8) * (1.0 - x).powi(4) + xfx_q2_pdf(-1, x),
        2 => 5.107200 * x.powf(0.8) * (1.0 - x).powi(3) + xfx_q2_pdf(-2, x),
        _ => panic!("PDF PID {} not implemented", pid),
    }
}

// --- Toy FF as D(z,Q), not z*D(z,Q) ---
// Based on 1501.00494, Eqs. 3.3 and 3.4

fn fxq_ff(pid: i32, z: f64, _q: f64) -> f64 {
    xfx_q2_ff(pid, z) / z
}

fn xfx_q2_ff(pid: i32, z: f64) -> f64 {
    let n_v = 1.00881;
    let n_s = 17.6255;
    let n_g = 438.189;

    let xd_u = z * n_v * z.powf(-0.963) * (1.0 - z).powf(1.370);
    let xd_ub = z * n_s * z.powf(0.718) * (1.0 - z).powf(6.266);
    let xd_g = z * n_g * z.powf(1.943) * (1.0 - z).powi(8);

    match pid {
        -3 => xd_ub,
        -2 => xd_ub,
        -1 => xd_u,
        0 | 21 => xd_g,
        1 => xd_ub,
        2 => xd_u,
        3 => xd_ub,
        _ => panic!("FF PID {} not implemented", pid),
    }
}

fn main() {
    let central_x = 0.2;
    let central_z = 0.35;

    let x_min = 0.199;
    let x_max = 0.201;

    let z_min = 0.349;
    let z_max = 0.351;

    let q = 10.0;
    let nf = 5.0;

    let pid_pdf = 1;
    let pid_ff = 2;

    let epsrel = 0.001;

    // Replace this with your actual imported SIDIS coefficient functions.
    let coeffs: Cf2D = cf();

    let point = Conv2DPointQuad::new(
        central_x,
        central_z,
        q,
        nf,
        coeffs.clone(),
        pid_pdf,
        pid_ff,
        fxq_pdf,
        fxq_ff,
        epsrel,
    );

    // let bin = Conv2DBinQuad::new(
    //     x_min,
    //     x_max,
    //     z_min,
    //     z_max,
    //     q,
    //     nf,
    //     coeffs.clone(),
    //     pid_pdf,
    //     pid_ff,
    //     fxq_pdf,
    //     fxq_ff,
    //     epsrel,
    // );

    let (point_val, point_err) = point.compute_full();
    // let (bin_val, bin_err) = bin.compute_full();

    let xgrid_itp = lambertgrid(10, 1e-5, 1.0);
    let zgrid_itp = lambertgrid(10, 1e-3, 1.0);

    let mode_log_x = true;
    let mode_log_z = true;

    let point_grid = Conv2DPointGrid::new(
        central_x,
        central_z,
        q,
        nf,
        coeffs,
        xgrid_itp.clone(),
        zgrid_itp.clone(),
        mode_log_x,
        mode_log_z,
    );

    let subgrid = point_grid.compute();

    let pdf_on_grid: Vec<f64> = xgrid_itp
        .iter()
        .map(|&x| fxq_pdf(pid_pdf, x, q))
        .collect();

    let ff_on_grid: Vec<f64> = zgrid_itp
        .iter()
        .map(|&z| fxq_ff(pid_ff, z, q))
        .collect();

    let subgrid_result: f64 = subgrid
        .iter()
        .enumerate()
        .map(|(a, row)| {
            row.iter()
                .enumerate()
                .map(|(b, w)| w * pdf_on_grid[a] * ff_on_grid[b])
                .sum::<f64>()
        })
        .sum();

    println!("--- Custom quad/nquad Results ---\n");

    println!("Explcit subgrid convolution result: {:.12e}\n", subgrid_result);

    println!("Point (x = {}, z = {}):", central_x, central_z);
    println!("  value = {:.12e}", point_val);
    println!("  error = {:.6e}\n", point_err);

    // println!(
    //     "Bin (x_min = {}, x_max = {}, z_min = {}, z_max = {}):",
    //     x_min, x_max, z_min, z_max
    // );
    // println!(
    //     "  value = {:.12e}",
    //     bin_val / ((x_max - x_min) * (z_max - z_min))
    // );
    // println!("  error = {:.6e}", bin_err);

    // println!("\n--- Subgrid result ---");
    // println!("Point (x = {}, z = {}):", central_x, central_z);
    // println!("  value = {:.12e}", subgrid_result);
    // println!("rr: {}", coeffs.rr(0.20001, 0.30001, 5.0));
    // println!("rs: {}", coeffs.rs(0.20001, 0.30001, 5.0));
    // println!("sr: {}", coeffs.sr(0.20001, 0.30001, 5.0));
    // println!("ss: {}", coeffs.ss(0.20001, 0.30001, 5.0));
    // println!("rl: {}", coeffs.rl(0.20001, 0.30001, 5.0));
    // println!("sl: {}", coeffs.sl(0.20001, 0.30001, 5.0));
    // println!("lr: {}", coeffs.lr(0.20001, 0.30001, 5.0));
    // println!("ls: {}", coeffs.ls(0.20001, 0.30001, 5.0));
    // println!("ll: {}", coeffs.ll(0.20001, 0.30001, 5.0));
}