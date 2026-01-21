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
        tmp = 3. / 4. * pow(x, -1) * pow(z, -1) * NQCD + (- 3. / 4. * pow(x, -1) * NQCD) + 3. / 4. * pow(z, -2) * NQCD + (- 7. / 2. * pow(z, -1) * NQCD) + 4 * pow(NQCD, -1) + (- 5. / 2. * NQCD) + (- 4 * z * pow(NQCD, -1)) + 21. / 4. * z * NQCD + (- 3. / 4. * x * pow(z, -2) * NQCD) + (- 16 * x * pow(z, -1) * pow(NQCD, -1)) + (- 25. / 2. * x * pow(z, -1) * NQCD) + 28 * x * pow(NQCD, -1) + (- 16 * x * pow(NQCD, -1) * pow(rln2, 2)) + 5. / 2. * x * NQCD + (- 12 * x * z * pow(NQCD, -1)) + 16 * x * z * pow(NQCD, -1) * pow(rln2, 2) + 43. / 4. * x * z * NQCD + (- 16 * x * z * NQCD * pow(rln2, 2)) + 16 * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + 61. / 4. * pow(x, 2) * pow(z, -1) * NQCD + (- 32 * pow(x, 2) * pow(NQCD, -1)) + 16 * pow(x, 2) * pow(NQCD, -1) * pow(rln2, 2) + 3. / 4. * pow(x, 2) * NQCD + 16 * pow(x, 2) * z * pow(NQCD, -1) + (- 16 * pow(x, 2) * z * pow(NQCD, -1) * pow(rln2, 2)) + (- 16 * pow(x, 2) * z * NQCD) + 16 * pow(x, 2) * z * NQCD * pow(rln2, 2) + (- 2. / 3. * pow(pi, 2) * x * pow(NQCD, -1)) + 2. / 3. * pow(pi, 2) * x * NQCD + (- 2. / 3. * pow(pi, 2) * x * z * pow(NQCD, -1)) + 2. / 3. * pow(pi, 2) * x * z * NQCD + 4. / 3. * pow(pi, 2) * pow(x, 2) * z * pow(NQCD, -1) + (- 4. / 3. * pow(pi, 2) * pow(x, 2) * z * NQCD) + (- 2 * ln(1 - z) * pow(NQCD, -1)) + 2 * ln(1 - z) * NQCD + 2 * ln(1 - z) * z * pow(NQCD, -1) + (- 2 * ln(1 - z) * z * NQCD) + (- 8 * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 8 * ln(1 - z) * x * pow(z, -1) * NQCD + 2 * ln(1 - z) * x * pow(NQCD, -1) + (- 2 * ln(1 - z) * x * NQCD) + 6 * ln(1 - z) * x * z * pow(NQCD, -1) + (- 6 * ln(1 - z) * x * z * NQCD) + 8 * ln(1 - z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 8 * ln(1 - z) * pow(x, 2) * pow(z, -1) * NQCD) + (- 8 * ln(1 - z) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * ln(1 - z) * pow(x, 2) * z * NQCD + 24 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) * rln2 +  + (-8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD * rln2) + (- 24 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) * rln2) + 24 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD * rln2 + (- 24 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) * rln2) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD * rln2 + 24 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) * rln2 + (- 24 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD * rln2) + (- 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * pow(NQCD, -1)) + 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * NQCD + 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * z * pow(NQCD, -1) + (- 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * z * NQCD) + 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * pow(NQCD, -1) + (- 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * NQCD) + (- 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * pow(x, 2) * z * NQCD + (- 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + (- 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) +  + (-8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD + (- 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD + 16 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD + (- 16 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD) + 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) * rln2 + 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD * rln2 + (- 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) * rln2) + 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD * rln2 + (- 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) * rln2) + (- 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD * rln2) + 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) * rln2 + (- 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD * rln2) + (- 2 * ln(1 - x) * pow(NQCD, -1)) +  + 2 * ln(1 - x) * NQCD + 2 * ln(1 - x) * z * pow(NQCD, -1) + (- 2 * ln(1 - x) * z * NQCD) + (- 8 * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1)) + 8 * ln(1 - x) * x * pow(z, -1) * NQCD + 2 * ln(1 - x) * x * pow(NQCD, -1) + (- 2 * ln(1 - x) * x * NQCD) + 6 * ln(1 - x) * x * z * pow(NQCD, -1) + (- 6 * ln(1 - x) * x * z * NQCD) + 8 * ln(1 - x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 8 * ln(1 - x) * pow(x, 2) * pow(z, -1) * NQCD) + (- 8 * ln(1 - x) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * ln(1 - x) * pow(x, 2) * z * NQCD + 3. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD +  + (-1. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD) + (- 2 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1)) + 7. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD + 3. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD + 2 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1) + 7 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * NQCD + (- 6 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1)) + 19. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD + 15. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD + 30 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1) + (- 105. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * NQCD) + 35. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD + (- 3. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD) + 1. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD + 2 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1) +  + (-7. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD) + (- 3. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD) + (- 2 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1)) + (- 7 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * NQCD) + 6 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 19. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD) + (- 15. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD) + (- 30 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 105. / 2. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * NQCD + (- 35. / 4. * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD) + (- 3. / 8. * ln(x) * pow(x, -1) * pow(z, -1) * NQCD) + 3. / 8. * ln(x) * pow(x, -1) * NQCD + 3. / 8. * ln(x) * pow(z, -2) * NQCD + (- 1. / 4. * ln(x) * pow(z, -1) * NQCD) + 3 * ln(x) * pow(NQCD, -1) + (- 15. / 4. * ln(x) * NQCD) + (- 3 * ln(x) * z * pow(NQCD, -1)) + 29. / 8. * ln(x) * z * NQCD + 3. / 8. * ln(x) * x * pow(z, -2) * NQCD + 8 * ln(x) * x * pow(z, -1) * pow(NQCD, -1) + (- 49. / 4. * ln(x) * x * pow(z, -1) * NQCD) + 5 * ln(x) * x * pow(NQCD, -1) + (- 16 * ln(x) * x * pow(NQCD, -1) * rln2) + (- 7. / 4. * ln(x) * x * NQCD) + 8 * ln(x) * x * NQCD * rln2 + (- 13 * ln(x) * x * z * pow(NQCD, -1)) +  + 16 * ln(x) * x * z * pow(NQCD, -1) * rln2 + 109. / 8. * ln(x) * x * z * NQCD + (- 16 * ln(x) * x * z * NQCD * rln2) + (- 8 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 29. / 8. * ln(x) * pow(x, 2) * pow(z, -1) * NQCD + 16 * ln(x) * pow(x, 2) * pow(NQCD, -1) * rln2 + 35. / 8. * ln(x) * pow(x, 2) * NQCD + (- 8 * ln(x) * pow(x, 2) * NQCD * rln2) + 8 * ln(x) * pow(x, 2) * z * pow(NQCD, -1) + (- 16 * ln(x) * pow(x, 2) * z * pow(NQCD, -1) * rln2) + (- 8 * ln(x) * pow(x, 2) * z * NQCD) + 16 * ln(x) * pow(x, 2) * z * NQCD * rln2 + (- 4 * ln(x) * ln(1 - z) * x * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - z) * x * NQCD + 4 * ln(x) * ln(1 - z) * x * z * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 - z) * x * z * NQCD) + 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD) + (- 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD + 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + 8 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 8 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 8 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 8 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) +  + 8 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + (- 4 * ln(x) * ln(1 - x) * x * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - x) * x * NQCD + 4 * ln(x) * ln(1 - x) * x * z * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 - x) * x * z * NQCD) + 4 * ln(x) * ln(1 - x) * pow(x, 2) * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 - x) * pow(x, 2) * NQCD) + (- 4 * ln(x) * ln(1 - x) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * ln(x) * ln(1 - x) * pow(x, 2) * z * NQCD + 8 * ln(x) * ln(1 + x) * x * NQCD + 8 * ln(x) * ln(1 + x) * x * z * pow(NQCD, -1) + (- 8 * ln(x) * ln(1 + x) * x * z * NQCD) + 8 * ln(x) * ln(1 + x) * pow(x, 2) * NQCD + 8 * ln(x) * ln(1 + x) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * ln(x) * ln(1 + x) * pow(x, 2) * z * NQCD) + (- 8 * ln(x) * ln(1 + x * z) * x * NQCD) + (- 8 * ln(x) * ln(1 + x * z) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * ln(x) * ln(1 + x * z) * pow(x, 2) * z * NQCD + (- 8 * ln(x) * ln(z + x) * x * z * pow(NQCD, -1)) + 8 * ln(x) * ln(z + x) * x * z * NQCD + (- 8 * ln(x) * ln(z + x) * pow(x, 2) * NQCD) + 2 * pow(ln(x), 2) * x * pow(NQCD, -1) + (- 2 * pow(ln(x), 2) * x * NQCD) + (- 2 * pow(ln(x), 2) * x * z * pow(NQCD, -1)) + 2 * pow(ln(x), 2) * x * z * NQCD + 2 * pow(ln(x), 2) * pow(x, 2) * pow(NQCD, -1) + (- 2 * pow(ln(x), 2) * pow(x, 2) * NQCD) + (- 2 * pow(ln(x), 2) * pow(x, 2) * z * pow(NQCD, -1)) + 2 * pow(ln(x), 2) * pow(x, 2) * z * NQCD + 4 * ln(x) * ln(z) * x * pow(NQCD, -1) + (- 12 * ln(x) * ln(z) * x * NQCD) + 12 * ln(x) * ln(z) * x * z * pow(NQCD, -1) + (- 12 * ln(x) * ln(z) * x * z * NQCD) +  + 8 * ln(x) * ln(z) * pow(x, 2) * NQCD + (- 8 * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD) + 8 * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD + 3. / 8. * ln(z) * pow(x, -1) * pow(z, -1) * NQCD + 3. / 8. * ln(z) * pow(x, -1) * NQCD + (- 3. / 8. * ln(z) * pow(z, -2) * NQCD) + (- 1. / 4. * ln(z) * pow(z, -1) * NQCD) + ln(z) * pow(NQCD, -1) + (- 17. / 4. * ln(z) * NQCD) + ln(z) * z * pow(NQCD, -1) + (- 3. / 8. * ln(z) * z * NQCD) + 3. / 8. * ln(z) * x * pow(z, -2) * NQCD + (- 16 * ln(z) * x * pow(z, -1) * pow(NQCD, -1)) + 49. / 4. * ln(z) * x * pow(z, -1) * NQCD + (- 9 * ln(z) * x * pow(NQCD, -1)) + (- 16 * ln(z) * x * pow(NQCD, -1) * rln2) + 1. / 4. * ln(z) * x * NQCD + (- 8 * ln(z) * x * NQCD * rln2) + (- ln(z) * x * z * pow(NQCD, -1)) + 16 * ln(z) * x * z * pow(NQCD, -1) * rln2 + 3. / 8. * ln(z) * x * z * NQCD + (- 16 * ln(z) * x * z * NQCD * rln2) + 16 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NQCD, -1) + (- 99. / 8. * ln(z) * pow(x, 2) * pow(z, -1) * NQCD) + 8 * ln(z) * pow(x, 2) * pow(NQCD, -1) + 16 * ln(z) * pow(x, 2) * pow(NQCD, -1) * rln2 + 29. / 8. * ln(z) * pow(x, 2) * NQCD + 8 * ln(z) * pow(x, 2) * NQCD * rln2 + (- 16 * ln(z) * pow(x, 2) * z * pow(NQCD, -1) * rln2) + 16 * ln(z) * pow(x, 2) * z * NQCD * rln2 + 8 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 8 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 8 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 8 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 8 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) +  + 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * NQCD + (- 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + (- 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * NQCD) + 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + (- 8 * ln(z) * ln(1 - x) * x * pow(NQCD, -1)) + 8 * ln(z) * ln(1 - x) * x * NQCD + 8 * ln(z) * ln(1 - x) * pow(x, 2) * pow(NQCD, -1) + (- 8 * ln(z) * ln(1 - x) * pow(x, 2) * NQCD) + (- 8 * ln(z) * ln(1 + x * z) * x * NQCD) + (- 8 * ln(z) * ln(1 + x * z) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * ln(z) * ln(1 + x * z) * pow(x, 2) * z * NQCD + 8 * ln(z) * ln(z + x) * x * z * pow(NQCD, -1) + (- 8 * ln(z) * ln(z + x) * x * z * NQCD) + 8 * ln(z) * ln(z + x) * pow(x, 2) * NQCD + (- 8 * pow(ln(z), 2) * x * pow(NQCD, -1)) + 4 * pow(ln(z), 2) * x * NQCD + (- 4 * pow(ln(z), 2) * x * z * pow(NQCD, -1)) + 4 * pow(ln(z), 2) * x * z * NQCD + 8 * pow(ln(z), 2) * pow(x, 2) * pow(NQCD, -1) + (- 8 * pow(ln(z), 2) * pow(x, 2) * NQCD) + (- 3. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD) +  + 1. / 2. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD + 2 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1) + (- 7. / 2. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD) + (- 3. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD) + (- 2 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1)) + (- 7 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * NQCD) + 6 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 19. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD) + (- 15. / 2. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD) + (- 30 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 105. / 2. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * NQCD + (- 35. / 4. * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD) + (- 8 * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD) + 8 * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD + (- 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * NQCD) + 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * NQCD + 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * NQCD + (- 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * pow(x, 2) * NQCD) +  + 8 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1) + (- 8 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1)) + 8 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD + (- 8 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1)) + 8 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD) + (- 8 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, -1)) + 8 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, -1) + (- 8 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * NQCD) + 8 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * pow(NQCD, -1) + (- 8 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * pow(x, 2) * z * NQCD + (- 8 * Li2(-x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 8 * Li2(-x * pow(z, -1)) * x * z * NQCD + (- 8 * Li2(-x * pow(z, -1)) * pow(x, 2) * NQCD) + 8 * Li2(-x) * x * NQCD + 8 * Li2(-x) * x * z * pow(NQCD, -1) + (- 8 * Li2(-x) * x * z * NQCD) + 8 * Li2(-x) * pow(x, 2) * NQCD + 8 * Li2(-x) * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * Li2(-x) * pow(x, 2) * z * NQCD) + (- 8 * Li2(-x * z) * x * NQCD) + (- 8 * Li2(-x * z) * pow(x, 2) * z * pow(NQCD, -1)) + 8 * Li2(-x * z) * pow(x, 2) * z * NQCD +  + 4 * Li2(x) * pow(x, 2) * pow(NQCD, -1) + (- 4 * Li2(x) * pow(x, 2) * NQCD) + (- 4 * Li2(x) * pow(x, 2) * z * pow(NQCD, -1)) + 4 * Li2(x) * pow(x, 2) * z * NQCD + 8 * Li2(z) * x * pow(NQCD, -1) + (- 8 * Li2(z) * x * NQCD) + (- 8 * Li2(z) * pow(x, 2) * pow(NQCD, -1)) + 8 * Li2(z) * pow(x, 2) * NQCD + 3. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD + (- 1. / 4. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD) + (- InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1)) + 7. / 4. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD + 3. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD + InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1) + 7. / 2. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * NQCD + (- 3 * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1)) + 19. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD + 15. / 4. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD + 15 * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1) + (- 105. / 4. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * NQCD) + 35. / 8. * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD + (- 3. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD) + 1. / 4. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD +  + InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1) + (- 7. / 4. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD) + (- 3. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD) + (- InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1)) + (- 7. / 2. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * NQCD) + 3 * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 19. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD) + (- 15. / 4. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD) + (- 15 * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1)) + 105. / 4. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * x * z * NQCD + (- 35. / 8. * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD) + 3. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -2) * NQCD + (- 1. / 2. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NQCD) + (- 2 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * pow(NQCD, -1)) + 7. / 2. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, -1) * z * NQCD + 3. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, -2) * NQCD + 2 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(NQCD, -1) + 7 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * NQCD + (- 6 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * pow(NQCD, -1)) +  + 19. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(z, 2) * NQCD + 15. / 2. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * pow(z, -1) * NQCD + 30 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * pow(NQCD, -1) + (- 105. / 2. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * x * z * NQCD) + 35. / 4. * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * pow(x, 2) * NQCD + (- 16 * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * NQCD * rln2) + 16 * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * NQCD * rln2;
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
        tmp = 16 * lmua * x * pow(z, -1) * pow(NQCD, -1) + (- 16 * lmua * x * pow(z, -1) * NQCD) + (- 8 * lmua * x * pow(NQCD, -1)) + 8 * lmua * x * NQCD + (- 8 * lmua * x * z * pow(NQCD, -1)) + 8 * lmua * x * z * NQCD + (- 16 * lmua * pow(x, 2) * pow(z, -1) * pow(NQCD, -1)) + 16 * lmua * pow(x, 2) * pow(z, -1) * NQCD + 8 * lmua * pow(x, 2) * pow(NQCD, -1) + (- 8 * lmua * pow(x, 2) * NQCD) + 8 * lmua * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * lmua * pow(x, 2) * z * NQCD) + 16 * ln(z) * lmua * x * pow(NQCD, -1) + (- 16 * ln(z) * lmua * x * NQCD) + (- 16 * ln(z) * lmua * pow(x, 2) * pow(NQCD, -1)) + 16 * ln(z) * lmua * pow(x, 2) * NQCD;
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
        tmp = 4 * lmuf * pow(NQCD, -1) + (- 4 * lmuf * NQCD) + (- 4 * lmuf * z * pow(NQCD, -1)) + 4 * lmuf * z * NQCD + 4 * lmuf * x * pow(NQCD, -1) + (- 4 * lmuf * x * NQCD) + (- 4 * lmuf * x * z * pow(NQCD, -1)) + 4 * lmuf * x * z * NQCD + (- 8 * lmuf * pow(x, 2) * pow(NQCD, -1)) + 8 * lmuf * pow(x, 2) * NQCD + 8 * lmuf * pow(x, 2) * z * pow(NQCD, -1) + (- 8 * lmuf * pow(x, 2) * z * NQCD) + 8 * ln(x) * lmuf * x * pow(NQCD, -1) + (- 8 * ln(x) * lmuf * x * NQCD) + (- 8 * ln(x) * lmuf * x * z * pow(NQCD, -1)) + 8 * ln(x) * lmuf * x * z * NQCD;
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - RG_RG: 000, 001, 010
*/

/*
  Inverted Branch Report (By Number):
  - 000: RG_RG
  - 001: RG_RG
  - 010: RG_RG
*/
