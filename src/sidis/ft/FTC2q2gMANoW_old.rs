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
        let tmp: f64 = pow(NQCD, -1) + (- NQCD) + (- z * pow(NQCD, -1)) + z * NQCD + 2.0 * pow(z, 2) * pow(NQCD, -1) + (- 2.0 * pow(z, 2) * NQCD) + ln(1.0 - z) * pow(NQCD, -1) + (- ln(1.0 - z) * NQCD) + (- 2.0 * ln(1.0 - z) * z * pow(NQCD, -1)) + 2.0 * ln(1.0 - z) * z * NQCD + 2.0 * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -1) + (- 2.0 * ln(1.0 - z) * pow(z, 2) * NQCD) + (- ln(x) * pow(NQCD, -1)) + ln(x) * NQCD + 2.0 * ln(x) * z * pow(NQCD, -1) + (- 2.0 * ln(x) * z * NQCD) + (- 2.0 * ln(x) * pow(z, 2) * pow(NQCD, -1)) + 2.0 * ln(x) * pow(z, 2) * NQCD + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(NQCD, -1) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * NQCD) + (- 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * z * pow(NQCD, -1)) + 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * z * NQCD + 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -1) + (- 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 2) * NQCD) + (- 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 3) * pow(NQCD, -1)) + 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 3) * NQCD + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 4) * pow(NQCD, -1) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 4) * NQCD) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(NQCD, -1)) + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * NQCD + 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * z * pow(NQCD, -1) + (- 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * z * NQCD) + (-6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * pow(NQCD, -1)) + 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * NQCD + 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) * pow(NQCD, -1) + (- 5.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) * NQCD) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 4) * pow(NQCD, -1)) + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 4) * NQCD + (- 2.0 / (1.0 - z - x) * pow(NQCD, -1)) + 2.0 / (1.0 - z - x) * NQCD + 3.0 / (1.0 - z - x) * z * pow(NQCD, -1) + (- 3.0 / (1.0 - z - x) * z * NQCD) + (- 3.0 / (1.0 - z - x) * pow(z, 2) * pow(NQCD, -1)) + 3.0 / (1.0 - z - x) * pow(z, 2) * NQCD + 2.0 / (1.0 - z - x) * pow(z, 3) * pow(NQCD, -1) + (- 2.0 / (1.0 - z - x) * pow(z, 3) * NQCD) + (- 3.0 / (1.0 - z - x) * ln(1.0 - z) * pow(NQCD, -1)) + 3.0 / (1.0 - z - x) * ln(1.0 - z) * NQCD + 6.0 / (1.0 - z - x) * ln(1.0 - z) * z * pow(NQCD, -1) + (- 6.0 / (1.0 - z - x) * ln(1.0 - z) * z * NQCD) + (- 7.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -1)) + 7.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 2) * NQCD + 4.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 3) * pow(NQCD, -1) + (- 4.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 3) * NQCD) + 3.0 / (1.0 - z - x) * ln(x) * pow(NQCD, -1) + (- 3.0 / (1.0 - z - x) * ln(x) * NQCD) + (- 6.0 / (1.0 - z - x) * ln(x) * z * pow(NQCD, -1)) + 6.0 / (1.0 - z - x) * ln(x) * z * NQCD + 7.0 / (1.0 - z - x) * ln(x) * pow(z, 2) * pow(NQCD, -1) + (- 7.0 / (1.0 - z - x) * ln(x) * pow(z, 2) * NQCD) + (- 4.0 / (1.0 - z - x) * ln(x) * pow(z, 3) * pow(NQCD, -1)) + 4.0 / (1.0 - z - x) * ln(x) * pow(z, 3) * NQCD;
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
