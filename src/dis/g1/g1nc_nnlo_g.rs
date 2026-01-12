#![allow(non_snake_case)]
use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let x2: f64 = pow(x, 2);
    let S121mx: f64 = nl(1, 2, 1.0 - x).re;
    let S12mx: f64 = nl(1, 2, -x).re;
    let Li31mx: f64 = nl(2, 1, 1.0 - x).re;
    let Li3mx: f64 = nl(2, 1, -x).re;
    let Li3r: f64 = nl(2, 1, (1.0 - x) / (1.0 + x)).re;
    let Li3mr: f64 = nl(2, 1, -(1.0 - x) / (1.0 + x)).re;
    let Li21mx: f64 = nl(1, 1, 1.0 - x).re;
    let Li2mx: f64 = nl(1, 1, -x).re;
    let ln1mx: f64 = log(1.0 - x);
    let ln1mx2: f64 = ln1mx * ln1mx;
    let ln1mx3: f64 = ln1mx * ln1mx2;
    let lnx: f64 = log(x);
    let lnx2: f64 = pow(lnx, 2);
    let lnx3: f64 = pow(lnx, 3);
    let ln1px: f64 = log(1.0 + x);
    let ln1px2: f64 = pow(ln1px, 2);
    let res: f64 = nf * ( CF * TR * ( (1.0 - 2.0 * x) * ( 32.0 * Li31mx - 16.0 * ln1mx * Li21mx - 8.0 * lnx * Li21mx - 24.0 * z2 * lnx - 20.0 * ln1mx3 / 3.0 + 16.0 * lnx * ln1mx2 - 16.0 * lnx2 * ln1mx + 10.0 * lnx3 / 3.0 ) - 16.0 * (1.0 + x2 + 2.0 * x) * ( 4.0 * S12mx + 4.0 * ln1px * Li2mx + 2.0 * lnx * ln1px2 - lnx2 * ln1px + 2.0 * z2 * ln1px ) - 32.0 * (1.0 + x2 - 6.0 * x) * Li3mx + 8.0 * (1.0 + 4.0 * x2 - 2.0 * x) * S121mx + 16.0 * (13.0 * x2 + 12.0 * x + 4.0 / x) * (Li2mx + lnx * ln1px) / 3.0 + 4.0 * (5.0 - 12.0 * x) * Li21mx + 32.0 * (1.0 + x2 - 2.0 * x) * lnx * Li2mx + (123.0 - 104.0 * x2 - 48.0 * x) * lnx2 / 3.0 - (88.0 - 96.0 * x) * lnx * ln1mx + 6.0 * (9.0 - 12.0 * x) * ln1mx2 - 32.0 * z2 * x2 * ln1mx - 4.0 * (31.0 - 4.0 * x2 - 26.0 * x) * ln1mx + (416.0 - 48.0 * x2 - 274.0 * x) * lnx / 3.0 - 8.0 * (5.0 - 4.0 * x2 - 26.0 * x) * z3 - 4.0 * (81.0 - 52.0 * x2 - 108.0 * x) * z2 / 3.0 + 2.0 * (233.0 - 239.0 * x) / 3.0 ) + CA * TR * ( 16.0 * (1.0 + 2.0 * x) * (Li3r - Li3mr - ln1mx * Li2mx - lnx * Li21mx - lnx * ln1mx * ln1px) + 16.0 * (1.0 + x2 + 2.0 * x) * (2.0 * S12mx + lnx * ln1px2 + 2.0 * ln1px * Li2mx + z2 * ln1px) + 8.0 * (1.0 - 2.0 * x2 + 2.0 * x) * S121mx - 8.0 * (9.0 + 2.0 * x) * Li31mx - 8.0 * (1.0 - x2 + 2.0 * x) * (2.0 * Li3mx - lnx2 * ln1px - 2.0 * lnx * Li2mx) - 16.0 * (2.0 + x) * lnx2 * ln1mx + 24.0 * (lnx * ln1mx2 - 2.0 * z2 * lnx - Li21mx) - 16.0 * (6.0 + 11.0 * x2 + 12.0 * x + 2.0 / x) * (Li2mx + lnx * ln1px) / 3.0 - 4.0 * (1.0 - 2.0 * x) * ln1mx3 / 3.0 + 8.0 * (6.0 - 7.0 * x) * ln1mx2 + 8.0 * (3.0 + 2.0 * x2 - 10.0 * x) * z2 * ln1mx + 4.0 * (7.0 + 10.0 * x) * lnx3 / 3.0 + 2.0 * (135.0 + 44.0 * x2 - 48.0 * x) * lnx2 / 3.0 - 8.0 * (17.0 - 16.0 * x) * lnx * ln1mx + 8.0 * (118.0 + 3.0 * x2 - 26.0 * x) * lnx / 3.0 - 4.0 * (44.0 + 2.0 * x2 - 53.0 * x) * ln1mx - 4.0 * (3.0 + 4.0 * x2 + 10.0 * x) * z3 - 16.0 * (27.0 + 11.0 * x2 - 24.0 * x) * z2 / 3.0 + 8.0 * (5.0 + 2.0 * x) * ln1mx * Li21mx + 4.0 * (355.0 - 367.0 * x) / 3.0 ) + CF * TR * ( 16.0 * (1.0 + 2.0 * x) * (2.0 * Li21mx + 2.0 * lnx * ln1mx - lnx2) + 96.0 * (1.0 - x) * ln1mx - (144.0 + 64.0 * x) * lnx - 304.0 * (1.0 - x) ));
    return res;
}
