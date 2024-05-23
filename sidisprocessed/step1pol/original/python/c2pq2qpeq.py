from core.definitions import CF, NC, TR
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi


def C2Pq2qpEq(inx, inz, cx, cz, Q, muR, muF, muA):
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
        res = (
            -107.0 / 108.0 * pow(z, -1) * CF
            + 7.0 / 18.0 * pow(z, -1) * LMUA * CF
            + 1.0 / 3.0 * pow(z, -1) * pow(LMUA, 2) * CF
            - 11.0 / 9.0 * CF
            + 10.0 / 3.0 * LMUA * CF
            + 1.0 / 4.0 * pow(LMUA, 2) * CF
            - 4.0 / 9.0 * z * CF
            - 7.0 / 3.0 * z * LMUA * CF
            - 1.0 / 4.0 * z * pow(LMUA, 2) * CF
            + 287.0 / 108.0 * pow(z, 2) * CF
            - 25.0 / 18.0 * pow(z, 2) * LMUA * CF
            - 1.0 / 3.0 * pow(z, 2) * pow(LMUA, 2) * CF
            + 2 * zeta3 * CF
            + 2 * zeta3 * z * CF
            - 1.0 / 6.0 * pow(pi, 2) * CF
            - 1.0 / 6.0 * pow(pi, 2) * LMUA * CF
            - 1.0 / 4.0 * pow(pi, 2) * z * CF
            - 1.0 / 6.0 * pow(pi, 2) * z * LMUA * CF
            - 7.0 / 18.0 * ln(z) * pow(z, -1) * CF
            - 2.0 / 3.0 * ln(z) * pow(z, -1) * LMUA * CF
            - 5 * ln(z) * CF
            + 1.0 / 2.0 * ln(z) * LMUA * CF
            + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF
            - 9.0 / 2.0 * ln(z) * z * CF
            + 2 * ln(z) * z * LMUA * CF
            + 1.0 / 2.0 * ln(z) * z * pow(LMUA, 2) * CF
            - 31.0 / 18.0 * ln(z) * pow(z, 2) * CF
            + 2.0 / 3.0 * ln(z) * pow(z, 2) * LMUA * CF
            + 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF
            + 1.0 / 6.0 * ln(z) * pow(pi, 2) * z * CF
            + 1.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF
            - 1.0 / 8.0 * pow(ln(z), 2) * CF
            - pow(ln(z), 2) * LMUA * CF
            - 5.0 / 8.0 * pow(ln(z), 2) * z * CF
            - pow(ln(z), 2) * z * LMUA * CF
            + 5.0 / 12.0 * pow(ln(z), 3) * CF
            + 5.0 / 12.0 * pow(ln(z), 3) * z * CF
            - 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF
            - 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * z * CF
            - 7.0 / 18.0 * ln(omz) * pow(z, -1) * CF
            - 2.0 / 3.0 * ln(omz) * pow(z, -1) * LMUA * CF
            - 10.0 / 3.0 * ln(omz) * CF
            - 1.0 / 2.0 * ln(omz) * LMUA * CF
            + 7.0 / 3.0 * ln(omz) * z * CF
            + 1.0 / 2.0 * ln(omz) * z * LMUA * CF
            + 25.0 / 18.0 * ln(omz) * pow(z, 2) * CF
            + 2.0 / 3.0 * ln(omz) * pow(z, 2) * LMUA * CF
            + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * CF
            + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * z * CF
            + 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF
            + 1.0 / 4.0 * pow(ln(omz), 2) * CF
            - 1.0 / 4.0 * pow(ln(omz), 2) * z * CF
            - 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF
            - ln(omz) * Li2(1 - z) * CF
        )
        res += -ln(omz) * Li2(1 - z) * z * CF - 2 * ln(omz) * Li2(z) * CF - 2 * ln(omz) * Li2(z) * z * CF - Li3(1 - z) * CF - Li3(1 - z) * z * CF - 2 * Li3(z) * CF - 2 * Li3(z) * z * CF - 2.0 / 3.0 * Li2(z) * pow(z, -1) * CF + 1.0 / 2.0 * Li2(z) * CF + Li2(z) * LMUA * CF + 2 * Li2(z) * z * CF + Li2(z) * z * LMUA * CF + 2.0 / 3.0 * Li2(z) * pow(z, 2) * CF

        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = (
            -7.0 / 18.0 * pow(z, -1) * CF
            - 2.0 / 3.0 * pow(z, -1) * LMUA * CF
            - 10.0 / 3.0 * CF
            - 1.0 / 2.0 * LMUA * CF
            + 7.0 / 3.0 * z * CF
            + 1.0 / 2.0 * z * LMUA * CF
            + 25.0 / 18.0 * pow(z, 2) * CF
            + 2.0 / 3.0 * pow(z, 2) * LMUA * CF
            + 1.0 / 6.0 * pow(pi, 2) * CF
            + 1.0 / 6.0 * pow(pi, 2) * z * CF
            + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF
            - 1.0 / 2.0 * ln(z) * CF
            - ln(z) * LMUA * CF
            - 2 * ln(z) * z * CF
            - ln(z) * z * LMUA * CF
            - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF
            + pow(ln(z), 2) * CF
            + pow(ln(z), 2) * z * CF
            + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF
            + 1.0 / 2.0 * ln(omz) * CF
            - 1.0 / 2.0 * ln(omz) * z * CF
            - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF
            - Li2(z) * CF
            - Li2(z) * z * CF
        )

        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 2.0 / 3.0 * pow(z, -1) * CF + 1.0 / 2.0 * CF - 1.0 / 2.0 * z * CF - 2.0 / 3.0 * pow(z, 2) * CF + ln(z) * CF + ln(z) * z * CF

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
                -5.0 / 36.0 * pow(z, -1) * CF
                + 1.0 / 3.0 * pow(z, -1) * LMUA * CF
                + 2.0 / 3.0 * CF
                + 3.0 / 2.0 * LMUA * CF
                + 37.0 / 12.0 * z * CF
                - 1.0 / 2.0 * z * LMUA * CF
                - 65.0 / 18.0 * pow(z, 2) * CF
                - 4.0 / 3.0 * pow(z, 2) * LMUA * CF
                + 19.0 / 36.0 * x * pow(z, -1) * CF
                + 1.0 / 3.0 * x * pow(z, -1) * LMUA * CF
                + 5.0 / 3.0 * x * CF
                + 1.0 / 2.0 * x * LMUA * CF
                - 47.0 / 12.0 * x * z * CF
                - 3.0 / 2.0 * x * z * LMUA * CF
                + 31.0 / 18.0 * x * pow(z, 2) * CF
                + 2.0 / 3.0 * x * pow(z, 2) * LMUA * CF
                - 1.0 / 6.0 * pow(pi, 2) * CF
                - 1.0 / 3.0 * pow(pi, 2) * z * CF
                - 1.0 / 6.0 * pow(pi, 2) * x * CF
                - 4.0 / 3.0 * ln(x) * pow(z, -1) * CF * pow(omx, -1)
                + 2.0 / 3.0 * ln(x) * pow(z, -1) * CF
                - 5.0 / 2.0 * ln(x) * CF * pow(omx, -1)
                + 3 * ln(x) * CF
                + 5.0 / 2.0 * ln(x) * z * CF * pow(omx, -1)
                - ln(x) * z * CF
                + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF * pow(omx, -1)
                - 8.0 / 3.0 * ln(x) * pow(z, 2) * CF
                + 2.0 / 3.0 * ln(x) * x * pow(z, -1) * CF
                + ln(x) * x * CF
                - 3 * ln(x) * x * z * CF
                + 4.0 / 3.0 * ln(x) * x * pow(z, 2) * CF
                - 3 * ln(x) * ln(z) * CF * pow(omx, -1)
                + 2 * ln(x) * ln(z) * CF
                - 3 * ln(x) * ln(z) * z * CF * pow(omx, -1)
                + 4 * ln(x) * ln(z) * z * CF
                + 2 * ln(x) * ln(z) * x * CF
                - 1.0 / 3.0 * ln(z) * pow(z, -1) * CF
                - 5.0 / 2.0 * ln(z) * CF
                + ln(z) * LMUA * CF
                + 3.0 / 2.0 * ln(z) * z * CF
                + 2 * ln(z) * z * LMUA * CF
                + 4.0 / 3.0 * ln(z) * pow(z, 2) * CF
                - 1.0 / 3.0 * ln(z) * x * pow(z, -1) * CF
                + 1.0 / 2.0 * ln(z) * x * CF
                + ln(z) * x * LMUA * CF
                + 3.0 / 2.0 * ln(z) * x * z * CF
                - 2.0 / 3.0 * ln(z) * x * pow(z, 2) * CF
                - pow(ln(z), 2) * CF
                - 2 * pow(ln(z), 2) * z * CF
                - pow(ln(z), 2) * x * CF
                - ln(z) * ln(omx) * CF
                - 2 * ln(z) * ln(omx) * z * CF
                - ln(z) * ln(omx) * x * CF
                - 1.0 / 3.0 * ln(omx) * pow(z, -1) * CF
                - 3.0 / 2.0 * ln(omx) * CF
                + 1.0 / 2.0 * ln(omx) * z * CF
                + 4.0 / 3.0 * ln(omx) * pow(z, 2) * CF
                - 1.0 / 3.0 * ln(omx) * x * pow(z, -1) * CF
                - 1.0 / 2.0 * ln(omx) * x * CF
                + 3.0 / 2.0 * ln(omx) * x * z * CF
                - 2.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF
                - 1.0 / 3.0 * ln(omz) * pow(z, -1) * CF
            )
            tmp += -3.0 / 2.0 * ln(omz) * CF + 1.0 / 2.0 * ln(omz) * z * CF + 4.0 / 3.0 * ln(omz) * pow(z, 2) * CF - 1.0 / 3.0 * ln(omz) * x * pow(z, -1) * CF - 1.0 / 2.0 * ln(omz) * x * CF + 3.0 / 2.0 * ln(omz) * x * z * CF - 2.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF + Li2(z) * CF + 2 * Li2(z) * z * CF + Li2(z) * x * CF

            res += tmp

        return res
