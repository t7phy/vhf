from configs.eh import *


def C2Pq2qpEqp_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
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
        res = (
            9 * CF
            + 3 * LMUF * CF
            + 5.0 / 4.0 * pow(LMUF, 2) * CF
            - 9 * x * CF
            - 3 * x * LMUF * CF
            - 5.0 / 4.0 * x * pow(LMUF, 2) * CF
            - 1.0 / 2.0 * pow(pi, 2) * CF
            - 1.0 / 6.0 * pow(pi, 2) * LMUF * CF
            + 1.0 / 2.0 * pow(pi, 2) * x * CF
            - 1.0 / 6.0 * pow(pi, 2) * x * LMUF * CF
            + 25.0 / 4.0 * ln(x) * CF
            + 3 * ln(x) * LMUF * CF
            + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * CF
            - 3.0 / 4.0 * ln(x) * x * CF
            - 3 * ln(x) * x * LMUF * CF
            + 1.0 / 2.0 * ln(x) * x * pow(LMUF, 2) * CF
            - 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF
            - 1.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF
            + 17.0 / 8.0 * pow(ln(x), 2) * CF
            + pow(ln(x), 2) * LMUF * CF
            - 15.0 / 8.0 * pow(ln(x), 2) * x * CF
            + pow(ln(x), 2) * x * LMUF * CF
            + 5.0 / 12.0 * pow(ln(x), 3) * CF
            + 5.0 / 12.0 * pow(ln(x), 3) * x * CF
            - 5.0 / 2.0 * ln(x) * ln(omx) * CF
            + 5.0 / 2.0 * ln(x) * ln(omx) * x * CF
            - 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF
            - 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF
            + ln(x) * Li2(x) * CF
            + ln(x) * Li2(x) * x * CF
            - 3 * ln(omx) * CF
            - 5.0 / 2.0 * ln(omx) * LMUF * CF
            + 3 * ln(omx) * x * CF
            + 5.0 / 2.0 * ln(omx) * x * LMUF * CF
            + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * CF
            + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * x * CF
            + 5.0 / 4.0 * pow(ln(omx), 2) * CF
            - 5.0 / 4.0 * pow(ln(omx), 2) * x * CF
            - ln(omx) * Li2(1 - x) * CF
            - ln(omx) * Li2(1 - x) * x * CF
            - 2 * ln(omx) * Li2(x) * CF
            - 2 * ln(omx) * Li2(x) * x * CF
            - Li3(1 - x) * CF
            - Li3(1 - x) * x * CF
            + 1.0 / 2.0 * Li2(x) * CF
            + Li2(x) * LMUF * CF
            - 1.0 / 2.0 * Li2(x) * x * CF
            + Li2(x) * x * LMUF * CF
        )

        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = -3 * CF - 5.0 / 2.0 * LMUF * CF + 3 * x * CF + 5.0 / 2.0 * x * LMUF * CF + 1.0 / 6.0 * pow(pi, 2) * CF + 1.0 / 6.0 * pow(pi, 2) * x * CF - 3 * ln(x) * CF - ln(x) * LMUF * CF + 3 * ln(x) * x * CF - ln(x) * x * LMUF * CF - pow(ln(x), 2) * CF - pow(ln(x), 2) * x * CF + 5.0 / 2.0 * ln(omx) * CF - 5.0 / 2.0 * ln(omx) * x * CF - Li2(x) * CF - Li2(x) * x * CF

        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 5.0 / 2.0 * CF - 5.0 / 2.0 * x * CF + ln(x) * CF + ln(x) * x * CF

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
            tmp = 0

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = 0

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = 0

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
                -3 * pow(z, -1) * CF
                - 5.0 / 2.0 * pow(z, -1) * LMUF * CF
                + 10 * CF
                + 5 * LMUF * CF
                + 3 * x * pow(z, -1) * CF
                + 5.0 / 2.0 * x * pow(z, -1) * LMUF * CF
                - 10 * x * CF
                - 5 * x * LMUF * CF
                + 1.0 / 6.0 * pow(pi, 2) * pow(z, -1) * CF
                - 1.0 / 3.0 * pow(pi, 2) * CF
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF
                - 1.0 / 3.0 * pow(pi, 2) * x * CF
                - 3 * ln(x) * pow(z, -1) * CF
                - ln(x) * pow(z, -1) * LMUF * CF
                + 1.0 / 2.0 * ln(x) * CF * pow(poly2, -1)
                + 8 * ln(x) * CF
                + 2 * ln(x) * LMUF * CF
                + 3 * ln(x) * x * pow(z, -1) * CF
                - ln(x) * x * pow(z, -1) * LMUF * CF
                - 1.0 / 2.0 * ln(x) * x * CF * pow(poly2, -1)
                - 4 * ln(x) * x * CF
                + 2 * ln(x) * x * LMUF * CF
                - 1.0 / 2.0 * ln(x) * pow(x, 2) * CF * pow(poly2, -1)
                + 1.0 / 2.0 * ln(x) * pow(x, 3) * CF * pow(poly2, -1)
                + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                -pow(ln(x), 2) * pow(z, -1) * CF
                + 2 * pow(ln(x), 2) * CF
                - pow(ln(x), 2) * x * pow(z, -1) * CF
                + 2 * pow(ln(x), 2) * x * CF
                + ln(x) * ln(z) * pow(z, -1) * CF
                - ln(x) * ln(z) * CF
                + ln(x) * ln(z) * x * pow(z, -1) * CF
                - ln(x) * ln(z) * x * CF
                + ln(x) * ln(omz) * pow(z, -1) * CF
                - 2 * ln(x) * ln(omz) * CF
                + ln(x) * ln(omz) * x * pow(z, -1) * CF
                - 2 * ln(x) * ln(omz) * x * CF
                + 5.0 / 2.0 * ln(z) * pow(z, -1) * CF
                + 1.0 / 2.0 * ln(z) * CF * pow(poly2, -1)
                + ln(z) * CF * pow(omz, -1)
                - 2 * ln(z) * CF
                - 5.0 / 2.0 * ln(z) * x * pow(z, -1) * CF
                + 1.0 / 2.0 * ln(z) * x * CF * pow(poly2, -1)
                - ln(z) * x * CF * pow(omz, -1)
                + 2 * ln(z) * x * CF
                - 1.0 / 2.0 * ln(z) * pow(x, 2) * CF * pow(poly2, -1)
                - 1.0 / 2.0 * ln(z) * pow(x, 3) * CF * pow(poly2, -1)
                + 5.0 / 2.0 * ln(omx) * pow(z, -1) * CF
                - 5 * ln(omx) * CF
                - 5.0 / 2.0 * ln(omx) * x * pow(z, -1) * CF
                + 5 * ln(omx) * x * CF
                + 5.0 / 2.0 * ln(omz) * pow(z, -1) * CF
                - 5 * ln(omz) * CF
                - 5.0 / 2.0 * ln(omz) * x * pow(z, -1) * CF
                + 5 * ln(omz) * x * CF
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                -1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 7.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 1.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
            )
            tmp += (
                -Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 7.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 1.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(x) * pow(z, -1) * CF
                + 2 * Li2(x) * CF
                - Li2(x) * x * pow(z, -1) * CF
                + 2 * Li2(x) * x * CF
            )

            res += tmp

        return res


