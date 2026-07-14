use vhf::dis::couplings as old_couplings;
use vhf::sidis::couplings as new_couplings;


fn main() {
    let old = old_couplings::nc_ns(5, 2.0, "nc".to_string(), false);
    
    println!("Old NC NS Couplings:");
    for (pid, coupling) in old {
        println!("PID: {}, Coupling: {}", pid, coupling);
    }

    let new = new_couplings::nc_ns(11,5, 4.0, "nc");

    println!("\nNew NC NS Couplings:");
    for (pid, coupling) in new {
        println!("PID: {}, Coupling: {}", pid, coupling);
    }

    // let u_charge = new_couplings::quark_charges(2);
    // let ub_charge = new_couplings::quark_charges(-2);
    // println!("\nQuark Charges:");
    // println!("u quark: EM Charge: {}, Vector Coupling: {}, Weak Isospin3: {}", u_charge.0, u_charge.1, u_charge.2);
    // println!("u-bar quark: EM Charge: {}, Vector Coupling: {}, Weak Isospin3: {}", ub_charge.0, ub_charge.1, ub_charge.2);
}

   