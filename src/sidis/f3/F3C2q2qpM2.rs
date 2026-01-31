use crate::sidis::internal::*;

fn RG_DL_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 52. / 27. * pow(x, -1) * CF + (- 41. / 36. * CF) + 17. / 36. * x * CF + (- 34. / 27. * pow(x, 2) * CF) + 1. / 6. * pow(pi, 2) * CF + 1. / 2. * pow(pi, 2) * x * CF + 1. / 3. * pow(pi, 2) * pow(x, 2) * CF + 13. / 9. * ln(1.0 - x) * pow(x, -1) * CF + (- 11. / 6. * ln(1.0 - x) * CF) + 17. / 6. * ln(1.0 - x) * x * CF + (- 22. / 9. * ln(1.0 - x) * pow(x, 2) * CF) + 1. / 3. * ln(1.0 - x) * pow(pi, 2) * CF + 1. / 3. * ln(1.0 - x) * pow(pi, 2) * x * CF + 1. / 3. * pow(ln(1.0 - x), 2) * pow(x, -1) * CF + 1. / 4. * pow(ln(1.0 - x), 2) * CF + (- 1. / 4. * pow(ln(1.0 - x), 2) * x * CF) + (- 1. / 3. * pow(ln(1.0 - x), 2) * pow(x, 2) * CF) + (- ln(1.0 - x) * Li2(1.0 - x) * CF) + (- ln(1.0 - x) * Li2(1.0 - x) * x * CF) + (- 2.0 * ln(1.0 - x) * Li2(x) * CF) + (- 2.0 * ln(1.0 - x) * Li2(x) * x * CF) + 23. / 6. * ln(x) * CF + (- 5. / 6. * ln(x) * x * CF) + 38. / 9. * ln(x) * pow(x, 2) * CF + (- 1. / 3. * ln(x) * pow(pi, 2) * CF) + (- 1. / 3. * ln(x) * pow(pi, 2) * x * CF) + (- 2. / 3. * ln(x) * ln(1.0 - x) * pow(x, -1) * CF) + (- 1. / 2. * ln(x) * ln(1.0 - x) * CF) + 1. / 2. * ln(x) * ln(1.0 - x) * x * CF + 2. / 3. * ln(x) * ln(1.0 - x) * pow(x, 2) * CF +  (-3. / 2. * ln(x) * pow(ln(1.0 - x), 2) * CF) + (- 3. / 2. * ln(x) * pow(ln(1.0 - x), 2) * x * CF) + (- 13. / 8. * pow(ln(x), 2) * CF) + (- 13. / 8. * pow(ln(x), 2) * x * CF) + (- 5. / 3. * pow(ln(x), 2) * pow(x, 2) * CF) + 5. / 12. * pow(ln(x), 3) * CF + 5. / 12. * pow(ln(x), 3) * x * CF + ln(x) * Li2(x) * CF + ln(x) * Li2(x) * x * CF + (- Li3(1.0 - x) * CF) + (- Li3(1.0 - x) * x * CF) + (- 2. / 3. * Li2(x) * pow(x, -1) * CF) + (- 3. / 2. * Li2(x) * CF) + (- 5. / 2. * Li2(x) * x * CF) + (- 4. / 3. * Li2(x) * pow(x, 2) * CF);
    return res;
}

fn RG_DL_010(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- 26. / 9. * lmuf * pow(x, -1) * CF) + 11. / 3. * lmuf * CF + (- 17. / 3. * lmuf * x * CF) + 44. / 9. * lmuf * pow(x, 2) * CF + (- 1. / 3. * lmuf * pow(pi, 2) * CF) + (- 1. / 3. * lmuf * pow(pi, 2) * x * CF) + (- 4. / 3. * lmuf * ln(1.0 - x) * pow(x, -1) * CF) + (- lmuf * ln(1.0 - x) * CF) + lmuf * ln(1.0 - x) * x * CF + 4. / 3. * lmuf * ln(1.0 - x) * pow(x, 2) * CF + 2.0 * lmuf * Li2(x) * CF + 2.0 * lmuf * Li2(x) * x * CF + (- 2.0 * ln(x) * lmuf * CF) + (- 6.0 * ln(x) * lmuf * x * CF) + (- 4.0 * ln(x) * lmuf * pow(x, 2) * CF) + 2.0 * pow(ln(x), 2) * lmuf * CF + 2.0 * pow(ln(x), 2) * lmuf * x * CF;
    return res;
}

