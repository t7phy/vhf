from configs.eh import *


def C2Pq2gEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
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
        res = (
            1169.0 / 54.0 * pow(z, -1) * CF * NC
            + 4.0 / 3.0 * pow(z, -1) * CF * NC * pow(rln2, 3)
            - 9.0 / 2.0 * pow(z, -1) * LMUA * CF * pow(NC, -1)
            + 55.0 / 18.0 * pow(z, -1) * LMUA * CF * NC
            + 2.0 / 3.0 * pow(z, -1) * LMUA * LMUR * CF * NF
            - 11.0 / 3.0 * pow(z, -1) * LMUA * LMUR * CF * NC
            - 3.0 / 2.0 * pow(z, -1) * LMUA * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * pow(z, -1) * LMUA * LMUF * CF * NC
            - 2.0 / 3.0 * pow(z, -1) * pow(LMUA, 2) * CF * NF
            - 3.0 / 2.0 * pow(z, -1) * pow(LMUA, 2) * CF * NC
            + 3 * CF * pow(NC, -1)
            - 295.0 / 18.0 * CF * NC
            + 4.0 / 3.0 * CF * NC * pow(rln2, 3)
            + 17.0 / 4.0 * LMUA * CF * pow(NC, -1)
            - 95.0 / 12.0 * LMUA * CF * NC
            - 2.0 / 3.0 * LMUA * LMUR * CF * NF
            + 11.0 / 3.0 * LMUA * LMUR * CF * NC
            + 3.0 / 2.0 * LMUA * LMUF * CF * pow(NC, -1)
            - 3.0 / 2.0 * LMUA * LMUF * CF * NC
            - 1.0 / 2.0 * pow(LMUA, 2) * CF * pow(NC, -1)
            + 2.0 / 3.0 * pow(LMUA, 2) * CF * NF
            + 5.0 / 6.0 * pow(LMUA, 2) * CF * NC
            + 13.0 / 8.0 * z * CF * pow(NC, -1)
            - 389.0 / 72.0 * z * CF * NC
            + 2.0 / 3.0 * z * CF * NC * pow(rln2, 3)
            - 1.0 / 3.0 * z * LMUR * CF * NF
            + 11.0 / 6.0 * z * LMUR * CF * NC
            + 3.0 / 4.0 * z * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * z * LMUF * CF * NC
            - 7.0 / 4.0 * z * LMUA * CF * pow(NC, -1)
            + 1.0 / 3.0 * z * LMUA * CF * NF
            + 31.0 / 12.0 * z * LMUA * CF * NC
            + 1.0 / 3.0 * z * LMUA * LMUR * CF * NF
            - 11.0 / 6.0 * z * LMUA * LMUR * CF * NC
            - 3.0 / 4.0 * z * LMUA * LMUF * CF * pow(NC, -1)
            + 3.0 / 4.0 * z * LMUA * LMUF * CF * NC
            + 1.0 / 8.0 * z * pow(LMUA, 2) * CF * pow(NC, -1)
            - 1.0 / 3.0 * z * pow(LMUA, 2) * CF * NF
            + 53.0 / 24.0 * z * pow(LMUA, 2) * CF * NC
            - 269.0 / 54.0 * pow(z, 2) * CF * NC
            + 13.0 / 9.0 * pow(z, 2) * LMUA * CF * NC
            + 2.0 / 3.0 * pow(z, 2) * pow(LMUA, 2) * CF * NC
            - 5 * zeta3 * pow(z, -1) * CF * pow(NC, -1)
            - 14 * zeta3 * pow(z, -1) * CF * NC
            + 3 * zeta3 * CF * pow(NC, -1)
            - 3.0 / 2.0 * zeta3 * z * CF * pow(NC, -1)
            - 12 * zeta3 * z * CF * NC
            - 1.0 / 4.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
            - 1.0 / 4.0 * pow(pi, 2) * pow(z, -1) * CF * NC
        )
        res += (
            -2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * NC * rln2
            - 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * LMUF * CF * pow(NC, -1)
            + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * LMUF * CF * NC
            - 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * LMUA * CF * pow(NC, -1)
            + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * LMUA * CF * NC
            + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1)
            - 5.0 / 3.0 * pow(pi, 2) * CF * NC
            - 2.0 / 3.0 * pow(pi, 2) * CF * NC * rln2
            + 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
            - 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * NC
            + 1.0 / 2.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * LMUA * CF * NC
            - 1.0 / 8.0 * pow(pi, 2) * z * CF * pow(NC, -1)
            + 7.0 / 24.0 * pow(pi, 2) * z * CF * NC
            - 1.0 / 3.0 * pow(pi, 2) * z * CF * NC * rln2
            - 1.0 / 6.0 * pow(pi, 2) * z * LMUF * CF * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * z * LMUF * CF * NC
            - 1.0 / 4.0 * pow(pi, 2) * z * LMUA * CF * pow(NC, -1)
            + 7.0 / 12.0 * pow(pi, 2) * z * LMUA * CF * NC
            - 2 * ln(1 + z) * pow(z, -1) * CF * NC * pow(rln2, 2)
            - 2 * ln(1 + z) * CF * NC * pow(rln2, 2)
            - ln(1 + z) * z * CF * NC * pow(rln2, 2)
            + 1.0 / 3.0 * ln(1 + z) * pow(pi, 2) * pow(z, -1) * CF * NC
            + 1.0 / 3.0 * ln(1 + z) * pow(pi, 2) * CF * NC
            + 1.0 / 6.0 * ln(1 + z) * pow(pi, 2) * z * CF * NC
            + 9.0 / 2.0 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
            + 71.0 / 18.0 * ln(z) * pow(z, -1) * CF * NC
            - 2.0 / 3.0 * ln(z) * pow(z, -1) * LMUR * CF * NF
            + 11.0 / 3.0 * ln(z) * pow(z, -1) * LMUR * CF * NC
            + 3.0 / 2.0 * ln(z) * pow(z, -1) * LMUF * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(z) * pow(z, -1) * LMUF * CF * NC
            + 2.0 / 3.0 * ln(z) * pow(z, -1) * LMUA * CF * NF
            + 29.0 / 3.0 * ln(z) * pow(z, -1) * LMUA * CF * NC
            - 2 * ln(z) * pow(z, -1) * pow(LMUA, 2) * CF * NC
            - 67.0 / 8.0 * ln(z) * CF * pow(NC, -1)
            + 247.0 / 8.0 * ln(z) * CF * NC
            + 2.0 / 3.0 * ln(z) * LMUR * CF * NF
            - 11.0 / 3.0 * ln(z) * LMUR * CF * NC
            - 3.0 / 2.0 * ln(z) * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * ln(z) * LMUF * CF * NC
            - 3.0 / 2.0 * ln(z) * LMUA * CF * pow(NC, -1)
        )
        res += (
            -2.0 / 3.0 * ln(z) * LMUA * CF * NF
            + 19.0 / 6.0 * ln(z) * LMUA * CF * NC
            - 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF * NC
            + 45.0 / 8.0 * ln(z) * z * CF * pow(NC, -1)
            + 31.0 / 8.0 * ln(z) * z * CF * NC
            - 1.0 / 3.0 * ln(z) * z * LMUR * CF * NF
            + 11.0 / 6.0 * ln(z) * z * LMUR * CF * NC
            + 3.0 / 4.0 * ln(z) * z * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * ln(z) * z * LMUF * CF * NC
            + 3.0 / 4.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
            + 1.0 / 3.0 * ln(z) * z * LMUA * CF * NF
            - 55.0 / 12.0 * ln(z) * z * LMUA * CF * NC
            + 1.0 / 4.0 * ln(z) * z * pow(LMUA, 2) * CF * pow(NC, -1)
            - 9.0 / 4.0 * ln(z) * z * pow(LMUA, 2) * CF * NC
            + 31.0 / 9.0 * ln(z) * pow(z, 2) * CF * NC
            - 4.0 / 3.0 * ln(z) * pow(z, 2) * LMUA * CF * NC
            + 1.0 / 3.0 * ln(z) * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
            - ln(z) * pow(pi, 2) * pow(z, -1) * CF * NC
            - 1.0 / 2.0 * ln(z) * pow(pi, 2) * CF * pow(NC, -1)
            - 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF * NC
            + 1.0 / 4.0 * ln(z) * pow(pi, 2) * z * CF * pow(NC, -1)
            - 11.0 / 12.0 * ln(z) * pow(pi, 2) * z * CF * NC
            - 4 * ln(z) * ln(1 + z) * pow(z, -1) * LMUA * CF * NC
            - 4 * ln(z) * ln(1 + z) * LMUA * CF * NC
            + ln(z) * ln(1 + z) * z * CF * NC
            - 2 * ln(z) * ln(1 + z) * z * LMUA * CF * NC
            - 20.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF * NC
            + 6 * pow(ln(z), 2) * pow(z, -1) * LMUA * CF * NC
            + pow(ln(z), 2) * CF * pow(NC, -1)
            - 5 * pow(ln(z), 2) * CF * NC
            + pow(ln(z), 2) * LMUA * CF * pow(NC, -1)
            + 3 * pow(ln(z), 2) * LMUA * CF * NC
            - 13.0 / 16.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
            - 7.0 / 16.0 * pow(ln(z), 2) * z * CF * NC
            - 1.0 / 2.0 * pow(ln(z), 2) * z * LMUA * CF * pow(NC, -1)
            + 11.0 / 2.0 * pow(ln(z), 2) * z * LMUA * CF * NC
            + 3 * pow(ln(z), 2) * ln(1 + z) * pow(z, -1) * CF * NC
            + 3 * pow(ln(z), 2) * ln(1 + z) * CF * NC
            + 3.0 / 2.0 * pow(ln(z), 2) * ln(1 + z) * z * CF * NC
            - 10.0 / 3.0 * pow(ln(z), 3) * pow(z, -1) * CF * NC
            - 5.0 / 12.0 * pow(ln(z), 3) * CF * pow(NC, -1)
        )
        res += (
            -5.0 / 4.0 * pow(ln(z), 3) * CF * NC
            + 5.0 / 24.0 * pow(ln(z), 3) * z * CF * pow(NC, -1)
            - 65.0 / 24.0 * pow(ln(z), 3) * z * CF * NC
            + 2 * pow(ln(z), 2) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
            + pow(ln(z), 2) * ln(omz) * pow(z, -1) * CF * NC
            - 2 * pow(ln(z), 2) * ln(omz) * CF * pow(NC, -1)
            - pow(ln(z), 2) * ln(omz) * CF * NC
            + pow(ln(z), 2) * ln(omz) * z * CF * pow(NC, -1)
            + 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * z * CF * NC
            - 2 * ln(z) * ln(omz) * pow(z, -1) * LMUA * CF * pow(NC, -1)
            - 6 * ln(z) * ln(omz) * pow(z, -1) * LMUA * CF * NC
            + 2 * ln(z) * ln(omz) * LMUA * CF * pow(NC, -1)
            + 6 * ln(z) * ln(omz) * LMUA * CF * NC
            + 3 * ln(z) * ln(omz) * z * CF * NC
            - ln(z) * ln(omz) * z * LMUA * CF * pow(NC, -1)
            - 3 * ln(z) * ln(omz) * z * LMUA * CF * NC
            + 4 * ln(z) * ln(omz) * ln(1 + z) * pow(z, -1) * CF * NC
            + 4 * ln(z) * ln(omz) * ln(1 + z) * CF * NC
            + 2 * ln(z) * ln(omz) * ln(1 + z) * z * CF * NC
            + 3 * ln(z) * pow(ln(omz), 2) * pow(z, -1) * CF * NC
            + 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF * pow(NC, -1)
            + 15.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF * NC
            - 3.0 / 4.0 * ln(z) * pow(ln(omz), 2) * z * CF * pow(NC, -1)
            + 21.0 / 4.0 * ln(z) * pow(ln(omz), 2) * z * CF * NC
            + 2 * ln(z) * Li2(-z) * pow(z, -1) * CF * NC
            + 2 * ln(z) * Li2(-z) * CF * NC
            + ln(z) * Li2(-z) * z * CF * NC
            + 6 * ln(z) * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
            - 4 * ln(z) * Li2(z) * pow(z, -1) * CF * NC
            - 6 * ln(z) * Li2(z) * CF * pow(NC, -1)
            + 4 * ln(z) * Li2(z) * CF * NC
            + 3 * ln(z) * Li2(z) * z * CF * pow(NC, -1)
            - 2 * ln(z) * Li2(z) * z * CF * NC
            + 9.0 / 2.0 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
            - 55.0 / 18.0 * ln(omz) * pow(z, -1) * CF * NC
            - 2 * ln(omz) * pow(z, -1) * CF * NC * pow(rln2, 2)
            - 2.0 / 3.0 * ln(omz) * pow(z, -1) * LMUR * CF * NF
            + 11.0 / 3.0 * ln(omz) * pow(z, -1) * LMUR * CF * NC
            + 3.0 / 2.0 * ln(omz) * pow(z, -1) * LMUF * CF * pow(NC, -1)
        )
        res += (
            -3.0 / 2.0 * ln(omz) * pow(z, -1) * LMUF * CF * NC
            - 3.0 / 2.0 * ln(omz) * pow(z, -1) * LMUA * CF * pow(NC, -1)
            + 2.0 / 3.0 * ln(omz) * pow(z, -1) * LMUA * CF * NF
            + 49.0 / 6.0 * ln(omz) * pow(z, -1) * LMUA * CF * NC
            - ln(omz) * pow(z, -1) * pow(LMUA, 2) * CF * pow(NC, -1)
            + 3 * ln(omz) * pow(z, -1) * pow(LMUA, 2) * CF * NC
            - 9.0 / 2.0 * ln(omz) * CF * pow(NC, -1)
            + 23.0 / 3.0 * ln(omz) * CF * NC
            - 2 * ln(omz) * CF * NC * pow(rln2, 2)
            + 2.0 / 3.0 * ln(omz) * LMUR * CF * NF
            - 11.0 / 3.0 * ln(omz) * LMUR * CF * NC
            - 3.0 / 2.0 * ln(omz) * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * ln(omz) * LMUF * CF * NC
            + 5.0 / 2.0 * ln(omz) * LMUA * CF * pow(NC, -1)
            - 2.0 / 3.0 * ln(omz) * LMUA * CF * NF
            - 41.0 / 6.0 * ln(omz) * LMUA * CF * NC
            + ln(omz) * pow(LMUA, 2) * CF * pow(NC, -1)
            - 3 * ln(omz) * pow(LMUA, 2) * CF * NC
            + 5.0 / 2.0 * ln(omz) * z * CF * pow(NC, -1)
            - 31.0 / 6.0 * ln(omz) * z * CF * NC
            - ln(omz) * z * CF * NC * pow(rln2, 2)
            - 1.0 / 3.0 * ln(omz) * z * LMUR * CF * NF
            + 11.0 / 6.0 * ln(omz) * z * LMUR * CF * NC
            + 3.0 / 4.0 * ln(omz) * z * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * ln(omz) * z * LMUF * CF * NC
            + 1.0 / 3.0 * ln(omz) * z * LMUA * CF * NF
            - 17.0 / 6.0 * ln(omz) * z * LMUA * CF * NC
            - 1.0 / 2.0 * ln(omz) * z * pow(LMUA, 2) * CF * pow(NC, -1)
            + 3.0 / 2.0 * ln(omz) * z * pow(LMUA, 2) * CF * NC
            - 13.0 / 9.0 * ln(omz) * pow(z, 2) * CF * NC
            - 4.0 / 3.0 * ln(omz) * pow(z, 2) * LMUA * CF * NC
            + 2.0 / 3.0 * ln(omz) * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
            - 2.0 / 3.0 * ln(omz) * pow(pi, 2) * pow(z, -1) * CF * NC
            - ln(omz) * pow(pi, 2) * CF * pow(NC, -1)
            - ln(omz) * pow(pi, 2) * CF * NC
            + 1.0 / 2.0 * ln(omz) * pow(pi, 2) * z * CF * pow(NC, -1)
            - 7.0 / 6.0 * ln(omz) * pow(pi, 2) * z * CF * NC
            + 4 * ln(omz) * ln(1 + z) * pow(z, -1) * CF * NC * rln2
            + 4 * ln(omz) * ln(1 + z) * CF * NC * rln2
            + 2 * ln(omz) * ln(1 + z) * z * CF * NC * rln2
            - 2 * ln(omz) * pow(ln(1 + z), 2) * pow(z, -1) * CF * NC
        )
        res += (
            -2 * ln(omz) * pow(ln(1 + z), 2) * CF * NC
            - ln(omz) * pow(ln(1 + z), 2) * z * CF * NC
            + 3.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1)
            - 20.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF * NC
            + 2 * pow(ln(omz), 2) * pow(z, -1) * LMUA * CF * pow(NC, -1)
            - 4 * pow(ln(omz), 2) * pow(z, -1) * LMUA * CF * NC
            - 2 * pow(ln(omz), 2) * CF * pow(NC, -1)
            + 6 * pow(ln(omz), 2) * CF * NC
            - 2 * pow(ln(omz), 2) * LMUA * CF * pow(NC, -1)
            + 4 * pow(ln(omz), 2) * LMUA * CF * NC
            + 1.0 / 8.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
            - 1.0 / 8.0 * pow(ln(omz), 2) * z * CF * NC
            + pow(ln(omz), 2) * z * LMUA * CF * pow(NC, -1)
            - 2 * pow(ln(omz), 2) * z * LMUA * CF * NC
            + 2.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF * NC
            - 5.0 / 6.0 * pow(ln(omz), 3) * pow(z, -1) * CF * pow(NC, -1)
            + 7.0 / 6.0 * pow(ln(omz), 3) * pow(z, -1) * CF * NC
            + 5.0 / 6.0 * pow(ln(omz), 3) * CF * pow(NC, -1)
            - 7.0 / 6.0 * pow(ln(omz), 3) * CF * NC
            - 5.0 / 12.0 * pow(ln(omz), 3) * z * CF * pow(NC, -1)
            + 7.0 / 12.0 * pow(ln(omz), 3) * z * CF * NC
            - 2 * ln(omz) * Li2(1 - z) * pow(z, -1) * CF * pow(NC, -1)
            - 2 * ln(omz) * Li2(1 - z) * pow(z, -1) * CF * NC
            + 3 * ln(omz) * Li2(1 - z) * CF * pow(NC, -1)
            + 9 * ln(omz) * Li2(1 - z) * CF * NC
            - 3.0 / 2.0 * ln(omz) * Li2(1 - z) * z * CF * pow(NC, -1)
            + 3.0 / 2.0 * ln(omz) * Li2(1 - z) * z * CF * NC
            + 4 * ln(omz) * Li2(-z) * pow(z, -1) * CF * NC
            + 4 * ln(omz) * Li2(-z) * CF * NC
            + 2 * ln(omz) * Li2(-z) * z * CF * NC
            + 3 * ln(omz) * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
            + 3 * ln(omz) * Li2(z) * pow(z, -1) * CF * NC
            - ln(omz) * Li2(z) * CF * pow(NC, -1)
            + 11 * ln(omz) * Li2(z) * CF * NC
            + 1.0 / 2.0 * ln(omz) * Li2(z) * z * CF * pow(NC, -1)
            + 13.0 / 2.0 * ln(omz) * Li2(z) * z * CF * NC
            + 2.0 / 3.0 * ln(opz) * pow(pi, 2) * pow(z, -1) * CF * NC
            + 2.0 / 3.0 * ln(opz) * pow(pi, 2) * CF * NC
        )
        res += (
            +1.0 / 3.0 * ln(opz) * pow(pi, 2) * z * CF * NC
            - 4 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * pow(z, -1) * CF * NC
            - 4 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * CF * NC
            - 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * z * CF * NC
            - 4 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * pow(z, -1) * CF * NC
            - 4 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * CF * NC
            - 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * z * CF * NC
            + 3 * Li3(1 - z) * pow(z, -1) * CF * pow(NC, -1)
            + 7 * Li3(1 - z) * pow(z, -1) * CF * NC
            - 2 * Li3(1 - z) * CF * pow(NC, -1)
            + 8 * Li3(1 - z) * CF * NC
            + Li3(1 - z) * z * CF * pow(NC, -1)
            + 6 * Li3(1 - z) * z * CF * NC
            + 2 * Li3(-z) * pow(z, -1) * CF * NC
            + 2 * Li3(-z) * CF * NC
            + Li3(-z) * z * CF * NC
            + 4 * Li3(1 / (1 + z)) * pow(z, -1) * CF * NC
            + 4 * Li3(1 / (1 + z)) * CF * NC
            + 2 * Li3(1 / (1 + z)) * z * CF * NC
            - 4 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * pow(z, -1) * CF * NC
            - 4 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * CF * NC
            - 2 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * z * CF * NC
            - 6 * Li3(z) * pow(z, -1) * CF * pow(NC, -1)
            + 20 * Li3(z) * pow(z, -1) * CF * NC
            + 8 * Li3(z) * CF * pow(NC, -1)
            - 2 * Li3(z) * CF * NC
            - 4 * Li3(z) * z * CF * pow(NC, -1)
            + 15 * Li3(z) * z * CF * NC
            - 4 * Li2(-z) * pow(z, -1) * LMUA * CF * NC
            - 4 * Li2(-z) * LMUA * CF * NC
            + Li2(-z) * z * CF * NC
            - 2 * Li2(-z) * z * LMUA * CF * NC
            - 3.0 / 2.0 * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
            + 89.0 / 6.0 * Li2(z) * pow(z, -1) * CF * NC
            - 6 * Li2(z) * pow(z, -1) * LMUA * CF * pow(NC, -1)
            - 6 * Li2(z) * pow(z, -1) * LMUA * CF * NC
            - 2 * Li2(z) * CF * NC
            + 5 * Li2(z) * LMUA * CF * pow(NC, -1)
            - Li2(z) * LMUA * CF * NC
            + Li2(z) * z * CF * pow(NC, -1)
            + Li2(z) * z * CF * NC
            - 5.0 / 2.0 * Li2(z) * z * LMUA * CF * pow(NC, -1)
            - 11.0 / 2.0 * Li2(z) * z * LMUA * CF * NC
            - 4.0 / 3.0 * Li2(z) * pow(z, 2) * CF * NC
        )

        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = (
            9.0 / 2.0 * pow(z, -1) * CF * pow(NC, -1)
            - 55.0 / 18.0 * pow(z, -1) * CF * NC
            - 2.0 / 3.0 * pow(z, -1) * LMUR * CF * NF
            + 11.0 / 3.0 * pow(z, -1) * LMUR * CF * NC
            + 3.0 / 2.0 * pow(z, -1) * LMUF * CF * pow(NC, -1)
            - 3.0 / 2.0 * pow(z, -1) * LMUF * CF * NC
            - 3.0 / 2.0 * pow(z, -1) * LMUA * CF * pow(NC, -1)
            + 2.0 / 3.0 * pow(z, -1) * LMUA * CF * NF
            + 49.0 / 6.0 * pow(z, -1) * LMUA * CF * NC
            - 2 * pow(z, -1) * LMUA * LMUF * CF * pow(NC, -1)
            + 2 * pow(z, -1) * LMUA * LMUF * CF * NC
            - 17.0 / 4.0 * CF * pow(NC, -1)
            + 95.0 / 12.0 * CF * NC
            + 2.0 / 3.0 * LMUR * CF * NF
            - 11.0 / 3.0 * LMUR * CF * NC
            - 3.0 / 2.0 * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * LMUF * CF * NC
            + 5.0 / 2.0 * LMUA * CF * pow(NC, -1)
            - 2.0 / 3.0 * LMUA * CF * NF
            - 41.0 / 6.0 * LMUA * CF * NC
            + 2 * LMUA * LMUF * CF * pow(NC, -1)
            - 2 * LMUA * LMUF * CF * NC
            + 5.0 / 2.0 * z * CF * pow(NC, -1)
            - 31.0 / 6.0 * z * CF * NC
            - 1.0 / 3.0 * z * LMUR * CF * NF
            + 11.0 / 6.0 * z * LMUR * CF * NC
            + 7.0 / 4.0 * z * LMUF * CF * pow(NC, -1)
            - 7.0 / 4.0 * z * LMUF * CF * NC
            - z * LMUA * CF * pow(NC, -1)
            + 1.0 / 3.0 * z * LMUA * CF * NF
            - 11.0 / 6.0 * z * LMUA * CF * NC
            - z * LMUA * LMUF * CF * pow(NC, -1)
            + z * LMUA * LMUF * CF * NC
            - 13.0 / 9.0 * pow(z, 2) * CF * NC
            - 4.0 / 3.0 * pow(z, 2) * LMUA * CF * NC
            + 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
            - 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * NC
            - 5.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * CF * NC
            + 5.0 / 12.0 * pow(pi, 2) * z * CF * pow(NC, -1)
            - 3.0 / 4.0 * pow(pi, 2) * z * CF * NC
            + 3.0 / 2.0 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
            - 89.0 / 6.0 * ln(z) * pow(z, -1) * CF * NC
            + 2 * ln(z) * pow(z, -1) * LMUF * CF * pow(NC, -1)
            - 2 * ln(z) * pow(z, -1) * LMUF * CF * NC
            + 4 * ln(z) * pow(z, -1) * LMUA * CF * NC
            + 2 * ln(z) * CF * NC
            - 2 * ln(z) * LMUF * CF * pow(NC, -1)
            + 2 * ln(z) * LMUF * CF * NC
            + ln(z) * LMUA * CF * pow(NC, -1)
            + 3 * ln(z) * LMUA * CF * NC
            + 2 * ln(z) * z * CF * NC
            + ln(z) * z * LMUF * CF * pow(NC, -1)
        )
        res += (
            -ln(z) * z * LMUF * CF * NC
            - 1.0 / 2.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
            + 9.0 / 2.0 * ln(z) * z * LMUA * CF * NC
            + 4.0 / 3.0 * ln(z) * pow(z, 2) * CF * NC
            + 4 * ln(z) * ln(1 + z) * pow(z, -1) * CF * NC
            + 4 * ln(z) * ln(1 + z) * CF * NC
            + 2 * ln(z) * ln(1 + z) * z * CF * NC
            - 6 * pow(ln(z), 2) * pow(z, -1) * CF * NC
            - pow(ln(z), 2) * CF * pow(NC, -1)
            - 3 * pow(ln(z), 2) * CF * NC
            + 1.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
            - 11.0 / 2.0 * pow(ln(z), 2) * z * CF * NC
            + 2 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
            + 6 * ln(z) * ln(omz) * pow(z, -1) * CF * NC
            - 2 * ln(z) * ln(omz) * CF * pow(NC, -1)
            - 6 * ln(z) * ln(omz) * CF * NC
            + ln(z) * ln(omz) * z * CF * pow(NC, -1)
            + 3 * ln(z) * ln(omz) * z * CF * NC
            + 3 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
            - 40.0 / 3.0 * ln(omz) * pow(z, -1) * CF * NC
            + 2 * ln(omz) * pow(z, -1) * LMUF * CF * pow(NC, -1)
            - 2 * ln(omz) * pow(z, -1) * LMUF * CF * NC
            + 2 * ln(omz) * pow(z, -1) * LMUA * CF * pow(NC, -1)
            - 6 * ln(omz) * pow(z, -1) * LMUA * CF * NC
            - 4 * ln(omz) * CF * pow(NC, -1)
            + 12 * ln(omz) * CF * NC
            - 2 * ln(omz) * LMUF * CF * pow(NC, -1)
            + 2 * ln(omz) * LMUF * CF * NC
            - 2 * ln(omz) * LMUA * CF * pow(NC, -1)
            + 6 * ln(omz) * LMUA * CF * NC
            + 3.0 / 4.0 * ln(omz) * z * CF * pow(NC, -1)
            + 1.0 / 4.0 * ln(omz) * z * CF * NC
            + ln(omz) * z * LMUF * CF * pow(NC, -1)
            - ln(omz) * z * LMUF * CF * NC
            + ln(omz) * z * LMUA * CF * pow(NC, -1)
            - 3 * ln(omz) * z * LMUA * CF * NC
            + 4.0 / 3.0 * ln(omz) * pow(z, 2) * CF * NC
            - 2 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1)
            + 4 * pow(ln(omz), 2) * pow(z, -1) * CF * NC
            + 2 * pow(ln(omz), 2) * CF * pow(NC, -1)
            - 4 * pow(ln(omz), 2) * CF * NC
            - pow(ln(omz), 2) * z * CF * pow(NC, -1)
            + 2 * pow(ln(omz), 2) * z * CF * NC
            + 4 * Li2(-z) * pow(z, -1) * CF * NC
            + 4 * Li2(-z) * CF * NC
            + 2 * Li2(-z) * z * CF * NC
        )
        res += +6 * Li2(z) * pow(z, -1) * CF * pow(NC, -1) + 6 * Li2(z) * pow(z, -1) * CF * NC - 5 * Li2(z) * CF * pow(NC, -1) + Li2(z) * CF * NC + 5.0 / 2.0 * Li2(z) * z * CF * pow(NC, -1) + 11.0 / 2.0 * Li2(z) * z * CF * NC

        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = (
            3 * pow(z, -1) * CF * pow(NC, -1)
            - 40.0 / 3.0 * pow(z, -1) * CF * NC
            + 4 * pow(z, -1) * LMUF * CF * pow(NC, -1)
            - 4 * pow(z, -1) * LMUF * CF * NC
            + 2 * pow(z, -1) * LMUA * CF * pow(NC, -1)
            - 2 * pow(z, -1) * LMUA * CF * NC
            - 4 * CF * pow(NC, -1)
            + 12 * CF * NC
            - 4 * LMUF * CF * pow(NC, -1)
            + 4 * LMUF * CF * NC
            - 2 * LMUA * CF * pow(NC, -1)
            + 2 * LMUA * CF * NC
            + 3.0 / 4.0 * z * CF * pow(NC, -1)
            + 1.0 / 4.0 * z * CF * NC
            + 2 * z * LMUF * CF * pow(NC, -1)
            - 2 * z * LMUF * CF * NC
            + z * LMUA * CF * pow(NC, -1)
            - z * LMUA * CF * NC
            + 4.0 / 3.0 * pow(z, 2) * CF * NC
            - 2 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
            - 2 * ln(z) * pow(z, -1) * CF * NC
            + ln(z) * CF * pow(NC, -1)
            - 5 * ln(z) * CF * NC
            - 1.0 / 2.0 * ln(z) * z * CF * pow(NC, -1)
            - 7.0 / 2.0 * ln(z) * z * CF * NC
            - 4 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
            + 8 * ln(omz) * pow(z, -1) * CF * NC
            + 4 * ln(omz) * CF * pow(NC, -1)
            - 8 * ln(omz) * CF * NC
            - 2 * ln(omz) * z * CF * pow(NC, -1)
            + 4 * ln(omz) * z * CF * NC
        )

        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = -3 * pow(z, -1) * CF * pow(NC, -1) + 3 * pow(z, -1) * CF * NC + 3 * CF * pow(NC, -1) - 3 * CF * NC - 3.0 / 2.0 * z * CF * pow(NC, -1) + 3.0 / 2.0 * z * CF * NC

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
        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                8 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * pow(z, -1) * CF * pow(NC, -1)
                - 8 * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * CF * pow(NC, -1)
                + 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                - 14 * z * CF * pow(NC, -1)
                + 10 * x * pow(z, -1) * CF * pow(NC, -1)
                - 10 * x * CF * pow(NC, -1)
                - 5.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * pow(pi, 2) * CF * pow(NC, -1)
                - pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                + 48 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                - 54 * ln(x) * CF * pow(NC, -1)
                - 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 13 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 19 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * pow(ln(x), 2) * CF * pow(NC, -1)
                + 19.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 13 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 6 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 16 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 11 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                + 26 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 22 * ln(x) * ln(z) * CF * pow(NC, -1)
                - 13 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 5 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -10 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 20 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                + 28 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 32 * ln(x) * ln(omx) * CF * pow(NC, -1)
                - 14 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 8 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 22 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 17 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                + 32 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 34 * ln(x) * ln(omz) * CF * pow(NC, -1)
                - 16 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 22 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 10 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(xmz) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(xmz) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(x) * ln(omxmz) * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(omxmz) * x * CF * pow(NC, -1)
            )
            tmp += (
                +18 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                - 26 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 28 * ln(z) * CF * pow(NC, -1)
                + 16 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(z) * x * CF * pow(NC, -1)
                + 5 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 9 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * pow(ln(z), 2) * CF * pow(NC, -1)
                + 9.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 5 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 8 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * ln(omx) * CF * pow(NC, -1)
                + 6 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 12 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 20 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(z) * ln(omz) * CF * pow(NC, -1)
                + 10 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 8 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                - 2 * ln(z) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(z) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(xmz) * CF * pow(NC, -1)
            )
            tmp += (
                -2 * ln(z) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(z) * ln(xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(xmz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 22 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 26 * ln(omx) * CF * pow(NC, -1)
                + 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 9 * pow(ln(omx), 2) * CF * pow(NC, -1)
                + 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 16 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 13 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 22 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 26 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                + 11 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 16 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - 3 * ln(omx) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 6 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 32 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(omz) * CF * pow(NC, -1)
                + 20 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(omz) * z * CF * pow(NC, -1)
                + 8 * ln(omz) * x * CF * pow(NC, -1)
                + 8 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -13.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 11 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * pow(ln(omz), 2) * CF * pow(NC, -1)
                + 11.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 3 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 4 * ln(omz) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * ln(omz) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1)
                + 6 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(omz) * ln(omxmz) * CF * pow(NC, -1)
                - 3 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(omxmz) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                - 2 * Li2(omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1)
                - 2 * Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                +2 * Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                + Li2(z * pow(omx, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1)
                + Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * pow(NC, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * pow(NC, -1)
                + 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                8 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * pow(z, -1) * CF * pow(NC, -1)
                - 8 * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * CF * pow(NC, -1)
                + 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                - 14 * z * CF * pow(NC, -1)
                + 10 * x * pow(z, -1) * CF * pow(NC, -1)
                - 10 * x * CF * pow(NC, -1)
                - 5.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * pow(pi, 2) * CF * pow(NC, -1)
                - pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                + 48 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                - 54 * ln(x) * CF * pow(NC, -1)
                - 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(x) * ln(-omxmz) * CF * pow(NC, -1)
                + 3 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 13 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 20 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 19 * pow(ln(x), 2) * CF * pow(NC, -1)
                + 10 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 13 * pow(ln(x), 2) * z * CF * pow(NC, -1)
            )
            tmp += (
                -7.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 7 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 20 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                + 32 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 28 * ln(x) * ln(z) * CF * pow(NC, -1)
                - 16 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 12 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 16 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                + 22 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 26 * ln(x) * ln(omx) * CF * pow(NC, -1)
                - 11 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 22 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                + 34 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 32 * ln(x) * ln(omz) * CF * pow(NC, -1)
                - 17 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 22 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 12 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(xmz) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(xmz) * x * CF * pow(NC, -1)
            )
            tmp += (
                +18 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                - 26 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 28 * ln(z) * CF * pow(NC, -1)
                + 16 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(z) * x * CF * pow(NC, -1)
                + 5 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 9 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * pow(ln(z), 2) * CF * pow(NC, -1)
                + 9.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 5 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 8 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * ln(omx) * CF * pow(NC, -1)
                + 6 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 16 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 11 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 26 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 22 * ln(z) * ln(omz) * CF * pow(NC, -1)
                + 13 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 16 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 10 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                - 2 * ln(z) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(z) * ln(xmz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(xmz) * CF * pow(NC, -1)
            )
            tmp += (
                -2 * ln(z) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(z) * ln(xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(xmz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 22 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 26 * ln(omx) * CF * pow(NC, -1)
                + 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 9 * pow(ln(omx), 2) * CF * pow(NC, -1)
                + 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 12 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 16 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                + 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 12 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 32 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(omz) * CF * pow(NC, -1)
                + 20 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(omz) * z * CF * pow(NC, -1)
                + 8 * ln(omz) * x * CF * pow(NC, -1)
                - 4 * ln(omz) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                +3 * ln(omz) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1)
                + 6 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1)
                - 3 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 8 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 12 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * pow(ln(omz), 2) * CF * pow(NC, -1)
                + 6 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * pow(NC, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * pow(NC, -1)
                - Li2(pow(z, -1) * omx) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1)
                - Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1)
                - 2 * Li2(omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                +4 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1)
                - 2 * Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
            )

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                8 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * pow(z, -1) * CF * pow(NC, -1)
                - 8 * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * CF * pow(NC, -1)
                + 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                - 14 * z * CF * pow(NC, -1)
                + 10 * x * pow(z, -1) * CF * pow(NC, -1)
                - 10 * x * CF * pow(NC, -1)
                - 3 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 13.0 / 6.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                + 14.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 13.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1)
                - 7.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 5.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 5.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                + 48 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                - 54 * ln(x) * CF * pow(NC, -1)
                - 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(-xmz) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-xmz) * x * CF * pow(NC, -1)
                + 14 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 21 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 21 * pow(ln(x), 2) * CF * pow(NC, -1)
                + 21.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 14 * pow(ln(x), 2) * z * CF * pow(NC, -1)
            )
            tmp += (
                -7.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 7 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                + 30 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(x) * ln(z) * CF * pow(NC, -1)
                - 15 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 12 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 15 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                + 24 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 30 * ln(x) * ln(omx) * CF * pow(NC, -1)
                - 12 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 24 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                + 36 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 36 * ln(x) * ln(omz) * CF * pow(NC, -1)
                - 18 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 24 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 12 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(x) * ln(omxmz) * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                +2 * ln(x) * ln(omxmz) * x * CF * pow(NC, -1)
                + 18 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                - 26 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 28 * ln(z) * CF * pow(NC, -1)
                + 16 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(z) * x * CF * pow(NC, -1)
                - 2 * ln(z) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(z) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(-xmz) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(-xmz) * x * CF * pow(NC, -1)
                + 6 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 7.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 11 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 7 * pow(ln(z), 2) * CF * pow(NC, -1)
                + 11.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 5 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 6 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 5 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 8 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 10 * ln(z) * ln(omx) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - ln(z) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 14 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 9 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -24 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(z) * ln(omz) * CF * pow(NC, -1)
                + 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 14 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 10 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 22 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 26 * ln(omx) * CF * pow(NC, -1)
                + 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 7 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 11.0 / 2.0 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 10 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 11 * pow(ln(omx), 2) * CF * pow(NC, -1)
                + 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 7 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 3 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 12 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 11 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 14 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 22 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                + 7 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 12 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - ln(omx) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 32 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(omz) * CF * pow(NC, -1)
                + 20 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -24 * ln(omz) * z * CF * pow(NC, -1)
                + 8 * ln(omz) * x * CF * pow(NC, -1)
                + 10 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 15.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 15 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 15 * pow(ln(omz), 2) * CF * pow(NC, -1)
                + 15.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 5 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 4 * ln(omz) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * ln(omz) * ln(omxmz) * pow(z, -1) * CF * pow(NC, -1)
                + 6 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(omz) * ln(omxmz) * CF * pow(NC, -1)
                - 3 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(omxmz) * x * CF * pow(NC, -1)
                + 2 * Li2(pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1)
                + 2 * Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                + Li2(z * pow(omx, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1)
                + Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                +2 * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * pow(NC, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * pow(NC, -1)
                + 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                8 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * pow(z, -1) * CF * pow(NC, -1)
                - 8 * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * CF * pow(NC, -1)
                + 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                - 14 * z * CF * pow(NC, -1)
                + 10 * x * pow(z, -1) * CF * pow(NC, -1)
                - 10 * x * CF * pow(NC, -1)
                - 5.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * pow(pi, 2) * CF * pow(NC, -1)
                - pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                + 48 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                - 54 * ln(x) * CF * pow(NC, -1)
                - 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(x) * ln(-omxmz) * CF * pow(NC, -1)
                + 3 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(-xmz) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -2 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-xmz) * x * CF * pow(NC, -1)
                + 12 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 9 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 18 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * pow(ln(x), 2) * CF * pow(NC, -1)
                + 9 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 12 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 6 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                + 28 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 26 * ln(x) * ln(z) * CF * pow(NC, -1)
                - 14 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 5 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 10 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                + 26 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 28 * ln(x) * ln(omx) * CF * pow(NC, -1)
                - 13 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 8 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 20 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 15 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                + 30 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 30 * ln(x) * ln(omz) * CF * pow(NC, -1)
                - 15 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -10 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                - 26 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 28 * ln(z) * CF * pow(NC, -1)
                + 16 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(z) * x * CF * pow(NC, -1)
                - 2 * ln(z) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(z) * ln(-xmz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(-xmz) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(-xmz) * x * CF * pow(NC, -1)
                + 4 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 7 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 5 * pow(ln(z), 2) * CF * pow(NC, -1)
                + 7.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 3 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 10 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 7 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 16 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * ln(z) * ln(omx) * CF * pow(NC, -1)
                + 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - 3 * ln(z) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                + 6 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 14 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -22 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(z) * ln(omz) * CF * pow(NC, -1)
                + 11 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 14 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 8 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 22 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 26 * ln(omx) * CF * pow(NC, -1)
                + 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 9 * pow(ln(omx), 2) * CF * pow(NC, -1)
                + 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 12 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 16 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                + 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 12 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 32 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(omz) * CF * pow(NC, -1)
                + 20 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -24 * ln(omz) * z * CF * pow(NC, -1)
                + 8 * ln(omz) * x * CF * pow(NC, -1)
                - 4 * ln(omz) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * ln(omz) * ln(-omxmz) * pow(z, -1) * CF * pow(NC, -1)
                + 6 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1)
                - 3 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 8 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 12 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * pow(ln(omz), 2) * CF * pow(NC, -1)
                + 6 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * pow(NC, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1)
            )
            tmp += (
                -2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                - Li2(pow(z, -1) * omx) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1)
                - Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1)
                + 2 * Li2(pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(pow(omx, -1) * omz) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1)
                + 2 * Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                + 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                -4 * pow(z, -1) * CF * NC * pow(omx, -1)
                + 7 * pow(z, -1) * CF * NC
                + 4 * CF * NC * pow(omx, -1)
                - 9 * CF * NC
                - 5 * z * CF * NC * pow(omx, -1)
                + 4 * z * CF * NC
                - 3 * x * pow(z, -1) * CF * NC
                + 6 * x * CF * NC
                + pow(pi, 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 1.0 / 2.0 * pow(pi, 2) * pow(z, -1) * CF * NC
                - pow(pi, 2) * CF * NC * pow(omx, -1)
                + pow(pi, 2) * CF * NC
                + 1.0 / 2.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                - pow(pi, 2) * z * CF * NC
                - 1.0 / 2.0 * pow(pi, 2) * x * pow(z, -1) * CF * NC
                + pow(pi, 2) * x * CF * NC
                + 18 * ln(x) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 18 * ln(x) * pow(z, -1) * CF * NC
                - 18 * ln(x) * CF * NC * pow(omx, -1)
                + 15 * ln(x) * CF * NC
                + 12 * ln(x) * z * CF * NC * pow(omx, -1)
                - 18 * ln(x) * z * CF * NC
                + 18 * ln(x) * x * CF * NC
                - 2 * ln(x) * ln(-xmz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + ln(x) * ln(-xmz) * pow(z, -1) * CF * NC
                + 2 * ln(x) * ln(-xmz) * CF * NC * pow(omx, -1)
                - 2 * ln(x) * ln(-xmz) * CF * NC
                - ln(x) * ln(-xmz) * z * CF * NC * pow(omx, -1)
                + 2 * ln(x) * ln(-xmz) * z * CF * NC
                + ln(x) * ln(-xmz) * x * pow(z, -1) * CF * NC
                - 2 * ln(x) * ln(-xmz) * x * CF * NC
                - 7 * pow(ln(x), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * NC
                + 7 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                - 7 * pow(ln(x), 2) * CF * NC
                - 7.0 / 2.0 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                + 7 * pow(ln(x), 2) * z * CF * NC
                + 7.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * CF * NC
                - 7 * pow(ln(x), 2) * x * CF * NC
                + 12 * ln(x) * ln(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 6 * ln(x) * ln(z) * pow(z, -1) * CF * NC
                - 12 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                + 12 * ln(x) * ln(z) * CF * NC
                + 6 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                - 12 * ln(x) * ln(z) * z * CF * NC
                - 6 * ln(x) * ln(z) * x * pow(z, -1) * CF * NC
                + 12 * ln(x) * ln(z) * x * CF * NC
                + 12 * ln(x) * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
            )
            tmp += (
                -6 * ln(x) * ln(omx) * pow(z, -1) * CF * NC
                - 12 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                + 12 * ln(x) * ln(omx) * CF * NC
                + 6 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                - 12 * ln(x) * ln(omx) * z * CF * NC
                - 6 * ln(x) * ln(omx) * x * pow(z, -1) * CF * NC
                + 12 * ln(x) * ln(omx) * x * CF * NC
                + 6 * ln(x) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 3 * ln(x) * ln(omz) * pow(z, -1) * CF * NC
                - 6 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                + 6 * ln(x) * ln(omz) * CF * NC
                + 3 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 6 * ln(x) * ln(omz) * z * CF * NC
                - 3 * ln(x) * ln(omz) * x * pow(z, -1) * CF * NC
                + 6 * ln(x) * ln(omz) * x * CF * NC
                - 12 * ln(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 12 * ln(z) * pow(z, -1) * CF * NC
                + 12 * ln(z) * CF * NC * pow(omx, -1)
                - 10 * ln(z) * CF * NC
                - 8 * ln(z) * z * CF * NC * pow(omx, -1)
                + 12 * ln(z) * z * CF * NC
                - 12 * ln(z) * x * CF * NC
                + 2 * ln(z) * ln(-xmz) * pow(z, -1) * CF * NC * pow(omx, -1)
                - ln(z) * ln(-xmz) * pow(z, -1) * CF * NC
                - 2 * ln(z) * ln(-xmz) * CF * NC * pow(omx, -1)
                + 2 * ln(z) * ln(-xmz) * CF * NC
                + ln(z) * ln(-xmz) * z * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(-xmz) * z * CF * NC
                - ln(z) * ln(-xmz) * x * pow(z, -1) * CF * NC
                + 2 * ln(z) * ln(-xmz) * x * CF * NC
                - 5 * pow(ln(z), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * NC
                + 5 * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                - 5 * pow(ln(z), 2) * CF * NC
                - 5.0 / 2.0 * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                + 5 * pow(ln(z), 2) * z * CF * NC
                + 5.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * CF * NC
                - 5 * pow(ln(z), 2) * x * CF * NC
                - 10 * ln(z) * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 5 * ln(z) * ln(omx) * pow(z, -1) * CF * NC
                + 10 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                - 10 * ln(z) * ln(omx) * CF * NC
                - 5 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
            )
            tmp += (
                +10 * ln(z) * ln(omx) * z * CF * NC
                + 5 * ln(z) * ln(omx) * x * pow(z, -1) * CF * NC
                - 10 * ln(z) * ln(omx) * x * CF * NC
                - 2 * ln(z) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + ln(z) * ln(omz) * pow(z, -1) * CF * NC
                + 2 * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(omz) * CF * NC
                - ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 2 * ln(z) * ln(omz) * z * CF * NC
                + ln(z) * ln(omz) * x * pow(z, -1) * CF * NC
                - 2 * ln(z) * ln(omz) * x * CF * NC
                - 12 * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 12 * ln(omx) * pow(z, -1) * CF * NC
                + 12 * ln(omx) * CF * NC * pow(omx, -1)
                - 10 * ln(omx) * CF * NC
                - 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                + 12 * ln(omx) * z * CF * NC
                - 12 * ln(omx) * x * CF * NC
                - 4 * pow(ln(omx), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * pow(z, -1) * CF * NC
                + 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                - 4 * pow(ln(omx), 2) * CF * NC
                - 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                + 4 * pow(ln(omx), 2) * z * CF * NC
                + 2 * pow(ln(omx), 2) * x * pow(z, -1) * CF * NC
                - 4 * pow(ln(omx), 2) * x * CF * NC
                - 4 * ln(omx) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * ln(omx) * ln(omz) * pow(z, -1) * CF * NC
                + 4 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                - 4 * ln(omx) * ln(omz) * CF * NC
                - 2 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 4 * ln(omx) * ln(omz) * z * CF * NC
                + 2 * ln(omx) * ln(omz) * x * pow(z, -1) * CF * NC
                - 4 * ln(omx) * ln(omz) * x * CF * NC
                - 6 * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 6 * ln(omz) * pow(z, -1) * CF * NC
                + 6 * ln(omz) * CF * NC * pow(omx, -1)
                - 5 * ln(omz) * CF * NC
                - 4 * ln(omz) * z * CF * NC * pow(omx, -1)
                + 6 * ln(omz) * z * CF * NC
                - 6 * ln(omz) * x * CF * NC
                - pow(ln(omz), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * CF * NC
                + pow(ln(omz), 2) * CF * NC * pow(omx, -1)
            )
            tmp += (
                -pow(ln(omz), 2) * CF * NC
                - 1.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                + pow(ln(omz), 2) * z * CF * NC
                + 1.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * CF * NC
                - pow(ln(omz), 2) * x * CF * NC
                + 2 * Li2(pow(omx, -1) * omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                - Li2(pow(omx, -1) * omz) * pow(z, -1) * CF * NC
                - 2 * Li2(pow(omx, -1) * omz) * CF * NC * pow(omx, -1)
                + 2 * Li2(pow(omx, -1) * omz) * CF * NC
                + Li2(pow(omx, -1) * omz) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(pow(omx, -1) * omz) * z * CF * NC
                - Li2(pow(omx, -1) * omz) * x * pow(z, -1) * CF * NC
                + 2 * Li2(pow(omx, -1) * omz) * x * CF * NC
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(z, -1) * CF * NC
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * NC * pow(omx, -1)
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * NC
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * NC * pow(omx, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * NC
                + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * pow(z, -1) * CF * NC
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * x * CF * NC
                + 2 * Li2(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - Li2(z) * pow(z, -1) * CF * NC
                - 2 * Li2(z) * CF * NC * pow(omx, -1)
                + 2 * Li2(z) * CF * NC
                + Li2(z) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(z) * z * CF * NC
                - Li2(z) * x * pow(z, -1) * CF * NC
                + 2 * Li2(z) * x * CF * NC
            )

            res += tmp

        if round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                -4 * pow(z, -1) * CF * NC * pow(omx, -1)
                + 7 * pow(z, -1) * CF * NC
                + 4 * CF * NC * pow(omx, -1)
                - 9 * CF * NC
                - 5 * z * CF * NC * pow(omx, -1)
                + 4 * z * CF * NC
                - 3 * x * pow(z, -1) * CF * NC
                + 6 * x * CF * NC
                + pow(pi, 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 1.0 / 2.0 * pow(pi, 2) * pow(z, -1) * CF * NC
                - pow(pi, 2) * CF * NC * pow(omx, -1)
                + pow(pi, 2) * CF * NC
                + 1.0 / 2.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                - pow(pi, 2) * z * CF * NC
                - 1.0 / 2.0 * pow(pi, 2) * x * pow(z, -1) * CF * NC
                + pow(pi, 2) * x * CF * NC
                + 18 * ln(x) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 18 * ln(x) * pow(z, -1) * CF * NC
                - 18 * ln(x) * CF * NC * pow(omx, -1)
                + 15 * ln(x) * CF * NC
                + 12 * ln(x) * z * CF * NC * pow(omx, -1)
                - 18 * ln(x) * z * CF * NC
                + 18 * ln(x) * x * CF * NC
                - 6 * pow(ln(x), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 3 * pow(ln(x), 2) * pow(z, -1) * CF * NC
                + 6 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                - 6 * pow(ln(x), 2) * CF * NC
                - 3 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                + 6 * pow(ln(x), 2) * z * CF * NC
                + 3 * pow(ln(x), 2) * x * pow(z, -1) * CF * NC
                - 6 * pow(ln(x), 2) * x * CF * NC
                + 10 * ln(x) * ln(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 5 * ln(x) * ln(z) * pow(z, -1) * CF * NC
                - 10 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                + 10 * ln(x) * ln(z) * CF * NC
                + 5 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                - 10 * ln(x) * ln(z) * z * CF * NC
                - 5 * ln(x) * ln(z) * x * pow(z, -1) * CF * NC
                + 10 * ln(x) * ln(z) * x * CF * NC
                + 10 * ln(x) * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 5 * ln(x) * ln(omx) * pow(z, -1) * CF * NC
                - 10 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                + 10 * ln(x) * ln(omx) * CF * NC
                + 5 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                - 10 * ln(x) * ln(omx) * z * CF * NC
                - 5 * ln(x) * ln(omx) * x * pow(z, -1) * CF * NC
                + 10 * ln(x) * ln(omx) * x * CF * NC
                + 8 * ln(x) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
            )
            tmp += (
                -4 * ln(x) * ln(omz) * pow(z, -1) * CF * NC
                - 8 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                + 8 * ln(x) * ln(omz) * CF * NC
                + 4 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 8 * ln(x) * ln(omz) * z * CF * NC
                - 4 * ln(x) * ln(omz) * x * pow(z, -1) * CF * NC
                + 8 * ln(x) * ln(omz) * x * CF * NC
                - 2 * ln(x) * ln(xmz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + ln(x) * ln(xmz) * pow(z, -1) * CF * NC
                + 2 * ln(x) * ln(xmz) * CF * NC * pow(omx, -1)
                - 2 * ln(x) * ln(xmz) * CF * NC
                - ln(x) * ln(xmz) * z * CF * NC * pow(omx, -1)
                + 2 * ln(x) * ln(xmz) * z * CF * NC
                + ln(x) * ln(xmz) * x * pow(z, -1) * CF * NC
                - 2 * ln(x) * ln(xmz) * x * CF * NC
                - 12 * ln(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 12 * ln(z) * pow(z, -1) * CF * NC
                + 12 * ln(z) * CF * NC * pow(omx, -1)
                - 10 * ln(z) * CF * NC
                - 8 * ln(z) * z * CF * NC * pow(omx, -1)
                + 12 * ln(z) * z * CF * NC
                - 12 * ln(z) * x * CF * NC
                - 4 * pow(ln(z), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * pow(ln(z), 2) * pow(z, -1) * CF * NC
                + 4 * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                - 4 * pow(ln(z), 2) * CF * NC
                - 2 * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                + 4 * pow(ln(z), 2) * z * CF * NC
                + 2 * pow(ln(z), 2) * x * pow(z, -1) * CF * NC
                - 4 * pow(ln(z), 2) * x * CF * NC
                - 8 * ln(z) * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 4 * ln(z) * ln(omx) * pow(z, -1) * CF * NC
                + 8 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                - 8 * ln(z) * ln(omx) * CF * NC
                - 4 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                + 8 * ln(z) * ln(omx) * z * CF * NC
                + 4 * ln(z) * ln(omx) * x * pow(z, -1) * CF * NC
                - 8 * ln(z) * ln(omx) * x * CF * NC
                - 4 * ln(z) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * ln(z) * ln(omz) * pow(z, -1) * CF * NC
                + 4 * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                - 4 * ln(z) * ln(omz) * CF * NC
                - 2 * ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 4 * ln(z) * ln(omz) * z * CF * NC
            )
            tmp += (
                +2 * ln(z) * ln(omz) * x * pow(z, -1) * CF * NC
                - 4 * ln(z) * ln(omz) * x * CF * NC
                + 2 * ln(z) * ln(xmz) * pow(z, -1) * CF * NC * pow(omx, -1)
                - ln(z) * ln(xmz) * pow(z, -1) * CF * NC
                - 2 * ln(z) * ln(xmz) * CF * NC * pow(omx, -1)
                + 2 * ln(z) * ln(xmz) * CF * NC
                + ln(z) * ln(xmz) * z * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(xmz) * z * CF * NC
                - ln(z) * ln(xmz) * x * pow(z, -1) * CF * NC
                + 2 * ln(z) * ln(xmz) * x * CF * NC
                - 12 * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 12 * ln(omx) * pow(z, -1) * CF * NC
                + 12 * ln(omx) * CF * NC * pow(omx, -1)
                - 10 * ln(omx) * CF * NC
                - 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                + 12 * ln(omx) * z * CF * NC
                - 12 * ln(omx) * x * CF * NC
                - 4 * pow(ln(omx), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * pow(z, -1) * CF * NC
                + 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                - 4 * pow(ln(omx), 2) * CF * NC
                - 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                + 4 * pow(ln(omx), 2) * z * CF * NC
                + 2 * pow(ln(omx), 2) * x * pow(z, -1) * CF * NC
                - 4 * pow(ln(omx), 2) * x * CF * NC
                - 4 * ln(omx) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * ln(omx) * ln(omz) * pow(z, -1) * CF * NC
                + 4 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                - 4 * ln(omx) * ln(omz) * CF * NC
                - 2 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 4 * ln(omx) * ln(omz) * z * CF * NC
                + 2 * ln(omx) * ln(omz) * x * pow(z, -1) * CF * NC
                - 4 * ln(omx) * ln(omz) * x * CF * NC
                - 6 * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 6 * ln(omz) * pow(z, -1) * CF * NC
                + 6 * ln(omz) * CF * NC * pow(omx, -1)
                - 5 * ln(omz) * CF * NC
                - 4 * ln(omz) * z * CF * NC * pow(omx, -1)
                + 6 * ln(omz) * z * CF * NC
                - 6 * ln(omz) * x * CF * NC
                - pow(ln(omz), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * CF * NC
                + pow(ln(omz), 2) * CF * NC * pow(omx, -1)
            )
            tmp += (
                -pow(ln(omz), 2) * CF * NC
                - 1.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                + pow(ln(omz), 2) * z * CF * NC
                + 1.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * CF * NC
                - pow(ln(omz), 2) * x * CF * NC
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(z, -1) * CF * NC * pow(omx, -1)
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(z, -1) * CF * NC
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * NC * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * NC
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * NC
                - Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * pow(z, -1) * CF * NC
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * x * CF * NC
                - 2 * Li2(omx * pow(omz, -1)) * pow(z, -1) * CF * NC * pow(omx, -1)
                + Li2(omx * pow(omz, -1)) * pow(z, -1) * CF * NC
                + 2 * Li2(omx * pow(omz, -1)) * CF * NC * pow(omx, -1)
                - 2 * Li2(omx * pow(omz, -1)) * CF * NC
                - Li2(omx * pow(omz, -1)) * z * CF * NC * pow(omx, -1)
                + 2 * Li2(omx * pow(omz, -1)) * z * CF * NC
                + Li2(omx * pow(omz, -1)) * x * pow(z, -1) * CF * NC
                - 2 * Li2(omx * pow(omz, -1)) * x * CF * NC
                + 2 * Li2(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - Li2(z) * pow(z, -1) * CF * NC
                - 2 * Li2(z) * CF * NC * pow(omx, -1)
                + 2 * Li2(z) * CF * NC
                + Li2(z) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(z) * z * CF * NC
                - Li2(z) * x * pow(z, -1) * CF * NC
                + 2 * Li2(z) * x * CF * NC
            )

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
                -8 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * pow(z, -1) * CF * pow(NC, -1)
                - 4 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                + 2 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2)
                - 6 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                + 2 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                + 4 * pow(z, -1) * CF * NC * pow(omx, -1)
                + 89.0 / 18.0 * pow(z, -1) * CF * NC
                - 8 * pow(z, -1) * pow(CF, 2)
                + 1.0 / 3.0 * pow(z, -1) * LMUR * CF * NF
                - 11.0 / 6.0 * pow(z, -1) * LMUR * CF * NC
                - 7.0 / 4.0 * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + 7.0 / 4.0 * pow(z, -1) * LMUF * CF * NC
                - 2 * pow(z, -1) * LMUA * CF * pow(NC, -1)
                - 1.0 / 3.0 * pow(z, -1) * LMUA * CF * NF
                - 11.0 / 6.0 * pow(z, -1) * LMUA * CF * NC
                - 8 * pow(z, -1) * LMUA * pow(CF, 2)
                + pow(z, -1) * LMUA * LMUF * CF * pow(NC, -1)
                - pow(z, -1) * LMUA * LMUF * CF * NC
                + 8 * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * CF * pow(NC, -1) * pow(omxmz, -1)
                - 25.0 / 4.0 * CF * pow(NC, -1)
                + 4 * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                + 2 * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                + 2 * CF * pow(NC, -1) * sqrtxz1 * rln2
                - 4 * CF * NC * pow(omx, -1)
                - 13.0 / 12.0 * CF * NC
                - 8 * CF * NC * pow(rln2, 2) * pow(omx, -1)
                + 4 * CF * NC * pow(rln2, 2)
                - 4 * CF * NC * sqrtxz1 * rln2 * pow(omx, -1)
                + 4 * CF * NC * sqrtxz1 * rln2
                + 8 * pow(CF, 2)
                - 2.0 / 3.0 * LMUR * CF * NF
                + 11.0 / 3.0 * LMUR * CF * NC
                + 5.0 / 2.0 * LMUF * CF * pow(NC, -1)
                - 5.0 / 2.0 * LMUF * CF * NC
                + 1.0 / 2.0 * LMUA * CF * pow(NC, -1)
                + 2.0 / 3.0 * LMUA * CF * NF
                - 13.0 / 6.0 * LMUA * CF * NC
                + 8 * LMUA * pow(CF, 2)
                - LMUA * LMUF * CF * pow(NC, -1)
                + LMUA * LMUF * CF * NC
                - 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * z * CF * pow(NC, -1) * pow(omxmz, -1)
                + 21.0 / 2.0 * z * CF * pow(NC, -1)
                - 2 * z * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                + 5 * z * CF * NC * pow(omx, -1)
            )
            tmp += (
                -35.0 / 3.0 * z * CF * NC
                + 4 * z * CF * NC * pow(rln2, 2)
                + 8 * z * pow(CF, 2)
                + 2.0 / 3.0 * z * LMUR * CF * NF
                - 11.0 / 3.0 * z * LMUR * CF * NC
                - 3.0 / 2.0 * z * LMUF * CF * pow(NC, -1)
                + 3.0 / 2.0 * z * LMUF * CF * NC
                - 2.0 / 3.0 * z * LMUA * CF * NF
                + 14.0 / 3.0 * z * LMUA * CF * NC
                - 4 * z * LMUA * pow(CF, 2)
                + 1.0 / 2.0 * z * LMUA * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * z * LMUA * LMUF * CF * NC
                - 2 * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -1)
                + 41.0 / 9.0 * pow(z, 2) * CF * NC
                + 8.0 / 3.0 * pow(z, 2) * LMUA * CF * NC
                - 5 * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * x * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2)
                + 4 * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                + 11.0 / 18.0 * x * pow(z, -1) * CF * NC
                + 8 * x * pow(z, -1) * pow(CF, 2)
                + 1.0 / 3.0 * x * pow(z, -1) * LMUR * CF * NF
                - 11.0 / 6.0 * x * pow(z, -1) * LMUR * CF * NC
                + 1.0 / 4.0 * x * pow(z, -1) * LMUF * CF * pow(NC, -1)
                - 1.0 / 4.0 * x * pow(z, -1) * LMUF * CF * NC
                + 5 * x * pow(z, -1) * LMUA * CF * pow(NC, -1)
                - 1.0 / 3.0 * x * pow(z, -1) * LMUA * CF * NF
                - 65.0 / 6.0 * x * pow(z, -1) * LMUA * CF * NC
                + 8 * x * pow(z, -1) * LMUA * pow(CF, 2)
                + x * pow(z, -1) * LMUA * LMUF * CF * pow(NC, -1)
                - x * pow(z, -1) * LMUA * LMUF * CF * NC
                + 33.0 / 4.0 * x * CF * pow(NC, -1)
                - 115.0 / 12.0 * x * CF * NC
                + 4 * x * CF * NC * pow(rln2, 2)
                - 8 * x * pow(CF, 2)
                - 2.0 / 3.0 * x * LMUR * CF * NF
                + 11.0 / 3.0 * x * LMUR * CF * NC
                + 1.0 / 2.0 * x * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * x * LMUF * CF * NC
                - 9.0 / 2.0 * x * LMUA * CF * pow(NC, -1)
                + 2.0 / 3.0 * x * LMUA * CF * NF
                + 41.0 / 6.0 * x * LMUA * CF * NC
                - 8 * x * LMUA * pow(CF, 2)
                - x * LMUA * LMUF * CF * pow(NC, -1)
                + x * LMUA * LMUF * CF * NC
                - 9.0 / 2.0 * x * z * CF * pow(NC, -1)
                + 28.0 / 3.0 * x * z * CF * NC
                - 8 * x * z * pow(CF, 2)
                - x * z * LMUF * CF * pow(NC, -1)
                + x * z * LMUF * CF * NC
                + x * z * LMUA * CF * pow(NC, -1)
                + 2 * x * z * LMUA * CF * NC
                + 4 * x * z * LMUA * pow(CF, 2)
                + 1.0 / 2.0 * x * z * LMUA * LMUF * CF * pow(NC, -1)
            )
            tmp += (
                -1.0 / 2.0 * x * z * LMUA * LMUF * CF * NC
                - 19.0 / 9.0 * x * pow(z, 2) * CF * NC
                - 4.0 / 3.0 * x * pow(z, 2) * LMUA * CF * NC
                + 8.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 29.0 / 12.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * pow(pi, 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 17.0 / 12.0 * pow(pi, 2) * pow(z, -1) * CF * NC
                - 10.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 25.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
                + 4.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                - 5.0 / 6.0 * pow(pi, 2) * CF * NC
                + 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 5.0 / 2.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                - pow(pi, 2) * z * CF * NC * pow(omx, -1)
                + 5.0 / 2.0 * pow(pi, 2) * z * CF * NC
                - 13.0 / 12.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 17.0 / 12.0 * pow(pi, 2) * x * pow(z, -1) * CF * NC
                + 7.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(pi, 2) * x * CF * NC
                - 1.0 / 6.0 * pow(pi, 2) * x * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * z * CF * NC
                + 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                + 6 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                - 4 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * NC * rln2 * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * NC * rln2
                - 8 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * sqrtxz1
                + 12 * ln(1 + sqrtxz1 - z) * CF * NC * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * CF * NC * rln2
                + 4 * ln(1 + sqrtxz1 - z) * CF * NC * sqrtxz1 * pow(omx, -1)
            )
            tmp += (
                -4 * ln(1 + sqrtxz1 - z) * CF * NC * sqrtxz1
                + 4 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * z * CF * NC * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * z * CF * NC * rln2
                - 4 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                - 4 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                + 2 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * NC * rln2
                - 4 * ln(1 + sqrtxz1 - z) * x * CF * NC * rln2
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * NC
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * CF * NC * pow(omx, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * NC * pow(omx, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, -1) * CF * NC
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * NC
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * NC * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * NC
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * NC * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * NC
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * NC
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF * NC
            )
            tmp += (
                +4 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * NC * rln2 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * NC * rln2
                + 4 * ln(1 + sqrtxz1 + z) * CF * NC * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 + z) * CF * NC * rln2
                + 2 * ln(1 + sqrtxz1 + z) * z * CF * NC * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 + z) * z * CF * NC * rln2
                - 2 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * NC * rln2
                - 4 * ln(1 + sqrtxz1 + z) * x * CF * NC * rln2
                - 1.0 / 3.0 * ln(x * z * omx * omz) * pow(z, -1) * CF * NF * pow(omx, -1)
                + 36 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 153.0 / 4.0 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + 3 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2
                - 3 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                + ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                + 1.0 / 3.0 * ln(x) * pow(z, -1) * CF * NF * pow(omx, -1)
                - 1.0 / 3.0 * ln(x) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 119.0 / 12.0 * ln(x) * pow(z, -1) * CF * NC
                + 4 * ln(x) * pow(z, -1) * CF * NC * rln2 * pow(omx, -1)
                - 2 * ln(x) * pow(z, -1) * CF * NC * rln2
                - 4 * ln(x) * pow(z, -1) * pow(CF, 2)
                - 2 * ln(x) * pow(z, -1) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * ln(x) * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + 2 * ln(x) * pow(z, -1) * LMUF * CF * NC * pow(omx, -1)
                - 3.0 / 2.0 * ln(x) * pow(z, -1) * LMUF * CF * NC
                - 2 * ln(x) * pow(z, -1) * LMUA * CF * pow(NC, -1) * pow(omx, -1)
                + ln(x) * pow(z, -1) * LMUA * CF * pow(NC, -1)
                + 2 * ln(x) * pow(z, -1) * LMUA * CF * NC * pow(omx, -1)
                - ln(x) * pow(z, -1) * LMUA * CF * NC
                - 48 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * CF * pow(NC, -1) * pow(omxmz, -1)
                + 55 * ln(x) * CF * pow(NC, -1)
                + 6 * ln(x) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + ln(x) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
            )
            tmp += (
                +ln(x) * CF * pow(NC, -1) * sqrtxz1
                + 8 * ln(x) * CF * NC * pow(omx, -1)
                - 13 * ln(x) * CF * NC
                - 8 * ln(x) * CF * NC * rln2 * pow(omx, -1)
                + 2 * ln(x) * CF * NC * rln2
                - 2 * ln(x) * CF * NC * sqrtxz1 * pow(omx, -1)
                + 2 * ln(x) * CF * NC * sqrtxz1
                + 2 * ln(x) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * LMUF * CF * pow(NC, -1)
                - 2 * ln(x) * LMUF * CF * NC * pow(omx, -1)
                + 2 * ln(x) * LMUF * CF * NC
                + 2 * ln(x) * LMUA * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * LMUA * CF * pow(NC, -1)
                - 2 * ln(x) * LMUA * CF * NC * pow(omx, -1)
                + ln(x) * LMUA * CF * NC
                + 123.0 / 4.0 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(x) * z * CF * pow(NC, -1) * pow(omxmz, -2)
                - 8 * ln(x) * z * CF * pow(NC, -1) * pow(omxmz, -1)
                - 57.0 / 2.0 * ln(x) * z * CF * pow(NC, -1)
                - 3 * ln(x) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 75.0 / 4.0 * ln(x) * z * CF * NC * pow(omx, -1)
                + 39.0 / 2.0 * ln(x) * z * CF * NC
                + 2 * ln(x) * z * CF * NC * rln2 * pow(omx, -1)
                + 2 * ln(x) * z * CF * NC * rln2
                + 4 * ln(x) * z * pow(CF, 2)
                - ln(x) * z * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * ln(x) * z * LMUF * CF * pow(NC, -1)
                + ln(x) * z * LMUF * CF * NC * pow(omx, -1)
                - 3.0 / 2.0 * ln(x) * z * LMUF * CF * NC
                - ln(x) * z * LMUA * CF * pow(NC, -1) * pow(omx, -1)
                + 1.0 / 2.0 * ln(x) * z * LMUA * CF * pow(NC, -1)
                + ln(x) * z * LMUA * CF * NC * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * z * LMUA * CF * NC
                - 6 * ln(x) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                + 4 * ln(x) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -1)
                - 8.0 / 3.0 * ln(x) * pow(z, 2) * CF * NC * pow(omx, -1)
                + 16.0 / 3.0 * ln(x) * pow(z, 2) * CF * NC
                + 15.0 / 4.0 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1)
                + 3 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                + 2 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                - 205.0 / 12.0 * ln(x) * x * pow(z, -1) * CF * NC
                - 2 * ln(x) * x * pow(z, -1) * CF * NC * rln2
            )
            tmp += (
                +4 * ln(x) * x * pow(z, -1) * pow(CF, 2)
                + 3.0 / 2.0 * ln(x) * x * pow(z, -1) * LMUF * CF * pow(NC, -1)
                - 3.0 / 2.0 * ln(x) * x * pow(z, -1) * LMUF * CF * NC
                + ln(x) * x * pow(z, -1) * LMUA * CF * pow(NC, -1)
                - ln(x) * x * pow(z, -1) * LMUA * CF * NC
                - 6 * ln(x) * x * CF * pow(NC, -1) * pow(omxmz, -2)
                + 12 * ln(x) * x * CF * pow(NC, -1) * pow(omxmz, -1)
                + 4 * ln(x) * x * CF * pow(NC, -1)
                - 5 * ln(x) * x * CF * NC
                + 2 * ln(x) * x * CF * NC * rln2
                - 2 * ln(x) * x * LMUF * CF * pow(NC, -1)
                + 2 * ln(x) * x * LMUF * CF * NC
                - ln(x) * x * LMUA * CF * pow(NC, -1)
                + ln(x) * x * LMUA * CF * NC
                + 3.0 / 2.0 * ln(x) * x * z * CF * pow(NC, -1)
                + 9.0 / 2.0 * ln(x) * x * z * CF * NC
                + 4 * ln(x) * x * z * pow(CF, 2)
                + 1.0 / 2.0 * ln(x) * x * z * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * x * z * LMUF * CF * NC
                + 1.0 / 2.0 * ln(x) * x * z * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(x) * x * z * LMUA * CF * NC
                - 8.0 / 3.0 * ln(x) * x * pow(z, 2) * CF * NC
                + 6 * ln(x) * pow(x, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                - 6 * ln(x) * pow(x, 2) * CF * pow(NC, -1) * pow(omxmz, -1)
                - 2 * ln(x) * pow(x, 3) * CF * pow(NC, -1) * pow(omxmz, -2)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * NC
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * CF * NC * pow(omx, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * NC * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * NC
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * CF * NC * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF * NC
                + ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * NC
                - ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * CF * NC
                - 17 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 25.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                + 10 * pow(ln(x), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 11.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * NC
                + 24 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 23 * pow(ln(x), 2) * CF * pow(NC, -1)
                - 10 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                + 9 * pow(ln(x), 2) * CF * NC
                - 12 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 31.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                + 5 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                - 17.0 / 2.0 * pow(ln(x), 2) * z * CF * NC
                + 11.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 11.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * CF * NC
                - 9 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                + 9 * pow(ln(x), 2) * x * CF * NC
                + 1.0 / 2.0 * pow(ln(x), 2) * x * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(x), 2) * x * z * CF * NC
                + 16 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 11 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(x) * ln(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 3 * ln(x) * ln(z) * pow(z, -1) * CF * NC
                - 25 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(x) * ln(z) * CF * pow(NC, -1)
                + 19 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                - 16 * ln(x) * ln(z) * CF * NC
                + 25.0 / 2.0 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -17 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 7.0 / 2.0 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                - ln(x) * ln(z) * z * CF * NC
                - 5 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                + 3 * ln(x) * ln(z) * x * pow(z, -1) * CF * NC
                + 10 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(z) * x * CF * NC
                + 20 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 15 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                - 16 * ln(x) * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 8 * ln(x) * ln(omx) * pow(z, -1) * CF * NC
                - 26 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 30 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + 16 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                - 16 * ln(x) * ln(omx) * CF * NC
                + 13 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 19 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                - 8 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                + 15 * ln(x) * ln(omx) * z * CF * NC
                - 5 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                + 8 * ln(x) * ln(omx) * x * pow(z, -1) * CF * NC
                + 10 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 16 * ln(x) * ln(omx) * x * CF * NC
                - ln(x) * ln(omx) * x * z * CF * pow(NC, -1)
                + ln(x) * ln(omx) * x * z * CF * NC
                + 24 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 35.0 / 2.0 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                - 14 * ln(x) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 15.0 / 2.0 * ln(x) * ln(omz) * pow(z, -1) * CF * NC
                - 34 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 33 * ln(x) * ln(omz) * CF * pow(NC, -1)
                + 14 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                - 13 * ln(x) * ln(omz) * CF * NC
                + 17 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 22 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                - 7 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 12 * ln(x) * ln(omz) * z * CF * NC
            )
            tmp += (
                -15.0 / 2.0 * ln(x) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 15.0 / 2.0 * ln(x) * ln(omz) * x * pow(z, -1) * CF * NC
                + 13 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                - 13 * ln(x) * ln(omz) * x * CF * NC
                - ln(x) * ln(omz) * x * z * CF * pow(NC, -1)
                + ln(x) * ln(omz) * x * z * CF * NC
                - 15 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 19 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                - 3 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                + ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                + 1.0 / 3.0 * ln(z) * pow(z, -1) * CF * NF * pow(omx, -1)
                + 12 * ln(z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 19.0 / 3.0 * ln(z) * pow(z, -1) * CF * NC
                - 4 * ln(z) * pow(z, -1) * CF * NC * rln2 * pow(omx, -1)
                + 2 * ln(z) * pow(z, -1) * CF * NC * rln2
                + 8 * ln(z) * pow(z, -1) * pow(CF, 2)
                - ln(z) * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + ln(z) * pow(z, -1) * LMUF * CF * NC
                - 2 * ln(z) * pow(z, -1) * LMUA * CF * NC
                + 28 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 38 * ln(z) * CF * pow(NC, -1)
                + 2 * ln(z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + ln(z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                + ln(z) * CF * pow(NC, -1) * sqrtxz1
                - 10 * ln(z) * CF * NC * pow(omx, -1)
                + 20 * ln(z) * CF * NC
                - 8 * ln(z) * CF * NC * rln2 * pow(omx, -1)
                + 6 * ln(z) * CF * NC * rln2
                - 2 * ln(z) * CF * NC * sqrtxz1 * pow(omx, -1)
                + 2 * ln(z) * CF * NC * sqrtxz1
                - 8 * ln(z) * pow(CF, 2)
                + ln(z) * LMUF * CF * pow(NC, -1)
                - ln(z) * LMUF * CF * NC
                - ln(z) * LMUA * CF * pow(NC, -1)
                - 3 * ln(z) * LMUA * CF * NC
                - 17 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 22 * ln(z) * z * CF * pow(NC, -1)
                - ln(z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + 10 * ln(z) * z * CF * NC * pow(omx, -1)
            )
            tmp += (
                -18 * ln(z) * z * CF * NC
                - 2 * ln(z) * z * CF * NC * rln2 * pow(omx, -1)
                + 6 * ln(z) * z * CF * NC * rln2
                + 4 * ln(z) * z * pow(CF, 2)
                - 1.0 / 2.0 * ln(z) * z * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * z * LMUF * CF * NC
                - 1.0 / 2.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
                - 15.0 / 2.0 * ln(z) * z * LMUA * CF * NC
                - 8.0 / 3.0 * ln(z) * pow(z, 2) * CF * NC
                - 7 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                + ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                + 2 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                + 50.0 / 3.0 * ln(z) * x * pow(z, -1) * CF * NC
                + 2 * ln(z) * x * pow(z, -1) * CF * NC * rln2
                - 8 * ln(z) * x * pow(z, -1) * pow(CF, 2)
                - ln(z) * x * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + ln(z) * x * pow(z, -1) * LMUF * CF * NC
                - 2 * ln(z) * x * pow(z, -1) * LMUA * CF * NC
                - ln(z) * x * CF * pow(NC, -1)
                + 8 * ln(z) * x * CF * NC
                + 6 * ln(z) * x * CF * NC * rln2
                + 8 * ln(z) * x * pow(CF, 2)
                + ln(z) * x * LMUF * CF * pow(NC, -1)
                - ln(z) * x * LMUF * CF * NC
                + ln(z) * x * LMUA * CF * pow(NC, -1)
                - 5 * ln(z) * x * LMUA * CF * NC
                - 2 * ln(z) * x * z * CF * pow(NC, -1)
                - ln(z) * x * z * CF * NC
                - 4 * ln(z) * x * z * pow(CF, 2)
                - 1.0 / 2.0 * ln(z) * x * z * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * x * z * LMUF * CF * NC
                + 1.0 / 2.0 * ln(z) * x * z * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * x * z * LMUA * CF * NC
                + 4.0 / 3.0 * ln(z) * x * pow(z, 2) * CF * NC
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF * NC
                + ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * NC
                - ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -2 * ln(z) * ln(1 + sqrtxz1 - z) * x * CF * NC
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * NC
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * NC * pow(omx, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * NC
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * NC * pow(omx, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * NC
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * NC
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF * NC
                - 4 * ln(z) * ln(1 + z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 4 * ln(z) * ln(1 + z) * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(1 + z) * z * CF * NC * pow(omx, -1)
                - 3 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                + pow(ln(z), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * NC
                + 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * pow(ln(z), 2) * CF * pow(NC, -1)
                - 3 * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                + 7 * pow(ln(z), 2) * CF * NC
                - 3 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 9.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                + 15.0 / 2.0 * pow(ln(z), 2) * z * CF * NC
                + pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 5.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * CF * NC
                - 4 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 9 * pow(ln(z), 2) * x * CF * NC
                - 1.0 / 2.0 * pow(ln(z), 2) * x * z * CF * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * x * z * CF * NC
                - 8 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 7 * ln(z) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                + 8 * ln(z) * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 3 * ln(z) * ln(omx) * pow(z, -1) * CF * NC
                + 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -12 * ln(z) * ln(omx) * CF * pow(NC, -1)
                - 8 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                + 12 * ln(z) * ln(omx) * CF * NC
                - 6 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 9 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                + 4 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                - ln(z) * ln(omx) * z * CF * NC
                + 3 * ln(z) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 3 * ln(z) * ln(omx) * x * pow(z, -1) * CF * NC
                - 6 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 14 * ln(z) * ln(omx) * x * CF * NC
                - 12 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 5 * ln(z) * ln(omz) * pow(z, -1) * CF * NC
                + 20 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 12 * ln(z) * ln(omz) * CF * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                + 10 * ln(z) * ln(omz) * CF * NC
                - 10 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 10 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                + 2 * ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 10 * ln(z) * ln(omz) * z * CF * NC
                + 4 * ln(z) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * pow(z, -1) * CF * NC
                - 8 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                + 10 * ln(z) * ln(omz) * x * CF * NC
                - 18 * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 81.0 / 4.0 * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omx) * pow(z, -1) * CF * NF * pow(omx, -1)
                + 12 * ln(omx) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 103.0 / 12.0 * ln(omx) * pow(z, -1) * CF * NC
                + 8 * ln(omx) * pow(z, -1) * pow(CF, 2)
                - 2 * ln(omx) * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + 2 * ln(omx) * pow(z, -1) * LMUF * CF * NC
                - ln(omx) * pow(z, -1) * LMUA * CF * pow(NC, -1)
                + ln(omx) * pow(z, -1) * LMUA * CF * NC
                + 22 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -27 * ln(omx) * CF * pow(NC, -1)
                - 12 * ln(omx) * CF * NC * pow(omx, -1)
                + 8 * ln(omx) * CF * NC
                - 8 * ln(omx) * pow(CF, 2)
                + 3 * ln(omx) * LMUF * CF * pow(NC, -1)
                - 3 * ln(omx) * LMUF * CF * NC
                + ln(omx) * LMUA * CF * pow(NC, -1)
                - ln(omx) * LMUA * CF * NC
                - 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omx) * z * CF * pow(NC, -1)
                + 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                - 13 * ln(omx) * z * CF * NC
                + 4 * ln(omx) * z * pow(CF, 2)
                - 5.0 / 2.0 * ln(omx) * z * LMUF * CF * pow(NC, -1)
                + 5.0 / 2.0 * ln(omx) * z * LMUF * CF * NC
                - 1.0 / 2.0 * ln(omx) * z * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * z * LMUA * CF * NC
                - 8.0 / 3.0 * ln(omx) * pow(z, 2) * CF * NC
                - 27.0 / 4.0 * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                + 173.0 / 12.0 * ln(omx) * x * pow(z, -1) * CF * NC
                - 8 * ln(omx) * x * pow(z, -1) * pow(CF, 2)
                - 2 * ln(omx) * x * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + 2 * ln(omx) * x * pow(z, -1) * LMUF * CF * NC
                - ln(omx) * x * pow(z, -1) * LMUA * CF * pow(NC, -1)
                + ln(omx) * x * pow(z, -1) * LMUA * CF * NC
                + 2 * ln(omx) * x * CF * pow(NC, -1)
                - ln(omx) * x * CF * NC
                + 8 * ln(omx) * x * pow(CF, 2)
                + 3 * ln(omx) * x * LMUF * CF * pow(NC, -1)
                - 3 * ln(omx) * x * LMUF * CF * NC
                + ln(omx) * x * LMUA * CF * pow(NC, -1)
                - ln(omx) * x * LMUA * CF * NC
                - 3.0 / 2.0 * ln(omx) * x * z * CF * pow(NC, -1)
                - 3.0 / 2.0 * ln(omx) * x * z * CF * NC
                - 4 * ln(omx) * x * z * pow(CF, 2)
                - 1.0 / 2.0 * ln(omx) * x * z * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * x * z * LMUF * CF * NC
                - 1.0 / 2.0 * ln(omx) * x * z * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * x * z * LMUA * CF * NC
                + 4.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF * NC
                - 5 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * pow(ln(omx), 2) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * pow(ln(omx), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 7.0 / 2.0 * pow(ln(omx), 2) * pow(z, -1) * CF * NC
            )
            tmp += (
                +6 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 11 * pow(ln(omx), 2) * CF * pow(NC, -1)
                - 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                + 6 * pow(ln(omx), 2) * CF * NC
                - 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 13.0 / 2.0 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                + 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                - 11.0 / 2.0 * pow(ln(omx), 2) * z * CF * NC
                + 2 * pow(ln(omx), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(omx), 2) * x * pow(z, -1) * CF * NC
                - 3 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 6 * pow(ln(omx), 2) * x * CF * NC
                + 1.0 / 2.0 * pow(ln(omx), 2) * x * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * z * CF * NC
                - 12 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 11 * ln(omx) * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(omx) * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 6 * ln(omx) * ln(omz) * pow(z, -1) * CF * NC
                + 16 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 20 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                - 4 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                + 10 * ln(omx) * ln(omz) * CF * NC
                - 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                + 2 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 9 * ln(omx) * ln(omz) * z * CF * NC
                + 5 * ln(omx) * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(omx) * ln(omz) * x * pow(z, -1) * CF * NC
                - 8 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 10 * ln(omx) * ln(omz) * x * CF * NC
                + ln(omx) * ln(omz) * x * z * CF * pow(NC, -1)
                - ln(omx) * ln(omz) * x * z * CF * NC
                - 24 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 105.0 / 4.0 * ln(omz) * pow(z, -1) * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omz) * pow(z, -1) * CF * NF * pow(omx, -1)
                + 6 * ln(omz) * pow(z, -1) * CF * NC * pow(omx, -1)
            )
            tmp += (
                -31.0 / 12.0 * ln(omz) * pow(z, -1) * CF * NC
                + 8 * ln(omz) * pow(z, -1) * pow(CF, 2)
                - ln(omz) * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + ln(omz) * pow(z, -1) * LMUF * CF * NC
                - ln(omz) * pow(z, -1) * LMUA * CF * pow(NC, -1)
                + 3 * ln(omz) * pow(z, -1) * LMUA * CF * NC
                + 32 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(omz) * CF * pow(NC, -1) * pow(omxmz, -1)
                - 38 * ln(omz) * CF * pow(NC, -1)
                - 6 * ln(omz) * CF * NC * pow(omx, -1)
                + 3 * ln(omz) * CF * NC
                - 8 * ln(omz) * pow(CF, 2)
                + ln(omz) * LMUF * CF * pow(NC, -1)
                - ln(omz) * LMUF * CF * NC
                + ln(omz) * LMUA * CF * pow(NC, -1)
                - 5 * ln(omz) * LMUA * CF * NC
                - 20 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(omz) * z * CF * pow(NC, -1) * pow(omxmz, -2)
                + 8 * ln(omz) * z * CF * pow(NC, -1) * pow(omxmz, -1)
                + 37.0 / 2.0 * ln(omz) * z * CF * pow(NC, -1)
                + 4 * ln(omz) * z * CF * NC * pow(omx, -1)
                - 11.0 / 2.0 * ln(omz) * z * CF * NC
                + 4 * ln(omz) * z * pow(CF, 2)
                - 1.0 / 2.0 * ln(omz) * z * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * z * LMUF * CF * NC
                - 1.0 / 2.0 * ln(omz) * z * LMUA * CF * pow(NC, -1)
                + 9.0 / 2.0 * ln(omz) * z * LMUA * CF * NC
                + 6 * ln(omz) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                - 4 * ln(omz) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -1)
                - 8.0 / 3.0 * ln(omz) * pow(z, 2) * CF * NC
                - 27.0 / 4.0 * ln(omz) * x * pow(z, -1) * CF * pow(NC, -1)
                + 173.0 / 12.0 * ln(omz) * x * pow(z, -1) * CF * NC
                - 8 * ln(omz) * x * pow(z, -1) * pow(CF, 2)
                - ln(omz) * x * pow(z, -1) * LMUF * CF * pow(NC, -1)
                + ln(omz) * x * pow(z, -1) * LMUF * CF * NC
                - ln(omz) * x * pow(z, -1) * LMUA * CF * pow(NC, -1)
                + 3 * ln(omz) * x * pow(z, -1) * LMUA * CF * NC
                + 6 * ln(omz) * x * CF * pow(NC, -1) * pow(omxmz, -2)
                - 12 * ln(omz) * x * CF * pow(NC, -1) * pow(omxmz, -1)
                + 3 * ln(omz) * x * CF * pow(NC, -1)
                - 7 * ln(omz) * x * CF * NC
            )
            tmp += (
                +8 * ln(omz) * x * pow(CF, 2)
                + ln(omz) * x * LMUF * CF * pow(NC, -1)
                - ln(omz) * x * LMUF * CF * NC
                + ln(omz) * x * LMUA * CF * pow(NC, -1)
                - 5 * ln(omz) * x * LMUA * CF * NC
                - 3 * ln(omz) * x * z * CF * NC
                - 4 * ln(omz) * x * z * pow(CF, 2)
                - 1.0 / 2.0 * ln(omz) * x * z * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * x * z * LMUF * CF * NC
                - 1.0 / 2.0 * ln(omz) * x * z * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * x * z * LMUA * CF * NC
                + 4.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF * NC
                - 6 * ln(omz) * pow(x, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                + 6 * ln(omz) * pow(x, 2) * CF * pow(NC, -1) * pow(omxmz, -1)
                + 2 * ln(omz) * pow(x, 3) * CF * pow(NC, -1) * pow(omxmz, -2)
                - 8 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 7 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1)
                + pow(ln(omz), 2) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(z, -1) * CF * NC
                + 12 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 13 * pow(ln(omz), 2) * CF * pow(NC, -1)
                - pow(ln(omz), 2) * CF * NC * pow(omx, -1)
                + 4 * pow(ln(omz), 2) * CF * NC
                - 6 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 17.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC
                + 3 * pow(ln(omz), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * x * pow(z, -1) * CF * NC
                - 5 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                + 4 * pow(ln(omz), 2) * x * CF * NC
                + 1.0 / 2.0 * pow(ln(omz), 2) * x * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * x * z * CF * NC
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * NC * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * NC
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * NC
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * NC * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * NC
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * NC
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * NC
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * NC
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * NC
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * NC * pow(omx, -1)
            )
            tmp += (
                -2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * NC
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * NC
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * NC
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * NC * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * NC
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * NC
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * CF * NC
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * NC * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * NC
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * NC
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * CF * NC
                + 2 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * NC * pow(omx, -1)
                + Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * NC
                - 4 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * CF * NC * pow(omx, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * CF * NC
                + 2 * Li2(1 - x * pow(z, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * z * CF * pow(NC, -1)
                - Li2(1 - x * pow(z, -1)) * z * CF * NC * pow(omx, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * z * CF * NC
                - Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                + Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * CF * NC
                + 2 * Li2(1 - x * pow(z, -1)) * x * CF * pow(NC, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * x * CF * NC
                - 4 * Li2(-z) * pow(z, -1) * CF * NC * pow(omx, -1)
                - 4 * Li2(-z) * CF * NC * pow(omx, -1)
                - 2 * Li2(-z) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * Li2(x) * pow(z, -1) * CF * pow(NC, -1)
                - 1.0 / 2.0 * Li2(x) * pow(z, -1) * CF * NC
                + 2 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(x) * CF * pow(NC, -1)
                - Li2(x) * CF * NC
                - Li2(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(x) * z * CF * pow(NC, -1)
                + Li2(x) * z * CF * NC
                + 3.0 / 2.0 * Li2(x) * x * pow(z, -1) * CF * pow(NC, -1)
                - 1.0 / 2.0 * Li2(x) * x * pow(z, -1) * CF * NC
                - Li2(x) * x * CF * pow(NC, -1)
                - Li2(x) * x * CF * NC
                - 4 * Li2(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * pow(z, -1) * CF * pow(NC, -1)
                - 3 * Li2(z) * pow(z, -1) * CF * NC
                + 6 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(z) * CF * pow(NC, -1)
                - 3 * Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(z) * z * CF * pow(NC, -1)
                - 11 * Li2(z) * z * CF * NC
            )
            tmp += -3 * Li2(z) * x * pow(z, -1) * CF * NC - 2 * Li2(z) * x * CF * NC

            res += tmp

        return res


def c2p_q2g_eq(x, z, rsl, order, f=C2Pq2gEq_DR0123_scheme):
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
