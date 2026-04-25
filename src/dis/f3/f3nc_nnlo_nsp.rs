use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let res: f64 = - 206.1 - 576.8 * x - 3.922 * pow(dl, 3) - 33.31 * pow(dl, 2) - 67.60 * dl - 15.20 * pow(dl1, 3) + 94.61 * pow(dl1, 2) - 409.6 * dl1 - 147.9 * dl * pow(dl1, 2) + nf * ( - 6.337 - 14.97 * x + 2.207 * pow(dl, 2) + 8.683 * dl + 0.042 * pow(dl1, 3) - 0.808 * pow(dl1, 2) + 25.00 * dl1 + 9.684 * dl * dl1 );
    return res;
}

fn s_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1.0 - x);
    let dm: f64 = 1.0 / (1.0 - x);
    let res: f64 = (14.2222 * pow(dl1, 3) - 61.3333 * pow(dl1, 2) - 31.105 * dl1 + 188.64 + nf * ( 1.77778 * pow(dl1, 2) - 8.5926 * dl1 + 6.3489 )) * dm;
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1.0 - x);
    let res: f64 = 3.55555 * pow(dl1, 4) - 20.4444 * pow(dl1, 3) - 15.5525 * pow(dl1, 2) + 188.64 * dl1 - 338.531 - 0.104 + nf * (0.592593 * pow(dl1, 3) - 4.2963 * pow(dl1, 2) + 6.3489 * dl1 + 46.844 + 0.013);
    return res;
}

mkcoeff!(r_00, s_00, l_00);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns(nf as i8, q2, interaction_type, true)
}
const orders: [i8; 5] = [2, 2, 0, 0, 0];
const orders_red: [i8; 5] = [2, 0, 0, 0, 0];

const as_norm: f64 = inv4PI * inv4PI;
