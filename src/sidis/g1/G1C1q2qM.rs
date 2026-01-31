use crate::sidis::internal::*;

fn DL_DL_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 4.0 * pow(NQCD, -1) + (- 4.0 * NQCD);
    return res;
}

fn DL_DL_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 3. / 2. * lmua * pow(NQCD, -1) + (- 3. / 2. * lmua * NQCD);
    return res;
}

fn DL_DL_010(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 3. / 2. * lmuf * pow(NQCD, -1) + (- 3. / 2. * lmuf * NQCD);
    return res;
}

fn DL_D0_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 2.0 * lmua * pow(NQCD, -1) + (- 2.0 * lmua * NQCD);
    return res;
}

fn DL_D1_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-pow(NQCD, -1)) + NQCD;
    return res;
}

fn D0_DL_010(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 2.0 * lmuf * pow(NQCD, -1) + (- 2.0 * lmuf * NQCD);
    return res;
}

fn D0_D0_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-pow(NQCD, -1)) + NQCD;
    return res;
}

fn D1_DL_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-pow(NQCD, -1)) + NQCD;
    return res;
}

fn DL_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-1. / 2. * pow(NQCD, -1)) + 1. / 2. * NQCD + 1. / 2. * z * pow(NQCD, -1) + (- 1. / 2. * z * NQCD) + 1. / 2. * ln(1.0 - z) * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - z) * NQCD) + 1. / 2. * ln(1.0 - z) * z * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - z) * z * NQCD) + 1. / 2. * ln(z) * pow(NQCD, -1) + (- 1. / 2. * ln(z) * NQCD) + 1. / 2. * ln(z) * z * pow(NQCD, -1) + (- 1. / 2. * ln(z) * z * NQCD) + (- 1.0 / (1.0 - z) * ln(z) * pow(NQCD, -1)) + 1.0 / (1.0 - z) * ln(z) * NQCD;
    return res;
}

fn DL_RG_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- lmua * pow(NQCD, -1)) + lmua * NQCD + (- lmua * z * pow(NQCD, -1)) + lmua * z * NQCD;
    return res;
}

fn D0_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 1. / 2. * pow(NQCD, -1) + (- 1. / 2. * NQCD) + 1. / 2. * z * pow(NQCD, -1) + (- 1. / 2. * z * NQCD);
    return res;
}

fn RG_DL_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-1. / 2. * pow(NQCD, -1)) + 1. / 2. * NQCD + 1. / 2. * x * pow(NQCD, -1) + (- 1. / 2. * x * NQCD) + 1. / 2. * ln(1.0 - x) * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - x) * NQCD) + 1. / 2. * ln(1.0 - x) * x * pow(NQCD, -1) + (- 1. / 2. * ln(1.0 - x) * x * NQCD) + (- 1. / 2. * ln(x) * pow(NQCD, -1)) + 1. / 2. * ln(x) * NQCD + (- 1. / 2. * ln(x) * x * pow(NQCD, -1)) + 1. / 2. * ln(x) * x * NQCD + 1.0 / (1.0 - x) * ln(x) * pow(NQCD, -1) + (- 1.0 / (1.0 - x) * ln(x) * NQCD);
    return res;
}

fn RG_DL_010(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- lmuf * pow(NQCD, -1)) + lmuf * NQCD + (- lmuf * x * pow(NQCD, -1)) + lmuf * x * NQCD;
    return res;
}

fn RG_D0_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 1. / 2. * pow(NQCD, -1) + (- 1. / 2. * NQCD) + 1. / 2. * x * pow(NQCD, -1) + (- 1. / 2. * x * NQCD);
    return res;
}

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
        let tmp: f64 = (-z * pow(NQCD, -1)) + z * NQCD + (- x * pow(NQCD, -1)) + x * NQCD;
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, RG_D0_000, _, _, _, RG_DL_000, D0_RG_000, D0_D0_000, _, _, _, _, _, _, _, _, _, D1_DL_000, _, _, _, _, _, _, _, _, _, _, _, _, DL_RG_000, _, DL_D1_000, _, _, DL_DL_000]),
    ("001", [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, DL_RG_001, DL_D0_001, _, _, _, DL_DL_001]),
    ("010", [_, _, _, _, _, RG_DL_010, _, _, _, _, _, D0_DL_010, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, DL_DL_010])
);

/*
  SV mapping:
  - 000: D0_D0, D0_RG, D1_DL, DL_D1, DL_DL, DL_RG, RG_D0, RG_DL, RG_RG
    - 001: DL_D0, DL_DL, DL_RG
    - 010: D0_DL, DL_DL, RG_DL
*/
