#include "../sidis.h"



/* Helpers */

double DL_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-107. / 432. * pow(z, -1) * pow(NQCD, -1)) + 107. / 432. * pow(z, -1) * NQCD + (- 11. / 36. * pow(NQCD, -1)) + 11. / 36. * NQCD + (- 1. / 9. * z * pow(NQCD, -1)) + 1. / 9. * z * NQCD + 287. / 432. * pow(z, 2) * pow(NQCD, -1) + (- 287. / 432. * pow(z, 2) * NQCD) + 1. / 2. * zeta3 * pow(NQCD, -1) + (- 1. / 2. * zeta3 * NQCD) + 1. / 2. * zeta3 * z * pow(NQCD, -1) + (- 1. / 2. * zeta3 * z * NQCD) + (- 1. / 24. * pow(pi, 2) * pow(NQCD, -1)) + 1. / 24. * pow(pi, 2) * NQCD + (- 1. / 16. * pow(pi, 2) * z * pow(NQCD, -1)) + 1. / 16. * pow(pi, 2) * z * NQCD + (- 7. / 72. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + 7. / 72. * ln(1 - z) * pow(z, -1) * NQCD + (- 5. / 6. * ln(1 - z) * pow(NQCD, -1)) + 5. / 6. * ln(1 - z) * NQCD + 7. / 12. * ln(1 - z) * z * pow(NQCD, -1) + (- 7. / 12. * ln(1 - z) * z * NQCD) + 25. / 72. * ln(1 - z) * pow(z, 2) * pow(NQCD, -1) + (- 25. / 72. * ln(1 - z) * pow(z, 2) * NQCD) + 1. / 12. * ln(1 - z) * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 12. * ln(1 - z) * pow(pi, 2) * NQCD) + 1. / 12. * ln(1 - z) * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 12. * ln(1 - z) * pow(pi, 2) * z * NQCD) + 1. / 12. * pow(ln(1 - z), 2) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 12. * pow(ln(1 - z), 2) * pow(z, -1) * NQCD) + 1. / 16. * pow(ln(1 - z), 2) * pow(NQCD, -1) + (- 1. / 16. * pow(ln(1 - z), 2) * NQCD) + (- 1. / 16. * pow(ln(1 - z), 2) * z * pow(NQCD, -1)) + 1. / 16. * pow(ln(1 - z), 2) * z * NQCD + (- 1. / 12. * pow(ln(1 - z), 2) * pow(z, 2) * pow(NQCD, -1)) + 1. / 12. * pow(ln(1 - z), 2) * pow(z, 2) * NQCD + (- 1. / 4. * ln(1 - z) * Li2(1 - z) * pow(NQCD, -1)) + 1. / 4. * ln(1 - z) * Li2(1 - z) * NQCD + (- 1. / 4. * ln(1 - z) * Li2(1 - z) * z * pow(NQCD, -1)) + 1. / 4. * ln(1 - z) * Li2(1 - z) * z * NQCD + (- 1. / 2. * ln(1 - z) * Li2(z) * pow(NQCD, -1)) + 1. / 2. * ln(1 - z) * Li2(z) * NQCD + (- 1. / 2. * ln(1 - z) * Li2(z) * z * pow(NQCD, -1)) +  + 1. / 2. * ln(1 - z) * Li2(z) * z * NQCD +  + (- 7. / 72. * ln(z) * pow(z, -1) * pow(NQCD, -1)) + 7. / 72. * ln(z) * pow(z, -1) * NQCD + (- 5. / 4. * ln(z) * pow(NQCD, -1)) + 5. / 4. * ln(z) * NQCD + (- 9. / 8. * ln(z) * z * pow(NQCD, -1)) + 9. / 8. * ln(z) * z * NQCD + (- 31. / 72. * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 31. / 72. * ln(z) * pow(z, 2) * NQCD + 1. / 24. * ln(z) * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 24. * ln(z) * pow(pi, 2) * NQCD) + 1. / 24. * ln(z) * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 24. * ln(z) * pow(pi, 2) * z * NQCD) + (- 3. / 8. * ln(z) * pow(ln(1 - z), 2) * pow(NQCD, -1)) + 3. / 8. * ln(z) * pow(ln(1 - z), 2) * NQCD + (- 3. / 8. * ln(z) * pow(ln(1 - z), 2) * z * pow(NQCD, -1)) + 3. / 8. * ln(z) * pow(ln(1 - z), 2) * z * NQCD + 1. / 12. * pow(ln(z), 2) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 12. * pow(ln(z), 2) * pow(z, -1) * NQCD) + (- 1. / 32. * pow(ln(z), 2) * pow(NQCD, -1)) + 1. / 32. * pow(ln(z), 2) * NQCD + (- 5. / 32. * pow(ln(z), 2) * z * pow(NQCD, -1)) + 5. / 32. * pow(ln(z), 2) * z * NQCD +  + 5. / 48. * pow(ln(z), 3) * pow(NQCD, -1) + (- 5. / 48. * pow(ln(z), 3) * NQCD) + 5. / 48. * pow(ln(z), 3) * z * pow(NQCD, -1) + (- 5. / 48. * pow(ln(z), 3) * z * NQCD) + (- 1. / 4. * Li3(1 - z) * pow(NQCD, -1)) + 1. / 4. * Li3(1 - z) * NQCD + (- 1. / 4. * Li3(1 - z) * z * pow(NQCD, -1)) + 1. / 4. * Li3(1 - z) * z * NQCD + (- 1. / 2. * Li3(z) * pow(NQCD, -1)) + 1. / 2. * Li3(z) * NQCD + (- 1. / 2. * Li3(z) * z * pow(NQCD, -1)) + 1. / 2. * Li3(z) * z * NQCD + (- 1. / 6. * Li2(z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 6. * Li2(z) * pow(z, -1) * NQCD + 1. / 8. * Li2(z) * pow(NQCD, -1) + (- 1. / 8. * Li2(z) * NQCD) + 1. / 2. * Li2(z) * z * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * z * NQCD) + 1. / 6. * Li2(z) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 6. * Li2(z) * pow(z, 2) * NQCD);
    return res;
}

