from configs.eh import *


def C2Tg2gEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
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
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
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
                    +(-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(pi, 2) * pow(omz, -1) * pow(opx, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(pi, 2) * pow(omz, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(pi, 2)
                    + 1.0 / 6.0 * pow(NC, -1) * pow(x, -2) * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 6.0 * pow(NC, -1) * pow(x, -2) * pow(pi, 2)
                    + 1.0 / 6.0 * pow(NC, -1) * pow(x, -2) * z * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 6.0 * pow(NC, -1) * pow(x, -2) * z * pow(pi, 2)
                    + (-1) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * pow(omz, -1) * pow(opx, -1)
                    + 2.0 / 3.0 * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * pow(omz, -1)
                    + pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2)
                    + 1.0 / 2.0 * pow(NC, -1) * pow(x, -1) * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, -1) * pow(pi, 2)
                    + 1.0 / 2.0 * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2)
                    + 13.0 / 16.0 * pow(NC, -1) * pow(z, -1)
                    + 4 * pow(NC, -1) * pow(z, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 4 * pow(NC, -1) * pow(z, -1) * pow(rln2, 2)
                    + 8 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 8 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2
                    + 6 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 6 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(rln2, 2)
                    + (-1) * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * pow(omz, -1) * pow(opx, -1)
                    + pow(NC, -1) * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + 7.0 / 24.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * sqrtxz1
                    + 0
                )
                tmp += (
                    +24 * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + 18 * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 12 * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + 1.0 / 8.0 * pow(NC, -1)
                    + 4 * pow(NC, -1) * pow(rln2, 2)
                    + pow(NC, -1) * pow(pi, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * pow(sqrtxz1, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * pow(omz, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 4.0 * pow(NC, -1) * pow(pi, 2)
                    + (-1) * 8 * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 8 * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2
                    + (-1) * 6 * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + 6 * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + (-1) * 27.0 / 16.0 * pow(NC, -1) * z
                    + (-1) * 2 * pow(NC, -1) * z * pow(rln2, 2)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * pow(sqrtxz1, -1)
                    + 2.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 12.0 * pow(NC, -1) * z * pow(pi, 2)
                    + 1.0 / 4.0 * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 8 * pow(NC, -1) * x * pow(z, -1) * pow(rln2, 2) * pow(opz, -1)
                    + 8 * pow(NC, -1) * x * pow(z, -1) * pow(rln2, 2)
                    + (-1) * 16 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 16 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 12 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(rln2, 2) * pow(opz, -1)
                    + 12 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(rln2, 2)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * pow(omz, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 12.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2)
                    + 0
                )
                tmp += (
                    +(-1) * 2.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * sqrtxz1 * pow(opz, -1)
                    + 2.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * sqrtxz1
                    + (-1) * 80 * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 64 * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2
                    + (-1) * 60 * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + 48 * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + 1.0 / 2.0 * pow(NC, -1) * x
                    + (-1) * 8 * pow(NC, -1) * x * pow(rln2, 2)
                    + (-1) * 10.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * pow(sqrtxz1, -1)
                    + 2.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(NC, -1) * x * pow(pi, 2)
                    + 16 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2
                    + 12 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 12 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + 1.0 / 4.0 * pow(NC, -1) * x * z
                    + 4 * pow(NC, -1) * x * z * pow(rln2, 2)
                    + 2.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * pow(sqrtxz1, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2)
                    + 1.0 / 2.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 4 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 4 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(rln2, 2)
                    + 8 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 8 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2
                    + 6 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 6 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(rln2, 2)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2) * sqrtxz1
                    + 88 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 80 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2
                    + 66 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 60 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + (-1) * 9.0 / 4.0 * pow(NC, -1) * pow(x, 2)
                    + 4 * pow(NC, -1) * pow(x, 2) * pow(rln2, 2)
                    + 11.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 10.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(sqrtxz1, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                    + (-1) * 8 * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 8 * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2
                    + (-1) * 6 * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + 6 * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + 3.0 / 2.0 * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 4 * pow(NC, -1) * pow(x, 2) * z * pow(rln2, 2)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * z * pow(pi, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * z * pow(pi, 2) * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(NC, -1) * pow(x, 2) * z * pow(pi, 2)
                    + (-1) * 32 * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 32 * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 24 * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + 24 * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + (-1) * 4.0 / 3.0 * pow(NC, -1) * pow(x, 3) * pow(pi, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +4.0 / 3.0 * pow(NC, -1) * pow(x, 3) * pow(pi, 2) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 6.0 * NC * pow(x, -2) * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 6.0 * NC * pow(x, -2) * pow(z, -1) * pow(pi, 2)
                    + (-1) * 1.0 / 6.0 * NC * pow(x, -2) * z * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 6.0 * NC * pow(x, -2) * z * pow(pi, 2)
                    + (-1) * 5.0 / 16.0 * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * NC * pow(x, -1) * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 3.0 * NC * pow(x, -1) * pow(z, -1) * pow(pi, 2)
                    + 5.0 / 16.0 * NC * pow(x, -1)
                    + (-1) * 1.0 / 2.0 * NC * pow(x, -1) * z * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 3.0 * NC * pow(x, -1) * z * pow(pi, 2)
                    + (-1) * 5.0 / 16.0 * NC * pow(z, -2)
                    + (-1) * 11.0 / 16.0 * NC * pow(z, -1)
                    + 2 * NC * pow(z, -1) * pow(rln2, 2)
                    + 2 * NC * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 2.0 / 3.0 * NC * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 24.0 * NC * pow(z, -1) * pow(pi, 2)
                    + (-1) * 1.0 / 4.0 * NC
                    + (-1) * 2 * NC * pow(rln2, 2)
                    + 1.0 / 3.0 * NC * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 12.0 * NC * pow(pi, 2)
                    + 2 * NC * z
                    + 2 * NC * z * pow(rln2, 2)
                    + (-1) * 2.0 / 3.0 * NC * z * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 12.0 * NC * z * pow(pi, 2)
                    + 5.0 / 16.0 * NC * x * pow(z, -2)
                    + (-1) * 47.0 / 8.0 * NC * x * pow(z, -1)
                    + (-1) * 4 * NC * x * pow(z, -1) * pow(rln2, 2)
                    + (-1) * 4 * NC * x * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 1.0 / 3.0 * NC * x * pow(z, -1) * pow(pi, 2) * pow(opx, -1)
                    + 7.0 / 12.0 * NC * x * pow(z, -1) * pow(pi, 2)
                    + 41.0 / 8.0 * NC * x
                    + 4 * NC * x * pow(rln2, 2)
                    + 1.0 / 3.0 * NC * x * pow(pi, 2) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * NC * x * pow(pi, 2)
                    + (-1) * 9.0 / 16.0 * NC * x * z
                    + (-1) * 4 * NC * x * z * pow(rln2, 2)
                    + (-1) * 1.0 / 3.0 * NC * x * z * pow(pi, 2) * pow(opx, -1)
                    + 1.0 / 3.0 * NC * x * z * pow(pi, 2)
                    + 117.0 / 16.0 * NC * pow(x, 2) * pow(z, -1)
                    + 4 * NC * pow(x, 2) * pow(z, -1) * pow(rln2, 2)
                    + 4 * NC * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 2.0 / 3.0 * NC * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                    + (-1) * 89.0 / 16.0 * NC * pow(x, 2)
                    + 1.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                    + 0
                )
                tmp += +(-1) * 3.0 / 2.0 * NC * pow(x, 2) * z + 4 * NC * pow(x, 2) * z * pow(rln2, 2) + (-1) * 1.0 / 2.0 * NC * pow(x, 2) * z * pow(pi, 2) + 0
                tmp += (
                    +(-1) * 3.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                    + 3.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * sqrtxz3
                    + 3.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                    + (-1) * 15.0 / 2.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                    + 5.0 / 16.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                    + 9.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                    + 21.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                    + 5.0 / 16.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                    + 5.0 / 4.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * sqrtxz3
                    + (-1) * 19.0 / 16.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                    + 45.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                    + 105.0 / 8.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * z * sqrtxz3
                    + (-1) * 35.0 / 16.0 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                    + 3.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                    + (-1) * 3.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * sqrtxz3
                    + (-1) * 3.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                    + 15.0 / 2.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                    + (-1) * 5.0 / 16.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                    + (-1) * 9.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                    + (-1) * 21.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                    + 0
                )
                tmp += (
                    +(-1) * 5.0 / 16.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                    + (-1) * 5.0 / 4.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * sqrtxz3
                    + 19.0 / 16.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                    + (-1) * 45.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                    + (-1) * 105.0 / 8.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * z * sqrtxz3
                    + 35.0 / 16.0 * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                    + 3.0 / 4.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                    + (-1) * 3.0 / 4.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * sqrtxz3
                    + (-1) * 3.0 / 4.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                    + 15.0 / 4.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                    + (-1) * 5.0 / 32.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                    + (-1) * 9.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                    + (-1) * 21.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                    + (-1) * 5.0 / 32.0 * InvTanInt(-sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                    + (-1) * 5.0 / 8.0 * InvTanInt(-sqrtxz3) * NC * sqrtxz3
                    + 19.0 / 32.0 * InvTanInt(-sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                    + (-1) * 45.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                    + (-1) * 105.0 / 16.0 * InvTanInt(-sqrtxz3) * NC * x * z * sqrtxz3
                    + 35.0 / 32.0 * InvTanInt(-sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                    + 3.0 / 2.0 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                    + (-1) * 3.0 / 2.0 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * sqrtxz3
                    + (-1) * 3.0 / 2.0 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                    + 15.0 / 2.0 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                    + (-1) * 5.0 / 16.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                    + (-1) * 9.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                    + (-1) * 21.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                    + 0
                )
                tmp += (
                    +(-1) * 5.0 / 16.0 * InvTanInt(z * sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                    + (-1) * 5.0 / 4.0 * InvTanInt(z * sqrtxz3) * NC * sqrtxz3
                    + 19.0 / 16.0 * InvTanInt(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                    + (-1) * 45.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                    + (-1) * 105.0 / 8.0 * InvTanInt(z * sqrtxz3) * NC * x * z * sqrtxz3
                    + 35.0 / 16.0 * InvTanInt(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                    + (-1) * 3.0 / 4.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3
                    + 3.0 / 4.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * sqrtxz3
                    + 3.0 / 4.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3
                    + (-1) * 15.0 / 4.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3
                    + 5.0 / 32.0 * InvTanInt(sqrtxz3) * NC * pow(x, -2) * sqrtxz3
                    + 9.0 / 16.0 * InvTanInt(sqrtxz3) * NC * pow(x, -1) * pow(z, -1) * sqrtxz3
                    + 21.0 / 16.0 * InvTanInt(sqrtxz3) * NC * pow(x, -1) * z * sqrtxz3
                    + 5.0 / 32.0 * InvTanInt(sqrtxz3) * NC * pow(z, -2) * sqrtxz3
                    + 5.0 / 8.0 * InvTanInt(sqrtxz3) * NC * sqrtxz3
                    + (-1) * 19.0 / 32.0 * InvTanInt(sqrtxz3) * NC * pow(z, 2) * sqrtxz3
                    + 45.0 / 16.0 * InvTanInt(sqrtxz3) * NC * x * pow(z, -1) * sqrtxz3
                    + 105.0 / 16.0 * InvTanInt(sqrtxz3) * NC * x * z * sqrtxz3
                    + (-1) * 35.0 / 32.0 * InvTanInt(sqrtxz3) * NC * pow(x, 2) * sqrtxz3
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * rln2 * pow(opz, -1)
                    + 5 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * rln2
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 24 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * rln2
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2
                    + 3 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * rln2
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * rln2 * pow(opz, -1)
                    + (-1) * 10 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * rln2
                    + 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2
                    + 80 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 64 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 80 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 64 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2
                    + 12 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * rln2
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2 * pow(opz, -1)
                    + 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 88 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 80 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 88 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 80 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * rln2
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2
                    + 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * rln2
                    + 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 3 * ln(1 + sqrtxz1 - z) * NC * pow(z, -1) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * NC * pow(z, -1) * sqrtxz1
                    + 4 * ln(1 + sqrtxz1 - z) * NC * rln2
                    + (-1) * 3 * ln(1 + sqrtxz1 - z) * NC * z * rln2
                    + 6 * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1) * rln2
                    + 4 * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1) * sqrtxz1
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * NC * x * rln2
                    + 6 * ln(1 + sqrtxz1 - z) * NC * x * z * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * pow(z, -1) * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 2 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z * rln2
                    + (-1) * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(z, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 6 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * z
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 20 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * z
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 22 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(z, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC
                    + pow(ln(1 + sqrtxz1 - z), 2) * NC * z
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x * pow(z, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x * z
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(x, 2)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(x, 2) * z
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 3 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 12 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + 6 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 40 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z
                    + 0
                )
                tmp += (
                    +4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 44 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 40 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1)
                    + ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * z
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * pow(z, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * z
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * rln2 * pow(opz, -1)
                    + 3 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 12 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * rln2
                    + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2
                    + ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * rln2
                    + 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * rln2 * pow(opz, -1)
                    + (-1) * 6 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * rln2
                    + 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2
                    + 40 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 32 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2
                    + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * rln2
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2 * pow(opz, -1)
                    + 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 44 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 40 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * rln2
                    + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2
                    + 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * rln2
                    + 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2
                    + (-1) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1) * rln2
                    + (-1) * ln(1 + sqrtxz1 + z) * NC * z * rln2
                    + 2 * ln(1 + sqrtxz1 + z) * NC * x * pow(z, -1) * rln2
                    + 2 * ln(1 + sqrtxz1 + z) * NC * x * z * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * pow(z, -1) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z * rln2
                    + 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 3.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 5 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 11.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 5 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 1.0 / 2.0 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 4 * ln(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + 4 * ln(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * pow(NC, -1) * pow(x, -2)
                    + 2 * ln(x) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 2 * ln(x) * pow(NC, -1) * pow(x, -2) * z
                    + (-1) * 12 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 8 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + 12 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + 6 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, -1)
                    + 6 * ln(x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, -1) * z
                    + (-1) * 12 * ln(x) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 12 * ln(x) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 7.0 / 4.0 * ln(x) * pow(NC, -1) * pow(z, -1)
                    + 2 * ln(x) * pow(NC, -1) * pow(z, -1) * rln2 * pow(opz, -1)
                    + (-1) * 3 * ln(x) * pow(NC, -1) * pow(z, -1) * rln2
                    + 4 * ln(x) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 12 * ln(x) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * ln(x) * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(x) * pow(NC, -1) * pow(opx, -1)
                    + 9.0 / 4.0 * ln(x) * pow(NC, -1)
                    + 4 * ln(x) * pow(NC, -1) * rln2
                    + (-1) * 4 * ln(x) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(x) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 8 * ln(x) * pow(NC, -1) * z * pow(opx, -1)
                    + (-1) * 5 * ln(x) * pow(NC, -1) * z
                    + (-1) * 2 * ln(x) * pow(NC, -1) * z * rln2
                    + (-1) * 4 * ln(x) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + 4 * ln(x) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + 13 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(x) * pow(NC, -1) * x * pow(z, -1) * rln2 * pow(opz, -1)
                    + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1) * rln2
                    + (-1) * 8 * ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 40 * ln(x) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * ln(x) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 8 * ln(x) * pow(NC, -1) * x * pow(omz, -1)
                    + (-1) * 11.0 / 4.0 * ln(x) * pow(NC, -1) * x
                    + (-1) * 8 * ln(x) * pow(NC, -1) * x * rln2
                    + 8 * ln(x) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 4 * ln(x) * pow(NC, -1) * x * z * pow(opx, -1)
                    + (-1) * 5.0 / 4.0 * ln(x) * pow(NC, -1) * x * z
                    + 4 * ln(x) * pow(NC, -1) * x * z * rln2
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2 * pow(opz, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2
                    + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 44 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 40 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                    + 7.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2)
                    + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * rln2
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, 2) * z * rln2
                    + (-1) * 16 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 2 * ln(x) * NC * pow(x, -2) * pow(z, -1)
                    + (-1) * 2 * ln(x) * NC * pow(x, -2) * z * pow(opx, -1)
                    + 2 * ln(x) * NC * pow(x, -2) * z
                    + (-1) * 6 * ln(x) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 133.0 / 32.0 * ln(x) * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 5.0 / 32.0 * ln(x) * NC * pow(x, -1)
                    + (-1) * 6 * ln(x) * NC * pow(x, -1) * z * pow(opx, -1)
                    + 4 * ln(x) * NC * pow(x, -1) * z
                    + (-1) * 5.0 / 32.0 * ln(x) * NC * pow(z, -2)
                    + (-1) * 8 * ln(x) * NC * pow(z, -1) * pow(opx, -1)
                    + 59.0 / 16.0 * ln(x) * NC * pow(z, -1)
                    + 2 * ln(x) * NC * pow(z, -1) * rln2
                    + ln(x) * NC * pow(z, -1) * sqrtxz1
                    + 4 * ln(x) * NC * pow(opx, -1)
                    + (-1) * 67.0 / 16.0 * ln(x) * NC
                    + (-1) * 3 * ln(x) * NC * rln2
                    + (-1) * 8 * ln(x) * NC * z * pow(opx, -1)
                    + 165.0 / 32.0 * ln(x) * NC * z
                    + 2 * ln(x) * NC * z * rln2
                    + (-1) * 5.0 / 32.0 * ln(x) * NC * x * pow(z, -2)
                    + (-1) * 4 * ln(x) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 109.0 / 16.0 * ln(x) * NC * x * pow(z, -1)
                    + (-1) * 4 * ln(x) * NC * x * pow(z, -1) * rln2
                    + (-1) * 2 * ln(x) * NC * x * pow(z, -1) * sqrtxz1
                    + 4 * ln(x) * NC * x * pow(opx, -1)
                    + 73.0 / 16.0 * ln(x) * NC * x
                    + 6 * ln(x) * NC * x * rln2
                    + (-1) * 4 * ln(x) * NC * x * z * pow(opx, -1)
                    + 45.0 / 32.0 * ln(x) * NC * x * z
                    + (-1) * 4 * ln(x) * NC * x * z * rln2
                    + 109.0 / 32.0 * ln(x) * NC * pow(x, 2) * pow(z, -1)
                    + 4 * ln(x) * NC * pow(x, 2) * pow(z, -1) * rln2
                    + 2 * ln(x) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 77.0 / 32.0 * ln(x) * NC * pow(x, 2)
                    + (-1) * 2 * ln(x) * NC * pow(x, 2) * rln2
                    + (-1) * 1.0 / 2.0 * ln(x) * NC * pow(x, 2) * z
                    + 4 * ln(x) * NC * pow(x, 2) * z * rln2
                    + 0
                )
                tmp += (
                    +ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 6 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 20 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 22 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(z, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC
                    + (-1) * ln(x) * ln(1 + sqrtxz1 - z) * NC * z
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x * z
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 6 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 20 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 22 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 20 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z
                    + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1)
                    + ln(x) * ln(1 + sqrtxz1 + z) * NC
                    + (-1) * ln(x) * ln(1 + sqrtxz1 + z) * NC * z
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * z
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z
                    + 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z
                    + 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * pow(z, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * z
                    + 3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(z, -1)
                    + 3.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(z, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * NC
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * NC * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * pow(z, -1)) * NC * z
                    + ln(x) * ln(1 + x * pow(z, -1)) * NC * x * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * NC * x * pow(z, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * NC * x * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * NC * x * z * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * NC * x * z
                    + ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2)
                    + ln(x) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * z
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z
                    + 3 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z
                    + 3 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x
                    + (-1) * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * z * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * z) * NC * pow(x, -2) * pow(z, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 + x * z) * NC * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + x * z) * NC * pow(x, -2) * z
                    + 3.0 / 2.0 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * pow(z, -1)
                    + 3.0 / 2.0 * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * NC * pow(x, -1) * z
                    + 2 * ln(x) * ln(1 + x * z) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * NC * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * NC
                    + 2 * ln(x) * ln(1 + x * z) * NC * z * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * NC * x * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * NC * x * z * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * ln(1 + x * z) * NC * pow(x, 2) * z
                    + (-1) * ln(x) * ln(z + x) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + ln(x) * ln(z + x) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(z + x) * pow(NC, -1)
                    + 1.0 / 2.0 * ln(x) * ln(z + x) * pow(NC, -1) * z
                    + 2 * ln(x) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * pow(NC, -1) * x * pow(z, -1)
                    + ln(x) * ln(z + x) * pow(NC, -1) * x
                    + (-1) * ln(x) * ln(z + x) * pow(NC, -1) * x * z
                    + 0
                )
                tmp += (
                    +(-1) * ln(x) * ln(z + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + ln(x) * ln(z + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + ln(x) * ln(z + x) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(z + x) * NC * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(z + x) * NC * z
                    + ln(x) * ln(z + x) * NC * x * pow(z, -1)
                    + ln(x) * ln(z + x) * NC * x * z
                    + (-1) * ln(x) * ln(z + x) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(x) * ln(z + x) * NC * pow(x, 2)
                    + (-1) * ln(x) * ln(z + x) * NC * pow(x, 2) * z
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * 3.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + 3.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2)
                    + (-1) * 3.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + 3.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * z
                    + 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 9.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 9.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z
                    + 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * z * pow(opx, -1)
                    + pow(ln(x), 2) * pow(NC, -1) * z
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1)
                    + 3 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 15 * pow(ln(x), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 12 * pow(ln(x), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * x * pow(omz, -1)
                    + (-1) * pow(ln(x), 2) * pow(NC, -1) * x
                    + (-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 3 * pow(ln(x), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * z * pow(opx, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 33.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 15 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z
                    + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 3.0 / 4.0 * pow(ln(x), 2) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 3.0 / 4.0 * pow(ln(x), 2) * NC * pow(x, -2) * pow(z, -1)
                    + 3.0 / 4.0 * pow(ln(x), 2) * NC * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 3.0 / 4.0 * pow(ln(x), 2) * NC * pow(x, -2) * z
                    + 9.0 / 4.0 * pow(ln(x), 2) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, -1) * pow(z, -1)
                    + 9.0 / 4.0 * pow(ln(x), 2) * NC * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, -1) * z
                    + 3 * pow(ln(x), 2) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * pow(ln(x), 2) * NC * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(opx, -1)
                    + pow(ln(x), 2) * NC
                    + 3 * pow(ln(x), 2) * NC * z * pow(opx, -1)
                    + (-1) * pow(ln(x), 2) * NC * z
                    + 3.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * pow(ln(x), 2) * NC * x * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(opx, -1)
                    + pow(ln(x), 2) * NC * x
                    + 3.0 / 2.0 * pow(ln(x), 2) * NC * x * z * pow(opx, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, 2)
                    + pow(ln(x), 2) * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    +(-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + 1.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2)
                    + 1.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * z
                    + (-1) * 3 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + 3 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + 3.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1)
                    + 3.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z
                    + (-1) * 3 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 3 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + (-1) * 5.0 / 4.0 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 3 * ln(x) * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(opx, -1)
                    + ln(x) * ln(z) * pow(NC, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(x) * ln(z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(z) * pow(NC, -1) * z * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * z
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + 9.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1)
                    + 2 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 10 * ln(x) * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * x * z * pow(opx, -1)
                    + 2 * ln(x) * ln(z) * pow(NC, -1) * x * z
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 11 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 10 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                    + ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * z
                    + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(z) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * ln(x) * ln(z) * NC * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(z) * NC * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 2.0 * ln(x) * ln(z) * NC * pow(x, -2) * z
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(z) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(z) * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(z) * NC * pow(x, -1) * z * pow(opx, -1)
                    + ln(x) * ln(z) * NC * pow(x, -1) * z
                    + (-1) * 2 * ln(x) * ln(z) * NC * pow(z, -1) * pow(opx, -1)
                    + 3.0 / 4.0 * ln(x) * ln(z) * NC * pow(z, -1)
                    + ln(x) * ln(z) * NC * pow(opx, -1)
                    + (-1) * 5.0 / 2.0 * ln(x) * ln(z) * NC
                    + (-1) * 2 * ln(x) * ln(z) * NC * z * pow(opx, -1)
                    + 3.0 / 2.0 * ln(x) * ln(z) * NC * z
                    + (-1) * ln(x) * ln(z) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 7.0 / 2.0 * ln(x) * ln(z) * NC * x * pow(z, -1)
                    + ln(x) * ln(z) * NC * x * pow(opx, -1)
                    + (-1) * 3 * ln(x) * ln(z) * NC * x
                    + (-1) * ln(x) * ln(z) * NC * x * z * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * NC * x * z
                    + ln(x) * ln(z) * NC * pow(x, 2) * pow(z, -1)
                    + ln(x) * ln(z) * NC * pow(x, 2)
                    + ln(x) * ln(z) * NC * pow(x, 2) * z
                    + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2)
                    + (-1) * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * z
                    + 6 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 3 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 3 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z
                    + 6 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(NC, -1) * z * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * pow(NC, -1) * z
                    + 2 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 5 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(NC, -1) * x * z * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                    + (-1) * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                    + ln(x) * ln(omx) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(omx) * NC * pow(x, -2) * pow(z, -1)
                    + ln(x) * ln(omx) * NC * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * ln(x) * ln(omx) * NC * pow(x, -2) * z
                    + 3 * ln(x) * ln(omx) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * NC * pow(x, -1) * pow(z, -1)
                    + 3 * ln(x) * ln(omx) * NC * pow(x, -1) * z * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * ln(omx) * NC * pow(x, -1) * z
                    + 4 * ln(x) * ln(omx) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * 5.0 / 2.0 * ln(x) * ln(omx) * NC * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * NC * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * NC
                    + 4 * ln(x) * ln(omx) * NC * z * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * NC * z
                    + 2 * ln(x) * ln(omx) * NC * x * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(omx) * NC * x * pow(z, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * NC * x * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * NC * x * z * pow(opx, -1)
                    + (-1) * ln(x) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                    + ln(x) * ln(omx) * NC * pow(x, 2)
                    + 3.0 / 4.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1)
                    + 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(omz) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(omz) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * z
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 20 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + ln(x) * ln(omz) * pow(NC, -1) * x
                    + 4 * ln(x) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 22 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 8 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * 3.0 / 4.0 * ln(x) * ln(omz) * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(x) * ln(omz) * NC
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(omz) * NC * z
                    + 3.0 / 2.0 * ln(x) * ln(omz) * NC * x * pow(z, -1)
                    + (-1) * ln(x) * ln(omz) * NC * x
                    + (-1) * 2 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * ln(omz) * NC * pow(x, 2)
                    + (-1) * ln(x) * ln(omz) * NC * pow(x, 2) * z
                    + (-1) * 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + (-1) * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2)
                    + ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * z
                    + (-1) * 6 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + 6 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + 0
                )
                tmp += (
                    +3 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1)
                    + 3 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z
                    + (-1) * 6 * ln(x) * ln(opx) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 6 * ln(x) * ln(opx) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(opx, -1)
                    + ln(x) * ln(opx) * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * pow(NC, -1) * z * pow(opx, -1)
                    + (-1) * ln(x) * ln(opx) * pow(NC, -1) * z
                    + (-1) * 2 * ln(x) * ln(opx) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(opx) * pow(NC, -1) * x * pow(z, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * x
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * x * z * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * x * z
                    + (-1) * 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * ln(x) * ln(opx) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(opx) * NC * pow(x, -2) * pow(z, -1)
                    + (-1) * ln(x) * ln(opx) * NC * pow(x, -2) * z * pow(opx, -1)
                    + ln(x) * ln(opx) * NC * pow(x, -2) * z
                    + (-1) * 3 * ln(x) * ln(opx) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 3 * ln(x) * ln(opx) * NC * pow(x, -1) * z * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * NC * pow(x, -1) * z
                    + (-1) * 4 * ln(x) * ln(opx) * NC * pow(z, -1) * pow(opx, -1)
                    + ln(x) * ln(opx) * NC * pow(z, -1)
                    + 2 * ln(x) * ln(opx) * NC * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * NC
                    + (-1) * 4 * ln(x) * ln(opx) * NC * z * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +ln(x) * ln(opx) * NC * z
                    + (-1) * 2 * ln(x) * ln(opx) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * NC * x * pow(z, -1)
                    + 2 * ln(x) * ln(opx) * NC * x * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * NC * x * z * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * NC * x * z
                    + (-1) * 2 * ln(x) * ln(opx) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * ln(x) * ln(opx) * NC * pow(x, 2)
                    + (-1) * 2 * ln(x) * ln(opx) * NC * pow(x, 2) * z
                    + 23.0 / 8.0 * ln(z) * pow(NC, -1) * pow(z, -1)
                    + 6 * ln(z) * pow(NC, -1) * pow(z, -1) * rln2 * pow(opz, -1)
                    + (-1) * 5 * ln(z) * pow(NC, -1) * pow(z, -1) * rln2
                    + 4 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 8 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2
                    + 12 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 24 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * ln(z) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + ln(z) * pow(NC, -1)
                    + 4 * ln(z) * pow(NC, -1) * rln2
                    + (-1) * 4 * ln(z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 8 * ln(z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 8 * ln(z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2
                    + 1.0 / 8.0 * ln(z) * pow(NC, -1) * z
                    + (-1) * 2 * ln(z) * pow(NC, -1) * z * rln2
                    + (-1) * 7 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 12 * ln(z) * pow(NC, -1) * x * pow(z, -1) * rln2 * pow(opz, -1)
                    + 10 * ln(z) * pow(NC, -1) * x * pow(z, -1) * rln2
                    + (-1) * 8 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 16 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 16 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2
                    + 0
                )
                tmp += (
                    +(-1) * 40 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + (-1) * 80 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 64 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2
                    + (-1) * 3.0 / 4.0 * ln(z) * pow(NC, -1) * x
                    + (-1) * 8 * ln(z) * pow(NC, -1) * x * rln2
                    + 8 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 16 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2
                    + (-1) * ln(z) * pow(NC, -1) * x * z
                    + 4 * ln(z) * pow(NC, -1) * x * z * rln2
                    + 13.0 / 2.0 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 6 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2 * pow(opz, -1)
                    + (-1) * 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * rln2
                    + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 8 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2
                    + 44 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 40 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 88 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 80 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2
                    + 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(x, 2)
                    + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * rln2
                    + (-1) * 4 * ln(z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 8 * ln(z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 8 * ln(z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2
                    + 0
                )
                tmp += (
                    +ln(z) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 4 * ln(z) * pow(NC, -1) * pow(x, 2) * z * rln2
                    + (-1) * 16 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * 32 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 32 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 5.0 / 32.0 * ln(z) * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 5.0 / 32.0 * ln(z) * NC * pow(x, -1)
                    + 5.0 / 32.0 * ln(z) * NC * pow(z, -2)
                    + (-1) * 63.0 / 16.0 * ln(z) * NC * pow(z, -1)
                    + 2 * ln(z) * NC * pow(z, -1) * rln2
                    + ln(z) * NC * pow(z, -1) * sqrtxz1
                    + (-1) * 33.0 / 16.0 * ln(z) * NC
                    + (-1) * ln(z) * NC * rln2
                    + 1.0 / 32.0 * ln(z) * NC * z
                    + 2 * ln(z) * NC * z * rln2
                    + (-1) * 5.0 / 32.0 * ln(z) * NC * x * pow(z, -2)
                    + 93.0 / 16.0 * ln(z) * NC * x * pow(z, -1)
                    + (-1) * 4 * ln(z) * NC * x * pow(z, -1) * rln2
                    + (-1) * 2 * ln(z) * NC * x * pow(z, -1) * sqrtxz1
                    + (-1) * 7.0 / 16.0 * ln(z) * NC * x
                    + 2 * ln(z) * NC * x * rln2
                    + 27.0 / 32.0 * ln(z) * NC * x * z
                    + (-1) * 4 * ln(z) * NC * x * z * rln2
                    + (-1) * 131.0 / 32.0 * ln(z) * NC * pow(x, 2) * pow(z, -1)
                    + 4 * ln(z) * NC * pow(x, 2) * pow(z, -1) * rln2
                    + 2 * ln(z) * NC * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 61.0 / 32.0 * ln(z) * NC * pow(x, 2)
                    + 2 * ln(z) * NC * pow(x, 2) * rln2
                    + (-1) * ln(z) * NC * pow(x, 2) * z
                    + 4 * ln(z) * NC * pow(x, 2) * z * rln2
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 12 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 40 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 44 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 40 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z
                    + 16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * ln(z) * ln(1 + sqrtxz1 - z) * NC * pow(z, -1)
                    + 0
                )
                tmp += (
                    +ln(z) * ln(1 + sqrtxz1 - z) * NC
                    + (-1) * ln(z) * ln(1 + sqrtxz1 - z) * NC * z
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * z
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * pow(x, 2) * z
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + 3 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 12 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 6 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 40 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 44 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 40 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2)
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * z
                    + 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1)
                    + (-1) * ln(z) * ln(1 + sqrtxz1 + z) * NC * z
                    + 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * pow(z, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * z
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(x, 2) * z
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z
                    + (-1) * 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1)
                    + 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z
                    + (-1) * 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 3 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -2) * z
                    + (-1) * 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, -1) * z
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(z, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(z, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * NC
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * NC * z * pow(opx, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * pow(z, -1)) * NC * z
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * pow(z, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * NC * x * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * z * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * NC * x * z
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * pow(z, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2)
                    + 0
                )
                tmp += (
                    +(-1) * ln(z) * ln(1 + x * pow(z, -1)) * NC * pow(x, 2) * z
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z
                    + 3 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 3.0 / 2.0 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z
                    + 3 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x
                    + (-1) * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * z * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * z) * NC * pow(x, -2) * pow(z, -1)
                    + 1.0 / 2.0 * ln(z) * ln(1 + x * z) * NC * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(1 + x * z) * NC * pow(x, -2) * z
                    + 3.0 / 2.0 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * pow(z, -1)
                    + 3.0 / 2.0 * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * NC * pow(x, -1) * z
                    + 2 * ln(z) * ln(1 + x * z) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * NC * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * NC
                    + 2 * ln(z) * ln(1 + x * z) * NC * z * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * NC * x * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * NC * x * z * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * ln(z) * ln(1 + x * z) * NC * pow(x, 2) * z
                    + ln(z) * ln(z + x) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + (-1) * ln(z) * ln(z + x) * pow(NC, -1) * pow(z, -1)
                    + 1.0 / 2.0 * ln(z) * ln(z + x) * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * ln(z + x) * pow(NC, -1) * z
                    + (-1) * 2 * ln(z) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(z) * ln(z + x) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * ln(z) * ln(z + x) * pow(NC, -1) * x
                    + ln(z) * ln(z + x) * pow(NC, -1) * x * z
                    + ln(z) * ln(z + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + (-1) * ln(z) * ln(z + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(z) * ln(z + x) * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * ln(z) * ln(z + x) * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(z) * ln(z + x) * NC * z
                    + (-1) * ln(z) * ln(z + x) * NC * x * pow(z, -1)
                    + (-1) * ln(z) * ln(z + x) * NC * x * z
                    + ln(z) * ln(z + x) * NC * pow(x, 2) * pow(z, -1)
                    + ln(z) * ln(z + x) * NC * pow(x, 2)
                    + ln(z) * ln(z + x) * NC * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + (-1) * 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2)
                    + 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * z
                    + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + 3.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1)
                    + 3.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z
                    + 0
                )
                tmp += (
                    +(-1) * 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 15.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 5 * pow(ln(z), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + pow(ln(z), 2) * pow(NC, -1) * z * pow(opx, -1)
                    + 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * z
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 5 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 5 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 25 * pow(ln(z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 20 * pow(ln(z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + (-1) * pow(ln(z), 2) * pow(NC, -1) * x * pow(omz, -1)
                    + 5 * pow(ln(z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 5 * pow(ln(z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * z
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 55.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 25 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                    + pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 10 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 10 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 4.0 * pow(ln(z), 2) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 1.0 / 4.0 * pow(ln(z), 2) * NC * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 4.0 * pow(ln(z), 2) * NC * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 4.0 * pow(ln(z), 2) * NC * pow(x, -2) * z
                    + (-1) * 3.0 / 4.0 * pow(ln(z), 2) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 4.0 * pow(ln(z), 2) * NC * pow(x, -1) * z * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, -1) * z
                    + (-1) * pow(ln(z), 2) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(z, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * NC
                    + (-1) * pow(ln(z), 2) * NC * z * pow(opx, -1)
                    + (-1) * 1.0 / 4.0 * pow(ln(z), 2) * NC * z
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(z, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +pow(ln(z), 2) * NC * x * pow(z, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * NC * x * z * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * NC * x * z
                    + (-1) * 2 * pow(ln(z), 2) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * z
                    + ln(z) * ln(omx) * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * pow(NC, -1) * x
                    + 2 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                    + (-1) * ln(z) * ln(omx) * NC
                    + 2 * ln(z) * ln(omx) * NC * x
                    + (-1) * 2 * ln(z) * ln(omx) * NC * pow(x, 2)
                    + 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 6 * ln(z) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(omz) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 20 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * ln(z) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 22 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 8 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 15.0 / 8.0 * ln(omx) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 7.0 / 4.0 * ln(omx) * pow(NC, -1)
                    + 3.0 / 8.0 * ln(omx) * pow(NC, -1) * z
                    + (-1) * 5 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                    + 4 * ln(omx) * pow(NC, -1) * x
                    + (-1) * 1.0 / 4.0 * ln(omx) * pow(NC, -1) * x * z
                    + 9.0 / 2.0 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 7.0 / 2.0 * ln(omx) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(omx) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 15.0 / 8.0 * ln(omx) * NC * pow(z, -1)
                    + 7.0 / 4.0 * ln(omx) * NC
                    + (-1) * 3.0 / 8.0 * ln(omx) * NC * z
                    + 5 * ln(omx) * NC * x * pow(z, -1)
                    + (-1) * 4 * ln(omx) * NC * x
                    + 1.0 / 4.0 * ln(omx) * NC * x * z
                    + (-1) * 9.0 / 2.0 * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                    + 7.0 / 2.0 * ln(omx) * NC * pow(x, 2)
                    + 1.0 / 2.0 * ln(omx) * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1)
                    + 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1)
                    + (-1) * 1.0 / 4.0 * pow(ln(omx), 2) * pow(NC, -1) * z
                    + pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * pow(ln(omx), 2) * pow(NC, -1) * x
                    + 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * z
                    + (-1) * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * NC
                    + 1.0 / 4.0 * pow(ln(omx), 2) * NC * z
                    + (-1) * pow(ln(omx), 2) * NC * x * pow(z, -1)
                    + pow(ln(omx), 2) * NC * x
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * z
                    + pow(ln(omx), 2) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * pow(ln(omx), 2) * NC * pow(x, 2)
                    + 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * z
                    + (-1) * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1)
                    + ln(omx) * ln(omz) * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1) * z
                    + 2 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 2 * ln(omx) * ln(omz) * pow(NC, -1) * x
                    + ln(omx) * ln(omz) * pow(NC, -1) * x * z
                    + (-1) * 2 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                    + 0
                )
                tmp += (
                    +(-1) * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                    + ln(omx) * ln(omz) * NC * pow(z, -1)
                    + (-1) * ln(omx) * ln(omz) * NC
                    + 1.0 / 2.0 * ln(omx) * ln(omz) * NC * z
                    + (-1) * 2 * ln(omx) * ln(omz) * NC * x * pow(z, -1)
                    + 2 * ln(omx) * ln(omz) * NC * x
                    + (-1) * ln(omx) * ln(omz) * NC * x * z
                    + 2 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * ln(omx) * ln(omz) * NC * pow(x, 2)
                    + ln(omx) * ln(omz) * NC * pow(x, 2) * z
                    + 15.0 / 8.0 * ln(omz) * pow(NC, -1) * pow(z, -1)
                    + 4 * ln(omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2
                    + 12 * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 7.0 / 4.0 * ln(omz) * pow(NC, -1)
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 4 * ln(omz) * pow(NC, -1) * z * pow(sqrtxz1, -1) * rln2
                    + 3.0 / 8.0 * ln(omz) * pow(NC, -1) * z
                    + (-1) * 5 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 8 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2
                    + (-1) * 40 * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 32 * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2
                    + 4 * ln(omz) * pow(NC, -1) * x
                    + 8 * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2
                    + (-1) * 1.0 / 4.0 * ln(omz) * pow(NC, -1) * x * z
                    + 9.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * rln2
                    + 44 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 40 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 7.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * rln2
                    + (-1) * 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 16 * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 16 * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 15.0 / 8.0 * ln(omz) * NC * pow(z, -1)
                    + 7.0 / 4.0 * ln(omz) * NC
                    + (-1) * 3.0 / 8.0 * ln(omz) * NC * z
                    + 5 * ln(omz) * NC * x * pow(z, -1)
                    + (-1) * 4 * ln(omz) * NC * x
                    + 1.0 / 4.0 * ln(omz) * NC * x * z
                    + (-1) * 9.0 / 2.0 * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                    + 7.0 / 2.0 * ln(omz) * NC * pow(x, 2)
                    + 1.0 / 2.0 * ln(omz) * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 12 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 40 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + (-1) * 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 0
                )
                tmp += (
                    +(-1) * 44 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 40 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 6 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 20 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 22 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 20 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1)
                    + 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 6 * pow(ln(omz), 2) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * pow(ln(omz), 2) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * z
                    + pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 20 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * pow(ln(omz), 2) * pow(NC, -1) * x
                    + 4 * pow(ln(omz), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * z
                    + (-1) * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 22 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                    + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 8 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * NC * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * NC
                    + 1.0 / 4.0 * pow(ln(omz), 2) * NC * z
                    + (-1) * pow(ln(omz), 2) * NC * x * pow(z, -1)
                    + pow(ln(omz), 2) * NC * x
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * NC * x * z
                    + pow(ln(omz), 2) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * pow(ln(omz), 2) * NC * pow(x, 2)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2) * z
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 0
                )
                tmp += (
                    +6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 0
                )
                tmp += (
                    +22 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(x, 2)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1)
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 20 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 22 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + (-1) * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(x, 2)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * z
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * z
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 22 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * pow(z, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * z
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * pow(z, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * z
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * pow(x, 2) * z
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + (-1) * 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * z
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 0
                )
                tmp += (
                    +20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * z
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + (-1) * 22 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 20 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 2) * z
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * pow(z, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * z
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * pow(z, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * z
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * pow(x, 2) * z
                    + 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 12 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 40 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 44 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 40 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 12 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + (-1) * 40 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 44 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 40 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2)
                    + (-1) * 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z
                    + 3 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 3.0 / 2.0 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z
                    + 3 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 3 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z * pow(opx, -1)
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * z
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z
                    + Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * Li2(-x * pow(z, -1)) * NC * pow(x, -2) * pow(z, -1)
                    + 1.0 / 2.0 * Li2(-x * pow(z, -1)) * NC * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * Li2(-x * pow(z, -1)) * NC * pow(x, -2) * z
                    + 3.0 / 2.0 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * pow(z, -1)
                    + 3.0 / 2.0 * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * NC * pow(x, -1) * z
                    + 2 * Li2(-x * pow(z, -1)) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * NC * pow(z, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * NC * pow(opx, -1)
                    + Li2(-x * pow(z, -1)) * NC
                    + 0
                )
                tmp += (
                    +2 * Li2(-x * pow(z, -1)) * NC * z * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * NC * z
                    + Li2(-x * pow(z, -1)) * NC * x * pow(z, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * NC * x * pow(z, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * NC * x * pow(opx, -1)
                    + Li2(-x * pow(z, -1)) * NC * x * z * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * NC * x * z
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * NC * pow(x, 2)
                    + (-1) * 2 * Li2(-x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + Li2(-x) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + (-1) * Li2(-x) * pow(NC, -1) * pow(x, -2)
                    + Li2(-x) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * Li2(-x) * pow(NC, -1) * pow(x, -2) * z
                    + (-1) * 6 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 4 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + 6 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + 3 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * pow(NC, -1) * pow(x, -1)
                    + 3 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z
                    + (-1) * 6 * Li2(-x) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 6 * Li2(-x) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * pow(opx, -1)
                    + Li2(-x) * pow(NC, -1)
                    + 4 * Li2(-x) * pow(NC, -1) * z * pow(opx, -1)
                    + (-1) * Li2(-x) * pow(NC, -1) * z
                    + (-1) * 2 * Li2(-x) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * Li2(-x) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + 4 * Li2(-x) * pow(NC, -1) * x * pow(z, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * x
                    + 2 * Li2(-x) * pow(NC, -1) * x * z * pow(opx, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * x * z
                    + (-1) * 2 * Li2(-x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 2 * Li2(-x) * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * Li2(-x) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + Li2(-x) * NC * pow(x, -2) * pow(z, -1)
                    + (-1) * Li2(-x) * NC * pow(x, -2) * z * pow(opx, -1)
                    + Li2(-x) * NC * pow(x, -2) * z
                    + (-1) * 3 * Li2(-x) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * Li2(-x) * NC * pow(x, -1) * pow(z, -1)
                    + (-1) * 3 * Li2(-x) * NC * pow(x, -1) * z * pow(opx, -1)
                    + 2 * Li2(-x) * NC * pow(x, -1) * z
                    + (-1) * 4 * Li2(-x) * NC * pow(z, -1) * pow(opx, -1)
                    + Li2(-x) * NC * pow(z, -1)
                    + 2 * Li2(-x) * NC * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * NC
                    + (-1) * 4 * Li2(-x) * NC * z * pow(opx, -1)
                    + Li2(-x) * NC * z
                    + (-1) * 2 * Li2(-x) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * NC * x * pow(z, -1)
                    + 2 * Li2(-x) * NC * x * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * NC * x * z * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * NC * x * z
                    + (-1) * 2 * Li2(-x) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * Li2(-x) * NC * pow(x, 2)
                    + (-1) * 2 * Li2(-x) * NC * pow(x, 2) * z
                    + Li2(-x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + Li2(-x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + 1.0 / 2.0 * Li2(-x * z) * pow(NC, -1) * pow(x, -2)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 2.0 * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + 1.0 / 2.0 * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * z
                    + 3 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 3.0 / 2.0 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + Li2(-x * z) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 3.0 / 2.0 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z
                    + 3 * Li2(-x * z) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3 * Li2(-x * z) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + Li2(-x * z) * pow(NC, -1) * pow(z, -1) * pow(opz, -1)
                    + (-1) * Li2(-x * z) * pow(NC, -1) * pow(z, -1)
                    + (-1) * Li2(-x * z) * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(NC, -1) * z * pow(opx, -1)
                    + Li2(-x * z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + (-1) * Li2(-x * z) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(NC, -1) * x * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(NC, -1) * x
                    + (-1) * Li2(-x * z) * pow(NC, -1) * x * z * pow(opx, -1)
                    + Li2(-x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + Li2(-x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * Li2(-x * z) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * Li2(-x * z) * NC * pow(x, -2) * pow(z, -1)
                    + 1.0 / 2.0 * Li2(-x * z) * NC * pow(x, -2) * z * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 2.0 * Li2(-x * z) * NC * pow(x, -2) * z
                    + 3.0 / 2.0 * Li2(-x * z) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * z) * NC * pow(x, -1) * pow(z, -1)
                    + 3.0 / 2.0 * Li2(-x * z) * NC * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * Li2(-x * z) * NC * pow(x, -1) * z
                    + 2 * Li2(-x * z) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * z) * NC * pow(opx, -1)
                    + Li2(-x * z) * NC
                    + 2 * Li2(-x * z) * NC * z * pow(opx, -1)
                    + Li2(-x * z) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * z) * NC * x * pow(opx, -1)
                    + Li2(-x * z) * NC * x * z * pow(opx, -1)
                    + 2 * Li2(-x * z) * NC * pow(x, 2) * pow(z, -1)
                    + 2 * Li2(-x * z) * NC * pow(x, 2) * z
                    + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(z, -1) * sqrtxz1
                    + 6 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * z * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1
                    + 0
                )
                tmp += (
                    +(-1) * 20 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(sqrtxz1, -1)
                    + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1)
                    + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * sqrtxz1
                    + 22 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz1, -1)
                    + (-1) * 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz1, -1)
                    + 2 * Li2(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + 2 * Li2(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1)
                    + (-1) * Li2(x) * pow(NC, -1) * pow(x, -2) * pow(opx, -1)
                    + Li2(x) * pow(NC, -1) * pow(x, -2)
                    + (-1) * Li2(x) * pow(NC, -1) * pow(x, -2) * z * pow(opx, -1)
                    + Li2(x) * pow(NC, -1) * pow(x, -2) * z
                    + 6 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 6 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + 4 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1)
                    + (-1) * 3 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(opx, -1)
                    + 2 * Li2(x) * pow(NC, -1) * pow(x, -1)
                    + (-1) * 3 * Li2(x) * pow(NC, -1) * pow(x, -1) * z * pow(opx, -1)
                    + 2 * Li2(x) * pow(NC, -1) * pow(x, -1) * z
                    + 6 * Li2(x) * pow(NC, -1) * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 6 * Li2(x) * pow(NC, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 4.0 * Li2(x) * pow(NC, -1) * pow(z, -1)
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * Li2(x) * pow(NC, -1)
                    + (-1) * 4 * Li2(x) * pow(NC, -1) * z * pow(opx, -1)
                    + 3.0 / 2.0 * Li2(x) * pow(NC, -1) * z
                    + 2 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1) * pow(opx, -1)
                    + 4 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 7.0 / 2.0 * Li2(x) * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 4 * Li2(x) * pow(NC, -1) * x * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * Li2(x) * pow(NC, -1) * x
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * x * z * pow(opx, -1)
                    + 2 * Li2(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                    + (-1) * 3 * Li2(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                    + Li2(x) * pow(NC, -1) * pow(x, 2)
                    + (-1) * Li2(x) * pow(NC, -1) * pow(x, 2) * z
                    + Li2(x) * NC * pow(x, -2) * pow(z, -1) * pow(opx, -1)
                    + (-1) * Li2(x) * NC * pow(x, -2) * pow(z, -1)
                    + Li2(x) * NC * pow(x, -2) * z * pow(opx, -1)
                    + (-1) * Li2(x) * NC * pow(x, -2) * z
                    + 3 * Li2(x) * NC * pow(x, -1) * pow(z, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(x) * NC * pow(x, -1) * pow(z, -1)
                    + 3 * Li2(x) * NC * pow(x, -1) * z * pow(opx, -1)
                    + (-1) * 2 * Li2(x) * NC * pow(x, -1) * z
                    + 4 * Li2(x) * NC * pow(z, -1) * pow(opx, -1)
                    + (-1) * 7.0 / 4.0 * Li2(x) * NC * pow(z, -1)
                    + (-1) * 2 * Li2(x) * NC * pow(opx, -1)
                    + 3.0 / 2.0 * Li2(x) * NC
                    + 4 * Li2(x) * NC * z * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * Li2(x) * NC * z
                    + 2 * Li2(x) * NC * x * pow(z, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * Li2(x) * NC * x * pow(z, -1)
                    + (-1) * 2 * Li2(x) * NC * x * pow(opx, -1)
                    + Li2(x) * NC * x
                    + 2 * Li2(x) * NC * x * z * pow(opx, -1)
                    + Li2(x) * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * Li2(x) * NC * pow(x, 2)
                    + Li2(x) * NC * pow(x, 2) * z
                    + (-1) * Li2(z) * pow(NC, -1)
                    + 2 * Li2(z) * pow(NC, -1) * x
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * pow(x, 2)
                    + Li2(z) * NC
                    + (-1) * 2 * Li2(z) * NC * x
                    + 2 * Li2(z) * NC * pow(x, 2)
                    + 0
                )
            if "001" == order:
                tmp += (
                    (-1) * 11.0 / 8.0 * LMUA * pow(NC, -1) * pow(z, -1)
                    + 5.0 / 4.0 * LMUA * pow(NC, -1)
                    + 1.0 / 8.0 * LMUA * pow(NC, -1) * z
                    + 15.0 / 4.0 * LMUA * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 7.0 / 2.0 * LMUA * pow(NC, -1) * x
                    + 1.0 / 4.0 * LMUA * pow(NC, -1) * x * z
                    + (-1) * 15.0 / 4.0 * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 7.0 / 2.0 * LMUA * pow(NC, -1) * pow(x, 2)
                    + (-1) * 1.0 / 4.0 * LMUA * pow(NC, -1) * pow(x, 2) * z
                    + 11.0 / 8.0 * LMUA * NC * pow(z, -1)
                    + (-1) * 5.0 / 4.0 * LMUA * NC
                    + (-1) * 1.0 / 8.0 * LMUA * NC * z
                    + (-1) * 15.0 / 4.0 * LMUA * NC * x * pow(z, -1)
                    + 7.0 / 2.0 * LMUA * NC * x
                    + (-1) * 1.0 / 4.0 * LMUA * NC * x * z
                    + 15.0 / 4.0 * LMUA * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 7.0 / 2.0 * LMUA * NC * pow(x, 2)
                    + 1.0 / 4.0 * LMUA * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    (-1) * 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * pow(z, -1)
                    + 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1)
                    + (-1) * 1.0 / 4.0 * ln(x) * LMUA * pow(NC, -1) * z
                    + ln(x) * LMUA * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * ln(x) * LMUA * pow(NC, -1) * x
                    + 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * x * z
                    + (-1) * ln(x) * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + ln(x) * LMUA * pow(NC, -1) * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * ln(x) * LMUA * NC * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * LMUA * NC
                    + 1.0 / 4.0 * ln(x) * LMUA * NC * z
                    + (-1) * ln(x) * LMUA * NC * x * pow(z, -1)
                    + ln(x) * LMUA * NC * x
                    + (-1) * 1.0 / 2.0 * ln(x) * LMUA * NC * x * z
                    + ln(x) * LMUA * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(x) * LMUA * NC * pow(x, 2)
                    + 1.0 / 2.0 * ln(x) * LMUA * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    (-1) * 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1)
                    + (-1) * 1.0 / 4.0 * ln(z) * LMUA * pow(NC, -1) * z
                    + ln(z) * LMUA * pow(NC, -1) * x * pow(z, -1)
                    + ln(z) * LMUA * pow(NC, -1) * x
                    + 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * x * z
                    + (-1) * ln(z) * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(z) * LMUA * pow(NC, -1) * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * ln(z) * LMUA * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(z) * LMUA * NC
                    + 1.0 / 4.0 * ln(z) * LMUA * NC * z
                    + (-1) * ln(z) * LMUA * NC * x * pow(z, -1)
                    + (-1) * ln(z) * LMUA * NC * x
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUA * NC * x * z
                    + ln(z) * LMUA * NC * pow(x, 2) * pow(z, -1)
                    + ln(z) * LMUA * NC * pow(x, 2)
                    + 1.0 / 2.0 * ln(z) * LMUA * NC * pow(x, 2) * z
                    + 0
                )
                tmp += 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * pow(z, -1) + (-1) * 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) + 1.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1) * z + (-1) * ln(omx) * LMUA * pow(NC, -1) * x * pow(z, -1) + 0
                tmp += (
                    ln(omx) * LMUA * pow(NC, -1) * x
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * x * z
                    + ln(omx) * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(omx) * LMUA * pow(NC, -1) * pow(x, 2)
                    + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUA * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(omx) * LMUA * NC
                    + (-1) * 1.0 / 4.0 * ln(omx) * LMUA * NC * z
                    + ln(omx) * LMUA * NC * x * pow(z, -1)
                    + (-1) * ln(omx) * LMUA * NC * x
                    + 1.0 / 2.0 * ln(omx) * LMUA * NC * x * z
                    + (-1) * ln(omx) * LMUA * NC * pow(x, 2) * pow(z, -1)
                    + ln(omx) * LMUA * NC * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUA * NC * pow(x, 2) * z
                    + 0
                )
                tmp += 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * pow(z, -1) + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) + 1.0 / 4.0 * ln(omz) * LMUA * pow(NC, -1) * z + (-1) * ln(omz) * LMUA * pow(NC, -1) * x * pow(z, -1) + ln(omz) * LMUA * pow(NC, -1) * x + 0
                tmp += (
                    (-1) * 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * x * z
                    + ln(omz) * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(omz) * LMUA * pow(NC, -1) * pow(x, 2)
                    + 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(omz) * LMUA * NC
                    + (-1) * 1.0 / 4.0 * ln(omz) * LMUA * NC * z
                    + ln(omz) * LMUA * NC * x * pow(z, -1)
                    + (-1) * ln(omz) * LMUA * NC * x
                    + 1.0 / 2.0 * ln(omz) * LMUA * NC * x * z
                    + (-1) * ln(omz) * LMUA * NC * pow(x, 2) * pow(z, -1)
                    + ln(omz) * LMUA * NC * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * NC * pow(x, 2) * z
                    + 0
                )
            if "010" == order:
                tmp += (
                    (-1) * 1.0 / 2.0 * LMUF * pow(NC, -1) * pow(z, -1)
                    + 1.0 / 2.0 * LMUF * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * LMUF * pow(NC, -1) * z
                    + 5.0 / 4.0 * LMUF * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * LMUF * pow(NC, -1) * x
                    + (-1) * 3.0 / 4.0 * LMUF * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + 3.0 / 4.0 * LMUF * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * LMUF * NC * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * LMUF * NC
                    + 1.0 / 2.0 * LMUF * NC * z
                    + (-1) * 5.0 / 4.0 * LMUF * NC * x * pow(z, -1)
                    + 1.0 / 2.0 * LMUF * NC * x
                    + 3.0 / 4.0 * LMUF * NC * pow(x, 2) * pow(z, -1)
                    + (-1) * 3.0 / 4.0 * LMUF * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    (-1) * 1.0 / 4.0 * ln(x) * LMUF * pow(NC, -1) * pow(z, -1)
                    + (-1) * 1.0 / 4.0 * ln(x) * LMUF * pow(NC, -1) * z
                    + 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * z
                    + (-1) * ln(x) * LMUF * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + ln(x) * LMUF * pow(NC, -1) * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * pow(x, 2) * z
                    + 0
                )
                tmp += 1.0 / 4.0 * ln(x) * LMUF * NC * pow(z, -1) + 1.0 / 4.0 * ln(x) * LMUF * NC * z + (-1) * 1.0 / 2.0 * ln(x) * LMUF * NC * x * pow(z, -1) + 1.0 / 2.0 * ln(x) * LMUF * NC * x * z + ln(x) * LMUF * NC * pow(x, 2) * pow(z, -1) + (-1) * ln(x) * LMUF * NC * pow(x, 2) + 1.0 / 2.0 * ln(x) * LMUF * NC * pow(x, 2) * z + 0
                tmp += (
                    1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1)
                    + 1.0 / 4.0 * ln(z) * LMUF * pow(NC, -1) * z
                    + (-1) * ln(z) * LMUF * pow(NC, -1) * x * pow(z, -1)
                    + ln(z) * LMUF * pow(NC, -1) * x
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * x * z
                    + ln(z) * LMUF * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(z) * LMUF * pow(NC, -1) * pow(x, 2)
                    + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUF * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(z) * LMUF * NC
                    + (-1) * 1.0 / 4.0 * ln(z) * LMUF * NC * z
                    + 0
                )
                tmp += ln(z) * LMUF * NC * x * pow(z, -1) + (-1) * ln(z) * LMUF * NC * x + 1.0 / 2.0 * ln(z) * LMUF * NC * x * z + (-1) * ln(z) * LMUF * NC * pow(x, 2) * pow(z, -1) + ln(z) * LMUF * NC * pow(x, 2) + (-1) * 1.0 / 2.0 * ln(z) * LMUF * NC * pow(x, 2) * z + 0
                tmp += (
                    1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1)
                    + 1.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1) * z
                    + (-1) * ln(omx) * LMUF * pow(NC, -1) * x * pow(z, -1)
                    + ln(omx) * LMUF * pow(NC, -1) * x
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * x * z
                    + ln(omx) * LMUF * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(omx) * LMUF * pow(NC, -1) * pow(x, 2)
                    + 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUF * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(omx) * LMUF * NC
                    + (-1) * 1.0 / 4.0 * ln(omx) * LMUF * NC * z
                    + ln(omx) * LMUF * NC * x * pow(z, -1)
                    + (-1) * ln(omx) * LMUF * NC * x
                    + 1.0 / 2.0 * ln(omx) * LMUF * NC * x * z
                    + (-1) * ln(omx) * LMUF * NC * pow(x, 2) * pow(z, -1)
                    + ln(omx) * LMUF * NC * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUF * NC * pow(x, 2) * z
                    + 0
                )
                tmp += (
                    1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1)
                    + 1.0 / 4.0 * ln(omz) * LMUF * pow(NC, -1) * z
                    + (-1) * ln(omz) * LMUF * pow(NC, -1) * x * pow(z, -1)
                    + ln(omz) * LMUF * pow(NC, -1) * x
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * x * z
                    + ln(omz) * LMUF * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + (-1) * ln(omz) * LMUF * pow(NC, -1) * pow(x, 2)
                    + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * pow(x, 2) * z
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUF * NC * pow(z, -1)
                    + 1.0 / 2.0 * ln(omz) * LMUF * NC
                    + (-1) * 1.0 / 4.0 * ln(omz) * LMUF * NC * z
                    + ln(omz) * LMUF * NC * x * pow(z, -1)
                    + (-1) * ln(omz) * LMUF * NC * x
                    + 1.0 / 2.0 * ln(omz) * LMUF * NC * x * z
                    + (-1) * ln(omz) * LMUF * NC * pow(x, 2) * pow(z, -1)
                    + ln(omz) * LMUF * NC * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUF * NC * pow(x, 2) * z
                    + 0
                )
            if "011" == order:
                tmp += (
                    (-1) * 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * pow(z, -1)
                    + 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1)
                    + (-1) * 1.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * z
                    + LMUA * LMUF * pow(NC, -1) * x * pow(z, -1)
                    + (-1) * LMUA * LMUF * pow(NC, -1) * x
                    + 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * x * z
                    + (-1) * LMUA * LMUF * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                    + LMUA * LMUF * pow(NC, -1) * pow(x, 2)
                    + (-1) * 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * pow(x, 2) * z
                    + 1.0 / 2.0 * LMUA * LMUF * NC * pow(z, -1)
                    + (-1) * 1.0 / 2.0 * LMUA * LMUF * NC
                    + 1.0 / 4.0 * LMUA * LMUF * NC * z
                    + (-1) * LMUA * LMUF * NC * x * pow(z, -1)
                    + 0
                )
                tmp += LMUA * LMUF * NC * x + (-1) * 1.0 / 2.0 * LMUA * LMUF * NC * x * z + LMUA * LMUF * NC * pow(x, 2) * pow(z, -1) + (-1) * LMUA * LMUF * NC * pow(x, 2) + 1.0 / 2.0 * LMUA * LMUF * NC * pow(x, 2) * z + 0
            res += tmp

        return res


def C2Tg2gEq(x, z, rsl, order, f=C2Tg2gEq_DR0123_scheme):
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
