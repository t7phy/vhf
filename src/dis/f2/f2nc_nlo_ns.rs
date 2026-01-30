use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let res: f64 = CF*( - 2. * (1. + x) * log((1. - x) / x) - 4. * log(x) / (1. - x) + 6. + 4. * x);
    return res;
}

fn s_00(x: f64, nf: f64) -> f64 {
    let res: f64 = (-3. * CF)/(1. - x) + (4. * CF) * log(1. - x) / (1. - x);
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    let res: f64 = - CF * (9. + 4. * z2) + (-3. * CF) * log(1. - x) + (4. * CF) * pow(log(1. - x), 2)/2.;
    return res;
}

mkcoeff!(r_00, s_00, l_00);
