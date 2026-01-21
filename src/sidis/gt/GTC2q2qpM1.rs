use crate::sidis::internal::*;

pub fn DL_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-107. / 432. * pow(z, -1) * pow(NQCD, -1)) + 107. / 432. * pow(z, -1) * NQCD + (- 11. / 36. * pow(NQCD, -1)) + 11. / 36. * NQCD + (- 1. / 9. * z * pow(NQCD, -1)) + 1. / 9. * z * NQCD + 287. / 432. * pow(z, 2) * pow(NQCD, -1) + (- 287. / 432. * pow(z, 2) * NQCD) + 1. / 2. * zeta3 * pow(NQCD, -1) + (- 1. / 2. * zeta3 * NQCD) + 1. / 2. * zeta3 * z * pow(NQCD, -1) + (- 1. / 2. * zeta3 * z * NQCD) + (- 1. / 24. * pow(pi, 2) * pow(NQCD, -1)) + 1. / 24. * pow(pi, 2) * NQCD + (- 1. / 16. * pow(pi, 2) * z * pow(NQCD, -1)) + 1. / 16. * pow(pi, 2) * z * NQCD + (- 7. / 72. * ln(1.0 - z) * pow(z, -1) * pow(NQCD, -1)) + 7. / 72. * ln(1.0 - z) * pow(z, -1) * NQCD + (- 5. / 6. * ln(1.0 - z) * pow(NQCD, -1)) + 5. / 6. * ln(1.0 - z) * NQCD + 7. / 12. * ln(1.0 - z) * z * pow(NQCD, -1) + (- 7. / 12. * ln(1.0 - z) * z * NQCD) + 25. / 72. * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -1) + (- 25. / 72. * ln(1.0 - z) * pow(z, 2) * NQCD) + 1. / 12. * ln(1.0 - z) * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 12. * ln(1.0 - z) * pow(pi, 2) * NQCD) + 1. / 12. * ln(1.0 - z) * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 12. * ln(1.0 - z) * pow(pi, 2) * z * NQCD) + 1. / 12. * pow(ln(1.0 - z), 2) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 12. * pow(ln(1.0 - z), 2) * pow(z, -1) * NQCD) + 1. / 16. * pow(ln(1.0 - z), 2) * pow(NQCD, -1) + (- 1. / 16. * pow(ln(1.0 - z), 2) * NQCD) + (- 1. / 16. * pow(ln(1.0 - z), 2) * z * pow(NQCD, -1)) + 1. / 16. * pow(ln(1.0 - z), 2) * z * NQCD + (- 1. / 12. * pow(ln(1.0 - z), 2) * pow(z, 2) * pow(NQCD, -1)) + 1. / 12. * pow(ln(1.0 - z), 2) * pow(z, 2) * NQCD + (- 1. / 4. * ln(1.0 - z) * Li2(1.0 - z) * pow(NQCD, -1)) + 1. / 4. * ln(1.0 - z) * Li2(1.0 - z) * NQCD + (- 1. / 4. * ln(1.0 - z) * Li2(1.0 - z) * z * pow(NQCD, -1)) + 1. / 4. * ln(1.0 - z) * Li2(1.0 - z) * z * NQCD + (- 1. / 2. * ln(1.0 - z) * Li2(z) * pow(NQCD, -1)) + 1. / 2. * ln(1.0 - z) * Li2(z) * NQCD + (- 1. / 2. * ln(1.0 - z) * Li2(z) * z * pow(NQCD, -1)) +  1. / 2. * ln(1.0 - z) * Li2(z) * z * NQCD +  (- 7. / 72. * ln(z) * pow(z, -1) * pow(NQCD, -1)) + 7. / 72. * ln(z) * pow(z, -1) * NQCD + (- 5. / 4. * ln(z) * pow(NQCD, -1)) + 5. / 4. * ln(z) * NQCD + (- 9. / 8. * ln(z) * z * pow(NQCD, -1)) + 9. / 8. * ln(z) * z * NQCD + (- 31. / 72. * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 31. / 72. * ln(z) * pow(z, 2) * NQCD + 1. / 24. * ln(z) * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 24. * ln(z) * pow(pi, 2) * NQCD) + 1. / 24. * ln(z) * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 24. * ln(z) * pow(pi, 2) * z * NQCD) + (- 3. / 8. * ln(z) * pow(ln(1.0 - z), 2) * pow(NQCD, -1)) + 3. / 8. * ln(z) * pow(ln(1.0 - z), 2) * NQCD + (- 3. / 8. * ln(z) * pow(ln(1.0 - z), 2) * z * pow(NQCD, -1)) + 3. / 8. * ln(z) * pow(ln(1.0 - z), 2) * z * NQCD + 1. / 12. * pow(ln(z), 2) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 12. * pow(ln(z), 2) * pow(z, -1) * NQCD) + (- 1. / 32. * pow(ln(z), 2) * pow(NQCD, -1)) + 1. / 32. * pow(ln(z), 2) * NQCD + (- 5. / 32. * pow(ln(z), 2) * z * pow(NQCD, -1)) + 5. / 32. * pow(ln(z), 2) * z * NQCD +  5. / 48. * pow(ln(z), 3) * pow(NQCD, -1) + (- 5. / 48. * pow(ln(z), 3) * NQCD) + 5. / 48. * pow(ln(z), 3) * z * pow(NQCD, -1) + (- 5. / 48. * pow(ln(z), 3) * z * NQCD) + (- 1. / 4. * Li3(1.0 - z) * pow(NQCD, -1)) + 1. / 4. * Li3(1.0 - z) * NQCD + (- 1. / 4. * Li3(1.0 - z) * z * pow(NQCD, -1)) + 1. / 4. * Li3(1.0 - z) * z * NQCD + (- 1. / 2. * Li3(z) * pow(NQCD, -1)) + 1. / 2. * Li3(z) * NQCD + (- 1. / 2. * Li3(z) * z * pow(NQCD, -1)) + 1. / 2. * Li3(z) * z * NQCD + (- 1. / 6. * Li2(z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 6. * Li2(z) * pow(z, -1) * NQCD + 1. / 8. * Li2(z) * pow(NQCD, -1) + (- 1. / 8. * Li2(z) * NQCD) + 1. / 2. * Li2(z) * z * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * z * NQCD) + 1. / 6. * Li2(z) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 6. * Li2(z) * pow(z, 2) * NQCD);
    return res;
}

