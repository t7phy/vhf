#include "../sidis.h"

double ct_nnlo_q2qp_eq(double x, double z, double Q, int rsl, int orders) {

    double result = 0.0;
    double result_0r, result_1r;

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

            double pt0 = ct_nnlo_q2qp_eq(x0, z0, Q, rsl, orders);
            double pt1 = ct_nnlo_q2qp_eq(x1, z1, Q, rsl, orders);
            double pt2 = ct_nnlo_q2qp_eq(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = ct_nnlo_q2qp_eq(x0, z0, Q, rsl, orders);
            double pt1 = ct_nnlo_q2qp_eq(x1, z1, Q, rsl, orders);
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

            double pt0 = ct_nnlo_q2qp_eq(x0, z0, Q, rsl, orders);
            double pt1 = ct_nnlo_q2qp_eq(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 922000) {
            if (z != x && z != 1. - x) {
                result += -5.0 / 36.0 * pow(z, -1) * CF - 1.0 / 3.0 * CF - 1.0 / 6.0 * pow(pi, 2) * CF - 23.0 / 12.0 * z * CF + 43.0 / 18.0 * pow(z, 2) * CF + 19.0 / 36.0 * x * pow(z, -1) * CF + 8.0 / 3.0 * x * CF - 1.0 / 6.0 * x * pow(pi, 2) * CF + 13.0 / 12.0 * x * z * CF - 1.0 / 3.0 * x * z * pow(pi, 2) * CF - 77.0 / 18.0 * x * pow(z, 2) * CF - 4.0 / 3.0 * ln(x) * pow(z, -1) * CF * pow(omx, -1) + 2.0 / 3.0 * ln(x) * pow(z, -1) * CF - 5.0 / 2.0 * ln(x) * CF * pow(omx, -1) + ln(x) * CF + 5.0 / 2.0 * ln(x) * z * CF * pow(omx, -1) - 3 * ln(x) * z * CF + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF * pow(omx, -1) + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF + 2.0 / 3.0 * ln(x) * x * pow(z, -1) * CF + 3 * ln(x) * x * CF - ln(x) * x * z * CF - 8.0 / 3.0 * ln(x) * x * pow(z, 2) * CF - 3 * ln(x) * ln(z) * CF * pow(omx, -1) + 2 * ln(x) * ln(z) * CF - 3 * ln(x) * ln(z) * z * CF * pow(omx, -1) + 2 * ln(x) * ln(z) * x * CF + 4 * ln(x) * ln(z) * x * z * CF - 1.0 / 3.0 * ln(z) * pow(z, -1) * CF - 3.0 / 2.0 * ln(z) * CF - 1.0 / 2.0 * ln(z) * z * CF - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF - 1.0 / 3.0 * ln(z) * x * pow(z, -1) * CF - 1.0 / 2.0 * ln(z) * x * CF + 7.0 / 2.0 * ln(z) * x * z * CF + 4.0 / 3.0 * ln(z) * x * pow(z, 2) * CF - pow(ln(z), 2) * CF - pow(ln(z), 2) * x * CF - 2 * pow(ln(z), 2) * x * z * CF - ln(z) * ln(omx) * CF - ln(z) * ln(omx) * x * CF - 2 * ln(z) * ln(omx) * x * z * CF - 1.0 / 3.0 * ln(omx) * pow(z, -1) * CF - 1.0 / 2.0 * ln(omx) * CF + 3.0 / 2.0 * ln(omx) * z * CF - 2.0 / 3.0 * ln(omx) * pow(z, 2) * CF - 1.0 / 3.0 * ln(omx) * x * pow(z, -1) * CF - 3.0 / 2.0 * ln(omx) * x * CF + 1.0 / 2.0 * ln(omx) * x * z * CF + 4.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF - 1.0 / 3.0 * ln(omz) * pow(z, -1) * CF - 1.0 / 2.0 * ln(omz) * CF + 3.0 / 2.0 * ln(omz) * z * CF - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF - 1.0 / 3.0 * ln(omz) * x * pow(z, -1) * CF - 3.0 / 2.0 * ln(omz) * x * CF + 1.0 / 2.0 * ln(omz) * x * z * CF + 4.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF + Li2(z) * CF + Li2(z) * x * CF + 2 * Li2(z) * x * z * CF;
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
                result += +1.0 / 3.0 * LMUA * pow(z, -1) * CF + 1.0 / 2.0 * LMUA * CF - 3.0 / 2.0 * LMUA * z * CF + 2.0 / 3.0 * LMUA * pow(z, 2) * CF + 1.0 / 3.0 * LMUA * x * pow(z, -1) * CF + 3.0 / 2.0 * LMUA * x * CF - 1.0 / 2.0 * LMUA * x * z * CF - 4.0 / 3.0 * LMUA * x * pow(z, 2) * CF + ln(z) * LMUA * CF + ln(z) * LMUA * x * CF + 2 * ln(z) * LMUA * x * z * CF;
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
            result_0r = -7.0 / 18.0 * pow(z, -1) * CF - 10.0 / 3.0 * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 7.0 / 3.0 * z * CF + 1.0 / 6.0 * z * pow(pi, 2) * CF + 25.0 / 18.0 * pow(z, 2) * CF + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF - 1.0 / 2.0 * ln(z) * CF - 2 * ln(z) * z * CF - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF + pow(ln(z), 2) * CF + pow(ln(z), 2) * z * CF + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF + 1.0 / 2.0 * ln(omz) * CF - 1.0 / 2.0 * ln(omz) * z * CF - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF - Li2(z) * CF - Li2(z) * z * CF;
            result_1r = 2.0 / 3.0 * pow(z, -1) * CF + 1.0 / 2.0 * CF - 1.0 / 2.0 * z * CF - 2.0 / 3.0 * pow(z, 2) * CF + ln(z) * CF + ln(z) * z * CF;
            result += result_0r * 1 / (1 - x) + result_1r * ln(1 - x) / (1 - x);
        } else if (orders == 922001) {
            result_0r = -2.0 / 3.0 * LMUA * pow(z, -1) * CF - 1.0 / 2.0 * LMUA * CF + 1.0 / 2.0 * LMUA * z * CF + 2.0 / 3.0 * LMUA * pow(z, 2) * CF - ln(z) * LMUA * CF - ln(z) * LMUA * z * CF;
            result += result_0r * 1 / (1 - x);
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
            result += -107.0 / 108.0 * pow(z, -1) * CF - 11.0 / 9.0 * CF + 2 * zeta3 * CF - 1.0 / 6.0 * pow(pi, 2) * CF - 4.0 / 9.0 * z * CF + 2 * z * zeta3 * CF - 1.0 / 4.0 * z * pow(pi, 2) * CF + 287.0 / 108.0 * pow(z, 2) * CF - 7.0 / 18.0 * ln(z) * pow(z, -1) * CF - 5 * ln(z) * CF + 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF - 9.0 / 2.0 * ln(z) * z * CF + 1.0 / 6.0 * ln(z) * z * pow(pi, 2) * CF - 31.0 / 18.0 * ln(z) * pow(z, 2) * CF + 1.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF - 1.0 / 8.0 * pow(ln(z), 2) * CF - 5.0 / 8.0 * pow(ln(z), 2) * z * CF + 5.0 / 12.0 * pow(ln(z), 3) * CF + 5.0 / 12.0 * pow(ln(z), 3) * z * CF - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * z * CF - 7.0 / 18.0 * ln(omz) * pow(z, -1) * CF - 10.0 / 3.0 * ln(omz) * CF + 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF + 7.0 / 3.0 * ln(omz) * z * CF + 1.0 / 6.0 * ln(omz) * z * pow(pi, 2) * CF + 25.0 / 18.0 * ln(omz) * pow(z, 2) * CF + 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF + 1.0 / 4.0 * pow(ln(omz), 2) * CF - 1.0 / 4.0 * pow(ln(omz), 2) * z * CF - 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF - ln(omz) * Li2(z) * CF - ln(omz) * Li2(z) * z * CF - Li3(1 - z) * CF - Li3(1 - z) * z * CF - 2 * Li3(z) * CF - 2 * Li3(z) * z * CF - 2.0 / 3.0 * Li2(z) * pow(z, -1) * CF + 1.0 / 2.0 * Li2(z) * CF + 2 * Li2(z) * z * CF + 2.0 / 3.0 * Li2(z) * pow(z, 2) * CF;
            result_0r = -7.0 / 18.0 * pow(z, -1) * CF - 10.0 / 3.0 * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 7.0 / 3.0 * z * CF + 1.0 / 6.0 * z * pow(pi, 2) * CF + 25.0 / 18.0 * pow(z, 2) * CF + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF - 1.0 / 2.0 * ln(z) * CF - 2 * ln(z) * z * CF - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF + pow(ln(z), 2) * CF + pow(ln(z), 2) * z * CF + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF + 1.0 / 2.0 * ln(omz) * CF - 1.0 / 2.0 * ln(omz) * z * CF - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF - Li2(z) * CF - Li2(z) * z * CF;
            result_1r = 2.0 / 3.0 * pow(z, -1) * CF + 1.0 / 2.0 * CF - 1.0 / 2.0 * z * CF - 2.0 / 3.0 * pow(z, 2) * CF + ln(z) * CF + ln(z) * z * CF;
            result += result_0r * ln(1 - x) + result_1r * ln(1 - x) * ln(1 - x) / 2;
        } else if (orders == 922001) {
            result += +7.0 / 18.0 * LMUA * pow(z, -1) * CF + 10.0 / 3.0 * LMUA * CF - 1.0 / 6.0 * LMUA * pow(pi, 2) * CF - 7.0 / 3.0 * LMUA * z * CF - 1.0 / 6.0 * LMUA * z * pow(pi, 2) * CF - 25.0 / 18.0 * LMUA * pow(z, 2) * CF - 2.0 / 3.0 * ln(z) * LMUA * pow(z, -1) * CF + 1.0 / 2.0 * ln(z) * LMUA * CF + 2 * ln(z) * LMUA * z * CF + 2.0 / 3.0 * ln(z) * LMUA * pow(z, 2) * CF - pow(ln(z), 2) * LMUA * CF - pow(ln(z), 2) * LMUA * z * CF - 2.0 / 3.0 * ln(omz) * LMUA * pow(z, -1) * CF - 1.0 / 2.0 * ln(omz) * LMUA * CF + 1.0 / 2.0 * ln(omz) * LMUA * z * CF + 2.0 / 3.0 * ln(omz) * LMUA * pow(z, 2) * CF + Li2(z) * LMUA * CF + Li2(z) * LMUA * z * CF;
            result_0r = -2.0 / 3.0 * LMUA * pow(z, -1) * CF - 1.0 / 2.0 * LMUA * CF + 1.0 / 2.0 * LMUA * z * CF + 2.0 / 3.0 * LMUA * pow(z, 2) * CF - ln(z) * LMUA * CF - ln(z) * LMUA * z * CF;
            result += result_0r * ln(1 - x);
        } else if (orders == 922010) {
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
            result += +1.0 / 3.0 * pow(LMUA, 2) * pow(z, -1) * CF + 1.0 / 4.0 * pow(LMUA, 2) * CF - 1.0 / 4.0 * pow(LMUA, 2) * z * CF - 1.0 / 3.0 * pow(LMUA, 2) * pow(z, 2) * CF + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * z * CF;
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
