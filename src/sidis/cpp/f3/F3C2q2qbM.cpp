#include "../sidis.h"



/* Helpers */

double DL_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = 1. / 4. * CF * pow(NQCD, -1) + (- 2. / 3. * CF * pow(NQCD, -1) * pow(rln2, 3)) + (- 1. / 4. * z * CF * pow(NQCD, -1)) + 2. / 3. * z * CF * pow(NQCD, -1) * pow(rln2, 3) + (- 1. / 12. * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 3. * pow(pi, 2) * CF * pow(NQCD, -1) * rln2 + (- 1. / 12. * pow(pi, 2) * z * CF * pow(NQCD, -1)) + (- 1. / 3. * pow(pi, 2) * z * CF * pow(NQCD, -1) * rln2) + (- 2 * ln(1 - z) * CF * pow(NQCD, -1)) + ln(1 - z) * CF * pow(NQCD, -1) * pow(rln2, 2) + 2 * ln(1 - z) * z * CF * pow(NQCD, -1) + (- ln(1 - z) * z * CF * pow(NQCD, -1) * pow(rln2, 2)) + (- 1. / 6. * ln(1 - z) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 6. * ln(1 - z) * pow(pi, 2) * z * CF * pow(NQCD, -1) + (- 2 * ln(1 - z) * ln(1 + z) * CF * pow(NQCD, -1) * rln2) + 2 * ln(1 - z) * ln(1 + z) * z * CF * pow(NQCD, -1) * rln2 + ln(1 - z) * pow(ln(1 + z), 2) * CF * pow(NQCD, -1) + (- ln(1 - z) * pow(ln(1 + z), 2) * z * CF * pow(NQCD, -1)) + (- 2 * ln(1 - z) * Li2(-z) * CF * pow(NQCD, -1)) + 2 * ln(1 - z) * Li2(-z) * z * CF * pow(NQCD, -1) + ln(1 + z) * CF * pow(NQCD, -1) * pow(rln2, 2) + (- ln(1 + z) * z * CF * pow(NQCD, -1) * pow(rln2, 2)) + (- 1. / 2. * ln(1 + z) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 2. * ln(1 + z) * pow(pi, 2) * z * CF * pow(NQCD, -1) + (- 7. / 4. * ln(z) * CF * pow(NQCD, -1)) + 1. / 4. * ln(z) * z * CF * pow(NQCD, -1) + (- 2 * ln(z) * ln(1 - z) * ln(1 + z) * CF * pow(NQCD, -1)) + 2 * ln(z) * ln(1 - z) * ln(1 + z) * z * CF * pow(NQCD, -1) +  + ln(z) * ln(1 + z) * CF * pow(NQCD, -1) + ln(z) * ln(1 + z) * z * CF * pow(NQCD, -1) + (- pow(ln(z), 2) * CF * pow(NQCD, -1)) + (- pow(ln(z), 2) * z * CF * pow(NQCD, -1)) + (- 3. / 2. * pow(ln(z), 2) * ln(1 + z) * CF * pow(NQCD, -1)) + 3. / 2. * pow(ln(z), 2) * ln(1 + z) * z * CF * pow(NQCD, -1) + 5. / 12. * pow(ln(z), 3) * CF * pow(NQCD, -1) + (- 5. / 12. * pow(ln(z), 3) * z * CF * pow(NQCD, -1)) + (- ln(z) * Li2(-z) * CF * pow(NQCD, -1)) + ln(z) * Li2(-z) * z * CF * pow(NQCD, -1) + 2 * Li3(1. / 2. - 1. / 2. * z) * CF * pow(NQCD, -1) + (- 2 * Li3(1. / 2. - 1. / 2. * z) * z * CF * pow(NQCD, -1)) + 2 * Li3(1. / 2. + 1. / 2. * z) * CF * pow(NQCD, -1) + (- 2 * Li3(1. / 2. + 1. / 2. * z) * z * CF * pow(NQCD, -1)) + (- 2 * Li3(1 - z) * CF * pow(NQCD, -1)) + 2 * Li3(1 - z) * z * CF * pow(NQCD, -1) + (- Li3(-z) * CF * pow(NQCD, -1)) + Li3(-z) * z * CF * pow(NQCD, -1) + (- 2 * Li3(1 / (1 + z)) * CF * pow(NQCD, -1)) + 2 * Li3(1 / (1 + z)) * z * CF * pow(NQCD, -1) + 2 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * CF * pow(NQCD, -1) + (- 2 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * z * CF * pow(NQCD, -1)) + (- Li3(z) * CF * pow(NQCD, -1)) + Li3(z) * z * CF * pow(NQCD, -1) + Li2(-z) * CF * pow(NQCD, -1) + Li2(-z) * z * CF * pow(NQCD, -1) + Li2(z) * CF * pow(NQCD, -1) + Li2(z) * z * CF * pow(NQCD, -1) + 4. / 3. / (1 + z) * CF * pow(NQCD, -1) * pow(rln2, 3) + (- 2. / 3. / (1 + z) * pow(pi, 2) * CF * pow(NQCD, -1) * rln2) +  + (-2 / (1 + z) * ln(1 - z) * CF * pow(NQCD, -1) * pow(rln2, 2)) + 1. / 3. / (1 + z) * ln(1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + 4 / (1 + z) * ln(1 - z) * ln(1 + z) * CF * pow(NQCD, -1) * rln2 + (- 2 / (1 + z) * ln(1 - z) * pow(ln(1 + z), 2) * CF * pow(NQCD, -1)) + 4 / (1 + z) * ln(1 - z) * Li2(-z) * CF * pow(NQCD, -1) + (- 2 / (1 + z) * ln(1 + z) * CF * pow(NQCD, -1) * pow(rln2, 2)) + 1 / (1 + z) * ln(1 + z) * pow(pi, 2) * CF * pow(NQCD, -1) + 4 / (1 + z) * ln(z) * ln(1 - z) * ln(1 + z) * CF * pow(NQCD, -1) + 3 / (1 + z) * pow(ln(z), 2) * ln(1 + z) * CF * pow(NQCD, -1) + (- 5. / 6. / (1 + z) * pow(ln(z), 3) * CF * pow(NQCD, -1)) + 2 / (1 + z) * ln(z) * Li2(-z) * CF * pow(NQCD, -1) + (- 4 / (1 + z) * Li3(1. / 2. - 1. / 2. * z) * CF * pow(NQCD, -1)) + (- 4 / (1 + z) * Li3(1. / 2. + 1. / 2. * z) * CF * pow(NQCD, -1)) + 4 / (1 + z) * Li3(1 - z) * CF * pow(NQCD, -1) + 2 / (1 + z) * Li3(-z) * CF * pow(NQCD, -1) + 4 / (1 + z) * Li3(1 / (1 + z)) * CF * pow(NQCD, -1) + (- 4 / (1 + z) * Li3(1 / (1 + z) - 1 / (1 + z) * z) * CF * pow(NQCD, -1)) + 2 / (1 + z) * Li3(z) * CF * pow(NQCD, -1);
    return res;
}

double DL_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = 4 * lmua * CF * pow(NQCD, -1) + (- 4 * lmua * z * CF * pow(NQCD, -1)) + 1. / 3. * lmua * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 3. * lmua * pow(pi, 2) * z * CF * pow(NQCD, -1)) + 4 * lmua * Li2(-z) * CF * pow(NQCD, -1) + (- 4 * lmua * Li2(-z) * z * CF * pow(NQCD, -1)) + 2 * ln(z) * lmua * CF * pow(NQCD, -1) + 2 * ln(z) * lmua * z * CF * pow(NQCD, -1) + 4 * ln(z) * lmua * ln(1 + z) * CF * pow(NQCD, -1) + (- 4 * ln(z) * lmua * ln(1 + z) * z * CF * pow(NQCD, -1)) + (- pow(ln(z), 2) * lmua * CF * pow(NQCD, -1)) + pow(ln(z), 2) * lmua * z * CF * pow(NQCD, -1) + (- 2. / 3. / (1 + z) * lmua * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 8 / (1 + z) * lmua * Li2(-z) * CF * pow(NQCD, -1)) + (- 8 / (1 + z) * ln(z) * lmua * ln(1 + z) * CF * pow(NQCD, -1)) + 2 / (1 + z) * pow(ln(z), 2) * lmua * CF * pow(NQCD, -1);
    return res;
}

double D0_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-2 * CF * pow(NQCD, -1)) + 2 * z * CF * pow(NQCD, -1) + (- 1. / 6. * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 6. * pow(pi, 2) * z * CF * pow(NQCD, -1) + (- ln(z) * CF * pow(NQCD, -1)) + (- ln(z) * z * CF * pow(NQCD, -1)) + (- 2 * ln(z) * ln(1 + z) * CF * pow(NQCD, -1)) + 2 * ln(z) * ln(1 + z) * z * CF * pow(NQCD, -1) + 1. / 2. * pow(ln(z), 2) * CF * pow(NQCD, -1) + (- 1. / 2. * pow(ln(z), 2) * z * CF * pow(NQCD, -1)) + (- 2 * Li2(-z) * CF * pow(NQCD, -1)) + 2 * Li2(-z) * z * CF * pow(NQCD, -1) + 1. / 3. / (1 + z) * pow(pi, 2) * CF * pow(NQCD, -1) + 4 / (1 + z) * ln(z) * ln(1 + z) * CF * pow(NQCD, -1) + (- 1 / (1 + z) * pow(ln(z), 2) * CF * pow(NQCD, -1)) + 4 / (1 + z) * Li2(-z) * CF * pow(NQCD, -1);
    return res;
}

