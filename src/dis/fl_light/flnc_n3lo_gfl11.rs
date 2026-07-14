use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let x1: f64 = 1.0 - x;
    let res: f64 = pow(nf, 2) * ( ( -0.0105 * pow(dl1, 3) + 1.550 * pow(dl1, 2) + 19.72 * x * dl1 - 66.745 * x + 0.615 * pow(x, 2) ) * x1 + 20.0 * d27 * x * pow(dl, 4) + (280.0 / 81.0 + 2.260 * x) * x * pow(dl, 3) - (15.40 - 2.201 * x) * x * pow(dl, 2) - (71.66 - 0.121 * x) * x * dl);
    return res;
}

mkcoeff!(r_00, _, _);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_g_fl11(nf as i8, q2, interaction_type)
}
const orders: [i8; 5] = [3, 2, 0, 0, 0];
const orders_red: [i8; 5] = [3, 0, 0, 0, 0];

const as_norm: f64 = inv4PI * inv4PI * inv4PI;
