use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let x1: f64 = 1.0 - x;
    let res: f64 = nf * (( 966.0 * d81 * pow(dl1, 5) - 935.5 * d9 * pow(dl1, 4) + 89.31 * pow(dl1, 3) + 979.2 * pow(dl1, 2) - 2405.0 * dl1 + 1372.0 * (1.0 - x) * pow(dl1, 4) - 15729.0 - 310510.0 * x + 331570.0 * pow(x, 2) - 244150.0 * x * pow(dl, 2) - 253.3 * x * pow(dl, 5) + dl * dl1 * (138230.0 - 237010.0 * dl) - 11860.0 * dl - 700.8 * pow(dl, 2) - 1440.0 * pow(dl, 3) + 2480.5 * d81 * pow(dl, 4) - 134.0 * d9 * pow(dl, 5) - 6362.54 * x1 - 932.089 * dl * x1) + nf * ( 131.0 * d81 * pow(dl1, 4) - 14.72 * pow(dl1, 3) + 3.607 * pow(dl1, 2) - 226.1 * dl1 + 4.762 - 190.0 * x - 818.4 * pow(x, 2) - 4019.0 * x * pow(dl, 2) - dl * dl1 * (791.5 + 4646.0 * dl) + 739.0 * dl + 418.0 * pow(dl, 2) + 104.3 * pow(dl, 3) + 809.0 * d81 * pow(dl, 4) + 12.0 * d9 * pow(dl, 5) + 84.423 * x1));
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    return 0.625 * nf;
}

mkcoeff!(r_00, _, l_00);

pub fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_g(nf as i8, q2, interaction_type)
}

const orders: [i8; 5] = [3, 2, 0, 0, 0];
const orders_red: [i8; 5] = [3, 0, 0, 0, 0];

pub const as_norm: f64 = inv4PI * inv4PI * inv4PI;