double RG_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = 15. / 4. * CF * pow(NQCD, -1) + 2. / 3. * CF * pow(NQCD, -1) * pow(rln2, 3) + (- 15. / 4. * x * CF * pow(NQCD, -1)) + (- 2. / 3. * x * CF * pow(NQCD, -1) * pow(rln2, 3)) + zeta3 * CF * pow(NQCD, -1) + (- zeta3 * x * CF * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 3. * pow(pi, 2) * CF * pow(NQCD, -1) * rln2) + 1. / 12. * pow(pi, 2) * x * CF * pow(NQCD, -1) + 1. / 3. * pow(pi, 2) * x * CF * pow(NQCD, -1) * rln2 + 2 * ln(1 - x) * CF * pow(NQCD, -1) + (- ln(1 - x) * CF * pow(NQCD, -1) * pow(rln2, 2)) + (- 2 * ln(1 - x) * x * CF * pow(NQCD, -1)) + ln(1 - x) * x * CF * pow(NQCD, -1) * pow(rln2, 2) + 1. / 6. * ln(1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 6. * ln(1 - x) * pow(pi, 2) * x * CF * pow(NQCD, -1)) + 2 * ln(1 - x) * ln(1 + x) * CF * pow(NQCD, -1) * rln2 + (- 2 * ln(1 - x) * ln(1 + x) * x * CF * pow(NQCD, -1) * rln2) + (- ln(1 - x) * pow(ln(1 + x), 2) * CF * pow(NQCD, -1)) + ln(1 - x) * pow(ln(1 + x), 2) * x * CF * pow(NQCD, -1) + 2 * ln(1 - x) * Li2(-x) * CF * pow(NQCD, -1) + (- 2 * ln(1 - x) * Li2(-x) * x * CF * pow(NQCD, -1)) + (- ln(1 + x) * CF * pow(NQCD, -1) * pow(rln2, 2)) + ln(1 + x) * x * CF * pow(NQCD, -1) * pow(rln2, 2) + 1. / 3. * ln(1 + x) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 3. * ln(1 + x) * pow(pi, 2) * x * CF * pow(NQCD, -1)) + 1. / 3. * pow(ln(1 + x), 3) * CF * pow(NQCD, -1) + (- 1. / 3. * pow(ln(1 + x), 3) * x * CF * pow(NQCD, -1)) + 3. / 4. * ln(x) * CF * pow(NQCD, -1) +  + 19. / 4. * ln(x) * x * CF * pow(NQCD, -1) + (- 1. / 3. * ln(x) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 3. * ln(x) * pow(pi, 2) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(1 - x) * ln(1 + x) * CF * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 - x) * ln(1 + x) * x * CF * pow(NQCD, -1)) + (- ln(x) * ln(1 + x) * CF * pow(NQCD, -1)) + (- ln(x) * ln(1 + x) * x * CF * pow(NQCD, -1)) + (- pow(ln(x), 2) * x * CF * pow(NQCD, -1)) + (- 2 * pow(ln(x), 2) * ln(1 + x) * CF * pow(NQCD, -1)) + 2 * pow(ln(x), 2) * ln(1 + x) * x * CF * pow(NQCD, -1) + 1. / 4. * pow(ln(x), 3) * CF * pow(NQCD, -1) + (- 1. / 4. * pow(ln(x), 3) * x * CF * pow(NQCD, -1)) + (- 2 * ln(x) * Li2(-x) * CF * pow(NQCD, -1)) + 2 * ln(x) * Li2(-x) * x * CF * pow(NQCD, -1) + (- 2 * Li3(1. / 2. - 1. / 2. * x) * CF * pow(NQCD, -1)) + 2 * Li3(1. / 2. - 1. / 2. * x) * x * CF * pow(NQCD, -1) + (- 2 * Li3(1. / 2. + 1. / 2. * x) * CF * pow(NQCD, -1)) + 2 * Li3(1. / 2. + 1. / 2. * x) * x * CF * pow(NQCD, -1) + 2 * Li3(1 - x) * CF * pow(NQCD, -1) + (- 2 * Li3(1 - x) * x * CF * pow(NQCD, -1)) + (- 2 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * CF * pow(NQCD, -1)) + 2 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * x * CF * pow(NQCD, -1) + Li3(x) * CF * pow(NQCD, -1) + (- Li3(x) * x * CF * pow(NQCD, -1)) + (- Li2(-x) * CF * pow(NQCD, -1)) + (- Li2(-x) * x * CF * pow(NQCD, -1)) + (- Li2(x) * CF * pow(NQCD, -1)) + (- Li2(x) * x * CF * pow(NQCD, -1)) + (- 4. / 3. / (1 + x) * CF * pow(NQCD, -1) * pow(rln2, 3)) +  + (-2 / (1 + x) * zeta3 * CF * pow(NQCD, -1)) + 2. / 3. / (1 + x) * pow(pi, 2) * CF * pow(NQCD, -1) * rln2 + 2 / (1 + x) * ln(1 - x) * CF * pow(NQCD, -1) * pow(rln2, 2) + (- 1. / 3. / (1 + x) * ln(1 - x) * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 4 / (1 + x) * ln(1 - x) * ln(1 + x) * CF * pow(NQCD, -1) * rln2) + 2 / (1 + x) * ln(1 - x) * pow(ln(1 + x), 2) * CF * pow(NQCD, -1) + (- 4 / (1 + x) * ln(1 - x) * Li2(-x) * CF * pow(NQCD, -1)) + 2 / (1 + x) * ln(1 + x) * CF * pow(NQCD, -1) * pow(rln2, 2) + (- 2. / 3. / (1 + x) * ln(1 + x) * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 2. / 3. / (1 + x) * pow(ln(1 + x), 3) * CF * pow(NQCD, -1)) + 2. / 3. / (1 + x) * ln(x) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 4 / (1 + x) * ln(x) * ln(1 - x) * ln(1 + x) * CF * pow(NQCD, -1)) + 4 / (1 + x) * pow(ln(x), 2) * ln(1 + x) * CF * pow(NQCD, -1) + (- 1. / 2. / (1 + x) * pow(ln(x), 3) * CF * pow(NQCD, -1)) + 4 / (1 + x) * ln(x) * Li2(-x) * CF * pow(NQCD, -1) + 4 / (1 + x) * Li3(1. / 2. - 1. / 2. * x) * CF * pow(NQCD, -1) + 4 / (1 + x) * Li3(1. / 2. + 1. / 2. * x) * CF * pow(NQCD, -1) + (- 4 / (1 + x) * Li3(1 - x) * CF * pow(NQCD, -1)) + 4 / (1 + x) * Li3(1 / (1 + x) - 1 / (1 + x) * x) * CF * pow(NQCD, -1) + (- 2 / (1 + x) * Li3(x) * CF * pow(NQCD, -1));
    return res;
}

