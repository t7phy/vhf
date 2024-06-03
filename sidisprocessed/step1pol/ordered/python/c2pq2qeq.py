from core.definitions import CF, NC, TR, NF, ZETA3, ZETA2
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi


def C2Pq2qEq(inx, inz, cx, cz, Q, muR, muF, muA, orders: list, ndecimals):
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
            res += (
                +(-1) * 511.0 / 32.0 * CF * pow(NC, -1)
                + 127.0 / 24.0 * CF * NF
                + (-1) * 1537.0 / 96.0 * CF * NC
                + 15.0 / 2.0 * ZETA3 * CF * pow(NC, -1)
                + 2.0 / 3.0 * ZETA3 * CF * NF
                + 41.0 / 6.0 * ZETA3 * CF * NC
                + (-1) * 29.0 / 24.0 * pow(pi, 2) * CF * pow(NC, -1)
                + 19.0 / 54.0 * pow(pi, 2) * CF * NF
                + (-1) * 277.0 / 216.0 * pow(pi, 2) * CF * NC
                + 7.0 / 180.0 * pow(pi, 4) * CF * pow(NC, -1)
                + 1.0 / 18.0 * pow(pi, 4) * CF * NC
                + 0
            )
        if ("001" in orders) or ("all" in orders):
            res += (-1) * 93.0 / 16.0 * LMUA * CF * pow(NC, -1) + 1.0 / 12.0 * LMUA * CF * NF + 245.0 / 48.0 * LMUA * CF * NC + 5 * ZETA3 * LMUA * CF * pow(NC, -1) + (-1) * 2 * ZETA3 * LMUA * CF * NC + (-1) * 1.0 / 4.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1) + 1.0 / 9.0 * pow(pi, 2) * LMUA * CF * NF + (-1) * 13.0 / 36.0 * pow(pi, 2) * LMUA * CF * NC + 0
        if ("002" in orders) or ("all" in orders):
            res += (-1) * 9.0 / 16.0 * pow(LMUA, 2) * CF * pow(NC, -1) + (-1) * 1.0 / 4.0 * pow(LMUA, 2) * CF * NF + 31.0 / 16.0 * pow(LMUA, 2) * CF * NC + 1.0 / 6.0 * pow(pi, 2) * pow(LMUA, 2) * CF * pow(NC, -1) + (-1) * 1.0 / 6.0 * pow(pi, 2) * pow(LMUA, 2) * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += (-1) * 93.0 / 16.0 * LMUF * CF * pow(NC, -1) + 1.0 / 12.0 * LMUF * CF * NF + 245.0 / 48.0 * LMUF * CF * NC + 5 * ZETA3 * LMUF * CF * pow(NC, -1) + (-1) * 2 * ZETA3 * LMUF * CF * NC + (-1) * 1.0 / 4.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1) + 1.0 / 9.0 * pow(pi, 2) * LMUF * CF * NF + (-1) * 13.0 / 36.0 * pow(pi, 2) * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += (-1) * 9.0 / 8.0 * LMUA * LMUF * CF * pow(NC, -1) + 9.0 / 8.0 * LMUA * LMUF * CF * NC + 0
        if ("020" in orders) or ("all" in orders):
            res += (-1) * 9.0 / 16.0 * pow(LMUF, 2) * CF * pow(NC, -1) + (-1) * 1.0 / 4.0 * pow(LMUF, 2) * CF * NF + 31.0 / 16.0 * pow(LMUF, 2) * CF * NC + 1.0 / 6.0 * pow(pi, 2) * pow(LMUF, 2) * CF * pow(NC, -1) + (-1) * 1.0 / 6.0 * pow(pi, 2) * pow(LMUF, 2) * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += 8.0 / 3.0 * LMUR * CF * NF + (-1) * 44.0 / 3.0 * LMUR * CF * NC + 0
        if ("101" in orders) or ("all" in orders):
            res += 1.0 / 2.0 * LMUA * LMUR * CF * NF + (-1) * 11.0 / 4.0 * LMUA * LMUR * CF * NC + 0
        if ("110" in orders) or ("all" in orders):
            res += 1.0 / 2.0 * LMUF * LMUR * CF * NF + (-1) * 11.0 / 4.0 * LMUF * LMUR * CF * NC + 0
        return res

    if cx == "D" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 28.0 / 27.0 * CF * NF + (-1) * 202.0 / 27.0 * CF * NC + (-1) * 4 * ZETA3 * CF * pow(NC, -1) + 11 * ZETA3 * CF * NC + (-1) * 1.0 / 9.0 * pow(pi, 2) * CF * NF + 11.0 / 18.0 * pow(pi, 2) * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += (-1) * 8 * LMUA * CF * pow(NC, -1) + 10.0 / 9.0 * LMUA * CF * NF + 5.0 / 9.0 * LMUA * CF * NC + (-1) * 1.0 / 3.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1) + 2.0 / 3.0 * pow(pi, 2) * LMUA * CF * NC + 0
        if ("002" in orders) or ("all" in orders):
            res += (-1) * 3.0 / 2.0 * pow(LMUA, 2) * CF * pow(NC, -1) + (-1) * 1.0 / 3.0 * pow(LMUA, 2) * CF * NF + 10.0 / 3.0 * pow(LMUA, 2) * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += (-1) * 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1) + 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += (-1) * 3.0 / 2.0 * LMUA * LMUF * CF * pow(NC, -1) + 3.0 / 2.0 * LMUA * LMUF * CF * NC + 0
        if ("101" in orders) or ("all" in orders):
            res += 2.0 / 3.0 * LMUA * LMUR * CF * NF + (-1) * 11.0 / 3.0 * LMUA * LMUR * CF * NC + 0
        return res

    if cx == "D" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 8 * CF * pow(NC, -1) + (-1) * 10.0 / 9.0 * CF * NF + (-1) * 5.0 / 9.0 * CF * NC + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) + (-1) * pow(pi, 2) * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * LMUA * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * LMUA * CF * NC + 0
        if ("002" in orders) or ("all" in orders):
            res += (-1) * 2 * pow(LMUA, 2) * CF * pow(NC, -1) + 2 * pow(LMUA, 2) * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * LMUF * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += (-1) * 2.0 / 3.0 * LMUR * CF * NF + 11.0 / 3.0 * LMUR * CF * NC + 0
        return res

    if cx == "D" and cz == "2":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 1.0 / 3.0 * CF * NF + (-1) * 11.0 / 6.0 * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += 3 * LMUA * CF * pow(NC, -1) + (-1) * 3 * LMUA * CF * NC + 0
        return res

    if cx == "D" and cz == "3":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += +(-1) * CF * pow(NC, -1) + CF * NC + 0
        return res

    if cx == "0" and cz == "D":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 28.0 / 27.0 * CF * NF + (-1) * 202.0 / 27.0 * CF * NC + (-1) * 4 * ZETA3 * CF * pow(NC, -1) + 11 * ZETA3 * CF * NC + (-1) * 1.0 / 9.0 * pow(pi, 2) * CF * NF + 11.0 / 18.0 * pow(pi, 2) * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += (-1) * 1.0 / 3.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1) + 1.0 / 3.0 * pow(pi, 2) * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += (-1) * 8 * LMUF * CF * pow(NC, -1) + 10.0 / 9.0 * LMUF * CF * NF + 5.0 / 9.0 * LMUF * CF * NC + (-1) * 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1) + 2.0 / 3.0 * pow(pi, 2) * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += (-1) * 3.0 / 2.0 * LMUA * LMUF * CF * pow(NC, -1) + 3.0 / 2.0 * LMUA * LMUF * CF * NC + 0
        if ("020" in orders) or ("all" in orders):
            res += (-1) * 3.0 / 2.0 * pow(LMUF, 2) * CF * pow(NC, -1) + (-1) * 1.0 / 3.0 * pow(LMUF, 2) * CF * NF + 10.0 / 3.0 * pow(LMUF, 2) * CF * NC + 0
        if ("110" in orders) or ("all" in orders):
            res += 2.0 / 3.0 * LMUF * LMUR * CF * NF + (-1) * 11.0 / 3.0 * LMUF * LMUR * CF * NC + 0
        return res

    if cx == "0" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 8 * CF * pow(NC, -1) + (-1) * 10.0 / 9.0 * CF * NF + (-1) * 5.0 / 9.0 * CF * NC + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) + (-1) * pow(pi, 2) * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * LMUA * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += (-1) * 2 * LMUA * LMUF * CF * pow(NC, -1) + 2 * LMUA * LMUF * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += (-1) * 2.0 / 3.0 * LMUR * CF * NF + 11.0 / 3.0 * LMUR * CF * NC + 0
        return res

    if cx == "0" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 2.0 / 3.0 * CF * NF + (-1) * 11.0 / 3.0 * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += 4 * LMUA * CF * pow(NC, -1) + (-1) * 4 * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 2 * LMUF * CF * pow(NC, -1) + (-1) * 2 * LMUF * CF * NC + 0
        return res

    if cx == "0" and cz == "2":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += +(-1) * 3 * CF * pow(NC, -1) + 3 * CF * NC + 0
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
            res += 8 * CF * pow(NC, -1) + (-1) * 10.0 / 9.0 * CF * NF + (-1) * 5.0 / 9.0 * CF * NC + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) + (-1) * pow(pi, 2) * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * LMUA * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * LMUF * CF * NC + 0
        if ("020" in orders) or ("all" in orders):
            res += (-1) * 2 * pow(LMUF, 2) * CF * pow(NC, -1) + 2 * pow(LMUF, 2) * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += (-1) * 2.0 / 3.0 * LMUR * CF * NF + 11.0 / 3.0 * LMUR * CF * NC + 0
        return res

    if cx == "1" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 2.0 / 3.0 * CF * NF + (-1) * 11.0 / 3.0 * CF * NC + 0
        if ("001" in orders) or ("all" in orders):
            res += 2 * LMUA * CF * pow(NC, -1) + (-1) * 2 * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 4 * LMUF * CF * pow(NC, -1) + (-1) * 4 * LMUF * CF * NC + 0
        return res

    if cx == "1" and cz == "1":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += +(-1) * 6 * CF * pow(NC, -1) + 6 * CF * NC + 0
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
            res += 1.0 / 3.0 * CF * NF + (-1) * 11.0 / 6.0 * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 3 * LMUF * CF * pow(NC, -1) + (-1) * 3 * LMUF * CF * NC + 0
        return res

    if cx == "2" and cz == "0":

        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += +(-1) * 3 * CF * pow(NC, -1) + 3 * CF * NC + 0
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
            res += +(-1) * CF * pow(NC, -1) + CF * NC + 0
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
            res += (
                +(-1) * 107.0 / 108.0 * pow(z, -1) * CF
                + (-1) * 1.0 / 4.0 * CF * pow(NC, -1)
                + (-1) * 11.0 / 9.0 * CF
                + (-1) * 19.0 / 54.0 * CF * NF
                + 197.0 / 108.0 * CF * NC
                + 1.0 / 4.0 * z * CF * pow(NC, -1)
                + (-1) * 4.0 / 9.0 * z * CF
                + (-1) * 37.0 / 54.0 * z * CF * NF
                + 611.0 / 108.0 * z * CF * NC
                + 287.0 / 108.0 * pow(z, 2) * CF
                + 10 * ZETA3 * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 4 * ZETA3 * CF * pow(NC, -1)
                + 2 * ZETA3 * CF
                + (-1) * 14 * ZETA3 * CF * NC * pow(omz, -1)
                + 5.0 / 2.0 * ZETA3 * CF * NC
                + (-1) * 4 * ZETA3 * z * CF * pow(NC, -1)
                + 2 * ZETA3 * z * CF
                + 5.0 / 2.0 * ZETA3 * z * CF * NC
                + (-1) * 1.0 / 4.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * CF
                + 0
            )
            res += (
                +1.0 / 18.0 * pow(pi, 2) * CF * NF
                + 1.0 / 4.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
                + (-1) * 29.0 / 36.0 * pow(pi, 2) * CF * NC
                + 1.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + (-1) * 1.0 / 4.0 * pow(pi, 2) * z * CF
                + 1.0 / 18.0 * pow(pi, 2) * z * CF * NF
                + (-1) * 2.0 / 9.0 * pow(pi, 2) * z * CF * NC
                + (-1) * 7.0 / 18.0 * ln(z) * pow(z, -1) * CF
                + 19.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 15.0 / 4.0 * ln(z) * CF * pow(NC, -1)
                + (-1) * 5 * ln(z) * CF
                + (-1) * 5.0 / 9.0 * ln(z) * CF * NF * pow(omz, -1)
                + (-1) * 1.0 / 18.0 * ln(z) * CF * NF
                + (-1) * 113.0 / 18.0 * ln(z) * CF * NC * pow(omz, -1)
                + 233.0 / 36.0 * ln(z) * CF * NC
                + 0
            )
            res += (
                +(-1) * 29.0 / 4.0 * ln(z) * z * CF * pow(NC, -1)
                + (-1) * 9.0 / 2.0 * ln(z) * z * CF
                + 11.0 / 18.0 * ln(z) * z * CF * NF
                + 101.0 / 36.0 * ln(z) * z * CF * NC
                + (-1) * 31.0 / 18.0 * ln(z) * pow(z, 2) * CF
                + 1.0 / 2.0 * ln(z) * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 1.0 / 3.0 * ln(z) * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF
                + (-1) * 5.0 / 6.0 * ln(z) * pow(pi, 2) * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * pow(pi, 2) * CF * NC
                + (-1) * 1.0 / 3.0 * ln(z) * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * ln(z) * pow(pi, 2) * z * CF
                + 1.0 / 2.0 * ln(z) * pow(pi, 2) * z * CF * NC
                + 1.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF
                + (-1) * 9.0 / 8.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 21.0 / 8.0 * pow(ln(z), 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 8.0 * pow(ln(z), 2) * CF
                + (-1) * 1.0 / 6.0 * pow(ln(z), 2) * CF * NF * pow(omz, -1)
                + 1.0 / 12.0 * pow(ln(z), 2) * CF * NF
                + 49.0 / 24.0 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
                + (-1) * 25.0 / 12.0 * pow(ln(z), 2) * CF * NC
                + 7.0 / 8.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                + (-1) * 5.0 / 8.0 * pow(ln(z), 2) * z * CF
                + 1.0 / 12.0 * pow(ln(z), 2) * z * CF * NF
                + 0
            )
            res += (
                +(-1) * 5.0 / 6.0 * pow(ln(z), 2) * z * CF * NC
                + 5.0 / 3.0 * pow(ln(z), 3) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 25.0 / 24.0 * pow(ln(z), 3) * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(z), 3) * CF
                + (-1) * 5.0 / 6.0 * pow(ln(z), 3) * CF * NC * pow(omz, -1)
                + 5.0 / 8.0 * pow(ln(z), 3) * CF * NC
                + (-1) * 25.0 / 24.0 * pow(ln(z), 3) * z * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(z), 3) * z * CF
                + 5.0 / 8.0 * pow(ln(z), 3) * z * CF * NC
                + 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * CF * NC * pow(omz, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * CF * NC
                + (-1) * 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * z * CF * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * z * CF * NC
                + (-1) * 3.0 / 2.0 * ln(z) * ln(omz) * CF * pow(NC, -1)
                + 3.0 / 2.0 * ln(z) * ln(omz) * CF * NC
                + 3.0 / 2.0 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(z) * ln(omz) * z * CF * NC
                + (-1) * 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + ln(z) * pow(ln(omz), 2) * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF
                + 5.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
                + (-1) * 2 * ln(z) * pow(ln(omz), 2) * CF * NC
                + ln(z) * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * z * CF
                + (-1) * 2 * ln(z) * pow(ln(omz), 2) * z * CF * NC
                + 4 * ln(z) * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 2 * ln(z) * Li2(z) * CF * pow(NC, -1)
                + 0
            )
            res += (
                +(-1) * 6 * ln(z) * Li2(z) * CF * NC * pow(omz, -1)
                + 3 * ln(z) * Li2(z) * CF * NC
                + (-1) * 2 * ln(z) * Li2(z) * z * CF * pow(NC, -1)
                + 3 * ln(z) * Li2(z) * z * CF * NC
                + (-1) * 7.0 / 18.0 * ln(omz) * pow(z, -1) * CF
                + (-1) * 5.0 / 4.0 * ln(omz) * CF * pow(NC, -1)
                + (-1) * 10.0 / 3.0 * ln(omz) * CF
                + 2.0 / 9.0 * ln(omz) * CF * NF
                + 67.0 / 36.0 * ln(omz) * CF * NC
                + (-1) * 7 * ln(omz) * z * CF * pow(NC, -1)
                + 7.0 / 3.0 * ln(omz) * z * CF
                + 8.0 / 9.0 * ln(omz) * z * CF * NF
                + (-1) * 14.0 / 9.0 * ln(omz) * z * CF * NC
                + 25.0 / 18.0 * ln(omz) * pow(z, 2) * CF
                + (-1) * 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 5.0 / 12.0 * ln(omz) * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * CF
                + (-1) * 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF * NC * pow(omz, -1)
                + 3.0 / 4.0 * ln(omz) * pow(pi, 2) * CF * NC
                + (-1) * 5.0 / 12.0 * ln(omz) * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * z * CF
                + 3.0 / 4.0 * ln(omz) * pow(pi, 2) * z * CF * NC
                + 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF
                + 1.0 / 4.0 * pow(ln(omz), 2) * CF
                + (-1) * 1.0 / 6.0 * pow(ln(omz), 2) * CF * NF
                + 0
            )
            res += (
                +11.0 / 12.0 * pow(ln(omz), 2) * CF * NC
                + (-1) * 1.0 / 4.0 * pow(ln(omz), 2) * z * CF
                + (-1) * 1.0 / 6.0 * pow(ln(omz), 2) * z * CF * NF
                + 11.0 / 12.0 * pow(ln(omz), 2) * z * CF * NC
                + (-1) * 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF
                + 1.0 / 2.0 * pow(ln(omz), 3) * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(omz), 3) * CF * NC
                + 1.0 / 2.0 * pow(ln(omz), 3) * z * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(omz), 3) * z * CF * NC
                + 1.0 / 2.0 * ln(omz) * Li2(1 - z) * CF * pow(NC, -1)
                + (-1) * ln(omz) * Li2(1 - z) * CF
                + (-1) * 1.0 / 2.0 * ln(omz) * Li2(1 - z) * CF * NC
                + 1.0 / 2.0 * ln(omz) * Li2(1 - z) * z * CF * pow(NC, -1)
                + (-1) * ln(omz) * Li2(1 - z) * z * CF
                + (-1) * 1.0 / 2.0 * ln(omz) * Li2(1 - z) * z * CF * NC
                + ln(omz) * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(omz) * Li2(z) * CF * pow(NC, -1)
                + (-1) * 2 * ln(omz) * Li2(z) * CF
                + ln(omz) * Li2(z) * CF * NC * pow(omz, -1)
                + (-1) * 3.0 / 2.0 * ln(omz) * Li2(z) * CF * NC
                + 1.0 / 2.0 * ln(omz) * Li2(z) * z * CF * pow(NC, -1)
                + (-1) * 2 * ln(omz) * Li2(z) * z * CF
                + (-1) * 3.0 / 2.0 * ln(omz) * Li2(z) * z * CF * NC
                + 3 * Li3(1 - z) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * Li3(1 - z) * CF * pow(NC, -1)
                + (-1) * Li3(1 - z) * CF
                + 3 * Li3(1 - z) * CF * NC * pow(omz, -1)
                + (-1) * 2 * Li3(1 - z) * CF * NC
                + (-1) * Li3(1 - z) * z * CF * pow(NC, -1)
                + (-1) * Li3(1 - z) * z * CF
                + (-1) * 2 * Li3(1 - z) * z * CF * NC
                + (-1) * 10 * Li3(z) * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * Li3(z) * CF * pow(NC, -1)
                + (-1) * 2 * Li3(z) * CF
                + 14 * Li3(z) * CF * NC * pow(omz, -1)
                + (-1) * 8 * Li3(z) * CF * NC
                + 6 * Li3(z) * z * CF * pow(NC, -1)
                + (-1) * 2 * Li3(z) * z * CF
                + (-1) * 8 * Li3(z) * z * CF * NC
                + (-1) * 2.0 / 3.0 * Li2(z) * pow(z, -1) * CF
                + 3.0 / 2.0 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 9.0 / 2.0 * Li2(z) * CF * pow(NC, -1)
                + 0
            )
            res += +1.0 / 2.0 * Li2(z) * CF + (-1) * 3.0 / 2.0 * Li2(z) * CF * NC * pow(omz, -1) + 7.0 / 2.0 * Li2(z) * CF * NC + 2 * Li2(z) * z * CF + (-1) * Li2(z) * z * CF * NC + 2.0 / 3.0 * Li2(z) * pow(z, 2) * CF + 0
        if ("001" in orders) or ("all" in orders):
            res += 7.0 / 18.0 * pow(z, -1) * LMUA * CF + 7.0 / 4.0 * LMUA * CF * pow(NC, -1) + 10.0 / 3.0 * LMUA * CF + 1.0 / 9.0 * LMUA * CF * NF + (-1) * 169.0 / 36.0 * LMUA * CF * NC + 25.0 / 4.0 * z * LMUA * CF * pow(NC, -1) + (-1) * 7.0 / 3.0 * z * LMUA * CF + (-1) * 11.0 / 9.0 * z * LMUA * CF * NF + 149.0 / 36.0 * z * LMUA * CF * NC + (-1) * 25.0 / 18.0 * pow(z, 2) * LMUA * CF + 0
            res += (
                1.0 / 4.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUA * CF
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * LMUA * CF * NC
                + 1.0 / 4.0 * pow(pi, 2) * z * LMUA * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * z * LMUA * CF
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * z * LMUA * CF * NC
                + (-1) * 2.0 / 3.0 * ln(z) * pow(z, -1) * LMUA * CF
                + 3 * ln(z) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 17.0 / 4.0 * ln(z) * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * LMUA * CF
                + 2.0 / 3.0 * ln(z) * LMUA * CF * NF * pow(omz, -1)
                + (-1) * 1.0 / 3.0 * ln(z) * LMUA * CF * NF
                + (-1) * 20.0 / 3.0 * ln(z) * LMUA * CF * NC * pow(omz, -1)
                + 61.0 / 12.0 * ln(z) * LMUA * CF * NC
                + 0
            )
            res += (
                (-1) * 7.0 / 4.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
                + 2 * ln(z) * z * LMUA * CF
                + (-1) * 1.0 / 3.0 * ln(z) * z * LMUA * CF * NF
                + 31.0 / 12.0 * ln(z) * z * LMUA * CF * NC
                + 2.0 / 3.0 * ln(z) * pow(z, 2) * LMUA * CF
                + (-1) * 3 * pow(ln(z), 2) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * pow(ln(z), 2) * LMUA * CF * pow(NC, -1)
                + (-1) * pow(ln(z), 2) * LMUA * CF
                + 2 * pow(ln(z), 2) * LMUA * CF * NC * pow(omz, -1)
                + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * LMUA * CF * NC
                + 0
            )
            res += (
                2 * pow(ln(z), 2) * z * LMUA * CF * pow(NC, -1)
                + (-1) * pow(ln(z), 2) * z * LMUA * CF
                + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * z * LMUA * CF * NC
                + 2 * ln(z) * ln(omz) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * ln(z) * ln(omz) * LMUA * CF * pow(NC, -1)
                + (-1) * 2 * ln(z) * ln(omz) * LMUA * CF * NC * pow(omz, -1)
                + ln(z) * ln(omz) * LMUA * CF * NC
                + (-1) * ln(z) * ln(omz) * z * LMUA * CF * pow(NC, -1)
                + ln(z) * ln(omz) * z * LMUA * CF * NC
                + 0
            )
            res += (-1) * 2.0 / 3.0 * ln(omz) * pow(z, -1) * LMUA * CF + (-1) * 3.0 / 4.0 * ln(omz) * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * CF + 3.0 / 4.0 * ln(omz) * LMUA * CF * NC + (-1) * 3.0 / 4.0 * ln(omz) * z * LMUA * CF * pow(NC, -1) + 1.0 / 2.0 * ln(omz) * z * LMUA * CF + 3.0 / 4.0 * ln(omz) * z * LMUA * CF * NC + 2.0 / 3.0 * ln(omz) * pow(z, 2) * LMUA * CF + 0
            res += (-1) * 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * CF * pow(NC, -1) + 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * CF * NC + (-1) * 3.0 / 2.0 * pow(ln(omz), 2) * z * LMUA * CF * pow(NC, -1) + 3.0 / 2.0 * pow(ln(omz), 2) * z * LMUA * CF * NC + 0
            res += (-1) * 1.0 / 2.0 * Li2(z) * LMUA * CF * pow(NC, -1) + Li2(z) * LMUA * CF + 1.0 / 2.0 * Li2(z) * LMUA * CF * NC + (-1) * 1.0 / 2.0 * Li2(z) * z * LMUA * CF * pow(NC, -1) + Li2(z) * z * LMUA * CF + 1.0 / 2.0 * Li2(z) * z * LMUA * CF * NC + 0
        if ("002" in orders) or ("all" in orders):
            res += (
                1.0 / 3.0 * pow(z, -1) * pow(LMUA, 2) * CF
                + 5.0 / 4.0 * pow(LMUA, 2) * CF * pow(NC, -1)
                + 1.0 / 4.0 * pow(LMUA, 2) * CF
                + 1.0 / 6.0 * pow(LMUA, 2) * CF * NF
                + (-1) * 13.0 / 6.0 * pow(LMUA, 2) * CF * NC
                + 1.0 / 4.0 * z * pow(LMUA, 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 4.0 * z * pow(LMUA, 2) * CF
                + 1.0 / 6.0 * z * pow(LMUA, 2) * CF * NF
                + (-1) * 7.0 / 6.0 * z * pow(LMUA, 2) * CF * NC
                + (-1) * 1.0 / 3.0 * pow(z, 2) * pow(LMUA, 2) * CF
                + 0
            )
            res += ln(z) * pow(LMUA, 2) * CF * pow(NC, -1) * pow(omz, -1) + (-1) * 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * CF * pow(NC, -1) + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF + 0
            res += (-1) * ln(z) * pow(LMUA, 2) * CF * NC * pow(omz, -1) + 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * CF * NC + (-1) * 3.0 / 4.0 * ln(z) * z * pow(LMUA, 2) * CF * pow(NC, -1) + 1.0 / 2.0 * ln(z) * z * pow(LMUA, 2) * CF + 3.0 / 4.0 * ln(z) * z * pow(LMUA, 2) * CF * NC + 0
            res += ln(omz) * pow(LMUA, 2) * CF * pow(NC, -1) + (-1) * ln(omz) * pow(LMUA, 2) * CF * NC + ln(omz) * z * pow(LMUA, 2) * CF * pow(NC, -1) + (-1) * ln(omz) * z * pow(LMUA, 2) * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 3.0 / 4.0 * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 4.0 * LMUF * CF * NC + (-1) * 3.0 / 4.0 * z * LMUF * CF * pow(NC, -1) + 3.0 / 4.0 * z * LMUF * CF * NC + 0
            res += (
                1.0 / 6.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUF * CF * NC
                + 1.0 / 6.0 * pow(pi, 2) * z * LMUF * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * z * LMUF * CF * NC
                + 3.0 / 2.0 * ln(z) * LMUF * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 3.0 / 4.0 * ln(z) * LMUF * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(z) * LMUF * CF * NC * pow(omz, -1)
                + 3.0 / 4.0 * ln(z) * LMUF * CF * NC
                + 0
            )
            res += (-1) * 3.0 / 4.0 * ln(z) * z * LMUF * CF * pow(NC, -1) + 3.0 / 4.0 * ln(z) * z * LMUF * CF * NC + 0
            res += (-1) * 3.0 / 4.0 * ln(omz) * LMUF * CF * pow(NC, -1) + 3.0 / 4.0 * ln(omz) * LMUF * CF * NC + (-1) * 3.0 / 4.0 * ln(omz) * z * LMUF * CF * pow(NC, -1) + 3.0 / 4.0 * ln(omz) * z * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += 3.0 / 4.0 * LMUA * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 4.0 * LMUA * LMUF * CF * NC + 3.0 / 4.0 * z * LMUA * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 4.0 * z * LMUA * LMUF * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += (-1) * 1.0 / 3.0 * LMUR * CF * NF + 11.0 / 6.0 * LMUR * CF * NC + 1.0 / 3.0 * z * LMUR * CF * NF + (-1) * 11.0 / 6.0 * z * LMUR * CF * NC + 0
            res += (-1) * 2.0 / 3.0 * ln(z) * LMUR * CF * NF * pow(omz, -1) + 1.0 / 3.0 * ln(z) * LMUR * CF * NF + 11.0 / 3.0 * ln(z) * LMUR * CF * NC * pow(omz, -1) + (-1) * 11.0 / 6.0 * ln(z) * LMUR * CF * NC + 0
            res += 1.0 / 3.0 * ln(z) * z * LMUR * CF * NF + (-1) * 11.0 / 6.0 * ln(z) * z * LMUR * CF * NC + 0
            res += 1.0 / 3.0 * ln(omz) * LMUR * CF * NF + (-1) * 11.0 / 6.0 * ln(omz) * LMUR * CF * NC + 1.0 / 3.0 * ln(omz) * z * LMUR * CF * NF + (-1) * 11.0 / 6.0 * ln(omz) * z * LMUR * CF * NC + 0
        if ("101" in orders) or ("all" in orders):
            res += (-1) * 1.0 / 3.0 * LMUA * LMUR * CF * NF + 11.0 / 6.0 * LMUA * LMUR * CF * NC + (-1) * 1.0 / 3.0 * z * LMUA * LMUR * CF * NF + 11.0 / 6.0 * z * LMUA * LMUR * CF * NC + 0
        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += (
                +(-1) * 7.0 / 18.0 * pow(z, -1) * CF
                + (-1) * CF * pow(NC, -1)
                + (-1) * 10.0 / 3.0 * CF
                + 2.0 / 9.0 * CF * NF
                + 19.0 / 9.0 * CF * NC
                + (-1) * 7 * z * CF * pow(NC, -1)
                + 7.0 / 3.0 * z * CF
                + 8.0 / 9.0 * z * CF * NF
                + (-1) * 14.0 / 9.0 * z * CF * NC
                + 25.0 / 18.0 * pow(z, 2) * CF
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * CF
                + 7.0 / 12.0 * pow(pi, 2) * CF * NC
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * z * CF
                + 7.0 / 12.0 * pow(pi, 2) * z * CF * NC
                + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF
                + (-1) * 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(z) * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * ln(z) * CF
                + 3.0 / 2.0 * ln(z) * CF * NC * pow(omz, -1)
                + (-1) * 5.0 / 2.0 * ln(z) * CF * NC
                + ln(z) * z * CF * pow(NC, -1)
                + (-1) * 2 * ln(z) * z * CF
                + 0
            )
            res += (
                +(-1) * 2.0 / 3.0 * ln(z) * pow(z, 2) * CF
                + 3 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * 2 * pow(ln(z), 2) * CF * pow(NC, -1)
                + pow(ln(z), 2) * CF
                + (-1) * 2 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * CF * NC
                + (-1) * 2 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                + pow(ln(z), 2) * z * CF
                + 3.0 / 2.0 * pow(ln(z), 2) * z * CF * NC
                + (-1) * 2 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + ln(z) * ln(omz) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
                + (-1) * ln(z) * ln(omz) * CF * NC
                + ln(z) * ln(omz) * z * CF * pow(NC, -1)
                + (-1) * ln(z) * ln(omz) * z * CF * NC
                + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF
                + 1.0 / 2.0 * ln(omz) * CF
                + (-1) * 1.0 / 3.0 * ln(omz) * CF * NF
                + 11.0 / 6.0 * ln(omz) * CF * NC
                + (-1) * 1.0 / 2.0 * ln(omz) * z * CF
                + (-1) * 1.0 / 3.0 * ln(omz) * z * CF * NF
                + 11.0 / 6.0 * ln(omz) * z * CF * NC
                + (-1) * 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF
                + 3.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * pow(ln(omz), 2) * CF * NC
                + 3.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC
                + 1.0 / 2.0 * Li2(z) * CF * pow(NC, -1)
                + (-1) * Li2(z) * CF
                + (-1) * 1.0 / 2.0 * Li2(z) * CF * NC
                + 1.0 / 2.0 * Li2(z) * z * CF * pow(NC, -1)
                + (-1) * Li2(z) * z * CF
                + (-1) * 1.0 / 2.0 * Li2(z) * z * CF * NC
                + 0
            )
        if ("001" in orders) or ("all" in orders):
            res += (
                (-1) * 2.0 / 3.0 * pow(z, -1) * LMUA * CF
                + (-1) * 7.0 / 4.0 * LMUA * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * LMUA * CF
                + 7.0 / 4.0 * LMUA * CF * NC
                + 1.0 / 4.0 * z * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * z * LMUA * CF
                + (-1) * 1.0 / 4.0 * z * LMUA * CF * NC
                + 2.0 / 3.0 * pow(z, 2) * LMUA * CF
                + (-1) * 2 * ln(z) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * LMUA * CF * pow(NC, -1)
                + (-1) * ln(z) * LMUA * CF
                + 2 * ln(z) * LMUA * CF * NC * pow(omz, -1)
                + (-1) * 3.0 / 2.0 * ln(z) * LMUA * CF * NC
                + 3.0 / 2.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
                + (-1) * ln(z) * z * LMUA * CF
                + (-1) * 3.0 / 2.0 * ln(z) * z * LMUA * CF * NC
                + 0
            )
            res += (-1) * 2 * ln(omz) * LMUA * CF * pow(NC, -1) + 2 * ln(omz) * LMUA * CF * NC + (-1) * 2 * ln(omz) * z * LMUA * CF * pow(NC, -1) + 2 * ln(omz) * z * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += (
                1.0 / 4.0 * LMUF * CF * pow(NC, -1)
                + (-1) * 1.0 / 4.0 * LMUF * CF * NC
                + (-1) * 7.0 / 4.0 * z * LMUF * CF * pow(NC, -1)
                + 7.0 / 4.0 * z * LMUF * CF * NC
                + 2 * ln(z) * LMUF * CF * pow(NC, -1) * pow(omz, -1)
                + (-1) * ln(z) * LMUF * CF * pow(NC, -1)
                + (-1) * 2 * ln(z) * LMUF * CF * NC * pow(omz, -1)
                + ln(z) * LMUF * CF * NC
                + (-1) * ln(z) * z * LMUF * CF * pow(NC, -1)
                + ln(z) * z * LMUF * CF * NC
                + 0
            )
            res += (-1) * ln(omz) * LMUF * CF * pow(NC, -1) + ln(omz) * LMUF * CF * NC + (-1) * ln(omz) * z * LMUF * CF * pow(NC, -1) + ln(omz) * z * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += LMUA * LMUF * CF * pow(NC, -1) + (-1) * LMUA * LMUF * CF * NC + z * LMUA * LMUF * CF * pow(NC, -1) + (-1) * z * LMUA * LMUF * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += 1.0 / 3.0 * LMUR * CF * NF + (-1) * 11.0 / 6.0 * LMUR * CF * NC + 1.0 / 3.0 * z * LMUR * CF * NF + (-1) * 11.0 / 6.0 * z * LMUR * CF * NC + 0
        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += (
                2.0 / 3.0 * pow(z, -1) * CF
                + 1.0 / 2.0 * CF
                + (-1) * 1.0 / 3.0 * CF * NF
                + 11.0 / 6.0 * CF * NC
                + (-1) * 1.0 / 2.0 * z * CF
                + (-1) * 1.0 / 3.0 * z * CF * NF
                + 11.0 / 6.0 * z * CF * NC
                + (-1) * 2.0 / 3.0 * pow(z, 2) * CF
                + (-1) * 1.0 / 2.0 * ln(z) * CF * pow(NC, -1)
                + ln(z) * CF
                + 1.0 / 2.0 * ln(z) * CF * NC
                + (-1) * 1.0 / 2.0 * ln(z) * z * CF * pow(NC, -1)
                + ln(z) * z * CF
                + 1.0 / 2.0 * ln(z) * z * CF * NC
                + 3 * ln(omz) * CF * pow(NC, -1)
                + (-1) * 3 * ln(omz) * CF * NC
                + 3 * ln(omz) * z * CF * pow(NC, -1)
                + (-1) * 3 * ln(omz) * z * CF * NC
                + 0
            )
        if ("001" in orders) or ("all" in orders):
            res += (-1) * LMUA * CF * pow(NC, -1) + LMUA * CF * NC + (-1) * z * LMUA * CF * pow(NC, -1) + z * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += (-1) * 2 * LMUF * CF * pow(NC, -1) + 2 * LMUF * CF * NC + (-1) * 2 * z * LMUF * CF * pow(NC, -1) + 2 * z * LMUF * CF * NC + 0
        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * CF * NC + 3.0 / 2.0 * z * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * z * CF * NC + 0
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
                +(-1) * 35.0 / 4.0 * CF * pow(NC, -1)
                + 9 * CF
                + 23.0 / 54.0 * CF * NF
                + (-1) * 28.0 / 9.0 * CF * pow(NF, 2)
                + 2393.0 / 108.0 * CF * NC
                + (-1) * 78 * pow(CF, 2)
                + 33.0 / 4.0 * x * CF * pow(NC, -1)
                + (-1) * 9 * x * CF
                + (-1) * 79.0 / 54.0 * x * CF * NF
                + 28.0 / 9.0 * x * CF * pow(NF, 2)
                + (-1) * 1639.0 / 108.0 * x * CF * NC
                + 78 * x * pow(CF, 2)
                + (-1) * 7 * ZETA3 * CF * pow(NC, -1) * pow(omx, -1)
                + 11.0 / 2.0 * ZETA3 * CF * pow(NC, -1)
                + 5 * ZETA3 * CF * NC * pow(omx, -1)
                + (-1) * 8 * ZETA3 * CF * NC
                + 11.0 / 2.0 * ZETA3 * x * CF * pow(NC, -1)
                + (-1) * 8 * ZETA3 * x * CF * NC
                + 1.0 / 4.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 1.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * pow(pi, 2) * CF
                + (-1) * 1.0 / 9.0 * pow(pi, 2) * CF * NF * pow(omx, -1)
                + 1.0 / 9.0 * pow(pi, 2) * CF * NF
                + 0
            )
            res += (
                +13.0 / 36.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                + (-1) * 13.0 / 36.0 * pow(pi, 2) * CF * NC
                + 1.0 / 12.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                + 1.0 / 2.0 * pow(pi, 2) * x * CF
                + 1.0 / 9.0 * pow(pi, 2) * x * CF * NF
                + (-1) * 1.0 / 9.0 * pow(pi, 2) * x * CF * NC
                + (-1) * 4.0 / 3.0 * pow(pi, 2) * x * pow(CF, 2)
                + (-1) * 10 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                + 29.0 / 4.0 * ln(x) * CF * pow(NC, -1)
                + 25.0 / 4.0 * ln(x) * CF
                + 5.0 / 3.0 * ln(x) * CF * NF * pow(omx, -1)
                + (-1) * 1.0 / 6.0 * ln(x) * CF * NF
                + (-1) * 11.0 / 3.0 * ln(x) * CF * pow(NF, 2)
                + (-1) * 5.0 / 3.0 * ln(x) * CF * NC * pow(omx, -1)
                + 13.0 / 12.0 * ln(x) * CF * NC
                + (-1) * 18 * ln(x) * pow(CF, 2)
                + 0
            )
            res += (
                +6 * ln(x) * x * CF * pow(NC, -1)
                + (-1) * 3.0 / 4.0 * ln(x) * x * CF
                + (-1) * 11.0 / 6.0 * ln(x) * x * CF * NF
                + 5.0 / 3.0 * ln(x) * x * CF * pow(NF, 2)
                + 61.0 / 6.0 * ln(x) * x * CF * NC
                + (-1) * 32 * ln(x) * x * pow(CF, 2)
                + (-1) * ln(x) * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 2.0 / 3.0 * ln(x) * pow(pi, 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF
                + 5.0 / 3.0 * ln(x) * pow(pi, 2) * CF * NC * pow(omx, -1)
                + (-1) * ln(x) * pow(pi, 2) * CF * NC
                + 2.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF * pow(NC, -1)
                + (-1) * 1.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF
                + (-1) * ln(x) * pow(pi, 2) * x * CF * NC
                + 4 * ln(x) * ln(1 + x) * CF * NC * opx
                + (-1) * 8 * ln(x) * ln(1 + x) * pow(CF, 2)
                + (-1) * 8 * ln(x) * ln(1 + x) * x * pow(CF, 2)
                + (-1) * 9.0 / 8.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 5.0 / 4.0 * pow(ln(x), 2) * CF * pow(NC, -1)
                + 17.0 / 8.0 * pow(ln(x), 2) * CF
                + 5.0 / 6.0 * pow(ln(x), 2) * CF * NF * pow(omx, -1)
                + (-1) * 5.0 / 12.0 * pow(ln(x), 2) * CF * NF
                + (-1) * pow(ln(x), 2) * CF * pow(NF, 2)
                + (-1) * 83.0 / 24.0 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                + 49.0 / 24.0 * pow(ln(x), 2) * CF * NC
                + (-1) * 5.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                + 0
            )
            res += (
                +(-1) * 15.0 / 8.0 * pow(ln(x), 2) * x * CF
                + (-1) * 5.0 / 12.0 * pow(ln(x), 2) * x * CF * NF
                + (-1) * 1.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NF, 2)
                + 7.0 / 24.0 * pow(ln(x), 2) * x * CF * NC
                + 4 * pow(ln(x), 2) * x * pow(CF, 2)
                + (-1) * 5.0 / 24.0 * pow(ln(x), 3) * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(x), 3) * CF
                + (-1) * 1.0 / 2.0 * pow(ln(x), 3) * CF * NC * pow(omx, -1)
                + 11.0 / 24.0 * pow(ln(x), 3) * CF * NC
                + (-1) * 5.0 / 24.0 * pow(ln(x), 3) * x * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(x), 3) * x * CF
                + 11.0 / 24.0 * pow(ln(x), 3) * x * CF * NC
                + (-1) * 9.0 / 2.0 * pow(ln(x), 2) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 9.0 / 4.0 * pow(ln(x), 2) * ln(omx) * CF * pow(NC, -1)
                + 5.0 / 2.0 * pow(ln(x), 2) * ln(omx) * CF * NC * pow(omx, -1)
                + (-1) * 5.0 / 4.0 * pow(ln(x), 2) * ln(omx) * CF * NC
                + 9.0 / 4.0 * pow(ln(x), 2) * ln(omx) * x * CF * pow(NC, -1)
                + (-1) * 5.0 / 4.0 * pow(ln(x), 2) * ln(omx) * x * CF * NC
                + (-1) * 11.0 / 2.0 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + (-1) * 5.0 / 2.0 * ln(x) * ln(omx) * CF
                + (-1) * 2.0 / 3.0 * ln(x) * ln(omx) * CF * NF * pow(omx, -1)
                + 1.0 / 3.0 * ln(x) * ln(omx) * CF * NF
                + 11.0 / 3.0 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                + 11.0 / 3.0 * ln(x) * ln(omx) * CF * NC
                + (-1) * 12 * ln(x) * ln(omx) * pow(CF, 2)
                + 11.0 / 2.0 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                + 5.0 / 2.0 * ln(x) * ln(omx) * x * CF
                + 1.0 / 3.0 * ln(x) * ln(omx) * x * CF * NF
                + (-1) * 22.0 / 3.0 * ln(x) * ln(omx) * x * CF * NC
                + 12 * ln(x) * ln(omx) * x * pow(CF, 2)
                + 5.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 0
            )
            res += (
                +(-1) * 1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF
                + (-1) * 9.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                + 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * NC
                + (-1) * 1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF
                + 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF * NC
                + (-1) * 5 * ln(x) * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * Li2(x) * CF * pow(NC, -1)
                + ln(x) * Li2(x) * CF
                + ln(x) * Li2(x) * CF * NC * pow(omx, -1)
                + 2 * ln(x) * Li2(x) * x * CF * pow(NC, -1)
                + ln(x) * Li2(x) * x * CF
                + (-1) * 5 * ln(omx) * CF * pow(NC, -1)
                + (-1) * 3 * ln(omx) * CF
                + 2.0 / 9.0 * ln(omx) * CF * NF
                + 55.0 / 9.0 * ln(omx) * CF * NC
                + (-1) * 8 * ln(omx) * pow(CF, 2)
                + (-1) * 11.0 / 4.0 * ln(omx) * x * CF * pow(NC, -1)
                + 3 * ln(omx) * x * CF
                + 8.0 / 9.0 * ln(omx) * x * CF * NF
                + (-1) * 191.0 / 36.0 * ln(omx) * x * CF * NC
                + 8 * ln(omx) * x * pow(CF, 2)
                + 1.0 / 6.0 * ln(omx) * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + (-1) * 7.0 / 12.0 * ln(omx) * pow(pi, 2) * CF * pow(NC, -1)
                + 0
            )
            res += (
                +1.0 / 3.0 * ln(omx) * pow(pi, 2) * CF
                + 1.0 / 6.0 * ln(omx) * pow(pi, 2) * CF * NC * pow(omx, -1)
                + 7.0 / 12.0 * ln(omx) * pow(pi, 2) * CF * NC
                + (-1) * 7.0 / 12.0 * ln(omx) * pow(pi, 2) * x * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * x * CF
                + 7.0 / 12.0 * ln(omx) * pow(pi, 2) * x * CF * NC
                + 2 * pow(ln(omx), 2) * CF * pow(NC, -1)
                + 5.0 / 4.0 * pow(ln(omx), 2) * CF
                + (-1) * 1.0 / 6.0 * pow(ln(omx), 2) * CF * NF
                + (-1) * 13.0 / 12.0 * pow(ln(omx), 2) * CF * NC
                + 4 * pow(ln(omx), 2) * pow(CF, 2)
                + (-1) * 2 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + (-1) * 5.0 / 4.0 * pow(ln(omx), 2) * x * CF
                + (-1) * 1.0 / 6.0 * pow(ln(omx), 2) * x * CF * NF
                + 35.0 / 12.0 * pow(ln(omx), 2) * x * CF * NC
                + (-1) * 4 * pow(ln(omx), 2) * x * pow(CF, 2)
                + 1.0 / 2.0 * pow(ln(omx), 3) * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(omx), 3) * CF * NC
                + 1.0 / 2.0 * pow(ln(omx), 3) * x * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(omx), 3) * x * CF * NC
                + 1.0 / 2.0 * ln(omx) * Li2(1 - x) * CF * pow(NC, -1)
                + (-1) * ln(omx) * Li2(1 - x) * CF
                + (-1) * 1.0 / 2.0 * ln(omx) * Li2(1 - x) * CF * NC
                + 1.0 / 2.0 * ln(omx) * Li2(1 - x) * x * CF * pow(NC, -1)
                + (-1) * ln(omx) * Li2(1 - x) * x * CF
                + (-1) * 1.0 / 2.0 * ln(omx) * Li2(1 - x) * x * CF * NC
                + (-1) * ln(omx) * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * ln(omx) * Li2(x) * CF * pow(NC, -1)
                + (-1) * 2 * ln(omx) * Li2(x) * CF
                + (-1) * ln(omx) * Li2(x) * CF * NC * pow(omx, -1)
                + (-1) * 1.0 / 2.0 * ln(omx) * Li2(x) * CF * NC
                + 3.0 / 2.0 * ln(omx) * Li2(x) * x * CF * pow(NC, -1)
                + (-1) * 2 * ln(omx) * Li2(x) * x * CF
                + (-1) * 1.0 / 2.0 * ln(omx) * Li2(x) * x * CF * NC
                + (-1) * 3 * Li3(1 - x) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li3(1 - x) * CF * pow(NC, -1)
                + (-1) * Li3(1 - x) * CF
                + (-1) * 5 * Li3(1 - x) * CF * NC * pow(omx, -1)
                + 0
            )
            res += (
                +2 * Li3(1 - x) * CF * NC
                + 2 * Li3(1 - x) * x * CF * pow(NC, -1)
                + (-1) * Li3(1 - x) * x * CF
                + 2 * Li3(1 - x) * x * CF * NC
                + 7 * Li3(x) * CF * pow(NC, -1) * pow(omx, -1)
                + (-1) * 7.0 / 2.0 * Li3(x) * CF * pow(NC, -1)
                + (-1) * 5 * Li3(x) * CF * NC * pow(omx, -1)
                + 5.0 / 2.0 * Li3(x) * CF * NC
                + (-1) * 7.0 / 2.0 * Li3(x) * x * CF * pow(NC, -1)
                + 5.0 / 2.0 * Li3(x) * x * CF * NC
                + 4 * Li2(-x) * CF * NC * opx
                + (-1) * 8 * Li2(-x) * pow(CF, 2)
                + (-1) * 8 * Li2(-x) * x * pow(CF, 2)
                + (-1) * 3.0 / 2.0 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
                + (-1) * 2 * Li2(x) * CF * pow(NC, -1)
                + 1.0 / 2.0 * Li2(x) * CF
                + 2.0 / 3.0 * Li2(x) * CF * NF * pow(omx, -1)
                + (-1) * 1.0 / 3.0 * Li2(x) * CF * NF
                + (-1) * 13.0 / 6.0 * Li2(x) * CF * NC * pow(omx, -1)
                + 17.0 / 6.0 * Li2(x) * CF * NC
                + (-1) * 4 * Li2(x) * pow(CF, 2)
                + 1.0 / 2.0 * Li2(x) * x * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * Li2(x) * x * CF
                + (-1) * 1.0 / 3.0 * Li2(x) * x * CF * NF
                + 1.0 / 3.0 * Li2(x) * x * CF * NC
                + 4 * Li2(x) * x * pow(CF, 2)
                + 0
            )
        if ("001" in orders) or ("all" in orders):
            res += (-1) * 9.0 / 4.0 * LMUA * CF * pow(NC, -1) + 9.0 / 4.0 * LMUA * CF * NC + (-1) * 6 * LMUA * pow(CF, 2) + 9.0 / 4.0 * x * LMUA * CF * pow(NC, -1) + (-1) * 9.0 / 4.0 * x * LMUA * CF * NC + 6 * x * LMUA * pow(CF, 2) + 0
            res += 1.0 / 6.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUA * CF * NC + 1.0 / 6.0 * pow(pi, 2) * x * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * LMUA * CF * NC + (-1) * 3.0 / 2.0 * ln(x) * LMUA * CF * pow(NC, -1) * pow(omx, -1) + 3.0 / 4.0 * ln(x) * LMUA * CF * pow(NC, -1) + 0
            res += 3.0 / 2.0 * ln(x) * LMUA * CF * NC * pow(omx, -1) + (-1) * 3.0 / 4.0 * ln(x) * LMUA * CF * NC + 3.0 / 4.0 * ln(x) * x * LMUA * CF * pow(NC, -1) + (-1) * 3.0 / 4.0 * ln(x) * x * LMUA * CF * NC + 0
            res += (-1) * 3.0 / 4.0 * ln(omx) * LMUA * CF * pow(NC, -1) + 3.0 / 4.0 * ln(omx) * LMUA * CF * NC + (-1) * 3.0 / 4.0 * ln(omx) * x * LMUA * CF * pow(NC, -1) + 3.0 / 4.0 * ln(omx) * x * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += 11.0 / 4.0 * LMUF * CF * pow(NC, -1) + 3 * LMUF * CF + 1.0 / 9.0 * LMUF * CF * NF + (-1) * 205.0 / 36.0 * LMUF * CF * NC + 2 * LMUF * pow(CF, 2) + 21.0 / 4.0 * x * LMUF * CF * pow(NC, -1) + (-1) * 3 * x * LMUF * CF + (-1) * 11.0 / 9.0 * x * LMUF * CF * NF + 185.0 / 36.0 * x * LMUF * CF * NC + (-1) * 2 * x * LMUF * pow(CF, 2) + 0
            res += (
                1.0 / 4.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUF * CF
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * LMUF * CF * NC
                + 1.0 / 4.0 * pow(pi, 2) * x * LMUF * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * LMUF * CF
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * x * LMUF * CF * NC
                + (-1) * 3 * ln(x) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                + 11.0 / 4.0 * ln(x) * LMUF * CF * pow(NC, -1)
                + 3 * ln(x) * LMUF * CF
                + 2.0 / 3.0 * ln(x) * LMUF * CF * NF * pow(omx, -1)
                + (-1) * 1.0 / 3.0 * ln(x) * LMUF * CF * NF
                + (-1) * 2.0 / 3.0 * ln(x) * LMUF * CF * NC * pow(omx, -1)
                + (-1) * 23.0 / 12.0 * ln(x) * LMUF * CF * NC
                + 4 * ln(x) * LMUF * pow(CF, 2)
                + 0
            )
            res += (
                (-1) * 11.0 / 4.0 * ln(x) * x * LMUF * CF * pow(NC, -1)
                + (-1) * 3 * ln(x) * x * LMUF * CF
                + (-1) * 1.0 / 3.0 * ln(x) * x * LMUF * CF * NF
                + 43.0 / 12.0 * ln(x) * x * LMUF * CF * NC
                + (-1) * 4 * ln(x) * x * LMUF * pow(CF, 2)
                + pow(ln(x), 2) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                + (-1) * pow(ln(x), 2) * LMUF * CF * pow(NC, -1)
                + pow(ln(x), 2) * LMUF * CF
                + (-1) * 2 * pow(ln(x), 2) * LMUF * CF * NC * pow(omx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * LMUF * CF * NC
                + 0
            )
            res += (
                (-1) * pow(ln(x), 2) * x * LMUF * CF * pow(NC, -1)
                + pow(ln(x), 2) * x * LMUF * CF
                + 3.0 / 2.0 * pow(ln(x), 2) * x * LMUF * CF * NC
                + (-1) * 6 * ln(x) * ln(omx) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * ln(x) * ln(omx) * LMUF * CF * pow(NC, -1)
                + 6 * ln(x) * ln(omx) * LMUF * CF * NC * pow(omx, -1)
                + (-1) * 3 * ln(x) * ln(omx) * LMUF * CF * NC
                + 3 * ln(x) * ln(omx) * x * LMUF * CF * pow(NC, -1)
                + (-1) * 3 * ln(x) * ln(omx) * x * LMUF * CF * NC
                + 0
            )
            res += (-1) * 19.0 / 4.0 * ln(omx) * LMUF * CF * pow(NC, -1) + (-1) * 5.0 / 2.0 * ln(omx) * LMUF * CF + 19.0 / 4.0 * ln(omx) * LMUF * CF * NC + (-1) * 8 * ln(omx) * LMUF * pow(CF, 2) + 13.0 / 4.0 * ln(omx) * x * LMUF * CF * pow(NC, -1) + 5.0 / 2.0 * ln(omx) * x * LMUF * CF + (-1) * 13.0 / 4.0 * ln(omx) * x * LMUF * CF * NC + 8 * ln(omx) * x * LMUF * pow(CF, 2) + 0
            res += (-1) * 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * CF * pow(NC, -1) + 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * CF * NC + (-1) * 3.0 / 2.0 * pow(ln(omx), 2) * x * LMUF * CF * pow(NC, -1) + 3.0 / 2.0 * pow(ln(omx), 2) * x * LMUF * CF * NC + 0
            res += (-1) * 1.0 / 2.0 * Li2(x) * LMUF * CF * pow(NC, -1) + Li2(x) * LMUF * CF + 1.0 / 2.0 * Li2(x) * LMUF * CF * NC + (-1) * 1.0 / 2.0 * Li2(x) * x * LMUF * CF * pow(NC, -1) + Li2(x) * x * LMUF * CF + 1.0 / 2.0 * Li2(x) * x * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += 3.0 / 4.0 * LMUA * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 4.0 * LMUA * LMUF * CF * NC + 3.0 / 4.0 * x * LMUA * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 4.0 * x * LMUA * LMUF * CF * NC + 0
        if ("020" in orders) or ("all" in orders):
            res += 5.0 / 4.0 * pow(LMUF, 2) * CF * pow(NC, -1) + 5.0 / 4.0 * pow(LMUF, 2) * CF + 1.0 / 6.0 * pow(LMUF, 2) * CF * NF + (-1) * 13.0 / 6.0 * pow(LMUF, 2) * CF * NC + 1.0 / 4.0 * x * pow(LMUF, 2) * CF * pow(NC, -1) + (-1) * 5.0 / 4.0 * x * pow(LMUF, 2) * CF + 1.0 / 6.0 * x * pow(LMUF, 2) * CF * NF + (-1) * 7.0 / 6.0 * x * pow(LMUF, 2) * CF * NC + 0
            res += ln(x) * pow(LMUF, 2) * CF * pow(NC, -1) * pow(omx, -1) + (-1) * 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * CF * pow(NC, -1) + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * CF + (-1) * ln(x) * pow(LMUF, 2) * CF * NC * pow(omx, -1) + 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * CF * NC + 0
            res += (-1) * 3.0 / 4.0 * ln(x) * x * pow(LMUF, 2) * CF * pow(NC, -1) + 1.0 / 2.0 * ln(x) * x * pow(LMUF, 2) * CF + 3.0 / 4.0 * ln(x) * x * pow(LMUF, 2) * CF * NC + 0
            res += ln(omx) * pow(LMUF, 2) * CF * pow(NC, -1) + (-1) * ln(omx) * pow(LMUF, 2) * CF * NC + ln(omx) * x * pow(LMUF, 2) * CF * pow(NC, -1) + (-1) * ln(omx) * x * pow(LMUF, 2) * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += (-1) * 1.0 / 3.0 * LMUR * CF * NF + 11.0 / 6.0 * LMUR * CF * NC + 1.0 / 3.0 * x * LMUR * CF * NF + (-1) * 11.0 / 6.0 * x * LMUR * CF * NC + 0
            res += 2.0 / 3.0 * ln(x) * LMUR * CF * NF * pow(omx, -1) + (-1) * 1.0 / 3.0 * ln(x) * LMUR * CF * NF + (-1) * 11.0 / 3.0 * ln(x) * LMUR * CF * NC * pow(omx, -1) + 11.0 / 6.0 * ln(x) * LMUR * CF * NC + 0
            res += (-1) * 1.0 / 3.0 * ln(x) * x * LMUR * CF * NF + 11.0 / 6.0 * ln(x) * x * LMUR * CF * NC + 0
            res += 1.0 / 3.0 * ln(omx) * LMUR * CF * NF + (-1) * 11.0 / 6.0 * ln(omx) * LMUR * CF * NC + 1.0 / 3.0 * ln(omx) * x * LMUR * CF * NF + (-1) * 11.0 / 6.0 * ln(omx) * x * LMUR * CF * NC + 0
        if ("110" in orders) or ("all" in orders):
            res += (-1) * 1.0 / 3.0 * LMUF * LMUR * CF * NF + 11.0 / 6.0 * LMUF * LMUR * CF * NC + (-1) * 1.0 / 3.0 * x * LMUF * LMUR * CF * NF + 11.0 / 6.0 * x * LMUF * LMUR * CF * NC + 0
        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += (
                +(-1) * 5 * CF * pow(NC, -1)
                + (-1) * 3 * CF
                + 2.0 / 9.0 * CF * NF
                + 55.0 / 9.0 * CF * NC
                + (-1) * 8 * pow(CF, 2)
                + (-1) * 3 * x * CF * pow(NC, -1)
                + 3 * x * CF
                + 8.0 / 9.0 * x * CF * NF
                + (-1) * 50.0 / 9.0 * x * CF * NC
                + 8 * x * pow(CF, 2)
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * CF
                + 7.0 / 12.0 * pow(pi, 2) * CF * NC
                + (-1) * 5.0 / 12.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * CF
                + 7.0 / 12.0 * pow(pi, 2) * x * CF * NC
                + 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                + (-1) * 2 * ln(x) * CF * pow(NC, -1)
                + (-1) * 3 * ln(x) * CF
                + (-1) * 4.0 / 3.0 * ln(x) * CF * NF * pow(omx, -1)
                + 2.0 / 3.0 * ln(x) * CF * NF
                + 35.0 / 6.0 * ln(x) * CF * NC * pow(omx, -1)
                + (-1) * 2.0 / 3.0 * ln(x) * CF * NC
                + (-1) * 4 * ln(x) * pow(CF, 2)
                + 7.0 / 2.0 * ln(x) * x * CF * pow(NC, -1)
                + 3 * ln(x) * x * CF
                + 2.0 / 3.0 * ln(x) * x * CF * NF
                + (-1) * 37.0 / 6.0 * ln(x) * x * CF * NC
                + 4 * ln(x) * x * pow(CF, 2)
                + 0
            )
            res += (
                +(-1) * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + pow(ln(x), 2) * CF * pow(NC, -1)
                + (-1) * pow(ln(x), 2) * CF
                + 2 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * CF * NC
                + pow(ln(x), 2) * x * CF * pow(NC, -1)
                + (-1) * pow(ln(x), 2) * x * CF
                + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * x * CF * NC
                + 6 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + (-1) * 3 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + (-1) * 6 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                + 3 * ln(x) * ln(omx) * CF * NC
                + (-1) * 3 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * CF * NC
                + 4 * ln(omx) * CF * pow(NC, -1)
                + 5.0 / 2.0 * ln(omx) * CF
                + (-1) * 1.0 / 3.0 * ln(omx) * CF * NF
                + (-1) * 13.0 / 6.0 * ln(omx) * CF * NC
                + 8 * ln(omx) * pow(CF, 2)
                + (-1) * 4 * ln(omx) * x * CF * pow(NC, -1)
                + (-1) * 5.0 / 2.0 * ln(omx) * x * CF
                + (-1) * 1.0 / 3.0 * ln(omx) * x * CF * NF
                + 35.0 / 6.0 * ln(omx) * x * CF * NC
                + (-1) * 8 * ln(omx) * x * pow(CF, 2)
                + 3.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * pow(ln(omx), 2) * CF * NC
                + 3.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * pow(ln(omx), 2) * x * CF * NC
                + 1.0 / 2.0 * Li2(x) * CF * pow(NC, -1)
                + (-1) * Li2(x) * CF
                + (-1) * 1.0 / 2.0 * Li2(x) * CF * NC
                + 1.0 / 2.0 * Li2(x) * x * CF * pow(NC, -1)
                + (-1) * Li2(x) * x * CF
                + (-1) * 1.0 / 2.0 * Li2(x) * x * CF * NC
                + 0
            )
        if ("001" in orders) or ("all" in orders):
            res += (
                (-1) * 15.0 / 4.0 * LMUA * CF * pow(NC, -1)
                + 15.0 / 4.0 * LMUA * CF * NC
                + (-1) * 8 * LMUA * pow(CF, 2)
                + 9.0 / 4.0 * x * LMUA * CF * pow(NC, -1)
                + (-1) * 9.0 / 4.0 * x * LMUA * CF * NC
                + 8 * x * LMUA * pow(CF, 2)
                + (-1) * 2 * ln(x) * LMUA * CF * pow(NC, -1) * pow(omx, -1)
                + ln(x) * LMUA * CF * pow(NC, -1)
                + 2 * ln(x) * LMUA * CF * NC * pow(omx, -1)
                + (-1) * ln(x) * LMUA * CF * NC
                + 0
            )
            res += ln(x) * x * LMUA * CF * pow(NC, -1) + (-1) * ln(x) * x * LMUA * CF * NC + (-1) * ln(omx) * LMUA * CF * pow(NC, -1) + ln(omx) * LMUA * CF * NC + (-1) * ln(omx) * x * LMUA * CF * pow(NC, -1) + ln(omx) * x * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += (
                (-1) * 7.0 / 4.0 * LMUF * CF * pow(NC, -1)
                + (-1) * 5.0 / 2.0 * LMUF * CF
                + 7.0 / 4.0 * LMUF * CF * NC
                + 1.0 / 4.0 * x * LMUF * CF * pow(NC, -1)
                + 5.0 / 2.0 * x * LMUF * CF
                + (-1) * 1.0 / 4.0 * x * LMUF * CF * NC
                + (-1) * 2 * ln(x) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * ln(x) * LMUF * CF * pow(NC, -1)
                + (-1) * ln(x) * LMUF * CF
                + 2 * ln(x) * LMUF * CF * NC * pow(omx, -1)
                + (-1) * 3.0 / 2.0 * ln(x) * LMUF * CF * NC
                + 3.0 / 2.0 * ln(x) * x * LMUF * CF * pow(NC, -1)
                + (-1) * ln(x) * x * LMUF * CF
                + 0
            )
            res += (-1) * 3.0 / 2.0 * ln(x) * x * LMUF * CF * NC + (-1) * 2 * ln(omx) * LMUF * CF * pow(NC, -1) + 2 * ln(omx) * LMUF * CF * NC + (-1) * 2 * ln(omx) * x * LMUF * CF * pow(NC, -1) + 2 * ln(omx) * x * LMUF * CF * NC + 0
        if ("011" in orders) or ("all" in orders):
            res += LMUA * LMUF * CF * pow(NC, -1) + (-1) * LMUA * LMUF * CF * NC + x * LMUA * LMUF * CF * pow(NC, -1) + (-1) * x * LMUA * LMUF * CF * NC + 0
        if ("100" in orders) or ("all" in orders):
            res += 1.0 / 3.0 * LMUR * CF * NF + (-1) * 11.0 / 6.0 * LMUR * CF * NC + 1.0 / 3.0 * x * LMUR * CF * NF + (-1) * 11.0 / 6.0 * x * LMUR * CF * NC + 0
        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += (
                4 * CF * pow(NC, -1)
                + 5.0 / 2.0 * CF
                + (-1) * 1.0 / 3.0 * CF * NF
                + (-1) * 13.0 / 6.0 * CF * NC
                + 8 * pow(CF, 2)
                + (-1) * 4 * x * CF * pow(NC, -1)
                + (-1) * 5.0 / 2.0 * x * CF
                + (-1) * 1.0 / 3.0 * x * CF * NF
                + 35.0 / 6.0 * x * CF * NC
                + (-1) * 8 * x * pow(CF, 2)
                + 4 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                + (-1) * 5.0 / 2.0 * ln(x) * CF * pow(NC, -1)
                + ln(x) * CF
                + (-1) * 4 * ln(x) * CF * NC * pow(omx, -1)
                + 5.0 / 2.0 * ln(x) * CF * NC
                + (-1) * 5.0 / 2.0 * ln(x) * x * CF * pow(NC, -1)
                + ln(x) * x * CF
                + 5.0 / 2.0 * ln(x) * x * CF * NC
                + 3 * ln(omx) * CF * pow(NC, -1)
                + (-1) * 3 * ln(omx) * CF * NC
                + 3 * ln(omx) * x * CF * pow(NC, -1)
                + (-1) * 3 * ln(omx) * x * CF * NC
                + 0
            )
        if ("001" in orders) or ("all" in orders):
            res += (-1) * 2 * LMUA * CF * pow(NC, -1) + 2 * LMUA * CF * NC + (-1) * 2 * x * LMUA * CF * pow(NC, -1) + 2 * x * LMUA * CF * NC + 0
        if ("010" in orders) or ("all" in orders):
            res += (-1) * LMUF * CF * pow(NC, -1) + LMUF * CF * NC + (-1) * x * LMUF * CF * pow(NC, -1) + x * LMUF * CF * NC + 0
        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if ("000" in orders) or ("all" in orders):
            res += 3.0 / 2.0 * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * CF * NC + 3.0 / 2.0 * x * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * x * CF * NC + 0
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
                tmp += (
                    8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 4 * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * CF * pow(NC, -1)
                    + (-1) * 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 14 * z * CF * pow(NC, -1)
                    + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * x * CF * pow(NC, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 7.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * pow(pi, 2) * CF * pow(NC, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                    + 1.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                    + (-1) * 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 18 * ln(x) * CF * pow(NC, -1)
                    + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 36 * ln(x) * z * CF * pow(NC, -1)
                    + (-1) * 12 * ln(x) * x * CF * pow(NC, -1)
                    + 12 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 9 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 9 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * pow(ln(x), 2) * CF * pow(NC, -1)
                    + (-1) * 9 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                    + (-1) * 20 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 15 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 15 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(z) * CF * pow(NC, -1)
                    + 15 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 20 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +5 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                    + (-1) * 18 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 13 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + 14 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(omx) * CF * pow(NC, -1)
                    + 13 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                    + (-1) * 18 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 14 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 13 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(x) * ln(omz) * CF * pow(NC, -1)
                    + 14 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                    + 5 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(xmz) * CF * pow(NC, -1)
                    + (-1) * 3 * ln(x) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(xmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(xmz) * x * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(omxmz) * x * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + 12 * ln(z) * CF * pow(NC, -1)
                    + (-1) * 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 24 * ln(z) * z * CF * pow(NC, -1)
                    + 8 * ln(z) * x * CF * pow(NC, -1)
                    + 8 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(z), 2) * CF * pow(NC, -1)
                    + (-1) * 6 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                    + 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 10 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(z) * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                    + 12 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(z) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 10 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(z) * ln(xmz) * CF * pow(NC, -1)
                    + 3 * ln(z) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(xmz) * z * CF * pow(NC, -1)
                    + ln(z) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(xmz) * x * CF * pow(NC, -1)
                    + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omx) * z * CF * pow(NC, -1)
                    + 6 * ln(omx) * x * CF * pow(NC, -1)
                    + 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                    + 10 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 7 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 10 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 3 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                    + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omz) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +6 * ln(omz) * x * CF * pow(NC, -1)
                    + 4 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(omz), 2) * CF * pow(NC, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 3 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1)
                    + ln(omz) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                    + Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1)
                    + Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                    + 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1)
                    + (-1) * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1)
                    + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * z * CF * pow(NC, -1)
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += (
                    8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 4 * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * CF * pow(NC, -1)
                    + (-1) * 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 14 * z * CF * pow(NC, -1)
                    + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * x * CF * pow(NC, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 7.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * pow(pi, 2) * CF * pow(NC, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                    + 1.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                    + (-1) * 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 18 * ln(x) * CF * pow(NC, -1)
                    + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 36 * ln(x) * z * CF * pow(NC, -1)
                    + (-1) * 12 * ln(x) * x * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1)
                    + 13 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 10 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 19.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * pow(ln(x), 2) * CF * pow(NC, -1)
                    + (-1) * 10 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 13 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 7.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 7 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                    + (-1) * 22 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 17 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 16 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(z) * CF * pow(NC, -1)
                    + 17 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 22 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                    + 6 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                    + (-1) * 16 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 11 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + 13 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(omx) * CF * pow(NC, -1)
                    + 11 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 16 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                    + 3 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                    + (-1) * 20 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 16 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 14 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(x) * ln(omz) * CF * pow(NC, -1)
                    + 16 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 20 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                    + 6 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(xmz) * CF * pow(NC, -1)
                    + (-1) * 3 * ln(x) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(xmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * ln(xmz) * x * CF * pow(NC, -1)
                    + 24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + 12 * ln(z) * CF * pow(NC, -1)
                    + (-1) * 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 24 * ln(z) * z * CF * pow(NC, -1)
                    + 8 * ln(z) * x * CF * pow(NC, -1)
                    + 8 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(z), 2) * CF * pow(NC, -1)
                    + (-1) * 6 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                    + 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 10 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(z) * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                    + 14 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 9 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(z) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 14 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 5 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(xmz) * CF * pow(NC, -1)
                    + 3 * ln(z) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(xmz) * z * CF * pow(NC, -1)
                    + ln(z) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(xmz) * x * CF * pow(NC, -1)
                    + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omx) * z * CF * pow(NC, -1)
                    + 6 * ln(omx) * x * CF * pow(NC, -1)
                    + 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                    + 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                    + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +18 * ln(omz) * z * CF * pow(NC, -1)
                    + 6 * ln(omz) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1)
                    + ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1)
                    + 5 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 3 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(omz), 2) * CF * pow(NC, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 5 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1)
                    + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1)
                    + Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1)
                    + Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1)
                    + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * z * CF * pow(NC, -1)
                    + 0
                )
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += (
                    8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 4 * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * CF * pow(NC, -1)
                    + (-1) * 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 14 * z * CF * pow(NC, -1)
                    + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * x * CF * pow(NC, -1)
                    + (-1) * 8.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 13.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 11.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * pow(pi, 2) * CF * pow(NC, -1)
                    + 13.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 8.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 5.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                    + (-1) * 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 18 * ln(x) * CF * pow(NC, -1)
                    + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 36 * ln(x) * z * CF * pow(NC, -1)
                    + (-1) * 12 * ln(x) * x * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(-xmz) * CF * pow(NC, -1)
                    + (-1) * 3 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(-xmz) * x * CF * pow(NC, -1)
                    + 14 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 21.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 21.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 7 * pow(ln(x), 2) * CF * pow(NC, -1)
                    + (-1) * 21.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +14 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 7 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                    + (-1) * 24 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 18 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(z) * CF * pow(NC, -1)
                    + 18 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 24 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                    + 6 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                    + (-1) * 18 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 12 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + 15 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(omx) * CF * pow(NC, -1)
                    + 12 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                    + 3 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                    + (-1) * 18 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 15 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(x) * ln(omz) * CF * pow(NC, -1)
                    + 15 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                    + 6 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * ln(omxmz) * x * CF * pow(NC, -1)
                    + 24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + 12 * ln(z) * CF * pow(NC, -1)
                    + (-1) * 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 24 * ln(z) * z * CF * pow(NC, -1)
                    + 8 * ln(z) * x * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(-xmz) * CF * pow(NC, -1)
                    + 3 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1)
                    + ln(z) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(-xmz) * x * CF * pow(NC, -1)
                    + 10 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 15.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 15.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 5 * pow(ln(z), 2) * CF * pow(NC, -1)
                    + (-1) * 15.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 10 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 5 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                    + 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 7 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 11 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(z) * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 7 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                    + 12 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 11 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 7 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 11 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 5 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                    + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omx) * z * CF * pow(NC, -1)
                    + 6 * ln(omx) * x * CF * pow(NC, -1)
                    + 7 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                    + (-1) * 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 7 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 3 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                    + 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 5 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                    + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(omz) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omz) * z * CF * pow(NC, -1)
                    + 6 * ln(omz) * x * CF * pow(NC, -1)
                    + 6 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(omz), 2) * CF * pow(NC, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 6 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 5 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1)
                    + ln(omz) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * x * CF * pow(NC, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                    + 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1)
                    + (-1) * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1)
                    + (-1) * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1)
                    + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * z * CF * pow(NC, -1)
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += (
                    8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 4 * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * CF * pow(NC, -1)
                    + (-1) * 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 14 * z * CF * pow(NC, -1)
                    + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * x * CF * pow(NC, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 7.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * pow(pi, 2) * CF * pow(NC, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                    + 1.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                    + (-1) * 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 18 * ln(x) * CF * pow(NC, -1)
                    + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 36 * ln(x) * z * CF * pow(NC, -1)
                    + (-1) * 12 * ln(x) * x * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(-xmz) * CF * pow(NC, -1)
                    + (-1) * 3 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(-xmz) * x * CF * pow(NC, -1)
                    + 13 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 19.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 10 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 7 * pow(ln(x), 2) * CF * pow(NC, -1)
                    + (-1) * 19.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 13 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                    + (-1) * 22 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 16 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 17 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(z) * CF * pow(NC, -1)
                    + 16 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 22 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                    + 5 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                    + (-1) * 20 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 14 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + 16 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(x) * ln(omx) * CF * pow(NC, -1)
                    + 14 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 20 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                    + (-1) * 16 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 13 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 11 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(x) * ln(omz) * CF * pow(NC, -1)
                    + 13 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 16 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +5 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                    + 24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + 12 * ln(z) * CF * pow(NC, -1)
                    + (-1) * 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 24 * ln(z) * z * CF * pow(NC, -1)
                    + 8 * ln(z) * x * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(-xmz) * CF * pow(NC, -1)
                    + 3 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1)
                    + ln(z) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(-xmz) * x * CF * pow(NC, -1)
                    + 8 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 13.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 5 * pow(ln(z), 2) * CF * pow(NC, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 3 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                    + 16 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 11 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 13 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(z) * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 11 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 16 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                    + (-1) * 3 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                    + 10 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 9 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 6 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 9 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 10 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                    + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omx) * z * CF * pow(NC, -1)
                    + 6 * ln(omx) * x * CF * pow(NC, -1)
                    + 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                    + 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                    + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 10 * ln(omz) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omz) * z * CF * pow(NC, -1)
                    + 6 * ln(omz) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1)
                    + ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1)
                    + 5 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 3 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(omz), 2) * CF * pow(NC, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 5 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1)
                    + Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                    + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1)
                    + (-1) * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1)
                    + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * z * CF * pow(NC, -1)
                    + 0
                )
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
                tmp += (
                    +(-1) * 4 * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * CF * NC * pow(omx, -1)
                    + 7 * CF * NC * pow(omz, -1)
                    + (-1) * 5 * CF * NC
                    + 5 * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * z * CF * NC
                    + (-1) * 3 * x * CF * NC * pow(omz, -1)
                    + 6 * x * CF * NC
                    + 4.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * z * CF * NC
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * x * CF * NC * pow(omz, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * x * CF * NC
                    + 18 * ln(x) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(x) * CF * NC * pow(omx, -1)
                    + (-1) * 18 * ln(x) * CF * NC * pow(omz, -1)
                    + (-1) * 3 * ln(x) * CF * NC
                    + (-1) * 12 * ln(x) * z * CF * NC * pow(omx, -1)
                    + 18 * ln(x) * z * CF * NC
                    + 18 * ln(x) * x * CF * NC
                    + (-1) * 7 * pow(ln(x), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 7.0 / 2.0 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                    + 7.0 / 2.0 * pow(ln(x), 2) * CF * NC * pow(omz, -1)
                    + 7.0 / 2.0 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 7 * pow(ln(x), 2) * z * CF * NC
                    + 7.0 / 2.0 * pow(ln(x), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * 7 * pow(ln(x), 2) * x * CF * NC
                    + 6 * ln(x) * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(z) * CF * NC * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                    + 6 * ln(x) * ln(z) * z * CF * NC
                    + (-1) * 3 * ln(x) * ln(z) * x * CF * NC * pow(omz, -1)
                    + 6 * ln(x) * ln(z) * x * CF * NC
                    + 12 * ln(x) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * CF * NC * pow(omz, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                    + 12 * ln(x) * ln(omx) * z * CF * NC
                    + (-1) * 6 * ln(x) * ln(omx) * x * CF * NC * pow(omz, -1)
                    + 12 * ln(x) * ln(omx) * x * CF * NC
                    + 12 * ln(x) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(omz) * CF * NC * pow(omz, -1)
                    + (-1) * 6 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + 12 * ln(x) * ln(omz) * z * CF * NC
                    + (-1) * 6 * ln(x) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + 12 * ln(x) * ln(omz) * x * CF * NC
                    + (-1) * 2 * ln(x) * ln(omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + ln(x) * ln(omxmz) * CF * NC * pow(omx, -1)
                    + ln(x) * ln(omxmz) * CF * NC * pow(omz, -1)
                    + ln(x) * ln(omxmz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(omxmz) * z * CF * NC
                    + ln(x) * ln(omxmz) * x * CF * NC * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omxmz) * x * CF * NC
                    + (-1) * 6 * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(z) * CF * NC * pow(omx, -1)
                    + 6 * ln(z) * CF * NC * pow(omz, -1)
                    + ln(z) * CF * NC
                    + 4 * ln(z) * z * CF * NC * pow(omx, -1)
                    + (-1) * 6 * ln(z) * z * CF * NC
                    + (-1) * 6 * ln(z) * x * CF * NC
                    + (-1) * pow(ln(z), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * pow(ln(z), 2) * z * CF * NC
                    + 1.0 / 2.0 * pow(ln(z), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * pow(ln(z), 2) * x * CF * NC
                    + (-1) * 4 * ln(z) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                    + 2 * ln(z) * ln(omx) * CF * NC * pow(omz, -1)
                    + 2 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omx) * z * CF * NC
                    + 2 * ln(z) * ln(omx) * x * CF * NC * pow(omz, -1)
                    + (-1) * 4 * ln(z) * ln(omx) * x * CF * NC
                    + (-1) * 4 * ln(z) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                    + 2 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
                    + 2 * ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * z * CF * NC
                    + 2 * ln(z) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * x * CF * NC
                    + 0
                )
                tmp += (
                    +(-1) * 12 * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 4 * ln(omx) * CF * NC * pow(omx, -1)
                    + 12 * ln(omx) * CF * NC * pow(omz, -1)
                    + 2 * ln(omx) * CF * NC
                    + 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                    + (-1) * 12 * ln(omx) * z * CF * NC
                    + (-1) * 12 * ln(omx) * x * CF * NC
                    + (-1) * 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                    + 2 * pow(ln(omx), 2) * CF * NC * pow(omz, -1)
                    + 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * pow(ln(omx), 2) * z * CF * NC
                    + 2 * pow(ln(omx), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * 4 * pow(ln(omx), 2) * x * CF * NC
                    + (-1) * 10 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 5 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                    + 5 * ln(omx) * ln(omz) * CF * NC * pow(omz, -1)
                    + 5 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 10 * ln(omx) * ln(omz) * z * CF * NC
                    + 5 * ln(omx) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + (-1) * 10 * ln(omx) * ln(omz) * x * CF * NC
                    + (-1) * 12 * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 4 * ln(omz) * CF * NC * pow(omx, -1)
                    + 12 * ln(omz) * CF * NC * pow(omz, -1)
                    + 2 * ln(omz) * CF * NC
                    + 8 * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 12 * ln(omz) * z * CF * NC
                    + (-1) * 12 * ln(omz) * x * CF * NC
                    + (-1) * 5 * pow(ln(omz), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 5.0 / 2.0 * pow(ln(omz), 2) * CF * NC * pow(omx, -1)
                    + 5.0 / 2.0 * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
                    + 5.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 5 * pow(ln(omz), 2) * z * CF * NC
                    + 5.0 / 2.0 * pow(ln(omz), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * 5 * pow(ln(omz), 2) * x * CF * NC
                    + 2 * ln(omz) * ln(omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * ln(omz) * ln(omxmz) * CF * NC * pow(omx, -1)
                    + (-1) * ln(omz) * ln(omxmz) * CF * NC * pow(omz, -1)
                    + (-1) * ln(omz) * ln(omxmz) * z * CF * NC * pow(omx, -1)
                    + 2 * ln(omz) * ln(omxmz) * z * CF * NC
                    + 0
                )
                tmp += (
                    +(-1) * ln(omz) * ln(omxmz) * x * CF * NC * pow(omz, -1)
                    + 2 * ln(omz) * ln(omxmz) * x * CF * NC
                    + 2 * Li2(z * pow(omx, -1)) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * Li2(z * pow(omx, -1)) * CF * NC * pow(omx, -1)
                    + (-1) * Li2(z * pow(omx, -1)) * CF * NC * pow(omz, -1)
                    + (-1) * Li2(z * pow(omx, -1)) * z * CF * NC * pow(omx, -1)
                    + 2 * Li2(z * pow(omx, -1)) * z * CF * NC
                    + (-1) * Li2(z * pow(omx, -1)) * x * CF * NC * pow(omz, -1)
                    + 2 * Li2(z * pow(omx, -1)) * x * CF * NC
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * NC * pow(omx, -1)
                    + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * NC * pow(omz, -1)
                    + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * NC * pow(omx, -1)
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * NC
                    + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * CF * NC * pow(omz, -1)
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * CF * NC
                    + (-1) * 2 * Li2(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + Li2(z) * CF * NC * pow(omx, -1)
                    + Li2(z) * CF * NC * pow(omz, -1)
                    + Li2(z) * z * CF * NC * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * z * CF * NC
                    + Li2(z) * x * CF * NC * pow(omz, -1)
                    + (-1) * 2 * Li2(z) * x * CF * NC
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += (
                    +(-1) * 4 * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * CF * NC * pow(omx, -1)
                    + 7 * CF * NC * pow(omz, -1)
                    + (-1) * 5 * CF * NC
                    + 5 * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * z * CF * NC
                    + (-1) * 3 * x * CF * NC * pow(omz, -1)
                    + 6 * x * CF * NC
                    + 4.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * z * CF * NC
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * x * CF * NC * pow(omz, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * x * CF * NC
                    + 18 * ln(x) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(x) * CF * NC * pow(omx, -1)
                    + (-1) * 18 * ln(x) * CF * NC * pow(omz, -1)
                    + (-1) * 3 * ln(x) * CF * NC
                    + (-1) * 12 * ln(x) * z * CF * NC * pow(omx, -1)
                    + 18 * ln(x) * z * CF * NC
                    + 18 * ln(x) * x * CF * NC
                    + (-1) * 2 * ln(x) * ln(-omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + ln(x) * ln(-omxmz) * CF * NC * pow(omx, -1)
                    + ln(x) * ln(-omxmz) * CF * NC * pow(omz, -1)
                    + ln(x) * ln(-omxmz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(-omxmz) * z * CF * NC
                    + ln(x) * ln(-omxmz) * x * CF * NC * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(-omxmz) * x * CF * NC
                    + (-1) * 6 * pow(ln(x), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 3 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                    + 3 * pow(ln(x), 2) * CF * NC * pow(omz, -1)
                    + 3 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 6 * pow(ln(x), 2) * z * CF * NC
                    + 3 * pow(ln(x), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * 6 * pow(ln(x), 2) * x * CF * NC
                    + 8 * ln(x) * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(z) * CF * NC * pow(omz, -1)
                    + (-1) * 4 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                    + 8 * ln(x) * ln(z) * z * CF * NC
                    + (-1) * 4 * ln(x) * ln(z) * x * CF * NC * pow(omz, -1)
                    + 8 * ln(x) * ln(z) * x * CF * NC
                    + 10 * ln(x) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 5 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(omx) * CF * NC * pow(omz, -1)
                    + (-1) * 5 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                    + 10 * ln(x) * ln(omx) * z * CF * NC
                    + (-1) * 5 * ln(x) * ln(omx) * x * CF * NC * pow(omz, -1)
                    + 10 * ln(x) * ln(omx) * x * CF * NC
                    + 10 * ln(x) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 5 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(omz) * CF * NC * pow(omz, -1)
                    + (-1) * 5 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + 10 * ln(x) * ln(omz) * z * CF * NC
                    + (-1) * 5 * ln(x) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + 10 * ln(x) * ln(omz) * x * CF * NC
                    + (-1) * 6 * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(z) * CF * NC * pow(omx, -1)
                    + 6 * ln(z) * CF * NC * pow(omz, -1)
                    + ln(z) * CF * NC
                    + 4 * ln(z) * z * CF * NC * pow(omx, -1)
                    + (-1) * 6 * ln(z) * z * CF * NC
                    + (-1) * 6 * ln(z) * x * CF * NC
                    + (-1) * pow(ln(z), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * pow(ln(z), 2) * z * CF * NC
                    + 1.0 / 2.0 * pow(ln(z), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * pow(ln(z), 2) * x * CF * NC
                    + (-1) * 4 * ln(z) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                    + 2 * ln(z) * ln(omx) * CF * NC * pow(omz, -1)
                    + 2 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omx) * z * CF * NC
                    + 2 * ln(z) * ln(omx) * x * CF * NC * pow(omz, -1)
                    + (-1) * 4 * ln(z) * ln(omx) * x * CF * NC
                    + (-1) * 6 * ln(z) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 3 * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                    + 3 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
                    + 3 * ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 6 * ln(z) * ln(omz) * z * CF * NC
                    + 3 * ln(z) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + (-1) * 6 * ln(z) * ln(omz) * x * CF * NC
                    + 0
                )
                tmp += (
                    +(-1) * 12 * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 4 * ln(omx) * CF * NC * pow(omx, -1)
                    + 12 * ln(omx) * CF * NC * pow(omz, -1)
                    + 2 * ln(omx) * CF * NC
                    + 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                    + (-1) * 12 * ln(omx) * z * CF * NC
                    + (-1) * 12 * ln(omx) * x * CF * NC
                    + (-1) * 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                    + 2 * pow(ln(omx), 2) * CF * NC * pow(omz, -1)
                    + 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * pow(ln(omx), 2) * z * CF * NC
                    + 2 * pow(ln(omx), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * 4 * pow(ln(omx), 2) * x * CF * NC
                    + (-1) * 8 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                    + 4 * ln(omx) * ln(omz) * CF * NC * pow(omz, -1)
                    + 4 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 8 * ln(omx) * ln(omz) * z * CF * NC
                    + 4 * ln(omx) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + (-1) * 8 * ln(omx) * ln(omz) * x * CF * NC
                    + (-1) * 12 * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 4 * ln(omz) * CF * NC * pow(omx, -1)
                    + 12 * ln(omz) * CF * NC * pow(omz, -1)
                    + 2 * ln(omz) * CF * NC
                    + 8 * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 12 * ln(omz) * z * CF * NC
                    + (-1) * 12 * ln(omz) * x * CF * NC
                    + 2 * ln(omz) * ln(-omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * ln(omz) * ln(-omxmz) * CF * NC * pow(omx, -1)
                    + (-1) * ln(omz) * ln(-omxmz) * CF * NC * pow(omz, -1)
                    + (-1) * ln(omz) * ln(-omxmz) * z * CF * NC * pow(omx, -1)
                    + 2 * ln(omz) * ln(-omxmz) * z * CF * NC
                    + (-1) * ln(omz) * ln(-omxmz) * x * CF * NC * pow(omz, -1)
                    + 2 * ln(omz) * ln(-omxmz) * x * CF * NC
                    + (-1) * 4 * pow(ln(omz), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 2 * pow(ln(omz), 2) * CF * NC * pow(omx, -1)
                    + 2 * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
                    + 2 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * z * CF * NC
                    + 0
                )
                tmp += (
                    +2 * pow(ln(omz), 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * x * CF * NC
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * NC * pow(omx, -1)
                    + (-1) * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * NC * pow(omz, -1)
                    + (-1) * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * NC * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * NC
                    + (-1) * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * CF * NC * pow(omz, -1)
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * CF * NC
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + Li2(pow(z, -1) * omx) * CF * NC * pow(omx, -1)
                    + Li2(pow(z, -1) * omx) * CF * NC * pow(omz, -1)
                    + Li2(pow(z, -1) * omx) * z * CF * NC * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * z * CF * NC
                    + Li2(pow(z, -1) * omx) * x * CF * NC * pow(omz, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * x * CF * NC
                    + (-1) * 2 * Li2(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + Li2(z) * CF * NC * pow(omx, -1)
                    + Li2(z) * CF * NC * pow(omz, -1)
                    + Li2(z) * z * CF * NC * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * z * CF * NC
                    + Li2(z) * x * CF * NC * pow(omz, -1)
                    + (-1) * 2 * Li2(z) * x * CF * NC
                    + 0
                )
            res += tmp

        if round(z, ndecimals) != round(x, ndecimals) and round(z, ndecimals) != round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if ("000" in orders) or ("all" in orders):
                tmp += (
                    +(-1) * 12 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 12 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                    + 2 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2)
                    + (-1) * 6 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + 2 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + (-1) * 113.0 / 36.0 * pow(z, -1) * CF
                    + (-1) * CF * pow(NC, -1) * pow(poly2, -1)
                    + 4 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 4 * CF * pow(NC, -1) * pow(omx, -1)
                    + 10 * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 10 * CF * pow(NC, -1)
                    + (-1) * 8 * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                    + 4 * CF * pow(NC, -1) * pow(rln2, 2)
                    + (-1) * 6 * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + 6 * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + 47.0 / 3.0 * CF
                    + 6 * CF * pow(rln2, 2) * pow(omx, -1)
                    + (-1) * 4 * CF * pow(rln2, 2)
                    + 6 * CF * sqrtxz1 * rln2 * pow(omx, -1)
                    + (-1) * 4 * CF * sqrtxz1 * rln2
                    + 2.0 / 3.0 * CF * NF
                    + 4 * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + CF * NC * pow(omx, -1)
                    + (-1) * 7 * CF * NC * pow(omz, -1)
                    + (-1) * 14.0 / 3.0 * CF * NC
                    + 16 * pow(CF, 2)
                    + 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * z * CF * pow(NC, -1) * pow(omxmz, -1)
                    + (-1) * 11 * z * CF * pow(NC, -1)
                    + (-1) * 4 * z * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                    + 4 * z * CF * pow(NC, -1) * pow(rln2, 2)
                    + (-1) * 11.0 / 12.0 * z * CF
                    + 4 * z * CF * pow(rln2, 2) * pow(omx, -1)
                    + (-1) * 10.0 / 9.0 * z * CF * NF
                    + (-1) * 5 * z * CF * NC * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +1.0 / 2.0 * z * CF * NC * pow(omxmz, -1)
                    + 76.0 / 9.0 * z * CF * NC
                    + (-1) * 8 * z * pow(CF, 2)
                    + (-1) * 65.0 / 18.0 * pow(z, 2) * CF
                    + 16 * pow(z, 2) * CF * pow(rln2, 2) * pow(omx, -1)
                    + (-1) * 16 * pow(z, 2) * CF * pow(rln2, 2)
                    + 4 * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 19.0 / 2.0 * x * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * x * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2)
                    + 4 * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + 127.0 / 36.0 * x * pow(z, -1) * CF
                    + x * CF * pow(NC, -1) * pow(poly2, -1)
                    + (-1) * 14 * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * x * CF * pow(NC, -1) * pow(xmz, -1)
                    + 22 * x * CF * pow(NC, -1)
                    + 4 * x * CF * pow(NC, -1) * pow(rln2, 2)
                    + (-1) * 25.0 / 3.0 * x * CF
                    + (-1) * 16.0 / 9.0 * x * CF * NF
                    + 3 * x * CF * NC * pow(omz, -1)
                    + 1.0 / 2.0 * x * CF * NC * pow(xmz, -1)
                    + 46.0 / 9.0 * x * CF * NC
                    + (-1) * 16 * x * pow(CF, 2)
                    + 6 * x * z * CF * pow(NC, -1)
                    + (-1) * 47.0 / 12.0 * x * z * CF
                    + (-1) * 8 * x * z * CF * pow(rln2, 2)
                    + (-1) * 9.0 / 2.0 * x * z * CF * NC
                    + 8 * x * z * pow(CF, 2)
                    + 0
                )
                tmp += (
                    +31.0 / 18.0 * x * pow(z, 2) * CF
                    + (-1) * pow(x, 2) * CF * pow(NC, -1) * pow(poly2, -1)
                    + (-1) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -1)
                    + (-1) * pow(x, 2) * CF * NC * pow(xmz, -1)
                    + pow(x, 3) * CF * pow(NC, -1) * pow(poly2, -1)
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(NC, -1)
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(opx, -1)
                    + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF
                    + 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF
                    + 4.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                    + 1.0 / 6.0 * pow(pi, 2) * pow(z, -1) * CF
                    + 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 11.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
                    + (-1) * 5.0 / 6.0 * pow(pi, 2) * CF * pow(omx, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * CF * pow(opx, -1)
                    + (-1) * 1.0 / 6.0 * pow(pi, 2) * CF
                    + (-1) * pow(pi, 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                    + 1.0 / 2.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
                    + (-1) * 1.0 / 6.0 * pow(pi, 2) * CF * NC
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + pow(pi, 2) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 13.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                    + 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(omx, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(opx, -1)
                    + (-1) * pow(pi, 2) * z * CF
                    + 1.0 / 2.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 13.0 / 6.0 * pow(pi, 2) * z * CF * NC
                    + (-1) * 2 * pow(pi, 2) * pow(z, 2) * CF * pow(omx, -1)
                    + 2 * pow(pi, 2) * pow(z, 2) * CF * pow(opx, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * pow(z, 2) * CF
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF
                    + 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                    + (-1) * 5.0 / 6.0 * pow(pi, 2) * x * CF
                    + 1.0 / 2.0 * pow(pi, 2) * x * CF * NC * pow(omz, -1)
                    + (-1) * 13.0 / 6.0 * pow(pi, 2) * x * CF * NC
                    + 1.0 / 6.0 * pow(pi, 2) * x * z * CF * pow(NC, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * x * z * CF
                    + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * z * CF * NC
                    + 4 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + 6 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 0
                )
                tmp += (
                    +8 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * rln2
                    + 6 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * CF * rln2 * pow(omx, -1)
                    + 6 * ln(1 + sqrtxz1 - z) * CF * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1 * pow(omx, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1
                    + 4 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * z * CF * rln2
                    + (-1) * 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * x * CF * rln2
                    + 12 * ln(1 + sqrtxz1 - z) * x * z * CF * rln2
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(omx, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF
                    + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * CF
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF
                    + 4 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + 8 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * CF * rln2 * pow(omx, -1)
                    + 2 * ln(1 + sqrtxz1 + z) * CF * rln2
                    + 4 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * rln2
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * z * CF * rln2 * pow(omx, -1)
                    + 4 * ln(1 + sqrtxz1 + z) * z * CF * rln2
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * rln2
                    + 2 * ln(1 + sqrtxz1 + z) * x * CF * rln2
                    + 4 * ln(1 + sqrtxz1 + z) * x * z * CF * rln2
                    + (-1) * 6 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                    + 2 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 6 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 8 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * sqrtxz3
                    + (-1) * 6 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 4 * ln(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + 8 * ln(x) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(x, -2) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * pow(x, -2) * CF * pow(opx, -1)
                    + 4 * ln(x) * pow(x, -2) * CF
                    + 8 * ln(x) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(x, -2) * z * CF
                    + (-1) * 4 * ln(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 8 * ln(x) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * pow(x, -1) * CF
                    + 8 * ln(x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 8 * ln(x) * pow(x, -1) * z * CF
                    + 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF
                    + 48 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 87.0 / 2.0 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 32 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 33 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + (-1) * 3 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4.0 / 3.0 * ln(x) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 7.0 / 3.0 * ln(x) * pow(z, -1) * CF
                    + (-1) * 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(poly2, -2)
                    + ln(x) * CF * pow(NC, -1) * pow(poly2, -1)
                    + (-1) * 12 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(xmz, -1)
                    + (-1) * 20 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 8 * ln(x) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(xmz, -1)
                    + 1.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(omxmz, -1)
                    + 15 * ln(x) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 2 * ln(x) * CF * pow(NC, -1) * rln2
                    + (-1) * 3 * ln(x) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 3 * ln(x) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 9.0 / 2.0 * ln(x) * CF * pow(omx, -1)
                    + 4 * ln(x) * CF * pow(opx, -1)
                    + 25.0 / 2.0 * ln(x) * CF
                    + 5 * ln(x) * CF * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(x) * CF * rln2
                    + 3 * ln(x) * CF * sqrtxz1 * pow(omx, -1)
                    + (-1) * 2 * ln(x) * CF * sqrtxz1
                    + ln(x) * CF * NF * pow(omx, -1)
                    + (-1) * 18 * ln(x) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * CF * NC * pow(omx, -1) * pow(xmz, -1)
                    + 7.0 / 2.0 * ln(x) * CF * NC * pow(omx, -1)
                    + 18 * ln(x) * CF * NC * pow(omz, -1)
                    + 3.0 / 2.0 * ln(x) * CF * NC * pow(xmz, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * CF * NC * pow(omxmz, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * CF * NC
                    + 4 * ln(x) * pow(CF, 2) * opx
                    + 0
                )
                tmp += (
                    +(-1) * 73.0 / 2.0 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * ln(x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * z * CF * pow(NC, -1) * pow(omxmz, -2)
                    + 3.0 / 2.0 * ln(x) * z * CF * pow(NC, -1) * pow(omxmz, -1)
                    + 79.0 / 2.0 * ln(x) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 2 * ln(x) * z * CF * pow(NC, -1) * rln2
                    + 11.0 / 2.0 * ln(x) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * z * CF * pow(opx, -1)
                    + (-1) * 3 * ln(x) * z * CF
                    + (-1) * 2 * ln(x) * z * CF * rln2 * pow(omx, -1)
                    + 4 * ln(x) * z * CF * rln2
                    + ln(x) * z * CF * NF * pow(omx, -1)
                    + (-1) * 4.0 / 3.0 * ln(x) * z * CF * NF
                    + 17.0 / 2.0 * ln(x) * z * CF * NC * pow(omx, -1)
                    + 1.0 / 2.0 * ln(x) * z * CF * NC * pow(omxmz, -2)
                    + (-1) * 1.0 / 2.0 * ln(x) * z * CF * NC * pow(omxmz, -1)
                    + (-1) * 67.0 / 6.0 * ln(x) * z * CF * NC
                    + (-1) * 4 * ln(x) * z * pow(CF, 2) * opx
                    + 1.0 / 2.0 * ln(x) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                    + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF * pow(omx, -1)
                    + 16 * ln(x) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8.0 / 3.0 * ln(x) * pow(z, 2) * CF
                    + 16 * ln(x) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + (-1) * 16 * ln(x) * pow(z, 2) * CF * rln2
                    + (-1) * 1.0 / 2.0 * ln(x) * pow(z, 2) * CF * NC * pow(omxmz, -2)
                    + (-1) * 16 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 16 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1)
                    + ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + 2 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 11.0 / 3.0 * ln(x) * x * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +3.0 / 2.0 * ln(x) * x * CF * pow(NC, -1) * pow(poly2, -2)
                    + 16 * ln(x) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * x * CF * pow(NC, -1) * pow(xmz, -1)
                    + 11 * ln(x) * x * CF * pow(NC, -1)
                    + 2 * ln(x) * x * CF * pow(NC, -1) * rln2
                    + (-1) * ln(x) * x * CF * pow(xmz, -1)
                    + (-1) * 9.0 / 2.0 * ln(x) * x * CF
                    + 2 * ln(x) * x * CF * rln2
                    + (-1) * 4.0 / 3.0 * ln(x) * x * CF * NF
                    + 3.0 / 2.0 * ln(x) * x * CF * NC * pow(xmz, -1)
                    + (-1) * 79.0 / 6.0 * ln(x) * x * CF * NC
                    + (-1) * 3.0 / 2.0 * ln(x) * x * z * CF * pow(NC, -1)
                    + (-1) * 3 * ln(x) * x * z * CF
                    + (-1) * 8 * ln(x) * x * z * CF * rln2
                    + 3.0 / 2.0 * ln(x) * x * z * CF * NC
                    + 4.0 / 3.0 * ln(x) * x * pow(z, 2) * CF
                    + (-1) * 1.0 / 2.0 * ln(x) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -2)
                    + (-1) * 3 * ln(x) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -1)
                    + 2 * ln(x) * pow(x, 2) * CF * pow(xmz, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * pow(x, 2) * CF * NC * pow(xmz, -2)
                    + ln(x) * pow(x, 2) * CF * NC * pow(xmz, -1)
                    + ln(x) * pow(x, 3) * CF * pow(NC, -1) * pow(poly2, -1)
                    + ln(x) * pow(x, 3) * CF * pow(NC, -1) * pow(xmz, -2)
                    + ln(x) * pow(x, 3) * CF * NC * pow(xmz, -2)
                    + 3.0 / 2.0 * ln(x) * pow(x, 4) * CF * pow(NC, -1) * pow(poly2, -2)
                    + (-1) * 3.0 / 2.0 * ln(x) * pow(x, 5) * CF * pow(NC, -1) * pow(poly2, -2)
                    + ln(x) * ln(1 - sqrtxz2 + x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 0
                )
                tmp += (
                    +ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                    + (-1) * 2 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                    + 3 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 4 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                    + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * ln(x) * ln(1 + sqrtxz2 + x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 0
                )
                tmp += (
                    +(-1) * 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                    + (-1) * 3 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * ln(1 + sqrtxz1 - z) * CF
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * CF
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                    + (-1) * 3 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                    + (-1) * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * CF
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                    + 0
                )
                tmp += (
                    +ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                    + (-1) * 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF
                    + (-1) * 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                    + ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * CF * pow(NC, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * x * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF
                    + 4 * ln(x) * ln(1 + x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 8 * ln(x) * ln(1 + x) * CF * pow(NC, -1) * pow(opx, -1)
                    + 8 * ln(x) * ln(1 + x) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(1 + x) * CF * pow(opx, -1)
                    + (-1) * 6 * ln(x) * ln(1 + x) * CF
                    + 4 * ln(x) * ln(1 + x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 8 * ln(x) * ln(1 + x) * z * CF * pow(opx, -1)
                    + 12 * ln(x) * ln(1 + x) * z * CF
                    + 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x) * x * CF
                    + 4 * ln(x) * ln(1 + x) * x * z * CF
                    + ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1)
                    + ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * pow(x, -2) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF
                    + ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1)
                    + ln(x) * ln(1 + x * z) * pow(x, -1) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF
                    + (-1) * 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(1 + x * z) * CF * pow(omx, -1)
                    + ln(x) * ln(1 + x * z) * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(1 + x * z) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF
                    + 2 * ln(x) * ln(1 + x * z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x * z) * x * z * CF
                    + 2 * ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(z + x) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * CF * pow(omx, -1)
                    + ln(x) * ln(z + x) * CF
                    + 2 * ln(x) * ln(z + x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * z * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(z + x) * z * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(z + x) * z * CF
                    + (-1) * 4 * ln(x) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                    + 4 * ln(x) * ln(z + x) * pow(z, 2) * CF
                    + (-1) * ln(x) * ln(z + x) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * x * CF * pow(NC, -1)
                    + ln(x) * ln(z + x) * x * CF
                    + 2 * ln(x) * ln(z + x) * x * z * CF
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(x, -2) * CF * pow(NC, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(x, -2) * z * CF
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -1) * CF * pow(NC, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * CF
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 3 * pow(ln(x), 2) * pow(x, -1) * z * CF
                    + (-1) * 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 16 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 16 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 11 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 10 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * pow(ln(x), 2) * pow(z, -1) * CF
                    + (-1) * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 13 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + 5 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 21.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(x), 2) * CF * pow(omx, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(x), 2) * CF * pow(opx, -1)
                    + 5 * pow(ln(x), 2) * CF
                    + 8 * pow(ln(x), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 5 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                    + (-1) * 4 * pow(ln(x), 2) * CF * NC * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(x), 2) * CF * NC
                    + 13 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 31.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                    + 4 * pow(ln(x), 2) * z * CF * pow(omx, -1)
                    + 5 * pow(ln(x), 2) * z * CF * pow(opx, -1)
                    + (-1) * 6 * pow(ln(x), 2) * z * CF
                    + (-1) * 5 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                    + 17.0 / 2.0 * pow(ln(x), 2) * z * CF * NC
                    + (-1) * 2 * pow(ln(x), 2) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * pow(ln(x), 2) * pow(z, 2) * CF
                    + 5 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 5 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * pow(ln(x), 2) * x * pow(z, -1) * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 17.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                    + 4 * pow(ln(x), 2) * x * CF
                    + (-1) * 4 * pow(ln(x), 2) * x * CF * NC * pow(omz, -1)
                    + 17.0 / 2.0 * pow(ln(x), 2) * x * CF * NC
                    + (-1) * 1.0 / 2.0 * pow(ln(x), 2) * x * z * CF * pow(NC, -1)
                    + (-1) * 4 * pow(ln(x), 2) * x * z * CF
                    + 1.0 / 2.0 * pow(ln(x), 2) * x * z * CF * NC
                    + (-1) * ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -2) * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(z) * pow(x, -2) * CF * pow(opx, -1)
                    + ln(x) * ln(z) * pow(x, -2) * CF
                    + 2 * ln(x) * ln(z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -2) * z * CF
                    + (-1) * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(z) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(z) * pow(x, -1) * CF
                    + 2 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(z) * pow(x, -1) * z * CF
                    + 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF
                    + 16 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 16 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 10 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 12 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                    + ln(x) * ln(z) * pow(z, -1) * CF
                    + 4 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 23.0 / 2.0 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(z) * CF * pow(NC, -1)
                    + ln(x) * ln(z) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(z) * CF * pow(opx, -1)
                    + (-1) * 8 * ln(x) * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 7.0 / 2.0 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                    + 4 * ln(x) * ln(z) * CF * NC * pow(omz, -1)
                    + (-1) * 27.0 / 2.0 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 19 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                    + (-1) * 7 * ln(x) * ln(z) * z * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(z) * z * CF * pow(opx, -1)
                    + 6 * ln(x) * ln(z) * z * CF
                    + 7.0 / 2.0 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(z) * z * CF * NC
                    + 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(z) * pow(z, 2) * CF
                    + (-1) * 6 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + ln(x) * ln(z) * x * pow(z, -1) * CF
                    + 9 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(z) * x * CF
                    + 4 * ln(x) * ln(z) * x * CF * NC * pow(omz, -1)
                    + (-1) * 5 * ln(x) * ln(z) * x * CF * NC
                    + (-1) * 2 * ln(x) * ln(z) * x * z * CF
                    + 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(x, -2) * CF
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF
                    + 2 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -1) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(omx) * pow(x, -1) * CF
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF
                    + (-1) * 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 8 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 8 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                    + 28 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 17 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 21 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(opx, -1)
                    + 15 * ln(x) * ln(omx) * CF * pow(NC, -1)
                    + 3 * ln(x) * ln(omx) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * CF
                    + (-1) * 10 * ln(x) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 8 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                    + 5 * ln(x) * ln(omx) * CF * NC * pow(omz, -1)
                    + (-1) * ln(x) * ln(omx) * CF * NC
                    + (-1) * 17 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 23 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * z * CF * pow(omx, -1)
                    + 4 * ln(x) * ln(omx) * z * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * z * CF
                    + 8 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                    + (-1) * 13 * ln(x) * ln(omx) * z * CF * NC
                    + 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8 * ln(x) * ln(omx) * pow(z, 2) * CF
                    + 4 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 7 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +9 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                    + 5 * ln(x) * ln(omx) * x * CF * NC * pow(omz, -1)
                    + (-1) * 13 * ln(x) * ln(omx) * x * CF * NC
                    + ln(x) * ln(omx) * x * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(omx) * x * z * CF * NC
                    + ln(x) * ln(omz) * pow(z, -1) * CF
                    + 18 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 16 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 12 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + 7 * ln(x) * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(omz) * CF
                    + (-1) * 12 * ln(x) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 8 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                    + 6 * ln(x) * ln(omz) * CF * NC * pow(omz, -1)
                    + (-1) * ln(x) * ln(omz) * CF * NC
                    + (-1) * 16 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 20 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                    + 8 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 14 * ln(x) * ln(omz) * z * CF * NC
                    + ln(x) * ln(omz) * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 14 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(omz) * x * CF
                    + 6 * ln(x) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + (-1) * 14 * ln(x) * ln(omz) * x * CF * NC
                    + ln(x) * ln(omz) * x * z * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(omz) * x * z * CF * NC
                    + (-1) * 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * pow(x, -2) * CF
                    + 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF
                    + (-1) * 2 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * pow(x, -1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * ln(opx) * pow(x, -1) * CF
                    + 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF
                    + 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * ln(x) * ln(opx) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(opx) * CF
                    + 4 * ln(x) * ln(opx) * z * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * z * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * z * CF
                    + 8 * ln(x) * ln(opx) * pow(z, 2) * CF
                    + (-1) * 2 * ln(x) * ln(opx) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * x * CF
                    + 4 * ln(x) * ln(opx) * x * z * CF
                    + (-1) * 24 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 27 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 6 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 3 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + (-1) * 3 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 13.0 / 6.0 * ln(z) * pow(z, -1) * CF
                    + (-1) * 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(poly2, -2)
                    + ln(z) * CF * pow(NC, -1) * pow(poly2, -1)
                    + 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(xmz, -1)
                    + 18 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 12 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(xmz, -1)
                    + (-1) * 45.0 / 2.0 * ln(z) * CF * pow(NC, -1)
                    + (-1) * 12 * ln(z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 6 * ln(z) * CF * pow(NC, -1) * rln2
                    + (-1) * 3 * ln(z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 3 * ln(z) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 3 * ln(z) * CF * pow(omx, -1)
                    + ln(z) * CF * pow(omz, -1)
                    + 7 * ln(z) * CF * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(z) * CF * rln2
                    + 3 * ln(z) * CF * sqrtxz1 * pow(omx, -1)
                    + (-1) * 2 * ln(z) * CF * sqrtxz1
                    + 9.0 / 2.0 * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * ln(z) * CF * NC * pow(omx, -1) * pow(xmz, -1)
                    + (-1) * 2 * ln(z) * CF * NC * pow(omx, -1)
                    + (-1) * 9 * ln(z) * CF * NC * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * ln(z) * CF * NC * pow(xmz, -1)
                    + 3 * ln(z) * CF * NC
                    + 8 * ln(z) * pow(CF, 2) * pow(omz, -1)
                    + (-1) * 4 * ln(z) * pow(CF, 2)
                    + 23 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 32 * ln(z) * z * CF * pow(NC, -1)
                    + (-1) * 6 * ln(z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 6 * ln(z) * z * CF * pow(NC, -1) * rln2
                    + (-1) * 3 * ln(z) * z * CF * pow(omx, -1)
                    + 7.0 / 2.0 * ln(z) * z * CF
                    + 10 * ln(z) * z * CF * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(z) * z * CF * rln2
                    + (-1) * 4 * ln(z) * z * CF * NC * pow(omx, -1)
                    + 11 * ln(z) * z * CF * NC
                    + (-1) * 4 * ln(z) * z * pow(CF, 2)
                    + 4.0 / 3.0 * ln(z) * pow(z, 2) * CF
                    + 16 * ln(z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 16 * ln(z) * pow(z, 2) * CF * rln2
                    + 8 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 11 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 3 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + 2 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 17.0 / 6.0 * ln(z) * x * pow(z, -1) * CF
                    + (-1) * 3.0 / 2.0 * ln(z) * x * CF * pow(NC, -1) * pow(poly2, -2)
                    + (-1) * 12 * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * ln(z) * x * CF * pow(NC, -1) * pow(xmz, -1)
                    + (-1) * 11.0 / 2.0 * ln(z) * x * CF * pow(NC, -1)
                    + 6 * ln(z) * x * CF * pow(NC, -1) * rln2
                    + (-1) * ln(z) * x * CF * pow(omz, -1)
                    + ln(z) * x * CF * pow(xmz, -1)
                    + 4 * ln(z) * x * CF
                    + (-1) * 2 * ln(z) * x * CF * rln2
                    + 3 * ln(z) * x * CF * NC * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * ln(z) * x * CF * NC * pow(xmz, -1)
                    + 6 * ln(z) * x * CF * NC
                    + (-1) * 8 * ln(z) * x * pow(CF, 2) * pow(omz, -1)
                    + 4 * ln(z) * x * pow(CF, 2)
                    + 2 * ln(z) * x * z * CF * pow(NC, -1)
                    + 3.0 / 2.0 * ln(z) * x * z * CF
                    + (-1) * 8 * ln(z) * x * z * CF * rln2
                    + (-1) * 2 * ln(z) * x * z * CF * NC
                    + 4 * ln(z) * x * z * pow(CF, 2)
                    + (-1) * 2.0 / 3.0 * ln(z) * x * pow(z, 2) * CF
                    + 1.0 / 2.0 * ln(z) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -2)
                    + 3 * ln(z) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -1)
                    + (-1) * 2 * ln(z) * pow(x, 2) * CF * pow(xmz, -1)
                    + 1.0 / 2.0 * ln(z) * pow(x, 2) * CF * NC * pow(xmz, -2)
                    + (-1) * ln(z) * pow(x, 2) * CF * NC * pow(xmz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(z) * pow(x, 3) * CF * pow(NC, -1) * pow(poly2, -1)
                    + (-1) * ln(z) * pow(x, 3) * CF * pow(NC, -1) * pow(xmz, -2)
                    + (-1) * ln(z) * pow(x, 3) * CF * NC * pow(xmz, -2)
                    + 3.0 / 2.0 * ln(z) * pow(x, 4) * CF * pow(NC, -1) * pow(poly2, -2)
                    + 3.0 / 2.0 * ln(z) * pow(x, 5) * CF * pow(NC, -1) * pow(poly2, -2)
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1)
                    + (-1) * 3 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                    + (-1) * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * CF
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 + z) * CF
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF
                    + 0
                )
                tmp += (
                    +(-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                    + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * CF
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF
                    + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * x * CF
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF
                    + ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1)
                    + ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * pow(x, -2) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF
                    + ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1)
                    + ln(z) * ln(1 + x * z) * pow(x, -1) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF
                    + (-1) * 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * z) * CF * pow(omx, -1)
                    + ln(z) * ln(1 + x * z) * CF * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(z) * ln(1 + x * z) * z * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1)
                    + 4 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF
                    + 2 * ln(z) * ln(1 + x * z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(1 + x * z) * x * z * CF
                    + (-1) * 2 * ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(z + x) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(z) * ln(z + x) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(z + x) * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(z + x) * CF
                    + (-1) * 2 * ln(z) * ln(z + x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(z) * ln(z + x) * z * CF * pow(NC, -1)
                    + 4 * ln(z) * ln(z + x) * z * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(z + x) * z * CF
                    + 4 * ln(z) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(z + x) * pow(z, 2) * CF
                    + ln(z) * ln(z + x) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(z + x) * x * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(z + x) * x * CF
                    + (-1) * 2 * ln(z) * ln(z + x) * x * z * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + pow(ln(z), 2) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(x, -2) * CF * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF * pow(opx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF
                    + pow(ln(z), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(x, -2) * z * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +pow(ln(z), 2) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * CF
                    + pow(ln(z), 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(x, -1) * z * CF * pow(NC, -1)
                    + pow(ln(z), 2) * pow(x, -1) * z * CF
                    + 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 3 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(z), 2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1)
                    + (-1) * pow(ln(z), 2) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(opx, -1)
                    + pow(ln(z), 2) * CF
                    + 2 * pow(ln(z), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * CF * NC
                    + 3 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                    + 2 * pow(ln(z), 2) * z * CF * pow(omx, -1)
                    + pow(ln(z), 2) * z * CF * pow(opx, -1)
                    + (-1) * 6 * pow(ln(z), 2) * z * CF
                    + (-1) * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * z * CF * NC
                    + (-1) * 2 * pow(ln(z), 2) * pow(z, 2) * CF * pow(omx, -1)
                    + 4 * pow(ln(z), 2) * pow(z, 2) * CF
                    + pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(z), 2) * x * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * x * CF * NC
                    + 1.0 / 2.0 * pow(ln(z), 2) * x * z * CF * pow(NC, -1)
                    + 2 * pow(ln(z), 2) * x * z * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * x * z * CF * NC
                    + (-1) * 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 8 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + 9 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(z) * ln(omx) * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(omx) * CF
                    + 4 * ln(z) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * CF * NC * pow(omz, -1)
                    + 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 11 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * z * CF
                    + (-1) * 2 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                    + 3 * ln(z) * ln(omx) * z * CF * NC
                    + 3 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 5 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(omx) * x * CF
                    + (-1) * 2 * ln(z) * ln(omx) * x * CF * NC * pow(omz, -1)
                    + 3 * ln(z) * ln(omx) * x * CF * NC
                    + (-1) * 14 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 13 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 11 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 6 * ln(z) * ln(omz) * CF * pow(NC, -1)
                    + ln(z) * ln(omz) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * CF
                    + 2 * ln(z) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
                    + 13 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 18 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * z * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(omz) * z * CF
                    + (-1) * ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +6 * ln(z) * ln(omz) * z * CF * NC
                    + 5 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 12 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + 6 * ln(z) * ln(omz) * x * CF * NC
                    + 6 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 2 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                    + 6 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                    + 8 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * sqrtxz3
                    + 6 * ln(sqrtxz3) * ArcTan(sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                    + 13.0 / 6.0 * ln(omx) * pow(z, -1) * CF
                    + (-1) * 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 23.0 / 2.0 * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 13.0 / 2.0 * ln(omx) * CF
                    + 12 * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(omx) * CF * NC * pow(omx, -1)
                    + (-1) * 12 * ln(omx) * CF * NC * pow(omz, -1)
                    + 1.0 / 2.0 * ln(omx) * CF * NC
                    + (-1) * 4 * ln(omx) * pow(CF, 2)
                    + 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 39.0 / 2.0 * ln(omx) * z * CF * pow(NC, -1)
                    + 1.0 / 2.0 * ln(omx) * z * CF
                    + 2.0 / 3.0 * ln(omx) * z * CF * NF
                    + (-1) * 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                    + 59.0 / 6.0 * ln(omx) * z * CF * NC
                    + (-1) * 4 * ln(omx) * z * pow(CF, 2)
                    + 4.0 / 3.0 * ln(omx) * pow(z, 2) * CF
                    + (-1) * 17.0 / 6.0 * ln(omx) * x * pow(z, -1) * CF
                    + (-1) * 5.0 / 2.0 * ln(omx) * x * CF * pow(NC, -1)
                    + 9.0 / 2.0 * ln(omx) * x * CF
                    + 0
                )
                tmp += (
                    +2.0 / 3.0 * ln(omx) * x * CF * NF
                    + 35.0 / 6.0 * ln(omx) * x * CF * NC
                    + 4 * ln(omx) * x * pow(CF, 2)
                    + 3.0 / 2.0 * ln(omx) * x * z * CF * pow(NC, -1)
                    + 3.0 / 2.0 * ln(omx) * x * z * CF
                    + (-1) * 3.0 / 2.0 * ln(omx) * x * z * CF * NC
                    + 4 * ln(omx) * x * z * pow(CF, 2)
                    + (-1) * 2.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF
                    + (-1) * 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1)
                    + 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                    + (-1) * 2 * pow(ln(omx), 2) * CF * NC * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(omx), 2) * CF * NC
                    + 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 13.0 / 2.0 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                    + 11.0 / 2.0 * pow(ln(omx), 2) * z * CF * NC
                    + 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(omx), 2) * x * CF * NC * pow(omz, -1)
                    + 11.0 / 2.0 * pow(ln(omx), 2) * x * CF * NC
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * x * z * CF * pow(NC, -1)
                    + 1.0 / 2.0 * pow(ln(omx), 2) * x * z * CF * NC
                    + (-1) * 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 5 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +8 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * CF * NC * pow(omz, -1)
                    + ln(omx) * ln(omz) * CF * NC
                    + 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 11 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                    + 11 * ln(omx) * ln(omz) * z * CF * NC
                    + 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 7 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * x * CF * NC * pow(omz, -1)
                    + 11 * ln(omx) * ln(omz) * x * CF * NC
                    + (-1) * ln(omx) * ln(omz) * x * z * CF * pow(NC, -1)
                    + ln(omx) * ln(omz) * x * z * CF * NC
                    + 13.0 / 6.0 * ln(omz) * pow(z, -1) * CF
                    + (-1) * 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                    + 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 1.0 / 2.0 * ln(omz) * CF * pow(NC, -1) * pow(omxmz, -1)
                    + (-1) * 14 * ln(omz) * CF * pow(NC, -1)
                    + (-1) * 13.0 / 2.0 * ln(omz) * CF
                    + 12 * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(omz) * CF * NC * pow(omx, -1)
                    + (-1) * 12 * ln(omz) * CF * NC * pow(omz, -1)
                    + 3.0 / 2.0 * ln(omz) * CF * NC * pow(omxmz, -1)
                    + 2 * ln(omz) * CF * NC
                    + (-1) * 4 * ln(omz) * pow(CF, 2)
                    + 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 1.0 / 2.0 * ln(omz) * z * CF * pow(NC, -1) * pow(omxmz, -2)
                    + (-1) * 3.0 / 2.0 * ln(omz) * z * CF * pow(NC, -1) * pow(omxmz, -1)
                    + (-1) * 18 * ln(omz) * z * CF * pow(NC, -1)
                    + 1.0 / 2.0 * ln(omz) * z * CF
                    + 2.0 / 3.0 * ln(omz) * z * CF * NF
                    + (-1) * 8 * ln(omz) * z * CF * NC * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * ln(omz) * z * CF * NC * pow(omxmz, -2)
                    + 1.0 / 2.0 * ln(omz) * z * CF * NC * pow(omxmz, -1)
                    + 0
                )
                tmp += (
                    +25.0 / 3.0 * ln(omz) * z * CF * NC
                    + (-1) * 4 * ln(omz) * z * pow(CF, 2)
                    + (-1) * 1.0 / 2.0 * ln(omz) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                    + 4.0 / 3.0 * ln(omz) * pow(z, 2) * CF
                    + 1.0 / 2.0 * ln(omz) * pow(z, 2) * CF * NC * pow(omxmz, -2)
                    + (-1) * 17.0 / 6.0 * ln(omz) * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(omz) * x * CF * pow(NC, -1)
                    + 9.0 / 2.0 * ln(omz) * x * CF
                    + 2.0 / 3.0 * ln(omz) * x * CF * NF
                    + 13.0 / 3.0 * ln(omz) * x * CF * NC
                    + 4 * ln(omz) * x * pow(CF, 2)
                    + 3.0 / 2.0 * ln(omz) * x * z * CF
                    + 4 * ln(omz) * x * z * pow(CF, 2)
                    + (-1) * 2.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF
                    + (-1) * 5 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 9.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1)
                    + 4 * pow(ln(omz), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * CF * NC * pow(omx, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * CF * NC
                    + 9.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 13.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                    + 11.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC
                    + 2 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * pow(ln(omz), 2) * x * CF * NC * pow(omz, -1)
                    + 11.0 / 2.0 * pow(ln(omz), 2) * x * CF * NC
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * x * z * CF * pow(NC, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * x * z * CF * NC
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                    + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 0
                )
                tmp += (
                    +3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 0
                )
                tmp += (
                    +3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1)
                    + 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1)
                    + (-1) * 6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                    + (-1) * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1)
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                    + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                    + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * CF * pow(NC, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1)
                    + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF
                    + 0
                )
                tmp += (
                    +Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * CF
                    + 8 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 8 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 6 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 6 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 6 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1)
                    + (-1) * Li2(1 - x * pow(z, -1)) * CF * pow(omx, -1)
                    + 2 * Li2(1 - x * pow(z, -1)) * CF
                    + 2 * Li2(1 - x * pow(z, -1)) * CF * NC * pow(omx, -1) * pow(omz, -1)
                    + (-1) * Li2(1 - x * pow(z, -1)) * CF * NC * pow(omx, -1)
                    + (-1) * Li2(1 - x * pow(z, -1)) * CF * NC * pow(omz, -1)
                    + (-1) * 6 * Li2(1 - x * pow(z, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * Li2(1 - x * pow(z, -1)) * z * CF * pow(NC, -1)
                    + 2 * Li2(1 - x * pow(z, -1)) * z * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(1 - x * pow(z, -1)) * z * CF
                    + (-1) * Li2(1 - x * pow(z, -1)) * z * CF * NC * pow(omx, -1)
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                    + Li2(1 - x * pow(z, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * Li2(1 - x * pow(z, -1)) * x * CF * pow(NC, -1)
                    + (-1) * Li2(1 - x * pow(z, -1)) * x * CF * NC * pow(omz, -1)
                    + Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1)
                    + Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(x, -2) * CF
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF
                    + Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                    + Li2(-x * pow(z, -1)) * pow(x, -1) * CF
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(-x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * CF * pow(omx, -1)
                    + Li2(-x * pow(z, -1)) * CF * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * z * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1)
                    + 4 * Li2(-x * pow(z, -1)) * z * CF
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * x * CF * pow(NC, -1)
                    + 2 * Li2(-x * pow(z, -1)) * x * CF
                    + (-1) * 2 * Li2(-x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(-x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(-x) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * pow(x, -2) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x) * pow(x, -2) * CF * pow(opx, -1)
                    + 2 * Li2(-x) * pow(x, -2) * CF
                    + 4 * Li2(-x) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * pow(x, -2) * z * CF
                    + (-1) * 2 * Li2(-x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(-x) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x) * pow(x, -1) * CF
                    + 4 * Li2(-x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 4 * Li2(-x) * pow(x, -1) * z * CF
                    + 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * Li2(-x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(-x) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(-x) * CF * pow(NC, -1)
                    + 2 * Li2(-x) * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * CF
                    + 4 * Li2(-x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * z * CF * pow(opx, -1)
                    + 8 * Li2(-x) * z * CF
                    + 8 * Li2(-x) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(-x) * x * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(-x) * x * CF
                    + 8 * Li2(-x) * x * z * CF
                    + Li2(-x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * Li2(-x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(x, -2) * CF * pow(NC, -1)
                    + Li2(-x * z) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * Li2(-x * z) * pow(x, -2) * CF
                    + (-1) * 2 * Li2(-x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(x, -2) * z * CF
                    + Li2(-x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * Li2(-x * z) * pow(x, -1) * CF * pow(NC, -1)
                    + Li2(-x * z) * pow(x, -1) * CF
                    + (-1) * 2 * Li2(-x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(x, -1) * z * CF
                    + (-1) * 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(-x * z) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(-x * z) * CF * pow(NC, -1)
                    + 2 * Li2(-x * z) * CF * pow(omx, -1)
                    + Li2(-x * z) * CF * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * z) * CF
                    + (-1) * 2 * Li2(-x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(-x * z) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(-x * z) * z * CF * pow(opx, -1)
                    + 4 * Li2(-x * z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * Li2(-x * z) * pow(z, 2) * CF
                    + 2 * Li2(-x * z) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(-x * z) * x * z * CF
                    + 2 * Li2(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(x) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(x) * pow(x, -2) * CF * pow(NC, -1)
                    + 2 * Li2(x) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * 2 * Li2(x) * pow(x, -2) * CF
                    + (-1) * 4 * Li2(x) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 4 * Li2(x) * pow(x, -2) * z * CF
                    + 2 * Li2(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(x) * pow(x, -1) * CF * pow(NC, -1)
                    + 2 * Li2(x) * pow(x, -1) * CF
                    + (-1) * 4 * Li2(x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(x) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(x) * pow(x, -1) * z * CF
                    + (-1) * 8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 8 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 8 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(x) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * Li2(x) * pow(z, -1) * CF
                    + 12 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + (-1) * 3 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 8 * Li2(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * Li2(x) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(x) * CF * pow(NC, -1)
                    + 3 * Li2(x) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(x) * CF * pow(opx, -1)
                    + (-1) * 3 * Li2(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 3 * Li2(x) * z * CF * pow(NC, -1)
                    + (-1) * 6 * Li2(x) * z * CF * pow(omx, -1)
                    + 4 * Li2(x) * z * CF * pow(opx, -1)
                    + 4 * Li2(x) * z * CF
                    + Li2(x) * z * CF * NC
                    + 8 * Li2(x) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * Li2(x) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8 * Li2(x) * pow(z, 2) * CF
                    + 4 * Li2(x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4 * Li2(x) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * Li2(x) * x * pow(z, -1) * CF
                    + (-1) * 4 * Li2(x) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * Li2(x) * x * CF * pow(NC, -1)
                    + 2 * Li2(x) * x * CF
                    + Li2(x) * x * CF * NC
                    + (-1) * 4 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                    + 5 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(z) * CF * pow(NC, -1)
                    + Li2(z) * CF * pow(omx, -1)
                    + (-1) * Li2(z) * CF
                    + 5 * Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 7 * Li2(z) * z * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(z) * z * CF * pow(omx, -1)
                    + 6 * Li2(z) * z * CF
                    + 3 * Li2(z) * z * CF * NC
                    + Li2(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 5 * Li2(z) * x * CF * pow(NC, -1)
                    + Li2(z) * x * CF
                    + 3 * Li2(z) * x * CF * NC
                    + 3 * InvTanInt(-sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * InvTanInt(-sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                    + 3 * InvTanInt(-sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                    + 4 * InvTanInt(-sqrtxz3) * z * CF * sqrtxz3
                    + 3 * InvTanInt(-sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                    + 6 * InvTanInt(z * sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 2 * InvTanInt(z * sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                    + 6 * InvTanInt(z * sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                    + 8 * InvTanInt(z * sqrtxz3) * z * CF * sqrtxz3
                    + 6 * InvTanInt(z * sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 3 * InvTanInt(sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                    + InvTanInt(sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 3 * InvTanInt(sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                    + (-1) * 4 * InvTanInt(sqrtxz3) * z * CF * sqrtxz3
                    + (-1) * 3 * InvTanInt(sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                    + 0
                )
            if ("001" in orders) or ("all" in orders):
                tmp += 1.0 / 3.0 * pow(z, -1) * LMUA * CF + 3 * LMUA * CF * pow(NC, -1) + 3.0 / 2.0 * LMUA * CF + (-1) * 3 * LMUA * CF * NC + 4 * LMUA * pow(CF, 2) + 0
                tmp += (
                    3.0 / 2.0 * z * LMUA * CF * pow(NC, -1)
                    + (-1) * 1.0 / 2.0 * z * LMUA * CF
                    + (-1) * 3.0 / 2.0 * z * LMUA * CF * NC
                    + 4 * z * LMUA * pow(CF, 2)
                    + (-1) * 4.0 / 3.0 * pow(z, 2) * LMUA * CF
                    + 1.0 / 3.0 * x * pow(z, -1) * LMUA * CF
                    + (-1) * 1.0 / 2.0 * x * LMUA * CF * pow(NC, -1)
                    + 1.0 / 2.0 * x * LMUA * CF
                    + 1.0 / 2.0 * x * LMUA * CF * NC
                    + (-1) * 4 * x * LMUA * pow(CF, 2)
                    + (-1) * x * z * LMUA * CF * pow(NC, -1)
                    + (-1) * 3.0 / 2.0 * x * z * LMUA * CF
                    + 0
                )
                tmp += x * z * LMUA * CF * NC + (-1) * 4 * x * z * LMUA * pow(CF, 2) + 2.0 / 3.0 * x * pow(z, 2) * LMUA * CF + 0
                tmp += ln(x) * LMUA * CF * pow(NC, -1) * pow(omx, -1) + (-1) * 1.0 / 2.0 * ln(x) * LMUA * CF * pow(NC, -1) + (-1) * ln(x) * LMUA * CF * NC * pow(omx, -1) + 0
                tmp += 1.0 / 2.0 * ln(x) * LMUA * CF * NC + ln(x) * z * LMUA * CF * pow(NC, -1) * pow(omx, -1) + (-1) * 1.0 / 2.0 * ln(x) * z * LMUA * CF * pow(NC, -1) + (-1) * ln(x) * z * LMUA * CF * NC * pow(omx, -1) + 1.0 / 2.0 * ln(x) * z * LMUA * CF * NC + 0
                tmp += (-1) * 1.0 / 2.0 * ln(x) * x * LMUA * CF * pow(NC, -1) + 1.0 / 2.0 * ln(x) * x * LMUA * CF * NC + (-1) * 1.0 / 2.0 * ln(x) * x * z * LMUA * CF * pow(NC, -1) + 1.0 / 2.0 * ln(x) * x * z * LMUA * CF * NC + 0
                tmp += ln(z) * LMUA * CF * pow(NC, -1) * pow(omz, -1) + (-1) * 1.0 / 2.0 * ln(z) * LMUA * CF * pow(NC, -1) + ln(z) * LMUA * CF + (-1) * ln(z) * LMUA * CF * NC * pow(omz, -1) + 1.0 / 2.0 * ln(z) * LMUA * CF * NC + (-1) * 3.0 / 2.0 * ln(z) * z * LMUA * CF * pow(NC, -1) + 2 * ln(z) * z * LMUA * CF + 3.0 / 2.0 * ln(z) * z * LMUA * CF * NC + 0
                tmp += ln(z) * x * LMUA * CF * pow(NC, -1) * pow(omz, -1) + (-1) * 3.0 / 2.0 * ln(z) * x * LMUA * CF * pow(NC, -1) + ln(z) * x * LMUA * CF + (-1) * ln(z) * x * LMUA * CF * NC * pow(omz, -1) + 3.0 / 2.0 * ln(z) * x * LMUA * CF * NC + (-1) * 1.0 / 2.0 * ln(z) * x * z * LMUA * CF * pow(NC, -1) + 1.0 / 2.0 * ln(z) * x * z * LMUA * CF * NC + 0
                tmp += 1.0 / 2.0 * ln(omx) * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omx) * LMUA * CF * NC + 1.0 / 2.0 * ln(omx) * z * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omx) * z * LMUA * CF * NC + 0
                tmp += 1.0 / 2.0 * ln(omx) * x * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omx) * x * LMUA * CF * NC + 1.0 / 2.0 * ln(omx) * x * z * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omx) * x * z * LMUA * CF * NC + 0
                tmp += 1.0 / 2.0 * ln(omz) * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * CF * NC + 0
                tmp += 5.0 / 2.0 * ln(omz) * z * LMUA * CF * pow(NC, -1) + (-1) * 5.0 / 2.0 * ln(omz) * z * LMUA * CF * NC + 5.0 / 2.0 * ln(omz) * x * LMUA * CF * pow(NC, -1) + (-1) * 5.0 / 2.0 * ln(omz) * x * LMUA * CF * NC + 1.0 / 2.0 * ln(omz) * x * z * LMUA * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omz) * x * z * LMUA * CF * NC + 0
            if ("010" in orders) or ("all" in orders):
                tmp += (-1) * 5.0 / 2.0 * pow(z, -1) * LMUF * CF + LMUF * CF * pow(NC, -1) + 5 * LMUF * CF + (-1) * LMUF * CF * NC + 0
                tmp += 3.0 / 2.0 * z * LMUF * CF * pow(NC, -1) + (-1) * 3.0 / 2.0 * z * LMUF * CF * NC + 5.0 / 2.0 * x * pow(z, -1) * LMUF * CF + (-1) * 1.0 / 2.0 * x * LMUF * CF * pow(NC, -1) + (-1) * 5 * x * LMUF * CF + 1.0 / 2.0 * x * LMUF * CF * NC + x * z * LMUF * CF * pow(NC, -1) + (-1) * x * z * LMUF * CF * NC + 0
                tmp += (-1) * ln(x) * pow(z, -1) * LMUF * CF + ln(x) * LMUF * CF * pow(NC, -1) * pow(omx, -1) + (-1) * 1.0 / 2.0 * ln(x) * LMUF * CF * pow(NC, -1) + 2 * ln(x) * LMUF * CF + (-1) * ln(x) * LMUF * CF * NC * pow(omx, -1) + 1.0 / 2.0 * ln(x) * LMUF * CF * NC + 0
                tmp += ln(x) * z * LMUF * CF * pow(NC, -1) * pow(omx, -1) + (-1) * 3.0 / 2.0 * ln(x) * z * LMUF * CF * pow(NC, -1) + (-1) * ln(x) * z * LMUF * CF * NC * pow(omx, -1) + 3.0 / 2.0 * ln(x) * z * LMUF * CF * NC + 0
                tmp += (-1) * ln(x) * x * pow(z, -1) * LMUF * CF + (-1) * 3.0 / 2.0 * ln(x) * x * LMUF * CF * pow(NC, -1) + 2 * ln(x) * x * LMUF * CF + 3.0 / 2.0 * ln(x) * x * LMUF * CF * NC + (-1) * 1.0 / 2.0 * ln(x) * x * z * LMUF * CF * pow(NC, -1) + 1.0 / 2.0 * ln(x) * x * z * LMUF * CF * NC + 0
                tmp += (-1) * ln(z) * LMUF * CF * pow(NC, -1) * pow(omz, -1) + 1.0 / 2.0 * ln(z) * LMUF * CF * pow(NC, -1) + ln(z) * LMUF * CF * NC * pow(omz, -1) + (-1) * 1.0 / 2.0 * ln(z) * LMUF * CF * NC + 1.0 / 2.0 * ln(z) * z * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(z) * z * LMUF * CF * NC + 0
                tmp += (-1) * ln(z) * x * LMUF * CF * pow(NC, -1) * pow(omz, -1) + 1.0 / 2.0 * ln(z) * x * LMUF * CF * pow(NC, -1) + ln(z) * x * LMUF * CF * NC * pow(omz, -1) + (-1) * 1.0 / 2.0 * ln(z) * x * LMUF * CF * NC + 1.0 / 2.0 * ln(z) * x * z * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(z) * x * z * LMUF * CF * NC + 0
                tmp += 1.0 / 2.0 * ln(omx) * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omx) * LMUF * CF * NC + 5.0 / 2.0 * ln(omx) * z * LMUF * CF * pow(NC, -1) + (-1) * 5.0 / 2.0 * ln(omx) * z * LMUF * CF * NC + 0
                tmp += 5.0 / 2.0 * ln(omx) * x * LMUF * CF * pow(NC, -1) + (-1) * 5.0 / 2.0 * ln(omx) * x * LMUF * CF * NC + 1.0 / 2.0 * ln(omx) * x * z * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omx) * x * z * LMUF * CF * NC + 0
                tmp += 1.0 / 2.0 * ln(omz) * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omz) * LMUF * CF * NC + 0
                tmp += 1.0 / 2.0 * ln(omz) * z * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omz) * z * LMUF * CF * NC + 1.0 / 2.0 * ln(omz) * x * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omz) * x * LMUF * CF * NC + 1.0 / 2.0 * ln(omz) * x * z * LMUF * CF * pow(NC, -1) + (-1) * 1.0 / 2.0 * ln(omz) * x * z * LMUF * CF * NC + 0
            if ("011" in orders) or ("all" in orders):
                tmp += (-1) * 1.0 / 2.0 * LMUA * LMUF * CF * pow(NC, -1) + 1.0 / 2.0 * LMUA * LMUF * CF * NC + 0
                tmp += (-1) * 1.0 / 2.0 * z * LMUA * LMUF * CF * pow(NC, -1) + 1.0 / 2.0 * z * LMUA * LMUF * CF * NC + (-1) * 1.0 / 2.0 * x * LMUA * LMUF * CF * pow(NC, -1) + 1.0 / 2.0 * x * LMUA * LMUF * CF * NC + 0
                tmp += (-1) * 1.0 / 2.0 * x * z * LMUA * LMUF * CF * pow(NC, -1) + 1.0 / 2.0 * x * z * LMUA * LMUF * CF * NC + 0
            if ("100" in orders) or ("all" in orders):
                tmp += (-1) * 2.0 / 3.0 * z * LMUR * CF * NF + 11.0 / 3.0 * z * LMUR * CF * NC + (-1) * 2.0 / 3.0 * x * LMUR * CF * NF + 11.0 / 3.0 * x * LMUR * CF * NC + 0
            res += tmp

        return res
