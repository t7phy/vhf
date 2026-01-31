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
        let tmp: f64 = (-pow(NQCD, -1)) + NQCD + 1. / 2. * z * pow(NQCD, -1) + (- 1. / 2. * z * NQCD) + 1. / 2. * pow(z, 2) * pow(NQCD, -1) + (- 1. / 2. * pow(z, 2) * NQCD) + 7. / 4. * x * pow(NQCD, -1) + (- 7. / 4. * x * NQCD) + (- 7. / 4. * x * pow(z, 2) * pow(NQCD, -1)) + 7. / 4. * x * pow(z, 2) * NQCD + (- 1. / 12. * pow(pi, 2) * x * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * x * NQCD + (- 1. / 6. * pow(pi, 2) * x * z * pow(NQCD, -1)) + 1. / 6. * pow(pi, 2) * x * z * NQCD + (- ln(1.0 - z) * x * pow(NQCD, -1)) + ln(1.0 - z) * x * NQCD + 1. / 2. * ln(1.0 - z) * x * z * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - z) * x * z * NQCD) + 1. / 2. * ln(1.0 - z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - z) * x * pow(z, 2) * NQCD) + (- ln(1.0 - x) * x * pow(NQCD, -1)) + ln(1.0 - x) * x * NQCD + 1. / 2. * ln(1.0 - x) * x * z * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - x) * x * z * NQCD) + 1. / 2. * ln(1.0 - x) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - x) * x * pow(z, 2) * NQCD) + 2.0 * ln(x) * x * pow(NQCD, -1) + (- 2.0 * ln(x) * x * NQCD) + (- ln(x) * x * z * pow(NQCD, -1)) + ln(x) * x * z * NQCD + (- ln(x) * x * pow(z, 2) * pow(NQCD, -1)) + ln(x) * x * pow(z, 2) * NQCD + ln(x) * ln(z) * x * pow(NQCD, -1) + (- ln(x) * ln(z) * x * NQCD) + 2.0 * ln(x) * ln(z) * x * z * pow(NQCD, -1) + (- 2.0 * ln(x) * ln(z) * x * z * NQCD) + (- 1. / 2. * ln(z) * pow(NQCD, -1)) + 1. / 2. * ln(z) * NQCD + (- ln(z) * z * pow(NQCD, -1)) + ln(z) * z * NQCD + (- 1. / 2. * ln(z) * x * pow(NQCD, -1)) + 1. / 2. * ln(z) * x * NQCD + 2.0 * ln(z) * x * z * pow(NQCD, -1) + (- 2.0 * ln(z) * x * z * NQCD) + 1. / 2. * ln(z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 2. * ln(z) * x * pow(z, 2) * NQCD) + (-1. / 2. * ln(z) * ln(1.0 - x) * x * pow(NQCD, -1)) + 1. / 2. * ln(z) * ln(1.0 - x) * x * NQCD + (- ln(z) * ln(1.0 - x) * x * z * pow(NQCD, -1)) + ln(z) * ln(1.0 - x) * x * z * NQCD + (- 1. / 2. * pow(ln(z), 2) * x * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * x * NQCD + (- pow(ln(z), 2) * x * z * pow(NQCD, -1)) + pow(ln(z), 2) * x * z * NQCD + 1. / 2. * Li2(z) * x * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * x * NQCD) + Li2(z) * x * z * pow(NQCD, -1) + (- Li2(z) * x * z * NQCD);
        res += tmp;
    }

    return res;
}

fn RG_RG_001(x: f64, z: f64, NF: f64) -> f64 {
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

        let pt0: f64 = RG_RG_001(x0, z0, NF);
        let pt1: f64 = RG_RG_001(x1, z1, NF);
        let pt2: f64 = RG_RG_001(x2, z2, NF);

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

        let pt0: f64 = RG_RG_001(x0, z0, NF);
        let pt1: f64 = RG_RG_001(x1, z1, NF);
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

        let pt0: f64 = RG_RG_001(x0, z0, NF);
        let pt1: f64 = RG_RG_001(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }

    if z != x && z != 1. - x {
        let tmp: f64 = 2.0 * lmua * x * pow(NQCD, -1) + (- 2.0 * lmua * x * NQCD) + (- lmua * x * z * pow(NQCD, -1)) + lmua * x * z * NQCD + (- lmua * x * pow(z, 2) * pow(NQCD, -1)) + lmua * x * pow(z, 2) * NQCD + ln(z) * lmua * x * pow(NQCD, -1) + (- ln(z) * lmua * x * NQCD) + 2.0 * ln(z) * lmua * x * z * pow(NQCD, -1) + (- 2.0 * ln(z) * lmua * x * z * NQCD);
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("001", [RG_RG_001, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _])
);

/*
  SV mapping:
  - 000: RG_RG
    - 001: RG_RG
*/
