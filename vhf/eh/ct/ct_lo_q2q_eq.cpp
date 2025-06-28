#include "../sidis.h"

double ct_lo_q2q_eq(double x, double z, double Q, int rsl, int orders) {
    if (rsl == 99 && orders == 902000) {
        return 1.0;
    } else {
        return 0.0;
    }
}