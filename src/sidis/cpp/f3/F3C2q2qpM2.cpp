#include "../sidis.h"



/* Helpers */

double RG_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = 52. / 27. * pow(x, -1) * CF + (- 41. / 36. * CF) + 17. / 36. * x * CF + (- 34. / 27. * pow(x, 2) * CF) + 1. / 6. * pow(pi, 2) * CF + 1. / 2. * pow(pi, 2) * x * CF + 1. / 3. * pow(pi, 2) * pow(x, 2) * CF + 13. / 9. * ln(1 - x) * pow(x, -1) * CF + (- 11. / 6. * ln(1 - x) * CF) + 17. / 6. * ln(1 - x) * x * CF + (- 22. / 9. * ln(1 - x) * pow(x, 2) * CF) + 1. / 3. * ln(1 - x) * pow(pi, 2) * CF + 1. / 3. * ln(1 - x) * pow(pi, 2) * x * CF + 1. / 3. * pow(ln(1 - x), 2) * pow(x, -1) * CF + 1. / 4. * pow(ln(1 - x), 2) * CF + (- 1. / 4. * pow(ln(1 - x), 2) * x * CF) + (- 1. / 3. * pow(ln(1 - x), 2) * pow(x, 2) * CF) + (- ln(1 - x) * Li2(1 - x) * CF) + (- ln(1 - x) * Li2(1 - x) * x * CF) + (- 2 * ln(1 - x) * Li2(x) * CF) + (- 2 * ln(1 - x) * Li2(x) * x * CF) + 23. / 6. * ln(x) * CF + (- 5. / 6. * ln(x) * x * CF) + 38. / 9. * ln(x) * pow(x, 2) * CF + (- 1. / 3. * ln(x) * pow(pi, 2) * CF) + (- 1. / 3. * ln(x) * pow(pi, 2) * x * CF) + (- 2. / 3. * ln(x) * ln(1 - x) * pow(x, -1) * CF) + (- 1. / 2. * ln(x) * ln(1 - x) * CF) + 1. / 2. * ln(x) * ln(1 - x) * x * CF + 2. / 3. * ln(x) * ln(1 - x) * pow(x, 2) * CF +  + (-3. / 2. * ln(x) * pow(ln(1 - x), 2) * CF) + (- 3. / 2. * ln(x) * pow(ln(1 - x), 2) * x * CF) + (- 13. / 8. * pow(ln(x), 2) * CF) + (- 13. / 8. * pow(ln(x), 2) * x * CF) + (- 5. / 3. * pow(ln(x), 2) * pow(x, 2) * CF) + 5. / 12. * pow(ln(x), 3) * CF + 5. / 12. * pow(ln(x), 3) * x * CF + ln(x) * Li2(x) * CF + ln(x) * Li2(x) * x * CF + (- Li3(1 - x) * CF) + (- Li3(1 - x) * x * CF) + (- 2. / 3. * Li2(x) * pow(x, -1) * CF) + (- 3. / 2. * Li2(x) * CF) + (- 5. / 2. * Li2(x) * x * CF) + (- 4. / 3. * Li2(x) * pow(x, 2) * CF);
    return res;
}

double RG_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 26. / 9. * lmuf * pow(x, -1) * CF) + 11. / 3. * lmuf * CF + (- 17. / 3. * lmuf * x * CF) + 44. / 9. * lmuf * pow(x, 2) * CF + (- 1. / 3. * lmuf * pow(pi, 2) * CF) + (- 1. / 3. * lmuf * pow(pi, 2) * x * CF) + (- 4. / 3. * lmuf * ln(1 - x) * pow(x, -1) * CF) + (- lmuf * ln(1 - x) * CF) + lmuf * ln(1 - x) * x * CF + 4. / 3. * lmuf * ln(1 - x) * pow(x, 2) * CF + 2 * lmuf * Li2(x) * CF + 2 * lmuf * Li2(x) * x * CF + (- 2 * ln(x) * lmuf * CF) + (- 6 * ln(x) * lmuf * x * CF) + (- 4 * ln(x) * lmuf * pow(x, 2) * CF) + 2 * pow(ln(x), 2) * lmuf * CF + 2 * pow(ln(x), 2) * lmuf * x * CF;
    return res;
}

double RG_DL_020(double x, double z, double NF) {
    double res = 0.0;
    res = 4. / 3. * pow(lmuf, 2) * pow(x, -1) * CF + pow(lmuf, 2) * CF + (- pow(lmuf, 2) * x * CF) + (- 4. / 3. * pow(lmuf, 2) * pow(x, 2) * CF) + 2 * ln(x) * pow(lmuf, 2) * CF + 2 * ln(x) * pow(lmuf, 2) * x * CF;
    return res;
}

