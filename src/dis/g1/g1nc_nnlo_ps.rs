#![allow(non_snake_case)]
use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let x2: f64 = pow(x, 2);
    let Li31mx: f64 = nl(2, 1, 1.0 - x).re;
    let Li21mx: f64 = nl(1, 1, 1.0 - x).re;
    let Li2mx: f64 = nl(1, 1, -x).re;
    let ln1mx: f64 = log(1.0 - x);
    let ln1mx2: f64 = pow(ln1mx, 2);
    let lnx: f64 = log(x);
    let lnx2: f64 = pow(lnx, 2);
    let lnx3: f64 = pow(lnx, 3);
    let ln1px: f64 = log(1.0 + x);
    let res: f64 =  nf * CF * TR * ((1.0 + x)* ( -16.0 * Li31mx + 16.0 * ln1mx * Li21mx - 16.0 * lnx * Li21mx - 16.0 * z2 * lnx + 8.0 * lnx * ln1mx2 - 16.0 * lnx2 * ln1mx * 20.0 * lnx3 / 3.0)+ (1.0 - x) * (20.0 * ln1mx2 - 88.0 * ln1mx + 760.0 / 3.0)- 32.0 * (1.0 + x2 / 3.0 + x + 1.0 / x / 3.0) * (Li2mx + lnx * ln1px)+ (50.0 + 16.0 * x2 / 3.0 - 10.0 * x) * lnx2- 32.0 * (2.0 - x) * lnx * ln1mx+ 4.0 * (119.0 - 13.0 * x) * lnx / 3.0- (72.0 + 32.0 * x2 / 3.0 - 40.0 * x) * z2- 8.0 * (3.0 + x) * Li21mx );
    return res;
}

mkcoeff!(r_00, _, _);
