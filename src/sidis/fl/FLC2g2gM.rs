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
        let tmp: f64 = 3. / 4. * (1.0 / x) * (1.0 / z) * NQCD + (- 3. / 4. * (1.0 / x) * NQCD) + 3. / 4. * (1.0 / (z * z)) * NQCD + (- 7. / 2. * (1.0 / z) * NQCD) + 4.0 * (1.0 / NQCD) + (- 5. / 2. * NQCD) + (- 4.0 * z * (1.0 / NQCD)) + 21. / 4. * z * NQCD + (- 3. / 4. * x * (1.0 / (z * z)) * NQCD) + (- 16.0 * x * (1.0 / z) * (1.0 / NQCD)) + (- 25. / 2. * x * (1.0 / z) * NQCD) + 28.0 * x * (1.0 / NQCD) + (- 16.0 * x * (1.0 / NQCD) * (rln2 * rln2)) + 5. / 2. * x * NQCD + (- 12.0 * x * z * (1.0 / NQCD)) + 16.0 * x * z * (1.0 / NQCD) * (rln2 * rln2) + 43. / 4. * x * z * NQCD + (- 16.0 * x * z * NQCD * (rln2 * rln2)) + 16.0 * (x * x) * (1.0 / z) * (1.0 / NQCD) + 61. / 4. * (x * x) * (1.0 / z) * NQCD + (- 32.0 * (x * x) * (1.0 / NQCD)) + 16.0 * (x * x) * (1.0 / NQCD) * (rln2 * rln2) + 3. / 4. * (x * x) * NQCD + 16.0 * (x * x) * z * (1.0 / NQCD) + (- 16.0 * (x * x) * z * (1.0 / NQCD) * (rln2 * rln2)) + (- 16.0 * (x * x) * z * NQCD) + 16.0 * (x * x) * z * NQCD * (rln2 * rln2) + (- 2. / 3. * (pi * pi) * x * (1.0 / NQCD)) + 2. / 3. * (pi * pi) * x * NQCD + (- 2. / 3. * (pi * pi) * x * z * (1.0 / NQCD)) + 2. / 3. * (pi * pi) * x * z * NQCD + 4. / 3. * (pi * pi) * (x * x) * z * (1.0 / NQCD) + (- 4. / 3. * (pi * pi) * (x * x) * z * NQCD) + (- 2.0 * ln(1.0 - z) * (1.0 / NQCD)) + 2.0 * ln(1.0 - z) * NQCD + 2.0 * ln(1.0 - z) * z * (1.0 / NQCD) + (- 2.0 * ln(1.0 - z) * z * NQCD) + (- 8.0 * ln(1.0 - z) * x * (1.0 / z) * (1.0 / NQCD)) + 8.0 * ln(1.0 - z) * x * (1.0 / z) * NQCD + 2.0 * ln(1.0 - z) * x * (1.0 / NQCD) + (- 2.0 * ln(1.0 - z) * x * NQCD) + 6.0 * ln(1.0 - z) * x * z * (1.0 / NQCD) + (- 6.0 * ln(1.0 - z) * x * z * NQCD) + 8.0 * ln(1.0 - z) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 8.0 * ln(1.0 - z) * (x * x) * (1.0 / z) * NQCD) + (- 8.0 * ln(1.0 - z) * (x * x) * z * (1.0 / NQCD)) + 8.0 * ln(1.0 - z) * (x * x) * z * NQCD + 24.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) * rln2 + (-8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD * rln2) + (- 24.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) * rln2) + 24.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD * rln2 + (- 24.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) * rln2) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD * rln2 + 24.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) * rln2 + (- 24.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD * rln2) + (- 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * (1.0 / NQCD)) + 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * NQCD + 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * z * (1.0 / NQCD) + (- 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * z * NQCD) + 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * (1.0 / NQCD) + (- 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * NQCD) + (- 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * z * (1.0 / NQCD)) + 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * z * NQCD + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) + (-8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD)) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD + 16.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD + (- 16.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD) + 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) * rln2 + 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD * rln2 + (- 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) * rln2) + 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD * rln2 + (- 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) * rln2) + (- 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD * rln2) + 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) * rln2 + (- 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD * rln2) + (- 2.0 * ln(1.0 - x) * (1.0 / NQCD)) + 2.0 * ln(1.0 - x) * NQCD + 2.0 * ln(1.0 - x) * z * (1.0 / NQCD) + (- 2.0 * ln(1.0 - x) * z * NQCD) + (- 8.0 * ln(1.0 - x) * x * (1.0 / z) * (1.0 / NQCD)) + 8.0 * ln(1.0 - x) * x * (1.0 / z) * NQCD + 2.0 * ln(1.0 - x) * x * (1.0 / NQCD) + (- 2.0 * ln(1.0 - x) * x * NQCD) + 6.0 * ln(1.0 - x) * x * z * (1.0 / NQCD) + (- 6.0 * ln(1.0 - x) * x * z * NQCD) + 8.0 * ln(1.0 - x) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 8.0 * ln(1.0 - x) * (x * x) * (1.0 / z) * NQCD) + (- 8.0 * ln(1.0 - x) * (x * x) * z * (1.0 / NQCD)) + 8.0 * ln(1.0 - x) * (x * x) * z * NQCD + 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + (-1. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + (- 2.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 7. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 2.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + 7.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD + (- 6.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 19. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + 15. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + 30.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 105. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 35. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + (- 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + 1. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + 2.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (-7. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + (- 3. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 2.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + (- 7.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD) + 6.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 19. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + (- 15. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + (- 30.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 105. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 35. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + (- 3. / 8. * ln(x) * (1.0 / x) * (1.0 / z) * NQCD) + 3. / 8. * ln(x) * (1.0 / x) * NQCD + 3. / 8. * ln(x) * (1.0 / (z * z)) * NQCD + (- 1. / 4. * ln(x) * (1.0 / z) * NQCD) + 3.0 * ln(x) * (1.0 / NQCD) + (- 15. / 4. * ln(x) * NQCD) + (- 3.0 * ln(x) * z * (1.0 / NQCD)) + 29. / 8. * ln(x) * z * NQCD + 3. / 8. * ln(x) * x * (1.0 / (z * z)) * NQCD + 8.0 * ln(x) * x * (1.0 / z) * (1.0 / NQCD) + (- 49. / 4. * ln(x) * x * (1.0 / z) * NQCD) + 5.0 * ln(x) * x * (1.0 / NQCD) + (- 16.0 * ln(x) * x * (1.0 / NQCD) * rln2) + (- 7. / 4. * ln(x) * x * NQCD) + 8.0 * ln(x) * x * NQCD * rln2 + (- 13.0 * ln(x) * x * z * (1.0 / NQCD)) + 16.0 * ln(x) * x * z * (1.0 / NQCD) * rln2 + 109. / 8. * ln(x) * x * z * NQCD + (- 16.0 * ln(x) * x * z * NQCD * rln2) + (- 8.0 * ln(x) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 29. / 8. * ln(x) * (x * x) * (1.0 / z) * NQCD + 16.0 * ln(x) * (x * x) * (1.0 / NQCD) * rln2 + 35. / 8. * ln(x) * (x * x) * NQCD + (- 8.0 * ln(x) * (x * x) * NQCD * rln2) + 8.0 * ln(x) * (x * x) * z * (1.0 / NQCD) + (- 16.0 * ln(x) * (x * x) * z * (1.0 / NQCD) * rln2) + (- 8.0 * ln(x) * (x * x) * z * NQCD) + 16.0 * ln(x) * (x * x) * z * NQCD * rln2 + (- 4.0 * ln(x) * ln(1.0 - z) * x * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - z) * x * NQCD + 4.0 * ln(x) * ln(1.0 - z) * x * z * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 - z) * x * z * NQCD) + 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD) + (- 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD + 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + 8.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 8.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 8.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 8.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 8.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + (- 4.0 * ln(x) * ln(1.0 - x) * x * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - x) * x * NQCD + 4.0 * ln(x) * ln(1.0 - x) * x * z * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 - x) * x * z * NQCD) + 4.0 * ln(x) * ln(1.0 - x) * (x * x) * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 - x) * (x * x) * NQCD) + (- 4.0 * ln(x) * ln(1.0 - x) * (x * x) * z * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - x) * (x * x) * z * NQCD + 8.0 * ln(x) * ln(1.0 + x) * x * NQCD + 8.0 * ln(x) * ln(1.0 + x) * x * z * (1.0 / NQCD) + (- 8.0 * ln(x) * ln(1.0 + x) * x * z * NQCD) + 8.0 * ln(x) * ln(1.0 + x) * (x * x) * NQCD + 8.0 * ln(x) * ln(1.0 + x) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * ln(x) * ln(1.0 + x) * (x * x) * z * NQCD) + (- 8.0 * ln(x) * ln(1.0 + x * z) * x * NQCD) + (- 8.0 * ln(x) * ln(1.0 + x * z) * (x * x) * z * (1.0 / NQCD)) + 8.0 * ln(x) * ln(1.0 + x * z) * (x * x) * z * NQCD + (- 8.0 * ln(x) * ln(z + x) * x * z * (1.0 / NQCD)) + 8.0 * ln(x) * ln(z + x) * x * z * NQCD + (- 8.0 * ln(x) * ln(z + x) * (x * x) * NQCD) + 2.0 * pow(ln(x), 2) * x * (1.0 / NQCD) + (- 2.0 * pow(ln(x), 2) * x * NQCD) + (- 2.0 * pow(ln(x), 2) * x * z * (1.0 / NQCD)) + 2.0 * pow(ln(x), 2) * x * z * NQCD + 2.0 * pow(ln(x), 2) * (x * x) * (1.0 / NQCD) + (- 2.0 * pow(ln(x), 2) * (x * x) * NQCD) + (- 2.0 * pow(ln(x), 2) * (x * x) * z * (1.0 / NQCD)) + 2.0 * pow(ln(x), 2) * (x * x) * z * NQCD + 4.0 * ln(x) * ln(z) * x * (1.0 / NQCD) + (- 12.0 * ln(x) * ln(z) * x * NQCD) + 12.0 * ln(x) * ln(z) * x * z * (1.0 / NQCD) + (- 12.0 * ln(x) * ln(z) * x * z * NQCD) + 8.0 * ln(x) * ln(z) * (x * x) * NQCD + (- 8.0 * ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD) + 8.0 * ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD + 3. / 8. * ln(z) * (1.0 / x) * (1.0 / z) * NQCD + 3. / 8. * ln(z) * (1.0 / x) * NQCD + (- 3. / 8. * ln(z) * (1.0 / (z * z)) * NQCD) + (- 1. / 4. * ln(z) * (1.0 / z) * NQCD) + ln(z) * (1.0 / NQCD) + (- 17. / 4. * ln(z) * NQCD) + ln(z) * z * (1.0 / NQCD) + (- 3. / 8. * ln(z) * z * NQCD) + 3. / 8. * ln(z) * x * (1.0 / (z * z)) * NQCD + (- 16.0 * ln(z) * x * (1.0 / z) * (1.0 / NQCD)) + 49. / 4. * ln(z) * x * (1.0 / z) * NQCD + (- 9.0 * ln(z) * x * (1.0 / NQCD)) + (- 16.0 * ln(z) * x * (1.0 / NQCD) * rln2) + 1. / 4. * ln(z) * x * NQCD + (- 8.0 * ln(z) * x * NQCD * rln2) + (- ln(z) * x * z * (1.0 / NQCD)) + 16.0 * ln(z) * x * z * (1.0 / NQCD) * rln2 + 3. / 8. * ln(z) * x * z * NQCD + (- 16.0 * ln(z) * x * z * NQCD * rln2) + 16.0 * ln(z) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 99. / 8. * ln(z) * (x * x) * (1.0 / z) * NQCD) + 8.0 * ln(z) * (x * x) * (1.0 / NQCD) + 16.0 * ln(z) * (x * x) * (1.0 / NQCD) * rln2 + 29. / 8. * ln(z) * (x * x) * NQCD + 8.0 * ln(z) * (x * x) * NQCD * rln2 + (- 16.0 * ln(z) * (x * x) * z * (1.0 / NQCD) * rln2) + 16.0 * ln(z) * (x * x) * z * NQCD * rln2 + 8.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 8.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 8.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 8.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 8.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD + (- 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + (- 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD) + 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + (- 8.0 * ln(z) * ln(1.0 - x) * x * (1.0 / NQCD)) + 8.0 * ln(z) * ln(1.0 - x) * x * NQCD + 8.0 * ln(z) * ln(1.0 - x) * (x * x) * (1.0 / NQCD) + (- 8.0 * ln(z) * ln(1.0 - x) * (x * x) * NQCD) + (- 8.0 * ln(z) * ln(1.0 + x * z) * x * NQCD) + (- 8.0 * ln(z) * ln(1.0 + x * z) * (x * x) * z * (1.0 / NQCD)) + 8.0 * ln(z) * ln(1.0 + x * z) * (x * x) * z * NQCD + 8.0 * ln(z) * ln(z + x) * x * z * (1.0 / NQCD) + (- 8.0 * ln(z) * ln(z + x) * x * z * NQCD) + 8.0 * ln(z) * ln(z + x) * (x * x) * NQCD + (- 8.0 * pow(ln(z), 2) * x * (1.0 / NQCD)) + 4.0 * pow(ln(z), 2) * x * NQCD + (- 4.0 * pow(ln(z), 2) * x * z * (1.0 / NQCD)) + 4.0 * pow(ln(z), 2) * x * z * NQCD + 8.0 * pow(ln(z), 2) * (x * x) * (1.0 / NQCD) + (- 8.0 * pow(ln(z), 2) * (x * x) * NQCD) + (- 3. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + 1. / 2. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + 2.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 7. / 2. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + (- 3. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 2.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + (- 7.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD) + 6.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 19. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + (- 15. / 2. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + (- 30.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 105. / 2. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 35. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + (- 8.0 * ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD) + 8.0 * ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD + (- 8.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * NQCD) + 8.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * NQCD + 8.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * NQCD + (- 8.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * NQCD) + 8.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 8.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 8.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 8.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 8.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + (- 8.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + 8.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) + (- 8.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD) + 8.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + (- 8.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD)) + 8.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD + (- 8.0 * Li2(-x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 8.0 * Li2(-x * (1.0 / z)) * x * z * NQCD + (- 8.0 * Li2(-x * (1.0 / z)) * (x * x) * NQCD) + 8.0 * Li2(-x) * x * NQCD + 8.0 * Li2(-x) * x * z * (1.0 / NQCD) + (- 8.0 * Li2(-x) * x * z * NQCD) + 8.0 * Li2(-x) * (x * x) * NQCD + 8.0 * Li2(-x) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * Li2(-x) * (x * x) * z * NQCD) + (- 8.0 * Li2(-x * z) * x * NQCD) + (- 8.0 * Li2(-x * z) * (x * x) * z * (1.0 / NQCD)) + 8.0 * Li2(-x * z) * (x * x) * z * NQCD + 4.0 * Li2(x) * (x * x) * (1.0 / NQCD) + (- 4.0 * Li2(x) * (x * x) * NQCD) + (- 4.0 * Li2(x) * (x * x) * z * (1.0 / NQCD)) + 4.0 * Li2(x) * (x * x) * z * NQCD + 8.0 * Li2(z) * x * (1.0 / NQCD) + (- 8.0 * Li2(z) * x * NQCD) + (- 8.0 * Li2(z) * (x * x) * (1.0 / NQCD)) + 8.0 * Li2(z) * (x * x) * NQCD + 3. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + (- 1. / 4. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + (- InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 7. / 4. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + 3. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + 7. / 2. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD + (- 3.0 * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 19. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + 15. / 4. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + 15.0 * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 105. / 4. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 35. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + (- 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + 1. / 4. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 7. / 4. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + (- 3. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + (- 7. / 2. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD) + 3.0 * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 19. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + (- 15. / 4. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + (- 15.0 * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 105. / 4. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 35. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + 3. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + (- 1. / 2. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + (- 2.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 7. / 2. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + 3. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 2.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + 7.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD + (- 6.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 19. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + 15. / 2. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + 30.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 105. / 2. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 35. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + (- 16.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD * rln2) + 16.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD * rln2;
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
        let tmp: f64 = 16.0 * lmua * x * (1.0 / z) * (1.0 / NQCD) + (- 16.0 * lmua * x * (1.0 / z) * NQCD) + (- 8.0 * lmua * x * (1.0 / NQCD)) + 8.0 * lmua * x * NQCD + (- 8.0 * lmua * x * z * (1.0 / NQCD)) + 8.0 * lmua * x * z * NQCD + (- 16.0 * lmua * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 16.0 * lmua * (x * x) * (1.0 / z) * NQCD + 8.0 * lmua * (x * x) * (1.0 / NQCD) + (- 8.0 * lmua * (x * x) * NQCD) + 8.0 * lmua * (x * x) * z * (1.0 / NQCD) + (- 8.0 * lmua * (x * x) * z * NQCD) + 16.0 * ln(z) * lmua * x * (1.0 / NQCD) + (- 16.0 * ln(z) * lmua * x * NQCD) + (- 16.0 * ln(z) * lmua * (x * x) * (1.0 / NQCD)) + 16.0 * ln(z) * lmua * (x * x) * NQCD;
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
        let tmp: f64 = 4.0 * lmuf * (1.0 / NQCD) + (- 4.0 * lmuf * NQCD) + (- 4.0 * lmuf * z * (1.0 / NQCD)) + 4.0 * lmuf * z * NQCD + 4.0 * lmuf * x * (1.0 / NQCD) + (- 4.0 * lmuf * x * NQCD) + (- 4.0 * lmuf * x * z * (1.0 / NQCD)) + 4.0 * lmuf * x * z * NQCD + (- 8.0 * lmuf * (x * x) * (1.0 / NQCD)) + 8.0 * lmuf * (x * x) * NQCD + 8.0 * lmuf * (x * x) * z * (1.0 / NQCD) + (- 8.0 * lmuf * (x * x) * z * NQCD) + 8.0 * ln(x) * lmuf * x * (1.0 / NQCD) + (- 8.0 * ln(x) * lmuf * x * NQCD) + (- 8.0 * ln(x) * lmuf * x * z * (1.0 / NQCD)) + 8.0 * ln(x) * lmuf * x * z * NQCD;
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("001", [RG_RG_001, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("010", [RG_RG_010, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _])
);

/*
  SV mapping:
  - 000: RG_RG
    - 001: RG_RG
    - 010: RG_RG
*/
