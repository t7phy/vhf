use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = nf * ( (15.94 - 5.212 * x) * pow(1.-x, 2) * dl1 + (0.421 + 1.520 * x) * pow(dl, 2) + 28.09 * (1.-x) * dl - (2.370/x - 19.27) * pow(1.-x, 3) );
    return res;
}
