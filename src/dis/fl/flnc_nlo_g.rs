use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    return nf * TR * 16.0 * x * (1.0 - x);
}

mkcoeff!(r_00, _, _);
