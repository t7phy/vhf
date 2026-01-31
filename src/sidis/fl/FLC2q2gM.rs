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
        let tmp: f64 = -4. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) + 4. / 3. * pow(pi, 2) * x * pow(z, -1) + 3.0 * pow(pi, 2) * x * pow(NQCD, -2) - 3.0 * pow(pi, 2) * x - 5. / 3. * pow(pi, 2) * x * z * pow(NQCD, -2) + 5. / 3. * pow(pi, 2) * x * z - 8.0 * ln(1.0 - z) * x * pow(NQCD, -2) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * pow(NQCD, -2) - 8.0 * ln(1.0 - z) * x * z + 5.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) - 5.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) - 13.0 * pow(ln(1.0 - z), 2) * x * pow(NQCD, -2) + 13.0 * pow(ln(1.0 - z), 2) * x + 8.0 * pow(ln(1.0 - z), 2) * x * z * pow(NQCD, -2) - 8.0 * pow(ln(1.0 - z), 2) * x * z - 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * pow(z, -1) + 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * pow(NQCD, -2) - 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x - 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z * pow(NQCD, -2) + 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z - 6.0 * ln(1.0 - x) * x * pow(NQCD, -2) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * pow(NQCD, -2) - 6.0 * ln(1.0 - x) * x * z + 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) - 26.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, -2) + 26.0 * ln(1.0 - x) * ln(1.0 - z) * x + 16.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 16.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) - 9.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, -2) + 9.0 * pow(ln(1.0 - x), 2) * x + 5.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, -2) - 5.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * pow(NQCD, -2) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * pow(NQCD, -2) + 12.0 * ln(x) * x * z - 12.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) + 12.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) + 34.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, -2) - 34.0 * ln(x) * ln(1.0 - z) * x - 22.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, -2) + 22.0 * ln(x) * ln(1.0 - z) * x * z + 2.0 * ln(x) * ln(1.0 - z - x) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * ln(x) * ln(1.0 - z - x) * x * pow(z, -1) - 6.0 * ln(x) * ln(1.0 - z - x) * x * pow(NQCD, -2) + 6.0 * ln(x) * ln(1.0 - z - x) * x + 4.0 * ln(x) * ln(1.0 - z - x) * x * z * pow(NQCD, -2) - 4.0 * ln(x) * ln(1.0 - z - x) * x * z - 12.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + 12.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) + 32.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, -2) - 32.0 * ln(x) * ln(1.0 - x) * x - 20.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, -2) + 20.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(-z + x) * x * pow(NQCD, -2) + 2.0 * ln(x) * ln(-z + x) * x + 2.0 * ln(x) * ln(-z + x) * x * z * pow(NQCD, -2) - 2.0 * ln(x) * ln(-z + x) * x * z + 7.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 7.0 * pow(ln(x), 2) * x * pow(z, -1) - 20.0 * pow(ln(x), 2) * x * pow(NQCD, -2) + 20.0 * pow(ln(x), 2) * x + 13.0 * pow(ln(x), 2) * x * z * pow(NQCD, -2) - 13.0 * pow(ln(x), 2) * x * z - 6.0 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) + 6.0 * ln(x) * ln(z) * x * pow(z, -1) + 22.0 * ln(x) * ln(z) * x * pow(NQCD, -2) - 22.0 * ln(x) * ln(z) * x - 16.0 * ln(x) * ln(z) * x * z * pow(NQCD, -2) + 16.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * pow(NQCD, -2) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * pow(NQCD, -2) - 6.0 * ln(z) * x * z + 4.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) - 16.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, -2) + 16.0 * ln(z) * ln(1.0 - z) * x + 12.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 12.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) + -12.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, -2) + 12.0 * ln(z) * ln(1.0 - x) * x + 8.0 * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, -2) - 8.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(-z + x) * x * pow(NQCD, -2) - 2.0 * ln(z) * ln(-z + x) * x - 2.0 * ln(z) * ln(-z + x) * x * z * pow(NQCD, -2) + 2.0 * ln(z) * ln(-z + x) * x * z + pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) - pow(ln(z), 2) * x * pow(z, -1) - 6.0 * pow(ln(z), 2) * x * pow(NQCD, -2) + 6.0 * pow(ln(z), 2) * x + 5.0 * pow(ln(z), 2) * x * z * pow(NQCD, -2) - 5.0 * pow(ln(z), 2) * x * z + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z + 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x - 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x * z * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x * z - 2.0 * Li2(1.0 / (1.0 - x) * z) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * pow(z, -1) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * pow(z, -1) - 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * pow(NQCD, -2) + 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z + 2.0 * Li2(z) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(z) * x * pow(z, -1) - 4.0 * Li2(z) * x * pow(NQCD, -2) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * pow(NQCD, -2) - 2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z > 1. - x && z < x {
        let tmp: f64 = -4. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) + 4. / 3. * pow(pi, 2) * x * pow(z, -1) + 3.0 * pow(pi, 2) * x * pow(NQCD, -2) - 3.0 * pow(pi, 2) * x - 5. / 3. * pow(pi, 2) * x * z * pow(NQCD, -2) + 5. / 3. * pow(pi, 2) * x * z - 8.0 * ln(1.0 - z) * x * pow(NQCD, -2) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * pow(NQCD, -2) - 8.0 * ln(1.0 - z) * x * z - 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * pow(z, -1) + 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * pow(NQCD, -2) - 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x - 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z * pow(NQCD, -2) + 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z + 4.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) - 12.0 * pow(ln(1.0 - z), 2) * x * pow(NQCD, -2) + 12.0 * pow(ln(1.0 - z), 2) * x + 8.0 * pow(ln(1.0 - z), 2) * x * z * pow(NQCD, -2) - 8.0 * pow(ln(1.0 - z), 2) * x * z - 6.0 * ln(1.0 - x) * x * pow(NQCD, -2) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * pow(NQCD, -2) - 6.0 * ln(1.0 - x) * x * z + 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) - 20.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, -2) + 20.0 * ln(1.0 - x) * ln(1.0 - z) * x + 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) - 9.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, -2) + 9.0 * pow(ln(1.0 - x), 2) * x + 5.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, -2) - 5.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * pow(NQCD, -2) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * pow(NQCD, -2) + 12.0 * ln(x) * x * z + 2.0 * ln(x) * ln(-1.0 + z + x) * x * pow(z, -1) * pow(NQCD, -2) + -2.0 * ln(x) * ln(-1.0 + z + x) * x * pow(z, -1) - 6.0 * ln(x) * ln(-1.0 + z + x) * x * pow(NQCD, -2) + 6.0 * ln(x) * ln(-1.0 + z + x) * x + 4.0 * ln(x) * ln(-1.0 + z + x) * x * z * pow(NQCD, -2) - 4.0 * ln(x) * ln(-1.0 + z + x) * x * z - 10.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) + 10.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) + 32.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, -2) - 32.0 * ln(x) * ln(1.0 - z) * x - 22.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, -2) + 22.0 * ln(x) * ln(1.0 - z) * x * z - 10.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + 10.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) + 26.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, -2) - 26.0 * ln(x) * ln(1.0 - x) * x - 16.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, -2) + 16.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(-z + x) * x * pow(NQCD, -2) + 2.0 * ln(x) * ln(-z + x) * x + 2.0 * ln(x) * ln(-z + x) * x * z * pow(NQCD, -2) - 2.0 * ln(x) * ln(-z + x) * x * z + 6.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 6.0 * pow(ln(x), 2) * x * pow(z, -1) - 19.0 * pow(ln(x), 2) * x * pow(NQCD, -2) + 19.0 * pow(ln(x), 2) * x + 13.0 * pow(ln(x), 2) * x * z * pow(NQCD, -2) - 13.0 * pow(ln(x), 2) * x * z - 8.0 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) + 8.0 * ln(x) * ln(z) * x * pow(z, -1) + 28.0 * ln(x) * ln(z) * x * pow(NQCD, -2) - 28.0 * ln(x) * ln(z) * x - 20.0 * ln(x) * ln(z) * x * z * pow(NQCD, -2) + 20.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * pow(NQCD, -2) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * pow(NQCD, -2) - 6.0 * ln(z) * x * z + 6.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 6.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) - 22.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, -2) + 22.0 * ln(z) * ln(1.0 - z) * x + 16.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 16.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + -4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) - 12.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, -2) + 12.0 * ln(z) * ln(1.0 - x) * x + 8.0 * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, -2) - 8.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(-z + x) * x * pow(NQCD, -2) - 2.0 * ln(z) * ln(-z + x) * x - 2.0 * ln(z) * ln(-z + x) * x * z * pow(NQCD, -2) + 2.0 * ln(z) * ln(-z + x) * x * z + pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) - pow(ln(z), 2) * x * pow(z, -1) - 6.0 * pow(ln(z), 2) * x * pow(NQCD, -2) + 6.0 * pow(ln(z), 2) * x + 5.0 * pow(ln(z), 2) * x * z * pow(NQCD, -2) - 5.0 * pow(ln(z), 2) * x * z - 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) + 4.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(NQCD, -2) - 4.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x - 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z * pow(NQCD, -2) + 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z + 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) - 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(NQCD, -2) + 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z - 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x + 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x * z * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x * z + 2.0 * Li2(z) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(z) * x * pow(z, -1) - 4.0 * Li2(z) * x * pow(NQCD, -2) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * pow(NQCD, -2) - 2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z < 1. - x && z > x {
        let tmp: f64 = -4. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) + 4. / 3. * pow(pi, 2) * x * pow(z, -1) + 13. / 3. * pow(pi, 2) * x * pow(NQCD, -2) - 13. / 3. * pow(pi, 2) * x - 3.0 * pow(pi, 2) * x * z * pow(NQCD, -2) + 3.0 * pow(pi, 2) * x * z - 8.0 * ln(1.0 - z) * x * pow(NQCD, -2) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * pow(NQCD, -2) - 8.0 * ln(1.0 - z) * x * z + 5.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) - 5.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) - 15.0 * pow(ln(1.0 - z), 2) * x * pow(NQCD, -2) + 15.0 * pow(ln(1.0 - z), 2) * x + 10.0 * pow(ln(1.0 - z), 2) * x * z * pow(NQCD, -2) - 10.0 * pow(ln(1.0 - z), 2) * x * z - 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * pow(z, -1) + 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * pow(NQCD, -2) - 6.0 * ln(1.0 - z) * ln(1.0 - z - x) * x - 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z * pow(NQCD, -2) + 4.0 * ln(1.0 - z) * ln(1.0 - z - x) * x * z - 6.0 * ln(1.0 - x) * x * pow(NQCD, -2) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * pow(NQCD, -2) - 6.0 * ln(1.0 - x) * x * z + 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 10.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) - 22.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, -2) + 22.0 * ln(1.0 - x) * ln(1.0 - z) * x + 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) - 11.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, -2) + 11.0 * pow(ln(1.0 - x), 2) * x + 7.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, -2) - 7.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * pow(NQCD, -2) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * pow(NQCD, -2) + 12.0 * ln(x) * x * z - 12.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) + 12.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) + 36.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, -2) - 36.0 * ln(x) * ln(1.0 - z) * x - 24.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, -2) + 24.0 * ln(x) * ln(1.0 - z) * x * z + 2.0 * ln(x) * ln(1.0 - z - x) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * ln(x) * ln(1.0 - z - x) * x * pow(z, -1) - 6.0 * ln(x) * ln(1.0 - z - x) * x * pow(NQCD, -2) + 6.0 * ln(x) * ln(1.0 - z - x) * x + 4.0 * ln(x) * ln(1.0 - z - x) * x * z * pow(NQCD, -2) - 4.0 * ln(x) * ln(1.0 - z - x) * x * z - 12.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + 12.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) + 30.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, -2) - 30.0 * ln(x) * ln(1.0 - x) * x - 18.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, -2) + 18.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(z - x) * x * pow(NQCD, -2) + 2.0 * ln(x) * ln(z - x) * x + 2.0 * ln(x) * ln(z - x) * x * z * pow(NQCD, -2) - 2.0 * ln(x) * ln(z - x) * x * z + 7.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 7.0 * pow(ln(x), 2) * x * pow(z, -1) - 21.0 * pow(ln(x), 2) * x * pow(NQCD, -2) + 21.0 * pow(ln(x), 2) * x + 14.0 * pow(ln(x), 2) * x * z * pow(NQCD, -2) - 14.0 * pow(ln(x), 2) * x * z - 6.0 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) + 6.0 * ln(x) * ln(z) * x * pow(z, -1) + 24.0 * ln(x) * ln(z) * x * pow(NQCD, -2) - 24.0 * ln(x) * ln(z) * x - 18.0 * ln(x) * ln(z) * x * z * pow(NQCD, -2) + 18.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * pow(NQCD, -2) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * pow(NQCD, -2) - 6.0 * ln(z) * x * z + 4.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) - 18.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, -2) + 18.0 * ln(z) * ln(1.0 - z) * x + 14.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 14.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) + -10.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, -2) + 10.0 * ln(z) * ln(1.0 - x) * x + 6.0 * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, -2) - 6.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(z - x) * x * pow(NQCD, -2) - 2.0 * ln(z) * ln(z - x) * x - 2.0 * ln(z) * ln(z - x) * x * z * pow(NQCD, -2) + 2.0 * ln(z) * ln(z - x) * x * z + pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) - pow(ln(z), 2) * x * pow(z, -1) - 7.0 * pow(ln(z), 2) * x * pow(NQCD, -2) + 7.0 * pow(ln(z), 2) * x + 6.0 * pow(ln(z), 2) * x * z * pow(NQCD, -2) - 6.0 * pow(ln(z), 2) * x * z - 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x + 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x * z * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - z) * x * pow(z, -1) - 1.0 / (1.0 - z) * pow(x, 2) * pow(z, -1)) * x * z - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z - 2.0 * Li2(1.0 / (1.0 - x) * z) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * pow(z, -1) + 2.0 * Li2(1.0 / (1.0 - x) * z) * x * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * pow(z, -1) - 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * pow(NQCD, -2) + 4.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x + 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) / (1.0 - z) * x * z) * x * z + 2.0 * Li2(z) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(z) * x * pow(z, -1) - 4.0 * Li2(z) * x * pow(NQCD, -2) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * pow(NQCD, -2) + -2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z > 1. - x && z > x {
        let tmp: f64 = -4. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) + 4. / 3. * pow(pi, 2) * x * pow(z, -1) + 3.0 * pow(pi, 2) * x * pow(NQCD, -2) - 3.0 * pow(pi, 2) * x - 5. / 3. * pow(pi, 2) * x * z * pow(NQCD, -2) + 5. / 3. * pow(pi, 2) * x * z - 8.0 * ln(1.0 - z) * x * pow(NQCD, -2) + 8.0 * ln(1.0 - z) * x + 8.0 * ln(1.0 - z) * x * z * pow(NQCD, -2) - 8.0 * ln(1.0 - z) * x * z - 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * pow(z, -1) + 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * pow(NQCD, -2) - 6.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x - 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z * pow(NQCD, -2) + 4.0 * ln(1.0 - z) * ln(-1.0 + z + x) * x * z + 4.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) - 12.0 * pow(ln(1.0 - z), 2) * x * pow(NQCD, -2) + 12.0 * pow(ln(1.0 - z), 2) * x + 8.0 * pow(ln(1.0 - z), 2) * x * z * pow(NQCD, -2) - 8.0 * pow(ln(1.0 - z), 2) * x * z - 6.0 * ln(1.0 - x) * x * pow(NQCD, -2) + 6.0 * ln(1.0 - x) * x + 6.0 * ln(1.0 - x) * x * z * pow(NQCD, -2) - 6.0 * ln(1.0 - x) * x * z + 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) - 20.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, -2) + 20.0 * ln(1.0 - x) * ln(1.0 - z) * x + 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) - 9.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, -2) + 9.0 * pow(ln(1.0 - x), 2) * x + 5.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, -2) - 5.0 * pow(ln(1.0 - x), 2) * x * z + 12.0 * ln(x) * x * pow(NQCD, -2) - 12.0 * ln(x) * x - 12.0 * ln(x) * x * z * pow(NQCD, -2) + 12.0 * ln(x) * x * z + 2.0 * ln(x) * ln(-1.0 + z + x) * x * pow(z, -1) * pow(NQCD, -2) + -2.0 * ln(x) * ln(-1.0 + z + x) * x * pow(z, -1) - 6.0 * ln(x) * ln(-1.0 + z + x) * x * pow(NQCD, -2) + 6.0 * ln(x) * ln(-1.0 + z + x) * x + 4.0 * ln(x) * ln(-1.0 + z + x) * x * z * pow(NQCD, -2) - 4.0 * ln(x) * ln(-1.0 + z + x) * x * z - 10.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) + 10.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) + 30.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, -2) - 30.0 * ln(x) * ln(1.0 - z) * x - 20.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, -2) + 20.0 * ln(x) * ln(1.0 - z) * x * z - 10.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + 10.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) + 28.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, -2) - 28.0 * ln(x) * ln(1.0 - x) * x - 18.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, -2) + 18.0 * ln(x) * ln(1.0 - x) * x * z - 2.0 * ln(x) * ln(z - x) * x * pow(NQCD, -2) + 2.0 * ln(x) * ln(z - x) * x + 2.0 * ln(x) * ln(z - x) * x * z * pow(NQCD, -2) - 2.0 * ln(x) * ln(z - x) * x * z + 6.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) - 6.0 * pow(ln(x), 2) * x * pow(z, -1) - 18.0 * pow(ln(x), 2) * x * pow(NQCD, -2) + 18.0 * pow(ln(x), 2) * x + 12.0 * pow(ln(x), 2) * x * z * pow(NQCD, -2) - 12.0 * pow(ln(x), 2) * x * z - 8.0 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) + 8.0 * ln(x) * ln(z) * x * pow(z, -1) + 26.0 * ln(x) * ln(z) * x * pow(NQCD, -2) - 26.0 * ln(x) * ln(z) * x - 18.0 * ln(x) * ln(z) * x * z * pow(NQCD, -2) + 18.0 * ln(x) * ln(z) * x * z - 6.0 * ln(z) * x * pow(NQCD, -2) + 6.0 * ln(z) * x + 6.0 * ln(z) * x * z * pow(NQCD, -2) - 6.0 * ln(z) * x * z + 6.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) - 6.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) - 20.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, -2) + 20.0 * ln(z) * ln(1.0 - z) * x + 14.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, -2) - 14.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + -4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) - 14.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, -2) + 14.0 * ln(z) * ln(1.0 - x) * x + 10.0 * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, -2) - 10.0 * ln(z) * ln(1.0 - x) * x * z + 2.0 * ln(z) * ln(z - x) * x * pow(NQCD, -2) - 2.0 * ln(z) * ln(z - x) * x - 2.0 * ln(z) * ln(z - x) * x * z * pow(NQCD, -2) + 2.0 * ln(z) * ln(z - x) * x * z + pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) - pow(ln(z), 2) * x * pow(z, -1) - 5.0 * pow(ln(z), 2) * x * pow(NQCD, -2) + 5.0 * pow(ln(z), 2) * x + 4.0 * pow(ln(z), 2) * x * z * pow(NQCD, -2) - 4.0 * pow(ln(z), 2) * x * z - 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) + 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) + 4.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(NQCD, -2) - 4.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x - 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z * pow(NQCD, -2) + 2.0 * Li2(1.0 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z + 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) - 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(NQCD, -2) + 2.0 * Li2(pow(z, -1) - x * pow(z, -1)) * x - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z + 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x * pow(NQCD, -2) - 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x - 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x * z * pow(NQCD, -2) + 2.0 * Li2(1.0 / (1.0 - x) * pow(x, -1) * z - 1.0 / (1.0 - x) * pow(x, -1) * pow(z, 2)) * x * z + 2.0 * Li2(z) * x * pow(z, -1) * pow(NQCD, -2) - 2.0 * Li2(z) * x * pow(z, -1) - 4.0 * Li2(z) * x * pow(NQCD, -2) + 4.0 * Li2(z) * x + 2.0 * Li2(z) * x * z * pow(NQCD, -2) - 2.0 * Li2(z) * x * z;
        res += tmp;
    }

    if z > x {
        let tmp: f64 = -pow(pi, 2) * x + pow(pi, 2) * x * pow(NQCD, 2) + pow(pi, 2) * x * z - pow(pi, 2) * x * z * pow(NQCD, 2) - 2.0 * ln(1.0 - z) * x * z + 2.0 * ln(1.0 - z) * x * z * pow(NQCD, 2) + pow(ln(1.0 - z), 2) * x - pow(ln(1.0 - z), 2) * x * pow(NQCD, 2) - pow(ln(1.0 - z), 2) * x * z + pow(ln(1.0 - z), 2) * x * z * pow(NQCD, 2) - 4.0 * ln(1.0 - x) * x * z + 4.0 * ln(1.0 - x) * x * z * pow(NQCD, 2) + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, 2) - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, 2) + 4.0 * pow(ln(1.0 - x), 2) * x - 4.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, 2) - 4.0 * pow(ln(1.0 - x), 2) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, 2) + 6.0 * ln(x) * x * z - 6.0 * ln(x) * x * z * pow(NQCD, 2) - 6.0 * ln(x) * ln(1.0 - z) * x + 6.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, 2) + 6.0 * ln(x) * ln(1.0 - z) * x * z - 6.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, 2) - 12.0 * ln(x) * ln(1.0 - x) * x + 12.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, 2) + 12.0 * ln(x) * ln(1.0 - x) * x * z - 12.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, 2) + 2.0 * ln(x) * ln(z - x) * x - 2.0 * ln(x) * ln(z - x) * x * pow(NQCD, 2) - 2.0 * ln(x) * ln(z - x) * x * z + 2.0 * ln(x) * ln(z - x) * x * z * pow(NQCD, 2) + 7.0 * pow(ln(x), 2) * x - 7.0 * pow(ln(x), 2) * x * pow(NQCD, 2) - 7.0 * pow(ln(x), 2) * x * z + 7.0 * pow(ln(x), 2) * x * z * pow(NQCD, 2) - 12.0 * ln(x) * ln(z) * x + 12.0 * ln(x) * ln(z) * x * pow(NQCD, 2) + 12.0 * ln(x) * ln(z) * x * z - 12.0 * ln(x) * ln(z) * x * z * pow(NQCD, 2) - 4.0 * ln(z) * x * z + 4.0 * ln(z) * x * z * pow(NQCD, 2) + 2.0 * ln(z) * ln(1.0 - z) * x - 2.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, 2) - 2.0 * ln(z) * ln(1.0 - z) * x * z + 2.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, 2) + 10.0 * ln(z) * ln(1.0 - x) * x - 10.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, 2) - 10.0 * ln(z) * ln(1.0 - x) * x * z + 10.0 * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, 2) - 2.0 * ln(z) * ln(z - x) * x + 2.0 * ln(z) * ln(z - x) * x * pow(NQCD, 2) + 2.0 * ln(z) * ln(z - x) * x * z - 2.0 * ln(z) * ln(z - x) * x * z * pow(NQCD, 2) + 5.0 * pow(ln(z), 2) * x - 5.0 * pow(ln(z), 2) * x * pow(NQCD, 2) - 5.0 * pow(ln(z), 2) * x * z + 5.0 * pow(ln(z), 2) * x * z * pow(NQCD, 2) - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * pow(NQCD, 2) + 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z - 2.0 * Li2(1.0 / (1.0 - x) - 1.0 / (1.0 - x) * z) * x * z * pow(NQCD, 2) + 2.0 * Li2(1.0 / (1.0 - x) * x * pow(z, -1) - 1.0 / (1.0 - x) * x) * x - 2.0 * Li2(1.0 / (1.0 - x) * x * pow(z, -1) - 1.0 / (1.0 - x) * x) * x * pow(NQCD, 2) - 2.0 * Li2(1.0 / (1.0 - x) * x * pow(z, -1) - 1.0 / (1.0 - x) * x) * x * z + 2.0 * Li2(1.0 / (1.0 - x) * x * pow(z, -1) - 1.0 / (1.0 - x) * x) * x * z * pow(NQCD, 2) - 2.0 * Li2(z) * x + 2.0 * Li2(z) * x * pow(NQCD, 2) + 2.0 * Li2(z) * x * z - 2.0 * Li2(z) * x * z * pow(NQCD, 2);
        res += tmp;
    }

    if z < x {
        let tmp: f64 = -pow(pi, 2) * x + pow(pi, 2) * x * pow(NQCD, 2) + pow(pi, 2) * x * z - pow(pi, 2) * x * z * pow(NQCD, 2) - 2.0 * ln(1.0 - z) * x * z + 2.0 * ln(1.0 - z) * x * z * pow(NQCD, 2) + pow(ln(1.0 - z), 2) * x - pow(ln(1.0 - z), 2) * x * pow(NQCD, 2) - pow(ln(1.0 - z), 2) * x * z + pow(ln(1.0 - z), 2) * x * z * pow(NQCD, 2) - 4.0 * ln(1.0 - x) * x * z + 4.0 * ln(1.0 - x) * x * z * pow(NQCD, 2) + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, 2) - 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + 4.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, 2) + 4.0 * pow(ln(1.0 - x), 2) * x - 4.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, 2) - 4.0 * pow(ln(1.0 - x), 2) * x * z + 4.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, 2) + 6.0 * ln(x) * x * z - 6.0 * ln(x) * x * z * pow(NQCD, 2) - 8.0 * ln(x) * ln(1.0 - z) * x + 8.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, 2) + 8.0 * ln(x) * ln(1.0 - z) * x * z - 8.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, 2) - 10.0 * ln(x) * ln(1.0 - x) * x + 10.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, 2) + 10.0 * ln(x) * ln(1.0 - x) * x * z - 10.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, 2) + 2.0 * ln(x) * ln(-z + x) * x - 2.0 * ln(x) * ln(-z + x) * x * pow(NQCD, 2) - 2.0 * ln(x) * ln(-z + x) * x * z + 2.0 * ln(x) * ln(-z + x) * x * z * pow(NQCD, 2) + 6.0 * pow(ln(x), 2) * x - 6.0 * pow(ln(x), 2) * x * pow(NQCD, 2) - 6.0 * pow(ln(x), 2) * x * z + 6.0 * pow(ln(x), 2) * x * z * pow(NQCD, 2) - 10.0 * ln(x) * ln(z) * x + 10.0 * ln(x) * ln(z) * x * pow(NQCD, 2) + 10.0 * ln(x) * ln(z) * x * z - 10.0 * ln(x) * ln(z) * x * z * pow(NQCD, 2) - 4.0 * ln(z) * x * z + 4.0 * ln(z) * x * z * pow(NQCD, 2) + 4.0 * ln(z) * ln(1.0 - z) * x - 4.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, 2) - 4.0 * ln(z) * ln(1.0 - z) * x * z + 4.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, 2) + 8.0 * ln(z) * ln(1.0 - x) * x - 8.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, 2) - 8.0 * ln(z) * ln(1.0 - x) * x * z + 8.0 * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, 2) - 2.0 * ln(z) * ln(-z + x) * x + 2.0 * ln(z) * ln(-z + x) * x * pow(NQCD, 2) + 2.0 * ln(z) * ln(-z + x) * x * z - 2.0 * ln(z) * ln(-z + x) * x * z * pow(NQCD, 2) + 4.0 * pow(ln(z), 2) * x - 4.0 * pow(ln(z), 2) * x * pow(NQCD, 2) - 4.0 * pow(ln(z), 2) * x * z + 4.0 * pow(ln(z), 2) * x * z * pow(NQCD, 2) + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * pow(NQCD, 2) - 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z + 2.0 * Li2(1.0 / (1.0 - z) - 1.0 / (1.0 - z) * x) * x * z * pow(NQCD, 2) - 2.0 * Li2(1.0 / (1.0 - z) * pow(x, -1) * z - 1.0 / (1.0 - z) * z) * x + 2.0 * Li2(1.0 / (1.0 - z) * pow(x, -1) * z - 1.0 / (1.0 - z) * z) * x * pow(NQCD, 2) + 2.0 * Li2(1.0 / (1.0 - z) * pow(x, -1) * z - 1.0 / (1.0 - z) * z) * x * z - 2.0 * Li2(1.0 / (1.0 - z) * pow(x, -1) * z - 1.0 / (1.0 - z) * z) * x * z * pow(NQCD, 2) - 2.0 * Li2(z) * x + 2.0 * Li2(z) * x * pow(NQCD, 2) + 2.0 * Li2(z) * x * z - 2.0 * Li2(z) * x * z * pow(NQCD, 2);
        res += tmp;
    }

    if z != x && z != 1. - x {
        let tmp: f64 = (-6.0) + 1. / 2. * pow(z, -1) * pow(NQCD, -2) + (- pow(z, -1)) + 1. / 2. * pow(z, -1) * pow(NQCD, 2) + pow(NQCD, -2) + 5.0 * pow(NQCD, 2) + 1. / 2. * z * pow(NQCD, -2) + 3.0 * z + (- 7. / 2. * z * pow(NQCD, 2)) + (- 2.0 * pow(z, 2) * pow(NQCD, -2)) + 4.0 * pow(z, 2) + (- 2.0 * pow(z, 2) * pow(NQCD, 2)) + (- 1. / 2. * x * pow(z, -1) * pow(NQCD, -2)) + (- 3.0 * x * pow(z, -1)) + 7. / 2. * x * pow(z, -1) * pow(NQCD, 2) + (- 17. / 2. * x * pow(NQCD, -2)) + 20.0 * x + (- 4.0 * x * pow(rln2, 2)) + (- 23. / 2. * x * pow(NQCD, 2)) + 4.0 * x * pow(NQCD, 2) * pow(rln2, 2) + 9.0 * x * z * pow(NQCD, -2) + (- 12.0 * x * z) + (- 4.0 * x * z * pow(rln2, 2)) + 3.0 * x * z * pow(NQCD, 2) + 4.0 * x * z * pow(NQCD, 2) * pow(rln2, 2) + (- 5.0 * x * pow(z, 2)) + 5.0 * x * pow(z, 2) * pow(NQCD, 2) + 4. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) + (- 4. / 3. * pow(pi, 2) * x * pow(z, -1)) + (- 23. / 6. * pow(pi, 2) * x * pow(NQCD, -2)) + 13. / 3. * pow(pi, 2) * x + (- 1. / 2. * pow(pi, 2) * x * pow(NQCD, 2)) + 7. / 3. * pow(pi, 2) * x * z * pow(NQCD, -2) + (- 14. / 3. * pow(pi, 2) * x * z) + 7. / 3. * pow(pi, 2) * x * z * pow(NQCD, 2) + (- 2.0 * ln(1.0 - z)) + ln(1.0 - z) * pow(NQCD, -2) + ln(1.0 - z) * pow(NQCD, 2) + ln(1.0 - z) * z * pow(NQCD, -2) + (- ln(1.0 - z) * z * pow(NQCD, 2)) + (- 2.0 * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -2)) + 2.0 * ln(1.0 - z) * pow(z, 2) + ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) + (- 4.0 * ln(1.0 - z) * x * pow(z, -1)) + 3.0 * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, 2) + 7. / 2. * ln(1.0 - z) * x * pow(NQCD, -2) + (- ln(1.0 - z) * x) + (- 5. / 2. * ln(1.0 - z) * x * pow(NQCD, 2)) + (- 9. / 2. * ln(1.0 - z) * x * z * pow(NQCD, -2)) + 5.0 * ln(1.0 - z) * x * z + (- 1. / 2. * ln(1.0 - z) * x * z * pow(NQCD, 2)) + 2.0 * ln(1.0 - z) * x * pow(z, 2) + (- 2.0 * ln(1.0 - z) * x * pow(z, 2) * pow(NQCD, 2)) + (- 4.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) * pow(NQCD, -2)) + 4.0 * pow(ln(1.0 - z), 2) * x * pow(z, -1) + 12.0 * pow(ln(1.0 - z), 2) * x * pow(NQCD, -2) + (- 15.0 * pow(ln(1.0 - z), 2) * x) + 3.0 * pow(ln(1.0 - z), 2) * x * pow(NQCD, 2) + (- 8.0 * pow(ln(1.0 - z), 2) * x * z * pow(NQCD, -2)) + 11.0 * pow(ln(1.0 - z), 2) * x * z + (- 3.0 * pow(ln(1.0 - z), 2) * x * z * pow(NQCD, 2)) + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * rln2 + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2) * rln2) + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * rln2 + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2) * rln2) + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2) + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z) + 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2) + 2.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1) * pow(NQCD, -2) + (- 2.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1)) + 2.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, -2) + 2.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x + (- 4.0 * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, 2)) + 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * rln2 + (- 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2) * rln2) + 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * rln2 + (- 4.0 * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2) * rln2) + (- 2.0 * ln(1.0 - x)) + ln(1.0 - x) * pow(NQCD, -2) + ln(1.0 - x) * pow(NQCD, 2) + (- ln(1.0 - x) * z * pow(NQCD, -2)) + 2.0 * ln(1.0 - x) * z + (- ln(1.0 - x) * z * pow(NQCD, 2)) + ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + (- 4.0 * ln(1.0 - x) * x * pow(z, -1)) + 3.0 * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, 2) + 7. / 2. * ln(1.0 - x) * x * pow(NQCD, -2) + (- 3.0 * ln(1.0 - x) * x) + (- 1. / 2. * ln(1.0 - x) * x * pow(NQCD, 2)) + (- 9. / 2. * ln(1.0 - x) * x * z * pow(NQCD, -2)) + 9.0 * ln(1.0 - x) * x * z + (- 9. / 2. * ln(1.0 - x) * x * z * pow(NQCD, 2)) + 2.0 * ln(1.0 - x) * x * pow(z, 2) + (- 2.0 * ln(1.0 - x) * x * pow(z, 2) * pow(NQCD, 2)) + (- 6.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2)) + 6.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(z, -1) + 18.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, -2) + (- 26.0 * ln(1.0 - x) * ln(1.0 - z) * x) + 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * pow(NQCD, 2) + (- 12.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, -2)) + 20.0 * ln(1.0 - x) * ln(1.0 - z) * x * z + (- 8.0 * ln(1.0 - x) * ln(1.0 - z) * x * z * pow(NQCD, 2)) + (- 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) * pow(NQCD, -2)) + 4.0 * pow(ln(1.0 - x), 2) * x * pow(z, -1) + 10.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, -2) + (- 15.0 * pow(ln(1.0 - x), 2) * x) + 5.0 * pow(ln(1.0 - x), 2) * x * pow(NQCD, 2) + (- 6.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, -2)) + 11.0 * pow(ln(1.0 - x), 2) * x * z + (- 5.0 * pow(ln(1.0 - x), 2) * x * z * pow(NQCD, 2)) + 2.0 * ln(x) + (- ln(x) * pow(NQCD, -2)) + (- ln(x) * pow(NQCD, 2)) + (- ln(x) * z * pow(NQCD, -2)) + ln(x) * z * pow(NQCD, 2) + 2.0 * ln(x) * pow(z, 2) * pow(NQCD, -2) + (- 2.0 * ln(x) * pow(z, 2)) + (- 1. / 2. * ln(x) * x * pow(z, -1) * pow(NQCD, -2)) + 4.0 * ln(x) * x * pow(z, -1) + (- 7. / 2. * ln(x) * x * pow(z, -1) * pow(NQCD, 2)) + (- 15. / 2. * ln(x) * x * pow(NQCD, -2)) + 11.0 * ln(x) * x + (- 2.0 * ln(x) * x * rln2) + (- 7. / 2. * ln(x) * x * pow(NQCD, 2)) + 2.0 * ln(x) * x * pow(NQCD, 2) * rln2 + 8.0 * ln(x) * x * z * pow(NQCD, -2) + (- 17.0 * ln(x) * x * z) + (- 2.0 * ln(x) * x * z * rln2) + 9.0 * ln(x) * x * z * pow(NQCD, 2) + 2.0 * ln(x) * x * z * pow(NQCD, 2) * rln2 + (- 4.0 * ln(x) * x * pow(z, 2)) + 4.0 * ln(x) * x * pow(z, 2) * pow(NQCD, 2) + 10.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2) + (- 10.0 * ln(x) * ln(1.0 - z) * x * pow(z, -1)) + (- 31.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, -2)) + 42.0 * ln(x) * ln(1.0 - z) * x + (- 11.0 * ln(x) * ln(1.0 - z) * x * pow(NQCD, 2)) + 21.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, -2) + (- 32.0 * ln(x) * ln(1.0 - z) * x * z) + 11.0 * ln(x) * ln(1.0 - z) * x * z * pow(NQCD, 2) + 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2)) + 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + (- 2.0 * ln(x) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2)) + 10.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2) + (- 10.0 * ln(x) * ln(1.0 - x) * x * pow(z, -1)) + (-28.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, -2)) + 42.0 * ln(x) * ln(1.0 - x) * x + (- 14.0 * ln(x) * ln(1.0 - x) * x * pow(NQCD, 2)) + 18.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, -2) + (- 32.0 * ln(x) * ln(1.0 - x) * x * z) + 14.0 * ln(x) * ln(1.0 - x) * x * z * pow(NQCD, 2) + (- 7.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2)) + 7.0 * pow(ln(x), 2) * x * pow(z, -1) + 22.0 * pow(ln(x), 2) * x * pow(NQCD, -2) + (- 30.0 * pow(ln(x), 2) * x) + 8.0 * pow(ln(x), 2) * x * pow(NQCD, 2) + (- 15.0 * pow(ln(x), 2) * x * z * pow(NQCD, -2)) + 23.0 * pow(ln(x), 2) * x * z + (- 8.0 * pow(ln(x), 2) * x * z * pow(NQCD, 2)) + 6.0 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) + (- 6.0 * ln(x) * ln(z) * x * pow(z, -1)) + (- 20.0 * ln(x) * ln(z) * x * pow(NQCD, -2)) + 36.0 * ln(x) * ln(z) * x + (- 16.0 * ln(x) * ln(z) * x * pow(NQCD, 2)) + 17.0 * ln(x) * ln(z) * x * z * pow(NQCD, -2) + (- 16.0 * ln(x) * ln(z) * x * z) + (- ln(x) * ln(z) * x * z * pow(NQCD, 2)) + (- ln(x) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1) * pow(NQCD, -2)) + ln(x) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1) + (- ln(x) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, -2)) + (- ln(x) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x) + 2.0 * ln(x) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, 2) + (- 6.0 * ln(z)) + 2.0 * ln(z) * pow(NQCD, -2) + 4.0 * ln(z) * pow(NQCD, 2) + (- 4.0 * ln(z) * z) + 4.0 * ln(z) * z * pow(NQCD, 2) + 2.0 * ln(z) * x * pow(z, -1) * pow(NQCD, -2) + (- 7.0 * ln(z) * x * pow(z, -1)) + 5.0 * ln(z) * x * pow(z, -1) * pow(NQCD, 2) + 6.0 * ln(z) * x * pow(NQCD, -2) + (- 8.0 * ln(z) * x) + (- 6.0 * ln(z) * x * rln2) + 2.0 * ln(z) * x * pow(NQCD, 2) + 6.0 * ln(z) * x * pow(NQCD, 2) * rln2 + (- 9.0 * ln(z) * x * z * pow(NQCD, -2)) + 23.0 * ln(z) * x * z + (- 6.0 * ln(z) * x * z * rln2) + (- 14.0 * ln(z) * x * z * pow(NQCD, 2)) + 6.0 * ln(z) * x * z * pow(NQCD, 2) * rln2 + 2.0 * ln(z) * x * pow(z, 2) + (- 2.0 * ln(z) * x * pow(z, 2) * pow(NQCD, 2)) + (- 2.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) * pow(NQCD, -2)) + 2.0 * ln(z) * ln(1.0 - z) * x * pow(z, -1) + 12.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, -2) + (- 22.0 * ln(z) * ln(1.0 - z) * x) + 10.0 * ln(z) * ln(1.0 - z) * x * pow(NQCD, 2) + (- 10.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, -2)) + 20.0 * ln(z) * ln(1.0 - z) * x * z + (- 10.0 * ln(z) * ln(1.0 - z) * x * z * pow(NQCD, 2)) + 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2)) + 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + (- 2.0 * ln(z) * ln(1.0 - z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2)) + 4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2)) + 4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + (- 4.0 * ln(z) * ln(1.0 + z + mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2)) + (- 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) * pow(NQCD, -2)) + 4.0 * ln(z) * ln(1.0 - x) * x * pow(z, -1) + 12.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, -2) + (- 24.0 * ln(z) * ln(1.0 - x) * x) + 12.0 * ln(z) * ln(1.0 - x) * x * pow(NQCD, 2) + (- 9.0 * ln(z) * ln(1.0 - x) * x * z * pow(NQCD, -2)) + 10.0 * ln(z) * ln(1.0 - x) * x * z + (- ln(z) * ln(1.0 - x) * x * z * pow(NQCD, 2)) + (- pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2)) + pow(ln(z), 2) * x * pow(z, -1) + 5.0 * pow(ln(z), 2) * x * pow(NQCD, -2) + (- 13.0 * pow(ln(z), 2) * x) + 8.0 * pow(ln(z), 2) * x * pow(NQCD, 2) + (- 5.0 * pow(ln(z), 2) * x * z * pow(NQCD, -2)) + (- 2.0 * pow(ln(z), 2) * x * z) + 7.0 * pow(ln(z), 2) * x * z * pow(NQCD, 2) + (- ln(z) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1) * pow(NQCD, -2)) + ln(z) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1) + (- ln(z) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, -2)) + (- ln(z) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x) + 2.0 * ln(z) * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, 2) + (- 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x) + 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * pow(NQCD, 2) + (- 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z) + 2.0 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z * pow(NQCD, 2) + 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x + (- 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * pow(NQCD, 2)) + 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z + (- 2.0 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * pow(z, -1)) * x * z * pow(NQCD, 2)) + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x + (- 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2)) + 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z + (- 2.0 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2)) + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x) + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * pow(NQCD, 2) + (- 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z) + 2.0 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z)) * x * z * pow(NQCD, 2) + (- 2.0 * Li2(1.0 - x * pow(z, -1)) * x * pow(NQCD, -2)) + 4.0 * Li2(1.0 - x * pow(z, -1)) * x + (- 2.0 * Li2(1.0 - x * pow(z, -1)) * x * pow(NQCD, 2)) + 2.0 * Li2(1.0 - x * pow(z, -1)) * x * z * pow(NQCD, -2) + (- 4.0 * Li2(1.0 - x * pow(z, -1)) * x * z) + 2.0 * Li2(1.0 - x * pow(z, -1)) * x * z * pow(NQCD, 2) + Li2(x) * x * pow(NQCD, -2) + (- Li2(x) * x * pow(NQCD, 2)) + (- Li2(x) * x * z * pow(NQCD, -2)) + Li2(x) * x * z * pow(NQCD, 2) + 2.0 * Li2(z) * x * pow(z, -1) * pow(NQCD, -2) + (- 2.0 * Li2(z) * x * pow(z, -1)) + (- 2.0 * Li2(z) * x * pow(NQCD, -2)) + 2.0 * Li2(z) * x + Li2(z) * x * z * pow(NQCD, -2) + 10.0 * Li2(z) * x * z + (- 11.0 * Li2(z) * x * z * pow(NQCD, 2)) + (- 2.0 * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1) * pow(NQCD, -2) * rln2) + 2.0 * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(z, -1) * rln2 + (- 2.0 * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, -2) * rln2) + (- 2.0 * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * rln2) + 4.0 * mysqrt(1.0 - 2.0 * z + pow(z, 2) + 4.0 * x * z) * x * pow(NQCD, 2) * rln2 + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * z * pow(NQCD, -2) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * z) + (- 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -2)) + 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 2) + 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 3) * pow(NQCD, -2) + (- 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 3)) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 4) * pow(NQCD, -2)) + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(1.0 - z) * pow(z, 4) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * z * pow(NQCD, -2)) + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * z + 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * pow(NQCD, -2) + (- 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 2)) + (- 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) * pow(NQCD, -2)) + 6.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) + 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 4) * pow(NQCD, -2) + (- 2.0 / (1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)) * ln(x) * pow(z, 4)) + (- 2.0 / (1.0 - z - x) * z * pow(NQCD, -2)) + 2.0 / (1.0 - z - x) * z + 4.0 / (1.0 - z - x) * pow(z, 2) * pow(NQCD, -2) + (- 4.0 / (1.0 - z - x) * pow(z, 2)) + (- 2.0 / (1.0 - z - x) * pow(z, 3) * pow(NQCD, -2)) + 2.0 / (1.0 - z - x) * pow(z, 3) + (- 4.0 / (1.0 - z - x) * ln(1.0 - z) * z * pow(NQCD, -2)) + 4.0 / (1.0 - z - x) * ln(1.0 - z) * z + 8.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 2) * pow(NQCD, -2) + (- 8.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 2)) + (- 4.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 3) * pow(NQCD, -2)) + 4.0 / (1.0 - z - x) * ln(1.0 - z) * pow(z, 3) + 4.0 / (1.0 - z - x) * ln(x) * z * pow(NQCD, -2) + (- 4.0 / (1.0 - z - x) * ln(x) * z) + (- 8.0 / (1.0 - z - x) * ln(x) * pow(z, 2) * pow(NQCD, -2)) + 8.0 / (1.0 - z - x) * ln(x) * pow(z, 2) + 4.0 / (1.0 - z - x) * ln(x) * pow(z, 3) * pow(NQCD, -2) + (- 4.0 / (1.0 - z - x) * ln(x) * pow(z, 3));
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
        let tmp: f64 = (- 2.0 * lmua * x * pow(z, -1) * pow(NQCD, -2)) + 8.0 * lmua * x * pow(z, -1) + (-6.0 * lmua * x * pow(z, -1) * pow(NQCD, 2)) + 4.0 * lmua * x * pow(NQCD, -2) + 10. / 3. * lmua * x + (- 22. / 3. * lmua * x * pow(NQCD, 2)) + (- 4. / 3. * lmua * x * NF * pow(NQCD, -1)) + 4. / 3. * lmua * x * NF * NQCD + (- 2.0 * lmua * x * z * pow(NQCD, -2)) + (- 22. / 3. * lmua * x * z) + 28. / 3. * lmua * x * z * pow(NQCD, 2) + 4. / 3. * lmua * x * z * NF * pow(NQCD, -1) + (- 4. / 3. * lmua * x * z * NF * NQCD) + (- 4.0 * lmua * x * pow(z, 2)) + 4.0 * lmua * x * pow(z, 2) * pow(NQCD, 2) + 8.0 * lmua * ln(1.0 - z) * x + (- 8.0 * lmua * ln(1.0 - z) * x * pow(NQCD, 2)) + (- 8.0 * lmua * ln(1.0 - z) * x * z) + 8.0 * lmua * ln(1.0 - z) * x * z * pow(NQCD, 2) + 8.0 * ln(z) * lmua * x + (-8.0 * ln(z) * lmua * x * pow(NQCD, 2)) + 2.0 * ln(z) * lmua * x * z * pow(NQCD, -2) + 12.0 * ln(z) * lmua * x * z + (- 14.0 * ln(z) * lmua * x * z * pow(NQCD, 2));
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
        let tmp: f64 = 4.0 * lmuf + (- 2.0 * lmuf * pow(NQCD, -2)) + (- 2.0 * lmuf * pow(NQCD, 2)) + 2.0 * lmuf * z * pow(NQCD, -2) + (- 4.0 * lmuf * z) + 2.0 * lmuf * z * pow(NQCD, 2) + (- lmuf * x * pow(NQCD, -2)) + 2.0 * lmuf * x + (- lmuf * x * pow(NQCD, 2)) + lmuf * x * z * pow(NQCD, -2) + (- 2.0 * lmuf * x * z) + lmuf * x * z * pow(NQCD, 2) + (- 4.0 * lmuf * ln(1.0 - x) * x * pow(NQCD, -2)) + 8.0 * lmuf * ln(1.0 - x) * x + (- 4.0 * lmuf * ln(1.0 - x) * x * pow(NQCD, 2)) + 4.0 * lmuf * ln(1.0 - x) * x * z * pow(NQCD, -2) + (- 8.0 * lmuf * ln(1.0 - x) * x * z) + 4.0 * lmuf * ln(1.0 - x) * x * z * pow(NQCD, 2) + 2.0 * ln(x) * lmuf * x * pow(NQCD, -2) + (- 4.0 * ln(x) * lmuf * x) + 2.0 * ln(x) * lmuf * x * pow(NQCD, 2) + (- 2.0 * ln(x) * lmuf * x * z * pow(NQCD, -2)) + 4.0 * ln(x) * lmuf * x * z + (- 2.0 * ln(x) * lmuf * x * z * pow(NQCD, 2));
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
        let tmp: f64 = (- 22. / 3. * lmur * x) + 22. / 3. * lmur * x * pow(NQCD, 2) + 4. / 3. * lmur * x * NF * pow(NQCD, -1) + (- 4. / 3. * lmur * x * NF * NQCD) + 22. / 3. * lmur * x * z + (- 22. / 3. * lmur * x * z * pow(NQCD, 2)) + (- 4. / 3. * lmur * x * z * NF * pow(NQCD, -1)) + 4. / 3. * lmur * x * z * NF * NQCD;
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
