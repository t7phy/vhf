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
        tmp = 1. / 2. * CF + (- 2 * CF * pow(rln2, 2)) + (- 4 * x * z * CF * pow(rln2, 2)) + 1. / 6. * pow(pi, 2) * CF + (- 1. / 3. * pow(pi, 2) * z * CF) + (- 1. / 6. * pow(pi, 2) * x * CF) + 1. / 3. * pow(pi, 2) * x * z * CF + 3 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * rln2 + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * rln2) + (- ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * CF * rln2) + 6 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF * rln2 + (- pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * CF) + 2 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * z * CF + pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * CF + (- 2 * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * x * z * CF) + (- ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF) + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF) + (- ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * CF) + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF) + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF + ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * rln2 + 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * rln2 + ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * CF * rln2 + 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF * rln2 + 4 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * z * CF +  + (-4 * ln(mysqrt(x * pow(z, -1))) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * z * CF) + ln(x) * CF + (- 2 * ln(x) * CF * rln2) + (- ln(x) * z * CF) + 2 * ln(x) * z * CF * rln2 + ln(x) * x * CF * rln2 + (- 4 * ln(x) * x * z * CF * rln2) + ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + (- 2 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF) + (- ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * CF) + 2 * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF + ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + 2 * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF + ln(x) * ln(1 - x) * x * CF + (- 2 * ln(x) * ln(1 - x) * x * z * CF) + (- ln(x) * ln(1 + x * z) * CF) + (- 2 * ln(x) * ln(1 + x * z) * x * z * CF) + 2 * ln(x) * ln(z + x) * z * CF + ln(x) * ln(z + x) * x * CF + (- 1. / 2. * pow(ln(x), 2) * x * CF) + pow(ln(x), 2) * x * z * CF + (- ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF) + 1. / 2. * ln(z) * CF + (- 2 * ln(z) * CF * rln2) + ln(z) * z * CF + (- 2 * ln(z) * z * CF * rln2) + (- ln(z) * x * CF * rln2) + (- 4 * ln(z) * x * z * CF * rln2) + (- ln(z) * ln(1 - z) * CF) + 2 * ln(z) * ln(1 - z) * z * CF + ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + 2 * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF + ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF + ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * CF + 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF + (- ln(z) * ln(1 + x * z) * CF) + (- 2 * ln(z) * ln(1 + x * z) * x * z * CF) + (- 2 * ln(z) * ln(z + x) * z * CF) +  + (-ln(z) * ln(z + x) * x * CF) + 1. / 2. * pow(ln(z), 2) * CF + (- pow(ln(z), 2) * z * CF) + (- 4 * ln(z) * ArcTan(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * z * CF) + (- ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF) + (- 2 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF) + (- Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * CF) + 2 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF + Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * CF + Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + 2 * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF + (- Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF) + (- 2 * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * CF) + Li2(1 - x * pow(z, -1)) * CF + (- 2 * Li2(1 - x * pow(z, -1)) * z * CF) + 2 * Li2(-x * pow(z, -1)) * z * CF + Li2(-x * pow(z, -1)) * x * CF + (- Li2(-x * z) * CF) + (- 2 * Li2(-x * z) * x * z * CF) + Li2(x) * x * CF + (- 2 * Li2(x) * x * z * CF) + (- Li2(z) * CF) + 2 * Li2(z) * z * CF + 2 * InvTanInt(-mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * z * CF + (- 2 * InvTanInt(mysqrt(x * pow(z, -1))) * mysqrt(x * pow(z, -1)) * z * CF) + 4 * InvTanInt(mysqrt(x * pow(z, -1)) * z) * mysqrt(x * pow(z, -1)) * z * CF + (- 2 * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * rln2) + 1 / (1 - x) * CF * pow(rln2, 2) + 6 / (1 - x) * z * CF * pow(rln2, 2) + 1. / 4. / (1 - x) * pow(pi, 2) * CF + (- 1. / 2. / (1 - x) * pow(pi, 2) * z * CF) +  + (-8 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * rln2) + (- 1 / (1 - x) * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * CF) + 2 / (1 - x) * pow(ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)), 2) * z * CF + 2 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + 4 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF + (- 1 / (1 - x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF) + (- 2 / (1 - x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF * rln2) + (- 4 / (1 - x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF * rln2) + (- 1. / 2. / (1 - x) * ln(x) * CF * rln2) + 1. / 2. / (1 - x) * ln(x) * z * CF + 5 / (1 - x) * ln(x) * z * CF * rln2 + 1 / (1 - x) * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + (- 2 / (1 - x) * ln(x) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF) + (- 1. / 2. / (1 - x) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF) + (- 3 / (1 - x) * ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF) + (- 3. / 2. / (1 - x) * ln(x) * ln(1 - x) * CF) + 3 / (1 - x) * ln(x) * ln(1 - x) * z * CF + 1 / (1 - x) * ln(x) * ln(1 + x * z) * CF + 2 / (1 - x) * ln(x) * ln(1 + x * z) * z * CF + (- 1 / (1 - x) * ln(x) * ln(z + x) * CF) + (- 2 / (1 - x) * ln(x) * ln(z + x) * z * CF) + 1. / 2. / (1 - x) * pow(ln(x), 2) * CF + (- 1 / (1 - x) * pow(ln(x), 2) * z * CF) + 2 / (1 - x) * ln(x) * ln(z) * z * CF + 1. / 2. / (1 - x) * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF + (- 1. / 2. / (1 - x) * ln(z) * CF) +  + 5. / 2. / (1 - x) * ln(z) * CF * rln2 + (- 1. / 2. / (1 - x) * ln(z) * z * CF) + 7 / (1 - x) * ln(z) * z * CF * rln2 + 1. / 2. / (1 - x) * ln(z) * ln(1 - z) * CF + (- 1 / (1 - x) * ln(z) * ln(1 - z) * z * CF) + (- 1. / 2. / (1 - x) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF) + (- 3 / (1 - x) * ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF) + (- 2 / (1 - x) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF) + (- 4 / (1 - x) * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF) + 1 / (1 - x) * ln(z) * ln(1 + x * z) * CF + 2 / (1 - x) * ln(z) * ln(1 + x * z) * z * CF + 1 / (1 - x) * ln(z) * ln(z + x) * CF + 2 / (1 - x) * ln(z) * ln(z + x) * z * CF + 1. / 2. / (1 - x) * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF + 3. / 2. / (1 - x) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF + 1 / (1 - x) * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF + (- 3. / 2. / (1 - x) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * CF) + (- 1 / (1 - x) * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * z * CF) + (- 1. / 2. / (1 - x) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF) + (- 3 / (1 - x) * Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF) + 1. / 2. / (1 - x) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * CF + 3 / (1 - x) * Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * z * CF + (- 1. / 2. / (1 - x) * Li2(1 - x * pow(z, -1)) * CF) +  + 1 / (1 - x) * Li2(1 - x * pow(z, -1)) * z * CF + (- 1 / (1 - x) * Li2(-x * pow(z, -1)) * CF) + (- 2 / (1 - x) * Li2(-x * pow(z, -1)) * z * CF) + 1 / (1 - x) * Li2(-x * z) * CF + 2 / (1 - x) * Li2(-x * z) * z * CF + (- 3. / 2. / (1 - x) * Li2(x) * CF) + 3 / (1 - x) * Li2(x) * z * CF + 1. / 2. / (1 - x) * Li2(z) * CF + (- 1 / (1 - x) * Li2(z) * z * CF) + 1 / (1 - x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * rln2 + 1. / 6. / (1 + x) * pow(pi, 2) * CF + (- 1. / 3. / (1 + x) * pow(pi, 2) * z * CF) + 1 / (1 + x) * ln(x) * ln(1 + x * z) * CF + (- 2 / (1 + x) * ln(x) * ln(1 + x * z) * z * CF) + 1 / (1 + x) * ln(x) * ln(z + x) * CF + (- 2 / (1 + x) * ln(x) * ln(z + x) * z * CF) + (- 1. / 2. / (1 + x) * pow(ln(x), 2) * CF) + 1 / (1 + x) * pow(ln(x), 2) * z * CF + (- 2 / (1 + x) * ln(x) * ln(z) * CF) + 4 / (1 + x) * ln(x) * ln(z) * z * CF + 1 / (1 + x) * ln(z) * ln(1 + x * z) * CF + (- 2 / (1 + x) * ln(z) * ln(1 + x * z) * z * CF) + (- 1 / (1 + x) * ln(z) * ln(z + x) * CF) + 2 / (1 + x) * ln(z) * ln(z + x) * z * CF + 1. / 2. / (1 + x) * pow(ln(z), 2) * CF + (- 1 / (1 + x) * pow(ln(z), 2) * z * CF) + 1 / (1 + x) * Li2(-x * pow(z, -1)) * CF + (- 2 / (1 + x) * Li2(-x * pow(z, -1)) * z * CF) + 1 / (1 + x) * Li2(-x * z) * CF + (- 2 / (1 + x) * Li2(-x * z) * z * CF) + (- 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * CF) + 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * z * CF + (- 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * CF) + 5 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * z * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * CF) + (- 1 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * z * CF) + (- 3 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * z * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * CF + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) +  + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF +  + (-4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF +  + (-2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) + 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF) + 1. / 2. / (z - x) * ln(x) * z * CF + (- 1 / (z - x) * ln(x) * pow(z, 2) * CF) + (- 1. / 2. / (z - x) * ln(z) * z * CF) +  + 1 / (z - x) * ln(z) * pow(z, 2) * CF + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + (- 1 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF + 1 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF) + (- 1 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF) +  + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF + 1 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF + 1 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF) + (- 1 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF;
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - RG_RG: 000
*/