fn RG_DL_020(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 4. / 3. * pow(lmuf, 2) * pow(x, -1) * CF + pow(lmuf, 2) * CF + (- pow(lmuf, 2) * x * CF) + (- 4. / 3. * pow(lmuf, 2) * pow(x, 2) * CF) + 2.0 * ln(x) * pow(lmuf, 2) * CF + 2.0 * ln(x) * pow(lmuf, 2) * x * CF;
    return res;
}

fn RG_D0_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 13. / 9. * pow(x, -1) * CF + (- 11. / 6. * CF) + 17. / 6. * x * CF + (- 22. / 9. * pow(x, 2) * CF) + 1. / 6. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * CF + 2. / 3. * ln(1.0 - x) * pow(x, -1) * CF + 1. / 2. * ln(1.0 - x) * CF + (- 1. / 2. * ln(1.0 - x) * x * CF) + (- 2. / 3. * ln(1.0 - x) * pow(x, 2) * CF) + ln(x) * CF + 3.0 * ln(x) * x * CF + 2.0 * ln(x) * pow(x, 2) * CF + (- pow(ln(x), 2) * CF) + (- pow(ln(x), 2) * x * CF) + (- Li2(x) * CF) + (- Li2(x) * x * CF);
    return res;
}

fn RG_D0_010(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = (- 4. / 3. * lmuf * pow(x, -1) * CF) + (- lmuf * CF) + lmuf * x * CF + 4. / 3. * lmuf * pow(x, 2) * CF + (- 2.0 * ln(x) * lmuf * CF) + (- 2.0 * ln(x) * lmuf * x * CF);
    return res;
}

