from configs.eh import *


def C2Lq2gEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
    res = 0.0

    if cx == "D" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "D":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "3":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
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
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    8.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 10.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 24 * ln(x) * pow(NC, -1) * x * CF
                    + 24 * ln(x) * pow(NC, -1) * x * z * CF
                    + (-1) * 14 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 40 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 26 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 44 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 32 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + 24 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 64 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 40 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 24 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 68 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 44 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * ln(x) * ln(omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 24 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 32 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 24 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF
                    + 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +18 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 10 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 20 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 52 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 32 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 16 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 10 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 26 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF
                    + 8 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    8.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 10.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 24 * ln(x) * pow(NC, -1) * x * CF
                    + 24 * ln(x) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 12 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 38 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 26 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + 16 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 56 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 40 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + 20 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 52 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 32 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 20 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 64 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 44 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 24 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 12 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 44 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 32 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF
                    + 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +18 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 10 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 16 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 40 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 16 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(omz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + 8 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 24 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 8 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * CF
                    + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    8.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 26.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 6 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 24 * ln(x) * pow(NC, -1) * x * CF
                    + 24 * ln(x) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 14 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 42 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 28 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 48 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 36 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + 24 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 60 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 36 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 24 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 72 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 48 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * ln(x) * ln(omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF
                    + 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 14 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 12 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 20 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 36 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 28 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +22 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 14 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 20 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 44 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 16 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 10 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 30 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 20 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF
                    + 8 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF
                    + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    8.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 10.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 24 * ln(x) * pow(NC, -1) * x * CF
                    + 24 * ln(x) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 12 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 36 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 24 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + 16 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 52 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 36 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + 20 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 56 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 36 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 20 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 60 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 40 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF
                    + 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 10 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 8 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 28 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 20 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 12 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 40 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 28 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 12 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +18 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 10 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 16 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 40 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 16 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(omz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + 8 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 24 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 8 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * CF
                    + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF
                    + 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    2 * NC * x * pow(pi, 2) * CF
                    + (-1) * 2 * NC * x * z * pow(pi, 2) * CF
                    + (-1) * 12 * ln(x) * NC * x * z * CF
                    + (-1) * 4 * ln(x) * ln(-xmz) * NC * x * CF
                    + 4 * ln(x) * ln(-xmz) * NC * x * z * CF
                    + (-1) * 14 * pow(ln(x), 2) * NC * x * CF
                    + 14 * pow(ln(x), 2) * NC * x * z * CF
                    + 24 * ln(x) * ln(z) * NC * x * CF
                    + (-1) * 24 * ln(x) * ln(z) * NC * x * z * CF
                    + 24 * ln(x) * ln(omx) * NC * x * CF
                    + (-1) * 24 * ln(x) * ln(omx) * NC * x * z * CF
                    + 12 * ln(x) * ln(omz) * NC * x * CF
                    + (-1) * 12 * ln(x) * ln(omz) * NC * x * z * CF
                    + 8 * ln(z) * NC * x * z * CF
                    + 4 * ln(z) * ln(-xmz) * NC * x * CF
                    + (-1) * 4 * ln(z) * ln(-xmz) * NC * x * z * CF
                    + (-1) * 10 * pow(ln(z), 2) * NC * x * CF
                    + 10 * pow(ln(z), 2) * NC * x * z * CF
                    + (-1) * 20 * ln(z) * ln(omx) * NC * x * CF
                    + 20 * ln(z) * ln(omx) * NC * x * z * CF
                    + (-1) * 4 * ln(z) * ln(omz) * NC * x * CF
                    + 4 * ln(z) * ln(omz) * NC * x * z * CF
                    + 8 * ln(omx) * NC * x * z * CF
                    + (-1) * 8 * pow(ln(omx), 2) * NC * x * CF
                    + 8 * pow(ln(omx), 2) * NC * x * z * CF
                    + (-1) * 8 * ln(omx) * ln(omz) * NC * x * CF
                    + 8 * ln(omx) * ln(omz) * NC * x * z * CF
                    + 4 * ln(omz) * NC * x * z * CF
                    + (-1) * 2 * pow(ln(omz), 2) * NC * x * CF
                    + 2 * pow(ln(omz), 2) * NC * x * z * CF
                    + 4 * Li2(pow(omx, -1) * omz) * NC * x * CF
                    + (-1) * 4 * Li2(pow(omx, -1) * omz) * NC * x * z * CF
                    + (-1) * 4 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * x * CF
                    + 4 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * x * z * CF
                    + 4 * Li2(z) * NC * x * CF
                    + (-1) * 4 * Li2(z) * NC * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    2 * NC * x * pow(pi, 2) * CF
                    + (-1) * 2 * NC * x * z * pow(pi, 2) * CF
                    + (-1) * 12 * ln(x) * NC * x * z * CF
                    + (-1) * 12 * pow(ln(x), 2) * NC * x * CF
                    + 12 * pow(ln(x), 2) * NC * x * z * CF
                    + 20 * ln(x) * ln(z) * NC * x * CF
                    + (-1) * 20 * ln(x) * ln(z) * NC * x * z * CF
                    + 20 * ln(x) * ln(omx) * NC * x * CF
                    + (-1) * 20 * ln(x) * ln(omx) * NC * x * z * CF
                    + 16 * ln(x) * ln(omz) * NC * x * CF
                    + (-1) * 16 * ln(x) * ln(omz) * NC * x * z * CF
                    + (-1) * 4 * ln(x) * ln(xmz) * NC * x * CF
                    + 4 * ln(x) * ln(xmz) * NC * x * z * CF
                    + 8 * ln(z) * NC * x * z * CF
                    + (-1) * 8 * pow(ln(z), 2) * NC * x * CF
                    + 8 * pow(ln(z), 2) * NC * x * z * CF
                    + (-1) * 16 * ln(z) * ln(omx) * NC * x * CF
                    + 16 * ln(z) * ln(omx) * NC * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omz) * NC * x * CF
                    + 8 * ln(z) * ln(omz) * NC * x * z * CF
                    + 4 * ln(z) * ln(xmz) * NC * x * CF
                    + (-1) * 4 * ln(z) * ln(xmz) * NC * x * z * CF
                    + 8 * ln(omx) * NC * x * z * CF
                    + (-1) * 8 * pow(ln(omx), 2) * NC * x * CF
                    + 8 * pow(ln(omx), 2) * NC * x * z * CF
                    + (-1) * 8 * ln(omx) * ln(omz) * NC * x * CF
                    + 8 * ln(omx) * ln(omz) * NC * x * z * CF
                    + 4 * ln(omz) * NC * x * z * CF
                    + (-1) * 2 * pow(ln(omz), 2) * NC * x * CF
                    + 2 * pow(ln(omz), 2) * NC * x * z * CF
                    + 4 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * x * CF
                    + (-1) * 4 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * x * z * CF
                    + (-1) * 4 * Li2(omx * pow(omz, -1)) * NC * x * CF
                    + 4 * Li2(omx * pow(omz, -1)) * NC * x * z * CF
                    + 4 * Li2(z) * NC * x * CF
                    + (-1) * 4 * Li2(z) * NC * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) != round(x, ndecimals) and round(z, ndecimals) != round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    +(-1) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 2 * pow(NC, -1) * CF
                    + 3 * pow(NC, -1) * z * CF
                    + pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF
                    + (-1) * 8.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + 17 * pow(NC, -1) * x * CF
                    + 4 * pow(NC, -1) * x * sqrtxz1 * rln2 * CF
                    + 23.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + (-1) * 14 * pow(NC, -1) * x * z * CF
                    + (-1) * 14.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + 4 * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1)
                    + (-1) * 4 * pow(NC, -1) * pow(x, 2) * CF
                    + (-1) * 4 * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1)
                    + NC * pow(z, -1) * CF
                    + 10 * NC * CF
                    + (-1) * 7 * NC * z * CF
                    + (-1) * 4 * NC * pow(z, 2) * CF
                    + 7 * NC * x * pow(z, -1) * CF
                    + (-1) * 23 * NC * x * CF
                    + 8 * NC * x * pow(rln2, 2) * CF
                    + 8 * NC * x * sqrtxz1 * rln2 * CF
                    + (-1) * NC * x * pow(pi, 2) * CF
                    + 6 * NC * x * z * CF
                    + 8 * NC * x * z * pow(rln2, 2) * CF
                    + 14.0 / 3.0 * NC * x * z * pow(pi, 2) * CF
                    + 10 * NC * x * pow(z, 2) * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * sqrtxz1 * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * NC * x * rln2 * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * NC * x * sqrtxz1 * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * NC * x * z * rln2 * CF
                    + 0
                )
                tmp += (
                    +8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * CF
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * z * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * NC * x * rln2 * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * NC * x * z * rln2 * CF
                    + 2 * ln(x) * pow(NC, -1) * CF
                    + (-1) * 2 * ln(x) * pow(NC, -1) * z * CF
                    + ln(x) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                    + 7 * ln(x) * pow(NC, -1) * x * CF
                    + 8 * ln(x) * pow(NC, -1) * x * CF * omx
                    + 2 * ln(x) * pow(NC, -1) * x * sqrtxz1 * CF
                    + (-1) * 16 * ln(x) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1)
                    + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * CF
                    + 4 * ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -2)
                    + (-1) * 8 * ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, 4) * CF * pow(omxmz, -2)
                    + (-1) * 2 * ln(x) * NC * CF
                    + 2 * ln(x) * NC * z * CF
                    + (-1) * 7 * ln(x) * NC * x * pow(z, -1) * CF
                    + (-1) * 7 * ln(x) * NC * x * CF
                    + 4 * ln(x) * NC * x * rln2 * CF
                    + 4 * ln(x) * NC * x * sqrtxz1 * CF
                    + 18 * ln(x) * NC * x * z * CF
                    + 4 * ln(x) * NC * x * z * rln2 * CF
                    + 8 * ln(x) * NC * x * pow(z, 2) * CF
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * CF
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * z * CF
                    + 14 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 44 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + 30 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + 16 * pow(ln(x), 2) * NC * x * CF
                    + (-1) * 16 * pow(ln(x), 2) * NC * x * z * CF
                    + (-1) * 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 40 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 34 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 32 * ln(x) * ln(z) * NC * x * CF
                    + (-1) * 2 * ln(x) * ln(z) * NC * x * z * CF
                    + 0
                )
                tmp += (
                    +(-1) * 20 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 56 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 36 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 28 * ln(x) * ln(omx) * NC * x * CF
                    + 28 * ln(x) * ln(omx) * NC * x * z * CF
                    + (-1) * 20 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 62 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 42 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 22 * ln(x) * ln(omz) * NC * x * CF
                    + 22 * ln(x) * ln(omz) * NC * x * z * CF
                    + (-1) * 4 * ln(z) * pow(NC, -1) * CF
                    + (-1) * 4 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                    + (-1) * 12 * ln(z) * pow(NC, -1) * x * CF
                    + 2 * ln(z) * pow(NC, -1) * x * sqrtxz1 * CF
                    + 18 * ln(z) * pow(NC, -1) * x * z * CF
                    + 8 * ln(z) * NC * CF
                    + 8 * ln(z) * NC * z * CF
                    + 10 * ln(z) * NC * x * pow(z, -1) * CF
                    + 4 * ln(z) * NC * x * CF
                    + 12 * ln(z) * NC * x * rln2 * CF
                    + 4 * ln(z) * NC * x * sqrtxz1 * CF
                    + (-1) * 28 * ln(z) * NC * x * z * CF
                    + 12 * ln(z) * NC * x * z * rln2 * CF
                    + (-1) * 4 * ln(z) * NC * x * pow(z, 2) * CF
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * CF
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * z * CF
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * CF
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * z * CF
                    + 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 10 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + 16 * pow(ln(z), 2) * NC * x * CF
                    + 14 * pow(ln(z), 2) * NC * x * z * CF
                    + 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 24 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + 18 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 24 * ln(z) * ln(omx) * NC * x * CF
                    + (-1) * 2 * ln(z) * ln(omx) * NC * x * z * CF
                    + 4 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 24 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + 0
                )
                tmp += (
                    +20 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 20 * ln(z) * ln(omz) * NC * x * CF
                    + (-1) * 20 * ln(z) * ln(omz) * NC * x * z * CF
                    + (-1) * 2 * ln(omx) * pow(NC, -1) * CF
                    + 2 * ln(omx) * pow(NC, -1) * z * CF
                    + (-1) * 2 * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 7 * ln(omx) * pow(NC, -1) * x * CF
                    + 9 * ln(omx) * pow(NC, -1) * x * z * CF
                    + 2 * ln(omx) * NC * CF
                    + (-1) * 2 * ln(omx) * NC * z * CF
                    + 6 * ln(omx) * NC * x * pow(z, -1) * CF
                    + (-1) * ln(omx) * NC * x * CF
                    + (-1) * 9 * ln(omx) * NC * x * z * CF
                    + (-1) * 4 * ln(omx) * NC * x * pow(z, 2) * CF
                    + 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 20 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + 12 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + 10 * pow(ln(omx), 2) * NC * x * CF
                    + (-1) * 10 * pow(ln(omx), 2) * NC * x * z * CF
                    + 12 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 36 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 16 * ln(omx) * ln(omz) * NC * x * CF
                    + (-1) * 16 * ln(omx) * ln(omz) * NC * x * z * CF
                    + (-1) * 2 * ln(omz) * pow(NC, -1) * CF
                    + 2 * ln(omz) * pow(NC, -1) * z * CF
                    + (-1) * 2 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * CF * omx
                    + 9 * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1)
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -2)
                    + 8 * ln(omz) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1)
                    + 4 * ln(omz) * pow(NC, -1) * pow(x, 4) * CF * pow(omxmz, -2)
                    + 2 * ln(omz) * NC * CF
                    + (-1) * 2 * ln(omz) * NC * z * CF
                    + 6 * ln(omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 5 * ln(omz) * NC * x * CF
                    + (-1) * ln(omz) * NC * x * z * CF
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(omz) * NC * x * pow(z, 2) * CF
                    + 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 24 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + 6 * pow(ln(omz), 2) * NC * x * CF
                    + (-1) * 6 * pow(ln(omz), 2) * NC * x * z * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * z * CF
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * CF
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * z * CF
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * CF
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * z * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * z * CF
                    + 4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * Li2(1 - x * pow(z, -1)) * NC * x * CF
                    + 4 * Li2(1 - x * pow(z, -1)) * NC * x * z * CF
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * x * CF
                    + 2 * Li2(x) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * Li2(x) * NC * x * CF
                    + 2 * Li2(x) * NC * x * z * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 22 * Li2(z) * NC * x * z * CF
                    + 0
                )
            if "001" == order:
                tmp += 2 * LMUA * pow(NC, -1) * x * pow(z, -1) * CF + (-1) * 4 * LMUA * pow(NC, -1) * x * CF + 2 * LMUA * pow(NC, -1) * x * z * CF + (-1) * 6 * LMUA * NC * x * pow(z, -1) * CF + (-1) * 22.0 / 3.0 * LMUA * NC * x * CF + 28.0 / 3.0 * LMUA * NC * x * z * CF + 4 * LMUA * NC * x * pow(z, 2) * CF + 4.0 / 3.0 * LMUA * NF * x * CF + (-1) * 4.0 / 3.0 * LMUA * NF * x * z * CF + 0
                tmp += (-1) * 2 * ln(z) * LMUA * pow(NC, -1) * x * z * CF + (-1) * 8 * ln(z) * LMUA * NC * x * CF + (-1) * 14 * ln(z) * LMUA * NC * x * z * CF + 0
                tmp += (-1) * 8 * ln(omz) * LMUA * NC * x * CF + 8 * ln(omz) * LMUA * NC * x * z * CF + 0
            if "010" == order:
                tmp += 2 * LMUF * pow(NC, -1) * CF + (-1) * 2 * LMUF * pow(NC, -1) * z * CF + LMUF * pow(NC, -1) * x * CF + (-1) * LMUF * pow(NC, -1) * x * z * CF + (-1) * 2 * LMUF * NC * CF + 2 * LMUF * NC * z * CF + (-1) * LMUF * NC * x * CF + LMUF * NC * x * z * CF + 0
                tmp += (-1) * 2 * ln(x) * LMUF * pow(NC, -1) * x * CF + 2 * ln(x) * LMUF * pow(NC, -1) * x * z * CF + 2 * ln(x) * LMUF * NC * x * CF + (-1) * 2 * ln(x) * LMUF * NC * x * z * CF + 0
                tmp += 4 * ln(omx) * LMUF * pow(NC, -1) * x * CF + (-1) * 4 * ln(omx) * LMUF * pow(NC, -1) * x * z * CF + (-1) * 4 * ln(omx) * LMUF * NC * x * CF + 4 * ln(omx) * LMUF * NC * x * z * CF + 0
            if "100" == order:
                tmp += 22.0 / 3.0 * LMUR * NC * x * CF + (-1) * 22.0 / 3.0 * LMUR * NC * x * z * CF + (-1) * 4.0 / 3.0 * LMUR * NF * x * CF + 4.0 / 3.0 * LMUR * NF * x * z * CF + 0
            res += tmp

        return res


def c2lq2g_eq(x, z, rsl, order, f=C2Lq2gEq_DR0123_scheme):
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
