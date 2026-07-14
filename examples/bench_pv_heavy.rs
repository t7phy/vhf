use vhf::dis::{f3_heavy, g4_heavy, gl_heavy};

fn main() {
    let pid: f64 = 4.0;
    let m2: f64 = 1.273_f64.powi(2);

    let test_points: Vec<(f64, f64)> = vec![
        (0.01, 10.0),
        (0.1, 10.0),
        (0.001, 100.0),
        (0.01, 100.0),
        (0.1, 100.0),
        (0.5, 10.0),
        (0.3, 10.0),
        (0.001, 10000.0),
        (0.01, 10000.0),
        (0.4, 10.0),
        (0.01, 5000.0),
    ];

    println!("# pv_heavy NC NNLO benchmark");
    println!("# x, Q2, f3_r, f3_l, g4_r, g4_l, gl_r, gl_l");

    for &(x, q2) in &test_points {
        let f3_r = f3_heavy::f3nc_nnlo_ns::r_00(x, q2, pid);
        let f3_l = f3_heavy::f3nc_nnlo_ns::l_00(x, q2, pid);
        let g4_r = g4_heavy::g4nc_nnlo_ns::r_00(x, q2, pid);
        let g4_l = g4_heavy::g4nc_nnlo_ns::l_00(x, q2, pid);
        let gl_r = gl_heavy::glnc_nnlo_ns::r_00(x, q2, pid);
        let gl_l = gl_heavy::glnc_nnlo_ns::l_00(x, q2, pid);

        println!(
            "{:.6e}, {:.6e}, {:.15e}, {:.15e}, {:.15e}, {:.15e}, {:.15e}, {:.15e}",
            x, q2, f3_r, f3_l, g4_r, g4_l, gl_r, gl_l
        );
    }
}