double DL_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = 7. / 36. * lmua * pow(z, -1) * pow(NQCD, -1) + (- 7. / 36. * lmua * pow(z, -1) * NQCD) + 5. / 3. * lmua * pow(NQCD, -1) + (- 5. / 3. * lmua * NQCD) + (- 7. / 6. * lmua * z * pow(NQCD, -1)) + 7. / 6. * lmua * z * NQCD + (- 25. / 36. * lmua * pow(z, 2) * pow(NQCD, -1)) + 25. / 36. * lmua * pow(z, 2) * NQCD + (- 1. / 12. * lmua * pow(pi, 2) * pow(NQCD, -1)) + 1. / 12. * lmua * pow(pi, 2) * NQCD + (- 1. / 12. * lmua * pow(pi, 2) * z * pow(NQCD, -1)) + 1. / 12. * lmua * pow(pi, 2) * z * NQCD + (- 1. / 3. * lmua * ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * lmua * ln(1 - z) * pow(z, -1) * NQCD + (- 1. / 4. * lmua * ln(1 - z) * pow(NQCD, -1)) + 1. / 4. * lmua * ln(1 - z) * NQCD + 1. / 4. * lmua * ln(1 - z) * z * pow(NQCD, -1) + (- 1. / 4. * lmua * ln(1 - z) * z * NQCD) + 1. / 3. * lmua * ln(1 - z) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * lmua * ln(1 - z) * pow(z, 2) * NQCD) + 1. / 2. * lmua * Li2(z) * pow(NQCD, -1) + (- 1. / 2. * lmua * Li2(z) * NQCD) + 1. / 2. * lmua * Li2(z) * z * pow(NQCD, -1) + (- 1. / 2. * lmua * Li2(z) * z * NQCD) + (- 1. / 3. * ln(z) * lmua * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * ln(z) * lmua * pow(z, -1) * NQCD + 1. / 4. * ln(z) * lmua * pow(NQCD, -1) + (- 1. / 4. * ln(z) * lmua * NQCD) + ln(z) * lmua * z * pow(NQCD, -1) + (- ln(z) * lmua * z * NQCD) + 1. / 3. * ln(z) * lmua * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(z) * lmua * pow(z, 2) * NQCD) + (-1. / 2. * pow(ln(z), 2) * lmua * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * lmua * NQCD + (- 1. / 2. * pow(ln(z), 2) * lmua * z * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * lmua * z * NQCD;
    return res;
}

double DL_RG_002(double x, double z, double NF) {
    double res = 0.0;
    res = 1. / 3. * pow(lmua, 2) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 3. * pow(lmua, 2) * pow(z, -1) * NQCD) + 1. / 4. * pow(lmua, 2) * pow(NQCD, -1) + (- 1. / 4. * pow(lmua, 2) * NQCD) + (- 1. / 4. * pow(lmua, 2) * z * pow(NQCD, -1)) + 1. / 4. * pow(lmua, 2) * z * NQCD + (- 1. / 3. * pow(lmua, 2) * pow(z, 2) * pow(NQCD, -1)) + 1. / 3. * pow(lmua, 2) * pow(z, 2) * NQCD + 1. / 2. * ln(z) * pow(lmua, 2) * pow(NQCD, -1) + (- 1. / 2. * ln(z) * pow(lmua, 2) * NQCD) + 1. / 2. * ln(z) * pow(lmua, 2) * z * pow(NQCD, -1) + (- 1. / 2. * ln(z) * pow(lmua, 2) * z * NQCD);
    return res;
}

