#include "../sidis.h"



/* Helpers */

double DL_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-107. / 108. * pow(z, -1) * CF) + (- 11. / 9. * CF) + (- 4. / 9. * z * CF) + 287. / 108. * pow(z, 2) * CF + 2 * zeta3 * CF + 2 * zeta3 * z * CF + (- 1. / 6. * pow(pi, 2) * CF) + (- 1. / 4. * pow(pi, 2) * z * CF) + (- 7. / 18. * ln(1 - z) * pow(z, -1) * CF) + (- 10. / 3. * ln(1 - z) * CF) + 7. / 3. * ln(1 - z) * z * CF + 25. / 18. * ln(1 - z) * pow(z, 2) * CF + 1. / 3. * ln(1 - z) * pow(pi, 2) * CF + 1. / 3. * ln(1 - z) * pow(pi, 2) * z * CF + 1. / 3. * pow(ln(1 - z), 2) * pow(z, -1) * CF + 1. / 4. * pow(ln(1 - z), 2) * CF + (- 1. / 4. * pow(ln(1 - z), 2) * z * CF) + (- 1. / 3. * pow(ln(1 - z), 2) * pow(z, 2) * CF) + (- ln(1 - z) * Li2(1 - z) * CF) + (- ln(1 - z) * Li2(1 - z) * z * CF) + (- 2 * ln(1 - z) * Li2(z) * CF) + (- 2 * ln(1 - z) * Li2(z) * z * CF) + (- 7. / 18. * ln(z) * pow(z, -1) * CF) + (- 5 * ln(z) * CF) + (- 9. / 2. * ln(z) * z * CF) + (- 31. / 18. * ln(z) * pow(z, 2) * CF) + 1. / 6. * ln(z) * pow(pi, 2) * CF + 1. / 6. * ln(z) * pow(pi, 2) * z * CF + (- 3. / 2. * ln(z) * pow(ln(1 - z), 2) * CF) + (- 3. / 2. * ln(z) * pow(ln(1 - z), 2) * z * CF) +  + 1. / 3. * pow(ln(z), 2) * pow(z, -1) * CF + (- 1. / 8. * pow(ln(z), 2) * CF) + (- 5. / 8. * pow(ln(z), 2) * z * CF) + 5. / 12. * pow(ln(z), 3) * CF + 5. / 12. * pow(ln(z), 3) * z * CF + (- Li3(1 - z) * CF) + (- Li3(1 - z) * z * CF) + (- 2 * Li3(z) * CF) + (- 2 * Li3(z) * z * CF) + (- 2. / 3. * Li2(z) * pow(z, -1) * CF) + 1. / 2. * Li2(z) * CF + 2 * Li2(z) * z * CF + 2. / 3. * Li2(z) * pow(z, 2) * CF;
    return res;
}

double DL_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = 7. / 9. * lmua * pow(z, -1) * CF + 20. / 3. * lmua * CF + (- 14. / 3. * lmua * z * CF) + (- 25. / 9. * lmua * pow(z, 2) * CF) + (- 1. / 3. * lmua * pow(pi, 2) * CF) + (- 1. / 3. * lmua * pow(pi, 2) * z * CF) + (- 4. / 3. * lmua * ln(1 - z) * pow(z, -1) * CF) + (- lmua * ln(1 - z) * CF) + lmua * ln(1 - z) * z * CF + 4. / 3. * lmua * ln(1 - z) * pow(z, 2) * CF + 2 * lmua * Li2(z) * CF + 2 * lmua * Li2(z) * z * CF + (- 4. / 3. * ln(z) * lmua * pow(z, -1) * CF) + ln(z) * lmua * CF + 4 * ln(z) * lmua * z * CF + 4. / 3. * ln(z) * lmua * pow(z, 2) * CF + (- 2 * pow(ln(z), 2) * lmua * CF) + (- 2 * pow(ln(z), 2) * lmua * z * CF);
    return res;
}

double DL_RG_002(double x, double z, double NF) {
    double res = 0.0;
    res = 4. / 3. * pow(lmua, 2) * pow(z, -1) * CF + pow(lmua, 2) * CF + (- pow(lmua, 2) * z * CF) + (- 4. / 3. * pow(lmua, 2) * pow(z, 2) * CF) + 2 * ln(z) * pow(lmua, 2) * CF + 2 * ln(z) * pow(lmua, 2) * z * CF;
    return res;
}

double D0_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-7. / 18. * pow(z, -1) * CF) + (- 10. / 3. * CF) + 7. / 3. * z * CF + 25. / 18. * pow(z, 2) * CF + 1. / 6. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * z * CF + 2. / 3. * ln(1 - z) * pow(z, -1) * CF + 1. / 2. * ln(1 - z) * CF + (- 1. / 2. * ln(1 - z) * z * CF) + (- 2. / 3. * ln(1 - z) * pow(z, 2) * CF) + 2. / 3. * ln(z) * pow(z, -1) * CF + (- 1. / 2. * ln(z) * CF) + (- 2 * ln(z) * z * CF) + (- 2. / 3. * ln(z) * pow(z, 2) * CF) + pow(ln(z), 2) * CF + pow(ln(z), 2) * z * CF + (- Li2(z) * CF) + (- Li2(z) * z * CF);
    return res;
}

