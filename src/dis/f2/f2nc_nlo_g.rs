use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let res: f64 = nf * ((2.0 - 4.0 * x * (1.0 - x)) * log((1.0 - x) / x) - 2.0 + 16.0 * x * (1.0 - x)) * (2.0 * TR);
    return res;
}
