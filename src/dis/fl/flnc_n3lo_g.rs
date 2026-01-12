use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let x1: f64 = 1.0 - x;
    let res: f64 = nf * (( (144.0 * pow(dl1, 4) - 47024.0 * d27 * pow(dl1, 3) + 6319.0 * pow(dl1, 2) + 53160.0 * dl1) * x1 + dl * dl1 * (72549.0 + 88238.0 * dl) + (3709.0 - 33514.0 * x - 9533.0 * pow(x, 2)) * x1 + 66773.0 * x * pow(dl, 2) - 1117.0 * dl + 45.37 * pow(dl, 2) - 5360.0 * d27 * pow(dl, 3) - 2044.70 / x * x1 - 409.506 * dl / x) + nf * ( (288.0 * d27 * pow(dl1, 3) - 3648.0 * d27 * pow(dl1, 2) - 592.3 * dl1 + 1511.0 * x * dl1) * x1 + dl * dl1 * (311.3 + 14.24 * dl) + (577.3 - 729.0 * x) * x1 + 30.78 * x * pow(dl, 3) + 366.0 * dl + 3000.0 * d27 * pow(dl, 2) + 480.0 * d27 * pow(dl, 3) + 88.5037 / x * x1));
    return res;
}
