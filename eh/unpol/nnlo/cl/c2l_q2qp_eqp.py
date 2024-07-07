from configs.eh import *

LMUR = 1
LMUF = 1
LMUA = 1


def cl_nnlo_q2qp_eqp(x, z, rsl, orders):

    omz = 1.0 - z
    opz = 1.0 + z
    omx = 1.0 - x
    opx = 1.0 + x
    op6xpxsq = 1.0 + 6.0 * x + x * x
    xmz = x - z
    omxmz = 1.0 - x - z
    poly2 = 1 + 2 * x + x * x - 4 * x * z
    sqrtxz1 = sqrt(1 - 2 * z + z * z + 4 * x * z)
    sqrtxz2 = sqrt(poly2)
    sqrtxz3 = sqrt(x / z)

    if rsl == "rr":
        result = 0
        if orders == "000":
            if z != x and z != round(1 - x, ndecimals):
                result += 20.0 / 9.0 * pow(x, -1) * CF - 50.0 / 3.0 * CF + 20 * z * CF + 14.0 / 3.0 * x * CF - 2.0 / 3.0 * x * pow(pi, 2) * CF - 20 * x * z * CF + 88.0 / 9.0 * pow(x, 2) * CF - 1.0 / 2.0 * ln(x) * pow(x, -1) * pow(poly2, -1) * CF + 1.0 / 2.0 * ln(x) * pow(x, -1) * CF + 1.0 / 2.0 * ln(x) * pow(poly2, -1) * CF - 3.0 / 2.0 * ln(x) * CF + 10 * ln(x) * z * CF + ln(x) * x * pow(poly2, -1) * CF - 33.0 / 2.0 * ln(x) * x * CF + 10 * ln(x) * x * z * CF - ln(x) * pow(x, 2) * pow(poly2, -1) * CF - 17.0 / 2.0 * ln(x) * pow(x, 2) * CF - 1.0 / 2.0 * ln(x) * pow(x, 3) * pow(poly2, -1) * CF + 1.0 / 2.0 * ln(x) * pow(x, 4) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(sqrtxz2, -1) * CF + ln(x) * ln(1 - sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 4 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF + 20 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF - 20 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                result += -1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(sqrtxz2, -1) * CF - ln(x) * ln(1 + sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF - 20 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF + 20 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * pow(ln(x), 2) * x * CF - 2 * ln(x) * ln(z) * x * CF - 4 * ln(x) * ln(omz) * x * CF - 1.0 / 2.0 * ln(z) * pow(x, -1) * pow(poly2, -1) * CF + 11.0 / 6.0 * ln(z) * pow(x, -1) * CF - 1.0 / 2.0 * ln(z) * pow(poly2, -1) * CF - 13.0 / 2.0 * ln(z) * CF + 10 * ln(z) * z * CF + ln(z) * x * pow(poly2, -1) * CF + 3.0 / 2.0 * ln(z) * x * CF - 10 * ln(z) * x * z * CF + ln(z) * pow(x, 2) * pow(poly2, -1) * CF + 19.0 / 6.0 * ln(z) * pow(x, 2) * CF - 1.0 / 2.0 * ln(z) * pow(x, 3) * pow(poly2, -1) * CF - 1.0 / 2.0 * ln(z) * pow(x, 4) * pow(poly2, -1) * CF + 4.0 / 3.0 * ln(omx) * pow(x, -1) * CF - 4 * ln(omx) * CF + 8.0 / 3.0 * ln(omx) * pow(x, 2) * CF + 4.0 / 3.0 * ln(omz) * pow(x, -1) * CF - 4 * ln(omz) * CF + 8.0 / 3.0 * ln(omz) * pow(x, 2) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                result += +1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF + 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF - 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF
                result += -Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF - 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF + 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF - 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF
                result += +20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF + 20 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF - 20 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 7.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * Li2(x) * x * CF
        elif orders == "010":
            if z != x and z != round(1 - x, ndecimals):
                result += -4.0 / 3.0 * LMUF * pow(x, -1) * CF + 4 * LMUF * CF - 8.0 / 3.0 * LMUF * pow(x, 2) * CF + 4 * ln(x) * LMUF * x * CF
        return result
    elif rsl == "rs":
        result = 0
        return result
    elif rsl == "rl":
        result = 0
        return result
    elif rsl == "sr":
        result = 0
        return result
    elif rsl == "ss":
        result = 0
        return result
    elif rsl == "sl":
        result = 0
        return result
    elif rsl == "lr":
        result = 0
        return result
    elif rsl == "ls":
        result = 0
        return result
    elif rsl == "ll":
        result = 0
        return result
    else:
        raise ValueError("Invalid rsl value")
