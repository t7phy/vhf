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

    if z < 1. - x && z < x {
        let tmp: f64 = -4. / 3. * (pi * pi) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 4. / 3. * (pi * pi) * x * (1.0 / z) + 3.0 * (pi * pi) * x * (1.0 / (NQCD * NQCD)) - 3.0 * (pi * pi) * x - 5. / 3. * (pi * pi) * x * z * (1.0 / (NQCD * NQCD)) + 5. / 3. * (pi * pi) * x * z - 8.0 * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * ln(1.0 - z) * x * z + 5.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 5.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) - 13.0 * pow(ln(1.0 - z), 2) * x * (1.0 / (NQCD * NQCD)) + 13.0 * pow(ln(1.0 - z), 2) * x + 8.0 * pow(ln(1.0 - z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * pow(ln(1.0 - z), 2) * x * z - 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * (1.0 / z) + 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x - 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z * (1.0 / (NQCD * NQCD)) + 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z - 6.0 * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - x) * x * z + 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) - 26.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 26.0 * ln(1.0 - x) * ln(1.0 - z) * x + 16.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 16.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) - 9.0 * pow(ln(1.0 - x), 2) * x * (1.0 / (NQCD * NQCD)) + 9.0 * pow(ln(1.0 - x), 2) * x + 5.0 * pow(ln(1.0 - x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 5.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * (1.0 / (NQCD * NQCD)) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * x * z - 12.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) + 34.0 * ln(x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) - 34.0 * ln(x) * ln(1.0 - z) * x - 22.0 * ln(x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) + 22.0 * ln(x) * ln(1.0 - z) * x * z + 2.0 * ln(x) * ln(1.0 - z - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * ln(x) * ln(1.0 - z - x) * x * (1.0 / z) - 6.0 * ln(x) * ln(1.0 - z - x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(x) * ln(1.0 - z - x) * x + 4.0 * ln(x) * ln(1.0 - z - x) * x * z * (1.0 / (NQCD * NQCD)) - 4.0 * ln(x) * ln(1.0 - z - x) * x * z - 12.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) + 32.0 * ln(x) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) - 32.0 * ln(x) * ln(1.0 - x) * x - 20.0 * ln(x) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) + 20.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(-z + x) * x * (1.0 / (NQCD * NQCD)) + 2.0 * ln(x) * ln(-z + x) * x + 2.0 * ln(x) * ln(-z + x) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * ln(x) * ln(-z + x) * x * z + 7.0 * pow(ln(x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 7.0 * pow(ln(x), 2) * x * (1.0 / z) - 20.0 * pow(ln(x), 2) * x * (1.0 / (NQCD * NQCD)) + 20.0 * pow(ln(x), 2) * x + 13.0 * pow(ln(x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 13.0 * pow(ln(x), 2) * x * z - 6.0 * ln(x) * ln(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 6.0 * ln(x) * ln(z) * x * (1.0 / z) + 22.0 * ln(x) * ln(z) * x * (1.0 / (NQCD * NQCD)) - 22.0 * ln(x) * ln(z) * x - 16.0 * ln(x) * ln(z) * x * z * (1.0 / (NQCD * NQCD)) + 16.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(z) * x * z + 4.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) - 16.0 * ln(z) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 16.0 * ln(z) * ln(1.0 - z) * x + 12.0 * ln(z) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 12.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) + -12.0 * ln(z) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 12.0 * ln(z) * ln(1.0 - x) * x + 8.0 * ln(z) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(-z + x) * x * (1.0 / (NQCD * NQCD)) - 2.0 * ln(z) * ln(-z + x) * x - 2.0 * ln(z) * ln(-z + x) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * ln(z) * ln(-z + x) * x * z + pow(ln(z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - pow(ln(z), 2) * x * (1.0 / z) - 6.0 * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD)) + 6.0 * pow(ln(z), 2) * x + 5.0 * pow(ln(z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 5.0 * pow(ln(z), 2) * x * z + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z + 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x - 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x * z - 2.0 * Li2(1.0 / (1.0 - x) * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * (1.0 / z) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * (1.0 / z) - 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * (1.0 / (NQCD * NQCD)) + 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z + 2.0 * Li2(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(z) * x * (1.0 / z) - 4.0 * Li2(z) * x * (1.0 / (NQCD * NQCD)) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z > 1. - x && z < x {
        let tmp: f64 = -4. / 3. * (pi * pi) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 4. / 3. * (pi * pi) * x * (1.0 / z) + 3.0 * (pi * pi) * x * (1.0 / (NQCD * NQCD)) - 3.0 * (pi * pi) * x - 5. / 3. * (pi * pi) * x * z * (1.0 / (NQCD * NQCD)) + 5. / 3. * (pi * pi) * x * z - 8.0 * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * ln(1.0 - z) * x * z - 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * (1.0 / z) + 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x - 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z * (1.0 / (NQCD * NQCD)) + 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z + 4.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) - 12.0 * pow(ln(1.0 - z), 2) * x * (1.0 / (NQCD * NQCD)) + 12.0 * pow(ln(1.0 - z), 2) * x + 8.0 * pow(ln(1.0 - z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * pow(ln(1.0 - z), 2) * x * z - 6.0 * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - x) * x * z + 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) - 20.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 20.0 * ln(1.0 - x) * ln(1.0 - z) * x + 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) - 9.0 * pow(ln(1.0 - x), 2) * x * (1.0 / (NQCD * NQCD)) + 9.0 * pow(ln(1.0 - x), 2) * x + 5.0 * pow(ln(1.0 - x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 5.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * (1.0 / (NQCD * NQCD)) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * x * z + 2.0 * ln(x) * ln(-1.0 + z + x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + -2.0 * ln(x) * ln(-1.0 + z + x) * x * (1.0 / z) - 6.0 * ln(x) * ln(-1.0 + z + x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(x) * ln(-1.0 + z + x) * x + 4.0 * ln(x) * ln(-1.0 + z + x) * x * z * (1.0 / (NQCD * NQCD)) - 4.0 * ln(x) * ln(-1.0 + z + x) * x * z - 10.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 10.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) + 32.0 * ln(x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) - 32.0 * ln(x) * ln(1.0 - z) * x - 22.0 * ln(x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) + 22.0 * ln(x) * ln(1.0 - z) * x * z - 10.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 10.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) + 26.0 * ln(x) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) - 26.0 * ln(x) * ln(1.0 - x) * x - 16.0 * ln(x) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) + 16.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(-z + x) * x * (1.0 / (NQCD * NQCD)) + 2.0 * ln(x) * ln(-z + x) * x + 2.0 * ln(x) * ln(-z + x) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * ln(x) * ln(-z + x) * x * z + 6.0 * pow(ln(x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 6.0 * pow(ln(x), 2) * x * (1.0 / z) - 19.0 * pow(ln(x), 2) * x * (1.0 / (NQCD * NQCD)) + 19.0 * pow(ln(x), 2) * x + 13.0 * pow(ln(x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 13.0 * pow(ln(x), 2) * x * z - 8.0 * ln(x) * ln(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 8.0 * ln(x) * ln(z) * x * (1.0 / z) + 28.0 * ln(x) * ln(z) * x * (1.0 / (NQCD * NQCD)) - 28.0 * ln(x) * ln(z) * x - 20.0 * ln(x) * ln(z) * x * z * (1.0 / (NQCD * NQCD)) + 20.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(z) * x * z + 6.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 6.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) - 22.0 * ln(z) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 22.0 * ln(z) * ln(1.0 - z) * x + 16.0 * ln(z) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 16.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + -4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) - 12.0 * ln(z) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 12.0 * ln(z) * ln(1.0 - x) * x + 8.0 * ln(z) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(-z + x) * x * (1.0 / (NQCD * NQCD)) - 2.0 * ln(z) * ln(-z + x) * x - 2.0 * ln(z) * ln(-z + x) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * ln(z) * ln(-z + x) * x * z + pow(ln(z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - pow(ln(z), 2) * x * (1.0 / z) - 6.0 * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD)) + 6.0 * pow(ln(z), 2) * x + 5.0 * pow(ln(z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 5.0 * pow(ln(z), 2) * x * z - 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * (1.0 / z) + 4.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) - 4.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x - 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * z + 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x * (1.0 / z) - 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) + 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z - 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x + 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x * z + 2.0 * Li2(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(z) * x * (1.0 / z) - 4.0 * Li2(z) * x * (1.0 / (NQCD * NQCD)) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z < 1. - x && z > x {
        let tmp: f64 = -4. / 3. * (pi * pi) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 4. / 3. * (pi * pi) * x * (1.0 / z) + 13. / 3. * (pi * pi) * x * (1.0 / (NQCD * NQCD)) - 13. / 3. * (pi * pi) * x - 3.0 * (pi * pi) * x * z * (1.0 / (NQCD * NQCD)) + 3.0 * (pi * pi) * x * z - 8.0 * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * ln(1.0 - z) * x * z + 5.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 5.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) - 15.0 * pow(ln(1.0 - z), 2) * x * (1.0 / (NQCD * NQCD)) + 15.0 * pow(ln(1.0 - z), 2) * x + 10.0 * pow(ln(1.0 - z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 10.0 * pow(ln(1.0 - z), 2) * x * z - 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * (1.0 / z) + 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x - 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z * (1.0 / (NQCD * NQCD)) + 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z - 6.0 * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - x) * x * z + 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) - 22.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 22.0 * ln(1.0 - x) * ln(1.0 - z) * x + 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) - 11.0 * pow(ln(1.0 - x), 2) * x * (1.0 / (NQCD * NQCD)) + 11.0 * pow(ln(1.0 - x), 2) * x + 7.0 * pow(ln(1.0 - x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 7.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * (1.0 / (NQCD * NQCD)) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * x * z - 12.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) + 36.0 * ln(x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) - 36.0 * ln(x) * ln(1.0 - z) * x - 24.0 * ln(x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) + 24.0 * ln(x) * ln(1.0 - z) * x * z + 2.0 * ln(x) * ln(1.0 - z - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * ln(x) * ln(1.0 - z - x) * x * (1.0 / z) - 6.0 * ln(x) * ln(1.0 - z - x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(x) * ln(1.0 - z - x) * x + 4.0 * ln(x) * ln(1.0 - z - x) * x * z * (1.0 / (NQCD * NQCD)) - 4.0 * ln(x) * ln(1.0 - z - x) * x * z - 12.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) + 30.0 * ln(x) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) - 30.0 * ln(x) * ln(1.0 - x) * x - 18.0 * ln(x) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) + 18.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(z - x) * x * (1.0 / (NQCD * NQCD)) + 2.0 * ln(x) * ln(z - x) * x + 2.0 * ln(x) * ln(z - x) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * ln(x) * ln(z - x) * x * z + 7.0 * pow(ln(x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 7.0 * pow(ln(x), 2) * x * (1.0 / z) - 21.0 * pow(ln(x), 2) * x * (1.0 / (NQCD * NQCD)) + 21.0 * pow(ln(x), 2) * x + 14.0 * pow(ln(x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 14.0 * pow(ln(x), 2) * x * z - 6.0 * ln(x) * ln(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 6.0 * ln(x) * ln(z) * x * (1.0 / z) + 24.0 * ln(x) * ln(z) * x * (1.0 / (NQCD * NQCD)) - 24.0 * ln(x) * ln(z) * x - 18.0 * ln(x) * ln(z) * x * z * (1.0 / (NQCD * NQCD)) + 18.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(z) * x * z + 4.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) - 18.0 * ln(z) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 18.0 * ln(z) * ln(1.0 - z) * x + 14.0 * ln(z) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 14.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) + -10.0 * ln(z) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 10.0 * ln(z) * ln(1.0 - x) * x + 6.0 * ln(z) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(z - x) * x * (1.0 / (NQCD * NQCD)) - 2.0 * ln(z) * ln(z - x) * x - 2.0 * ln(z) * ln(z - x) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * ln(z) * ln(z - x) * x * z + pow(ln(z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - pow(ln(z), 2) * x * (1.0 / z) - 7.0 * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD)) + 7.0 * pow(ln(z), 2) * x + 6.0 * pow(ln(z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * pow(ln(z), 2) * x * z - 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x + 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - z) * x * (1.0 / z) - 1.0 / (1.0 - z) * (x * x) * (1.0 / z)) * x * z - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z - 2.0 * Li2(1.0 / (1.0 - x) * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * (1.0 / z) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * (1.0 / z) - 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * (1.0 / (NQCD * NQCD)) + 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z + 2.0 * Li2(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(z) * x * (1.0 / z) - 4.0 * Li2(z) * x * (1.0 / (NQCD * NQCD)) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * (1.0 / (NQCD * NQCD)) + -2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z > 1. - x && z > x {
        let tmp: f64 = -4. / 3. * (pi * pi) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 4. / 3. * (pi * pi) * x * (1.0 / z) + 3.0 * (pi * pi) * x * (1.0 / (NQCD * NQCD)) - 3.0 * (pi * pi) * x - 5. / 3. * (pi * pi) * x * z * (1.0 / (NQCD * NQCD)) + 5. / 3. * (pi * pi) * x * z - 8.0 * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * ln(1.0 - z) * x * z - 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * (1.0 / z) + 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x - 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z * (1.0 / (NQCD * NQCD)) + 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z + 4.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) - 12.0 * pow(ln(1.0 - z), 2) * x * (1.0 / (NQCD * NQCD)) + 12.0 * pow(ln(1.0 - z), 2) * x + 8.0 * pow(ln(1.0 - z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 8.0 * pow(ln(1.0 - z), 2) * x * z - 6.0 * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(1.0 - x) * x * z + 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) - 20.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 20.0 * ln(1.0 - x) * ln(1.0 - z) * x + 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) - 9.0 * pow(ln(1.0 - x), 2) * x * (1.0 / (NQCD * NQCD)) + 9.0 * pow(ln(1.0 - x), 2) * x + 5.0 * pow(ln(1.0 - x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 5.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * (1.0 / (NQCD * NQCD)) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * (1.0 / (NQCD * NQCD)) + 12.0 * ln(x) * x * z + 2.0 * ln(x) * ln(-1.0 + z + x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + -2.0 * ln(x) * ln(-1.0 + z + x) * x * (1.0 / z) - 6.0 * ln(x) * ln(-1.0 + z + x) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(x) * ln(-1.0 + z + x) * x + 4.0 * ln(x) * ln(-1.0 + z + x) * x * z * (1.0 / (NQCD * NQCD)) - 4.0 * ln(x) * ln(-1.0 + z + x) * x * z - 10.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 10.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) + 30.0 * ln(x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) - 30.0 * ln(x) * ln(1.0 - z) * x - 20.0 * ln(x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) + 20.0 * ln(x) * ln(1.0 - z) * x * z - 10.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 10.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) + 28.0 * ln(x) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) - 28.0 * ln(x) * ln(1.0 - x) * x - 18.0 * ln(x) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) + 18.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(z - x) * x * (1.0 / (NQCD * NQCD)) + 2.0 * ln(x) * ln(z - x) * x + 2.0 * ln(x) * ln(z - x) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * ln(x) * ln(z - x) * x * z + 6.0 * pow(ln(x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 6.0 * pow(ln(x), 2) * x * (1.0 / z) - 18.0 * pow(ln(x), 2) * x * (1.0 / (NQCD * NQCD)) + 18.0 * pow(ln(x), 2) * x + 12.0 * pow(ln(x), 2) * x * z * (1.0 / (NQCD * NQCD)) - 12.0 * pow(ln(x), 2) * x * z - 8.0 * ln(x) * ln(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 8.0 * ln(x) * ln(z) * x * (1.0 / z) + 26.0 * ln(x) * ln(z) * x * (1.0 / (NQCD * NQCD)) - 26.0 * ln(x) * ln(z) * x - 18.0 * ln(x) * ln(z) * x * z * (1.0 / (NQCD * NQCD)) + 18.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * (1.0 / (NQCD * NQCD)) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * (1.0 / (NQCD * NQCD)) - 6.0 * ln(z) * x * z + 6.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 6.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) - 20.0 * ln(z) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + 20.0 * ln(z) * ln(1.0 - z) * x + 14.0 * ln(z) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) - 14.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + -4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) - 14.0 * ln(z) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + 14.0 * ln(z) * ln(1.0 - x) * x + 10.0 * ln(z) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) - 10.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(z - x) * x * (1.0 / (NQCD * NQCD)) - 2.0 * ln(z) * ln(z - x) * x - 2.0 * ln(z) * ln(z - x) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * ln(z) * ln(z - x) * x * z + pow(ln(z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - pow(ln(z), 2) * x * (1.0 / z) - 5.0 * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD)) + 5.0 * pow(ln(z), 2) * x + 4.0 * pow(ln(z), 2) * x * z * (1.0 / (NQCD * NQCD)) - 4.0 * pow(ln(z), 2) * x * z - 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * (1.0 / z) + 4.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) - 4.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x - 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 + (1.0 / x) * (1.0 / z) - (1.0 / x) - (1.0 / z)) * x * z + 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x * (1.0 / z) - 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x * (1.0 / (NQCD * NQCD)) + 2.0 * Li2((1.0 / z) - x * (1.0 / z)) * x - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z + 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x - 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x * z * (1.0 / (NQCD * NQCD)) + 2.0 * Li2(1.0 / (1.0 - x) * (1.0 / x) * z - 1.0 / (1.0 - x) * (1.0 / x) * (z * z)) * x * z + 2.0 * Li2(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(z) * x * (1.0 / z) - 4.0 * Li2(z) * x * (1.0 / (NQCD * NQCD)) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * (1.0 / (NQCD * NQCD)) - 2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z > x {
        let tmp: f64 = -(pi * pi) * x + (pi * pi) * x * (NQCD * NQCD) + (pi * pi) * x * z - (pi * pi) * x * z * (NQCD * NQCD) - 2.0 * ln(1.0 - z) * x * z + 2.0 * ln(1.0 - z) * x * z * (NQCD * NQCD) + pow(ln(1.0 - z), 2) * x - pow(ln(1.0 - z), 2) * x * (NQCD * NQCD) - pow(ln(1.0 - z), 2) * x * z + pow(ln(1.0 - z), 2) * x * z * (NQCD * NQCD) - 4.0 * ln(1.0 - x) * x * z + 4.0 * ln(1.0 - x) * x * z * (NQCD * NQCD) + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * (NQCD * NQCD) - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (NQCD * NQCD) + 4.0 * pow(ln(1.0 - x), 2) * x - 4.0 * pow(ln(1.0 - x), 2) * x * (NQCD * NQCD) - 4.0 * pow(ln(1.0 - x), 2) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * z * (NQCD * NQCD) + 6.0 * ln(x) * x * z - 6.0 * ln(x) * x * z * (NQCD * NQCD) - 6.0 * ln(x) * ln(1.0 - z) * x + 6.0 * ln(x) * ln(1.0 - z) * x * (NQCD * NQCD) + 6.0 * ln(x) * ln(1.0 - z) * x * z - 6.0 * ln(x) * ln(1.0 - z) * x * z * (NQCD * NQCD) - 12.0 * ln(x) * ln(1.0 - x) * x + 12.0 * ln(x) * ln(1.0 - x) * x * (NQCD * NQCD) + 12.0 * ln(x) * ln(1.0 - x) * x * z - 12.0 * ln(x) * ln(1.0 - x) * x * z * (NQCD * NQCD) + 2.0 * ln(x) * ln(z - x) * x - 2.0 * ln(x) * ln(z - x) * x * (NQCD * NQCD) - 2.0 * ln(x) * ln(z - x) * x * z + 2.0 * ln(x) * ln(z - x) * x * z * (NQCD * NQCD) + 7.0 * pow(ln(x), 2) * x - 7.0 * pow(ln(x), 2) * x * (NQCD * NQCD) - 7.0 * pow(ln(x), 2) * x * z + 7.0 * pow(ln(x), 2) * x * z * (NQCD * NQCD) - 12.0 * ln(x) * ln(z) * x + 12.0 * ln(x) * ln(z) * x * (NQCD * NQCD) + 12.0 * ln(x) * ln(z) * x * z - 12.0 * ln(x) * ln(z) * x * z * (NQCD * NQCD) - 4.0 * ln(z) * x * z + 4.0 * ln(z) * x * z * (NQCD * NQCD) + 2.0 * ln(z) * ln(1.0 - z) * x - 2.0 * ln(z) * ln(1.0 - z) * x * (NQCD * NQCD) - 2.0 * ln(z) * ln(1.0 - z) * x * z + 2.0 * ln(z) * ln(1.0 - z) * x * z * (NQCD * NQCD) + 10.0 * ln(z) * ln(1.0 - x) * x - 10.0 * ln(z) * ln(1.0 - x) * x * (NQCD * NQCD) - 10.0 * ln(z) * ln(1.0 - x) * x * z + 10.0 * ln(z) * ln(1.0 - x) * x * z * (NQCD * NQCD) - 2.0 * ln(z) * ln(z - x) * x + 2.0 * ln(z) * ln(z - x) * x * (NQCD * NQCD) + 2.0 * ln(z) * ln(z - x) * x * z - 2.0 * ln(z) * ln(z - x) * x * z * (NQCD * NQCD) + 5.0 * pow(ln(z), 2) * x - 5.0 * pow(ln(z), 2) * x * (NQCD * NQCD) - 5.0 * pow(ln(z), 2) * x * z + 5.0 * pow(ln(z), 2) * x * z * (NQCD * NQCD) - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * (NQCD * NQCD) + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z * (NQCD * NQCD) + 2.0 * Li2(1.0 / (1.0 - x) * x * (1.0 / z) - 1.0 / (1.0 - x) * x) * x - 2.0 * Li2(1.0 / (1.0 - x) * x * (1.0 / z) - 1.0 / (1.0 - x) * x) * x * (NQCD * NQCD) - 2.0 * Li2(1.0 / (1.0 - x) * x * (1.0 / z) - 1.0 / (1.0 - x) * x) * x * z + 2.0 * Li2(1.0 / (1.0 - x) * x * (1.0 / z) - 1.0 / (1.0 - x) * x) * x * z * (NQCD * NQCD) - 2.0 * Li2(z) * x + 2.0 * Li2(z) * x * (NQCD * NQCD) + 2.0 * Li2(z) * x * z - 2.0 * Li2(z) * x * z * (NQCD * NQCD);
        res += tmp;
    }

    if z < x {
        let tmp: f64 = -(pi * pi) * x + (pi * pi) * x * (NQCD * NQCD) + (pi * pi) * x * z - (pi * pi) * x * z * (NQCD * NQCD) - 2.0 * ln(1.0 - z) * x * z + 2.0 * ln(1.0 - z) * x * z * (NQCD * NQCD) + pow(ln(1.0 - z), 2) * x - pow(ln(1.0 - z), 2) * x * (NQCD * NQCD) - pow(ln(1.0 - z), 2) * x * z + pow(ln(1.0 - z), 2) * x * z * (NQCD * NQCD) - 4.0 * ln(1.0 - x) * x * z + 4.0 * ln(1.0 - x) * x * z * (NQCD * NQCD) + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * (NQCD * NQCD) - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (NQCD * NQCD) + 4.0 * pow(ln(1.0 - x), 2) * x - 4.0 * pow(ln(1.0 - x), 2) * x * (NQCD * NQCD) - 4.0 * pow(ln(1.0 - x), 2) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * z * (NQCD * NQCD) + 6.0 * ln(x) * x * z - 6.0 * ln(x) * x * z * (NQCD * NQCD) - 8.0 * ln(x) * ln(1.0 - z) * x + 8.0 * ln(x) * ln(1.0 - z) * x * (NQCD * NQCD) + 8.0 * ln(x) * ln(1.0 - z) * x * z - 8.0 * ln(x) * ln(1.0 - z) * x * z * (NQCD * NQCD) - 10.0 * ln(x) * ln(1.0 - x) * x + 10.0 * ln(x) * ln(1.0 - x) * x * (NQCD * NQCD) + 10.0 * ln(x) * ln(1.0 - x) * x * z - 10.0 * ln(x) * ln(1.0 - x) * x * z * (NQCD * NQCD) + 2.0 * ln(x) * ln(-z + x) * x - 2.0 * ln(x) * ln(-z + x) * x * (NQCD * NQCD) - 2.0 * ln(x) * ln(-z + x) * x * z + 2.0 * ln(x) * ln(-z + x) * x * z * (NQCD * NQCD) + 6.0 * pow(ln(x), 2) * x - 6.0 * pow(ln(x), 2) * x * (NQCD * NQCD) - 6.0 * pow(ln(x), 2) * x * z + 6.0 * pow(ln(x), 2) * x * z * (NQCD * NQCD) - 10.0 * ln(x) * ln(z) * x + 10.0 * ln(x) * ln(z) * x * (NQCD * NQCD) + 10.0 * ln(x) * ln(z) * x * z - 10.0 * ln(x) * ln(z) * x * z * (NQCD * NQCD) - 4.0 * ln(z) * x * z + 4.0 * ln(z) * x * z * (NQCD * NQCD) + 4.0 * ln(z) * ln(1.0 - z) * x - 4.0 * ln(z) * ln(1.0 - z) * x * (NQCD * NQCD) - 4.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - z) * x * z * (NQCD * NQCD) + 8.0 * ln(z) * ln(1.0 - x) * x - 8.0 * ln(z) * ln(1.0 - x) * x * (NQCD * NQCD) - 8.0 * ln(z) * ln(1.0 - x) * x * z + 8.0 * ln(z) * ln(1.0 - x) * x * z * (NQCD * NQCD) - 2.0 * ln(z) * ln(-z + x) * x + 2.0 * ln(z) * ln(-z + x) * x * (NQCD * NQCD) + 2.0 * ln(z) * ln(-z + x) * x * z - 2.0 * ln(z) * ln(-z + x) * x * z * (NQCD * NQCD) + 4.0 * pow(ln(z), 2) * x - 4.0 * pow(ln(z), 2) * x * (NQCD * NQCD) - 4.0 * pow(ln(z), 2) * x * z + 4.0 * pow(ln(z), 2) * x * z * (NQCD * NQCD) + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * (NQCD * NQCD) - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z * (NQCD * NQCD) - 2.0 * Li2(1.0 / (1.0 - z) * (1.0 / x) * z - 1.0 / (1.0 - z) * z) * x + 2.0 * Li2(1.0 / (1.0 - z) * (1.0 / x) * z - 1.0 / (1.0 - z) * z) * x * (NQCD * NQCD) + 2.0 * Li2(1.0 / (1.0 - z) * (1.0 / x) * z - 1.0 / (1.0 - z) * z) * x * z - 2.0 * Li2(1.0 / (1.0 - z) * (1.0 / x) * z - 1.0 / (1.0 - z) * z) * x * z * (NQCD * NQCD) - 2.0 * Li2(z) * x + 2.0 * Li2(z) * x * (NQCD * NQCD) + 2.0 * Li2(z) * x * z - 2.0 * Li2(z) * x * z * (NQCD * NQCD);
        res += tmp;
    }

    if z != x && z != 1. - x {
        let tmp: f64 = (-6.0) + 1. / 2. * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- (1.0 / z)) + 1. / 2. * (1.0 / z) * (NQCD * NQCD) + (1.0 / (NQCD * NQCD)) + 5.0 * (NQCD * NQCD) + 1. / 2. * z * (1.0 / (NQCD * NQCD)) + 3.0 * z + (- 7. / 2. * z * (NQCD * NQCD)) + (- 2.0 * (z * z) * (1.0 / (NQCD * NQCD))) + 4.0 * (z * z) + (- 2.0 * (z * z) * (NQCD * NQCD)) + (- 1. / 2. * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + (- 3.0 * x * (1.0 / z)) + 7. / 2. * x * (1.0 / z) * (NQCD * NQCD) + (- 17. / 2. * x * (1.0 / (NQCD * NQCD))) + 20.0 * x + (- 4.0 * x * (rln2 * rln2)) + (- 23. / 2. * x * (NQCD * NQCD)) + 4.0 * x * (NQCD * NQCD) * (rln2 * rln2) + 9.0 * x * z * (1.0 / (NQCD * NQCD)) + (- 12.0 * x * z) + (- 4.0 * x * z * (rln2 * rln2)) + 3.0 * x * z * (NQCD * NQCD) + 4.0 * x * z * (NQCD * NQCD) * (rln2 * rln2) + (- 5.0 * x * (z * z)) + 5.0 * x * (z * z) * (NQCD * NQCD) + 4. / 3. * (pi * pi) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 4. / 3. * (pi * pi) * x * (1.0 / z)) + (- 23. / 6. * (pi * pi) * x * (1.0 / (NQCD * NQCD))) + 13. / 3. * (pi * pi) * x + (- 1. / 2. * (pi * pi) * x * (NQCD * NQCD)) + 7. / 3. * (pi * pi) * x * z * (1.0 / (NQCD * NQCD)) + (- 14. / 3. * (pi * pi) * x * z) + 7. / 3. * (pi * pi) * x * z * (NQCD * NQCD) + (- 2.0 * ln(1.0 - z)) + ln(1.0 - z) * (1.0 / (NQCD * NQCD)) + ln(1.0 - z) * (NQCD * NQCD) + ln(1.0 - z) * z * (1.0 / (NQCD * NQCD)) + (- ln(1.0 - z) * z * (NQCD * NQCD)) + (- 2.0 * ln(1.0 - z) * (z * z) * (1.0 / (NQCD * NQCD))) + 2.0 * ln(1.0 - z) * (z * z) + ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(1.0 - z) * x * (1.0 / z)) + 3.0 * ln(1.0 - z) * x * (1.0 / z) * (NQCD * NQCD) + 7. / 2. * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + (- ln(1.0 - z) * x) + (- 5. / 2. * ln(1.0 - z) * x * (NQCD * NQCD)) + (- 9. / 2. * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD))) + 5.0 * ln(1.0 - z) * x * z + (- 1. / 2. * ln(1.0 - z) * x * z * (NQCD * NQCD)) + 2.0 * ln(1.0 - z) * x * (z * z) + (- 2.0 * ln(1.0 - z) * x * (z * z) * (NQCD * NQCD)) + (- 4.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 4.0 * pow(ln(1.0 - z), 2) * x * (1.0 / z) + 12.0 * pow(ln(1.0 - z), 2) * x * (1.0 / (NQCD * NQCD)) + (- 15.0 * pow(ln(1.0 - z), 2) * x) + 3.0 * pow(ln(1.0 - z), 2) * x * (NQCD * NQCD) + (- 8.0 * pow(ln(1.0 - z), 2) * x * z * (1.0 / (NQCD * NQCD))) + 11.0 * pow(ln(1.0 - z), 2) * x * z + (- 3.0 * pow(ln(1.0 - z), 2) * x * z * (NQCD * NQCD)) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * rln2 + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD) * rln2) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * rln2 + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD) * rln2) + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD) + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z) + 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD) + 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z)) + 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / (NQCD * NQCD)) + 2.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x + (- 4.0 * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (NQCD * NQCD)) + 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * rln2 + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD) * rln2) + 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * rln2 + (- 4.0 * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD) * rln2) + (- 2.0 * ln(1.0 - x)) + ln(1.0 - x) * (1.0 / (NQCD * NQCD)) + ln(1.0 - x) * (NQCD * NQCD) + (- ln(1.0 - x) * z * (1.0 / (NQCD * NQCD))) + 2.0 * ln(1.0 - x) * z + (- ln(1.0 - x) * z * (NQCD * NQCD)) + ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(1.0 - x) * x * (1.0 / z)) + 3.0 * ln(1.0 - x) * x * (1.0 / z) * (NQCD * NQCD) + 7. / 2. * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + (- 3.0 * ln(1.0 - x) * x) + (- 1. / 2. * ln(1.0 - x) * x * (NQCD * NQCD)) + (- 9. / 2. * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD))) + 9.0 * ln(1.0 - x) * x * z + (- 9. / 2. * ln(1.0 - x) * x * z * (NQCD * NQCD)) + 2.0 * ln(1.0 - x) * x * (z * z) + (- 2.0 * ln(1.0 - x) * x * (z * z) * (NQCD * NQCD)) + (- 6.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 6.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / z) + 18.0 * ln(1.0 - x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + (- 26.0 * ln(1.0 - x) * ln(1.0 - z) * x) + 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * (NQCD * NQCD) + (- 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD))) + 20.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + (- 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * (NQCD * NQCD)) + (- 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 4.0 * pow(ln(1.0 - x), 2) * x * (1.0 / z) + 10.0 * pow(ln(1.0 - x), 2) * x * (1.0 / (NQCD * NQCD)) + (- 15.0 * pow(ln(1.0 - x), 2) * x) + 5.0 * pow(ln(1.0 - x), 2) * x * (NQCD * NQCD) + (- 6.0 * pow(ln(1.0 - x), 2) * x * z * (1.0 / (NQCD * NQCD))) + 11.0 * pow(ln(1.0 - x), 2) * x * z + (- 5.0 * pow(ln(1.0 - x), 2) * x * z * (NQCD * NQCD)) + 2.0 * ln(x) + (- ln(x) * (1.0 / (NQCD * NQCD))) + (- ln(x) * (NQCD * NQCD)) + (- ln(x) * z * (1.0 / (NQCD * NQCD))) + ln(x) * z * (NQCD * NQCD) + 2.0 * ln(x) * (z * z) * (1.0 / (NQCD * NQCD)) + (- 2.0 * ln(x) * (z * z)) + (- 1. / 2. * ln(x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 4.0 * ln(x) * x * (1.0 / z) + (- 7. / 2. * ln(x) * x * (1.0 / z) * (NQCD * NQCD)) + (- 15. / 2. * ln(x) * x * (1.0 / (NQCD * NQCD))) + 11.0 * ln(x) * x + (- 2.0 * ln(x) * x * rln2) + (- 7. / 2. * ln(x) * x * (NQCD * NQCD)) + 2.0 * ln(x) * x * (NQCD * NQCD) * rln2 + 8.0 * ln(x) * x * z * (1.0 / (NQCD * NQCD)) + (- 17.0 * ln(x) * x * z) + (- 2.0 * ln(x) * x * z * rln2) + 9.0 * ln(x) * x * z * (NQCD * NQCD) + 2.0 * ln(x) * x * z * (NQCD * NQCD) * rln2 + (- 4.0 * ln(x) * x * (z * z)) + 4.0 * ln(x) * x * (z * z) * (NQCD * NQCD) + 10.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 10.0 * ln(x) * ln(1.0 - z) * x * (1.0 / z)) + (- 31.0 * ln(x) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD))) + 42.0 * ln(x) * ln(1.0 - z) * x + (- 11.0 * ln(x) * ln(1.0 - z) * x * (NQCD * NQCD)) + 21.0 * ln(x) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD)) + (- 32.0 * ln(x) * ln(1.0 - z) * x * z) + 11.0 * ln(x) * ln(1.0 - z) * x * z * (NQCD * NQCD) + 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD)) + 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD)) + 10.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 10.0 * ln(x) * ln(1.0 - x) * x * (1.0 / z)) + (-28.0 * ln(x) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD))) + 42.0 * ln(x) * ln(1.0 - x) * x + (- 14.0 * ln(x) * ln(1.0 - x) * x * (NQCD * NQCD)) + 18.0 * ln(x) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) + (- 32.0 * ln(x) * ln(1.0 - x) * x * z) + 14.0 * ln(x) * ln(1.0 - x) * x * z * (NQCD * NQCD) + (- 7.0 * pow(ln(x), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 7.0 * pow(ln(x), 2) * x * (1.0 / z) + 22.0 * pow(ln(x), 2) * x * (1.0 / (NQCD * NQCD)) + (- 30.0 * pow(ln(x), 2) * x) + 8.0 * pow(ln(x), 2) * x * (NQCD * NQCD) + (- 15.0 * pow(ln(x), 2) * x * z * (1.0 / (NQCD * NQCD))) + 23.0 * pow(ln(x), 2) * x * z + (- 8.0 * pow(ln(x), 2) * x * z * (NQCD * NQCD)) + 6.0 * ln(x) * ln(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 6.0 * ln(x) * ln(z) * x * (1.0 / z)) + (- 20.0 * ln(x) * ln(z) * x * (1.0 / (NQCD * NQCD))) + 36.0 * ln(x) * ln(z) * x + (- 16.0 * ln(x) * ln(z) * x * (NQCD * NQCD)) + 17.0 * ln(x) * ln(z) * x * z * (1.0 / (NQCD * NQCD)) + (- 16.0 * ln(x) * ln(z) * x * z) + (- ln(x) * ln(z) * x * z * (NQCD * NQCD)) + (- ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) + (- ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / (NQCD * NQCD))) + (- ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x) + 2.0 * ln(x) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (NQCD * NQCD) + (- 6.0 * ln(z)) + 2.0 * ln(z) * (1.0 / (NQCD * NQCD)) + 4.0 * ln(z) * (NQCD * NQCD) + (- 4.0 * ln(z) * z) + 4.0 * ln(z) * z * (NQCD * NQCD) + 2.0 * ln(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 7.0 * ln(z) * x * (1.0 / z)) + 5.0 * ln(z) * x * (1.0 / z) * (NQCD * NQCD) + 6.0 * ln(z) * x * (1.0 / (NQCD * NQCD)) + (- 8.0 * ln(z) * x) + (- 6.0 * ln(z) * x * rln2) + 2.0 * ln(z) * x * (NQCD * NQCD) + 6.0 * ln(z) * x * (NQCD * NQCD) * rln2 + (- 9.0 * ln(z) * x * z * (1.0 / (NQCD * NQCD))) + 23.0 * ln(z) * x * z + (- 6.0 * ln(z) * x * z * rln2) + (- 14.0 * ln(z) * x * z * (NQCD * NQCD)) + 6.0 * ln(z) * x * z * (NQCD * NQCD) * rln2 + 2.0 * ln(z) * x * (z * z) + (- 2.0 * ln(z) * x * (z * z) * (NQCD * NQCD)) + (- 2.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 2.0 * ln(z) * ln(1.0 - z) * x * (1.0 / z) + 12.0 * ln(z) * ln(1.0 - z) * x * (1.0 / (NQCD * NQCD)) + (- 22.0 * ln(z) * ln(1.0 - z) * x) + 10.0 * ln(z) * ln(1.0 - z) * x * (NQCD * NQCD) + (- 10.0 * ln(z) * ln(1.0 - z) * x * z * (1.0 / (NQCD * NQCD))) + 20.0 * ln(z) * ln(1.0 - z) * x * z + (- 10.0 * ln(z) * ln(1.0 - z) * x * z * (NQCD * NQCD)) + 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD)) + 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD)) + 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD)) + 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD)) + (- 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 4.0 * ln(z) * ln(1.0 - x) * x * (1.0 / z) + 12.0 * ln(z) * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD)) + (- 24.0 * ln(z) * ln(1.0 - x) * x) + 12.0 * ln(z) * ln(1.0 - x) * x * (NQCD * NQCD) + (- 9.0 * ln(z) * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD))) + 10.0 * ln(z) * ln(1.0 - x) * x * z + (- ln(z) * ln(1.0 - x) * x * z * (NQCD * NQCD)) + (- pow(ln(z), 2) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + pow(ln(z), 2) * x * (1.0 / z) + 5.0 * pow(ln(z), 2) * x * (1.0 / (NQCD * NQCD)) + (- 13.0 * pow(ln(z), 2) * x) + 8.0 * pow(ln(z), 2) * x * (NQCD * NQCD) + (- 5.0 * pow(ln(z), 2) * x * z * (1.0 / (NQCD * NQCD))) + (- 2.0 * pow(ln(z), 2) * x * z) + 7.0 * pow(ln(z), 2) * x * z * (NQCD * NQCD) + (- ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) + (- ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / (NQCD * NQCD))) + (- ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x) + 2.0 * ln(z) * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (NQCD * NQCD) + (- 2.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x) + 2.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (NQCD * NQCD) + (- 2.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z) + 2.0 * Li2(1. / 2. - 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z * (NQCD * NQCD) + 2.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x + (- 2.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * (NQCD * NQCD)) + 2.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z + (- 2.0 * Li2(1. / 2. + 1. / 2. * (1.0 / z) - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * (1.0 / z)) * x * z * (NQCD * NQCD)) + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x + (- 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD)) + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z + (- 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD)) + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x) + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * (NQCD * NQCD) + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z) + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt((1.0 - z).powi(2) + 4.0 * x * z)) * x * z * (NQCD * NQCD) + (- 2.0 * Li2(1.0 - x * (1.0 / z)) * x * (1.0 / (NQCD * NQCD))) + 4.0 * Li2(1.0 - x * (1.0 / z)) * x + (- 2.0 * Li2(1.0 - x * (1.0 / z)) * x * (NQCD * NQCD)) + 2.0 * Li2(1.0 - x * (1.0 / z)) * x * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * Li2(1.0 - x * (1.0 / z)) * x * z) + 2.0 * Li2(1.0 - x * (1.0 / z)) * x * z * (NQCD * NQCD) + Li2(x) * x * (1.0 / (NQCD * NQCD)) + (- Li2(x) * x * (NQCD * NQCD)) + (- Li2(x) * x * z * (1.0 / (NQCD * NQCD))) + Li2(x) * x * z * (NQCD * NQCD) + 2.0 * Li2(z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) + (- 2.0 * Li2(z) * x * (1.0 / z)) + (- 2.0 * Li2(z) * x * (1.0 / (NQCD * NQCD))) + 2.0 * Li2(z) * x + Li2(z) * x * z * (1.0 / (NQCD * NQCD)) + 10.0 * Li2(z) * x * z + (- 11.0 * Li2(z) * x * z * (NQCD * NQCD)) + (- 2.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * (1.0 / (NQCD * NQCD)) * rln2) + 2.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / z) * rln2 + (- 2.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (1.0 / (NQCD * NQCD)) * rln2) + (- 2.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * rln2) + 4.0 * mysqrt((1.0 - z).powi(2) + 4.0 * x * z) * x * (NQCD * NQCD) * rln2 + 2.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * z * (1.0 / (NQCD * NQCD)) + (- 2.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * z) + (- 6.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * (z * z) * (1.0 / (NQCD * NQCD))) + 6.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * (z * z) + 6.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * (z * z * z) * (1.0 / (NQCD * NQCD)) + (- 6.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * (z * z * z)) + (- 2.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * (z * z * z * z) * (1.0 / (NQCD * NQCD))) + 2.0 / ((1.0 - x - z).powi(2)) * ln(1.0 - z) * (z * z * z * z) + (- 2.0 / ((1.0 - x - z).powi(2)) * ln(x) * z * (1.0 / (NQCD * NQCD))) + 2.0 / ((1.0 - x - z).powi(2)) * ln(x) * z + 6.0 / ((1.0 - x - z).powi(2)) * ln(x) * (z * z) * (1.0 / (NQCD * NQCD)) + (- 6.0 / ((1.0 - x - z).powi(2)) * ln(x) * (z * z)) + (- 6.0 / ((1.0 - x - z).powi(2)) * ln(x) * (z * z * z) * (1.0 / (NQCD * NQCD))) + 6.0 / ((1.0 - x - z).powi(2)) * ln(x) * (z * z * z) + 2.0 / ((1.0 - x - z).powi(2)) * ln(x) * (z * z * z * z) * (1.0 / (NQCD * NQCD)) + (- 2.0 / ((1.0 - x - z).powi(2)) * ln(x) * (z * z * z * z)) + (- 2.0 / (1.0 - z - x) * z * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 - z - x) * z + 4.0 / (1.0 - z - x) * (z * z) * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 - z - x) * (z * z)) + (- 2.0 / (1.0 - z - x) * (z * z * z) * (1.0 / (NQCD * NQCD))) + 2.0 / (1.0 - z - x) * (z * z * z) + (- 4.0 / (1.0 - z - x) * ln(1.0 - z) * z * (1.0 / (NQCD * NQCD))) + 4.0 / (1.0 - z - x) * ln(1.0 - z) * z + 8.0 / (1.0 - z - x) * ln(1.0 - z) * (z * z) * (1.0 / (NQCD * NQCD)) + (- 8.0 / (1.0 - z - x) * ln(1.0 - z) * (z * z)) + (- 4.0 / (1.0 - z - x) * ln(1.0 - z) * (z * z * z) * (1.0 / (NQCD * NQCD))) + 4.0 / (1.0 - z - x) * ln(1.0 - z) * (z * z * z) + 4.0 / (1.0 - z - x) * ln(x) * z * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 - z - x) * ln(x) * z) + (- 8.0 / (1.0 - z - x) * ln(x) * (z * z) * (1.0 / (NQCD * NQCD))) + 8.0 / (1.0 - z - x) * ln(x) * (z * z) + 4.0 / (1.0 - z - x) * ln(x) * (z * z * z) * (1.0 / (NQCD * NQCD)) + (- 4.0 / (1.0 - z - x) * ln(x) * (z * z * z));
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
        let tmp: f64 = (- 2.0 * lmua * x * (1.0 / z) * (1.0 / (NQCD * NQCD))) + 8.0 * lmua * x * (1.0 / z) + (-6.0 * lmua * x * (1.0 / z) * (NQCD * NQCD)) + 4.0 * lmua * x * (1.0 / (NQCD * NQCD)) + 10. / 3. * lmua * x + (- 22. / 3. * lmua * x * (NQCD * NQCD)) + (- 4. / 3. * lmua * x * NF * (1.0 / NQCD)) + 4. / 3. * lmua * x * NF * NQCD + (- 2.0 * lmua * x * z * (1.0 / (NQCD * NQCD))) + (- 22. / 3. * lmua * x * z) + 28. / 3. * lmua * x * z * (NQCD * NQCD) + 4. / 3. * lmua * x * z * NF * (1.0 / NQCD) + (- 4. / 3. * lmua * x * z * NF * NQCD) + (- 4.0 * lmua * x * (z * z)) + 4.0 * lmua * x * (z * z) * (NQCD * NQCD) + 8.0 * lmua * ln(1.0 - z) * x + (- 8.0 * lmua * ln(1.0 - z) * x * (NQCD * NQCD)) + (- 8.0 * lmua * ln(1.0 - z) * x * z) + 8.0 * lmua * ln(1.0 - z) * x * z * (NQCD * NQCD) + 8.0 * ln(z) * lmua * x + (-8.0 * ln(z) * lmua * x * (NQCD * NQCD)) + 2.0 * ln(z) * lmua * x * z * (1.0 / (NQCD * NQCD)) + 12.0 * ln(z) * lmua * x * z + (- 14.0 * ln(z) * lmua * x * z * (NQCD * NQCD));
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
        let tmp: f64 = 4.0 * lmuf + (- 2.0 * lmuf * (1.0 / (NQCD * NQCD))) + (- 2.0 * lmuf * (NQCD * NQCD)) + 2.0 * lmuf * z * (1.0 / (NQCD * NQCD)) + (- 4.0 * lmuf * z) + 2.0 * lmuf * z * (NQCD * NQCD) + (- lmuf * x * (1.0 / (NQCD * NQCD))) + 2.0 * lmuf * x + (- lmuf * x * (NQCD * NQCD)) + lmuf * x * z * (1.0 / (NQCD * NQCD)) + (- 2.0 * lmuf * x * z) + lmuf * x * z * (NQCD * NQCD) + (- 4.0 * lmuf * ln(1.0 - x) * x * (1.0 / (NQCD * NQCD))) + 8.0 * lmuf * ln(1.0 - x) * x + (- 4.0 * lmuf * ln(1.0 - x) * x * (NQCD * NQCD)) + 4.0 * lmuf * ln(1.0 - x) * x * z * (1.0 / (NQCD * NQCD)) + (- 8.0 * lmuf * ln(1.0 - x) * x * z) + 4.0 * lmuf * ln(1.0 - x) * x * z * (NQCD * NQCD) + 2.0 * ln(x) * lmuf * x * (1.0 / (NQCD * NQCD)) + (- 4.0 * ln(x) * lmuf * x) + 2.0 * ln(x) * lmuf * x * (NQCD * NQCD) + (- 2.0 * ln(x) * lmuf * x * z * (1.0 / (NQCD * NQCD))) + 4.0 * ln(x) * lmuf * x * z + (- 2.0 * ln(x) * lmuf * x * z * (NQCD * NQCD));
        res += tmp;
    }

    return res;
}