double D0_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-7. / 72. * pow(z, -1) * pow(NQCD, -1)) + 7. / 72. * pow(z, -1) * NQCD + (- 5. / 6. * pow(NQCD, -1)) + 5. / 6. * NQCD + 7. / 12. * z * pow(NQCD, -1) + (- 7. / 12. * z * NQCD) + 25. / 72. * pow(z, 2) * pow(NQCD, -1) + (- 25. / 72. * pow(z, 2) * NQCD) + 1. / 24. * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 24. * pow(pi, 2) * NQCD) + 1. / 24. * pow(pi, 2) * z * pow(NQCD, -1) + (- 1. / 24. * pow(pi, 2) * z * NQCD) + 1. / 6. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(1 - z) * pow(z, -1) * NQCD) + 1. / 8. * ln(1 - z) * pow(NQCD, -1) + (- 1. / 8. * ln(1 - z) * NQCD) + (- 1. / 8. * ln(1 - z) * z * pow(NQCD, -1)) + 1. / 8. * ln(1 - z) * z * NQCD + (- 1. / 6. * ln(1 - z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1 - z) * pow(z, 2) * NQCD + 1. / 6. * ln(z) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(z) * pow(z, -1) * NQCD) + (- 1. / 8. * ln(z) * pow(NQCD, -1)) + 1. / 8. * ln(z) * NQCD + (- 1. / 2. * ln(z) * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * z * NQCD + (- 1. / 6. * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(z) * pow(z, 2) * NQCD + 1. / 4. * pow(ln(z), 2) * pow(NQCD, -1) + (- 1. / 4. * pow(ln(z), 2) * NQCD) + 1. / 4. * pow(ln(z), 2) * z * pow(NQCD, -1) + (- 1. / 4. * pow(ln(z), 2) * z * NQCD) +  + (-1. / 4. * Li2(z) * pow(NQCD, -1)) + 1. / 4. * Li2(z) * NQCD + (- 1. / 4. * Li2(z) * z * pow(NQCD, -1)) + 1. / 4. * Li2(z) * z * NQCD;
    return res;
}

double D0_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 1. / 3. * lmua * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. * lmua * pow(z, -1) * NQCD + (- 1. / 4. * lmua * pow(NQCD, -1)) + 1. / 4. * lmua * NQCD + 1. / 4. * lmua * z * pow(NQCD, -1) + (- 1. / 4. * lmua * z * NQCD) + 1. / 3. * lmua * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * lmua * pow(z, 2) * NQCD) + (- 1. / 2. * ln(z) * lmua * pow(NQCD, -1)) + 1. / 2. * ln(z) * lmua * NQCD + (- 1. / 2. * ln(z) * lmua * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * lmua * z * NQCD;
    return res;
}

