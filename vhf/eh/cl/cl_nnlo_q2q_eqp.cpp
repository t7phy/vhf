#include "../sidis.h"

double cl_nnlo_q2q_eqp(double x, double z, double Q, int rsl, int orders) {

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

            double pt0 = cl_nnlo_q2q_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_q2q_eqp(x1, z1, Q, rsl, orders);
            double pt2 = cl_nnlo_q2q_eqp(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = cl_nnlo_q2q_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_q2q_eqp(x1, z1, Q, rsl, orders);
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

            double pt0 = cl_nnlo_q2q_eqp(x0, z0, Q, rsl, orders);
            double pt1 = cl_nnlo_q2q_eqp(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 922000) {
            if (z != x && z != 1. - x) {
                result += 3.0 / 4.0 * pow(x, -1) * pow(z, -1) * CF - 3.0 / 4.0 * pow(x, -1) * CF + 3.0 / 4.0 * pow(z, -2) * CF - 7.0 / 2.0 * pow(z, -1) * CF + 3.0 / 2.0 * CF + 5.0 / 4.0 * z * CF - 3.0 / 4.0 * x * pow(z, -2) * CF + 3.0 / 2.0 * x * pow(z, -1) * CF + 1.0 / 2.0 * x * CF - 5.0 / 4.0 * x * z * CF + 5.0 / 4.0 * pow(x, 2) * pow(z, -1) * CF - 5.0 / 4.0 * pow(x, 2) * CF - 3.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -2) * sqrtxz3 * CF + 1.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF - 3.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 3.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, -2) * sqrtxz3 * CF + ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * sqrtxz3 * CF + 5.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 3.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF + 9.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * z * sqrtxz3 * CF + 5.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 3.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 1.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF + 3.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 3.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - ArcTan(sqrtxz3) * ln(sqrtxz3) * sqrtxz3 * CF - 5.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * z * sqrtxz3 * CF - 5.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 3.0 / 8.0 * InvTanInt(-sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 1.0 / 4.0 * InvTanInt(-sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF + 3.0 / 4.0 * InvTanInt(-sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 3.0 / 8.0 * InvTanInt(-sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - 1.0 / 2.0 * InvTanInt(-sqrtxz3) * sqrtxz3 * CF - 5.0 / 8.0 * InvTanInt(-sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3.0 / 4.0 * InvTanInt(-sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9.0 / 4.0 * InvTanInt(-sqrtxz3) * x * z * sqrtxz3 * CF - 5.0 / 8.0 * InvTanInt(-sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 3.0 / 4.0 * InvTanInt(z * sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 1.0 / 2.0 * InvTanInt(z * sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF + 3.0 / 2.0 * InvTanInt(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 3.0 / 4.0 * InvTanInt(z * sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - InvTanInt(z * sqrtxz3) * sqrtxz3 * CF - 5.0 / 4.0 * InvTanInt(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3.0 / 2.0 * InvTanInt(z * sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9.0 / 2.0 * InvTanInt(z * sqrtxz3) * x * z * sqrtxz3 * CF - 5.0 / 4.0 * InvTanInt(z * sqrtxz3) * pow(x, 2) * sqrtxz3 * CF - 3.0 / 8.0 * InvTanInt(sqrtxz3) * pow(x, -2) * sqrtxz3 * CF + 1.0 / 4.0 * InvTanInt(sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF - 3.0 / 4.0 * InvTanInt(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 3.0 / 8.0 * InvTanInt(sqrtxz3) * pow(z, -2) * sqrtxz3 * CF + 1.0 / 2.0 * InvTanInt(sqrtxz3) * sqrtxz3 * CF + 5.0 / 8.0 * InvTanInt(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 3.0 / 4.0 * InvTanInt(sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF + 9.0 / 4.0 * InvTanInt(sqrtxz3) * x * z * sqrtxz3 * CF + 5.0 / 8.0 * InvTanInt(sqrtxz3) * pow(x, 2) * sqrtxz3 * CF - 3.0 / 8.0 * ln(x) * pow(x, -1) * pow(z, -1) * CF + 3.0 / 8.0 * ln(x) * pow(x, -1) * CF + 3.0 / 8.0 * ln(x) * pow(z, -2) * CF - 1.0 / 4.0 * ln(x) * pow(z, -1) * CF - 3.0 / 4.0 * ln(x) * CF + 5.0 / 8.0 * ln(x) * z * CF + 3.0 / 8.0 * ln(x) * x * pow(z, -2) * CF - 13.0 / 4.0 * ln(x) * x * pow(z, -1) * CF + 9.0 / 4.0 * ln(x) * x * CF + 5.0 / 8.0 * ln(x) * x * z * CF + 5.0 / 8.0 * ln(x) * pow(x, 2) * pow(z, -1) * CF - 5.0 / 8.0 * ln(x) * pow(x, 2) * CF - 4 * ln(x) * ln(z) * x * CF + 3.0 / 8.0 * ln(z) * pow(x, -1) * pow(z, -1) * CF + 3.0 / 8.0 * ln(z) * pow(x, -1) * CF - 3.0 / 8.0 * ln(z) * pow(z, -2) * CF - 1.0 / 4.0 * ln(z) * pow(z, -1) * CF - 13.0 / 4.0 * ln(z) * CF + 5.0 / 8.0 * ln(z) * z * CF + 3.0 / 8.0 * ln(z) * x * pow(z, -2) * CF - 3.0 / 4.0 * ln(z) * x * pow(z, -1) * CF + 9.0 / 4.0 * ln(z) * x * CF - 5.0 / 8.0 * ln(z) * x * z * CF + 5.0 / 8.0 * ln(z) * pow(x, 2) * pow(z, -1) * CF + 5.0 / 8.0 * ln(z) * pow(x, 2) * CF;
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