fn RG_RG_100(x: f64, z: f64, NF: f64) -> f64 {
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

        let pt0: f64 = RG_RG_100(x0, z0, NF);
        let pt1: f64 = RG_RG_100(x1, z1, NF);
        let pt2: f64 = RG_RG_100(x2, z2, NF);

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

        let pt0: f64 = RG_RG_100(x0, z0, NF);
        let pt1: f64 = RG_RG_100(x1, z1, NF);
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

        let pt0: f64 = RG_RG_100(x0, z0, NF);
        let pt1: f64 = RG_RG_100(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }

    if z != x && z != 1. - x {
        let tmp: f64 = (- 22. / 3. * lmur * x) + 22. / 3. * lmur * x * (NQCD * NQCD) + 4. / 3. * lmur * x * NF * (1.0 / NQCD) + (- 4. / 3. * lmur * x * NF * NQCD) + 22. / 3. * lmur * x * z + (- 22. / 3. * lmur * x * z * (NQCD * NQCD)) + (- 4. / 3. * lmur * x * z * NF * (1.0 / NQCD)) + 4. / 3. * lmur * x * z * NF * NQCD;
        res += tmp;
    }

    return res;
}

mkcoeff!(
    ("000", [RG_RG_000, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("001", [RG_RG_001, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("010", [RG_RG_010, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]),
    ("100", [RG_RG_100, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _])
);

/*
  SV mapping:
  - 000: RG_RG
    - 001: RG_RG
    - 010: RG_RG
    - 100: RG_RG
*/
