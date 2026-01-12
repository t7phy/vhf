#include "../sidis.h"



/* Helpers */

double RG_RG_000(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_000(x0, z0, NF);
        double pt1 = RG_RG_000(x1, z1, NF);
        double pt2 = RG_RG_000(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_000(x0, z0, NF);
        double pt1 = RG_RG_000(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_000(x0, z0, NF);
        double pt1 = RG_RG_000(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }


    if (z < 1. - x && z < x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z > 1. - x && z < x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z < 1. - x && z > x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z > 1. - x && z > x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z > x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z < x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z < 1. - x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z > 1. - x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = (-5. / 8. * pow(x, -1) * pow(z, -1) * NQCD) + 5. / 8. * pow(x, -1) * NQCD + (- 5. / 8. * pow(z, -2) * NQCD) + 13. / 8. * pow(z, -1) * pow(NQCD, -1) + (- 11. / 8. * pow(z, -1) * NQCD) + 4 * pow(z, -1) * NQCD * pow(rln2, 2) + 1. / 4. * pow(NQCD, -1) + 8 * pow(NQCD, -1) * pow(rln2, 2) + (- 1. / 2. * NQCD) + (- 4 * NQCD * pow(rln2, 2)) + (- 27. / 8. * z * pow(NQCD, -1)) + (- 4 * z * pow(NQCD, -1) * pow(rln2, 2)) + 4 * z * NQCD + 4 * z * NQCD * pow(rln2, 2) + 5. / 8. * x * pow(z, -2) * NQCD + 1. / 2. * x * pow(z, -1) * pow(NQCD, -1) + (- 47. / 4. * x * pow(z, -1) * NQCD) + (- 8 * x * pow(z, -1) * NQCD * pow(rln2, 2)) + x * pow(NQCD, -1) + (- 16 * x * pow(NQCD, -1) * pow(rln2, 2)) + 41. / 4. * x * NQCD + 8 * x * NQCD * pow(rln2, 2) + 1. / 2. * x * z * pow(NQCD, -1) + 8 * x * z * pow(NQCD, -1) * pow(rln2, 2) + (- 9. / 8. * x * z * NQCD) + (- 8 * x * z * NQCD * pow(rln2, 2)) + pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + 117. / 8. * pow(x, 2) * pow(z, -1) * NQCD + 8 * pow(x, 2) * pow(z, -1) * NQCD * pow(rln2, 2) + (- 9. / 2. * pow(x, 2) * pow(NQCD, -1)) + 8 * pow(x, 2) * pow(NQCD, -1) * pow(rln2, 2) + (- 89. / 8. * pow(x, 2) * NQCD) + 3 * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * pow(x, 2) * z * pow(NQCD, -1) * pow(rln2, 2)) + (- 3 * pow(x, 2) * z * NQCD) + 8 * pow(x, 2) * z * NQCD * pow(rln2, 2) + 7. / 12. * pow(pi, 2) * pow(z, -1) * pow(NQCD, -1) + (- 7. / 12. * pow(pi, 2) * pow(z, -1) * NQCD) + (- 1. / 2. * pow(pi, 2) * pow(NQCD, -1)) + 1. / 2. * pow(pi, 2) * NQCD + 1. / 2. * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 2. * pow(pi, 2) * z * NQCD) + (- 7. / 6. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -1)) + 7. / 6. * pow(pi, 2) * x * pow(z, -1) * NQCD + pow(pi, 2) * x * pow(NQCD, -1) + (- pow(pi, 2) * x * NQCD) + (- 2. / 3. * pow(pi, 2) * x * z * pow(NQCD, -1)) + 2. / 3. * pow(pi, 2) * x * z * NQCD + 4. / 3. * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) +  + (-4. / 3. * pow(pi, 2) * pow(x, 2) * pow(z, -1) * NQCD) + (- 2. / 3. * pow(pi, 2) * pow(x, 2) * pow(NQCD, -1)) + 2. / 3. * pow(pi, 2) * pow(x, 2) * NQCD + pow(pi, 2) * pow(x, 2) * z * pow(NQCD, -1) + (- pow(pi, 2) * pow(x, 2) * z * NQCD) + 15. / 4. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 15. / 4. * ln(1 - z) * pow(z, -1) * NQCD) + (- 7. / 2. * ln(1 - z) * pow(NQCD, -1)) + 7. / 2. * ln(1 - z) * NQCD + 3. / 4. * ln(1 - z) * z * pow(NQCD, -1) + (- 3. / 4. * ln(1 - z) * z * NQCD) + (- 10 * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 10 * ln(1 - z) * x * pow(z, -1) * NQCD + 8 * ln(1 - z) * x * pow(NQCD, -1) + (- 8 * ln(1 - z) * x * NQCD) + (- 1. / 2. * ln(1 - z) * x * z * pow(NQCD, -1)) + 1. / 2. * ln(1 - z) * x * z * NQCD + 9 * ln(1 - z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 9 * ln(1 - z) * pow(x, 2) * pow(z, -1) * NQCD) + (- 7 * ln(1 - z) * pow(x, 2) * pow(NQCD, -1)) + 7 * ln(1 - z) * pow(x, 2) * NQCD + (- ln(1 - z) * pow(x, 2) * z * pow(NQCD, -1)) + ln(1 - z) * pow(x, 2) * z * NQCD + (- pow(ln(1 - z), 2) * pow(z, -1) * pow(NQCD, -1)) + pow(ln(1 - z), 2) * pow(z, -1) * NQCD + pow(ln(1 - z), 2) * pow(NQCD, -1) + (- pow(ln(1 - z), 2) * NQCD) + (- 1. / 2. * pow(ln(1 - z), 2) * z * pow(NQCD, -1)) + 1. / 2. * pow(ln(1 - z), 2) * z * NQCD + 2 * pow(ln(1 - z), 2) * x * pow(z, -1) * pow(NQCD, -1) + (- 2 * pow(ln(1 - z), 2) * x * pow(z, -1) * NQCD) + (- 2 * pow(ln(1 - z), 2) * x * pow(NQCD, -1)) + 2 * pow(ln(1 - z), 2) * x * NQCD + pow(ln(1 - z), 2) * x * z * pow(NQCD, -1) + (- pow(ln(1 - z), 2) * x * z * NQCD) + (- 2 * pow(ln(1 - z), 2) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 2 * pow(ln(1 - z), 2) * pow(x, 2) * pow(z, -1) * NQCD + 2 * pow(ln(1 - z), 2) * pow(x, 2) * pow(NQCD, -1) + (- 2 * pow(ln(1 - z), 2) * pow(x, 2) * NQCD) + (- pow(ln(1 - z), 2) * pow(x, 2) * z * pow(NQCD, -1)) +  + pow(ln(1 - z), 2) * pow(x, 2) * z * NQCD + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * pow(NQCD, -1) * rln2 + (- 6 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD * rln2) + (- 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) * rln2) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * NQCD * rln2 + 6 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1) * rln2 + (- 6 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD * rln2) + (- 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * pow(NQCD, -1) * rln2) + 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD * rln2 + 24 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) * rln2 + (- 16 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD * rln2) + (- 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) * rln2) + 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD * rln2 + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) * rln2 + (- 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD * rln2) + (- 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) * rln2) + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD * rln2 + 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) * rln2 + (- 12 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD * rln2) + (- 2 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(z, -1) * pow(NQCD, -1)) +  + 2 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(z, -1) * NQCD + 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(NQCD, -1) + (- 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * NQCD) + (- 2 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * z * pow(NQCD, -1)) + 2 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * z * NQCD + 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * pow(z, -1) * pow(NQCD, -1) + (- 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * pow(z, -1) * NQCD) + (- 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * pow(NQCD, -1)) + 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * NQCD + 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * z * pow(NQCD, -1) + (- 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * z * NQCD) + (- 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * pow(z, -1) * NQCD + 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * pow(NQCD, -1) + (- 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * NQCD) + (- 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * z * NQCD + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * pow(NQCD, -1) +  + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1)) + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD + (- 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * pow(NQCD, -1)) + (- 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD) + (- 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) + (- 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD) + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) +  + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD + (- 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD + (- 4 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * NQCD) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD + (- 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD) + (- 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * pow(NQCD, -1) * rln2) + (- 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD * rln2) + (- 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) * rln2) + 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1) * rln2 + (- 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD * rln2) + 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * pow(NQCD, -1) * rln2 + 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD * rln2 + 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) * rln2 + (- 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) * rln2) + 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD * rln2 + (- 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) * rln2) +  + (-4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD * rln2) + (- 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) * rln2) + (- 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD * rln2) + 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) * rln2 + (- 4 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD * rln2) + 15. / 4. * ln(1 - x) * pow(z, -1) * pow(NQCD, -1) + (- 15. / 4. * ln(1 - x) * pow(z, -1) * NQCD) + (- 7. / 2. * ln(1 - x) * pow(NQCD, -1)) + 7. / 2. * ln(1 - x) * NQCD + 3. / 4. * ln(1 - x) * z * pow(NQCD, -1) + (- 3. / 4. * ln(1 - x) * z * NQCD) + (- 10 * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1)) + 10 * ln(1 - x) * x * pow(z, -1) * NQCD + 8 * ln(1 - x) * x * pow(NQCD, -1) + (- 8 * ln(1 - x) * x * NQCD) + (- 1. / 2. * ln(1 - x) * x * z * pow(NQCD, -1)) + 1. / 2. * ln(1 - x) * x * z * NQCD + 9 * ln(1 - x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 9 * ln(1 - x) * pow(x, 2) * pow(z, -1) * NQCD) + (- 7 * ln(1 - x) * pow(x, 2) * pow(NQCD, -1)) + 7 * ln(1 - x) * pow(x, 2) * NQCD + (- ln(1 - x) * pow(x, 2) * z * pow(NQCD, -1)) + ln(1 - x) * pow(x, 2) * z * NQCD + (- 2 * ln(1 - x) * ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + 2 * ln(1 - x) * ln(1 - z) * pow(z, -1) * NQCD + 2 * ln(1 - x) * ln(1 - z) * pow(NQCD, -1) + (- 2 * ln(1 - x) * ln(1 - z) * NQCD) + (- ln(1 - x) * ln(1 - z) * z * pow(NQCD, -1)) + ln(1 - x) * ln(1 - z) * z * NQCD + 4 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1) + (- 4 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) * NQCD) + (- 4 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, -1)) + 4 * ln(1 - x) * ln(1 - z) * x * NQCD + 2 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, -1) +  + (-2 * ln(1 - x) * ln(1 - z) * x * z * NQCD) + (- 4 * ln(1 - x) * ln(1 - z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 4 * ln(1 - x) * ln(1 - z) * pow(x, 2) * pow(z, -1) * NQCD + 4 * ln(1 - x) * ln(1 - z) * pow(x, 2) * pow(NQCD, -1) + (- 4 * ln(1 - x) * ln(1 - z) * pow(x, 2) * NQCD) + (- 2 * ln(1 - x) * ln(1 - z) * pow(x, 2) * z * pow(NQCD, -1)) + 2 * ln(1 - x) * ln(1 - z) * pow(x, 2) * z * NQCD + (- pow(ln(1 - x), 2) * pow(z, -1) * pow(NQCD, -1)) + pow(ln(1 - x), 2) * pow(z, -1) * NQCD + pow(ln(1 - x), 2) * pow(NQCD, -1) + (- pow(ln(1 - x), 2) * NQCD) + (- 1. / 2. * pow(ln(1 - x), 2) * z * pow(NQCD, -1)) + 1. / 2. * pow(ln(1 - x), 2) * z * NQCD + 2 * pow(ln(1 - x), 2) * x * pow(z, -1) * pow(NQCD, -1) + (- 2 * pow(ln(1 - x), 2) * x * pow(z, -1) * NQCD) + (- 2 * pow(ln(1 - x), 2) * x * pow(NQCD, -1)) + 2 * pow(ln(1 - x), 2) * x * NQCD + pow(ln(1 - x), 2) * x * z * pow(NQCD, -1) + (- pow(ln(1 - x), 2) * x * z * NQCD) + (- 2 * pow(ln(1 - x), 2) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 2 * pow(ln(1 - x), 2) * pow(x, 2) * pow(z, -1) * NQCD + 2 * pow(ln(1 - x), 2) * pow(x, 2) * pow(NQCD, -1) + (- 2 * pow(ln(1 - x), 2) * pow(x, 2) * NQCD) + (- pow(ln(1 - x), 2) * pow(x, 2) * z * pow(NQCD, -1)) + pow(ln(1 - x), 2) * pow(x, 2) * z * NQCD +  +  +  +  + (- 5. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD) + (- 9. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD) +  + 3 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1) + (- 21. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD) + (- 5. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD) + (- 3 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1)) + (- 5. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * NQCD) + (- 3 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1)) + 19. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD + (- 45. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD) + 15 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1) + (- 105. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * NQCD) + 35. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD + 5. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD + 9. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD + (- 3 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1)) + 21. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD +  + 5. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD + 3 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1) + 5. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * NQCD + 3 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 19. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD) + 45. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD + (- 15 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 105. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * NQCD + (- 35. / 8. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD) + 5. / 16. * ln(x) * pow(x, -1) * pow(z, -1) * NQCD + (- 5. / 16. * ln(x) * pow(x, -1) * NQCD) + (- 5. / 16. * ln(x) * pow(z, -2) * NQCD) + (- 7. / 2. * ln(x) * pow(z, -1) * pow(NQCD, -1)) + (- 2 * ln(x) * pow(z, -1) * pow(NQCD, -1) * rln2) + (- 5. / 8. * ln(x) * pow(z, -1) * NQCD) + 4 * ln(x) * pow(z, -1) * NQCD * rln2 + 9. / 2. * ln(x) * pow(NQCD, -1) + 8 * ln(x) * pow(NQCD, -1) * rln2 + (- 3. / 8. * ln(x) * NQCD) + (- 6 * ln(x) * NQCD * rln2) + (- 2 * ln(x) * z * pow(NQCD, -1)) + (- 4 * ln(x) * z * pow(NQCD, -1) * rln2) + 37. / 16. * ln(x) * z * NQCD + 4 * ln(x) * z * NQCD * rln2 + (- 5. / 16. * ln(x) * x * pow(z, -2) * NQCD) + 10 * ln(x) * x * pow(z, -1) * pow(NQCD, -1) + 4 * ln(x) * x * pow(z, -1) * pow(NQCD, -1) * rln2 +  + (-109. / 8. * ln(x) * x * pow(z, -1) * NQCD) + (- 8 * ln(x) * x * pow(z, -1) * NQCD * rln2) + (- 11. / 2. * ln(x) * x * pow(NQCD, -1)) + (- 16 * ln(x) * x * pow(NQCD, -1) * rln2) + 73. / 8. * ln(x) * x * NQCD + 12 * ln(x) * x * NQCD * rln2 + (- 5. / 2. * ln(x) * x * z * pow(NQCD, -1)) + 8 * ln(x) * x * z * pow(NQCD, -1) * rln2 + 45. / 16. * ln(x) * x * z * NQCD + (- 8 * ln(x) * x * z * NQCD * rln2) + (- 9 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + (- 4 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) * rln2) + 109. / 16. * ln(x) * pow(x, 2) * pow(z, -1) * NQCD + 8 * ln(x) * pow(x, 2) * pow(z, -1) * NQCD * rln2 + 7 * ln(x) * pow(x, 2) * pow(NQCD, -1) + 8 * ln(x) * pow(x, 2) * pow(NQCD, -1) * rln2 + (- 77. / 16. * ln(x) * pow(x, 2) * NQCD) + (- 4 * ln(x) * pow(x, 2) * NQCD * rln2) + ln(x) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * ln(x) * pow(x, 2) * z * pow(NQCD, -1) * rln2) + (- ln(x) * pow(x, 2) * z * NQCD) + 8 * ln(x) * pow(x, 2) * z * NQCD * rln2 + 3. / 2. * ln(x) * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 3. / 2. * ln(x) * ln(1 - z) * pow(z, -1) * NQCD) + (- ln(x) * ln(1 - z) * pow(NQCD, -1)) + ln(x) * ln(1 - z) * NQCD + ln(x) * ln(1 - z) * z * pow(NQCD, -1) + (- ln(x) * ln(1 - z) * z * NQCD) + (- 3 * ln(x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 3 * ln(x) * ln(1 - z) * x * pow(z, -1) * NQCD + 2 * ln(x) * ln(1 - z) * x * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - z) * x * NQCD) + 4 * ln(x) * ln(1 - z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 - z) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * ln(x) * ln(1 - z) * pow(x, 2) * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - z) * pow(x, 2) * NQCD + 2 * ln(x) * ln(1 - z) * pow(x, 2) * z * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - z) * pow(x, 2) * z * NQCD) + 2 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * pow(NQCD, -1) +  + (-2 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD) + (- 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * NQCD + 2 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD) + (- 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD + 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD) + (- 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD + 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + (- 2 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD) + (- 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1)) +  + 2 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * NQCD + 2 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD) + 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD + 8 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD) + (- 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + ln(x) * ln(1 - x) * pow(z, -1) * pow(NQCD, -1) + (- ln(x) * ln(1 - x) * pow(z, -1) * NQCD) + (- 2 * ln(x) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1)) + 2 * ln(x) * ln(1 - x) * x * pow(z, -1) * NQCD + 2 * ln(x) * ln(1 - x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - x) * pow(x, 2) * pow(z, -1) * NQCD) + (- 2 * ln(x) * ln(1 - x) * pow(x, 2) * pow(NQCD, -1)) + 2 * ln(x) * ln(1 - x) * pow(x, 2) * NQCD + (- 2 * ln(x) * ln(1 + x) * pow(z, -1) * NQCD) + 2 * ln(x) * ln(1 + x) * pow(NQCD, -1) + 2 * ln(x) * ln(1 + x) * z * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 + x) * z * NQCD) + (- 4 * ln(x) * ln(1 + x) * x * pow(z, -1) * NQCD) + 4 * ln(x) * ln(1 + x) * x * pow(NQCD, -1) +  + 4 * ln(x) * ln(1 + x) * x * z * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 + x) * x * z * NQCD) + (- 4 * ln(x) * ln(1 + x) * pow(x, 2) * pow(z, -1) * NQCD) + 4 * ln(x) * ln(1 + x) * pow(x, 2) * NQCD + 4 * ln(x) * ln(1 + x) * pow(x, 2) * z * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 + x) * pow(x, 2) * z * NQCD) + 2 * ln(x) * ln(1 + x * z) * pow(z, -1) * NQCD + (- 2 * ln(x) * ln(1 + x * z) * z * pow(NQCD, -1)) + 2 * ln(x) * ln(1 + x * z) * z * NQCD + (- 4 * ln(x) * ln(1 + x * z) * x * pow(NQCD, -1)) + 4 * ln(x) * ln(1 + x * z) * pow(x, 2) * pow(z, -1) * NQCD + (- 4 * ln(x) * ln(1 + x * z) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * ln(x) * ln(1 + x * z) * pow(x, 2) * z * NQCD +  + (- 2 * ln(x) * ln(z + x) * pow(NQCD, -1)) + 4 * ln(x) * ln(z + x) * x * pow(z, -1) * NQCD + (- 4 * ln(x) * ln(z + x) * x * z * pow(NQCD, -1)) + 4 * ln(x) * ln(z + x) * x * z * NQCD + (- 4 * ln(x) * ln(z + x) * pow(x, 2) * NQCD) + (- pow(ln(x), 2) * pow(z, -1) * pow(NQCD, -1)) + pow(ln(x), 2) * pow(z, -1) * NQCD + pow(ln(x), 2) * pow(NQCD, -1) + (- pow(ln(x), 2) * NQCD) + (- pow(ln(x), 2) * z * pow(NQCD, -1)) + pow(ln(x), 2) * z * NQCD + 2 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -1) + (- 2 * pow(ln(x), 2) * x * pow(z, -1) * NQCD) + (- 2 * pow(ln(x), 2) * x * pow(NQCD, -1)) + 2 * pow(ln(x), 2) * x * NQCD + (- 3 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 3 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * NQCD + 3 * pow(ln(x), 2) * pow(x, 2) * pow(NQCD, -1) + (- 3 * pow(ln(x), 2) * pow(x, 2) * NQCD) + (- 2 * pow(ln(x), 2) * pow(x, 2) * z * pow(NQCD, -1)) + 2 * pow(ln(x), 2) * pow(x, 2) * z * NQCD + (- 1. / 2. * ln(x) * ln(z) * pow(z, -1) * pow(NQCD, -1)) + (- 3. / 2. * ln(x) * ln(z) * pow(z, -1) * NQCD) + 3 * ln(x) * ln(z) * pow(NQCD, -1) + (- 3 * ln(x) * ln(z) * NQCD) +  + ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -1) + (- 9 * ln(x) * ln(z) * x * pow(z, -1) * NQCD) + 2 * ln(x) * ln(z) * x * pow(NQCD, -1) + (- 6 * ln(x) * ln(z) * x * NQCD) + 6 * ln(x) * ln(z) * x * z * pow(NQCD, -1) + (- 6 * ln(x) * ln(z) * x * z * NQCD) + 4 * ln(x) * ln(z) * pow(x, 2) * NQCD + 2 * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * NQCD + (- 4 * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD) + 4 * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD + (- 5. / 16. * ln(z) * pow(x, -1) * pow(z, -1) * NQCD) + (- 5. / 16. * ln(z) * pow(x, -1) * NQCD) + 5. / 16. * ln(z) * pow(z, -2) * NQCD + 23. / 4. * ln(z) * pow(z, -1) * pow(NQCD, -1) + 2 * ln(z) * pow(z, -1) * pow(NQCD, -1) * rln2 + (- 63. / 8. * ln(z) * pow(z, -1) * NQCD) + 4 * ln(z) * pow(z, -1) * NQCD * rln2 + 2 * ln(z) * pow(NQCD, -1) + 8 * ln(z) * pow(NQCD, -1) * rln2 + (- 33. / 8. * ln(z) * NQCD) + (- 2 * ln(z) * NQCD * rln2) + 1. / 4. * ln(z) * z * pow(NQCD, -1) + (- 4 * ln(z) * z * pow(NQCD, -1) * rln2) + 1. / 16. * ln(z) * z * NQCD + 4 * ln(z) * z * NQCD * rln2 + (- 5. / 16. * ln(z) * x * pow(z, -2) * NQCD) + (- 14 * ln(z) * x * pow(z, -1) * pow(NQCD, -1)) + (- 4 * ln(z) * x * pow(z, -1) * pow(NQCD, -1) * rln2) + 93. / 8. * ln(z) * x * pow(z, -1) * NQCD + (- 8 * ln(z) * x * pow(z, -1) * NQCD * rln2) + (- 3. / 2. * ln(z) * x * pow(NQCD, -1)) + (- 16 * ln(z) * x * pow(NQCD, -1) * rln2) + (- 7. / 8. * ln(z) * x * NQCD) + 4 * ln(z) * x * NQCD * rln2 + (- 2 * ln(z) * x * z * pow(NQCD, -1)) + 8 * ln(z) * x * z * pow(NQCD, -1) * rln2 + 27. / 16. * ln(z) * x * z * NQCD + (- 8 * ln(z) * x * z * NQCD * rln2) + 13 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + 4 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) * rln2 + (- 131. / 16. * ln(z) * pow(x, 2) * pow(z, -1) * NQCD) + 8 * ln(z) * pow(x, 2) * pow(z, -1) * NQCD * rln2 +  + ln(z) * pow(x, 2) * pow(NQCD, -1) + 8 * ln(z) * pow(x, 2) * pow(NQCD, -1) * rln2 + 61. / 16. * ln(z) * pow(x, 2) * NQCD + 4 * ln(z) * pow(x, 2) * NQCD * rln2 + 2 * ln(z) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * ln(z) * pow(x, 2) * z * pow(NQCD, -1) * rln2) + (- 2 * ln(z) * pow(x, 2) * z * NQCD) + 8 * ln(z) * pow(x, 2) * z * NQCD * rln2 + (- 2 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD) + (- 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1)) + 2 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * NQCD + 2 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1) + (- 2 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD) + 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD + 8 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD) + (- 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + (- 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * pow(NQCD, -1)) + (- 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD) +  + (-4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1)) + 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1) + (- 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD) + 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * pow(NQCD, -1) + 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD + 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + (- 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + (- 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD) + 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 4 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + 2 * ln(z) * ln(1 - x) * pow(NQCD, -1) + (- 2 * ln(z) * ln(1 - x) * NQCD) + (- 4 * ln(z) * ln(1 - x) * x * pow(NQCD, -1)) + 4 * ln(z) * ln(1 - x) * x * NQCD + 4 * ln(z) * ln(1 - x) * pow(x, 2) * pow(NQCD, -1) + (- 4 * ln(z) * ln(1 - x) * pow(x, 2) * NQCD) + 2 * ln(z) * ln(1 + x * z) * pow(z, -1) * NQCD + (- 2 * ln(z) * ln(1 + x * z) * z * pow(NQCD, -1)) + 2 * ln(z) * ln(1 + x * z) * z * NQCD + (- 4 * ln(z) * ln(1 + x * z) * x * pow(NQCD, -1)) +  + 4 * ln(z) * ln(1 + x * z) * pow(x, 2) * pow(z, -1) * NQCD + (- 4 * ln(z) * ln(1 + x * z) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * ln(z) * ln(1 + x * z) * pow(x, 2) * z * NQCD +  + 2 * ln(z) * ln(z + x) * pow(NQCD, -1) + (- 4 * ln(z) * ln(z + x) * x * pow(z, -1) * NQCD) + 4 * ln(z) * ln(z + x) * x * z * pow(NQCD, -1) + (- 4 * ln(z) * ln(z + x) * x * z * NQCD) + 4 * ln(z) * ln(z + x) * pow(x, 2) * NQCD + 3 * pow(ln(z), 2) * pow(z, -1) * pow(NQCD, -1) + (- pow(ln(z), 2) * pow(z, -1) * NQCD) + 1. / 2. * pow(ln(z), 2) * z * pow(NQCD, -1) + (- 1. / 2. * pow(ln(z), 2) * z * NQCD) + (- 6 * pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -1)) + 4 * pow(ln(z), 2) * x * pow(z, -1) * NQCD + (- 2 * pow(ln(z), 2) * x * pow(NQCD, -1)) + (- 3 * pow(ln(z), 2) * x * z * pow(NQCD, -1)) + 3 * pow(ln(z), 2) * x * z * NQCD + 6 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 2 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * NQCD) + 2 * pow(ln(z), 2) * pow(x, 2) * pow(NQCD, -1) + (- 2 * pow(ln(z), 2) * pow(x, 2) * NQCD) + pow(ln(z), 2) * pow(x, 2) * z * pow(NQCD, -1) + (- pow(ln(z), 2) * pow(x, 2) * z * NQCD) + 5. / 8. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD + 9. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD + (- 3 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1)) + 21. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD +  + 5. / 8. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD + 3 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1) + 5. / 2. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * NQCD + 3 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 19. / 8. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD) + 45. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD + (- 15 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 105. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * NQCD + (- 35. / 8. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD) + 2 * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * NQCD + (- 4 * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD) + 4 * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD + 2 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(z, -1) * pow(NQCD, -1) + 2 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * NQCD + (- 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -1)) + (- 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * NQCD) + 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) +  + 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * NQCD + (- 2 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(z, -1) * pow(NQCD, -1)) + (- 2 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * NQCD) + 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -1) + 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * NQCD + (- 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + (- 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * NQCD) + (- 2 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD) + (- 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1)) + 2 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * NQCD + 2 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1) + (- 2 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD) + 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD + 8 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD) + (- 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) +  + 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + 2 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(z, -1) * NQCD + 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) + (- 2 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * NQCD) + (- 2 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * pow(NQCD, -1)) + 2 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * NQCD + (- 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(z, -1) * NQCD) + (- 8 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD + 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) + (- 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD) + 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(z, -1) * NQCD + 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) +  + (-4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD + (- 2 * Li2(-x * pow(z, -1)) * pow(NQCD, -1)) + 4 * Li2(-x * pow(z, -1)) * x * pow(z, -1) * NQCD + (- 4 * Li2(-x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 4 * Li2(-x * pow(z, -1)) * x * z * NQCD + (- 4 * Li2(-x * pow(z, -1)) * pow(x, 2) * NQCD) + (- 2 * Li2(-x) * pow(z, -1) * NQCD) + 2 * Li2(-x) * pow(NQCD, -1) + 2 * Li2(-x) * z * pow(NQCD, -1) + (- 2 * Li2(-x) * z * NQCD) + (- 4 * Li2(-x) * x * pow(z, -1) * NQCD) + 4 * Li2(-x) * x * pow(NQCD, -1) + 4 * Li2(-x) * x * z * pow(NQCD, -1) + (- 4 * Li2(-x) * x * z * NQCD) + (- 4 * Li2(-x) * pow(x, 2) * pow(z, -1) * NQCD) + 4 * Li2(-x) * pow(x, 2) * NQCD + 4 * Li2(-x) * pow(x, 2) * z * pow(NQCD, -1) + (- 4 * Li2(-x) * pow(x, 2) * z * NQCD) + 2 * Li2(-x * z) * pow(z, -1) * NQCD + (- 2 * Li2(-x * z) * z * pow(NQCD, -1)) + 2 * Li2(-x * z) * z * NQCD + (- 4 * Li2(-x * z) * x * pow(NQCD, -1)) + 4 * Li2(-x * z) * pow(x, 2) * pow(z, -1) * NQCD + (- 4 * Li2(-x * z) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * Li2(-x * z) * pow(x, 2) * z * NQCD + (- 1. / 2. * Li2(x) * pow(z, -1) * pow(NQCD, -1)) + 1. / 2. * Li2(x) * pow(z, -1) * NQCD + Li2(x) * pow(NQCD, -1) + (- Li2(x) * NQCD) + (- Li2(x) * z * pow(NQCD, -1)) + Li2(x) * z * NQCD + Li2(x) * x * pow(z, -1) * pow(NQCD, -1) + (- Li2(x) * x * pow(z, -1) * NQCD) + (- 2 * Li2(x) * x * pow(NQCD, -1)) + 2 * Li2(x) * x * NQCD + (- 2 * Li2(x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 2 * Li2(x) * pow(x, 2) * pow(z, -1) * NQCD + 2 * Li2(x) * pow(x, 2) * pow(NQCD, -1) + (- 2 * Li2(x) * pow(x, 2) * NQCD) + (- 2 * Li2(x) * pow(x, 2) * z * pow(NQCD, -1)) + 2 * Li2(x) * pow(x, 2) * z * NQCD +  + (-2 * Li2(z) * pow(NQCD, -1)) + 2 * Li2(z) * NQCD + 4 * Li2(z) * x * pow(NQCD, -1) + (- 4 * Li2(z) * x * NQCD) + (- 4 * Li2(z) * pow(x, 2) * pow(NQCD, -1)) + 4 * Li2(z) * pow(x, 2) * NQCD + (- 5. / 16. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD) + (- 9. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD) + 3. / 2. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1) + (- 21. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD) + (- 5. / 16. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD) + (- 3. / 2. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1)) + (- 5. / 4. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * NQCD) + (- 3. / 2. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1)) + 19. / 16. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD + (- 45. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD) + 15. / 2. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1) + (- 105. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * NQCD) + 35. / 16. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD + 5. / 16. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD + 9. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD + (- 3. / 2. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1)) +  + 21. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD + 5. / 16. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD + 3. / 2. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1) + 5. / 4. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * NQCD + 3. / 2. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 19. / 16. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD) + 45. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD + (- 15. / 2. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 105. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * NQCD + (- 35. / 16. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD) + (- 5. / 8. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD) + (- 9. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD) + 3 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1) + (- 21. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD) + (- 5. / 8. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD) + (- 3 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1)) + (- 5. / 2. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * NQCD) + (- 3 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1)) + 19. / 8. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD +  + (-45. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD) + 15 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1) + (- 105. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * NQCD) + 35. / 8. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD + 4 * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * NQCD * rln2 + (- 8 * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD * rln2) + 8 * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD * rln2 + (- 4 / (1 - z) * ln(x) * ln(1 + x) * pow(NQCD, -1)) + (- 8 / (1 - z) * ln(x) * ln(1 + x) * x * pow(NQCD, -1)) + (- 4 / (1 - z) * ln(x) * ln(1 + x) * pow(x, 2) * pow(NQCD, -1)) + 2 / (1 - z) * ln(x) * ln(1 + x * z) * pow(NQCD, -1) + 4 / (1 - z) * ln(x) * ln(1 + x * z) * x * pow(NQCD, -1) + 2 / (1 - z) * ln(x) * ln(1 + x * z) * pow(x, 2) * pow(NQCD, -1) + 2 / (1 - z) * ln(x) * ln(z + x) * pow(NQCD, -1) + 4 / (1 - z) * ln(x) * ln(z + x) * x * pow(NQCD, -1) + 2 / (1 - z) * ln(x) * ln(z + x) * pow(x, 2) * pow(NQCD, -1) + (- 2 / (1 - z) * ln(x) * ln(z) * pow(NQCD, -1)) + (- 4 / (1 - z) * ln(x) * ln(z) * x * pow(NQCD, -1)) + (- 2 / (1 - z) * ln(x) * ln(z) * pow(x, 2) * pow(NQCD, -1)) + 2 / (1 - z) * ln(z) * ln(1 + x * z) * pow(NQCD, -1) + 4 / (1 - z) * ln(z) * ln(1 + x * z) * x * pow(NQCD, -1) + 2 / (1 - z) * ln(z) * ln(1 + x * z) * pow(x, 2) * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * ln(z + x) * pow(NQCD, -1)) + (- 4 / (1 - z) * ln(z) * ln(z + x) * x * pow(NQCD, -1)) + (- 2 / (1 - z) * ln(z) * ln(z + x) * pow(x, 2) * pow(NQCD, -1)) + 2 / (1 - z) * pow(ln(z), 2) * pow(NQCD, -1) + 2 / (1 - z) * pow(ln(z), 2) * pow(x, 2) * pow(NQCD, -1) + 2 / (1 - z) * Li2(-x * pow(z, -1)) * pow(NQCD, -1) +  + 4 / (1 - z) * Li2(-x * pow(z, -1)) * x * pow(NQCD, -1) + 2 / (1 - z) * Li2(-x * pow(z, -1)) * pow(x, 2) * pow(NQCD, -1) + (- 4 / (1 - z) * Li2(-x) * pow(NQCD, -1)) + (- 8 / (1 - z) * Li2(-x) * x * pow(NQCD, -1)) + (- 4 / (1 - z) * Li2(-x) * pow(x, 2) * pow(NQCD, -1)) + 2 / (1 - z) * Li2(-x * z) * pow(NQCD, -1) + 4 / (1 - z) * Li2(-x * z) * x * pow(NQCD, -1) + 2 / (1 - z) * Li2(-x * z) * pow(x, 2) * pow(NQCD, -1) + (- 8 / (1 + z) * pow(NQCD, -1) * pow(rln2, 2)) + 16 / (1 + z) * x * pow(NQCD, -1) * pow(rln2, 2) + (- 8 / (1 + z) * pow(x, 2) * pow(NQCD, -1) * pow(rln2, 2)) + 8 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) * rln2 + (- 16 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) * rln2) + 8 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) * rln2 + (- 8 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1)) + 16 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 8 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 8 / (1 + z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) * rln2 + (- 16 / (1 + z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) * rln2) + 8 / (1 + z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) * rln2 + (- 4 / (1 + z) * ln(x) * pow(NQCD, -1) * rln2) + 8 / (1 + z) * ln(x) * x * pow(NQCD, -1) * rln2 +  + (-4 / (1 + z) * ln(x) * pow(x, 2) * pow(NQCD, -1) * rln2) + 4 / (1 + z) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) + (- 8 / (1 + z) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + 4 / (1 + z) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) + (- 2 / (1 + z) * ln(x) * ln(1 + x * z) * pow(NQCD, -1)) + 4 / (1 + z) * ln(x) * ln(1 + x * z) * x * pow(NQCD, -1) + (- 2 / (1 + z) * ln(x) * ln(1 + x * z) * pow(x, 2) * pow(NQCD, -1)) + 2 / (1 + z) * ln(x) * ln(z + x) * pow(NQCD, -1) + (- 4 / (1 + z) * ln(x) * ln(z + x) * x * pow(NQCD, -1)) + 2 / (1 + z) * ln(x) * ln(z + x) * pow(x, 2) * pow(NQCD, -1) + (- 2 / (1 + z) * ln(x) * ln(z) * pow(NQCD, -1)) + 4 / (1 + z) * ln(x) * ln(z) * x * pow(NQCD, -1) + (- 2 / (1 + z) * ln(x) * ln(z) * pow(x, 2) * pow(NQCD, -1)) + (- 12 / (1 + z) * ln(z) * pow(NQCD, -1) * rln2) + 24 / (1 + z) * ln(z) * x * pow(NQCD, -1) * rln2 + (- 12 / (1 + z) * ln(z) * pow(x, 2) * pow(NQCD, -1) * rln2) + 4 / (1 + z) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) + (- 8 / (1 + z) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + 4 / (1 + z) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) + 8 / (1 + z) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) + (- 16 / (1 + z) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + 8 / (1 + z) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) + (- 2 / (1 + z) * ln(z) * ln(1 + x * z) * pow(NQCD, -1)) + 4 / (1 + z) * ln(z) * ln(1 + x * z) * x * pow(NQCD, -1) +  + (-2 / (1 + z) * ln(z) * ln(1 + x * z) * pow(x, 2) * pow(NQCD, -1)) + (- 2 / (1 + z) * ln(z) * ln(z + x) * pow(NQCD, -1)) + 4 / (1 + z) * ln(z) * ln(z + x) * x * pow(NQCD, -1) + (- 2 / (1 + z) * ln(z) * ln(z + x) * pow(x, 2) * pow(NQCD, -1)) + (- 2 / (1 + z) * pow(ln(z), 2) * pow(NQCD, -1)) + 4 / (1 + z) * pow(ln(z), 2) * x * pow(NQCD, -1) + (- 2 / (1 + z) * pow(ln(z), 2) * pow(x, 2) * pow(NQCD, -1)) + (- 4 / (1 + z) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(NQCD, -1)) + 8 / (1 + z) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * pow(NQCD, -1) + (- 4 / (1 + z) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * pow(NQCD, -1)) + 4 / (1 + z) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(NQCD, -1) + (- 8 / (1 + z) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * pow(NQCD, -1)) + 4 / (1 + z) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * pow(NQCD, -1) + 4 / (1 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1) + (- 8 / (1 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + 4 / (1 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) + (- 4 / (1 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(NQCD, -1)) + 8 / (1 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) +  + (-4 / (1 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 2 / (1 + z) * Li2(-x * pow(z, -1)) * pow(NQCD, -1) + (- 4 / (1 + z) * Li2(-x * pow(z, -1)) * x * pow(NQCD, -1)) + 2 / (1 + z) * Li2(-x * pow(z, -1)) * pow(x, 2) * pow(NQCD, -1) + (- 2 / (1 + z) * Li2(-x * z) * pow(NQCD, -1)) + 4 / (1 + z) * Li2(-x * z) * x * pow(NQCD, -1) + (- 2 / (1 + z) * Li2(-x * z) * pow(x, 2) * pow(NQCD, -1));
        res += tmp;
    }

    return res;
}

double RG_RG_001(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_001(x0, z0, NF);
        double pt1 = RG_RG_001(x1, z1, NF);
        double pt2 = RG_RG_001(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_001(x0, z0, NF);
        double pt1 = RG_RG_001(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_001(x0, z0, NF);
        double pt1 = RG_RG_001(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = (- 11. / 2. * lmua * pow(z, -1) * pow(NQCD, -1)) + 11. / 2. * lmua * pow(z, -1) * NQCD + 5 * lmua * pow(NQCD, -1) + (- 5 * lmua * NQCD) + 1. / 2. * lmua * z * pow(NQCD, -1) + (- 1. / 2. * lmua * z * NQCD) + 15 * lmua * x * pow(z, -1) * pow(NQCD, -1) + (- 15 * lmua * x * pow(z, -1) * NQCD) + (- 14 * lmua * x * pow(NQCD, -1)) + 14 * lmua * x * NQCD + lmua * x * z * pow(NQCD, -1) + (- lmua * x * z * NQCD) + (- 15 * lmua * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 15 * lmua * pow(x, 2) * pow(z, -1) * NQCD + 14 * lmua * pow(x, 2) * pow(NQCD, -1) + (- 14 * lmua * pow(x, 2) * NQCD) + (- lmua * pow(x, 2) * z * pow(NQCD, -1)) + lmua * pow(x, 2) * z * NQCD + 2 * lmua * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 2 * lmua * ln(1 - z) * pow(z, -1) * NQCD) + (- 2 * lmua * ln(1 - z) * pow(NQCD, -1)) + 2 * lmua * ln(1 - z) * NQCD + lmua * ln(1 - z) * z * pow(NQCD, -1) + (- lmua * ln(1 - z) * z * NQCD) + (- 4 * lmua * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 4 * lmua * ln(1 - z) * x * pow(z, -1) * NQCD + 4 * lmua * ln(1 - z) * x * pow(NQCD, -1) + (- 4 * lmua * ln(1 - z) * x * NQCD) + (- 2 * lmua * ln(1 - z) * x * z * pow(NQCD, -1)) + 2 * lmua * ln(1 - z) * x * z * NQCD + 4 * lmua * ln(1 - z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 4 * lmua * ln(1 - z) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * lmua * ln(1 - z) * pow(x, 2) * pow(NQCD, -1)) + 4 * lmua * ln(1 - z) * pow(x, 2) * NQCD + 2 * lmua * ln(1 - z) * pow(x, 2) * z * pow(NQCD, -1) + (- 2 * lmua * ln(1 - z) * pow(x, 2) * z * NQCD) + 2 * lmua * ln(1 - x) * pow(z, -1) * pow(NQCD, -1) + (- 2 * lmua * ln(1 - x) * pow(z, -1) * NQCD) + (- 2 * lmua * ln(1 - x) * pow(NQCD, -1)) + 2 * lmua * ln(1 - x) * NQCD + lmua * ln(1 - x) * z * pow(NQCD, -1) + (- lmua * ln(1 - x) * z * NQCD) + (- 4 * lmua * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1)) + 4 * lmua * ln(1 - x) * x * pow(z, -1) * NQCD + 4 * lmua * ln(1 - x) * x * pow(NQCD, -1) + (- 4 * lmua * ln(1 - x) * x * NQCD) + (- 2 * lmua * ln(1 - x) * x * z * pow(NQCD, -1)) + 2 * lmua * ln(1 - x) * x * z * NQCD + 4 * lmua * ln(1 - x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 4 * lmua * ln(1 - x) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * lmua * ln(1 - x) * pow(x, 2) * pow(NQCD, -1)) + 4 * lmua * ln(1 - x) * pow(x, 2) * NQCD + 2 * lmua * ln(1 - x) * pow(x, 2) * z * pow(NQCD, -1) + (- 2 * lmua * ln(1 - x) * pow(x, 2) * z * NQCD) + (- 2 * ln(x) * lmua * pow(z, -1) * pow(NQCD, -1)) + 2 * ln(x) * lmua * pow(z, -1) * NQCD + 2 * ln(x) * lmua * pow(NQCD, -1) + (- 2 * ln(x) * lmua * NQCD) + (- ln(x) * lmua * z * pow(NQCD, -1)) + ln(x) * lmua * z * NQCD + 4 * ln(x) * lmua * x * pow(z, -1) * pow(NQCD, -1) + (- 4 * ln(x) * lmua * x * pow(z, -1) * NQCD) + (- 4 * ln(x) * lmua * x * pow(NQCD, -1)) + 4 * ln(x) * lmua * x * NQCD + 2 * ln(x) * lmua * x * z * pow(NQCD, -1) + (- 2 * ln(x) * lmua * x * z * NQCD) + (- 4 * ln(x) * lmua * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 4 * ln(x) * lmua * pow(x, 2) * pow(z, -1) * NQCD + 4 * ln(x) * lmua * pow(x, 2) * pow(NQCD, -1) + (- 4 * ln(x) * lmua * pow(x, 2) * NQCD) + (- 2 * ln(x) * lmua * pow(x, 2) * z * pow(NQCD, -1)) + 2 * ln(x) * lmua * pow(x, 2) * z * NQCD + (- 2 * ln(z) * lmua * pow(z, -1) * pow(NQCD, -1)) + 2 * ln(z) * lmua * pow(z, -1) * NQCD + (- 2 * ln(z) * lmua * pow(NQCD, -1)) + 2 * ln(z) * lmua * NQCD + (- ln(z) * lmua * z * pow(NQCD, -1)) + ln(z) * lmua * z * NQCD + 4 * ln(z) * lmua * x * pow(z, -1) * pow(NQCD, -1) + (- 4 * ln(z) * lmua * x * pow(z, -1) * NQCD) + 4 * ln(z) * lmua * x * pow(NQCD, -1) + (- 4 * ln(z) * lmua * x * NQCD) + 2 * ln(z) * lmua * x * z * pow(NQCD, -1) + (- 2 * ln(z) * lmua * x * z * NQCD) + (- 4 * ln(z) * lmua * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 4 * ln(z) * lmua * pow(x, 2) * pow(z, -1) * NQCD + (- 4 * ln(z) * lmua * pow(x, 2) * pow(NQCD, -1)) + 4 * ln(z) * lmua * pow(x, 2) * NQCD + (- 2 * ln(z) * lmua * pow(x, 2) * z * pow(NQCD, -1)) + 2 * ln(z) * lmua * pow(x, 2) * z * NQCD;
        res += tmp;
    }

    return res;
}

double RG_RG_010(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_010(x0, z0, NF);
        double pt1 = RG_RG_010(x1, z1, NF);
        double pt2 = RG_RG_010(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_010(x0, z0, NF);
        double pt1 = RG_RG_010(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_010(x0, z0, NF);
        double pt1 = RG_RG_010(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = (- 2 * lmuf * pow(z, -1) * pow(NQCD, -1)) + 2 * lmuf * pow(z, -1) * NQCD + 2 * lmuf * pow(NQCD, -1) + (- 2 * lmuf * NQCD) + (- 2 * lmuf * z * pow(NQCD, -1)) + 2 * lmuf * z * NQCD + 5 * lmuf * x * pow(z, -1) * pow(NQCD, -1) + (- 5 * lmuf * x * pow(z, -1) * NQCD) + (- 2 * lmuf * x * pow(NQCD, -1)) + 2 * lmuf * x * NQCD + (- 3 * lmuf * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 3 * lmuf * pow(x, 2) * pow(z, -1) * NQCD + 3 * lmuf * pow(x, 2) * z * pow(NQCD, -1) + (- 3 * lmuf * pow(x, 2) * z * NQCD) + 2 * lmuf * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 2 * lmuf * ln(1 - z) * pow(z, -1) * NQCD) + (- 2 * lmuf * ln(1 - z) * pow(NQCD, -1)) + 2 * lmuf * ln(1 - z) * NQCD + lmuf * ln(1 - z) * z * pow(NQCD, -1) + (- lmuf * ln(1 - z) * z * NQCD) + (- 4 * lmuf * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 4 * lmuf * ln(1 - z) * x * pow(z, -1) * NQCD + 4 * lmuf * ln(1 - z) * x * pow(NQCD, -1) + (- 4 * lmuf * ln(1 - z) * x * NQCD) + (- 2 * lmuf * ln(1 - z) * x * z * pow(NQCD, -1)) + 2 * lmuf * ln(1 - z) * x * z * NQCD + 4 * lmuf * ln(1 - z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 4 * lmuf * ln(1 - z) * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * lmuf * ln(1 - z) * pow(x, 2) * pow(NQCD, -1)) + 4 * lmuf * ln(1 - z) * pow(x, 2) * NQCD + 2 * lmuf * ln(1 - z) * pow(x, 2) * z * pow(NQCD, -1) + (- 2 * lmuf * ln(1 - z) * pow(x, 2) * z * NQCD) + 2 * lmuf * ln(1 - x) * pow(z, -1) * pow(NQCD, -1) + (- 2 * lmuf * ln(1 - x) * pow(z, -1) * NQCD) + (- 2 * lmuf * ln(1 - x) * pow(NQCD, -1)) + 2 * lmuf * ln(1 - x) * NQCD + lmuf * ln(1 - x) * z * pow(NQCD, -1) + (- lmuf * ln(1 - x) * z * NQCD) + (- 4 * lmuf * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1)) + 4 * lmuf * ln(1 - x) * x * pow(z, -1) * NQCD + 4 * lmuf * ln(1 - x) * x * pow(NQCD, -1) + (- 4 * lmuf * ln(1 - x) * x * NQCD) + (- 2 * lmuf * ln(1 - x) * x * z * pow(NQCD, -1)) + 2 * lmuf * ln(1 - x) * x * z * NQCD + 4 * lmuf * ln(1 - x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 4 * lmuf * ln(1 - x) * pow(x, 2) * pow(z, -1) * NQCD) + (-4 * lmuf * ln(1 - x) * pow(x, 2) * pow(NQCD, -1)) + 4 * lmuf * ln(1 - x) * pow(x, 2) * NQCD + 2 * lmuf * ln(1 - x) * pow(x, 2) * z * pow(NQCD, -1) + (- 2 * lmuf * ln(1 - x) * pow(x, 2) * z * NQCD) + (- ln(x) * lmuf * pow(z, -1) * pow(NQCD, -1)) + ln(x) * lmuf * pow(z, -1) * NQCD + (-ln(x) * lmuf * z * pow(NQCD, -1)) + ln(x) * lmuf * z * NQCD + 2 * ln(x) * lmuf * x * pow(z, -1) * pow(NQCD, -1) + (- 2 * ln(x) * lmuf * x * pow(z, -1) * NQCD) + (- 2 * ln(x) * lmuf * x * z * pow(NQCD, -1)) + 2 * ln(x) * lmuf * x * z * NQCD + (- 4 * ln(x) * lmuf * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 4 * ln(x) * lmuf * pow(x, 2) * pow(z, -1) * NQCD + 4 * ln(x) * lmuf * pow(x, 2) * pow(NQCD, -1) + (- 4 * ln(x) * lmuf * pow(x, 2) * NQCD) + (- 2 * ln(x) * lmuf * pow(x, 2) * z * pow(NQCD, -1)) + 2 * ln(x) * lmuf * pow(x, 2) * z * NQCD + 2 * ln(z) * lmuf * pow(z, -1) * pow(NQCD, -1) + (- 2 * ln(z) * lmuf * pow(z, -1) * NQCD) + (- 2 * ln(z) * lmuf * pow(NQCD, -1)) + 2 * ln(z) * lmuf * NQCD + ln(z) * lmuf * z * pow(NQCD, -1) + (- ln(z) * lmuf * z * NQCD) + (- 4 * ln(z) * lmuf * x * pow(z, -1) * pow(NQCD, -1)) + 4 * ln(z) * lmuf * x * pow(z, -1) * NQCD + 4 * ln(z) * lmuf * x * pow(NQCD, -1) + (- 4 * ln(z) * lmuf * x * NQCD) + (- 2 * ln(z) * lmuf * x * z * pow(NQCD, -1)) + 2 * ln(z) * lmuf * x * z * NQCD + 4 * ln(z) * lmuf * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 4 * ln(z) * lmuf * pow(x, 2) * pow(z, -1) * NQCD) + (- 4 * ln(z) * lmuf * pow(x, 2) * pow(NQCD, -1)) + 4 * ln(z) * lmuf * pow(x, 2) * NQCD + 2 * ln(z) * lmuf * pow(x, 2) * z * pow(NQCD, -1) + (- 2 * ln(z) * lmuf * pow(x, 2) * z * NQCD);
        res += tmp;
    }

    return res;
}

double RG_RG_011(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_011(x0, z0, NF);
        double pt1 = RG_RG_011(x1, z1, NF);
        double pt2 = RG_RG_011(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_011(x0, z0, NF);
        double pt1 = RG_RG_011(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_011(x0, z0, NF);
        double pt1 = RG_RG_011(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = (- 4 * lmuf * lmua * pow(z, -1) * pow(NQCD, -1)) + 4 * lmuf * lmua * pow(z, -1) * NQCD + 4 * lmuf * lmua * pow(NQCD, -1) + (- 4 * lmuf * lmua * NQCD) + (- 2 * lmuf * lmua * z * pow(NQCD, -1)) + 2 * lmuf * lmua * z * NQCD + 8 * lmuf * lmua * x * pow(z, -1) * pow(NQCD, -1) + (- 8 * lmuf * lmua * x * pow(z, -1) * NQCD) + (- 8 * lmuf * lmua * x * pow(NQCD, -1)) + 8 * lmuf * lmua * x * NQCD + 4 * lmuf * lmua * x * z * pow(NQCD, -1) + (- 4 * lmuf * lmua * x * z * NQCD) + (- 8 * lmuf * lmua * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 8 * lmuf * lmua * pow(x, 2) * pow(z, -1) * NQCD + 8 * lmuf * lmua * pow(x, 2) * pow(NQCD, -1) + (- 8 * lmuf * lmua * pow(x, 2) * NQCD) + (- 4 * lmuf * lmua * pow(x, 2) * z * pow(NQCD, -1)) + 4 * lmuf * lmua * pow(x, 2) * z * NQCD;
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - RG_RG: 000, 001, 010, 011
*/
