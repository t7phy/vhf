use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = nf * ( (15.94 - 5.212 * x) * pow(1.-x, 2) * dl1 + (0.421 + 1.520 * x) * pow(dl, 2) + 28.09 * (1.-x) * dl - (2.370/x - 19.27) * pow(1.-x, 3) );
    return res;
}

mkcoeff!(r_00, _, _);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_s(nf as i8, q2, interaction_type)
}
const orders: [i8; 5] = [2, 2, 0, 0, 0];
const orders_red: [i8; 5] = [2, 0, 0, 0, 0];

const as_norm: f64 = inv4PI * inv4PI;
