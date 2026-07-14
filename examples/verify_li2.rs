use vhf::core::polylogs::{Li2, Li3};

fn main() {
    let eps: f64 = 1e-14;
    let n_uniform: usize = 200;

    println!(
        "{:>3} {:>20} {:>20} {:>20} {:>12}",
        "k", "x", "Li2", "Li3", "status"
    );

    for k in 0..n_uniform {
        // Map to [-1 + eps, 1 - eps]
        let x = -1.0 + eps + (2.0 - 2.0 * eps) * (k as f64) / ((n_uniform - 1) as f64);

        let li2_val = Li2(x);
        let li3_val = Li3(x);
        let ln = x.ln();

        let li2_bad = li2_val.is_nan() || li2_val.is_infinite();
        let li3_bad = li3_val.is_nan() || li3_val.is_infinite();

        let status = match (li2_bad, li3_bad) {
            (false, false) => "ok",
            (true, false) => "Li2_bad",
            (false, true) => "Li3_bad",
            (true, true) => "both_bad",
        };

        println!(
            "k = {:3}, x = {:.16e}, Li2 = {:.16e}, Li3 = {:.16e}, ln = {:.16e}, status = {:>10}",
            k,
            x,
            li2_val,
            li3_val,
            ln,
            status
        );
    }
}