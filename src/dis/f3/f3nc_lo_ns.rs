use crate::dis::internal::*;


fn l_00(x: f64, nf: f64) -> f64 {
    return 1.0;
}

mkcoeff!(_, _, l_00);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns(nf as i8, q2, interaction_type, true)
}
const orders: [i8; 5] = [0, 2, 0, 0, 0];
const orders_red: [i8; 5] = [0, 0, 0, 0, 0];

const as_norm: f64 = 1.0;
