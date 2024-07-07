from configs.eh import *

LMUR = 1
LMUF = 1
LMUA = 1


def ct_nnlo_q2qp_eq(x, z, rsl, orders):

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
                result += -5.0 / 36.0 * pow(z, -1) * CF - 1.0 / 3.0 * CF - 1.0 / 6.0 * pow(pi, 2) * CF - 23.0 / 12.0 * z * CF + 43.0 / 18.0 * pow(z, 2) * CF + 19.0 / 36.0 * x * pow(z, -1) * CF + 8.0 / 3.0 * x * CF - 1.0 / 6.0 * x * pow(pi, 2) * CF + 13.0 / 12.0 * x * z * CF - 1.0 / 3.0 * x * z * pow(pi, 2) * CF - 77.0 / 18.0 * x * pow(z, 2) * CF - 4.0 / 3.0 * ln(x) * pow(z, -1) * CF * pow(omx, -1) + 2.0 / 3.0 * ln(x) * pow(z, -1) * CF - 5.0 / 2.0 * ln(x) * CF * pow(omx, -1) + ln(x) * CF + 5.0 / 2.0 * ln(x) * z * CF * pow(omx, -1) - 3 * ln(x) * z * CF + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF * pow(omx, -1) + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF + 2.0 / 3.0 * ln(x) * x * pow(z, -1) * CF + 3 * ln(x) * x * CF - ln(x) * x * z * CF - 8.0 / 3.0 * ln(x) * x * pow(z, 2) * CF - 3 * ln(x) * ln(z) * CF * pow(omx, -1) + 2 * ln(x) * ln(z) * CF - 3 * ln(x) * ln(z) * z * CF * pow(omx, -1) + 2 * ln(x) * ln(z) * x * CF + 4 * ln(x) * ln(z) * x * z * CF - 1.0 / 3.0 * ln(z) * pow(z, -1) * CF - 3.0 / 2.0 * ln(z) * CF - 1.0 / 2.0 * ln(z) * z * CF - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF - 1.0 / 3.0 * ln(z) * x * pow(z, -1) * CF - 1.0 / 2.0 * ln(z) * x * CF + 7.0 / 2.0 * ln(z) * x * z * CF + 4.0 / 3.0 * ln(z) * x * pow(z, 2) * CF - pow(ln(z), 2) * CF - pow(ln(z), 2) * x * CF - 2 * pow(ln(z), 2) * x * z * CF - ln(z) * ln(omx) * CF - ln(z) * ln(omx) * x * CF - 2 * ln(z) * ln(omx) * x * z * CF - 1.0 / 3.0 * ln(omx) * pow(z, -1) * CF - 1.0 / 2.0 * ln(omx) * CF + 3.0 / 2.0 * ln(omx) * z * CF - 2.0 / 3.0 * ln(omx) * pow(z, 2) * CF - 1.0 / 3.0 * ln(omx) * x * pow(z, -1) * CF - 3.0 / 2.0 * ln(omx) * x * CF + 1.0 / 2.0 * ln(omx) * x * z * CF + 4.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF
                result += -1.0 / 3.0 * ln(omz) * pow(z, -1) * CF - 1.0 / 2.0 * ln(omz) * CF + 3.0 / 2.0 * ln(omz) * z * CF - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF - 1.0 / 3.0 * ln(omz) * x * pow(z, -1) * CF - 3.0 / 2.0 * ln(omz) * x * CF + 1.0 / 2.0 * ln(omz) * x * z * CF + 4.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF + Li2(z) * CF + Li2(z) * x * CF + 2 * Li2(z) * x * z * CF
        elif orders == "001":
            if z != x and z != round(1 - x, ndecimals):
                result += +1.0 / 3.0 * LMUA * pow(z, -1) * CF + 1.0 / 2.0 * LMUA * CF - 3.0 / 2.0 * LMUA * z * CF + 2.0 / 3.0 * LMUA * pow(z, 2) * CF + 1.0 / 3.0 * LMUA * x * pow(z, -1) * CF + 3.0 / 2.0 * LMUA * x * CF - 1.0 / 2.0 * LMUA * x * z * CF - 4.0 / 3.0 * LMUA * x * pow(z, 2) * CF + ln(z) * LMUA * CF + ln(z) * LMUA * x * CF + 2 * ln(z) * LMUA * x * z * CF
        return result
    elif rsl == "rs":
        result = 0
        return result
    elif rsl == "rl":
        result = 0
        return result
    elif rsl == "sr":
        result = 0
        if orders == "000":
            result_0r = -7.0 / 18.0 * pow(z, -1) * CF - 10.0 / 3.0 * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 7.0 / 3.0 * z * CF + 1.0 / 6.0 * z * pow(pi, 2) * CF + 25.0 / 18.0 * pow(z, 2) * CF + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF - 1.0 / 2.0 * ln(z) * CF - 2 * ln(z) * z * CF - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF + pow(ln(z), 2) * CF + pow(ln(z), 2) * z * CF + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF + 1.0 / 2.0 * ln(omz) * CF - 1.0 / 2.0 * ln(omz) * z * CF - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF - Li2(z) * CF - Li2(z) * z * CF
            result_1r = 2.0 / 3.0 * pow(z, -1) * CF + 1.0 / 2.0 * CF - 1.0 / 2.0 * z * CF - 2.0 / 3.0 * pow(z, 2) * CF + ln(z) * CF + ln(z) * z * CF
            result += result_0r * 1 / (1 - x) + result_1r * ln(1 - x) / (1 - x)
        elif orders == "001":
            result_0r = -2.0 / 3.0 * LMUA * pow(z, -1) * CF - 1.0 / 2.0 * LMUA * CF + 1.0 / 2.0 * LMUA * z * CF + 2.0 / 3.0 * LMUA * pow(z, 2) * CF - ln(z) * LMUA * CF - ln(z) * LMUA * z * CF
            result += result_0r * 1 / (1 - x)
        return result
    elif rsl == "ss":
        result = 0
        return result
    elif rsl == "sl":
        result = 0
        return result
    elif rsl == "lr":
        result = 0
        if orders == "000":
            result_0r = -7.0 / 18.0 * pow(z, -1) * CF - 10.0 / 3.0 * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 7.0 / 3.0 * z * CF + 1.0 / 6.0 * z * pow(pi, 2) * CF + 25.0 / 18.0 * pow(z, 2) * CF + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF - 1.0 / 2.0 * ln(z) * CF - 2 * ln(z) * z * CF - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF + pow(ln(z), 2) * CF + pow(ln(z), 2) * z * CF + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF + 1.0 / 2.0 * ln(omz) * CF - 1.0 / 2.0 * ln(omz) * z * CF - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF - Li2(z) * CF - Li2(z) * z * CF
            result_1r = 2.0 / 3.0 * pow(z, -1) * CF + 1.0 / 2.0 * CF - 1.0 / 2.0 * z * CF - 2.0 / 3.0 * pow(z, 2) * CF + ln(z) * CF + ln(z) * z * CF
            result += -107.0 / 108.0 * pow(z, -1) * CF - 11.0 / 9.0 * CF + 2 * zeta3 * CF - 1.0 / 6.0 * pow(pi, 2) * CF - 4.0 / 9.0 * z * CF + 2 * z * zeta3 * CF - 1.0 / 4.0 * z * pow(pi, 2) * CF + 287.0 / 108.0 * pow(z, 2) * CF - 7.0 / 18.0 * ln(z) * pow(z, -1) * CF - 5 * ln(z) * CF + 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF - 9.0 / 2.0 * ln(z) * z * CF + 1.0 / 6.0 * ln(z) * z * pow(pi, 2) * CF - 31.0 / 18.0 * ln(z) * pow(z, 2) * CF + 1.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF - 1.0 / 8.0 * pow(ln(z), 2) * CF - 5.0 / 8.0 * pow(ln(z), 2) * z * CF + 5.0 / 12.0 * pow(ln(z), 3) * CF + 5.0 / 12.0 * pow(ln(z), 3) * z * CF - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * z * CF - 7.0 / 18.0 * ln(omz) * pow(z, -1) * CF - 10.0 / 3.0 * ln(omz) * CF + 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF + 7.0 / 3.0 * ln(omz) * z * CF + 1.0 / 6.0 * ln(omz) * z * pow(pi, 2) * CF + 25.0 / 18.0 * ln(omz) * pow(z, 2) * CF + 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF + 1.0 / 4.0 * pow(ln(omz), 2) * CF - 1.0 / 4.0 * pow(ln(omz), 2) * z * CF - 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF - ln(omz) * Li2(z) * CF - ln(omz) * Li2(z) * z * CF - Li3(1 - z) * CF - Li3(1 - z) * z * CF - 2 * Li3(z) * CF - 2 * Li3(z) * z * CF - 2.0 / 3.0 * Li2(z) * pow(z, -1) * CF + 1.0 / 2.0 * Li2(z) * CF + 2 * Li2(z) * z * CF + 2.0 / 3.0 * Li2(z) * pow(z, 2) * CF
            result += result_0r * ln(1 - x) + result_1r * (1 / 2) * ln(1 - x) * ln(1 - x)
        elif orders == "001":
            result_0r = -2.0 / 3.0 * LMUA * pow(z, -1) * CF - 1.0 / 2.0 * LMUA * CF + 1.0 / 2.0 * LMUA * z * CF + 2.0 / 3.0 * LMUA * pow(z, 2) * CF - ln(z) * LMUA * CF - ln(z) * LMUA * z * CF
            result += +7.0 / 18.0 * LMUA * pow(z, -1) * CF + 10.0 / 3.0 * LMUA * CF - 1.0 / 6.0 * LMUA * pow(pi, 2) * CF - 7.0 / 3.0 * LMUA * z * CF - 1.0 / 6.0 * LMUA * z * pow(pi, 2) * CF - 25.0 / 18.0 * LMUA * pow(z, 2) * CF - 2.0 / 3.0 * ln(z) * LMUA * pow(z, -1) * CF + 1.0 / 2.0 * ln(z) * LMUA * CF + 2 * ln(z) * LMUA * z * CF + 2.0 / 3.0 * ln(z) * LMUA * pow(z, 2) * CF - pow(ln(z), 2) * LMUA * CF - pow(ln(z), 2) * LMUA * z * CF - 2.0 / 3.0 * ln(omz) * LMUA * pow(z, -1) * CF - 1.0 / 2.0 * ln(omz) * LMUA * CF + 1.0 / 2.0 * ln(omz) * LMUA * z * CF + 2.0 / 3.0 * ln(omz) * LMUA * pow(z, 2) * CF + Li2(z) * LMUA * CF + Li2(z) * LMUA * z * CF
            result += result_0r * ln(1 - x)
        elif orders == "002":
            result += +1.0 / 3.0 * pow(LMUA, 2) * pow(z, -1) * CF + 1.0 / 4.0 * pow(LMUA, 2) * CF - 1.0 / 4.0 * pow(LMUA, 2) * z * CF - 1.0 / 3.0 * pow(LMUA, 2) * pow(z, 2) * CF + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * z * CF
        return result
    elif rsl == "ls":
        result = 0
        return result
    elif rsl == "ll":
        result = 0
        return result
    else:
        raise ValueError("Invalid rsl value")
