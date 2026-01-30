use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let x1: f64 = 1.0 - x;
    let res: f64 = nf * (( (1568.0 * d27 * pow(dl1, 3) - 11904.0 * d27 * pow(dl1, 2) + 5124.0 * dl1) * pow(x1, 2) + dl * dl1 * (2184.0 * dl + 6059.0 * x1) - (795.6 + 1036.0 * x) * pow(x1, 2) - 143.6 * dl * x1 + 8544.0 * d27 * pow(dl, 2) - 1600.0 * d27 * pow(dl, 3) - 885.53 / x * pow(x1, 2) - 182.00 * dl / x * x1) + nf * ( (-96.0 * d27 * pow(dl1, 2) + 29.52 * dl1) * pow(x1, 2) + dl * dl1 * (35.18 * dl + 73.06 * x1) - (14.16 - 69.84 * x) * pow(x1, 2) - 35.24 * x * pow(dl, 2) - 69.41 * dl * x1 - 384.0 * d27 * pow(dl, 2) + 40.239 / x * pow(x1, 2)));
    return res;
}

mkcoeff!(r_00, _, _);