def c2p_q2qp_eqp(x, z, rsl, order, f=C2Pq2qpEqp_DR0123_scheme):
    if rsl == "ll":
        f_DD = f(x, z, "D", "D", order)
        f_D0 = ln(1 - z) * f(x, z, "D", "0", order)
        f_D1 = 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "D", "1", order)
        f_D2 = 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "D", "2", order)
        f_00 = ln(1 - x) * ln(1 - z) * f(x, z, "0", "0", order)
        f_01 = ln(1 - x) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "0", "1", order)
        f_02 = ln(1 - x) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "0", "2", order)
        f_10 = 1 / 2 * pow(ln(1 - x), 2) * ln(1 - z) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - x), 2) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - x), 2) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "1", "2", order)
        f_20 = 1 / 3 * pow(ln(1 - x), 3) * ln(1 - z) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - x), 3) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - x), 3) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "2", "2", order)

        return f_DD + f_D0 + f_D1 + f_D2 + f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    elif rsl == "lr":
        f_DR = f(x, z, "D", "R", order)
        f_0R = ln(1 - x) * f(x, z, "0", "R", order)
        f_1R = 1 / 2 * pow(ln(1 - x), 2) * f(x, z, "1", "R", order)
        f_2R = 1 / 3 * pow(ln(1 - x), 3) * f(x, z, "2", "R", order)

        return f_DR + f_0R + f_1R + f_2R

    elif rsl == "rl":
        f_RD = f(x, z, "R", "D", order)
        f_R0 = ln(1 - z) * f(x, z, "R", "0", order)
        f_R1 = 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "R", "1", order)
        f_R2 = 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "R", "2", order)

        return f_RD + f_R0 + f_R1 + f_R2

    elif rsl == "rr":
        f_RR = f(x, z, "R", "R", order)

        return f_RR

    elif rsl == "rs":
        f_R0 = 1 / (1 - z) * f(x, z, "R", "0", order)
        f_R1 = ln(1 - z) / (1 - z) * f(x, z, "R", "1", order)
        f_R2 = pow(ln(1 - z), 2) / (1 - z) * f(x, z, "R", "2", order)

        return f_R0 + f_R1 + f_R2

    elif rsl == "sr":
        f_0R = 1 / (1 - x) * f(x, z, "0", "R", order)
        f_1R = ln(1 - x) / (1 - x) * f(x, z, "1", "R", order)
        f_2R = pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "R", order)

        return f_0R + f_1R + f_2R

    elif rsl == "ss":
        f_00 = 1 / ((1 - x) * (1 - z)) * f(x, z, "0", "0", order)
        f_01 = ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "0", "1", order)
        f_02 = pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "0", "2", order)
        f_10 = ln(1 - x) / ((1 - x) * (1 - z)) * f(x, z, "1", "0", order)
        f_11 = ln(1 - x) * ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "1", "1", order)
        f_12 = ln(1 - x) * pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "1", "2", order)
        f_20 = pow(ln(1 - x), 2) / ((1 - x) * (1 - z)) * f(x, z, "2", "0", order)
        f_21 = pow(ln(1 - x), 2) * ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "2", "1", order)
        f_22 = pow(ln(1 - x), 2) * pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "2", "2", order)

        return f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    elif rsl == "ls":
        f_D0 = 1 / (1 - z) * f(x, z, "D", "0", order)
        f_D1 = ln(1 - z) / (1 - z) * f(x, z, "D", "1", order)
        f_D2 = pow(ln(1 - z), 2) / (1 - z) * f(x, z, "D", "2", order)
        f_00 = ln(1 - x) / (1 - z) * f(x, z, "0", "0", order)
        f_01 = ln(1 - x) * ln(1 - z) / (1 - z) * f(x, z, "0", "1", order)
        f_02 = ln(1 - x) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "0", "2", order)
        f_10 = 1 / 2 * pow(ln(1 - x), 2) / (1 - z) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - x), 2) * ln(1 - z) / (1 - z) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - x), 2) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "1", "2", order)
        f_20 = 1 / 3 * pow(ln(1 - x), 3) / (1 - z) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - x), 3) * ln(1 - z) / (1 - z) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - x), 3) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "2", "2", order)

        return f_D0 + f_D1 + f_D2 + f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    elif rsl == "sl":
        f_0D = 1 / (1 - x) * f(x, z, "0", "D", order)
        f_1D = ln(1 - x) / (1 - x) * f(x, z, "1", "D", order)
        f_2D = pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "D", order)
        f_00 = ln(1 - z) / (1 - x) * f(x, z, "0", "0", order)
        f_01 = ln(1 - z) * ln(1 - x) / (1 - x) * f(x, z, "0", "1", order)
        f_02 = ln(1 - z) * pow(ln(1 - x), 2) / (1 - x) * f(x, z, "0", "2", order)
        f_10 = 1 / 2 * pow(ln(1 - z), 2) / (1 - x) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - z), 2) * ln(1 - x) / (1 - x) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - z), 2) * pow(ln(1 - x), 2) / (1 - x) * f(x, z, "1", "2", order)
        f_20 = 1 / 3 * pow(ln(1 - z), 3) / (1 - x) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - z), 3) * ln(1 - x) / (1 - x) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - z), 3) * pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "2", order)

        return f_0D + f_1D + f_2D + f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    else:
        raise ValueError("Incorrect rsl choice, rsl must have a value of: 'll', 'lr', 'rl', 'rr', 'rs', 'sr', 'ss', 'ls' or 'sl'")
