use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let res: f64 = nf * ( 1./x * (11.90 + 1494.* dl1) + 5.319 * pow(dl, 3) - 59.48 * pow(dl, 2) - 284.8 * dl + 392.4 - 1483.* dl1 + (6.445 + 209.4 * (1.-x)) * pow(dl1, 3) - 24.00 * pow(dl1, 2) - 724.1 * pow(dl, 2) * dl1 - 871.8 * dl * pow(dl1, 2) );
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    return - nf * 0.28;
}

mkcoeff!(r_00, _, l_00);

pub fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_g(nf as i8, q2, interaction_type)
}

const orders: [i8; 5] = [2, 2, 0, 0, 0];
const orders_red: [i8; 5] = [2, 0, 0, 0, 0];

pub const as_norm: f64 = inv4PI * inv4PI;
