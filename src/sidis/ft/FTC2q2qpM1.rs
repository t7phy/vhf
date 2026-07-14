use crate::sidis::internal::*;

fn DL_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 107. / 216. * (1.0 / z) * (1.0 / NQCD) + (- 107. / 216. * (1.0 / z) * NQCD) + 11. / 18. * (1.0 / NQCD) + (- 11. / 18. * NQCD) + 2. / 9. * z * (1.0 / NQCD) + (- 2. / 9. * z * NQCD) + (- 287. / 216. * (z * z) * (1.0 / NQCD)) + 287. / 216. * (z * z) * NQCD + (- zeta3 * (1.0 / NQCD)) + zeta3 * NQCD + (- zeta3 * z * (1.0 / NQCD)) + zeta3 * z * NQCD + 1. / 12. * (pi * pi) * (1.0 / NQCD) + (- 1. / 12. * (pi * pi) * NQCD) + 1. / 8. * (pi * pi) * z * (1.0 / NQCD) + (- 1. / 8. * (pi * pi) * z * NQCD) + 7. / 36. * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD) + (- 7. / 36. * ln(1.0 - z) * (1.0 / z) * NQCD) + 5. / 3. * ln(1.0 - z) * (1.0 / NQCD) + (- 5. / 3. * ln(1.0 - z) * NQCD) + (- 7. / 6. * ln(1.0 - z) * z * (1.0 / NQCD)) + 7. / 6. * ln(1.0 - z) * z * NQCD + (- 25. / 36. * ln(1.0 - z) * (z * z) * (1.0 / NQCD)) + 25. / 36. * ln(1.0 - z) * (z * z) * NQCD + (- 1. / 6. * ln(1.0 - z) * (pi * pi) * (1.0 / NQCD)) + 1. / 6. * ln(1.0 - z) * (pi * pi) * NQCD + (- 1. / 6. * ln(1.0 - z) * (pi * pi) * z * (1.0 / NQCD)) + 1. / 6. * ln(1.0 - z) * (pi * pi) * z * NQCD + (- 1. / 6. * pow(ln(1.0 - z), 2) * (1.0 / z) * (1.0 / NQCD)) + 1. / 6. * pow(ln(1.0 - z), 2) * (1.0 / z) * NQCD + (- 1. / 8. * pow(ln(1.0 - z), 2) * (1.0 / NQCD)) + 1. / 8. * pow(ln(1.0 - z), 2) * NQCD + 1. / 8. * pow(ln(1.0 - z), 2) * z * (1.0 / NQCD) + (- 1. / 8. * pow(ln(1.0 - z), 2) * z * NQCD) + 1. / 6. * pow(ln(1.0 - z), 2) * (z * z) * (1.0 / NQCD) + (- 1. / 6. * pow(ln(1.0 - z), 2) * (z * z) * NQCD) + 1. / 2. * ln(1.0 - z) * Li2(1.0 - z) * (1.0 / NQCD) + (- 1. / 2. * ln(1.0 - z) * Li2(1.0 - z) * NQCD) + 1. / 2. * ln(1.0 - z) * Li2(1.0 - z) * z * (1.0 / NQCD) + (- 1. / 2. * ln(1.0 - z) * Li2(1.0 - z) * z * NQCD) + ln(1.0 - z) * Li2(z) * (1.0 / NQCD) + (- ln(1.0 - z) * Li2(z) * NQCD) + ln(1.0 - z) * Li2(z) * z * (1.0 / NQCD) + (- ln(1.0 - z) * Li2(z) * z * NQCD) + 7. / 36. * ln(z) * (1.0 / z) * (1.0 / NQCD) + (- 7. / 36. * ln(z) * (1.0 / z) * NQCD) + 5. / 2. * ln(z) * (1.0 / NQCD) + (- 5. / 2. * ln(z) * NQCD) + 9. / 4. * ln(z) * z * (1.0 / NQCD) + (- 9. / 4. * ln(z) * z * NQCD) + 31. / 36. * ln(z) * (z * z) * (1.0 / NQCD) + (- 31. / 36. * ln(z) * (z * z) * NQCD) + (- 1. / 12. * ln(z) * (pi * pi) * (1.0 / NQCD)) + 1. / 12. * ln(z) * (pi * pi) * NQCD + (- 1. / 12. * ln(z) * (pi * pi) * z * (1.0 / NQCD)) + 1. / 12. * ln(z) * (pi * pi) * z * NQCD + 3. / 4. * ln(z) * pow(ln(1.0 - z), 2) * (1.0 / NQCD) + (- 3. / 4. * ln(z) * pow(ln(1.0 - z), 2) * NQCD) + 3. / 4. * ln(z) * pow(ln(1.0 - z), 2) * z * (1.0 / NQCD) + (- 3. / 4. * ln(z) * pow(ln(1.0 - z), 2) * z * NQCD) + (- 1. / 6. * pow(ln(z), 2) * (1.0 / z) * (1.0 / NQCD)) + 1. / 6. * pow(ln(z), 2) * (1.0 / z) * NQCD + 1. / 16. * pow(ln(z), 2) * (1.0 / NQCD) + (- 1. / 16. * pow(ln(z), 2) * NQCD) + 5. / 16. * pow(ln(z), 2) * z * (1.0 / NQCD) + (- 5. / 16. * pow(ln(z), 2) * z * NQCD) +  (- 5. / 24. * pow(ln(z), 3) * (1.0 / NQCD)) + 5. / 24. * pow(ln(z), 3) * NQCD + (- 5. / 24. * pow(ln(z), 3) * z * (1.0 / NQCD)) + 5. / 24. * pow(ln(z), 3) * z * NQCD + 1. / 2. * Li3(1.0 - z) * (1.0 / NQCD) + (- 1. / 2. * Li3(1.0 - z) * NQCD) + 1. / 2. * Li3(1.0 - z) * z * (1.0 / NQCD) + (- 1. / 2. * Li3(1.0 - z) * z * NQCD) + Li3(z) * (1.0 / NQCD) + (- Li3(z) * NQCD) + Li3(z) * z * (1.0 / NQCD) + (- Li3(z) * z * NQCD) + 1. / 3. * Li2(z) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 3. * Li2(z) * (1.0 / z) * NQCD) + (- 1. / 4. * Li2(z) * (1.0 / NQCD)) + 1. / 4. * Li2(z) * NQCD + (- Li2(z) * z * (1.0 / NQCD)) + Li2(z) * z * NQCD + (- 1. / 3. * Li2(z) * (z * z) * (1.0 / NQCD)) + 1. / 3. * Li2(z) * (z * z) * NQCD;
    return res;
}

