use vhf::dis::f2_light;

fn main() {
    let nf = 3.0;
    let x_vec: Vec<f64> = (-5..=-1)
        .flat_map(|exp| {
            let base = 10f64.powi(exp);
            let max = if exp == -1 { 4 } else { 9 };
            (1..=max).map(move |i| i as f64 * base)
        })
        .collect();

    let coefficients = vec![
        ("LO NS", f2_light::f2nc_lo_ns::cf()),
        ("NLO NS", f2_light::f2nc_nlo_ns::cf()),
        ("NLO G", f2_light::f2nc_nlo_g::cf()),
        ("NNLO NSP", f2_light::f2nc_nnlo_nsp::cf()),
        ("NNLO PS", f2_light::f2nc_nnlo_ps::cf()),
        ("NNLO G", f2_light::f2nc_nnlo_g::cf()),
        ("N3LO NSP", f2_light::f2nc_n3lo_nsp::cf()),
        ("N3LO NSM", f2_light::f2cc_n3lo_nsm::cf()),
        ("N3LO PS", f2_light::f2nc_n3lo_ps::cf()),
        ("N3LO G", f2_light::f2nc_n3lo_g::cf()),
        ("N3LO Q_Fl11", f2_light::f2nc_n3lo_qfl11::cf()),
        ("N3LO G_Fl11", f2_light::f2nc_n3lo_gfl11::cf())
    ];

    for (name, cf) in coefficients {
        println!("\n--- Table for: {} ---", name);
        
        // Header: x is now narrower (8), results stay wide (20)
        println!("{:>8} | {:>20} | {:>20} | {:>20}", "x", "r(x, nf)", "s(x, nf)", "l(x, nf)");
        println!("{}", "-".repeat(75));

        for &x in &x_vec {
            let r_val = cf.r(x, nf);
            let s_val = cf.s(x, nf);
            let l_val = cf.l(x, nf);

            // :>8.1e  -> Right-aligned, width 8, scientific with 1 decimal (e.g., 1.0e-5)
            // :>20.10f -> Right-aligned, width 20, decimal with 10 places
            println!(
                "{:>8.1e} | {:>20.10} | {:>20.10} | {:>20.10}",
                x, r_val, s_val, l_val
            );
        }
    }
}