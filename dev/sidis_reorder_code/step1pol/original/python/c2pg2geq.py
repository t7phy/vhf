from configs.eh import *


def C2Pg2gEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
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
                13.0 / 16.0 * pow(z, -1) * pow(NC, -1)
                - 4 * pow(z, -1) * pow(NC, -1) * pow(rln2, 2) * pow(opz, -1)
                + 4 * pow(z, -1) * pow(NC, -1) * pow(rln2, 2)
                - 8 * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                + 8 * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 6 * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(rln2, 2) * pow(opz, -1)
                + 6 * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(rln2, 2)
                - 157.0 / 16.0 * pow(z, -1) * NC
                - 2 * pow(z, -1) * NC * pow(rln2, 2)
                - 2 * pow(z, -1) * NC * sqrtxz1 * rln2
                + 3.0 / 4.0 * pow(z, -1) * LMUF * pow(NC, -1)
                - 3.0 / 4.0 * pow(z, -1) * LMUF * NC
                + 19.0 / 8.0 * pow(z, -1) * LMUA * pow(NC, -1)
                - 19.0 / 8.0 * pow(z, -1) * LMUA * NC
                + 1.0 / 2.0 * pow(z, -1) * LMUA * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * pow(z, -1) * LMUA * LMUF * NC
                - 24 * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 16 * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 18 * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                + 12 * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                + 7.0 / 8.0 * pow(NC, -1)
                - 4 * pow(NC, -1) * pow(rln2, 2)
                + 65.0 / 8.0 * NC
                + 2 * NC * pow(rln2, 2)
                - 1.0 / 2.0 * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * LMUF * NC
                - 9.0 / 4.0 * LMUA * pow(NC, -1)
                + 9.0 / 4.0 * LMUA * NC
                - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * LMUA * LMUF * NC
                + 8 * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 8 * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 6 * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                - 6 * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                - 43.0 / 16.0 * z * pow(NC, -1)
                + 2 * z * pow(NC, -1) * pow(rln2, 2)
                + 43.0 / 16.0 * z * NC
                - 2 * z * NC * pow(rln2, 2)
                - 3.0 / 4.0 * z * LMUF * pow(NC, -1)
                + 3.0 / 4.0 * z * LMUF * NC
                + 3.0 / 8.0 * z * LMUA * pow(NC, -1)
                - 3.0 / 8.0 * z * LMUA * NC
                + 1.0 / 4.0 * z * LMUA * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * z * LMUA * LMUF * NC
            )
            tmp += (
                +3.0 / 4.0 * x * pow(z, -1) * pow(NC, -1)
                + 8 * x * pow(z, -1) * pow(NC, -1) * pow(rln2, 2) * pow(opz, -1)
                - 8 * x * pow(z, -1) * pow(NC, -1) * pow(rln2, 2)
                + 16 * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                - 16 * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                + 12 * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(rln2, 2) * pow(opz, -1)
                - 12 * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(rln2, 2)
                + 41.0 / 4.0 * x * pow(z, -1) * NC
                + 4 * x * pow(z, -1) * NC * pow(rln2, 2)
                + 4 * x * pow(z, -1) * NC * sqrtxz1 * rln2
                - 3.0 / 4.0 * x * pow(z, -1) * LMUF * pow(NC, -1)
                + 3.0 / 4.0 * x * pow(z, -1) * LMUF * NC
                - 15.0 / 4.0 * x * pow(z, -1) * LMUA * pow(NC, -1)
                + 15.0 / 4.0 * x * pow(z, -1) * LMUA * NC
                - x * pow(z, -1) * LMUA * LMUF * pow(NC, -1)
                + x * pow(z, -1) * LMUA * LMUF * NC
                + 80 * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 64 * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 60 * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                - 48 * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                - 5.0 / 2.0 * x * pow(NC, -1)
                + 8 * x * pow(NC, -1) * pow(rln2, 2)
                - 17.0 / 2.0 * x * NC
                - 4 * x * NC * pow(rln2, 2)
                + 1.0 / 2.0 * x * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * x * LMUF * NC
                + 7.0 / 2.0 * x * LMUA * pow(NC, -1)
                - 7.0 / 2.0 * x * LMUA * NC
                + x * LMUA * LMUF * pow(NC, -1)
                - x * LMUA * LMUF * NC
                - 16 * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 16 * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 12 * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                + 12 * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                + 11.0 / 4.0 * x * z * pow(NC, -1)
                - 4 * x * z * pow(NC, -1) * pow(rln2, 2)
                - 11.0 / 4.0 * x * z * NC
                + 4 * x * z * NC * pow(rln2, 2)
                + x * z * LMUF * pow(NC, -1)
                - x * z * LMUF * NC
                - 1.0 / 4.0 * x * z * LMUA * pow(NC, -1)
            )
            tmp += (
                +1.0 / 4.0 * x * z * LMUA * NC
                - 1.0 / 2.0 * x * z * LMUA * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * x * z * LMUA * LMUF * NC
                - 4 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(rln2, 2) * pow(opz, -1)
                + 4 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(rln2, 2)
                - 8 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                + 8 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 6 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(rln2, 2) * pow(opz, -1)
                + 6 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(rln2, 2)
                - 88 * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 80 * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 66 * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                + 60 * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                - 4 * pow(x, 2) * pow(NC, -1) * pow(rln2, 2)
                + 4 * pow(x, 2) * NC * pow(rln2, 2)
                + 8 * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 8 * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 6 * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                - 6 * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                + 32 * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 32 * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 24 * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                - 24 * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                -1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * NC
                + 1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * z * pow(NC, -1)
                - 1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * z * NC * pow(opx, -1)
                + 1.0 / 6.0 * pow(pi, 2) * pow(x, -2) * z * NC
                - pow(pi, 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + pow(pi, 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * NC
                + 1.0 / 2.0 * pow(pi, 2) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(NC, -1)
                + 1.0 / 2.0 * pow(pi, 2) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * pow(NC, -1)
                - 1.0 / 2.0 * pow(pi, 2) * pow(x, -1) * z * NC * pow(opx, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * NC
                - pow(pi, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + pow(pi, 2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 7.0 / 24.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * NC * pow(opx, -1)
                + 7.0 / 24.0 * pow(pi, 2) * pow(z, -1) * NC
                - pow(pi, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2.0 / 3.0 * pow(pi, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +2.0 / 3.0 * pow(pi, 2) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 12.0 * pow(pi, 2) * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * NC * pow(opx, -1)
                + 1.0 / 12.0 * pow(pi, 2) * NC
                + 1.0 / 3.0 * pow(pi, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 3.0 * pow(pi, 2) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 6.0 * pow(pi, 2) * z * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * z * NC * pow(opx, -1)
                + 1.0 / 6.0 * pow(pi, 2) * z * NC
                - 1.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 5.0 / 4.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1)
                + 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 7.0 / 12.0 * pow(pi, 2) * x * pow(z, -1) * NC
                + 10.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * pow(pi, 2) * x * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * NC * pow(opx, -1)
                + 1.0 / 2.0 * pow(pi, 2) * x * NC
                - 2.0 / 3.0 * pow(pi, 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2.0 / 3.0 * pow(pi, 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 2.0 * pow(pi, 2) * x * z * pow(NC, -1)
                - 1.0 / 2.0 * pow(pi, 2) * x * z * NC
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
            )
            tmp += (
                -11.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 10.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * NC
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4.0 / 3.0 * pow(pi, 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4.0 / 3.0 * pow(pi, 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                - 5 * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * rln2
                + 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                - 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                + 3 * ln(1 + sqrtxz1 - z) * pow(z, -1) * NC * rln2
                + 2 * ln(1 + sqrtxz1 - z) * pow(z, -1) * NC * sqrtxz1
                + 24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * rln2
                - 4 * ln(1 + sqrtxz1 - z) * NC * rln2
                - 8 * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                -8 * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 8 * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 3 * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * rln2
                + 3 * ln(1 + sqrtxz1 - z) * z * NC * rln2
                - 8 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                + 10 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * rln2
                - 16 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 16 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 16 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                + 16 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 6 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * NC * rln2
                - 4 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * NC * sqrtxz1
                - 80 * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 64 * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 80 * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 64 * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 12 * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * rln2
                + 8 * ln(1 + sqrtxz1 - z) * x * NC * rln2
                + 16 * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 16 * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 16 * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 6 * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * rln2
                - 6 * ln(1 + sqrtxz1 - z) * x * z * NC * rln2
                + 4 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
            )
            tmp += (
                -4 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2
                + 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                - 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                + 88 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 80 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 88 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 80 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 6 * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * rln2
                - 6 * ln(1 + sqrtxz1 - z) * pow(x, 2) * NC * rln2
                - 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 8 * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 32 * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 32 * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 32 * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 32 * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
            )
            tmp += (
                +2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * NC
                - 6 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + pow(ln(1 + sqrtxz1 - z), 2) * z * pow(NC, -1)
                - pow(ln(1 + sqrtxz1 - z), 2) * z * NC
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, -1) * pow(NC, -1)
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, -1) * NC
                + 20 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(NC, -1)
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * NC
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * pow(NC, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * NC
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 22 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
            )
            tmp += (
                +20 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * pow(NC, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * NC
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 3 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * NC
                - 12 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1)
                - ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * NC
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
            )
            tmp += (
                -6 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1)
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * NC
                + 40 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 32 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1)
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1)
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * NC
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 44 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 40 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1)
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * NC
            )
            tmp += (
                +4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                - 3 * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * rln2
                + 4 * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                - 4 * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                + ln(1 + sqrtxz1 + z) * pow(z, -1) * NC * rln2
                + 12 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * rln2
                - 4 * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 4 * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * rln2
                + ln(1 + sqrtxz1 + z) * z * NC * rln2
                - 8 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                + 6 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * rln2
                - 8 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                + 8 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 2 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * NC * rln2
                - 40 * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 32 * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
            )
            tmp += (
                -4 * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * rln2
                + 8 * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 8 * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 2 * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * rln2
                - 2 * ln(1 + sqrtxz1 + z) * x * z * NC * rln2
                + 4 * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                - 4 * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2
                + 4 * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                - 4 * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                + 44 * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 40 * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 2 * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * rln2
                - 2 * ln(1 + sqrtxz1 + z) * pow(x, 2) * NC * rln2
                - 4 * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 4 * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 16 * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 16 * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 3.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                +1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 5 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 11.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 5 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(x, -1) * NC * sqrtxz3
            )
            tmp += (
                +5 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(z, -1) * NC * sqrtxz3
                - 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * pow(NC, -1) * sqrtxz3
                + 9 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * NC * sqrtxz3
                + 5 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * x * NC * sqrtxz3
                - 4 * ln(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 4 * ln(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                + 2 * ln(x) * pow(x, -2) * pow(z, -1) * NC
                + 2 * ln(x) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * pow(x, -2) * pow(NC, -1)
                + 2 * ln(x) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * pow(x, -2) * z * pow(NC, -1)
                - 2 * ln(x) * pow(x, -2) * z * NC * pow(opx, -1)
                + 2 * ln(x) * pow(x, -2) * z * NC
                - 12 * ln(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 8 * ln(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 12 * ln(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 8 * ln(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                - 6 * ln(x) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                + 4 * ln(x) * pow(x, -1) * pow(z, -1) * NC
                + 6 * ln(x) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * pow(x, -1) * pow(NC, -1)
                + 6 * ln(x) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * pow(x, -1) * z * pow(NC, -1)
                - 6 * ln(x) * pow(x, -1) * z * NC * pow(opx, -1)
                + 4 * ln(x) * pow(x, -1) * z * NC
                - 12 * ln(x) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 12 * ln(x) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 11.0 / 4.0 * ln(x) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
            )
            tmp += (
                +3 * ln(x) * pow(z, -1) * pow(NC, -1) * rln2
                - 4 * ln(x) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(x) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 4 * ln(x) * pow(z, -1) * NC * pow(opx, -1)
                - 15.0 / 4.0 * ln(x) * pow(z, -1) * NC
                - 2 * ln(x) * pow(z, -1) * NC * rln2
                - ln(x) * pow(z, -1) * NC * sqrtxz1
                + 1.0 / 4.0 * ln(x) * pow(z, -1) * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(x) * pow(z, -1) * LMUF * NC
                + 1.0 / 2.0 * ln(x) * pow(z, -1) * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * pow(z, -1) * LMUA * NC
                - 12 * ln(x) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(x) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(x) * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(x) * pow(NC, -1) * pow(opx, -1)
                - 11.0 / 2.0 * ln(x) * pow(NC, -1)
                - 4 * ln(x) * pow(NC, -1) * rln2
                - 4 * ln(x) * NC * pow(opx, -1)
                + 13.0 / 2.0 * ln(x) * NC
                + 3 * ln(x) * NC * rln2
                - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * LMUA * NC
                + 4 * ln(x) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(x) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(x) * z * pow(NC, -1) * pow(opx, -1)
                - 7.0 / 4.0 * ln(x) * z * pow(NC, -1)
                + 2 * ln(x) * z * pow(NC, -1) * rln2
                - 4 * ln(x) * z * NC * pow(opx, -1)
                + 7.0 / 4.0 * ln(x) * z * NC
                - 2 * ln(x) * z * NC * rln2
                - 1.0 / 4.0 * ln(x) * z * LMUF * pow(NC, -1)
                + 1.0 / 4.0 * ln(x) * z * LMUF * NC
                + 1.0 / 4.0 * ln(x) * z * LMUA * pow(NC, -1)
                - 1.0 / 4.0 * ln(x) * z * LMUA * NC
                - 4 * ln(x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 8 * ln(x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * x * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                - 6 * ln(x) * x * pow(z, -1) * pow(NC, -1) * rln2
                + 8 * ln(x) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
            )
            tmp += (
                -8 * ln(x) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 1.0 / 2.0 * ln(x) * x * pow(z, -1) * NC
                + 4 * ln(x) * x * pow(z, -1) * NC * rln2
                + 2 * ln(x) * x * pow(z, -1) * NC * sqrtxz1
                - 1.0 / 2.0 * ln(x) * x * pow(z, -1) * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * x * pow(z, -1) * LMUF * NC
                - ln(x) * x * pow(z, -1) * LMUA * pow(NC, -1)
                + ln(x) * x * pow(z, -1) * LMUA * NC
                + 40 * ln(x) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 32 * ln(x) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * ln(x) * x * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * x * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * x * pow(NC, -1)
                + 8 * ln(x) * x * pow(NC, -1) * rln2
                - 4 * ln(x) * x * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * x * NC
                - 6 * ln(x) * x * NC * rln2
                + ln(x) * x * LMUA * pow(NC, -1)
                - ln(x) * x * LMUA * NC
                - 8 * ln(x) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(x) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(x) * x * z * pow(NC, -1) * rln2
                + 4 * ln(x) * x * z * NC * rln2
                - 1.0 / 2.0 * ln(x) * x * z * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * x * z * LMUF * NC
                - 1.0 / 2.0 * ln(x) * x * z * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * x * z * LMUA * NC
                - 4 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                + 2 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2
                - 4 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 44 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 40 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(x) * pow(x, 2) * pow(NC, -1) * rln2
                + 4 * ln(x) * pow(x, 2) * NC * rln2
            )
            tmp += (
                +4 * ln(x) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(x) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 16 * ln(x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * NC
                - 6 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(x) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1)
                + ln(x) * ln(1 + sqrtxz1 - z) * z * NC
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * NC
                + 20 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * NC
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                +2 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * NC
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 22 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 20 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * NC
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * NC
                + 6 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1)
                - ln(x) * ln(1 + sqrtxz1 + z) * NC
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                -ln(x) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1)
                + ln(x) * ln(1 + sqrtxz1 + z) * z * NC
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * NC
                - 20 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 16 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * NC
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * NC
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 22 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 20 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * NC
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
            )
            tmp += (
                +2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * NC
                + 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NC
            )
            tmp += (
                -3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * pow(NC, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * NC * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * NC
                + 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * NC
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * NC
                - ln(x) * ln(1 + x * pow(z, -1)) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * z * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * z * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * z * NC
                + ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * NC
                - ln(x) * ln(1 + x * pow(z, -1)) * x * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * x * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * x * NC * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * x * z * pow(NC, -1)
            )
            tmp += (
                +ln(x) * ln(1 + x * pow(z, -1)) * x * z * NC
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, 2) * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, 2) * NC
                + ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * NC
                + 3 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                - ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * NC
                - 3.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * pow(x, -1) * pow(NC, -1)
            )
            tmp += (
                -3.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * pow(x, -1) * z * pow(NC, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * NC * pow(opx, -1)
                - ln(x) * ln(1 + x * z) * pow(x, -1) * z * NC
                + 3 * ln(x) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 3 * ln(x) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + ln(x) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1)
                + ln(x) * ln(1 + x * z) * pow(z, -1) * NC * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * NC * pow(opx, -1)
                - ln(x) * ln(1 + x * z) * NC
                - ln(x) * ln(1 + x * z) * z * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * z * NC * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 4 * ln(x) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1)
                + 2 * ln(x) * ln(1 + x * z) * x * pow(z, -1) * NC
                - ln(x) * ln(1 + x * z) * x * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * x * NC * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * x * z * pow(NC, -1)
                + 2 * ln(x) * ln(1 + x * z) * x * z * NC
                + ln(x) * ln(1 + x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(1 + x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(x, 2) * pow(NC, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(x, 2) * NC
                + ln(x) * ln(z + x) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - ln(x) * ln(z + x) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                +1.0 / 2.0 * ln(x) * ln(z + x) * pow(z, -1) * NC
                + 1.0 / 2.0 * ln(x) * ln(z + x) * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(z + x) * z * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(z + x) * z * NC
                - 2 * ln(x) * ln(z + x) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 2 * ln(x) * ln(z + x) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(z + x) * x * pow(z, -1) * NC
                - ln(x) * ln(z + x) * x * pow(NC, -1)
                + ln(x) * ln(z + x) * x * z * pow(NC, -1)
                - ln(x) * ln(z + x) * x * z * NC
                + ln(x) * ln(z + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - ln(x) * ln(z + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + ln(x) * ln(z + x) * pow(x, 2) * pow(NC, -1)
                - ln(x) * ln(z + x) * pow(x, 2) * NC
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * NC
                - 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * pow(NC, -1)
                - 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * z * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * z * NC * pow(opx, -1)
                - 3.0 / 4.0 * pow(ln(x), 2) * pow(x, -2) * z * NC
                + 9.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 3 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 3 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                +9.0 / 4.0 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * NC
                - 9.0 / 4.0 * pow(ln(x), 2) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * pow(NC, -1)
                - 9.0 / 4.0 * pow(ln(x), 2) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * z * pow(NC, -1)
                + 9.0 / 4.0 * pow(ln(x), 2) * pow(x, -1) * z * NC * pow(opx, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * z * NC
                + 9.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 9.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * NC
                + 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(opx, -1)
                + pow(ln(x), 2) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(opx, -1)
                - pow(ln(x), 2) * NC
                - 3.0 / 2.0 * pow(ln(x), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * z * pow(NC, -1) * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * z * NC * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 3 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 4 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                -3 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 3 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + pow(ln(x), 2) * x * pow(z, -1) * NC
                - 15 * pow(ln(x), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 12 * pow(ln(x), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 3 * pow(ln(x), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * x * pow(NC, -1) * pow(opx, -1)
                + pow(ln(x), 2) * x * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * x * NC * pow(opx, -1)
                - pow(ln(x), 2) * x * NC
                + 3 * pow(ln(x), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 3 * pow(ln(x), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - pow(ln(x), 2) * x * z * pow(NC, -1)
                + pow(ln(x), 2) * x * z * NC
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 33.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 15 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * NC
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 6 * pow(ln(x), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 6 * pow(ln(x), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
            )
            tmp += (
                +ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * NC
                + 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * z * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * z * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(z) * pow(x, -2) * z * NC
                - 3 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                + ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * NC
                + 3.0 / 2.0 * ln(x) * ln(z) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(z) * pow(x, -1) * pow(NC, -1)
                + 3.0 / 2.0 * ln(x) * ln(z) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(z) * pow(x, -1) * z * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * ln(z) * pow(x, -1) * z * NC * pow(opx, -1)
                + ln(x) * ln(z) * pow(x, -1) * z * NC
                - 3 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 3 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 5.0 / 4.0 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1)
                + ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
            )
            tmp += (
                -ln(x) * ln(z) * pow(z, -1) * NC * pow(opx, -1)
                - 7.0 / 4.0 * ln(x) * ln(z) * pow(z, -1) * NC
                + 3 * ln(x) * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(z) * pow(NC, -1)
                - ln(x) * ln(z) * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(z) * NC
                - ln(x) * ln(z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + ln(x) * ln(z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + ln(x) * ln(z) * z * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(z) * z * pow(NC, -1)
                - ln(x) * ln(z) * z * NC * pow(opx, -1)
                - ln(x) * ln(z) * z * NC
                - ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 1.0 / 2.0 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 1.0 / 2.0 * ln(x) * ln(z) * x * pow(z, -1) * NC
                - 10 * ln(x) * ln(z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(x) * ln(z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                + ln(x) * ln(z) * x * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(z) * x * pow(NC, -1)
                - ln(x) * ln(z) * x * NC * pow(opx, -1)
                - 3 * ln(x) * ln(z) * x * NC
                + 2 * ln(x) * ln(z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(x) * ln(z) * x * z * pow(NC, -1)
                + ln(x) * ln(z) * x * z * NC
                - ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 2 * ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 11 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 10 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(z) * pow(x, 2) * pow(NC, -1)
                + ln(x) * ln(z) * pow(x, 2) * NC
                - ln(x) * ln(z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + ln(x) * ln(z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(x) * ln(z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(x) * ln(z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * NC
                - ln(x) * ln(omx) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(omx) * pow(x, -2) * pow(NC, -1)
                - ln(x) * ln(omx) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(omx) * pow(x, -2) * z * pow(NC, -1)
                + ln(x) * ln(omx) * pow(x, -2) * z * NC * pow(opx, -1)
                - ln(x) * ln(omx) * pow(x, -2) * z * NC
                + 6 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -6 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * NC
                - 3 * ln(x) * ln(omx) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -1) * pow(NC, -1)
                - 3 * ln(x) * ln(omx) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -1) * z * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * pow(x, -1) * z * NC * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * pow(x, -1) * z * NC
                + 6 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 6 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(x) * ln(omx) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(x) * ln(omx) * pow(z, -1) * NC
                - 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(NC, -1)
                + 2 * ln(x) * ln(omx) * NC * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * NC
                - 2 * ln(x) * ln(omx) * z * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * z * NC * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 3 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(omx) * x * pow(z, -1) * NC
                - 4 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * x * NC * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                -2 * ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1)
                + ln(x) * ln(omx) * pow(x, 2) * NC
                - 3.0 / 4.0 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 3.0 / 4.0 * ln(x) * ln(omz) * pow(z, -1) * NC
                - 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(x) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(omz) * NC
                + 2 * ln(x) * ln(omz) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * ln(x) * ln(omz) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 3.0 / 2.0 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 3.0 / 2.0 * ln(x) * ln(omz) * x * pow(z, -1) * NC
                + 20 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(x) * ln(omz) * x * pow(NC, -1)
                + ln(x) * ln(omz) * x * NC
                - 4 * ln(x) * ln(omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(x) * ln(omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + ln(x) * ln(omz) * x * z * pow(NC, -1)
                - ln(x) * ln(omz) * x * z * NC
                - 2 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 22 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 20 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(x) * ln(omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
            )
            tmp += (
                -2 * ln(x) * ln(omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * ln(x) * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(x) * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                + ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * NC
                + ln(x) * ln(opx) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(opx) * pow(x, -2) * pow(NC, -1)
                + ln(x) * ln(opx) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(opx) * pow(x, -2) * z * pow(NC, -1)
                - ln(x) * ln(opx) * pow(x, -2) * z * NC * pow(opx, -1)
                + ln(x) * ln(opx) * pow(x, -2) * z * NC
                - 6 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 6 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                - 3 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * NC
                + 3 * ln(x) * ln(opx) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(x, -1) * pow(NC, -1)
                + 3 * ln(x) * ln(opx) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(x, -1) * z * pow(NC, -1)
                - 3 * ln(x) * ln(opx) * pow(x, -1) * z * NC * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(x, -1) * z * NC
                - 6 * ln(x) * ln(opx) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
            )
            tmp += (
                +6 * ln(x) * ln(opx) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(z, -1) * NC * pow(opx, -1)
                - ln(x) * ln(opx) * pow(z, -1) * NC
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(opx) * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * NC * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * NC
                + 2 * ln(x) * ln(opx) * z * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(opx) * z * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * z * NC * pow(opx, -1)
                - ln(x) * ln(opx) * z * NC
                - 2 * ln(x) * ln(opx) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(opx) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * x * pow(z, -1) * NC
                + 2 * ln(x) * ln(opx) * x * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * x * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * x * NC * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * x * z * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * x * z * NC
                - 2 * ln(x) * ln(opx) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(opx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(x) * ln(opx) * pow(x, 2) * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * pow(x, 2) * NC
                - 33.0 / 8.0 * ln(z) * pow(z, -1) * pow(NC, -1)
                - 6 * ln(z) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                + 5 * ln(z) * pow(z, -1) * pow(NC, -1) * rln2
                - 4 * ln(z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 8 * ln(z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                + 8 * ln(z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                + 5.0 / 8.0 * ln(z) * pow(z, -1) * NC
                - 2 * ln(z) * pow(z, -1) * NC * rln2
                - ln(z) * pow(z, -1) * NC * sqrtxz1
                - 1.0 / 2.0 * ln(z) * pow(z, -1) * LMUF * pow(NC, -1)
            )
            tmp += (
                +1.0 / 2.0 * ln(z) * pow(z, -1) * LMUF * NC
                + 1.0 / 2.0 * ln(z) * pow(z, -1) * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * pow(z, -1) * LMUA * NC
                - 12 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 24 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 16 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 3.0 / 4.0 * ln(z) * pow(NC, -1)
                - 4 * ln(z) * pow(NC, -1) * rln2
                - 17.0 / 4.0 * ln(z) * NC
                + ln(z) * NC * rln2
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * LMUF * NC
                + 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * LMUA * NC
                + 4 * ln(z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * ln(z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 8 * ln(z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 9.0 / 8.0 * ln(z) * z * pow(NC, -1)
                + 2 * ln(z) * z * pow(NC, -1) * rln2
                + 9.0 / 8.0 * ln(z) * z * NC
                - 2 * ln(z) * z * NC * rln2
                - 1.0 / 4.0 * ln(z) * z * LMUF * pow(NC, -1)
                + 1.0 / 4.0 * ln(z) * z * LMUF * NC
                + 1.0 / 4.0 * ln(z) * z * LMUA * pow(NC, -1)
                - 1.0 / 4.0 * ln(z) * z * LMUA * NC
                + 13.0 / 2.0 * ln(z) * x * pow(z, -1) * pow(NC, -1)
                + 12 * ln(z) * x * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                - 10 * ln(z) * x * pow(z, -1) * pow(NC, -1) * rln2
                + 8 * ln(z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 8 * ln(z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 16 * ln(z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                - 16 * ln(z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 3 * ln(z) * x * pow(z, -1) * NC
                + 4 * ln(z) * x * pow(z, -1) * NC * rln2
                + 2 * ln(z) * x * pow(z, -1) * NC * sqrtxz1
                + ln(z) * x * pow(z, -1) * LMUF * pow(NC, -1)
                - ln(z) * x * pow(z, -1) * LMUF * NC
                - ln(z) * x * pow(z, -1) * LMUA * pow(NC, -1)
            )
            tmp += (
                +ln(z) * x * pow(z, -1) * LMUA * NC
                + 40 * ln(z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 32 * ln(z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 80 * ln(z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 64 * ln(z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 8 * ln(z) * x * pow(NC, -1) * rln2
                + 7.0 / 2.0 * ln(z) * x * NC
                - 2 * ln(z) * x * NC * rln2
                - ln(z) * x * LMUF * pow(NC, -1)
                + ln(z) * x * LMUF * NC
                - ln(z) * x * LMUA * pow(NC, -1)
                + ln(z) * x * LMUA * NC
                - 8 * ln(z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 16 * ln(z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 16 * ln(z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 5.0 / 4.0 * ln(z) * x * z * pow(NC, -1)
                - 4 * ln(z) * x * z * pow(NC, -1) * rln2
                - 5.0 / 4.0 * ln(z) * x * z * NC
                + 4 * ln(z) * x * z * NC * rln2
                + 1.0 / 2.0 * ln(z) * x * z * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * x * z * LMUF * NC
                - 1.0 / 2.0 * ln(z) * x * z * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * x * z * LMUA * NC
                - 6 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2 * pow(opz, -1)
                + 6 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * rln2
                - 4 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 8 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                + 8 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 44 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 40 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 88 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 80 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 4 * ln(z) * pow(x, 2) * pow(NC, -1) * rln2
            )
            tmp += (
                +4 * ln(z) * pow(x, 2) * NC * rln2
                + 4 * ln(z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * ln(z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 8 * ln(z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 16 * ln(z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 32 * ln(z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 32 * ln(z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * NC
                + 12 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1)
                - ln(z) * ln(1 + sqrtxz1 - z) * NC
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(z) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1)
                + ln(z) * ln(1 + sqrtxz1 - z) * z * NC
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 8 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
            )
            tmp += (
                -2 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * NC
                - 40 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 32 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * x * NC
                + 8 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * NC
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 44 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 40 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * NC
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 3 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                +4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * NC
                + 12 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(z) * ln(1 + sqrtxz1 + z) * z * pow(NC, -1)
                + ln(z) * ln(1 + sqrtxz1 + z) * z * NC
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 6 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * NC
                - 40 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 32 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(NC, -1)
                + 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * pow(NC, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * NC
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
            )
            tmp += (
                -4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 44 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 40 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * pow(NC, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * NC
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * NC
                + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * NC * pow(opx, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * NC
                - 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
            )
            tmp += (
                +2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NC
                + 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(NC, -1)
                + 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * pow(NC, -1)
                - 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * NC * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * NC
                - 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * NC
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * NC
                + ln(z) * ln(1 + x * pow(z, -1)) * z * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * z * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * z * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * z * NC
                - ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * NC
                + ln(z) * ln(1 + x * pow(z, -1)) * x * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * x * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * x * NC * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * x * z * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * x * z * NC
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, 2) * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, 2) * NC
                + ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * NC * pow(opx, -1)
                - 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * NC
                + 3 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -3 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                - ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * NC
                - 3.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * pow(x, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * pow(x, -1) * z * pow(NC, -1)
                + 3.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * NC * pow(opx, -1)
                - ln(z) * ln(1 + x * z) * pow(x, -1) * z * NC
                + 3 * ln(z) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 3 * ln(z) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - ln(z) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + ln(z) * ln(1 + x * z) * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(1 + x * z) * pow(z, -1) * NC * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * NC * pow(opx, -1)
                - ln(z) * ln(1 + x * z) * NC
                - ln(z) * ln(1 + x * z) * z * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * z * NC * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(z) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 4 * ln(z) * ln(1 + x * z) * x * pow(z, -1) * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * z) * x * pow(z, -1) * NC
                - ln(z) * ln(1 + x * z) * x * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * x * NC * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * x * z * pow(NC, -1)
            )
            tmp += (
                +2 * ln(z) * ln(1 + x * z) * x * z * NC
                + ln(z) * ln(1 + x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - ln(z) * ln(1 + x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(x, 2) * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(x, 2) * NC
                - ln(z) * ln(z + x) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + ln(z) * ln(z + x) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(z + x) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(z) * ln(z + x) * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * ln(z + x) * z * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(z + x) * z * NC
                + 2 * ln(z) * ln(z + x) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * ln(z) * ln(z + x) * x * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(z + x) * x * pow(z, -1) * NC
                + ln(z) * ln(z + x) * x * pow(NC, -1)
                - ln(z) * ln(z + x) * x * z * pow(NC, -1)
                + ln(z) * ln(z + x) * x * z * NC
                - ln(z) * ln(z + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + ln(z) * ln(z + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - ln(z) * ln(z + x) * pow(x, 2) * pow(NC, -1)
                + ln(z) * ln(z + x) * pow(x, 2) * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * NC
                + 1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * z * pow(NC, -1)
            )
            tmp += (
                -1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * z * NC * pow(opx, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * pow(x, -2) * z * NC
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 4.0 * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * NC
                + 3.0 / 4.0 * pow(ln(z), 2) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(z), 2) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * z * pow(NC, -1)
                - 3.0 / 4.0 * pow(ln(z), 2) * pow(x, -1) * z * NC * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * z * NC
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - pow(ln(z), 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * NC * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * NC
                - 15.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 5 * pow(ln(z), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                + pow(ln(z), 2) * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC
            )
            tmp += (
                +5.0 / 2.0 * pow(ln(z), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * z * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * z * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * z * NC * pow(opx, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * z * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 2 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1)
                + 5 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 5 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 2 * pow(ln(z), 2) * x * pow(z, -1) * NC
                + 25 * pow(ln(z), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 20 * pow(ln(z), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + pow(ln(z), 2) * x * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1) * pow(opx, -1)
                + pow(ln(z), 2) * x * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * x * NC * pow(opx, -1)
                - 5 * pow(ln(z), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 5 * pow(ln(z), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * x * z * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * x * z * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
            )
            tmp += (
                -55.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 25 * pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + pow(ln(z), 2) * pow(x, 2) * pow(NC, -1)
                - pow(ln(z), 2) * pow(x, 2) * NC
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 10 * pow(ln(z), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 10 * pow(ln(z), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(z) * ln(omx) * pow(NC, -1)
                + ln(z) * ln(omx) * NC
                + 2 * ln(z) * ln(omx) * x * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * NC
                - 2 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 6 * ln(z) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(omz) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * ln(z) * ln(omz) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 20 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(z) * ln(omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(z) * ln(omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 22 * ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
            )
            tmp += (
                +20 * ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(z) * ln(omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * ln(z) * ln(omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * ln(z) * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(z) * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(x, -1) * NC * sqrtxz3
                - 5 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(z, -1) * NC * sqrtxz3
                + 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * pow(NC, -1) * sqrtxz3
                - 9 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * NC * sqrtxz3
                - 5 * ln(sqrtxz3) * ArcTan(sqrtxz3) * x * NC * sqrtxz3
                - 25.0 / 8.0 * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 25.0 / 8.0 * ln(omx) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(omx) * pow(z, -1) * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * pow(z, -1) * LMUF * NC
                - 1.0 / 2.0 * ln(omx) * pow(z, -1) * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * pow(z, -1) * LMUA * NC
                + 11.0 / 4.0 * ln(omx) * pow(NC, -1)
                - 11.0 / 4.0 * ln(omx) * NC
                + 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * LMUF * NC
                + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * LMUA * NC
                + 3.0 / 8.0 * ln(omx) * z * pow(NC, -1)
                - 3.0 / 8.0 * ln(omx) * z * NC
                - 1.0 / 4.0 * ln(omx) * z * LMUF * pow(NC, -1)
                + 1.0 / 4.0 * ln(omx) * z * LMUF * NC
                - 1.0 / 4.0 * ln(omx) * z * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * ln(omx) * z * LMUA * NC
                + 9.0 / 2.0 * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 9.0 / 2.0 * ln(omx) * x * pow(z, -1) * NC
                + ln(omx) * x * pow(z, -1) * LMUF * pow(NC, -1)
                - ln(omx) * x * pow(z, -1) * LMUF * NC
                + ln(omx) * x * pow(z, -1) * LMUA * pow(NC, -1)
                - ln(omx) * x * pow(z, -1) * LMUA * NC
                - 4 * ln(omx) * x * pow(NC, -1)
                + 4 * ln(omx) * x * NC
                - ln(omx) * x * LMUF * pow(NC, -1)
            )
            tmp += (
                +ln(omx) * x * LMUF * NC
                - ln(omx) * x * LMUA * pow(NC, -1)
                + ln(omx) * x * LMUA * NC
                - 3.0 / 4.0 * ln(omx) * x * z * pow(NC, -1)
                + 3.0 / 4.0 * ln(omx) * x * z * NC
                + 1.0 / 2.0 * ln(omx) * x * z * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * x * z * LMUF * NC
                + 1.0 / 2.0 * ln(omx) * x * z * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * x * z * LMUA * NC
                + 1.0 / 2.0 * pow(ln(omx), 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * pow(z, -1) * NC
                - 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC
                + 1.0 / 4.0 * pow(ln(omx), 2) * z * pow(NC, -1)
                - 1.0 / 4.0 * pow(ln(omx), 2) * z * NC
                - pow(ln(omx), 2) * x * pow(z, -1) * pow(NC, -1)
                + pow(ln(omx), 2) * x * pow(z, -1) * NC
                + pow(ln(omx), 2) * x * pow(NC, -1)
                - pow(ln(omx), 2) * x * NC
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * z * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * x * z * NC
                + ln(omx) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - ln(omx) * ln(omz) * pow(z, -1) * NC
                - ln(omx) * ln(omz) * pow(NC, -1)
                + ln(omx) * ln(omz) * NC
                + 1.0 / 2.0 * ln(omx) * ln(omz) * z * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * ln(omz) * z * NC
                - 2 * ln(omx) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 2 * ln(omx) * ln(omz) * x * pow(z, -1) * NC
                + 2 * ln(omx) * ln(omz) * x * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * NC
                - ln(omx) * ln(omz) * x * z * pow(NC, -1)
                + ln(omx) * ln(omz) * x * z * NC
                - 25.0 / 8.0 * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 4 * ln(omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                + 4 * ln(omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                + 25.0 / 8.0 * ln(omz) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(omz) * pow(z, -1) * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * pow(z, -1) * LMUF * NC
                - 1.0 / 2.0 * ln(omz) * pow(z, -1) * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * pow(z, -1) * LMUA * NC
                - 12 * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
            )
            tmp += (
                +8 * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 11.0 / 4.0 * ln(omz) * pow(NC, -1)
                - 11.0 / 4.0 * ln(omz) * NC
                + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * LMUF * NC
                + 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * LMUA * NC
                + 4 * ln(omz) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 4 * ln(omz) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 3.0 / 8.0 * ln(omz) * z * pow(NC, -1)
                - 3.0 / 8.0 * ln(omz) * z * NC
                - 1.0 / 4.0 * ln(omz) * z * LMUF * pow(NC, -1)
                + 1.0 / 4.0 * ln(omz) * z * LMUF * NC
                - 1.0 / 4.0 * ln(omz) * z * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * ln(omz) * z * LMUA * NC
                + 9.0 / 2.0 * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 8 * ln(omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                - 8 * ln(omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 9.0 / 2.0 * ln(omz) * x * pow(z, -1) * NC
                + ln(omz) * x * pow(z, -1) * LMUF * pow(NC, -1)
                - ln(omz) * x * pow(z, -1) * LMUF * NC
                + ln(omz) * x * pow(z, -1) * LMUA * pow(NC, -1)
                - ln(omz) * x * pow(z, -1) * LMUA * NC
                + 40 * ln(omz) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 32 * ln(omz) * x * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 4 * ln(omz) * x * pow(NC, -1)
                + 4 * ln(omz) * x * NC
                - ln(omz) * x * LMUF * pow(NC, -1)
                + ln(omz) * x * LMUF * NC
                - ln(omz) * x * LMUA * pow(NC, -1)
                + ln(omz) * x * LMUA * NC
                - 8 * ln(omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 8 * ln(omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                - 3.0 / 4.0 * ln(omz) * x * z * pow(NC, -1)
                + 3.0 / 4.0 * ln(omz) * x * z * NC
                + 1.0 / 2.0 * ln(omz) * x * z * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * x * z * LMUF * NC
                + 1.0 / 2.0 * ln(omz) * x * z * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * x * z * LMUA * NC
                - 4 * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
            )
            tmp += (
                +4 * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * rln2
                - 44 * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                + 40 * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 4 * ln(omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 4 * ln(omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 16 * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                - 16 * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 12 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(omz) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 8 * ln(omz) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 40 * ln(omz) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 32 * ln(omz) * ln(1 + sqrtxz1 - z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * ln(omz) * ln(1 + sqrtxz1 - z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
            )
            tmp += (
                +44 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 40 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 6 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 20 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 16 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                +2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 22 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 20 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * NC
                - 6 * pow(ln(omz), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * pow(ln(omz), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * NC
                + 2 * pow(ln(omz), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * pow(ln(omz), 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 1.0 / 4.0 * pow(ln(omz), 2) * z * pow(NC, -1)
                - 1.0 / 4.0 * pow(ln(omz), 2) * z * NC
                - pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1)
                + 4 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + pow(ln(omz), 2) * x * pow(z, -1) * NC
            )
            tmp += (
                +20 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + pow(ln(omz), 2) * x * pow(NC, -1)
                - pow(ln(omz), 2) * x * NC
                - 4 * pow(ln(omz), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * pow(ln(omz), 2) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * x * z * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * x * z * NC
                - 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 22 * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 20 * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * pow(ln(omz), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * pow(ln(omz), 2) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * pow(ln(omz), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * pow(ln(omz), 2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                -Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * NC
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
            )
            tmp += (
                -22 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                -4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 20 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * NC
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 22 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 20 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                +2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * NC
                + 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * pow(NC, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * NC
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
            )
            tmp += (
                +4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * NC
                - 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * NC
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * NC
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 22 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * NC
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                -8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * NC
                + 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * pow(NC, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * NC
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * NC
                - 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
            )
            tmp += (
                +16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * NC
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * NC
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 22 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * NC
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
            )
            tmp += (
                -4 * Li2(pow(sqrtxz1, -1) * omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 12 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * Li2(pow(sqrtxz1, -1) * omz) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(pow(sqrtxz1, -1) * omz) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * Li2(pow(sqrtxz1, -1) * omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 8 * Li2(pow(sqrtxz1, -1) * omz) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 40 * Li2(pow(sqrtxz1, -1) * omz) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 32 * Li2(pow(sqrtxz1, -1) * omz) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 8 * Li2(pow(sqrtxz1, -1) * omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * Li2(pow(sqrtxz1, -1) * omz) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 44 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 40 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
            )
            tmp += (
                +4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 12 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * Li2(-sqrtxz1 * pow(omz, -1)) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(-sqrtxz1 * pow(omz, -1)) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 8 * Li2(-sqrtxz1 * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 40 * Li2(-sqrtxz1 * pow(omz, -1)) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 32 * Li2(-sqrtxz1 * pow(omz, -1)) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 8 * Li2(-sqrtxz1 * pow(omz, -1)) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 44 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 40 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
            )
            tmp += (
                -Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * NC
                - 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * pow(NC, -1)
                + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * NC * pow(opx, -1)
                - 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * NC
                + 3 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                - Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * NC
                - 3.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -1) * pow(NC, -1)
                - 3.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -1) * z * pow(NC, -1)
                + 3.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * NC * pow(opx, -1)
                - Li2(-x * pow(z, -1)) * pow(x, -1) * z * NC
                + 3 * Li2(-x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
            )
            tmp += (
                -3 * Li2(-x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - Li2(-x * pow(z, -1)) * pow(z, -1) * pow(NC, -1)
                + Li2(-x * pow(z, -1)) * pow(z, -1) * NC * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(z, -1) * NC
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(NC, -1)
                + Li2(-x * pow(z, -1)) * NC * pow(opx, -1)
                - Li2(-x * pow(z, -1)) * NC
                - Li2(-x * pow(z, -1)) * z * pow(NC, -1) * pow(opx, -1)
                - Li2(-x * pow(z, -1)) * z * pow(NC, -1)
                + Li2(-x * pow(z, -1)) * z * NC * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * z * NC
                + Li2(-x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - Li2(-x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - Li2(-x * pow(z, -1)) * x * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * x * pow(NC, -1)
                + Li2(-x * pow(z, -1)) * x * NC * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + Li2(-x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(-x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * Li2(-x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(-x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                - Li2(-x) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                + Li2(-x) * pow(x, -2) * pow(z, -1) * NC
            )
            tmp += (
                +Li2(-x) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                - Li2(-x) * pow(x, -2) * pow(NC, -1)
                + Li2(-x) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                - Li2(-x) * pow(x, -2) * z * pow(NC, -1)
                - Li2(-x) * pow(x, -2) * z * NC * pow(opx, -1)
                + Li2(-x) * pow(x, -2) * z * NC
                - 6 * Li2(-x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 4 * Li2(-x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 6 * Li2(-x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 4 * Li2(-x) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                - 3 * Li2(-x) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                + 2 * Li2(-x) * pow(x, -1) * pow(z, -1) * NC
                + 3 * Li2(-x) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x) * pow(x, -1) * pow(NC, -1)
                + 3 * Li2(-x) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x) * pow(x, -1) * z * pow(NC, -1)
                - 3 * Li2(-x) * pow(x, -1) * z * NC * pow(opx, -1)
                + 2 * Li2(-x) * pow(x, -1) * z * NC
                - 6 * Li2(-x) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 6 * Li2(-x) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x) * pow(z, -1) * NC * pow(opx, -1)
                - Li2(-x) * pow(z, -1) * NC
                + 4 * Li2(-x) * pow(NC, -1) * pow(opx, -1)
                - Li2(-x) * pow(NC, -1)
                - 2 * Li2(-x) * NC * pow(opx, -1)
                + 2 * Li2(-x) * NC
                + 2 * Li2(-x) * z * pow(NC, -1) * pow(opx, -1)
                + Li2(-x) * z * pow(NC, -1)
                - 2 * Li2(-x) * z * NC * pow(opx, -1)
                - Li2(-x) * z * NC
                - 2 * Li2(-x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 4 * Li2(-x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(-x) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 4 * Li2(-x) * x * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(-x) * x * pow(z, -1) * NC
            )
            tmp += (
                +2 * Li2(-x) * x * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x) * x * pow(NC, -1)
                - 2 * Li2(-x) * x * NC * pow(opx, -1)
                + 2 * Li2(-x) * x * z * pow(NC, -1)
                - 2 * Li2(-x) * x * z * NC
                - 2 * Li2(-x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(-x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(-x) * pow(x, 2) * pow(NC, -1)
                - 2 * Li2(-x) * pow(x, 2) * NC
                + Li2(-x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - Li2(-x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - Li2(-x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * z) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * pow(z, -1) * NC
                - 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * z * pow(NC, -1)
                + 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * z * NC * pow(opx, -1)
                - 1.0 / 2.0 * Li2(-x * z) * pow(x, -2) * z * NC
                + 3 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
                - Li2(-x * z) * pow(x, -1) * pow(z, -1) * NC
                - 3.0 / 2.0 * Li2(-x * z) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * z) * pow(x, -1) * pow(NC, -1)
                - 3.0 / 2.0 * Li2(-x * z) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
            )
            tmp += (
                +Li2(-x * z) * pow(x, -1) * z * pow(NC, -1)
                + 3.0 / 2.0 * Li2(-x * z) * pow(x, -1) * z * NC * pow(opx, -1)
                - Li2(-x * z) * pow(x, -1) * z * NC
                + 3 * Li2(-x * z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 3 * Li2(-x * z) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - Li2(-x * z) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                + Li2(-x * z) * pow(z, -1) * pow(NC, -1)
                + Li2(-x * z) * pow(z, -1) * NC * pow(opx, -1)
                - 2 * Li2(-x * z) * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * z) * NC * pow(opx, -1)
                - Li2(-x * z) * NC
                - Li2(-x * z) * z * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * z) * z * NC * pow(opx, -1)
                + Li2(-x * z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 2 * Li2(-x * z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - Li2(-x * z) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x * z) * x * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 4 * Li2(-x * z) * x * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(-x * z) * x * pow(z, -1) * NC
                - Li2(-x * z) * x * pow(NC, -1) * pow(opx, -1)
                + Li2(-x * z) * x * NC * pow(opx, -1)
                - 2 * Li2(-x * z) * x * z * pow(NC, -1)
                + 2 * Li2(-x * z) * x * z * NC
                + Li2(-x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - Li2(-x * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(opz, -1)
                - 2 * Li2(-x * z) * pow(x, 2) * pow(NC, -1)
                + 2 * Li2(-x * z) * pow(x, 2) * NC
                - 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 6 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
            )
            tmp += (
                +4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                - 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * pow(z, -1) * pow(NC, -1) * sqrtxz1
                + 20 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 16 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * pow(NC, -1) * pow(sqrtxz1, -1)
                - 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * z * pow(NC, -1) * pow(sqrtxz1, -1)
                - 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * sqrtxz1
                - 22 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
            )
            tmp += (
                +20 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 2) * z * pow(NC, -1) * pow(sqrtxz1, -1)
                + 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                - 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz1, -1)
                + 2 * Li2(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 2 * Li2(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(x) * pow(x, -2) * pow(z, -1) * pow(NC, -1)
                + Li2(x) * pow(x, -2) * pow(z, -1) * NC * pow(opx, -1)
                - Li2(x) * pow(x, -2) * pow(z, -1) * NC
                - Li2(x) * pow(x, -2) * pow(NC, -1) * pow(opx, -1)
                + Li2(x) * pow(x, -2) * pow(NC, -1)
                - Li2(x) * pow(x, -2) * z * pow(NC, -1) * pow(opx, -1)
                + Li2(x) * pow(x, -2) * z * pow(NC, -1)
                + Li2(x) * pow(x, -2) * z * NC * pow(opx, -1)
                - Li2(x) * pow(x, -2) * z * NC
                + 6 * Li2(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 4 * Li2(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 6 * Li2(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 4 * Li2(x) * pow(x, -1) * pow(z, -1) * pow(NC, -1)
                + 3 * Li2(x) * pow(x, -1) * pow(z, -1) * NC * pow(opx, -1)
            )
            tmp += (
                -2 * Li2(x) * pow(x, -1) * pow(z, -1) * NC
                - 3 * Li2(x) * pow(x, -1) * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(x) * pow(x, -1) * pow(NC, -1)
                - 3 * Li2(x) * pow(x, -1) * z * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(x) * pow(x, -1) * z * pow(NC, -1)
                + 3 * Li2(x) * pow(x, -1) * z * NC * pow(opx, -1)
                - 2 * Li2(x) * pow(x, -1) * z * NC
                + 6 * Li2(x) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                - 6 * Li2(x) * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 4.0 * Li2(x) * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(x) * pow(z, -1) * NC * pow(opx, -1)
                - 1.0 / 4.0 * Li2(x) * pow(z, -1) * NC
                - 2 * Li2(x) * pow(NC, -1) * pow(omz, -1)
                - 4 * Li2(x) * pow(NC, -1) * pow(opx, -1)
                + 3.0 / 2.0 * Li2(x) * pow(NC, -1)
                + 2 * Li2(x) * NC * pow(opx, -1)
                - 3.0 / 2.0 * Li2(x) * NC
                - 2 * Li2(x) * z * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(x) * z * NC * pow(opx, -1)
                + 2 * Li2(x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                + 4 * Li2(x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(x) * x * pow(z, -1) * pow(NC, -1) * pow(opx, -1)
                - 9.0 / 2.0 * Li2(x) * x * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(x) * x * pow(z, -1) * NC
                - 4 * Li2(x) * x * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(x) * x * pow(NC, -1) * pow(opx, -1)
                + Li2(x) * x * pow(NC, -1)
                + 2 * Li2(x) * x * NC * pow(opx, -1)
                - Li2(x) * x * NC
                - Li2(x) * x * z * pow(NC, -1)
                + Li2(x) * x * z * NC
                + 2 * Li2(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(x) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - Li2(x) * pow(x, 2) * pow(NC, -1)
                + Li2(x) * pow(x, 2) * NC
                + Li2(z) * pow(NC, -1)
                - Li2(z) * NC
                - 2 * Li2(z) * x * pow(NC, -1)
                + 2 * Li2(z) * x * NC
                - 1.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(x, -1) * NC * sqrtxz3
                - 5.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(z, -1) * NC * sqrtxz3
            )
            tmp += (
                +2 * InvTanInt(-sqrtxz3) * z * pow(NC, -1) * sqrtxz3
                - 9.0 / 2.0 * InvTanInt(-sqrtxz3) * z * NC * sqrtxz3
                - 5.0 / 2.0 * InvTanInt(-sqrtxz3) * x * NC * sqrtxz3
                - InvTanInt(z * sqrtxz3) * pow(x, -1) * NC * sqrtxz3
                - 5 * InvTanInt(z * sqrtxz3) * pow(z, -1) * NC * sqrtxz3
                + 4 * InvTanInt(z * sqrtxz3) * z * pow(NC, -1) * sqrtxz3
                - 9 * InvTanInt(z * sqrtxz3) * z * NC * sqrtxz3
                - 5 * InvTanInt(z * sqrtxz3) * x * NC * sqrtxz3
                + 1.0 / 2.0 * InvTanInt(sqrtxz3) * pow(x, -1) * NC * sqrtxz3
                + 5.0 / 2.0 * InvTanInt(sqrtxz3) * pow(z, -1) * NC * sqrtxz3
                - 2 * InvTanInt(sqrtxz3) * z * pow(NC, -1) * sqrtxz3
                + 9.0 / 2.0 * InvTanInt(sqrtxz3) * z * NC * sqrtxz3
                + 5.0 / 2.0 * InvTanInt(sqrtxz3) * x * NC * sqrtxz3
            )

            res += tmp

        return res


def c2p_g2g_eq(x, z, rsl, order, f=C2Pg2gEq_DR0123_scheme):
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
