use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let res: f64 = pow(nf, 2) * ( 3.211 * pow(dl1, 2) + 19.04 * x * dl1 + 0.623 * (1.0 - x) * pow(dl1, 3) - 64.47 * x + 121.6 * pow(x, 2) - 45.82 * pow(x, 3) - x * dl * dl1 * (31.68 + 37.24 * dl) - x * dl * (82.40 + 16.08 * dl) + x * pow(dl, 3) * (520.0 * d81 + 11.27 * x) + 60.0 * d81 * x * pow(dl, 4));
    return res;
}

mkcoeff!(r_00, _, _);
