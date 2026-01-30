use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let res: f64 = nf * ( (107.0 + 321.05 * x - 54.62 * pow(x, 2)) * (1.0 - x) - 26.717 - 320.0 * d81 * pow(dl, 3) - 640.0 * d81 * pow(dl, 2) + 9.773 * dl + x * dl * (363.8 + 68.32 * dl)) * x;
    return res;
}

mkcoeff!(r_00, _, _);
