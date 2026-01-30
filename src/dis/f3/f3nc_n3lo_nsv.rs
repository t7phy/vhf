use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let x1: f64 = 1.0 - x;
    let fl02: f64 = 1.0;
    let res: f64 = fl02 * nf * ( 48.79 - (242.4 - 150.7 * x) * x1 - 16.0 / 27.0 * pow(dl, 5) + 17.26 * pow(dl, 3) - 113.4 * pow(dl, 2) - 477.0 * dl + 2.147 * pow(dl1, 2) - 24.57 * dl1 + x * dl * (218.1 + 82.27 * pow(dl, 2)) - dl * dl1 * (81.70 + 9.412 * dl1)) * x1;
    return res;
}

mkcoeff!(r_00, _, _);
