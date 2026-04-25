use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let x1: f64 = 1.0 - x;
    let res: f64 = nf * ( (126.42 - 50.29 * x - 50.15 * pow(x, 2)) * x1 - 26.717 - 320.0 * d81 * pow(dl, 2) * (dl + 5.0) + 59.59 * dl - x * pow(dl, 2) * (101.8 + 34.79 * dl + 3.070 * pow(dl, 2)) - 9.075 * x * x1 * dl1) * x;
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    return -nf * 11.8880;
}

mkcoeff!(r_00, _, l_00);

pub fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns_fl11(nf as i8, q2, interaction_type)
}

const orders: [i8; 5] = [3, 2, 0, 0, 0];
const orders_red: [i8; 5] = [3, 0, 0, 0, 0];

pub const as_norm: f64 = inv4PI * inv4PI * inv4PI;
