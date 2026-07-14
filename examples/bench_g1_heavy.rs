use vhf::dis::g1_heavy;

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
        (0.4, 10.0),
    ];

    println!("# g1_heavy NC NNLO benchmark");
    println!("# x, Q2, gvv, gaa, psvv, psaa, ns_r, ns_l");

    for &(x, q2) in &test_points {
        let xi = q2 / m2;
        let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;

        let gvv = g1_heavy::g1nc_nnlo_gvv::r_00(x, q2, pid);
        let gaa = g1_heavy::g1nc_nnlo_gaa::r_00(x, q2, pid);
        let psvv = g1_heavy::g1nc_nnlo_psvv::r_00(x, q2, pid);
        let psaa = g1_heavy::g1nc_nnlo_psaa::r_00(x, q2, pid);
        let ns_r = g1_heavy::g1nc_nnlo_ns::r_00(x, q2, pid);
        let ns_l = g1_heavy::g1nc_nnlo_ns::l_00(x, q2, pid);

        println!(
            "{:.6e}, {:.6e}, {:.15e}, {:.15e}, {:.15e}, {:.15e}, {:.15e}, {:.15e}",
            x, q2, gvv, gaa, psvv, psaa, ns_r, ns_l
        );
    }
}