pub fn DL_RG_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 7. / 36. * lmua * pow(z, -1) * pow(NQCD, -1) + (- 7. / 36. * lmua * pow(z, -1) * NQCD) + 5. / 3. * lmua * pow(NQCD, -1) + (- 5. / 3. * lmua * NQCD) + (- 7. / 6. * lmua * z * pow(NQCD, -1)) + 7. / 6. * lmua * z * NQCD + (- 25. / 36. * lmua * pow(z, 2) * pow(NQCD, -1)) + 25. / 36. * lmua * pow(z, 2) * NQCD + (- 1. / 12. * lmua * pow(pi, 2) * pow(NQCD, -1)) + 1. / 12. * lmua * pow(pi, 2) * NQCD + (- 1. / 12. * lmua * pow(pi, 2) * z * pow(NQCD, -1)) + 1. / 12. * lmua * pow(pi, 2) * z * NQCD + (- 1. / 3. * lmua * ln(1.0 - z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * lmua * ln(1.0 - z) * pow(z, -1) * NQCD + (- 1. / 4. * lmua * ln(1.0 - z) * pow(NQCD, -1)) + 1. / 4. * lmua * ln(1.0 - z) * NQCD + 1. / 4. * lmua * ln(1.0 - z) * z * pow(NQCD, -1) + (- 1. / 4. * lmua * ln(1.0 - z) * z * NQCD) + 1. / 3. * lmua * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * lmua * ln(1.0 - z) * pow(z, 2) * NQCD) + 1. / 2. * lmua * Li2(z) * pow(NQCD, -1) + (- 1. / 2. * lmua * Li2(z) * NQCD) + 1. / 2. * lmua * Li2(z) * z * pow(NQCD, -1) + (- 1. / 2. * lmua * Li2(z) * z * NQCD) + (- 1. / 3. * ln(z) * lmua * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * ln(z) * lmua * pow(z, -1) * NQCD + 1. / 4. * ln(z) * lmua * pow(NQCD, -1) + (- 1. / 4. * ln(z) * lmua * NQCD) + ln(z) * lmua * z * pow(NQCD, -1) + (- ln(z) * lmua * z * NQCD) + 1. / 3. * ln(z) * lmua * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(z) * lmua * pow(z, 2) * NQCD) + (-1. / 2. * pow(ln(z), 2) * lmua * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * lmua * NQCD + (- 1. / 2. * pow(ln(z), 2) * lmua * z * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * lmua * z * NQCD;
    return res;
}

pub fn DL_RG_002(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 1. / 3. * pow(lmua, 2) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 3. * pow(lmua, 2) * pow(z, -1) * NQCD) + 1. / 4. * pow(lmua, 2) * pow(NQCD, -1) + (- 1. / 4. * pow(lmua, 2) * NQCD) + (- 1. / 4. * pow(lmua, 2) * z * pow(NQCD, -1)) + 1. / 4. * pow(lmua, 2) * z * NQCD + (- 1. / 3. * pow(lmua, 2) * pow(z, 2) * pow(NQCD, -1)) + 1. / 3. * pow(lmua, 2) * pow(z, 2) * NQCD + 1. / 2. * ln(z) * pow(lmua, 2) * pow(NQCD, -1) + (- 1. / 2. * ln(z) * pow(lmua, 2) * NQCD) + 1. / 2. * ln(z) * pow(lmua, 2) * z * pow(NQCD, -1) + (- 1. / 2. * ln(z) * pow(lmua, 2) * z * NQCD);
    return res;
}

pub fn D0_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-7. / 72. * pow(z, -1) * pow(NQCD, -1)) + 7. / 72. * pow(z, -1) * NQCD + (- 5. / 6. * pow(NQCD, -1)) + 5. / 6. * NQCD + 7. / 12. * z * pow(NQCD, -1) + (- 7. / 12. * z * NQCD) + 25. / 72. * pow(z, 2) * pow(NQCD, -1) + (- 25. / 72. * pow(z, 2) * NQCD) + 1. / 24. * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 24. * pow(pi, 2) * NQCD) + 1. / 24. * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 24. * pow(pi, 2) * z * NQCD) + 1. / 6. * ln(1.0 - z) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(1.0 - z) * pow(z, -1) * NQCD) + 1. / 8. * ln(1.0 - z) * pow(NQCD, -1) + (- 1. / 8. * ln(1.0 - z) * NQCD) + (- 1. / 8. * ln(1.0 - z) * z * pow(NQCD, -1)) + 1. / 8. * ln(1.0 - z) * z * NQCD + (- 1. / 6. * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1.0 - z) * pow(z, 2) * NQCD + 1. / 6. * ln(z) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(z) * pow(z, -1) * NQCD) + (- 1. / 8. * ln(z) * pow(NQCD, -1)) + 1. / 8. * ln(z) * NQCD + (- 1. / 2. * ln(z) * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * z * NQCD + (- 1. / 6. * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(z) * pow(z, 2) * NQCD + 1. / 4. * pow(ln(z), 2) * pow(NQCD, -1) + (- 1. / 4. * pow(ln(z), 2) * NQCD) + 1. / 4. * pow(ln(z), 2) * z * pow(NQCD, -1) + (- 1. / 4. * pow(ln(z), 2) * z * NQCD) +  (-1. / 4. * Li2(z) * pow(NQCD, -1)) + 1. / 4. * Li2(z) * NQCD + (- 1. / 4. * Li2(z) * z * pow(NQCD, -1)) + 1. / 4. * Li2(z) * z * NQCD;
    return res;
}

pub fn D0_RG_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- 1. / 3. * lmua * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * lmua * pow(z, -1) * NQCD + (- 1. / 4. * lmua * pow(NQCD, -1)) + 1. / 4. * lmua * NQCD + 1. / 4. * lmua * z * pow(NQCD, -1) + (- 1. / 4. * lmua * z * NQCD) + 1. / 3. * lmua * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * lmua * pow(z, 2) * NQCD) + (- 1. / 2. * ln(z) * lmua * pow(NQCD, -1)) + 1. / 2. * ln(z) * lmua * NQCD + (- 1. / 2. * ln(z) * lmua * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * lmua * z * NQCD;
    return res;
}

