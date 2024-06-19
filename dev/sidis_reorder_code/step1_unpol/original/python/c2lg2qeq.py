from configs.eh import *


def C2Lg2qEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
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
            tmp = (
                2 * pow(NC, -1) * x * pow(z, -1)
                + 2 * pow(NC, -1) * x * pow(omz, -1)
                - 7.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 7.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                - 4 * NC * x
                + 2.0 / 3.0 * NC * x * pow(pi, 2)
                + 4 * NC * pow(x, 2)
                - 2.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * NC * x
                + 12 * ln(x) * NC * pow(x, 2)
                + 13 * pow(ln(x), 2) * pow(NC, -1) * x
                - 13 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 12 * pow(ln(x), 2) * NC * x
                + 12 * pow(ln(x), 2) * NC * pow(x, 2)
                - 16 * ln(x) * ln(z) * pow(NC, -1) * x
                + 16 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 20 * ln(x) * ln(z) * NC * x
                - 20 * ln(x) * ln(z) * NC * pow(x, 2)
                - 22 * ln(x) * ln(omx) * pow(NC, -1) * x
                + 22 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 16 * ln(x) * ln(omx) * NC * x
                - 16 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 20 * ln(x) * ln(omz) * pow(NC, -1) * x
                + 20 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 20 * ln(x) * ln(omz) * NC * x
                - 20 * ln(x) * ln(omz) * NC * pow(x, 2)
                + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(xmz) * NC * x
                + 4 * ln(x) * ln(xmz) * NC * pow(x, 2)
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(omxmz) * NC * x
                + 4 * ln(x) * ln(omxmz) * NC * pow(x, 2)
                - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(z) * NC * x
                - 8 * ln(z) * NC * pow(x, 2)
            )
            tmp += (
                +5 * pow(ln(z), 2) * pow(NC, -1) * x
                - 5 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - 8 * pow(ln(z), 2) * NC * x
                + 8 * pow(ln(z), 2) * NC * pow(x, 2)
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * x
                - 12 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 8 * ln(z) * ln(omx) * NC * x
                + 8 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 8 * ln(z) * ln(omz) * pow(NC, -1) * x
                - 8 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 16 * ln(z) * ln(omz) * NC * x
                + 16 * ln(z) * ln(omz) * NC * pow(x, 2)
                - 2 * ln(z) * ln(xmz) * pow(NC, -1) * x
                + 2 * ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(z) * ln(xmz) * NC * x
                - 4 * ln(z) * ln(xmz) * NC * pow(x, 2)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 4 * ln(omx) * NC * x
                - 4 * ln(omx) * NC * pow(x, 2)
                + 8 * pow(ln(omx), 2) * pow(NC, -1) * x
                - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 2 * pow(ln(omx), 2) * NC * x
                + 2 * pow(ln(omx), 2) * NC * pow(x, 2)
                + 14 * ln(omx) * ln(omz) * pow(NC, -1) * x
                - 14 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 12 * ln(omx) * ln(omz) * NC * x
                + 12 * ln(omx) * ln(omz) * NC * pow(x, 2)
                - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(omz) * NC * x
                - 8 * ln(omz) * NC * pow(x, 2)
                + 6 * pow(ln(omz), 2) * pow(NC, -1) * x
                - 6 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                - 6 * pow(ln(omz), 2) * NC * x
                + 6 * pow(ln(omz), 2) * NC * pow(x, 2)
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x
                + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(omz) * ln(omxmz) * NC * x
            )
            tmp += (
                -4 * ln(omz) * ln(omxmz) * NC * pow(x, 2)
                + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x
                - 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x
                - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 4 * Li2(omx * pow(omz, -1)) * NC * x
                - 4 * Li2(omx * pow(omz, -1)) * NC * pow(x, 2)
                - 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(z * pow(omx, -1)) * NC * x
                + 4 * Li2(z * pow(omx, -1)) * NC * pow(x, 2)
                + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                2 * pow(NC, -1) * x * pow(z, -1)
                + 2 * pow(NC, -1) * x * pow(omz, -1)
                - 7.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 7.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                - 4 * NC * x
                + 2.0 / 3.0 * NC * x * pow(pi, 2)
                + 4 * NC * pow(x, 2)
                - 2.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * NC * x
                + 12 * ln(x) * NC * pow(x, 2)
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(-omxmz) * NC * x
                + 4 * ln(x) * ln(-omxmz) * NC * pow(x, 2)
                + 12 * pow(ln(x), 2) * pow(NC, -1) * x
                - 12 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 14 * pow(ln(x), 2) * NC * x
                + 14 * pow(ln(x), 2) * NC * pow(x, 2)
                - 18 * ln(x) * ln(z) * pow(NC, -1) * x
                + 18 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 24 * ln(x) * ln(z) * NC * x
                - 24 * ln(x) * ln(z) * NC * pow(x, 2)
                - 20 * ln(x) * ln(omx) * pow(NC, -1) * x
                + 20 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 12 * ln(x) * ln(omx) * NC * x
                - 12 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 18 * ln(x) * ln(omz) * pow(NC, -1) * x
                + 18 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 24 * ln(x) * ln(omz) * NC * x
                - 24 * ln(x) * ln(omz) * NC * pow(x, 2)
                + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(xmz) * NC * x
                + 4 * ln(x) * ln(xmz) * NC * pow(x, 2)
                - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(z) * NC * x
                - 8 * ln(z) * NC * pow(x, 2)
            )
            tmp += (
                +5 * pow(ln(z), 2) * pow(NC, -1) * x
                - 5 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - 8 * pow(ln(z), 2) * NC * x
                + 8 * pow(ln(z), 2) * NC * pow(x, 2)
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * x
                - 12 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 8 * ln(z) * ln(omx) * NC * x
                + 8 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 10 * ln(z) * ln(omz) * pow(NC, -1) * x
                - 10 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 20 * ln(z) * ln(omz) * NC * x
                + 20 * ln(z) * ln(omz) * NC * pow(x, 2)
                - 2 * ln(z) * ln(xmz) * pow(NC, -1) * x
                + 2 * ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(z) * ln(xmz) * NC * x
                - 4 * ln(z) * ln(xmz) * NC * pow(x, 2)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 4 * ln(omx) * NC * x
                - 4 * ln(omx) * NC * pow(x, 2)
                + 8 * pow(ln(omx), 2) * pow(NC, -1) * x
                - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 2 * pow(ln(omx), 2) * NC * x
                + 2 * pow(ln(omx), 2) * NC * pow(x, 2)
                + 12 * ln(omx) * ln(omz) * pow(NC, -1) * x
                - 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 8 * ln(omx) * ln(omz) * NC * x
                + 8 * ln(omx) * ln(omz) * NC * pow(x, 2)
                - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(omz) * NC * x
                - 8 * ln(omz) * NC * pow(x, 2)
                - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(omz) * ln(-omxmz) * NC * x
                - 4 * ln(omz) * ln(-omxmz) * NC * pow(x, 2)
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * x
                - 5 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                - 8 * pow(ln(omz), 2) * NC * x
            )
            tmp += (
                +8 * pow(ln(omz), 2) * NC * pow(x, 2)
                - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2)
                + 4 * Li2(pow(z, -1) * omx) * NC * x
                - 4 * Li2(pow(z, -1) * omx) * NC * pow(x, 2)
                + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x
                - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 4 * Li2(omx * pow(omz, -1)) * NC * x
                - 4 * Li2(omx * pow(omz, -1)) * NC * pow(x, 2)
                - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x
                + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2)
            )

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                2 * pow(NC, -1) * x * pow(z, -1)
                + 2 * pow(NC, -1) * x * pow(omz, -1)
                - 7.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 7.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                - 4 * NC * x
                + 10.0 / 3.0 * NC * x * pow(pi, 2)
                + 4 * NC * pow(x, 2)
                - 10.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * NC * x
                + 12 * ln(x) * NC * pow(x, 2)
                + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(-xmz) * NC * x
                + 4 * ln(x) * ln(-xmz) * NC * pow(x, 2)
                + 14 * pow(ln(x), 2) * pow(NC, -1) * x
                - 14 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 14 * pow(ln(x), 2) * NC * x
                + 14 * pow(ln(x), 2) * NC * pow(x, 2)
                - 18 * ln(x) * ln(z) * pow(NC, -1) * x
                + 18 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 24 * ln(x) * ln(z) * NC * x
                - 24 * ln(x) * ln(z) * NC * pow(x, 2)
                - 24 * ln(x) * ln(omx) * pow(NC, -1) * x
                + 24 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 12 * ln(x) * ln(omx) * NC * x
                - 12 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 18 * ln(x) * ln(omz) * pow(NC, -1) * x
                + 18 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 24 * ln(x) * ln(omz) * NC * x
                - 24 * ln(x) * ln(omz) * NC * pow(x, 2)
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(omxmz) * NC * x
                + 4 * ln(x) * ln(omxmz) * NC * pow(x, 2)
                - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(z) * NC * x
            )
            tmp += (
                -8 * ln(z) * NC * pow(x, 2)
                - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x
                + 2 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(z) * ln(-xmz) * NC * x
                - 4 * ln(z) * ln(-xmz) * NC * pow(x, 2)
                + 6 * pow(ln(z), 2) * pow(NC, -1) * x
                - 6 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - 10 * pow(ln(z), 2) * NC * x
                + 10 * pow(ln(z), 2) * NC * pow(x, 2)
                + 14 * ln(z) * ln(omx) * pow(NC, -1) * x
                - 14 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(z) * ln(omx) * NC * x
                + 4 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 6 * ln(z) * ln(omz) * pow(NC, -1) * x
                - 6 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 20 * ln(z) * ln(omz) * NC * x
                + 20 * ln(z) * ln(omz) * NC * pow(x, 2)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 4 * ln(omx) * NC * x
                - 4 * ln(omx) * NC * pow(x, 2)
                + 8 * pow(ln(omx), 2) * pow(NC, -1) * x
                - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 6 * pow(ln(omx), 2) * NC * x
                + 6 * pow(ln(omx), 2) * NC * pow(x, 2)
                + 14 * ln(omx) * ln(omz) * pow(NC, -1) * x
                - 14 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(omx) * ln(omz) * NC * x
                + 4 * ln(omx) * ln(omz) * NC * pow(x, 2)
                - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(omz) * NC * x
                - 8 * ln(omz) * NC * pow(x, 2)
                + 6 * pow(ln(omz), 2) * pow(NC, -1) * x
                - 6 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                - 10 * pow(ln(omz), 2) * NC * x
                + 10 * pow(ln(omz), 2) * NC * pow(x, 2)
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x
                + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
            )
            tmp += (
                +4 * ln(omz) * ln(omxmz) * NC * x
                - 4 * ln(omz) * ln(omxmz) * NC * pow(x, 2)
                - 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x
                + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(pow(omx, -1) * omz) * NC * x
                + 4 * Li2(pow(omx, -1) * omz) * NC * pow(x, 2)
                - 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(z * pow(omx, -1)) * NC * x
                + 4 * Li2(z * pow(omx, -1)) * NC * pow(x, 2)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x
                + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2)
                + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                2 * pow(NC, -1) * x * pow(z, -1)
                + 2 * pow(NC, -1) * x * pow(omz, -1)
                - 7.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 7.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                - 4 * NC * x
                + 2.0 / 3.0 * NC * x * pow(pi, 2)
                + 4 * NC * pow(x, 2)
                - 2.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * NC * x
                + 12 * ln(x) * NC * pow(x, 2)
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(-omxmz) * NC * x
                + 4 * ln(x) * ln(-omxmz) * NC * pow(x, 2)
                + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(-xmz) * NC * x
                + 4 * ln(x) * ln(-xmz) * NC * pow(x, 2)
                + 13 * pow(ln(x), 2) * pow(NC, -1) * x
                - 13 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 12 * pow(ln(x), 2) * NC * x
                + 12 * pow(ln(x), 2) * NC * pow(x, 2)
                - 20 * ln(x) * ln(z) * pow(NC, -1) * x
                + 20 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 20 * ln(x) * ln(z) * NC * x
                - 20 * ln(x) * ln(z) * NC * pow(x, 2)
                - 22 * ln(x) * ln(omx) * pow(NC, -1) * x
                + 22 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 16 * ln(x) * ln(omx) * NC * x
                - 16 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 16 * ln(x) * ln(omz) * pow(NC, -1) * x
                + 16 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 20 * ln(x) * ln(omz) * NC * x
                - 20 * ln(x) * ln(omz) * NC * pow(x, 2)
                - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(z) * NC * x
            )
            tmp += (
                -8 * ln(z) * NC * pow(x, 2)
                - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x
                + 2 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(z) * ln(-xmz) * NC * x
                - 4 * ln(z) * ln(-xmz) * NC * pow(x, 2)
                + 6 * pow(ln(z), 2) * pow(NC, -1) * x
                - 6 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - 6 * pow(ln(z), 2) * NC * x
                + 6 * pow(ln(z), 2) * NC * pow(x, 2)
                + 14 * ln(z) * ln(omx) * pow(NC, -1) * x
                - 14 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 12 * ln(z) * ln(omx) * NC * x
                + 12 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 8 * ln(z) * ln(omz) * pow(NC, -1) * x
                - 8 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 16 * ln(z) * ln(omz) * NC * x
                + 16 * ln(z) * ln(omz) * NC * pow(x, 2)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 4 * ln(omx) * NC * x
                - 4 * ln(omx) * NC * pow(x, 2)
                + 8 * pow(ln(omx), 2) * pow(NC, -1) * x
                - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 2 * pow(ln(omx), 2) * NC * x
                + 2 * pow(ln(omx), 2) * NC * pow(x, 2)
                + 12 * ln(omx) * ln(omz) * pow(NC, -1) * x
                - 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 8 * ln(omx) * ln(omz) * NC * x
                + 8 * ln(omx) * ln(omz) * NC * pow(x, 2)
                - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(omz) * NC * x
                - 8 * ln(omz) * NC * pow(x, 2)
                - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(omz) * ln(-omxmz) * NC * x
                - 4 * ln(omz) * ln(-omxmz) * NC * pow(x, 2)
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * x
                - 5 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
            )
            tmp += (
                -8 * pow(ln(omz), 2) * NC * x
                + 8 * pow(ln(omz), 2) * NC * pow(x, 2)
                - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2)
                + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x
                - 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2)
                + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2)
                + 4 * Li2(pow(z, -1) * omx) * NC * x
                - 4 * Li2(pow(z, -1) * omx) * NC * pow(x, 2)
                - 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x
                + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(pow(omx, -1) * omz) * NC * x
                + 4 * Li2(pow(omx, -1) * omz) * NC * pow(x, 2)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
            )

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
                1.0 / 8.0 * pow(NC, -1) * pow(x, -1) * pow(poly2, -1)
                - 1.0 / 8.0 * pow(NC, -1) * pow(x, -1)
                - 1.0 / 2.0 * pow(NC, -1) * pow(z, -1)
                - 1.0 / 8.0 * pow(NC, -1) * pow(poly2, -1)
                + 3.0 / 8.0 * pow(NC, -1)
                - 1.0 / 2.0 * pow(NC, -1) * z
                - 5.0 / 2.0 * pow(NC, -1) * x * pow(z, -1)
                - 1.0 / 4.0 * pow(NC, -1) * x * pow(poly2, -1)
                - 2 * pow(NC, -1) * x * pow(omz, -1)
                + pow(NC, -1) * x * pow(omxmz, -1)
                + 37.0 / 8.0 * pow(NC, -1) * x
                + 3 * pow(NC, -1) * x * pow(pi, 2)
                + 17.0 / 2.0 * pow(NC, -1) * x * z
                - pow(NC, -1) * x * z * pow(pi, 2)
                + 3 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 1.0 / 4.0 * pow(NC, -1) * pow(x, 2) * pow(poly2, -1)
                + 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1)
                - 39.0 / 8.0 * pow(NC, -1) * pow(x, 2)
                - 7.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                - 8 * pow(NC, -1) * pow(x, 2) * z
                + 1.0 / 8.0 * pow(NC, -1) * pow(x, 3) * pow(poly2, -1)
                + pow(NC, -1) * pow(x, 3) * pow(omxmz, -1)
                - 1.0 / 8.0 * pow(NC, -1) * pow(x, 4) * pow(poly2, -1)
                - 1.0 / 8.0 * NC * pow(x, -1) * pow(poly2, -1)
                + 169.0 / 72.0 * NC * pow(x, -1)
                + 1.0 / 2.0 * NC * pow(z, -1)
                + 1.0 / 8.0 * NC * pow(poly2, -1)
                - 409.0 / 24.0 * NC
                + 41.0 / 2.0 * NC * z
                + 1.0 / 2.0 * NC * x * pow(z, -1)
                + 1.0 / 4.0 * NC * x * pow(poly2, -1)
                - NC * x * pow(omxmz, -1)
                - 95.0 / 24.0 * NC * x
                - 17.0 / 3.0 * NC * x * pow(pi, 2)
                - 57.0 / 2.0 * NC * x * z
                + NC * x * z * pow(pi, 2)
                - NC * pow(x, 2) * pow(z, -1)
                - 1.0 / 4.0 * NC * pow(x, 2) * pow(poly2, -1)
                + 2 * NC * pow(x, 2) * pow(omxmz, -1)
                + 1343.0 / 72.0 * NC * pow(x, 2)
                + 3 * NC * pow(x, 2) * pow(pi, 2)
                + 8 * NC * pow(x, 2) * z
                - 1.0 / 8.0 * NC * pow(x, 3) * pow(poly2, -1)
                - NC * pow(x, 3) * pow(omxmz, -1)
                + 1.0 / 8.0 * NC * pow(x, 4) * pow(poly2, -1)
                + 22.0 / 3.0 * LMUR * NC * x
                - 22.0 / 3.0 * LMUR * NC * pow(x, 2)
                - 4.0 / 3.0 * LMUR * NF * x
                + 4.0 / 3.0 * LMUR * NF * pow(x, 2)
                + LMUF * pow(NC, -1) * z
            )
            tmp += (
                +LMUF * pow(NC, -1) * x * z
                - 2 * LMUF * pow(NC, -1) * pow(x, 2) * z
                - 4.0 / 3.0 * LMUF * NC * pow(x, -1)
                + 4 * LMUF * NC
                - LMUF * NC * z
                + 38.0 / 3.0 * LMUF * NC * x
                - LMUF * NC * x * z
                - 46.0 / 3.0 * LMUF * NC * pow(x, 2)
                + 2 * LMUF * NC * pow(x, 2) * z
                + 4.0 / 3.0 * LMUF * NF * x
                - 4.0 / 3.0 * LMUF * NF * pow(x, 2)
                + LMUA * pow(NC, -1) * x
                + 2 * LMUA * pow(NC, -1) * x * z
                - LMUA * pow(NC, -1) * pow(x, 2)
                - 2 * LMUA * pow(NC, -1) * pow(x, 2) * z
                - LMUA * NC * x
                - 2 * LMUA * NC * x * z
                + LMUA * NC * pow(x, 2)
                + 2 * LMUA * NC * pow(x, 2) * z
                + 3.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1)
                - 3.0 / 16.0 * ln(x) * pow(NC, -1) * pow(poly2, -2)
                + 1.0 / 16.0 * ln(x) * pow(NC, -1) * pow(poly2, -1)
                + 1.0 / 2.0 * ln(x) * pow(NC, -1)
                + 1.0 / 4.0 * ln(x) * pow(NC, -1) * z
                - 7 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                - 9.0 / 16.0 * ln(x) * pow(NC, -1) * x * pow(poly2, -2)
                - 3.0 / 8.0 * ln(x) * pow(NC, -1) * x * pow(poly2, -1)
                - 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1)
                - ln(x) * pow(NC, -1) * x * pow(omxmz, -1)
                + ln(x) * pow(NC, -1) * x
                + 17.0 / 4.0 * ln(x) * pow(NC, -1) * x * z
                + ln(x) * pow(NC, -1) * x * pow(z, 3) * pow(xmz, -2)
                + 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 9.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2)
                + 5.0 / 8.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1)
                + 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 2 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(xmz, -1)
                + ln(x) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -2)
                + ln(x) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1)
                - 7.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * pow(NC, -1) * pow(x, 2) * z
                + 9.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2)
                + 9.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1)
                + 5 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(xmz, -1)
            )
            tmp += (
                -2 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(omxmz, -2)
                - 9.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2)
                - 11.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1)
                - ln(x) * pow(NC, -1) * pow(x, 4) * pow(xmz, -2)
                + ln(x) * pow(NC, -1) * pow(x, 4) * pow(omxmz, -2)
                - 3.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(x) * NC * pow(x, -1) * pow(poly2, -2)
                - 5.0 / 16.0 * ln(x) * NC * pow(x, -1) * pow(poly2, -1)
                + 1.0 / 2.0 * ln(x) * NC * pow(x, -1)
                + 3.0 / 16.0 * ln(x) * NC * pow(poly2, -2)
                + 7.0 / 16.0 * ln(x) * NC * pow(poly2, -1)
                - 2 * ln(x) * NC
                + 39.0 / 4.0 * ln(x) * NC * z
                + ln(x) * NC * x * pow(z, -1)
                + 9.0 / 16.0 * ln(x) * NC * x * pow(poly2, -2)
                + 3.0 / 8.0 * ln(x) * NC * x * pow(poly2, -1)
                + ln(x) * NC * x * pow(omxmz, -1)
                + 19.0 / 2.0 * ln(x) * NC * x
                + 23.0 / 4.0 * ln(x) * NC * x * z
                - ln(x) * NC * x * pow(z, 3) * pow(xmz, -2)
                - 9.0 / 16.0 * ln(x) * NC * pow(x, 2) * pow(poly2, -2)
                - 5.0 / 8.0 * ln(x) * NC * pow(x, 2) * pow(poly2, -1)
                - ln(x) * NC * pow(x, 2) * pow(omxmz, -2)
                - 3 * ln(x) * NC * pow(x, 2) * pow(omxmz, -1)
                - 64 * ln(x) * NC * pow(x, 2)
                + 4 * ln(x) * NC * pow(x, 2) * z
                - 9.0 / 16.0 * ln(x) * NC * pow(x, 3) * pow(poly2, -2)
                - 1.0 / 16.0 * ln(x) * NC * pow(x, 3) * pow(poly2, -1)
                - 3 * ln(x) * NC * pow(x, 3) * pow(xmz, -1)
                + 2 * ln(x) * NC * pow(x, 3) * pow(omxmz, -2)
                + 2 * ln(x) * NC * pow(x, 3) * pow(omxmz, -1)
                + 9.0 / 16.0 * ln(x) * NC * pow(x, 4) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(x) * NC * pow(x, 4) * pow(poly2, -1)
                + ln(x) * NC * pow(x, 4) * pow(xmz, -2)
                - ln(x) * NC * pow(x, 4) * pow(omxmz, -2)
                + 3.0 / 16.0 * ln(x) * NC * pow(x, 5) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(x) * NC * pow(x, 6) * pow(poly2, -2)
                + 2 * ln(x) * LMUF * pow(NC, -1) * x * z
            )
            tmp += (
                +16 * ln(x) * LMUF * NC * x
                - 2 * ln(x) * LMUF * NC * x * z
                + 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                + 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 31.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                - 11.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                + 11.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                - 29.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                + 9.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 73.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                - 5.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1)
                + 5.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * z * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 151.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1)
                + 51.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * z * pow(sqrtxz2, -1)
                - 51.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 129.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                + 129.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                - 9.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 193.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                -1.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                - 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 31.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                + 11.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                - 11.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                + 29.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                - 9.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 73.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +5.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1)
                - 5.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * z * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 151.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1)
                - 51.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * z * pow(sqrtxz2, -1)
                + 51.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 129.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                - 129.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                + 9.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 193.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x
                - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x * z
                + 4 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(x, 2)
                - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(x, 2) * z
                + 4 * ln(x) * ln(1 + x) * NC * x * z
                + 4 * ln(x) * ln(1 + x) * NC * pow(x, 2) * z
                - 15 * pow(ln(x), 2) * pow(NC, -1) * x
                + pow(ln(x), 2) * pow(NC, -1) * x * z
                + 13 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z
                + 29 * pow(ln(x), 2) * NC * x
            )
            tmp += (
                -pow(ln(x), 2) * NC * x * z
                - 13 * pow(ln(x), 2) * NC * pow(x, 2)
                - 3 * pow(ln(x), 2) * NC * pow(x, 2) * z
                + 10 * ln(x) * ln(z) * pow(NC, -1) * x
                + 2 * ln(x) * ln(z) * pow(NC, -1) * x * z
                - 14 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                - 22 * ln(x) * ln(z) * NC * x
                - 2 * ln(x) * ln(z) * NC * x * z
                + 18 * ln(x) * ln(z) * NC * pow(x, 2)
                + 22 * ln(x) * ln(omx) * pow(NC, -1) * x
                + 2 * ln(x) * ln(omx) * pow(NC, -1) * x * z
                - 22 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * z
                - 18 * ln(x) * ln(omx) * NC * x
                - 2 * ln(x) * ln(omx) * NC * x * z
                + 18 * ln(x) * ln(omx) * NC * pow(x, 2)
                + 2 * ln(x) * ln(omx) * NC * pow(x, 2) * z
                + 20 * ln(x) * ln(omz) * pow(NC, -1) * x
                - 2 * ln(x) * ln(omz) * pow(NC, -1) * x * z
                - 20 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 40 * ln(x) * ln(omz) * NC * x
                + 2 * ln(x) * ln(omz) * NC * x * z
                + 24 * ln(x) * ln(omz) * NC * pow(x, 2)
                + 3.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1)
                + 3.0 / 16.0 * ln(z) * pow(NC, -1) * pow(poly2, -2)
                - 1.0 / 16.0 * ln(z) * pow(NC, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * ln(z) * pow(NC, -1)
                - 7.0 / 4.0 * ln(z) * pow(NC, -1) * z
                + 2 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                - 9.0 / 16.0 * ln(z) * pow(NC, -1) * x * pow(poly2, -2)
                - 3.0 / 8.0 * ln(z) * pow(NC, -1) * x * pow(poly2, -1)
                + 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                - 15.0 / 4.0 * ln(z) * pow(NC, -1) * x
                + 11.0 / 4.0 * ln(z) * pow(NC, -1) * x * z
                - ln(z) * pow(NC, -1) * x * pow(z, 3) * pow(xmz, -2)
                - 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 9.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2)
                - 5.0 / 8.0 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1)
                - 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(xmz, -1)
            )
            tmp += (
                +11.0 / 2.0 * ln(z) * pow(NC, -1) * pow(x, 2)
                + 9.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2)
                + 9.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1)
                - 5 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(xmz, -1)
                + 9.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2)
                + 11.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1)
                + ln(z) * pow(NC, -1) * pow(x, 4) * pow(xmz, -2)
                - 3.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(z) * NC * pow(x, -1) * pow(poly2, -2)
                - 5.0 / 16.0 * ln(z) * NC * pow(x, -1) * pow(poly2, -1)
                + 11.0 / 6.0 * ln(z) * NC * pow(x, -1)
                - 3.0 / 16.0 * ln(z) * NC * pow(poly2, -2)
                - 7.0 / 16.0 * ln(z) * NC * pow(poly2, -1)
                - 27.0 / 4.0 * ln(z) * NC
                + 47.0 / 4.0 * ln(z) * NC * z
                + 9.0 / 16.0 * ln(z) * NC * x * pow(poly2, -2)
                + 3.0 / 8.0 * ln(z) * NC * x * pow(poly2, -1)
                - 95.0 / 4.0 * ln(z) * NC * x
                - 51.0 / 4.0 * ln(z) * NC * x * z
                + ln(z) * NC * x * pow(z, 3) * pow(xmz, -2)
                + 9.0 / 16.0 * ln(z) * NC * pow(x, 2) * pow(poly2, -2)
                + 5.0 / 8.0 * ln(z) * NC * pow(x, 2) * pow(poly2, -1)
                + 80.0 / 3.0 * ln(z) * NC * pow(x, 2)
                - 9.0 / 16.0 * ln(z) * NC * pow(x, 3) * pow(poly2, -2)
                - 1.0 / 16.0 * ln(z) * NC * pow(x, 3) * pow(poly2, -1)
                + 3 * ln(z) * NC * pow(x, 3) * pow(xmz, -1)
                - 9.0 / 16.0 * ln(z) * NC * pow(x, 4) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(z) * NC * pow(x, 4) * pow(poly2, -1)
                - ln(z) * NC * pow(x, 4) * pow(xmz, -2)
                + 3.0 / 16.0 * ln(z) * NC * pow(x, 5) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(z) * NC * pow(x, 6) * pow(poly2, -2)
                - 2 * ln(z) * LMUA * pow(NC, -1) * x
                + 2 * ln(z) * LMUA * pow(NC, -1) * pow(x, 2)
                + 2 * ln(z) * LMUA * NC * x
                - 2 * ln(z) * LMUA * NC * pow(x, 2)
                - 2 * pow(ln(z), 2) * pow(NC, -1) * x
                + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
            )
            tmp += (
                +3 * pow(ln(z), 2) * NC * x
                - 3 * pow(ln(z), 2) * NC * pow(x, 2)
                - 8 * ln(z) * ln(omx) * pow(NC, -1) * x
                + 8 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 10 * ln(z) * ln(omx) * NC * x
                - 10 * ln(z) * ln(omx) * NC * pow(x, 2)
                - 14 * ln(z) * ln(omz) * pow(NC, -1) * x
                + 14 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 22 * ln(z) * ln(omz) * NC * x
                - 22 * ln(z) * ln(omz) * NC * pow(x, 2)
                - ln(omx) * pow(NC, -1) * z
                + 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + ln(omx) * pow(NC, -1) * x
                - 3 * ln(omx) * pow(NC, -1) * x * z
                - 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(omx) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * z
                + 4.0 / 3.0 * ln(omx) * NC * pow(x, -1)
                - 4 * ln(omx) * NC
                + ln(omx) * NC * z
                - 29 * ln(omx) * NC * x
                + 3 * ln(omx) * NC * x * z
                + 95.0 / 3.0 * ln(omx) * NC * pow(x, 2)
                - 4 * ln(omx) * NC * pow(x, 2) * z
                - 8 * ln(omx) * LMUF * NC * x
                + 8 * ln(omx) * LMUF * NC * pow(x, 2)
                - 8 * pow(ln(omx), 2) * pow(NC, -1) * x
                + 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                + 6 * pow(ln(omx), 2) * NC * x
                - 6 * pow(ln(omx), 2) * NC * pow(x, 2)
                - 14 * ln(omx) * ln(omz) * pow(NC, -1) * x
                + 14 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 16 * ln(omx) * ln(omz) * NC * x
                - 16 * ln(omx) * ln(omz) * NC * pow(x, 2)
                - ln(omz) * pow(NC, -1) * z
                + 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(omz) * pow(NC, -1) * x * pow(omxmz, -1)
                + 4 * ln(omz) * pow(NC, -1) * x
                - 3 * ln(omz) * pow(NC, -1) * x * z
                - 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -2)
                - ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1)
            )
            tmp += (
                -4 * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(omxmz, -2)
                - ln(omz) * pow(NC, -1) * pow(x, 4) * pow(omxmz, -2)
                + 4.0 / 3.0 * ln(omz) * NC * pow(x, -1)
                - 4 * ln(omz) * NC
                + ln(omz) * NC * z
                - ln(omz) * NC * x * pow(omxmz, -1)
                - 30 * ln(omz) * NC * x
                + 3 * ln(omz) * NC * x * z
                + ln(omz) * NC * pow(x, 2) * pow(omxmz, -2)
                + 3 * ln(omz) * NC * pow(x, 2) * pow(omxmz, -1)
                + 98.0 / 3.0 * ln(omz) * NC * pow(x, 2)
                - 4 * ln(omz) * NC * pow(x, 2) * z
                - 2 * ln(omz) * NC * pow(x, 3) * pow(omxmz, -2)
                - 2 * ln(omz) * NC * pow(x, 3) * pow(omxmz, -1)
                + ln(omz) * NC * pow(x, 4) * pow(omxmz, -2)
                + 4 * ln(omz) * LMUA * pow(NC, -1) * x
                - 4 * ln(omz) * LMUA * pow(NC, -1) * pow(x, 2)
                - 4 * ln(omz) * LMUA * NC * x
                + 4 * ln(omz) * LMUA * NC * pow(x, 2)
                - 7 * pow(ln(omz), 2) * pow(NC, -1) * x
                + 7 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                + 10 * pow(ln(omz), 2) * NC * x
                - 10 * pow(ln(omz), 2) * NC * pow(x, 2)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 31.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                - 11.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                + 11.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                - 29.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                + 9.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 73.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                - 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1)
                + 5.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * z * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 151.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1)
                + 51.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * z * pow(sqrtxz2, -1)
                - 51.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 129.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                + 129.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                - 9.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 193.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                +1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 31.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                + 11.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                - 11.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                + 29.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
            )
            tmp += (
                -9.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 73.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                + 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1)
                - 5.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * z * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 151.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1)
            )
            tmp += (
                -51.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * z * pow(sqrtxz2, -1)
                + 51.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 129.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                - 129.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                + 9.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 193.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
            )
            tmp += (
                +3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 31.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                + 11.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                - 11.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                + 29.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                - 9.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 73.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1)
                - 5.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * z * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 151.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1)
                - 51.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * z * pow(sqrtxz2, -1)
                + 51.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 129.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                - 129.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                + 9.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 193.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +1.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 31.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                - 11.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                + 11.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                - 29.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                + 9.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 73.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                - 5.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1)
                + 5.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * z * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 151.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1)
                + 51.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * z * pow(sqrtxz2, -1)
                - 51.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 129.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                + 129.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                - 9.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 193.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x
            )
            tmp += (
                -2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(x, 2)
                - 6 * Li2(1 - x * pow(z, -1)) * NC * x
                + 6 * Li2(1 - x * pow(z, -1)) * NC * pow(x, 2)
                + 4 * Li2(-x) * pow(NC, -1) * x
                - 4 * Li2(-x) * pow(NC, -1) * x * z
                + 4 * Li2(-x) * pow(NC, -1) * pow(x, 2)
                - 4 * Li2(-x) * pow(NC, -1) * pow(x, 2) * z
                + 4 * Li2(-x) * NC * x * z
                + 4 * Li2(-x) * NC * pow(x, 2) * z
                + 2 * Li2(x) * pow(NC, -1) * x
                + 4 * Li2(x) * pow(NC, -1) * x * z
                - 2 * Li2(x) * pow(NC, -1) * pow(x, 2)
                - 2 * Li2(x) * pow(NC, -1) * pow(x, 2) * z
                + 18 * Li2(x) * NC * x
                - 4 * Li2(x) * NC * x * z
                - 2 * Li2(x) * NC * pow(x, 2)
                + 2 * Li2(x) * NC * pow(x, 2) * z
                - 8 * Li2(z) * pow(NC, -1) * x
                + 8 * Li2(z) * pow(NC, -1) * pow(x, 2)
                + 8 * Li2(z) * NC * x
                - 8 * Li2(z) * NC * pow(x, 2)
            )

            res += tmp

        return res


def c2lg2q_eq(x, z, rsl, order, f=C2Lg2qEq_DR0123_scheme):
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
