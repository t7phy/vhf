use crate::dis::internal::*;
use super::f3nc_n3lo_nsp;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let x1: f64 = 1.0 - x;
    let res1: f64 = f3nc_n3lo_nsp::r_00(x, nf);
    let res2: f64 = (( - 553.5 + 1412.5 * x - 990.3 * pow(x, 2) + 361.1 * pow(x, 3) + 0.1458 * pow(dl, 5) + 9.688 * pow(dl, 4) + 90.62 * pow(dl, 3) + 83.684 * pow(dl, 2) - 602.32 * dl - 382.5 * dl * dl1 - x * dl * (2.805 + 325.92 * dl) + 133.5 * dl1 + 10.135 * pow(dl1, 2)) + nf * ( -16.777 + 77.78 * x - 24.81 * pow(x, 2) - 28.89 * pow(x, 3) - 0.7714 * pow(dl, 4) - 7.701 * pow(dl, 3) - 21.522 * pow(dl, 2) - 7.897 * dl - 16.17 * dl * dl1 + x * dl * (43.21 + 67.04 * dl) + 1.519 * dl1)) * x1;
    let res: f64 = res1 + res2;
    return res;
}

pub fn s_00(x: f64, nf: f64) -> f64 {
    return f3nc_n3lo_nsp::s_00(x, nf);
}

pub fn l_00(x: f64, nf: f64) -> f64 {
    let res1: f64 = f3nc_n3lo_nsp::l_00(x, nf);
    let res2: f64 = - 0.0029 + 0.00006 * nf;
    let res: f64 = res1 + res2;
    return res;
}