fn DL_RG_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- 7. / 18. * lmua * (1.0 / z) * (1.0 / NQCD)) + 7. / 18. * lmua * (1.0 / z) * NQCD + (- 10. / 3. * lmua * (1.0 / NQCD)) + 10. / 3. * lmua * NQCD + 7. / 3. * lmua * z * (1.0 / NQCD) + (- 7. / 3. * lmua * z * NQCD) + 25. / 18. * lmua * (z * z) * (1.0 / NQCD) + (- 25. / 18. * lmua * (z * z) * NQCD) + 1. / 6. * lmua * (pi * pi) * (1.0 / NQCD) + (- 1. / 6. * lmua * (pi * pi) * NQCD) + 1. / 6. * lmua * (pi * pi) * z * (1.0 / NQCD) + (- 1. / 6. * lmua * (pi * pi) * z * NQCD) + 2. / 3. * lmua * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD) + (- 2. / 3. * lmua * ln(1.0 - z) * (1.0 / z) * NQCD) + 1. / 2. * lmua * ln(1.0 - z) * (1.0 / NQCD) + (- 1. / 2. * lmua * ln(1.0 - z) * NQCD) + (- 1. / 2. * lmua * ln(1.0 - z) * z * (1.0 / NQCD)) + 1. / 2. * lmua * ln(1.0 - z) * z * NQCD + (- 2. / 3. * lmua * ln(1.0 - z) * (z * z) * (1.0 / NQCD)) + 2. / 3. * lmua * ln(1.0 - z) * (z * z) * NQCD + (- lmua * Li2(z) * (1.0 / NQCD)) + lmua * Li2(z) * NQCD + (- lmua * Li2(z) * z * (1.0 / NQCD)) + lmua * Li2(z) * z * NQCD + 2. / 3. * ln(z) * lmua * (1.0 / z) * (1.0 / NQCD) + (- 2. / 3. * ln(z) * lmua * (1.0 / z) * NQCD) + (- 1. / 2. * ln(z) * lmua * (1.0 / NQCD)) + 1. / 2. * ln(z) * lmua * NQCD + (- 2.0 * ln(z) * lmua * z * (1.0 / NQCD)) + 2.0 * ln(z) * lmua * z * NQCD + (- 2. / 3. * ln(z) * lmua * (z * z) * (1.0 / NQCD)) + 2. / 3. * ln(z) * lmua * (z * z) * NQCD + pow(ln(z), 2) * lmua * (1.0 / NQCD) + (- pow(ln(z), 2) * lmua * NQCD) + pow(ln(z), 2) * lmua * z * (1.0 / NQCD) + (-pow(ln(z), 2) * lmua * z * NQCD);
    return res;
}

