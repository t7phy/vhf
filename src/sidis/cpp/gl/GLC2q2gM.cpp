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
        tmp = 2 * x * pow(z, -1) * pow(NQCD, -2) - 2 * x * pow(z, -1) - 4 * x * pow(NQCD, -2) + 4 * x + 2 * x * z * pow(NQCD, -2) - 2 * x * z + 2. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) - 2. / 3. * pow(pi, 2) * x * pow(z, -1) - 3. / 2. * pow(pi, 2) * x * pow(NQCD, -2) + 3. / 2. * pow(pi, 2) * x + 5. / 6. * pow(pi, 2) * x * z * pow(NQCD, -2) - 5. / 6. * pow(pi, 2) * x * z - 2 * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - z) * x * pow(z, -1) + 10 * ln(1 - z) * x * pow(NQCD, -2) - 10 * ln(1 - z) * x - 8 * ln(1 - z) * x * z * pow(NQCD, -2) + 8 * ln(1 - z) * x * z - 5. / 2. * pow(ln(1 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 5. / 2. * pow(ln(1 - z), 2) * x * pow(z, -1) + 13. / 2. * pow(ln(1 - z), 2) * x * pow(NQCD, -2) - 13. / 2. * pow(ln(1 - z), 2) * x - 4 * pow(ln(1 - z), 2) * x * z * pow(NQCD, -2) + 4 * pow(ln(1 - z), 2) * x * z + ln(1 - z) * ln(1 - z - x) * x * pow(z, -1) * pow(NQCD, -2) - ln(1 - z) * ln(1 - z - x) * x * pow(z, -1) - 3 * ln(1 - z) * ln(1 - z - x) * x * pow(NQCD, -2) + 3 * ln(1 - z) * ln(1 - z - x) * x + 2 * ln(1 - z) * ln(1 - z - x) * x * z * pow(NQCD, -2) - 2 * ln(1 - z) * ln(1 - z - x) * x * z - 2 * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - x) * x * pow(z, -1) + 8 * ln(1 - x) * x * pow(NQCD, -2) - 8 * ln(1 - x) * x - 6 * ln(1 - x) * x * z * pow(NQCD, -2) + 6 * ln(1 - x) * x * z - 5 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 5 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) + 13 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, -2) - 13 * ln(1 - x) * ln(1 - z) * x - 8 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, -2) + 8 * ln(1 - x) * ln(1 - z) * x * z - 2 * pow(ln(1 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 2 * pow(ln(1 - x), 2) * x * pow(z, -1) + 9. / 2. * pow(ln(1 - x), 2) * x * pow(NQCD, -2) + -9. / 2. * pow(ln(1 - x), 2) * x - 5. / 2. * pow(ln(1 - x), 2) * x * z * pow(NQCD, -2) + 5. / 2. * pow(ln(1 - x), 2) * x * z + 3 * ln(x) * x * pow(z, -1) * pow(NQCD, -2) - 3 * ln(x) * x * pow(z, -1) - 15 * ln(x) * x * pow(NQCD, -2) + 15 * ln(x) * x + 12 * ln(x) * x * z * pow(NQCD, -2) - 12 * ln(x) * x * z + 6 * ln(x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) - 6 * ln(x) * ln(1 - z) * x * pow(z, -1) - 17 * ln(x) * ln(1 - z) * x * pow(NQCD, -2) + 17 * ln(x) * ln(1 - z) * x + 11 * ln(x) * ln(1 - z) * x * z * pow(NQCD, -2) - 11 * ln(x) * ln(1 - z) * x * z - ln(x) * ln(1 - z - x) * x * pow(z, -1) * pow(NQCD, -2) + ln(x) * ln(1 - z - x) * x * pow(z, -1) + 3 * ln(x) * ln(1 - z - x) * x * pow(NQCD, -2) - 3 * ln(x) * ln(1 - z - x) * x - 2 * ln(x) * ln(1 - z - x) * x * z * pow(NQCD, -2) + 2 * ln(x) * ln(1 - z - x) * x * z + 6 * ln(x) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) - 6 * ln(x) * ln(1 - x) * x * pow(z, -1) - 16 * ln(x) * ln(1 - x) * x * pow(NQCD, -2) + 16 * ln(x) * ln(1 - x) * x + 10 * ln(x) * ln(1 - x) * x * z * pow(NQCD, -2) - 10 * ln(x) * ln(1 - x) * x * z + ln(x) * ln(-z + x) * x * pow(NQCD, -2) - ln(x) * ln(-z + x) * x - ln(x) * ln(-z + x) * x * z * pow(NQCD, -2) + ln(x) * ln(-z + x) * x * z - 7. / 2. * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 7. / 2. * pow(ln(x), 2) * x * pow(z, -1) + 10 * pow(ln(x), 2) * x * pow(NQCD, -2) - 10 * pow(ln(x), 2) * x - 13. / 2. * pow(ln(x), 2) * x * z * pow(NQCD, -2) + 13. / 2. * pow(ln(x), 2) * x * z + 3 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) - 3 * ln(x) * ln(z) * x * pow(z, -1) - 11 * ln(x) * ln(z) * x * pow(NQCD, -2) + 11 * ln(x) * ln(z) * x + 8 * ln(x) * ln(z) * x * z * pow(NQCD, -2) - 8 * ln(x) * ln(z) * x * z - ln(z) * x * pow(z, -1) * pow(NQCD, -2) + +ln(z) * x * pow(z, -1) + 7 * ln(z) * x * pow(NQCD, -2) - 7 * ln(z) * x - 6 * ln(z) * x * z * pow(NQCD, -2) + 6 * ln(z) * x * z - 2 * ln(z) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(z) * ln(1 - z) * x * pow(z, -1) + 8 * ln(z) * ln(1 - z) * x * pow(NQCD, -2) - 8 * ln(z) * ln(1 - z) * x - 6 * ln(z) * ln(1 - z) * x * z * pow(NQCD, -2) + 6 * ln(z) * ln(1 - z) * x * z - 2 * ln(z) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(z) * ln(1 - x) * x * pow(z, -1) + 6 * ln(z) * ln(1 - x) * x * pow(NQCD, -2) - 6 * ln(z) * ln(1 - x) * x - 4 * ln(z) * ln(1 - x) * x * z * pow(NQCD, -2) + 4 * ln(z) * ln(1 - x) * x * z - ln(z) * ln(-z + x) * x * pow(NQCD, -2) + ln(z) * ln(-z + x) * x + ln(z) * ln(-z + x) * x * z * pow(NQCD, -2) - ln(z) * ln(-z + x) * x * z - 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) + 3 * pow(ln(z), 2) * x * pow(NQCD, -2) - 3 * pow(ln(z), 2) * x - 5. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, -2) + 5. / 2. * pow(ln(z), 2) * x * z - Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * pow(NQCD, -2) + Li2(1 / (1 - z) - 1 / (1 - z) * x) * x + Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * z * pow(NQCD, -2) - Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * z - Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * pow(NQCD, -2) + Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x + Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * z * pow(NQCD, -2) - Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * z + Li2(1 / (1 - x) * z) * x * pow(z, -1) * pow(NQCD, -2) - Li2(1 / (1 - x) * z) * x * pow(z, -1) - Li2(1 / (1 - x) * z) * x * pow(NQCD, -2) + Li2(1 / (1 - x) * z) * x + -Li2(1 / (1 - x) / (1 - z) * x * z) * x * pow(z, -1) * pow(NQCD, -2) + Li2(1 / (1 - x) / (1 - z) * x * z) * x * pow(z, -1) + 2 * Li2(1 / (1 - x) / (1 - z) * x * z) * x * pow(NQCD, -2) - 2 * Li2(1 / (1 - x) / (1 - z) * x * z) * x - Li2(1 / (1 - x) / (1 - z) * x * z) * x * z * pow(NQCD, -2) + Li2(1 / (1 - x) / (1 - z) * x * z) * x * z - Li2(z) * x * pow(z, -1) * pow(NQCD, -2) + Li2(z) * x * pow(z, -1) + 2 * Li2(z) * x * pow(NQCD, -2) - 2 * Li2(z) * x - Li2(z) * x * z * pow(NQCD, -2) + Li2(z) * x * z;

        res += tmp;
    }
    if (z > 1. - x && z < x) {
        double tmp = 0.0;
        tmp = 2 * x * pow(z, -1) * pow(NQCD, -2) - 2 * x * pow(z, -1) - 4 * x * pow(NQCD, -2) + 4 * x + 2 * x * z * pow(NQCD, -2) - 2 * x * z + 2. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) - 2. / 3. * pow(pi, 2) * x * pow(z, -1) - 3. / 2. * pow(pi, 2) * x * pow(NQCD, -2) + 3. / 2. * pow(pi, 2) * x + 5. / 6. * pow(pi, 2) * x * z * pow(NQCD, -2) - 5. / 6. * pow(pi, 2) * x * z - 2 * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - z) * x * pow(z, -1) + 10 * ln(1 - z) * x * pow(NQCD, -2) - 10 * ln(1 - z) * x - 8 * ln(1 - z) * x * z * pow(NQCD, -2) + 8 * ln(1 - z) * x * z + ln(1 - z) * ln(-1 + z + x) * x * pow(z, -1) * pow(NQCD, -2) - ln(1 - z) * ln(-1 + z + x) * x * pow(z, -1) - 3 * ln(1 - z) * ln(-1 + z + x) * x * pow(NQCD, -2) + 3 * ln(1 - z) * ln(-1 + z + x) * x + 2 * ln(1 - z) * ln(-1 + z + x) * x * z * pow(NQCD, -2) - 2 * ln(1 - z) * ln(-1 + z + x) * x * z - 2 * pow(ln(1 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 2 * pow(ln(1 - z), 2) * x * pow(z, -1) + 6 * pow(ln(1 - z), 2) * x * pow(NQCD, -2) - 6 * pow(ln(1 - z), 2) * x - 4 * pow(ln(1 - z), 2) * x * z * pow(NQCD, -2) + 4 * pow(ln(1 - z), 2) * x * z - 2 * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - x) * x * pow(z, -1) + 8 * ln(1 - x) * x * pow(NQCD, -2) - 8 * ln(1 - x) * x - 6 * ln(1 - x) * x * z * pow(NQCD, -2) + 6 * ln(1 - x) * x * z - 4 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 4 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) + 10 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, -2) - 10 * ln(1 - x) * ln(1 - z) * x - 6 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, -2) + 6 * ln(1 - x) * ln(1 - z) * x * z - 2 * pow(ln(1 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 2 * pow(ln(1 - x), 2) * x * pow(z, -1) + 9. / 2. * pow(ln(1 - x), 2) * x * pow(NQCD, -2) + -9. / 2. * pow(ln(1 - x), 2) * x - 5. / 2. * pow(ln(1 - x), 2) * x * z * pow(NQCD, -2) + 5. / 2. * pow(ln(1 - x), 2) * x * z + 3 * ln(x) * x * pow(z, -1) * pow(NQCD, -2) - 3 * ln(x) * x * pow(z, -1) - 15 * ln(x) * x * pow(NQCD, -2) + 15 * ln(x) * x + 12 * ln(x) * x * z * pow(NQCD, -2) - 12 * ln(x) * x * z - ln(x) * ln(-1 + z + x) * x * pow(z, -1) * pow(NQCD, -2) + ln(x) * ln(-1 + z + x) * x * pow(z, -1) + 3 * ln(x) * ln(-1 + z + x) * x * pow(NQCD, -2) - 3 * ln(x) * ln(-1 + z + x) * x - 2 * ln(x) * ln(-1 + z + x) * x * z * pow(NQCD, -2) + 2 * ln(x) * ln(-1 + z + x) * x * z + 5 * ln(x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) - 5 * ln(x) * ln(1 - z) * x * pow(z, -1) - 16 * ln(x) * ln(1 - z) * x * pow(NQCD, -2) + 16 * ln(x) * ln(1 - z) * x + 11 * ln(x) * ln(1 - z) * x * z * pow(NQCD, -2) - 11 * ln(x) * ln(1 - z) * x * z + 5 * ln(x) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) - 5 * ln(x) * ln(1 - x) * x * pow(z, -1) - 13 * ln(x) * ln(1 - x) * x * pow(NQCD, -2) + 13 * ln(x) * ln(1 - x) * x + 8 * ln(x) * ln(1 - x) * x * z * pow(NQCD, -2) - 8 * ln(x) * ln(1 - x) * x * z + ln(x) * ln(-z + x) * x * pow(NQCD, -2) - ln(x) * ln(-z + x) * x - ln(x) * ln(-z + x) * x * z * pow(NQCD, -2) + ln(x) * ln(-z + x) * x * z - 3 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 3 * pow(ln(x), 2) * x * pow(z, -1) + 19. / 2. * pow(ln(x), 2) * x * pow(NQCD, -2) - 19. / 2. * pow(ln(x), 2) * x - 13. / 2. * pow(ln(x), 2) * x * z * pow(NQCD, -2) + 13. / 2. * pow(ln(x), 2) * x * z + 4 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) - 4 * ln(x) * ln(z) * x * pow(z, -1) - 14 * ln(x) * ln(z) * x * pow(NQCD, -2) + 14 * ln(x) * ln(z) * x + 10 * ln(x) * ln(z) * x * z * pow(NQCD, -2) - 10 * ln(x) * ln(z) * x * z - ln(z) * x * pow(z, -1) * pow(NQCD, -2) + +ln(z) * x * pow(z, -1) + 7 * ln(z) * x * pow(NQCD, -2) - 7 * ln(z) * x - 6 * ln(z) * x * z * pow(NQCD, -2) + 6 * ln(z) * x * z - 3 * ln(z) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 3 * ln(z) * ln(1 - z) * x * pow(z, -1) + 11 * ln(z) * ln(1 - z) * x * pow(NQCD, -2) - 11 * ln(z) * ln(1 - z) * x - 8 * ln(z) * ln(1 - z) * x * z * pow(NQCD, -2) + 8 * ln(z) * ln(1 - z) * x * z - 2 * ln(z) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(z) * ln(1 - x) * x * pow(z, -1) + 6 * ln(z) * ln(1 - x) * x * pow(NQCD, -2) - 6 * ln(z) * ln(1 - x) * x - 4 * ln(z) * ln(1 - x) * x * z * pow(NQCD, -2) + 4 * ln(z) * ln(1 - x) * x * z - ln(z) * ln(-z + x) * x * pow(NQCD, -2) + ln(z) * ln(-z + x) * x + ln(z) * ln(-z + x) * x * z * pow(NQCD, -2) - ln(z) * ln(-z + x) * x * z - 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) + 3 * pow(ln(z), 2) * x * pow(NQCD, -2) - 3 * pow(ln(z), 2) * x - 5. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, -2) + 5. / 2. * pow(ln(z), 2) * x * z + Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) - Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) - 2 * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(NQCD, -2) + 2 * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x + Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z * pow(NQCD, -2) - Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z - Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) + Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) + Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(NQCD, -2) - Li2(pow(z, -1) - x * pow(z, -1)) * x + -Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * pow(NQCD, -2) + Li2(1 / (1 - z) - 1 / (1 - z) * x) * x + Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * z * pow(NQCD, -2) - Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * z + Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * pow(NQCD, -2) - Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x - Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * z * pow(NQCD, -2) + Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * z - Li2(z) * x * pow(z, -1) * pow(NQCD, -2) + Li2(z) * x * pow(z, -1) + 2 * Li2(z) * x * pow(NQCD, -2) - 2 * Li2(z) * x - Li2(z) * x * z * pow(NQCD, -2) + Li2(z) * x * z;

        res += tmp;
    }
    if (z < 1. - x && z > x) {
        double tmp = 0.0;
        tmp = 2 * x * pow(z, -1) * pow(NQCD, -2) - 2 * x * pow(z, -1) - 4 * x * pow(NQCD, -2) + 4 * x + 2 * x * z * pow(NQCD, -2) - 2 * x * z + 2. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) - 2. / 3. * pow(pi, 2) * x * pow(z, -1) - 13. / 6. * pow(pi, 2) * x * pow(NQCD, -2) + 13. / 6. * pow(pi, 2) * x + 3. / 2. * pow(pi, 2) * x * z * pow(NQCD, -2) - 3. / 2. * pow(pi, 2) * x * z - 2 * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - z) * x * pow(z, -1) + 10 * ln(1 - z) * x * pow(NQCD, -2) - 10 * ln(1 - z) * x - 8 * ln(1 - z) * x * z * pow(NQCD, -2) + 8 * ln(1 - z) * x * z - 5. / 2. * pow(ln(1 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 5. / 2. * pow(ln(1 - z), 2) * x * pow(z, -1) + 15. / 2. * pow(ln(1 - z), 2) * x * pow(NQCD, -2) - 15. / 2. * pow(ln(1 - z), 2) * x - 5 * pow(ln(1 - z), 2) * x * z * pow(NQCD, -2) + 5 * pow(ln(1 - z), 2) * x * z + ln(1 - z) * ln(1 - z - x) * x * pow(z, -1) * pow(NQCD, -2) - ln(1 - z) * ln(1 - z - x) * x * pow(z, -1) - 3 * ln(1 - z) * ln(1 - z - x) * x * pow(NQCD, -2) + 3 * ln(1 - z) * ln(1 - z - x) * x + 2 * ln(1 - z) * ln(1 - z - x) * x * z * pow(NQCD, -2) - 2 * ln(1 - z) * ln(1 - z - x) * x * z - 2 * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - x) * x * pow(z, -1) + 8 * ln(1 - x) * x * pow(NQCD, -2) - 8 * ln(1 - x) * x - 6 * ln(1 - x) * x * z * pow(NQCD, -2) + 6 * ln(1 - x) * x * z - 5 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 5 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) + 11 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, -2) - 11 * ln(1 - x) * ln(1 - z) * x - 6 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, -2) + 6 * ln(1 - x) * ln(1 - z) * x * z - 2 * pow(ln(1 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 2 * pow(ln(1 - x), 2) * x * pow(z, -1) + 11. / 2. * pow(ln(1 - x), 2) * x * pow(NQCD, -2) + -11. / 2. * pow(ln(1 - x), 2) * x - 7. / 2. * pow(ln(1 - x), 2) * x * z * pow(NQCD, -2) + 7. / 2. * pow(ln(1 - x), 2) * x * z + 3 * ln(x) * x * pow(z, -1) * pow(NQCD, -2) - 3 * ln(x) * x * pow(z, -1) - 15 * ln(x) * x * pow(NQCD, -2) + 15 * ln(x) * x + 12 * ln(x) * x * z * pow(NQCD, -2) - 12 * ln(x) * x * z + 6 * ln(x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) - 6 * ln(x) * ln(1 - z) * x * pow(z, -1) - 18 * ln(x) * ln(1 - z) * x * pow(NQCD, -2) + 18 * ln(x) * ln(1 - z) * x + 12 * ln(x) * ln(1 - z) * x * z * pow(NQCD, -2) - 12 * ln(x) * ln(1 - z) * x * z - ln(x) * ln(1 - z - x) * x * pow(z, -1) * pow(NQCD, -2) + ln(x) * ln(1 - z - x) * x * pow(z, -1) + 3 * ln(x) * ln(1 - z - x) * x * pow(NQCD, -2) - 3 * ln(x) * ln(1 - z - x) * x - 2 * ln(x) * ln(1 - z - x) * x * z * pow(NQCD, -2) + 2 * ln(x) * ln(1 - z - x) * x * z + 6 * ln(x) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) - 6 * ln(x) * ln(1 - x) * x * pow(z, -1) - 15 * ln(x) * ln(1 - x) * x * pow(NQCD, -2) + 15 * ln(x) * ln(1 - x) * x + 9 * ln(x) * ln(1 - x) * x * z * pow(NQCD, -2) - 9 * ln(x) * ln(1 - x) * x * z + ln(x) * ln(z - x) * x * pow(NQCD, -2) - ln(x) * ln(z - x) * x - ln(x) * ln(z - x) * x * z * pow(NQCD, -2) + ln(x) * ln(z - x) * x * z - 7. / 2. * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 7. / 2. * pow(ln(x), 2) * x * pow(z, -1) + 21. / 2. * pow(ln(x), 2) * x * pow(NQCD, -2) - 21. / 2. * pow(ln(x), 2) * x - 7 * pow(ln(x), 2) * x * z * pow(NQCD, -2) + 7 * pow(ln(x), 2) * x * z + 3 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) - 3 * ln(x) * ln(z) * x * pow(z, -1) - 12 * ln(x) * ln(z) * x * pow(NQCD, -2) + 12 * ln(x) * ln(z) * x + 9 * ln(x) * ln(z) * x * z * pow(NQCD, -2) - 9 * ln(x) * ln(z) * x * z - ln(z) * x * pow(z, -1) * pow(NQCD, -2) + ln(z) * x * pow(z, -1) + +7 * ln(z) * x * pow(NQCD, -2) - 7 * ln(z) * x - 6 * ln(z) * x * z * pow(NQCD, -2) + 6 * ln(z) * x * z - 2 * ln(z) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(z) * ln(1 - z) * x * pow(z, -1) + 9 * ln(z) * ln(1 - z) * x * pow(NQCD, -2) - 9 * ln(z) * ln(1 - z) * x - 7 * ln(z) * ln(1 - z) * x * z * pow(NQCD, -2) + 7 * ln(z) * ln(1 - z) * x * z - 2 * ln(z) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(z) * ln(1 - x) * x * pow(z, -1) + 5 * ln(z) * ln(1 - x) * x * pow(NQCD, -2) - 5 * ln(z) * ln(1 - x) * x - 3 * ln(z) * ln(1 - x) * x * z * pow(NQCD, -2) + 3 * ln(z) * ln(1 - x) * x * z - ln(z) * ln(z - x) * x * pow(NQCD, -2) + ln(z) * ln(z - x) * x + ln(z) * ln(z - x) * x * z * pow(NQCD, -2) - ln(z) * ln(z - x) * x * z - 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) + 7. / 2. * pow(ln(z), 2) * x * pow(NQCD, -2) - 7. / 2. * pow(ln(z), 2) * x - 3 * pow(ln(z), 2) * x * z * pow(NQCD, -2) + 3 * pow(ln(z), 2) * x * z + Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * pow(NQCD, -2) - Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x - Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * z * pow(NQCD, -2) + Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * z + Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * pow(NQCD, -2) - Li2(1 / (1 - x) - 1 / (1 - x) * z) * x - Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * z * pow(NQCD, -2) + Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * z + Li2(1 / (1 - x) * z) * x * pow(z, -1) * pow(NQCD, -2) - Li2(1 / (1 - x) * z) * x * pow(z, -1) - Li2(1 / (1 - x) * z) * x * pow(NQCD, -2) + Li2(1 / (1 - x) * z) * x - Li2(1 / (1 - x) / (1 - z) * x * z) * x * pow(z, -1) * pow(NQCD, -2) + +Li2(1 / (1 - x) / (1 - z) * x * z) * x * pow(z, -1) + 2 * Li2(1 / (1 - x) / (1 - z) * x * z) * x * pow(NQCD, -2) - 2 * Li2(1 / (1 - x) / (1 - z) * x * z) * x - Li2(1 / (1 - x) / (1 - z) * x * z) * x * z * pow(NQCD, -2) + Li2(1 / (1 - x) / (1 - z) * x * z) * x * z - Li2(z) * x * pow(z, -1) * pow(NQCD, -2) + Li2(z) * x * pow(z, -1) + 2 * Li2(z) * x * pow(NQCD, -2) - 2 * Li2(z) * x - Li2(z) * x * z * pow(NQCD, -2) + Li2(z) * x * z;

        res += tmp;
    }
    if (z > 1. - x && z > x) {
        double tmp = 0.0;
        tmp = 2 * x * pow(z, -1) * pow(NQCD, -2) - 2 * x * pow(z, -1) - 4 * x * pow(NQCD, -2) + 4 * x + 2 * x * z * pow(NQCD, -2) - 2 * x * z + 2. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2) - 2. / 3. * pow(pi, 2) * x * pow(z, -1) - 3. / 2. * pow(pi, 2) * x * pow(NQCD, -2) + 3. / 2. * pow(pi, 2) * x + 5. / 6. * pow(pi, 2) * x * z * pow(NQCD, -2) - 5. / 6. * pow(pi, 2) * x * z - 2 * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - z) * x * pow(z, -1) + 10 * ln(1 - z) * x * pow(NQCD, -2) - 10 * ln(1 - z) * x - 8 * ln(1 - z) * x * z * pow(NQCD, -2) + 8 * ln(1 - z) * x * z + ln(1 - z) * ln(-1 + z + x) * x * pow(z, -1) * pow(NQCD, -2) - ln(1 - z) * ln(-1 + z + x) * x * pow(z, -1) - 3 * ln(1 - z) * ln(-1 + z + x) * x * pow(NQCD, -2) + 3 * ln(1 - z) * ln(-1 + z + x) * x + 2 * ln(1 - z) * ln(-1 + z + x) * x * z * pow(NQCD, -2) - 2 * ln(1 - z) * ln(-1 + z + x) * x * z - 2 * pow(ln(1 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 2 * pow(ln(1 - z), 2) * x * pow(z, -1) + 6 * pow(ln(1 - z), 2) * x * pow(NQCD, -2) - 6 * pow(ln(1 - z), 2) * x - 4 * pow(ln(1 - z), 2) * x * z * pow(NQCD, -2) + 4 * pow(ln(1 - z), 2) * x * z - 2 * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(1 - x) * x * pow(z, -1) + 8 * ln(1 - x) * x * pow(NQCD, -2) - 8 * ln(1 - x) * x - 6 * ln(1 - x) * x * z * pow(NQCD, -2) + 6 * ln(1 - x) * x * z - 4 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 4 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) + 10 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, -2) - 10 * ln(1 - x) * ln(1 - z) * x - 6 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, -2) + 6 * ln(1 - x) * ln(1 - z) * x * z - 2 * pow(ln(1 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 2 * pow(ln(1 - x), 2) * x * pow(z, -1) + 9. / 2. * pow(ln(1 - x), 2) * x * pow(NQCD, -2) + -9. / 2. * pow(ln(1 - x), 2) * x - 5. / 2. * pow(ln(1 - x), 2) * x * z * pow(NQCD, -2) + 5. / 2. * pow(ln(1 - x), 2) * x * z + 3 * ln(x) * x * pow(z, -1) * pow(NQCD, -2) - 3 * ln(x) * x * pow(z, -1) - 15 * ln(x) * x * pow(NQCD, -2) + 15 * ln(x) * x + 12 * ln(x) * x * z * pow(NQCD, -2) - 12 * ln(x) * x * z - ln(x) * ln(-1 + z + x) * x * pow(z, -1) * pow(NQCD, -2) + ln(x) * ln(-1 + z + x) * x * pow(z, -1) + 3 * ln(x) * ln(-1 + z + x) * x * pow(NQCD, -2) - 3 * ln(x) * ln(-1 + z + x) * x - 2 * ln(x) * ln(-1 + z + x) * x * z * pow(NQCD, -2) + 2 * ln(x) * ln(-1 + z + x) * x * z + 5 * ln(x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) - 5 * ln(x) * ln(1 - z) * x * pow(z, -1) - 15 * ln(x) * ln(1 - z) * x * pow(NQCD, -2) + 15 * ln(x) * ln(1 - z) * x + 10 * ln(x) * ln(1 - z) * x * z * pow(NQCD, -2) - 10 * ln(x) * ln(1 - z) * x * z + 5 * ln(x) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) - 5 * ln(x) * ln(1 - x) * x * pow(z, -1) - 14 * ln(x) * ln(1 - x) * x * pow(NQCD, -2) + 14 * ln(x) * ln(1 - x) * x + 9 * ln(x) * ln(1 - x) * x * z * pow(NQCD, -2) - 9 * ln(x) * ln(1 - x) * x * z + ln(x) * ln(z - x) * x * pow(NQCD, -2) - ln(x) * ln(z - x) * x - ln(x) * ln(z - x) * x * z * pow(NQCD, -2) + ln(x) * ln(z - x) * x * z - 3 * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) + 3 * pow(ln(x), 2) * x * pow(z, -1) + 9 * pow(ln(x), 2) * x * pow(NQCD, -2) - 9 * pow(ln(x), 2) * x - 6 * pow(ln(x), 2) * x * z * pow(NQCD, -2) + 6 * pow(ln(x), 2) * x * z + 4 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2) - 4 * ln(x) * ln(z) * x * pow(z, -1) - 13 * ln(x) * ln(z) * x * pow(NQCD, -2) + 13 * ln(x) * ln(z) * x + 9 * ln(x) * ln(z) * x * z * pow(NQCD, -2) - 9 * ln(x) * ln(z) * x * z - ln(z) * x * pow(z, -1) * pow(NQCD, -2) + ln(z) * x * pow(z, -1) + +7 * ln(z) * x * pow(NQCD, -2) - 7 * ln(z) * x - 6 * ln(z) * x * z * pow(NQCD, -2) + 6 * ln(z) * x * z - 3 * ln(z) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + 3 * ln(z) * ln(1 - z) * x * pow(z, -1) + 10 * ln(z) * ln(1 - z) * x * pow(NQCD, -2) - 10 * ln(z) * ln(1 - z) * x - 7 * ln(z) * ln(1 - z) * x * z * pow(NQCD, -2) + 7 * ln(z) * ln(1 - z) * x * z - 2 * ln(z) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + 2 * ln(z) * ln(1 - x) * x * pow(z, -1) + 7 * ln(z) * ln(1 - x) * x * pow(NQCD, -2) - 7 * ln(z) * ln(1 - x) * x - 5 * ln(z) * ln(1 - x) * x * z * pow(NQCD, -2) + 5 * ln(z) * ln(1 - x) * x * z - ln(z) * ln(z - x) * x * pow(NQCD, -2) + ln(z) * ln(z - x) * x + ln(z) * ln(z - x) * x * z * pow(NQCD, -2) - ln(z) * ln(z - x) * x * z - 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) + 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) + 5. / 2. * pow(ln(z), 2) * x * pow(NQCD, -2) - 5. / 2. * pow(ln(z), 2) * x - 2 * pow(ln(z), 2) * x * z * pow(NQCD, -2) + 2 * pow(ln(z), 2) * x * z + Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) - Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(z, -1) - 2 * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * pow(NQCD, -2) + 2 * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x + Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z * pow(NQCD, -2) - Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * z - Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) * pow(NQCD, -2) + Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(z, -1) + Li2(pow(z, -1) - x * pow(z, -1)) * x * pow(NQCD, -2) - Li2(pow(z, -1) - x * pow(z, -1)) * x + Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * pow(NQCD, -2) + -Li2(1 / (1 - x) - 1 / (1 - x) * z) * x - Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * z * pow(NQCD, -2) + Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * z - Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * pow(NQCD, -2) + Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x + Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * z * pow(NQCD, -2) - Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * z - Li2(z) * x * pow(z, -1) * pow(NQCD, -2) + Li2(z) * x * pow(z, -1) + 2 * Li2(z) * x * pow(NQCD, -2) - 2 * Li2(z) * x - Li2(z) * x * z * pow(NQCD, -2) + Li2(z) * x * z;

        res += tmp;
    }
    if (z > x) {
        double tmp = 0.0;
        tmp = 2 * x - 2 * x * pow(NQCD, 2) - x * z + x * z * pow(NQCD, 2) + 1. / 2. * pow(pi, 2) * x - 1. / 2. * pow(pi, 2) * x * pow(NQCD, 2) - 1. / 2. * pow(pi, 2) * x * z + 1. / 2. * pow(pi, 2) * x * z * pow(NQCD, 2) - ln(1 - z) * x + ln(1 - z) * x * pow(NQCD, 2) + 2 * ln(1 - z) * x * z - 2 * ln(1 - z) * x * z * pow(NQCD, 2) - 1. / 2. * pow(ln(1 - z), 2) * x + 1. / 2. * pow(ln(1 - z), 2) * x * pow(NQCD, 2) + 1. / 2. * pow(ln(1 - z), 2) * x * z - 1. / 2. * pow(ln(1 - z), 2) * x * z * pow(NQCD, 2) - 2 * ln(1 - x) * x + 2 * ln(1 - x) * x * pow(NQCD, 2) + 4 * ln(1 - x) * x * z - 4 * ln(1 - x) * x * z * pow(NQCD, 2) - 2 * ln(1 - x) * ln(1 - z) * x + 2 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, 2) + 2 * ln(1 - x) * ln(1 - z) * x * z - 2 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, 2) - 2 * pow(ln(1 - x), 2) * x + 2 * pow(ln(1 - x), 2) * x * pow(NQCD, 2) + 2 * pow(ln(1 - x), 2) * x * z - 2 * pow(ln(1 - x), 2) * x * z * pow(NQCD, 2) + 3 * ln(x) * x - 3 * ln(x) * x * pow(NQCD, 2) - 6 * ln(x) * x * z + 6 * ln(x) * x * z * pow(NQCD, 2) + 3 * ln(x) * ln(1 - z) * x - 3 * ln(x) * ln(1 - z) * x * pow(NQCD, 2) - 3 * ln(x) * ln(1 - z) * x * z + 3 * ln(x) * ln(1 - z) * x * z * pow(NQCD, 2) + 6 * ln(x) * ln(1 - x) * x - 6 * ln(x) * ln(1 - x) * x * pow(NQCD, 2) - 6 * ln(x) * ln(1 - x) * x * z + 6 * ln(x) * ln(1 - x) * x * z * pow(NQCD, 2) - ln(x) * ln(z - x) * x + ln(x) * ln(z - x) * x * pow(NQCD, 2) + ln(x) * ln(z - x) * x * z - ln(x) * ln(z - x) * x * z * pow(NQCD, 2) - 7. / 2. * pow(ln(x), 2) * x + 7. / 2. * pow(ln(x), 2) * x * pow(NQCD, 2) + 7. / 2. * pow(ln(x), 2) * x * z - 7. / 2. * pow(ln(x), 2) * x * z * pow(NQCD, 2) + 6 * ln(x) * ln(z) * x - 6 * ln(x) * ln(z) * x * pow(NQCD, 2) - 6 * ln(x) * ln(z) * x * z + 6 * ln(x) * ln(z) * x * z * pow(NQCD, 2) - 2 * ln(z) * x + 2 * ln(z) * x * pow(NQCD, 2) + +4 * ln(z) * x * z - 4 * ln(z) * x * z * pow(NQCD, 2) - ln(z) * ln(1 - z) * x + ln(z) * ln(1 - z) * x * pow(NQCD, 2) + ln(z) * ln(1 - z) * x * z - ln(z) * ln(1 - z) * x * z * pow(NQCD, 2) - 5 * ln(z) * ln(1 - x) * x + 5 * ln(z) * ln(1 - x) * x * pow(NQCD, 2) + 5 * ln(z) * ln(1 - x) * x * z - 5 * ln(z) * ln(1 - x) * x * z * pow(NQCD, 2) + ln(z) * ln(z - x) * x - ln(z) * ln(z - x) * x * pow(NQCD, 2) - ln(z) * ln(z - x) * x * z + ln(z) * ln(z - x) * x * z * pow(NQCD, 2) - 5. / 2. * pow(ln(z), 2) * x + 5. / 2. * pow(ln(z), 2) * x * pow(NQCD, 2) + 5. / 2. * pow(ln(z), 2) * x * z - 5. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, 2) + Li2(1 / (1 - x) - 1 / (1 - x) * z) * x - Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * pow(NQCD, 2) - Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * z + Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * z * pow(NQCD, 2) - Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * x + Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * x * pow(NQCD, 2) + Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * x * z - Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * x * z * pow(NQCD, 2) + Li2(z) * x - Li2(z) * x * pow(NQCD, 2) - Li2(z) * x * z + Li2(z) * x * z * pow(NQCD, 2);

        res += tmp;
    }
    if (z < x) {
        double tmp = 0.0;
        tmp = 2 * x - 2 * x * pow(NQCD, 2) - x * z + x * z * pow(NQCD, 2) + 1. / 2. * pow(pi, 2) * x - 1. / 2. * pow(pi, 2) * x * pow(NQCD, 2) - 1. / 2. * pow(pi, 2) * x * z + 1. / 2. * pow(pi, 2) * x * z * pow(NQCD, 2) - ln(1 - z) * x + ln(1 - z) * x * pow(NQCD, 2) + 2 * ln(1 - z) * x * z - 2 * ln(1 - z) * x * z * pow(NQCD, 2) - 1. / 2. * pow(ln(1 - z), 2) * x + 1. / 2. * pow(ln(1 - z), 2) * x * pow(NQCD, 2) + 1. / 2. * pow(ln(1 - z), 2) * x * z - 1. / 2. * pow(ln(1 - z), 2) * x * z * pow(NQCD, 2) - 2 * ln(1 - x) * x + 2 * ln(1 - x) * x * pow(NQCD, 2) + 4 * ln(1 - x) * x * z - 4 * ln(1 - x) * x * z * pow(NQCD, 2) - 2 * ln(1 - x) * ln(1 - z) * x + 2 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, 2) + 2 * ln(1 - x) * ln(1 - z) * x * z - 2 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, 2) - 2 * pow(ln(1 - x), 2) * x + 2 * pow(ln(1 - x), 2) * x * pow(NQCD, 2) + 2 * pow(ln(1 - x), 2) * x * z - 2 * pow(ln(1 - x), 2) * x * z * pow(NQCD, 2) + 3 * ln(x) * x - 3 * ln(x) * x * pow(NQCD, 2) - 6 * ln(x) * x * z + 6 * ln(x) * x * z * pow(NQCD, 2) + 4 * ln(x) * ln(1 - z) * x - 4 * ln(x) * ln(1 - z) * x * pow(NQCD, 2) - 4 * ln(x) * ln(1 - z) * x * z + 4 * ln(x) * ln(1 - z) * x * z * pow(NQCD, 2) + 5 * ln(x) * ln(1 - x) * x - 5 * ln(x) * ln(1 - x) * x * pow(NQCD, 2) - 5 * ln(x) * ln(1 - x) * x * z + 5 * ln(x) * ln(1 - x) * x * z * pow(NQCD, 2) - ln(x) * ln(-z + x) * x + ln(x) * ln(-z + x) * x * pow(NQCD, 2) + ln(x) * ln(-z + x) * x * z - ln(x) * ln(-z + x) * x * z * pow(NQCD, 2) - 3 * pow(ln(x), 2) * x + 3 * pow(ln(x), 2) * x * pow(NQCD, 2) + 3 * pow(ln(x), 2) * x * z - 3 * pow(ln(x), 2) * x * z * pow(NQCD, 2) + 5 * ln(x) * ln(z) * x - 5 * ln(x) * ln(z) * x * pow(NQCD, 2) - 5 * ln(x) * ln(z) * x * z + 5 * ln(x) * ln(z) * x * z * pow(NQCD, 2) - 2 * ln(z) * x + 2 * ln(z) * x * pow(NQCD, 2) + +4 * ln(z) * x * z - 4 * ln(z) * x * z * pow(NQCD, 2) - 2 * ln(z) * ln(1 - z) * x + 2 * ln(z) * ln(1 - z) * x * pow(NQCD, 2) + 2 * ln(z) * ln(1 - z) * x * z - 2 * ln(z) * ln(1 - z) * x * z * pow(NQCD, 2) - 4 * ln(z) * ln(1 - x) * x + 4 * ln(z) * ln(1 - x) * x * pow(NQCD, 2) + 4 * ln(z) * ln(1 - x) * x * z - 4 * ln(z) * ln(1 - x) * x * z * pow(NQCD, 2) + ln(z) * ln(-z + x) * x - ln(z) * ln(-z + x) * x * pow(NQCD, 2) - ln(z) * ln(-z + x) * x * z + ln(z) * ln(-z + x) * x * z * pow(NQCD, 2) - 2 * pow(ln(z), 2) * x + 2 * pow(ln(z), 2) * x * pow(NQCD, 2) + 2 * pow(ln(z), 2) * x * z - 2 * pow(ln(z), 2) * x * z * pow(NQCD, 2) - Li2(1 / (1 - z) - 1 / (1 - z) * x) * x + Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * pow(NQCD, 2) + Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * z - Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * z * pow(NQCD, 2) + Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * x - Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * x * pow(NQCD, 2) - Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * x * z + Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * x * z * pow(NQCD, 2) + Li2(z) * x - Li2(z) * x * pow(NQCD, 2) - Li2(z) * x * z + Li2(z) * x * z * pow(NQCD, 2);

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
        tmp = 3 + (- 1. / 4. * pow(z, -1) * pow(NQCD, -2)) + 1. / 2. * pow(z, -1) + (- 1. / 4. * pow(z, -1) * pow(NQCD, 2)) + (- 1. / 2. * pow(NQCD, -2)) + (- 5. / 2. * pow(NQCD, 2)) + (- 1. / 4. * z * pow(NQCD, -2)) + (- 3. / 2. * z) + 7. / 4. * z * pow(NQCD, 2) + pow(z, 2) * pow(NQCD, -2) + (- 2 * pow(z, 2)) + pow(z, 2) * pow(NQCD, 2) + (- 7. / 4. * x * pow(z, -1) * pow(NQCD, -2)) + 7. / 2. * x * pow(z, -1) + (- 7. / 4. * x * pow(z, -1) * pow(NQCD, 2)) + 33. / 4. * x * pow(NQCD, -2) + (- 16 * x) + 2 * x * pow(rln2, 2) + 31. / 4. * x * pow(NQCD, 2) + (- 2 * x * pow(NQCD, 2) * pow(rln2, 2)) + (- 13. / 2. * x * z * pow(NQCD, -2)) + 9 * x * z + 2 * x * z * pow(rln2, 2) + (- 5. / 2. * x * z * pow(NQCD, 2)) + (- 2 * x * z * pow(NQCD, 2) * pow(rln2, 2)) + 5. / 2. * x * pow(z, 2) + (- 5. / 2. * x * pow(z, 2) * pow(NQCD, 2)) + (- 2. / 3. * pow(pi, 2) * x * pow(z, -1) * pow(NQCD, -2)) + 2. / 3. * pow(pi, 2) * x * pow(z, -1) + 23. / 12. * pow(pi, 2) * x * pow(NQCD, -2) + (- 13. / 6. * pow(pi, 2) * x) + 1. / 4. * pow(pi, 2) * x * pow(NQCD, 2) + (- 7. / 6. * pow(pi, 2) * x * z * pow(NQCD, -2)) + 7. / 3. * pow(pi, 2) * x * z + (- 7. / 6. * pow(pi, 2) * x * z * pow(NQCD, 2)) + ln(1 - z) + (- 1. / 2. * ln(1 - z) * pow(NQCD, -2)) + (- 1. / 2. * ln(1 - z) * pow(NQCD, 2)) + (- 1. / 2. * ln(1 - z) * z * pow(NQCD, -2)) + 1. / 2. * ln(1 - z) * z * pow(NQCD, 2) + ln(1 - z) * pow(z, 2) * pow(NQCD, -2) + (- ln(1 - z) * pow(z, 2)) + 3. / 2. * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + (- 3. / 2. * ln(1 - z) * x * pow(z, -1) * pow(NQCD, 2)) + (- 31. / 4. * ln(1 - z) * x * pow(NQCD, -2)) + 15. / 2. * ln(1 - z) * x + 1. / 4. * ln(1 - z) * x * pow(NQCD, 2) + 25. / 4. * ln(1 - z) * x * z * pow(NQCD, -2) + (- 15. / 2. * ln(1 - z) * x * z) + 5. / 4. * ln(1 - z) * x * z * pow(NQCD, 2) + (- ln(1 - z) * x * pow(z, 2)) + ln(1 - z) * x * pow(z, 2) * pow(NQCD, 2) + 2 * pow(ln(1 - z), 2) * x * pow(z, -1) * pow(NQCD, -2) +  + (-2 * pow(ln(1 - z), 2) * x * pow(z, -1)) + (- 6 * pow(ln(1 - z), 2) * x * pow(NQCD, -2)) + 15. / 2. * pow(ln(1 - z), 2) * x + (- 3. / 2. * pow(ln(1 - z), 2) * x * pow(NQCD, 2)) + 4 * pow(ln(1 - z), 2) * x * z * pow(NQCD, -2) + (- 11. / 2. * pow(ln(1 - z), 2) * x * z) + 3. / 2. * pow(ln(1 - z), 2) * x * z * pow(NQCD, 2) + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * rln2) + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2) * rln2 + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * rln2) + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2) * rln2 + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2)) + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z + (- 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2)) + (- ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * pow(NQCD, -2)) + ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) + (- ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, -2)) + (- ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x) + 2 * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, 2) +  + (-2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * rln2) + 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2) * rln2 + (- 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * rln2) + 2 * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2) * rln2 + ln(1 - x) + (- 1. / 2. * ln(1 - x) * pow(NQCD, -2)) + (- 1. / 2. * ln(1 - x) * pow(NQCD, 2)) + 1. / 2. * ln(1 - x) * z * pow(NQCD, -2) + (- ln(1 - x) * z) + 1. / 2. * ln(1 - x) * z * pow(NQCD, 2) + 3. / 2. * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + (- 3. / 2. * ln(1 - x) * x * pow(z, -1) * pow(NQCD, 2)) + (- 27. / 4. * ln(1 - x) * x * pow(NQCD, -2)) + 17. / 2. * ln(1 - x) * x + (- 7. / 4. * ln(1 - x) * x * pow(NQCD, 2)) + 21. / 4. * ln(1 - x) * x * z * pow(NQCD, -2) + (- 19. / 2. * ln(1 - x) * x * z) + 17. / 4. * ln(1 - x) * x * z * pow(NQCD, 2) + (- ln(1 - x) * x * pow(z, 2)) + ln(1 - x) * x * pow(z, 2) * pow(NQCD, 2) + 3 * ln(1 - x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + (- 3 * ln(1 - x) * ln(1 - z) * x * pow(z, -1)) + (- 9 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, -2)) + 13 * ln(1 - x) * ln(1 - z) * x + (- 4 * ln(1 - x) * ln(1 - z) * x * pow(NQCD, 2)) + 6 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, -2) + (- 10 * ln(1 - x) * ln(1 - z) * x * z) + 4 * ln(1 - x) * ln(1 - z) * x * z * pow(NQCD, 2) + 2 * pow(ln(1 - x), 2) * x * pow(z, -1) * pow(NQCD, -2) + (- 2 * pow(ln(1 - x), 2) * x * pow(z, -1)) + (- 5 * pow(ln(1 - x), 2) * x * pow(NQCD, -2)) + 15. / 2. * pow(ln(1 - x), 2) * x + (- 5. / 2. * pow(ln(1 - x), 2) * x * pow(NQCD, 2)) + 3 * pow(ln(1 - x), 2) * x * z * pow(NQCD, -2) + (- 11. / 2. * pow(ln(1 - x), 2) * x * z) + 5. / 2. * pow(ln(1 - x), 2) * x * z * pow(NQCD, 2) +  +  + (- ln(x)) + 1. / 2. * ln(x) * pow(NQCD, -2) + 1. / 2. * ln(x) * pow(NQCD, 2) + 1. / 2. * ln(x) * z * pow(NQCD, -2) + (- 1. / 2. * ln(x) * z * pow(NQCD, 2)) + (- ln(x) * pow(z, 2) * pow(NQCD, -2)) + ln(x) * pow(z, 2) + (- 11. / 4. * ln(x) * x * pow(z, -1) * pow(NQCD, -2)) + ln(x) * x * pow(z, -1) + 7. / 4. * ln(x) * x * pow(z, -1) * pow(NQCD, 2) + 51. / 4. * ln(x) * x * pow(NQCD, -2) + (- 35. / 2. * ln(x) * x) + ln(x) * x * rln2 + 19. / 4. * ln(x) * x * pow(NQCD, 2) + (- ln(x) * x * pow(NQCD, 2) * rln2) + (- 10 * ln(x) * x * z * pow(NQCD, -2)) + 35. / 2. * ln(x) * x * z + ln(x) * x * z * rln2 + (- 15. / 2. * ln(x) * x * z * pow(NQCD, 2)) + (- ln(x) * x * z * pow(NQCD, 2) * rln2) + 2 * ln(x) * x * pow(z, 2) + (- 2 * ln(x) * x * pow(z, 2) * pow(NQCD, 2)) + (- 5 * ln(x) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2)) + 5 * ln(x) * ln(1 - z) * x * pow(z, -1) + 31. / 2. * ln(x) * ln(1 - z) * x * pow(NQCD, -2) + (- 21 * ln(x) * ln(1 - z) * x) + 11. / 2. * ln(x) * ln(1 - z) * x * pow(NQCD, 2) + (- 21. / 2. * ln(x) * ln(1 - z) * x * z * pow(NQCD, -2)) + 16 * ln(x) * ln(1 - z) * x * z + (- 11. / 2. * ln(x) * ln(1 - z) * x * z * pow(NQCD, 2)) + (- ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x) + ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2) + (- ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z) + ln(x) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2) + (- 5 * ln(x) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2)) +  + 5 * ln(x) * ln(1 - x) * x * pow(z, -1) + 14 * ln(x) * ln(1 - x) * x * pow(NQCD, -2) + (- 21 * ln(x) * ln(1 - x) * x) + 7 * ln(x) * ln(1 - x) * x * pow(NQCD, 2) + (- 9 * ln(x) * ln(1 - x) * x * z * pow(NQCD, -2)) + 16 * ln(x) * ln(1 - x) * x * z + (- 7 * ln(x) * ln(1 - x) * x * z * pow(NQCD, 2)) + 7. / 2. * pow(ln(x), 2) * x * pow(z, -1) * pow(NQCD, -2) + (- 7. / 2. * pow(ln(x), 2) * x * pow(z, -1)) + (- 11 * pow(ln(x), 2) * x * pow(NQCD, -2)) + 15 * pow(ln(x), 2) * x + (- 4 * pow(ln(x), 2) * x * pow(NQCD, 2)) + 15. / 2. * pow(ln(x), 2) * x * z * pow(NQCD, -2) + (- 23. / 2. * pow(ln(x), 2) * x * z) + 4 * pow(ln(x), 2) * x * z * pow(NQCD, 2) + (- 3 * ln(x) * ln(z) * x * pow(z, -1) * pow(NQCD, -2)) + 3 * ln(x) * ln(z) * x * pow(z, -1) + 10 * ln(x) * ln(z) * x * pow(NQCD, -2) + (- 18 * ln(x) * ln(z) * x) + 8 * ln(x) * ln(z) * x * pow(NQCD, 2) + (- 17. / 2. * ln(x) * ln(z) * x * z * pow(NQCD, -2)) + 8 * ln(x) * ln(z) * x * z + 1. / 2. * ln(x) * ln(z) * x * z * pow(NQCD, 2) + 1. / 2. * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * pow(NQCD, -2) + (- 1. / 2. * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1)) + 1. / 2. * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, -2) + 1. / 2. * ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x + (- ln(x) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, 2)) + 3 * ln(z) + (- ln(z) * pow(NQCD, -2)) + (- 2 * ln(z) * pow(NQCD, 2)) + 2 * ln(z) * z + (- 2 * ln(z) * z * pow(NQCD, 2)) + 5. / 2. * ln(z) * x * pow(z, -1) +  + (-5. / 2. * ln(z) * x * pow(z, -1) * pow(NQCD, 2)) + (- 7 * ln(z) * x * pow(NQCD, -2)) + 10 * ln(z) * x + 3 * ln(z) * x * rln2 + (- 3 * ln(z) * x * pow(NQCD, 2)) + (- 3 * ln(z) * x * pow(NQCD, 2) * rln2) + 15. / 2. * ln(z) * x * z * pow(NQCD, -2) + (- 33. / 2. * ln(z) * x * z) + 3 * ln(z) * x * z * rln2 + 9 * ln(z) * x * z * pow(NQCD, 2) + (- 3 * ln(z) * x * z * pow(NQCD, 2) * rln2) + (- ln(z) * x * pow(z, 2)) + ln(z) * x * pow(z, 2) * pow(NQCD, 2) + ln(z) * ln(1 - z) * x * pow(z, -1) * pow(NQCD, -2) + (- ln(z) * ln(1 - z) * x * pow(z, -1)) + (- 6 * ln(z) * ln(1 - z) * x * pow(NQCD, -2)) + 11 * ln(z) * ln(1 - z) * x + (- 5 * ln(z) * ln(1 - z) * x * pow(NQCD, 2)) + 5 * ln(z) * ln(1 - z) * x * z * pow(NQCD, -2) + (- 10 * ln(z) * ln(1 - z) * x * z) + 5 * ln(z) * ln(1 - z) * x * z * pow(NQCD, 2) + (- ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x) + ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2) + (- ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z) + ln(z) * ln(1 - z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2) + (- 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x) + 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2) + (- 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z) + 2 * ln(z) * ln(1 + z + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2) + 2 * ln(z) * ln(1 - x) * x * pow(z, -1) * pow(NQCD, -2) + (- 2 * ln(z) * ln(1 - x) * x * pow(z, -1)) + (- 6 * ln(z) * ln(1 - x) * x * pow(NQCD, -2)) + 12 * ln(z) * ln(1 - x) * x + (- 6 * ln(z) * ln(1 - x) * x * pow(NQCD, 2)) + 9. / 2. * ln(z) * ln(1 - x) * x * z * pow(NQCD, -2) + (- 5 * ln(z) * ln(1 - x) * x * z) + 1. / 2. * ln(z) * ln(1 - x) * x * z * pow(NQCD, 2) +  + 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) * pow(NQCD, -2) + (- 1. / 2. * pow(ln(z), 2) * x * pow(z, -1)) + (- 5. / 2. * pow(ln(z), 2) * x * pow(NQCD, -2)) + 13. / 2. * pow(ln(z), 2) * x + (- 4 * pow(ln(z), 2) * x * pow(NQCD, 2)) + 5. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, -2) + pow(ln(z), 2) * x * z + (- 7. / 2. * pow(ln(z), 2) * x * z * pow(NQCD, 2)) + 1. / 2. * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * pow(NQCD, -2) + (- 1. / 2. * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1)) + 1. / 2. * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, -2) + 1. / 2. * ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x + (- ln(z) * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, 2)) + Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x + (- Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * pow(NQCD, 2)) + Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * z + (- Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * z * pow(NQCD, 2)) + (- Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x) + Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * pow(NQCD, 2) + (- Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * z) +  + Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1)) * x * z * pow(NQCD, 2) + (- Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x) + Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2) + (- Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z) + Li2(1. / 2. - 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2) + Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x + (- Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * pow(NQCD, 2)) + Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z + (- Li2(1. / 2. + 1. / 2. * z - 1. / 2. * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z)) * x * z * pow(NQCD, 2)) + Li2(1 - x * pow(z, -1)) * x * pow(NQCD, -2) + (- 2 * Li2(1 - x * pow(z, -1)) * x) + Li2(1 - x * pow(z, -1)) * x * pow(NQCD, 2) + (- Li2(1 - x * pow(z, -1)) * x * z * pow(NQCD, -2)) + 2 * Li2(1 - x * pow(z, -1)) * x * z + (- Li2(1 - x * pow(z, -1)) * x * z * pow(NQCD, 2)) + (- 1. / 2. * Li2(x) * x * pow(NQCD, -2)) + 1. / 2. * Li2(x) * x * pow(NQCD, 2) + 1. / 2. * Li2(x) * x * z * pow(NQCD, -2) + (- 1. / 2. * Li2(x) * x * z * pow(NQCD, 2)) + (- Li2(z) * x * pow(z, -1) * pow(NQCD, -2)) + Li2(z) * x * pow(z, -1) + Li2(z) * x * pow(NQCD, -2) + (- Li2(z) * x) + (- 1. / 2. * Li2(z) * x * z * pow(NQCD, -2)) + (- 5 * Li2(z) * x * z) + 11. / 2. * Li2(z) * x * z * pow(NQCD, 2) + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * pow(NQCD, -2) * rln2 + (- mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * rln2) + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, -2) * rln2 +  + mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * rln2 + (- 2 * mysqrt(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NQCD, 2) * rln2) + (- 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * z * pow(NQCD, -2)) + 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * z + 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 2) * pow(NQCD, -2) + (- 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 2)) + (- 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 3) * pow(NQCD, -2)) + 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 3) + 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 4) * pow(NQCD, -2) + (- 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 4)) + 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * z * pow(NQCD, -2) + (- 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * z) + (- 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * pow(NQCD, -2)) + 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) + 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) * pow(NQCD, -2) + (- 3 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 3)) + (- 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 4) * pow(NQCD, -2)) + 1 / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 4) + 1 / (1 - z - x) * z * pow(NQCD, -2) + (- 1 / (1 - z - x) * z) + (- 2 / (1 - z - x) * pow(z, 2) * pow(NQCD, -2)) + 2 / (1 - z - x) * pow(z, 2) + 1 / (1 - z - x) * pow(z, 3) * pow(NQCD, -2) +  + (-1 / (1 - z - x) * pow(z, 3)) + 2 / (1 - z - x) * ln(1 - z) * z * pow(NQCD, -2) + (- 2 / (1 - z - x) * ln(1 - z) * z) + (- 4 / (1 - z - x) * ln(1 - z) * pow(z, 2) * pow(NQCD, -2)) + 4 / (1 - z - x) * ln(1 - z) * pow(z, 2) + 2 / (1 - z - x) * ln(1 - z) * pow(z, 3) * pow(NQCD, -2) + (- 2 / (1 - z - x) * ln(1 - z) * pow(z, 3)) + (- 2 / (1 - z - x) * ln(x) * z * pow(NQCD, -2)) + 2 / (1 - z - x) * ln(x) * z + 4 / (1 - z - x) * ln(x) * pow(z, 2) * pow(NQCD, -2) + (- 4 / (1 - z - x) * ln(x) * pow(z, 2)) + (- 2 / (1 - z - x) * ln(x) * pow(z, 3) * pow(NQCD, -2)) + 2 / (1 - z - x) * ln(x) * pow(z, 3);
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
        tmp = lmua * x * pow(z, -1) * pow(NQCD, -2) + (- 4 * lmua * x * pow(z, -1)) + 3 * lmua * x * pow(z, -1) * pow(NQCD, 2) + (- 2 * lmua * x * pow(NQCD, -2)) + (- 5. / 3. * lmua * x) + 11. / 3. * lmua * x * pow(NQCD, 2) + 2. / 3. * lmua * x * NF * pow(NQCD, -1) + (- 2. / 3. * lmua * x * NF * NQCD) + lmua * x * z * pow(NQCD, -2) + 11. / 3. * lmua * x * z + (- 14. / 3. * lmua * x * z * pow(NQCD, 2)) + (- 2. / 3. * lmua * x * z * NF * pow(NQCD, -1)) + 2. / 3. * lmua * x * z * NF * NQCD + 2 * lmua * x * pow(z, 2) + (- 2 * lmua * x * pow(z, 2) * pow(NQCD, 2)) + (- 4 * lmua * ln(1 - z) * x) + 4 * lmua * ln(1 - z) * x * pow(NQCD, 2) + 4 * lmua * ln(1 - z) * x * z + (- 4 * lmua * ln(1 - z) * x * z * pow(NQCD, 2)) + (-4 * ln(z) * lmua * x) + 4 * ln(z) * lmua * x * pow(NQCD, 2) + (- ln(z) * lmua * x * z * pow(NQCD, -2)) + (- 6 * ln(z) * lmua * x * z) + 7 * ln(z) * lmua * x * z * pow(NQCD, 2);
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
        tmp = (- 2 * lmuf) + lmuf * pow(NQCD, -2) + lmuf * pow(NQCD, 2) + (- lmuf * z * pow(NQCD, -2)) + 2 * lmuf * z + (- lmuf * z * pow(NQCD, 2)) + 1. / 2. * lmuf * x * pow(NQCD, -2) + (- lmuf * x) + 1. / 2. * lmuf * x * pow(NQCD, 2) + (- 1. / 2. * lmuf * x * z * pow(NQCD, -2)) + lmuf * x * z + (- 1. / 2. * lmuf * x * z * pow(NQCD, 2)) + 2 * lmuf * ln(1 - x) * x * pow(NQCD, -2) + (- 4 * lmuf * ln(1 - x) * x) + 2 * lmuf * ln(1 - x) * x * pow(NQCD, 2) + (- 2 * lmuf * ln(1 - x) * x * z * pow(NQCD, -2)) + 4 * lmuf * ln(1 - x) * x * z + (- 2 * lmuf * ln(1 - x) * x * z * pow(NQCD, 2)) + (- ln(x) * lmuf * x * pow(NQCD, -2)) + 2 * ln(x) * lmuf * x + (- ln(x) * lmuf * x * pow(NQCD, 2)) + ln(x) * lmuf * x * z * pow(NQCD, -2) + (- 2 * ln(x) * lmuf * x * z) + ln(x) * lmuf * x * z * pow(NQCD, 2);
        res += tmp;
    }

    return res;
}

double RG_RG_100(double x, double z, double NF) {

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

        double pt0 = RG_RG_100(x0, z0, NF);
        double pt1 = RG_RG_100(x1, z1, NF);
        double pt2 = RG_RG_100(x2, z2, NF);

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

        double pt0 = RG_RG_100(x0, z0, NF);
        double pt1 = RG_RG_100(x1, z1, NF);
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

        double pt0 = RG_RG_100(x0, z0, NF);
        double pt1 = RG_RG_100(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = 11. / 3. * lmur * x + (- 11. / 3. * lmur * x * pow(NQCD, 2)) + (-2. / 3. * lmur * x * NF * pow(NQCD, -1)) + 2. / 3. * lmur * x * NF * NQCD + (- 11. / 3. * lmur * x * z) + 11. / 3. * lmur * x * z * pow(NQCD, 2) + 2. / 3. * lmur * x * z * NF * pow(NQCD, -1) + (- 2. / 3. * lmur * x * z * NF * NQCD);
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - RG_RG: 000, 001, 010, 100
*/

/*
  Inverted Branch Report (By Number):
  - 000: RG_RG
  - 001: RG_RG
  - 010: RG_RG
  - 100: RG_RG
*/
