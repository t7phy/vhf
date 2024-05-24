from core.definitions import CF, NC, TR, NF, ZETA3, ZETA2
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi


def C1Pq2qEq(inx, inz, cx, cz, Q, muR, muF, muA, order):
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
        if (order == "000") or (order == "all"):

            res += +(-1) * 8 * CF + 0
        if (order == "010") or (order == "all"):

            res += (-1) * 3.0 / 2.0 * LMUF * CF + 0
        if (order == "001") or (order == "all"):

            res += (-1) * 3.0 / 2.0 * LMUA * CF + 0

        return res

    if cx == "D" and cz == "0":

        # Split orders:
        res = 0
        if (order == "000") or (order == "all"):

            res += +0
        if (order == "001") or (order == "all"):

            res += (-1) * 2 * LMUA * CF + 0

        return res

    if cx == "D" and cz == "1":

        res = 2 * CF

        return res

    if cx == "D" and cz == "2":

        res = 0

        return res

    if cx == "D" and cz == "3":

        res = 0

        return res

    if cx == "0" and cz == "D":

        # Split orders:
        res = 0
        if (order == "000") or (order == "all"):

            res += +0
        if (order == "010") or (order == "all"):

            res += (-1) * 2 * LMUF * CF + 0

        return res

    if cx == "0" and cz == "0":

        res = 2 * CF

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

        res = 2 * CF

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
        # Split orders:
        res = 0
        if (order == "000") or (order == "all"):

            res += CF + (-1) * z * CF + 2 * ln(z) * CF * pow(omz, +(-1) * 1) + (-1) * ln(z) * CF + (-1) * ln(z) * z * CF + (-1) * ln(omz) * CF + (-1) * ln(omz) * z * CF + 0
        if (order == "001") or (order == "all"):

            res += LMUA * CF + z * LMUA * CF + 0

        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = -CF - z * CF

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
        # Split orders:
        res = 0
        if (order == "000") or (order == "all"):

            res += CF + (-1) * x * CF + (-1) * 2 * ln(x) * CF * pow(omx, +(-1) * 1) + ln(x) * CF + ln(x) * x * CF + (-1) * ln(omx) * CF + (-1) * ln(omx) * x * CF + 0
        if (order == "010") or (order == "all"):

            res += LMUF * CF + x * LMUF * CF + 0

        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = -CF - x * CF

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
        if z < 1.0 - x and z < x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z > 1.0 - x and z < x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z < 1.0 - x and z > x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z > 1.0 - x and z > x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z > x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z < x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z < 1.0 - x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z > 1.0 - x:

            tmp = 0.0
            tmp = 0

            res += tmp

        if z != x and z != 1.0 - x:

            tmp = 0.0
            tmp = 2 * z * CF + 2 * x * CF

            res += tmp

        return res
