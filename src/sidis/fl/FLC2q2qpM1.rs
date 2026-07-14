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
        let tmp: f64 = 2.0 * (1.0 / NQCD) + (- 2.0 * NQCD) + (- z * (1.0 / NQCD)) + z * NQCD + (- (z * z) * (1.0 / NQCD)) + (z * z) * NQCD + (- 7. / 2. * x * (1.0 / NQCD)) + 7. / 2. * x * NQCD + 7. / 2. * x * (z * z) * (1.0 / NQCD) + (- 7. / 2. * x * (z * z) * NQCD) + 1. / 6. * (pi * pi) * x * (1.0 / NQCD) + (- 1. / 6. * (pi * pi) * x * NQCD) + 1. / 3. * (pi * pi) * x * z * (1.0 / NQCD) + (- 1. / 3. * (pi * pi) * x * z * NQCD) + 2.0 * ln(1.0 - z) * x * (1.0 / NQCD) + (- 2.0 * ln(1.0 - z) * x * NQCD) + (- ln(1.0 - z) * x * z * (1.0 / NQCD)) + ln(1.0 - z) * x * z * NQCD + (- ln(1.0 - z) * x * (z * z) * (1.0 / NQCD)) + ln(1.0 - z) * x * (z * z) * NQCD + 2.0 * ln(1.0 - x) * x * (1.0 / NQCD) + (- 2.0 * ln(1.0 - x) * x * NQCD) + (- ln(1.0 - x) * x * z * (1.0 / NQCD)) + ln(1.0 - x) * x * z * NQCD + (- ln(1.0 - x) * x * (z * z) * (1.0 / NQCD)) + ln(1.0 - x) * x * (z * z) * NQCD + (- 4.0 * ln(x) * x * (1.0 / NQCD)) + 4.0 * ln(x) * x * NQCD + 2.0 * ln(x) * x * z * (1.0 / NQCD) + (- 2.0 * ln(x) * x * z * NQCD) + 2.0 * ln(x) * x * (z * z) * (1.0 / NQCD) + (- 2.0 * ln(x) * x * (z * z) * NQCD) + (- 2.0 * ln(x) * ln(z) * x * (1.0 / NQCD)) + 2.0 * ln(x) * ln(z) * x * NQCD + (- 4.0 * ln(x) * ln(z) * x * z * (1.0 / NQCD)) + 4.0 * ln(x) * ln(z) * x * z * NQCD + ln(z) * (1.0 / NQCD) + (- ln(z) * NQCD) + 2.0 * ln(z) * z * (1.0 / NQCD) + (- 2.0 * ln(z) * z * NQCD) + ln(z) * x * (1.0 / NQCD) + (- ln(z) * x * NQCD) + (- 4.0 * ln(z) * x * z * (1.0 / NQCD)) + 4.0 * ln(z) * x * z * NQCD + (- ln(z) * x * (z * z) * (1.0 / NQCD)) + ln(z) * x * (z * z) * NQCD + ln(z) * ln(1.0 - x) * x * (1.0 / NQCD) + (- ln(z) * ln(1.0 - x) * x * NQCD) + 2.0 * ln(z) * ln(1.0 - x) * x * z * (1.0 / NQCD) + (- 2.0 * ln(z) * ln(1.0 - x) * x * z * NQCD) + pow(ln(z), 2) * x * (1.0 / NQCD) + (- pow(ln(z), 2) * x * NQCD) + 2.0 * pow(ln(z), 2) * x * z * (1.0 / NQCD) + (- 2.0 * pow(ln(z), 2) * x * z * NQCD) + (- Li2(z) * x * (1.0 / NQCD)) + Li2(z) * x * NQCD + (- 2.0 * Li2(z) * x * z * (1.0 / NQCD)) + 2.0 * Li2(z) * x * z * NQCD;
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
        let tmp: f64 = (- 4.0 * lmua * x * (1.0 / NQCD)) + 4.0 * lmua * x * NQCD + 2.0 * lmua * x * z * (1.0 / NQCD) + (- 2.0 * lmua * x * z * NQCD) + 2.0 * lmua * x * (z * z) * (1.0 / NQCD) + (- 2.0 * lmua * x * (z * z) * NQCD) + (- 2.0 * ln(z) * lmua * x * (1.0 / NQCD)) + 2.0 * ln(z) * lmua * x * NQCD + (- 4.0 * ln(z) * lmua * x * z * (1.0 / NQCD)) + 4.0 * ln(z) * lmua * x * z * NQCD;
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
