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
        let tmp: f64 = (-5. / 8. * (1.0 / x) * (1.0 / z) * NQCD) + 5. / 8. * (1.0 / x) * NQCD + (- 5. / 8. * (1.0 / (z * z)) * NQCD) + 13. / 8. * (1.0 / z) * (1.0 / NQCD) + (- 11. / 8. * (1.0 / z) * NQCD) + 4.0 * (1.0 / z) * NQCD * (rln2 * rln2) + 1. / 4. * (1.0 / NQCD) + 8.0 * (1.0 / NQCD) * (rln2 * rln2) + (- 1. / 2. * NQCD) + (- 4.0 * NQCD * (rln2 * rln2)) + (- 27. / 8. * z * (1.0 / NQCD)) + (- 4.0 * z * (1.0 / NQCD) * (rln2 * rln2)) + 4.0 * z * NQCD + 4.0 * z * NQCD * (rln2 * rln2) + 5. / 8. * x * (1.0 / (z * z)) * NQCD + 1. / 2. * x * (1.0 / z) * (1.0 / NQCD) + (- 47. / 4. * x * (1.0 / z) * NQCD) + (- 8.0 * x * (1.0 / z) * NQCD * (rln2 * rln2)) + x * (1.0 / NQCD) + (- 16.0 * x * (1.0 / NQCD) * (rln2 * rln2)) + 41. / 4. * x * NQCD + 8.0 * x * NQCD * (rln2 * rln2) + 1. / 2. * x * z * (1.0 / NQCD) + 8.0 * x * z * (1.0 / NQCD) * (rln2 * rln2) + (- 9. / 8. * x * z * NQCD) + (- 8.0 * x * z * NQCD * (rln2 * rln2)) + (x * x) * (1.0 / z) * (1.0 / NQCD) + 117. / 8. * (x * x) * (1.0 / z) * NQCD + 8.0 * (x * x) * (1.0 / z) * NQCD * (rln2 * rln2) + (- 9. / 2. * (x * x) * (1.0 / NQCD)) + 8.0 * (x * x) * (1.0 / NQCD) * (rln2 * rln2) + (- 89. / 8. * (x * x) * NQCD) + 3.0 * (x * x) * z * (1.0 / NQCD) + (- 8.0 * (x * x) * z * (1.0 / NQCD) * (rln2 * rln2)) + (- 3.0 * (x * x) * z * NQCD) + 8.0 * (x * x) * z * NQCD * (rln2 * rln2) + 7. / 12. * (pi * pi) * (1.0 / z) * (1.0 / NQCD) + (- 7. / 12. * (pi * pi) * (1.0 / z) * NQCD) + (- 1. / 2. * (pi * pi) * (1.0 / NQCD)) + 1. / 2. * (pi * pi) * NQCD + 1. / 2. * (pi * pi) * z * (1.0 / NQCD) + (- 1. / 2. * (pi * pi) * z * NQCD) + (- 7. / 6. * (pi * pi) * x * (1.0 / z) * (1.0 / NQCD)) + 7. / 6. * (pi * pi) * x * (1.0 / z) * NQCD + (pi * pi) * x * (1.0 / NQCD) + (- (pi * pi) * x * NQCD) + (- 2. / 3. * (pi * pi) * x * z * (1.0 / NQCD)) + 2. / 3. * (pi * pi) * x * z * NQCD + 4. / 3. * (pi * pi) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (-4. / 3. * (pi * pi) * (x * x) * (1.0 / z) * NQCD) + (- 2. / 3. * (pi * pi) * (x * x) * (1.0 / NQCD)) + 2. / 3. * (pi * pi) * (x * x) * NQCD + (pi * pi) * (x * x) * z * (1.0 / NQCD) + (- (pi * pi) * (x * x) * z * NQCD) + 15. / 4. * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD) + (- 15. / 4. * ln(1.0 - z) * (1.0 / z) * NQCD) + (- 7. / 2. * ln(1.0 - z) * (1.0 / NQCD)) + 7. / 2. * ln(1.0 - z) * NQCD + 3. / 4. * ln(1.0 - z) * z * (1.0 / NQCD) + (- 3. / 4. * ln(1.0 - z) * z * NQCD) + (- 10.0 * ln(1.0 - z) * x * (1.0 / z) * (1.0 / NQCD)) + 10.0 * ln(1.0 - z) * x * (1.0 / z) * NQCD + 8.0 * ln(1.0 - z) * x * (1.0 / NQCD) + (- 8.0 * ln(1.0 - z) * x * NQCD) + (- 1. / 2. * ln(1.0 - z) * x * z * (1.0 / NQCD)) + 1. / 2. * ln(1.0 - z) * x * z * NQCD + 9.0 * ln(1.0 - z) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 9.0 * ln(1.0 - z) * (x * x) * (1.0 / z) * NQCD) + (- 7.0 * ln(1.0 - z) * (x * x) * (1.0 / NQCD)) + 7.0 * ln(1.0 - z) * (x * x) * NQCD + (- ln(1.0 - z) * (x * x) * z * (1.0 / NQCD)) + ln(1.0 - z) * (x * x) * z * NQCD + (- pow(ln(1.0 - z), 2) * (1.0 / z) * (1.0 / NQCD)) + pow(ln(1.0 - z), 2) * (1.0 / z) * NQCD + pow(ln(1.0 - z), 2) * (1.0 / NQCD) + (- pow(ln(1.0 - z), 2) * NQCD) + (- 1. / 2. * pow(ln(1.0 - z), 2) * z * (1.0 / NQCD)) + 1. / 2. * pow(ln(1.0 - z), 2) * z * NQCD + 2.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) * NQCD) + (- 2.0 * pow(ln(1.0 - z), 2) * x * (1.0 / NQCD)) + 2.0 * pow(ln(1.0 - z), 2) * x * NQCD + pow(ln(1.0 - z), 2) * x * z * (1.0 / NQCD) + (- pow(ln(1.0 - z), 2) * x * z * NQCD) + (- 2.0 * pow(ln(1.0 - z), 2) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 2.0 * pow(ln(1.0 - z), 2) * (x * x) * (1.0 / z) * NQCD + 2.0 * pow(ln(1.0 - z), 2) * (x * x) * (1.0 / NQCD) + (- 2.0 * pow(ln(1.0 - z), 2) * (x * x) * NQCD) + (- pow(ln(1.0 - z), 2) * (x * x) * z * (1.0 / NQCD)) + pow(ln(1.0 - z), 2) * (x * x) * z * NQCD + 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * (1.0 / NQCD) * rln2 + (- 6.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD * rln2) + (- 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) * rln2) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * NQCD * rln2 + 6.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD) * rln2 + (- 6.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD * rln2) + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * (1.0 / NQCD) * rln2) + 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD * rln2 + 24.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) * rln2 + (- 16.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD * rln2) + (- 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) * rln2) + 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD * rln2 + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * (1.0 / NQCD) * rln2 + (- 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD * rln2) + (- 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) * rln2) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD * rln2 + 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) * rln2 + (- 12.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD * rln2) + (- 2.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (1.0 / z) * (1.0 / NQCD)) + 2.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (1.0 / z) * NQCD + 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (1.0 / NQCD) + (- 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * NQCD) + (- 2.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * z * (1.0 / NQCD)) + 2.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * z * NQCD + 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * (1.0 / z) * NQCD) + (- 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * (1.0 / NQCD)) + 8.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * NQCD + 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * z * (1.0 / NQCD) + (- 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * x * z * NQCD) + (- 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * (1.0 / z) * NQCD + 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * (1.0 / NQCD) + (- 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * NQCD) + (- 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * z * (1.0 / NQCD)) + 4.0 * pow(ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)), 2.0) * (x * x) * z * NQCD + 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * (1.0 / NQCD) + 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) + (- 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD)) + 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * (1.0 / NQCD)) + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD) + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * (1.0 / NQCD) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD)) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z) * NQCD) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD) + (- 2.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * (1.0 / NQCD) * rln2) + (- 2.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD * rln2) + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) * rln2) + 2.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD) * rln2 + (- 2.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD * rln2) + 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * (1.0 / NQCD) * rln2 + 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD * rln2 + 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) * rln2 + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) * rln2) + 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD * rln2 + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * (1.0 / NQCD) * rln2) + (-4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD * rln2) + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) * rln2) + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD * rln2) + 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) * rln2 + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD * rln2) + 15. / 4. * ln(1.0 - x) * (1.0 / z) * (1.0 / NQCD) + (- 15. / 4. * ln(1.0 - x) * (1.0 / z) * NQCD) + (- 7. / 2. * ln(1.0 - x) * (1.0 / NQCD)) + 7. / 2. * ln(1.0 - x) * NQCD + 3. / 4. * ln(1.0 - x) * z * (1.0 / NQCD) + (- 3. / 4. * ln(1.0 - x) * z * NQCD) + (- 10.0 * ln(1.0 - x) * x * (1.0 / z) * (1.0 / NQCD)) + 10.0 * ln(1.0 - x) * x * (1.0 / z) * NQCD + 8.0 * ln(1.0 - x) * x * (1.0 / NQCD) + (- 8.0 * ln(1.0 - x) * x * NQCD) + (- 1. / 2. * ln(1.0 - x) * x * z * (1.0 / NQCD)) + 1. / 2. * ln(1.0 - x) * x * z * NQCD + 9.0 * ln(1.0 - x) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 9.0 * ln(1.0 - x) * (x * x) * (1.0 / z) * NQCD) + (- 7.0 * ln(1.0 - x) * (x * x) * (1.0 / NQCD)) + 7.0 * ln(1.0 - x) * (x * x) * NQCD + (- ln(1.0 - x) * (x * x) * z * (1.0 / NQCD)) + ln(1.0 - x) * (x * x) * z * NQCD + (- 2.0 * ln(1.0 - x) * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD)) + 2.0 * ln(1.0 - x) * ln(1.0 - z) * (1.0 / z) * NQCD + 2.0 * ln(1.0 - x) * ln(1.0 - z) * (1.0 / NQCD) + (- 2.0 * ln(1.0 - x) * ln(1.0 - z) * NQCD) + (- ln(1.0 - x) * ln(1.0 - z) * z * (1.0 / NQCD)) + ln(1.0 - x) * ln(1.0 - z) * z * NQCD + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) * NQCD) + (- 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / NQCD)) + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * NQCD + 2.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (1.0 / NQCD) + (-2.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * NQCD) + (- 4.0 * ln(1.0 - x) * ln(1.0 - z) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 4.0 * ln(1.0 - x) * ln(1.0 - z) * (x * x) * (1.0 / z) * NQCD + 4.0 * ln(1.0 - x) * ln(1.0 - z) * (x * x) * (1.0 / NQCD) + (- 4.0 * ln(1.0 - x) * ln(1.0 - z) * (x * x) * NQCD) + (- 2.0 * ln(1.0 - x) * ln(1.0 - z) * (x * x) * z * (1.0 / NQCD)) + 2.0 * ln(1.0 - x) * ln(1.0 - z) * (x * x) * z * NQCD + (- pow(ln(1.0 - x), 2) * (1.0 / z) * (1.0 / NQCD)) + pow(ln(1.0 - x), 2) * (1.0 / z) * NQCD + pow(ln(1.0 - x), 2) * (1.0 / NQCD) + (- pow(ln(1.0 - x), 2) * NQCD) + (- 1. / 2. * pow(ln(1.0 - x), 2) * z * (1.0 / NQCD)) + 1. / 2. * pow(ln(1.0 - x), 2) * z * NQCD + 2.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) * NQCD) + (- 2.0 * pow(ln(1.0 - x), 2) * x * (1.0 / NQCD)) + 2.0 * pow(ln(1.0 - x), 2) * x * NQCD + pow(ln(1.0 - x), 2) * x * z * (1.0 / NQCD) + (- pow(ln(1.0 - x), 2) * x * z * NQCD) + (- 2.0 * pow(ln(1.0 - x), 2) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 2.0 * pow(ln(1.0 - x), 2) * (x * x) * (1.0 / z) * NQCD + 2.0 * pow(ln(1.0 - x), 2) * (x * x) * (1.0 / NQCD) + (- 2.0 * pow(ln(1.0 - x), 2) * (x * x) * NQCD) + (- pow(ln(1.0 - x), 2) * (x * x) * z * (1.0 / NQCD)) + pow(ln(1.0 - x), 2) * (x * x) * z * NQCD + (- 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + (- 9. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + 3.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 21. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + (- 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 3.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + (- 5. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD) + (- 3.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 19. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + (- 45. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + 15.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 105. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 35. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + 9. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + (- 3.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 21. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + 5. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 3.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + 5. / 2. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD + 3.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 19. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + 45. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + (- 15.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 105. / 4. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 35. / 8. * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + 5. / 16. * ln(x) * (1.0 / x) * (1.0 / z) * NQCD + (- 5. / 16. * ln(x) * (1.0 / x) * NQCD) + (- 5. / 16. * ln(x) * (1.0 / (z * z)) * NQCD) + (- 7. / 2. * ln(x) * (1.0 / z) * (1.0 / NQCD)) + (- 2.0 * ln(x) * (1.0 / z) * (1.0 / NQCD) * rln2) + (- 5. / 8. * ln(x) * (1.0 / z) * NQCD) + 4.0 * ln(x) * (1.0 / z) * NQCD * rln2 + 9. / 2. * ln(x) * (1.0 / NQCD) + 8.0 * ln(x) * (1.0 / NQCD) * rln2 + (- 3. / 8. * ln(x) * NQCD) + (- 6.0 * ln(x) * NQCD * rln2) + (- 2.0 * ln(x) * z * (1.0 / NQCD)) + (- 4.0 * ln(x) * z * (1.0 / NQCD) * rln2) + 37. / 16. * ln(x) * z * NQCD + 4.0 * ln(x) * z * NQCD * rln2 + (- 5. / 16. * ln(x) * x * (1.0 / (z * z)) * NQCD) + 10.0 * ln(x) * x * (1.0 / z) * (1.0 / NQCD) + 4.0 * ln(x) * x * (1.0 / z) * (1.0 / NQCD) * rln2 + (-109. / 8. * ln(x) * x * (1.0 / z) * NQCD) + (- 8.0 * ln(x) * x * (1.0 / z) * NQCD * rln2) + (- 11. / 2. * ln(x) * x * (1.0 / NQCD)) + (- 16.0 * ln(x) * x * (1.0 / NQCD) * rln2) + 73. / 8. * ln(x) * x * NQCD + 12.0 * ln(x) * x * NQCD * rln2 + (- 5. / 2. * ln(x) * x * z * (1.0 / NQCD)) + 8.0 * ln(x) * x * z * (1.0 / NQCD) * rln2 + 45. / 16. * ln(x) * x * z * NQCD + (- 8.0 * ln(x) * x * z * NQCD * rln2) + (- 9.0 * ln(x) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + (- 4.0 * ln(x) * (x * x) * (1.0 / z) * (1.0 / NQCD) * rln2) + 109. / 16. * ln(x) * (x * x) * (1.0 / z) * NQCD + 8.0 * ln(x) * (x * x) * (1.0 / z) * NQCD * rln2 + 7.0 * ln(x) * (x * x) * (1.0 / NQCD) + 8.0 * ln(x) * (x * x) * (1.0 / NQCD) * rln2 + (- 77. / 16. * ln(x) * (x * x) * NQCD) + (- 4.0 * ln(x) * (x * x) * NQCD * rln2) + ln(x) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * ln(x) * (x * x) * z * (1.0 / NQCD) * rln2) + (- ln(x) * (x * x) * z * NQCD) + 8.0 * ln(x) * (x * x) * z * NQCD * rln2 + 3. / 2. * ln(x) * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD) + (- 3. / 2. * ln(x) * ln(1.0 - z) * (1.0 / z) * NQCD) + (- ln(x) * ln(1.0 - z) * (1.0 / NQCD)) + ln(x) * ln(1.0 - z) * NQCD + ln(x) * ln(1.0 - z) * z * (1.0 / NQCD) + (- ln(x) * ln(1.0 - z) * z * NQCD) + (- 3.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / NQCD)) + 3.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) * NQCD + 2.0 * ln(x) * ln(1.0 - z) * x * (1.0 / NQCD) + (- 2.0 * ln(x) * ln(1.0 - z) * x * NQCD) + 4.0 * ln(x) * ln(1.0 - z) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 - z) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * ln(x) * ln(1.0 - z) * (x * x) * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - z) * (x * x) * NQCD + 2.0 * ln(x) * ln(1.0 - z) * (x * x) * z * (1.0 / NQCD) + (- 2.0 * ln(x) * ln(1.0 - z) * (x * x) * z * NQCD) + 2.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * (1.0 / NQCD) + (-2.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD) + (- 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * NQCD + 2.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD) + (- 2.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD) + (- 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD + 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 8.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD) + (- 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD + 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD) + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD)) + 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * NQCD + 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD) + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD) + 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD + 8.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD) + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + ln(x) * ln(1.0 - x) * (1.0 / z) * (1.0 / NQCD) + (- ln(x) * ln(1.0 - x) * (1.0 / z) * NQCD) + (- 2.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / NQCD)) + 2.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) * NQCD + 2.0 * ln(x) * ln(1.0 - x) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * ln(x) * ln(1.0 - x) * (x * x) * (1.0 / z) * NQCD) + (- 2.0 * ln(x) * ln(1.0 - x) * (x * x) * (1.0 / NQCD)) + 2.0 * ln(x) * ln(1.0 - x) * (x * x) * NQCD + (- 2.0 * ln(x) * ln(1.0 + x) * (1.0 / z) * NQCD) + 2.0 * ln(x) * ln(1.0 + x) * (1.0 / NQCD) + 2.0 * ln(x) * ln(1.0 + x) * z * (1.0 / NQCD) + (- 2.0 * ln(x) * ln(1.0 + x) * z * NQCD) + (- 4.0 * ln(x) * ln(1.0 + x) * x * (1.0 / z) * NQCD) + 4.0 * ln(x) * ln(1.0 + x) * x * (1.0 / NQCD) + 4.0 * ln(x) * ln(1.0 + x) * x * z * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 + x) * x * z * NQCD) + (- 4.0 * ln(x) * ln(1.0 + x) * (x * x) * (1.0 / z) * NQCD) + 4.0 * ln(x) * ln(1.0 + x) * (x * x) * NQCD + 4.0 * ln(x) * ln(1.0 + x) * (x * x) * z * (1.0 / NQCD) + (- 4.0 * ln(x) * ln(1.0 + x) * (x * x) * z * NQCD) + 2.0 * ln(x) * ln(1.0 + x * z) * (1.0 / z) * NQCD + (- 2.0 * ln(x) * ln(1.0 + x * z) * z * (1.0 / NQCD)) + 2.0 * ln(x) * ln(1.0 + x * z) * z * NQCD + (- 4.0 * ln(x) * ln(1.0 + x * z) * x * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 + x * z) * (x * x) * (1.0 / z) * NQCD + (- 4.0 * ln(x) * ln(1.0 + x * z) * (x * x) * z * (1.0 / NQCD)) + 4.0 * ln(x) * ln(1.0 + x * z) * (x * x) * z * NQCD + (- 2.0 * ln(x) * ln(z + x) * (1.0 / NQCD)) + 4.0 * ln(x) * ln(z + x) * x * (1.0 / z) * NQCD + (- 4.0 * ln(x) * ln(z + x) * x * z * (1.0 / NQCD)) + 4.0 * ln(x) * ln(z + x) * x * z * NQCD + (- 4.0 * ln(x) * ln(z + x) * (x * x) * NQCD) + (- pow(ln(x), 2) * (1.0 / z) * (1.0 / NQCD)) + pow(ln(x), 2) * (1.0 / z) * NQCD + pow(ln(x), 2) * (1.0 / NQCD) + (- pow(ln(x), 2) * NQCD) + (- pow(ln(x), 2) * z * (1.0 / NQCD)) + pow(ln(x), 2) * z * NQCD + 2.0 * pow(ln(x), 2) * x * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * pow(ln(x), 2) * x * (1.0 / z) * NQCD) + (- 2.0 * pow(ln(x), 2) * x * (1.0 / NQCD)) + 2.0 * pow(ln(x), 2) * x * NQCD + (- 3.0 * pow(ln(x), 2) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 3.0 * pow(ln(x), 2) * (x * x) * (1.0 / z) * NQCD + 3.0 * pow(ln(x), 2) * (x * x) * (1.0 / NQCD) + (- 3.0 * pow(ln(x), 2) * (x * x) * NQCD) + (- 2.0 * pow(ln(x), 2) * (x * x) * z * (1.0 / NQCD)) + 2.0 * pow(ln(x), 2) * (x * x) * z * NQCD + (- 1. / 2. * ln(x) * ln(z) * (1.0 / z) * (1.0 / NQCD)) + (- 3. / 2. * ln(x) * ln(z) * (1.0 / z) * NQCD) + 3.0 * ln(x) * ln(z) * (1.0 / NQCD) + (- 3.0 * ln(x) * ln(z) * NQCD) + ln(x) * ln(z) * x * (1.0 / z) * (1.0 / NQCD) + (- 9.0 * ln(x) * ln(z) * x * (1.0 / z) * NQCD) + 2.0 * ln(x) * ln(z) * x * (1.0 / NQCD) + (- 6.0 * ln(x) * ln(z) * x * NQCD) + 6.0 * ln(x) * ln(z) * x * z * (1.0 / NQCD) + (- 6.0 * ln(x) * ln(z) * x * z * NQCD) + 4.0 * ln(x) * ln(z) * (x * x) * NQCD + 2.0 * ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z) * NQCD + (- 4.0 * ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD) + 4.0 * ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD + (- 5. / 16. * ln(z) * (1.0 / x) * (1.0 / z) * NQCD) + (- 5. / 16. * ln(z) * (1.0 / x) * NQCD) + 5. / 16. * ln(z) * (1.0 / (z * z)) * NQCD + 23. / 4. * ln(z) * (1.0 / z) * (1.0 / NQCD) + 2.0 * ln(z) * (1.0 / z) * (1.0 / NQCD) * rln2 + (- 63. / 8. * ln(z) * (1.0 / z) * NQCD) + 4.0 * ln(z) * (1.0 / z) * NQCD * rln2 + 2.0 * ln(z) * (1.0 / NQCD) + 8.0 * ln(z) * (1.0 / NQCD) * rln2 + (- 33. / 8. * ln(z) * NQCD) + (- 2.0 * ln(z) * NQCD * rln2) + 1. / 4. * ln(z) * z * (1.0 / NQCD) + (- 4.0 * ln(z) * z * (1.0 / NQCD) * rln2) + 1. / 16. * ln(z) * z * NQCD + 4.0 * ln(z) * z * NQCD * rln2 + (- 5. / 16. * ln(z) * x * (1.0 / (z * z)) * NQCD) + (- 14.0 * ln(z) * x * (1.0 / z) * (1.0 / NQCD)) + (- 4.0 * ln(z) * x * (1.0 / z) * (1.0 / NQCD) * rln2) + 93. / 8. * ln(z) * x * (1.0 / z) * NQCD + (- 8.0 * ln(z) * x * (1.0 / z) * NQCD * rln2) + (- 3. / 2. * ln(z) * x * (1.0 / NQCD)) + (- 16.0 * ln(z) * x * (1.0 / NQCD) * rln2) + (- 7. / 8. * ln(z) * x * NQCD) + 4.0 * ln(z) * x * NQCD * rln2 + (- 2.0 * ln(z) * x * z * (1.0 / NQCD)) + 8.0 * ln(z) * x * z * (1.0 / NQCD) * rln2 + 27. / 16. * ln(z) * x * z * NQCD + (- 8.0 * ln(z) * x * z * NQCD * rln2) + 13.0 * ln(z) * (x * x) * (1.0 / z) * (1.0 / NQCD) + 4.0 * ln(z) * (x * x) * (1.0 / z) * (1.0 / NQCD) * rln2 + (- 131. / 16. * ln(z) * (x * x) * (1.0 / z) * NQCD) + 8.0 * ln(z) * (x * x) * (1.0 / z) * NQCD * rln2 + ln(z) * (x * x) * (1.0 / NQCD) + 8.0 * ln(z) * (x * x) * (1.0 / NQCD) * rln2 + 61. / 16. * ln(z) * (x * x) * NQCD + 4.0 * ln(z) * (x * x) * NQCD * rln2 + 2.0 * ln(z) * (x * x) * z * (1.0 / NQCD) + (- 8.0 * ln(z) * (x * x) * z * (1.0 / NQCD) * rln2) + (- 2.0 * ln(z) * (x * x) * z * NQCD) + 8.0 * ln(z) * (x * x) * z * NQCD * rln2 + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD) + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD)) + 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * NQCD + 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD) + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD) + 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD + 8.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD) + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + (- 2.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * (1.0 / NQCD)) + (- 2.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD) + (-4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD)) + 2.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD) + (- 2.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD) + 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * (1.0 / NQCD) + 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD + 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * NQCD) + 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + 2.0 * ln(z) * ln(1.0 - x) * (1.0 / NQCD) + (- 2.0 * ln(z) * ln(1.0 - x) * NQCD) + (- 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / NQCD)) + 4.0 * ln(z) * ln(1.0 - x) * x * NQCD + 4.0 * ln(z) * ln(1.0 - x) * (x * x) * (1.0 / NQCD) + (- 4.0 * ln(z) * ln(1.0 - x) * (x * x) * NQCD) + 2.0 * ln(z) * ln(1.0 + x * z) * (1.0 / z) * NQCD + (- 2.0 * ln(z) * ln(1.0 + x * z) * z * (1.0 / NQCD)) + 2.0 * ln(z) * ln(1.0 + x * z) * z * NQCD + (- 4.0 * ln(z) * ln(1.0 + x * z) * x * (1.0 / NQCD)) + 4.0 * ln(z) * ln(1.0 + x * z) * (x * x) * (1.0 / z) * NQCD + (- 4.0 * ln(z) * ln(1.0 + x * z) * (x * x) * z * (1.0 / NQCD)) + 4.0 * ln(z) * ln(1.0 + x * z) * (x * x) * z * NQCD + 2.0 * ln(z) * ln(z + x) * (1.0 / NQCD) + (- 4.0 * ln(z) * ln(z + x) * x * (1.0 / z) * NQCD) + 4.0 * ln(z) * ln(z + x) * x * z * (1.0 / NQCD) + (- 4.0 * ln(z) * ln(z + x) * x * z * NQCD) + 4.0 * ln(z) * ln(z + x) * (x * x) * NQCD + 3.0 * pow(ln(z), 2) * (1.0 / z) * (1.0 / NQCD) + (- pow(ln(z), 2) * (1.0 / z) * NQCD) + 1. / 2. * pow(ln(z), 2) * z * (1.0 / NQCD) + (- 1. / 2. * pow(ln(z), 2) * z * NQCD) + (- 6.0 * pow(ln(z), 2) * x * (1.0 / z) * (1.0 / NQCD)) + 4.0 * pow(ln(z), 2) * x * (1.0 / z) * NQCD + (- 2.0 * pow(ln(z), 2) * x * (1.0 / NQCD)) + (- 3.0 * pow(ln(z), 2) * x * z * (1.0 / NQCD)) + 3.0 * pow(ln(z), 2) * x * z * NQCD + 6.0 * pow(ln(z), 2) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * pow(ln(z), 2) * (x * x) * (1.0 / z) * NQCD) + 2.0 * pow(ln(z), 2) * (x * x) * (1.0 / NQCD) + (- 2.0 * pow(ln(z), 2) * (x * x) * NQCD) + pow(ln(z), 2) * (x * x) * z * (1.0 / NQCD) + (- pow(ln(z), 2) * (x * x) * z * NQCD) + 5. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + 9. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + (- 3.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 21. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + 5. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 3.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + 5. / 2. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD + 3.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 19. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + 45. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + (- 15.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 105. / 4. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 35. / 8. * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + 2.0 * ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z) * NQCD + (- 4.0 * ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD) + 4.0 * ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD + 2.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (1.0 / z) * (1.0 / NQCD) + 2.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * NQCD + (- 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD)) + (- 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * NQCD) + 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * (1.0 / z) * (1.0 / NQCD) + 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * NQCD + (- 2.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (1.0 / z) * (1.0 / NQCD)) + (- 2.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * NQCD) + 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / z) * (1.0 / NQCD) + 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * NQCD + (- 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + (- 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * NQCD) + (- 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD) + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD)) + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * NQCD + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD) + (- 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD) + 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD + 8.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD) + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD)) + 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD) + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD) + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / z) * NQCD + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * NQCD) + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * (1.0 / NQCD)) + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * z * NQCD + (- 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / z) * NQCD) + (- 8.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * NQCD + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / NQCD) + (- 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * NQCD) + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / z) * NQCD + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + (-4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * (1.0 / NQCD)) + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * z * NQCD + (- 2.0 * Li2(-x * (1.0 / z)) * (1.0 / NQCD)) + 4.0 * Li2(-x * (1.0 / z)) * x * (1.0 / z) * NQCD + (- 4.0 * Li2(-x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 4.0 * Li2(-x * (1.0 / z)) * x * z * NQCD + (- 4.0 * Li2(-x * (1.0 / z)) * (x * x) * NQCD) + (- 2.0 * Li2(-x) * (1.0 / z) * NQCD) + 2.0 * Li2(-x) * (1.0 / NQCD) + 2.0 * Li2(-x) * z * (1.0 / NQCD) + (- 2.0 * Li2(-x) * z * NQCD) + (- 4.0 * Li2(-x) * x * (1.0 / z) * NQCD) + 4.0 * Li2(-x) * x * (1.0 / NQCD) + 4.0 * Li2(-x) * x * z * (1.0 / NQCD) + (- 4.0 * Li2(-x) * x * z * NQCD) + (- 4.0 * Li2(-x) * (x * x) * (1.0 / z) * NQCD) + 4.0 * Li2(-x) * (x * x) * NQCD + 4.0 * Li2(-x) * (x * x) * z * (1.0 / NQCD) + (- 4.0 * Li2(-x) * (x * x) * z * NQCD) + 2.0 * Li2(-x * z) * (1.0 / z) * NQCD + (- 2.0 * Li2(-x * z) * z * (1.0 / NQCD)) + 2.0 * Li2(-x * z) * z * NQCD + (- 4.0 * Li2(-x * z) * x * (1.0 / NQCD)) + 4.0 * Li2(-x * z) * (x * x) * (1.0 / z) * NQCD + (- 4.0 * Li2(-x * z) * (x * x) * z * (1.0 / NQCD)) + 4.0 * Li2(-x * z) * (x * x) * z * NQCD + (- 1. / 2. * Li2(x) * (1.0 / z) * (1.0 / NQCD)) + 1. / 2. * Li2(x) * (1.0 / z) * NQCD + Li2(x) * (1.0 / NQCD) + (- Li2(x) * NQCD) + (- Li2(x) * z * (1.0 / NQCD)) + Li2(x) * z * NQCD + Li2(x) * x * (1.0 / z) * (1.0 / NQCD) + (- Li2(x) * x * (1.0 / z) * NQCD) + (- 2.0 * Li2(x) * x * (1.0 / NQCD)) + 2.0 * Li2(x) * x * NQCD + (- 2.0 * Li2(x) * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 2.0 * Li2(x) * (x * x) * (1.0 / z) * NQCD + 2.0 * Li2(x) * (x * x) * (1.0 / NQCD) + (- 2.0 * Li2(x) * (x * x) * NQCD) + (- 2.0 * Li2(x) * (x * x) * z * (1.0 / NQCD)) + 2.0 * Li2(x) * (x * x) * z * NQCD + (-2.0 * Li2(z) * (1.0 / NQCD)) + 2.0 * Li2(z) * NQCD + 4.0 * Li2(z) * x * (1.0 / NQCD) + (- 4.0 * Li2(z) * x * NQCD) + (- 4.0 * Li2(z) * (x * x) * (1.0 / NQCD)) + 4.0 * Li2(z) * (x * x) * NQCD + (- 5. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + (- 9. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + 3. / 2. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 21. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + (- 5. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 3. / 2. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + (- 5. / 4. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD) + (- 3. / 2. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 19. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + (- 45. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + 15. / 2. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 105. / 8. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 35. / 16. * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + 5. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD + 9. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD + (- 3. / 2. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD)) + 21. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD + 5. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD + 3. / 2. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD) + 5. / 4. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * NQCD + 3. / 2. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD) + (- 19. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD) + 45. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD + (- 15. / 2. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD)) + 105. / 8. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * x * z * NQCD + (- 35. / 16. * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD) + (- 5. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (x * x)) * NQCD) + (- 9. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * (1.0 / z) * NQCD) + 3.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * (1.0 / NQCD) + (- 21. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / x) * z * NQCD) + (- 5. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / (z * z)) * NQCD) + (- 3.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (1.0 / NQCD)) + (- 5. / 2. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * NQCD) + (- 3.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / NQCD)) + 19. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * NQCD + (-45. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * (1.0 / z) * NQCD) + 15.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * (1.0 / NQCD) + (- 105. / 4. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * x * z * NQCD) + 35. / 8. * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (x * x) * NQCD + 4.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z) * NQCD * rln2 + (- 8.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * NQCD * rln2) + 8.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (x * x) * (1.0 / z) * NQCD * rln2 + (- 4.0 / (1.0 - z) * ln(x) * ln(1.0 + x) * (1.0 / NQCD)) + (- 8.0 / (1.0 - z) * ln(x) * ln(1.0 + x) * x * (1.0 / NQCD)) + (- 4.0 / (1.0 - z) * ln(x) * ln(1.0 + x) * (x * x) * (1.0 / NQCD)) + 2.0 / (1.0 - z) * ln(x) * ln(1.0 + x * z) * (1.0 / NQCD) + 4.0 / (1.0 - z) * ln(x) * ln(1.0 + x * z) * x * (1.0 / NQCD) + 2.0 / (1.0 - z) * ln(x) * ln(1.0 + x * z) * (x * x) * (1.0 / NQCD) + 2.0 / (1.0 - z) * ln(x) * ln(z + x) * (1.0 / NQCD) + 4.0 / (1.0 - z) * ln(x) * ln(z + x) * x * (1.0 / NQCD) + 2.0 / (1.0 - z) * ln(x) * ln(z + x) * (x * x) * (1.0 / NQCD) + (- 2.0 / (1.0 - z) * ln(x) * ln(z) * (1.0 / NQCD)) + (- 4.0 / (1.0 - z) * ln(x) * ln(z) * x * (1.0 / NQCD)) + (- 2.0 / (1.0 - z) * ln(x) * ln(z) * (x * x) * (1.0 / NQCD)) + 2.0 / (1.0 - z) * ln(z) * ln(1.0 + x * z) * (1.0 / NQCD) + 4.0 / (1.0 - z) * ln(z) * ln(1.0 + x * z) * x * (1.0 / NQCD) + 2.0 / (1.0 - z) * ln(z) * ln(1.0 + x * z) * (x * x) * (1.0 / NQCD) + (- 2.0 / (1.0 - z) * ln(z) * ln(z + x) * (1.0 / NQCD)) + (- 4.0 / (1.0 - z) * ln(z) * ln(z + x) * x * (1.0 / NQCD)) + (- 2.0 / (1.0 - z) * ln(z) * ln(z + x) * (x * x) * (1.0 / NQCD)) + 2.0 / (1.0 - z) * pow(ln(z), 2) * (1.0 / NQCD) + 2.0 / (1.0 - z) * pow(ln(z), 2) * (x * x) * (1.0 / NQCD) + 2.0 / (1.0 - z) * Li2(-x * (1.0 / z)) * (1.0 / NQCD) + 4.0 / (1.0 - z) * Li2(-x * (1.0 / z)) * x * (1.0 / NQCD) + 2.0 / (1.0 - z) * Li2(-x * (1.0 / z)) * (x * x) * (1.0 / NQCD) + (- 4.0 / (1.0 - z) * Li2(-x) * (1.0 / NQCD)) + (- 8.0 / (1.0 - z) * Li2(-x) * x * (1.0 / NQCD)) + (- 4.0 / (1.0 - z) * Li2(-x) * (x * x) * (1.0 / NQCD)) + 2.0 / (1.0 - z) * Li2(-x * z) * (1.0 / NQCD) + 4.0 / (1.0 - z) * Li2(-x * z) * x * (1.0 / NQCD) + 2.0 / (1.0 - z) * Li2(-x * z) * (x * x) * (1.0 / NQCD) + (- 8.0 / (1.0 + z) * (1.0 / NQCD) * (rln2 * rln2)) + 16.0 / (1.0 + z) * x * (1.0 / NQCD) * (rln2 * rln2) + (- 8.0 / (1.0 + z) * (x * x) * (1.0 / NQCD) * (rln2 * rln2)) + 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) * rln2 + (- 16.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) * rln2) + 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) * rln2 + (- 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD)) + 16.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (- 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 8.0 / (1.0 + z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) * rln2 + (- 16.0 / (1.0 + z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) * rln2) + 8.0 / (1.0 + z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) * rln2 + (- 4.0 / (1.0 + z) * ln(x) * (1.0 / NQCD) * rln2) + 8.0 / (1.0 + z) * ln(x) * x * (1.0 / NQCD) * rln2 + (-4.0 / (1.0 + z) * ln(x) * (x * x) * (1.0 / NQCD) * rln2) + 4.0 / (1.0 + z) * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) + (- 8.0 / (1.0 + z) * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + 4.0 / (1.0 + z) * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * ln(x) * ln(1.0 + x * z) * (1.0 / NQCD)) + 4.0 / (1.0 + z) * ln(x) * ln(1.0 + x * z) * x * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * ln(x) * ln(1.0 + x * z) * (x * x) * (1.0 / NQCD)) + 2.0 / (1.0 + z) * ln(x) * ln(z + x) * (1.0 / NQCD) + (- 4.0 / (1.0 + z) * ln(x) * ln(z + x) * x * (1.0 / NQCD)) + 2.0 / (1.0 + z) * ln(x) * ln(z + x) * (x * x) * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * ln(x) * ln(z) * (1.0 / NQCD)) + 4.0 / (1.0 + z) * ln(x) * ln(z) * x * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * ln(x) * ln(z) * (x * x) * (1.0 / NQCD)) + (- 12.0 / (1.0 + z) * ln(z) * (1.0 / NQCD) * rln2) + 24.0 / (1.0 + z) * ln(z) * x * (1.0 / NQCD) * rln2 + (- 12.0 / (1.0 + z) * ln(z) * (x * x) * (1.0 / NQCD) * rln2) + 4.0 / (1.0 + z) * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) + (- 8.0 / (1.0 + z) * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + 4.0 / (1.0 + z) * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + 8.0 / (1.0 + z) * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) + (- 16.0 / (1.0 + z) * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + 8.0 / (1.0 + z) * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * ln(z) * ln(1.0 + x * z) * (1.0 / NQCD)) + 4.0 / (1.0 + z) * ln(z) * ln(1.0 + x * z) * x * (1.0 / NQCD) + (-2.0 / (1.0 + z) * ln(z) * ln(1.0 + x * z) * (x * x) * (1.0 / NQCD)) + (- 2.0 / (1.0 + z) * ln(z) * ln(z + x) * (1.0 / NQCD)) + 4.0 / (1.0 + z) * ln(z) * ln(z + x) * x * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * ln(z) * ln(z + x) * (x * x) * (1.0 / NQCD)) + (- 2.0 / (1.0 + z) * pow(ln(z), 2) * (1.0 / NQCD)) + 4.0 / (1.0 + z) * pow(ln(z), 2) * x * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * pow(ln(z), 2) * (x * x) * (1.0 / NQCD)) + (- 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (1.0 / NQCD)) + 8.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / NQCD) + (- 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * (1.0 / NQCD)) + 4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (1.0 / NQCD) + (- 8.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / NQCD)) + 4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * (x * x) * (1.0 / NQCD) + 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD) + (- 8.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD)) + 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD) + (- 4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (1.0 / NQCD)) + 8.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / NQCD) + (-4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * (x * x) * (1.0 / NQCD)) + 2.0 / (1.0 + z) * Li2(-x * (1.0 / z)) * (1.0 / NQCD) + (- 4.0 / (1.0 + z) * Li2(-x * (1.0 / z)) * x * (1.0 / NQCD)) + 2.0 / (1.0 + z) * Li2(-x * (1.0 / z)) * (x * x) * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * Li2(-x * z) * (1.0 / NQCD)) + 4.0 / (1.0 + z) * Li2(-x * z) * x * (1.0 / NQCD) + (- 2.0 / (1.0 + z) * Li2(-x * z) * (x * x) * (1.0 / NQCD));
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
        let tmp: f64 = (- 11. / 2. * lmua * (1.0 / z) * (1.0 / NQCD)) + 11. / 2. * lmua * (1.0 / z) * NQCD + 5.0 * lmua * (1.0 / NQCD) + (- 5.0 * lmua * NQCD) + 1. / 2. * lmua * z * (1.0 / NQCD) + (- 1. / 2. * lmua * z * NQCD) + 15.0 * lmua * x * (1.0 / z) * (1.0 / NQCD) + (- 15.0 * lmua * x * (1.0 / z) * NQCD) + (- 14.0 * lmua * x * (1.0 / NQCD)) + 14.0 * lmua * x * NQCD + lmua * x * z * (1.0 / NQCD) + (- lmua * x * z * NQCD) + (- 15.0 * lmua * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 15.0 * lmua * (x * x) * (1.0 / z) * NQCD + 14.0 * lmua * (x * x) * (1.0 / NQCD) + (- 14.0 * lmua * (x * x) * NQCD) + (- lmua * (x * x) * z * (1.0 / NQCD)) + lmua * (x * x) * z * NQCD + 2.0 * lmua * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * lmua * ln(1.0 - z) * (1.0 / z) * NQCD) + (- 2.0 * lmua * ln(1.0 - z) * (1.0 / NQCD)) + 2.0 * lmua * ln(1.0 - z) * NQCD + lmua * ln(1.0 - z) * z * (1.0 / NQCD) + (- lmua * ln(1.0 - z) * z * NQCD) + (- 4.0 * lmua * ln(1.0 - z) * x * (1.0 / z) * (1.0 / NQCD)) + 4.0 * lmua * ln(1.0 - z) * x * (1.0 / z) * NQCD + 4.0 * lmua * ln(1.0 - z) * x * (1.0 / NQCD) + (- 4.0 * lmua * ln(1.0 - z) * x * NQCD) + (- 2.0 * lmua * ln(1.0 - z) * x * z * (1.0 / NQCD)) + 2.0 * lmua * ln(1.0 - z) * x * z * NQCD + 4.0 * lmua * ln(1.0 - z) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * lmua * ln(1.0 - z) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * lmua * ln(1.0 - z) * (x * x) * (1.0 / NQCD)) + 4.0 * lmua * ln(1.0 - z) * (x * x) * NQCD + 2.0 * lmua * ln(1.0 - z) * (x * x) * z * (1.0 / NQCD) + (- 2.0 * lmua * ln(1.0 - z) * (x * x) * z * NQCD) + 2.0 * lmua * ln(1.0 - x) * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * lmua * ln(1.0 - x) * (1.0 / z) * NQCD) + (- 2.0 * lmua * ln(1.0 - x) * (1.0 / NQCD)) + 2.0 * lmua * ln(1.0 - x) * NQCD + lmua * ln(1.0 - x) * z * (1.0 / NQCD) + (- lmua * ln(1.0 - x) * z * NQCD) + (- 4.0 * lmua * ln(1.0 - x) * x * (1.0 / z) * (1.0 / NQCD)) + 4.0 * lmua * ln(1.0 - x) * x * (1.0 / z) * NQCD + 4.0 * lmua * ln(1.0 - x) * x * (1.0 / NQCD) + (- 4.0 * lmua * ln(1.0 - x) * x * NQCD) + (- 2.0 * lmua * ln(1.0 - x) * x * z * (1.0 / NQCD)) + 2.0 * lmua * ln(1.0 - x) * x * z * NQCD + 4.0 * lmua * ln(1.0 - x) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * lmua * ln(1.0 - x) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * lmua * ln(1.0 - x) * (x * x) * (1.0 / NQCD)) + 4.0 * lmua * ln(1.0 - x) * (x * x) * NQCD + 2.0 * lmua * ln(1.0 - x) * (x * x) * z * (1.0 / NQCD) + (- 2.0 * lmua * ln(1.0 - x) * (x * x) * z * NQCD) + (- 2.0 * ln(x) * lmua * (1.0 / z) * (1.0 / NQCD)) + 2.0 * ln(x) * lmua * (1.0 / z) * NQCD + 2.0 * ln(x) * lmua * (1.0 / NQCD) + (- 2.0 * ln(x) * lmua * NQCD) + (- ln(x) * lmua * z * (1.0 / NQCD)) + ln(x) * lmua * z * NQCD + 4.0 * ln(x) * lmua * x * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * ln(x) * lmua * x * (1.0 / z) * NQCD) + (- 4.0 * ln(x) * lmua * x * (1.0 / NQCD)) + 4.0 * ln(x) * lmua * x * NQCD + 2.0 * ln(x) * lmua * x * z * (1.0 / NQCD) + (- 2.0 * ln(x) * lmua * x * z * NQCD) + (- 4.0 * ln(x) * lmua * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 4.0 * ln(x) * lmua * (x * x) * (1.0 / z) * NQCD + 4.0 * ln(x) * lmua * (x * x) * (1.0 / NQCD) + (- 4.0 * ln(x) * lmua * (x * x) * NQCD) + (- 2.0 * ln(x) * lmua * (x * x) * z * (1.0 / NQCD)) + 2.0 * ln(x) * lmua * (x * x) * z * NQCD + (- 2.0 * ln(z) * lmua * (1.0 / z) * (1.0 / NQCD)) + 2.0 * ln(z) * lmua * (1.0 / z) * NQCD + (- 2.0 * ln(z) * lmua * (1.0 / NQCD)) + 2.0 * ln(z) * lmua * NQCD + (- ln(z) * lmua * z * (1.0 / NQCD)) + ln(z) * lmua * z * NQCD + 4.0 * ln(z) * lmua * x * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * ln(z) * lmua * x * (1.0 / z) * NQCD) + 4.0 * ln(z) * lmua * x * (1.0 / NQCD) + (- 4.0 * ln(z) * lmua * x * NQCD) + 2.0 * ln(z) * lmua * x * z * (1.0 / NQCD) + (- 2.0 * ln(z) * lmua * x * z * NQCD) + (- 4.0 * ln(z) * lmua * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 4.0 * ln(z) * lmua * (x * x) * (1.0 / z) * NQCD + (- 4.0 * ln(z) * lmua * (x * x) * (1.0 / NQCD)) + 4.0 * ln(z) * lmua * (x * x) * NQCD + (- 2.0 * ln(z) * lmua * (x * x) * z * (1.0 / NQCD)) + 2.0 * ln(z) * lmua * (x * x) * z * NQCD;
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
        let tmp: f64 = (- 2.0 * lmuf * (1.0 / z) * (1.0 / NQCD)) + 2.0 * lmuf * (1.0 / z) * NQCD + 2.0 * lmuf * (1.0 / NQCD) + (- 2.0 * lmuf * NQCD) + (- 2.0 * lmuf * z * (1.0 / NQCD)) + 2.0 * lmuf * z * NQCD + 5.0 * lmuf * x * (1.0 / z) * (1.0 / NQCD) + (- 5.0 * lmuf * x * (1.0 / z) * NQCD) + (- 2.0 * lmuf * x * (1.0 / NQCD)) + 2.0 * lmuf * x * NQCD + (- 3.0 * lmuf * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 3.0 * lmuf * (x * x) * (1.0 / z) * NQCD + 3.0 * lmuf * (x * x) * z * (1.0 / NQCD) + (- 3.0 * lmuf * (x * x) * z * NQCD) + 2.0 * lmuf * ln(1.0 - z) * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * lmuf * ln(1.0 - z) * (1.0 / z) * NQCD) + (- 2.0 * lmuf * ln(1.0 - z) * (1.0 / NQCD)) + 2.0 * lmuf * ln(1.0 - z) * NQCD + lmuf * ln(1.0 - z) * z * (1.0 / NQCD) + (- lmuf * ln(1.0 - z) * z * NQCD) + (- 4.0 * lmuf * ln(1.0 - z) * x * (1.0 / z) * (1.0 / NQCD)) + 4.0 * lmuf * ln(1.0 - z) * x * (1.0 / z) * NQCD + 4.0 * lmuf * ln(1.0 - z) * x * (1.0 / NQCD) + (- 4.0 * lmuf * ln(1.0 - z) * x * NQCD) + (- 2.0 * lmuf * ln(1.0 - z) * x * z * (1.0 / NQCD)) + 2.0 * lmuf * ln(1.0 - z) * x * z * NQCD + 4.0 * lmuf * ln(1.0 - z) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * lmuf * ln(1.0 - z) * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * lmuf * ln(1.0 - z) * (x * x) * (1.0 / NQCD)) + 4.0 * lmuf * ln(1.0 - z) * (x * x) * NQCD + 2.0 * lmuf * ln(1.0 - z) * (x * x) * z * (1.0 / NQCD) + (- 2.0 * lmuf * ln(1.0 - z) * (x * x) * z * NQCD) + 2.0 * lmuf * ln(1.0 - x) * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * lmuf * ln(1.0 - x) * (1.0 / z) * NQCD) + (- 2.0 * lmuf * ln(1.0 - x) * (1.0 / NQCD)) + 2.0 * lmuf * ln(1.0 - x) * NQCD + lmuf * ln(1.0 - x) * z * (1.0 / NQCD) + (- lmuf * ln(1.0 - x) * z * NQCD) + (- 4.0 * lmuf * ln(1.0 - x) * x * (1.0 / z) * (1.0 / NQCD)) + 4.0 * lmuf * ln(1.0 - x) * x * (1.0 / z) * NQCD + 4.0 * lmuf * ln(1.0 - x) * x * (1.0 / NQCD) + (- 4.0 * lmuf * ln(1.0 - x) * x * NQCD) + (- 2.0 * lmuf * ln(1.0 - x) * x * z * (1.0 / NQCD)) + 2.0 * lmuf * ln(1.0 - x) * x * z * NQCD + 4.0 * lmuf * ln(1.0 - x) * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * lmuf * ln(1.0 - x) * (x * x) * (1.0 / z) * NQCD) + (-4.0 * lmuf * ln(1.0 - x) * (x * x) * (1.0 / NQCD)) + 4.0 * lmuf * ln(1.0 - x) * (x * x) * NQCD + 2.0 * lmuf * ln(1.0 - x) * (x * x) * z * (1.0 / NQCD) + (- 2.0 * lmuf * ln(1.0 - x) * (x * x) * z * NQCD) + (- ln(x) * lmuf * (1.0 / z) * (1.0 / NQCD)) + ln(x) * lmuf * (1.0 / z) * NQCD + (-ln(x) * lmuf * z * (1.0 / NQCD)) + ln(x) * lmuf * z * NQCD + 2.0 * ln(x) * lmuf * x * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * ln(x) * lmuf * x * (1.0 / z) * NQCD) + (- 2.0 * ln(x) * lmuf * x * z * (1.0 / NQCD)) + 2.0 * ln(x) * lmuf * x * z * NQCD + (- 4.0 * ln(x) * lmuf * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 4.0 * ln(x) * lmuf * (x * x) * (1.0 / z) * NQCD + 4.0 * ln(x) * lmuf * (x * x) * (1.0 / NQCD) + (- 4.0 * ln(x) * lmuf * (x * x) * NQCD) + (- 2.0 * ln(x) * lmuf * (x * x) * z * (1.0 / NQCD)) + 2.0 * ln(x) * lmuf * (x * x) * z * NQCD + 2.0 * ln(z) * lmuf * (1.0 / z) * (1.0 / NQCD) + (- 2.0 * ln(z) * lmuf * (1.0 / z) * NQCD) + (- 2.0 * ln(z) * lmuf * (1.0 / NQCD)) + 2.0 * ln(z) * lmuf * NQCD + ln(z) * lmuf * z * (1.0 / NQCD) + (- ln(z) * lmuf * z * NQCD) + (- 4.0 * ln(z) * lmuf * x * (1.0 / z) * (1.0 / NQCD)) + 4.0 * ln(z) * lmuf * x * (1.0 / z) * NQCD + 4.0 * ln(z) * lmuf * x * (1.0 / NQCD) + (- 4.0 * ln(z) * lmuf * x * NQCD) + (- 2.0 * ln(z) * lmuf * x * z * (1.0 / NQCD)) + 2.0 * ln(z) * lmuf * x * z * NQCD + 4.0 * ln(z) * lmuf * (x * x) * (1.0 / z) * (1.0 / NQCD) + (- 4.0 * ln(z) * lmuf * (x * x) * (1.0 / z) * NQCD) + (- 4.0 * ln(z) * lmuf * (x * x) * (1.0 / NQCD)) + 4.0 * ln(z) * lmuf * (x * x) * NQCD + 2.0 * ln(z) * lmuf * (x * x) * z * (1.0 / NQCD) + (- 2.0 * ln(z) * lmuf * (x * x) * z * NQCD);
        res += tmp;
    }

    return res;
}

