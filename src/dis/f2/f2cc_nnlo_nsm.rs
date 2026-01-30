use crate::dis::internal::*;

fn r_00(x: f64, nf: f64) -> f64 {
    let dl: f64 = log(x);
    let dl1: f64 = log(1. - x);
    let res: f64 = - 84.18 - 1010.* x - 3.748 * pow(dl, 3) - 19.56 * pow(dl, 2) - 1.235 * dl - 17.19 * pow(dl1, 3) + 71.08 * pow(dl1, 2) - 663.0 * dl1 - 192.4 * dl * pow(dl1, 2) + 80.41 * pow(dl, 2) * dl1 + nf * ( - 5.691 - 37.91 * x + 2.244 * pow(dl, 2) + 5.770 * dl - 1.707 * pow(dl1, 2)  + 22.95 * dl1 + 3.036 * pow(dl, 2) * dl1 + 17.97 * dl * dl1 );
    return res;
}

fn s_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1. - x);
    let dm: f64 = 1.0 / (1.0 - x);
    let res: f64 = (14.2222 * pow(dl1, 3) - 61.3333 * pow(dl1, 2) - 31.105 * dl1 + 188.64 + nf * ( 1.77778 * pow(dl1, 2) - 8.5926 * dl1 + 6.3489 )) * dm;
    return res;
}

fn l_00(x: f64, nf: f64) -> f64 {
    let dl1: f64 = log(1. - x);
    let res: f64 =  3.55555 * pow(dl1, 4) - 20.4444 * pow(dl1, 3) - 15.5525 * pow(dl1, 2) + 188.64 * dl1 - 338.531 + 0.537 + nf * (0.592593 * pow(dl1, 3) - 4.2963 * pow(dl1, 2) + 6.3489 * dl1 + 46.844 - 0.0035);
    return res;
}

mkcoeff!(r_00, s_00, l_00);
