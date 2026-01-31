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
        let tmp: f64 = 2.0 + pow(z, -1) * pow(NQCD, -2) + (- pow(z, -1)) + (- 2.0 * pow(NQCD, -2)) + 3. / 2. * z * pow(NQCD, -2) + (- 3. / 2. * z) + (- 7. / 8. * x * pow(z, -1) * pow(NQCD, -2)) + 7. / 8. * x * pow(z, -1) + 7. / 4. * x * pow(NQCD, -2) + (- 7. / 4. * x) + (- 11. / 8. * x * z * pow(NQCD, -2)) + 11. / 8. * x * z + (- 1. / 24. * pow(pi, 2) * pow(z, -1) * pow(NQCD, -2)) + 1. / 24. * pow(pi, 2) * pow(z, -1) + 1. / 12. * pow(pi, 2) * pow(NQCD, -2) + (- 1. / 12. * pow(pi, 2)) + (- 1. / 24. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2)) + 1. / 24. * pow(pi, 2) * x * pow(z, -1) + 1. / 12. * pow(pi, 2) * x * pow(NQCD, -2) + (- 1. / 12. * pow(pi, 2) * x) + (- 1. / 12. * pow(pi, 2) * x * z * pow(NQCD, -2)) + 1. / 12. * pow(pi, 2) * x * z + 1. / 2. * ln(x) + 1. / 4. * ln(x) * pow(z, -1) * pow(NQCD, -2) + (- 1. / 4. * ln(x) * pow(z, -1)) + (- 1. / 2. * ln(x) * pow(NQCD, -2)) + 1. / 2. * ln(x) * z * pow(NQCD, -2) + (- 1. / 2. * ln(x) * z) + 1. / 4. * ln(x) * x * pow(z, -1) * pow(NQCD, -2) + (- 1. / 4. * ln(x) * x * pow(z, -1)) + (- 1. / 2. * ln(x) * x * pow(NQCD, -2)) + 1. / 2. * ln(x) * x + 1. / 2. * ln(x) * x * z * pow(NQCD, -2) + (- 1. / 2. * ln(x) * x * z) + 1. / 2. * ln(x) * ln(1.0 - x) + 1. / 4. * ln(x) * ln(1.0 - x) * pow(z, -1) * pow(NQCD, -2) + (- 1. / 4. * ln(x) * ln(1.0 - x) * pow(z, -1)) + (- 1. / 2. * ln(x) * ln(1.0 - x) * pow(NQCD, -2)) + 1. / 4. * ln(x) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + (- 1. / 4. * ln(x) * ln(1.0 - x) * x * pow(z, -1)) + (- 1. / 2. * ln(x) * ln(1.0 - x) * x * pow(NQCD, -2)) + 1. / 2. * ln(x) * ln(1.0 - x) * x + 1. / 2. * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, -2) + (- 1. / 2. * ln(x) * ln(1.0 - x) * x * z) + (- 1. / 4. * pow(ln(x), 2)) + (- 1. / 8. * pow(ln(x), 2) * pow(z, -1) * pow(NQCD, -2)) + 1. / 8. * pow(ln(x), 2) * pow(z, -1) + 1. / 4. * pow(ln(x), 2) * pow(NQCD, -2) + (- 1. / 8. * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2)) + 1. / 8. * pow(ln(x), 2) * x * pow(z, -1) + 1. / 4. * pow(ln(x), 2) * x * pow(NQCD, -2) + (- 1. / 4. * pow(ln(x), 2) * x) + (- 1. / 4. * pow(ln(x), 2) * x * z * pow(NQCD, -2)) + 1. / 4. * pow(ln(x), 2) * x * z + 1. / 2. * Li2(x) + 1. / 4. * Li2(x) * pow(z, -1) * pow(NQCD, -2) + (- 1. / 4. * Li2(x) * pow(z, -1)) + (- 1. / 2. * Li2(x) * pow(NQCD, -2)) + 1. / 4. * Li2(x) * x * pow(z, -1) * pow(NQCD, -2) + (- 1. / 4. * Li2(x) * x * pow(z, -1)) + (- 1. / 2. * Li2(x) * x * pow(NQCD, -2)) + 1. / 2. * Li2(x) * x + 1. / 2. * Li2(x) * x * z * pow(NQCD, -2) + (- 1. / 2. * Li2(x) * x * z) + 1. / 12. / (1.0 - x) * pow(pi, 2) * pow(z, -1) * pow(NQCD, -2) + (- 1. / 12. / (1.0 - x) * pow(pi, 2) * pow(z, -1)) + (- 1. / 6. / (1.0 - x) * pow(pi, 2) * pow(NQCD, -2)) + 1. / 6. / (1.0 - x) * pow(pi, 2) + 1. / 12. / (1.0 - x) * pow(pi, 2) * z * pow(NQCD, -2) + (- 1. / 12. / (1.0 - x) * pow(pi, 2) * z) + 3. / 4. / (1.0 - x) * ln(x) + 3. / 8. / (1.0 - x) * ln(x) * pow(z, -1) * pow(NQCD, -2) + (- 3. / 8. / (1.0 - x) * ln(x) * pow(z, -1)) + (- 3. / 4. / (1.0 - x) * ln(x) * pow(NQCD, -2)) + 3. / 8. / (1.0 - x) * ln(x) * z * pow(NQCD, -2) + (- 3. / 8. / (1.0 - x) * ln(x) * z) + (- 1.0 / (1.0 - x) * ln(x) * ln(1.0 - x)) + (- 1. / 2. / (1.0 - x) * ln(x) * ln(1.0 - x) * pow(z, -1) * pow(NQCD, -2)) + 1. / 2. / (1.0 - x) * ln(x) * ln(1.0 - x) * pow(z, -1) + 1.0 / (1.0 - x) * ln(x) * ln(1.0 - x) * pow(NQCD, -2) + (- 1. / 2. / (1.0 - x) * ln(x) * ln(1.0 - x) * z * pow(NQCD, -2)) + 1. / 2. / (1.0 - x) * ln(x) * ln(1.0 - x) * z + 1. / 2. / (1.0 - x) * pow(ln(x), 2) + 1. / 4. / (1.0 - x) * pow(ln(x), 2) * pow(z, -1) * pow(NQCD, -2) + (- 1. / 4. / (1.0 - x) * pow(ln(x), 2) * pow(z, -1)) + (- 1. / 2. / (1.0 - x) * pow(ln(x), 2) * pow(NQCD, -2)) + 1. / 4. / (1.0 - x) * pow(ln(x), 2) * z * pow(NQCD, -2) + (- 1. / 4. / (1.0 - x) * pow(ln(x), 2) * z) + (- 1.0 / (1.0 - x) * Li2(x)) + (- 1. / 2. / (1.0 - x) * Li2(x) * pow(z, -1) * pow(NQCD, -2)) + 1. / 2. / (1.0 - x) * Li2(x) * pow(z, -1) + 1.0 / (1.0 - x) * Li2(x) * pow(NQCD, -2) + (- 1. / 2. / (1.0 - x) * Li2(x) * z * pow(NQCD, -2)) + 1. / 2. / (1.0 - x) * Li2(x) * z;
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
