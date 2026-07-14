use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    return CF * 4.0 * x;
}

mkcoeff!(r_00, _, _);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns(nf as i8, q2, interaction_type, false)
}
const orders: [i8; 5] = [1, 2, 0, 0, 0];
const orders_red: [i8; 5] = [1, 0, 0, 0, 0];

const as_norm: f64 = inv4PI;
