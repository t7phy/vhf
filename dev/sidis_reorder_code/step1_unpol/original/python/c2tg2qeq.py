from configs.eh import *


def C2Tg2qEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
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
            17.0 / 8.0 * pow(NC, -1)
            - 4 * pow(NC, -1) * zeta3
            - 1.0 / 8.0 * pow(NC, -1) * pow(pi, 2)
            - 81.0 / 16.0 * pow(NC, -1) * x
            + 8 * pow(NC, -1) * x * zeta3
            + 5.0 / 12.0 * pow(NC, -1) * x * pow(pi, 2)
            + 57.0 / 16.0 * pow(NC, -1) * pow(x, 2)
            - 8 * pow(NC, -1) * pow(x, 2) * zeta3
            - 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
            + 52.0 / 27.0 * NC * pow(x, -1)
            - 43.0 / 18.0 * NC
            + 9.0 / 4.0 * NC * zeta3
            - 1.0 / 3.0 * NC * pow(rln2, 3)
            + 7.0 / 24.0 * NC * pow(pi, 2)
            + 1.0 / 6.0 * NC * pow(pi, 2) * rln2
            + 1049.0 / 144.0 * NC * x
            - 13.0 / 2.0 * NC * x * zeta3
            - 2.0 / 3.0 * NC * x * pow(rln2, 3)
            - 1.0 / 4.0 * NC * x * pow(pi, 2)
            + 1.0 / 3.0 * NC * x * pow(pi, 2) * rln2
            - 3433.0 / 432.0 * NC * pow(x, 2)
            + 9.0 / 2.0 * NC * pow(x, 2) * zeta3
            - 2.0 / 3.0 * NC * pow(x, 2) * pow(rln2, 3)
            + 29.0 / 12.0 * NC * pow(x, 2) * pow(pi, 2)
            + 1.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2) * rln2
            + 11.0 / 6.0 * LMUR * NC * x
            - 11.0 / 6.0 * LMUR * NC * pow(x, 2)
            - 1.0 / 3.0 * LMUR * NF * x
            + 1.0 / 3.0 * LMUR * NF * pow(x, 2)
            - 3.0 / 8.0 * LMUF * pow(NC, -1)
            - 1.0 / 24.0 * LMUF * pow(NC, -1) * pow(pi, 2)
            - 5.0 / 8.0 * LMUF * pow(NC, -1) * x
            + 1.0 / 12.0 * LMUF * pow(NC, -1) * x * pow(pi, 2)
            - 3.0 / 8.0 * LMUF * pow(NC, -1) * pow(x, 2)
            - 1.0 / 6.0 * LMUF * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
            - 13.0 / 9.0 * LMUF * NC * pow(x, -1)
            + 59.0 / 24.0 * LMUF * NC
            + 1.0 / 24.0 * LMUF * NC * pow(pi, 2)
            - 181.0 / 24.0 * LMUF * NC * x
            - 3.0 / 4.0 * LMUF * NC * x * pow(pi, 2)
            + 533.0 / 72.0 * LMUF * NC * pow(x, 2)
            + 1.0 / 2.0 * LMUF * NC * pow(x, 2) * pow(pi, 2)
            + 1.0 / 3.0 * LMUF * NF * x
            - 1.0 / 3.0 * LMUF * NF * pow(x, 2)
            - 11.0 / 12.0 * LMUF * LMUR * NC
            + 11.0 / 6.0 * LMUF * LMUR * NC * x
            - 11.0 / 6.0 * LMUF * LMUR * NC * pow(x, 2)
            + 1.0 / 6.0 * LMUF * LMUR * NF
            - 1.0 / 3.0 * LMUF * LMUR * NF * x
            + 1.0 / 3.0 * LMUF * LMUR * NF * pow(x, 2)
            + 1.0 / 16.0 * pow(LMUF, 2) * pow(NC, -1)
            - 1.0 / 4.0 * pow(LMUF, 2) * pow(NC, -1) * x
            + 1.0 / 3.0 * pow(LMUF, 2) * NC * pow(x, -1)
        )
        res += (
            +53.0 / 48.0 * pow(LMUF, 2) * NC
            + 5.0 / 12.0 * pow(LMUF, 2) * NC * x
            - 3.0 / 4.0 * pow(LMUF, 2) * NC * pow(x, 2)
            - 1.0 / 6.0 * pow(LMUF, 2) * NF
            + 1.0 / 3.0 * pow(LMUF, 2) * NF * x
            - 1.0 / 3.0 * pow(LMUF, 2) * NF * pow(x, 2)
            - 1.0 / 12.0 * LMUA * pow(NC, -1) * pow(pi, 2)
            + 3.0 / 4.0 * LMUA * pow(NC, -1) * x
            + 1.0 / 6.0 * LMUA * pow(NC, -1) * x * pow(pi, 2)
            - 3.0 / 4.0 * LMUA * pow(NC, -1) * pow(x, 2)
            - 1.0 / 6.0 * LMUA * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
            + 1.0 / 12.0 * LMUA * NC * pow(pi, 2)
            - 3.0 / 4.0 * LMUA * NC * x
            - 1.0 / 6.0 * LMUA * NC * x * pow(pi, 2)
            + 3.0 / 4.0 * LMUA * NC * pow(x, 2)
            + 1.0 / 6.0 * LMUA * NC * pow(x, 2) * pow(pi, 2)
            - 3.0 / 8.0 * LMUA * LMUF * pow(NC, -1)
            + 3.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * x
            - 3.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * pow(x, 2)
            + 3.0 / 8.0 * LMUA * LMUF * NC
            - 3.0 / 4.0 * LMUA * LMUF * NC * x
            + 3.0 / 4.0 * LMUA * LMUF * NC * pow(x, 2)
            + 1.0 / 2.0 * ln(1 + x) * NC * pow(rln2, 2)
            + 1.0 / 12.0 * ln(1 + x) * NC * pow(pi, 2)
            + ln(1 + x) * NC * x * pow(rln2, 2)
            + 1.0 / 6.0 * ln(1 + x) * NC * x * pow(pi, 2)
            + ln(1 + x) * NC * pow(x, 2) * pow(rln2, 2)
            + 1.0 / 6.0 * ln(1 + x) * NC * pow(x, 2) * pow(pi, 2)
            - 1.0 / 6.0 * pow(ln(1 + x), 3) * NC
            - 1.0 / 3.0 * pow(ln(1 + x), 3) * NC * x
            - 1.0 / 3.0 * pow(ln(1 + x), 3) * NC * pow(x, 2)
            - 3.0 / 4.0 * ln(x) * pow(NC, -1)
            - 1.0 / 4.0 * ln(x) * pow(NC, -1) * pow(pi, 2)
            - 37.0 / 16.0 * ln(x) * pow(NC, -1) * x
            + 1.0 / 2.0 * ln(x) * pow(NC, -1) * x * pow(pi, 2)
            + 7.0 / 8.0 * ln(x) * pow(NC, -1) * pow(x, 2)
            - 2.0 / 3.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
            + 29.0 / 6.0 * ln(x) * NC
            + 1.0 / 12.0 * ln(x) * NC * pow(pi, 2)
            + 143.0 / 48.0 * ln(x) * NC * x
            - 3.0 / 2.0 * ln(x) * NC * x * pow(pi, 2)
            + 583.0 / 72.0 * ln(x) * NC * pow(x, 2)
            + ln(x) * NC * pow(x, 2) * pow(pi, 2)
            - 11.0 / 12.0 * ln(x) * LMUR * NC
            + 11.0 / 6.0 * ln(x) * LMUR * NC * x
            - 11.0 / 6.0 * ln(x) * LMUR * NC * pow(x, 2)
        )
        res += (
            +1.0 / 6.0 * ln(x) * LMUR * NF
            - 1.0 / 3.0 * ln(x) * LMUR * NF * x
            + 1.0 / 3.0 * ln(x) * LMUR * NF * pow(x, 2)
            + 3.0 / 8.0 * ln(x) * LMUF * pow(NC, -1)
            - 9.0 / 4.0 * ln(x) * LMUF * pow(NC, -1) * x
            + 7.0 / 4.0 * ln(x) * LMUF * pow(NC, -1) * pow(x, 2)
            - 11.0 / 24.0 * ln(x) * LMUF * NC
            + 5.0 / 12.0 * ln(x) * LMUF * NC * x
            - 149.0 / 12.0 * ln(x) * LMUF * NC * pow(x, 2)
            - 1.0 / 6.0 * ln(x) * LMUF * NF
            + 1.0 / 3.0 * ln(x) * LMUF * NF * x
            - 1.0 / 3.0 * ln(x) * LMUF * NF * pow(x, 2)
            + 1.0 / 8.0 * ln(x) * pow(LMUF, 2) * pow(NC, -1)
            - 1.0 / 4.0 * ln(x) * pow(LMUF, 2) * pow(NC, -1) * x
            + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * pow(NC, -1) * pow(x, 2)
            + 3.0 / 8.0 * ln(x) * pow(LMUF, 2) * NC
            + 9.0 / 4.0 * ln(x) * pow(LMUF, 2) * NC * x
            - 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * NC * pow(x, 2)
            - 3.0 / 8.0 * ln(x) * LMUA * pow(NC, -1)
            + 3.0 / 4.0 * ln(x) * LMUA * pow(NC, -1) * x
            - 3.0 / 4.0 * ln(x) * LMUA * pow(NC, -1) * pow(x, 2)
            + 3.0 / 8.0 * ln(x) * LMUA * NC
            - 3.0 / 4.0 * ln(x) * LMUA * NC * x
            + 3.0 / 4.0 * ln(x) * LMUA * NC * pow(x, 2)
            + ln(x) * ln(1 + x) * NC * x
            + ln(x) * ln(1 + x) * NC * pow(x, 2)
            + ln(x) * ln(1 + x) * LMUF * NC
            + 2 * ln(x) * ln(1 + x) * LMUF * NC * x
            + 2 * ln(x) * ln(1 + x) * LMUF * NC * pow(x, 2)
            + 7.0 / 32.0 * pow(ln(x), 2) * pow(NC, -1)
            - 15.0 / 8.0 * pow(ln(x), 2) * pow(NC, -1) * x
            + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
            - 59.0 / 32.0 * pow(ln(x), 2) * NC
            + 19.0 / 8.0 * pow(ln(x), 2) * NC * x
            - 137.0 / 12.0 * pow(ln(x), 2) * NC * pow(x, 2)
            + 1.0 / 4.0 * pow(ln(x), 2) * LMUF * pow(NC, -1)
            - 1.0 / 2.0 * pow(ln(x), 2) * LMUF * pow(NC, -1) * x
            + pow(ln(x), 2) * LMUF * pow(NC, -1) * pow(x, 2)
            + 3.0 / 4.0 * pow(ln(x), 2) * LMUF * NC
            + 7.0 / 2.0 * pow(ln(x), 2) * LMUF * NC * x
            - pow(ln(x), 2) * LMUF * NC * pow(x, 2)
            + pow(ln(x), 2) * ln(1 + x) * NC
            + 2 * pow(ln(x), 2) * ln(1 + x) * NC * x
            + 2 * pow(ln(x), 2) * ln(1 + x) * NC * pow(x, 2)
        )
        res += (
            +1.0 / 48.0 * pow(ln(x), 3) * pow(NC, -1)
            - 1.0 / 24.0 * pow(ln(x), 3) * pow(NC, -1) * x
            + 1.0 / 4.0 * pow(ln(x), 3) * pow(NC, -1) * pow(x, 2)
            + 19.0 / 48.0 * pow(ln(x), 3) * NC
            + 29.0 / 24.0 * pow(ln(x), 3) * NC * x
            - 1.0 / 4.0 * pow(ln(x), 3) * NC * pow(x, 2)
            - 3.0 / 8.0 * pow(ln(x), 2) * ln(omx) * pow(NC, -1)
            + 3.0 / 4.0 * pow(ln(x), 2) * ln(omx) * pow(NC, -1) * x
            - 3.0 / 4.0 * pow(ln(x), 2) * ln(omx) * pow(NC, -1) * pow(x, 2)
            + 11.0 / 8.0 * pow(ln(x), 2) * ln(omx) * NC
            - 11.0 / 4.0 * pow(ln(x), 2) * ln(omx) * NC * x
            + 11.0 / 4.0 * pow(ln(x), 2) * ln(omx) * NC * pow(x, 2)
            - 7.0 / 8.0 * ln(x) * ln(omx) * pow(NC, -1)
            + 7.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * x
            - 3 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
            - 2.0 / 3.0 * ln(x) * ln(omx) * NC * pow(x, -1)
            + 3.0 / 8.0 * ln(x) * ln(omx) * NC
            - 15.0 / 2.0 * ln(x) * ln(omx) * NC * x
            + 49.0 / 6.0 * ln(x) * ln(omx) * NC * pow(x, 2)
            - ln(x) * ln(omx) * LMUF * pow(NC, -1)
            + 2 * ln(x) * ln(omx) * LMUF * pow(NC, -1) * x
            - 2 * ln(x) * ln(omx) * LMUF * pow(NC, -1) * pow(x, 2)
            + 2 * ln(x) * ln(omx) * LMUF * NC
            - 4 * ln(x) * ln(omx) * LMUF * NC * x
            + 4 * ln(x) * ln(omx) * LMUF * NC * pow(x, 2)
            - ln(x) * ln(omx) * ln(1 + x) * NC
            - 2 * ln(x) * ln(omx) * ln(1 + x) * NC * x
            - 2 * ln(x) * ln(omx) * ln(1 + x) * NC * pow(x, 2)
            + ln(x) * pow(ln(omx), 2) * pow(NC, -1)
            - 2 * ln(x) * pow(ln(omx), 2) * pow(NC, -1) * x
            + 7.0 / 4.0 * ln(x) * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
            - 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * NC
            - 7.0 / 4.0 * ln(x) * pow(ln(omx), 2) * NC * pow(x, 2)
            + ln(x) * Li2(-x) * NC
            + 2 * ln(x) * Li2(-x) * NC * x
            + 2 * ln(x) * Li2(-x) * NC * pow(x, 2)
            - 1.0 / 2.0 * ln(x) * Li2(x) * pow(NC, -1)
            + ln(x) * Li2(x) * pow(NC, -1) * x
            - 1.0 / 2.0 * ln(x) * Li2(x) * pow(NC, -1) * pow(x, 2)
            + 5.0 / 2.0 * ln(x) * Li2(x) * NC
            + ln(x) * Li2(x) * NC * x
        )
        res += (
            +5.0 / 2.0 * ln(x) * Li2(x) * NC * pow(x, 2)
            + 3.0 / 8.0 * ln(omx) * pow(NC, -1)
            + 1.0 / 12.0 * ln(omx) * pow(NC, -1) * pow(pi, 2)
            + 7.0 / 4.0 * ln(omx) * pow(NC, -1) * x
            - 1.0 / 6.0 * ln(omx) * pow(NC, -1) * x * pow(pi, 2)
            - 7.0 / 8.0 * ln(omx) * pow(NC, -1) * pow(x, 2)
            + 1.0 / 4.0 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
            + 13.0 / 9.0 * ln(omx) * NC * pow(x, -1)
            - 59.0 / 24.0 * ln(omx) * NC
            + 1.0 / 2.0 * ln(omx) * NC * pow(rln2, 2)
            - 1.0 / 6.0 * ln(omx) * NC * pow(pi, 2)
            + 16.0 / 3.0 * ln(omx) * NC * x
            + ln(omx) * NC * x * pow(rln2, 2)
            + ln(omx) * NC * x * pow(pi, 2)
            - 383.0 / 72.0 * ln(omx) * NC * pow(x, 2)
            + ln(omx) * NC * pow(x, 2) * pow(rln2, 2)
            - 3.0 / 4.0 * ln(omx) * NC * pow(x, 2) * pow(pi, 2)
            + 11.0 / 12.0 * ln(omx) * LMUR * NC
            - 11.0 / 6.0 * ln(omx) * LMUR * NC * x
            + 11.0 / 6.0 * ln(omx) * LMUR * NC * pow(x, 2)
            - 1.0 / 6.0 * ln(omx) * LMUR * NF
            + 1.0 / 3.0 * ln(omx) * LMUR * NF * x
            - 1.0 / 3.0 * ln(omx) * LMUR * NF * pow(x, 2)
            - 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1)
            + 9.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1) * x
            - 7.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1) * pow(x, 2)
            - 2.0 / 3.0 * ln(omx) * LMUF * NC * pow(x, -1)
            - 11.0 / 12.0 * ln(omx) * LMUF * NC
            - 53.0 / 12.0 * ln(omx) * LMUF * NC * x
            + 61.0 / 12.0 * ln(omx) * LMUF * NC * pow(x, 2)
            + 1.0 / 6.0 * ln(omx) * LMUF * NF
            - 1.0 / 3.0 * ln(omx) * LMUF * NF * x
            + 1.0 / 3.0 * ln(omx) * LMUF * NF * pow(x, 2)
            - 1.0 / 4.0 * ln(omx) * pow(LMUF, 2) * pow(NC, -1)
            + 1.0 / 2.0 * ln(omx) * pow(LMUF, 2) * pow(NC, -1) * x
            - 1.0 / 2.0 * ln(omx) * pow(LMUF, 2) * pow(NC, -1) * pow(x, 2)
            + 3.0 / 4.0 * ln(omx) * pow(LMUF, 2) * NC
            - 3.0 / 2.0 * ln(omx) * pow(LMUF, 2) * NC * x
            + 3.0 / 2.0 * ln(omx) * pow(LMUF, 2) * NC * pow(x, 2)
            + 3.0 / 8.0 * ln(omx) * LMUA * pow(NC, -1)
            - 3.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1) * x
            + 3.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1) * pow(x, 2)
            - 3.0 / 8.0 * ln(omx) * LMUA * NC
            + 3.0 / 4.0 * ln(omx) * LMUA * NC * x
        )
        res += (
            -3.0 / 4.0 * ln(omx) * LMUA * NC * pow(x, 2)
            - ln(omx) * ln(1 + x) * NC * rln2
            - 2 * ln(omx) * ln(1 + x) * NC * x * rln2
            - 2 * ln(omx) * ln(1 + x) * NC * pow(x, 2) * rln2
            + 1.0 / 2.0 * ln(omx) * pow(ln(1 + x), 2) * NC
            + ln(omx) * pow(ln(1 + x), 2) * NC * x
            + ln(omx) * pow(ln(1 + x), 2) * NC * pow(x, 2)
            + 7.0 / 16.0 * pow(ln(omx), 2) * pow(NC, -1)
            - 7.0 / 4.0 * pow(ln(omx), 2) * pow(NC, -1) * x
            + 3.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
            + 1.0 / 3.0 * pow(ln(omx), 2) * NC * pow(x, -1)
            - 3.0 / 16.0 * pow(ln(omx), 2) * NC
            + 13.0 / 4.0 * pow(ln(omx), 2) * NC * x
            - 43.0 / 12.0 * pow(ln(omx), 2) * NC * pow(x, 2)
            + 1.0 / 2.0 * pow(ln(omx), 2) * LMUF * pow(NC, -1)
            - pow(ln(omx), 2) * LMUF * pow(NC, -1) * x
            + pow(ln(omx), 2) * LMUF * pow(NC, -1) * pow(x, 2)
            - pow(ln(omx), 2) * LMUF * NC
            + 2 * pow(ln(omx), 2) * LMUF * NC * x
            - 2 * pow(ln(omx), 2) * LMUF * NC * pow(x, 2)
            - 5.0 / 24.0 * pow(ln(omx), 3) * pow(NC, -1)
            + 5.0 / 12.0 * pow(ln(omx), 3) * pow(NC, -1) * x
            - 5.0 / 12.0 * pow(ln(omx), 3) * pow(NC, -1) * pow(x, 2)
            + 7.0 / 24.0 * pow(ln(omx), 3) * NC
            - 7.0 / 12.0 * pow(ln(omx), 3) * NC * x
            + 7.0 / 12.0 * pow(ln(omx), 3) * NC * pow(x, 2)
            - ln(omx) * Li2(-x) * NC
            - 2 * ln(omx) * Li2(-x) * NC * x
            - 2 * ln(omx) * Li2(-x) * NC * pow(x, 2)
            + 1.0 / 2.0 * ln(omx) * Li2(x) * pow(NC, -1)
            - ln(omx) * Li2(x) * pow(NC, -1) * x
            + 1.0 / 2.0 * ln(omx) * Li2(x) * pow(NC, -1) * pow(x, 2)
            - ln(omx) * Li2(x) * NC
            - 4 * ln(omx) * Li2(x) * NC * x
            + 1.0 / 2.0 * ln(omx) * Li2(x) * NC * pow(x, 2)
            - 1.0 / 4.0 * ln(opx) * NC * pow(pi, 2)
            - 1.0 / 2.0 * ln(opx) * NC * x * pow(pi, 2)
            - 1.0 / 2.0 * ln(opx) * NC * pow(x, 2) * pow(pi, 2)
            + Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * NC
            + 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * NC * x
            + 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * NC * pow(x, 2)
            + Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * NC
        )
        res += (
            +2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * NC * x
            + 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * NC * pow(x, 2)
            + 3.0 / 2.0 * Li3(1 - x) * pow(NC, -1)
            - 3 * Li3(1 - x) * pow(NC, -1) * x
            + 5.0 / 2.0 * Li3(1 - x) * pow(NC, -1) * pow(x, 2)
            - 3.0 / 2.0 * Li3(1 - x) * NC
            - 7 * Li3(1 - x) * NC * x
            - 1.0 / 2.0 * Li3(1 - x) * NC * pow(x, 2)
            + Li3(1 / (1 + x) - 1 / (1 + x) * x) * NC
            + 2 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * NC * x
            + 2 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * NC * pow(x, 2)
            + 5.0 / 4.0 * Li3(x) * pow(NC, -1)
            - 5.0 / 2.0 * Li3(x) * pow(NC, -1) * x
            + 5.0 / 2.0 * Li3(x) * pow(NC, -1) * pow(x, 2)
            - 9.0 / 4.0 * Li3(x) * NC
            + 5.0 / 2.0 * Li3(x) * NC * x
            - 9.0 / 2.0 * Li3(x) * NC * pow(x, 2)
            + Li2(-x) * NC * x
            + Li2(-x) * NC * pow(x, 2)
            + Li2(-x) * LMUF * NC
            + 2 * Li2(-x) * LMUF * NC * x
            + 2 * Li2(-x) * LMUF * NC * pow(x, 2)
            - 1.0 / 8.0 * Li2(x) * pow(NC, -1)
            - 2.0 / 3.0 * Li2(x) * NC * pow(x, -1)
            - 11.0 / 8.0 * Li2(x) * NC
            - 4 * Li2(x) * NC * x
            - 22.0 / 3.0 * Li2(x) * NC * pow(x, 2)
            - 1.0 / 4.0 * Li2(x) * LMUF * pow(NC, -1)
            + 1.0 / 2.0 * Li2(x) * LMUF * pow(NC, -1) * x
            + 5.0 / 4.0 * Li2(x) * LMUF * NC
            + 7.0 / 2.0 * Li2(x) * LMUF * NC * x
        )

        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            3.0 / 8.0 * pow(NC, -1)
            + 1.0 / 8.0 * pow(NC, -1) * pow(pi, 2)
            + 11.0 / 8.0 * pow(NC, -1) * x
            - 1.0 / 4.0 * pow(NC, -1) * x * pow(pi, 2)
            - 3.0 / 8.0 * pow(NC, -1) * pow(x, 2)
            + 1.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
            + 13.0 / 9.0 * NC * pow(x, -1)
            - 59.0 / 24.0 * NC
            - 1.0 / 8.0 * NC * pow(pi, 2)
            + 119.0 / 24.0 * NC * x
            + 11.0 / 12.0 * NC * x * pow(pi, 2)
            - 347.0 / 72.0 * NC * pow(x, 2)
            - 2.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
            + 11.0 / 12.0 * LMUR * NC
            - 11.0 / 6.0 * LMUR * NC * x
            + 11.0 / 6.0 * LMUR * NC * pow(x, 2)
            - 1.0 / 6.0 * LMUR * NF
            + 1.0 / 3.0 * LMUR * NF * x
            - 1.0 / 3.0 * LMUR * NF * pow(x, 2)
            - 1.0 / 2.0 * LMUF * pow(NC, -1)
            + 5.0 / 4.0 * LMUF * pow(NC, -1) * x
            - 3.0 / 4.0 * LMUF * pow(NC, -1) * pow(x, 2)
            - 2.0 / 3.0 * LMUF * NC * pow(x, -1)
            - 11.0 / 12.0 * LMUF * NC
            - 41.0 / 12.0 * LMUF * NC * x
            + 49.0 / 12.0 * LMUF * NC * pow(x, 2)
            + 1.0 / 6.0 * LMUF * NF
            - 1.0 / 3.0 * LMUF * NF * x
            + 1.0 / 3.0 * LMUF * NF * pow(x, 2)
            + 3.0 / 8.0 * LMUA * pow(NC, -1)
            + 1.0 / 4.0 * LMUA * pow(NC, -1) * x
            - 1.0 / 4.0 * LMUA * pow(NC, -1) * pow(x, 2)
            - 3.0 / 8.0 * LMUA * NC
            - 1.0 / 4.0 * LMUA * NC * x
            + 1.0 / 4.0 * LMUA * NC * pow(x, 2)
            - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1)
            + LMUA * LMUF * pow(NC, -1) * x
            - LMUA * LMUF * pow(NC, -1) * pow(x, 2)
            + 1.0 / 2.0 * LMUA * LMUF * NC
            - LMUA * LMUF * NC * x
            + LMUA * LMUF * NC * pow(x, 2)
            - 3.0 / 4.0 * ln(x) * pow(NC, -1)
            + 3 * ln(x) * pow(NC, -1) * x
            - 5.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2)
            + 7.0 / 4.0 * ln(x) * NC
            - 3 * ln(x) * NC * x
            + 15 * ln(x) * NC * pow(x, 2)
            - 1.0 / 4.0 * ln(x) * LMUF * pow(NC, -1)
            + 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x
            - ln(x) * LMUF * pow(NC, -1) * pow(x, 2)
            - 3.0 / 4.0 * ln(x) * LMUF * NC
            - 9.0 / 2.0 * ln(x) * LMUF * NC * x
            + ln(x) * LMUF * NC * pow(x, 2)
            - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1)
            + ln(x) * LMUA * pow(NC, -1) * x
            - ln(x) * LMUA * pow(NC, -1) * pow(x, 2)
            + 1.0 / 2.0 * ln(x) * LMUA * NC
        )
        res += (
            -ln(x) * LMUA * NC * x
            + ln(x) * LMUA * NC * pow(x, 2)
            - ln(x) * ln(1 + x) * NC
            - 2 * ln(x) * ln(1 + x) * NC * x
            - 2 * ln(x) * ln(1 + x) * NC * pow(x, 2)
            - 1.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
            + 1.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x
            - pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
            - 3.0 / 4.0 * pow(ln(x), 2) * NC
            - 7.0 / 2.0 * pow(ln(x), 2) * NC * x
            + pow(ln(x), 2) * NC * pow(x, 2)
            + ln(x) * ln(omx) * pow(NC, -1)
            - 2 * ln(x) * ln(omx) * pow(NC, -1) * x
            + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
            - 2 * ln(x) * ln(omx) * NC
            + 4 * ln(x) * ln(omx) * NC * x
            - 4 * ln(x) * ln(omx) * NC * pow(x, 2)
            + 7.0 / 8.0 * ln(omx) * pow(NC, -1)
            - 3 * ln(omx) * pow(NC, -1) * x
            + 5.0 / 2.0 * ln(omx) * pow(NC, -1) * pow(x, 2)
            + 2.0 / 3.0 * ln(omx) * NC * pow(x, -1)
            - 3.0 / 8.0 * ln(omx) * NC
            + 7 * ln(omx) * NC * x
            - 23.0 / 3.0 * ln(omx) * NC * pow(x, 2)
            + 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1)
            - ln(omx) * LMUF * pow(NC, -1) * x
            + ln(omx) * LMUF * pow(NC, -1) * pow(x, 2)
            - 3.0 / 2.0 * ln(omx) * LMUF * NC
            + 3 * ln(omx) * LMUF * NC * x
            - 3 * ln(omx) * LMUF * NC * pow(x, 2)
            + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1)
            - ln(omx) * LMUA * pow(NC, -1) * x
            + ln(omx) * LMUA * pow(NC, -1) * pow(x, 2)
            - 1.0 / 2.0 * ln(omx) * LMUA * NC
            + ln(omx) * LMUA * NC * x
            - ln(omx) * LMUA * NC * pow(x, 2)
            - 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1)
            + pow(ln(omx), 2) * pow(NC, -1) * x
            - pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
            + pow(ln(omx), 2) * NC
            - 2 * pow(ln(omx), 2) * NC * x
            + 2 * pow(ln(omx), 2) * NC * pow(x, 2)
            - Li2(-x) * NC
            - 2 * Li2(-x) * NC * x
            - 2 * Li2(-x) * NC * pow(x, 2)
            + 1.0 / 4.0 * Li2(x) * pow(NC, -1)
            - 1.0 / 2.0 * Li2(x) * pow(NC, -1) * x
            - 5.0 / 4.0 * Li2(x) * NC
            - 7.0 / 2.0 * Li2(x) * NC * x
        )

        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            7.0 / 8.0 * pow(NC, -1)
            - 3 * pow(NC, -1) * x
            + 5.0 / 2.0 * pow(NC, -1) * pow(x, 2)
            + 2.0 / 3.0 * NC * pow(x, -1)
            - 3.0 / 8.0 * NC
            + 7 * NC * x
            - 23.0 / 3.0 * NC * pow(x, 2)
            + 1.0 / 2.0 * LMUF * pow(NC, -1)
            - LMUF * pow(NC, -1) * x
            + LMUF * pow(NC, -1) * pow(x, 2)
            - 1.0 / 2.0 * LMUF * NC
            + LMUF * NC * x
            - LMUF * NC * pow(x, 2)
            + LMUA * pow(NC, -1)
            - 2 * LMUA * pow(NC, -1) * x
            + 2 * LMUA * pow(NC, -1) * pow(x, 2)
            - LMUA * NC
            + 2 * LMUA * NC * x
            - 2 * LMUA * NC * pow(x, 2)
            + 3.0 / 4.0 * ln(x) * pow(NC, -1)
            - 3.0 / 2.0 * ln(x) * pow(NC, -1) * x
            + 2 * ln(x) * pow(NC, -1) * pow(x, 2)
            + 1.0 / 4.0 * ln(x) * NC
            + 11.0 / 2.0 * ln(x) * NC * x
            - 2 * ln(x) * NC * pow(x, 2)
            - ln(omx) * pow(NC, -1)
            + 2 * ln(omx) * pow(NC, -1) * x
            - 2 * ln(omx) * pow(NC, -1) * pow(x, 2)
            + 2 * ln(omx) * NC
            - 4 * ln(omx) * NC * x
            + 4 * ln(omx) * NC * pow(x, 2)
        )

        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = -3.0 / 4.0 * pow(NC, -1) + 3.0 / 2.0 * pow(NC, -1) * x - 3.0 / 2.0 * pow(NC, -1) * pow(x, 2) + 3.0 / 4.0 * NC - 3.0 / 2.0 * NC * x + 3.0 / 2.0 * NC * pow(x, 2)

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
                3.0 / 2.0 * pow(NC, -1) * pow(z, -1)
                - 11.0 / 12.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2)
                + 3.0 / 2.0 * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 12.0 * pow(NC, -1) * pow(pi, 2)
                + 11.0 / 6.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2)
                + 5.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                + 1.0 / 12.0 * NC * pow(z, -1) * pow(pi, 2)
                - 2 * NC
                + 1.0 / 12.0 * NC * pow(pi, 2) * pow(omz, -1)
                - 1.0 / 6.0 * NC * pow(pi, 2)
                - 1.0 / 6.0 * NC * x * pow(z, -1) * pow(pi, 2)
                - 2 * NC * x
                - 1.0 / 6.0 * NC * x * pow(pi, 2) * pow(omz, -1)
                + 1.0 / 3.0 * NC * x * pow(pi, 2)
                + 1.0 / 6.0 * NC * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                + 2 * NC * pow(x, 2)
                + 1.0 / 6.0 * NC * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                - 1.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(z, -1)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(x) * pow(NC, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(z, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * NC
                - 6 * ln(x) * NC * x
                + 6 * ln(x) * NC * pow(x, 2)
                + 5 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1)
                + 19.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                - 13.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
                - 10 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x
                + 13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(z, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                + 3 * pow(ln(x), 2) * NC
                + 3 * pow(ln(x), 2) * NC * x * pow(z, -1)
                + 3 * pow(ln(x), 2) * NC * x * pow(omz, -1)
                - 6 * pow(ln(x), 2) * NC * x
                - 3 * pow(ln(x), 2) * NC * pow(x, 2) * pow(z, -1)
                - 3 * pow(ln(x), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 6 * pow(ln(x), 2) * NC * pow(x, 2)
                - 11.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1)
                - 13.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * ln(z) * pow(NC, -1)
                + 11 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1)
                + 13 * ln(x) * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                - 8 * ln(x) * ln(z) * pow(NC, -1) * x
                - 8 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 8 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 5.0 / 2.0 * ln(x) * ln(z) * NC * pow(z, -1)
                + 5.0 / 2.0 * ln(x) * ln(z) * NC * pow(omz, -1)
                - 5 * ln(x) * ln(z) * NC
                - 5 * ln(x) * ln(z) * NC * x * pow(z, -1)
                - 5 * ln(x) * ln(z) * NC * x * pow(omz, -1)
                + 10 * ln(x) * ln(z) * NC * x
                + 5 * ln(x) * ln(z) * NC * pow(x, 2) * pow(z, -1)
                + 5 * ln(x) * ln(z) * NC * pow(x, 2) * pow(omz, -1)
                - 10 * ln(x) * ln(z) * NC * pow(x, 2)
                - 17.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1)
                - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 11.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1)
                + 17 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + 16 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                - 11 * ln(x) * ln(omx) * pow(NC, -1) * x
                - 11 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 11 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 11 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
            )
            tmp += (
                +2 * ln(x) * ln(omx) * NC * pow(z, -1)
                + 2 * ln(x) * ln(omx) * NC * pow(omz, -1)
                - 4 * ln(x) * ln(omx) * NC
                - 4 * ln(x) * ln(omx) * NC * x * pow(z, -1)
                - 4 * ln(x) * ln(omx) * NC * x * pow(omz, -1)
                + 8 * ln(x) * ln(omx) * NC * x
                + 4 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                + 4 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 8 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1)
                - 7 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 5 * ln(x) * ln(omz) * pow(NC, -1)
                + 16 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 14 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * pow(NC, -1) * x
                - 10 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 10 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 10 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 5.0 / 2.0 * ln(x) * ln(omz) * NC * pow(z, -1)
                + 5.0 / 2.0 * ln(x) * ln(omz) * NC * pow(omz, -1)
                - 5 * ln(x) * ln(omz) * NC
                - 5 * ln(x) * ln(omz) * NC * x * pow(z, -1)
                - 5 * ln(x) * ln(omz) * NC * x * pow(omz, -1)
                + 10 * ln(x) * ln(omz) * NC * x
                + 5 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 5 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * pow(NC, -1) * pow(z, -1)
                + ln(x) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * pow(NC, -1)
                - ln(x) * ln(xmz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(xmz) * pow(NC, -1) * x
                + ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * NC * pow(omz, -1)
            )
            tmp += (
                +ln(x) * ln(xmz) * NC
                + ln(x) * ln(xmz) * NC * x * pow(z, -1)
                + ln(x) * ln(xmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(xmz) * NC * x
                - ln(x) * ln(xmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(xmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * NC * pow(x, 2)
                + ln(x) * ln(omxmz) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1)
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(omxmz) * pow(NC, -1) * x
                + ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * NC * pow(omz, -1)
                + ln(x) * ln(omxmz) * NC
                + ln(x) * ln(omxmz) * NC * x * pow(z, -1)
                + ln(x) * ln(omxmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * NC * x
                - ln(x) * ln(omxmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(omxmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * NC * pow(x, 2)
                + ln(z) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * pow(NC, -1)
                + ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(z) * NC * pow(z, -1)
                - ln(z) * NC * pow(omz, -1)
                + 3 * ln(z) * NC
                + 4 * ln(z) * NC * x
                - 4 * ln(z) * NC * pow(x, 2)
                + 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1)
                + 9.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1)
                - 3 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1)
                - 9.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x
            )
            tmp += (
                +5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - pow(ln(z), 2) * NC * pow(z, -1)
                - pow(ln(z), 2) * NC * pow(omz, -1)
                + 2 * pow(ln(z), 2) * NC
                + 2 * pow(ln(z), 2) * NC * x * pow(z, -1)
                + 2 * pow(ln(z), 2) * NC * x * pow(omz, -1)
                - 4 * pow(ln(z), 2) * NC * x
                - 2 * pow(ln(z), 2) * NC * pow(x, 2) * pow(z, -1)
                - 2 * pow(ln(z), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * pow(ln(z), 2) * NC * pow(x, 2)
                + 4 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1)
                + 5 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(z) * ln(omx) * pow(NC, -1)
                - 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 10 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * x
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - ln(z) * ln(omx) * NC * pow(z, -1)
                - ln(z) * ln(omx) * NC * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * NC
                + 2 * ln(z) * ln(omx) * NC * x * pow(z, -1)
                + 2 * ln(z) * ln(omx) * NC * x * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * NC * x
                - 2 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                - 2 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 3 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 3 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(omz) * pow(NC, -1)
                - 6 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 6 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * x
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                -4 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 2 * ln(z) * ln(omz) * NC * pow(z, -1)
                - 2 * ln(z) * ln(omz) * NC * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * NC
                + 4 * ln(z) * ln(omz) * NC * x * pow(z, -1)
                + 4 * ln(z) * ln(omz) * NC * x * pow(omz, -1)
                - 8 * ln(z) * ln(omz) * NC * x
                - 4 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 4 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * pow(NC, -1) * pow(z, -1)
                - ln(z) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * pow(NC, -1)
                + ln(z) * ln(xmz) * pow(NC, -1) * x * pow(z, -1)
                + 2 * ln(z) * ln(xmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(z) * ln(xmz) * pow(NC, -1) * x
                - ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * NC * pow(omz, -1)
                - ln(z) * ln(xmz) * NC
                - ln(z) * ln(xmz) * NC * x * pow(z, -1)
                - ln(z) * ln(xmz) * NC * x * pow(omz, -1)
                + 2 * ln(z) * ln(xmz) * NC * x
                + ln(z) * ln(xmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(z) * ln(xmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * NC * pow(x, 2)
                + ln(omx) * pow(NC, -1) * pow(z, -1)
                + ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omx) * pow(NC, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(omx) * NC
                + 2 * ln(omx) * NC * x
                - 2 * ln(omx) * NC * pow(x, 2)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(ln(omx), 2) * pow(NC, -1)
                - 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1)
            )
            tmp += (
                -6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(z, -1)
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(z, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(omz, -1)
                - pow(ln(omx), 2) * NC * x
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(z, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(omz, -1)
                + pow(ln(omx), 2) * NC * pow(x, 2)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 9.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1)
                - 12 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 9 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 7 * ln(omx) * ln(omz) * pow(NC, -1) * x
                + 7 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 7 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 3.0 / 2.0 * ln(omx) * ln(omz) * NC * pow(z, -1)
                - 3.0 / 2.0 * ln(omx) * ln(omz) * NC * pow(omz, -1)
                + 3 * ln(omx) * ln(omz) * NC
                + 3 * ln(omx) * ln(omz) * NC * x * pow(z, -1)
                + 3 * ln(omx) * ln(omz) * NC * x * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * NC * x
                - 3 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 3 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(z, -1)
                + ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(omz) * pow(NC, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(omz) * NC * pow(z, -1)
                - ln(omz) * NC * pow(omz, -1)
                + 3 * ln(omz) * NC
                + 4 * ln(omz) * NC * x
                - 4 * ln(omz) * NC * pow(x, 2)
                + 11.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1)
                + 7.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * x
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                - 3.0 / 4.0 * pow(ln(omz), 2) * NC * pow(z, -1)
                - 3.0 / 4.0 * pow(ln(omz), 2) * NC * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(omz), 2) * NC
                + 3.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(z, -1)
                + 3.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(omz, -1)
                - 3 * pow(ln(omz), 2) * NC * x
                - 3.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(z, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 3 * pow(ln(omz), 2) * NC * pow(x, 2)
                - ln(omz) * ln(omxmz) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1)
                + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1)
                + ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(omz) * ln(omxmz) * pow(NC, -1) * x
                - ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * NC * pow(omz, -1)
                - ln(omz) * ln(omxmz) * NC
                - ln(omz) * ln(omxmz) * NC * x * pow(z, -1)
            )
            tmp += (
                -ln(omz) * ln(omxmz) * NC * x * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * NC * x
                + ln(omz) * ln(omxmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(omz) * ln(omxmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * NC * pow(x, 2)
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(omz, -1)
                - Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC
                - Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x * pow(z, -1)
                - Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2) * pow(z, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2)
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1)
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1)
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(NC, -1)
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1)
                - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * pow(omz, -1)
            )
            tmp += (
                +Li2(omx * pow(omz, -1)) * pow(NC, -1) * x
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * NC * pow(omz, -1)
                - Li2(omx * pow(omz, -1)) * NC
                - Li2(omx * pow(omz, -1)) * NC * x * pow(z, -1)
                - Li2(omx * pow(omz, -1)) * NC * x * pow(omz, -1)
                + 2 * Li2(omx * pow(omz, -1)) * NC * x
                + Li2(omx * pow(omz, -1)) * NC * pow(x, 2) * pow(z, -1)
                + Li2(omx * pow(omz, -1)) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * Li2(omx * pow(omz, -1)) * NC * pow(x, 2)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1)
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1)
                + Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * x
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * NC * pow(z, -1)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * NC * pow(omz, -1)
                + Li2(z * pow(omx, -1)) * NC
                + Li2(z * pow(omx, -1)) * NC * x * pow(z, -1)
                + Li2(z * pow(omx, -1)) * NC * x * pow(omz, -1)
                - 2 * Li2(z * pow(omx, -1)) * NC * x
                - Li2(z * pow(omx, -1)) * NC * pow(x, 2) * pow(z, -1)
                - Li2(z * pow(omx, -1)) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * NC * pow(x, 2)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1)
                - Li2(z) * pow(NC, -1) * x * pow(z, -1)
                + Li2(z) * pow(NC, -1) * x * pow(omz, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                3.0 / 2.0 * pow(NC, -1) * pow(z, -1)
                - 11.0 / 12.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2)
                + 3.0 / 2.0 * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 12.0 * pow(NC, -1) * pow(pi, 2)
                + 11.0 / 6.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2)
                + 5.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                + 1.0 / 12.0 * NC * pow(z, -1) * pow(pi, 2)
                - 2 * NC
                + 1.0 / 12.0 * NC * pow(pi, 2) * pow(omz, -1)
                - 1.0 / 6.0 * NC * pow(pi, 2)
                - 1.0 / 6.0 * NC * x * pow(z, -1) * pow(pi, 2)
                - 2 * NC * x
                - 1.0 / 6.0 * NC * x * pow(pi, 2) * pow(omz, -1)
                + 1.0 / 3.0 * NC * x * pow(pi, 2)
                + 1.0 / 6.0 * NC * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                + 2 * NC * pow(x, 2)
                + 1.0 / 6.0 * NC * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                - 1.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(z, -1)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(x) * pow(NC, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(z, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * NC
                - 6 * ln(x) * NC * x
                + 6 * ln(x) * NC * pow(x, 2)
                + ln(x) * ln(-omxmz) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1)
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(-omxmz) * pow(NC, -1) * x
                + ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * NC * pow(omz, -1)
                + ln(x) * ln(-omxmz) * NC
                + ln(x) * ln(-omxmz) * NC * x * pow(z, -1)
                + ln(x) * ln(-omxmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * NC * x
                - ln(x) * ln(-omxmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(-omxmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * NC * pow(x, 2)
                + 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1)
                + 9.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                - 3 * pow(ln(x), 2) * pow(NC, -1)
                - 9 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1)
                - 9 * pow(ln(x), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 6 * pow(ln(x), 2) * pow(NC, -1) * x
                + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 7.0 / 4.0 * pow(ln(x), 2) * NC * pow(z, -1)
                - 7.0 / 4.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * NC
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(z, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(omz, -1)
                - 7 * pow(ln(x), 2) * NC * x
                - 7.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, 2) * pow(z, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 7 * pow(ln(x), 2) * NC * pow(x, 2)
                - 13.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1)
                - 7 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1)
                + 13 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1)
                + 14 * ln(x) * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                - 9 * ln(x) * ln(z) * pow(NC, -1) * x
                - 9 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 9 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                +9 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 3 * ln(x) * ln(z) * NC * pow(z, -1)
                + 3 * ln(x) * ln(z) * NC * pow(omz, -1)
                - 6 * ln(x) * ln(z) * NC
                - 6 * ln(x) * ln(z) * NC * x * pow(z, -1)
                - 6 * ln(x) * ln(z) * NC * x * pow(omz, -1)
                + 12 * ln(x) * ln(z) * NC * x
                + 6 * ln(x) * ln(z) * NC * pow(x, 2) * pow(z, -1)
                + 6 * ln(x) * ln(z) * NC * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * ln(z) * NC * pow(x, 2)
                - 15.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1)
                - 15.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 5 * ln(x) * ln(omx) * pow(NC, -1)
                + 15 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + 15 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                - 10 * ln(x) * ln(omx) * pow(NC, -1) * x
                - 10 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 10 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 10 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 3.0 / 2.0 * ln(x) * ln(omx) * NC * pow(z, -1)
                + 3.0 / 2.0 * ln(x) * ln(omx) * NC * pow(omz, -1)
                - 3 * ln(x) * ln(omx) * NC
                - 3 * ln(x) * ln(omx) * NC * x * pow(z, -1)
                - 3 * ln(x) * ln(omx) * NC * x * pow(omz, -1)
                + 6 * ln(x) * ln(omx) * NC * x
                + 3 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                + 3 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 7 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1)
                - 13.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1)
                + 14 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 13 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                - 9 * ln(x) * ln(omz) * pow(NC, -1) * x
                - 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 3 * ln(x) * ln(omz) * NC * pow(z, -1)
            )
            tmp += (
                +3 * ln(x) * ln(omz) * NC * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * NC
                - 6 * ln(x) * ln(omz) * NC * x * pow(z, -1)
                - 6 * ln(x) * ln(omz) * NC * x * pow(omz, -1)
                + 12 * ln(x) * ln(omz) * NC * x
                + 6 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 6 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(x) * ln(xmz) * pow(NC, -1) * pow(z, -1)
                + ln(x) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * pow(NC, -1)
                - ln(x) * ln(xmz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(xmz) * pow(NC, -1) * x
                + ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(xmz) * NC * pow(omz, -1)
                + ln(x) * ln(xmz) * NC
                + ln(x) * ln(xmz) * NC * x * pow(z, -1)
                + ln(x) * ln(xmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(xmz) * NC * x
                - ln(x) * ln(xmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(xmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * NC * pow(x, 2)
                + ln(z) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * pow(NC, -1)
                + ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(z) * NC * pow(z, -1)
                - ln(z) * NC * pow(omz, -1)
                + 3 * ln(z) * NC
                + 4 * ln(z) * NC * x
                - 4 * ln(z) * NC * pow(x, 2)
                + 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1)
                + 9.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1)
                - 3 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1)
                - 9.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x
            )
            tmp += (
                +5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - pow(ln(z), 2) * NC * pow(z, -1)
                - pow(ln(z), 2) * NC * pow(omz, -1)
                + 2 * pow(ln(z), 2) * NC
                + 2 * pow(ln(z), 2) * NC * x * pow(z, -1)
                + 2 * pow(ln(z), 2) * NC * x * pow(omz, -1)
                - 4 * pow(ln(z), 2) * NC * x
                - 2 * pow(ln(z), 2) * NC * pow(x, 2) * pow(z, -1)
                - 2 * pow(ln(z), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * pow(ln(z), 2) * NC * pow(x, 2)
                + 4 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1)
                + 5 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(z) * ln(omx) * pow(NC, -1)
                - 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 10 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * x
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - ln(z) * ln(omx) * NC * pow(z, -1)
                - ln(z) * ln(omx) * NC * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * NC
                + 2 * ln(z) * ln(omx) * NC * x * pow(z, -1)
                + 2 * ln(z) * ln(omx) * NC * x * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * NC * x
                - 2 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                - 2 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 7.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1)
                - 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 7 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 5 * ln(z) * ln(omz) * pow(NC, -1) * x
                + 5 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 5 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                -5 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(z, -1)
                - 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(omz, -1)
                + 5 * ln(z) * ln(omz) * NC
                + 5 * ln(z) * ln(omz) * NC * x * pow(z, -1)
                + 5 * ln(z) * ln(omz) * NC * x * pow(omz, -1)
                - 10 * ln(z) * ln(omz) * NC * x
                - 5 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 5 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(z) * ln(xmz) * pow(NC, -1) * pow(z, -1)
                - ln(z) * ln(xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * pow(NC, -1)
                + ln(z) * ln(xmz) * pow(NC, -1) * x * pow(z, -1)
                + 2 * ln(z) * ln(xmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(z) * ln(xmz) * pow(NC, -1) * x
                - ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * ln(xmz) * NC * pow(omz, -1)
                - ln(z) * ln(xmz) * NC
                - ln(z) * ln(xmz) * NC * x * pow(z, -1)
                - ln(z) * ln(xmz) * NC * x * pow(omz, -1)
                + 2 * ln(z) * ln(xmz) * NC * x
                + ln(z) * ln(xmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(z) * ln(xmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * NC * pow(x, 2)
                + ln(omx) * pow(NC, -1) * pow(z, -1)
                + ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omx) * pow(NC, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(omx) * NC
                + 2 * ln(omx) * NC * x
                - 2 * ln(omx) * NC * pow(x, 2)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(ln(omx), 2) * pow(NC, -1)
            )
            tmp += (
                -6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1)
                - 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(z, -1)
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(z, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(omz, -1)
                - pow(ln(omx), 2) * NC * x
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(z, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(omz, -1)
                + pow(ln(omx), 2) * NC * pow(x, 2)
                + 5 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(omx) * ln(omz) * pow(NC, -1)
                - 10 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 8 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * x
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - ln(omx) * ln(omz) * NC * pow(z, -1)
                - ln(omx) * ln(omz) * NC * pow(omz, -1)
                + 2 * ln(omx) * ln(omz) * NC
                + 2 * ln(omx) * ln(omz) * NC * x * pow(z, -1)
                + 2 * ln(omx) * ln(omz) * NC * x * pow(omz, -1)
                - 4 * ln(omx) * ln(omz) * NC * x
                - 2 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 2 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(z, -1)
                + ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(omz) * pow(NC, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(omz) * NC * pow(z, -1)
                - ln(omz) * NC * pow(omz, -1)
                + 3 * ln(omz) * NC
                + 4 * ln(omz) * NC * x
                - 4 * ln(omz) * NC * pow(x, 2)
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1)
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * x
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * NC * pow(omz, -1)
                - ln(omz) * ln(-omxmz) * NC
                - ln(omz) * ln(-omxmz) * NC * x * pow(z, -1)
                - ln(omz) * ln(-omxmz) * NC * x * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * NC * x
                + ln(omz) * ln(-omxmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(omz) * ln(-omxmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * NC * pow(x, 2)
                + 9.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1)
                + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1)
                - 9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1)
                - 3 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x
                + 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                - pow(ln(omz), 2) * NC * pow(z, -1)
                - pow(ln(omz), 2) * NC * pow(omz, -1)
            )
            tmp += (
                +2 * pow(ln(omz), 2) * NC
                + 2 * pow(ln(omz), 2) * NC * x * pow(z, -1)
                + 2 * pow(ln(omz), 2) * NC * x * pow(omz, -1)
                - 4 * pow(ln(omz), 2) * NC * x
                - 2 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(z, -1)
                - 2 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * NC * pow(x, 2)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1)
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1)
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1)
                - Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * x
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * NC * pow(omz, -1)
                - Li2(pow(z, -1) * omx) * NC
                - Li2(pow(z, -1) * omx) * NC * x * pow(z, -1)
                - Li2(pow(z, -1) * omx) * NC * x * pow(omz, -1)
                + 2 * Li2(pow(z, -1) * omx) * NC * x
                + Li2(pow(z, -1) * omx) * NC * pow(x, 2) * pow(z, -1)
                + Li2(pow(z, -1) * omx) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * NC * pow(x, 2)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1)
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * pow(NC, -1)
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1)
                - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * x
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(omx * pow(omz, -1)) * NC * pow(omz, -1)
                - Li2(omx * pow(omz, -1)) * NC
                - Li2(omx * pow(omz, -1)) * NC * x * pow(z, -1)
                - Li2(omx * pow(omz, -1)) * NC * x * pow(omz, -1)
                + 2 * Li2(omx * pow(omz, -1)) * NC * x
                + Li2(omx * pow(omz, -1)) * NC * pow(x, 2) * pow(z, -1)
                + Li2(omx * pow(omz, -1)) * NC * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                -2 * Li2(omx * pow(omz, -1)) * NC * pow(x, 2)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(z, -1)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(omz, -1)
                + Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC
                + Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x * pow(z, -1)
                + Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x * pow(omz, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2) * pow(z, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2)
                + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1)
                - Li2(z) * pow(NC, -1) * x * pow(z, -1)
                + Li2(z) * pow(NC, -1) * x * pow(omz, -1)
            )

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                3.0 / 2.0 * pow(NC, -1) * pow(z, -1)
                - 11.0 / 12.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2)
                + 3.0 / 2.0 * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 12.0 * pow(NC, -1) * pow(pi, 2)
                + 11.0 / 6.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2)
                + 5.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                + 5.0 / 12.0 * NC * pow(z, -1) * pow(pi, 2)
                - 2 * NC
                + 5.0 / 12.0 * NC * pow(pi, 2) * pow(omz, -1)
                - 5.0 / 6.0 * NC * pow(pi, 2)
                - 5.0 / 6.0 * NC * x * pow(z, -1) * pow(pi, 2)
                - 2 * NC * x
                - 5.0 / 6.0 * NC * x * pow(pi, 2) * pow(omz, -1)
                + 5.0 / 3.0 * NC * x * pow(pi, 2)
                + 5.0 / 6.0 * NC * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                + 2 * NC * pow(x, 2)
                + 5.0 / 6.0 * NC * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                - 5.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(z, -1)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(x) * pow(NC, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(z, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * NC
                - 6 * ln(x) * NC * x
                + 6 * ln(x) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(z, -1)
                + ln(x) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(NC, -1)
                - ln(x) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(-xmz) * pow(NC, -1) * x
                + ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * NC * pow(omz, -1)
                + ln(x) * ln(-xmz) * NC
                + ln(x) * ln(-xmz) * NC * x * pow(z, -1)
                + ln(x) * ln(-xmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(-xmz) * NC * x
                - ln(x) * ln(-xmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(-xmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * NC * pow(x, 2)
                + 21.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1)
                + 21.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 7 * pow(ln(x), 2) * pow(NC, -1) * x
                + 7 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 7 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 7.0 / 4.0 * pow(ln(x), 2) * NC * pow(z, -1)
                - 7.0 / 4.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * NC
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(z, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(omz, -1)
                - 7 * pow(ln(x), 2) * NC * x
                - 7.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, 2) * pow(z, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 7 * pow(ln(x), 2) * NC * pow(x, 2)
                - 6 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1)
                - 15.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1)
                + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1)
                + 15 * ln(x) * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                - 9 * ln(x) * ln(z) * pow(NC, -1) * x
                - 9 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 9 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                +9 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 3 * ln(x) * ln(z) * NC * pow(z, -1)
                + 3 * ln(x) * ln(z) * NC * pow(omz, -1)
                - 6 * ln(x) * ln(z) * NC
                - 6 * ln(x) * ln(z) * NC * x * pow(z, -1)
                - 6 * ln(x) * ln(z) * NC * x * pow(omz, -1)
                + 12 * ln(x) * ln(z) * NC * x
                + 6 * ln(x) * ln(z) * NC * pow(x, 2) * pow(z, -1)
                + 6 * ln(x) * ln(z) * NC * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * ln(z) * NC * pow(x, 2)
                - 9 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1)
                - 9 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 6 * ln(x) * ln(omx) * pow(NC, -1)
                + 18 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + 18 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                - 12 * ln(x) * ln(omx) * pow(NC, -1) * x
                - 12 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 12 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 12 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 3.0 / 2.0 * ln(x) * ln(omx) * NC * pow(z, -1)
                + 3.0 / 2.0 * ln(x) * ln(omx) * NC * pow(omz, -1)
                - 3 * ln(x) * ln(omx) * NC
                - 3 * ln(x) * ln(omx) * NC * x * pow(z, -1)
                - 3 * ln(x) * ln(omx) * NC * x * pow(omz, -1)
                + 6 * ln(x) * ln(omx) * NC * x
                + 3 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                + 3 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 15.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1)
                - 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1)
                + 15 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 12 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                - 9 * ln(x) * ln(omz) * pow(NC, -1) * x
                - 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 3 * ln(x) * ln(omz) * NC * pow(z, -1)
            )
            tmp += (
                +3 * ln(x) * ln(omz) * NC * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * NC
                - 6 * ln(x) * ln(omz) * NC * x * pow(z, -1)
                - 6 * ln(x) * ln(omz) * NC * x * pow(omz, -1)
                + 12 * ln(x) * ln(omz) * NC * x
                + 6 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 6 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * NC * pow(x, 2)
                + ln(x) * ln(omxmz) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * pow(NC, -1)
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(omxmz) * pow(NC, -1) * x
                + ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(omxmz) * NC * pow(omz, -1)
                + ln(x) * ln(omxmz) * NC
                + ln(x) * ln(omxmz) * NC * x * pow(z, -1)
                + ln(x) * ln(omxmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * NC * x
                - ln(x) * ln(omxmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(omxmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * NC * pow(x, 2)
                + ln(z) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * pow(NC, -1)
                + ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(z) * NC * pow(z, -1)
                - ln(z) * NC * pow(omz, -1)
                + 3 * ln(z) * NC
                + 4 * ln(z) * NC * x
                - 4 * ln(z) * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(z, -1)
                - ln(z) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(NC, -1)
                + ln(z) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1)
            )
            tmp += (
                +2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(z) * ln(-xmz) * pow(NC, -1) * x
                - ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * NC * pow(omz, -1)
                - ln(z) * ln(-xmz) * NC
                - ln(z) * ln(-xmz) * NC * x * pow(z, -1)
                - ln(z) * ln(-xmz) * NC * x * pow(omz, -1)
                + 2 * ln(z) * ln(-xmz) * NC * x
                + ln(z) * ln(-xmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(z) * ln(-xmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * NC * pow(x, 2)
                + 7.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1)
                + 11.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1)
                - 11.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 3 * pow(ln(z), 2) * pow(NC, -1) * x
                + 3 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 3 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 3 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - 5.0 / 4.0 * pow(ln(z), 2) * NC * pow(z, -1)
                - 5.0 / 4.0 * pow(ln(z), 2) * NC * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * NC
                + 5.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(z, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(omz, -1)
                - 5 * pow(ln(z), 2) * NC * x
                - 5.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * pow(z, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 5 * pow(ln(z), 2) * NC * pow(x, 2)
                + 9.0 / 2.0 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1)
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * ln(z) * ln(omx) * pow(NC, -1)
                - 9 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 12 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
            )
            tmp += (
                +7 * ln(z) * ln(omx) * pow(NC, -1) * x
                + 7 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 7 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(z) * ln(omx) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(z) * ln(omx) * NC * pow(omz, -1)
                + ln(z) * ln(omx) * NC
                + ln(z) * ln(omx) * NC * x * pow(z, -1)
                + ln(z) * ln(omx) * NC * x * pow(omz, -1)
                - 2 * ln(z) * ln(omx) * NC * x
                - ln(z) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                - ln(z) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 5.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 4 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 3 * ln(z) * ln(omz) * pow(NC, -1) * x
                + 3 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 3 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 3 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(z, -1)
                - 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(omz, -1)
                + 5 * ln(z) * ln(omz) * NC
                + 5 * ln(z) * ln(omz) * NC * x * pow(z, -1)
                + 5 * ln(z) * ln(omz) * NC * x * pow(omz, -1)
                - 10 * ln(z) * ln(omz) * NC * x
                - 5 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 5 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * NC * pow(x, 2)
                + ln(omx) * pow(NC, -1) * pow(z, -1)
                + ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omx) * pow(NC, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(omx) * NC
                + 2 * ln(omx) * NC * x
            )
            tmp += (
                -2 * ln(omx) * NC * pow(x, 2)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(ln(omx), 2) * pow(NC, -1)
                - 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1)
                - 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 3.0 / 4.0 * pow(ln(omx), 2) * NC * pow(z, -1)
                - 3.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(omx), 2) * NC
                + 3.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(z, -1)
                + 3.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(omz, -1)
                - 3 * pow(ln(omx), 2) * NC * x
                - 3.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(z, -1)
                - 3.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 3 * pow(ln(omx), 2) * NC * pow(x, 2)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 9.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1)
                - 12 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 9 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 7 * ln(omx) * ln(omz) * pow(NC, -1) * x
                + 7 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 7 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(omx) * ln(omz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(omx) * ln(omz) * NC * pow(omz, -1)
                + ln(omx) * ln(omz) * NC
                + ln(omx) * ln(omz) * NC * x * pow(z, -1)
                + ln(omx) * ln(omz) * NC * x * pow(omz, -1)
                - 2 * ln(omx) * ln(omz) * NC * x
                - ln(omx) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - ln(omx) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                +2 * ln(omx) * ln(omz) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(z, -1)
                + ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(omz) * pow(NC, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(omz) * NC * pow(z, -1)
                - ln(omz) * NC * pow(omz, -1)
                + 3 * ln(omz) * NC
                + 4 * ln(omz) * NC * x
                - 4 * ln(omz) * NC * pow(x, 2)
                + 11.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1)
                + 7.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * x
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                - 5.0 / 4.0 * pow(ln(omz), 2) * NC * pow(z, -1)
                - 5.0 / 4.0 * pow(ln(omz), 2) * NC * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(z, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(omz, -1)
                - 5 * pow(ln(omz), 2) * NC * x
                - 5.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(z, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 5 * pow(ln(omz), 2) * NC * pow(x, 2)
                - ln(omz) * ln(omxmz) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * pow(NC, -1)
                + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1)
                + ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(omz) * ln(omxmz) * pow(NC, -1) * x
                - ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                +ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(omz) * ln(omxmz) * NC * pow(omz, -1)
                - ln(omz) * ln(omxmz) * NC
                - ln(omz) * ln(omxmz) * NC * x * pow(z, -1)
                - ln(omz) * ln(omxmz) * NC * x * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * NC * x
                + ln(omz) * ln(omxmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(omz) * ln(omxmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * NC * pow(x, 2)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(NC, -1)
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1)
                + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * x
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * NC * pow(z, -1)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * NC * pow(omz, -1)
                + Li2(pow(omx, -1) * omz) * NC
                + Li2(pow(omx, -1) * omz) * NC * x * pow(z, -1)
                + Li2(pow(omx, -1) * omz) * NC * x * pow(omz, -1)
                - 2 * Li2(pow(omx, -1) * omz) * NC * x
                - Li2(pow(omx, -1) * omz) * NC * pow(x, 2) * pow(z, -1)
                - Li2(pow(omx, -1) * omz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * Li2(pow(omx, -1) * omz) * NC * pow(x, 2)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(z * pow(omx, -1)) * pow(NC, -1)
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1)
                + Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * x
            )
            tmp += (
                -Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * NC * pow(z, -1)
                - 1.0 / 2.0 * Li2(z * pow(omx, -1)) * NC * pow(omz, -1)
                + Li2(z * pow(omx, -1)) * NC
                + Li2(z * pow(omx, -1)) * NC * x * pow(z, -1)
                + Li2(z * pow(omx, -1)) * NC * x * pow(omz, -1)
                - 2 * Li2(z * pow(omx, -1)) * NC * x
                - Li2(z * pow(omx, -1)) * NC * pow(x, 2) * pow(z, -1)
                - Li2(z * pow(omx, -1)) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * NC * pow(x, 2)
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(z, -1)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(omz, -1)
                + Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC
                + Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x * pow(z, -1)
                + Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x * pow(omz, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2) * pow(z, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                +2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1)
                - Li2(z) * pow(NC, -1) * x * pow(z, -1)
                + Li2(z) * pow(NC, -1) * x * pow(omz, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                3.0 / 2.0 * pow(NC, -1) * pow(z, -1)
                - 11.0 / 12.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2)
                + 3.0 / 2.0 * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 12.0 * pow(NC, -1) * pow(pi, 2)
                + 11.0 / 6.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2)
                + 5.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                - pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                + 7.0 / 6.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                + 1.0 / 12.0 * NC * pow(z, -1) * pow(pi, 2)
                - 2 * NC
                + 1.0 / 12.0 * NC * pow(pi, 2) * pow(omz, -1)
                - 1.0 / 6.0 * NC * pow(pi, 2)
                - 1.0 / 6.0 * NC * x * pow(z, -1) * pow(pi, 2)
                - 2 * NC * x
                - 1.0 / 6.0 * NC * x * pow(pi, 2) * pow(omz, -1)
                + 1.0 / 3.0 * NC * x * pow(pi, 2)
                + 1.0 / 6.0 * NC * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                + 2 * NC * pow(x, 2)
                + 1.0 / 6.0 * NC * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                - 1.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(z, -1)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                + 3 * ln(x) * pow(NC, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 3 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(z, -1)
                + 3.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * NC
                - 6 * ln(x) * NC * x
                + 6 * ln(x) * NC * pow(x, 2)
                + ln(x) * ln(-omxmz) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * pow(NC, -1)
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(-omxmz) * pow(NC, -1) * x
                + ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(-omxmz) * NC * pow(omz, -1)
                + ln(x) * ln(-omxmz) * NC
                + ln(x) * ln(-omxmz) * NC * x * pow(z, -1)
                + ln(x) * ln(-omxmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * NC * x
                - ln(x) * ln(-omxmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(-omxmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(z, -1)
                + ln(x) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * pow(NC, -1)
                - ln(x) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * pow(omz, -1)
                + ln(x) * ln(-xmz) * pow(NC, -1) * x
                + ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(x) * ln(-xmz) * NC * pow(omz, -1)
                + ln(x) * ln(-xmz) * NC
                + ln(x) * ln(-xmz) * NC * x * pow(z, -1)
                + ln(x) * ln(-xmz) * NC * x * pow(omz, -1)
                - 2 * ln(x) * ln(-xmz) * NC * x
                - ln(x) * ln(-xmz) * NC * pow(x, 2) * pow(z, -1)
                - ln(x) * ln(-xmz) * NC * pow(x, 2) * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * NC * pow(x, 2)
                + 19.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1)
                + 5 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                - 13.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1)
                - 10 * pow(ln(x), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x
                + 13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 13.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                - 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(z, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                + 3 * pow(ln(x), 2) * NC
                + 3 * pow(ln(x), 2) * NC * x * pow(z, -1)
                + 3 * pow(ln(x), 2) * NC * x * pow(omz, -1)
                - 6 * pow(ln(x), 2) * NC * x
                - 3 * pow(ln(x), 2) * NC * pow(x, 2) * pow(z, -1)
                - 3 * pow(ln(x), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 6 * pow(ln(x), 2) * NC * pow(x, 2)
                - 7 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1)
                - 8 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 5 * ln(x) * ln(z) * pow(NC, -1)
                + 14 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1)
                + 16 * ln(x) * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                - 10 * ln(x) * ln(z) * pow(NC, -1) * x
                - 10 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 10 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 10 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                + 5.0 / 2.0 * ln(x) * ln(z) * NC * pow(z, -1)
                + 5.0 / 2.0 * ln(x) * ln(z) * NC * pow(omz, -1)
                - 5 * ln(x) * ln(z) * NC
                - 5 * ln(x) * ln(z) * NC * x * pow(z, -1)
                - 5 * ln(x) * ln(z) * NC * x * pow(omz, -1)
                + 10 * ln(x) * ln(z) * NC * x
                + 5 * ln(x) * ln(z) * NC * pow(x, 2) * pow(z, -1)
                + 5 * ln(x) * ln(z) * NC * pow(x, 2) * pow(omz, -1)
                - 10 * ln(x) * ln(z) * NC * pow(x, 2)
                - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1)
                - 17.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 11.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1)
                + 16 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + 17 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                - 11 * ln(x) * ln(omx) * pow(NC, -1) * x
                - 11 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 11 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 11 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
            )
            tmp += (
                +2 * ln(x) * ln(omx) * NC * pow(z, -1)
                + 2 * ln(x) * ln(omx) * NC * pow(omz, -1)
                - 4 * ln(x) * ln(omx) * NC
                - 4 * ln(x) * ln(omx) * NC * x * pow(z, -1)
                - 4 * ln(x) * ln(omx) * NC * x * pow(omz, -1)
                + 8 * ln(x) * ln(omx) * NC * x
                + 4 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                + 4 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * NC * pow(x, 2)
                - 13.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1)
                - 11.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * ln(omz) * pow(NC, -1)
                + 13 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 11 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                - 8 * ln(x) * ln(omz) * pow(NC, -1) * x
                - 8 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 8 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 5.0 / 2.0 * ln(x) * ln(omz) * NC * pow(z, -1)
                + 5.0 / 2.0 * ln(x) * ln(omz) * NC * pow(omz, -1)
                - 5 * ln(x) * ln(omz) * NC
                - 5 * ln(x) * ln(omz) * NC * x * pow(z, -1)
                - 5 * ln(x) * ln(omz) * NC * x * pow(omz, -1)
                + 10 * ln(x) * ln(omz) * NC * x
                + 5 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 5 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * NC * pow(x, 2)
                + ln(z) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * pow(NC, -1)
                + ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(z) * NC * pow(z, -1)
                - ln(z) * NC * pow(omz, -1)
                + 3 * ln(z) * NC
                + 4 * ln(z) * NC * x
                - 4 * ln(z) * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(z, -1)
                - ln(z) * ln(-xmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * pow(NC, -1)
                + ln(z) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1)
            )
            tmp += (
                +2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(z) * ln(-xmz) * pow(NC, -1) * x
                - ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(z) * ln(-xmz) * NC * pow(omz, -1)
                - ln(z) * ln(-xmz) * NC
                - ln(z) * ln(-xmz) * NC * x * pow(z, -1)
                - ln(z) * ln(-xmz) * NC * x * pow(omz, -1)
                + 2 * ln(z) * ln(-xmz) * NC * x
                + ln(z) * ln(-xmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(z) * ln(-xmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * NC * pow(x, 2)
                + 7.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1)
                + 11.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1)
                - 11.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 3 * pow(ln(z), 2) * pow(NC, -1) * x
                + 3 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 3 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 3 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - 3.0 / 4.0 * pow(ln(z), 2) * NC * pow(z, -1)
                - 3.0 / 4.0 * pow(ln(z), 2) * NC * pow(omz, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * NC
                + 3.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(z, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(omz, -1)
                - 3 * pow(ln(z), 2) * NC * x
                - 3.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * pow(z, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 3 * pow(ln(z), 2) * NC * pow(x, 2)
                + 9.0 / 2.0 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1)
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 7.0 / 2.0 * ln(z) * ln(omx) * pow(NC, -1)
                - 9 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 12 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
            )
            tmp += (
                +7 * ln(z) * ln(omx) * pow(NC, -1) * x
                + 7 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 7 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 3.0 / 2.0 * ln(z) * ln(omx) * NC * pow(z, -1)
                - 3.0 / 2.0 * ln(z) * ln(omx) * NC * pow(omz, -1)
                + 3 * ln(z) * ln(omx) * NC
                + 3 * ln(z) * ln(omx) * NC * x * pow(z, -1)
                + 3 * ln(z) * ln(omx) * NC * x * pow(omz, -1)
                - 6 * ln(z) * ln(omx) * NC * x
                - 3 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                - 3 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                + 6 * ln(z) * ln(omx) * NC * pow(x, 2)
                + 7.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 5.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(omz) * pow(NC, -1)
                - 7 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 5 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * x
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - 2 * ln(z) * ln(omz) * NC * pow(z, -1)
                - 2 * ln(z) * ln(omz) * NC * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * NC
                + 4 * ln(z) * ln(omz) * NC * x * pow(z, -1)
                + 4 * ln(z) * ln(omz) * NC * x * pow(omz, -1)
                - 8 * ln(z) * ln(omz) * NC * x
                - 4 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 4 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * NC * pow(x, 2)
                + ln(omx) * pow(NC, -1) * pow(z, -1)
                + ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omx) * pow(NC, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(z, -1)
                - 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(omx) * NC
                + 2 * ln(omx) * NC * x
            )
            tmp += (
                -2 * ln(omx) * NC * pow(x, 2)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(ln(omx), 2) * pow(NC, -1)
                - 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1)
                - 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(z, -1)
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(z, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(omz, -1)
                - pow(ln(omx), 2) * NC * x
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(z, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(omz, -1)
                + pow(ln(omx), 2) * NC * pow(x, 2)
                + 5 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3 * ln(omx) * ln(omz) * pow(NC, -1)
                - 10 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 8 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * x
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - ln(omx) * ln(omz) * NC * pow(z, -1)
                - ln(omx) * ln(omz) * NC * pow(omz, -1)
                + 2 * ln(omx) * ln(omz) * NC
                + 2 * ln(omx) * ln(omz) * NC * x * pow(z, -1)
                + 2 * ln(omx) * ln(omz) * NC * x * pow(omz, -1)
                - 4 * ln(omx) * ln(omz) * NC * x
                - 2 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 2 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * NC * pow(x, 2)
            )
            tmp += (
                +1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(z, -1)
                + ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(omz) * pow(NC, -1)
                + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(omz) * NC * pow(z, -1)
                - ln(omz) * NC * pow(omz, -1)
                + 3 * ln(omz) * NC
                + 4 * ln(omz) * NC * x
                - 4 * ln(omz) * NC * pow(x, 2)
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * pow(NC, -1)
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(omz, -1)
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * x
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(omz) * ln(-omxmz) * NC * pow(omz, -1)
                - ln(omz) * ln(-omxmz) * NC
                - ln(omz) * ln(-omxmz) * NC * x * pow(z, -1)
                - ln(omz) * ln(-omxmz) * NC * x * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * NC * x
                + ln(omz) * ln(-omxmz) * NC * pow(x, 2) * pow(z, -1)
                + ln(omz) * ln(-omxmz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * NC * pow(x, 2)
                + 9.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1)
                + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1)
                - 9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1)
                - 3 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x
                + 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                -5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                - pow(ln(omz), 2) * NC * pow(z, -1)
                - pow(ln(omz), 2) * NC * pow(omz, -1)
                + 2 * pow(ln(omz), 2) * NC
                + 2 * pow(ln(omz), 2) * NC * x * pow(z, -1)
                + 2 * pow(ln(omz), 2) * NC * x * pow(omz, -1)
                - 4 * pow(ln(omz), 2) * NC * x
                - 2 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(z, -1)
                - 2 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * NC * pow(x, 2)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(omz, -1)
                - Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC
                - Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x * pow(z, -1)
                - Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2) * pow(z, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(z, -1)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -1.0 / 2.0 * Li2(pow(z, -1) * omx) * pow(NC, -1)
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1)
                - Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * x
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(pow(z, -1) * omx) * NC * pow(omz, -1)
                - Li2(pow(z, -1) * omx) * NC
                - Li2(pow(z, -1) * omx) * NC * x * pow(z, -1)
                - Li2(pow(z, -1) * omx) * NC * x * pow(omz, -1)
                + 2 * Li2(pow(z, -1) * omx) * NC * x
                + Li2(pow(z, -1) * omx) * NC * pow(x, 2) * pow(z, -1)
                + Li2(pow(z, -1) * omx) * NC * pow(x, 2) * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * NC * pow(x, 2)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * pow(NC, -1)
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1)
                + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * pow(omz, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * x
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * NC * pow(z, -1)
                - 1.0 / 2.0 * Li2(pow(omx, -1) * omz) * NC * pow(omz, -1)
                + Li2(pow(omx, -1) * omz) * NC
                + Li2(pow(omx, -1) * omz) * NC * x * pow(z, -1)
                + Li2(pow(omx, -1) * omz) * NC * x * pow(omz, -1)
                - 2 * Li2(pow(omx, -1) * omz) * NC * x
                - Li2(pow(omx, -1) * omz) * NC * pow(x, 2) * pow(z, -1)
                - Li2(pow(omx, -1) * omz) * NC * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                +2 * Li2(pow(omx, -1) * omz) * NC * pow(x, 2)
                + 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1)
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(omz, -1)
                - Li2(z) * pow(NC, -1) * x * pow(z, -1)
                + Li2(z) * pow(NC, -1) * x * pow(omz, -1)
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
                -1.0 / 16.0 * pow(NC, -1) * pow(x, -1) * pow(poly2, -1)
                + 1.0 / 16.0 * pow(NC, -1) * pow(x, -1)
                - 2 * pow(NC, -1) * pow(z, -1) * pow(omz, -1)
                + 9.0 / 16.0 * pow(NC, -1) * pow(z, -1)
                + 3.0 / 4.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2)
                + 1.0 / 16.0 * pow(NC, -1) * pow(poly2, -1)
                + 1.0 / 2.0 * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 4.0 * pow(NC, -1) * pow(omxmz, -1)
                - 21.0 / 16.0 * pow(NC, -1)
                + 3.0 / 4.0 * pow(NC, -1) * pow(pi, 2) * pow(omz, -1)
                - 5.0 / 12.0 * pow(NC, -1) * pow(pi, 2)
                + 7.0 / 16.0 * pow(NC, -1) * z
                - 1.0 / 12.0 * pow(NC, -1) * z * pow(pi, 2)
                + 4 * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                - 3 * pow(NC, -1) * x * pow(z, -1)
                - 13.0 / 6.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2)
                - 4 * pow(NC, -1) * x * pow(omz, -1)
                + 3.0 / 4.0 * pow(NC, -1) * x * pow(omxmz, -1)
                - 7.0 / 16.0 * pow(NC, -1) * x
                - 3.0 / 2.0 * pow(NC, -1) * x * pow(pi, 2) * pow(omz, -1)
                + 5.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2)
                + pow(NC, -1) * x * z
                - 1.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2)
                - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                + 11.0 / 4.0 * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(pi, 2)
                + 3 * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - pow(NC, -1) * pow(x, 2) * pow(omxmz, -1)
                - 7.0 / 16.0 * pow(NC, -1) * pow(x, 2)
                + pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                - 4.0 / 3.0 * pow(NC, -1) * pow(x, 2) * pow(pi, 2)
                - 3.0 / 2.0 * pow(NC, -1) * pow(x, 2) * z
                - 1.0 / 6.0 * pow(NC, -1) * pow(x, 2) * z * pow(pi, 2)
                + 1.0 / 16.0 * pow(NC, -1) * pow(x, 3) * pow(poly2, -1)
                + 1.0 / 2.0 * pow(NC, -1) * pow(x, 3) * pow(omxmz, -1)
                - 1.0 / 16.0 * pow(NC, -1) * pow(x, 4) * pow(poly2, -1)
                + 13.0 / 9.0 * NC * pow(x, -1) * pow(z, -1)
                + 1.0 / 16.0 * NC * pow(x, -1) * pow(poly2, -1)
                - 425.0 / 144.0 * NC * pow(x, -1)
                + 2 * NC * pow(z, -1) * pow(omz, -1)
            )
            tmp += (
                -199.0 / 48.0 * NC * pow(z, -1)
                - 1.0 / 3.0 * NC * pow(z, -1) * pow(pi, 2) * pow(omz, -1)
                + 1.0 / 6.0 * NC * pow(z, -1) * pow(pi, 2)
                - 1.0 / 16.0 * NC * pow(poly2, -1)
                - 2 * NC * pow(omz, -1)
                + 1.0 / 4.0 * NC * pow(omxmz, -1)
                + 71.0 / 48.0 * NC
                + 1.0 / 6.0 * NC * pow(pi, 2) * pow(omz, -1)
                + 1.0 / 4.0 * NC * pow(pi, 2)
                + 153.0 / 16.0 * NC * z
                + 1.0 / 12.0 * NC * z * pow(pi, 2)
                - 4 * NC * x * pow(z, -1) * pow(omz, -1)
                + 28.0 / 3.0 * NC * x * pow(z, -1)
                + 2.0 / 3.0 * NC * x * pow(z, -1) * pow(pi, 2) * pow(omz, -1)
                + 2.0 / 3.0 * NC * x * pow(z, -1) * pow(pi, 2)
                + 4 * NC * x * pow(omz, -1)
                - 3.0 / 4.0 * NC * x * pow(omxmz, -1)
                - 155.0 / 48.0 * NC * x
                - 1.0 / 3.0 * NC * x * pow(pi, 2) * pow(omz, -1)
                - 3 * NC * x * pow(pi, 2)
                - 11 * NC * x * z
                + 1.0 / 3.0 * NC * x * z * pow(pi, 2)
                + 4 * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - 161.0 / 18.0 * NC * pow(x, 2) * pow(z, -1)
                - 2.0 / 3.0 * NC * pow(x, 2) * pow(z, -1) * pow(pi, 2) * pow(omz, -1)
                - 4 * NC * pow(x, 2) * pow(omz, -1)
                + NC * pow(x, 2) * pow(omxmz, -1)
                + 1127.0 / 144.0 * NC * pow(x, 2)
                + 1.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2) * pow(omz, -1)
                + 5.0 / 3.0 * NC * pow(x, 2) * pow(pi, 2)
                + 3.0 / 2.0 * NC * pow(x, 2) * z
                + 1.0 / 6.0 * NC * pow(x, 2) * z * pow(pi, 2)
                - 1.0 / 16.0 * NC * pow(x, 3) * pow(poly2, -1)
                - 1.0 / 2.0 * NC * pow(x, 3) * pow(omxmz, -1)
                + 1.0 / 16.0 * NC * pow(x, 4) * pow(poly2, -1)
                + 11.0 / 12.0 * LMUR * NC * pow(z, -1)
                - 11.0 / 6.0 * LMUR * NC
                - 11.0 / 6.0 * LMUR * NC * x * pow(z, -1)
                + 11.0 / 3.0 * LMUR * NC * x
                + 11.0 / 6.0 * LMUR * NC * pow(x, 2) * pow(z, -1)
                - 11.0 / 3.0 * LMUR * NC * pow(x, 2)
                - 1.0 / 6.0 * LMUR * NF * pow(z, -1)
                + 1.0 / 3.0 * LMUR * NF
                + 1.0 / 3.0 * LMUR * NF * x * pow(z, -1)
                - 2.0 / 3.0 * LMUR * NF * x
                - 1.0 / 3.0 * LMUR * NF * pow(x, 2) * pow(z, -1)
                + 2.0 / 3.0 * LMUR * NF * pow(x, 2)
                + 1.0 / 2.0 * LMUF * pow(NC, -1) * z
                - 1.0 / 2.0 * LMUF * pow(NC, -1) * x
                + 3.0 / 4.0 * LMUF * pow(NC, -1) * pow(x, 2)
            )
            tmp += (
                -3.0 / 4.0 * LMUF * pow(NC, -1) * pow(x, 2) * z
                - 2.0 / 3.0 * LMUF * NC * pow(x, -1) * pow(z, -1)
                + 4.0 / 3.0 * LMUF * NC * pow(x, -1)
                - 17.0 / 12.0 * LMUF * NC * pow(z, -1)
                + 17.0 / 6.0 * LMUF * NC
                - 1.0 / 2.0 * LMUF * NC * z
                - 13.0 / 6.0 * LMUF * NC * x * pow(z, -1)
                + 29.0 / 6.0 * LMUF * NC * x
                + 10.0 / 3.0 * LMUF * NC * pow(x, 2) * pow(z, -1)
                - 89.0 / 12.0 * LMUF * NC * pow(x, 2)
                + 3.0 / 4.0 * LMUF * NC * pow(x, 2) * z
                + 1.0 / 6.0 * LMUF * NF * pow(z, -1)
                - 1.0 / 3.0 * LMUF * NF
                - 1.0 / 3.0 * LMUF * NF * x * pow(z, -1)
                + 2.0 / 3.0 * LMUF * NF * x
                + 1.0 / 3.0 * LMUF * NF * pow(x, 2) * pow(z, -1)
                - 2.0 / 3.0 * LMUF * NF * pow(x, 2)
                - 1.0 / 4.0 * LMUA * pow(NC, -1)
                - 1.0 / 8.0 * LMUA * pow(NC, -1) * z
                - 1.0 / 4.0 * LMUA * pow(NC, -1) * x * z
                + 1.0 / 4.0 * LMUA * pow(NC, -1) * pow(x, 2) * z
                + 1.0 / 4.0 * LMUA * NC
                + 1.0 / 8.0 * LMUA * NC * z
                + 1.0 / 4.0 * LMUA * NC * x * z
                - 1.0 / 4.0 * LMUA * NC * pow(x, 2) * z
                + 1.0 / 4.0 * LMUA * LMUF * pow(NC, -1)
                + 1.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * z
                - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * x
                - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * x * z
                + 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * pow(x, 2) * z
                - 1.0 / 4.0 * LMUA * LMUF * NC
                - 1.0 / 4.0 * LMUA * LMUF * NC * z
                + 1.0 / 2.0 * LMUA * LMUF * NC * x
                + 1.0 / 2.0 * LMUA * LMUF * NC * x * z
                - 1.0 / 2.0 * LMUA * LMUF * NC * pow(x, 2)
                - 1.0 / 2.0 * LMUA * LMUF * NC * pow(x, 2) * z
                - 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2)
                + 5.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1)
                - 1.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, -1)
                + 8 * ln(x) * pow(NC, -1) * pow(z, -1) * pow(omz, -1)
                - 53.0 / 8.0 * ln(x) * pow(NC, -1) * pow(z, -1)
                + 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(poly2, -1)
                - 13.0 / 2.0 * ln(x) * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(omxmz, -1)
                - 53.0 / 16.0 * ln(x) * pow(NC, -1)
            )
            tmp += (
                +3.0 / 8.0 * ln(x) * pow(NC, -1) * z
                - 16 * ln(x) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                + 69.0 / 4.0 * ln(x) * pow(NC, -1) * x * pow(z, -1)
                + 3.0 / 32.0 * ln(x) * pow(NC, -1) * x * pow(poly2, -2)
                - 15.0 / 16.0 * ln(x) * pow(NC, -1) * x * pow(poly2, -1)
                + 16 * ln(x) * pow(NC, -1) * x * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * x * pow(xmz, -1)
                - 1.0 / 4.0 * ln(x) * pow(NC, -1) * x * pow(omxmz, -2)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * x * pow(omxmz, -1)
                - 1.0 / 2.0 * ln(x) * pow(NC, -1) * x
                + 1.0 / 8.0 * ln(x) * pow(NC, -1) * x * z
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * x * pow(z, 3) * pow(xmz, -2)
                + 8 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - 13.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2)
                + 15.0 / 16.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1)
                - 5 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - ln(x) * pow(NC, -1) * pow(x, 2) * pow(xmz, -1)
                + 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -2)
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1)
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * z
                + 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2)
                + 9.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1)
                + 5.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(xmz, -1)
                - ln(x) * pow(NC, -1) * pow(x, 3) * pow(omxmz, -2)
                - 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2)
                - 11.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1)
                - 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(xmz, -2)
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(omxmz, -2)
                - 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(x) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(x) * NC * pow(x, -1) * pow(poly2, -2)
            )
            tmp += (
                +3.0 / 32.0 * ln(x) * NC * pow(x, -1) * pow(poly2, -1)
                - 3.0 / 16.0 * ln(x) * NC * pow(x, -1)
                - 8 * ln(x) * NC * pow(z, -1) * pow(omz, -1)
                + 61.0 / 8.0 * ln(x) * NC * pow(z, -1)
                - 3.0 / 32.0 * ln(x) * NC * pow(poly2, -2)
                - 5.0 / 32.0 * ln(x) * NC * pow(poly2, -1)
                + 13.0 / 2.0 * ln(x) * NC * pow(omz, -1)
                - 3.0 / 4.0 * ln(x) * NC * pow(omxmz, -1)
                + 1.0 / 16.0 * ln(x) * NC
                + 37.0 / 8.0 * ln(x) * NC * z
                + 16 * ln(x) * NC * x * pow(z, -1) * pow(omz, -1)
                - 69.0 / 4.0 * ln(x) * NC * x * pow(z, -1)
                - 3.0 / 32.0 * ln(x) * NC * x * pow(poly2, -2)
                + 23.0 / 16.0 * ln(x) * NC * x * pow(poly2, -1)
                - 16 * ln(x) * NC * x * pow(omz, -1)
                + 1.0 / 4.0 * ln(x) * NC * x * pow(omxmz, -2)
                + 2 * ln(x) * NC * x * pow(omxmz, -1)
                + 19.0 / 4.0 * ln(x) * NC * x
                + 39.0 / 8.0 * ln(x) * NC * x * z
                - 1.0 / 2.0 * ln(x) * NC * x * pow(z, 3) * pow(xmz, -2)
                - 16 * ln(x) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                + 30 * ln(x) * NC * pow(x, 2) * pow(z, -1)
                + 3.0 / 32.0 * ln(x) * NC * pow(x, 2) * pow(poly2, -2)
                - 23.0 / 16.0 * ln(x) * NC * pow(x, 2) * pow(poly2, -1)
                + 16 * ln(x) * NC * pow(x, 2) * pow(omz, -1)
                - 3.0 / 4.0 * ln(x) * NC * pow(x, 2) * pow(omxmz, -2)
                - 3.0 / 2.0 * ln(x) * NC * pow(x, 2) * pow(omxmz, -1)
                - 129.0 / 4.0 * ln(x) * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(x) * NC * pow(x, 2) * z
                - 3.0 / 32.0 * ln(x) * NC * pow(x, 3) * pow(poly2, -2)
                - 1.0 / 32.0 * ln(x) * NC * pow(x, 3) * pow(poly2, -1)
                - 3.0 / 2.0 * ln(x) * NC * pow(x, 3) * pow(xmz, -1)
                + ln(x) * NC * pow(x, 3) * pow(omxmz, -2)
                + ln(x) * NC * pow(x, 3) * pow(omxmz, -1)
                + 3.0 / 32.0 * ln(x) * NC * pow(x, 4) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(x) * NC * pow(x, 4) * pow(poly2, -1)
                + 1.0 / 2.0 * ln(x) * NC * pow(x, 4) * pow(xmz, -2)
                - 1.0 / 2.0 * ln(x) * NC * pow(x, 4) * pow(omxmz, -2)
                + 3.0 / 32.0 * ln(x) * NC * pow(x, 5) * pow(poly2, -2)
                - 3.0 / 32.0 * ln(x) * NC * pow(x, 6) * pow(poly2, -2)
                - 1.0 / 4.0 * ln(x) * LMUF * pow(NC, -1)
            )
            tmp += (
                +1.0 / 4.0 * ln(x) * LMUF * pow(NC, -1) * z
                - 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x
                + 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * z
                + 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * pow(x, 2) * z
                - ln(x) * LMUF * NC * pow(z, -1)
                + 9.0 / 4.0 * ln(x) * LMUF * NC
                - 1.0 / 4.0 * ln(x) * LMUF * NC * z
                - 4 * ln(x) * LMUF * NC * x * pow(z, -1)
                + 17.0 / 2.0 * ln(x) * LMUF * NC * x
                - 1.0 / 2.0 * ln(x) * LMUF * NC * x * z
                - 1.0 / 2.0 * ln(x) * LMUF * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * LMUF * NC * pow(x, 2) * z
                + 1.0 / 4.0 * ln(x) * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * ln(x) * LMUA * pow(NC, -1) * z
                - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * x
                - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * x * z
                + 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * pow(x, 2) * z
                - 1.0 / 4.0 * ln(x) * LMUA * NC
                - 1.0 / 4.0 * ln(x) * LMUA * NC * z
                + 1.0 / 2.0 * ln(x) * LMUA * NC * x
                + 1.0 / 2.0 * ln(x) * LMUA * NC * x * z
                - 1.0 / 2.0 * ln(x) * LMUA * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(x) * LMUA * NC * pow(x, 2) * z
                - 3.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(omz, -1)
                + 259.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                - 11.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                + 11.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                + 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 29.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                + 19.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 73.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                -5.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(z, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 9.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1)
                + 9.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * z * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(z, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(omz, -1)
                - 211.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1)
                + 51.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * z * pow(sqrtxz2, -1)
                - 51.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 2 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                - 2 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 129.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                + 129.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                - 23.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 193.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                +1.0 / 16.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                + 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(omz, -1)
                - 259.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                + 11.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                - 11.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                - 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 29.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
            )
            tmp += (
                +29.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                - 19.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 73.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 5.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(z, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 9.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1)
                - 9.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * z * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(z, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(omz, -1)
            )
            tmp += (
                +211.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1)
                - 51.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * z * pow(sqrtxz2, -1)
                + 51.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 2 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                + 2 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 129.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                - 129.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                + 23.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 193.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 16.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 2 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(z, -1)
                + 2 * ln(x) * ln(1 + x) * pow(NC, -1)
                - ln(x) * ln(1 + x) * pow(NC, -1) * z
                - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x * pow(z, -1)
                + 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x
                - 2 * ln(x) * ln(1 + x) * pow(NC, -1) * x * z
                - 2 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(x, 2)
                - 2 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(x, 2) * z
                - ln(x) * ln(1 + x) * NC
                + ln(x) * ln(1 + x) * NC * z
                - 2 * ln(x) * ln(1 + x) * NC * x
            )
            tmp += (
                +2 * ln(x) * ln(1 + x) * NC * x * z
                + 2 * ln(x) * ln(1 + x) * NC * pow(x, 2) * z
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * pow(omz, -1)
                - 7.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1)
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1)
                + 13.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1)
                + pow(ln(x), 2) * pow(NC, -1) * z
                + 6 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                + 11.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1)
                + 6 * pow(ln(x), 2) * pow(NC, -1) * x * pow(omz, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 5 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 7 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2)
                + 2 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z
                + 5.0 / 2.0 * pow(ln(x), 2) * NC * pow(z, -1) * pow(omz, -1)
                - 2 * pow(ln(x), 2) * NC * pow(z, -1)
                - 1.0 / 4.0 * pow(ln(x), 2) * NC * pow(omz, -1)
                - 5.0 / 4.0 * pow(ln(x), 2) * NC
                - pow(ln(x), 2) * NC * z
                - 5 * pow(ln(x), 2) * NC * x * pow(z, -1) * pow(omz, -1)
                - 2 * pow(ln(x), 2) * NC * x * pow(z, -1)
                + 1.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(omz, -1)
                + 33.0 / 2.0 * pow(ln(x), 2) * NC * x
                + 5 * pow(ln(x), 2) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - 2 * pow(ln(x), 2) * NC * pow(x, 2) * pow(z, -1)
                - 1.0 / 2.0 * pow(ln(x), 2) * NC * pow(x, 2) * pow(omz, -1)
                - 7 * pow(ln(x), 2) * NC * pow(x, 2)
                - 2 * pow(ln(x), 2) * NC * pow(x, 2) * z
                + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * pow(omz, -1)
                + 17.0 / 4.0 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1)
                + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1)
                - 4 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1)
            )
            tmp += (
                -8 * ln(x) * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                + 5 * ln(x) * ln(z) * pow(NC, -1) * x
                + ln(x) * ln(z) * pow(NC, -1) * x * z
                + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                + 6 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 6 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 7 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2)
                - 3 * ln(x) * ln(z) * NC * pow(z, -1) * pow(omz, -1)
                + 5.0 / 4.0 * ln(x) * ln(z) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(x) * ln(z) * NC * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * ln(z) * NC
                + 6 * ln(x) * ln(z) * NC * x * pow(z, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * ln(z) * NC * x * pow(z, -1)
                + ln(x) * ln(z) * NC * x * pow(omz, -1)
                - 11 * ln(x) * ln(z) * NC * x
                - ln(x) * ln(z) * NC * x * z
                - 6 * ln(x) * ln(z) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                + ln(x) * ln(z) * NC * pow(x, 2) * pow(z, -1)
                + ln(x) * ln(z) * NC * pow(x, 2) * pow(omz, -1)
                + 9 * ln(x) * ln(z) * NC * pow(x, 2)
                + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1)
                + 19.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                - 13.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1)
                - ln(x) * ln(omx) * pow(NC, -1) * z
                - 16 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                - 19 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                + 13 * ln(x) * ln(omx) * pow(NC, -1) * x
                + 2 * ln(x) * ln(omx) * pow(NC, -1) * x * z
                + 11 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 12 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 12 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2)
                - 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * z
                + 2 * ln(x) * ln(omx) * NC * pow(z, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(omx) * NC * pow(z, -1)
                - 7.0 / 2.0 * ln(x) * ln(omx) * NC * pow(omz, -1)
                + 11.0 / 2.0 * ln(x) * ln(omx) * NC
                + ln(x) * ln(omx) * NC * z
                - 4 * ln(x) * ln(omx) * NC * x * pow(z, -1) * pow(omz, -1)
            )
            tmp += (
                +8 * ln(x) * ln(omx) * NC * x * pow(z, -1)
                + 7 * ln(x) * ln(omx) * NC * x * pow(omz, -1)
                - 11 * ln(x) * ln(omx) * NC * x
                - 2 * ln(x) * ln(omx) * NC * x * z
                + 4 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                - 7 * ln(x) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                + 10 * ln(x) * ln(omx) * NC * pow(x, 2)
                + 2 * ln(x) * ln(omx) * NC * pow(x, 2) * z
                + 7 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1)
                + 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(x) * ln(omz) * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * z
                - 14 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                - 12 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                + 11 * ln(x) * ln(omz) * pow(NC, -1) * x
                + 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 9 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 11 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2)
                - ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                - 2 * ln(x) * ln(omz) * NC * pow(z, -1)
                - 3 * ln(x) * ln(omz) * NC * pow(omz, -1)
                + 4 * ln(x) * ln(omz) * NC
                + 1.0 / 2.0 * ln(x) * ln(omz) * NC * z
                + 10 * ln(x) * ln(omz) * NC * x * pow(z, -1)
                + 6 * ln(x) * ln(omz) * NC * x * pow(omz, -1)
                - 21 * ln(x) * ln(omz) * NC * x
                - 6 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                - 6 * ln(x) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                + 13 * ln(x) * ln(omz) * NC * pow(x, 2)
                + ln(x) * ln(omz) * NC * pow(x, 2) * z
                - 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2)
                + 5.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1)
                - 1.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, -1)
                - 4 * ln(z) * pow(NC, -1) * pow(z, -1) * pow(omz, -1)
                + 23.0 / 8.0 * ln(z) * pow(NC, -1) * pow(z, -1)
                - 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(poly2, -1)
            )
            tmp += (
                +7.0 / 2.0 * ln(z) * pow(NC, -1) * pow(omz, -1)
                + 27.0 / 16.0 * ln(z) * pow(NC, -1)
                - 3.0 / 4.0 * ln(z) * pow(NC, -1) * z
                + 8 * ln(z) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                - 15.0 / 2.0 * ln(z) * pow(NC, -1) * x * pow(z, -1)
                + 3.0 / 32.0 * ln(z) * pow(NC, -1) * x * pow(poly2, -2)
                - 15.0 / 16.0 * ln(z) * pow(NC, -1) * x * pow(poly2, -1)
                - 9 * ln(z) * pow(NC, -1) * x * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * pow(NC, -1) * x * pow(xmz, -1)
                - 11.0 / 8.0 * ln(z) * pow(NC, -1) * x
                + 17.0 / 8.0 * ln(z) * pow(NC, -1) * x * z
                - 1.0 / 2.0 * ln(z) * pow(NC, -1) * x * pow(z, 3) * pow(xmz, -2)
                - 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                + 3 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2)
                - 15.0 / 16.0 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1)
                + 3 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + ln(z) * pow(NC, -1) * pow(x, 2) * pow(xmz, -1)
                + 11.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 2)
                - ln(z) * pow(NC, -1) * pow(x, 2) * z
                + 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2)
                + 9.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1)
                - 5.0 / 2.0 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(xmz, -1)
                + 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2)
                + 11.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1)
                + 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(x, 4) * pow(xmz, -2)
                - 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2)
                - 3.0 / 32.0 * ln(z) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2)
                + 2.0 / 3.0 * ln(z) * NC * pow(x, -1) * pow(z, -1)
                + 3.0 / 32.0 * ln(z) * NC * pow(x, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(z) * NC * pow(x, -1) * pow(poly2, -1)
                + 2.0 / 3.0 * ln(z) * NC * pow(x, -1) * pow(omz, -1)
                - 73.0 / 48.0 * ln(z) * NC * pow(x, -1)
                + 4 * ln(z) * NC * pow(z, -1) * pow(omz, -1)
            )
            tmp += (
                -19.0 / 8.0 * ln(z) * NC * pow(z, -1)
                + 3.0 / 32.0 * ln(z) * NC * pow(poly2, -2)
                + 5.0 / 32.0 * ln(z) * NC * pow(poly2, -1)
                - 4 * ln(z) * NC * pow(omz, -1)
                - 63.0 / 16.0 * ln(z) * NC
                + 23.0 / 4.0 * ln(z) * NC * z
                - 8 * ln(z) * NC * x * pow(z, -1) * pow(omz, -1)
                + 23.0 / 2.0 * ln(z) * NC * x * pow(z, -1)
                - 3.0 / 32.0 * ln(z) * NC * x * pow(poly2, -2)
                + 23.0 / 16.0 * ln(z) * NC * x * pow(poly2, -1)
                + 13 * ln(z) * NC * x * pow(omz, -1)
                - 91.0 / 8.0 * ln(z) * NC * x
                - 57.0 / 8.0 * ln(z) * NC * x * z
                + 1.0 / 2.0 * ln(z) * NC * x * pow(z, 3) * pow(xmz, -2)
                + 8 * ln(z) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - 79.0 / 6.0 * ln(z) * NC * pow(x, 2) * pow(z, -1)
                - 3.0 / 32.0 * ln(z) * NC * pow(x, 2) * pow(poly2, -2)
                + 23.0 / 16.0 * ln(z) * NC * pow(x, 2) * pow(poly2, -1)
                - 38.0 / 3.0 * ln(z) * NC * pow(x, 2) * pow(omz, -1)
                + 77.0 / 6.0 * ln(z) * NC * pow(x, 2)
                + ln(z) * NC * pow(x, 2) * z
                - 3.0 / 32.0 * ln(z) * NC * pow(x, 3) * pow(poly2, -2)
                - 1.0 / 32.0 * ln(z) * NC * pow(x, 3) * pow(poly2, -1)
                + 3.0 / 2.0 * ln(z) * NC * pow(x, 3) * pow(xmz, -1)
                - 3.0 / 32.0 * ln(z) * NC * pow(x, 4) * pow(poly2, -2)
                - 3.0 / 32.0 * ln(z) * NC * pow(x, 4) * pow(poly2, -1)
                - 1.0 / 2.0 * ln(z) * NC * pow(x, 4) * pow(xmz, -2)
                + 3.0 / 32.0 * ln(z) * NC * pow(x, 5) * pow(poly2, -2)
                + 3.0 / 32.0 * ln(z) * NC * pow(x, 6) * pow(poly2, -2)
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 4.0 * ln(z) * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(z) * LMUF * pow(NC, -1) * z
                - ln(z) * LMUF * pow(NC, -1) * x * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * x
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * x * z
                + ln(z) * LMUF * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * pow(x, 2) * z
                - 1.0 / 2.0 * ln(z) * LMUF * NC * pow(omz, -1)
                + 1.0 / 4.0 * ln(z) * LMUF * NC
                + 1.0 / 4.0 * ln(z) * LMUF * NC * z
            )
            tmp += (
                +ln(z) * LMUF * NC * x * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * LMUF * NC * x
                - 1.0 / 2.0 * ln(z) * LMUF * NC * x * z
                - ln(z) * LMUF * NC * pow(x, 2) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * LMUF * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(z) * LMUF * NC * pow(x, 2) * z
                - 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 4.0 * ln(z) * LMUA * pow(NC, -1)
                + 1.0 / 4.0 * ln(z) * LMUA * pow(NC, -1) * z
                + ln(z) * LMUA * pow(NC, -1) * x * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * x
                - 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * x * z
                - ln(z) * LMUA * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * pow(x, 2) * z
                + 1.0 / 2.0 * ln(z) * LMUA * NC * pow(omz, -1)
                - 3.0 / 4.0 * ln(z) * LMUA * NC
                - 1.0 / 4.0 * ln(z) * LMUA * NC * z
                - ln(z) * LMUA * NC * x * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * LMUA * NC * x
                + 1.0 / 2.0 * ln(z) * LMUA * NC * x * z
                + ln(z) * LMUA * NC * pow(x, 2) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * LMUA * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(z) * LMUA * NC * pow(x, 2) * z
                - 5.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1)
                - pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * pow(NC, -1) * z
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1)
                + 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * z
                - 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * z
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(z, -1) * pow(omz, -1)
                + 1.0 / 4.0 * pow(ln(z), 2) * NC * pow(z, -1)
                - 1.0 / 4.0 * pow(ln(z), 2) * NC * pow(omz, -1)
            )
            tmp += (
                -1.0 / 2.0 * pow(ln(z), 2) * NC
                + 1.0 / 4.0 * pow(ln(z), 2) * NC * z
                - pow(ln(z), 2) * NC * x * pow(z, -1) * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(z, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(omz, -1)
                + pow(ln(z), 2) * NC * x
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * x * z
                + pow(ln(z), 2) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * pow(z, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * pow(omz, -1)
                - pow(ln(z), 2) * NC * pow(x, 2)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * pow(x, 2) * z
                - 7.0 / 2.0 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1)
                - 4 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * pow(NC, -1)
                + 7 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * pow(NC, -1) * x
                - 5 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 5 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 3.0 / 2.0 * ln(z) * ln(omx) * NC * pow(z, -1)
                + 3.0 / 2.0 * ln(z) * ln(omx) * NC * pow(omz, -1)
                - 5.0 / 2.0 * ln(z) * ln(omx) * NC
                - 3 * ln(z) * ln(omx) * NC * x * pow(z, -1)
                - 3 * ln(z) * ln(omx) * NC * x * pow(omz, -1)
                + 5 * ln(z) * ln(omx) * NC * x
                + 3 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                + 3 * ln(z) * ln(omx) * NC * pow(x, 2) * pow(omz, -1)
                - 5 * ln(z) * ln(omx) * NC * pow(x, 2)
                - 3 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1)
                - 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1)
                + 6 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                - 7 * ln(z) * ln(omz) * pow(NC, -1) * x
                - 5 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 5 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                +7 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(z, -1)
                + 5.0 / 2.0 * ln(z) * ln(omz) * NC * pow(omz, -1)
                - 11.0 / 2.0 * ln(z) * ln(omz) * NC
                - 5 * ln(z) * ln(omz) * NC * x * pow(z, -1)
                - 5 * ln(z) * ln(omz) * NC * x * pow(omz, -1)
                + 11 * ln(z) * ln(omz) * NC * x
                + 5 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 5 * ln(z) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                - 11 * ln(z) * ln(omz) * NC * pow(x, 2)
                - 1.0 / 4.0 * ln(omx) * pow(NC, -1) * pow(z, -1)
                - ln(omx) * pow(NC, -1) * pow(omz, -1)
                + 7.0 / 4.0 * ln(omx) * pow(NC, -1)
                - 3.0 / 8.0 * ln(omx) * pow(NC, -1) * z
                - 3.0 / 2.0 * ln(omx) * pow(NC, -1) * x * pow(z, -1)
                + 3.0 / 2.0 * ln(omx) * pow(NC, -1) * x
                + 1.0 / 4.0 * ln(omx) * pow(NC, -1) * x * z
                - 1.0 / 2.0 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 2 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 11.0 / 4.0 * ln(omx) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(omx) * pow(NC, -1) * pow(x, 2) * z
                + 2.0 / 3.0 * ln(omx) * NC * pow(x, -1) * pow(z, -1)
                - 4.0 / 3.0 * ln(omx) * NC * pow(x, -1)
                + 1.0 / 4.0 * ln(omx) * NC * pow(z, -1)
                + 1.0 / 2.0 * ln(omx) * NC * pow(omz, -1)
                - 5.0 / 4.0 * ln(omx) * NC
                + 3.0 / 8.0 * ln(omx) * NC * z
                + 11.0 / 2.0 * ln(omx) * NC * x * pow(z, -1)
                - 27.0 / 2.0 * ln(omx) * NC * x
                - 1.0 / 4.0 * ln(omx) * NC * x * z
                - 20.0 / 3.0 * ln(omx) * NC * pow(x, 2) * pow(z, -1)
                + 193.0 / 12.0 * ln(omx) * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(omx) * NC * pow(x, 2) * z
                - 1.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1) * z
                + 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * x
                + 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * x * z
                - 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * pow(x, 2) * z
                - ln(omx) * LMUF * NC * pow(z, -1)
                + 9.0 / 4.0 * ln(omx) * LMUF * NC
                + 1.0 / 4.0 * ln(omx) * LMUF * NC * z
            )
            tmp += (
                +2 * ln(omx) * LMUF * NC * x * pow(z, -1)
                - 9.0 / 2.0 * ln(omx) * LMUF * NC * x
                - 1.0 / 2.0 * ln(omx) * LMUF * NC * x * z
                - 2 * ln(omx) * LMUF * NC * pow(x, 2) * pow(z, -1)
                + 9.0 / 2.0 * ln(omx) * LMUF * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(omx) * LMUF * NC * pow(x, 2) * z
                - 1.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1)
                - 1.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1) * z
                + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * x
                + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * x * z
                - 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * pow(x, 2) * z
                + 1.0 / 4.0 * ln(omx) * LMUA * NC
                + 1.0 / 4.0 * ln(omx) * LMUA * NC * z
                - 1.0 / 2.0 * ln(omx) * LMUA * NC * x
                - 1.0 / 2.0 * ln(omx) * LMUA * NC * x * z
                + 1.0 / 2.0 * ln(omx) * LMUA * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(omx) * LMUA * NC * pow(x, 2) * z
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1)
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1)
                + 9.0 / 4.0 * pow(ln(omx), 2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * pow(NC, -1) * z
                + 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1)
                + 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(omz, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x
                - 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * z
                - 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 4 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) * z
                + 3.0 / 4.0 * pow(ln(omx), 2) * NC * pow(z, -1)
                + 1.0 / 4.0 * pow(ln(omx), 2) * NC * pow(omz, -1)
                - 7.0 / 4.0 * pow(ln(omx), 2) * NC
                - 1.0 / 4.0 * pow(ln(omx), 2) * NC * z
                - 3.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(z, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(omz, -1)
                + 7.0 / 2.0 * pow(ln(omx), 2) * NC * x
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * z
                + 3.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                +1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2)
                - 1.0 / 2.0 * pow(ln(omx), 2) * NC * pow(x, 2) * z
                - 9.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1)
                - 4 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * ln(omz) * pow(NC, -1) * z
                + 9 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 8 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(omz, -1)
                - 8 * ln(omx) * ln(omz) * pow(NC, -1) * x
                - ln(omx) * ln(omz) * pow(NC, -1) * x * z
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 8 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2)
                + ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                + 2 * ln(omx) * ln(omz) * NC * pow(z, -1)
                + ln(omx) * ln(omz) * NC * pow(omz, -1)
                - 9.0 / 2.0 * ln(omx) * ln(omz) * NC
                - 1.0 / 2.0 * ln(omx) * ln(omz) * NC * z
                - 4 * ln(omx) * ln(omz) * NC * x * pow(z, -1)
                - 2 * ln(omx) * ln(omz) * NC * x * pow(omz, -1)
                + 9 * ln(omx) * ln(omz) * NC * x
                + ln(omx) * ln(omz) * NC * x * z
                + 4 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 2 * ln(omx) * ln(omz) * NC * pow(x, 2) * pow(omz, -1)
                - 9 * ln(omx) * ln(omz) * NC * pow(x, 2)
                - ln(omx) * ln(omz) * NC * pow(x, 2) * z
                + 1.0 / 4.0 * ln(omz) * pow(NC, -1) * pow(z, -1)
                - ln(omz) * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 4.0 * ln(omz) * pow(NC, -1) * pow(omxmz, -1)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1)
                - 3.0 / 8.0 * ln(omz) * pow(NC, -1) * z
                - 3.0 / 2.0 * ln(omz) * pow(NC, -1) * x * pow(z, -1)
                + 1.0 / 4.0 * ln(omz) * pow(NC, -1) * x * pow(omxmz, -2)
                + 3.0 / 2.0 * ln(omz) * pow(NC, -1) * x * pow(omxmz, -1)
                + 3 * ln(omz) * pow(NC, -1) * x
                + 1.0 / 4.0 * ln(omz) * pow(NC, -1) * x * z
                - 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
            )
            tmp += (
                -ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - 3.0 / 4.0 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -2)
                - 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1)
                - 13.0 / 4.0 * ln(omz) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 2) * z
                + ln(omz) * pow(NC, -1) * pow(x, 3) * pow(omxmz, -2)
                - 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 4) * pow(omxmz, -2)
                + 2.0 / 3.0 * ln(omz) * NC * pow(x, -1) * pow(z, -1)
                - 4.0 / 3.0 * ln(omz) * NC * pow(x, -1)
                + 3.0 / 4.0 * ln(omz) * NC * pow(z, -1)
                + ln(omz) * NC * pow(omz, -1)
                + 3.0 / 4.0 * ln(omz) * NC * pow(omxmz, -1)
                - 7.0 / 2.0 * ln(omz) * NC
                + 3.0 / 8.0 * ln(omz) * NC * z
                + 11.0 / 2.0 * ln(omz) * NC * x * pow(z, -1)
                - 1.0 / 4.0 * ln(omz) * NC * x * pow(omxmz, -2)
                - 2 * ln(omz) * NC * x * pow(omxmz, -1)
                - 14 * ln(omz) * NC * x
                - 1.0 / 4.0 * ln(omz) * NC * x * z
                - 20.0 / 3.0 * ln(omz) * NC * pow(x, 2) * pow(z, -1)
                + 3.0 / 4.0 * ln(omz) * NC * pow(x, 2) * pow(omxmz, -2)
                + 3.0 / 2.0 * ln(omz) * NC * pow(x, 2) * pow(omxmz, -1)
                + 199.0 / 12.0 * ln(omz) * NC * pow(x, 2)
                - 1.0 / 2.0 * ln(omz) * NC * pow(x, 2) * z
                - ln(omz) * NC * pow(x, 3) * pow(omxmz, -2)
                - ln(omz) * NC * pow(x, 3) * pow(omxmz, -1)
                + 1.0 / 2.0 * ln(omz) * NC * pow(x, 4) * pow(omxmz, -2)
                - 1.0 / 4.0 * ln(omz) * LMUF * pow(NC, -1)
                - 1.0 / 4.0 * ln(omz) * LMUF * pow(NC, -1) * z
                + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * x
                + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * x * z
                - 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * pow(x, 2) * z
                + 1.0 / 4.0 * ln(omz) * LMUF * NC
                + 1.0 / 4.0 * ln(omz) * LMUF * NC * z
                - 1.0 / 2.0 * ln(omz) * LMUF * NC * x
                - 1.0 / 2.0 * ln(omz) * LMUF * NC * x * z
                + 1.0 / 2.0 * ln(omz) * LMUF * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * LMUF * NC * pow(x, 2) * z
                + 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * pow(z, -1)
                - 5.0 / 4.0 * ln(omz) * LMUA * pow(NC, -1)
            )
            tmp += (
                -1.0 / 4.0 * ln(omz) * LMUA * pow(NC, -1) * z
                - ln(omz) * LMUA * pow(NC, -1) * x * pow(z, -1)
                + 5.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * x
                + 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * x * z
                + ln(omz) * LMUA * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 5.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * pow(x, 2)
                - 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * pow(x, 2) * z
                - 1.0 / 2.0 * ln(omz) * LMUA * NC * pow(z, -1)
                + 5.0 / 4.0 * ln(omz) * LMUA * NC
                + 1.0 / 4.0 * ln(omz) * LMUA * NC * z
                + ln(omz) * LMUA * NC * x * pow(z, -1)
                - 5.0 / 2.0 * ln(omz) * LMUA * NC * x
                - 1.0 / 2.0 * ln(omz) * LMUA * NC * x * z
                - ln(omz) * LMUA * NC * pow(x, 2) * pow(z, -1)
                + 5.0 / 2.0 * ln(omz) * LMUA * NC * pow(x, 2)
                + 1.0 / 2.0 * ln(omz) * LMUA * NC * pow(x, 2) * z
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1)
                + 2 * pow(ln(omz), 2) * pow(NC, -1)
                + 1.0 / 4.0 * pow(ln(omz), 2) * pow(NC, -1) * z
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1)
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(omz, -1)
                - 4 * pow(ln(omz), 2) * pow(NC, -1) * x
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * z
                - 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * z
                + 5.0 / 4.0 * pow(ln(omz), 2) * NC * pow(z, -1)
                + pow(ln(omz), 2) * NC * pow(omz, -1)
                - 11.0 / 4.0 * pow(ln(omz), 2) * NC
                - 1.0 / 4.0 * pow(ln(omz), 2) * NC * z
                - 5.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(z, -1)
                - 2 * pow(ln(omz), 2) * NC * x * pow(omz, -1)
                + 11.0 / 2.0 * pow(ln(omz), 2) * NC * x
                + 1.0 / 2.0 * pow(ln(omz), 2) * NC * x * z
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(z, -1)
                + 2 * pow(ln(omz), 2) * NC * pow(x, 2) * pow(omz, -1)
            )
            tmp += (
                -11.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2)
                - 1.0 / 2.0 * pow(ln(omz), 2) * NC * pow(x, 2) * z
                - 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(omz, -1)
                + 259.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                - 11.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                + 11.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
            )
            tmp += (
                -3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 29.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                + 19.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 73.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                -5.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(z, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 9.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1)
                + 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * z * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(z, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(omz, -1)
                - 211.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1)
                + 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * z * pow(sqrtxz2, -1)
                - 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 129.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1)
            )
            tmp += (
                +129.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                - 23.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 193.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(omz, -1)
                - 259.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                + 11.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                - 11.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 29.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                - 19.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 73.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 5.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(z, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 9.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1)
                - 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * z * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(z, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(omz, -1)
                + 211.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1)
                - 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * z * pow(sqrtxz2, -1)
                + 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 129.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                - 129.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                + 23.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 193.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(omz, -1)
                - 259.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                + 11.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                - 11.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
            )
            tmp += (
                -29.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                + 29.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                - 19.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 73.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 5.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(z, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                + 9.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1)
                - 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * z * pow(sqrtxz2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(z, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(omz, -1)
                + 211.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1)
                - 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * z * pow(sqrtxz2, -1)
                + 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 129.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                - 129.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                + 23.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 193.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 16.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                +3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * z * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(omz, -1)
                + 259.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1)
                - 11.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1)
                + 11.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 29.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1)
                - 29.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1)
            )
            tmp += (
                -Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                + 19.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 73.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 5.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, -1) * pow(sqrtxz2, -1)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(z, -1) * pow(sqrtxz2, -1)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1) * pow(omz, -1)
                - 9.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(sqrtxz2, -1)
                + 9.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * z * pow(sqrtxz2, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(z, -1) * pow(sqrtxz2, -1)
                - 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 5.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1) * pow(omz, -1)
                - 211.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(sqrtxz2, -1)
                + 51.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * z * pow(sqrtxz2, -1)
                - 51.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 129.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * pow(sqrtxz2, -1)
                + 129.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(z, -1) * pow(sqrtxz2, -1)
                - 23.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 193.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 3) * pow(sqrtxz2, -1)
                + 3.0 / 32.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 16.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 64.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * pow(omz, -1)
                - 3.0 / 2.0 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1)
                - 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * pow(NC, -1)
            )
            tmp += (
                -4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * pow(omz, -1)
                + 3 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1)
                + Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * pow(omz, -1)
                + Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x
                + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(x, 2)
                - Li2(1 - x * pow(z, -1)) * NC * pow(z, -1) * pow(omz, -1)
                + 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(1 - x * pow(z, -1)) * NC * pow(omz, -1)
                + 3.0 / 2.0 * Li2(1 - x * pow(z, -1)) * NC
                + 2 * Li2(1 - x * pow(z, -1)) * NC * x * pow(z, -1) * pow(omz, -1)
                - Li2(1 - x * pow(z, -1)) * NC * x * pow(z, -1)
                - Li2(1 - x * pow(z, -1)) * NC * x * pow(omz, -1)
                - 3 * Li2(1 - x * pow(z, -1)) * NC * x
                - 2 * Li2(1 - x * pow(z, -1)) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                + Li2(1 - x * pow(z, -1)) * NC * pow(x, 2) * pow(z, -1)
                + Li2(1 - x * pow(z, -1)) * NC * pow(x, 2) * pow(omz, -1)
                + 3 * Li2(1 - x * pow(z, -1)) * NC * pow(x, 2)
                - 2 * Li2(-x) * pow(NC, -1) * pow(z, -1)
                + 2 * Li2(-x) * pow(NC, -1)
                - Li2(-x) * pow(NC, -1) * z
                - 4 * Li2(-x) * pow(NC, -1) * x * pow(z, -1)
                + 4 * Li2(-x) * pow(NC, -1) * x
                - 2 * Li2(-x) * pow(NC, -1) * x * z
                - 2 * Li2(-x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * Li2(-x) * pow(NC, -1) * pow(x, 2)
                - 2 * Li2(-x) * pow(NC, -1) * pow(x, 2) * z
                - Li2(-x) * NC
                + Li2(-x) * NC * z
                - 2 * Li2(-x) * NC * x
                + 2 * Li2(-x) * NC * x * z
                + 2 * Li2(-x) * NC * pow(x, 2) * z
                + 1.0 / 2.0 * Li2(x) * pow(NC, -1) * pow(z, -1)
                + 2 * Li2(x) * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -3.0 / 2.0 * Li2(x) * pow(NC, -1)
                - 1.0 / 2.0 * Li2(x) * pow(NC, -1) * z
                - Li2(x) * pow(NC, -1) * x * pow(z, -1)
                - 4 * Li2(x) * pow(NC, -1) * x * pow(omz, -1)
                + 2 * Li2(x) * pow(NC, -1) * x
                + 2 * Li2(x) * pow(NC, -1) * x * z
                + Li2(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                + 2 * Li2(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                - Li2(x) * pow(NC, -1) * pow(x, 2)
                - Li2(x) * pow(NC, -1) * pow(x, 2) * z
                + 2 * Li2(x) * NC * pow(z, -1) * pow(omz, -1)
                - 5.0 / 2.0 * Li2(x) * NC * pow(z, -1)
                - 2 * Li2(x) * NC * pow(omz, -1)
                + 5.0 / 2.0 * Li2(x) * NC
                + 1.0 / 2.0 * Li2(x) * NC * z
                - 4 * Li2(x) * NC * x * pow(z, -1) * pow(omz, -1)
                - Li2(x) * NC * x * pow(z, -1)
                + 4 * Li2(x) * NC * x * pow(omz, -1)
                + 8 * Li2(x) * NC * x
                - 2 * Li2(x) * NC * x * z
                + 4 * Li2(x) * NC * pow(x, 2) * pow(z, -1) * pow(omz, -1)
                - 3 * Li2(x) * NC * pow(x, 2) * pow(z, -1)
                - 4 * Li2(x) * NC * pow(x, 2) * pow(omz, -1)
                - Li2(x) * NC * pow(x, 2)
                + Li2(x) * NC * pow(x, 2) * z
                - Li2(z) * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(z) * pow(NC, -1)
                + 2 * Li2(z) * pow(NC, -1) * x * pow(omz, -1)
                - 4 * Li2(z) * pow(NC, -1) * x
                - Li2(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1)
                - Li2(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1)
                + 4 * Li2(z) * pow(NC, -1) * pow(x, 2)
                + 1.0 / 2.0 * Li2(z) * NC * pow(z, -1)
                + 1.0 / 2.0 * Li2(z) * NC * pow(omz, -1)
                - 2 * Li2(z) * NC
                - Li2(z) * NC * x * pow(z, -1)
                - Li2(z) * NC * x * pow(omz, -1)
                + 4 * Li2(z) * NC * x
                + Li2(z) * NC * pow(x, 2) * pow(z, -1)
                + Li2(z) * NC * pow(x, 2) * pow(omz, -1)
                - 4 * Li2(z) * NC * pow(x, 2)
            )

            res += tmp

        return res


def c2tg2q_eq(x, z, rsl, order, f=C2Tg2qEq_DR0123_scheme):
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