fn DL_RG_002(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- 2. / 3. * (lmua * lmua) * (1.0 / z) * (1.0 / NQCD)) + 2. / 3. * (lmua * lmua) * (1.0 / z) * NQCD + (- 1. / 2. * (lmua * lmua) * (1.0 / NQCD)) + 1. / 2. * (lmua * lmua) * NQCD + 1. / 2. * (lmua * lmua) * z * (1.0 / NQCD) + (- 1. / 2. * (lmua * lmua) * z * NQCD) + 2. / 3. * (lmua * lmua) * (z * z) * (1.0 / NQCD) + (- 2. / 3. * (lmua * lmua) * (z * z) * NQCD) + (- ln(z) * (lmua * lmua) * (1.0 / NQCD)) + ln(z) * (lmua * lmua) * NQCD + (- ln(z) * (lmua * lmua) * z * (1.0 / NQCD)) + ln(z) * (lmua * lmua) * z * NQCD;
    return res;
}

fn D0_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 7. / 36. * (1.0 / z) * (1.0 / NQCD) + (- 7. / 36. * (1.0 / z) * NQCD) + 5. / 3. * (1.0 / NQCD) + (- 5. / 3. * NQCD) + (- 7. / 6. * z * (1.0 / NQCD)) + 7. / 6. * z * NQCD + (- 25. / 36. * (z * z) * (1.0 / NQCD)) + 25. / 36. * (z * z) * NQCD + (- 1. / 12. * (pi * pi) * (1.0 / NQCD)) + 1. / 12. * (pi * pi) * NQCD + (- 1. / 12. * (pi * pi) * z * (1.0 / NQCD)) + 1. / 12. * (pi * pi) * z * NQCD + (- 1. / 3. * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD)) + 1. / 3. * ln(1.0 - z) * (1.0 / z) * NQCD + (- 1. / 4. * ln(1.0 - z) * (1.0 / NQCD)) + 1. / 4. * ln(1.0 - z) * NQCD + 1. / 4. * ln(1.0 - z) * z * (1.0 / NQCD) + (- 1. / 4. * ln(1.0 - z) * z * NQCD) + 1. / 3. * ln(1.0 - z) * (z * z) * (1.0 / NQCD) + (- 1. / 3. * ln(1.0 - z) * (z * z) * NQCD) + (- 1. / 3. * ln(z) * (1.0 / z) * (1.0 / NQCD)) + 1. / 3. * ln(z) * (1.0 / z) * NQCD + 1. / 4. * ln(z) * (1.0 / NQCD) + (- 1. / 4. * ln(z) * NQCD) + ln(z) * z * (1.0 / NQCD) + (- ln(z) * z * NQCD) + 1. / 3. * ln(z) * (z * z) * (1.0 / NQCD) + (- 1. / 3. * ln(z) * (z * z) * NQCD) + (- 1. / 2. * pow(ln(z), 2) * (1.0 / NQCD)) + 1. / 2. * pow(ln(z), 2) * NQCD + (- 1. / 2. * pow(ln(z), 2) * z * (1.0 / NQCD)) + 1. / 2. * pow(ln(z), 2) * z * NQCD + 1. / 2. * Li2(z) * (1.0 / NQCD) +  (-1. / 2. * Li2(z) * NQCD) + 1. / 2. * Li2(z) * z * (1.0 / NQCD) + (- 1. / 2. * Li2(z) * z * NQCD);
    return res;
}

