#include "../sidis.h"



/* Helpers */

double RG_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-4 * pow(NQCD, -1)) + 4 * NQCD + 4 * x * pow(NQCD, -1) + (- 4 * x * NQCD) + 1. / 4. * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 4. * pow(pi, 2) * NQCD) + (- 1. / 4. * pow(pi, 2) * x * pow(NQCD, -1)) + 1. / 4. * pow(pi, 2) * x * NQCD + 3. / 2. * ln(1 - x) * pow(NQCD, -1) + (- 3. / 2. * ln(1 - x) * NQCD) + (- 3. / 2. * ln(1 - x) * x * pow(NQCD, -1)) + 3. / 2. * ln(1 - x) * x * NQCD + (- 1. / 6. * ln(1 - x) * pow(pi, 2) * pow(NQCD, -1)) + 1. / 6. * ln(1 - x) * pow(pi, 2) * NQCD + (- 1. / 6. * ln(1 - x) * pow(pi, 2) * x * pow(NQCD, -1)) + 1. / 6. * ln(1 - x) * pow(pi, 2) * x * NQCD + (- 5. / 8. * pow(ln(1 - x), 2) * pow(NQCD, -1)) + 5. / 8. * pow(ln(1 - x), 2) * NQCD + 5. / 8. * pow(ln(1 - x), 2) * x * pow(NQCD, -1) + (- 5. / 8. * pow(ln(1 - x), 2) * x * NQCD) + 1. / 2. * ln(1 - x) * Li2(1 - x) * pow(NQCD, -1) + (- 1. / 2. * ln(1 - x) * Li2(1 - x) * NQCD) + 1. / 2. * ln(1 - x) * Li2(1 - x) * x * pow(NQCD, -1) + (- 1. / 2. * ln(1 - x) * Li2(1 - x) * x * NQCD) + ln(1 - x) * Li2(x) * pow(NQCD, -1) + (- ln(1 - x) * Li2(x) * NQCD) + ln(1 - x) * Li2(x) * x * pow(NQCD, -1) + (- ln(1 - x) * Li2(x) * x * NQCD) +  + (- 19. / 8. * ln(x) * pow(NQCD, -1)) + 19. / 8. * ln(x) * NQCD + 1. / 8. * ln(x) * x * pow(NQCD, -1) + (- 1. / 8. * ln(x) * x * NQCD) + 1. / 6. * ln(x) * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 6. * ln(x) * pow(pi, 2) * NQCD) + 1. / 6. * ln(x) * pow(pi, 2) * x * pow(NQCD, -1) + (- 1. / 6. * ln(x) * pow(pi, 2) * x * NQCD) + 5. / 4. * ln(x) * ln(1 - x) * pow(NQCD, -1) + (- 5. / 4. * ln(x) * ln(1 - x) * NQCD) + (- 5. / 4. * ln(x) * ln(1 - x) * x * pow(NQCD, -1)) + 5. / 4. * ln(x) * ln(1 - x) * x * NQCD + 3. / 4. * ln(x) * pow(ln(1 - x), 2) * pow(NQCD, -1) + (- 3. / 4. * ln(x) * pow(ln(1 - x), 2) * NQCD) + 3. / 4. * ln(x) * pow(ln(1 - x), 2) * x * pow(NQCD, -1) + (- 3. / 4. * ln(x) * pow(ln(1 - x), 2) * x * NQCD) + (- 13. / 16. * pow(ln(x), 2) * pow(NQCD, -1)) + 13. / 16. * pow(ln(x), 2) * NQCD + 17. / 16. * pow(ln(x), 2) * x * pow(NQCD, -1) + (- 17. / 16. * pow(ln(x), 2) * x * NQCD) +  + (- 5. / 24. * pow(ln(x), 3) * pow(NQCD, -1)) + 5. / 24. * pow(ln(x), 3) * NQCD + (- 5. / 24. * pow(ln(x), 3) * x * pow(NQCD, -1)) + 5. / 24. * pow(ln(x), 3) * x * NQCD + (- 1. / 2. * ln(x) * Li2(x) * pow(NQCD, -1)) + 1. / 2. * ln(x) * Li2(x) * NQCD + (- 1. / 2. * ln(x) * Li2(x) * x * pow(NQCD, -1)) + 1. / 2. * ln(x) * Li2(x) * x * NQCD + 1. / 2. * Li3(1 - x) * pow(NQCD, -1) + (- 1. / 2. * Li3(1 - x) * NQCD) + 1. / 2. * Li3(1 - x) * x * pow(NQCD, -1) + (- 1. / 2. * Li3(1 - x) * x * NQCD) + (- 1. / 4. * Li2(x) * pow(NQCD, -1)) + 1. / 4. * Li2(x) * NQCD + 1. / 4. * Li2(x) * x * pow(NQCD, -1) + (- 1. / 4. * Li2(x) * x * NQCD);
    return res;
}

