#include "../sidis.h"

double cl_nnlo_g2g_eq(double x, double z, double Q, int rsl, int orders) {

    double result = 0.0;

    double omz = 1.0 - z;
    double opz = 1.0 + z;
    double omx = 1.0 - x;
    double opx = 1.0 + x;
    double op6xpxsq = 1.0 + 6.0 * x + x * x;
    double xmz = x - z;
    double omxmz = 1.0 - x - z;
    double poly2 = 1 + 2 * x + x * x - 4 * x * z;
    double sqrtxz1 = sqrt(1 - 2 * z + z * z + 4 * x * z);
    double sqrtxz2 = sqrt(poly2);
    double sqrtxz3 = sqrt(x / z);


    if (rsl == 77) {

        double tiny = 1E-4;
        double tinyinv = 1. / tiny;

        double u = x + z;
        double v = x - z;

        if (std::abs(v) <= tiny && u >= 2 - tiny) {
            result = 0.;
        } else if (std::abs(v) <= tiny && u <= tiny) {
            result = 0.;
        } else if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
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

            double pt0 = cl_nnlo_g2g_eq(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_g2g_eq(x1, z1, Q, rsl, orders);
            double pt2 = cl_nnlo_g2g_eq(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = cl_nnlo_g2g_eq(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_g2g_eq(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        } else if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
            result = 0.;
        } else if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
            result = 0.;
        } else if (std::abs(u - 1.) < .99 * tiny) {
            double u0 = 1. - tiny;
            double u1 = 1. + tiny;

            double x0 = .5 * (u0 + v);
            double z0 = .5 * (u0 - v);
            double x1 = .5 * (u1 + v);
            double z1 = .5 * (u1 - v);

            double pt0 = cl_nnlo_g2g_eq(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_g2g_eq(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 922000) {
            if (z != x && z != 1. - x) {
                result += (4.0 / 3.0 * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2) * pow(opx, -1) - 4.0 / 3.0 * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2) + 4 * pow(NC, -1) - 4 * pow(NC, -1) * z + 8.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * pow(opx, -1) - 4.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) - 16 * pow(NC, -1) * x * pow(z, -1) + 28 * pow(NC, -1) * x - 16 * pow(NC, -1) * x * pow(rln2, 2) - 2.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) - 12 * pow(NC, -1) * x * z + 16 * pow(NC, -1) * x * z * pow(rln2, 2) + 4.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * pow(opx, -1) - 2.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) + 16 * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 32 * pow(NC, -1) * pow(x, 2) + 16 * pow(NC, -1) * pow(x, 2) * pow(rln2, 2) + 16 * pow(NC, -1) * pow(x, 2) * z - 16 * pow(NC, -1) * pow(x, 2) * z * pow(rln2, 2) + 4.0 / 3.0 * pow(NC, -1) * pow(x, 2) * z * pow(pi, 2) + 3.0 / 4.0 * NC * pow(x, -1) * pow(z, -1) - 3.0 / 4.0 * NC * pow(x, -1) + 4.0 / 3.0 * NC * pow(x, -1) * pow(pi, 2) * pow(opx, -1) - 4.0 / 3.0 * NC * pow(x, -1) * pow(pi, 2) - 4.0 / 3.0 * NC * pow(x, -1) * z * pow(pi, 2) * pow(opx, -1) + 4.0 / 3.0 * NC * pow(x, -1) * z * pow(pi, 2) + 3.0 / 4.0 * NC * pow(z, -2) - 7.0 / 2.0 * NC * pow(z, -1) - 5.0 / 2.0 * NC + 8.0 / 3.0 * NC * pow(pi, 2) * pow(opx, -1) - 4.0 / 3.0 * NC * pow(pi, 2) + 21.0 / 4.0 * NC * z - 8.0 / 3.0 * NC * z * pow(pi, 2) * pow(opx, -1) + 4.0 / 3.0 * NC * z * pow(pi, 2) - 3.0 / 4.0 * NC * x * pow(z, -2) - 25.0 / 2.0 * NC * x * pow(z, -1) - 16 * NC * x * pow(z, -1) * sqrtxz1 * rln2 + 5.0 / 2.0 * NC * x + 4.0 / 3.0 * NC * x * pow(pi, 2) * pow(opx, -1) + 2.0 / 3.0 * NC * x * pow(pi, 2) + 43.0 / 4.0 * NC * x * z - 16 * NC * x * z * pow(rln2, 2) - 4.0 / 3.0 * NC * x * z * pow(pi, 2) * pow(opx, -1) + 2.0 / 3.0 * NC * x * z * pow(pi, 2) + 61.0 / 4.0 * NC * pow(x, 2) * pow(z, -1) + 16 * NC * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2 + 3.0 / 4.0 * NC * pow(x, 2) - 16 * NC * pow(x, 2) * z);
                result += (+16 * NC * pow(x, 2) * z * pow(rln2, 2) - 4.0 / 3.0 * NC * pow(x, 2) * z * pow(pi, 2) + 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 - 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * sqrtxz3 + 6 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 - 30 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 - 3.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -2) * sqrtxz3 + 1.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3 - 7.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3 - 3.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z, -2) * sqrtxz3 - 7 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * sqrtxz3 - 19.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3 - 15.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3 + 105.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * z * sqrtxz3 - 35.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3);
                result += (-2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 + 2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * sqrtxz3 - 6 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 + 30 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 + 3.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -2) * sqrtxz3 - 1.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3 + 7.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3 + 3.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z, -2) * sqrtxz3 + 7 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * sqrtxz3 + 19.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + 15.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3 - 105.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * z * sqrtxz3 + 35.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, 2) * sqrtxz3 - InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 + InvTanInt(-sqrtxz3) * pow(NC, -1) * sqrtxz3 - 3 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 + 15 * InvTanInt(-sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 + 3.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -2) * sqrtxz3 - 1.0 / 4.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3 + 7.0 / 4.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3 + 3.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * pow(z, -2) * sqrtxz3 + 7.0 / 2.0 * InvTanInt(-sqrtxz3) * NC * sqrtxz3 + 19.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + 15.0 / 4.0 * InvTanInt(-sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3 - 105.0 / 4.0 * InvTanInt(-sqrtxz3) * NC * x * z * sqrtxz3 + 35.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * pow(x, 2) * sqrtxz3);
                result += (-2 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 + 2 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * sqrtxz3 - 6 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 + 30 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 + 3.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -2) * sqrtxz3 - 1.0 / 2.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3 + 7.0 / 2.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3 + 3.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * pow(z, -2) * sqrtxz3 + 7 * InvTanInt(z * sqrtxz3) * NC * sqrtxz3 + 19.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + 15.0 / 2.0 * InvTanInt(z * sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3 - 105.0 / 2.0 * InvTanInt(z * sqrtxz3) * NC * x * z * sqrtxz3 + 35.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3 + InvTanInt(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 - InvTanInt(sqrtxz3) * pow(NC, -1) * sqrtxz3 + 3 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 - 15 * InvTanInt(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 - 3.0 / 8.0 * InvTanInt(sqrtxz3) * NC * pow(x, -2) * sqrtxz3 + 1.0 / 4.0 * InvTanInt(sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3 - 7.0 / 4.0 * InvTanInt(sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3 - 3.0 / 8.0 * InvTanInt(sqrtxz3) * NC * pow(z, -2) * sqrtxz3 - 7.0 / 2.0 * InvTanInt(sqrtxz3) * NC * sqrtxz3 - 19.0 / 8.0 * InvTanInt(sqrtxz3) * NC * pow(z, 2) * sqrtxz3 - 15.0 / 4.0 * InvTanInt(sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3 + 105.0 / 4.0 * InvTanInt(sqrtxz3) * NC * x * z * sqrtxz3 - 35.0 / 8.0 * InvTanInt(sqrtxz3) * NC * pow(x, 2) * sqrtxz3 + 24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * rln2 - 24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * rln2 - 24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * rln2);
                result += (+24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * rln2 + 16 * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1) * sqrtxz1 - 8 * ln(1 + sqrtxz1 - z) * NC * x * rln2 + 24 * ln(1 + sqrtxz1 - z) * NC * x * z * rln2 - 16 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1 + 8 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * rln2 - 24 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z * rln2 - 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * z + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) - 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * z + 8 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x - 8 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x * z - 8 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(x, 2) + 8 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(x, 2) * z - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * z + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z + 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * rln2 - 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * rln2 - 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * rln2 + 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * rln2 + 8 * ln(1 + sqrtxz1 + z) * NC * x * rln2 + 8 * ln(1 + sqrtxz1 + z) * NC * x * z * rln2);
                result += (-8 * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * rln2 - 8 * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z * rln2 + 16 * ln(x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) - 16 * ln(x) * pow(NC, -1) * pow(x, -1) * z + 3 * ln(x) * pow(NC, -1) + 32 * ln(x) * pow(NC, -1) * z * pow(opx, -1) - 19 * ln(x) * pow(NC, -1) * z + 8 * ln(x) * pow(NC, -1) * x * pow(z, -1) + 5 * ln(x) * pow(NC, -1) * x - 16 * ln(x) * pow(NC, -1) * x * rln2 + 16 * ln(x) * pow(NC, -1) * x * z * pow(opx, -1) - 13 * ln(x) * pow(NC, -1) * x * z + 16 * ln(x) * pow(NC, -1) * x * z * rln2 - 8 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 16 * ln(x) * pow(NC, -1) * pow(x, 2) * rln2 + 8 * ln(x) * pow(NC, -1) * pow(x, 2) * z - 16 * ln(x) * pow(NC, -1) * pow(x, 2) * z * rln2 - 3.0 / 8.0 * ln(x) * NC * pow(x, -1) * pow(z, -1) + 16 * ln(x) * NC * pow(x, -1) * pow(opx, -1) - 125.0 / 8.0 * ln(x) * NC * pow(x, -1) - 16 * ln(x) * NC * pow(x, -1) * z * pow(opx, -1) + 16 * ln(x) * NC * pow(x, -1) * z + 3.0 / 8.0 * ln(x) * NC * pow(z, -2) - 1.0 / 4.0 * ln(x) * NC * pow(z, -1) + 32 * ln(x) * NC * pow(opx, -1) - 79.0 / 4.0 * ln(x) * NC - 32 * ln(x) * NC * z * pow(opx, -1) + 157.0 / 8.0 * ln(x) * NC * z + 3.0 / 8.0 * ln(x) * NC * x * pow(z, -2) - 49.0 / 4.0 * ln(x) * NC * x * pow(z, -1) - 8 * ln(x) * NC * x * pow(z, -1) * sqrtxz1 + 16 * ln(x) * NC * x * pow(opx, -1) - 7.0 / 4.0 * ln(x) * NC * x + 8 * ln(x) * NC * x * rln2 - 16 * ln(x) * NC * x * z * pow(opx, -1) + 109.0 / 8.0 * ln(x) * NC * x * z - 16 * ln(x) * NC * x * z * rln2 + 29.0 / 8.0 * ln(x) * NC * pow(x, 2) * pow(z, -1) + 8 * ln(x) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1 + 35.0 / 8.0 * ln(x) * NC * pow(x, 2) - 8 * ln(x) * NC * pow(x, 2) * rln2 - 8 * ln(x) * NC * pow(x, 2) * z + 16 * ln(x) * NC * pow(x, 2) * z * rln2);
                result += (+8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x - 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z - 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z - 8 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x + 8 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x * z + 8 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) - 8 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z + 8 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * z - 8 * ln(x) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z - 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * z - 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z - 8 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC + 8 * ln(x) * ln(1 + x * pow(z, -1)) * NC * z * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * z);
                result += (-4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x + 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x * z * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x * z - 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * z - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z - 8 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * z * pow(opx, -1) - 8 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * z - 4 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) + 4 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * z * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * z - 8 * ln(x) * ln(1 + x * z) * NC * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * NC + 8 * ln(x) * ln(1 + x * z) * NC * z * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * NC * z - 4 * ln(x) * ln(1 + x * z) * NC * x * pow(opx, -1) - 8 * ln(x) * ln(1 + x * z) * NC * x + 4 * ln(x) * ln(1 + x * z) * NC * x * z * pow(opx, -1) + 8 * ln(x) * ln(1 + x * z) * NC * pow(x, 2) * z - 4 * ln(x) * ln(z + x) * pow(NC, -1) * x * z + 4 * ln(x) * ln(z + x) * pow(NC, -1) * pow(x, 2) * z + 4 * ln(x) * ln(z + x) * NC * x + 4 * ln(x) * ln(z + x) * NC * x * z - 4 * ln(x) * ln(z + x) * NC * pow(x, 2) - 4 * ln(x) * ln(z + x) * NC * pow(x, 2) * z - 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z - 12 * pow(ln(x), 2) * pow(NC, -1) * z * pow(opx, -1) + 6 * pow(ln(x), 2) * pow(NC, -1) * z + 2 * pow(ln(x), 2) * pow(NC, -1) * x - 6 * pow(ln(x), 2) * pow(NC, -1) * x * z * pow(opx, -1));
                result += (-2 * pow(ln(x), 2) * pow(NC, -1) * x * z + 2 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) - 2 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z - 6 * pow(ln(x), 2) * NC * pow(x, -1) * pow(opx, -1) + 6 * pow(ln(x), 2) * NC * pow(x, -1) + 6 * pow(ln(x), 2) * NC * pow(x, -1) * z * pow(opx, -1) - 6 * pow(ln(x), 2) * NC * pow(x, -1) * z - 12 * pow(ln(x), 2) * NC * pow(opx, -1) + 6 * pow(ln(x), 2) * NC + 12 * pow(ln(x), 2) * NC * z * pow(opx, -1) - 6 * pow(ln(x), 2) * NC * z - 6 * pow(ln(x), 2) * NC * x * pow(opx, -1) - 2 * pow(ln(x), 2) * NC * x + 6 * pow(ln(x), 2) * NC * x * z * pow(opx, -1) + 2 * pow(ln(x), 2) * NC * x * z - 2 * pow(ln(x), 2) * NC * pow(x, 2) + 2 * pow(ln(x), 2) * NC * pow(x, 2) * z + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z + 8 * ln(x) * ln(z) * pow(NC, -1) * z * pow(opx, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * z + 4 * ln(x) * ln(z) * pow(NC, -1) * x + 4 * ln(x) * ln(z) * pow(NC, -1) * x * z * pow(opx, -1) + 8 * ln(x) * ln(z) * pow(NC, -1) * x * z - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * z + 4 * ln(x) * ln(z) * NC * pow(x, -1) * pow(opx, -1) - 4 * ln(x) * ln(z) * NC * pow(x, -1) - 4 * ln(x) * ln(z) * NC * pow(x, -1) * z * pow(opx, -1) + 4 * ln(x) * ln(z) * NC * pow(x, -1) * z + 8 * ln(x) * ln(z) * NC * pow(opx, -1) - 4 * ln(x) * ln(z) * NC - 8 * ln(x) * ln(z) * NC * z * pow(opx, -1) + 4 * ln(x) * ln(z) * NC * z + 4 * ln(x) * ln(z) * NC * x * pow(opx, -1) - 16 * ln(x) * ln(z) * NC * x - 4 * ln(x) * ln(z) * NC * x * z * pow(opx, -1) - 8 * ln(x) * ln(z) * NC * x * z + 4 * ln(x) * ln(z) * NC * pow(x, 2) + 4 * ln(x) * ln(z) * NC * pow(x, 2) * z - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z - 16 * ln(x) * ln(omx) * pow(NC, -1) * z * pow(opx, -1));
                result += (+8 * ln(x) * ln(omx) * pow(NC, -1) * z - 4 * ln(x) * ln(omx) * pow(NC, -1) * x - 8 * ln(x) * ln(omx) * pow(NC, -1) * x * z * pow(opx, -1) + 4 * ln(x) * ln(omx) * pow(NC, -1) * x * z + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * z - 8 * ln(x) * ln(omx) * NC * pow(x, -1) * pow(opx, -1) + 8 * ln(x) * ln(omx) * NC * pow(x, -1) + 8 * ln(x) * ln(omx) * NC * pow(x, -1) * z * pow(opx, -1) - 8 * ln(x) * ln(omx) * NC * pow(x, -1) * z - 16 * ln(x) * ln(omx) * NC * pow(opx, -1) + 8 * ln(x) * ln(omx) * NC + 16 * ln(x) * ln(omx) * NC * z * pow(opx, -1) - 8 * ln(x) * ln(omx) * NC * z - 8 * ln(x) * ln(omx) * NC * x * pow(opx, -1) + 4 * ln(x) * ln(omx) * NC * x + 8 * ln(x) * ln(omx) * NC * x * z * pow(opx, -1) - 4 * ln(x) * ln(omx) * NC * x * z - 4 * ln(x) * ln(omx) * NC * pow(x, 2) + 4 * ln(x) * ln(omx) * NC * pow(x, 2) * z - 4 * ln(x) * ln(omz) * pow(NC, -1) * x + 4 * ln(x) * ln(omz) * pow(NC, -1) * x * z + 4 * ln(x) * ln(omz) * NC * x - 4 * ln(x) * ln(omz) * NC * x * z + 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) - 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z + 16 * ln(x) * ln(opx) * pow(NC, -1) * z * pow(opx, -1) - 8 * ln(x) * ln(opx) * pow(NC, -1) * z + 8 * ln(x) * ln(opx) * pow(NC, -1) * x * z * pow(opx, -1) + 8 * ln(x) * ln(opx) * pow(NC, -1) * x * z + 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, 2) * z + 8 * ln(x) * ln(opx) * NC * pow(x, -1) * pow(opx, -1) - 8 * ln(x) * ln(opx) * NC * pow(x, -1) - 8 * ln(x) * ln(opx) * NC * pow(x, -1) * z * pow(opx, -1) + 8 * ln(x) * ln(opx) * NC * pow(x, -1) * z + 16 * ln(x) * ln(opx) * NC * pow(opx, -1) - 8 * ln(x) * ln(opx) * NC - 16 * ln(x) * ln(opx) * NC * z * pow(opx, -1) + 8 * ln(x) * ln(opx) * NC * z + 8 * ln(x) * ln(opx) * NC * x * pow(opx, -1) + 8 * ln(x) * ln(opx) * NC * x);
                result += (-8 * ln(x) * ln(opx) * NC * x * z * pow(opx, -1) - 8 * ln(x) * ln(opx) * NC * x * z + 8 * ln(x) * ln(opx) * NC * pow(x, 2) - 8 * ln(x) * ln(opx) * NC * pow(x, 2) * z + ln(z) * pow(NC, -1) + ln(z) * pow(NC, -1) * z - 16 * ln(z) * pow(NC, -1) * x * pow(z, -1) - 9 * ln(z) * pow(NC, -1) * x - 16 * ln(z) * pow(NC, -1) * x * rln2 - ln(z) * pow(NC, -1) * x * z + 16 * ln(z) * pow(NC, -1) * x * z * rln2 + 16 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 8 * ln(z) * pow(NC, -1) * pow(x, 2) + 16 * ln(z) * pow(NC, -1) * pow(x, 2) * rln2 - 16 * ln(z) * pow(NC, -1) * pow(x, 2) * z * rln2 + 3.0 / 8.0 * ln(z) * NC * pow(x, -1) * pow(z, -1) + 3.0 / 8.0 * ln(z) * NC * pow(x, -1) - 3.0 / 8.0 * ln(z) * NC * pow(z, -2) - 1.0 / 4.0 * ln(z) * NC * pow(z, -1) - 17.0 / 4.0 * ln(z) * NC - 3.0 / 8.0 * ln(z) * NC * z + 3.0 / 8.0 * ln(z) * NC * x * pow(z, -2) + 49.0 / 4.0 * ln(z) * NC * x * pow(z, -1) - 8 * ln(z) * NC * x * pow(z, -1) * sqrtxz1 + 1.0 / 4.0 * ln(z) * NC * x - 8 * ln(z) * NC * x * rln2 + 3.0 / 8.0 * ln(z) * NC * x * z - 16 * ln(z) * NC * x * z * rln2 - 99.0 / 8.0 * ln(z) * NC * pow(x, 2) * pow(z, -1) + 8 * ln(z) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1 + 29.0 / 8.0 * ln(z) * NC * pow(x, 2) + 8 * ln(z) * NC * pow(x, 2) * rln2 + 16 * ln(z) * NC * pow(x, 2) * z * rln2 + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z + 8 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * z - 8 * ln(z) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x - 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z);
                result += (-8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z + 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x + 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * z - 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) - 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z + 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * z + 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z + 8 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC - 8 * ln(z) * ln(1 + x * pow(z, -1)) * NC * z * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * z + 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x - 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * z * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * z + 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * z - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z - 8 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z * pow(opx, -1));
                result += (+4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * z * pow(opx, -1) - 8 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * z - 4 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * pow(opx, -1) + 4 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) + 4 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * z * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * z - 8 * ln(z) * ln(1 + x * z) * NC * pow(opx, -1) + 4 * ln(z) * ln(1 + x * z) * NC + 8 * ln(z) * ln(1 + x * z) * NC * z * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * NC * z - 4 * ln(z) * ln(1 + x * z) * NC * x * pow(opx, -1) - 8 * ln(z) * ln(1 + x * z) * NC * x + 4 * ln(z) * ln(1 + x * z) * NC * x * z * pow(opx, -1) + 8 * ln(z) * ln(1 + x * z) * NC * pow(x, 2) * z + 4 * ln(z) * ln(z + x) * pow(NC, -1) * x * z - 4 * ln(z) * ln(z + x) * pow(NC, -1) * pow(x, 2) * z - 4 * ln(z) * ln(z + x) * NC * x - 4 * ln(z) * ln(z + x) * NC * x * z + 4 * ln(z) * ln(z + x) * NC * pow(x, 2) + 4 * ln(z) * ln(z + x) * NC * pow(x, 2) * z + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) - 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z + 4 * pow(ln(z), 2) * pow(NC, -1) * z * pow(opx, -1) - 2 * pow(ln(z), 2) * pow(NC, -1) * z - 8 * pow(ln(z), 2) * pow(NC, -1) * x + 2 * pow(ln(z), 2) * pow(NC, -1) * x * z * pow(opx, -1) + 8 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) + 4 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * z + 2 * pow(ln(z), 2) * NC * pow(x, -1) * pow(opx, -1) - 2 * pow(ln(z), 2) * NC * pow(x, -1) - 2 * pow(ln(z), 2) * NC * pow(x, -1) * z * pow(opx, -1) + 2 * pow(ln(z), 2) * NC * pow(x, -1) * z + 4 * pow(ln(z), 2) * NC * pow(opx, -1) - 2 * pow(ln(z), 2) * NC - 4 * pow(ln(z), 2) * NC * z * pow(opx, -1) + 2 * pow(ln(z), 2) * NC * z + 2 * pow(ln(z), 2) * NC * x * pow(opx, -1) + 8 * pow(ln(z), 2) * NC * x);
                result += (-2 * pow(ln(z), 2) * NC * x * z * pow(opx, -1) - 4 * pow(ln(z), 2) * NC * pow(x, 2) - 4 * pow(ln(z), 2) * NC * pow(x, 2) * z - 8 * ln(z) * ln(omx) * pow(NC, -1) * x + 8 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) + 8 * ln(z) * ln(omx) * NC * x - 8 * ln(z) * ln(omx) * NC * pow(x, 2) - 2 * ln(omx) * pow(NC, -1) + 2 * ln(omx) * pow(NC, -1) * z - 8 * ln(omx) * pow(NC, -1) * x * pow(z, -1) + 2 * ln(omx) * pow(NC, -1) * x + 6 * ln(omx) * pow(NC, -1) * x * z + 8 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 8 * ln(omx) * pow(NC, -1) * pow(x, 2) * z + 2 * ln(omx) * NC - 2 * ln(omx) * NC * z + 8 * ln(omx) * NC * x * pow(z, -1) - 2 * ln(omx) * NC * x - 6 * ln(omx) * NC * x * z - 8 * ln(omx) * NC * pow(x, 2) * pow(z, -1) + 8 * ln(omx) * NC * pow(x, 2) * z - 2 * ln(omz) * pow(NC, -1) + 2 * ln(omz) * pow(NC, -1) * z - 8 * ln(omz) * pow(NC, -1) * x * pow(z, -1) + 2 * ln(omz) * pow(NC, -1) * x + 6 * ln(omz) * pow(NC, -1) * x * z + 8 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 8 * ln(omz) * pow(NC, -1) * pow(x, 2) * z + 2 * ln(omz) * NC - 2 * ln(omz) * NC * z + 8 * ln(omz) * NC * x * pow(z, -1) - 2 * ln(omz) * NC * x - 6 * ln(omz) * NC * x * z - 8 * ln(omz) * NC * pow(x, 2) * pow(z, -1) + 8 * ln(omz) * NC * pow(x, 2) * z - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(x, 2) + 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x - 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(x, 2) + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * z - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2));
                result += (+8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * z - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * pow(x, 2) * z - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * z + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * z + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * pow(x, 2) * z - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z - 8 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1) - 8 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z - 4 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) + 4 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * z - 8 * Li2(-x * pow(z, -1)) * NC * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * NC + 8 * Li2(-x * pow(z, -1)) * NC * z * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * NC * z - 4 * Li2(-x * pow(z, -1)) * NC * x * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * NC * x * z * pow(opx, -1) + 8 * Li2(-x * pow(z, -1)) * NC * x * z - 8 * Li2(-x * pow(z, -1)) * NC * pow(x, 2) + 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) - 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z + 16 * Li2(-x) * pow(NC, -1) * z * pow(opx, -1));
                result += (-8 * Li2(-x) * pow(NC, -1) * z + 8 * Li2(-x) * pow(NC, -1) * x * z * pow(opx, -1) + 8 * Li2(-x) * pow(NC, -1) * x * z + 8 * Li2(-x) * pow(NC, -1) * pow(x, 2) * z + 8 * Li2(-x) * NC * pow(x, -1) * pow(opx, -1) - 8 * Li2(-x) * NC * pow(x, -1) - 8 * Li2(-x) * NC * pow(x, -1) * z * pow(opx, -1) + 8 * Li2(-x) * NC * pow(x, -1) * z + 16 * Li2(-x) * NC * pow(opx, -1) - 8 * Li2(-x) * NC - 16 * Li2(-x) * NC * z * pow(opx, -1) + 8 * Li2(-x) * NC * z + 8 * Li2(-x) * NC * x * pow(opx, -1) + 8 * Li2(-x) * NC * x - 8 * Li2(-x) * NC * x * z * pow(opx, -1) - 8 * Li2(-x) * NC * x * z + 8 * Li2(-x) * NC * pow(x, 2) - 8 * Li2(-x) * NC * pow(x, 2) * z - 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z - 8 * Li2(-x * z) * pow(NC, -1) * z * pow(opx, -1) + 4 * Li2(-x * z) * pow(NC, -1) * z - 4 * Li2(-x * z) * pow(NC, -1) * x * z * pow(opx, -1) - 8 * Li2(-x * z) * pow(NC, -1) * pow(x, 2) * z - 4 * Li2(-x * z) * NC * pow(x, -1) * pow(opx, -1) + 4 * Li2(-x * z) * NC * pow(x, -1) + 4 * Li2(-x * z) * NC * pow(x, -1) * z * pow(opx, -1) - 4 * Li2(-x * z) * NC * pow(x, -1) * z - 8 * Li2(-x * z) * NC * pow(opx, -1) + 4 * Li2(-x * z) * NC + 8 * Li2(-x * z) * NC * z * pow(opx, -1) - 4 * Li2(-x * z) * NC * z - 4 * Li2(-x * z) * NC * x * pow(opx, -1) - 8 * Li2(-x * z) * NC * x + 4 * Li2(-x * z) * NC * x * z * pow(opx, -1) + 8 * Li2(-x * z) * NC * pow(x, 2) * z - 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1) + 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * z - 16 * Li2(x) * pow(NC, -1) * z * pow(opx, -1) + 8 * Li2(x) * pow(NC, -1) * z - 8 * Li2(x) * pow(NC, -1) * x * z * pow(opx, -1) + 4 * Li2(x) * pow(NC, -1) * pow(x, 2) - 4 * Li2(x) * pow(NC, -1) * pow(x, 2) * z);
                result += (-8 * Li2(x) * NC * pow(x, -1) * pow(opx, -1) + 8 * Li2(x) * NC * pow(x, -1) + 8 * Li2(x) * NC * pow(x, -1) * z * pow(opx, -1) - 8 * Li2(x) * NC * pow(x, -1) * z - 16 * Li2(x) * NC * pow(opx, -1) + 8 * Li2(x) * NC + 16 * Li2(x) * NC * z * pow(opx, -1) - 8 * Li2(x) * NC * z - 8 * Li2(x) * NC * x * pow(opx, -1) + 8 * Li2(x) * NC * x * z * pow(opx, -1) - 4 * Li2(x) * NC * pow(x, 2) + 4 * Li2(x) * NC * pow(x, 2) * z + 8 * Li2(z) * pow(NC, -1) * x - 8 * Li2(z) * pow(NC, -1) * pow(x, 2) - 8 * Li2(z) * NC * x + 8 * Li2(z) * NC * pow(x, 2));
            }
            if (z < 1. - x && z < x) {
            }
            if (z > 1. - x && z < x) {
            }
            if (z < 1. - x && z > x) {
            }
            if (z > 1. - x && z > x) {
            }
            if (z > x) {
            }
            if (z < x) {
            }
            if (z < 1. - x) {
            }
            if (z > 1. - x) {
            }
        } else if (orders == 922001) {
            if (z != x && z != 1. - x) {
                result += 8 * LMUA * pow(NC, -1) * x * pow(z, -1) - 4 * LMUA * pow(NC, -1) * x - 4 * LMUA * pow(NC, -1) * x * z - 8 * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * LMUA * pow(NC, -1) * pow(x, 2) + 4 * LMUA * pow(NC, -1) * pow(x, 2) * z - 8 * LMUA * NC * x * pow(z, -1) + 4 * LMUA * NC * x + 4 * LMUA * NC * x * z + 8 * LMUA * NC * pow(x, 2) * pow(z, -1) - 4 * LMUA * NC * pow(x, 2) - 4 * LMUA * NC * pow(x, 2) * z;
                result += 8 * ln(z) * LMUA * pow(NC, -1) * x - 8 * ln(z) * LMUA * pow(NC, -1) * pow(x, 2) - 8 * ln(z) * LMUA * NC * x + 8 * ln(z) * LMUA * NC * pow(x, 2);
            }
        } else if (orders == 922010) {
            if (z != x && z != 1. - x) {
                result += 2 * LMUF * pow(NC, -1) - 2 * LMUF * pow(NC, -1) * z + 2 * LMUF * pow(NC, -1) * x - 2 * LMUF * pow(NC, -1) * x * z - 4 * LMUF * pow(NC, -1) * pow(x, 2) + 4 * LMUF * pow(NC, -1) * pow(x, 2) * z - 2 * LMUF * NC + 2 * LMUF * NC * z - 2 * LMUF * NC * x + 2 * LMUF * NC * x * z + 4 * LMUF * NC * pow(x, 2) - 4 * LMUF * NC * pow(x, 2) * z;
                result += 4 * ln(x) * LMUF * pow(NC, -1) * x - 4 * ln(x) * LMUF * pow(NC, -1) * x * z - 4 * ln(x) * LMUF * NC * x;
                result += 4 * ln(x) * LMUF * NC * x * z;
            }
        } else if (orders == 922100) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 922011) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 922101) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 922110) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 922002) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 922020) {
            if (z != x && z != 1. - x) {
            }
        }

    } else if (rsl == 78) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 79) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 87) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 88) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 89) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 97) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 98) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 99) {

        if (orders == 922000) {
        } else if (orders == 922001) {
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else {
        throw std::invalid_argument("Invalid rsl value");
    }

    return result;
}