fn RG_RG_011(x: f64, z: f64, NF: f64) -> f64 {
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

        let pt0: f64 = RG_RG_011(x0, z0, NF);
        let pt1: f64 = RG_RG_011(x1, z1, NF);
        let pt2: f64 = RG_RG_011(x2, z2, NF);

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

        let pt0: f64 = RG_RG_011(x0, z0, NF);
        let pt1: f64 = RG_RG_011(x1, z1, NF);
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

        let pt0: f64 = RG_RG_011(x0, z0, NF);
        let pt1: f64 = RG_RG_011(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }

    if z != x && z != 1. - x {
        let tmp: f64 = (- 4.0 * lmuf * lmua * (1.0 / z) * (1.0 / NQCD)) + 4.0 * lmuf * lmua * (1.0 / z) * NQCD + 4.0 * lmuf * lmua * (1.0 / NQCD) + (- 4.0 * lmuf * lmua * NQCD) + (- 2.0 * lmuf * lmua * z * (1.0 / NQCD)) + 2.0 * lmuf * lmua * z * NQCD + 8.0 * lmuf * lmua * x * (1.0 / z) * (1.0 / NQCD) + (- 8.0 * lmuf * lmua * x * (1.0 / z) * NQCD) + (- 8.0 * lmuf * lmua * x * (1.0 / NQCD)) + 8.0 * lmuf * lmua * x * NQCD + 4.0 * lmuf * lmua * x * z * (1.0 / NQCD) + (- 4.0 * lmuf * lmua * x * z * NQCD) + (- 8.0 * lmuf * lmua * (x * x) * (1.0 / z) * (1.0 / NQCD)) + 8.0 * lmuf * lmua * (x * x) * (1.0 / z) * NQCD + 8.0 * lmuf * lmua * (x * x) * (1.0 / NQCD) + (- 8.0 * lmuf * lmua * (x * x) * NQCD) + (- 4.0 * lmuf * lmua * (x * x) * z * (1.0 / NQCD)) + 4.0 * lmuf * lmua * (x * x) * z * NQCD;
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("001", [RG_RG_001, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("010", [RG_RG_010, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("011", [RG_RG_011, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _])
);

/*
  SV mapping:
  - 000: RG_RG
    - 001: RG_RG
    - 010: RG_RG
    - 011: RG_RG
*/