double D1_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = 1. / 6. * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * pow(z, -1) * NQCD) + 1. / 8. * pow(NQCD, -1) + (- 1. / 8. * NQCD) + (- 1. / 8. * z * pow(NQCD, -1)) + 1. / 8. * z * NQCD + (- 1. / 6. * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * pow(z, 2) * NQCD + 1. / 4. * ln(z) * pow(NQCD, -1) + (- 1. / 4. * ln(z) * NQCD) + 1. / 4. * ln(z) * z * pow(NQCD, -1) + (- 1. / 4. * ln(z) * z * NQCD);
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
        tmp = (-5. / 144. * pow(z, -1) * pow(NQCD, -1)) + 5. / 144. * pow(z, -1) * NQCD + (- 1. / 12. * pow(NQCD, -1)) + 1. / 12. * NQCD + (- 23. / 48. * z * pow(NQCD, -1)) + 23. / 48. * z * NQCD + 43. / 72. * pow(z, 2) * pow(NQCD, -1) + (- 43. / 72. * pow(z, 2) * NQCD) + 19. / 144. * x * pow(z, -1) * pow(NQCD, -1) + (- 19. / 144. * x * pow(z, -1) * NQCD) + 2. / 3. * x * pow(NQCD, -1) + (- 2. / 3. * x * NQCD) + 13. / 48. * x * z * pow(NQCD, -1) + (- 13. / 48. * x * z * NQCD) + (- 77. / 72. * x * pow(z, 2) * pow(NQCD, -1)) + 77. / 72. * x * pow(z, 2) * NQCD + (- 1. / 24. * pow(pi, 2) * pow(NQCD, -1)) + 1. / 24. * pow(pi, 2) * NQCD + (- 1. / 24. * pow(pi, 2) * x * pow(NQCD, -1)) + 1. / 24. * pow(pi, 2) * x * NQCD + (- 1. / 12. * pow(pi, 2) * x * z * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * x * z * NQCD + (- 1. / 12. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1 - z) * pow(z, -1) * NQCD + (- 1. / 8. * ln(1 - z) * pow(NQCD, -1)) + 1. / 8. * ln(1 - z) * NQCD + 3. / 8. * ln(1 - z) * z * pow(NQCD, -1) + (- 3. / 8. * ln(1 - z) * z * NQCD) + (- 1. / 6. * ln(1 - z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1 - z) * pow(z, 2) * NQCD + (- 1. / 12. * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1 - z) * x * pow(z, -1) * NQCD + (- 3. / 8. * ln(1 - z) * x * pow(NQCD, -1)) + 3. / 8. * ln(1 - z) * x * NQCD + 1. / 8. * ln(1 - z) * x * z * pow(NQCD, -1) + (- 1. / 8. * ln(1 - z) * x * z * NQCD) + 1. / 3. * ln(1 - z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(1 - z) * x * pow(z, 2) * NQCD) + (- 1. / 12. * ln(1 - x) * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1 - x) * pow(z, -1) * NQCD + (- 1. / 8. * ln(1 - x) * pow(NQCD, -1)) + 1. / 8. * ln(1 - x) * NQCD + 3. / 8. * ln(1 - x) * z * pow(NQCD, -1) + (- 3. / 8. * ln(1 - x) * z * NQCD) + (- 1. / 6. * ln(1 - x) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1 - x) * pow(z, 2) * NQCD +  + (-1. / 12. * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(1 - x) * x * pow(z, -1) * NQCD + (- 3. / 8. * ln(1 - x) * x * pow(NQCD, -1)) + 3. / 8. * ln(1 - x) * x * NQCD + 1. / 8. * ln(1 - x) * x * z * pow(NQCD, -1) + (- 1. / 8. * ln(1 - x) * x * z * NQCD) + 1. / 3. * ln(1 - x) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(1 - x) * x * pow(z, 2) * NQCD) + 1. / 6. * ln(x) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(x) * pow(z, -1) * NQCD) + 1. / 4. * ln(x) * pow(NQCD, -1) + (- 1. / 4. * ln(x) * NQCD) + (- 3. / 4. * ln(x) * z * pow(NQCD, -1)) + 3. / 4. * ln(x) * z * NQCD + 1. / 3. * ln(x) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(x) * pow(z, 2) * NQCD) + 1. / 6. * ln(x) * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * ln(x) * x * pow(z, -1) * NQCD) + 3. / 4. * ln(x) * x * pow(NQCD, -1) + (- 3. / 4. * ln(x) * x * NQCD) + (- 1. / 4. * ln(x) * x * z * pow(NQCD, -1)) + 1. / 4. * ln(x) * x * z * NQCD + (- 2. / 3. * ln(x) * x * pow(z, 2) * pow(NQCD, -1)) +  + 2. / 3. * ln(x) * x * pow(z, 2) * NQCD + 1. / 2. * ln(x) * ln(z) * pow(NQCD, -1) + (- 1. / 2. * ln(x) * ln(z) * NQCD) + 1. / 2. * ln(x) * ln(z) * x * pow(NQCD, -1) + (- 1. / 2. * ln(x) * ln(z) * x * NQCD) + ln(x) * ln(z) * x * z * pow(NQCD, -1) + (- ln(x) * ln(z) * x * z * NQCD) + (- 1. / 12. * ln(z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(z) * pow(z, -1) * NQCD + (- 3. / 8. * ln(z) * pow(NQCD, -1)) + 3. / 8. * ln(z) * NQCD + (- 1. / 8. * ln(z) * z * pow(NQCD, -1)) + 1. / 8. * ln(z) * z * NQCD + (- 1. / 6. * ln(z) * pow(z, 2) * pow(NQCD, -1)) + 1. / 6. * ln(z) * pow(z, 2) * NQCD + (- 1. / 12. * ln(z) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * ln(z) * x * pow(z, -1) * NQCD + (- 1. / 8. * ln(z) * x * pow(NQCD, -1)) + 1. / 8. * ln(z) * x * NQCD + 7. / 8. * ln(z) * x * z * pow(NQCD, -1) + (- 7. / 8. * ln(z) * x * z * NQCD) + 1. / 3. * ln(z) * x * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * ln(z) * x * pow(z, 2) * NQCD) + (- 1. / 4. * ln(z) * ln(1 - x) * pow(NQCD, -1)) + 1. / 4. * ln(z) * ln(1 - x) * NQCD + (- 1. / 4. * ln(z) * ln(1 - x) * x * pow(NQCD, -1)) + 1. / 4. * ln(z) * ln(1 - x) * x * NQCD + (- 1. / 2. * ln(z) * ln(1 - x) * x * z * pow(NQCD, -1)) + 1. / 2. * ln(z) * ln(1 - x) * x * z * NQCD + (- 1. / 4. * pow(ln(z), 2) * pow(NQCD, -1)) + 1. / 4. * pow(ln(z), 2) * NQCD + (- 1. / 4. * pow(ln(z), 2) * x * pow(NQCD, -1)) + 1. / 4. * pow(ln(z), 2) * x * NQCD + (- 1. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, -1)) + 1. / 2. * pow(ln(z), 2) * x * z * NQCD + 1. / 4. * Li2(z) * pow(NQCD, -1) + (- 1. / 4. * Li2(z) * NQCD) +  + 1. / 4. * Li2(z) * x * pow(NQCD, -1) + (- 1. / 4. * Li2(z) * x * NQCD) + 1. / 2. * Li2(z) * x * z * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * x * z * NQCD) + (- 1. / 3. / (1 - x) * ln(x) * pow(z, -1) * pow(NQCD, -1)) + 1. / 3. / (1 - x) * ln(x) * pow(z, -1) * NQCD + (- 5. / 8. / (1 - x) * ln(x) * pow(NQCD, -1)) + 5. / 8. / (1 - x) * ln(x) * NQCD + 5. / 8. / (1 - x) * ln(x) * z * pow(NQCD, -1) + (- 5. / 8. / (1 - x) * ln(x) * z * NQCD) + 1. / 3. / (1 - x) * ln(x) * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. / (1 - x) * ln(x) * pow(z, 2) * NQCD) + (- 3. / 4. / (1 - x) * ln(x) * ln(z) * pow(NQCD, -1)) + 3. / 4. / (1 - x) * ln(x) * ln(z) * NQCD + (- 3. / 4. / (1 - x) * ln(x) * ln(z) * z * pow(NQCD, -1)) + 3. / 4. / (1 - x) * ln(x) * ln(z) * z * NQCD;
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
        tmp = 1. / 6. * lmua * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * lmua * pow(z, -1) * NQCD) + 1. / 4. * lmua * pow(NQCD, -1) + (- 1. / 4. * lmua * NQCD) + (- 3. / 4. * lmua * z * pow(NQCD, -1)) + 3. / 4. * lmua * z * NQCD + 1. / 3. * lmua * pow(z, 2) * pow(NQCD, -1) + (- 1. / 3. * lmua * pow(z, 2) * NQCD) + 1. / 6. * lmua * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 6. * lmua * x * pow(z, -1) * NQCD) + 3. / 4. * lmua * x * pow(NQCD, -1) + (- 3. / 4. * lmua * x * NQCD) + (- 1. / 4. * lmua * x * z * pow(NQCD, -1)) + 1. / 4. * lmua * x * z * NQCD + (- 2. / 3. * lmua * x * pow(z, 2) * pow(NQCD, -1)) + 2. / 3. * lmua * x * pow(z, 2) * NQCD + 1. / 2. * ln(z) * lmua * pow(NQCD, -1) + (- 1. / 2. * ln(z) * lmua * NQCD) + 1. / 2. * ln(z) * lmua * x * pow(NQCD, -1) + (- 1. / 2. * ln(z) * lmua * x * NQCD) + ln(z) * lmua * x * z * pow(NQCD, -1) + (- ln(z) * lmua * x * z * NQCD);
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
