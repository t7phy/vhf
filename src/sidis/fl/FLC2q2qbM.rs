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
        let tmp: f64 = (-4.0 * z * (1.0 / (NQCD * NQCD))) + 4.0 * z + 8.0 * x * (1.0 / (NQCD * NQCD)) * (rln2 * rln2) + (- 8.0 * x * (rln2 * rln2)) + 4.0 * x * z * (1.0 / (NQCD * NQCD)) + (- 8.0 * x * z * (1.0 / (NQCD * NQCD)) * (rln2 * rln2)) + (- 4.0 * x * z) + 8.0 * x * z * (rln2 * rln2) + 1. / 3. * (pi * pi) * x * z * (1.0 / (NQCD * NQCD)) + (- 1. / 3. * (pi * pi) * x * z) + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) * rln2) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * rln2 + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD)) * rln2 + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * rln2) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + (- 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD))) + 8.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z + (- 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) * rln2) + 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * rln2 + 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD)) * rln2 + (- 8.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * rln2) + 8.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / (NQCD * NQCD)) + (- 8.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z)) + (- 8.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / (NQCD * NQCD))) + 8.0 * ln(mysqrt(x * (1.0 / z))) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) + (- 2.0 * ln(x) * z * (1.0 / (NQCD * NQCD))) + 2.0 * ln(x) * z + 4.0 * ln(x) * x * (1.0 / (NQCD * NQCD)) * rln2 + (- 4.0 * ln(x) * x * rln2) + (- 2.0 * ln(x) * x * z * (1.0 / (NQCD * NQCD))) + (- 4.0 * ln(x) * x * z * (1.0 / (NQCD * NQCD)) * rln2) + 2.0 * ln(x) * x * z + 4.0 * ln(x) * x * z * rln2 + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD))) + 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z) + (- 4.0 * ln(x) * ln(1.0 + x) * x * (1.0 / (NQCD * NQCD))) + 4.0 * ln(x) * ln(1.0 + x) * x + 4.0 * ln(x) * ln(1.0 + x * z) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(x) * ln(1.0 + x * z) * x) + 4.0 * ln(x) * ln(z + x) * x * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(x) * ln(z + x) * x * z) + (- pow(ln(x), 2) * x * z * (1.0 / (NQCD * NQCD))) + pow(ln(x), 2) * x * z + (- 6.0 * ln(x) * ln(z) * x * z * (1.0 / (NQCD * NQCD))) + 6.0 * ln(x) * ln(z) * x * z + (- 2.0 * ln(z) * z * (1.0 / (NQCD * NQCD))) + 2.0 * ln(z) * z + 12.0 * ln(z) * x * (1.0 / (NQCD * NQCD)) * rln2 + (- 12.0 * ln(z) * x * rln2) + 2.0 * ln(z) * x * z * (1.0 / (NQCD * NQCD)) + (- 12.0 * ln(z) * x * z * (1.0 / (NQCD * NQCD)) * rln2) + (- 2.0 * ln(z) * x * z) + 12.0 * ln(z) * x * z * rln2 + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD))) + 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z) + (- 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD))) + 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD)) + (- 8.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z) + 4.0 * ln(z) * ln(1.0 + x * z) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(z) * ln(1.0 + x * z) * x) + (- 4.0 * ln(z) * ln(z + x) * x * z * (1.0 / (NQCD * NQCD))) + 4.0 * ln(z) * ln(z + x) * x * z + 3.0 * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD)) + (- 3.0 * pow(ln(z), 2) * x) + (- pow(ln(z), 2) * x * z * (1.0 / (NQCD * NQCD))) + pow(ln(z), 2) * x * z + (- 8.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / (NQCD * NQCD))) + 8.0 * ln(z) * ArcTan(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) + 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x) + (- 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD))) + 4.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z + (- 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / (NQCD * NQCD))) + 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x + 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z) + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD))) + 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z) + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + (- 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (1.0 / (NQCD * NQCD))) + 4.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z + 4.0 * Li2(-x * (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * Li2(-x * (1.0 / z)) * x * z) + (- 4.0 * Li2(-x) * x * (1.0 / (NQCD * NQCD))) + 4.0 * Li2(-x) * x + 4.0 * Li2(-x * z) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 * Li2(-x * z) * x) + 4.0 * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / (NQCD * NQCD)) + (- 4.0 * InvTanInt(-mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z)) + (- 4.0 * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / (NQCD * NQCD))) + 4.0 * InvTanInt(mysqrt(x * (1.0 / z))) * mysqrt(x * (1.0 / z)) * (z * z) + 8.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z) * (1.0 / (NQCD * NQCD)) + (- 8.0 * InvTanInt(mysqrt(x * (1.0 / z)) * z) * mysqrt(x * (1.0 / z)) * (z * z)) + 4.0 / (1.0 - z) * ln(x) * ln(1.0 + x) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 - z) * ln(x) * ln(1.0 + x) * x) + (- 2.0 / (1.0 - z) * ln(x) * ln(1.0 + x * z) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 - z) * ln(x) * ln(1.0 + x * z) * x + (- 2.0 / (1.0 - z) * ln(x) * ln(z + x) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 - z) * ln(x) * ln(z + x) * x + 2.0 / (1.0 - z) * ln(x) * ln(z) * x * (1.0 / (NQCD * NQCD)) + (- 2.0 / (1.0 - z) * ln(x) * ln(z) * x) + (- 2.0 / (1.0 - z) * ln(z) * ln(1.0 + x * z) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 - z) * ln(z) * ln(1.0 + x * z) * x + 2.0 / (1.0 - z) * ln(z) * ln(z + x) * x * (1.0 / (NQCD * NQCD)) + (- 2.0 / (1.0 - z) * ln(z) * ln(z + x) * x) + (- 1.0 / (1.0 - z) * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD))) + 1.0 / (1.0 - z) * pow(ln(z), 2) * x + (- 2.0 / (1.0 - z) * Li2(-x * (1.0 / z)) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 - z) * Li2(-x * (1.0 / z)) * x + 4.0 / (1.0 - z) * Li2(-x) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 - z) * Li2(-x) * x) + (- 2.0 / (1.0 - z) * Li2(-x * z) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 - z) * Li2(-x * z) * x + (- 8.0 / (1.0 + z) * x * (1.0 / (NQCD * NQCD)) * (rln2 * rln2)) + 8.0 / (1.0 + z) * x * (rln2 * rln2) + 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) * rln2 + (- 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * rln2) + (- 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD))) + 8.0 / (1.0 + z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + 8.0 / (1.0 + z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) * rln2 + (- 8.0 / (1.0 + z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * rln2) + (- 4.0 / (1.0 + z) * ln(x) * x * (1.0 / (NQCD * NQCD)) * rln2) + 4.0 / (1.0 + z) * ln(x) * x * rln2 + 4.0 / (1.0 + z) * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 + z) * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + (- 2.0 / (1.0 + z) * ln(x) * ln(1.0 + x * z) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 + z) * ln(x) * ln(1.0 + x * z) * x + 2.0 / (1.0 + z) * ln(x) * ln(z + x) * x * (1.0 / (NQCD * NQCD)) + (- 2.0 / (1.0 + z) * ln(x) * ln(z + x) * x) + (- 2.0 / (1.0 + z) * ln(x) * ln(z) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 + z) * ln(x) * ln(z) * x + (-12.0 / (1.0 + z) * ln(z) * x * (1.0 / (NQCD * NQCD)) * rln2) + 12.0 / (1.0 + z) * ln(z) * x * rln2 + 4.0 / (1.0 + z) * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 + z) * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + 8.0 / (1.0 + z) * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) + (- 8.0 / (1.0 + z) * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + (- 2.0 / (1.0 + z) * ln(z) * ln(1.0 + x * z) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 + z) * ln(z) * ln(1.0 + x * z) * x + (- 2.0 / (1.0 + z) * ln(z) * ln(z + x) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 + z) * ln(z) * ln(z + x) * x + (- 2.0 / (1.0 + z) * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 + z) * pow(ln(z), 2) * x + (- 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / (NQCD * NQCD))) + 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x + 4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x) + 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + (- 4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (1.0 / (NQCD * NQCD))) + 4.0 / (1.0 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + 2.0 / (1.0 + z) * Li2(-x * (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) + (- 2.0 / (1.0 + z) * Li2(-x * (1.0 / z)) * x) + (-2.0 / (1.0 + z) * Li2(-x * z) * x * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 + z) * Li2(-x * z) * x;
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
