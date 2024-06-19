from configs.eh import *


def C2Lg2gEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
    res = 0.0

    if cx == "D" and cz == "D":

        res = 0

        return res

    if cx == "D" and cz == "0":

        res = 0

        return res

    if cx == "D" and cz == "1":

        res = 0

        return res

    if cx == "D" and cz == "2":

        res = 0

        return res

    if cx == "D" and cz == "3":

        res = 0

        return res

    if cx == "0" and cz == "D":

        res = 0

        return res

    if cx == "0" and cz == "0":

        res = 0

        return res

    if cx == "0" and cz == "1":

        res = 0

        return res

    if cx == "0" and cz == "2":

        res = 0

        return res

    if cx == "0" and cz == "3":

        res = 0

        return res

    if cx == "1" and cz == "D":

        res = 0

        return res

    if cx == "1" and cz == "0":

        res = 0

        return res

    if cx == "1" and cz == "1":

        res = 0

        return res

    if cx == "1" and cz == "2":

        res = 0

        return res

    if cx == "1" and cz == "3":

        res = 0

        return res

    if cx == "2" and cz == "D":

        res = 0

        return res

    if cx == "2" and cz == "0":

        res = 0

        return res

    if cx == "2" and cz == "1":

        res = 0

        return res

    if cx == "2" and cz == "2":

        res = 0

        return res

    if cx == "2" and cz == "3":

        res = 0

        return res

    if cx == "3" and cz == "D":

        res = 0

        return res

    if cx == "3" and cz == "0":

        res = 0

        return res

    if cx == "3" and cz == "1":

        res = 0

        return res

    if cx == "3" and cz == "2":

        res = 0

        return res

    if cx == "3" and cz == "3":

        res = 0

        return res

    if cx == "D" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 0

        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 0

        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 0

        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 0

        return res

    if cx == "3" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 0

        return res

    if cx == "R" and cz == "D":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 0

        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 0

        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 0

        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 0

        return res

    if cx == "R" and cz == "3":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 0

        return res

    if cx == "R" and cz == "R":

        x = inx
        z = inz
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
        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) != round(x, ndecimals) and round(z, ndecimals) != round(1.0 - x, ndecimals):

            tmp = 0.0
            tmp = (
                2.0 / 3.0 * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2) * pow(opx, -1)
                - 2.0 / 3.0 * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2)
                + 2 * pow(NC, -1)
                - 2 * pow(NC, -1) * z
                + 4.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * pow(opx, -1)
                - 2.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2)
                - 8 * pow(NC, -1) * x * pow(z, -1)
                + 14 * pow(NC, -1) * x
                - 8 * pow(NC, -1) * x * pow(rln2, 2)
                - 1.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2)
                - 6 * pow(NC, -1) * x * z
                + 8 * pow(NC, -1) * x * z * pow(rln2, 2)
                + 2.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * pow(opx, -1)
                - 1.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2)
                + 8 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 16 * pow(NC, -1) * pow(x, 2)
                + 8 * pow(NC, -1) * pow(x, 2) * pow(rln2, 2)
                + 8 * pow(NC, -1) * pow(x, 2) * z
                - 8 * pow(NC, -1) * pow(x, 2) * z * pow(rln2, 2)
                + 2.0 / 3.0 * pow(NC, -1) * pow(x, 2) * z * pow(pi, 2)
                + 3.0 / 8.0 * NC * pow(x, -1) * pow(z, -1)
                - 3.0 / 8.0 * NC * pow(x, -1)
                + 2.0 / 3.0 * NC * pow(x, -1) * pow(pi, 2) * pow(opx, -1)
                - 2.0 / 3.0 * NC * pow(x, -1) * pow(pi, 2)
                - 2.0 / 3.0 * NC * pow(x, -1) * z * pow(pi, 2) * pow(opx, -1)
                + 2.0 / 3.0 * NC * pow(x, -1) * z * pow(pi, 2)
                + 3.0 / 8.0 * NC * pow(z, -2)
                - 7.0 / 4.0 * NC * pow(z, -1)
                - 5.0 / 4.0 * NC
                + 4.0 / 3.0 * NC * pow(pi, 2) * pow(opx, -1)
                - 2.0 / 3.0 * NC * pow(pi, 2)
                + 21.0 / 8.0 * NC * z
                - 4.0 / 3.0 * NC * z * pow(pi, 2) * pow(opx, -1)
                + 2.0 / 3.0 * NC * z * pow(pi, 2)
                - 3.0 / 8.0 * NC * x * pow(z, -2)
                - 25.0 / 4.0 * NC * x * pow(z, -1)
                - 8 * NC * x * pow(z, -1) * sqrtxz1 * rln2
                + 5.0 / 4.0 * NC * x
                + 2.0 / 3.0 * NC * x * pow(pi, 2) * pow(opx, -1)
                + 1.0 / 3.0 * NC * x * pow(pi, 2)
                + 43.0 / 8.0 * NC * x * z
                - 8 * NC * x * z * pow(rln2, 2)
                - 2.0 / 3.0 * NC * x * z * pow(pi, 2) * pow(opx, -1)
                + 1.0 / 3.0 * NC * x * z * pow(pi, 2)
                + 61.0 / 8.0 * NC * pow(x, 2) * pow(z, -1)
                + 8 * NC * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2
                + 3.0 / 8.0 * NC * pow(x, 2)
                - 8 * NC * pow(x, 2) * z
                + 8 * NC * pow(x, 2) * z * pow(rln2, 2)
            )
            tmp += (
                -2.0 / 3.0 * NC * pow(x, 2) * z * pow(pi, 2)
                + LMUF * pow(NC, -1)
                - LMUF * pow(NC, -1) * z
                + LMUF * pow(NC, -1) * x
                - LMUF * pow(NC, -1) * x * z
                - 2 * LMUF * pow(NC, -1) * pow(x, 2)
                + 2 * LMUF * pow(NC, -1) * pow(x, 2) * z
                - LMUF * NC
                + LMUF * NC * z
                - LMUF * NC * x
                + LMUF * NC * x * z
                + 2 * LMUF * NC * pow(x, 2)
                - 2 * LMUF * NC * pow(x, 2) * z
                + 4 * LMUA * pow(NC, -1) * x * pow(z, -1)
                - 2 * LMUA * pow(NC, -1) * x
                - 2 * LMUA * pow(NC, -1) * x * z
                - 4 * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * LMUA * pow(NC, -1) * pow(x, 2)
                + 2 * LMUA * pow(NC, -1) * pow(x, 2) * z
                - 4 * LMUA * NC * x * pow(z, -1)
                + 2 * LMUA * NC * x
                + 2 * LMUA * NC * x * z
                + 4 * LMUA * NC * pow(x, 2) * pow(z, -1)
                - 2 * LMUA * NC * pow(x, 2)
                - 2 * LMUA * NC * pow(x, 2) * z
                + ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                - ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * sqrtxz3
                + 3 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                - 15 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                - 3.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                + 1.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                - 7.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                - 3.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                - 7.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * sqrtxz3
                - 19.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                - 15.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                + 105.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * z * sqrtxz3
                - 35.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3
            )
            tmp += (
                -ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                + ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * sqrtxz3
                - 3 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                + 15 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                + 3.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                - 1.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                + 7.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                + 3.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                + 7.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * sqrtxz3
                + 19.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                + 15.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                - 105.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * z * sqrtxz3
                + 35.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                - 1.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                + 1.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * sqrtxz3
                - 3.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                + 15.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                + 3.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                - 1.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                + 7.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                + 3.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                + 7.0 / 4.0 * InvTanInt(-sqrtxz3) * NC * sqrtxz3
                + 19.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                + 15.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                - 105.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * x * z * sqrtxz3
            )
            tmp += (
                +35.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                - InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                + InvTanInt(z * sqrtxz3) * pow(NC, -1) * sqrtxz3
                - 3 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                + 15 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                + 3.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                - 1.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                + 7.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                + 3.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                + 7.0 / 2.0 * InvTanInt(z * sqrtxz3) * NC * sqrtxz3
                + 19.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                + 15.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                - 105.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * x * z * sqrtxz3
                + 35.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                + 1.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                - 1.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * sqrtxz3
                + 3.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                - 15.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                - 3.0 / 16.0 * InvTanInt(sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                + 1.0 / 8.0 * InvTanInt(sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                - 7.0 / 8.0 * InvTanInt(sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                - 3.0 / 16.0 * InvTanInt(sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                - 7.0 / 4.0 * InvTanInt(sqrtxz3) * NC * sqrtxz3
                - 19.0 / 16.0 * InvTanInt(sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                - 15.0 / 8.0 * InvTanInt(sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                + 105.0 / 8.0 * InvTanInt(sqrtxz3) * NC * x * z * sqrtxz3
                - 35.0 / 16.0 * InvTanInt(sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                + 12 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * rln2
            )
            tmp += (
                -12 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * rln2
                - 12 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * rln2
                + 12 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * rln2
                + 8 * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1) * sqrtxz1
                - 4 * ln(1 + sqrtxz1 - z) * NC * x * rln2
                + 12 * ln(1 + sqrtxz1 - z) * NC * x * z * rln2
                - 8 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1
                + 4 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * rln2
                - 12 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z * rln2
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * z
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2)
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * z
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x * z
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(x, 2)
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(x, 2) * z
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * z
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z
                + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * rln2
                - 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * rln2
                - 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * rln2
                + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * rln2
            )
            tmp += (
                +4 * ln(1 + sqrtxz1 + z) * NC * x * rln2
                + 4 * ln(1 + sqrtxz1 + z) * NC * x * z * rln2
                - 4 * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * rln2
                - 4 * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z * rln2
                + 8 * ln(x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                - 8 * ln(x) * pow(NC, -1) * pow(x, -1) * z
                + 3.0 / 2.0 * ln(x) * pow(NC, -1)
                + 16 * ln(x) * pow(NC, -1) * z * pow(opx, -1)
                - 19.0 / 2.0 * ln(x) * pow(NC, -1) * z
                + 4 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                + 5.0 / 2.0 * ln(x) * pow(NC, -1) * x
                - 8 * ln(x) * pow(NC, -1) * x * rln2
                + 8 * ln(x) * pow(NC, -1) * x * z * pow(opx, -1)
                - 13.0 / 2.0 * ln(x) * pow(NC, -1) * x * z
                + 8 * ln(x) * pow(NC, -1) * x * z * rln2
                - 4 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 8 * ln(x) * pow(NC, -1) * pow(x, 2) * rln2
                + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * z
                - 8 * ln(x) * pow(NC, -1) * pow(x, 2) * z * rln2
                - 3.0 / 16.0 * ln(x) * NC * pow(x, -1) * pow(z, -1)
                + 8 * ln(x) * NC * pow(x, -1) * pow(opx, -1)
                - 125.0 / 16.0 * ln(x) * NC * pow(x, -1)
                - 8 * ln(x) * NC * pow(x, -1) * z * pow(opx, -1)
                + 8 * ln(x) * NC * pow(x, -1) * z
                + 3.0 / 16.0 * ln(x) * NC * pow(z, -2)
                - 1.0 / 8.0 * ln(x) * NC * pow(z, -1)
                + 16 * ln(x) * NC * pow(opx, -1)
                - 79.0 / 8.0 * ln(x) * NC
                - 16 * ln(x) * NC * z * pow(opx, -1)
                + 157.0 / 16.0 * ln(x) * NC * z
                + 3.0 / 16.0 * ln(x) * NC * x * pow(z, -2)
                - 49.0 / 8.0 * ln(x) * NC * x * pow(z, -1)
                - 4 * ln(x) * NC * x * pow(z, -1) * sqrtxz1
                + 8 * ln(x) * NC * x * pow(opx, -1)
                - 7.0 / 8.0 * ln(x) * NC * x
                + 4 * ln(x) * NC * x * rln2
                - 8 * ln(x) * NC * x * z * pow(opx, -1)
                + 109.0 / 16.0 * ln(x) * NC * x * z
                - 8 * ln(x) * NC * x * z * rln2
                + 29.0 / 16.0 * ln(x) * NC * pow(x, 2) * pow(z, -1)
                + 4 * ln(x) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1
                + 35.0 / 16.0 * ln(x) * NC * pow(x, 2)
                - 4 * ln(x) * NC * pow(x, 2) * rln2
                - 4 * ln(x) * NC * pow(x, 2) * z
                + 8 * ln(x) * NC * pow(x, 2) * z * rln2
            )
            tmp += (
                +2 * ln(x) * LMUF * pow(NC, -1) * x
                - 2 * ln(x) * LMUF * pow(NC, -1) * x * z
                - 2 * ln(x) * LMUF * NC * x
                + 2 * ln(x) * LMUF * NC * x * z
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x * z
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2)
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * z
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * z
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC
                + 4 * ln(x) * ln(1 + x * pow(z, -1)) * NC * z * pow(opx, -1)
            )
            tmp += (
                -2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * z
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x * z * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * x * z
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * z
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z
                - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * z * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * z
                - 2 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * NC * pow(x, -1)
                + 2 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * z * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * z
                - 4 * ln(x) * ln(1 + x * z) * NC * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * NC
                + 4 * ln(x) * ln(1 + x * z) * NC * z * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * NC * z
                - 2 * ln(x) * ln(1 + x * z) * NC * x * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x * z) * NC * x
                + 2 * ln(x) * ln(1 + x * z) * NC * x * z * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * z) * NC * pow(x, 2) * z
                - 2 * ln(x) * ln(z + x) * pow(NC, -1) * x * z
                + 2 * ln(x) * ln(z + x) * pow(NC, -1) * pow(x, 2) * z
                + 2 * ln(x) * ln(z + x) * NC * x
                + 2 * ln(x) * ln(z + x) * NC * x * z
                - 2 * ln(x) * ln(z + x) * NC * pow(x, 2)
                - 2 * ln(x) * ln(z + x) * NC * pow(x, 2) * z
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z
                - 6 * pow(ln(x), 2) * pow(NC, -1) * z * pow(opx, -1)
                + 3 * pow(ln(x), 2) * pow(NC, -1) * z
                + pow(ln(x), 2) * pow(NC, -1) * x
            )
            tmp += (
                -3 * pow(ln(x), 2) * pow(NC, -1) * x * z * pow(opx, -1)
                - pow(ln(x), 2) * pow(NC, -1) * x * z
                + pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z
                - 3 * pow(ln(x), 2) * NC * pow(x, -1) * pow(opx, -1)
                + 3 * pow(ln(x), 2) * NC * pow(x, -1)
                + 3 * pow(ln(x), 2) * NC * pow(x, -1) * z * pow(opx, -1)
                - 3 * pow(ln(x), 2) * NC * pow(x, -1) * z
                - 6 * pow(ln(x), 2) * NC * pow(opx, -1)
                + 3 * pow(ln(x), 2) * NC
                + 6 * pow(ln(x), 2) * NC * z * pow(opx, -1)
                - 3 * pow(ln(x), 2) * NC * z
                - 3 * pow(ln(x), 2) * NC * x * pow(opx, -1)
                - pow(ln(x), 2) * NC * x
                + 3 * pow(ln(x), 2) * NC * x * z * pow(opx, -1)
                + pow(ln(x), 2) * NC * x * z
                - pow(ln(x), 2) * NC * pow(x, 2)
                + pow(ln(x), 2) * NC * pow(x, 2) * z
                + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                - 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z
                + 4 * ln(x) * ln(z) * pow(NC, -1) * z * pow(opx, -1)
                - 2 * ln(x) * ln(z) * pow(NC, -1) * z
                + 2 * ln(x) * ln(z) * pow(NC, -1) * x
                + 2 * ln(x) * ln(z) * pow(NC, -1) * x * z * pow(opx, -1)
                + 4 * ln(x) * ln(z) * pow(NC, -1) * x * z
                - 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * z
                + 2 * ln(x) * ln(z) * NC * pow(x, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(z) * NC * pow(x, -1)
                - 2 * ln(x) * ln(z) * NC * pow(x, -1) * z * pow(opx, -1)
                + 2 * ln(x) * ln(z) * NC * pow(x, -1) * z
                + 4 * ln(x) * ln(z) * NC * pow(opx, -1)
                - 2 * ln(x) * ln(z) * NC
                - 4 * ln(x) * ln(z) * NC * z * pow(opx, -1)
                + 2 * ln(x) * ln(z) * NC * z
                + 2 * ln(x) * ln(z) * NC * x * pow(opx, -1)
                - 8 * ln(x) * ln(z) * NC * x
                - 2 * ln(x) * ln(z) * NC * x * z * pow(opx, -1)
                - 4 * ln(x) * ln(z) * NC * x * z
                + 2 * ln(x) * ln(z) * NC * pow(x, 2)
                + 2 * ln(x) * ln(z) * NC * pow(x, 2) * z
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z
            )
            tmp += (
                -8 * ln(x) * ln(omx) * pow(NC, -1) * z * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * z
                - 2 * ln(x) * ln(omx) * pow(NC, -1) * x
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * x * z * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(NC, -1) * x * z
                + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * z
                - 4 * ln(x) * ln(omx) * NC * pow(x, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * NC * pow(x, -1)
                + 4 * ln(x) * ln(omx) * NC * pow(x, -1) * z * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * NC * pow(x, -1) * z
                - 8 * ln(x) * ln(omx) * NC * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * NC
                + 8 * ln(x) * ln(omx) * NC * z * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * NC * z
                - 4 * ln(x) * ln(omx) * NC * x * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * NC * x
                + 4 * ln(x) * ln(omx) * NC * x * z * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * NC * x * z
                - 2 * ln(x) * ln(omx) * NC * pow(x, 2)
                + 2 * ln(x) * ln(omx) * NC * pow(x, 2) * z
                - 2 * ln(x) * ln(omz) * pow(NC, -1) * x
                + 2 * ln(x) * ln(omz) * pow(NC, -1) * x * z
                + 2 * ln(x) * ln(omz) * NC * x
                - 2 * ln(x) * ln(omz) * NC * x * z
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z
                + 8 * ln(x) * ln(opx) * pow(NC, -1) * z * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * pow(NC, -1) * z
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * x * z * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * x * z
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, 2) * z
                + 4 * ln(x) * ln(opx) * NC * pow(x, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * NC * pow(x, -1)
                - 4 * ln(x) * ln(opx) * NC * pow(x, -1) * z * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * NC * pow(x, -1) * z
                + 8 * ln(x) * ln(opx) * NC * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * NC
                - 8 * ln(x) * ln(opx) * NC * z * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * NC * z
                + 4 * ln(x) * ln(opx) * NC * x * pow(opx, -1)
            )
            tmp += (
                +4 * ln(x) * ln(opx) * NC * x
                - 4 * ln(x) * ln(opx) * NC * x * z * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * NC * x * z
                + 4 * ln(x) * ln(opx) * NC * pow(x, 2)
                - 4 * ln(x) * ln(opx) * NC * pow(x, 2) * z
                + 1.0 / 2.0 * ln(z) * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * pow(NC, -1) * z
                - 8 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                - 9.0 / 2.0 * ln(z) * pow(NC, -1) * x
                - 8 * ln(z) * pow(NC, -1) * x * rln2
                - 1.0 / 2.0 * ln(z) * pow(NC, -1) * x * z
                + 8 * ln(z) * pow(NC, -1) * x * z * rln2
                + 8 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * pow(NC, -1) * pow(x, 2)
                + 8 * ln(z) * pow(NC, -1) * pow(x, 2) * rln2
                - 8 * ln(z) * pow(NC, -1) * pow(x, 2) * z * rln2
                + 3.0 / 16.0 * ln(z) * NC * pow(x, -1) * pow(z, -1)
                + 3.0 / 16.0 * ln(z) * NC * pow(x, -1)
                - 3.0 / 16.0 * ln(z) * NC * pow(z, -2)
                - 1.0 / 8.0 * ln(z) * NC * pow(z, -1)
                - 17.0 / 8.0 * ln(z) * NC
                - 3.0 / 16.0 * ln(z) * NC * z
                + 3.0 / 16.0 * ln(z) * NC * x * pow(z, -2)
                + 49.0 / 8.0 * ln(z) * NC * x * pow(z, -1)
                - 4 * ln(z) * NC * x * pow(z, -1) * sqrtxz1
                + 1.0 / 8.0 * ln(z) * NC * x
                - 4 * ln(z) * NC * x * rln2
                + 3.0 / 16.0 * ln(z) * NC * x * z
                - 8 * ln(z) * NC * x * z * rln2
                - 99.0 / 16.0 * ln(z) * NC * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1
                + 29.0 / 16.0 * ln(z) * NC * pow(x, 2)
                + 4 * ln(z) * NC * pow(x, 2) * rln2
                + 8 * ln(z) * NC * pow(x, 2) * z * rln2
                + 4 * ln(z) * LMUA * pow(NC, -1) * x
                - 4 * ln(z) * LMUA * pow(NC, -1) * pow(x, 2)
                - 4 * ln(z) * LMUA * NC * x
                + 4 * ln(z) * LMUA * NC * pow(x, 2)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * z
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x
            )
            tmp += (
                -4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * z
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * z
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC
                - 4 * ln(z) * ln(1 + x * pow(z, -1)) * NC * z * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * z
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * z * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * z
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * z
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z
            )
            tmp += (
                -4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * z * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * z
                - 2 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * NC * pow(x, -1)
                + 2 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * z * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * z
                - 4 * ln(z) * ln(1 + x * z) * NC * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * NC
                + 4 * ln(z) * ln(1 + x * z) * NC * z * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * NC * z
                - 2 * ln(z) * ln(1 + x * z) * NC * x * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * z) * NC * x
                + 2 * ln(z) * ln(1 + x * z) * NC * x * z * pow(opx, -1)
                + 4 * ln(z) * ln(1 + x * z) * NC * pow(x, 2) * z
                + 2 * ln(z) * ln(z + x) * pow(NC, -1) * x * z
                - 2 * ln(z) * ln(z + x) * pow(NC, -1) * pow(x, 2) * z
                - 2 * ln(z) * ln(z + x) * NC * x
                - 2 * ln(z) * ln(z + x) * NC * x * z
                + 2 * ln(z) * ln(z + x) * NC * pow(x, 2)
                + 2 * ln(z) * ln(z + x) * NC * pow(x, 2) * z
                + pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                - pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z
                + 2 * pow(ln(z), 2) * pow(NC, -1) * z * pow(opx, -1)
                - pow(ln(z), 2) * pow(NC, -1) * z
                - 4 * pow(ln(z), 2) * pow(NC, -1) * x
                + pow(ln(z), 2) * pow(NC, -1) * x * z * pow(opx, -1)
                + 4 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * z
                + pow(ln(z), 2) * NC * pow(x, -1) * pow(opx, -1)
                - pow(ln(z), 2) * NC * pow(x, -1)
                - pow(ln(z), 2) * NC * pow(x, -1) * z * pow(opx, -1)
                + pow(ln(z), 2) * NC * pow(x, -1) * z
                + 2 * pow(ln(z), 2) * NC * pow(opx, -1)
                - pow(ln(z), 2) * NC
                - 2 * pow(ln(z), 2) * NC * z * pow(opx, -1)
                + pow(ln(z), 2) * NC * z
                + pow(ln(z), 2) * NC * x * pow(opx, -1)
            )
            tmp += (
                +4 * pow(ln(z), 2) * NC * x
                - pow(ln(z), 2) * NC * x * z * pow(opx, -1)
                - 2 * pow(ln(z), 2) * NC * pow(x, 2)
                - 2 * pow(ln(z), 2) * NC * pow(x, 2) * z
                - 4 * ln(z) * ln(omx) * pow(NC, -1) * x
                + 4 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(z) * ln(omx) * NC * x
                - 4 * ln(z) * ln(omx) * NC * pow(x, 2)
                - ln(omx) * pow(NC, -1)
                + ln(omx) * pow(NC, -1) * z
                - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + ln(omx) * pow(NC, -1) * x
                + 3 * ln(omx) * pow(NC, -1) * x * z
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * z
                + ln(omx) * NC
                - ln(omx) * NC * z
                + 4 * ln(omx) * NC * x * pow(z, -1)
                - ln(omx) * NC * x
                - 3 * ln(omx) * NC * x * z
                - 4 * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                + 4 * ln(omx) * NC * pow(x, 2) * z
                - ln(omz) * pow(NC, -1)
                + ln(omz) * pow(NC, -1) * z
                - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + ln(omz) * pow(NC, -1) * x
                + 3 * ln(omz) * pow(NC, -1) * x * z
                + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                + ln(omz) * NC
                - ln(omz) * NC * z
                + 4 * ln(omz) * NC * x * pow(z, -1)
                - ln(omz) * NC * x
                - 3 * ln(omz) * NC * x * z
                - 4 * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 4 * ln(omz) * NC * pow(x, 2) * z
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(x, 2)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(x, 2)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * z
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2)
            )
            tmp += (
                +4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * z
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * pow(x, 2) * z
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * z
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * z
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * pow(x, 2) * z
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z
                - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1)
                - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z
                - 2 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * NC * pow(x, -1)
                + 2 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * z
                - 4 * Li2(-x * pow(z, -1)) * NC * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * NC
                + 4 * Li2(-x * pow(z, -1)) * NC * z * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * NC * z
                - 2 * Li2(-x * pow(z, -1)) * NC * x * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * NC * x * z * pow(opx, -1)
                + 4 * Li2(-x * pow(z, -1)) * NC * x * z
                - 4 * Li2(-x * pow(z, -1)) * NC * pow(x, 2)
                + 4 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                - 4 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z
                + 8 * Li2(-x) * pow(NC, -1) * z * pow(opx, -1)
            )
            tmp += (
                -4 * Li2(-x) * pow(NC, -1) * z
                + 4 * Li2(-x) * pow(NC, -1) * x * z * pow(opx, -1)
                + 4 * Li2(-x) * pow(NC, -1) * x * z
                + 4 * Li2(-x) * pow(NC, -1) * pow(x, 2) * z
                + 4 * Li2(-x) * NC * pow(x, -1) * pow(opx, -1)
                - 4 * Li2(-x) * NC * pow(x, -1)
                - 4 * Li2(-x) * NC * pow(x, -1) * z * pow(opx, -1)
                + 4 * Li2(-x) * NC * pow(x, -1) * z
                + 8 * Li2(-x) * NC * pow(opx, -1)
                - 4 * Li2(-x) * NC
                - 8 * Li2(-x) * NC * z * pow(opx, -1)
                + 4 * Li2(-x) * NC * z
                + 4 * Li2(-x) * NC * x * pow(opx, -1)
                + 4 * Li2(-x) * NC * x
                - 4 * Li2(-x) * NC * x * z * pow(opx, -1)
                - 4 * Li2(-x) * NC * x * z
                + 4 * Li2(-x) * NC * pow(x, 2)
                - 4 * Li2(-x) * NC * pow(x, 2) * z
                - 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z
                - 4 * Li2(-x * z) * pow(NC, -1) * z * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(NC, -1) * z
                - 2 * Li2(-x * z) * pow(NC, -1) * x * z * pow(opx, -1)
                - 4 * Li2(-x * z) * pow(NC, -1) * pow(x, 2) * z
                - 2 * Li2(-x * z) * NC * pow(x, -1) * pow(opx, -1)
                + 2 * Li2(-x * z) * NC * pow(x, -1)
                + 2 * Li2(-x * z) * NC * pow(x, -1) * z * pow(opx, -1)
                - 2 * Li2(-x * z) * NC * pow(x, -1) * z
                - 4 * Li2(-x * z) * NC * pow(opx, -1)
                + 2 * Li2(-x * z) * NC
                + 4 * Li2(-x * z) * NC * z * pow(opx, -1)
                - 2 * Li2(-x * z) * NC * z
                - 2 * Li2(-x * z) * NC * x * pow(opx, -1)
                - 4 * Li2(-x * z) * NC * x
                + 2 * Li2(-x * z) * NC * x * z * pow(opx, -1)
                + 4 * Li2(-x * z) * NC * pow(x, 2) * z
                - 4 * Li2(x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                + 4 * Li2(x) * pow(NC, -1) * pow(x, -1) * z
                - 8 * Li2(x) * pow(NC, -1) * z * pow(opx, -1)
                + 4 * Li2(x) * pow(NC, -1) * z
                - 4 * Li2(x) * pow(NC, -1) * x * z * pow(opx, -1)
                + 2 * Li2(x) * pow(NC, -1) * pow(x, 2)
                - 2 * Li2(x) * pow(NC, -1) * pow(x, 2) * z
                - 4 * Li2(x) * NC * pow(x, -1) * pow(opx, -1)
            )
            tmp += (
                +4 * Li2(x) * NC * pow(x, -1)
                + 4 * Li2(x) * NC * pow(x, -1) * z * pow(opx, -1)
                - 4 * Li2(x) * NC * pow(x, -1) * z
                - 8 * Li2(x) * NC * pow(opx, -1)
                + 4 * Li2(x) * NC
                + 8 * Li2(x) * NC * z * pow(opx, -1)
                - 4 * Li2(x) * NC * z
                - 4 * Li2(x) * NC * x * pow(opx, -1)
                + 4 * Li2(x) * NC * x * z * pow(opx, -1)
                - 2 * Li2(x) * NC * pow(x, 2)
                + 2 * Li2(x) * NC * pow(x, 2) * z
                + 4 * Li2(z) * pow(NC, -1) * x
                - 4 * Li2(z) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(z) * NC * x
                + 4 * Li2(z) * NC * pow(x, 2)
            )

            res += tmp

        return res


def c2lg2g_eq(x, z, rsl, order, f=C2Lg2gEq_DR0123_scheme):
    if rsl == "ll":
        f_DD = f(x, z, "D", "D", order)
        f_D0 = ln(1 - z) * f(x, z, "D", "0", order)
        f_D1 = 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "D", "1", order)
        f_D2 = 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "D", "2", order)
        f_D3 = 1 / 4 * pow(ln(1 - z), 4) * f(x, z, "D", "3", order)
        f_0D = ln(1 - x) * f(x, z, "0", "D", order)
        f_00 = ln(1 - x) * ln(1 - z) * f(x, z, "0", "0", order)
        f_01 = ln(1 - x) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "0", "1", order)
        f_02 = ln(1 - x) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "0", "2", order)
        f_03 = ln(1 - x) * 1 / 4 * pow(ln(1 - z), 4) * f(x, z, "0", "3", order)
        f_1D = 1 / 2 * pow(ln(1 - x), 2) * f(x, z, "1", "D", order)
        f_10 = 1 / 2 * pow(ln(1 - x), 2) * ln(1 - z) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - x), 2) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - x), 2) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "1", "2", order)
        f_13 = 1 / 2 * pow(ln(1 - x), 2) * 1 / 4 * pow(ln(1 - z), 4) * f(x, z, "1", "3", order)
        f_2D = 1 / 3 * pow(ln(1 - x), 3) * f(x, z, "2", "D", order)
        f_20 = 1 / 3 * pow(ln(1 - x), 3) * ln(1 - z) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - x), 3) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - x), 3) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "2", "2", order)
        f_23 = 1 / 3 * pow(ln(1 - x), 3) * 1 / 4 * pow(ln(1 - z), 4) * f(x, z, "2", "3", order)
        f_3D = 1 / 4 * pow(ln(1 - x), 4) * f(x, z, "3", "D", order)
        f_30 = 1 / 4 * pow(ln(1 - x), 4) * ln(1 - z) * f(x, z, "3", "0", order)
        f_31 = 1 / 4 * pow(ln(1 - x), 4) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "3", "1", order)
        f_32 = 1 / 4 * pow(ln(1 - x), 4) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "3", "2", order)
        f_33 = 1 / 4 * pow(ln(1 - x), 4) * 1 / 4 * pow(ln(1 - z), 4) * f(x, z, "3", "3", order)

        return f_DD + f_D0 + f_D1 + f_D2 + f_D3 + f_0D + f_00 + f_01 + f_02 + f_03 + f_1D + f_10 + f_11 + f_12 + f_13 + f_2D + f_20 + f_21 + f_22 + f_23 + f_3D + f_30 + f_31 + f_32 + f_33

    elif rsl == "lr":
        f_DR = f(x, z, "D", "R", order)
        f_0R = ln(1 - x) * f(x, z, "0", "R", order)
        f_1R = 1 / 2 * pow(ln(1 - x), 2) * f(x, z, "1", "R", order)
        f_2R = 1 / 3 * pow(ln(1 - x), 3) * f(x, z, "2", "R", order)
        f_3R = 1 / 4 * pow(ln(1 - x), 4) * f(x, z, "3", "R", order)

        return f_DR + f_0R + f_1R + f_2R + f_3R

    elif rsl == "rl":
        f_RD = f(x, z, "R", "D", order)
        f_R0 = ln(1 - z) * f(x, z, "R", "0", order)
        f_R1 = 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "R", "1", order)
        f_R2 = 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "R", "2", order)
        f_R3 = 1 / 4 * pow(ln(1 - z), 4) * f(x, z, "R", "3", order)

        return f_RD + f_R0 + f_R1 + f_R2 + f_R3

    elif rsl == "rr":
        f_RR = f(x, z, "R", "R", order)

        return f_RR

    elif rsl == "rs":
        f_R0 = 1 / (1 - z) * f(x, z, "R", "0", order)
        f_R1 = ln(1 - z) / (1 - z) * f(x, z, "R", "1", order)
        f_R2 = pow(ln(1 - z), 2) / (1 - z) * f(x, z, "R", "2", order)
        f_R3 = pow(ln(1 - z), 3) / (1 - z) * f(x, z, "R", "3", order)

        return f_R0 + f_R1 + f_R2 + f_R3

    elif rsl == "sr":
        f_0R = 1 / (1 - x) * f(x, z, "0", "R", order)
        f_1R = ln(1 - x) / (1 - x) * f(x, z, "1", "R", order)
        f_2R = pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "R", order)
        f_3R = pow(ln(1 - x), 3) / (1 - x) * f(x, z, "3", "R", order)

        return f_0R + f_1R + f_2R + f_3R

    elif rsl == "ss":
        f_00 = 1 / ((1 - x) * (1 - z)) * f(x, z, "0", "0", order)
        f_01 = ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "0", "1", order)
        f_02 = pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "0", "2", order)
        f_03 = pow(ln(1 - z), 3) / ((1 - x) * (1 - z)) * f(x, z, "0", "3", order)
        f_10 = ln(1 - x) / ((1 - x) * (1 - z)) * f(x, z, "1", "0", order)
        f_11 = ln(1 - x) * ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "1", "1", order)
        f_12 = ln(1 - x) * pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "1", "2", order)
        f_13 = ln(1 - x) * pow(ln(1 - z), 3) / ((1 - x) * (1 - z)) * f(x, z, "1", "3", order)
        f_20 = pow(ln(1 - x), 2) / ((1 - x) * (1 - z)) * f(x, z, "2", "0", order)
        f_21 = pow(ln(1 - x), 2) * ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "2", "1", order)
        f_22 = pow(ln(1 - x), 2) * pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "2", "2", order)
        f_23 = pow(ln(1 - x), 2) * pow(ln(1 - z), 3) / ((1 - x) * (1 - z)) * f(x, z, "2", "3", order)
        f_30 = pow(ln(1 - x), 3) / ((1 - x) * (1 - z)) * f(x, z, "3", "0", order)
        f_31 = pow(ln(1 - x), 3) * ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "3", "1", order)
        f_32 = pow(ln(1 - x), 3) * pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "3", "2", order)
        f_33 = pow(ln(1 - x), 3) * pow(ln(1 - z), 3) / ((1 - x) * (1 - z)) * f(x, z, "3", "3", order)

        return f_00 + f_01 + f_02 + f_03 + f_10 + f_11 + f_12 + f_13 + f_20 + f_21 + f_22 + f_23 + f_30 + f_31 + f_32 + f_33

    elif rsl == "ls":
        f_D0 = 1 / (1 - z) * f(x, z, "D", "0", order)
        f_D1 = ln(1 - z) / (1 - z) * f(x, z, "D", "1", order)
        f_D2 = pow(ln(1 - z), 2) / (1 - z) * f(x, z, "D", "2", order)
        f_D3 = pow(ln(1 - z), 3) / (1 - z) * f(x, z, "D", "3", order)
        f_00 = ln(1 - x) / (1 - z) * f(x, z, "0", "0", order)
        f_01 = ln(1 - x) * ln(1 - z) / (1 - z) * f(x, z, "0", "1", order)
        f_02 = ln(1 - x) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "0", "2", order)
        f_03 = ln(1 - x) * pow(ln(1 - z), 3) / (1 - z) * f(x, z, "0", "3", order)
        f_10 = 1 / 2 * pow(ln(1 - x), 2) / (1 - z) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - x), 2) * ln(1 - z) / (1 - z) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - x), 2) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "1", "2", order)
        f_13 = 1 / 2 * pow(ln(1 - x), 2) * pow(ln(1 - z), 3) / (1 - z) * f(x, z, "1", "3", order)
        f_20 = 1 / 3 * pow(ln(1 - x), 3) / (1 - z) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - x), 3) * ln(1 - z) / (1 - z) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - x), 3) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "2", "2", order)
        f_23 = 1 / 3 * pow(ln(1 - x), 3) * pow(ln(1 - z), 3) / (1 - z) * f(x, z, "2", "3", order)
        f_30 = 1 / 4 * pow(ln(1 - x), 4) / (1 - z) * f(x, z, "3", "0", order)
        f_31 = 1 / 4 * pow(ln(1 - x), 4) * ln(1 - z) / (1 - z) * f(x, z, "3", "1", order)
        f_32 = 1 / 4 * pow(ln(1 - x), 4) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "3", "2", order)
        f_33 = 1 / 4 * pow(ln(1 - x), 4) * pow(ln(1 - z), 3) / (1 - z) * f(x, z, "3", "3", order)

        return f_D0 + f_D1 + f_D2 + f_D3 + f_00 + f_01 + f_02 + f_03 + f_10 + f_11 + f_12 + f_13 + f_20 + f_21 + f_22 + f_23 + f_30 + f_31 + f_32 + f_33

    elif rsl == "sl":
        f_0D = 1 / (1 - x) * f(x, z, "0", "D", order)
        f_1D = ln(1 - x) / (1 - x) * f(x, z, "1", "D", order)
        f_2D = pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "D", order)
        f_3D = pow(ln(1 - x), 3) / (1 - x) * f(x, z, "3", "D", order)
        f_00 = 1 / (1 - x) * ln(1 - z) * f(x, z, "0", "0", order)
        f_01 = 1 / (1 - x) * pow(ln(1 - z), 2) / 2 * f(x, z, "0", "1", order)
        f_02 = 1 / (1 - x) * pow(ln(1 - z), 3) / 3 * f(x, z, "0", "2", order)
        f_03 = 1 / (1 - x) * pow(ln(1 - z), 4) / 4 * f(x, z, "0", "3", order)
        f_10 = ln(1 - x) / (1 - x) * ln(1 - z) * f(x, z, "1", "0", order)
        f_11 = ln(1 - x) / (1 - x) * pow(ln(1 - z), 2) / 2 * f(x, z, "1", "1", order)
        f_12 = ln(1 - x) / (1 - x) * pow(ln(1 - z), 3) / 3 * f(x, z, "1", "2", order)
        f_13 = ln(1 - x) / (1 - x) * pow(ln(1 - z), 4) / 4 * f(x, z, "1", "3", order)
        f_20 = pow(ln(1 - x), 2) / (1 - x) * ln(1 - z) * f(x, z, "2", "0", order)
        f_21 = pow(ln(1 - x), 2) / (1 - x) * pow(ln(1 - z), 2) / 2 * f(x, z, "2", "1", order)
        f_22 = pow(ln(1 - x), 2) / (1 - x) * pow(ln(1 - z), 3) / 3 * f(x, z, "2", "2", order)
        f_23 = pow(ln(1 - x), 2) / (1 - x) * pow(ln(1 - z), 4) / 4 * f(x, z, "2", "3", order)
        f_30 = pow(ln(1 - x), 3) / (1 - x) * ln(1 - z) * f(x, z, "3", "0", order)
        f_31 = pow(ln(1 - x), 3) / (1 - x) * pow(ln(1 - z), 2) / 2 * f(x, z, "3", "1", order)
        f_32 = pow(ln(1 - x), 3) / (1 - x) * pow(ln(1 - z), 3) / 3 * f(x, z, "3", "2", order)
        f_33 = pow(ln(1 - x), 3) / (1 - x) * pow(ln(1 - z), 4) / 4 * f(x, z, "3", "3", order)

        return f_0D + f_1D + f_2D + f_3D + f_00 + f_01 + f_02 + f_03 + f_10 + f_11 + f_12 + f_13 + f_20 + f_21 + f_22 + f_23 + f_30 + f_31 + f_32 + f_33

    else:
        raise ValueError("Incorrect rsl choice, rsl must have a value of: 'll', 'lr', 'rl', 'rr', 'rs', 'sr', 'ss', 'ls' or 'sl'")
