use crate::dis::internal::*;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1.0 - x);
    let x1: f64 = 1.0 - x;
    let res: f64 = nf * (( ( 856.0 * d81 * pow(dl1, 4) - 6032.0 * d81 * pow(dl1, 3) + 130.57 * pow(dl1, 2) - 542.0 * dl1 + 8501.0 - 4714.0 * x + 61.50 * pow(x, 2) ) * x1 + dl * dl1 * (8831.0 * dl + 4162.0 * x1) - 15.44 * x * pow(dl, 5) + 3333.0 * x * pow(dl, 2) + 1615.0 * dl + 1208.0 * pow(dl, 2) - 333.73 * pow(dl, 3) + 4244.0 * d81 * pow(dl, 4) - 40.0 * d9 * pow(dl, 5) - 2731.82 * x1 / x - 414.262 * dl / x) + nf * ( ( -64.0 * d81 * pow(dl1, 3) + 208.0 * d81 * pow(dl1, 2) + 23.09 * dl1 - 220.27 + 59.80 * x - 177.6 * pow(x, 2) ) * x1 + -dl * dl1 * (160.3 * dl + 135.4 * x1) - 24.14 * x * pow(dl, 3) - 215.4 * x * pow(dl, 2) - 209.8 * dl - 90.38 * pow(dl, 2) - 3568.0 / 243.0 * pow(dl, 3) - 184.0 * d81 * pow(dl, 4) + 40.2426 * x1 / x));
    return res;
}