double RG_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 4 * lmuf * CF * pow(NQCD, -1)) + 4 * lmuf * x * CF * pow(NQCD, -1) + (- 1. / 3. * lmuf * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 3. * lmuf * pow(pi, 2) * x * CF * pow(NQCD, -1) + (- 4 * lmuf * Li2(-x) * CF * pow(NQCD, -1)) + 4 * lmuf * Li2(-x) * x * CF * pow(NQCD, -1) + (- 2 * ln(x) * lmuf * CF * pow(NQCD, -1)) + (- 2 * ln(x) * lmuf * x * CF * pow(NQCD, -1)) + (- 4 * ln(x) * lmuf * ln(1 + x) * CF * pow(NQCD, -1)) + 4 * ln(x) * lmuf * ln(1 + x) * x * CF * pow(NQCD, -1) + pow(ln(x), 2) * lmuf * CF * pow(NQCD, -1) + (- pow(ln(x), 2) * lmuf * x * CF * pow(NQCD, -1)) + 2. / 3. / (1 + x) * lmuf * pow(pi, 2) * CF * pow(NQCD, -1) + 8 / (1 + x) * lmuf * Li2(-x) * CF * pow(NQCD, -1) + 8 / (1 + x) * ln(x) * lmuf * ln(1 + x) * CF * pow(NQCD, -1) + (- 2 / (1 + x) * pow(ln(x), 2) * lmuf * CF * pow(NQCD, -1));
    return res;
}

