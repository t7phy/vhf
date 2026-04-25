use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let li2: f64 = nl(1, 1, x).re;
    let res: f64 = - 2220.5 - 7884.0 * x + 4168.0 * pow(x, 2) - 1280.0 * d81 * pow(dl, 3) - 7456.0 / 27.0 * pow(dl, 2) - 1355.7 * dl + 512.0 / 27.0 * pow(dl1, 4) - 177.40 * pow(dl1, 3) + 650.6 * pow(dl1, 2) - 2729.0 * dl1 + 208.3 * x * pow(dl, 3) - pow(dl1, 3) * (1.0 - x) * (125.3 - 195.6 * dl1) - dl * dl1 * (844.7 * dl + 517.3 * dl1) + nf * ( 408.4 - 9.345 * x - 919.3 * pow(x, 2) + 1728.0 * d81 * pow(dl, 2) + 200.73 * dl - 1792.0 * d81 * x * pow(dl, 3) + 1024.0 * d81 * pow(dl1, 3) - 112.35 * pow(dl1, 2) + 344.1 * dl1 + (1.0 - x) * pow(dl1, 2) * (239.7 + 20.63 * dl1) + dl * dl1 * (887.3 + 294.5 * dl - 59.14 * dl1)) + pow(nf, 2) * ( -19.0 + (317.0 / 6.0 - 12.0 * z2) * x + 9.0 * x * pow(dl, 2) + dl * (-6.0 + 50.0 * x) + 3.0 * x * pow(dl1, 2) + dl1 * (6.0 - 25.0 * x) - 6.0 * x * dl * dl1 + 6.0 * x * li2) * 64.0 * d81;
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    return 0.113 + nf * 0.006;
}

mkcoeff!(r_00, _, l_00);

fn nc_coupling(nf: f64, q2: f64, interaction_type: String) ->  Vec<(i8, f64)> {
    couplings::nc_ns(nf as i8, q2, interaction_type, false)
}
const orders: [i8; 5] = [3, 2, 0, 0, 0];
const orders_red: [i8; 5] = [3, 0, 0, 0, 0];

const as_norm: f64 = inv4PI * inv4PI * inv4PI;
