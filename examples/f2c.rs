use libome_rs::AQg;
use vhf::core::scits::quad::{quad, nquad, Bound};
use vhf::dis::f2_heavy::f2nc_nlo_gvv;
use vhf::dis::f2_light::f2nc_nlo_ns;
use neopdf::pdf::PDF;
use std::f64::consts::PI;

pub fn main() {

    let mc2 = 1.3 * 1.3;
    
    let toypdf = PDF::load("ToyPDF_NLO", 0);
    
    let conv_e = |x: f64, q2: f64| -> f64 {
        let mu2 = q2;// + mc2;
        let chi = x * (1.0 +  4.0 *mc2 / q2);
        toypdf.xfxq2(4, &[chi, mu2]) / chi
    };

    let conv_e_nlo = |x: f64, q2: f64| -> f64 {
        let cf_ns = f2nc_nlo_ns::cf();
        let chi = x * (1.0 +  4.0 *mc2 / q2);
        let mu2 = q2; //+ mc2;
        let fxq_local = toypdf.xfxq2(4, &[chi, mu2]) / chi;

        let (val_r, _) = quad(
            |xhat: f64| {
                let fxq = toypdf.xfxq2(4, &[chi / xhat, mu2]) / (chi / xhat);
                fxq * cf_ns.r(xhat, 4.) / xhat
            },
            chi,
            1.0,
            1e-6,
        );

        let (val_s, _) = quad(
            |xhat: f64| {
                let fxq = toypdf.xfxq2(4, &[chi / xhat, mu2]) / (chi / xhat);
                cf_ns.s(xhat, 4.) * (fxq / xhat - fxq_local)
            },
            chi,
            1.0,
            1e-6,
        );

        let val_l = fxq_local * cf_ns.l(chi, 4.);
        
        (toypdf.alphas_q2(mu2) / (4.0 * PI)) * (val_r + val_s + val_l)
    };

    let conv_c = |x: f64, q2: f64| -> f64 {
        let mu2 = q2; //+ mc2;
        let prefactor = toypdf.alphas_q2(mu2) / (4.0 * PI);
        let (val, _) = quad(
            |xhat: f64| {
                let fxq = toypdf.xfxq2(21, &[x / xhat, mu2]) / (x / xhat);
                let cf = f2nc_nlo_gvv::r_00(xhat, q2, mc2);
                fxq * cf / xhat
            },
            x,
            1.0,
            1e-6,
        );
        val * prefactor
    };

    let conv_sub = |x: f64, q2: f64| -> f64 {
        let mu2 = q2; //+ mc2;
        let prefactor = toypdf.alphas_q2(mu2) / (4.0 * PI);
        let chi = x * (1.0 +  4.0 *mc2 / q2);
        let (val, _) = quad(
            |xhat: f64| {
                let fxq = toypdf.xfxq2(21, &[chi / xhat, mu2]) / (chi / xhat);
                let cf =  AQg::reg_coeff_as(1, (mc2 / mu2).ln(), 4.0, xhat);
                fxq * cf / xhat
            },
            chi,
            1.0,
            1e-6,
        );
        val * prefactor
    };

    let q_vec = [
        1.30, 1.50, 1.75, 1.80, 2.00, 2.50, 3.50, 4.00, 4.75, 5.00, 6.00, 8.00, 10.00, 15.00,
        20.00, 30.00, 40.00, 50.00, 60.00, 70.00, 75.00, 80.00, 90.00, 100.00, 110.00, 200.00,
        300.00, 400.00,
    ];

    let yao_vec = [
        0.024756, 0.0298795, 0.0367383, 0.038189, 0.0440585, 0.0593135, 0.0888989, 0.102123,
        0.119609, 0.12485, 0.143182, 0.170387, 0.189542, 0.219941, 0.238512, 0.261366,
        0.275703, 0.285948, 0.293824, 0.30017, 0.302923, 0.305452, 0.309956, 0.313868,
        0.317317, 0.337183, 0.349139, 0.356981,
    ];
    
    let x = 0.01;
    let total_prefactor = x * (4.0 / 9.0); 

    // println!("{:<6} | {:<10} | {:<10} | {:<10}", "q", "Mine", "Yao's", "Rel_Diff");
    println!("{:<6} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10}", "q", "Fe_LO", "Fe_NLO", "Fc", "Sub", "Total");
    println!("------------------------------------------------------------------------");

    for (i, &q) in q_vec.iter().enumerate() {
        let q2 = q * q;
        let res = total_prefactor * (2.0 * conv_e(x, q2) + 2.0 * conv_e_nlo(x, q2) + 1.0 * conv_c(x, q2) - 1.0 *conv_sub(x, q2));
        // let fe_lo = conv_e(x, q2);
        // let fe_nlo = conv_e_nlo(x, q2);
        // let fc = conv_c(x, q2);
        // let sub = conv_sub(x, q2);
        // let yao_res = yao_vec[i];
        // let rel_diff = (res - yao_res) / yao_res;

        // println!("{:<6.1} | {:<10.6} | {:<10.6} | {:<+9.4}%", q, res, yao_res, rel_diff * 100.0);
        // println!("{:<6.1} | {:<10.6} | {:<10.6} | {:<10.6} | {:<10.6}", q, fe_lo, fe_nlo, fc, sub);
        let fe_lo = conv_e(x, q2);
        let fe_nlo = conv_e_nlo(x, q2);
        let fc = conv_c(x, q2);
        let sub = conv_sub(x, q2);
        
        let term_fe_lo = total_prefactor * 2.0 * fe_lo;
        let term_fe_nlo = total_prefactor * 2.0 * fe_nlo;
        let term_fc = total_prefactor * fc;
        let term_sub = total_prefactor * sub;
        
        let res = term_fe_lo + term_fe_nlo + term_fc - term_sub;
        println!(
            "{:<7.2} {:<14.8} {:<14.8} {:<14.8} {:<14.8} {:<14.8}",
            q,
            term_fe_lo,
            term_fe_nlo,
            term_fc,
            term_sub,
            res
        );
    }
}

