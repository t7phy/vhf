#include "../sidis.h"



/* Helpers */

double DL_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = 107. / 216. * pow(z, -1) * pow(NQCD, -1) + (- 107. / 216. * pow(z, -1) * NQCD) + 11. / 18. * pow(NQCD, -1) + (- 11. / 18. * NQCD) + 2. / 9. * z * pow(NQCD, -1) + (- 2. / 9. * z * NQCD) + (- 287. / 216. * pow(z, 2) * pow(NQCD, -1)) + 287. / 216. * pow(z, 2) * NQCD + (- zeta3 * pow(NQCD, -1)) + zeta3 * NQCD + (- zeta3 * z * pow(NQCD, -1)) + zeta3 * z * NQCD + 1. / 12. * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 12. * pow(pi, 2) * NQCD) + 1. / 8. * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 8. * pow(pi, 2) * z * NQCD) + 7. / 36. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 7. / 36. * ln(1 - z) * pow(z, -1) * NQCD) + 5. / 3. * ln(1 - z) * pow(NQCD, -1) + (- 5. / 3. * ln(1 - z) * NQCD) + (- 7. / 6. * ln(1 - z) * z * pow(NQCD, -1)) + 7. / 6. * ln(1 - z) * z * NQCD + (- 25. / 36. * ln(1 - z) * pow(z, 2) * pow(NQCD, -1)) + 25. / 36. * ln(1 - z) * pow(z, 2) * NQCD + (- 1. / 6. * ln(1 - z) * pow(pi, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1 - z) * pow(pi, 2) * NQCD + (- 1. / 6. * ln(1 - z) * pow(pi, 2) * z * pow(NQCD, -1)) + 1. / 6. * ln(1 - z) * pow(pi, 2) * z * NQCD + (- 1. / 6. * pow(ln(1 - z), 2) * pow(z, -1) * pow(NQCD, -1)) + 1. / 6. * pow(ln(1 - z), 2) * pow(z, -1) * NQCD + (- 1. / 8. * pow(ln(1 - z), 2) * pow(NQCD, -1)) + 1. / 8. * pow(ln(1 - z), 2) * NQCD + 1. / 8. * pow(ln(1 - z), 2) * z * pow(NQCD, -1) + (- 1. / 8. * pow(ln(1 - z), 2) * z * NQCD) + 1. / 6. * pow(ln(1 - z), 2) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 6. * pow(ln(1 - z), 2) * pow(z, 2) * NQCD) + 1. / 2. * ln(1 - z) * Li2(1 - z) * pow(NQCD, -1) + (- 1. / 2. * ln(1 - z) * Li2(1 - z) * NQCD) + 1. / 2. * ln(1 - z) * Li2(1 - z) * z * pow(NQCD, -1) + (- 1. / 2. * ln(1 - z) * Li2(1 - z) * z * NQCD) + ln(1 - z) * Li2(z) * pow(NQCD, -1) + (- ln(1 - z) * Li2(z) * NQCD) + ln(1 - z) * Li2(z) * z * pow(NQCD, -1) + (- ln(1 - z) * Li2(z) * z * NQCD) +  +  + 7. / 36. * ln(z) * pow(z, -1) * pow(NQCD, -1) + (- 7. / 36. * ln(z) * pow(z, -1) * NQCD) + 5. / 2. * ln(z) * pow(NQCD, -1) + (- 5. / 2. * ln(z) * NQCD) + 9. / 4. * ln(z) * z * pow(NQCD, -1) + (- 9. / 4. * ln(z) * z * NQCD) + 31. / 36. * ln(z) * pow(z, 2) * pow(NQCD, -1) + (- 31. / 36. * ln(z) * pow(z, 2) * NQCD) + (- 1. / 12. * ln(z) * pow(pi, 2) * pow(NQCD, -1)) + 1. / 12. * ln(z) * pow(pi, 2) * NQCD + (- 1. / 12. * ln(z) * pow(pi, 2) * z * pow(NQCD, -1)) + 1. / 12. * ln(z) * pow(pi, 2) * z * NQCD + 3. / 4. * ln(z) * pow(ln(1 - z), 2) * pow(NQCD, -1) + (- 3. / 4. * ln(z) * pow(ln(1 - z), 2) * NQCD) + 3. / 4. * ln(z) * pow(ln(1 - z), 2) * z * pow(NQCD, -1) + (- 3. / 4. * ln(z) * pow(ln(1 - z), 2) * z * NQCD) + (- 1. / 6. * pow(ln(z), 2) * pow(z, -1) * pow(NQCD, -1)) + 1. / 6. * pow(ln(z), 2) * pow(z, -1) * NQCD + 1. / 16. * pow(ln(z), 2) * pow(NQCD, -1) + (- 1. / 16. * pow(ln(z), 2) * NQCD) + 5. / 16. * pow(ln(z), 2) * z * pow(NQCD, -1) + (- 5. / 16. * pow(ln(z), 2) * z * NQCD) +  + (- 5. / 24. * pow(ln(z), 3) * pow(NQCD, -1)) + 5. / 24. * pow(ln(z), 3) * NQCD + (- 5. / 24. * pow(ln(z), 3) * z * pow(NQCD, -1)) + 5. / 24. * pow(ln(z), 3) * z * NQCD + 1. / 2. * Li3(1 - z) * pow(NQCD, -1) + (- 1. / 2. * Li3(1 - z) * NQCD) + 1. / 2. * Li3(1 - z) * z * pow(NQCD, -1) + (- 1. / 2. * Li3(1 - z) * z * NQCD) + Li3(z) * pow(NQCD, -1) + (- Li3(z) * NQCD) + Li3(z) * z * pow(NQCD, -1) + (- Li3(z) * z * NQCD) + 1. / 3. * Li2(z) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 3. * Li2(z) * pow(z, -1) * NQCD) + (- 1. / 4. * Li2(z) * pow(NQCD, -1)) + 1. / 4. * Li2(z) * NQCD + (- Li2(z) * z * pow(NQCD, -1)) + Li2(z) * z * NQCD + (- 1. / 3. * Li2(z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 3. * Li2(z) * pow(z, 2) * NQCD;
    return res;
}

double DL_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 7. / 18. * lmua * pow(z, -1) * pow(NQCD, -1)) + 7. / 18. * lmua * pow(z, -1) * NQCD + (- 10. / 3. * lmua * pow(NQCD, -1)) + 10. / 3. * lmua * NQCD + 7. / 3. * lmua * z * pow(NQCD, -1) + (- 7. / 3. * lmua * z * NQCD) + 25. / 18. * lmua * pow(z, 2) * pow(NQCD, -1) + (- 25. / 18. * lmua * pow(z, 2) * NQCD) + 1. / 6. * lmua * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 6. * lmua * pow(pi, 2) * NQCD) + 1. / 6. * lmua * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 6. * lmua * pow(pi, 2) * z * NQCD) + 2. / 3. * lmua * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 2. / 3. * lmua * ln(1 - z) * pow(z, -1) * NQCD) + 1. / 2. * lmua * ln(1 - z) * pow(NQCD, -1) + (- 1. / 2. * lmua * ln(1 - z) * NQCD) + (- 1. / 2. * lmua * ln(1 - z) * z * pow(NQCD, -1)) + 1. / 2. * lmua * ln(1 - z) * z * NQCD + (- 2. / 3. * lmua * ln(1 - z) * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * lmua * ln(1 - z) * pow(z, 2) * NQCD + (- lmua * Li2(z) * pow(NQCD, -1)) + lmua * Li2(z) * NQCD + (- lmua * Li2(z) * z * pow(NQCD, -1)) + lmua * Li2(z) * z * NQCD + 2. / 3. * ln(z) * lmua * pow(z, -1) * pow(NQCD, -1) + (- 2. / 3. * ln(z) * lmua * pow(z, -1) * NQCD) + (- 1. / 2. * ln(z) * lmua * pow(NQCD, -1)) + 1. / 2. * ln(z) * lmua * NQCD + (- 2 * ln(z) * lmua * z * pow(NQCD, -1)) + 2 * ln(z) * lmua * z * NQCD + (- 2. / 3. * ln(z) * lmua * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * ln(z) * lmua * pow(z, 2) * NQCD + pow(ln(z), 2) * lmua * pow(NQCD, -1) + (- pow(ln(z), 2) * lmua * NQCD) + pow(ln(z), 2) * lmua * z * pow(NQCD, -1) + (-pow(ln(z), 2) * lmua * z * NQCD);
    return res;
}

double DL_RG_002(double x, double z, double NF) {
    double res = 0.0;
    res = (- 2. / 3. * pow(lmua, 2) * pow(z, -1) * pow(NQCD, -1)) + 2. / 3. * pow(lmua, 2) * pow(z, -1) * NQCD + (- 1. / 2. * pow(lmua, 2) * pow(NQCD, -1)) + 1. / 2. * pow(lmua, 2) * NQCD + 1. / 2. * pow(lmua, 2) * z * pow(NQCD, -1) + (- 1. / 2. * pow(lmua, 2) * z * NQCD) + 2. / 3. * pow(lmua, 2) * pow(z, 2) * pow(NQCD, -1) + (- 2. / 3. * pow(lmua, 2) * pow(z, 2) * NQCD) + (- ln(z) * pow(lmua, 2) * pow(NQCD, -1)) + ln(z) * pow(lmua, 2) * NQCD + (- ln(z) * pow(lmua, 2) * z * pow(NQCD, -1)) + ln(z) * pow(lmua, 2) * z * NQCD;
    return res;
}

double D0_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = 7. / 36. * pow(z, -1) * pow(NQCD, -1) + (- 7. / 36. * pow(z, -1) * NQCD) + 5. / 3. * pow(NQCD, -1) + (- 5. / 3. * NQCD) + (- 7. / 6. * z * pow(NQCD, -1)) + 7. / 6. * z * NQCD + (- 25. / 36. * pow(z, 2) * pow(NQCD, -1)) + 25. / 36. * pow(z, 2) * NQCD + (- 1. / 12. * pow(pi, 2) * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * NQCD + (- 1. / 12. * pow(pi, 2) * z * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * z * NQCD + (- 1. / 3. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * ln(1 - z) * pow(z, -1) * NQCD + (- 1. / 4. * ln(1 - z) * pow(NQCD, -1)) + 1. / 4. * ln(1 - z) * NQCD + 1. / 4. * ln(1 - z) * z * pow(NQCD, -1) + (- 1. / 4. * ln(1 - z) * z * NQCD) + 1. / 3. * ln(1 - z) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(1 - z) * pow(z, 2) * NQCD) + (- 1. / 3. * ln(z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * ln(z) * pow(z, -1) * NQCD + 1. / 4. * ln(z) * pow(NQCD, -1) + (- 1. / 4. * ln(z) * NQCD) + ln(z) * z * pow(NQCD, -1) + (- ln(z) * z * NQCD) + 1. / 3. * ln(z) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(z) * pow(z, 2) * NQCD) + (- 1. / 2. * pow(ln(z), 2) * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * NQCD + (- 1. / 2. * pow(ln(z), 2) * z * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * z * NQCD + 1. / 2. * Li2(z) * pow(NQCD, -1) +  + (-1. / 2. * Li2(z) * NQCD) + 1. / 2. * Li2(z) * z * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * z * NQCD);
    return res;
}

double D0_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = 2. / 3. * lmua * pow(z, -1) * pow(NQCD, -1) + (- 2. / 3. * lmua * pow(z, -1) * NQCD) + 1. / 2. * lmua * pow(NQCD, -1) + (- 1. / 2. * lmua * NQCD) + (- 1. / 2. * lmua * z * pow(NQCD, -1)) + 1. / 2. * lmua * z * NQCD + (- 2. / 3. * lmua * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * lmua * pow(z, 2) * NQCD + ln(z) * lmua * pow(NQCD, -1) + (- ln(z) * lmua * NQCD) + ln(z) * lmua * z * pow(NQCD, -1) + (- ln(z) * lmua * z * NQCD);
    return res;
}

double D1_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-1. / 3. * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * pow(z, -1) * NQCD + (- 1. / 4. * pow(NQCD, -1)) + 1. / 4. * NQCD + 1. / 4. * z * pow(NQCD, -1) + (- 1. / 4. * z * NQCD) + 1. / 3. * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * pow(z, 2) * NQCD) + (- 1. / 2. * ln(z) * pow(NQCD, -1)) + 1. / 2. * ln(z) * NQCD + (- 1. / 2. * ln(z) * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * z * NQCD;
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
        tmp = 5. / 72. * pow(z, -1) * pow(NQCD, -1) + (- 5. / 72. * pow(z, -1) * NQCD) + (- 1. / 3. * pow(NQCD, -1)) + 1. / 3. * NQCD + (- 37. / 24. * z * pow(NQCD, -1)) + 37. / 24. * z * NQCD + 65. / 36. * pow(z, 2) * pow(NQCD, -1) + (- 65. / 36. * pow(z, 2) * NQCD) + (- 19. / 72. * x * pow(z, -1) * pow(NQCD, -1)) + 19. / 72. * x * pow(z, -1) * NQCD + (- 5. / 6. * x * pow(NQCD, -1)) + 5. / 6. * x * NQCD + 47. / 24. * x * z * pow(NQCD, -1) + (- 47. / 24. * x * z * NQCD) + (- 31. / 36. * x * pow(z, 2) * pow(NQCD, -1)) + 31. / 36. * x * pow(z, 2) * NQCD + 1. / 12. * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 12. * pow(pi, 2) * NQCD) + 1. / 6. * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 6. * pow(pi, 2) * z * NQCD) + 1. / 12. * pow(pi, 2) * x * pow(NQCD, -1) + (- 1. / 12. * pow(pi, 2) * x * NQCD) + 1. / 6. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(1 - z) * pow(z, -1) * NQCD) + 3. / 4. * ln(1 - z) * pow(NQCD, -1) + (- 3. / 4. * ln(1 - z) * NQCD) + (- 1. / 4. * ln(1 - z) * z * pow(NQCD, -1)) + 1. / 4. * ln(1 - z) * z * NQCD + (- 2. / 3. * ln(1 - z) * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * ln(1 - z) * pow(z, 2) * NQCD + 1. / 6. * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(1 - z) * x * pow(z, -1) * NQCD) + 1. / 4. * ln(1 - z) * x * pow(NQCD, -1) + (- 1. / 4. * ln(1 - z) * x * NQCD) + (- 3. / 4. * ln(1 - z) * x * z * pow(NQCD, -1)) + 3. / 4. * ln(1 - z) * x * z * NQCD + 1. / 3. * ln(1 - z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(1 - z) * x * pow(z, 2) * NQCD) + 1. / 6. * ln(1 - x) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(1 - x) * pow(z, -1) * NQCD) + 3. / 4. * ln(1 - x) * pow(NQCD, -1) + (- 3. / 4. * ln(1 - x) * NQCD) + (- 1. / 4. * ln(1 - x) * z * pow(NQCD, -1)) + 1. / 4. * ln(1 - x) * z * NQCD + (- 2. / 3. * ln(1 - x) * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * ln(1 - x) * pow(z, 2) * NQCD + 1. / 6. * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1) +  + (-1. / 6. * ln(1 - x) * x * pow(z, -1) * NQCD) + 1. / 4. * ln(1 - x) * x * pow(NQCD, -1) + (- 1. / 4. * ln(1 - x) * x * NQCD) + (- 3. / 4. * ln(1 - x) * x * z * pow(NQCD, -1)) + 3. / 4. * ln(1 - x) * x * z * NQCD + 1. / 3. * ln(1 - x) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(1 - x) * x * pow(z, 2) * NQCD) + (- 1. / 3. * ln(x) * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * ln(x) * pow(z, -1) * NQCD + (- 3. / 2. * ln(x) * pow(NQCD, -1)) + 3. / 2. * ln(x) * NQCD + 1. / 2. * ln(x) * z * pow(NQCD, -1) + (- 1. / 2. * ln(x) * z * NQCD) + 4. / 3. * ln(x) * pow(z, 2) * pow(NQCD, -1) + (- 4. / 3. * ln(x) * pow(z, 2) * NQCD) + (- 1. / 3. * ln(x) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * ln(x) * x * pow(z, -1) * NQCD + (- 1. / 2. * ln(x) * x * pow(NQCD, -1)) + 1. / 2. * ln(x) * x * NQCD + 3. / 2. * ln(x) * x * z * pow(NQCD, -1) + (- 3. / 2. * ln(x) * x * z * NQCD) + (- 2. / 3. * ln(x) * x * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * ln(x) * x * pow(z, 2) * NQCD + (- ln(x) * ln(z) * pow(NQCD, -1)) +  + ln(x) * ln(z) * NQCD + (- 2 * ln(x) * ln(z) * z * pow(NQCD, -1)) + 2 * ln(x) * ln(z) * z * NQCD + (- ln(x) * ln(z) * x * pow(NQCD, -1)) + ln(x) * ln(z) * x * NQCD + 1. / 6. * ln(z) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(z) * pow(z, -1) * NQCD) + 5. / 4. * ln(z) * pow(NQCD, -1) + (- 5. / 4. * ln(z) * NQCD) + (- 3. / 4. * ln(z) * z * pow(NQCD, -1)) + 3. / 4. * ln(z) * z * NQCD + (- 2. / 3. * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * ln(z) * pow(z, 2) * NQCD + 1. / 6. * ln(z) * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(z) * x * pow(z, -1) * NQCD) + (- 1. / 4. * ln(z) * x * pow(NQCD, -1)) + 1. / 4. * ln(z) * x * NQCD + (- 3. / 4. * ln(z) * x * z * pow(NQCD, -1)) + 3. / 4. * ln(z) * x * z * NQCD + 1. / 3. * ln(z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(z) * x * pow(z, 2) * NQCD) + 1. / 2. * ln(z) * ln(1 - x) * pow(NQCD, -1) + (- 1. / 2. * ln(z) * ln(1 - x) * NQCD) + ln(z) * ln(1 - x) * z * pow(NQCD, -1) + (- ln(z) * ln(1 - x) * z * NQCD) + 1. / 2. * ln(z) * ln(1 - x) * x * pow(NQCD, -1) + (- 1. / 2. * ln(z) * ln(1 - x) * x * NQCD) + 1. / 2. * pow(ln(z), 2) * pow(NQCD, -1) + (- 1. / 2. * pow(ln(z), 2) * NQCD) + pow(ln(z), 2) * z * pow(NQCD, -1) + (- pow(ln(z), 2) * z * NQCD) + 1. / 2. * pow(ln(z), 2) * x * pow(NQCD, -1) + (- 1. / 2. * pow(ln(z), 2) * x * NQCD) + (- 1. / 2. * Li2(z) * pow(NQCD, -1)) + 1. / 2. * Li2(z) * NQCD + (- Li2(z) * z * pow(NQCD, -1)) + Li2(z) * z * NQCD + (- 1. / 2. * Li2(z) * x * pow(NQCD, -1)) + 1. / 2. * Li2(z) * x * NQCD + 2. / 3. / (1 - x) * ln(x) * pow(z, -1) * pow(NQCD, -1) + (- 2. / 3. / (1 - x) * ln(x) * pow(z, -1) * NQCD) +  + 5. / 4. / (1 - x) * ln(x) * pow(NQCD, -1) + (- 5. / 4. / (1 - x) * ln(x) * NQCD) + (- 5. / 4. / (1 - x) * ln(x) * z * pow(NQCD, -1)) + 5. / 4. / (1 - x) * ln(x) * z * NQCD + (- 2. / 3. / (1 - x) * ln(x) * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. / (1 - x) * ln(x) * pow(z, 2) * NQCD + 3. / 2. / (1 - x) * ln(x) * ln(z) * pow(NQCD, -1) + (- 3. / 2. / (1 - x) * ln(x) * ln(z) * NQCD) + 3. / 2. / (1 - x) * ln(x) * ln(z) * z * pow(NQCD, -1) + (- 3. / 2. / (1 - x) * ln(x) * ln(z) * z * NQCD);
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
        tmp = (- 1. / 3. * lmua * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * lmua * pow(z, -1) * NQCD + (- 3. / 2. * lmua * pow(NQCD, -1)) + 3. / 2. * lmua * NQCD + 1. / 2. * lmua * z * pow(NQCD, -1) + (- 1. / 2. * lmua * z * NQCD) + 4. / 3. * lmua * pow(z, 2) * pow(NQCD, -1) + (- 4. / 3. * lmua * pow(z, 2) * NQCD) + (- 1. / 3. * lmua * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * lmua * x * pow(z, -1) * NQCD + (- 1. / 2. * lmua * x * pow(NQCD, -1)) + 1. / 2. * lmua * x * NQCD + 3. / 2. * lmua * x * z * pow(NQCD, -1) + (- 3. / 2. * lmua * x * z * NQCD) + (- 2. / 3. * lmua * x * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * lmua * x * pow(z, 2) * NQCD + (- ln(z) * lmua * pow(NQCD, -1)) + ln(z) * lmua * NQCD + (- 2 * ln(z) * lmua * z * pow(NQCD, -1)) + 2 * ln(z) * lmua * z * NQCD + (- ln(z) * lmua * x * pow(NQCD, -1)) + ln(z) * lmua * x * NQCD;
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
