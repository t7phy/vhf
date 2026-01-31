use crate::sidis::internal::*;

fn DL_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-107. / 108. * pow(z, -1) * CF) + (- 11. / 9. * CF) + (- 4. / 9. * z * CF) + 287. / 108. * pow(z, 2) * CF + 2.0 * zeta3 * CF + 2.0 * zeta3 * z * CF + (- 1. / 6. * pow(pi, 2) * CF) + (- 1. / 4. * pow(pi, 2) * z * CF) + (- 7. / 18. * ln(1.0 - z) * pow(z, -1) * CF) + (- 10. / 3. * ln(1.0 - z) * CF) + 7. / 3. * ln(1.0 - z) * z * CF + 25. / 18. * ln(1.0 - z) * pow(z, 2) * CF + 1. / 3. * ln(1.0 - z) * pow(pi, 2) * CF + 1. / 3. * ln(1.0 - z) * pow(pi, 2) * z * CF + 1. / 3. * pow(ln(1.0 - z), 2) * pow(z, -1) * CF + 1. / 4. * pow(ln(1.0 - z), 2) * CF + (- 1. / 4. * pow(ln(1.0 - z), 2) * z * CF) + (- 1. / 3. * pow(ln(1.0 - z), 2) * pow(z, 2) * CF) + (- ln(1.0 - z) * Li2(1.0 - z) * CF) + (- ln(1.0 - z) * Li2(1.0 - z) * z * CF) + (- 2.0 * ln(1.0 - z) * Li2(z) * CF) + (- 2.0 * ln(1.0 - z) * Li2(z) * z * CF) + (- 7. / 18. * ln(z) * pow(z, -1) * CF) + (- 5.0 * ln(z) * CF) + (- 9. / 2. * ln(z) * z * CF) + (- 31. / 18. * ln(z) * pow(z, 2) * CF) + 1. / 6. * ln(z) * pow(pi, 2) * CF + 1. / 6. * ln(z) * pow(pi, 2) * z * CF + (- 3. / 2. * ln(z) * pow(ln(1.0 - z), 2) * CF) + (- 3. / 2. * ln(z) * pow(ln(1.0 - z), 2) * z * CF) +  1. / 3. * pow(ln(z), 2) * pow(z, -1) * CF + (- 1. / 8. * pow(ln(z), 2) * CF) + (- 5. / 8. * pow(ln(z), 2) * z * CF) + 5. / 12. * pow(ln(z), 3) * CF + 5. / 12. * pow(ln(z), 3) * z * CF + (- Li3(1.0 - z) * CF) + (- Li3(1.0 - z) * z * CF) + (- 2.0 * Li3(z) * CF) + (- 2.0 * Li3(z) * z * CF) + (- 2. / 3. * Li2(z) * pow(z, -1) * CF) + 1. / 2. * Li2(z) * CF + 2.0 * Li2(z) * z * CF + 2. / 3. * Li2(z) * pow(z, 2) * CF;
    return res;
}

fn DL_RG_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 7. / 9. * lmua * pow(z, -1) * CF + 20. / 3. * lmua * CF + (- 14. / 3. * lmua * z * CF) + (- 25. / 9. * lmua * pow(z, 2) * CF) + (- 1. / 3. * lmua * pow(pi, 2) * CF) + (- 1. / 3. * lmua * pow(pi, 2) * z * CF) + (- 4. / 3. * lmua * ln(1.0 - z) * pow(z, -1) * CF) + (- lmua * ln(1.0 - z) * CF) + lmua * ln(1.0 - z) * z * CF + 4. / 3. * lmua * ln(1.0 - z) * pow(z, 2) * CF + 2.0 * lmua * Li2(z) * CF + 2.0 * lmua * Li2(z) * z * CF + (- 4. / 3. * ln(z) * lmua * pow(z, -1) * CF) + ln(z) * lmua * CF + 4.0 * ln(z) * lmua * z * CF + 4. / 3. * ln(z) * lmua * pow(z, 2) * CF + (- 2.0 * pow(ln(z), 2) * lmua * CF) + (- 2.0 * pow(ln(z), 2) * lmua * z * CF);
    return res;
}

fn DL_RG_002(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 4. / 3. * pow(lmua, 2) * pow(z, -1) * CF + pow(lmua, 2) * CF + (- pow(lmua, 2) * z * CF) + (- 4. / 3. * pow(lmua, 2) * pow(z, 2) * CF) + 2.0 * ln(z) * pow(lmua, 2) * CF + 2.0 * ln(z) * pow(lmua, 2) * z * CF;
    return res;
}

fn D0_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-7. / 18. * pow(z, -1) * CF) + (- 10. / 3. * CF) + 7. / 3. * z * CF + 25. / 18. * pow(z, 2) * CF + 1. / 6. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * z * CF + 2. / 3. * ln(1.0 - z) * pow(z, -1) * CF + 1. / 2. * ln(1.0 - z) * CF + (- 1. / 2. * ln(1.0 - z) * z * CF) + (- 2. / 3. * ln(1.0 - z) * pow(z, 2) * CF) + 2. / 3. * ln(z) * pow(z, -1) * CF + (- 1. / 2. * ln(z) * CF) + (- 2.0 * ln(z) * z * CF) + (- 2. / 3. * ln(z) * pow(z, 2) * CF) + pow(ln(z), 2) * CF + pow(ln(z), 2) * z * CF + (- Li2(z) * CF) + (- Li2(z) * z * CF);
    return res;
}

