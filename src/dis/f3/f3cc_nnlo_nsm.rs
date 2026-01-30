use crate::dis::internal::*;
use super::f3nc_nnlo_nsp;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let res: f64 = - 242.9 - 467.2 * x - 3.049 * pow(dl, 3) - 30.14 * pow(dl, 2) - 79.14 * dl - 15.20 * pow(dl1, 3) + 94.61 * pow(dl1, 2) - 396.1 * dl1 - 92.43 * dl * pow(dl1, 2) + nf * ( - 6.337 - 14.97 * x + 2.207 * pow(dl, 2) + 8.683 * dl + 0.042 * pow(dl1, 3) - 0.808 * pow(dl1, 2)  + 25.00 * dl1 + 9.684 * dl * dl1 );
    return res;
}

fn s_00(x: f64, nf: f64) -> f64 {
    return f3nc_nnlo_nsp::cf().s.unwrap()(x, nf);
}

fn l_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1.0 - x);
    let res: f64 = 3.55555 * pow(dl1, 4) - 20.4444 * pow(dl1, 3) - 15.5525 * pow(dl1, 2) + 188.64 * dl1 - 338.531  - 0.152 + nf * (0.592593 * pow(dl1, 3) - 4.2963 * pow(dl1, 2) + 6.3489 * dl1 + 46.844 + 0.013);
    return res;
}

mkcoeff!(r_00, s_00, l_00);
