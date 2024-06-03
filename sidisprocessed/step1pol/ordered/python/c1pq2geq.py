from core.definitions import CF, NC, TR, NF, ZETA3, ZETA2
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi


def C1Pq2gEq(inx, inz, cx, cz, Q, muR, muF, muA, orders: list, ndecimals):
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
            res += +z * CF + 2 * ln(z) * pow(z, -1) * CF + (-1) * 2 * ln(z) * CF + ln(z) * z * CF + 2 * ln(omz) * pow(z, -1) * CF + (-1) * 2 * ln(omz) * CF + ln(omz) * z * CF + 0
        if ("001" in orders) or ("all" in orders):
            res += (-1) * 2 * pow(z, -1) * LMUA * CF + 2 * LMUA * CF + (-1) * z * LMUA * CF + 0
        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 2 * pow(z, -1) * CF + (-1) * 2 * CF + z * CF + 0
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
            res += 0 + 0
        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 0 + 0
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
                tmp += +(-1) * pow(z, -1) * CF + 2 * CF + (-1) * 2 * z * CF + (-1) * x * pow(z, -1) * CF + 2 * x * CF + 0
            res += tmp

        return res
