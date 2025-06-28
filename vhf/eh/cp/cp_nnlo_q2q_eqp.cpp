#include "../sidis.h"

double cp_nnlo_q2q_eqp(double x, double z, double Q, int rsl, int orders) {

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

            double pt0 = cp_nnlo_q2q_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cp_nnlo_q2q_eqp(x1, z1, Q, rsl, orders);
            double pt2 = cp_nnlo_q2q_eqp(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = cp_nnlo_q2q_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cp_nnlo_q2q_eqp(x1, z1, Q, rsl, orders);
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

            double pt0 = cp_nnlo_q2q_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cp_nnlo_q2q_eqp(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 922000) {
            if (z != x && z != 1. - x) {
                result += -8 * pow(z, -1) * CF + 8 * CF + 8 * x * pow(z, -1) * CF - 8 * x * CF + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(x, -1) * CF * sqrtxz3 + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(z, -1) * CF * sqrtxz3 + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * sqrtxz3 + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * x * CF * sqrtxz3 - 3 * ln(x) * pow(z, -1) * CF + 3 * ln(x) * CF - 3 * ln(x) * x * pow(z, -1) * CF + 3 * ln(x) * x * CF - 2 * ln(x) * ln(z) * pow(z, -1) * CF - 2 * ln(x) * ln(z) * CF - 2 * ln(x) * ln(z) * x * pow(z, -1) * CF - 2 * ln(x) * ln(z) * x * CF - 3 * ln(z) * pow(z, -1) * CF - 3 * ln(z) * CF + 3 * ln(z) * x * pow(z, -1) * CF + 3 * ln(z) * x * CF - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(x, -1) * CF * sqrtxz3 - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(z, -1) * CF * sqrtxz3 - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * sqrtxz3 - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * x * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * pow(x, -1) * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * pow(z, -1) * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * z * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * x * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * pow(x, -1) * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * pow(z, -1) * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * z * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * x * CF * sqrtxz3 + 2 * InvTanInt(sqrtxz3) * pow(x, -1) * CF * sqrtxz3 + 2 * InvTanInt(sqrtxz3) * pow(z, -1) * CF * sqrtxz3 + 2 * InvTanInt(sqrtxz3) * z * CF * sqrtxz3 + 2 * InvTanInt(sqrtxz3) * x * CF * sqrtxz3;
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
            result += (-2 * CF + 2 * x * CF - 3 * ln(x) * CF + ln(x) * x * CF - pow(ln(x), 2) * CF - 1. / 2. * pow(ln(x), 2) * x * CF);
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