double RG_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 3 * lmuf * pow(NQCD, -1)) + 3 * lmuf * NQCD + 3 * lmuf * x * pow(NQCD, -1) + (- 3 * lmuf * x * NQCD) + 1. / 6. * lmuf * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 6. * lmuf * pow(pi, 2) * NQCD) + 1. / 6. * lmuf * pow(pi, 2) * x * pow(NQCD, -1) + (- 1. / 6. * lmuf * pow(pi, 2) * x * NQCD) + 5. / 2. * lmuf * ln(1 - x) * pow(NQCD, -1) + (- 5. / 2. * lmuf * ln(1 - x) * NQCD) + (- 5. / 2. * lmuf * ln(1 - x) * x * pow(NQCD, -1)) + 5. / 2. * lmuf * ln(1 - x) * x * NQCD + (- lmuf * Li2(x) * pow(NQCD, -1)) + lmuf * Li2(x) * NQCD + (- lmuf * Li2(x) * x * pow(NQCD, -1)) + lmuf * Li2(x) * x * NQCD + (- 3 * ln(x) * lmuf * pow(NQCD, -1)) + 3 * ln(x) * lmuf * NQCD + 3 * ln(x) * lmuf * x * pow(NQCD, -1) + (- 3 * ln(x) * lmuf * x * NQCD) + (- pow(ln(x), 2) * lmuf * pow(NQCD, -1)) + pow(ln(x), 2) * lmuf * NQCD + (- pow(ln(x), 2) * lmuf * x * pow(NQCD, -1)) + pow(ln(x), 2) * lmuf * x * NQCD;
    return res;
}

double RG_DL_020(double x, double z, double NF) {
    double res = 0.0;
    res = (- 5. / 2. * pow(lmuf, 2) * pow(NQCD, -1)) + 5. / 2. * pow(lmuf, 2) * NQCD + 5. / 2. * pow(lmuf, 2) * x * pow(NQCD, -1) + (- 5. / 2. * pow(lmuf, 2) * x * NQCD) + (- ln(x) * pow(lmuf, 2) * pow(NQCD, -1)) + ln(x) * pow(lmuf, 2) * NQCD + (- ln(x) * pow(lmuf, 2) * x * pow(NQCD, -1)) + ln(x) * pow(lmuf, 2) * x * NQCD;
    return res;
}

