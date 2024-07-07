from configs.eh import *

LMUR = 1
LMUF = 1
LMUA = 1


def ct_nnlo_q2q_eqp(x, z, rsl, orders):

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
                result += -5.0 / 8.0 * pow(x, -1) * pow(z, -1) * CF + 5.0 / 8.0 * pow(x, -1) * CF - 5.0 / 8.0 * pow(z, -2) * CF - 15.0 / 4.0 * pow(z, -1) * CF + 15.0 / 4.0 * CF + 5.0 / 8.0 * z * CF + 5.0 / 8.0 * x * pow(z, -2) * CF + 15.0 / 4.0 * x * pow(z, -1) * CF - 15.0 / 4.0 * x * CF - 5.0 / 8.0 * x * z * CF + 5.0 / 8.0 * pow(x, 2) * pow(z, -1) * CF - 5.0 / 8.0 * pow(x, 2) * CF + 5.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -2) * sqrtxz3 * CF + 9.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF + 9.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 5.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, -2) * sqrtxz3 * CF + 13.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * sqrtxz3 * CF + 5.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 9.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF + 9.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * z * sqrtxz3 * CF + 5.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, 2) * sqrtxz3 * CF - 5.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 9.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF - 9.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 5.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - 13.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * sqrtxz3 * CF - 5.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 9.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * z * sqrtxz3 * CF - 5.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, 2) * sqrtxz3 * CF - 5.0 / 16.0 * InvTanInt(-sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 9.0 / 8.0 * InvTanInt(-sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF
                result += -9.0 / 8.0 * InvTanInt(-sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 5.0 / 16.0 * InvTanInt(-sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - 13.0 / 4.0 * InvTanInt(-sqrtxz3) * sqrtxz3 * CF - 5.0 / 16.0 * InvTanInt(-sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 9.0 / 8.0 * InvTanInt(-sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9.0 / 8.0 * InvTanInt(-sqrtxz3) * x * z * sqrtxz3 * CF - 5.0 / 16.0 * InvTanInt(-sqrtxz3) * pow(x, 2) * sqrtxz3 * CF - 5.0 / 8.0 * InvTanInt(z * sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 9.0 / 4.0 * InvTanInt(z * sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF - 9.0 / 4.0 * InvTanInt(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 5.0 / 8.0 * InvTanInt(z * sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - 13.0 / 2.0 * InvTanInt(z * sqrtxz3) * sqrtxz3 * CF - 5.0 / 8.0 * InvTanInt(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 9.0 / 4.0 * InvTanInt(z * sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9.0 / 4.0 * InvTanInt(z * sqrtxz3) * x * z * sqrtxz3 * CF - 5.0 / 8.0 * InvTanInt(z * sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 5.0 / 16.0 * InvTanInt(sqrtxz3) * pow(x, -2) * sqrtxz3 * CF + 9.0 / 8.0 * InvTanInt(sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF + 9.0 / 8.0 * InvTanInt(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 5.0 / 16.0 * InvTanInt(sqrtxz3) * pow(z, -2) * sqrtxz3 * CF + 13.0 / 4.0 * InvTanInt(sqrtxz3) * sqrtxz3 * CF + 5.0 / 16.0 * InvTanInt(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 9.0 / 8.0 * InvTanInt(sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF + 9.0 / 8.0 * InvTanInt(sqrtxz3) * x * z * sqrtxz3 * CF + 5.0 / 16.0 * InvTanInt(sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 5.0 / 16.0 * ln(x) * pow(x, -1) * pow(z, -1) * CF - 5.0 / 16.0 * ln(x) * pow(x, -1) * CF - 5.0 / 16.0 * ln(x) * pow(z, -2) * CF - 17.0 / 8.0 * ln(x) * pow(z, -1) * CF + 17.0 / 8.0 * ln(x) * CF + 5.0 / 16.0 * ln(x) * z * CF
                result += -5.0 / 16.0 * ln(x) * x * pow(z, -2) * CF - 17.0 / 8.0 * ln(x) * x * pow(z, -1) * CF + 17.0 / 8.0 * ln(x) * x * CF + 5.0 / 16.0 * ln(x) * x * z * CF + 5.0 / 16.0 * ln(x) * pow(x, 2) * pow(z, -1) * CF - 5.0 / 16.0 * ln(x) * pow(x, 2) * CF - 2 * ln(x) * ln(z) * pow(z, -1) * CF - 2 * ln(x) * ln(z) * CF - 2 * ln(x) * ln(z) * x * pow(z, -1) * CF - 2 * ln(x) * ln(z) * x * CF - 5.0 / 16.0 * ln(z) * pow(x, -1) * pow(z, -1) * CF - 5.0 / 16.0 * ln(z) * pow(x, -1) * CF + 5.0 / 16.0 * ln(z) * pow(z, -2) * CF - 17.0 / 8.0 * ln(z) * pow(z, -1) * CF - 17.0 / 8.0 * ln(z) * CF + 5.0 / 16.0 * ln(z) * z * CF - 5.0 / 16.0 * ln(z) * x * pow(z, -2) * CF + 17.0 / 8.0 * ln(z) * x * pow(z, -1) * CF + 17.0 / 8.0 * ln(z) * x * CF - 5.0 / 16.0 * ln(z) * x * z * CF + 5.0 / 16.0 * ln(z) * pow(x, 2) * pow(z, -1) * CF + 5.0 / 16.0 * ln(z) * pow(x, 2) * CF
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
