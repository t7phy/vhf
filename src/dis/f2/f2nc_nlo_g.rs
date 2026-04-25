use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let res: f64 = nf * ((2.0 - 4.0 * x * (1.0 - x)) * log((1.0 - x) / x) - 2.0 + 16.0 * x * (1.0 - x)) * (2.0 * TR);
    return res;
}

mkcoeff!(r_00, _, _);

pub fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_g(nf as i8, q2, interaction_type)
}

const orders: [i8; 5] = [1, 2, 0, 0, 0];
const orders_red: [i8; 5] = [1, 0, 0, 0, 0];

pub const as_norm: f64 = inv4PI;
