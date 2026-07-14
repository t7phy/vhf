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
        let tmp: f64 = (-3. / 8. * (1.0 / x) * (1.0 / z) * (1.0 / NQCD)) + 3. / 8. * (1.0 / x) * (1.0 / z) * NQCD + 3. / 8. * (1.0 / x) * (1.0 / NQCD) + (- 3. / 8. * (1.0 / x) * NQCD) + (- 3. / 8. * (1.0 / (z * z)) * (1.0 / NQCD)) + 3. / 8. * (1.0 / (z * z)) * NQCD + 7. / 4. * (1.0 / z) * (1.0 / NQCD) + (- 7. / 4. * (1.0 / z) * NQCD) + (- 3. / 4. * (1.0 / NQCD)) + 3. / 4. * NQCD + (- 5. / 8. * z * (1.0 / NQCD)) + 5. / 8. * z * NQCD + 3. / 8. * x * (1.0 / (z * z)) * (1.0 / NQCD) + (- 3. / 8. * x * (1.0 / (z * z)) * NQCD) + (- 3. / 4. * x * (1.0 / z) * (1.0 / NQCD)) + 3. / 4. * x * (1.0 / z) * NQCD + (- 1. / 4. * x * (1.0 / NQCD)) + 1. / 4. * x * NQCD + 5. / 8. * x * z * (1.0 / NQCD) + (- 5. / 8. * x * z * NQCD) + (- 5. / 8. * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 5. / 8. * (x * x) * (1.0 / z) * NQCD + 5. / 8. * (x * x) * (1.0 / NQCD) + (- 5. / 8. * (x * x) * NQCD) + (- 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * (1.0 / NQCD)) + 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + 1. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + (- 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + (- 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * (1.0 / NQCD)) + 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 1. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + (- 1. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD) + 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + (- 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD)) + 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + 9. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 9. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * (1.0 / NQCD) + (- 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * (1.0 / NQCD) + (- 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + (- 1. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD)) + 1. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * (1.0 / NQCD) + (- 3. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 1. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + 1. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD + (- 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD) + (- 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + (- 9. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 9. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * (1.0 / NQCD)) + 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + 3. / 16. * ln(x) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD) + (- 3. / 16. * ln(x) * (1.0 / x) * (1.0 / z) * NQCD) + (- 3. / 16. * ln(x) * (1.0 / x) * (1.0 / NQCD)) + 3. / 16. * ln(x) * (1.0 / x) * NQCD + (- 3. / 16. * ln(x) * (1.0 / (z * z)) * (1.0 / NQCD)) + 3. / 16. * ln(x) * (1.0 / (z * z)) * NQCD + 1. / 8. * ln(x) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 8. * ln(x) * (1.0 / z) * NQCD) + 3. / 8. * ln(x) * (1.0 / NQCD) + (- 3. / 8. * ln(x) * NQCD) + (- 5. / 16. * ln(x) * z * (1.0 / NQCD)) + 5. / 16. * ln(x) * z * NQCD + (- 3. / 16. * ln(x) * x * (1.0 / (z * z)) * (1.0 / NQCD)) + 3. / 16. * ln(x) * x * (1.0 / (z * z)) * NQCD + 13. / 8. * ln(x) * x * (1.0 / z) * (1.0 / NQCD) + (- 13. / 8. * ln(x) * x * (1.0 / z) * NQCD) + (- 9. / 8. * ln(x) * x * (1.0 / NQCD)) + 9. / 8. * ln(x) * x * NQCD + (- 5. / 16. * ln(x) * x * z * (1.0 / NQCD)) + 5. / 16. * ln(x) * x * z * NQCD + (- 5. / 16. * ln(x) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 5. / 16. * ln(x) * (x * x) * (1.0 / z) * NQCD + 5. / 16. * ln(x) * (x * x) * (1.0 / NQCD) + (- 5. / 16. * ln(x) * (x * x) * NQCD) + 2.0 * ln(x) * ln(z) * x * (1.0 / NQCD) + (- 2.0 * ln(x) * ln(z) * x * NQCD) + (- 3. / 16. * ln(z) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD)) + 3. / 16. * ln(z) * (1.0 / x) * (1.0 / z) * NQCD + (- 3. / 16. * ln(z) * (1.0 / x) * (1.0 / NQCD)) + 3. / 16. * ln(z) * (1.0 / x) * NQCD + 3. / 16. * ln(z) * (1.0 / (z * z)) * (1.0 / NQCD) + (- 3. / 16. * ln(z) * (1.0 / (z * z)) * NQCD) + 1. / 8. * ln(z) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 8. * ln(z) * (1.0 / z) * NQCD) + 13. / 8. * ln(z) * (1.0 / NQCD) + (- 13. / 8. * ln(z) * NQCD) + (- 5. / 16. * ln(z) * z * (1.0 / NQCD)) + 5. / 16. * ln(z) * z * NQCD + (- 3. / 16. * ln(z) * x * (1.0 / (z * z)) * (1.0 / NQCD)) + 3. / 16. * ln(z) * x * (1.0 / (z * z)) * NQCD + 3. / 8. * ln(z) * x * (1.0 / z) * (1.0 / NQCD) + (- 3. / 8. * ln(z) * x * (1.0 / z) * NQCD) + (-9. / 8. * ln(z) * x * (1.0 / NQCD)) + 9. / 8. * ln(z) * x * NQCD + 5. / 16. * ln(z) * x * z * (1.0 / NQCD) + (- 5. / 16. * ln(z) * x * z * NQCD) + (- 5. / 16. * ln(z) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 5. / 16. * ln(z) * (x * x) * (1.0 / z) * NQCD + (- 5. / 16. * ln(z) * (x * x) * (1.0 / NQCD)) + 5. / 16. * ln(z) * (x * x) * NQCD + 3. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * (1.0 / NQCD) + (- 3. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + (- 1. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD)) + 1. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + 3. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 3. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + 3. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * (1.0 / NQCD) + (- 3. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 1. / 2. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + 1. / 2. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD + (- 5. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 5. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + 3. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD) + (- 3. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + (-9. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 9. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 5. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * (1.0 / NQCD)) + 5. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + (- 3. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * (1.0 / NQCD)) + 3. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + 1. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + (- 3. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 3. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + (- 3. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * (1.0 / NQCD)) + 3. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 1. / 4. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + (- 1. / 4. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD) + 5. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 5. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + (- 3. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD)) + 3. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + 9. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 9. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 5. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * (1.0 / NQCD) + (- 5. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + 3. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * (1.0 / NQCD) + (- 3. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + (- 1. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD)) + 1. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + 3. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * (1.0 / NQCD) + (- 3. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 1. / 4. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + 1. / 4. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD + (- 5. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 5. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD) + (-3. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + (- 9. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 9. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 5. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * (1.0 / NQCD)) + 5. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + (- 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * (1.0 / NQCD)) + 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + 1. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * (1.0 / NQCD) + (- 1. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + (- 3. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 3. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + (- 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * (1.0 / NQCD)) + 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 1. / 2. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + (- 1. / 2. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD) + 5. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 5. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + (- 3. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD)) + 3. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + 9. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 9. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 5. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * (1.0 / NQCD) + (- 5. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD);
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
