use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = nf * ( (94.74 - 49.20 * x) * (1.-x) * pow(dl1, 2) + 864.8 * (1.-x) * dl1 + 1161.* x * dl * dl1 + 60.06 * x * pow(dl, 2) + 39.66 * (1.-x) * dl - 5.333 * (1./x - 1.) );
    return res;
}

mkcoeff!(r_00, _, _);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_g(nf as i8, q2, interaction_type)
}
const orders: [i8; 5] = [2, 2, 0, 0, 0];
const orders_red: [i8; 5] = [2, 0, 0, 0, 0];

const as_norm: f64 = inv4PI * inv4PI;