double RG_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = 3. / 2. * pow(NQCD, -1) + (- 3. / 2. * NQCD) + (- 3. / 2. * x * pow(NQCD, -1)) + 3. / 2. * x * NQCD + (- 1. / 12. * pow(pi, 2) * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * NQCD + (- 1. / 12. * pow(pi, 2) * x * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * x * NQCD + (- 5. / 4. * ln(1 - x) * pow(NQCD, -1)) + 5. / 4. * ln(1 - x) * NQCD + 5. / 4. * ln(1 - x) * x * pow(NQCD, -1) + (- 5. / 4. * ln(1 - x) * x * NQCD) + 3. / 2. * ln(x) * pow(NQCD, -1) + (- 3. / 2. * ln(x) * NQCD) + (- 3. / 2. * ln(x) * x * pow(NQCD, -1)) + 3. / 2. * ln(x) * x * NQCD + 1. / 2. * pow(ln(x), 2) * pow(NQCD, -1) + (- 1. / 2. * pow(ln(x), 2) * NQCD) + 1. / 2. * pow(ln(x), 2) * x * pow(NQCD, -1) + (- 1. / 2. * pow(ln(x), 2) * x * NQCD) + 1. / 2. * Li2(x) * pow(NQCD, -1) + (- 1. / 2. * Li2(x) * NQCD) + 1. / 2. * Li2(x) * x * pow(NQCD, -1) + (- 1. / 2. * Li2(x) * x * NQCD);
    return res;
}

double RG_D0_010(double x, double z, double NF) {
    double res = 0.0;
    res = 5. / 2. * lmuf * pow(NQCD, -1) + (- 5. / 2. * lmuf * NQCD) + (- 5. / 2. * lmuf * x * pow(NQCD, -1)) + 5. / 2. * lmuf * x * NQCD + ln(x) * lmuf * pow(NQCD, -1) + (- ln(x) * lmuf * NQCD) + ln(x) * lmuf * x * pow(NQCD, -1) + (- ln(x) * lmuf * x * NQCD);
    return res;
}

double RG_D1_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-5. / 4. * pow(NQCD, -1)) + 5. / 4. * NQCD + 5. / 4. * x * pow(NQCD, -1) + (- 5. / 4. * x * NQCD) + (- 1. / 2. * ln(x) * pow(NQCD, -1)) + 1. / 2. * ln(x) * NQCD + (- 1. / 2. * ln(x) * x * pow(NQCD, -1)) + 1. / 2. * ln(x) * x * NQCD;
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
        tmp = 3. / 2. * pow(z, -1) * pow(NQCD, -1) + (- 3. / 2. * pow(z, -1) * NQCD) + (- 5 * pow(NQCD, -1)) + 5 * NQCD + (- 3. / 2. * x * pow(z, -1) * pow(NQCD, -1)) + 3. / 2. * x * pow(z, -1) * NQCD + 5 * x * pow(NQCD, -1) + (- 5 * x * NQCD) + (- 1. / 12. * pow(pi, 2) * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * pow(z, -1) * NQCD + 1. / 6. * pow(pi, 2) * pow(NQCD, -1) + (- 1. / 6. * pow(pi, 2) * NQCD) + (- 1. / 12. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 12. * pow(pi, 2) * x * pow(z, -1) * NQCD + 1. / 6. * pow(pi, 2) * x * pow(NQCD, -1) + (- 1. / 6. * pow(pi, 2) * x * NQCD) + (- 5. / 4. * ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + 5. / 4. * ln(1 - z) * pow(z, -1) * NQCD + 5. / 2. * ln(1 - z) * pow(NQCD, -1) + (- 5. / 2. * ln(1 - z) * NQCD) + 5. / 4. * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1) + (- 5. / 4. * ln(1 - z) * x * pow(z, -1) * NQCD) + (- 5. / 2. * ln(1 - z) * x * pow(NQCD, -1)) + 5. / 2. * ln(1 - z) * x * NQCD + (- 5. / 4. * ln(1 - x) * pow(z, -1) * pow(NQCD, -1)) + 5. / 4. * ln(1 - x) * pow(z, -1) * NQCD + 5. / 2. * ln(1 - x) * pow(NQCD, -1) + (- 5. / 2. * ln(1 - x) * NQCD) + 5. / 4. * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -1) + (- 5. / 4. * ln(1 - x) * x * pow(z, -1) * NQCD) + (- 5. / 2. * ln(1 - x) * x * pow(NQCD, -1)) + 5. / 2. * ln(1 - x) * x * NQCD + 3. / 2. * ln(x) * pow(z, -1) * pow(NQCD, -1) + (- 3. / 2. * ln(x) * pow(z, -1) * NQCD) + (- 13. / 4. * ln(x) * pow(NQCD, -1)) + 13. / 4. * ln(x) * NQCD +  + (-ln(x) * z * pow(NQCD, -1)) + ln(x) * z * NQCD + (- 3. / 2. * ln(x) * x * pow(z, -1) * pow(NQCD, -1)) + 3. / 2. * ln(x) * x * pow(z, -1) * NQCD + 7. / 4. * ln(x) * x * pow(NQCD, -1) + (- 7. / 4. * ln(x) * x * NQCD) + (- 1. / 2. * ln(x) * ln(1 - z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 2. * ln(x) * ln(1 - z) * pow(z, -1) * NQCD + ln(x) * ln(1 - z) * pow(NQCD, -1) + (- ln(x) * ln(1 - z) * NQCD) + (- 1. / 2. * ln(x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 2. * ln(x) * ln(1 - z) * x * pow(z, -1) * NQCD + ln(x) * ln(1 - z) * x * pow(NQCD, -1) + (- ln(x) * ln(1 - z) * x * NQCD) + (- ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1)) + ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD + ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1) + (- ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD) + 1. / 2. * pow(ln(x), 2) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 2. * pow(ln(x), 2) * pow(z, -1) * NQCD) + (- pow(ln(x), 2) * pow(NQCD, -1)) + pow(ln(x), 2) * NQCD + 1. / 2. * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 2. * pow(ln(x), 2) * x * pow(z, -1) * NQCD) +  + (-pow(ln(x), 2) * x * pow(NQCD, -1)) + pow(ln(x), 2) * x * NQCD + (- 1. / 2. * ln(x) * ln(z) * pow(z, -1) * pow(NQCD, -1)) + 1. / 2. * ln(x) * ln(z) * pow(z, -1) * NQCD + 1. / 2. * ln(x) * ln(z) * pow(NQCD, -1) + (- 1. / 2. * ln(x) * ln(z) * NQCD) + (- 1. / 2. * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -1)) + 1. / 2. * ln(x) * ln(z) * x * pow(z, -1) * NQCD + 1. / 2. * ln(x) * ln(z) * x * pow(NQCD, -1) + (- 1. / 2. * ln(x) * ln(z) * x * NQCD) + (- 5. / 4. * ln(z) * pow(z, -1) * pow(NQCD, -1)) + 5. / 4. * ln(z) * pow(z, -1) * NQCD + 3. / 4. * ln(z) * pow(NQCD, -1) + (- 3. / 4. * ln(z) * NQCD) + ln(z) * z * pow(NQCD, -1) + (- ln(z) * z * NQCD) + 5. / 4. * ln(z) * x * pow(z, -1) * pow(NQCD, -1) + (- 5. / 4. * ln(z) * x * pow(z, -1) * NQCD) + (- 3. / 4. * ln(z) * x * pow(NQCD, -1)) + 3. / 4. * ln(z) * x * NQCD + (- Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1)) + Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1) + (- Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD) + Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1) + (- Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD) + (- Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(NQCD, -1)) +  + Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * NQCD + 1. / 2. * Li2(x) * pow(z, -1) * pow(NQCD, -1) + (- 1. / 2. * Li2(x) * pow(z, -1) * NQCD) + (- Li2(x) * pow(NQCD, -1)) + Li2(x) * NQCD + 1. / 2. * Li2(x) * x * pow(z, -1) * pow(NQCD, -1) + (- 1. / 2. * Li2(x) * x * pow(z, -1) * NQCD) + (- Li2(x) * x * pow(NQCD, -1)) + Li2(x) * x * NQCD + (- 1. / 2. / (1 - z) * ln(z) * pow(NQCD, -1)) + 1. / 2. / (1 - z) * ln(z) * NQCD + 1. / 2. / (1 - z) * ln(z) * x * pow(NQCD, -1) + (- 1. / 2. / (1 - z) * ln(z) * x * NQCD) + (- 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * pow(NQCD, -1)) + 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * NQCD + 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * z * pow(NQCD, -1) + (- 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * z * NQCD) + (- 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(NQCD, -1)) + 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * NQCD + 5 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * z * pow(NQCD, -1) + (- 5 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * z * NQCD) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * NQCD + (- 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * z * pow(NQCD, -1)) + 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * z * NQCD + (- 3 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * z * pow(NQCD, -1)) + 3 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * z * NQCD + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * NQCD) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1)) +  + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1) +  + (-2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1)) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * pow(NQCD, -1)) +  + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * NQCD + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * pow(NQCD, -1) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * NQCD) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * NQCD +  + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * pow(NQCD, -1) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * NQCD) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1)) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * pow(NQCD, -1)) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * NQCD + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * pow(NQCD, -1) +  + (-8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * NQCD) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1)) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1) +  + (-8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1)) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * pow(NQCD, -1) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * NQCD) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * pow(NQCD, -1)) +  + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD) + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) +  + (-2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * NQCD) + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1)) +  + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * NQCD + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * pow(NQCD, -1) + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD +  + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1) + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * NQCD) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * pow(NQCD, -1)) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * NQCD + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(NQCD, -1) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * NQCD) +  + (-4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * pow(NQCD, -1)) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * NQCD;
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
        tmp = 5. / 2. * lmuf * pow(z, -1) * pow(NQCD, -1) + (- 5. / 2. * lmuf * pow(z, -1) * NQCD) + (- 5 * lmuf * pow(NQCD, -1)) + 5 * lmuf * NQCD + (- 5. / 2. * lmuf * x * pow(z, -1) * pow(NQCD, -1)) + 5. / 2. * lmuf * x * pow(z, -1) * NQCD + 5 * lmuf * x * pow(NQCD, -1) + (- 5 * lmuf * x * NQCD) + ln(x) * lmuf * pow(z, -1) * pow(NQCD, -1) + (- ln(x) * lmuf * pow(z, -1) * NQCD) + (- 2 * ln(x) * lmuf * pow(NQCD, -1)) + 2 * ln(x) * lmuf * NQCD + ln(x) * lmuf * x * pow(z, -1) * pow(NQCD, -1) + (- ln(x) * lmuf * x * pow(z, -1) * NQCD) + (- 2 * ln(x) * lmuf * x * pow(NQCD, -1)) + 2 * ln(x) * lmuf * x * NQCD;
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - RG_D0: 000, 010
  - RG_D1: 000
  - RG_DL: 000, 010, 020
  - RG_RG: 000, 010
*/

/*
  Inverted Branch Report (By Number):
  - 000: RG_D0, RG_D1, RG_DL, RG_RG
  - 010: RG_D0, RG_DL, RG_RG
  - 020: RG_DL
*/
