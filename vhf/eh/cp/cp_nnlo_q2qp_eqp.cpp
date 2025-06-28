#include "../sidis.h"

double cp_nnlo_q2qp_eqp(double x, double z, double Q, int rsl, int orders) {

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

            double pt0 = cp_nnlo_q2qp_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cp_nnlo_q2qp_eqp(x1, z1, Q, rsl, orders);
            double pt2 = cp_nnlo_q2qp_eqp(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = cp_nnlo_q2qp_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cp_nnlo_q2qp_eqp(x1, z1, Q, rsl, orders);
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

            double pt0 = cp_nnlo_q2qp_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cp_nnlo_q2qp_eqp(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 922000) {
            if (z != x && z != 1. - x) {
                result += (-3 * pow(z, -1) * CF + 10 * CF + 3 * x * pow(z, -1) * CF - 10 * x * CF + 1. / 6. * pow(pi, 2) * pow(z, -1) * CF - 1. / 3. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * pow(z, -1) * CF - 1. / 3. * pow(pi, 2) * x * CF - 3 * ln(x) * pow(z, -1) * CF + 1. / 2. * ln(x) * CF * pow(poly2, -1) + 8 * ln(x) * CF + 3 * ln(x) * x * pow(z, -1) * CF - 1. / 2. * ln(x) * x * CF * pow(poly2, -1) - 4 * ln(x) * x * CF - 1. / 2. * ln(x) * pow(x, 2) * CF * pow(poly2, -1) + 1. / 2. * ln(x) * pow(x, 3) * CF * pow(poly2, -1) + 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) + 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1) - ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1) - 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) - 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1) + ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) - 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1));
                result += (-pow(ln(x), 2) * pow(z, -1) * CF + 2 * pow(ln(x), 2) * CF - pow(ln(x), 2) * x * pow(z, -1) * CF + 2 * pow(ln(x), 2) * x * CF + ln(x) * ln(z) * pow(z, -1) * CF - ln(x) * ln(z) * CF + ln(x) * ln(z) * x * pow(z, -1) * CF - ln(x) * ln(z) * x * CF + ln(x) * ln(omz) * pow(z, -1) * CF - 2 * ln(x) * ln(omz) * CF + ln(x) * ln(omz) * x * pow(z, -1) * CF - 2 * ln(x) * ln(omz) * x * CF + 5. / 2. * ln(z) * pow(z, -1) * CF + 1. / 2. * ln(z) * CF * pow(poly2, -1) + ln(z) * CF * pow(omz, -1) - 2 * ln(z) * CF - 5. / 2. * ln(z) * x * pow(z, -1) * CF + 1. / 2. * ln(z) * x * CF * pow(poly2, -1) - ln(z) * x * CF * pow(omz, -1) + 2 * ln(z) * x * CF - 1. / 2. * ln(z) * pow(x, 2) * CF * pow(poly2, -1) - 1. / 2. * ln(z) * pow(x, 3) * CF * pow(poly2, -1) + 5. / 2. * ln(omx) * pow(z, -1) * CF - 5 * ln(omx) * CF - 5. / 2. * ln(omx) * x * pow(z, -1) * CF + 5 * ln(omx) * x * CF + 5. / 2. * ln(omz) * pow(z, -1) * CF - 5 * ln(omz) * CF - 5. / 2. * ln(omz) * x * pow(z, -1) * CF + 5 * ln(omz) * x * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1));
                result += (-1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * CF * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) - 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * CF * pow(sqrtxz2, -1));
                result += (-Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - Li2(x) * pow(z, -1) * CF + 2 * Li2(x) * CF - Li2(x) * x * pow(z, -1) * CF + 2 * Li2(x) * x * CF);
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
                result += (-5. / 2. * pow(z, -1) * LMUF * CF + 5 * LMUF * CF + 5. / 2. * x * pow(z, -1) * LMUF * CF - 5 * x * LMUF * CF - ln(x) * pow(z, -1) * LMUF * CF + 2 * ln(x) * LMUF * CF - ln(x) * x * pow(z, -1) * LMUF * CF + 2 * ln(x) * x * LMUF * CF);
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
            result_r0 = (-3 * CF + 3 * x * CF + 1. / 6. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * CF - 3 * ln(x) * CF + 3 * ln(x) * x * CF - pow(ln(x), 2) * CF - pow(ln(x), 2) * x * CF + 5. / 2. * ln(omx) * CF - 5. / 2. * ln(omx) * x * CF - Li2(x) * CF - Li2(x) * x * CF);
            result_r1 = (5. / 2. * CF - 5. / 2. * x * CF + ln(x) * CF + ln(x) * x * CF);
            result += result_r0 * 1 / (1 - z) + result_r1 * ln(1 - z) / (1 - z);
        } else if (orders == 922001) {
        } else if (orders == 922010) {
            result_r0 = (-5. / 2. * LMUF * CF + 5. / 2. * x * LMUF * CF - ln(x) * LMUF * CF - ln(x) * x * LMUF * CF);
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
            result += (9 * CF - 9 * x * CF - 1. / 2. * pow(pi, 2) * CF + 1. / 2. * pow(pi, 2) * x * CF + 25. / 4. * ln(x) * CF - 3. / 4. * ln(x) * x * CF - 1. / 3. * ln(x) * pow(pi, 2) * CF - 1. / 3. * ln(x) * pow(pi, 2) * x * CF + 17. / 8. * pow(ln(x), 2) * CF - 15. / 8. * pow(ln(x), 2) * x * CF + 5. / 12. * pow(ln(x), 3) * CF + 5. / 12. * pow(ln(x), 3) * x * CF - 5. / 2. * ln(x) * ln(omx) * CF + 5. / 2. * ln(x) * ln(omx) * x * CF - 3. / 2. * ln(x) * pow(ln(omx), 2) * CF - 3. / 2. * ln(x) * pow(ln(omx), 2) * x * CF + ln(x) * Li2(x) * CF + ln(x) * Li2(x) * x * CF - 3 * ln(omx) * CF + 3 * ln(omx) * x * CF + 1. / 3. * ln(omx) * pow(pi, 2) * CF + 1. / 3. * ln(omx) * pow(pi, 2) * x * CF + 5. / 4. * pow(ln(omx), 2) * CF - 5. / 4. * pow(ln(omx), 2) * x * CF - ln(omx) * Li2(1 - x) * CF - ln(omx) * Li2(1 - x) * x * CF - 2 * ln(omx) * Li2(x) * CF - 2 * ln(omx) * Li2(x) * x * CF - Li3(1 - x) * CF - Li3(1 - x) * x * CF + 1. / 2. * Li2(x) * CF - 1. / 2. * Li2(x) * x * CF);
            result_r0 = (-3 * CF + 3 * x * CF + 1. / 6. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * CF - 3 * ln(x) * CF + 3 * ln(x) * x * CF - pow(ln(x), 2) * CF - pow(ln(x), 2) * x * CF + 5. / 2. * ln(omx) * CF - 5. / 2. * ln(omx) * x * CF - Li2(x) * CF - Li2(x) * x * CF);
            result_r1 = (5. / 2. * CF - 5. / 2. * x * CF + ln(x) * CF + ln(x) * x * CF);
            result += result_r0 * ln(1 - z) + result_r1 * ln(1 - z) * ln(1 - z) / 2;
        } else if (orders == 922001) {
        } else if (orders == 922010) {
            result += (3 * LMUF * CF - 3 * x * LMUF * CF - 1. / 6. * pow(pi, 2) * LMUF * CF - 1. / 6. * pow(pi, 2) * x * LMUF * CF + 3 * ln(x) * LMUF * CF - 3 * ln(x) * x * LMUF * CF + pow(ln(x), 2) * LMUF * CF + pow(ln(x), 2) * x * LMUF * CF - 5. / 2. * ln(omx) * LMUF * CF + 5. / 2. * ln(omx) * x * LMUF * CF + Li2(x) * LMUF * CF + Li2(x) * x * LMUF * CF);
            result_r0 = (-5. / 2. * LMUF * CF + 5. / 2. * x * LMUF * CF - ln(x) * LMUF * CF - ln(x) * x * LMUF * CF);
            result += result_r0 * ln(1 - z);
        } else if (orders == 922100) {
        } else if (orders == 922011) {
        } else if (orders == 922101) {
        } else if (orders == 922110) {
        } else if (orders == 922002) {
        } else if (orders == 922020) {
            result += (5. / 4. * pow(LMUF, 2) * CF - 5. / 4. * x * pow(LMUF, 2) * CF + 1. / 2. * ln(x) * pow(LMUF, 2) * CF + 1. / 2. * ln(x) * x * pow(LMUF, 2) * CF);
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
