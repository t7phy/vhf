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
        tmp = (-10. / 9. * pow(x, -1) * pow(NQCD, -1)) + 10. / 9. * pow(x, -1) * NQCD + 25. / 3. * pow(NQCD, -1) + (- 25. / 3. * NQCD) + (- 10 * z * pow(NQCD, -1)) + 10 * z * NQCD + (- 7. / 3. * x * pow(NQCD, -1)) + 7. / 3. * x * NQCD + 10 * x * z * pow(NQCD, -1) + (- 10 * x * z * NQCD) + (- 44. / 9. * pow(x, 2) * pow(NQCD, -1)) + 44. / 9. * pow(x, 2) * NQCD + 1. / 3. * pow(pi, 2) * x * pow(NQCD, -1) + (- 1. / 3. * pow(pi, 2) * x * NQCD) + (- 2. / 3. * ln(1 - z) * pow(x, -1) * pow(NQCD, -1)) + 2. / 3. * ln(1 - z) * pow(x, -1) * NQCD + 2 * ln(1 - z) * pow(NQCD, -1) + (- 2 * ln(1 - z) * NQCD) + (- 4. / 3. * ln(1 - z) * pow(x, 2) * pow(NQCD, -1)) + 4. / 3. * ln(1 - z) * pow(x, 2) * NQCD + (- 2. / 3. * ln(1 - x) * pow(x, -1) * pow(NQCD, -1)) + 2. / 3. * ln(1 - x) * pow(x, -1) * NQCD + 2 * ln(1 - x) * pow(NQCD, -1) + (- 2 * ln(1 - x) * NQCD) + (- 4. / 3. * ln(1 - x) * pow(x, 2) * pow(NQCD, -1)) + 4. / 3. * ln(1 - x) * pow(x, 2) * NQCD + (- 4 * ln(x) * pow(z, 2) * pow(NQCD, -1)) + 4 * ln(x) * pow(z, 2) * NQCD + 9 * ln(x) * x * pow(NQCD, -1) + (- 9 * ln(x) * x * NQCD) + (- 6 * ln(x) * x * z * pow(NQCD, -1)) + 6 * ln(x) * x * z * NQCD + 4 * ln(x) * pow(x, 2) * pow(NQCD, -1) + (- 4 * ln(x) * pow(x, 2) * NQCD) + 2 * ln(x) * ln(1 - z) * x * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - z) * x * NQCD) + 2 * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD) +  + (-4 * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * pow(NQCD, -1)) + 4 * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * NQCD + (- 2 * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1)) + 2 * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD + 4 * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * NQCD) + (- 2 * pow(ln(x), 2) * x * pow(NQCD, -1)) + 2 * pow(ln(x), 2) * x * NQCD + ln(x) * ln(z) * x * pow(NQCD, -1) + (- ln(x) * ln(z) * x * NQCD) + (- 2. / 3. * ln(z) * pow(x, -1) * pow(NQCD, -1)) + 2. / 3. * ln(z) * pow(x, -1) * NQCD + 3 * ln(z) * pow(NQCD, -1) + (- 3 * ln(z) * NQCD) + (- 8 * ln(z) * z * pow(NQCD, -1)) + 8 * ln(z) * z * NQCD + 4 * ln(z) * pow(z, 2) * pow(NQCD, -1) + (- 4 * ln(z) * pow(z, 2) * NQCD) + (- ln(z) * x * pow(NQCD, -1)) + ln(z) * x * NQCD + 6 * ln(z) * x * z * pow(NQCD, -1) + (- 6 * ln(z) * x * z * NQCD) + (- 4. / 3. * ln(z) * pow(x, 2) * pow(NQCD, -1)) + 4. / 3. * ln(z) * pow(x, 2) * NQCD + 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1) + (- 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD) +  + (-4 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * pow(NQCD, -1)) + 4 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * NQCD + (- 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1)) + 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD + 4 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * pow(NQCD, -1) + (- 4 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * NQCD) + (- 2 * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1)) + 2 * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD + 4 * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * pow(NQCD, -1) + (- 4 * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * NQCD) + 2 * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1) + (- 2 * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD) +  + (-4 * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * pow(NQCD, -1)) + 4 * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * z * NQCD + (- 2 * Li2(x) * x * pow(NQCD, -1)) + 2 * Li2(x) * x * NQCD + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * z * NQCD + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * NQCD) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * z * pow(NQCD, -1)) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * z * NQCD + 28 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * pow(NQCD, -1) + (- 28 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * NQCD) + (- 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 3) * pow(NQCD, -1)) + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 3) * NQCD + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * z * NQCD) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * pow(z, 2) * NQCD + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * z * NQCD) + (- 20 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * pow(NQCD, -1)) + 20 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * NQCD + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 3) * pow(NQCD, -1) + (- 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 3) * NQCD) +  + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1)) + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD +  + 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1) + (- 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD) + (- 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * pow(NQCD, -1)) + 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * NQCD + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD +  + (-4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD) + (- 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1)) + 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD + 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * pow(NQCD, -1) + (- 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * NQCD) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * NQCD) +  + (-12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1)) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * pow(NQCD, -1) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * NQCD) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * pow(NQCD, -1)) + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * NQCD + 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * pow(NQCD, -1) +  + (-64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * NQCD) + (- 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 4) * pow(NQCD, -1)) + 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 4) * NQCD + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * NQCD + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * NQCD +  + (-4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * pow(NQCD, -1) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * NQCD) + (- 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * pow(NQCD, -1)) + 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * NQCD + 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 4) * pow(NQCD, -1) + (- 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 4) * NQCD) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1)) +  + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD) + (- 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1)) +  + 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD + 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * pow(NQCD, -1) + (- 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * NQCD) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) +  + (-4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1)) + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD + 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1) + (- 64 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD) + (- 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * pow(NQCD, -1)) + 32 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * NQCD + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * NQCD + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) +  + (-12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * NQCD) + (- 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD +  + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * NQCD + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD) +  + (-8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * NQCD + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * NQCD) + (- 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1)) +  + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * NQCD) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * NQCD) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * NQCD) +  + (-12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * NQCD +  + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) + (- 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * NQCD + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD;
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
        tmp = 4. / 3. * lmuf * pow(x, -1) * pow(NQCD, -1) + (- 4. / 3. * lmuf * pow(x, -1) * NQCD) + (- 4 * lmuf * pow(NQCD, -1)) + 4 * lmuf * NQCD + 8. / 3. * lmuf * pow(x, 2) * pow(NQCD, -1) + (- 8. / 3. * lmuf * pow(x, 2) * NQCD) + (- 4 * ln(x) * lmuf * x * pow(NQCD, -1)) + 4 * ln(x) * lmuf * x * NQCD;
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - RG_RG: 000, 010
*/
