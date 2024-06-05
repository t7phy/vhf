from core.definitions import CF, NC, TR, NF, ZETA3, ZETA2
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi


def C2Pq2qpEqp(inx, inz, cx, cz, Q, muR, muF, muA, orders: list, ndecimals):
    res = 0.0

    rln2 = ln(2.0)

    LMUR = 2 * ln(muR / Q)
    LMUF = 2 * ln(muF / Q)
    LMUA = 2 * ln(muA / Q)

    NC = 3.0
    CF = 4.0 / 3.0
    TR = 0.5

    if cx == "D" and cz == "D":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "D" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "D" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "D" and cz == "2":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "D" and cz == "3":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "0" and cz == "D":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "0" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "0" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "0" and cz == "2":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "0" and cz == "3":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "1" and cz == "D":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "1" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "1" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "1" and cz == "2":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "1" and cz == "3":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "2" and cz == "D":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "2" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "2" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "2" and cz == "2":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "2" and cz == "3":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "3" and cz == "D":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "3" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "3" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "3" and cz == "2":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "3" and cz == "3":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "D" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "3" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "R" and cz == "D":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += (
                9 * CF
                + (-1) * 9 * x * CF
                + (-1) * 1.0 / 2.0 * pow(pi, 2) * CF
                + 1.0 / 2.0 * pow(pi, 2) * x * CF
                + 25.0 / 4.0 * ln(x) * CF
                + (-1) * 3.0 / 4.0 * ln(x) * x * CF
                + (-1) * 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF
                + (-1) * 1.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF
                + 17.0 / 8.0 * pow(ln(x), 2) * CF
                + (-1) * 15.0 / 8.0 * pow(ln(x), 2) * x * CF
                + 5.0 / 12.0 * pow(ln(x), 3) * CF
                + 5.0 / 12.0 * pow(ln(x), 3) * x * CF
                + (-1) * 5.0 / 2.0 * ln(x) * ln(omx) * CF
                + 5.0 / 2.0 * ln(x) * ln(omx) * x * CF
                + (-1) * 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF
                + (-1) * 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF
                + ln(x) * Li2(x) * CF
                + ln(x) * Li2(x) * x * CF
                + (-1) * 3 * ln(omx) * CF
                + 3 * ln(omx) * x * CF
                + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * CF
                + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * x * CF
                + 5.0 / 4.0 * pow(ln(omx), 2) * CF
                + (-1) * 5.0 / 4.0 * pow(ln(omx), 2) * x * CF
                + (-1) * ln(omx) * Li2(1 - x) * CF
                + (-1) * ln(omx) * Li2(1 - x) * x * CF
                + (-1) * 2 * ln(omx) * Li2(x) * CF
                + (-1) * 2 * ln(omx) * Li2(x) * x * CF
                + (-1) * Li3(1 - x) * CF
                + (-1) * Li3(1 - x) * x * CF
                + 1.0 / 2.0 * Li2(x) * CF
                + (-1) * 1.0 / 2.0 * Li2(x) * x * CF
                + 0
            )
        if ("010" in orders) or ("all" in orders):
            res += 3 * LMUF * CF + (-1) * 3 * x * LMUF * CF + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUF * CF + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * LMUF * CF + 3 * ln(x) * LMUF * CF + (-1) * 3 * ln(x) * x * LMUF * CF + pow(ln(x), 2) * LMUF * CF + pow(ln(x), 2) * x * LMUF * CF + (-1) * 5.0 / 2.0 * ln(omx) * LMUF * CF + 5.0 / 2.0 * ln(omx) * x * LMUF * CF + Li2(x) * LMUF * CF + Li2(x) * x * LMUF * CF + 0
        if ("020" in orders) or ("all" in orders):
            res += 5.0 / 4.0 * pow(LMUF, 2) * CF + (-1) * 5.0 / 4.0 * x * pow(LMUF, 2) * CF + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * CF + 1.0 / 2.0 * ln(x) * x * pow(LMUF, 2) * CF + 0
        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += +(-1) * 3 * CF + 3 * x * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 1.0 / 6.0 * pow(pi, 2) * x * CF + (-1) * 3 * ln(x) * CF + 3 * ln(x) * x * CF + (-1) * pow(ln(x), 2) * CF + (-1) * pow(ln(x), 2) * x * CF + 5.0 / 2.0 * ln(omx) * CF + (-1) * 5.0 / 2.0 * ln(omx) * x * CF + (-1) * Li2(x) * CF + (-1) * Li2(x) * x * CF + 0
        if ("010" in orders) or ("all" in orders):
            res += (-1) * 5.0 / 2.0 * LMUF * CF + 5.0 / 2.0 * x * LMUF * CF + (-1) * ln(x) * LMUF * CF + (-1) * ln(x) * x * LMUF * CF + 0
        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 5.0 / 2.0 * CF + (-1) * 5.0 / 2.0 * x * CF + ln(x) * CF + ln(x) * x * CF + 0
        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "R" and cz == "3":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
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
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) != round(x, ndecimals) and round(z, ndecimals) != round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += (
                    +(-1) * 3 * pow(z, -1) * CF
                    + 10 * CF
                    + 3 * x * pow(z, -1) * CF
                    + (-1) * 10 * x * CF
                    + 1.0 / 6.0 * pow(pi, 2) * pow(z, -1) * CF
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * CF
                    + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * x * CF
                    + (-1) * 3 * ln(x) * pow(z, -1) * CF
                    + 1.0 / 2.0 * ln(x) * CF * pow(poly2, -1)
                    + 8 * ln(x) * CF
                    + 3 * ln(x) * x * pow(z, -1) * CF
                    + (-1) * 1.0 / 2.0 * ln(x) * x * CF * pow(poly2, -1)
                    + (-1) * 4 * ln(x) * x * CF
                    + (-1) * 1.0 / 2.0 * ln(x) * pow(x, 2) * CF * pow(poly2, -1)
                    + 1.0 / 2.0 * ln(x) * pow(x, 3) * CF * pow(poly2, -1)
                    + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 7.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                    + (-1) * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 7.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 7.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                    + ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 7.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 0
                )
                tmp += (
                    +(-1) * pow(ln(x), 2) * pow(z, -1) * CF
                    + 2 * pow(ln(x), 2) * CF
                    + (-1) * pow(ln(x), 2) * x * pow(z, -1) * CF
                    + 2 * pow(ln(x), 2) * x * CF
                    + ln(x) * ln(z) * pow(z, -1) * CF
                    + (-1) * ln(x) * ln(z) * CF
                    + ln(x) * ln(z) * x * pow(z, -1) * CF
                    + (-1) * ln(x) * ln(z) * x * CF
                    + ln(x) * ln(omz) * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * ln(omz) * CF
                    + ln(x) * ln(omz) * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * ln(omz) * x * CF
                    + 5.0 / 2.0 * ln(z) * pow(z, -1) * CF
                    + 1.0 / 2.0 * ln(z) * CF * pow(poly2, -1)
                    + ln(z) * CF * pow(omz, -1)
                    + (-1) * 2 * ln(z) * CF
                    + (-1) * 5.0 / 2.0 * ln(z) * x * pow(z, -1) * CF
                    + 1.0 / 2.0 * ln(z) * x * CF * pow(poly2, -1)
                    + (-1) * ln(z) * x * CF * pow(omz, -1)
                    + 2 * ln(z) * x * CF
                    + (-1) * 1.0 / 2.0 * ln(z) * pow(x, 2) * CF * pow(poly2, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * pow(x, 3) * CF * pow(poly2, -1)
                    + 5.0 / 2.0 * ln(omx) * pow(z, -1) * CF
                    + (-1) * 5 * ln(omx) * CF
                    + (-1) * 5.0 / 2.0 * ln(omx) * x * pow(z, -1) * CF
                    + 5 * ln(omx) * x * CF
                    + 5.0 / 2.0 * ln(omz) * pow(z, -1) * CF
                    + (-1) * 5 * ln(omz) * CF
                    + (-1) * 5.0 / 2.0 * ln(omz) * x * pow(z, -1) * CF
                    + 5 * ln(omz) * x * CF
                    + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 7.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                    + 0
                )
                tmp += (
                    +(-1) * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 7.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * Li2(x) * pow(z, -1) * CF
                    + 2 * Li2(x) * CF
                    + (-1) * Li2(x) * x * pow(z, -1) * CF
                    + 2 * Li2(x) * x * CF
                    + 0
                )
            if ("010" in orders) or ("all" in orders):
                tmp += (-1) * 5.0 / 2.0 * pow(z, -1) * LMUF * CF + 5 * LMUF * CF + 5.0 / 2.0 * x * pow(z, -1) * LMUF * CF + (-1) * 5 * x * LMUF * CF + (-1) * ln(x) * pow(z, -1) * LMUF * CF + 2 * ln(x) * LMUF * CF + (-1) * ln(x) * x * pow(z, -1) * LMUF * CF + 2 * ln(x) * x * LMUF * CF + 0
            res += tmp

        return res
