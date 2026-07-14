use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = - 40.41 + 97.48 * x + (26.56 * x - 0.031) * pow(dl, 2) - 14.85 * dl + 13.62 * pow(dl1, 2) - 55.79 * dl1 - 150.5 * dl * dl1 + nf * 16./27.0 * ( 6.* x*dl1 - 12.* x*dl - 25.* x + 6.);
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    return -0.164;
}

mkcoeff!(r_00, _, l_00);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns(nf as i8, q2, interaction_type, false)
}
const orders: [i8; 5] = [2, 2, 0, 0, 0];
const orders_red: [i8; 5] = [2, 0, 0, 0, 0];

const as_norm: f64 = inv4PI * inv4PI;
