use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = - 52.27 + 100.8 * x + (23.29 * x - 0.043) * pow(dl, 2) - 22.21 * dl + 13.30 * pow(dl1, 2) - 59.12 * dl1 - 141.7 * dl * dl1 + nf * 16./27.0 * ( 6.* x*dl1 - 12.* x*dl - 25.* x + 6.);
    return res;
}

pub fn l_00(x: f64, nf: f64) -> f64 {
    return -0.150;
}
