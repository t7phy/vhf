use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let res: f64 = 4.0 * nf * TR * ((2.0 * x - 1.0) * log((1.0 - x) / x) - 4.0 * x + 3.0);
    return res;
}