fn D0_RG_001(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 2. / 3. * lmua * (1.0 / z) * (1.0 / NQCD) + (- 2. / 3. * lmua * (1.0 / z) * NQCD) + 1. / 2. * lmua * (1.0 / NQCD) + (- 1. / 2. * lmua * NQCD) + (- 1. / 2. * lmua * z * (1.0 / NQCD)) + 1. / 2. * lmua * z * NQCD + (- 2. / 3. * lmua * (z * z) * (1.0 / NQCD)) + 2. / 3. * lmua * (z * z) * NQCD + ln(z) * lmua * (1.0 / NQCD) + (- ln(z) * lmua * NQCD) + ln(z) * lmua * z * (1.0 / NQCD) + (- ln(z) * lmua * z * NQCD);
    return res;
}

fn D1_RG_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (-1. / 3. * (1.0 / z) * (1.0 / NQCD)) + 1. / 3. * (1.0 / z) * NQCD + (- 1. / 4. * (1.0 / NQCD)) + 1. / 4. * NQCD + 1. / 4. * z * (1.0 / NQCD) + (- 1. / 4. * z * NQCD) + 1. / 3. * (z * z) * (1.0 / NQCD) + (- 1. / 3. * (z * z) * NQCD) + (- 1. / 2. * ln(z) * (1.0 / NQCD)) + 1. / 2. * ln(z) * NQCD + (- 1. / 2. * ln(z) * z * (1.0 / NQCD)) + 1. / 2. * ln(z) * z * NQCD;
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
        let tmp: f64 = 5. / 72. * (1.0 / z) * (1.0 / NQCD) + (- 5. / 72. * (1.0 / z) * NQCD) + 1. / 6. * (1.0 / NQCD) + (- 1. / 6. * NQCD) + 23. / 24. * z * (1.0 / NQCD) + (- 23. / 24. * z * NQCD) + (- 43. / 36. * (z * z) * (1.0 / NQCD)) + 43. / 36. * (z * z) * NQCD + (- 19. / 72. * x * (1.0 / z) * (1.0 / NQCD)) + 19. / 72. * x * (1.0 / z) * NQCD + (- 4. / 3. * x * (1.0 / NQCD)) + 4. / 3. * x * NQCD + (- 13. / 24. * x * z * (1.0 / NQCD)) + 13. / 24. * x * z * NQCD + 77. / 36. * x * (z * z) * (1.0 / NQCD) + (- 77. / 36. * x * (z * z) * NQCD) + 1. / 12. * (pi * pi) * (1.0 / NQCD) + (- 1. / 12. * (pi * pi) * NQCD) + 1. / 12. * (pi * pi) * x * (1.0 / NQCD) + (- 1. / 12. * (pi * pi) * x * NQCD) + 1. / 6. * (pi * pi) * x * z * (1.0 / NQCD) + (- 1. / 6. * (pi * pi) * x * z * NQCD) + 1. / 6. * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 6. * ln(1.0 - z) * (1.0 / z) * NQCD) + 1. / 4. * ln(1.0 - z) * (1.0 / NQCD) + (- 1. / 4. * ln(1.0 - z) * NQCD) + (- 3. / 4. * ln(1.0 - z) * z * (1.0 / NQCD)) + 3. / 4. * ln(1.0 - z) * z * NQCD + 1. / 3. * ln(1.0 - z) * (z * z) * (1.0 / NQCD) + (- 1. / 3. * ln(1.0 - z) * (z * z) * NQCD) + 1. / 6. * ln(1.0 - z) * x * (1.0 / z) * (1.0 / NQCD) + (- 1. / 6. * ln(1.0 - z) * x * (1.0 / z) * NQCD) + 3. / 4. * ln(1.0 - z) * x * (1.0 / NQCD) + (- 3. / 4. * ln(1.0 - z) * x * NQCD) + (- 1. / 4. * ln(1.0 - z) * x * z * (1.0 / NQCD)) + 1. / 4. * ln(1.0 - z) * x * z * NQCD + (- 2. / 3. * ln(1.0 - z) * x * (z * z) * (1.0 / NQCD)) + 2. / 3. * ln(1.0 - z) * x * (z * z) * NQCD + 1. / 6. * ln(1.0 - x) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 6. * ln(1.0 - x) * (1.0 / z) * NQCD) + 1. / 4. * ln(1.0 - x) * (1.0 / NQCD) + (- 1. / 4. * ln(1.0 - x) * NQCD) + (- 3. / 4. * ln(1.0 - x) * z * (1.0 / NQCD)) + 3. / 4. * ln(1.0 - x) * z * NQCD + 1. / 3. * ln(1.0 - x) * (z * z) * (1.0 / NQCD) + (- 1. / 3. * ln(1.0 - x) * (z * z) * NQCD) + 1. / 6. * ln(1.0 - x) * x * (1.0 / z) * (1.0 / NQCD) + (-1. / 6. * ln(1.0 - x) * x * (1.0 / z) * NQCD) + 3. / 4. * ln(1.0 - x) * x * (1.0 / NQCD) + (- 3. / 4. * ln(1.0 - x) * x * NQCD) + (- 1. / 4. * ln(1.0 - x) * x * z * (1.0 / NQCD)) + 1. / 4. * ln(1.0 - x) * x * z * NQCD + (- 2. / 3. * ln(1.0 - x) * x * (z * z) * (1.0 / NQCD)) + 2. / 3. * ln(1.0 - x) * x * (z * z) * NQCD + (- 1. / 3. * ln(x) * (1.0 / z) * (1.0 / NQCD)) + 1. / 3. * ln(x) * (1.0 / z) * NQCD + (- 1. / 2. * ln(x) * (1.0 / NQCD)) + 1. / 2. * ln(x) * NQCD + 3. / 2. * ln(x) * z * (1.0 / NQCD) + (- 3. / 2. * ln(x) * z * NQCD) + (- 2. / 3. * ln(x) * (z * z) * (1.0 / NQCD)) + 2. / 3. * ln(x) * (z * z) * NQCD + (- 1. / 3. * ln(x) * x * (1.0 / z) * (1.0 / NQCD)) + 1. / 3. * ln(x) * x * (1.0 / z) * NQCD + (- 3. / 2. * ln(x) * x * (1.0 / NQCD)) + 3. / 2. * ln(x) * x * NQCD + 1. / 2. * ln(x) * x * z * (1.0 / NQCD) + (- 1. / 2. * ln(x) * x * z * NQCD) + 4. / 3. * ln(x) * x * (z * z) * (1.0 / NQCD) + (- 4. / 3. * ln(x) * x * (z * z) * NQCD) + (- ln(x) * ln(z) * (1.0 / NQCD)) + ln(x) * ln(z) * NQCD + (- ln(x) * ln(z) * x * (1.0 / NQCD)) + ln(x) * ln(z) * x * NQCD + (- 2.0 * ln(x) * ln(z) * x * z * (1.0 / NQCD)) + 2.0 * ln(x) * ln(z) * x * z * NQCD + 1. / 6. * ln(z) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 6. * ln(z) * (1.0 / z) * NQCD) + 3. / 4. * ln(z) * (1.0 / NQCD) + (- 3. / 4. * ln(z) * NQCD) + 1. / 4. * ln(z) * z * (1.0 / NQCD) + (- 1. / 4. * ln(z) * z * NQCD) + 1. / 3. * ln(z) * (z * z) * (1.0 / NQCD) + (- 1. / 3. * ln(z) * (z * z) * NQCD) + 1. / 6. * ln(z) * x * (1.0 / z) * (1.0 / NQCD) + (- 1. / 6. * ln(z) * x * (1.0 / z) * NQCD) + 1. / 4. * ln(z) * x * (1.0 / NQCD) + (- 1. / 4. * ln(z) * x * NQCD) + (- 7. / 4. * ln(z) * x * z * (1.0 / NQCD)) + 7. / 4. * ln(z) * x * z * NQCD + (- 2. / 3. * ln(z) * x * (z * z) * (1.0 / NQCD)) + 2. / 3. * ln(z) * x * (z * z) * NQCD + 1. / 2. * ln(z) * ln(1.0 - x) * (1.0 / NQCD) + (- 1. / 2. * ln(z) * ln(1.0 - x) * NQCD) + 1. / 2. * ln(z) * ln(1.0 - x) * x * (1.0 / NQCD) + (- 1. / 2. * ln(z) * ln(1.0 - x) * x * NQCD) + ln(z) * ln(1.0 - x) * x * z * (1.0 / NQCD) + (- ln(z) * ln(1.0 - x) * x * z * NQCD) + 1. / 2. * pow(ln(z), 2) * (1.0 / NQCD) + (- 1. / 2. * pow(ln(z), 2) * NQCD) + 1. / 2. * pow(ln(z), 2) * x * (1.0 / NQCD) + (- 1. / 2. * pow(ln(z), 2) * x * NQCD) + pow(ln(z), 2) * x * z * (1.0 / NQCD) + (- pow(ln(z), 2) * x * z * NQCD) + (- 1. / 2. * Li2(z) * (1.0 / NQCD)) + 1. / 2. * Li2(z) * NQCD + (- 1. / 2. * Li2(z) * x * (1.0 / NQCD)) + 1. / 2. * Li2(z) * x * NQCD + (- Li2(z) * x * z * (1.0 / NQCD)) + Li2(z) * x * z * NQCD + 2. / 3. / (1.0 - x) * ln(x) * (1.0 / z) * (1.0 / NQCD) + (-2. / 3. / (1.0 - x) * ln(x) * (1.0 / z) * NQCD) + 5. / 4. / (1.0 - x) * ln(x) * (1.0 / NQCD) + (- 5. / 4. / (1.0 - x) * ln(x) * NQCD) + (- 5. / 4. / (1.0 - x) * ln(x) * z * (1.0 / NQCD)) + 5. / 4. / (1.0 - x) * ln(x) * z * NQCD + (- 2. / 3. / (1.0 - x) * ln(x) * (z * z) * (1.0 / NQCD)) + 2. / 3. / (1.0 - x) * ln(x) * (z * z) * NQCD + 3. / 2. / (1.0 - x) * ln(x) * ln(z) * (1.0 / NQCD) + (- 3. / 2. / (1.0 - x) * ln(x) * ln(z) * NQCD) + 3. / 2. / (1.0 - x) * ln(x) * ln(z) * z * (1.0 / NQCD) + (- 3. / 2. / (1.0 - x) * ln(x) * ln(z) * z * NQCD);
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
        let tmp: f64 = (- 1. / 3. * lmua * (1.0 / z) * (1.0 / NQCD)) + 1. / 3. * lmua * (1.0 / z) * NQCD + (- 1. / 2. * lmua * (1.0 / NQCD)) + 1. / 2. * lmua * NQCD + 3. / 2. * lmua * z * (1.0 / NQCD) + (- 3. / 2. * lmua * z * NQCD) + (- 2. / 3. * lmua * (z * z) * (1.0 / NQCD)) + 2. / 3. * lmua * (z * z) * NQCD + (- 1. / 3. * lmua * x * (1.0 / z) * (1.0 / NQCD)) + 1. / 3. * lmua * x * (1.0 / z) * NQCD + (- 3. / 2. * lmua * x * (1.0 / NQCD)) + 3. / 2. * lmua * x * NQCD + 1. / 2. * lmua * x * z * (1.0 / NQCD) + (- 1. / 2. * lmua * x * z * NQCD) + 4. / 3. * lmua * x * (z * z) * (1.0 / NQCD) + (- 4. / 3. * lmua * x * (z * z) * NQCD) + (- ln(z) * lmua * (1.0 / NQCD)) + ln(z) * lmua * NQCD + (- ln(z) * lmua * x * (1.0 / NQCD)) + ln(z) * lmua * x * NQCD + (- 2.0 * ln(z) * lmua * x * z * (1.0 / NQCD)) + 2.0 * ln(z) * lmua * x * z * NQCD;
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
