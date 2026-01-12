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
        tmp = 4 * pow(z, -1) * CF * pow(NQCD, -1) + (- 8 * CF * pow(NQCD, -1)) + 2 * z * CF * pow(NQCD, -1) + (- 7. / 2. * x * pow(z, -1) * CF * pow(NQCD, -1)) + 7 * x * CF * pow(NQCD, -1) + (- 3. / 2. * x * z * CF * pow(NQCD, -1)) + (- 1. / 6. * pow(pi, 2) * pow(z, -1) * CF * pow(NQCD, -1)) + 1. / 3. * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 3. * pow(pi, 2) * z * CF * pow(NQCD, -1)) + (- 1. / 6. * pow(pi, 2) * x * pow(z, -1) * CF * pow(NQCD, -1)) + 1. / 3. * pow(pi, 2) * x * CF * pow(NQCD, -1) + ln(x) * pow(z, -1) * CF * pow(NQCD, -1) + (- 2 * ln(x) * CF * pow(NQCD, -1)) + ln(x) * x * pow(z, -1) * CF * pow(NQCD, -1) + (- 2 * ln(x) * x * CF * pow(NQCD, -1)) + ln(x) * ln(1 - x) * pow(z, -1) * CF * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - x) * CF * pow(NQCD, -1)) + 2 * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) + ln(x) * ln(1 - x) * x * pow(z, -1) * CF * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1)) + (- 1. / 2. * pow(ln(x), 2) * pow(z, -1) * CF * pow(NQCD, -1)) + pow(ln(x), 2) * CF * pow(NQCD, -1) + (- pow(ln(x), 2) * z * CF * pow(NQCD, -1)) + (- 1. / 2. * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NQCD, -1)) + pow(ln(x), 2) * x * CF * pow(NQCD, -1) + Li2(x) * pow(z, -1) * CF * pow(NQCD, -1) + (- 2 * Li2(x) * CF * pow(NQCD, -1)) + 2 * Li2(x) * z * CF * pow(NQCD, -1) + Li2(x) * x * pow(z, -1) * CF * pow(NQCD, -1) + (- 2 * Li2(x) * x * CF * pow(NQCD, -1)) + 1. / 3. / (1 - x) * pow(pi, 2) * pow(z, -1) * CF * pow(NQCD, -1) + (- 2. / 3. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 3. / (1 - x) * pow(pi, 2) * z * CF * pow(NQCD, -1) + 3. / 2. / (1 - x) * ln(x) * pow(z, -1) * CF * pow(NQCD, -1) + (- 3 / (1 - x) * ln(x) * CF * pow(NQCD, -1)) + 3. / 2. / (1 - x) * ln(x) * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(x) * ln(1 - x) * pow(z, -1) * CF * pow(NQCD, -1)) + 4 / (1 - x) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) +  + (-2 / (1 - x) * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1)) + 1 / (1 - x) * pow(ln(x), 2) * pow(z, -1) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1)) + 1 / (1 - x) * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * Li2(x) * pow(z, -1) * CF * pow(NQCD, -1)) + 4 / (1 - x) * Li2(x) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * Li2(x) * z * CF * pow(NQCD, -1));
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - RG_RG: 000
*/
