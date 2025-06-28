#include "../sidis.h"

double ct_nlo_g2q_eq(double x, double z, double Q, int rsl, int orders) {

    double result = 0.0;
    double result_r0;

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

            double pt0 = ct_nlo_g2q_eq(x0, z0, Q, rsl, orders);
            double pt1 = ct_nlo_g2q_eq(x1, z1, Q, rsl, orders);
            double pt2 = ct_nlo_g2q_eq(x2, z2, Q, rsl, orders);

            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        } else if (std::abs(v) < .99 * tiny) {
            double v0 = -tiny;
            double v1 = tiny;

            double x0 = .5 * (u + v0);
            double z0 = .5 * (u - v0);
            double x1 = .5 * (u + v1);
            double z1 = .5 * (u - v1);

            double pt0 = ct_nlo_g2q_eq(x0, z0, Q, rsl, orders);
            double pt1 = ct_nlo_g2q_eq(x1, z1, Q, rsl, orders);
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

            double pt0 = ct_nlo_g2q_eq(x0, z0, Q, rsl, orders);
            double pt1 = ct_nlo_g2q_eq(x1, z1, Q, rsl, orders);
            result = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        } else if (orders == 912000) {
            if (z != x && z != 1. - x) {
                result += pow(z, -1) * TR - 2 * TR - 2 * x * pow(z, -1) * TR + 4 * x * TR + 2 * pow(x, 2) * pow(z, -1) * TR - 4 * pow(x, 2) * TR;
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
            result_r0 = TR - 2 * x * TR + 2 * pow(x, 2) * TR;
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
            result += 2 * x * TR - 2 * pow(x, 2) * TR - ln(x) * TR + 2 * ln(x) * x * TR - 2 * ln(x) * pow(x, 2) * TR + ln(omx) * TR - 2 * ln(omx) * x * TR + 2 * ln(omx) * pow(x, 2) * TR;
            result_r0 = TR - 2 * x * TR + 2 * pow(x, 2) * TR;
            result += result_r0 * ln(1 - z);
        } else if (orders == 912001) {
        } else if (orders == 912010) {
            result += -LMUF * TR + 2 * LMUF * x * TR - 2 * LMUF * pow(x, 2) * TR;
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 87) {

        if (orders == 912000) {
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
        } else if (orders == 912001) {
        } else if (orders == 912010) {
        } else if (orders == 912100) {
        } else if (orders == 912011) {
        } else if (orders == 912101) {
        } else if (orders == 912110) {
        } else if (orders == 912002) {
        } else if (orders == 912020) {
        }

    } else if (rsl == 97) {

        if (orders == 912000) {
        } else if (orders == 912001) {
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
        } else if (orders == 912001) {
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
        } else if (orders == 912001) {
        } else if (orders == 912010) {
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