fn RG_D1_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 2. / 3. * pow(x, -1) * CF + 1. / 2. * CF + (- 1. / 2. * x * CF) + (- 2. / 3. * pow(x, 2) * CF) + ln(x) * CF + ln(x) * x * CF;
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
        let tmp: f64 = (-13. / 9. * pow(x, -1) * pow(z, -1) * CF) + 11. / 6. * pow(z, -1) * CF + 4.0 * CF + (- 17. / 6. * x * pow(z, -1) * CF) + (- 4.0 * x * CF) + 22. / 9. * pow(x, 2) * pow(z, -1) * CF + (- 1. / 6. * pow(pi, 2) * pow(z, -1) * CF) + (- 1. / 6. * pow(pi, 2) * x * pow(z, -1) * CF) + (- 2. / 3. * ln(1.0 - z) * pow(x, -1) * pow(z, -1) * CF) + (- 1. / 2. * ln(1.0 - z) * pow(z, -1) * CF) + 1. / 2. * ln(1.0 - z) * x * pow(z, -1) * CF + 2. / 3. * ln(1.0 - z) * pow(x, 2) * pow(z, -1) * CF + (- 2. / 3. * ln(1.0 - x) * pow(x, -1) * pow(z, -1) * CF) + (- 1. / 2. * ln(1.0 - x) * pow(z, -1) * CF) + 1. / 2. * ln(1.0 - x) * x * pow(z, -1) * CF + 2. / 3. * ln(1.0 - x) * pow(x, 2) * pow(z, -1) * CF + (- ln(x) * pow(z, -1) * CF) + 1. / 2. * ln(x) * CF + 2.0 * ln(x) * z * CF + (- 3.0 * ln(x) * x * pow(z, -1) * CF) + 5. / 2. * ln(x) * x * CF + (- 2.0 * ln(x) * pow(x, 2) * pow(z, -1) * CF) + (- ln(x) * ln(1.0 - z) * pow(z, -1) * CF) + (- ln(x) * ln(1.0 - z) * x * pow(z, -1) * CF) + 2.0 * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * CF + (- 2.0 * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * CF) + pow(ln(x), 2) * pow(z, -1) * CF + pow(ln(x), 2) * x * pow(z, -1) * CF + (- ln(x) * ln(z) * pow(z, -1) * CF) + ln(x) * ln(z) * CF + (- ln(x) * ln(z) * x * pow(z, -1) * CF) + ln(x) * ln(z) * x * CF + (- 2. / 3. * ln(z) * pow(x, -1) * pow(z, -1) * CF) + (- 1. / 2. * ln(z) * pow(z, -1) * CF) + 7. / 2. * ln(z) * CF + (- 2.0 * ln(z) * z * CF) + 1. / 2. * ln(z) * x * pow(z, -1) * CF + (-7. / 2. * ln(z) * x * CF) + 2. / 3. * ln(z) * pow(x, 2) * pow(z, -1) * CF + 2.0 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * CF + (- 2.0 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * CF) + (- 2.0 * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * CF) + 2.0 * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * CF + Li2(x) * pow(z, -1) * CF + Li2(x) * x * pow(z, -1) * CF + 2. / 3. / (1.0 - z) * ln(z) * pow(x, -1) * CF + (- 1.0 / (1.0 - z) * ln(z) * CF) + 1.0 / (1.0 - z) * ln(z) * x * CF + (- 2. / 3. / (1.0 - z) * ln(z) * pow(x, 2) * CF) + 2.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(x) * CF + (- 2.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(x) * z * CF) + 2.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(x) * x * CF + (- 10.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(x) * x * z * CF) + 8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * CF + 2.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(z) * z * CF + 6.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(z) * x * z * CF + (- 8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * CF) + 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF + (- 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF + (-24.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 2) * CF) + 16.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 3) * CF + (- 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF) + 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF) + 24.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 2) * CF + (- 16.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 3) * CF) + 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF + (- 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF) + 8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF + (-24.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF) + 16.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF + (- 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF) + 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF + (- 8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF) + 24.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF + (- 16.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF) + (- 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF) + 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF + (-8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF) + 24.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 2) * CF + (- 16.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 3) * CF) + 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF + (- 4.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 8.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF + (- 24.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 2) * CF) + 16.0 / (1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * pow(z, 3) * CF + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF) + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * CF) + 8.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * CF + (- 8.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * ln(x) * ln(1.0 + x + mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF) + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF) + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF) + 8.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF) + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF + (-8.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF) + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * CF + (- 8.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF) + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * z * CF) + 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 4.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * CF) + 8.0 / (mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))) * x * z * CF;
        res += tmp;
    }

    return res;
}

fn RG_RG_010(x: f64, z: f64, NF: f64) -> f64 {
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

        let pt0: f64 = RG_RG_010(x0, z0, NF);
        let pt1: f64 = RG_RG_010(x1, z1, NF);
        let pt2: f64 = RG_RG_010(x2, z2, NF);

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

        let pt0: f64 = RG_RG_010(x0, z0, NF);
        let pt1: f64 = RG_RG_010(x1, z1, NF);
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

        let pt0: f64 = RG_RG_010(x0, z0, NF);
        let pt1: f64 = RG_RG_010(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }

    if z != x && z != 1. - x {
        let tmp: f64 = 4. / 3. * lmuf * pow(x, -1) * pow(z, -1) * CF + lmuf * pow(z, -1) * CF + (- lmuf * x * pow(z, -1) * CF) + (- 4. / 3. * lmuf * pow(x, 2) * pow(z, -1) * CF) + 2.0 * ln(x) * lmuf * pow(z, -1) * CF + 2.0 * ln(x) * lmuf * x * pow(z, -1) * CF;
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, RG_D0_000, RG_D1_000, _, _, RG_DL_000, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("010", [RG_RG_010, RG_D0_010, _, _, _, RG_DL_010, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("020", [_, _, _, _, _, RG_DL_020, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _])
);

/*
  SV mapping:
  - 000: RG_D0, RG_D1, RG_DL, RG_RG
    - 010: RG_D0, RG_DL, RG_RG
    - 020: RG_DL
*/