double RG_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = 13. / 9. * pow(x, -1) * CF + (- 11. / 6. * CF) + 17. / 6. * x * CF + (- 22. / 9. * pow(x, 2) * CF) + 1. / 6. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * CF + 2. / 3. * ln(1 - x) * pow(x, -1) * CF + 1. / 2. * ln(1 - x) * CF + (- 1. / 2. * ln(1 - x) * x * CF) + (- 2. / 3. * ln(1 - x) * pow(x, 2) * CF) + ln(x) * CF + 3 * ln(x) * x * CF + 2 * ln(x) * pow(x, 2) * CF + (- pow(ln(x), 2) * CF) + (- pow(ln(x), 2) * x * CF) + (- Li2(x) * CF) + (- Li2(x) * x * CF);
    return res;
}

double RG_D0_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 4. / 3. * lmuf * pow(x, -1) * CF) + (- lmuf * CF) + lmuf * x * CF + 4. / 3. * lmuf * pow(x, 2) * CF + (- 2 * ln(x) * lmuf * CF) + (- 2 * ln(x) * lmuf * x * CF);
    return res;
}

double RG_D1_000(double x, double z, double NF) {
    double res = 0.0;
    res = 2. / 3. * pow(x, -1) * CF + 1. / 2. * CF + (- 1. / 2. * x * CF) + (- 2. / 3. * pow(x, 2) * CF) + ln(x) * CF + ln(x) * x * CF;
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
        tmp = (-13. / 9. * pow(x, -1) * pow(z, -1) * CF) + 11. / 6. * pow(z, -1) * CF + 4 * CF + (- 17. / 6. * x * pow(z, -1) * CF) + (- 4 * x * CF) + 22. / 9. * pow(x, 2) * pow(z, -1) * CF + (- 1. / 6. * pow(pi, 2) * pow(z, -1) * CF) + (- 1. / 6. * pow(pi, 2) * x * pow(z, -1) * CF) + (- 2. / 3. * ln(1 - z) * pow(x, -1) * pow(z, -1) * CF) + (- 1. / 2. * ln(1 - z) * pow(z, -1) * CF) + 1. / 2. * ln(1 - z) * x * pow(z, -1) * CF + 2. / 3. * ln(1 - z) * pow(x, 2) * pow(z, -1) * CF + (- 2. / 3. * ln(1 - x) * pow(x, -1) * pow(z, -1) * CF) + (- 1. / 2. * ln(1 - x) * pow(z, -1) * CF) + 1. / 2. * ln(1 - x) * x * pow(z, -1) * CF + 2. / 3. * ln(1 - x) * pow(x, 2) * pow(z, -1) * CF + (- ln(x) * pow(z, -1) * CF) + 1. / 2. * ln(x) * CF + 2 * ln(x) * z * CF + (- 3 * ln(x) * x * pow(z, -1) * CF) + 5. / 2. * ln(x) * x * CF + (- 2 * ln(x) * pow(x, 2) * pow(z, -1) * CF) + (- ln(x) * ln(1 - z) * pow(z, -1) * CF) + (- ln(x) * ln(1 - z) * x * pow(z, -1) * CF) + 2 * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF + (- 2 * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF) + pow(ln(x), 2) * pow(z, -1) * CF + pow(ln(x), 2) * x * pow(z, -1) * CF + (- ln(x) * ln(z) * pow(z, -1) * CF) + ln(x) * ln(z) * CF + (- ln(x) * ln(z) * x * pow(z, -1) * CF) + ln(x) * ln(z) * x * CF + (- 2. / 3. * ln(z) * pow(x, -1) * pow(z, -1) * CF) + (- 1. / 2. * ln(z) * pow(z, -1) * CF) + 7. / 2. * ln(z) * CF + (- 2 * ln(z) * z * CF) + 1. / 2. * ln(z) * x * pow(z, -1) * CF +  + (-7. / 2. * ln(z) * x * CF) + 2. / 3. * ln(z) * pow(x, 2) * pow(z, -1) * CF + 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF + (- 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF) + (- 2 * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF) + 2 * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF + Li2(x) * pow(z, -1) * CF + Li2(x) * x * pow(z, -1) * CF + 2. / 3. / (1 - z) * ln(z) * pow(x, -1) * CF + (- 1 / (1 - z) * ln(z) * CF) + 1 / (1 - z) * ln(z) * x * CF + (- 2. / 3. / (1 - z) * ln(z) * pow(x, 2) * CF) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * CF + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * z * CF) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * CF + (- 10 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * z * CF) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * CF + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * z * CF + 6 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * z * CF + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF +  + (-24 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF) + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + 24 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF + (- 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF +  + (-24 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF) + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF) + 24 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF + (- 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF +  + (-8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + 24 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF + (- 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF + (- 24 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF) + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF) +  + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF +  + (-8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) + 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 4 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF;
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
        tmp = 4. / 3. * lmuf * pow(x, -1) * pow(z, -1) * CF + lmuf * pow(z, -1) * CF + (- lmuf * x * pow(z, -1) * CF) + (- 4. / 3. * lmuf * pow(x, 2) * pow(z, -1) * CF) + 2 * ln(x) * lmuf * pow(z, -1) * CF + 2 * ln(x) * lmuf * x * pow(z, -1) * CF;
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
