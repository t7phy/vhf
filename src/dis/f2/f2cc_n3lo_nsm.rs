use crate::dis::internal::*;
use super::f2nc_n3lo_nsp;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let x1: f64 = 1.0 - x;
    let res1: f64 = f2nc_n3lo_nsp::r_00(x, nf);
    let res2: f64 = (( 273.59 - 44.95 * x - 73.56 * pow(x, 2) + 40.68 * pow(x, 3) + 0.1356 * pow(dl, 5) + 8.483 * pow(dl, 4) + 55.90 * pow(dl, 3) + 120.67 * pow(dl, 2) + 388.0 * dl - 329.8 * dl * dl1 - x * dl * (316.2 + 71.63 * dl) + 46.30 * dl1 + 5.447 * pow(dl1, 2)) + nf * ( -19.093 + 12.97 * x + 36.44 * pow(x, 2) - 29.256 * pow(x, 3) - 0.76 * pow(dl, 4) - 5.317 * pow(dl, 3) - 19.82 * pow(dl, 2) - 38.958 * dl - 13.395 * dl * dl1 + x * dl * (14.44 + 17.74 * dl) + 1.395 * dl1)) * x1;
    let res: f64 = res1 - res2;
    return res;
}

pub fn s_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1. - x);
    let dm: f64 = 1.0 / (1.0 - x);
    let res: f64 = (1536.0 * d81 * pow(dl1, 5) - 16320.0 * d81 * pow(dl1, 4) + 5.01099e2 * pow(dl1, 3) + 1.17154e3 * pow(dl1, 2) - 7.32845e3 * dl1 + 4.44276e3 + nf * ( 640.0 * d81 * pow(dl1, 4) - 6592.0 * d81 * pow(dl1, 3) + 220.573 * pow(dl1, 2) + 294.906 * dl1 - 729.359) + pow(nf, 2) * (64.0 * d81 * pow(dl1, 3) - 464.0 * d81 * pow(dl1, 2) + 7.67505 * dl1 + 1.00830)) * dm;
    return res;
}

pub fn l_00(x: f64, nf: f64) -> f64 {
    let res1: f64 = f2nc_n3lo_nsp::l_00(x, nf);
    let res2: f64 = - 0.0008 + 0.0001 * nf;
    let res: f64 = res1 - res2;
    return res;
}
