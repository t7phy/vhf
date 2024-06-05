from core.definitions import CF, NC, TR, NF, ZETA3, ZETA2
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi


def C2Pg2qEq(inx, inz, cx, cz, Q, muR, muF, muA, orders: list, ndecimals):
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
        res = (
            -35.0 / 16.0 * pow(NC, -1)
            + 263.0 / 16.0 * NC
            - 1.0 / 3.0 * NC * pow(rln2, 3)
            - 1.0 / 3.0 * LMUR * NF
            + 11.0 / 6.0 * LMUR * NC
            - 1.0 / 2.0 * LMUF * pow(NC, -1)
            + 1.0 / 3.0 * LMUF * NF
            + 8.0 / 3.0 * LMUF * NC
            - 1.0 / 6.0 * LMUF * LMUR * NF
            + 11.0 / 12.0 * LMUF * LMUR * NC
            - 3.0 / 16.0 * pow(LMUF, 2) * pow(NC, -1)
            + 1.0 / 6.0 * pow(LMUF, 2) * NF
            + 109.0 / 48.0 * pow(LMUF, 2) * NC
            + 3.0 / 4.0 * LMUA * pow(NC, -1)
            - 3.0 / 4.0 * LMUA * NC
            + 3.0 / 8.0 * LMUA * LMUF * pow(NC, -1)
            - 3.0 / 8.0 * LMUA * LMUF * NC
            + 45.0 / 16.0 * x * pow(NC, -1)
            - 281.0 / 16.0 * x * NC
            - 2.0 / 3.0 * x * NC * pow(rln2, 3)
            + 1.0 / 3.0 * x * LMUR * NF
            - 11.0 / 6.0 * x * LMUR * NC
            - 7.0 / 8.0 * x * LMUF * pow(NC, -1)
            - 1.0 / 3.0 * x * LMUF * NF
            - 43.0 / 24.0 * x * LMUF * NC
            + 1.0 / 3.0 * x * LMUF * LMUR * NF
            - 11.0 / 6.0 * x * LMUF * LMUR * NC
            - 1.0 / 3.0 * x * pow(LMUF, 2) * NF
            - 7.0 / 6.0 * x * pow(LMUF, 2) * NC
            - 3.0 / 4.0 * x * LMUA * pow(NC, -1)
            + 3.0 / 4.0 * x * LMUA * NC
            - 3.0 / 4.0 * x * LMUA * LMUF * pow(NC, -1)
            + 3.0 / 4.0 * x * LMUA * LMUF * NC
            + 4 * ZETA3 * pow(NC, -1)
            - 13.0 / 4.0 * ZETA3 * NC
            - 8 * ZETA3 * x * pow(NC, -1)
            + 9.0 / 2.0 * ZETA3 * x * NC
            + 5.0 / 24.0 * pow(pi, 2) * pow(NC, -1)
            - 23.0 / 24.0 * pow(pi, 2) * NC
            + 1.0 / 6.0 * pow(pi, 2) * NC * rln2
            + 1.0 / 24.0 * pow(pi, 2) * LMUF * pow(NC, -1)
            - 3.0 / 8.0 * pow(pi, 2) * LMUF * NC
            + 1.0 / 12.0 * pow(pi, 2) * LMUA * pow(NC, -1)
            - 1.0 / 12.0 * pow(pi, 2) * LMUA * NC
            - 1.0 / 4.0 * pow(pi, 2) * x * pow(NC, -1)
            + 19.0 / 12.0 * pow(pi, 2) * x * NC
            + 1.0 / 3.0 * pow(pi, 2) * x * NC * rln2
            - 1.0 / 12.0 * pow(pi, 2) * x * LMUF * pow(NC, -1)
            + 1.0 / 12.0 * pow(pi, 2) * x * LMUF * NC
            - 1.0 / 6.0 * pow(pi, 2) * x * LMUA * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * x * LMUA * NC
            + 1.0 / 2.0 * ln(1 + x) * NC * pow(rln2, 2)
            + ln(1 + x) * x * NC * pow(rln2, 2)
            + 1.0 / 12.0 * ln(1 + x) * pow(pi, 2) * NC
            + 1.0 / 6.0 * ln(1 + x) * pow(pi, 2) * x * NC
            - 1.0 / 6.0 * pow(ln(1 + x), 3) * NC
            - 1.0 / 3.0 * pow(ln(1 + x), 3) * x * NC
        )
        res += (
            -19.0 / 8.0 * ln(x) * pow(NC, -1)
            + 99.0 / 8.0 * ln(x) * NC
            - 1.0 / 6.0 * ln(x) * LMUR * NF
            + 11.0 / 12.0 * ln(x) * LMUR * NC
            - 11.0 / 8.0 * ln(x) * LMUF * pow(NC, -1)
            + 1.0 / 6.0 * ln(x) * LMUF * NF
            + 143.0 / 24.0 * ln(x) * LMUF * NC
            - 1.0 / 8.0 * ln(x) * pow(LMUF, 2) * pow(NC, -1)
            + 9.0 / 8.0 * ln(x) * pow(LMUF, 2) * NC
            + 3.0 / 8.0 * ln(x) * LMUA * pow(NC, -1)
            - 3.0 / 8.0 * ln(x) * LMUA * NC
            - 1.0 / 16.0 * ln(x) * x * pow(NC, -1)
            + 1.0 / 16.0 * ln(x) * x * NC
            + 1.0 / 3.0 * ln(x) * x * LMUR * NF
            - 11.0 / 6.0 * ln(x) * x * LMUR * NC
            + 5.0 / 4.0 * ln(x) * x * LMUF * pow(NC, -1)
            - 1.0 / 3.0 * ln(x) * x * LMUF * NF
            - 89.0 / 12.0 * ln(x) * x * LMUF * NC
            + 1.0 / 4.0 * ln(x) * x * pow(LMUF, 2) * pow(NC, -1)
            + 3.0 / 4.0 * ln(x) * x * pow(LMUF, 2) * NC
            - 3.0 / 4.0 * ln(x) * x * LMUA * pow(NC, -1)
            + 3.0 / 4.0 * ln(x) * x * LMUA * NC
            + 1.0 / 4.0 * ln(x) * pow(pi, 2) * pow(NC, -1)
            - 3.0 / 4.0 * ln(x) * pow(pi, 2) * NC
            - 1.0 / 2.0 * ln(x) * pow(pi, 2) * x * pow(NC, -1)
            + 1.0 / 6.0 * ln(x) * pow(pi, 2) * x * NC
            + ln(x) * ln(1 + x) * NC
            + ln(x) * ln(1 + x) * LMUF * NC
            + ln(x) * ln(1 + x) * x * NC
            + 2 * ln(x) * ln(1 + x) * x * LMUF * NC
            - 37.0 / 32.0 * pow(ln(x), 2) * pow(NC, -1)
            + 153.0 / 32.0 * pow(ln(x), 2) * NC
            - 1.0 / 4.0 * pow(ln(x), 2) * LMUF * pow(NC, -1)
            + 7.0 / 4.0 * pow(ln(x), 2) * LMUF * NC
            + 3.0 / 4.0 * pow(ln(x), 2) * x * pow(NC, -1)
            - 25.0 / 4.0 * pow(ln(x), 2) * x * NC
            + 1.0 / 2.0 * pow(ln(x), 2) * x * LMUF * pow(NC, -1)
            + 3.0 / 2.0 * pow(ln(x), 2) * x * LMUF * NC
            + pow(ln(x), 2) * ln(1 + x) * NC
            + 2 * pow(ln(x), 2) * ln(1 + x) * x * NC
            - 1.0 / 48.0 * pow(ln(x), 3) * pow(NC, -1)
            + 29.0 / 48.0 * pow(ln(x), 3) * NC
            + 1.0 / 24.0 * pow(ln(x), 3) * x * pow(NC, -1)
            + 19.0 / 24.0 * pow(ln(x), 3) * x * NC
            + 3.0 / 8.0 * pow(ln(x), 2) * ln(omx) * pow(NC, -1)
            - 11.0 / 8.0 * pow(ln(x), 2) * ln(omx) * NC
            - 3.0 / 4.0 * pow(ln(x), 2) * ln(omx) * x * pow(NC, -1)
            + 11.0 / 4.0 * pow(ln(x), 2) * ln(omx) * x * NC
        )
        res += (
            +21.0 / 8.0 * ln(x) * ln(omx) * pow(NC, -1)
            - 69.0 / 8.0 * ln(x) * ln(omx) * NC
            + ln(x) * ln(omx) * LMUF * pow(NC, -1)
            - 2 * ln(x) * ln(omx) * LMUF * NC
            - 3 * ln(x) * ln(omx) * x * pow(NC, -1)
            + 9 * ln(x) * ln(omx) * x * NC
            - 2 * ln(x) * ln(omx) * x * LMUF * pow(NC, -1)
            + 4 * ln(x) * ln(omx) * x * LMUF * NC
            - ln(x) * ln(omx) * ln(1 + x) * NC
            - 2 * ln(x) * ln(omx) * ln(1 + x) * x * NC
            - 5.0 / 4.0 * ln(x) * pow(ln(omx), 2) * pow(NC, -1)
            - 7.0 / 4.0 * ln(x) * pow(ln(omx), 2) * NC
            + 5.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * pow(NC, -1)
            - 11.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * NC
            + ln(x) * Li2(-x) * NC
            + 2 * ln(x) * Li2(-x) * x * NC
            + 1.0 / 2.0 * ln(x) * Li2(x) * pow(NC, -1)
            + 1.0 / 2.0 * ln(x) * Li2(x) * NC
            - ln(x) * Li2(x) * x * pow(NC, -1)
            + 5 * ln(x) * Li2(x) * x * NC
            + 7.0 / 4.0 * ln(omx) * pow(NC, -1)
            - 19.0 / 4.0 * ln(omx) * NC
            + 1.0 / 2.0 * ln(omx) * NC * pow(rln2, 2)
            + 1.0 / 6.0 * ln(omx) * LMUR * NF
            - 11.0 / 12.0 * ln(omx) * LMUR * NC
            + 7.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1)
            - 1.0 / 6.0 * ln(omx) * LMUF * NF
            - 41.0 / 6.0 * ln(omx) * LMUF * NC
            + 1.0 / 4.0 * ln(omx) * pow(LMUF, 2) * pow(NC, -1)
            - 3.0 / 4.0 * ln(omx) * pow(LMUF, 2) * NC
            - 3.0 / 8.0 * ln(omx) * LMUA * pow(NC, -1)
            + 3.0 / 8.0 * ln(omx) * LMUA * NC
            - 1.0 / 2.0 * ln(omx) * x * pow(NC, -1)
            + 15.0 / 4.0 * ln(omx) * x * NC
            + ln(omx) * x * NC * pow(rln2, 2)
            - 1.0 / 3.0 * ln(omx) * x * LMUR * NF
            + 11.0 / 6.0 * ln(omx) * x * LMUR * NC
            - 7.0 / 4.0 * ln(omx) * x * LMUF * pow(NC, -1)
            + 1.0 / 3.0 * ln(omx) * x * LMUF * NF
            + 71.0 / 12.0 * ln(omx) * x * LMUF * NC
            - 1.0 / 2.0 * ln(omx) * x * pow(LMUF, 2) * pow(NC, -1)
            + 3.0 / 2.0 * ln(omx) * x * pow(LMUF, 2) * NC
            + 3.0 / 4.0 * ln(omx) * x * LMUA * pow(NC, -1)
            - 3.0 / 4.0 * ln(omx) * x * LMUA * NC
            - 1.0 / 24.0 * ln(omx) * pow(pi, 2) * pow(NC, -1)
            + 19.0 / 24.0 * ln(omx) * pow(pi, 2) * NC
            + 1.0 / 12.0 * ln(omx) * pow(pi, 2) * x * pow(NC, -1)
        )
        res += (
            +1.0 / 12.0 * ln(omx) * pow(pi, 2) * x * NC
            - ln(omx) * ln(1 + x) * NC * rln2
            - 2 * ln(omx) * ln(1 + x) * x * NC * rln2
            + 1.0 / 2.0 * ln(omx) * pow(ln(1 + x), 2) * NC
            + ln(omx) * pow(ln(1 + x), 2) * x * NC
            - 21.0 / 16.0 * pow(ln(omx), 2) * pow(NC, -1)
            + 61.0 / 16.0 * pow(ln(omx), 2) * NC
            - 1.0 / 2.0 * pow(ln(omx), 2) * LMUF * pow(NC, -1)
            + pow(ln(omx), 2) * LMUF * NC
            + 3.0 / 2.0 * pow(ln(omx), 2) * x * pow(NC, -1)
            - 4 * pow(ln(omx), 2) * x * NC
            + pow(ln(omx), 2) * x * LMUF * pow(NC, -1)
            - 2 * pow(ln(omx), 2) * x * LMUF * NC
            + 5.0 / 24.0 * pow(ln(omx), 3) * pow(NC, -1)
            - 7.0 / 24.0 * pow(ln(omx), 3) * NC
            - 5.0 / 12.0 * pow(ln(omx), 3) * x * pow(NC, -1)
            + 7.0 / 12.0 * pow(ln(omx), 3) * x * NC
            - 1.0 / 4.0 * ln(omx) * Li2(1 - x) * pow(NC, -1)
            - 7.0 / 4.0 * ln(omx) * Li2(1 - x) * NC
            + 1.0 / 2.0 * ln(omx) * Li2(1 - x) * x * pow(NC, -1)
            - 5.0 / 2.0 * ln(omx) * Li2(1 - x) * x * NC
            - ln(omx) * Li2(-x) * NC
            - 2 * ln(omx) * Li2(-x) * x * NC
            - 3.0 / 4.0 * ln(omx) * Li2(x) * pow(NC, -1)
            - 15.0 / 4.0 * ln(omx) * Li2(x) * NC
            + 3.0 / 2.0 * ln(omx) * Li2(x) * x * pow(NC, -1)
            - 9.0 / 2.0 * ln(omx) * Li2(x) * x * NC
            - 1.0 / 4.0 * ln(opx) * pow(pi, 2) * NC
            - 1.0 / 2.0 * ln(opx) * pow(pi, 2) * x * NC
            + Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * NC
            + 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * x * NC
            + Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * NC
            + 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * x * NC
            - 3.0 / 2.0 * Li3(1 - x) * pow(NC, -1)
            - 7.0 / 2.0 * Li3(1 - x) * NC
            + 3 * Li3(1 - x) * x * pow(NC, -1)
            - 3 * Li3(1 - x) * x * NC
            + Li3(1 / (1 + x) - 1 / (1 + x) * x) * NC
            + 2 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * x * NC
            - 5.0 / 4.0 * Li3(x) * pow(NC, -1)
            + 5.0 / 4.0 * Li3(x) * NC
            + 5.0 / 2.0 * Li3(x) * x * pow(NC, -1)
            - 9.0 / 2.0 * Li3(x) * x * NC
            + Li2(-x) * NC
            + Li2(-x) * LMUF * NC
            + Li2(-x) * x * NC
            + 2 * Li2(-x) * x * LMUF * NC
            + 3.0 / 8.0 * Li2(x) * pow(NC, -1)
        )
        res += -7.0 / 8.0 * Li2(x) * NC + 1.0 / 4.0 * Li2(x) * LMUF * pow(NC, -1) + 7.0 / 4.0 * Li2(x) * LMUF * NC - 1.0 / 2.0 * Li2(x) * x * pow(NC, -1) - 3.0 / 2.0 * Li2(x) * x * NC - 1.0 / 2.0 * Li2(x) * x * LMUF * pow(NC, -1) + 5.0 / 2.0 * Li2(x) * x * LMUF * NC

        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            5.0 / 4.0 * pow(NC, -1)
            - 21.0 / 4.0 * NC
            + 1.0 / 6.0 * LMUR * NF
            - 11.0 / 12.0 * LMUR * NC
            + 3.0 / 4.0 * LMUF * pow(NC, -1)
            - 1.0 / 6.0 * LMUF * NF
            - 35.0 / 6.0 * LMUF * NC
            + 5.0 / 8.0 * LMUA * pow(NC, -1)
            - 5.0 / 8.0 * LMUA * NC
            + 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1)
            - 1.0 / 2.0 * LMUA * LMUF * NC
            + 1.0 / 8.0 * x * pow(NC, -1)
            + 35.0 / 8.0 * x * NC
            - 1.0 / 3.0 * x * LMUR * NF
            + 11.0 / 6.0 * x * LMUR * NC
            - 3.0 / 4.0 * x * LMUF * pow(NC, -1)
            + 1.0 / 3.0 * x * LMUF * NF
            + 59.0 / 12.0 * x * LMUF * NC
            - 1.0 / 4.0 * x * LMUA * pow(NC, -1)
            + 1.0 / 4.0 * x * LMUA * NC
            - x * LMUA * LMUF * pow(NC, -1)
            + x * LMUA * LMUF * NC
            - 1.0 / 8.0 * pow(pi, 2) * pow(NC, -1)
            + 11.0 / 24.0 * pow(pi, 2) * NC
            + 1.0 / 4.0 * pow(pi, 2) * x * pow(NC, -1)
            - 1.0 / 4.0 * pow(pi, 2) * x * NC
            + 7.0 / 4.0 * ln(x) * pow(NC, -1)
            - 29.0 / 4.0 * ln(x) * NC
            + 1.0 / 4.0 * ln(x) * LMUF * pow(NC, -1)
            - 9.0 / 4.0 * ln(x) * LMUF * NC
            + 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1)
            - 1.0 / 2.0 * ln(x) * LMUA * NC
            - 2 * ln(x) * x * pow(NC, -1)
            + 10 * ln(x) * x * NC
            - 1.0 / 2.0 * ln(x) * x * LMUF * pow(NC, -1)
            - 3.0 / 2.0 * ln(x) * x * LMUF * NC
            - ln(x) * x * LMUA * pow(NC, -1)
            + ln(x) * x * LMUA * NC
            - ln(x) * ln(1 + x) * NC
            - 2 * ln(x) * ln(1 + x) * x * NC
            + 1.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
            - 7.0 / 4.0 * pow(ln(x), 2) * NC
            - 1.0 / 2.0 * pow(ln(x), 2) * x * pow(NC, -1)
            - 3.0 / 2.0 * pow(ln(x), 2) * x * NC
            - ln(x) * ln(omx) * pow(NC, -1)
            + 2 * ln(x) * ln(omx) * NC
            + 2 * ln(x) * ln(omx) * x * pow(NC, -1)
            - 4 * ln(x) * ln(omx) * x * NC
            - 17.0 / 8.0 * ln(omx) * pow(NC, -1)
            + 65.0 / 8.0 * ln(omx) * NC
            - 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1)
            + 3.0 / 2.0 * ln(omx) * LMUF * NC
            - 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1)
            + 1.0 / 2.0 * ln(omx) * LMUA * NC
            + 5.0 / 2.0 * ln(omx) * x * pow(NC, -1)
            - 17.0 / 2.0 * ln(omx) * x * NC
            + ln(omx) * x * LMUF * pow(NC, -1)
            - 3 * ln(omx) * x * LMUF * NC
            + ln(omx) * x * LMUA * pow(NC, -1)
            - ln(omx) * x * LMUA * NC
        )
        res += +1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) - pow(ln(omx), 2) * NC - pow(ln(omx), 2) * x * pow(NC, -1) + 2 * pow(ln(omx), 2) * x * NC - Li2(-x) * NC - 2 * Li2(-x) * x * NC - 1.0 / 4.0 * Li2(x) * pow(NC, -1) - 7.0 / 4.0 * Li2(x) * NC + 1.0 / 2.0 * Li2(x) * x * pow(NC, -1) - 5.0 / 2.0 * Li2(x) * x * NC

        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            -17.0 / 8.0 * pow(NC, -1)
            + 65.0 / 8.0 * NC
            - 1.0 / 2.0 * LMUF * pow(NC, -1)
            + 1.0 / 2.0 * LMUF * NC
            - LMUA * pow(NC, -1)
            + LMUA * NC
            + 5.0 / 2.0 * x * pow(NC, -1)
            - 17.0 / 2.0 * x * NC
            + x * LMUF * pow(NC, -1)
            - x * LMUF * NC
            + 2 * x * LMUA * pow(NC, -1)
            - 2 * x * LMUA * NC
            - 3.0 / 4.0 * ln(x) * pow(NC, -1)
            + 11.0 / 4.0 * ln(x) * NC
            + 3.0 / 2.0 * ln(x) * x * pow(NC, -1)
            + 1.0 / 2.0 * ln(x) * x * NC
            + ln(omx) * pow(NC, -1)
            - 2 * ln(omx) * NC
            - 2 * ln(omx) * x * pow(NC, -1)
            + 4 * ln(omx) * x * NC
        )

        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 3.0 / 4.0 * pow(NC, -1) - 3.0 / 4.0 * NC - 3.0 / 2.0 * x * pow(NC, -1) + 3.0 / 2.0 * x * NC

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
                2 * pow(z, -1) * pow(NC, -1)
                - pow(z, -1) * NC
                + 2 * pow(NC, -1) * pow(omz, -1)
                - pow(NC, -1)
                - NC * pow(omz, -1)
                + 2 * NC
                + x * pow(z, -1) * pow(NC, -1)
                + x * pow(NC, -1) * pow(omz, -1)
                - 4 * x * pow(NC, -1)
                + 11.0 / 12.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 12.0 * pow(pi, 2) * pow(z, -1) * NC
                + 5.0 / 6.0 * pow(pi, 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 12.0 * pow(pi, 2) * pow(NC, -1)
                - 1.0 / 12.0 * pow(pi, 2) * NC * pow(omz, -1)
                + 1.0 / 6.0 * pow(pi, 2) * NC
                - 11.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * NC
                - 5.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 6.0 * pow(pi, 2) * x * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * NC * pow(omz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * NC
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * pow(z, -1) * NC
                + 9.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                + 3 * ln(x) * NC
                - 12 * ln(x) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * x * pow(z, -1) * NC
                - 12 * ln(x) * x * pow(NC, -1) * pow(omz, -1)
                + 18 * ln(x) * x * pow(NC, -1)
                + 6 * ln(x) * x * NC * pow(omz, -1)
                - 18 * ln(x) * x * NC
                - 5 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * NC
                - 19.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                + 13.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                - 3 * pow(ln(x), 2) * NC
                + 10 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * pow(z, -1) * NC
                + 19.0 / 2.0 * pow(ln(x), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 13.0 / 2.0 * pow(ln(x), 2) * x * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * NC * pow(omz, -1)
            )
            tmp += (
                +6 * pow(ln(x), 2) * x * NC
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 3 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 11.0 / 2.0 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(z) * pow(z, -1) * NC
                + 13.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(z) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(z) * NC * pow(omz, -1)
                + 5 * ln(x) * ln(z) * NC
                - 11 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(z) * x * pow(z, -1) * NC
                - 13 * ln(x) * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(z) * x * pow(NC, -1)
                + 5 * ln(x) * ln(z) * x * NC * pow(omz, -1)
                - 10 * ln(x) * ln(z) * x * NC
                + 3 * ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 17.0 / 2.0 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * ln(omx) * pow(z, -1) * NC
                + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 11.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1)
                - 2 * ln(x) * ln(omx) * NC * pow(omz, -1)
                + 4 * ln(x) * ln(omx) * NC
                - 17 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * pow(z, -1) * NC
                - 16 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                + 11 * ln(x) * ln(omx) * x * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * NC * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * x * NC
                + 6 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(omz) * pow(z, -1) * NC
                + 7 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(x) * ln(omz) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(omz) * NC * pow(omz, -1)
                + 5 * ln(x) * ln(omz) * NC
                - 16 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * x * pow(z, -1) * NC
            )
            tmp += (
                -14 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(x) * ln(omz) * x * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * x * NC * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * x * NC
                + 6 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * pow(z, -1) * NC
                - ln(x) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * NC * pow(omz, -1)
                - ln(x) * ln(xmz) * NC
                + ln(x) * ln(xmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(xmz) * x * pow(z, -1) * NC
                + 2 * ln(x) * ln(xmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(xmz) * x * pow(NC, -1)
                - ln(x) * ln(xmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * x * NC
                - ln(x) * ln(xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(omxmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * NC * pow(omz, -1)
                - ln(x) * ln(omxmz) * NC
                + 2 * ln(x) * ln(omxmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * pow(z, -1) * NC
                + ln(x) * ln(omxmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(omxmz) * x * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * x * NC
                - ln(x) * ln(omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(z) * pow(z, -1) * pow(NC, -1)
                + ln(z) * pow(z, -1) * NC
                - 5.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * pow(NC, -1)
                + ln(z) * NC * pow(omz, -1)
                - 2 * ln(z) * NC
                + 6 * ln(z) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(z) * x * pow(z, -1) * NC
                + 6 * ln(z) * x * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -9 * ln(z) * x * pow(NC, -1)
                - 4 * ln(z) * x * NC * pow(omz, -1)
                + 12 * ln(z) * x * NC
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1)
                + pow(ln(z), 2) * pow(z, -1) * NC
                - 9.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                + 5.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1)
                + pow(ln(z), 2) * NC * pow(omz, -1)
                - 2 * pow(ln(z), 2) * NC
                + 3 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * pow(z, -1) * NC
                + 9.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * NC * pow(omz, -1)
                + 4 * pow(ln(z), 2) * x * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(omx) * pow(z, -1) * NC
                - 5 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(omx) * pow(NC, -1)
                + ln(z) * ln(omx) * NC * pow(omz, -1)
                - 2 * ln(z) * ln(omx) * NC
                + 8 * ln(z) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * pow(z, -1) * NC
                + 10 * ln(z) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(z) * ln(omx) * x * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * NC * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * x * NC
                - 2 * ln(z) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 4 * ln(z) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(z) * ln(omz) * pow(z, -1) * NC
                - 3 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * pow(NC, -1)
                + 2 * ln(z) * ln(omz) * NC * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * NC
                + 6 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * pow(z, -1) * NC
                + 6 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -4 * ln(z) * ln(omz) * x * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * NC * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * x * NC
                - 2 * ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * pow(z, -1) * NC
                + ln(z) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * NC * pow(omz, -1)
                + ln(z) * ln(xmz) * NC
                - ln(z) * ln(xmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(xmz) * x * pow(z, -1) * NC
                - 2 * ln(z) * ln(xmz) * x * pow(NC, -1) * pow(omz, -1)
                + ln(z) * ln(xmz) * x * pow(NC, -1)
                + ln(z) * ln(xmz) * x * NC * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * x * NC
                + ln(z) * ln(xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * pow(z, -1) * NC
                - 3 * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                - ln(omx) * NC
                + 8 * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * x * pow(z, -1) * NC
                + 8 * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(omx) * x * pow(NC, -1)
                - 2 * ln(omx) * x * NC * pow(omz, -1)
                + 6 * ln(omx) * x * NC
                - 3 * pow(ln(omx), 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * pow(z, -1) * NC
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC
                + 6 * pow(ln(omx), 2) * x * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * NC
                + 6 * pow(ln(omx), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * x * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * NC * pow(omz, -1)
            )
            tmp += (
                +pow(ln(omx), 2) * x * NC
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * ln(omx) * ln(omz) * pow(z, -1) * NC
                - 9.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1)
                + 3.0 / 2.0 * ln(omx) * ln(omz) * NC * pow(omz, -1)
                - 3 * ln(omx) * ln(omz) * NC
                + 12 * ln(omx) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 3 * ln(omx) * ln(omz) * x * pow(z, -1) * NC
                + 9 * ln(omx) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 7 * ln(omx) * ln(omz) * x * pow(NC, -1)
                - 3 * ln(omx) * ln(omz) * x * NC * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * x * NC
                - 5 * ln(omx) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * ln(omz) * pow(z, -1) * pow(NC, -1)
                + ln(omz) * pow(z, -1) * NC
                - 2 * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(omz) * pow(NC, -1)
                + ln(omz) * NC * pow(omz, -1)
                - 2 * ln(omz) * NC
                + 6 * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(omz) * x * pow(z, -1) * NC
                + 6 * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(omz) * x * pow(NC, -1)
                - 4 * ln(omz) * x * NC * pow(omz, -1)
                + 12 * ln(omz) * x * NC
                - 11.0 / 4.0 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(omz), 2) * pow(z, -1) * NC
                - 7.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(omz), 2) * NC * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * NC
                + 11.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * NC
                + 7.0 / 2.0 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 3 * pow(ln(omz), 2) * x * pow(NC, -1)
            )
            tmp += (
                -3.0 / 2.0 * pow(ln(omz), 2) * x * NC * pow(omz, -1)
                + 3 * pow(ln(omz), 2) * x * NC
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + ln(omz) * ln(omxmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(z, -1) * NC
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * NC * pow(omz, -1)
                + ln(omz) * ln(omxmz) * NC
                - 2 * ln(omz) * ln(omxmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * pow(z, -1) * NC
                - ln(omz) * ln(omxmz) * x * pow(NC, -1) * pow(omz, -1)
                + ln(omz) * ln(omxmz) * x * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * NC * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * x * NC
                + ln(omz) * ln(omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(z, -1) * NC
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(omz, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * pow(z, -1) * NC
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * NC * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * NC
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(z, -1) * pow(NC, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * pow(NC, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * pow(NC, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(z, -1) * NC
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * NC * pow(omz, -1)
                + Li2(omx * pow(omz, -1)) * NC
                + Li2(omx * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * x * pow(z, -1) * NC
                + 2 * Li2(omx * pow(omz, -1)) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(omx * pow(omz, -1)) * x * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * x * NC * pow(omz, -1)
                - 2 * Li2(omx * pow(omz, -1)) * x * NC
                - Li2(omx * pow(omz, -1)) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + Li2(z * pow(omx, -1)) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(z, -1) * NC
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * NC * pow(omz, -1)
                - Li2(z * pow(omx, -1)) * NC
                - 2 * Li2(z * pow(omx, -1)) * x * pow(z, -1) * pow(NC, -1)
                - Li2(z * pow(omx, -1)) * x * pow(z, -1) * NC
                - Li2(z * pow(omx, -1)) * x * pow(NC, -1) * pow(omz, -1)
                + Li2(z * pow(omx, -1)) * x * pow(NC, -1)
                - Li2(z * pow(omx, -1)) * x * NC * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * x * NC
                + Li2(z * pow(omx, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1)
                + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * pow(NC, -1)
            )
            tmp += -Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) - 1.0 / 2.0 * Li2(z) * pow(z, -1) * pow(NC, -1) + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1) + Li2(z) * x * pow(z, -1) * pow(NC, -1) - Li2(z) * x * pow(NC, -1) * pow(omz, -1) - Li2(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + Li2(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                2 * pow(z, -1) * pow(NC, -1)
                - pow(z, -1) * NC
                + 2 * pow(NC, -1) * pow(omz, -1)
                - pow(NC, -1)
                - NC * pow(omz, -1)
                + 2 * NC
                + x * pow(z, -1) * pow(NC, -1)
                + x * pow(NC, -1) * pow(omz, -1)
                - 4 * x * pow(NC, -1)
                + 11.0 / 12.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 12.0 * pow(pi, 2) * pow(z, -1) * NC
                + 5.0 / 6.0 * pow(pi, 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 12.0 * pow(pi, 2) * pow(NC, -1)
                - 1.0 / 12.0 * pow(pi, 2) * NC * pow(omz, -1)
                + 1.0 / 6.0 * pow(pi, 2) * NC
                - 11.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * NC
                - 5.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 6.0 * pow(pi, 2) * x * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * NC * pow(omz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * NC
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * pow(z, -1) * NC
                + 9.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                + 3 * ln(x) * NC
                - 12 * ln(x) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * x * pow(z, -1) * NC
                - 12 * ln(x) * x * pow(NC, -1) * pow(omz, -1)
                + 18 * ln(x) * x * pow(NC, -1)
                + 6 * ln(x) * x * NC * pow(omz, -1)
                - 18 * ln(x) * x * NC
                - ln(x) * ln(-omxmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * NC * pow(omz, -1)
                - ln(x) * ln(-omxmz) * NC
                + 2 * ln(x) * ln(-omxmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(-omxmz) * x * pow(z, -1) * NC
                + ln(x) * ln(-omxmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(-omxmz) * x * pow(NC, -1)
            )
            tmp += (
                -ln(x) * ln(-omxmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * x * NC
                - ln(x) * ln(-omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 9.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1)
                + 7.0 / 4.0 * pow(ln(x), 2) * pow(z, -1) * NC
                - 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                + 3 * pow(ln(x), 2) * pow(NC, -1)
                + 7.0 / 4.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * NC
                + 9 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * NC
                + 9 * pow(ln(x), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 6 * pow(ln(x), 2) * x * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * x * NC * pow(omz, -1)
                + 7 * pow(ln(x), 2) * x * NC
                - 3 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 3 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 13.0 / 2.0 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1)
                - 3 * ln(x) * ln(z) * pow(z, -1) * NC
                + 7 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1)
                - 3 * ln(x) * ln(z) * NC * pow(omz, -1)
                + 6 * ln(x) * ln(z) * NC
                - 13 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * pow(z, -1) * NC
                - 14 * ln(x) * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                + 9 * ln(x) * ln(z) * x * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * NC * pow(omz, -1)
                - 12 * ln(x) * ln(z) * x * NC
                + 4 * ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 15.0 / 2.0 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * ln(omx) * pow(z, -1) * NC
                + 15.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(x) * ln(omx) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * ln(omx) * NC * pow(omz, -1)
                + 3 * ln(x) * ln(omx) * NC
                - 15 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * pow(z, -1) * NC
            )
            tmp += (
                -15 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(x) * ln(omx) * x * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * NC * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * x * NC
                + 5 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 7 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 3 * ln(x) * ln(omz) * pow(z, -1) * NC
                + 13.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1)
                - 3 * ln(x) * ln(omz) * NC * pow(omz, -1)
                + 6 * ln(x) * ln(omz) * NC
                - 14 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * pow(z, -1) * NC
                - 13 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                + 9 * ln(x) * ln(omz) * x * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * NC * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * x * NC
                + 5 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * pow(z, -1) * NC
                - ln(x) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * NC * pow(omz, -1)
                - ln(x) * ln(xmz) * NC
                + ln(x) * ln(xmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(xmz) * x * pow(z, -1) * NC
                + 2 * ln(x) * ln(xmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(xmz) * x * pow(NC, -1)
                - ln(x) * ln(xmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * x * NC
                - ln(x) * ln(xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * pow(z, -1) * pow(NC, -1)
                + ln(z) * pow(z, -1) * NC
                - 5.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * pow(NC, -1)
                + ln(z) * NC * pow(omz, -1)
                - 2 * ln(z) * NC
                + 6 * ln(z) * x * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                -4 * ln(z) * x * pow(z, -1) * NC
                + 6 * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(z) * x * pow(NC, -1)
                - 4 * ln(z) * x * NC * pow(omz, -1)
                + 12 * ln(z) * x * NC
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1)
                + pow(ln(z), 2) * pow(z, -1) * NC
                - 9.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                + 5.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1)
                + pow(ln(z), 2) * NC * pow(omz, -1)
                - 2 * pow(ln(z), 2) * NC
                + 3 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * pow(z, -1) * NC
                + 9.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * NC * pow(omz, -1)
                + 4 * pow(ln(z), 2) * x * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(omx) * pow(z, -1) * NC
                - 5 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(omx) * pow(NC, -1)
                + ln(z) * ln(omx) * NC * pow(omz, -1)
                - 2 * ln(z) * ln(omx) * NC
                + 8 * ln(z) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * pow(z, -1) * NC
                + 10 * ln(z) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(z) * ln(omx) * x * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * NC * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * x * NC
                - 2 * ln(z) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 4 * ln(z) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + 5.0 / 2.0 * ln(z) * ln(omz) * pow(z, -1) * NC
                - 7.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 5.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1)
                + 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(omz, -1)
                - 5 * ln(z) * ln(omz) * NC
                + 8 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * pow(z, -1) * NC
            )
            tmp += (
                +7 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(z) * ln(omz) * x * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * NC * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * x * NC
                - 3 * ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * pow(z, -1) * NC
                + ln(z) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * NC * pow(omz, -1)
                + ln(z) * ln(xmz) * NC
                - ln(z) * ln(xmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(xmz) * x * pow(z, -1) * NC
                - 2 * ln(z) * ln(xmz) * x * pow(NC, -1) * pow(omz, -1)
                + ln(z) * ln(xmz) * x * pow(NC, -1)
                + ln(z) * ln(xmz) * x * NC * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * x * NC
                + ln(z) * ln(xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * pow(z, -1) * NC
                - 3 * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                - ln(omx) * NC
                + 8 * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * x * pow(z, -1) * NC
                + 8 * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(omx) * x * pow(NC, -1)
                - 2 * ln(omx) * x * NC * pow(omz, -1)
                + 6 * ln(omx) * x * NC
                - 3 * pow(ln(omx), 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * pow(z, -1) * NC
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC
                + 6 * pow(ln(omx), 2) * x * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * NC
                + 6 * pow(ln(omx), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * x * pow(NC, -1)
            )
            tmp += (
                -1.0 / 2.0 * pow(ln(omx), 2) * x * NC * pow(omz, -1)
                + pow(ln(omx), 2) * x * NC
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(omx) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + ln(omx) * ln(omz) * pow(z, -1) * NC
                - 4 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(omx) * ln(omz) * pow(NC, -1)
                + ln(omx) * ln(omz) * NC * pow(omz, -1)
                - 2 * ln(omx) * ln(omz) * NC
                + 10 * ln(omx) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * pow(z, -1) * NC
                + 8 * ln(omx) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * x * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * NC * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * x * NC
                - 4 * ln(omx) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * ln(omz) * pow(z, -1) * pow(NC, -1)
                + ln(omz) * pow(z, -1) * NC
                - 2 * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(omz) * pow(NC, -1)
                + ln(omz) * NC * pow(omz, -1)
                - 2 * ln(omz) * NC
                + 6 * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(omz) * x * pow(z, -1) * NC
                + 6 * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(omz) * x * pow(NC, -1)
                - 4 * ln(omz) * x * NC * pow(omz, -1)
                + 12 * ln(omz) * x * NC
                + ln(omz) * ln(-omxmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(z, -1) * NC
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * NC * pow(omz, -1)
                + ln(omz) * ln(-omxmz) * NC
                - 2 * ln(omz) * ln(-omxmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * pow(z, -1) * NC
                - ln(omz) * ln(-omxmz) * x * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +ln(omz) * ln(-omxmz) * x * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * NC * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * x * NC
                + ln(omz) * ln(-omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 9.0 / 4.0 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1)
                + pow(ln(omz), 2) * pow(z, -1) * NC
                - 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                + 5.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1)
                + pow(ln(omz), 2) * NC * pow(omz, -1)
                - 2 * pow(ln(omz), 2) * NC
                + 9.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * pow(z, -1) * NC
                + 3 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * x * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * NC * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * x * NC
                - 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * pow(z, -1) * pow(NC, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * pow(NC, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * pow(NC, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(z, -1) * pow(NC, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * pow(NC, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - Li2(pow(z, -1) * omx) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(z, -1) * NC
                - 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(pow(z, -1) * omx) * NC * pow(omz, -1)
                + Li2(pow(z, -1) * omx) * NC
                + 2 * Li2(pow(z, -1) * omx) * x * pow(z, -1) * pow(NC, -1)
                + Li2(pow(z, -1) * omx) * x * pow(z, -1) * NC
                + Li2(pow(z, -1) * omx) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(pow(z, -1) * omx) * x * pow(NC, -1)
                + Li2(pow(z, -1) * omx) * x * NC * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * x * NC
                - Li2(pow(z, -1) * omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(z, -1) * NC
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * NC * pow(omz, -1)
                + Li2(omx * pow(omz, -1)) * NC
                + Li2(omx * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * x * pow(z, -1) * NC
                + 2 * Li2(omx * pow(omz, -1)) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(omx * pow(omz, -1)) * x * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * x * NC * pow(omz, -1)
                - 2 * Li2(omx * pow(omz, -1)) * x * NC
                - Li2(omx * pow(omz, -1)) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(z, -1) * NC
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(omz, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * pow(z, -1) * NC
            )
            tmp += (
                -Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * NC * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * NC
                - 1.0 / 2.0 * Li2(z) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1)
                + Li2(z) * x * pow(z, -1) * pow(NC, -1)
                - Li2(z) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + Li2(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
            )

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                2 * pow(z, -1) * pow(NC, -1)
                - pow(z, -1) * NC
                + 2 * pow(NC, -1) * pow(omz, -1)
                - pow(NC, -1)
                - NC * pow(omz, -1)
                + 2 * NC
                + x * pow(z, -1) * pow(NC, -1)
                + x * pow(NC, -1) * pow(omz, -1)
                - 4 * x * pow(NC, -1)
                + 11.0 / 12.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 12.0 * pow(pi, 2) * pow(z, -1) * NC
                + 5.0 / 6.0 * pow(pi, 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 12.0 * pow(pi, 2) * pow(NC, -1)
                - 5.0 / 12.0 * pow(pi, 2) * NC * pow(omz, -1)
                + 5.0 / 6.0 * pow(pi, 2) * NC
                - 11.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1)
                + 5.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * NC
                - 5.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 6.0 * pow(pi, 2) * x * pow(NC, -1)
                + 5.0 / 6.0 * pow(pi, 2) * x * NC * pow(omz, -1)
                - 5.0 / 3.0 * pow(pi, 2) * x * NC
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * pow(z, -1) * NC
                + 9.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                + 3 * ln(x) * NC
                - 12 * ln(x) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * x * pow(z, -1) * NC
                - 12 * ln(x) * x * pow(NC, -1) * pow(omz, -1)
                + 18 * ln(x) * x * pow(NC, -1)
                + 6 * ln(x) * x * NC * pow(omz, -1)
                - 18 * ln(x) * x * NC
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(z, -1) * NC
                - ln(x) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * NC * pow(omz, -1)
                - ln(x) * ln(-xmz) * NC
                + ln(x) * ln(-xmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(-xmz) * x * pow(z, -1) * NC
                + 2 * ln(x) * ln(-xmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(-xmz) * x * pow(NC, -1)
            )
            tmp += (
                -ln(x) * ln(-xmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * x * NC
                - ln(x) * ln(-xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 21.0 / 4.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1)
                + 7.0 / 4.0 * pow(ln(x), 2) * pow(z, -1) * NC
                - 21.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1)
                + 7.0 / 4.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * NC
                + 21.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * NC
                + 21.0 / 2.0 * pow(ln(x), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 7 * pow(ln(x), 2) * x * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * x * NC * pow(omz, -1)
                + 7 * pow(ln(x), 2) * x * NC
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 6 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1)
                - 3 * ln(x) * ln(z) * pow(z, -1) * NC
                + 15.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1)
                - 3 * ln(x) * ln(z) * NC * pow(omz, -1)
                + 6 * ln(x) * ln(z) * NC
                - 12 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * pow(z, -1) * NC
                - 15 * ln(x) * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                + 9 * ln(x) * ln(z) * x * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * NC * pow(omz, -1)
                - 12 * ln(x) * ln(z) * x * NC
                + 3 * ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 9 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * ln(omx) * pow(z, -1) * NC
                + 9 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * ln(omx) * NC * pow(omz, -1)
                + 3 * ln(x) * ln(omx) * NC
                - 18 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * pow(z, -1) * NC
            )
            tmp += (
                -18 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                + 12 * ln(x) * ln(omx) * x * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * NC * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * x * NC
                + 6 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 15.0 / 2.0 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 3 * ln(x) * ln(omz) * pow(z, -1) * NC
                + 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1)
                - 3 * ln(x) * ln(omz) * NC * pow(omz, -1)
                + 6 * ln(x) * ln(omz) * NC
                - 15 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * pow(z, -1) * NC
                - 12 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                + 9 * ln(x) * ln(omz) * x * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * NC * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * x * NC
                + 6 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 3 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(omxmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * NC * pow(omz, -1)
                - ln(x) * ln(omxmz) * NC
                + 2 * ln(x) * ln(omxmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * pow(z, -1) * NC
                + ln(x) * ln(omxmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(omxmz) * x * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * x * NC
                - ln(x) * ln(omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(z) * pow(z, -1) * pow(NC, -1)
                + ln(z) * pow(z, -1) * NC
                - 5.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * pow(NC, -1)
                + ln(z) * NC * pow(omz, -1)
                - 2 * ln(z) * NC
            )
            tmp += (
                +6 * ln(z) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(z) * x * pow(z, -1) * NC
                + 6 * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(z) * x * pow(NC, -1)
                - 4 * ln(z) * x * NC * pow(omz, -1)
                + 12 * ln(z) * x * NC
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(z, -1) * NC
                + ln(z) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * NC * pow(omz, -1)
                + ln(z) * ln(-xmz) * NC
                - ln(z) * ln(-xmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * pow(z, -1) * NC
                - 2 * ln(z) * ln(-xmz) * x * pow(NC, -1) * pow(omz, -1)
                + ln(z) * ln(-xmz) * x * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * NC * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * x * NC
                + ln(z) * ln(-xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 4.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1)
                + 5.0 / 4.0 * pow(ln(z), 2) * pow(z, -1) * NC
                - 11.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1)
                + 5.0 / 4.0 * pow(ln(z), 2) * NC * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * NC
                + 7.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * NC
                + 11.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 3 * pow(ln(z), 2) * x * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * x * NC * pow(omz, -1)
                + 5 * pow(ln(z), 2) * x * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(z) * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * ln(omx) * pow(z, -1) * NC
                - 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(z) * ln(omx) * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * ln(omx) * NC * pow(omz, -1)
            )
            tmp += (
                -ln(z) * ln(omx) * NC
                + 9 * ln(z) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - ln(z) * ln(omx) * x * pow(z, -1) * NC
                + 12 * ln(z) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 7 * ln(z) * ln(omx) * x * pow(NC, -1)
                - ln(z) * ln(omx) * x * NC * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * x * NC
                - 2 * ln(z) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 5 * ln(z) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + 5.0 / 2.0 * ln(z) * ln(omz) * pow(z, -1) * NC
                - 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1)
                + 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(omz, -1)
                - 5 * ln(z) * ln(omz) * NC
                + 5 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * pow(z, -1) * NC
                + 4 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(z) * ln(omz) * x * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * NC * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * x * NC
                - 2 * ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * pow(z, -1) * NC
                - 3 * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                - ln(omx) * NC
                + 8 * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * x * pow(z, -1) * NC
                + 8 * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(omx) * x * pow(NC, -1)
                - 2 * ln(omx) * x * NC * pow(omz, -1)
                + 6 * ln(omx) * x * NC
                - 3 * pow(ln(omx), 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(omx), 2) * pow(z, -1) * NC
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(omx), 2) * NC
            )
            tmp += (
                +6 * pow(ln(omx), 2) * x * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * NC
                + 6 * pow(ln(omx), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * x * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(omx), 2) * x * NC * pow(omz, -1)
                + 3 * pow(ln(omx), 2) * x * NC
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * ln(omz) * pow(z, -1) * NC
                - 9.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * ln(omz) * NC * pow(omz, -1)
                - ln(omx) * ln(omz) * NC
                + 12 * ln(omx) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - ln(omx) * ln(omz) * x * pow(z, -1) * NC
                + 9 * ln(omx) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 7 * ln(omx) * ln(omz) * x * pow(NC, -1)
                - ln(omx) * ln(omz) * x * NC * pow(omz, -1)
                + 2 * ln(omx) * ln(omz) * x * NC
                - 5 * ln(omx) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * ln(omz) * pow(z, -1) * pow(NC, -1)
                + ln(omz) * pow(z, -1) * NC
                - 2 * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(omz) * pow(NC, -1)
                + ln(omz) * NC * pow(omz, -1)
                - 2 * ln(omz) * NC
                + 6 * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(omz) * x * pow(z, -1) * NC
                + 6 * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(omz) * x * pow(NC, -1)
                - 4 * ln(omz) * x * NC * pow(omz, -1)
                + 12 * ln(omz) * x * NC
                - 11.0 / 4.0 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1)
                + 5.0 / 4.0 * pow(ln(omz), 2) * pow(z, -1) * NC
                - 7.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1)
                + 5.0 / 4.0 * pow(ln(omz), 2) * NC * pow(omz, -1)
            )
            tmp += (
                -5.0 / 2.0 * pow(ln(omz), 2) * NC
                + 11.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * NC
                + 7.0 / 2.0 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 3 * pow(ln(omz), 2) * x * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * x * NC * pow(omz, -1)
                + 5 * pow(ln(omz), 2) * x * NC
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + ln(omz) * ln(omxmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(z, -1) * NC
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * NC * pow(omz, -1)
                + ln(omz) * ln(omxmz) * NC
                - 2 * ln(omz) * ln(omxmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * pow(z, -1) * NC
                - ln(omz) * ln(omxmz) * x * pow(NC, -1) * pow(omz, -1)
                + ln(omz) * ln(omxmz) * x * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * NC * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * x * NC
                + ln(omz) * ln(omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(z, -1) * NC
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * NC * pow(omz, -1)
                - Li2(pow(omx, -1) * omz) * NC
                - Li2(pow(omx, -1) * omz) * x * pow(z, -1) * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * x * pow(z, -1) * NC
                - 2 * Li2(pow(omx, -1) * omz) * x * pow(NC, -1) * pow(omz, -1)
                + Li2(pow(omx, -1) * omz) * x * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * x * NC * pow(omz, -1)
                + 2 * Li2(pow(omx, -1) * omz) * x * NC
                + Li2(pow(omx, -1) * omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +Li2(z * pow(omx, -1)) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(z, -1) * NC
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * NC * pow(omz, -1)
                - Li2(z * pow(omx, -1)) * NC
                - 2 * Li2(z * pow(omx, -1)) * x * pow(z, -1) * pow(NC, -1)
                - Li2(z * pow(omx, -1)) * x * pow(z, -1) * NC
                - Li2(z * pow(omx, -1)) * x * pow(NC, -1) * pow(omz, -1)
                + Li2(z * pow(omx, -1)) * x * pow(NC, -1)
                - Li2(z * pow(omx, -1)) * x * NC * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * x * NC
                + Li2(z * pow(omx, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(z, -1) * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(z, -1) * NC
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(omz, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * pow(z, -1) * NC
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * NC * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * NC
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1)
            )
            tmp += (
                +2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * pow(z, -1) * pow(NC, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * pow(NC, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(z) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1)
                + Li2(z) * x * pow(z, -1) * pow(NC, -1)
                - Li2(z) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + Li2(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                2 * pow(z, -1) * pow(NC, -1)
                - pow(z, -1) * NC
                + 2 * pow(NC, -1) * pow(omz, -1)
                - pow(NC, -1)
                - NC * pow(omz, -1)
                + 2 * NC
                + x * pow(z, -1) * pow(NC, -1)
                + x * pow(NC, -1) * pow(omz, -1)
                - 4 * x * pow(NC, -1)
                + 11.0 / 12.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 12.0 * pow(pi, 2) * pow(z, -1) * NC
                + 5.0 / 6.0 * pow(pi, 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 12.0 * pow(pi, 2) * pow(NC, -1)
                - 1.0 / 12.0 * pow(pi, 2) * NC * pow(omz, -1)
                + 1.0 / 6.0 * pow(pi, 2) * NC
                - 11.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * NC
                - 5.0 / 3.0 * pow(pi, 2) * x * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 6.0 * pow(pi, 2) * x * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * NC * pow(omz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * NC
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * pow(z, -1) * NC
                + 9.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                + 3 * ln(x) * NC
                - 12 * ln(x) * x * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * x * pow(z, -1) * NC
                - 12 * ln(x) * x * pow(NC, -1) * pow(omz, -1)
                + 18 * ln(x) * x * pow(NC, -1)
                + 6 * ln(x) * x * NC * pow(omz, -1)
                - 18 * ln(x) * x * NC
                - ln(x) * ln(-omxmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * NC * pow(omz, -1)
                - ln(x) * ln(-omxmz) * NC
                + 2 * ln(x) * ln(-omxmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(-omxmz) * x * pow(z, -1) * NC
                + ln(x) * ln(-omxmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(-omxmz) * x * pow(NC, -1)
            )
            tmp += (
                -ln(x) * ln(-omxmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * x * NC
                - ln(x) * ln(-omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(z, -1) * NC
                - ln(x) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * NC * pow(omz, -1)
                - ln(x) * ln(-xmz) * NC
                + ln(x) * ln(-xmz) * x * pow(z, -1) * pow(NC, -1)
                - ln(x) * ln(-xmz) * x * pow(z, -1) * NC
                + 2 * ln(x) * ln(-xmz) * x * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(-xmz) * x * pow(NC, -1)
                - ln(x) * ln(-xmz) * x * NC * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * x * NC
                - ln(x) * ln(-xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 19.0 / 4.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * NC
                - 5 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                + 13.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                - 3 * pow(ln(x), 2) * NC
                + 19.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * pow(z, -1) * NC
                + 10 * pow(ln(x), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 13.0 / 2.0 * pow(ln(x), 2) * x * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * NC * pow(omz, -1)
                + 6 * pow(ln(x), 2) * x * NC
                - 3 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 7 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(z) * pow(z, -1) * NC
                + 8 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(x) * ln(z) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(z) * NC * pow(omz, -1)
                + 5 * ln(x) * ln(z) * NC
                - 14 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(z) * x * pow(z, -1) * NC
            )
            tmp += (
                -16 * ln(x) * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(x) * ln(z) * x * pow(NC, -1)
                + 5 * ln(x) * ln(z) * x * NC * pow(omz, -1)
                - 10 * ln(x) * ln(z) * x * NC
                + 4 * ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * ln(omx) * pow(z, -1) * NC
                + 17.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 11.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1)
                - 2 * ln(x) * ln(omx) * NC * pow(omz, -1)
                + 4 * ln(x) * ln(omx) * NC
                - 16 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * pow(z, -1) * NC
                - 17 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                + 11 * ln(x) * ln(omx) * x * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * NC * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * x * NC
                + 5 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 6 * ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 13.0 / 2.0 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(omz) * pow(z, -1) * NC
                + 11.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(omz) * pow(NC, -1)
                - 5.0 / 2.0 * ln(x) * ln(omz) * NC * pow(omz, -1)
                + 5 * ln(x) * ln(omz) * NC
                - 13 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * x * pow(z, -1) * NC
                - 11 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(omz) * x * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * x * NC * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * x * NC
                + 5 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 3 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * pow(z, -1) * pow(NC, -1)
                + ln(z) * pow(z, -1) * NC
                - 5.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * pow(NC, -1)
                + ln(z) * NC * pow(omz, -1)
            )
            tmp += (
                -2 * ln(z) * NC
                + 6 * ln(z) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(z) * x * pow(z, -1) * NC
                + 6 * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(z) * x * pow(NC, -1)
                - 4 * ln(z) * x * NC * pow(omz, -1)
                + 12 * ln(z) * x * NC
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(z, -1) * NC
                + ln(z) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * NC * pow(omz, -1)
                + ln(z) * ln(-xmz) * NC
                - ln(z) * ln(-xmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * pow(z, -1) * NC
                - 2 * ln(z) * ln(-xmz) * x * pow(NC, -1) * pow(omz, -1)
                + ln(z) * ln(-xmz) * x * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * NC * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * x * NC
                + ln(z) * ln(-xmz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 4.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(z), 2) * pow(z, -1) * NC
                - 11.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1)
                + 3.0 / 4.0 * pow(ln(z), 2) * NC * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * NC
                + 7.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * NC
                + 11.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 3 * pow(ln(z), 2) * x * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * x * NC * pow(omz, -1)
                + 3 * pow(ln(z), 2) * x * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(z) * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * ln(z) * ln(omx) * pow(z, -1) * NC
                - 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(z) * ln(omx) * pow(NC, -1)
                + 3.0 / 2.0 * ln(z) * ln(omx) * NC * pow(omz, -1)
            )
            tmp += (
                -3 * ln(z) * ln(omx) * NC
                + 9 * ln(z) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 3 * ln(z) * ln(omx) * x * pow(z, -1) * NC
                + 12 * ln(z) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 7 * ln(z) * ln(omx) * x * pow(NC, -1)
                - 3 * ln(z) * ln(omx) * x * NC * pow(omz, -1)
                + 6 * ln(z) * ln(omx) * x * NC
                - 2 * ln(z) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 5 * ln(z) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(z) * ln(omz) * pow(z, -1) * NC
                - 5.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * pow(NC, -1)
                + 2 * ln(z) * ln(omz) * NC * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * NC
                + 7 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * pow(z, -1) * NC
                + 5 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * x * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * NC * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * x * NC
                - 3 * ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * pow(z, -1) * NC
                - 3 * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                - ln(omx) * NC
                + 8 * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * x * pow(z, -1) * NC
                + 8 * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(omx) * x * pow(NC, -1)
                - 2 * ln(omx) * x * NC * pow(omz, -1)
                + 6 * ln(omx) * x * NC
                - 3 * pow(ln(omx), 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * pow(z, -1) * NC
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC
            )
            tmp += (
                +6 * pow(ln(omx), 2) * x * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * NC
                + 6 * pow(ln(omx), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * x * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * NC * pow(omz, -1)
                + pow(ln(omx), 2) * x * NC
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(omx), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(omx) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + ln(omx) * ln(omz) * pow(z, -1) * NC
                - 4 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(omx) * ln(omz) * pow(NC, -1)
                + ln(omx) * ln(omz) * NC * pow(omz, -1)
                - 2 * ln(omx) * ln(omz) * NC
                + 10 * ln(omx) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * pow(z, -1) * NC
                + 8 * ln(omx) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * x * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * NC * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * x * NC
                - 4 * ln(omx) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * ln(omz) * pow(z, -1) * pow(NC, -1)
                + ln(omz) * pow(z, -1) * NC
                - 2 * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(omz) * pow(NC, -1)
                + ln(omz) * NC * pow(omz, -1)
                - 2 * ln(omz) * NC
                + 6 * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(omz) * x * pow(z, -1) * NC
                + 6 * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(omz) * x * pow(NC, -1)
                - 4 * ln(omz) * x * NC * pow(omz, -1)
                + 12 * ln(omz) * x * NC
                + ln(omz) * ln(-omxmz) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(z, -1) * NC
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * NC * pow(omz, -1)
            )
            tmp += (
                +ln(omz) * ln(-omxmz) * NC
                - 2 * ln(omz) * ln(-omxmz) * x * pow(z, -1) * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * pow(z, -1) * NC
                - ln(omz) * ln(-omxmz) * x * pow(NC, -1) * pow(omz, -1)
                + ln(omz) * ln(-omxmz) * x * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * NC * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * x * NC
                + ln(omz) * ln(-omxmz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 9.0 / 4.0 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1)
                + pow(ln(omz), 2) * pow(z, -1) * NC
                - 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                + 5.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1)
                + pow(ln(omz), 2) * NC * pow(omz, -1)
                - 2 * pow(ln(omz), 2) * NC
                + 9.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * pow(z, -1) * NC
                + 3 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * x * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * NC * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * x * NC
                - 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * pow(z, -1) * pow(NC, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * pow(NC, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * pow(NC, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(z, -1) * NC
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(omz, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC
            )
            tmp += (
                +Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * pow(z, -1) * NC
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * NC * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * NC
                - Li2(pow(z, -1) * omx) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(z, -1) * NC
                - 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(pow(z, -1) * omx) * NC * pow(omz, -1)
                + Li2(pow(z, -1) * omx) * NC
                + 2 * Li2(pow(z, -1) * omx) * x * pow(z, -1) * pow(NC, -1)
                + Li2(pow(z, -1) * omx) * x * pow(z, -1) * NC
                + Li2(pow(z, -1) * omx) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(pow(z, -1) * omx) * x * pow(NC, -1)
                + Li2(pow(z, -1) * omx) * x * NC * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * x * NC
                - Li2(pow(z, -1) * omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(z, -1) * NC
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * NC * pow(omz, -1)
                - Li2(pow(omx, -1) * omz) * NC
                - Li2(pow(omx, -1) * omz) * x * pow(z, -1) * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * x * pow(z, -1) * NC
                - 2 * Li2(pow(omx, -1) * omz) * x * pow(NC, -1) * pow(omz, -1)
                + Li2(pow(omx, -1) * omz) * x * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * x * NC * pow(omz, -1)
                + 2 * Li2(pow(omx, -1) * omz) * x * NC
                + Li2(pow(omx, -1) * omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(z, -1) * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1)
            )
            tmp += (
                +Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(z) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1)
                + Li2(z) * x * pow(z, -1) * pow(NC, -1)
                - Li2(z) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + Li2(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
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
                2 * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 47.0 / 16.0 * pow(z, -1) * pow(NC, -1)
                - 2 * pow(z, -1) * NC * pow(omz, -1)
                - 33.0 / 16.0 * pow(z, -1) * NC
                + 1.0 / 6.0 * pow(z, -1) * LMUR * NF
                - 11.0 / 12.0 * pow(z, -1) * LMUR * NC
                - 1.0 / 6.0 * pow(z, -1) * LMUF * NF
                - 61.0 / 12.0 * pow(z, -1) * LMUF * NC
                - 1.0 / 8.0 * pow(NC, -1) * pow(poly2, -1)
                - 4 * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(NC, -1)
                + 1.0 / 8.0 * NC * pow(poly2, -1)
                + 3 * NC * pow(omz, -1)
                + 14 * NC
                - 1.0 / 3.0 * LMUR * NF
                + 11.0 / 6.0 * LMUR * NC
                - 5.0 / 4.0 * LMUF * pow(NC, -1)
                + 1.0 / 3.0 * LMUF * NF
                + 137.0 / 12.0 * LMUF * NC
                - 1.0 / 4.0 * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * LMUA * NC
                - 1.0 / 4.0 * LMUA * LMUF * pow(NC, -1)
                + 1.0 / 4.0 * LMUA * LMUF * NC
                - 1.0 / 4.0 * z * pow(NC, -1) * pow(omxmz, -1)
                + 51.0 / 16.0 * z * pow(NC, -1)
                + 1.0 / 4.0 * z * NC * pow(omxmz, -1)
                - 51.0 / 16.0 * z * NC
                + 3.0 / 4.0 * z * LMUF * pow(NC, -1)
                - 3.0 / 4.0 * z * LMUF * NC
                - 3.0 / 8.0 * z * LMUA * pow(NC, -1)
                + 3.0 / 8.0 * z * LMUA * NC
                - 1.0 / 4.0 * z * LMUA * LMUF * pow(NC, -1)
                + 1.0 / 4.0 * z * LMUA * LMUF * NC
                + 1.0 / 2.0 * pow(z, 2) * pow(NC, -1) * pow(omxmz, -1)
                - 1.0 / 2.0 * pow(z, 2) * NC * pow(omxmz, -1)
                - 4 * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 11.0 / 4.0 * x * pow(z, -1) * pow(NC, -1)
                + 4 * x * pow(z, -1) * NC * pow(omz, -1)
                + 3.0 / 4.0 * x * pow(z, -1) * NC
                - 1.0 / 3.0 * x * pow(z, -1) * LMUR * NF
                + 11.0 / 6.0 * x * pow(z, -1) * LMUR * NC
                + 1.0 / 3.0 * x * pow(z, -1) * LMUF * NF
                + 25.0 / 6.0 * x * pow(z, -1) * LMUF * NC
                + 1.0 / 8.0 * x * pow(NC, -1) * pow(poly2, -1)
                + 3 * x * pow(NC, -1) * pow(omz, -1)
                + 37.0 / 8.0 * x * pow(NC, -1)
                - 1.0 / 8.0 * x * NC * pow(poly2, -1)
                - 4 * x * NC * pow(omz, -1)
                - 117.0 / 8.0 * x * NC
                + 2.0 / 3.0 * x * LMUR * NF
                - 11.0 / 3.0 * x * LMUR * NC
                + 3.0 / 2.0 * x * LMUF * pow(NC, -1)
                - 2.0 / 3.0 * x * LMUF * NF
                - 59.0 / 6.0 * x * LMUF * NC
                + 1.0 / 2.0 * x * LMUA * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * x * LMUA * LMUF * NC
            )
            tmp += (
                -11.0 / 4.0 * x * z * pow(NC, -1)
                + 11.0 / 4.0 * x * z * NC
                - x * z * LMUF * pow(NC, -1)
                + x * z * LMUF * NC
                + 1.0 / 4.0 * x * z * LMUA * pow(NC, -1)
                - 1.0 / 4.0 * x * z * LMUA * NC
                + 1.0 / 2.0 * x * z * LMUA * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * x * z * LMUA * LMUF * NC
                + 2 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 8.0 * pow(x, 2) * pow(NC, -1) * pow(poly2, -1)
                - 2 * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 8.0 * pow(x, 2) * NC * pow(poly2, -1)
                - 1.0 / 8.0 * pow(x, 3) * pow(NC, -1) * pow(poly2, -1)
                + 1.0 / 8.0 * pow(x, 3) * NC * pow(poly2, -1)
                - 13.0 / 12.0 * pow(pi, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * NC * pow(omz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * NC
                - 3.0 / 4.0 * pow(pi, 2) * pow(NC, -1) * pow(omz, -1)
                + 5.0 / 6.0 * pow(pi, 2) * pow(NC, -1)
                - 1.0 / 6.0 * pow(pi, 2) * NC * pow(omz, -1)
                - 3.0 / 2.0 * pow(pi, 2) * NC
                - 1.0 / 6.0 * pow(pi, 2) * z * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * z * NC
                + 3.0 / 2.0 * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1)
                - 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * NC * pow(omz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * NC
                + 3.0 / 2.0 * pow(pi, 2) * x * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 6.0 * pow(pi, 2) * x * pow(NC, -1)
                + 1.0 / 3.0 * pow(pi, 2) * x * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(pi, 2) * x * NC
                - 1.0 / 6.0 * pow(pi, 2) * x * z * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * z * NC
                - 5.0 / 6.0 * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 2.0 * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 6.0 * ln(pow(x, -1) * z * omx * omz) * pow(z, -1) * NF
                - 1.0 / 6.0 * ln(pow(x, -1) * z * omx * omz) * NF * pow(omz, -1)
                - 8 * ln(x) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 33.0 / 8.0 * ln(x) * pow(z, -1) * pow(NC, -1)
                - 1.0 / 6.0 * ln(x) * pow(z, -1) * NF
                + 8 * ln(x) * pow(z, -1) * NC * pow(omz, -1)
            )
            tmp += (
                -101.0 / 8.0 * ln(x) * pow(z, -1) * NC
                - 2 * ln(x) * pow(z, -1) * LMUF * NC
                - 3.0 / 16.0 * ln(x) * pow(NC, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * ln(x) * pow(NC, -1) * pow(poly2, -1)
                + 7.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omxmz, -2)
                + ln(x) * pow(NC, -1) * pow(omxmz, -1)
                + 41.0 / 16.0 * ln(x) * pow(NC, -1)
                - 1.0 / 6.0 * ln(x) * NF * pow(omz, -1)
                + 3.0 / 16.0 * ln(x) * NC * pow(poly2, -2)
                + 7.0 / 8.0 * ln(x) * NC * pow(poly2, -1)
                - 13.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * NC * pow(omxmz, -2)
                - 1.0 / 2.0 * ln(x) * NC * pow(omxmz, -1)
                + 207.0 / 16.0 * ln(x) * NC
                - 1.0 / 4.0 * ln(x) * LMUF * pow(NC, -1)
                + 17.0 / 4.0 * ln(x) * LMUF * NC
                - 1.0 / 4.0 * ln(x) * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * ln(x) * LMUA * NC
                - 1.0 / 4.0 * ln(x) * z * pow(NC, -1) * pow(omxmz, -2)
                + 2 * ln(x) * z * pow(NC, -1) * pow(omxmz, -1)
                - 3.0 / 4.0 * ln(x) * z * pow(NC, -1)
                + 1.0 / 4.0 * ln(x) * z * NC * pow(omxmz, -2)
                - 7.0 / 2.0 * ln(x) * z * NC * pow(omxmz, -1)
                + 7.0 / 4.0 * ln(x) * z * NC
                + 1.0 / 4.0 * ln(x) * z * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(x) * z * LMUF * NC
                - 1.0 / 4.0 * ln(x) * z * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * ln(x) * z * LMUA * NC
                + 3.0 / 4.0 * ln(x) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -2)
                - 5.0 / 2.0 * ln(x) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -1)
                - 3.0 / 4.0 * ln(x) * pow(z, 2) * NC * pow(omxmz, -2)
                + 7.0 / 2.0 * ln(x) * pow(z, 2) * NC * pow(omxmz, -1)
                + 16 * ln(x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 17.0 / 4.0 * ln(x) * x * pow(z, -1) * pow(NC, -1)
                - 16 * ln(x) * x * pow(z, -1) * NC * pow(omz, -1)
                + 73.0 / 4.0 * ln(x) * x * pow(z, -1) * NC
                - 2 * ln(x) * x * pow(z, -1) * LMUF * NC
                + 3.0 / 16.0 * ln(x) * x * pow(NC, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * ln(x) * x * pow(NC, -1) * pow(poly2, -1)
                - 4 * ln(x) * x * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * x * pow(NC, -1) * pow(xmz, -1)
            )
            tmp += (
                +3.0 / 2.0 * ln(x) * x * pow(NC, -1) * pow(omxmz, -2)
                - 3 * ln(x) * x * pow(NC, -1) * pow(omxmz, -1)
                - 251.0 / 16.0 * ln(x) * x * pow(NC, -1)
                - 3.0 / 16.0 * ln(x) * x * NC * pow(poly2, -2)
                - ln(x) * x * NC * pow(poly2, -1)
                + 10 * ln(x) * x * NC * pow(omz, -1)
                - 3.0 / 2.0 * ln(x) * x * NC * pow(omxmz, -2)
                + 3 * ln(x) * x * NC * pow(omxmz, -1)
                + 3.0 / 16.0 * ln(x) * x * NC
                - 1.0 / 2.0 * ln(x) * x * LMUF * pow(NC, -1)
                + 9.0 / 2.0 * ln(x) * x * LMUF * NC
                + 1.0 / 2.0 * ln(x) * x * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * x * LMUA * NC
                + 1.0 / 2.0 * ln(x) * x * z * LMUF * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * x * z * LMUF * NC
                + 1.0 / 2.0 * ln(x) * x * z * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * x * z * LMUA * NC
                - 8 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 8.0 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(poly2, -1)
                + 8 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + ln(x) * pow(x, 2) * pow(NC, -1) * pow(xmz, -1)
                - 3.0 / 2.0 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -2)
                + 3.0 / 2.0 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -1)
                + ln(x) * pow(x, 2) * pow(NC, -1)
                - 3.0 / 8.0 * ln(x) * pow(x, 2) * NC * pow(poly2, -2)
                + 5.0 / 8.0 * ln(x) * pow(x, 2) * NC * pow(poly2, -1)
                + 3.0 / 2.0 * ln(x) * pow(x, 2) * NC * pow(omxmz, -2)
                - 3.0 / 2.0 * ln(x) * pow(x, 2) * NC * pow(omxmz, -1)
                - 3.0 / 8.0 * ln(x) * pow(x, 3) * pow(NC, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * ln(x) * pow(x, 3) * pow(NC, -1) * pow(omxmz, -2)
                + 3.0 / 8.0 * ln(x) * pow(x, 3) * NC * pow(poly2, -2)
                - 1.0 / 2.0 * ln(x) * pow(x, 3) * NC * pow(poly2, -1)
                - 1.0 / 2.0 * ln(x) * pow(x, 3) * NC * pow(omxmz, -2)
                - 3.0 / 16.0 * ln(x) * pow(x, 4) * pow(NC, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(x) * pow(x, 4) * NC * pow(poly2, -2)
            )
            tmp += (
                +3.0 / 16.0 * ln(x) * pow(x, 5) * pow(NC, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(x) * pow(x, 5) * NC * pow(poly2, -2)
                - ln(x) * ln(1 - sqrtxz2 + x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 7.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 13.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1)
                - 3 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1)
                + 3 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 29.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 69.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1)
                + 69.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * NC * pow(sqrtxz2, -1)
                - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
            )
            tmp += (
                +9.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 111.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 9.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 11.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 9.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 9.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 7.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + ln(x) * ln(1 + sqrtxz2 + x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(z, -1) * NC * pow(sqrtxz2, -1)
            )
            tmp += (
                +3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 7.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 13.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1)
                + 3 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 3 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 29.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 69.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1)
                - 69.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * NC * pow(sqrtxz2, -1)
                + 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 9.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 111.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 9.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 11.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 9.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 9.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 7.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 2 * ln(x) * ln(1 + x) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(x) * ln(1 + x) * pow(NC, -1)
                - ln(x) * ln(1 + x) * NC
                - ln(x) * ln(1 + x) * z * pow(NC, -1)
                + ln(x) * ln(1 + x) * z * NC
                - 4 * ln(x) * ln(1 + x) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(1 + x) * x * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x) * x * NC
                - 2 * ln(x) * ln(1 + x) * x * z * pow(NC, -1)
            )
            tmp += (
                +2 * ln(x) * ln(1 + x) * x * z * NC
                - 2 * ln(x) * ln(1 + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(x) * ln(1 + x) * pow(x, 2) * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x) * pow(x, 2) * NC
                + 3 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 11.0 / 4.0 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * NC * pow(omz, -1)
                - pow(ln(x), 2) * pow(z, -1) * NC
                + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                - 19.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                + 33.0 / 4.0 * pow(ln(x), 2) * NC
                - 6 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1)
                + 5 * pow(ln(x), 2) * x * pow(z, -1) * NC * pow(omz, -1)
                - 4 * pow(ln(x), 2) * x * pow(z, -1) * NC
                - 6 * pow(ln(x), 2) * x * pow(NC, -1) * pow(omz, -1)
                + 13.0 / 2.0 * pow(ln(x), 2) * x * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(x), 2) * x * NC * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(x), 2) * x * NC
                + 2 * pow(ln(x), 2) * x * z * pow(NC, -1)
                - 2 * pow(ln(x), 2) * x * z * NC
                + 3 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, 2) * NC
                - 2 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 4.0 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1)
                + 3 * ln(x) * ln(z) * pow(z, -1) * NC * pow(omz, -1)
                + 3.0 / 4.0 * ln(x) * ln(z) * pow(z, -1) * NC
                - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 5.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * ln(z) * NC * pow(omz, -1)
                - 11.0 / 2.0 * ln(x) * ln(z) * NC
                + 1.0 / 2.0 * ln(x) * ln(z) * z * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(z) * z * NC
            )
            tmp += (
                +4 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 17.0 / 2.0 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1)
                - 6 * ln(x) * ln(z) * x * pow(z, -1) * NC * pow(omz, -1)
                + 5.0 / 2.0 * ln(x) * ln(z) * x * pow(z, -1) * NC
                + 8 * ln(x) * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                - 9 * ln(x) * ln(z) * x * pow(NC, -1)
                + ln(x) * ln(z) * x * NC * pow(omz, -1)
                + 9 * ln(x) * ln(z) * x * NC
                - 2 * ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(x) * ln(omx) * pow(z, -1) * NC * pow(omz, -1)
                + 4 * ln(x) * ln(omx) * pow(z, -1) * NC
                - 19.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 13.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1)
                + 7.0 / 2.0 * ln(x) * ln(omx) * NC * pow(omz, -1)
                - 11.0 / 2.0 * ln(x) * ln(omx) * NC
                + ln(x) * ln(omx) * z * pow(NC, -1)
                - ln(x) * ln(omx) * z * NC
                + 16 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * pow(z, -1) * NC * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * x * pow(z, -1) * NC
                + 19 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                - 13 * ln(x) * ln(omx) * x * pow(NC, -1)
                - 7 * ln(x) * ln(omx) * x * NC * pow(omz, -1)
                + 11 * ln(x) * ln(omx) * x * NC
                - 2 * ln(x) * ln(omx) * x * z * pow(NC, -1)
                + 2 * ln(x) * ln(omx) * x * z * NC
                - 5 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 7 * ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1)
                - ln(x) * ln(omx) * pow(x, 2) * NC
                - 7 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * pow(z, -1) * NC
                - 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 11.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1)
                + 3 * ln(x) * ln(omz) * NC * pow(omz, -1)
                - 21.0 / 2.0 * ln(x) * ln(omz) * NC
            )
            tmp += (
                +14 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 4 * ln(x) * ln(omz) * x * pow(z, -1) * NC
                + 12 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * x * pow(NC, -1)
                - 6 * ln(x) * ln(omz) * x * NC * pow(omz, -1)
                + 8 * ln(x) * ln(omz) * x * NC
                - ln(x) * ln(omz) * x * z * pow(NC, -1)
                + ln(x) * ln(omz) * x * z * NC
                - 5 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 3 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 13.0 / 8.0 * ln(z) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 6.0 * ln(z) * pow(z, -1) * NF
                - 4 * ln(z) * pow(z, -1) * NC * pow(omz, -1)
                + 69.0 / 8.0 * ln(z) * pow(z, -1) * NC
                - 3.0 / 16.0 * ln(z) * pow(NC, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * ln(z) * pow(NC, -1) * pow(poly2, -1)
                - 5.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 83.0 / 16.0 * ln(z) * pow(NC, -1)
                + 1.0 / 6.0 * ln(z) * NF * pow(omz, -1)
                + 3.0 / 16.0 * ln(z) * NC * pow(poly2, -2)
                + 7.0 / 8.0 * ln(z) * NC * pow(poly2, -1)
                + 7 * ln(z) * NC * pow(omz, -1)
                - 77.0 / 16.0 * ln(z) * NC
                - 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 4.0 * ln(z) * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * LMUF * NC * pow(omz, -1)
                - 1.0 / 4.0 * ln(z) * LMUF * NC
                + 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 4.0 * ln(z) * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * LMUA * NC * pow(omz, -1)
                + 3.0 / 4.0 * ln(z) * LMUA * NC
                + 9.0 / 8.0 * ln(z) * z * pow(NC, -1)
                - 9.0 / 8.0 * ln(z) * z * NC
                + 1.0 / 4.0 * ln(z) * z * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(z) * z * LMUF * NC
                - 1.0 / 4.0 * ln(z) * z * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * ln(z) * z * LMUA * NC
                - 8 * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(z) * x * pow(z, -1) * pow(NC, -1)
                + 8 * ln(z) * x * pow(z, -1) * NC * pow(omz, -1)
                - 10 * ln(z) * x * pow(z, -1) * NC
                - 3.0 / 16.0 * ln(z) * x * pow(NC, -1) * pow(poly2, -2)
            )
            tmp += (
                -1.0 / 2.0 * ln(z) * x * pow(NC, -1) * pow(poly2, -1)
                + 3 * ln(z) * x * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * x * pow(NC, -1) * pow(xmz, -1)
                + 187.0 / 16.0 * ln(z) * x * pow(NC, -1)
                + 3.0 / 16.0 * ln(z) * x * NC * pow(poly2, -2)
                + ln(z) * x * NC * pow(poly2, -1)
                - 8 * ln(z) * x * NC * pow(omz, -1)
                - 83.0 / 16.0 * ln(z) * x * NC
                + ln(z) * x * LMUF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * x * LMUF * pow(NC, -1)
                - ln(z) * x * LMUF * NC * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * x * LMUF * NC
                - ln(z) * x * LMUA * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * x * LMUA * pow(NC, -1)
                + ln(z) * x * LMUA * NC * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * x * LMUA * NC
                - 5.0 / 4.0 * ln(z) * x * z * pow(NC, -1)
                + 5.0 / 4.0 * ln(z) * x * z * NC
                - 1.0 / 2.0 * ln(z) * x * z * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * x * z * LMUF * NC
                + 1.0 / 2.0 * ln(z) * x * z * LMUA * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * x * z * LMUA * NC
                + 4 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 3.0 / 8.0 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(poly2, -2)
                - 1.0 / 8.0 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(poly2, -1)
                - 4 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - ln(z) * pow(x, 2) * pow(NC, -1) * pow(xmz, -1)
                - 3.0 / 8.0 * ln(z) * pow(x, 2) * NC * pow(poly2, -2)
                + 5.0 / 8.0 * ln(z) * pow(x, 2) * NC * pow(poly2, -1)
                + 3.0 / 8.0 * ln(z) * pow(x, 3) * pow(NC, -1) * pow(poly2, -2)
                - 3.0 / 8.0 * ln(z) * pow(x, 3) * NC * pow(poly2, -2)
                + 1.0 / 2.0 * ln(z) * pow(x, 3) * NC * pow(poly2, -1)
                - 3.0 / 16.0 * ln(z) * pow(x, 4) * pow(NC, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(z) * pow(x, 4) * NC * pow(poly2, -2)
                - 3.0 / 16.0 * ln(z) * pow(x, 5) * pow(NC, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(z) * pow(x, 5) * NC * pow(poly2, -2)
                + 5.0 / 4.0 * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                -1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * NC * pow(omz, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * pow(z, -1) * NC
                + pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC
                + 1.0 / 4.0 * pow(ln(z), 2) * z * pow(NC, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * z * NC
                - 5.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1)
                + pow(ln(z), 2) * x * pow(z, -1) * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * NC
                - 2 * pow(ln(z), 2) * x * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * x * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * x * NC * pow(omz, -1)
                - pow(ln(z), 2) * x * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * x * z * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * x * z * NC
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(z) * ln(omx) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 2.0 * ln(z) * ln(omx) * pow(z, -1) * NC
                + 4 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(omx) * pow(NC, -1)
                - 3.0 / 2.0 * ln(z) * ln(omx) * NC * pow(omz, -1)
                + 5.0 / 2.0 * ln(z) * ln(omx) * NC
                - 7 * ln(z) * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                + 3 * ln(z) * ln(omx) * x * pow(z, -1) * NC
                - 8 * ln(z) * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * x * pow(NC, -1)
                + 3 * ln(z) * ln(omx) * x * NC * pow(omz, -1)
                - 5 * ln(z) * ln(omx) * x * NC
                + 2 * ln(z) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 3 * ln(z) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 2.0 * ln(z) * ln(omz) * pow(z, -1) * NC
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1)
                - 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(omz, -1)
            )
            tmp += (
                +11.0 / 2.0 * ln(z) * ln(omz) * NC
                - 6 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 5 * ln(z) * ln(omz) * x * pow(z, -1) * NC
                - 8 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                + 7 * ln(z) * ln(omz) * x * pow(NC, -1)
                + 5 * ln(z) * ln(omz) * x * NC * pow(omz, -1)
                - 11 * ln(z) * ln(omz) * x * NC
                + ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 3 * ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 4.0 * ln(omx) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 6.0 * ln(omx) * pow(z, -1) * NF
                + 25.0 / 4.0 * ln(omx) * pow(z, -1) * NC
                + ln(omx) * pow(z, -1) * LMUF * NC
                + 3 * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omx) * pow(NC, -1)
                + 1.0 / 6.0 * ln(omx) * NF * pow(omz, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                - 14 * ln(omx) * NC
                + 1.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1)
                - 9.0 / 4.0 * ln(omx) * LMUF * NC
                + 1.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1)
                - 1.0 / 4.0 * ln(omx) * LMUA * NC
                - 3.0 / 8.0 * ln(omx) * z * pow(NC, -1)
                + 3.0 / 8.0 * ln(omx) * z * NC
                + 1.0 / 4.0 * ln(omx) * z * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(omx) * z * LMUF * NC
                + 1.0 / 4.0 * ln(omx) * z * LMUA * pow(NC, -1)
                - 1.0 / 4.0 * ln(omx) * z * LMUA * NC
                - 13.0 / 2.0 * ln(omx) * x * pow(z, -1) * pow(NC, -1)
                - 11.0 / 2.0 * ln(omx) * x * pow(z, -1) * NC
                - 2 * ln(omx) * x * pow(z, -1) * LMUF * NC
                - 8 * ln(omx) * x * pow(NC, -1) * pow(omz, -1)
                + 19.0 / 2.0 * ln(omx) * x * pow(NC, -1)
                + 2 * ln(omx) * x * NC * pow(omz, -1)
                + 21.0 / 2.0 * ln(omx) * x * NC
                - 1.0 / 2.0 * ln(omx) * x * LMUF * pow(NC, -1)
                + 9.0 / 2.0 * ln(omx) * x * LMUF * NC
                - 1.0 / 2.0 * ln(omx) * x * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * x * LMUA * NC
                + 3.0 / 4.0 * ln(omx) * x * z * pow(NC, -1)
                - 3.0 / 4.0 * ln(omx) * x * z * NC
                - 1.0 / 2.0 * ln(omx) * x * z * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * x * z * LMUF * NC
                - 1.0 / 2.0 * ln(omx) * x * z * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * x * z * LMUA * NC
            )
            tmp += (
                -ln(omx) * pow(x, 2) * pow(NC, -1)
                + 3 * pow(ln(omx), 2) * pow(z, -1) * pow(NC, -1)
                - 3.0 / 4.0 * pow(ln(omx), 2) * pow(z, -1) * NC
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 4.0 * pow(ln(omx), 2) * pow(NC, -1)
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                + 7.0 / 4.0 * pow(ln(omx), 2) * NC
                - 1.0 / 4.0 * pow(ln(omx), 2) * z * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * z * NC
                - 6 * pow(ln(omx), 2) * x * pow(z, -1) * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * NC
                - 6 * pow(ln(omx), 2) * x * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * pow(ln(omx), 2) * x * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * x * NC * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(omx), 2) * x * NC
                + 1.0 / 2.0 * pow(ln(omx), 2) * x * z * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * z * NC
                + 2 * pow(ln(omx), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * pow(ln(omx), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(omx) * ln(omz) * pow(z, -1) * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * pow(z, -1) * NC
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(omx) * ln(omz) * pow(NC, -1)
                - ln(omx) * ln(omz) * NC * pow(omz, -1)
                + 9.0 / 2.0 * ln(omx) * ln(omz) * NC
                - 1.0 / 2.0 * ln(omx) * ln(omz) * z * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * ln(omz) * z * NC
                - 9 * ln(omx) * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                + 4 * ln(omx) * ln(omz) * x * pow(z, -1) * NC
                - 8 * ln(omx) * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(omx) * ln(omz) * x * pow(NC, -1)
                + 2 * ln(omx) * ln(omz) * x * NC * pow(omz, -1)
                - 9 * ln(omx) * ln(omz) * x * NC
                + ln(omx) * ln(omz) * x * z * pow(NC, -1)
                - ln(omx) * ln(omz) * x * z * NC
                + 3 * ln(omx) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 2 * ln(omx) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 4.0 * ln(omz) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                +1.0 / 6.0 * ln(omz) * pow(z, -1) * NF
                + 23.0 / 4.0 * ln(omz) * pow(z, -1) * NC
                - 1.0 / 2.0 * ln(omz) * pow(z, -1) * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * pow(z, -1) * LMUA * NC
                + 2 * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(omxmz, -2)
                - ln(omz) * pow(NC, -1) * pow(omxmz, -1)
                + ln(omz) * pow(NC, -1)
                + 1.0 / 6.0 * ln(omz) * NF * pow(omz, -1)
                - ln(omz) * NC * pow(omz, -1)
                - 1.0 / 2.0 * ln(omz) * NC * pow(omxmz, -2)
                + 1.0 / 2.0 * ln(omz) * NC * pow(omxmz, -1)
                - 13 * ln(omz) * NC
                + 1.0 / 4.0 * ln(omz) * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(omz) * LMUF * NC
                + 5.0 / 4.0 * ln(omz) * LMUA * pow(NC, -1)
                - 5.0 / 4.0 * ln(omz) * LMUA * NC
                + 1.0 / 4.0 * ln(omz) * z * pow(NC, -1) * pow(omxmz, -2)
                - 2 * ln(omz) * z * pow(NC, -1) * pow(omxmz, -1)
                + 17.0 / 8.0 * ln(omz) * z * pow(NC, -1)
                - 1.0 / 4.0 * ln(omz) * z * NC * pow(omxmz, -2)
                + 7.0 / 2.0 * ln(omz) * z * NC * pow(omxmz, -1)
                - 25.0 / 8.0 * ln(omz) * z * NC
                + 1.0 / 4.0 * ln(omz) * z * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(omz) * z * LMUF * NC
                + 1.0 / 4.0 * ln(omz) * z * LMUA * pow(NC, -1)
                - 1.0 / 4.0 * ln(omz) * z * LMUA * NC
                - 3.0 / 4.0 * ln(omz) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -2)
                + 5.0 / 2.0 * ln(omz) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -1)
                + 3.0 / 4.0 * ln(omz) * pow(z, 2) * NC * pow(omxmz, -2)
                - 7.0 / 2.0 * ln(omz) * pow(z, 2) * NC * pow(omxmz, -1)
                - 9.0 / 2.0 * ln(omz) * x * pow(z, -1) * pow(NC, -1)
                - 7.0 / 2.0 * ln(omz) * x * pow(z, -1) * NC
                + ln(omz) * x * pow(z, -1) * LMUA * pow(NC, -1)
                - ln(omz) * x * pow(z, -1) * LMUA * NC
                - 6 * ln(omz) * x * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(omz) * x * pow(NC, -1) * pow(omxmz, -2)
                + 3 * ln(omz) * x * pow(NC, -1) * pow(omxmz, -1)
                + 5.0 / 2.0 * ln(omz) * x * pow(NC, -1)
                + 4 * ln(omz) * x * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(omz) * x * NC * pow(omxmz, -2)
                - 3 * ln(omz) * x * NC * pow(omxmz, -1)
            )
            tmp += (
                +13.0 / 2.0 * ln(omz) * x * NC
                - 1.0 / 2.0 * ln(omz) * x * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * x * LMUF * NC
                - 5.0 / 2.0 * ln(omz) * x * LMUA * pow(NC, -1)
                + 5.0 / 2.0 * ln(omz) * x * LMUA * NC
                + 3.0 / 4.0 * ln(omz) * x * z * pow(NC, -1)
                - 3.0 / 4.0 * ln(omz) * x * z * NC
                - 1.0 / 2.0 * ln(omz) * x * z * LMUF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * x * z * LMUF * NC
                - 1.0 / 2.0 * ln(omz) * x * z * LMUA * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * x * z * LMUA * NC
                + 3.0 / 2.0 * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -2)
                - 3.0 / 2.0 * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -1)
                - 3.0 / 2.0 * ln(omz) * pow(x, 2) * NC * pow(omxmz, -2)
                + 3.0 / 2.0 * ln(omz) * pow(x, 2) * NC * pow(omxmz, -1)
                - 1.0 / 2.0 * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(omxmz, -2)
                + 1.0 / 2.0 * ln(omz) * pow(x, 3) * NC * pow(omxmz, -2)
                + 5.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1)
                - 5.0 / 4.0 * pow(ln(omz), 2) * pow(z, -1) * NC
                + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(ln(omz), 2) * pow(NC, -1)
                - pow(ln(omz), 2) * NC * pow(omz, -1)
                + 11.0 / 4.0 * pow(ln(omz), 2) * NC
                - 1.0 / 4.0 * pow(ln(omz), 2) * z * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omz), 2) * z * NC
                - 5 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * NC
                - 3 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * x * pow(NC, -1)
                + 2 * pow(ln(omz), 2) * x * NC * pow(omz, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * x * NC
                + 1.0 / 2.0 * pow(ln(omz), 2) * x * z * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * x * z * NC
                + 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
            )
            tmp += (
                -3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 13.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * NC * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 29.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 69.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(NC, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +69.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * NC * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 111.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 11.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 7.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 13.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
            )
            tmp += (
                +Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 29.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 69.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(NC, -1) * pow(sqrtxz2, -1)
                - 69.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * NC * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
            )
            tmp += (
                -111.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 11.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 7.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                -1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 13.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 29.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 69.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * NC * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1)
                - 69.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * NC * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                -Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 111.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 11.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 7.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                +3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 7.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 13.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 29.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 69.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * NC * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +69.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * NC * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 111.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 11.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * NC * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 9.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 9.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -7.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 2 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * pow(NC, -1)
                + Li2(1 - x * pow(z, -1)) * pow(z, -1) * NC * pow(omz, -1)
                - 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * NC
                + 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * NC * pow(omz, -1)
                - 3.0 / 2.0 * Li2(1 - x * pow(z, -1)) * NC
                + 4 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                - 3 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * NC * pow(omz, -1)
                + Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * NC
                - Li2(1 - x * pow(z, -1)) * x * pow(NC, -1) * pow(omz, -1)
                - Li2(1 - x * pow(z, -1)) * x * pow(NC, -1)
                + Li2(1 - x * pow(z, -1)) * x * NC * pow(omz, -1)
                + 3 * Li2(1 - x * pow(z, -1)) * x * NC
                - 2 * Li2(1 - x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(-x) * pow(z, -1) * pow(NC, -1)
                + 2 * Li2(-x) * pow(NC, -1)
                - Li2(-x) * NC
                - Li2(-x) * z * pow(NC, -1)
                + Li2(-x) * z * NC
                - 4 * Li2(-x) * x * pow(z, -1) * pow(NC, -1)
                + 4 * Li2(-x) * x * pow(NC, -1)
                - 2 * Li2(-x) * x * NC
                - 2 * Li2(-x) * x * z * pow(NC, -1)
                + 2 * Li2(-x) * x * z * NC
                - 2 * Li2(-x) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
            )
            tmp += (
                +2 * Li2(-x) * pow(x, 2) * pow(NC, -1)
                - 2 * Li2(-x) * pow(x, 2) * NC
                - 1.0 / 2.0 * Li2(x) * pow(z, -1) * pow(NC, -1)
                - 2 * Li2(x) * pow(z, -1) * NC * pow(omz, -1)
                - 1.0 / 2.0 * Li2(x) * pow(z, -1) * NC
                - 2 * Li2(x) * pow(NC, -1) * pow(omz, -1)
                + Li2(x) * pow(NC, -1)
                + 2 * Li2(x) * NC * pow(omz, -1)
                + 4 * Li2(x) * NC
                + Li2(x) * z * pow(NC, -1)
                - Li2(x) * z * NC
                + Li2(x) * x * pow(z, -1) * pow(NC, -1)
                + 4 * Li2(x) * x * pow(z, -1) * NC * pow(omz, -1)
                - 5 * Li2(x) * x * pow(z, -1) * NC
                + 4 * Li2(x) * x * pow(NC, -1) * pow(omz, -1)
                - 3 * Li2(x) * x * pow(NC, -1)
                - 4 * Li2(x) * x * NC * pow(omz, -1)
                + 5 * Li2(x) * x * NC
                - Li2(x) * x * z * pow(NC, -1)
                + Li2(x) * x * z * NC
                - 2 * Li2(x) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
                + Li2(x) * pow(x, 2) * pow(NC, -1)
                - Li2(x) * pow(x, 2) * NC
                - 1.0 / 2.0 * Li2(z) * pow(z, -1) * NC
                + Li2(z) * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(z) * NC * pow(omz, -1)
                + 2 * Li2(z) * NC
                + Li2(z) * x * pow(z, -1) * NC
                - 2 * Li2(z) * x * pow(NC, -1) * pow(omz, -1)
                + 4 * Li2(z) * x * pow(NC, -1)
                + Li2(z) * x * NC * pow(omz, -1)
                - 4 * Li2(z) * x * NC
                - Li2(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1)
                + Li2(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1)
            )

            res += tmp

        return res
