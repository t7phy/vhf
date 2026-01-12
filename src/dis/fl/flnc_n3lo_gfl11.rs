use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let x1: f64 = 1.0 - x;
    let res: f64 = pow(nf, 2) * ( ( -0.0105 * pow(dl1, 3) + 1.550 * pow(dl1, 2) + 19.72 * x * dl1 - 66.745 * x + 0.615 * pow(x, 2) ) * x1 + 20.0 * d27 * x * pow(dl, 4) + (280.0 / 81.0 + 2.260 * x) * x * pow(dl, 3) - (15.40 - 2.201 * x) * x * pow(dl, 2) - (71.66 - 0.121 * x) * x * dl);
    return res;
}
