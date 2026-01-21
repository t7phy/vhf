#include "../sidis.h"



/* Helpers */

double DL_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-8 * CF);
    return res;
}

double DL_DL_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 3 * lmua * CF);
    return res;
}

double DL_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 3 * lmuf * CF);
    return res;
}

double DL_D0_001(double x, double z, double NF) {
    double res = 0.0;
    res = (-4 * lmua * CF);
    return res;
}

double DL_D1_000(double x, double z, double NF) {
    double res = 0.0;
    res = 2 * CF;
    return res;
}

double D0_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = (-4 * lmuf * CF);
    return res;
}

double D0_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = 2 * CF;
    return res;
}

double D1_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = 2 * CF;
    return res;
}

double DL_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = CF + (- z * CF) + (- ln(1 - z) * CF) + (- ln(1 - z) * z * CF) + (- ln(z) * CF) + (- ln(z) * z * CF) + 2 / (1 - z) * ln(z) * CF;
    return res;
}

double DL_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = 2 * lmua * CF + 2 * lmua * z * CF;
    return res;
}

double D0_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-CF) + (- z * CF);
    return res;
}

double RG_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = CF + (- x * CF) + (- ln(1 - x) * CF) + (- ln(1 - x) * x * CF) + ln(x) * CF + ln(x) * x * CF + (- 2 / (1 - x) * ln(x) * CF);
    return res;
}

double RG_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = 2 * lmuf * CF + 2 * lmuf * x * CF;
    return res;
}

double RG_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-CF) + (- x * CF);
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
        tmp = 2 * z * CF + 2 * x * CF;
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - D0_D0: 000
  - D0_DL: 010
  - D0_RG: 000
  - D1_DL: 000
  - DL_D0: 001
  - DL_D1: 000
  - DL_DL: 000, 001, 010
  - DL_RG: 000, 001
  - RG_D0: 000
  - RG_DL: 000, 010
  - RG_RG: 000
*/

/*
  Inverted Branch Report (By Number):
  - 000: D0_D0, D0_RG, D1_DL, DL_D1, DL_DL, DL_RG, RG_D0, RG_DL, RG_RG
  - 001: DL_D0, DL_DL, DL_RG
  - 010: D0_DL, DL_DL, RG_DL
*/
