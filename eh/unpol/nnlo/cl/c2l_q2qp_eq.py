from configs.eh import *

LMUR = 1
LMUF = 1
LMUA = 1


def cl_nnlo_q2qp_eq(x, z, rsl, orders):

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
                result += -4 * CF + 2 * z * CF + 2 * pow(z, 2) * CF + 7 * x * CF - 1.0 / 3.0 * x * pow(pi, 2) * CF - 2.0 / 3.0 * x * z * pow(pi, 2) * CF - 7 * x * pow(z, 2) * CF + 8 * ln(x) * x * CF - 4 * ln(x) * x * z * CF - 4 * ln(x) * x * pow(z, 2) * CF + 4 * ln(x) * ln(z) * x * CF + 8 * ln(x) * ln(z) * x * z * CF - 2 * ln(z) * CF - 4 * ln(z) * z * CF - 2 * ln(z) * x * CF + 8 * ln(z) * x * z * CF + 2 * ln(z) * x * pow(z, 2) * CF - 2 * pow(ln(z), 2) * x * CF - 4 * pow(ln(z), 2) * x * z * CF - 2 * ln(z) * ln(omx) * x * CF - 4 * ln(z) * ln(omx) * x * z * CF - 4 * ln(omx) * x * CF + 2 * ln(omx) * x * z * CF + 2 * ln(omx) * x * pow(z, 2) * CF - 4 * ln(omz) * x * CF + 2 * ln(omz) * x * z * CF + 2 * ln(omz) * x * pow(z, 2) * CF + 2 * Li2(z) * x * CF + 4 * Li2(z) * x * z * CF
        elif orders == "001":
            if z != x and z != round(1 - x, ndecimals):
                result += +4 * LMUA * x * CF - 2 * LMUA * x * z * CF - 2 * LMUA * x * pow(z, 2) * CF + 2 * ln(z) * LMUA * x * CF + 4 * ln(z) * LMUA * x * z * CF
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
