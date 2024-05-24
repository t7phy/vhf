from core.definitions import CF, NC, TR, NF, ZETA3, ZETA2
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi


def C2Pq2qpbEs(inx, inz, cx, cz, Q, muR, muF, muA, order):
    res = 0.0

    rln2 = ln(2.0)

    LMUR = 2 * ln(muR / Q)
    LMUF = 2 * ln(muF / Q)
    LMUA = 2 * ln(muA / Q)

    NC = 3.0
    CF = 4.0 / 3.0
    TR = 0.5

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
            tmp = (
                -5 * CF
                - 6 * CF * pow(rln2, 2) * pow(omx, -1)
                + 4 * CF * pow(rln2, 2)
                - 6 * CF * sqrtxz1 * rln2 * pow(omx, -1)
                + 4 * CF * sqrtxz1 * rln2
                + 4 * z * CF
                - 4 * z * CF * pow(rln2, 2) * pow(omx, -1)
                - 16 * pow(z, 2) * CF * pow(rln2, 2) * pow(omx, -1)
                + 16 * pow(z, 2) * CF * pow(rln2, 2)
                + 8 * x * z * CF * pow(rln2, 2)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(opx, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF
                - 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF
                - 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF
                - 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF
                + 5.0 / 6.0 * pow(pi, 2) * CF * pow(omx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * CF * pow(opx, -1)
                - 1.0 / 3.0 * pow(pi, 2) * CF
                - 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(omx, -1)
                + 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(opx, -1)
                + 2.0 / 3.0 * pow(pi, 2) * z * CF
                + 2 * pow(pi, 2) * pow(z, 2) * CF * pow(omx, -1)
                - 2 * pow(pi, 2) * pow(z, 2) * CF * pow(opx, -1)
                - 4.0 / 3.0 * pow(pi, 2) * pow(z, 2) * CF
                + 1.0 / 3.0 * pow(pi, 2) * x * CF
                - 2.0 / 3.0 * pow(pi, 2) * x * z * CF
                + 8 * ln(1 + sqrtxz1 - z) * CF * rln2 * pow(omx, -1)
                - 6 * ln(1 + sqrtxz1 - z) * CF * rln2
                + 6 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1
                + 4 * ln(1 + sqrtxz1 - z) * z * CF * rln2
                + 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                - 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2
                + 2 * ln(1 + sqrtxz1 - z) * x * CF * rln2
                - 12 * ln(1 + sqrtxz1 - z) * x * z * CF * rln2
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(omx, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(omx, -1)
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF
            )
            tmp += (
                -8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * CF
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF
                + 4 * ln(1 + sqrtxz1 + z) * CF * rln2 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 + z) * CF * rln2
                + 8 * ln(1 + sqrtxz1 + z) * z * CF * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 + z) * z * CF * rln2
                + 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                - 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2
                - 2 * ln(1 + sqrtxz1 + z) * x * CF * rln2
                - 4 * ln(1 + sqrtxz1 + z) * x * z * CF * rln2
                + 8 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * sqrtxz3
                + 4 * ln(x) * pow(x, -2) * CF * pow(opx, -1)
                - 4 * ln(x) * pow(x, -2) * CF
                - 8 * ln(x) * pow(x, -2) * z * CF * pow(opx, -1)
                + 8 * ln(x) * pow(x, -2) * z * CF
                + 4 * ln(x) * pow(x, -1) * CF
                - 8 * ln(x) * pow(x, -1) * z * CF
                - 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF
                + 1.0 / 2.0 * ln(x) * CF * pow(poly2, -1)
                + 2 * ln(x) * CF * pow(omx, -1)
                - 4 * ln(x) * CF * pow(opx, -1)
                - 3.0 / 2.0 * ln(x) * CF
                - 5 * ln(x) * CF * rln2 * pow(omx, -1)
                + 4 * ln(x) * CF * rln2
            )
            tmp += (
                -3 * ln(x) * CF * sqrtxz1 * pow(omx, -1)
                + 2 * ln(x) * CF * sqrtxz1
                - 3 * ln(x) * z * CF * pow(omx, -1)
                + 8 * ln(x) * z * CF * pow(opx, -1)
                + 2 * ln(x) * z * CF
                + 2 * ln(x) * z * CF * rln2 * pow(omx, -1)
                - 4 * ln(x) * z * CF * rln2
                - 16 * ln(x) * pow(z, 2) * CF * pow(opx, -1)
                - 16 * ln(x) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                + 16 * ln(x) * pow(z, 2) * CF * rln2
                - 1.0 / 2.0 * ln(x) * x * CF * pow(poly2, -1)
                + ln(x) * x * CF * pow(xmz, -1)
                + 3.0 / 2.0 * ln(x) * x * CF
                - 2 * ln(x) * x * CF * rln2
                + 8 * ln(x) * x * z * CF * rln2
                - 1.0 / 2.0 * ln(x) * pow(x, 2) * CF * pow(poly2, -1)
                - 2 * ln(x) * pow(x, 2) * CF * pow(xmz, -1)
                + 1.0 / 2.0 * ln(x) * pow(x, 3) * CF * pow(poly2, -1)
                + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                + 5.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                - 5 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                - 5.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                + 5 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +2 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * CF
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF
                + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * CF
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF
                + 3 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                - 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF
                + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * x * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF
                - 4 * ln(x) * ln(1 + x) * CF * pow(opx, -1)
                + 6 * ln(x) * ln(1 + x) * CF
                + 8 * ln(x) * ln(1 + x) * z * CF * pow(opx, -1)
                - 12 * ln(x) * ln(1 + x) * z * CF
                - 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF * pow(opx, -1)
            )
            tmp += (
                +8 * ln(x) * ln(1 + x) * pow(z, 2) * CF
                + 2 * ln(x) * ln(1 + x) * x * CF
                - 4 * ln(x) * ln(1 + x) * x * z * CF
                - ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * pow(x, -2) * CF
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF
                - ln(x) * ln(1 + x * z) * pow(x, -1) * CF
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF
                + 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                - 2 * ln(x) * ln(1 + x * z) * CF * pow(omx, -1)
                - ln(x) * ln(1 + x * z) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * CF
                - 4 * ln(x) * ln(1 + x * z) * z * CF * pow(omx, -1)
                + 2 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF
                + 4 * ln(x) * ln(1 + x * z) * x * z * CF
                + 2 * ln(x) * ln(z + x) * CF * pow(omx, -1)
                - ln(x) * ln(z + x) * CF
                + 4 * ln(x) * ln(z + x) * z * CF * pow(omx, -1)
                - 2 * ln(x) * ln(z + x) * z * CF
                + 4 * ln(x) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * ln(x) * ln(z + x) * pow(z, 2) * CF
                - ln(x) * ln(z + x) * x * CF
                - 2 * ln(x) * ln(z + x) * x * z * CF
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF
                + 3 * pow(ln(x), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                - 3 * pow(ln(x), 2) * pow(x, -2) * z * CF
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * CF
                + 3 * pow(ln(x), 2) * pow(x, -1) * z * CF
                + 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF
                + 2 * pow(ln(x), 2) * CF * pow(omx, -1)
                + 5.0 / 2.0 * pow(ln(x), 2) * CF * pow(opx, -1)
                - 3 * pow(ln(x), 2) * CF
                - 4 * pow(ln(x), 2) * z * CF * pow(omx, -1)
            )
            tmp += (
                -5 * pow(ln(x), 2) * z * CF * pow(opx, -1)
                + 6 * pow(ln(x), 2) * z * CF
                + 2 * pow(ln(x), 2) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * pow(ln(x), 2) * pow(z, 2) * CF
                - 2 * pow(ln(x), 2) * x * CF
                + 4 * pow(ln(x), 2) * x * z * CF
                + ln(x) * ln(z) * pow(x, -2) * CF * pow(opx, -1)
                - ln(x) * ln(z) * pow(x, -2) * CF
                - 2 * ln(x) * ln(z) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(z) * pow(x, -2) * z * CF
                + ln(x) * ln(z) * pow(x, -1) * CF
                - 2 * ln(x) * ln(z) * pow(x, -1) * z * CF
                - 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF
                - 4 * ln(x) * ln(z) * CF * pow(omx, -1)
                + ln(x) * ln(z) * CF * pow(opx, -1)
                + ln(x) * ln(z) * CF
                + 4 * ln(x) * ln(z) * z * CF * pow(omx, -1)
                - 2 * ln(x) * ln(z) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(z) * z * CF
                - 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(omx, -1)
                + 4 * ln(x) * ln(z) * pow(z, 2) * CF
                - ln(x) * ln(z) * x * CF
                + 2 * ln(x) * ln(z) * x * z * CF
                - 2 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -2) * CF
                + 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF
                - 2 * ln(x) * ln(omx) * pow(x, -1) * CF
                + 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF
                + 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF
                - 3 * ln(x) * ln(omx) * CF * pow(omx, -1)
                + 2 * ln(x) * ln(omx) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * CF
                + 6 * ln(x) * ln(omx) * z * CF * pow(omx, -1)
                - 4 * ln(x) * ln(omx) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * z * CF
                - 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx, -1)
                + 8 * ln(x) * ln(omx) * pow(z, 2) * CF
            )
            tmp += (
                +2 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(x, -2) * CF
                - 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF
                + 2 * ln(x) * ln(opx) * pow(x, -1) * CF
                - 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF
                - 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF
                + 2 * ln(x) * ln(opx) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * CF
                - 4 * ln(x) * ln(opx) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * z * CF
                - 8 * ln(x) * ln(opx) * pow(z, 2) * CF
                + 2 * ln(x) * ln(opx) * x * CF
                - 4 * ln(x) * ln(opx) * x * z * CF
                + 1.0 / 2.0 * ln(z) * CF * pow(poly2, -1)
                + 3 * ln(z) * CF * pow(omx, -1)
                - 9.0 / 2.0 * ln(z) * CF
                - 7 * ln(z) * CF * rln2 * pow(omx, -1)
                + 4 * ln(z) * CF * rln2
                - 3 * ln(z) * CF * sqrtxz1 * pow(omx, -1)
                + 2 * ln(z) * CF * sqrtxz1
                + 3 * ln(z) * z * CF * pow(omx, -1)
                - 2 * ln(z) * z * CF
                - 10 * ln(z) * z * CF * rln2 * pow(omx, -1)
                + 4 * ln(z) * z * CF * rln2
                - 16 * ln(z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                + 16 * ln(z) * pow(z, 2) * CF * rln2
                + 1.0 / 2.0 * ln(z) * x * CF * pow(poly2, -1)
                - ln(z) * x * CF * pow(xmz, -1)
                - 3.0 / 2.0 * ln(z) * x * CF
                + 2 * ln(z) * x * CF * rln2
                + 8 * ln(z) * x * z * CF * rln2
                - 1.0 / 2.0 * ln(z) * pow(x, 2) * CF * pow(poly2, -1)
                + 2 * ln(z) * pow(x, 2) * CF * pow(xmz, -1)
                - 1.0 / 2.0 * ln(z) * pow(x, 3) * CF * pow(poly2, -1)
                + 3 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                - 4 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * CF
            )
            tmp += (
                +8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF
                + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF
                - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * x * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF
                - ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * pow(x, -2) * CF
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF
                - ln(z) * ln(1 + x * z) * pow(x, -1) * CF
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF
                + 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                - 2 * ln(z) * ln(1 + x * z) * CF * pow(omx, -1)
                - ln(z) * ln(1 + x * z) * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * CF
                - 4 * ln(z) * ln(1 + x * z) * z * CF * pow(omx, -1)
            )
            tmp += (
                +2 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF
                + 4 * ln(z) * ln(1 + x * z) * x * z * CF
                - 2 * ln(z) * ln(z + x) * CF * pow(omx, -1)
                + ln(z) * ln(z + x) * CF
                - 4 * ln(z) * ln(z + x) * z * CF * pow(omx, -1)
                + 2 * ln(z) * ln(z + x) * z * CF
                - 4 * ln(z) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                + 4 * ln(z) * ln(z + x) * pow(z, 2) * CF
                + ln(z) * ln(z + x) * x * CF
                + 2 * ln(z) * ln(z + x) * x * z * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF
                - pow(ln(z), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                + pow(ln(z), 2) * pow(x, -2) * z * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * CF
                - pow(ln(z), 2) * pow(x, -1) * z * CF
                - 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF
                + pow(ln(z), 2) * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(opx, -1)
                - 2 * pow(ln(z), 2) * CF
                - 2 * pow(ln(z), 2) * z * CF * pow(omx, -1)
                - pow(ln(z), 2) * z * CF * pow(opx, -1)
                + 4 * pow(ln(z), 2) * z * CF
                + 2 * pow(ln(z), 2) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * pow(ln(z), 2) * pow(z, 2) * CF
                + pow(ln(z), 2) * x * CF
                - 2 * pow(ln(z), 2) * x * z * CF
                - ln(z) * ln(omz) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(omz) * CF
                + 2 * ln(z) * ln(omz) * z * CF * pow(omx, -1)
                - 4 * ln(z) * ln(omz) * z * CF
                - 8 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * sqrtxz3
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                + 5.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
            )
            tmp += (
                -5 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                - 5.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                + 5 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                - 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
            )
            tmp += (
                +6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                - 5.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                + 5 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                + 5.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                - 5 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
            )
            tmp += (
                +8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * CF
                + Li2(1 - x * pow(z, -1)) * CF * pow(omx, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * CF
                - 2 * Li2(1 - x * pow(z, -1)) * z * CF * pow(omx, -1)
                + 4 * Li2(1 - x * pow(z, -1)) * z * CF
                - Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -2) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF
                - Li2(-x * pow(z, -1)) * pow(x, -1) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF
                + 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                + 2 * Li2(-x * pow(z, -1)) * CF * pow(omx, -1)
                - Li2(-x * pow(z, -1)) * CF * pow(opx, -1)
                + 4 * Li2(-x * pow(z, -1)) * z * CF * pow(omx, -1)
                + 2 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1)
                - 4 * Li2(-x * pow(z, -1)) * z * CF
                + 4 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(omx, -1)
                - 2 * Li2(-x * pow(z, -1)) * x * CF
                + 2 * Li2(-x) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * Li2(-x) * pow(x, -2) * CF
                - 4 * Li2(-x) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * Li2(-x) * pow(x, -2) * z * CF
            )
            tmp += (
                +2 * Li2(-x) * pow(x, -1) * CF
                - 4 * Li2(-x) * pow(x, -1) * z * CF
                - 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF
                - 2 * Li2(-x) * CF * pow(opx, -1)
                + 4 * Li2(-x) * CF
                + 4 * Li2(-x) * z * CF * pow(opx, -1)
                - 8 * Li2(-x) * z * CF
                - 8 * Li2(-x) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * Li2(-x) * x * CF
                - 8 * Li2(-x) * x * z * CF
                - Li2(-x * z) * pow(x, -2) * CF * pow(opx, -1)
                + Li2(-x * z) * pow(x, -2) * CF
                + 2 * Li2(-x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * Li2(-x * z) * pow(x, -2) * z * CF
                - Li2(-x * z) * pow(x, -1) * CF
                + 2 * Li2(-x * z) * pow(x, -1) * z * CF
                + 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF
                - 2 * Li2(-x * z) * CF * pow(omx, -1)
                - Li2(-x * z) * CF * pow(opx, -1)
                + 2 * Li2(-x * z) * CF
                - 4 * Li2(-x * z) * z * CF * pow(omx, -1)
                + 2 * Li2(-x * z) * z * CF * pow(opx, -1)
                - 4 * Li2(-x * z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * Li2(-x * z) * pow(z, 2) * CF
                + 4 * Li2(-x * z) * x * z * CF
                - 2 * Li2(x) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * Li2(x) * pow(x, -2) * CF
                + 4 * Li2(x) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * Li2(x) * pow(x, -2) * z * CF
                - 2 * Li2(x) * pow(x, -1) * CF
                + 4 * Li2(x) * pow(x, -1) * z * CF
                + 8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF
                - 3 * Li2(x) * CF * pow(omx, -1)
                + 2 * Li2(x) * CF * pow(opx, -1)
                + 2 * Li2(x) * CF
                + 6 * Li2(x) * z * CF * pow(omx, -1)
                - 4 * Li2(x) * z * CF * pow(opx, -1)
                - 4 * Li2(x) * z * CF
                - 8 * Li2(x) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * Li2(x) * pow(z, 2) * CF * pow(opx, -1)
                + 8 * Li2(x) * pow(z, 2) * CF
                - Li2(z) * CF * pow(omx, -1)
                + 2 * Li2(z) * CF
                + 2 * Li2(z) * z * CF * pow(omx, -1)
            )
            tmp += -4 * Li2(z) * z * CF - 4 * InvTanInt(-sqrtxz3) * z * CF * sqrtxz3 - 8 * InvTanInt(z * sqrtxz3) * z * CF * sqrtxz3 + 4 * InvTanInt(sqrtxz3) * z * CF * sqrtxz3

            res += tmp

        return res
