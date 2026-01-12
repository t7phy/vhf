use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = nf * ( (94.74 - 49.20 * x) * (1.-x) * pow(dl1, 2) + 864.8 * (1.-x) * dl1 + 1161.* x * dl * dl1 + 60.06 * x * pow(dl, 2) + 39.66 * (1.-x) * dl - 5.333 * (1./x - 1.) );
    return res;
}
