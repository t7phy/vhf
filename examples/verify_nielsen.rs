// examples/verify_nielsen.rs
use std::env;
// Replace 'your_crate_name' with the name in your Cargo.toml
use vhf::core::nielsen::nl; 

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 4 {
        eprintln!("Usage: verify_nielsen <N> <M> <X>");
        std::process::exit(1);
    }

    let n: usize = args[1].parse().unwrap();
    let m: usize = args[2].parse().unwrap();
    let x: f64 = args[3].parse().unwrap();

    let result = nl(n as i64, m as i64, x);

    // Print in a format Python can easily parse: "real,imag"
    println!("{:.16},{:.16}", result.re, result.im);
}