#include "../sidis.h"

double cp_nlo_q2q_eq(double x, double z, double Q, int rsl, int orders) {

    double result = 0.0;
    double result_r0, result_0r, result_00, result_1l, result_0l, result_l1, result_l0;

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

            double pt0 = cp_nlo_q2q_eq(x0, z0, Q, rsl, orders);
            double pt1 = cp_nlo_q2q_eq(x1, z1, Q, rsl, orders);
            double pt2 = cp_nlo_q2q_eq(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = cp_nlo_q2q_eq(x0, z0, Q, rsl, orders);
            double pt1 = cp_nlo_q2q_eq(x1, z1, Q, rsl, orders);
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

            double pt0 = cp_nlo_q2q_eq(x0, z0, Q, rsl, orders);
            double pt1 = cp_nlo_q2q_eq(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 912000) {
            if (z != x && z != 1. - x) {
                result += 2 * z * CF + 2 * x * CF;
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
        } else if (orders == 912001) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 912010) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 912100) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 912011) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 912101) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 912110) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 912002) {
            if (z != x && z != 1. - x) {
            }
        } else if (orders == 912020) {
            if (z != x && z != 1. - x) {
            }
        }

    } else if (rsl == 78) {

        if (orders == 912000) {
            result_r0 = -CF - x * CF;
            result += result_r0 * 1 / (1 - z);
        } else if (orders == 912001) {
        } else if (orders == 912010) {
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 79) {

        if (orders == 912000) {
            result += CF - x * CF - 2 * ln(x) * CF * pow(omx, -1) + ln(x) * CF + ln(x) * x * CF - ln(omx) * CF - ln(omx) * x * CF;
            result_r0 = -CF - x * CF;
            result += result_r0 * ln(1 - z);
        } else if (orders == 912001) {
        } else if (orders == 912010) {
            result += +LMUF * CF + x * LMUF * CF;
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 87) {

        if (orders == 912000) {
            result_0r = -CF - z * CF;
            result += result_0r * 1 / (1 - x);
        } else if (orders == 912001) {
        } else if (orders == 912010) {
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 88) {

        if (orders == 912000) {
            result_00 = 2 * CF;
            result += result_00 * (1 / (1 - x)) * (1 / (1 - z));
        } else if (orders == 912001) {
        } else if (orders == 912010) {
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 89) {

        if (orders == 912000) {
            result_1l = 2 * CF;
            result += result_1l * ln(1 - x) / (1 - x);
            result_00 = 2 * CF;
            result += result_00 * (1 / (1 - x)) * (ln(1 - z));
        } else if (orders == 912001) {
        } else if (orders == 912010) {
            result_0l = -2 * LMUF * CF;
            result += result_0l * 1 / (1 - x);
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 97) {

        if (orders == 912000) {
            result += CF - z * CF + 2 * ln(z) * CF * pow(omz, -1) - ln(z) * CF - ln(z) * z * CF - ln(omz) * CF - ln(omz) * z * CF;
            result_0r = -CF - z * CF;
            result += result_0r * ln(1 - x);
        } else if (orders == 912001) {
            result += +LMUA * CF + z * LMUA * CF;
        } else if (orders == 912010) {
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 98) {

        if (orders == 912000) {
            result_l1 = 2 * CF;
            result += result_l1 * ln(1 - z) / (1 - z);
            result_00 = 2 * CF;
            result += result_00 * (1 / (1 - z)) * (ln(1 - x));
        } else if (orders == 912001) {
            result_l0 = -2 * LMUA * CF;
            result += result_l0 * 1 / (1 - z);
        } else if (orders == 912010) {
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 99) {

        if (orders == 912000) {
            result += -8 * CF;
            result_1l = 2 * CF;
            result += result_1l * ln(1 - x) * ln(1 - x) / 2;
            result_l1 = 2 * CF;
            result += result_l1 * ln(1 - z) * ln(1 - z) / 2;
            result_00 = 2 * CF;
            result += result_00 * (ln(1 - x)) * (ln(1 - z));
        } else if (orders == 912001) {
            result += -3. / 2. * LMUA * CF;
            result_l0 = -2 * LMUA * CF;
            result += result_l0 * ln(1 - z);
        } else if (orders == 912010) {
            result += -3. / 2. * LMUF * CF;
            result_0l = -2 * LMUF * CF;
            result += result_0l * ln(1 - x);
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else {
        throw std::invalid_argument("Invalid rsl value");
    }

    return result;
}