#include "../sidis.h"

double ct_nnlo_q2qp_eqp(double x, double z, double Q, int rsl, int orders) {

    double result = 0.0;
    double result_r0, result_r1;

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

            double pt0 = ct_nnlo_q2qp_eqp(x0, z0, Q, rsl, orders);
            double pt1 = ct_nnlo_q2qp_eqp(x1, z1, Q, rsl, orders);
            double pt2 = ct_nnlo_q2qp_eqp(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = ct_nnlo_q2qp_eqp(x0, z0, Q, rsl, orders);
            double pt1 = ct_nnlo_q2qp_eqp(x1, z1, Q, rsl, orders);
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

            double pt0 = ct_nnlo_q2qp_eqp(x0, z0, Q, rsl, orders);
            double pt1 = ct_nnlo_q2qp_eqp(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 922000) {
            if (z != x && z != 1. - x) {
                result += 13.0 / 9.0 * pow(x, -1) * pow(z, -1) * CF - 26.0 / 9.0 * pow(x, -1) * CF - 11.0 / 6.0 * pow(z, -1) * CF + 1.0 / 6.0 * pow(z, -1) * pow(pi, 2) * CF - 7.0 / 3.0 * CF - 1.0 / 3.0 * pow(pi, 2) * CF + 10 * z * CF + 17.0 / 6.0 * x * pow(z, -1) * CF + 1.0 / 6.0 * x * pow(z, -1) * pow(pi, 2) * CF + 1.0 / 3.0 * x * CF - 1.0 / 3.0 * x * pow(pi, 2) * CF - 10 * x * z * CF - 22.0 / 9.0 * pow(x, 2) * pow(z, -1) * CF + 44.0 / 9.0 * pow(x, 2) * CF + 1.0 / 4.0 * ln(x) * pow(x, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(x) * pow(x, -1) * CF + ln(x) * pow(z, -1) * CF - 1.0 / 4.0 * ln(x) * pow(poly2, -1) * CF - 19.0 / 4.0 * ln(x) * CF + 5 * ln(x) * z * CF + 3 * ln(x) * x * pow(z, -1) * CF - 35.0 / 4.0 * ln(x) * x * CF + 5 * ln(x) * x * z * CF + 2 * ln(x) * pow(x, 2) * pow(z, -1) * CF - 17.0 / 4.0 * ln(x) * pow(x, 2) * CF - 1.0 / 4.0 * ln(x) * pow(x, 3) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * pow(x, 4) * pow(poly2, -1) * CF + 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 7.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF + 10 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF - 10 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 7.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF - 10 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF + 10 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - pow(ln(x), 2) * pow(z, -1) * CF + 2 * pow(ln(x), 2) * CF - pow(ln(x), 2) * x * pow(z, -1) * CF + 2 * pow(ln(x), 2) * x * CF + ln(x) * ln(z) * pow(z, -1) * CF - ln(x) * ln(z) * CF + ln(x) * ln(z) * x * pow(z, -1) * CF - ln(x) * ln(z) * x * CF + ln(x) * ln(omz) * pow(z, -1) * CF - 2 * ln(x) * ln(omz) * CF + ln(x) * ln(omz) * x * pow(z, -1) * CF - 2 * ln(x) * ln(omz) * x * CF + 2.0 / 3.0 * ln(z) * pow(x, -1) * pow(z, -1) * CF + 1.0 / 4.0 * ln(z) * pow(x, -1) * pow(poly2, -1) * CF + 2.0 / 3.0 * ln(z) * pow(x, -1) * CF * pow(omz, -1) - 19.0 / 12.0 * ln(z) * pow(x, -1) * CF + 1.0 / 2.0 * ln(z) * pow(z, -1) * CF + 1.0 / 4.0 * ln(z) * pow(poly2, -1) * CF - ln(z) * CF * pow(omz, -1) - 5.0 / 4.0 * ln(z) * CF + 5 * ln(z) * z * CF - 1.0 / 2.0 * ln(z) * x * pow(z, -1) * CF + ln(z) * x * CF * pow(omz, -1) + 5.0 / 4.0 * ln(z) * x * CF - 5 * ln(z) * x * z * CF - 2.0 / 3.0 * ln(z) * pow(x, 2) * pow(z, -1) * CF - 2.0 / 3.0 * ln(z) * pow(x, 2) * CF * pow(omz, -1) + 19.0 / 12.0 * ln(z) * pow(x, 2) * CF - 1.0 / 4.0 * ln(z) * pow(x, 3) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(z) * pow(x, 4) * pow(poly2, -1) * CF + 2.0 / 3.0 * ln(omx) * pow(x, -1) * pow(z, -1) * CF - 4.0 / 3.0 * ln(omx) * pow(x, -1) * CF + 1.0 / 2.0 * ln(omx) * pow(z, -1) * CF - ln(omx) * CF - 1.0 / 2.0 * ln(omx) * x * pow(z, -1) * CF + ln(omx) * x * CF - 2.0 / 3.0 * ln(omx) * pow(x, 2) * pow(z, -1) * CF + 4.0 / 3.0 * ln(omx) * pow(x, 2) * CF + 2.0 / 3.0 * ln(omz) * pow(x, -1) * pow(z, -1) * CF - 4.0 / 3.0 * ln(omz) * pow(x, -1) * CF + 1.0 / 2.0 * ln(omz) * pow(z, -1) * CF - ln(omz) * CF - 1.0 / 2.0 * ln(omz) * x * pow(z, -1) * CF + ln(omz) * x * CF - 2.0 / 3.0 * ln(omz) * pow(x, 2) * pow(z, -1) * CF + 4.0 / 3.0 * ln(omz) * pow(x, 2) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF + 10 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF - 10 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF - 10 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF + 10 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF - 10 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF + 10 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 7.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF + 10 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF - 10 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - Li2(x) * pow(z, -1) * CF + 2 * Li2(x) * CF - Li2(x) * x * pow(z, -1) * CF + 2 * Li2(x) * x * CF;
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
                result += -2.0 / 3.0 * LMUF * pow(x, -1) * pow(z, -1) * CF + 4.0 / 3.0 * LMUF * pow(x, -1) * CF - 1.0 / 2.0 * LMUF * pow(z, -1) * CF + LMUF * CF + 1.0 / 2.0 * LMUF * x * pow(z, -1) * CF - LMUF * x * CF + 2.0 / 3.0 * LMUF * pow(x, 2) * pow(z, -1) * CF - 4.0 / 3.0 * LMUF * pow(x, 2) * CF - ln(x) * LMUF * pow(z, -1) * CF + 2 * ln(x) * LMUF * CF - ln(x) * LMUF * x * pow(z, -1) * CF + 2 * ln(x) * LMUF * x * CF;
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
            result_r0 = 13.0 / 9.0 * pow(x, -1) * CF - 11.0 / 6.0 * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 17.0 / 6.0 * x * CF + 1.0 / 6.0 * x * pow(pi, 2) * CF - 22.0 / 9.0 * pow(x, 2) * CF + ln(x) * CF + 3 * ln(x) * x * CF + 2 * ln(x) * pow(x, 2) * CF - pow(ln(x), 2) * CF - pow(ln(x), 2) * x * CF + 2.0 / 3.0 * ln(omx) * pow(x, -1) * CF + 1.0 / 2.0 * ln(omx) * CF - 1.0 / 2.0 * ln(omx) * x * CF - 2.0 / 3.0 * ln(omx) * pow(x, 2) * CF - Li2(x) * CF - Li2(x) * x * CF;
            result_r1 = 2.0 / 3.0 * pow(x, -1) * CF + 1.0 / 2.0 * CF - 1.0 / 2.0 * x * CF - 2.0 / 3.0 * pow(x, 2) * CF + ln(x) * CF + ln(x) * x * CF;
            result += result_r0 * 1 / (1 - z) + result_r1 * ln(1 - z) / (1 - z);
        } else if (orders == 922001) {
        } else if (orders == 922010) {
            result_r0 = -2.0 / 3.0 * LMUF * pow(x, -1) * CF - 1.0 / 2.0 * LMUF * CF + 1.0 / 2.0 * LMUF * x * CF + 2.0 / 3.0 * LMUF * pow(x, 2) * CF - ln(x) * LMUF * CF - ln(x) * LMUF * x * CF;
            result += result_r0 * 1 / (1 - z);
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
        }

    } else if (rsl == 79) {

        if (orders == 922000) {
            result += 52.0 / 27.0 * pow(x, -1) * CF - 41.0 / 36.0 * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 17.0 / 36.0 * x * CF + 1.0 / 2.0 * x * pow(pi, 2) * CF - 34.0 / 27.0 * pow(x, 2) * CF + 1.0 / 3.0 * pow(x, 2) * pow(pi, 2) * CF + 23.0 / 6.0 * ln(x) * CF - 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF - 5.0 / 6.0 * ln(x) * x * CF - 1.0 / 3.0 * ln(x) * x * pow(pi, 2) * CF + 38.0 / 9.0 * ln(x) * pow(x, 2) * CF - 13.0 / 8.0 * pow(ln(x), 2) * CF - 13.0 / 8.0 * pow(ln(x), 2) * x * CF - 5.0 / 3.0 * pow(ln(x), 2) * pow(x, 2) * CF + 5.0 / 12.0 * pow(ln(x), 3) * CF + 5.0 / 12.0 * pow(ln(x), 3) * x * CF - 2.0 / 3.0 * ln(x) * ln(omx) * pow(x, -1) * CF - 1.0 / 2.0 * ln(x) * ln(omx) * CF + 1.0 / 2.0 * ln(x) * ln(omx) * x * CF + 2.0 / 3.0 * ln(x) * ln(omx) * pow(x, 2) * CF - 1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF - 1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF + ln(x) * Li2(x) * CF + ln(x) * Li2(x) * x * CF + 13.0 / 9.0 * ln(omx) * pow(x, -1) * CF - 11.0 / 6.0 * ln(omx) * CF + 1.0 / 6.0 * ln(omx) * pow(pi, 2) * CF + 17.0 / 6.0 * ln(omx) * x * CF + 1.0 / 6.0 * ln(omx) * x * pow(pi, 2) * CF - 22.0 / 9.0 * ln(omx) * pow(x, 2) * CF + 1.0 / 3.0 * pow(ln(omx), 2) * pow(x, -1) * CF + 1.0 / 4.0 * pow(ln(omx), 2) * CF - 1.0 / 4.0 * pow(ln(omx), 2) * x * CF - 1.0 / 3.0 * pow(ln(omx), 2) * pow(x, 2) * CF - ln(omx) * Li2(x) * CF - ln(omx) * Li2(x) * x * CF - Li3(1 - x) * CF - Li3(1 - x) * x * CF - 2.0 / 3.0 * Li2(x) * pow(x, -1) * CF - 3.0 / 2.0 * Li2(x) * CF - 5.0 / 2.0 * Li2(x) * x * CF - 4.0 / 3.0 * Li2(x) * pow(x, 2) * CF;
            result_r0 = 13.0 / 9.0 * pow(x, -1) * CF - 11.0 / 6.0 * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 17.0 / 6.0 * x * CF + 1.0 / 6.0 * x * pow(pi, 2) * CF - 22.0 / 9.0 * pow(x, 2) * CF + ln(x) * CF + 3 * ln(x) * x * CF + 2 * ln(x) * pow(x, 2) * CF - pow(ln(x), 2) * CF - pow(ln(x), 2) * x * CF + 2.0 / 3.0 * ln(omx) * pow(x, -1) * CF + 1.0 / 2.0 * ln(omx) * CF - 1.0 / 2.0 * ln(omx) * x * CF - 2.0 / 3.0 * ln(omx) * pow(x, 2) * CF - Li2(x) * CF - Li2(x) * x * CF;
            result_r1 = 2.0 / 3.0 * pow(x, -1) * CF + 1.0 / 2.0 * CF - 1.0 / 2.0 * x * CF - 2.0 / 3.0 * pow(x, 2) * CF + ln(x) * CF + ln(x) * x * CF;
            result += result_r0 * ln(1 - z) + result_r1 * ln(1 - z) * ln(1 - z) / 2;
        } else if (orders == 922001) {
        } else if (orders == 922010) {
            result += -13.0 / 9.0 * LMUF * pow(x, -1) * CF + 11.0 / 6.0 * LMUF * CF - 1.0 / 6.0 * LMUF * pow(pi, 2) * CF - 17.0 / 6.0 * LMUF * x * CF - 1.0 / 6.0 * LMUF * x * pow(pi, 2) * CF + 22.0 / 9.0 * LMUF * pow(x, 2) * CF - ln(x) * LMUF * CF - 3 * ln(x) * LMUF * x * CF - 2 * ln(x) * LMUF * pow(x, 2) * CF + pow(ln(x), 2) * LMUF * CF + pow(ln(x), 2) * LMUF * x * CF - 2.0 / 3.0 * ln(omx) * LMUF * pow(x, -1) * CF - 1.0 / 2.0 * ln(omx) * LMUF * CF + 1.0 / 2.0 * ln(omx) * LMUF * x * CF + 2.0 / 3.0 * ln(omx) * LMUF * pow(x, 2) * CF + Li2(x) * LMUF * CF + Li2(x) * LMUF * x * CF;
            result_r0 = -2.0 / 3.0 * LMUF * pow(x, -1) * CF - 1.0 / 2.0 * LMUF * CF + 1.0 / 2.0 * LMUF * x * CF + 2.0 / 3.0 * LMUF * pow(x, 2) * CF - ln(x) * LMUF * CF - ln(x) * LMUF * x * CF;
            result += result_r0 * ln(1 - z);
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
            result += +1.0 / 3.0 * pow(LMUF, 2) * pow(x, -1) * CF + 1.0 / 4.0 * pow(LMUF, 2) * CF - 1.0 / 4.0 * pow(LMUF, 2) * x * CF - 1.0 / 3.0 * pow(LMUF, 2) * pow(x, 2) * CF + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * CF + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * x * CF;
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
