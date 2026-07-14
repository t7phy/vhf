use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = - 4926.0 + 7725.0 * x + 57256.0 * pow(x, 2) + 12898.0 * pow(x, 3) - 32.0 * d27 * pow(dl, 5) - 8796.0 * d243 * pow(dl, 4) - 309.1 * pow(dl, 3) - 899.6 * pow(dl, 2) - 775.8 * dl + 4.719 * x * pow(dl, 5) - 512.0 * d27 * pow(dl1, 5) + 6336.0 * d27 * pow(dl1, 4) - 3368.0 * pow(dl1, 3) - 2978.0 * pow(dl1, 2) + 18832.0 * dl1 - 56000.0 * (1.0 - x) * pow(dl1, 2) - dl * dl1 * (6158.0 + 1836.0 * dl) + nf * ( 831.6 - 6752.0 * x - 2778.0 * pow(x, 2) + 728.0 * d243 * pow(dl, 4) + 12224.0 * d243 * pow(dl, 3) + 187.3 * pow(dl, 2) + 275.6 * dl + 4.102 * x * pow(dl, 4) - 1920.0 * d243 * pow(dl1, 4) + 153.5 * pow(dl1, 3) - 828.7 * pow(dl1, 2) - 501.1 * dl1 + 171.0 * (1.0 - x) * pow(dl1, 4) + dl * dl1 * (4365.0 + 716.2 * dl - 5983.0 * dl1)) + pow(nf, 2) * ( 129.2 * x + 102.5 * pow(x, 2) - 368.0 * d243 * pow(dl, 3) - 1984.0 * d243 * pow(dl, 2) - 8.042 * dl - 192.0 * d243 * pow(dl1, 3) + 18.21 * pow(dl1, 2) - 19.09 * dl1 + dl * dl1 * (-96.07 - 12.46 * dl + 85.88 * dl1));
    return res;
}

fn s_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1. - x);
    let dm: f64 = 1.0 / (1.0 - x);
    let res: f64 = (1536.0 * d81 * pow(dl1, 5)  - 16320.0 * d81 * pow(dl1, 4)  + 5.01099e2 * pow(dl1, 3)  + 1.17154e3 * pow(dl1, 2)  - 7.32845e3 * dl1  + 4.44276e3  + nf  * ( 640.0 * d81 * pow(dl1, 4)  - 6592.0 * d81 * pow(dl1, 3)  + 220.573 * pow(dl1, 2)  + 294.906 * dl1  - 729.359) + pow(nf, 2) * (64.0 * d81 * pow(dl1, 3) - 464.0 * d81 * pow(dl1, 2) + 7.67505 * dl1 + 1.00830)) * dm;
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1. - x);
    let res: f64 =  256.0 * d81 * pow(dl1, 6)  - 3264.0 * d81 * pow(dl1, 5)  + 1.252745e2 * pow(dl1, 4)  + 3.905133e2 * pow(dl1, 3)  - 3.664225e3 * pow(dl1, 2)  + 4.44276e3 * dl1  - 9195.48  + 25.10  + nf  * (  128.0 * d81 * pow(dl1, 5)  - 1648.0 * d81 * pow(dl1, 4)  + 220.573 * d3 * pow(dl1, 3)  + 147.453 * pow(dl1, 2)  - 729.359 * dl1  + 2575.074  - 0.387) + pow(nf, 2) * (  16.0 * d81 * pow(dl1, 4)  - 464.0 * d81 * d3 * pow(dl1, 3)  + 7.67505 * 1.0 / 5.0 * pow(dl1, 2)  + 1.0083 * dl1  - 103.2521  + 0.0155);
    return res;
}

mkcoeff!(r_00, s_00, l_00);

pub fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns(nf as i8, q2, interaction_type, false)
}

const orders: [i8; 5] = [3, 2, 0, 0, 0];
const orders_red: [i8; 5] = [3, 0, 0, 0, 0];

pub const as_norm: f64 = inv4PI * inv4PI * inv4PI;
