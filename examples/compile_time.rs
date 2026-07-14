// examples/bench_ft.rs
// use vhf::dis::f2::f2nc_lo_ns::cf;
use vhf::sidis::ft::FTC2q2qM;

fn main() {
    // Call a function from ft to force the compiler to check it
    // Replace 'some_math_function' with an actual function in ft.rs
    // let _ = ft::some_math_function(); 
    // let _ = cf().l.unwrap()(0.5, 4.0);
    // let val = FTC2q2qM::cf("000").rs.unwrap()(0.5, 0.4, 3.0);    
    // println!("Computed value: {}", val);
    let val = FTC2q2qM::scales();
    println!("Available scales: {:?}", val);
}