pub fn D1_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 1. / 6. * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * pow(z, -1) * NQCD) + 1. / 8. * pow(NQCD, -1) + (- 1. / 8. * NQCD) + (- 1. / 8. * z * pow(NQCD, -1)) + 1. / 8. * z * NQCD + (- 1. / 6. * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * pow(z, 2) * NQCD + 1. / 4. * ln(z) * pow(NQCD, -1) + (- 1. / 4. * ln(z) * NQCD) + 1. / 4. * ln(z) * z * pow(NQCD, -1) + (- 1. / 4. * ln(z) * z * NQCD);
    return res;
}

pub fn RG_RG_000(x: f64, z: f64, NF: f64) -> f64 {
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
        let tmp: f64 = (-5. / 144. * pow(z, -1) * pow(NQCD, -1)) + 5. / 144. * pow(z, -1) * NQCD + (- 1. / 12. * pow(NQCD, -1)) + 1. / 12. * NQCD + (- 23. / 48. * z * pow(NQCD, -1)) + 23. / 48. * z * NQCD + 43. / 72. * pow(z, 2) * pow(NQCD, -1) + (- 43. / 72. * pow(z, 2) * NQCD) + 19. / 144. * x * pow(z, -1) * pow(NQCD, -1) + (- 19. / 144. * x * pow(z, -1) * NQCD) + 2. / 3. * x * pow(NQCD, -1) + (- 2. / 3. * x * NQCD) + 13. / 48. * x * z * pow(NQCD, -1) + (- 13. / 48. * x * z * NQCD) + (- 77. / 72. * x * pow(z, 2) * pow(NQCD, -1)) + 77. / 72. * x * pow(z, 2) * NQCD + (- 1. / 24. * pow(pi, 2) * pow(NQCD, -1)) + 1. / 24. * pow(pi, 2) * NQCD + (- 1. / 24. * pow(pi, 2) * x * pow(NQCD, -1)) + 1. / 24. * pow(pi, 2) * x * NQCD + (- 1. / 12. * pow(pi, 2) * x * z * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * x * z * NQCD + (- 1. / 12. * ln(1.0 - z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1.0 - z) * pow(z, -1) * NQCD + (- 1. / 8. * ln(1.0 - z) * pow(NQCD, -1)) + 1. / 8. * ln(1.0 - z) * NQCD + 3. / 8. * ln(1.0 - z) * z * pow(NQCD, -1) + (- 3. / 8. * ln(1.0 - z) * z * NQCD) + (- 1. / 6. * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1.0 - z) * pow(z, 2) * NQCD + (- 1. / 12. * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1.0 - z) * x * pow(z, -1) * NQCD + (- 3. / 8. * ln(1.0 - z) * x * pow(NQCD, -1)) + 3. / 8. * ln(1.0 - z) * x * NQCD + 1. / 8. * ln(1.0 - z) * x * z * pow(NQCD, -1) + (- 1. / 8. * ln(1.0 - z) * x * z * NQCD) + 1. / 3. * ln(1.0 - z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(1.0 - z) * x * pow(z, 2) * NQCD) + (- 1. / 12. * ln(1.0 - x) * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1.0 - x) * pow(z, -1) * NQCD + (- 1. / 8. * ln(1.0 - x) * pow(NQCD, -1)) + 1. / 8. * ln(1.0 - x) * NQCD + 3. / 8. * ln(1.0 - x) * z * pow(NQCD, -1) + (- 3. / 8. * ln(1.0 - x) * z * NQCD) + (- 1. / 6. * ln(1.0 - x) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1.0 - x) * pow(z, 2) * NQCD + (-1. / 12. * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1.0 - x) * x * pow(z, -1) * NQCD + (- 3. / 8. * ln(1.0 - x) * x * pow(NQCD, -1)) + 3. / 8. * ln(1.0 - x) * x * NQCD + 1. / 8. * ln(1.0 - x) * x * z * pow(NQCD, -1) + (- 1. / 8. * ln(1.0 - x) * x * z * NQCD) + 1. / 3. * ln(1.0 - x) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(1.0 - x) * x * pow(z, 2) * NQCD) + 1. / 6. * ln(x) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(x) * pow(z, -1) * NQCD) + 1. / 4. * ln(x) * pow(NQCD, -1) + (- 1. / 4. * ln(x) * NQCD) + (- 3. / 4. * ln(x) * z * pow(NQCD, -1)) + 3. / 4. * ln(x) * z * NQCD + 1. / 3. * ln(x) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(x) * pow(z, 2) * NQCD) + 1. / 6. * ln(x) * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(x) * x * pow(z, -1) * NQCD) + 3. / 4. * ln(x) * x * pow(NQCD, -1) + (- 3. / 4. * ln(x) * x * NQCD) + (- 1. / 4. * ln(x) * x * z * pow(NQCD, -1)) + 1. / 4. * ln(x) * x * z * NQCD + (- 2. / 3. * ln(x) * x * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * ln(x) * x * pow(z, 2) * NQCD + 1. / 2. * ln(x) * ln(z) * pow(NQCD, -1) + (- 1. / 2. * ln(x) * ln(z) * NQCD) + 1. / 2. * ln(x) * ln(z) * x * pow(NQCD, -1) + (- 1. / 2. * ln(x) * ln(z) * x * NQCD) + ln(x) * ln(z) * x * z * pow(NQCD, -1) + (- ln(x) * ln(z) * x * z * NQCD) + (- 1. / 12. * ln(z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(z) * pow(z, -1) * NQCD + (- 3. / 8. * ln(z) * pow(NQCD, -1)) + 3. / 8. * ln(z) * NQCD + (- 1. / 8. * ln(z) * z * pow(NQCD, -1)) + 1. / 8. * ln(z) * z * NQCD + (- 1. / 6. * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(z) * pow(z, 2) * NQCD + (- 1. / 12. * ln(z) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(z) * x * pow(z, -1) * NQCD + (- 1. / 8. * ln(z) * x * pow(NQCD, -1)) + 1. / 8. * ln(z) * x * NQCD + 7. / 8. * ln(z) * x * z * pow(NQCD, -1) + (- 7. / 8. * ln(z) * x * z * NQCD) + 1. / 3. * ln(z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(z) * x * pow(z, 2) * NQCD) + (- 1. / 4. * ln(z) * ln(1.0 - x) * pow(NQCD, -1)) + 1. / 4. * ln(z) * ln(1.0 - x) * NQCD + (- 1. / 4. * ln(z) * ln(1.0 - x) * x * pow(NQCD, -1)) + 1. / 4. * ln(z) * ln(1.0 - x) * x * NQCD + (- 1. / 2. * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * ln(1.0 - x) * x * z * NQCD + (- 1. / 4. * pow(ln(z), 2) * pow(NQCD, -1)) + 1. / 4. * pow(ln(z), 2) * NQCD + (- 1. / 4. * pow(ln(z), 2) * x * pow(NQCD, -1)) + 1. / 4. * pow(ln(z), 2) * x * NQCD + (- 1. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * x * z * NQCD + 1. / 4. * Li2(z) * pow(NQCD, -1) + (- 1. / 4. * Li2(z) * NQCD) + 1. / 4. * Li2(z) * x * pow(NQCD, -1) + (- 1. / 4. * Li2(z) * x * NQCD) + 1. / 2. * Li2(z) * x * z * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * x * z * NQCD) + (- 1. / 3. / (1.0 - x) * ln(x) * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. / (1.0 - x) * ln(x) * pow(z, -1) * NQCD + (- 5. / 8. / (1.0 - x) * ln(x) * pow(NQCD, -1)) + 5. / 8. / (1.0 - x) * ln(x) * NQCD + 5. / 8. / (1.0 - x) * ln(x) * z * pow(NQCD, -1) + (- 5. / 8. / (1.0 - x) * ln(x) * z * NQCD) + 1. / 3. / (1.0 - x) * ln(x) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. / (1.0 - x) * ln(x) * pow(z, 2) * NQCD) + (- 3. / 4. / (1.0 - x) * ln(x) * ln(z) * pow(NQCD, -1)) + 3. / 4. / (1.0 - x) * ln(x) * ln(z) * NQCD + (- 3. / 4. / (1.0 - x) * ln(x) * ln(z) * z * pow(NQCD, -1)) + 3. / 4. / (1.0 - x) * ln(x) * ln(z) * z * NQCD;
        res += tmp;
    }

    return res;
}

pub fn RG_RG_001(x: f64, z: f64, NF: f64) -> f64 {
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
        let tmp: f64 = 1. / 6. * lmua * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * lmua * pow(z, -1) * NQCD) + 1. / 4. * lmua * pow(NQCD, -1) + (- 1. / 4. * lmua * NQCD) + (- 3. / 4. * lmua * z * pow(NQCD, -1)) + 3. / 4. * lmua * z * NQCD + 1. / 3. * lmua * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * lmua * pow(z, 2) * NQCD) + 1. / 6. * lmua * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * lmua * x * pow(z, -1) * NQCD) + 3. / 4. * lmua * x * pow(NQCD, -1) + (- 3. / 4. * lmua * x * NQCD) + (- 1. / 4. * lmua * x * z * pow(NQCD, -1)) + 1. / 4. * lmua * x * z * NQCD + (- 2. / 3. * lmua * x * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * lmua * x * pow(z, 2) * NQCD + 1. / 2. * ln(z) * lmua * pow(NQCD, -1) + (- 1. / 2. * ln(z) * lmua * NQCD) + 1. / 2. * ln(z) * lmua * x * pow(NQCD, -1) + (- 1. / 2. * ln(z) * lmua * x * NQCD) + ln(z) * lmua * x * z * pow(NQCD, -1) + (- ln(z) * lmua * x * z * NQCD);
        res += tmp;
    }

    return res;
}
pub fn get_sv_map() -> HashMap<&'static str, Vec<&'static str>> {
    let mut m = HashMap::new();
    m.insert("000", vec!["D0_RG", "D1_RG", "DL_RG", "RG_RG"]);
    m.insert("001", vec!["D0_RG", "DL_RG", "RG_RG"]);
    m.insert("002", vec!["DL_RG"]);
    m
}