fn D0_RG_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- 4. / 3. * lmua * pow(z, -1) * CF) + (- lmua * CF) + lmua * z * CF + 4. / 3. * lmua * pow(z, 2) * CF + (- 2.0 * ln(z) * lmua * CF) + (- 2.0 * ln(z) * lmua * z * CF);
    return res;
}

fn D1_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 2. / 3. * pow(z, -1) * CF + 1. / 2. * CF + (- 1. / 2. * z * CF) + (- 2. / 3. * pow(z, 2) * CF) + ln(z) * CF + ln(z) * z * CF;
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
        let tmp: f64 = (-5. / 36. * pow(z, -1) * CF) + 2. / 3. * CF + 37. / 12. * z * CF + (- 65. / 18. * pow(z, 2) * CF) + 19. / 36. * x * pow(z, -1) * CF + 5. / 3. * x * CF + (- 47. / 12. * x * z * CF) + 31. / 18. * x * pow(z, 2) * CF + (- 1. / 6. * pow(pi, 2) * CF) + (- 1. / 3. * pow(pi, 2) * z * CF) + (- 1. / 6. * pow(pi, 2) * x * CF) + (- 1. / 3. * ln(1.0 - z) * pow(z, -1) * CF) + (- 3. / 2. * ln(1.0 - z) * CF) + 1. / 2. * ln(1.0 - z) * z * CF + 4. / 3. * ln(1.0 - z) * pow(z, 2) * CF + (- 1. / 3. * ln(1.0 - z) * x * pow(z, -1) * CF) + (- 1. / 2. * ln(1.0 - z) * x * CF) + 3. / 2. * ln(1.0 - z) * x * z * CF + (- 2. / 3. * ln(1.0 - z) * x * pow(z, 2) * CF) + (- 1. / 3. * ln(1.0 - x) * pow(z, -1) * CF) + (- 3. / 2. * ln(1.0 - x) * CF) + 1. / 2. * ln(1.0 - x) * z * CF + 4. / 3. * ln(1.0 - x) * pow(z, 2) * CF + (- 1. / 3. * ln(1.0 - x) * x * pow(z, -1) * CF) + (- 1. / 2. * ln(1.0 - x) * x * CF) + 3. / 2. * ln(1.0 - x) * x * z * CF + (- 2. / 3. * ln(1.0 - x) * x * pow(z, 2) * CF) + 2. / 3. * ln(x) * pow(z, -1) * CF + 3.0 * ln(x) * CF + (- ln(x) * z * CF) + (- 8. / 3. * ln(x) * pow(z, 2) * CF) + 2. / 3. * ln(x) * x * pow(z, -1) * CF + ln(x) * x * CF + (- 3.0 * ln(x) * x * z * CF) + 4. / 3. * ln(x) * x * pow(z, 2) * CF + 2.0 * ln(x) * ln(z) * CF + 4.0 * ln(x) * ln(z) * z * CF + 2.0 * ln(x) * ln(z) * x * CF + (- 1. / 3. * ln(z) * pow(z, -1) * CF) + (- 5. / 2. * ln(z) * CF) + 3. / 2. * ln(z) * z * CF + 4. / 3. * ln(z) * pow(z, 2) * CF + (- 1. / 3. * ln(z) * x * pow(z, -1) * CF) + 1. / 2. * ln(z) * x * CF + 3. / 2. * ln(z) * x * z * CF + (- 2. / 3. * ln(z) * x * pow(z, 2) * CF) + (- ln(z) * ln(1.0 - x) * CF) + (- 2.0 * ln(z) * ln(1.0 - x) * z * CF) + (- ln(z) * ln(1.0 - x) * x * CF) + (- pow(ln(z), 2) * CF) + (- 2.0 * pow(ln(z), 2) * z * CF) + (- pow(ln(z), 2) * x * CF) + Li2(z) * CF + 2.0 * Li2(z) * z * CF + Li2(z) * x * CF + (- 4. / 3. / (1.0 - x) * ln(x) * pow(z, -1) * CF) + (- 5. / 2. / (1.0 - x) * ln(x) * CF) + 5. / 2. / (1.0 - x) * ln(x) * z * CF + 4. / 3. / (1.0 - x) * ln(x) * pow(z, 2) * CF + (- 3.0 / (1.0 - x) * ln(x) * ln(z) * CF) + (- 3.0 / (1.0 - x) * ln(x) * ln(z) * z * CF);
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
        let tmp: f64 = 2. / 3. * lmua * pow(z, -1) * CF + 3.0 * lmua * CF + (- lmua * z * CF) + (- 8. / 3. * lmua * pow(z, 2) * CF) + 2. / 3. * lmua * x * pow(z, -1) * CF + lmua * x * CF + (- 3.0 * lmua * x * z * CF) + 4. / 3. * lmua * x * pow(z, 2) * CF + 2.0 * ln(z) * lmua * CF + 4.0 * ln(z) * lmua * z * CF + 2.0 * ln(z) * lmua * x * CF;
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, _, _, _, _, _, D0_RG_000, _, _, _, _, _, D1_RG_000, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, DL_RG_000, _, _, _, _, _]),
    ("001", [RG_RG_001, _, _, _, _, _, D0_RG_001, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, DL_RG_001, _, _, _, _, _]),
    ("002", [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, DL_RG_002, _, _, _, _, _])
);

/*
  SV mapping:
  - 000: D0_RG, D1_RG, DL_RG, RG_RG
    - 001: D0_RG, DL_RG, RG_RG
    - 002: DL_RG
*/
