#include "../sidis.h"



/* Helpers */

double DL_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-1. / 2. * z * pow(NQCD, -1)) + 1. / 2. * z * NQCD + (- ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + ln(1 - z) * pow(z, -1) * NQCD + ln(1 - z) * pow(NQCD, -1) + (- ln(1 - z) * NQCD) + (- 1. / 2. * ln(1 - z) * z * pow(NQCD, -1)) + 1. / 2. * ln(1 - z) * z * NQCD + (- ln(z) * pow(z, -1) * pow(NQCD, -1)) + ln(z) * pow(z, -1) * NQCD + ln(z) * pow(NQCD, -1) + (- ln(z) * NQCD) + (- 1. / 2. * ln(z) * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * z * NQCD;
    return res;
}

double DL_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = 2 * lmua * pow(z, -1) * pow(NQCD, -1) + (- 2 * lmua * pow(z, -1) * NQCD) + (- 2 * lmua * pow(NQCD, -1)) + 2 * lmua * NQCD + lmua * z * pow(NQCD, -1) + (- lmua * z * NQCD);
    return res;
}

double D0_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-pow(z, -1) * pow(NQCD, -1)) + pow(z, -1) * NQCD + pow(NQCD, -1) + (- NQCD) + (- 1. / 2. * z * pow(NQCD, -1)) + 1. / 2. * z * NQCD;
    return res;
}

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
        tmp = 1. / 2. * pow(z, -1) * pow(NQCD, -1) + (- 1. / 2. * pow(z, -1) * NQCD) + (- pow(NQCD, -1)) + NQCD + 1. / 2. * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 2. * x * pow(z, -1) * NQCD) + (- x * pow(NQCD, -1)) + x * NQCD + x * z * pow(NQCD, -1) + (- x * z * NQCD);
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - D0_RG: 000
  - DL_RG: 000, 001
  - RG_RG: 000
*/
