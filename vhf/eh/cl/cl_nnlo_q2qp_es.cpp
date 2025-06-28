#include "../sidis.h"

double cl_nnlo_q2qp_es(double x, double z, double Q, int rsl, int orders) {

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

            double pt0 = cl_nnlo_q2qp_es(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_q2qp_es(x1, z1, Q, rsl, orders);
            double pt2 = cl_nnlo_q2qp_es(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = cl_nnlo_q2qp_es(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_q2qp_es(x1, z1, Q, rsl, orders);
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

            double pt0 = cl_nnlo_q2qp_es(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_q2qp_es(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 922000) {
            if (z != x && z != 1. - x) {
                result += (-4.0 / 3.0 * pow(x, -1) * z * pow(pi, 2) * CF * pow(opx, -1) + 4.0 / 3.0 * pow(x, -1) * z * pow(pi, 2) * CF + 8.0 / 3.0 * pow(x, -1) * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1) - 8.0 / 3.0 * pow(x, -1) * pow(z, 2) * pow(pi, 2) * CF + 2 * CF - 2 * z * CF - 4.0 / 3.0 * z * pow(pi, 2) * CF * pow(opx, -1) + 8.0 / 3.0 * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1) - 2 * x * CF - 8 * x * sqrtxz1 * rln2 * CF + 2 * x * z * CF - 4.0 / 3.0 * x * z * pow(pi, 2) * CF - 32 * x * pow(z, 2) * pow(rln2, 2) * CF + 8.0 / 3.0 * x * pow(z, 2) * pow(pi, 2) * CF - 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * sqrtxz3 * CF - 46 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 6 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * z * sqrtxz3 * CF + 2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * sqrtxz3 * CF + 46 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 6 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * z * sqrtxz3 * CF + InvTanInt(-sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - InvTanInt(-sqrtxz3) * sqrtxz3 * CF + 23 * InvTanInt(-sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 3 * InvTanInt(-sqrtxz3) * x * z * sqrtxz3 * CF + 2 * InvTanInt(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 2 * InvTanInt(z * sqrtxz3) * sqrtxz3 * CF + 46 * InvTanInt(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 6 * InvTanInt(z * sqrtxz3) * x * z * sqrtxz3 * CF - InvTanInt(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + InvTanInt(sqrtxz3) * sqrtxz3 * CF - 23 * InvTanInt(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3 * InvTanInt(sqrtxz3) * x * z * sqrtxz3 * CF + 8 * ln(1 + sqrtxz1 - z) * x * sqrtxz1 * CF - 8 * ln(1 + sqrtxz1 - z) * x * z * rln2 * CF);
                result += (+48 * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * rln2 * CF + 8 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF - 16 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, 2) * CF - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF - 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF + 8 * ln(1 + sqrtxz1 + z) * x * z * rln2 * CF + 16 * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * rln2 * CF + 1.0 / 2.0 * ln(x) * pow(x, -1) * pow(poly2, -1) * CF - 1.0 / 2.0 * ln(x) * pow(x, -1) * CF - 16 * ln(x) * pow(x, -1) * z * CF * pow(opx, -1) + 16 * ln(x) * pow(x, -1) * z * CF + 32 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 32 * ln(x) * pow(x, -1) * pow(z, 2) * CF - 1.0 / 2.0 * ln(x) * pow(poly2, -1) * CF + 1.0 / 2.0 * ln(x) * CF - 16 * ln(x) * z * CF * pow(opx, -1) - ln(x) * z * CF + 32 * ln(x) * pow(z, 2) * CF * pow(opx, -1) - ln(x) * x * pow(poly2, -1) * CF + 11.0 / 2.0 * ln(x) * x * CF - 4 * ln(x) * x * sqrtxz1 * CF - 5 * ln(x) * x * z * CF + 8 * ln(x) * x * z * rln2 * CF - 32 * ln(x) * x * pow(z, 2) * rln2 * CF + ln(x) * pow(x, 2) * pow(poly2, -1) * CF - 4 * ln(x) * pow(x, 2) * CF * pow(xmz, -1) - 7.0 / 2.0 * ln(x) * pow(x, 2) * CF + 1.0 / 2.0 * ln(x) * pow(x, 3) * pow(poly2, -1) * CF + 4 * ln(x) * pow(x, 3) * CF * pow(xmz, -1) - 1.0 / 2.0 * ln(x) * pow(x, 4) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(sqrtxz2, -1) * CF - ln(x) * ln(1 - sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 4 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF + 12 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF);
                result += (-12 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 9.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 9 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(sqrtxz2, -1) * CF + ln(x) * ln(1 + sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF - 12 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF + 12 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 9.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 9 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF + 16 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF + 16 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1));
                result += (-4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF - 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF - 8 * ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF - 8 * ln(x) * ln(1 + x) * x * CF + 24 * ln(x) * ln(1 + x) * x * z * CF - 16 * ln(x) * ln(1 + x) * x * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF - 8 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1) - 16 * ln(x) * ln(1 + x * z) * x * pow(z, 2) * CF + 4 * ln(x) * ln(z + x) * x * z * CF + 8 * ln(x) * ln(z + x) * x * pow(z, 2) * CF + 6 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(opx, -1) - 6 * pow(ln(x), 2) * pow(x, -1) * z * CF - 12 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 12 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF + 6 * pow(ln(x), 2) * z * CF * pow(opx, -1) - 12 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1) + 4 * pow(ln(x), 2) * x * CF - 12 * pow(ln(x), 2) * x * z * CF + 8 * pow(ln(x), 2) * x * pow(z, 2) * CF - 4 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(z) * pow(x, -1) * z * CF + 8 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF - 4 * ln(x) * ln(z) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(opx, -1) + 4 * ln(x) * ln(z) * x * z * CF);
                result += (-8 * ln(x) * ln(z) * x * pow(z, 2) * CF + 8 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(omx) * pow(x, -1) * z * CF - 16 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 16 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF + 8 * ln(x) * ln(omx) * z * CF * pow(opx, -1) - 16 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(omx) * x * z * CF - 16 * ln(x) * ln(omx) * x * pow(z, 2) * CF - 8 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(opx) * pow(x, -1) * z * CF + 16 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 16 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF - 8 * ln(x) * ln(opx) * z * CF * pow(opx, -1) + 16 * ln(x) * ln(opx) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(x) * ln(opx) * x * z * CF + 16 * ln(x) * ln(opx) * x * pow(z, 2) * CF + 1.0 / 2.0 * ln(z) * pow(x, -1) * pow(poly2, -1) * CF - 1.0 / 2.0 * ln(z) * pow(x, -1) * CF + 1.0 / 2.0 * ln(z) * pow(poly2, -1) * CF + 3.0 / 2.0 * ln(z) * CF - ln(z) * z * CF - ln(z) * x * pow(poly2, -1) * CF - 1.0 / 2.0 * ln(z) * x * CF - 4 * ln(z) * x * sqrtxz1 * CF + 5 * ln(z) * x * z * CF - 8 * ln(z) * x * z * rln2 * CF - 32 * ln(z) * x * pow(z, 2) * rln2 * CF - ln(z) * pow(x, 2) * pow(poly2, -1) * CF + 4 * ln(z) * pow(x, 2) * CF * pow(xmz, -1) + 7.0 / 2.0 * ln(z) * pow(x, 2) * CF + 1.0 / 2.0 * ln(z) * pow(x, 3) * pow(poly2, -1) * CF - 4 * ln(z) * pow(x, 3) * CF * pow(xmz, -1) + 1.0 / 2.0 * ln(z) * pow(x, 4) * pow(poly2, -1) * CF + 16 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF + 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF + 16 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF + 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1));
                result += (-8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF - 4 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1) + 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF + 8 * ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF + 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF - 8 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1) - 8 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1) - 16 * ln(z) * ln(1 + x * z) * x * pow(z, 2) * CF - 4 * ln(z) * ln(z + x) * x * z * CF - 8 * ln(z) * ln(z + x) * x * pow(z, 2) * CF - 2 * pow(ln(z), 2) * pow(x, -1) * z * CF * pow(opx, -1) + 2 * pow(ln(z), 2) * pow(x, -1) * z * CF + 4 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 4 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF - 2 * pow(ln(z), 2) * z * CF * pow(opx, -1) + 4 * pow(ln(z), 2) * pow(z, 2) * CF * pow(opx, -1) + 2 * pow(ln(z), 2) * x * CF - 8 * pow(ln(z), 2) * x * z * CF + 8 * pow(ln(z), 2) * x * pow(z, 2) * CF - 4 * ln(z) * ln(omz) * x * CF + 8 * ln(z) * ln(omz) * x * z * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF);
                result += (-4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF + 12 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF - 12 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF - 12 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF + 12 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF);
                result += (+9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * CF + 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF - 12 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF + 12 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF);
                result += (-1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF + 12 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF - 12 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 9.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 9 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, 2) * CF - 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, 2) * CF + 4 * Li2(1 - x * pow(z, -1)) * x * CF - 8 * Li2(1 - x * pow(z, -1)) * x * z * CF + 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF);
                result += (-8 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF + 4 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1) - 8 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(-x * pow(z, -1)) * x * z * CF - 8 * Li2(-x) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * Li2(-x) * pow(x, -1) * z * CF + 16 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 16 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF - 8 * Li2(-x) * z * CF * pow(opx, -1) + 16 * Li2(-x) * pow(z, 2) * CF * pow(opx, -1) - 8 * Li2(-x) * x * CF + 16 * Li2(-x) * x * z * CF + 4 * Li2(-x * z) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * Li2(-x * z) * pow(x, -1) * z * CF - 8 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF + 4 * Li2(-x * z) * z * CF * pow(opx, -1) - 8 * Li2(-x * z) * pow(z, 2) * CF * pow(opx, -1) - 16 * Li2(-x * z) * x * pow(z, 2) * CF + 8 * Li2(x) * pow(x, -1) * z * CF * pow(opx, -1) - 8 * Li2(x) * pow(x, -1) * z * CF - 16 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 16 * Li2(x) * pow(x, -1) * pow(z, 2) * CF + 8 * Li2(x) * z * CF * pow(opx, -1) - 16 * Li2(x) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(x) * x * z * CF - 16 * Li2(x) * x * pow(z, 2) * CF - 4 * Li2(z) * x * CF + 8 * Li2(z) * x * z * CF);
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
            }
        } else if (orders == 922010) {
            if (z != x && z != 1. - x) {
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
