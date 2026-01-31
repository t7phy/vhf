use crate::sidis::internal::*;

fn RG_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let mut res: f64 = 0.0;
    let tiny: f64 = 1e-4;
    let tinyinv: f64 = 1.0 / tiny;

    let u: f64 = x + z;
    let v: f64 = x - z;

    // x=z
    if (v.abs() <= tiny && u >= 2.0 - tiny) || (v.abs() <= tiny && u <= tiny) {
        return 0.0;
    }

    // intersection region of x=z and x=1-z:
    if v.abs() < 0.99 * tiny && (u - 1.0).abs() < 0.99 * tiny {
        let u0: f64 = 1.0 - tiny;
        let v0: f64 = -tiny;
        let u1: f64 = 1.0 - tiny;
        let v1: f64 = tiny;
        let u2: f64 = 1.0 + tiny;
        let v2: f64 = -tiny;

        let x0: f64 = 0.5 * (u0 + v0);
        let z0: f64 = 0.5 * (u0 - v0);
        let x1: f64 = 0.5 * (u1 + v1);
        let z1: f64 = 0.5 * (u1 - v1);
        let x2: f64 = 0.5 * (u2 + v2);
        let z2: f64 = 0.5 * (u2 - v2);

        let pt0: f64 = RG_RG_000(x0, z0, NF);
        let pt1: f64 = RG_RG_000(x1, z1, NF);
        let pt2: f64 = RG_RG_000(x2, z2, NF);

        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (v - v0) + 0.5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if v.abs() < 0.99 * tiny {
        let v0: f64 = -tiny;
        let v1: f64 = tiny;

        let x0: f64 = 0.5 * (u + v0);
        let z0: f64 = 0.5 * (u - v0);
        let x1: f64 = 0.5 * (u + v1);
        let z1: f64 = 0.5 * (u - v1);

        let pt0: f64 = RG_RG_000(x0, z0, NF);
        let pt1: f64 = RG_RG_000(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (u - 1.0).abs() <= tiny && v <= tiny - 1.0 {
        res = 0.0;
        return res;
    }
    if (u - 1.0).abs() <= tiny && v >= 1.0 - tiny {
        res = 0.0;
        return res;
    }
    if (u - 1.0).abs() < 0.99 * tiny {
        let u0: f64 = 1.0 - tiny;
        let u1: f64 = 1.0 + tiny;

        let x0: f64 = 0.5 * (u0 + v);
        let z0: f64 = 0.5 * (u0 - v);
        let x1: f64 = 0.5 * (u1 + v);
        let z1: f64 = 0.5 * (u1 - v);

        let pt0: f64 = RG_RG_000(x0, z0, NF);
        let pt1: f64 = RG_RG_000(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }

    if z != x && z != 1. - x {
        let tmp: f64 = 2.0 * z * pow(NQCD, -2) + (- 2.0 * z) + (- 4.0 * x * pow(NQCD, -2) * pow(rln2, 2)) + 4.0 * x * pow(rln2, 2) + (- 2.0 * x * z * pow(NQCD, -2)) + 4.0 * x * z * pow(NQCD, -2) * pow(rln2, 2) + 2.0 * x * z + (- 4.0 * x * z * pow(rln2, 2)) + (- 1. / 6. * pow(pi, 2) * x * z * pow(NQCD, -2)) + 1. / 6. * pow(pi, 2) * x * z + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) * rln2 + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * rln2) + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2) * rln2) + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * rln2 + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2)) + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2) + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z) + 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) * rln2 + (- 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * rln2) + (- 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2) * rln2) + 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * rln2 + (- 4.0 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -2)) + 4.0 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) + 4.0 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -2) + (-4.0 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2)) + ln(x) * z * pow(NQCD, -2) + (- ln(x) * z) + (- 2.0 * ln(x) * x * pow(NQCD, -2) * rln2) + 2.0 * ln(x) * x * rln2 + ln(x) * x * z * pow(NQCD, -2) + 2.0 * ln(x) * x * z * pow(NQCD, -2) * rln2 + (- ln(x) * x * z) + (- 2.0 * ln(x) * x * z * rln2) + 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2)) + 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + 2.0 * ln(x) * ln(1.0 + x) * x * pow(NQCD, -2) + (- 2.0 * ln(x) * ln(1.0 + x) * x) + (- 2.0 * ln(x) * ln(1.0 + x * z) * x * pow(NQCD, -2)) + 2.0 * ln(x) * ln(1.0 + x * z) * x + (- 2.0 * ln(x) * ln(z + x) * x * z * pow(NQCD, -2)) + 2.0 * ln(x) * ln(z + x) * x * z + 1. / 2. * pow(ln(x), 2) * x * z * pow(NQCD, -2) + (- 1. / 2. * pow(ln(x), 2) * x * z) + 3.0 * ln(x) * ln(z) * x * z * pow(NQCD, -2) + (- 3.0 * ln(x) * ln(z) * x * z) + ln(z) * z * pow(NQCD, -2) + (- ln(z) * z) + (- 6.0 * ln(z) * x * pow(NQCD, -2) * rln2) + 6.0 * ln(z) * x * rln2 + (- ln(z) * x * z * pow(NQCD, -2)) + 6.0 * ln(z) * x * z * pow(NQCD, -2) * rln2 + ln(z) * x * z + (- 6.0 * ln(z) * x * z * rln2) + 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2)) + 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + 4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + (-4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2)) + 4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + (- 2.0 * ln(z) * ln(1.0 + x * z) * x * pow(NQCD, -2)) + 2.0 * ln(z) * ln(1.0 + x * z) * x + 2.0 * ln(z) * ln(z + x) * x * z * pow(NQCD, -2) + (- 2.0 * ln(z) * ln(z + x) * x * z) + (- 3. / 2. * pow(ln(z), 2) * x * pow(NQCD, -2)) + 3. / 2. * pow(ln(z), 2) * x + 1. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, -2) + (- 1. / 2. * pow(ln(z), 2) * x * z) + 4.0 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -2) + (- 4.0 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2)) + (- 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * pow(NQCD, -2)) + 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x + 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z * pow(NQCD, -2) + (- 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z) + 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * pow(NQCD, -2) + (- 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x) + (- 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z * pow(NQCD, -2)) + 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) + (- 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + (-2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2)) + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2)) + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, -2) + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z) + (- 2.0 * Li2(-x * pow(z, -1)) * x * z * pow(NQCD, -2)) + 2.0 * Li2(-x * pow(z, -1)) * x * z + 2.0 * Li2(-x) * x * pow(NQCD, -2) + (- 2.0 * Li2(-x) * x) + (- 2.0 * Li2(-x * z) * x * pow(NQCD, -2)) + 2.0 * Li2(-x * z) * x + (- 2.0 * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -2)) + 2.0 * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) + 2.0 * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -2) + (- 2.0 * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2)) + (- 4.0 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -2)) + 4.0 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) + (- 2.0 / (1.0 - z) * ln(x) * ln(1.0 + x) * x * pow(NQCD, -2)) + 2.0 / (1.0 - z) * ln(x) * ln(1.0 + x) * x + 1.0 / (1.0 - z) * ln(x) * ln(1.0 + x * z) * x * pow(NQCD, -2) + (- 1.0 / (1.0 - z) * ln(x) * ln(1.0 + x * z) * x) + 1.0 / (1.0 - z) * ln(x) * ln(z + x) * x * pow(NQCD, -2) + (- 1.0 / (1.0 - z) * ln(x) * ln(z + x) * x) + (- 1.0 / (1.0 - z) * ln(x) * ln(z) * x * pow(NQCD, -2)) + 1.0 / (1.0 - z) * ln(x) * ln(z) * x + 1.0 / (1.0 - z) * ln(z) * ln(1.0 + x * z) * x * pow(NQCD, -2) + (-1.0 / (1.0 - z) * ln(z) * ln(1.0 + x * z) * x) + (- 1.0 / (1.0 - z) * ln(z) * ln(z + x) * x * pow(NQCD, -2)) + 1.0 / (1.0 - z) * ln(z) * ln(z + x) * x + 1. / 2. / (1.0 - z) * pow(ln(z), 2) * x * pow(NQCD, -2) + (- 1. / 2. / (1.0 - z) * pow(ln(z), 2) * x) + 1.0 / (1.0 - z) * Li2(-x * pow(z, -1)) * x * pow(NQCD, -2) + (- 1.0 / (1.0 - z) * Li2(-x * pow(z, -1)) * x) + (- 2.0 / (1.0 - z) * Li2(-x) * x * pow(NQCD, -2)) + 2.0 / (1.0 - z) * Li2(-x) * x + 1.0 / (1.0 - z) * Li2(-x * z) * x * pow(NQCD, -2) + (- 1.0 / (1.0 - z) * Li2(-x * z) * x) + 4.0 / (1.0 + z) * x * pow(NQCD, -2) * pow(rln2, 2) + (- 4.0 / (1.0 + z) * x * pow(rln2, 2)) + (- 4.0 / (1.0 + z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) * rln2) + 4.0 / (1.0 + z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * rln2 + 4.0 / (1.0 + z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) + (- 4.0 / (1.0 + z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + (- 4.0 / (1.0 + z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) * rln2) + 4.0 / (1.0 + z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * rln2 + 2.0 / (1.0 + z) * ln(x) * x * pow(NQCD, -2) * rln2 + (- 2.0 / (1.0 + z) * ln(x) * x * rln2) + (- 2.0 / (1.0 + z) * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2)) + 2.0 / (1.0 + z) * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + 1.0 / (1.0 + z) * ln(x) * ln(1.0 + x * z) * x * pow(NQCD, -2) + (- 1.0 / (1.0 + z) * ln(x) * ln(1.0 + x * z) * x) + (- 1.0 / (1.0 + z) * ln(x) * ln(z + x) * x * pow(NQCD, -2)) + 1.0 / (1.0 + z) * ln(x) * ln(z + x) * x + 1.0 / (1.0 + z) * ln(x) * ln(z) * x * pow(NQCD, -2) + (- 1.0 / (1.0 + z) * ln(x) * ln(z) * x) + 6.0 / (1.0 + z) * ln(z) * x * pow(NQCD, -2) * rln2 + (- 6.0 / (1.0 + z) * ln(z) * x * rln2) + (- 2.0 / (1.0 + z) * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2)) + 2.0 / (1.0 + z) * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + (- 4.0 / (1.0 + z) * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2)) + 4.0 / (1.0 + z) * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + 1.0 / (1.0 + z) * ln(z) * ln(1.0 + x * z) * x * pow(NQCD, -2) + (- 1.0 / (1.0 + z) * ln(z) * ln(1.0 + x * z) * x) + 1.0 / (1.0 + z) * ln(z) * ln(z + x) * x * pow(NQCD, -2) + (- 1.0 / (1.0 + z) * ln(z) * ln(z + x) * x) + 1.0 / (1.0 + z) * pow(ln(z), 2) * x * pow(NQCD, -2) + (- 1.0 / (1.0 + z) * pow(ln(z), 2) * x) + 2.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * pow(NQCD, -2) + (- 2.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x) + (- 2.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * pow(NQCD, -2)) + 2.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x + (- 2.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2)) + 2.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + 2.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, -2) + (- 2.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + (- 1.0 / (1.0 + z) * Li2(-x * pow(z, -1)) * x * pow(NQCD, -2)) + 1.0 / (1.0 + z) * Li2(-x * pow(z, -1)) * x + 1.0 / (1.0 + z) * Li2(-x * z) * x * pow(NQCD, -2) + (- 1.0 / (1.0 + z) * Li2(-x * z) * x);
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _])
);

/*
  SV mapping:
  - 000: RG_RG
*/