double D0_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 4. / 3. * lmua * pow(z, -1) * CF) + (- lmua * CF) + lmua * z * CF + 4. / 3. * lmua * pow(z, 2) * CF + (- 2 * ln(z) * lmua * CF) + (- 2 * ln(z) * lmua * z * CF);
    return res;
}

double D1_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = 2. / 3. * pow(z, -1) * CF + 1. / 2. * CF + (- 1. / 2. * z * CF) + (- 2. / 3. * pow(z, 2) * CF) + ln(z) * CF + ln(z) * z * CF;
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
        tmp = (-5. / 36. * pow(z, -1) * CF) + 2. / 3. * CF + 37. / 12. * z * CF + (- 65. / 18. * pow(z, 2) * CF) + 19. / 36. * x * pow(z, -1) * CF + 5. / 3. * x * CF + (- 47. / 12. * x * z * CF) + 31. / 18. * x * pow(z, 2) * CF + (- 1. / 6. * pow(pi, 2) * CF) + (- 1. / 3. * pow(pi, 2) * z * CF) + (- 1. / 6. * pow(pi, 2) * x * CF) + (- 1. / 3. * ln(1 - z) * pow(z, -1) * CF) + (- 3. / 2. * ln(1 - z) * CF) + 1. / 2. * ln(1 - z) * z * CF + 4. / 3. * ln(1 - z) * pow(z, 2) * CF + (- 1. / 3. * ln(1 - z) * x * pow(z, -1) * CF) + (- 1. / 2. * ln(1 - z) * x * CF) + 3. / 2. * ln(1 - z) * x * z * CF + (- 2. / 3. * ln(1 - z) * x * pow(z, 2) * CF) + (- 1. / 3. * ln(1 - x) * pow(z, -1) * CF) + (- 3. / 2. * ln(1 - x) * CF) + 1. / 2. * ln(1 - x) * z * CF + 4. / 3. * ln(1 - x) * pow(z, 2) * CF + (- 1. / 3. * ln(1 - x) * x * pow(z, -1) * CF) + (- 1. / 2. * ln(1 - x) * x * CF) + 3. / 2. * ln(1 - x) * x * z * CF + (- 2. / 3. * ln(1 - x) * x * pow(z, 2) * CF) + 2. / 3. * ln(x) * pow(z, -1) * CF + 3 * ln(x) * CF + (- ln(x) * z * CF) + (- 8. / 3. * ln(x) * pow(z, 2) * CF) + 2. / 3. * ln(x) * x * pow(z, -1) * CF + ln(x) * x * CF + (- 3 * ln(x) * x * z * CF) + 4. / 3. * ln(x) * x * pow(z, 2) * CF + 2 * ln(x) * ln(z) * CF + 4 * ln(x) * ln(z) * z * CF + 2 * ln(x) * ln(z) * x * CF + (- 1. / 3. * ln(z) * pow(z, -1) * CF) + (- 5. / 2. * ln(z) * CF) + 3. / 2. * ln(z) * z * CF + 4. / 3. * ln(z) * pow(z, 2) * CF + (- 1. / 3. * ln(z) * x * pow(z, -1) * CF) + 1. / 2. * ln(z) * x * CF + 3. / 2. * ln(z) * x * z * CF + (- 2. / 3. * ln(z) * x * pow(z, 2) * CF) + (- ln(z) * ln(1 - x) * CF) + (- 2 * ln(z) * ln(1 - x) * z * CF) + (- ln(z) * ln(1 - x) * x * CF) +  + (- pow(ln(z), 2) * CF) + (- 2 * pow(ln(z), 2) * z * CF) + (- pow(ln(z), 2) * x * CF) + Li2(z) * CF + 2 * Li2(z) * z * CF + Li2(z) * x * CF + (- 4. / 3. / (1 - x) * ln(x) * pow(z, -1) * CF) + (- 5. / 2. / (1 - x) * ln(x) * CF) + 5. / 2. / (1 - x) * ln(x) * z * CF + 4. / 3. / (1 - x) * ln(x) * pow(z, 2) * CF + (- 3 / (1 - x) * ln(x) * ln(z) * CF) + (- 3 / (1 - x) * ln(x) * ln(z) * z * CF);
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
        tmp = 2. / 3. * lmua * pow(z, -1) * CF + 3 * lmua * CF + (- lmua * z * CF) + (- 8. / 3. * lmua * pow(z, 2) * CF) + 2. / 3. * lmua * x * pow(z, -1) * CF + lmua * x * CF + (- 3 * lmua * x * z * CF) + 4. / 3. * lmua * x * pow(z, 2) * CF + 2 * ln(z) * lmua * CF + 4 * ln(z) * lmua * z * CF + 2 * ln(z) * lmua * x * CF;
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - D0_RG: 000, 001
  - D1_RG: 000
  - DL_RG: 000, 001, 002
  - RG_RG: 000, 001
*/

/*
  Inverted Branch Report (By Number):
  - 000: D0_RG, D1_RG, DL_RG, RG_RG
  - 001: D0_RG, DL_RG, RG_RG
  - 002: DL_RG
*/
