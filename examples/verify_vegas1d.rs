use vhf::dis::CoeffFuncs as Cf1D;
use vhf::core::conv1dvegas::{Conv1DPointVegas, Conv1DBinVegas};

// --- Constants ---
const CF: f64 = 4.0 / 3.0;
const Z2: f64 = 1.644934066;

// pub type DISFunc = fn(f64, f64) -> f64;

// #[derive(Clone, Copy)]
// struct CoeffFuncs {
//     r_fn: DISFunc,
//     s_fn: DISFunc,
//     l_fn: DISFunc,
// }

// impl CoeffFuncs {
//     fn r(&self, x: f64, nf: f64) -> f64 {
//         (self.r_fn)(x, nf)
//     }
//     fn s(&self, x: f64, nf: f64) -> f64 {
//         (self.s_fn)(x, nf)
//     }
//     fn l(&self, x: f64, nf: f64) -> f64 {
//         (self.l_fn)(x, nf)
//     }
// }
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

// --- PDF Function (fxq) ---

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
    // --- Input parameters ---
    let central_x = 0.2;
    let x_min = 0.001;
    let x_max = 0.2;

    let q = 10.0;
    let nf = 5.0;
    let pid = 1;

    // --- Coefficient functions ---
    let coeffs = Cf1D {
        r_fn: r_00,
        s_fn: s_00,
        l_fn: l_00,
    };

    // =========================
    // Point computation
    // =========================
    let point = Conv1DPointVegas::new(
        central_x,
        q,
        nf,
        coeffs,
        pid,
        fxq,
    );

    let point_res = point.compute_full();

    // =========================
    // Bin computation
    // =========================
    let bin = Conv1DBinVegas::new(
        x_min,
        x_max,
        q,
        nf,
        coeffs,
        pid,
        fxq,
    );

    let bin_res = bin.compute_full();

    // =========================
    // Output
    // =========================
    println!("--- VEGAS+ Results ---\n");

    println!("Point (x = {}):", central_x);
    println!("  value     = {:.8e}", point_res.value);
    println!("  error     = {:.3e}", point_res.error);
    println!("  chi2/dof  = {:.3}\n", point_res.chi2_dof);

    println!("Bin (x_min = {}, x_max = {}):", x_min, x_max);
    println!("  value     = {:.8e}", bin_res.value);
    println!("  error     = {:.3e}", bin_res.error);
    println!("  chi2/dof  = {:.3}", bin_res.chi2_dof);
}