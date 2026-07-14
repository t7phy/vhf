use crate::dis::internal::*;
use super::super::f2_light::f2nc_nlo_ns;

fn r_00(x: f64, nf: f64) -> f64 {
    let res: f64 = f2nc_nlo_ns::cf().r(x, nf) - 2.0 * CF * (1.0 + x);
    return res;
}

fn s_00(x: f64, nf: f64) -> f64 {
    return f2nc_nlo_ns::cf().s(x, nf);
}

fn l_00(x: f64, nf: f64) -> f64 {
    return f2nc_nlo_ns::cf().l(x, nf);
}

mkcoeff!(r_00, s_00, l_00);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns(nf as i8, q2, interaction_type, true)
}
const orders: [i8; 5] = [1, 2, 0, 0, 0];
const orders_red: [i8; 5] = [1, 0, 0, 0, 0];

const as_norm: f64 = inv4PI;
