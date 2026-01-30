use crate::dis::internal::*;
use super::flnc_n3lo_nsp;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let x1: f64 = 1.0 - x;
    let res1: f64 = flnc_n3lo_nsp::cf().r.unwrap()(x, nf);
    let res2: f64 = (( -620.53 - 394.5 * x + 1609.0 * pow(x, 2) - 596.2 * pow(x, 3) + 0.217 * pow(dl, 3) + 62.18 * pow(dl, 2) + 208.47 * dl - 482.5 * dl * dl1 - x * dl * (1751.0 - 197.5 * dl) + 105.5 * dl1 + 0.442 * pow(dl1, 2)) + nf * ( -6.500 - 12.435 * x + 23.66 * pow(x, 2) + 0.914 * pow(x, 3) + 0.015 * pow(dl, 3) - 6.627 * pow(dl, 2) - 31.91 * dl - x * dl * (5.711 + 28.635 * dl))) * pow(x1, 2);
    return res1 - res2;
}

fn l_00(x: f64, nf: f64) -> f64 {
    return flnc_n3lo_nsp::cf().l.unwrap()(x, nf);
}

mkcoeff!(r_00, _, l_00);
