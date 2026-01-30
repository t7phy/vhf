use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let res: f64 = nf * ( 5.290 * (1./x-1.) + 4.310 * pow(dl, 3) - 2.086 * pow(dl, 2) + 39.78 * dl - 0.101 * (1.-x) * pow(dl1, 3) - (24.75 - 13.80 * x) * pow(dl, 2) * dl1 + 30.23 * dl * dl1 );
    return res;
}

mkcoeff!(r_00, _, _);