double RG_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = 2 * CF * pow(NQCD, -1) + (- 2 * x * CF * pow(NQCD, -1)) + 1. / 6. * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 6. * pow(pi, 2) * x * CF * pow(NQCD, -1)) + ln(x) * CF * pow(NQCD, -1) + ln(x) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(1 + x) * CF * pow(NQCD, -1) + (- 2 * ln(x) * ln(1 + x) * x * CF * pow(NQCD, -1)) + (- 1. / 2. * pow(ln(x), 2) * CF * pow(NQCD, -1)) + 1. / 2. * pow(ln(x), 2) * x * CF * pow(NQCD, -1) + 2 * Li2(-x) * CF * pow(NQCD, -1) + (- 2 * Li2(-x) * x * CF * pow(NQCD, -1)) + (- 1. / 3. / (1 + x) * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 4 / (1 + x) * ln(x) * ln(1 + x) * CF * pow(NQCD, -1)) + 1 / (1 + x) * pow(ln(x), 2) * CF * pow(NQCD, -1) + (- 4 / (1 + x) * Li2(-x) * CF * pow(NQCD, -1));
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
        tmp = (-4 * CF * pow(NQCD, -1)) + (- 8 * CF * pow(NQCD, -1) * pow(rln2, 2)) + 8 * z * CF * pow(NQCD, -1) * pow(rln2, 2) + 4 * x * CF * pow(NQCD, -1) + (- 1. / 3. * pow(pi, 2) * z * CF * pow(NQCD, -1)) + 1. / 3. * pow(pi, 2) * x * CF * pow(NQCD, -1) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2 + (- 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) * rln2) + (- 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 8 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) + 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2 + (- 8 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) * rln2) + (- 2 * ln(x) * CF * pow(NQCD, -1)) + (- 4 * ln(x) * CF * pow(NQCD, -1) * rln2) + 4 * ln(x) * z * CF * pow(NQCD, -1) * rln2 + (- 2 * ln(x) * x * CF * pow(NQCD, -1)) + 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1)) + 4 * ln(x) * ln(1 + x) * CF * pow(NQCD, -1) + 4 * ln(x) * ln(1 + x) * x * CF * pow(NQCD, -1) + (- 4 * ln(x) * ln(1 + x * z) * CF * pow(NQCD, -1)) + (- 4 * ln(x) * ln(z + x) * z * CF * pow(NQCD, -1)) + pow(ln(x), 2) * z * CF * pow(NQCD, -1) + (- pow(ln(x), 2) * x * CF * pow(NQCD, -1)) + 6 * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + (- 2 * ln(x) * ln(z) * x * CF * pow(NQCD, -1)) + (- 3 * ln(z) * CF * pow(NQCD, -1)) + (- 12 * ln(z) * CF * pow(NQCD, -1) * rln2) + 12 * ln(z) * z * CF * pow(NQCD, -1) * rln2 + 3 * ln(z) * x * CF * pow(NQCD, -1) + 4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) +  + (-4 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1)) + 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 8 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1)) + (- 4 * ln(z) * ln(1 + x * z) * CF * pow(NQCD, -1)) + 4 * ln(z) * ln(z + x) * z * CF * pow(NQCD, -1) + (- 3 * pow(ln(z), 2) * CF * pow(NQCD, -1)) + pow(ln(z), 2) * z * CF * pow(NQCD, -1) + (- 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1)) + 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF * pow(NQCD, -1) + 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1) + (- 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF * pow(NQCD, -1)) + 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 4 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1)) + (- 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 4 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) + (- 4 * Li2(-x * pow(z, -1)) * z * CF * pow(NQCD, -1)) + 4 * Li2(-x) * CF * pow(NQCD, -1) + 4 * Li2(-x) * x * CF * pow(NQCD, -1) + (- 4 * Li2(-x * z) * CF * pow(NQCD, -1)) + (- 4 / (1 - z) * ln(x) * ln(1 + x) * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(x) * ln(1 + x * z) * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(x) * ln(z + x) * CF * pow(NQCD, -1) +  + (-3 / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1)) + 1 / (1 - z) * ln(x) * ln(z) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(z) * CF * pow(NQCD, -1) + (- 1 / (1 - z) * ln(z) * x * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(z) * ln(1 + x * z) * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * ln(z + x) * CF * pow(NQCD, -1)) + 1 / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) + 2 / (1 - z) * Li2(-x * pow(z, -1)) * CF * pow(NQCD, -1) + (- 4 / (1 - z) * Li2(-x) * CF * pow(NQCD, -1)) + 2 / (1 - z) * Li2(-x * z) * CF * pow(NQCD, -1) + 4 / (1 - z) / (1 + x) * ln(x) * ln(1 + x) * CF * pow(NQCD, -1) + (- 2 / (1 - z) / (1 + x) * ln(x) * ln(1 + x * z) * CF * pow(NQCD, -1)) + (- 2 / (1 - z) / (1 + x) * ln(x) * ln(z + x) * CF * pow(NQCD, -1)) + 4 / (1 - z) / (1 + x) * ln(x) * ln(z) * CF * pow(NQCD, -1) + (- 2 / (1 - z) / (1 + x) * ln(z) * ln(1 + x * z) * CF * pow(NQCD, -1)) + 2 / (1 - z) / (1 + x) * ln(z) * ln(z + x) * CF * pow(NQCD, -1) + (- 1 / (1 - z) / (1 + x) * pow(ln(z), 2) * CF * pow(NQCD, -1)) + (- 2 / (1 - z) / (1 + x) * Li2(-x * pow(z, -1)) * CF * pow(NQCD, -1)) + 4 / (1 - z) / (1 + x) * Li2(-x) * CF * pow(NQCD, -1) + (- 2 / (1 - z) / (1 + x) * Li2(-x * z) * CF * pow(NQCD, -1)) + 8 / (1 + z) * CF * pow(NQCD, -1) * pow(rln2, 2) + (- 8 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2) + 8 / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 8 / (1 + z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2) + 4 / (1 + z) * ln(x) * CF * pow(NQCD, -1) * rln2 + (- 4 / (1 + z) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 2 / (1 + z) * ln(x) * ln(1 + x * z) * CF * pow(NQCD, -1) +  + (-2 / (1 + z) * ln(x) * ln(z + x) * CF * pow(NQCD, -1)) + 2 / (1 + z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 12 / (1 + z) * ln(z) * CF * pow(NQCD, -1) * rln2 + (- 4 / (1 + z) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + (- 8 / (1 + z) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 2 / (1 + z) * ln(z) * ln(1 + x * z) * CF * pow(NQCD, -1) + 2 / (1 + z) * ln(z) * ln(z + x) * CF * pow(NQCD, -1) + 2 / (1 + z) * pow(ln(z), 2) * CF * pow(NQCD, -1) + 4 / (1 + z) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1) + (- 4 / (1 + z) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1)) + (- 4 / (1 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 4 / (1 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 2 / (1 + z) * Li2(-x * pow(z, -1)) * CF * pow(NQCD, -1)) + 2 / (1 + z) * Li2(-x * z) * CF * pow(NQCD, -1) + 6 / (1 - x) * CF * pow(NQCD, -1) * pow(rln2, 2) + (- 6 / (1 - x) * z * CF * pow(NQCD, -1) * pow(rln2, 2)) + 1. / 6. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 6. / (1 - x) * pow(pi, 2) * z * CF * pow(NQCD, -1)) + (- 6 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2) + 6 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) * rln2 + 6 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 6 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1)) +  + 2 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NQCD, -1) + (- 6 / (1 - x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2) + 6 / (1 - x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) * rln2 + 1 / (1 - x) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(x) * CF * pow(NQCD, -1) * rln2 + (- 1 / (1 - x) * ln(x) * z * CF * pow(NQCD, -1)) + (- 3 / (1 - x) * ln(x) * z * CF * pow(NQCD, -1) * rln2) + (- 3 / (1 - x) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 3 / (1 - x) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(x) * ln(1 + x * z) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(x) * ln(1 + x * z) * z * CF * pow(NQCD, -1)) + (- 2 / (1 - x) * ln(x) * ln(z + x) * CF * pow(NQCD, -1)) + 2 / (1 - x) * ln(x) * ln(z + x) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(x) * ln(z) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(x) * ln(z) * z * CF * pow(NQCD, -1)) + (- 1 / (1 - x) * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NQCD, -1)) + 1 / (1 - x) * ln(z) * CF * pow(NQCD, -1) + 9 / (1 - x) * ln(z) * CF * pow(NQCD, -1) * rln2 + 1 / (1 - x) * ln(z) * z * CF * pow(NQCD, -1) + (- 9 / (1 - x) * ln(z) * z * CF * pow(NQCD, -1) * rln2) + (- 3 / (1 - x) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 3 / (1 - x) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(z) * ln(1 + z) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(z) * ln(1 + z) * z * CF * pow(NQCD, -1)) + (- 6 / (1 - x) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) +  + 6 / (1 - x) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(z) * ln(1 + x * z) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(z) * ln(1 + x * z) * z * CF * pow(NQCD, -1)) + 2 / (1 - x) * ln(z) * ln(z + x) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(z) * ln(z + x) * z * CF * pow(NQCD, -1)) + 1. / 2. / (1 - x) * pow(ln(z), 2) * CF * pow(NQCD, -1) + (- 1. / 2. / (1 - x) * pow(ln(z), 2) * z * CF * pow(NQCD, -1)) + (- 1 / (1 - x) * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NQCD, -1)) + 3 / (1 - x) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1) + (- 3 / (1 - x) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF * pow(NQCD, -1)) + (- 3 / (1 - x) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1)) + 3 / (1 - x) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF * pow(NQCD, -1) + (- 3 / (1 - x) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 3 / (1 - x) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1) + 3 / (1 - x) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 3 / (1 - x) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * pow(NQCD, -1)) + 2 / (1 - x) * Li2(-z) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * Li2(-z) * z * CF * pow(NQCD, -1)) + (- 2 / (1 - x) * Li2(-x * pow(z, -1)) * CF * pow(NQCD, -1)) + 2 / (1 - x) * Li2(-x * pow(z, -1)) * z * CF * pow(NQCD, -1) +  + 2 / (1 - x) * Li2(-x * z) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * Li2(-x * z) * z * CF * pow(NQCD, -1)) + (- 2 / (1 - x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NQCD, -1) * rln2) + (- 8 / (1 - x) / (1 + z) * CF * pow(NQCD, -1) * pow(rln2, 2)) + (- 1. / 3. / (1 - x) / (1 + z) * pow(pi, 2) * CF * pow(NQCD, -1)) + 8 / (1 - x) / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2 + (- 8 / (1 - x) / (1 + z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + 8 / (1 - x) / (1 + z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) * rln2 + (- 4 / (1 - x) / (1 + z) * ln(x) * CF * pow(NQCD, -1) * rln2) + 4 / (1 - x) / (1 + z) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 2 / (1 - x) / (1 + z) * ln(x) * ln(1 + x * z) * CF * pow(NQCD, -1)) + 2 / (1 - x) / (1 + z) * ln(x) * ln(z + x) * CF * pow(NQCD, -1) + (- 2 / (1 - x) / (1 + z) * ln(x) * ln(z) * CF * pow(NQCD, -1)) + (- 12 / (1 - x) / (1 + z) * ln(z) * CF * pow(NQCD, -1) * rln2) + 4 / (1 - x) / (1 + z) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 4 / (1 - x) / (1 + z) * ln(z) * ln(1 + z) * CF * pow(NQCD, -1)) + 8 / (1 - x) / (1 + z) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 2 / (1 - x) / (1 + z) * ln(z) * ln(1 + x * z) * CF * pow(NQCD, -1)) + (- 2 / (1 - x) / (1 + z) * ln(z) * ln(z + x) * CF * pow(NQCD, -1)) + (- 1 / (1 - x) / (1 + z) * pow(ln(z), 2) * CF * pow(NQCD, -1)) + (- 4 / (1 - x) / (1 + z) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1)) +  + 4 / (1 - x) / (1 + z) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF * pow(NQCD, -1) + 4 / (1 - x) / (1 + z) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1) + (- 4 / (1 - x) / (1 + z) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * pow(NQCD, -1)) + (- 4 / (1 - x) / (1 + z) * Li2(-z) * CF * pow(NQCD, -1)) + 2 / (1 - x) / (1 + z) * Li2(-x * pow(z, -1)) * CF * pow(NQCD, -1) + (- 2 / (1 - x) / (1 + z) * Li2(-x * z) * CF * pow(NQCD, -1)) + 1. / 3. / (1 + x) * pow(pi, 2) * CF * pow(NQCD, -1) + 1. / 3. / (1 + x) * pow(pi, 2) * z * CF * pow(NQCD, -1) + 2 / (1 + x) * ln(x) * ln(1 + x * z) * CF * pow(NQCD, -1) + 2 / (1 + x) * ln(x) * ln(1 + x * z) * z * CF * pow(NQCD, -1) + 2 / (1 + x) * ln(x) * ln(z + x) * CF * pow(NQCD, -1) + 2 / (1 + x) * ln(x) * ln(z + x) * z * CF * pow(NQCD, -1) + (- 1 / (1 + x) * pow(ln(x), 2) * CF * pow(NQCD, -1)) + (- 1 / (1 + x) * pow(ln(x), 2) * z * CF * pow(NQCD, -1)) + (- 4 / (1 + x) * ln(x) * ln(z) * CF * pow(NQCD, -1)) + (- 4 / (1 + x) * ln(x) * ln(z) * z * CF * pow(NQCD, -1)) + 2 / (1 + x) * ln(z) * ln(1 + x * z) * CF * pow(NQCD, -1) + 2 / (1 + x) * ln(z) * ln(1 + x * z) * z * CF * pow(NQCD, -1) + (- 2 / (1 + x) * ln(z) * ln(z + x) * CF * pow(NQCD, -1)) + (- 2 / (1 + x) * ln(z) * ln(z + x) * z * CF * pow(NQCD, -1)) + 1 / (1 + x) * pow(ln(z), 2) * CF * pow(NQCD, -1) + 1 / (1 + x) * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 2 / (1 + x) * Li2(-x * pow(z, -1)) * CF * pow(NQCD, -1) + 2 / (1 + x) * Li2(-x * pow(z, -1)) * z * CF * pow(NQCD, -1) + 2 / (1 + x) * Li2(-x * z) * CF * pow(NQCD, -1) + 2 / (1 + x) * Li2(-x * z) * z * CF * pow(NQCD, -1);
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - D0_RG: 000
  - DL_RG: 000, 001
  - RG_D0: 000
  - RG_DL: 000, 010
  - RG_RG: 000
*/

/*
  Inverted Branch Report (By Number):
  - 000: D0_RG, DL_RG, RG_D0, RG_DL, RG_RG
  - 001: DL_RG
  - 010: RG_DL
*/
