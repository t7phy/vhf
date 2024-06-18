from configs.eh import *


def C2Pq2qEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
    res = 0.0

    if cx == "D" and cz == "D":

        res = (
            -511.0 / 32.0 * CF * pow(NC, -1)
            + 127.0 / 24.0 * CF * NF
            - 1537.0 / 96.0 * CF * NC
            + 8.0 / 3.0 * LMUR * CF * NF
            - 44.0 / 3.0 * LMUR * CF * NC
            - 93.0 / 16.0 * LMUF * CF * pow(NC, -1)
            + 1.0 / 12.0 * LMUF * CF * NF
            + 245.0 / 48.0 * LMUF * CF * NC
            + 1.0 / 2.0 * LMUF * LMUR * CF * NF
            - 11.0 / 4.0 * LMUF * LMUR * CF * NC
            - 9.0 / 16.0 * pow(LMUF, 2) * CF * pow(NC, -1)
            - 1.0 / 4.0 * pow(LMUF, 2) * CF * NF
            + 31.0 / 16.0 * pow(LMUF, 2) * CF * NC
            - 93.0 / 16.0 * LMUA * CF * pow(NC, -1)
            + 1.0 / 12.0 * LMUA * CF * NF
            + 245.0 / 48.0 * LMUA * CF * NC
            + 1.0 / 2.0 * LMUA * LMUR * CF * NF
            - 11.0 / 4.0 * LMUA * LMUR * CF * NC
            - 9.0 / 8.0 * LMUA * LMUF * CF * pow(NC, -1)
            + 9.0 / 8.0 * LMUA * LMUF * CF * NC
            - 9.0 / 16.0 * pow(LMUA, 2) * CF * pow(NC, -1)
            - 1.0 / 4.0 * pow(LMUA, 2) * CF * NF
            + 31.0 / 16.0 * pow(LMUA, 2) * CF * NC
            + 15.0 / 2.0 * zeta3 * CF * pow(NC, -1)
            + 2.0 / 3.0 * zeta3 * CF * NF
            + 41.0 / 6.0 * zeta3 * CF * NC
            + 5 * zeta3 * LMUF * CF * pow(NC, -1)
            - 2 * zeta3 * LMUF * CF * NC
            + 5 * zeta3 * LMUA * CF * pow(NC, -1)
            - 2 * zeta3 * LMUA * CF * NC
            - 29.0 / 24.0 * pow(pi, 2) * CF * pow(NC, -1)
            + 19.0 / 54.0 * pow(pi, 2) * CF * NF
            - 277.0 / 216.0 * pow(pi, 2) * CF * NC
            - 1.0 / 4.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
            + 1.0 / 9.0 * pow(pi, 2) * LMUF * CF * NF
            - 13.0 / 36.0 * pow(pi, 2) * LMUF * CF * NC
            + 1.0 / 6.0 * pow(pi, 2) * pow(LMUF, 2) * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * pow(LMUF, 2) * CF * NC
            - 1.0 / 4.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
            + 1.0 / 9.0 * pow(pi, 2) * LMUA * CF * NF
            - 13.0 / 36.0 * pow(pi, 2) * LMUA * CF * NC
            + 1.0 / 6.0 * pow(pi, 2) * pow(LMUA, 2) * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * pow(LMUA, 2) * CF * NC
            + 7.0 / 180.0 * pow(pi, 4) * CF * pow(NC, -1)
            + 1.0 / 18.0 * pow(pi, 4) * CF * NC
        )

        return res

    if cx == "D" and cz == "0":

        res = (
            28.0 / 27.0 * CF * NF
            - 202.0 / 27.0 * CF * NC
            - 8 * LMUA * CF * pow(NC, -1)
            + 10.0 / 9.0 * LMUA * CF * NF
            + 5.0 / 9.0 * LMUA * CF * NC
            + 2.0 / 3.0 * LMUA * LMUR * CF * NF
            - 11.0 / 3.0 * LMUA * LMUR * CF * NC
            - 3.0 / 2.0 * LMUA * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * LMUA * LMUF * CF * NC
            - 3.0 / 2.0 * pow(LMUA, 2) * CF * pow(NC, -1)
            - 1.0 / 3.0 * pow(LMUA, 2) * CF * NF
            + 10.0 / 3.0 * pow(LMUA, 2) * CF * NC
            - 4 * zeta3 * CF * pow(NC, -1)
            + 11 * zeta3 * CF * NC
            - 1.0 / 9.0 * pow(pi, 2) * CF * NF
            + 11.0 / 18.0 * pow(pi, 2) * CF * NC
            - 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
            + 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * NC
            - 1.0 / 3.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
            + 2.0 / 3.0 * pow(pi, 2) * LMUA * CF * NC
        )

        return res

    if cx == "D" and cz == "1":

        res = (
            8 * CF * pow(NC, -1)
            - 10.0 / 9.0 * CF * NF
            - 5.0 / 9.0 * CF * NC
            - 2.0 / 3.0 * LMUR * CF * NF
            + 11.0 / 3.0 * LMUR * CF * NC
            + 3.0 / 2.0 * LMUF * CF * pow(NC, -1)
            - 3.0 / 2.0 * LMUF * CF * NC
            + 3.0 / 2.0 * LMUA * CF * pow(NC, -1)
            - 3.0 / 2.0 * LMUA * CF * NC
            - 2 * pow(LMUA, 2) * CF * pow(NC, -1)
            + 2 * pow(LMUA, 2) * CF * NC
            + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1)
            - pow(pi, 2) * CF * NC
        )

        return res

    if cx == "D" and cz == "2":

        res = 1.0 / 3.0 * CF * NF - 11.0 / 6.0 * CF * NC + 3 * LMUA * CF * pow(NC, -1) - 3 * LMUA * CF * NC

        return res

    if cx == "D" and cz == "3":

        res = -CF * pow(NC, -1) + CF * NC

        return res

    if cx == "0" and cz == "D":

        res = (
            28.0 / 27.0 * CF * NF
            - 202.0 / 27.0 * CF * NC
            - 8 * LMUF * CF * pow(NC, -1)
            + 10.0 / 9.0 * LMUF * CF * NF
            + 5.0 / 9.0 * LMUF * CF * NC
            + 2.0 / 3.0 * LMUF * LMUR * CF * NF
            - 11.0 / 3.0 * LMUF * LMUR * CF * NC
            - 3.0 / 2.0 * pow(LMUF, 2) * CF * pow(NC, -1)
            - 1.0 / 3.0 * pow(LMUF, 2) * CF * NF
            + 10.0 / 3.0 * pow(LMUF, 2) * CF * NC
            - 3.0 / 2.0 * LMUA * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * LMUA * LMUF * CF * NC
            - 4 * zeta3 * CF * pow(NC, -1)
            + 11 * zeta3 * CF * NC
            - 1.0 / 9.0 * pow(pi, 2) * CF * NF
            + 11.0 / 18.0 * pow(pi, 2) * CF * NC
            - 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
            + 2.0 / 3.0 * pow(pi, 2) * LMUF * CF * NC
            - 1.0 / 3.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
            + 1.0 / 3.0 * pow(pi, 2) * LMUA * CF * NC
        )

        return res

    if cx == "0" and cz == "0":

        res = (
            8 * CF * pow(NC, -1)
            - 10.0 / 9.0 * CF * NF
            - 5.0 / 9.0 * CF * NC
            - 2.0 / 3.0 * LMUR * CF * NF
            + 11.0 / 3.0 * LMUR * CF * NC
            + 3.0 / 2.0 * LMUF * CF * pow(NC, -1)
            - 3.0 / 2.0 * LMUF * CF * NC
            + 3.0 / 2.0 * LMUA * CF * pow(NC, -1)
            - 3.0 / 2.0 * LMUA * CF * NC
            - 2 * LMUA * LMUF * CF * pow(NC, -1)
            + 2 * LMUA * LMUF * CF * NC
            + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1)
            - pow(pi, 2) * CF * NC
        )

        return res

    if cx == "0" and cz == "1":

        res = 2.0 / 3.0 * CF * NF - 11.0 / 3.0 * CF * NC + 2 * LMUF * CF * pow(NC, -1) - 2 * LMUF * CF * NC + 4 * LMUA * CF * pow(NC, -1) - 4 * LMUA * CF * NC

        return res

    if cx == "0" and cz == "2":

        res = -3 * CF * pow(NC, -1) + 3 * CF * NC

        return res

    if cx == "0" and cz == "3":

        res = 0

        return res

    if cx == "1" and cz == "D":

        res = (
            8 * CF * pow(NC, -1)
            - 10.0 / 9.0 * CF * NF
            - 5.0 / 9.0 * CF * NC
            - 2.0 / 3.0 * LMUR * CF * NF
            + 11.0 / 3.0 * LMUR * CF * NC
            + 3.0 / 2.0 * LMUF * CF * pow(NC, -1)
            - 3.0 / 2.0 * LMUF * CF * NC
            - 2 * pow(LMUF, 2) * CF * pow(NC, -1)
            + 2 * pow(LMUF, 2) * CF * NC
            + 3.0 / 2.0 * LMUA * CF * pow(NC, -1)
            - 3.0 / 2.0 * LMUA * CF * NC
            + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1)
            - pow(pi, 2) * CF * NC
        )

        return res

    if cx == "1" and cz == "0":

        res = 2.0 / 3.0 * CF * NF - 11.0 / 3.0 * CF * NC + 4 * LMUF * CF * pow(NC, -1) - 4 * LMUF * CF * NC + 2 * LMUA * CF * pow(NC, -1) - 2 * LMUA * CF * NC

        return res

    if cx == "1" and cz == "1":

        res = -6 * CF * pow(NC, -1) + 6 * CF * NC

        return res

    if cx == "1" and cz == "2":

        res = 0

        return res

    if cx == "1" and cz == "3":

        res = 0

        return res

    if cx == "2" and cz == "D":

        res = 1.0 / 3.0 * CF * NF - 11.0 / 6.0 * CF * NC + 3 * LMUF * CF * pow(NC, -1) - 3 * LMUF * CF * NC

        return res

    if cx == "2" and cz == "0":

        res = -3 * CF * pow(NC, -1) + 3 * CF * NC

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

        res = -CF * pow(NC, -1) + CF * NC

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
            - 1.0 / 4.0 * CF * pow(NC, -1)
            - 11.0 / 9.0 * CF
            - 19.0 / 54.0 * CF * NF
            + 197.0 / 108.0 * CF * NC
            - 1.0 / 3.0 * LMUR * CF * NF
            + 11.0 / 6.0 * LMUR * CF * NC
            + 3.0 / 4.0 * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * LMUF * CF * NC
            + 7.0 / 4.0 * LMUA * CF * pow(NC, -1)
            + 10.0 / 3.0 * LMUA * CF
            + 1.0 / 9.0 * LMUA * CF * NF
            - 169.0 / 36.0 * LMUA * CF * NC
            - 1.0 / 3.0 * LMUA * LMUR * CF * NF
            + 11.0 / 6.0 * LMUA * LMUR * CF * NC
            + 3.0 / 4.0 * LMUA * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * LMUA * LMUF * CF * NC
            + 5.0 / 4.0 * pow(LMUA, 2) * CF * pow(NC, -1)
            + 1.0 / 4.0 * pow(LMUA, 2) * CF
            + 1.0 / 6.0 * pow(LMUA, 2) * CF * NF
            - 13.0 / 6.0 * pow(LMUA, 2) * CF * NC
            + 1.0 / 4.0 * z * CF * pow(NC, -1)
            - 4.0 / 9.0 * z * CF
            - 37.0 / 54.0 * z * CF * NF
            + 611.0 / 108.0 * z * CF * NC
            + 1.0 / 3.0 * z * LMUR * CF * NF
            - 11.0 / 6.0 * z * LMUR * CF * NC
            - 3.0 / 4.0 * z * LMUF * CF * pow(NC, -1)
            + 3.0 / 4.0 * z * LMUF * CF * NC
            + 25.0 / 4.0 * z * LMUA * CF * pow(NC, -1)
            - 7.0 / 3.0 * z * LMUA * CF
            - 11.0 / 9.0 * z * LMUA * CF * NF
            + 149.0 / 36.0 * z * LMUA * CF * NC
            - 1.0 / 3.0 * z * LMUA * LMUR * CF * NF
            + 11.0 / 6.0 * z * LMUA * LMUR * CF * NC
            + 3.0 / 4.0 * z * LMUA * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * z * LMUA * LMUF * CF * NC
            + 1.0 / 4.0 * z * pow(LMUA, 2) * CF * pow(NC, -1)
            - 1.0 / 4.0 * z * pow(LMUA, 2) * CF
            + 1.0 / 6.0 * z * pow(LMUA, 2) * CF * NF
            - 7.0 / 6.0 * z * pow(LMUA, 2) * CF * NC
            + 287.0 / 108.0 * pow(z, 2) * CF
            - 25.0 / 18.0 * pow(z, 2) * LMUA * CF
            - 1.0 / 3.0 * pow(z, 2) * pow(LMUA, 2) * CF
            + 10 * zeta3 * CF * pow(NC, -1) * pow(omz, -1)
            - 4 * zeta3 * CF * pow(NC, -1)
            + 2 * zeta3 * CF
            - 14 * zeta3 * CF * NC * pow(omz, -1)
            + 5.0 / 2.0 * zeta3 * CF * NC
            - 4 * zeta3 * z * CF * pow(NC, -1)
            + 2 * zeta3 * z * CF
            + 5.0 / 2.0 * zeta3 * z * CF * NC
            - 1.0 / 4.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
            + 7.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * CF
        )
        res += (
            +1.0 / 18.0 * pow(pi, 2) * CF * NF
            + 1.0 / 4.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
            - 29.0 / 36.0 * pow(pi, 2) * CF * NC
            + 1.0 / 6.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * LMUF * CF * NC
            + 1.0 / 4.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * LMUA * CF
            - 5.0 / 12.0 * pow(pi, 2) * LMUA * CF * NC
            + 1.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1)
            - 1.0 / 4.0 * pow(pi, 2) * z * CF
            + 1.0 / 18.0 * pow(pi, 2) * z * CF * NF
            - 2.0 / 9.0 * pow(pi, 2) * z * CF * NC
            + 1.0 / 6.0 * pow(pi, 2) * z * LMUF * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * z * LMUF * CF * NC
            + 1.0 / 4.0 * pow(pi, 2) * z * LMUA * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * z * LMUA * CF
            - 5.0 / 12.0 * pow(pi, 2) * z * LMUA * CF * NC
            - 7.0 / 18.0 * ln(z) * pow(z, -1) * CF
            - 2.0 / 3.0 * ln(z) * pow(z, -1) * LMUA * CF
            + 19.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
            - 15.0 / 4.0 * ln(z) * CF * pow(NC, -1)
            - 5 * ln(z) * CF
            - 5.0 / 9.0 * ln(z) * CF * NF * pow(omz, -1)
            - 1.0 / 18.0 * ln(z) * CF * NF
            - 113.0 / 18.0 * ln(z) * CF * NC * pow(omz, -1)
            + 233.0 / 36.0 * ln(z) * CF * NC
            - 2.0 / 3.0 * ln(z) * LMUR * CF * NF * pow(omz, -1)
            + 1.0 / 3.0 * ln(z) * LMUR * CF * NF
            + 11.0 / 3.0 * ln(z) * LMUR * CF * NC * pow(omz, -1)
            - 11.0 / 6.0 * ln(z) * LMUR * CF * NC
            + 3.0 / 2.0 * ln(z) * LMUF * CF * pow(NC, -1) * pow(omz, -1)
            - 3.0 / 4.0 * ln(z) * LMUF * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(z) * LMUF * CF * NC * pow(omz, -1)
            + 3.0 / 4.0 * ln(z) * LMUF * CF * NC
            + 3 * ln(z) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
            - 17.0 / 4.0 * ln(z) * LMUA * CF * pow(NC, -1)
            + 1.0 / 2.0 * ln(z) * LMUA * CF
            + 2.0 / 3.0 * ln(z) * LMUA * CF * NF * pow(omz, -1)
            - 1.0 / 3.0 * ln(z) * LMUA * CF * NF
            - 20.0 / 3.0 * ln(z) * LMUA * CF * NC * pow(omz, -1)
            + 61.0 / 12.0 * ln(z) * LMUA * CF * NC
            + ln(z) * pow(LMUA, 2) * CF * pow(NC, -1) * pow(omz, -1)
            - 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * CF * pow(NC, -1)
            + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF
        )
        res += (
            -ln(z) * pow(LMUA, 2) * CF * NC * pow(omz, -1)
            + 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * CF * NC
            - 29.0 / 4.0 * ln(z) * z * CF * pow(NC, -1)
            - 9.0 / 2.0 * ln(z) * z * CF
            + 11.0 / 18.0 * ln(z) * z * CF * NF
            + 101.0 / 36.0 * ln(z) * z * CF * NC
            + 1.0 / 3.0 * ln(z) * z * LMUR * CF * NF
            - 11.0 / 6.0 * ln(z) * z * LMUR * CF * NC
            - 3.0 / 4.0 * ln(z) * z * LMUF * CF * pow(NC, -1)
            + 3.0 / 4.0 * ln(z) * z * LMUF * CF * NC
            - 7.0 / 4.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
            + 2 * ln(z) * z * LMUA * CF
            - 1.0 / 3.0 * ln(z) * z * LMUA * CF * NF
            + 31.0 / 12.0 * ln(z) * z * LMUA * CF * NC
            - 3.0 / 4.0 * ln(z) * z * pow(LMUA, 2) * CF * pow(NC, -1)
            + 1.0 / 2.0 * ln(z) * z * pow(LMUA, 2) * CF
            + 3.0 / 4.0 * ln(z) * z * pow(LMUA, 2) * CF * NC
            - 31.0 / 18.0 * ln(z) * pow(z, 2) * CF
            + 2.0 / 3.0 * ln(z) * pow(z, 2) * LMUA * CF
            + 1.0 / 2.0 * ln(z) * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
            - 1.0 / 3.0 * ln(z) * pow(pi, 2) * CF * pow(NC, -1)
            + 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF
            - 5.0 / 6.0 * ln(z) * pow(pi, 2) * CF * NC * pow(omz, -1)
            + 1.0 / 2.0 * ln(z) * pow(pi, 2) * CF * NC
            - 1.0 / 3.0 * ln(z) * pow(pi, 2) * z * CF * pow(NC, -1)
            + 1.0 / 6.0 * ln(z) * pow(pi, 2) * z * CF
            + 1.0 / 2.0 * ln(z) * pow(pi, 2) * z * CF * NC
            + 1.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF
            - 9.0 / 8.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
            + 21.0 / 8.0 * pow(ln(z), 2) * CF * pow(NC, -1)
            - 1.0 / 8.0 * pow(ln(z), 2) * CF
            - 1.0 / 6.0 * pow(ln(z), 2) * CF * NF * pow(omz, -1)
            + 1.0 / 12.0 * pow(ln(z), 2) * CF * NF
            + 49.0 / 24.0 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
            - 25.0 / 12.0 * pow(ln(z), 2) * CF * NC
            - 3 * pow(ln(z), 2) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
            + 2 * pow(ln(z), 2) * LMUA * CF * pow(NC, -1)
            - pow(ln(z), 2) * LMUA * CF
            + 2 * pow(ln(z), 2) * LMUA * CF * NC * pow(omz, -1)
            - 3.0 / 2.0 * pow(ln(z), 2) * LMUA * CF * NC
            + 7.0 / 8.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
            - 5.0 / 8.0 * pow(ln(z), 2) * z * CF
            + 1.0 / 12.0 * pow(ln(z), 2) * z * CF * NF
        )
        res += (
            -5.0 / 6.0 * pow(ln(z), 2) * z * CF * NC
            + 2 * pow(ln(z), 2) * z * LMUA * CF * pow(NC, -1)
            - pow(ln(z), 2) * z * LMUA * CF
            - 3.0 / 2.0 * pow(ln(z), 2) * z * LMUA * CF * NC
            + 5.0 / 3.0 * pow(ln(z), 3) * CF * pow(NC, -1) * pow(omz, -1)
            - 25.0 / 24.0 * pow(ln(z), 3) * CF * pow(NC, -1)
            + 5.0 / 12.0 * pow(ln(z), 3) * CF
            - 5.0 / 6.0 * pow(ln(z), 3) * CF * NC * pow(omz, -1)
            + 5.0 / 8.0 * pow(ln(z), 3) * CF * NC
            - 25.0 / 24.0 * pow(ln(z), 3) * z * CF * pow(NC, -1)
            + 5.0 / 12.0 * pow(ln(z), 3) * z * CF
            + 5.0 / 8.0 * pow(ln(z), 3) * z * CF * NC
            + 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
            - 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * CF * pow(NC, -1)
            - 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * CF * NC * pow(omz, -1)
            + 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * CF * NC
            - 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * z * CF * pow(NC, -1)
            + 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * z * CF * NC
            - 3.0 / 2.0 * ln(z) * ln(omz) * CF * pow(NC, -1)
            + 3.0 / 2.0 * ln(z) * ln(omz) * CF * NC
            + 2 * ln(z) * ln(omz) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
            - ln(z) * ln(omz) * LMUA * CF * pow(NC, -1)
            - 2 * ln(z) * ln(omz) * LMUA * CF * NC * pow(omz, -1)
            + ln(z) * ln(omz) * LMUA * CF * NC
            + 3.0 / 2.0 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(z) * ln(omz) * z * CF * NC
            - ln(z) * ln(omz) * z * LMUA * CF * pow(NC, -1)
            + ln(z) * ln(omz) * z * LMUA * CF * NC
            - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
            + ln(z) * pow(ln(omz), 2) * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF
            + 5.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
            - 2 * ln(z) * pow(ln(omz), 2) * CF * NC
            + ln(z) * pow(ln(omz), 2) * z * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * z * CF
            - 2 * ln(z) * pow(ln(omz), 2) * z * CF * NC
            + 4 * ln(z) * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
            - 2 * ln(z) * Li2(z) * CF * pow(NC, -1)
        )
        res += (
            -6 * ln(z) * Li2(z) * CF * NC * pow(omz, -1)
            + 3 * ln(z) * Li2(z) * CF * NC
            - 2 * ln(z) * Li2(z) * z * CF * pow(NC, -1)
            + 3 * ln(z) * Li2(z) * z * CF * NC
            - 7.0 / 18.0 * ln(omz) * pow(z, -1) * CF
            - 2.0 / 3.0 * ln(omz) * pow(z, -1) * LMUA * CF
            - 5.0 / 4.0 * ln(omz) * CF * pow(NC, -1)
            - 10.0 / 3.0 * ln(omz) * CF
            + 2.0 / 9.0 * ln(omz) * CF * NF
            + 67.0 / 36.0 * ln(omz) * CF * NC
            + 1.0 / 3.0 * ln(omz) * LMUR * CF * NF
            - 11.0 / 6.0 * ln(omz) * LMUR * CF * NC
            - 3.0 / 4.0 * ln(omz) * LMUF * CF * pow(NC, -1)
            + 3.0 / 4.0 * ln(omz) * LMUF * CF * NC
            - 3.0 / 4.0 * ln(omz) * LMUA * CF * pow(NC, -1)
            - 1.0 / 2.0 * ln(omz) * LMUA * CF
            + 3.0 / 4.0 * ln(omz) * LMUA * CF * NC
            + ln(omz) * pow(LMUA, 2) * CF * pow(NC, -1)
            - ln(omz) * pow(LMUA, 2) * CF * NC
            - 7 * ln(omz) * z * CF * pow(NC, -1)
            + 7.0 / 3.0 * ln(omz) * z * CF
            + 8.0 / 9.0 * ln(omz) * z * CF * NF
            - 14.0 / 9.0 * ln(omz) * z * CF * NC
            + 1.0 / 3.0 * ln(omz) * z * LMUR * CF * NF
            - 11.0 / 6.0 * ln(omz) * z * LMUR * CF * NC
            - 3.0 / 4.0 * ln(omz) * z * LMUF * CF * pow(NC, -1)
            + 3.0 / 4.0 * ln(omz) * z * LMUF * CF * NC
            - 3.0 / 4.0 * ln(omz) * z * LMUA * CF * pow(NC, -1)
            + 1.0 / 2.0 * ln(omz) * z * LMUA * CF
            + 3.0 / 4.0 * ln(omz) * z * LMUA * CF * NC
            + ln(omz) * z * pow(LMUA, 2) * CF * pow(NC, -1)
            - ln(omz) * z * pow(LMUA, 2) * CF * NC
            + 25.0 / 18.0 * ln(omz) * pow(z, 2) * CF
            + 2.0 / 3.0 * ln(omz) * pow(z, 2) * LMUA * CF
            - 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
            - 5.0 / 12.0 * ln(omz) * pow(pi, 2) * CF * pow(NC, -1)
            + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * CF
            - 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF * NC * pow(omz, -1)
            + 3.0 / 4.0 * ln(omz) * pow(pi, 2) * CF * NC
            - 5.0 / 12.0 * ln(omz) * pow(pi, 2) * z * CF * pow(NC, -1)
            + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * z * CF
            + 3.0 / 4.0 * ln(omz) * pow(pi, 2) * z * CF * NC
            + 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF
            + 1.0 / 4.0 * pow(ln(omz), 2) * CF
            - 1.0 / 6.0 * pow(ln(omz), 2) * CF * NF
        )
        res += (
            +11.0 / 12.0 * pow(ln(omz), 2) * CF * NC
            - 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * CF * pow(NC, -1)
            + 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * CF * NC
            - 1.0 / 4.0 * pow(ln(omz), 2) * z * CF
            - 1.0 / 6.0 * pow(ln(omz), 2) * z * CF * NF
            + 11.0 / 12.0 * pow(ln(omz), 2) * z * CF * NC
            - 3.0 / 2.0 * pow(ln(omz), 2) * z * LMUA * CF * pow(NC, -1)
            + 3.0 / 2.0 * pow(ln(omz), 2) * z * LMUA * CF * NC
            - 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF
            + 1.0 / 2.0 * pow(ln(omz), 3) * CF * pow(NC, -1)
            - 1.0 / 2.0 * pow(ln(omz), 3) * CF * NC
            + 1.0 / 2.0 * pow(ln(omz), 3) * z * CF * pow(NC, -1)
            - 1.0 / 2.0 * pow(ln(omz), 3) * z * CF * NC
            + 1.0 / 2.0 * ln(omz) * Li2(1 - z) * CF * pow(NC, -1)
            - ln(omz) * Li2(1 - z) * CF
            - 1.0 / 2.0 * ln(omz) * Li2(1 - z) * CF * NC
            + 1.0 / 2.0 * ln(omz) * Li2(1 - z) * z * CF * pow(NC, -1)
            - ln(omz) * Li2(1 - z) * z * CF
            - 1.0 / 2.0 * ln(omz) * Li2(1 - z) * z * CF * NC
            + ln(omz) * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
            + 1.0 / 2.0 * ln(omz) * Li2(z) * CF * pow(NC, -1)
            - 2 * ln(omz) * Li2(z) * CF
            + ln(omz) * Li2(z) * CF * NC * pow(omz, -1)
            - 3.0 / 2.0 * ln(omz) * Li2(z) * CF * NC
            + 1.0 / 2.0 * ln(omz) * Li2(z) * z * CF * pow(NC, -1)
            - 2 * ln(omz) * Li2(z) * z * CF
            - 3.0 / 2.0 * ln(omz) * Li2(z) * z * CF * NC
            + 3 * Li3(1 - z) * CF * pow(NC, -1) * pow(omz, -1)
            - Li3(1 - z) * CF * pow(NC, -1)
            - Li3(1 - z) * CF
            + 3 * Li3(1 - z) * CF * NC * pow(omz, -1)
            - 2 * Li3(1 - z) * CF * NC
            - Li3(1 - z) * z * CF * pow(NC, -1)
            - Li3(1 - z) * z * CF
            - 2 * Li3(1 - z) * z * CF * NC
            - 10 * Li3(z) * CF * pow(NC, -1) * pow(omz, -1)
            + 6 * Li3(z) * CF * pow(NC, -1)
            - 2 * Li3(z) * CF
            + 14 * Li3(z) * CF * NC * pow(omz, -1)
            - 8 * Li3(z) * CF * NC
            + 6 * Li3(z) * z * CF * pow(NC, -1)
            - 2 * Li3(z) * z * CF
            - 8 * Li3(z) * z * CF * NC
            - 2.0 / 3.0 * Li2(z) * pow(z, -1) * CF
            + 3.0 / 2.0 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
            - 9.0 / 2.0 * Li2(z) * CF * pow(NC, -1)
        )
        res += (
            +1.0 / 2.0 * Li2(z) * CF
            - 3.0 / 2.0 * Li2(z) * CF * NC * pow(omz, -1)
            + 7.0 / 2.0 * Li2(z) * CF * NC
            - 1.0 / 2.0 * Li2(z) * LMUA * CF * pow(NC, -1)
            + Li2(z) * LMUA * CF
            + 1.0 / 2.0 * Li2(z) * LMUA * CF * NC
            + 2 * Li2(z) * z * CF
            - Li2(z) * z * CF * NC
            - 1.0 / 2.0 * Li2(z) * z * LMUA * CF * pow(NC, -1)
            + Li2(z) * z * LMUA * CF
            + 1.0 / 2.0 * Li2(z) * z * LMUA * CF * NC
            + 2.0 / 3.0 * Li2(z) * pow(z, 2) * CF
        )

        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = (
            -7.0 / 18.0 * pow(z, -1) * CF
            - 2.0 / 3.0 * pow(z, -1) * LMUA * CF
            - CF * pow(NC, -1)
            - 10.0 / 3.0 * CF
            + 2.0 / 9.0 * CF * NF
            + 19.0 / 9.0 * CF * NC
            + 1.0 / 3.0 * LMUR * CF * NF
            - 11.0 / 6.0 * LMUR * CF * NC
            + 1.0 / 4.0 * LMUF * CF * pow(NC, -1)
            - 1.0 / 4.0 * LMUF * CF * NC
            - 7.0 / 4.0 * LMUA * CF * pow(NC, -1)
            - 1.0 / 2.0 * LMUA * CF
            + 7.0 / 4.0 * LMUA * CF * NC
            + LMUA * LMUF * CF * pow(NC, -1)
            - LMUA * LMUF * CF * NC
            - 7 * z * CF * pow(NC, -1)
            + 7.0 / 3.0 * z * CF
            + 8.0 / 9.0 * z * CF * NF
            - 14.0 / 9.0 * z * CF * NC
            + 1.0 / 3.0 * z * LMUR * CF * NF
            - 11.0 / 6.0 * z * LMUR * CF * NC
            - 7.0 / 4.0 * z * LMUF * CF * pow(NC, -1)
            + 7.0 / 4.0 * z * LMUF * CF * NC
            + 1.0 / 4.0 * z * LMUA * CF * pow(NC, -1)
            + 1.0 / 2.0 * z * LMUA * CF
            - 1.0 / 4.0 * z * LMUA * CF * NC
            + z * LMUA * LMUF * CF * pow(NC, -1)
            - z * LMUA * LMUF * CF * NC
            + 25.0 / 18.0 * pow(z, 2) * CF
            + 2.0 / 3.0 * pow(z, 2) * LMUA * CF
            - 5.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * CF
            + 7.0 / 12.0 * pow(pi, 2) * CF * NC
            - 5.0 / 12.0 * pow(pi, 2) * z * CF * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * z * CF
            + 7.0 / 12.0 * pow(pi, 2) * z * CF * NC
            + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF
            - 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
            + 7.0 / 2.0 * ln(z) * CF * pow(NC, -1)
            - 1.0 / 2.0 * ln(z) * CF
            + 3.0 / 2.0 * ln(z) * CF * NC * pow(omz, -1)
            - 5.0 / 2.0 * ln(z) * CF * NC
            + 2 * ln(z) * LMUF * CF * pow(NC, -1) * pow(omz, -1)
            - ln(z) * LMUF * CF * pow(NC, -1)
            - 2 * ln(z) * LMUF * CF * NC * pow(omz, -1)
            + ln(z) * LMUF * CF * NC
            - 2 * ln(z) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
            + 3.0 / 2.0 * ln(z) * LMUA * CF * pow(NC, -1)
            - ln(z) * LMUA * CF
            + 2 * ln(z) * LMUA * CF * NC * pow(omz, -1)
            - 3.0 / 2.0 * ln(z) * LMUA * CF * NC
            + ln(z) * z * CF * pow(NC, -1)
            - 2 * ln(z) * z * CF
            - ln(z) * z * LMUF * CF * pow(NC, -1)
            + ln(z) * z * LMUF * CF * NC
            + 3.0 / 2.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
            - ln(z) * z * LMUA * CF
            - 3.0 / 2.0 * ln(z) * z * LMUA * CF * NC
        )
        res += (
            -2.0 / 3.0 * ln(z) * pow(z, 2) * CF
            + 3 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
            - 2 * pow(ln(z), 2) * CF * pow(NC, -1)
            + pow(ln(z), 2) * CF
            - 2 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
            + 3.0 / 2.0 * pow(ln(z), 2) * CF * NC
            - 2 * pow(ln(z), 2) * z * CF * pow(NC, -1)
            + pow(ln(z), 2) * z * CF
            + 3.0 / 2.0 * pow(ln(z), 2) * z * CF * NC
            - 2 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
            + ln(z) * ln(omz) * CF * pow(NC, -1)
            + 2 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
            - ln(z) * ln(omz) * CF * NC
            + ln(z) * ln(omz) * z * CF * pow(NC, -1)
            - ln(z) * ln(omz) * z * CF * NC
            + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF
            + 1.0 / 2.0 * ln(omz) * CF
            - 1.0 / 3.0 * ln(omz) * CF * NF
            + 11.0 / 6.0 * ln(omz) * CF * NC
            - ln(omz) * LMUF * CF * pow(NC, -1)
            + ln(omz) * LMUF * CF * NC
            - 2 * ln(omz) * LMUA * CF * pow(NC, -1)
            + 2 * ln(omz) * LMUA * CF * NC
            - 1.0 / 2.0 * ln(omz) * z * CF
            - 1.0 / 3.0 * ln(omz) * z * CF * NF
            + 11.0 / 6.0 * ln(omz) * z * CF * NC
            - ln(omz) * z * LMUF * CF * pow(NC, -1)
            + ln(omz) * z * LMUF * CF * NC
            - 2 * ln(omz) * z * LMUA * CF * pow(NC, -1)
            + 2 * ln(omz) * z * LMUA * CF * NC
            - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF
            + 3.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1)
            - 3.0 / 2.0 * pow(ln(omz), 2) * CF * NC
            + 3.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
            - 3.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC
            + 1.0 / 2.0 * Li2(z) * CF * pow(NC, -1)
            - Li2(z) * CF
            - 1.0 / 2.0 * Li2(z) * CF * NC
            + 1.0 / 2.0 * Li2(z) * z * CF * pow(NC, -1)
            - Li2(z) * z * CF
            - 1.0 / 2.0 * Li2(z) * z * CF * NC
        )

        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = (
            2.0 / 3.0 * pow(z, -1) * CF
            + 1.0 / 2.0 * CF
            - 1.0 / 3.0 * CF * NF
            + 11.0 / 6.0 * CF * NC
            - 2 * LMUF * CF * pow(NC, -1)
            + 2 * LMUF * CF * NC
            - LMUA * CF * pow(NC, -1)
            + LMUA * CF * NC
            - 1.0 / 2.0 * z * CF
            - 1.0 / 3.0 * z * CF * NF
            + 11.0 / 6.0 * z * CF * NC
            - 2 * z * LMUF * CF * pow(NC, -1)
            + 2 * z * LMUF * CF * NC
            - z * LMUA * CF * pow(NC, -1)
            + z * LMUA * CF * NC
            - 2.0 / 3.0 * pow(z, 2) * CF
            - 1.0 / 2.0 * ln(z) * CF * pow(NC, -1)
            + ln(z) * CF
            + 1.0 / 2.0 * ln(z) * CF * NC
            - 1.0 / 2.0 * ln(z) * z * CF * pow(NC, -1)
            + ln(z) * z * CF
            + 1.0 / 2.0 * ln(z) * z * CF * NC
            + 3 * ln(omz) * CF * pow(NC, -1)
            - 3 * ln(omz) * CF * NC
            + 3 * ln(omz) * z * CF * pow(NC, -1)
            - 3 * ln(omz) * z * CF * NC
        )

        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 3.0 / 2.0 * CF * pow(NC, -1) - 3.0 / 2.0 * CF * NC + 3.0 / 2.0 * z * CF * pow(NC, -1) - 3.0 / 2.0 * z * CF * NC

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
            -35.0 / 4.0 * CF * pow(NC, -1)
            + 9 * CF
            + 23.0 / 54.0 * CF * NF
            - 28.0 / 9.0 * CF * pow(NF, 2)
            + 2393.0 / 108.0 * CF * NC
            - 78 * pow(CF, 2)
            - 1.0 / 3.0 * LMUR * CF * NF
            + 11.0 / 6.0 * LMUR * CF * NC
            + 11.0 / 4.0 * LMUF * CF * pow(NC, -1)
            + 3 * LMUF * CF
            + 1.0 / 9.0 * LMUF * CF * NF
            - 205.0 / 36.0 * LMUF * CF * NC
            + 2 * LMUF * pow(CF, 2)
            - 1.0 / 3.0 * LMUF * LMUR * CF * NF
            + 11.0 / 6.0 * LMUF * LMUR * CF * NC
            + 5.0 / 4.0 * pow(LMUF, 2) * CF * pow(NC, -1)
            + 5.0 / 4.0 * pow(LMUF, 2) * CF
            + 1.0 / 6.0 * pow(LMUF, 2) * CF * NF
            - 13.0 / 6.0 * pow(LMUF, 2) * CF * NC
            - 9.0 / 4.0 * LMUA * CF * pow(NC, -1)
            + 9.0 / 4.0 * LMUA * CF * NC
            - 6 * LMUA * pow(CF, 2)
            + 3.0 / 4.0 * LMUA * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * LMUA * LMUF * CF * NC
            + 33.0 / 4.0 * x * CF * pow(NC, -1)
            - 9 * x * CF
            - 79.0 / 54.0 * x * CF * NF
            + 28.0 / 9.0 * x * CF * pow(NF, 2)
            - 1639.0 / 108.0 * x * CF * NC
            + 78 * x * pow(CF, 2)
            + 1.0 / 3.0 * x * LMUR * CF * NF
            - 11.0 / 6.0 * x * LMUR * CF * NC
            + 21.0 / 4.0 * x * LMUF * CF * pow(NC, -1)
            - 3 * x * LMUF * CF
            - 11.0 / 9.0 * x * LMUF * CF * NF
            + 185.0 / 36.0 * x * LMUF * CF * NC
            - 2 * x * LMUF * pow(CF, 2)
            - 1.0 / 3.0 * x * LMUF * LMUR * CF * NF
            + 11.0 / 6.0 * x * LMUF * LMUR * CF * NC
            + 1.0 / 4.0 * x * pow(LMUF, 2) * CF * pow(NC, -1)
            - 5.0 / 4.0 * x * pow(LMUF, 2) * CF
            + 1.0 / 6.0 * x * pow(LMUF, 2) * CF * NF
            - 7.0 / 6.0 * x * pow(LMUF, 2) * CF * NC
            + 9.0 / 4.0 * x * LMUA * CF * pow(NC, -1)
            - 9.0 / 4.0 * x * LMUA * CF * NC
            + 6 * x * LMUA * pow(CF, 2)
            + 3.0 / 4.0 * x * LMUA * LMUF * CF * pow(NC, -1)
            - 3.0 / 4.0 * x * LMUA * LMUF * CF * NC
            - 7 * zeta3 * CF * pow(NC, -1) * pow(omx, -1)
            + 11.0 / 2.0 * zeta3 * CF * pow(NC, -1)
            + 5 * zeta3 * CF * NC * pow(omx, -1)
            - 8 * zeta3 * CF * NC
            + 11.0 / 2.0 * zeta3 * x * CF * pow(NC, -1)
            - 8 * zeta3 * x * CF * NC
            + 1.0 / 4.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
            + 1.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
            - 1.0 / 2.0 * pow(pi, 2) * CF
            - 1.0 / 9.0 * pow(pi, 2) * CF * NF * pow(omx, -1)
            + 1.0 / 9.0 * pow(pi, 2) * CF * NF
        )
        res += (
            +13.0 / 36.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
            - 13.0 / 36.0 * pow(pi, 2) * CF * NC
            + 1.0 / 4.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * LMUF * CF
            - 5.0 / 12.0 * pow(pi, 2) * LMUF * CF * NC
            + 1.0 / 6.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * LMUA * CF * NC
            + 1.0 / 12.0 * pow(pi, 2) * x * CF * pow(NC, -1)
            + 1.0 / 2.0 * pow(pi, 2) * x * CF
            + 1.0 / 9.0 * pow(pi, 2) * x * CF * NF
            - 1.0 / 9.0 * pow(pi, 2) * x * CF * NC
            - 4.0 / 3.0 * pow(pi, 2) * x * pow(CF, 2)
            + 1.0 / 4.0 * pow(pi, 2) * x * LMUF * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * x * LMUF * CF
            - 5.0 / 12.0 * pow(pi, 2) * x * LMUF * CF * NC
            + 1.0 / 6.0 * pow(pi, 2) * x * LMUA * CF * pow(NC, -1)
            - 1.0 / 6.0 * pow(pi, 2) * x * LMUA * CF * NC
            - 10 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
            + 29.0 / 4.0 * ln(x) * CF * pow(NC, -1)
            + 25.0 / 4.0 * ln(x) * CF
            + 5.0 / 3.0 * ln(x) * CF * NF * pow(omx, -1)
            - 1.0 / 6.0 * ln(x) * CF * NF
            - 11.0 / 3.0 * ln(x) * CF * pow(NF, 2)
            - 5.0 / 3.0 * ln(x) * CF * NC * pow(omx, -1)
            + 13.0 / 12.0 * ln(x) * CF * NC
            - 18 * ln(x) * pow(CF, 2)
            + 2.0 / 3.0 * ln(x) * LMUR * CF * NF * pow(omx, -1)
            - 1.0 / 3.0 * ln(x) * LMUR * CF * NF
            - 11.0 / 3.0 * ln(x) * LMUR * CF * NC * pow(omx, -1)
            + 11.0 / 6.0 * ln(x) * LMUR * CF * NC
            - 3 * ln(x) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
            + 11.0 / 4.0 * ln(x) * LMUF * CF * pow(NC, -1)
            + 3 * ln(x) * LMUF * CF
            + 2.0 / 3.0 * ln(x) * LMUF * CF * NF * pow(omx, -1)
            - 1.0 / 3.0 * ln(x) * LMUF * CF * NF
            - 2.0 / 3.0 * ln(x) * LMUF * CF * NC * pow(omx, -1)
            - 23.0 / 12.0 * ln(x) * LMUF * CF * NC
            + 4 * ln(x) * LMUF * pow(CF, 2)
            + ln(x) * pow(LMUF, 2) * CF * pow(NC, -1) * pow(omx, -1)
            - 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * CF * pow(NC, -1)
            + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * CF
            - ln(x) * pow(LMUF, 2) * CF * NC * pow(omx, -1)
            + 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * CF * NC
            - 3.0 / 2.0 * ln(x) * LMUA * CF * pow(NC, -1) * pow(omx, -1)
            + 3.0 / 4.0 * ln(x) * LMUA * CF * pow(NC, -1)
        )
        res += (
            +3.0 / 2.0 * ln(x) * LMUA * CF * NC * pow(omx, -1)
            - 3.0 / 4.0 * ln(x) * LMUA * CF * NC
            + 6 * ln(x) * x * CF * pow(NC, -1)
            - 3.0 / 4.0 * ln(x) * x * CF
            - 11.0 / 6.0 * ln(x) * x * CF * NF
            + 5.0 / 3.0 * ln(x) * x * CF * pow(NF, 2)
            + 61.0 / 6.0 * ln(x) * x * CF * NC
            - 32 * ln(x) * x * pow(CF, 2)
            - 1.0 / 3.0 * ln(x) * x * LMUR * CF * NF
            + 11.0 / 6.0 * ln(x) * x * LMUR * CF * NC
            - 11.0 / 4.0 * ln(x) * x * LMUF * CF * pow(NC, -1)
            - 3 * ln(x) * x * LMUF * CF
            - 1.0 / 3.0 * ln(x) * x * LMUF * CF * NF
            + 43.0 / 12.0 * ln(x) * x * LMUF * CF * NC
            - 4 * ln(x) * x * LMUF * pow(CF, 2)
            - 3.0 / 4.0 * ln(x) * x * pow(LMUF, 2) * CF * pow(NC, -1)
            + 1.0 / 2.0 * ln(x) * x * pow(LMUF, 2) * CF
            + 3.0 / 4.0 * ln(x) * x * pow(LMUF, 2) * CF * NC
            + 3.0 / 4.0 * ln(x) * x * LMUA * CF * pow(NC, -1)
            - 3.0 / 4.0 * ln(x) * x * LMUA * CF * NC
            - ln(x) * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
            + 2.0 / 3.0 * ln(x) * pow(pi, 2) * CF * pow(NC, -1)
            - 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF
            + 5.0 / 3.0 * ln(x) * pow(pi, 2) * CF * NC * pow(omx, -1)
            - ln(x) * pow(pi, 2) * CF * NC
            + 2.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF * pow(NC, -1)
            - 1.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF
            - ln(x) * pow(pi, 2) * x * CF * NC
            + 4 * ln(x) * ln(1 + x) * CF * NC * opx
            - 8 * ln(x) * ln(1 + x) * pow(CF, 2)
            - 8 * ln(x) * ln(1 + x) * x * pow(CF, 2)
            - 9.0 / 8.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
            + 5.0 / 4.0 * pow(ln(x), 2) * CF * pow(NC, -1)
            + 17.0 / 8.0 * pow(ln(x), 2) * CF
            + 5.0 / 6.0 * pow(ln(x), 2) * CF * NF * pow(omx, -1)
            - 5.0 / 12.0 * pow(ln(x), 2) * CF * NF
            - pow(ln(x), 2) * CF * pow(NF, 2)
            - 83.0 / 24.0 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
            + 49.0 / 24.0 * pow(ln(x), 2) * CF * NC
            + pow(ln(x), 2) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
            - pow(ln(x), 2) * LMUF * CF * pow(NC, -1)
            + pow(ln(x), 2) * LMUF * CF
            - 2 * pow(ln(x), 2) * LMUF * CF * NC * pow(omx, -1)
            + 3.0 / 2.0 * pow(ln(x), 2) * LMUF * CF * NC
            - 5.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1)
        )
        res += (
            -15.0 / 8.0 * pow(ln(x), 2) * x * CF
            - 5.0 / 12.0 * pow(ln(x), 2) * x * CF * NF
            - 1.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NF, 2)
            + 7.0 / 24.0 * pow(ln(x), 2) * x * CF * NC
            + 4 * pow(ln(x), 2) * x * pow(CF, 2)
            - pow(ln(x), 2) * x * LMUF * CF * pow(NC, -1)
            + pow(ln(x), 2) * x * LMUF * CF
            + 3.0 / 2.0 * pow(ln(x), 2) * x * LMUF * CF * NC
            - 5.0 / 24.0 * pow(ln(x), 3) * CF * pow(NC, -1)
            + 5.0 / 12.0 * pow(ln(x), 3) * CF
            - 1.0 / 2.0 * pow(ln(x), 3) * CF * NC * pow(omx, -1)
            + 11.0 / 24.0 * pow(ln(x), 3) * CF * NC
            - 5.0 / 24.0 * pow(ln(x), 3) * x * CF * pow(NC, -1)
            + 5.0 / 12.0 * pow(ln(x), 3) * x * CF
            + 11.0 / 24.0 * pow(ln(x), 3) * x * CF * NC
            - 9.0 / 2.0 * pow(ln(x), 2) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
            + 9.0 / 4.0 * pow(ln(x), 2) * ln(omx) * CF * pow(NC, -1)
            + 5.0 / 2.0 * pow(ln(x), 2) * ln(omx) * CF * NC * pow(omx, -1)
            - 5.0 / 4.0 * pow(ln(x), 2) * ln(omx) * CF * NC
            + 9.0 / 4.0 * pow(ln(x), 2) * ln(omx) * x * CF * pow(NC, -1)
            - 5.0 / 4.0 * pow(ln(x), 2) * ln(omx) * x * CF * NC
            - 11.0 / 2.0 * ln(x) * ln(omx) * CF * pow(NC, -1)
            - 5.0 / 2.0 * ln(x) * ln(omx) * CF
            - 2.0 / 3.0 * ln(x) * ln(omx) * CF * NF * pow(omx, -1)
            + 1.0 / 3.0 * ln(x) * ln(omx) * CF * NF
            + 11.0 / 3.0 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
            + 11.0 / 3.0 * ln(x) * ln(omx) * CF * NC
            - 12 * ln(x) * ln(omx) * pow(CF, 2)
            - 6 * ln(x) * ln(omx) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
            + 3 * ln(x) * ln(omx) * LMUF * CF * pow(NC, -1)
            + 6 * ln(x) * ln(omx) * LMUF * CF * NC * pow(omx, -1)
            - 3 * ln(x) * ln(omx) * LMUF * CF * NC
            + 11.0 / 2.0 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
            + 5.0 / 2.0 * ln(x) * ln(omx) * x * CF
            + 1.0 / 3.0 * ln(x) * ln(omx) * x * CF * NF
            - 22.0 / 3.0 * ln(x) * ln(omx) * x * CF * NC
            + 12 * ln(x) * ln(omx) * x * pow(CF, 2)
            + 3 * ln(x) * ln(omx) * x * LMUF * CF * pow(NC, -1)
            - 3 * ln(x) * ln(omx) * x * LMUF * CF * NC
            + 5.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
        )
        res += (
            -1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF
            - 9.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
            + 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF * NC
            - 1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF * pow(NC, -1)
            - 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF
            + 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF * NC
            - 5 * ln(x) * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
            + 2 * ln(x) * Li2(x) * CF * pow(NC, -1)
            + ln(x) * Li2(x) * CF
            + ln(x) * Li2(x) * CF * NC * pow(omx, -1)
            + 2 * ln(x) * Li2(x) * x * CF * pow(NC, -1)
            + ln(x) * Li2(x) * x * CF
            - 5 * ln(omx) * CF * pow(NC, -1)
            - 3 * ln(omx) * CF
            + 2.0 / 9.0 * ln(omx) * CF * NF
            + 55.0 / 9.0 * ln(omx) * CF * NC
            - 8 * ln(omx) * pow(CF, 2)
            + 1.0 / 3.0 * ln(omx) * LMUR * CF * NF
            - 11.0 / 6.0 * ln(omx) * LMUR * CF * NC
            - 19.0 / 4.0 * ln(omx) * LMUF * CF * pow(NC, -1)
            - 5.0 / 2.0 * ln(omx) * LMUF * CF
            + 19.0 / 4.0 * ln(omx) * LMUF * CF * NC
            - 8 * ln(omx) * LMUF * pow(CF, 2)
            + ln(omx) * pow(LMUF, 2) * CF * pow(NC, -1)
            - ln(omx) * pow(LMUF, 2) * CF * NC
            - 3.0 / 4.0 * ln(omx) * LMUA * CF * pow(NC, -1)
            + 3.0 / 4.0 * ln(omx) * LMUA * CF * NC
            - 11.0 / 4.0 * ln(omx) * x * CF * pow(NC, -1)
            + 3 * ln(omx) * x * CF
            + 8.0 / 9.0 * ln(omx) * x * CF * NF
            - 191.0 / 36.0 * ln(omx) * x * CF * NC
            + 8 * ln(omx) * x * pow(CF, 2)
            + 1.0 / 3.0 * ln(omx) * x * LMUR * CF * NF
            - 11.0 / 6.0 * ln(omx) * x * LMUR * CF * NC
            + 13.0 / 4.0 * ln(omx) * x * LMUF * CF * pow(NC, -1)
            + 5.0 / 2.0 * ln(omx) * x * LMUF * CF
            - 13.0 / 4.0 * ln(omx) * x * LMUF * CF * NC
            + 8 * ln(omx) * x * LMUF * pow(CF, 2)
            + ln(omx) * x * pow(LMUF, 2) * CF * pow(NC, -1)
            - ln(omx) * x * pow(LMUF, 2) * CF * NC
            - 3.0 / 4.0 * ln(omx) * x * LMUA * CF * pow(NC, -1)
            + 3.0 / 4.0 * ln(omx) * x * LMUA * CF * NC
            + 1.0 / 6.0 * ln(omx) * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
            - 7.0 / 12.0 * ln(omx) * pow(pi, 2) * CF * pow(NC, -1)
        )
        res += (
            +1.0 / 3.0 * ln(omx) * pow(pi, 2) * CF
            + 1.0 / 6.0 * ln(omx) * pow(pi, 2) * CF * NC * pow(omx, -1)
            + 7.0 / 12.0 * ln(omx) * pow(pi, 2) * CF * NC
            - 7.0 / 12.0 * ln(omx) * pow(pi, 2) * x * CF * pow(NC, -1)
            + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * x * CF
            + 7.0 / 12.0 * ln(omx) * pow(pi, 2) * x * CF * NC
            + 2 * pow(ln(omx), 2) * CF * pow(NC, -1)
            + 5.0 / 4.0 * pow(ln(omx), 2) * CF
            - 1.0 / 6.0 * pow(ln(omx), 2) * CF * NF
            - 13.0 / 12.0 * pow(ln(omx), 2) * CF * NC
            + 4 * pow(ln(omx), 2) * pow(CF, 2)
            - 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * CF * NC
            - 2 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
            - 5.0 / 4.0 * pow(ln(omx), 2) * x * CF
            - 1.0 / 6.0 * pow(ln(omx), 2) * x * CF * NF
            + 35.0 / 12.0 * pow(ln(omx), 2) * x * CF * NC
            - 4 * pow(ln(omx), 2) * x * pow(CF, 2)
            - 3.0 / 2.0 * pow(ln(omx), 2) * x * LMUF * CF * pow(NC, -1)
            + 3.0 / 2.0 * pow(ln(omx), 2) * x * LMUF * CF * NC
            + 1.0 / 2.0 * pow(ln(omx), 3) * CF * pow(NC, -1)
            - 1.0 / 2.0 * pow(ln(omx), 3) * CF * NC
            + 1.0 / 2.0 * pow(ln(omx), 3) * x * CF * pow(NC, -1)
            - 1.0 / 2.0 * pow(ln(omx), 3) * x * CF * NC
            + 1.0 / 2.0 * ln(omx) * Li2(1 - x) * CF * pow(NC, -1)
            - ln(omx) * Li2(1 - x) * CF
            - 1.0 / 2.0 * ln(omx) * Li2(1 - x) * CF * NC
            + 1.0 / 2.0 * ln(omx) * Li2(1 - x) * x * CF * pow(NC, -1)
            - ln(omx) * Li2(1 - x) * x * CF
            - 1.0 / 2.0 * ln(omx) * Li2(1 - x) * x * CF * NC
            - ln(omx) * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
            + 3.0 / 2.0 * ln(omx) * Li2(x) * CF * pow(NC, -1)
            - 2 * ln(omx) * Li2(x) * CF
            - ln(omx) * Li2(x) * CF * NC * pow(omx, -1)
            - 1.0 / 2.0 * ln(omx) * Li2(x) * CF * NC
            + 3.0 / 2.0 * ln(omx) * Li2(x) * x * CF * pow(NC, -1)
            - 2 * ln(omx) * Li2(x) * x * CF
            - 1.0 / 2.0 * ln(omx) * Li2(x) * x * CF * NC
            - 3 * Li3(1 - x) * CF * pow(NC, -1) * pow(omx, -1)
            + 2 * Li3(1 - x) * CF * pow(NC, -1)
            - Li3(1 - x) * CF
            - 5 * Li3(1 - x) * CF * NC * pow(omx, -1)
        )
        res += (
            +2 * Li3(1 - x) * CF * NC
            + 2 * Li3(1 - x) * x * CF * pow(NC, -1)
            - Li3(1 - x) * x * CF
            + 2 * Li3(1 - x) * x * CF * NC
            + 7 * Li3(x) * CF * pow(NC, -1) * pow(omx, -1)
            - 7.0 / 2.0 * Li3(x) * CF * pow(NC, -1)
            - 5 * Li3(x) * CF * NC * pow(omx, -1)
            + 5.0 / 2.0 * Li3(x) * CF * NC
            - 7.0 / 2.0 * Li3(x) * x * CF * pow(NC, -1)
            + 5.0 / 2.0 * Li3(x) * x * CF * NC
            + 4 * Li2(-x) * CF * NC * opx
            - 8 * Li2(-x) * pow(CF, 2)
            - 8 * Li2(-x) * x * pow(CF, 2)
            - 3.0 / 2.0 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
            - 2 * Li2(x) * CF * pow(NC, -1)
            + 1.0 / 2.0 * Li2(x) * CF
            + 2.0 / 3.0 * Li2(x) * CF * NF * pow(omx, -1)
            - 1.0 / 3.0 * Li2(x) * CF * NF
            - 13.0 / 6.0 * Li2(x) * CF * NC * pow(omx, -1)
            + 17.0 / 6.0 * Li2(x) * CF * NC
            - 4 * Li2(x) * pow(CF, 2)
            - 1.0 / 2.0 * Li2(x) * LMUF * CF * pow(NC, -1)
            + Li2(x) * LMUF * CF
            + 1.0 / 2.0 * Li2(x) * LMUF * CF * NC
            + 1.0 / 2.0 * Li2(x) * x * CF * pow(NC, -1)
            - 1.0 / 2.0 * Li2(x) * x * CF
            - 1.0 / 3.0 * Li2(x) * x * CF * NF
            + 1.0 / 3.0 * Li2(x) * x * CF * NC
            + 4 * Li2(x) * x * pow(CF, 2)
            - 1.0 / 2.0 * Li2(x) * x * LMUF * CF * pow(NC, -1)
            + Li2(x) * x * LMUF * CF
            + 1.0 / 2.0 * Li2(x) * x * LMUF * CF * NC
        )

        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            -5 * CF * pow(NC, -1)
            - 3 * CF
            + 2.0 / 9.0 * CF * NF
            + 55.0 / 9.0 * CF * NC
            - 8 * pow(CF, 2)
            + 1.0 / 3.0 * LMUR * CF * NF
            - 11.0 / 6.0 * LMUR * CF * NC
            - 7.0 / 4.0 * LMUF * CF * pow(NC, -1)
            - 5.0 / 2.0 * LMUF * CF
            + 7.0 / 4.0 * LMUF * CF * NC
            - 15.0 / 4.0 * LMUA * CF * pow(NC, -1)
            + 15.0 / 4.0 * LMUA * CF * NC
            - 8 * LMUA * pow(CF, 2)
            + LMUA * LMUF * CF * pow(NC, -1)
            - LMUA * LMUF * CF * NC
            - 3 * x * CF * pow(NC, -1)
            + 3 * x * CF
            + 8.0 / 9.0 * x * CF * NF
            - 50.0 / 9.0 * x * CF * NC
            + 8 * x * pow(CF, 2)
            + 1.0 / 3.0 * x * LMUR * CF * NF
            - 11.0 / 6.0 * x * LMUR * CF * NC
            + 1.0 / 4.0 * x * LMUF * CF * pow(NC, -1)
            + 5.0 / 2.0 * x * LMUF * CF
            - 1.0 / 4.0 * x * LMUF * CF * NC
            + 9.0 / 4.0 * x * LMUA * CF * pow(NC, -1)
            - 9.0 / 4.0 * x * LMUA * CF * NC
            + 8 * x * LMUA * pow(CF, 2)
            + x * LMUA * LMUF * CF * pow(NC, -1)
            - x * LMUA * LMUF * CF * NC
            - 5.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * CF
            + 7.0 / 12.0 * pow(pi, 2) * CF * NC
            - 5.0 / 12.0 * pow(pi, 2) * x * CF * pow(NC, -1)
            + 1.0 / 6.0 * pow(pi, 2) * x * CF
            + 7.0 / 12.0 * pow(pi, 2) * x * CF * NC
            + 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
            - 2 * ln(x) * CF * pow(NC, -1)
            - 3 * ln(x) * CF
            - 4.0 / 3.0 * ln(x) * CF * NF * pow(omx, -1)
            + 2.0 / 3.0 * ln(x) * CF * NF
            + 35.0 / 6.0 * ln(x) * CF * NC * pow(omx, -1)
            - 2.0 / 3.0 * ln(x) * CF * NC
            - 4 * ln(x) * pow(CF, 2)
            - 2 * ln(x) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
            + 3.0 / 2.0 * ln(x) * LMUF * CF * pow(NC, -1)
            - ln(x) * LMUF * CF
            + 2 * ln(x) * LMUF * CF * NC * pow(omx, -1)
            - 3.0 / 2.0 * ln(x) * LMUF * CF * NC
            - 2 * ln(x) * LMUA * CF * pow(NC, -1) * pow(omx, -1)
            + ln(x) * LMUA * CF * pow(NC, -1)
            + 2 * ln(x) * LMUA * CF * NC * pow(omx, -1)
            - ln(x) * LMUA * CF * NC
            + 7.0 / 2.0 * ln(x) * x * CF * pow(NC, -1)
            + 3 * ln(x) * x * CF
            + 2.0 / 3.0 * ln(x) * x * CF * NF
            - 37.0 / 6.0 * ln(x) * x * CF * NC
            + 4 * ln(x) * x * pow(CF, 2)
            + 3.0 / 2.0 * ln(x) * x * LMUF * CF * pow(NC, -1)
            - ln(x) * x * LMUF * CF
        )
        res += (
            -3.0 / 2.0 * ln(x) * x * LMUF * CF * NC
            + ln(x) * x * LMUA * CF * pow(NC, -1)
            - ln(x) * x * LMUA * CF * NC
            - pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
            + pow(ln(x), 2) * CF * pow(NC, -1)
            - pow(ln(x), 2) * CF
            + 2 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
            - 3.0 / 2.0 * pow(ln(x), 2) * CF * NC
            + pow(ln(x), 2) * x * CF * pow(NC, -1)
            - pow(ln(x), 2) * x * CF
            - 3.0 / 2.0 * pow(ln(x), 2) * x * CF * NC
            + 6 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
            - 3 * ln(x) * ln(omx) * CF * pow(NC, -1)
            - 6 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
            + 3 * ln(x) * ln(omx) * CF * NC
            - 3 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
            + 3 * ln(x) * ln(omx) * x * CF * NC
            + 4 * ln(omx) * CF * pow(NC, -1)
            + 5.0 / 2.0 * ln(omx) * CF
            - 1.0 / 3.0 * ln(omx) * CF * NF
            - 13.0 / 6.0 * ln(omx) * CF * NC
            + 8 * ln(omx) * pow(CF, 2)
            - 2 * ln(omx) * LMUF * CF * pow(NC, -1)
            + 2 * ln(omx) * LMUF * CF * NC
            - ln(omx) * LMUA * CF * pow(NC, -1)
            + ln(omx) * LMUA * CF * NC
            - 4 * ln(omx) * x * CF * pow(NC, -1)
            - 5.0 / 2.0 * ln(omx) * x * CF
            - 1.0 / 3.0 * ln(omx) * x * CF * NF
            + 35.0 / 6.0 * ln(omx) * x * CF * NC
            - 8 * ln(omx) * x * pow(CF, 2)
            - 2 * ln(omx) * x * LMUF * CF * pow(NC, -1)
            + 2 * ln(omx) * x * LMUF * CF * NC
            - ln(omx) * x * LMUA * CF * pow(NC, -1)
            + ln(omx) * x * LMUA * CF * NC
            + 3.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1)
            - 3.0 / 2.0 * pow(ln(omx), 2) * CF * NC
            + 3.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
            - 3.0 / 2.0 * pow(ln(omx), 2) * x * CF * NC
            + 1.0 / 2.0 * Li2(x) * CF * pow(NC, -1)
            - Li2(x) * CF
            - 1.0 / 2.0 * Li2(x) * CF * NC
            + 1.0 / 2.0 * Li2(x) * x * CF * pow(NC, -1)
            - Li2(x) * x * CF
            - 1.0 / 2.0 * Li2(x) * x * CF * NC
        )

        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            4 * CF * pow(NC, -1)
            + 5.0 / 2.0 * CF
            - 1.0 / 3.0 * CF * NF
            - 13.0 / 6.0 * CF * NC
            + 8 * pow(CF, 2)
            - LMUF * CF * pow(NC, -1)
            + LMUF * CF * NC
            - 2 * LMUA * CF * pow(NC, -1)
            + 2 * LMUA * CF * NC
            - 4 * x * CF * pow(NC, -1)
            - 5.0 / 2.0 * x * CF
            - 1.0 / 3.0 * x * CF * NF
            + 35.0 / 6.0 * x * CF * NC
            - 8 * x * pow(CF, 2)
            - x * LMUF * CF * pow(NC, -1)
            + x * LMUF * CF * NC
            - 2 * x * LMUA * CF * pow(NC, -1)
            + 2 * x * LMUA * CF * NC
            + 4 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
            - 5.0 / 2.0 * ln(x) * CF * pow(NC, -1)
            + ln(x) * CF
            - 4 * ln(x) * CF * NC * pow(omx, -1)
            + 5.0 / 2.0 * ln(x) * CF * NC
            - 5.0 / 2.0 * ln(x) * x * CF * pow(NC, -1)
            + ln(x) * x * CF
            + 5.0 / 2.0 * ln(x) * x * CF * NC
            + 3 * ln(omx) * CF * pow(NC, -1)
            - 3 * ln(omx) * CF * NC
            + 3 * ln(omx) * x * CF * pow(NC, -1)
            - 3 * ln(omx) * x * CF * NC
        )

        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 3.0 / 2.0 * CF * pow(NC, -1) - 3.0 / 2.0 * CF * NC + 3.0 / 2.0 * x * CF * pow(NC, -1) - 3.0 / 2.0 * x * CF * NC

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
                8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 4 * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * CF * pow(NC, -1)
                - 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * z * CF * pow(NC, -1)
                + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * x * CF * pow(NC, -1)
                - 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 7.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                - pow(pi, 2) * CF * pow(NC, -1)
                + 5.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                - 18 * ln(x) * CF * pow(NC, -1)
                + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 12 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 9 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 9 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * pow(ln(x), 2) * CF * pow(NC, -1)
                - 9 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 20 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 15 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 15 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(z) * CF * pow(NC, -1)
                + 15 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 20 * ln(x) * ln(z) * z * CF * pow(NC, -1)
            )
            tmp += (
                +5 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 13 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + 13 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 14 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 8 * ln(x) * ln(omz) * CF * pow(NC, -1)
                + 14 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 5 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * CF * pow(NC, -1)
                - 3 * ln(x) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(x) * ln(xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * x * CF * pow(NC, -1)
            )
            tmp += (
                +24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                + 12 * ln(z) * CF * pow(NC, -1)
                - 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 24 * ln(z) * z * CF * pow(NC, -1)
                + 8 * ln(z) * x * CF * pow(NC, -1)
                + 8 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(z), 2) * CF * pow(NC, -1)
                - 6 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(z) * ln(omx) * CF * pow(NC, -1)
                - 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 12 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 10 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * CF * pow(NC, -1)
                - 10 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                - 4 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -2 * ln(z) * ln(xmz) * CF * pow(NC, -1)
                + 3 * ln(z) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(z) * ln(xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(omx) * CF * pow(NC, -1)
                - 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                - 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 10 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 7 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                - 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 10 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - 3 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(omz) * CF * pow(NC, -1)
                - 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omz) * z * CF * pow(NC, -1)
            )
            tmp += (
                +6 * ln(omz) * x * CF * pow(NC, -1)
                + 4 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(omz), 2) * CF * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 3 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1)
            )
            tmp += (
                +Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1)
                - Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 4 * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * CF * pow(NC, -1)
                - 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * z * CF * pow(NC, -1)
                + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * x * CF * pow(NC, -1)
                - 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 7.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                - pow(pi, 2) * CF * pow(NC, -1)
                + 5.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                - 18 * ln(x) * CF * pow(NC, -1)
                + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 13 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 10 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * pow(ln(x), 2) * CF * pow(NC, -1)
                - 10 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * pow(ln(x), 2) * z * CF * pow(NC, -1)
            )
            tmp += (
                -7.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 7 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 22 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 17 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(z) * CF * pow(NC, -1)
                + 17 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 22 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 16 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 11 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + 11 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 16 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 20 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 16 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 8 * ln(x) * ln(omz) * CF * pow(NC, -1)
                + 16 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 20 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * CF * pow(NC, -1)
                - 3 * ln(x) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(x) * ln(xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +2 * ln(x) * ln(xmz) * x * CF * pow(NC, -1)
                + 24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                + 12 * ln(z) * CF * pow(NC, -1)
                - 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 24 * ln(z) * z * CF * pow(NC, -1)
                + 8 * ln(z) * x * CF * pow(NC, -1)
                + 8 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(z), 2) * CF * pow(NC, -1)
                - 6 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(z) * ln(omx) * CF * pow(NC, -1)
                - 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 14 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 12 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 9 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * CF * pow(NC, -1)
                - 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                - 4 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                +3 * ln(z) * ln(xmz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * CF * pow(NC, -1)
                + 3 * ln(z) * ln(xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(z) * ln(xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(omx) * CF * pow(NC, -1)
                - 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                - 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                - 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(omz) * CF * pow(NC, -1)
                - 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                +18 * ln(omz) * z * CF * pow(NC, -1)
                + 6 * ln(omz) * x * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 9.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(omz), 2) * CF * pow(NC, -1)
                - 9.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * CF * pow(NC, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                - 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1)
            )
            tmp += (
                +Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(omx * pow(omz, -1)) * CF * pow(NC, -1)
                + Li2(omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
            )

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 4 * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * CF * pow(NC, -1)
                - 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * z * CF * pow(NC, -1)
                + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * x * CF * pow(NC, -1)
                - 8.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 13.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 11.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                - pow(pi, 2) * CF * pow(NC, -1)
                + 13.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 8.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 5.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                - 18 * ln(x) * CF * pow(NC, -1)
                + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * CF * pow(NC, -1)
                - 3 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * x * CF * pow(NC, -1)
                + 14 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 7 * pow(ln(x), 2) * CF * pow(NC, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                +14 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 7 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 24 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 18 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(z) * CF * pow(NC, -1)
                + 18 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 12 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 15 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + 12 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 18 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 15 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * CF * pow(NC, -1)
                + 15 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 6 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +2 * ln(x) * ln(omxmz) * x * CF * pow(NC, -1)
                + 24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                + 12 * ln(z) * CF * pow(NC, -1)
                - 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 24 * ln(z) * z * CF * pow(NC, -1)
                + 8 * ln(z) * x * CF * pow(NC, -1)
                - 4 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * CF * pow(NC, -1)
                + 3 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * x * CF * pow(NC, -1)
                + 10 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 15.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 15.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 5 * pow(ln(z), 2) * CF * pow(NC, -1)
                - 15.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 10 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 5 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 7 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 11 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(z) * ln(omx) * CF * pow(NC, -1)
                - 7 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 12 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -11 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 7 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * CF * pow(NC, -1)
                - 11 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 5 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(omx) * CF * pow(NC, -1)
                - 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 7 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 11.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                - 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 7 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 3 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 5 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                - 4 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(omz) * CF * pow(NC, -1)
            )
            tmp += (
                -16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omz) * z * CF * pow(NC, -1)
                + 6 * ln(omz) * x * CF * pow(NC, -1)
                + 6 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(omz), 2) * CF * pow(NC, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 5 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(omz) * ln(omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(omz) * ln(omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * x * CF * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                + 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(z * pow(omx, -1)) * z * CF * pow(NC, -1)
                - Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * x * CF * pow(NC, -1)
            )
            tmp += (
                +2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * z * CF * pow(NC, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * x * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                8 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 4 * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * CF * pow(NC, -1)
                - 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                + 14 * z * CF * pow(NC, -1)
                + 10 * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * x * CF * pow(NC, -1)
                - 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 7.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                - pow(pi, 2) * CF * pow(NC, -1)
                + 5.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 36 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 18 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                + 36 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                - 18 * ln(x) * CF * pow(NC, -1)
                + 30 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 36 * ln(x) * z * CF * pow(NC, -1)
                - 12 * ln(x) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(x) * ln(-omxmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * ln(x) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * CF * pow(NC, -1)
                - 3 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                +4 * ln(x) * ln(-xmz) * z * CF * pow(NC, -1)
                - ln(x) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * x * CF * pow(NC, -1)
                + 13 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 7 * pow(ln(x), 2) * CF * pow(NC, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 13 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                - 3 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                - 22 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 16 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 17 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(z) * CF * pow(NC, -1)
                + 16 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 22 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                + 5 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                - 20 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 14 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + 14 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 20 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                + 4 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                - 16 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 13 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 11 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * CF * pow(NC, -1)
                + 13 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 16 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
            )
            tmp += (
                +5 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                + 24 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 12 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 24 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                + 12 * ln(z) * CF * pow(NC, -1)
                - 20 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 24 * ln(z) * z * CF * pow(NC, -1)
                + 8 * ln(z) * x * CF * pow(NC, -1)
                - 4 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * ln(z) * ln(-xmz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * CF * pow(NC, -1)
                + 3 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(z) * ln(-xmz) * z * CF * pow(NC, -1)
                + ln(z) * ln(-xmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * x * CF * pow(NC, -1)
                + 8 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 11.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 13.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 5 * pow(ln(z), 2) * CF * pow(NC, -1)
                - 11.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 3 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                + 16 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 11 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 13 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(z) * ln(omx) * CF * pow(NC, -1)
                - 11 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - 3 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                + 10 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -9 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * CF * pow(NC, -1)
                - 9 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 10 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 4 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 8 * ln(omx) * CF * pow(NC, -1)
                - 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omx) * z * CF * pow(NC, -1)
                + 6 * ln(omx) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * CF * pow(NC, -1)
                - 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(omx), 2) * x * CF * pow(NC, -1)
                + 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * CF * pow(NC, -1)
                - 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                + 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 10 * ln(omz) * CF * pow(NC, -1)
            )
            tmp += (
                -16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omz) * z * CF * pow(NC, -1)
                + 6 * ln(omz) * x * CF * pow(NC, -1)
                - 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(omz) * ln(-omxmz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(omz) * ln(-omxmz) * z * CF * pow(NC, -1)
                + ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * x * CF * pow(NC, -1)
                + 5 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 9.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 3 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(omz), 2) * CF * pow(NC, -1)
                - 9.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 5 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                - 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(pow(z, -1) * omx) * z * CF * pow(NC, -1)
                + Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * x * CF * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(pow(omx, -1) * omz) * CF * pow(NC, -1)
                - Li2(pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(pow(omx, -1) * omz) * x * CF * pow(NC, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * CF * pow(NC, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * z * CF * pow(NC, -1)
                - 2 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(z) * z * CF * pow(NC, -1)
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
            tmp = (
                -4 * CF * NC * pow(omx, -1) * pow(omz, -1)
                - CF * NC * pow(omx, -1)
                + 7 * CF * NC * pow(omz, -1)
                - 5 * CF * NC
                + 5 * z * CF * NC * pow(omx, -1)
                - 4 * z * CF * NC
                - 3 * x * CF * NC * pow(omz, -1)
                + 6 * x * CF * NC
                + 4.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
                - 2.0 / 3.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                + 4.0 / 3.0 * pow(pi, 2) * z * CF * NC
                - 2.0 / 3.0 * pow(pi, 2) * x * CF * NC * pow(omz, -1)
                + 4.0 / 3.0 * pow(pi, 2) * x * CF * NC
                + 18 * ln(x) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(x) * CF * NC * pow(omx, -1)
                - 18 * ln(x) * CF * NC * pow(omz, -1)
                - 3 * ln(x) * CF * NC
                - 12 * ln(x) * z * CF * NC * pow(omx, -1)
                + 18 * ln(x) * z * CF * NC
                + 18 * ln(x) * x * CF * NC
                - 7 * pow(ln(x), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * CF * NC * pow(omz, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                - 7 * pow(ln(x), 2) * z * CF * NC
                + 7.0 / 2.0 * pow(ln(x), 2) * x * CF * NC * pow(omz, -1)
                - 7 * pow(ln(x), 2) * x * CF * NC
                + 6 * ln(x) * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                - 3 * ln(x) * ln(z) * CF * NC * pow(omz, -1)
                - 3 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                + 6 * ln(x) * ln(z) * z * CF * NC
                - 3 * ln(x) * ln(z) * x * CF * NC * pow(omz, -1)
                + 6 * ln(x) * ln(z) * x * CF * NC
                + 12 * ln(x) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                - 6 * ln(x) * ln(omx) * CF * NC * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                + 12 * ln(x) * ln(omx) * z * CF * NC
                - 6 * ln(x) * ln(omx) * x * CF * NC * pow(omz, -1)
                + 12 * ln(x) * ln(omx) * x * CF * NC
                + 12 * ln(x) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -6 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                - 6 * ln(x) * ln(omz) * CF * NC * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 12 * ln(x) * ln(omz) * z * CF * NC
                - 6 * ln(x) * ln(omz) * x * CF * NC * pow(omz, -1)
                + 12 * ln(x) * ln(omz) * x * CF * NC
                - 2 * ln(x) * ln(omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + ln(x) * ln(omxmz) * CF * NC * pow(omx, -1)
                + ln(x) * ln(omxmz) * CF * NC * pow(omz, -1)
                + ln(x) * ln(omxmz) * z * CF * NC * pow(omx, -1)
                - 2 * ln(x) * ln(omxmz) * z * CF * NC
                + ln(x) * ln(omxmz) * x * CF * NC * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * x * CF * NC
                - 6 * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * CF * NC * pow(omx, -1)
                + 6 * ln(z) * CF * NC * pow(omz, -1)
                + ln(z) * CF * NC
                + 4 * ln(z) * z * CF * NC * pow(omx, -1)
                - 6 * ln(z) * z * CF * NC
                - 6 * ln(z) * x * CF * NC
                - pow(ln(z), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                - pow(ln(z), 2) * z * CF * NC
                + 1.0 / 2.0 * pow(ln(z), 2) * x * CF * NC * pow(omz, -1)
                - pow(ln(z), 2) * x * CF * NC
                - 4 * ln(z) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                + 2 * ln(z) * ln(omx) * CF * NC * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                - 4 * ln(z) * ln(omx) * z * CF * NC
                + 2 * ln(z) * ln(omx) * x * CF * NC * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * x * CF * NC
                - 4 * ln(z) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                + 2 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 4 * ln(z) * ln(omz) * z * CF * NC
                + 2 * ln(z) * ln(omz) * x * CF * NC * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * x * CF * NC
            )
            tmp += (
                -12 * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 4 * ln(omx) * CF * NC * pow(omx, -1)
                + 12 * ln(omx) * CF * NC * pow(omz, -1)
                + 2 * ln(omx) * CF * NC
                + 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                - 12 * ln(omx) * z * CF * NC
                - 12 * ln(omx) * x * CF * NC
                - 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * CF * NC * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                - 4 * pow(ln(omx), 2) * z * CF * NC
                + 2 * pow(ln(omx), 2) * x * CF * NC * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * x * CF * NC
                - 10 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 5 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                + 5 * ln(omx) * ln(omz) * CF * NC * pow(omz, -1)
                + 5 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 10 * ln(omx) * ln(omz) * z * CF * NC
                + 5 * ln(omx) * ln(omz) * x * CF * NC * pow(omz, -1)
                - 10 * ln(omx) * ln(omz) * x * CF * NC
                - 12 * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 4 * ln(omz) * CF * NC * pow(omx, -1)
                + 12 * ln(omz) * CF * NC * pow(omz, -1)
                + 2 * ln(omz) * CF * NC
                + 8 * ln(omz) * z * CF * NC * pow(omx, -1)
                - 12 * ln(omz) * z * CF * NC
                - 12 * ln(omz) * x * CF * NC
                - 5 * pow(ln(omz), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * CF * NC * pow(omx, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                - 5 * pow(ln(omz), 2) * z * CF * NC
                + 5.0 / 2.0 * pow(ln(omz), 2) * x * CF * NC * pow(omz, -1)
                - 5 * pow(ln(omz), 2) * x * CF * NC
                + 2 * ln(omz) * ln(omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - ln(omz) * ln(omxmz) * CF * NC * pow(omx, -1)
                - ln(omz) * ln(omxmz) * CF * NC * pow(omz, -1)
                - ln(omz) * ln(omxmz) * z * CF * NC * pow(omx, -1)
                + 2 * ln(omz) * ln(omxmz) * z * CF * NC
            )
            tmp += (
                -ln(omz) * ln(omxmz) * x * CF * NC * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * x * CF * NC
                + 2 * Li2(z * pow(omx, -1)) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - Li2(z * pow(omx, -1)) * CF * NC * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * CF * NC * pow(omz, -1)
                - Li2(z * pow(omx, -1)) * z * CF * NC * pow(omx, -1)
                + 2 * Li2(z * pow(omx, -1)) * z * CF * NC
                - Li2(z * pow(omx, -1)) * x * CF * NC * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * x * CF * NC
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * NC * pow(omx, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * CF * NC * pow(omz, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * z * CF * NC
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * CF * NC * pow(omz, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * x * CF * NC
                - 2 * Li2(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * CF * NC * pow(omx, -1)
                + Li2(z) * CF * NC * pow(omz, -1)
                + Li2(z) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(z) * z * CF * NC
                + Li2(z) * x * CF * NC * pow(omz, -1)
                - 2 * Li2(z) * x * CF * NC
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals):

            tmp = 0.0
            tmp = (
                -4 * CF * NC * pow(omx, -1) * pow(omz, -1)
                - CF * NC * pow(omx, -1)
                + 7 * CF * NC * pow(omz, -1)
                - 5 * CF * NC
                + 5 * z * CF * NC * pow(omx, -1)
                - 4 * z * CF * NC
                - 3 * x * CF * NC * pow(omz, -1)
                + 6 * x * CF * NC
                + 4.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
                - 2.0 / 3.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                + 4.0 / 3.0 * pow(pi, 2) * z * CF * NC
                - 2.0 / 3.0 * pow(pi, 2) * x * CF * NC * pow(omz, -1)
                + 4.0 / 3.0 * pow(pi, 2) * x * CF * NC
                + 18 * ln(x) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(x) * CF * NC * pow(omx, -1)
                - 18 * ln(x) * CF * NC * pow(omz, -1)
                - 3 * ln(x) * CF * NC
                - 12 * ln(x) * z * CF * NC * pow(omx, -1)
                + 18 * ln(x) * z * CF * NC
                + 18 * ln(x) * x * CF * NC
                - 2 * ln(x) * ln(-omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + ln(x) * ln(-omxmz) * CF * NC * pow(omx, -1)
                + ln(x) * ln(-omxmz) * CF * NC * pow(omz, -1)
                + ln(x) * ln(-omxmz) * z * CF * NC * pow(omx, -1)
                - 2 * ln(x) * ln(-omxmz) * z * CF * NC
                + ln(x) * ln(-omxmz) * x * CF * NC * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * x * CF * NC
                - 6 * pow(ln(x), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 3 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                + 3 * pow(ln(x), 2) * CF * NC * pow(omz, -1)
                + 3 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                - 6 * pow(ln(x), 2) * z * CF * NC
                + 3 * pow(ln(x), 2) * x * CF * NC * pow(omz, -1)
                - 6 * pow(ln(x), 2) * x * CF * NC
                + 8 * ln(x) * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                - 4 * ln(x) * ln(z) * CF * NC * pow(omz, -1)
                - 4 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                + 8 * ln(x) * ln(z) * z * CF * NC
                - 4 * ln(x) * ln(z) * x * CF * NC * pow(omz, -1)
                + 8 * ln(x) * ln(z) * x * CF * NC
                + 10 * ln(x) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -5 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                - 5 * ln(x) * ln(omx) * CF * NC * pow(omz, -1)
                - 5 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                + 10 * ln(x) * ln(omx) * z * CF * NC
                - 5 * ln(x) * ln(omx) * x * CF * NC * pow(omz, -1)
                + 10 * ln(x) * ln(omx) * x * CF * NC
                + 10 * ln(x) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 5 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                - 5 * ln(x) * ln(omz) * CF * NC * pow(omz, -1)
                - 5 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 10 * ln(x) * ln(omz) * z * CF * NC
                - 5 * ln(x) * ln(omz) * x * CF * NC * pow(omz, -1)
                + 10 * ln(x) * ln(omz) * x * CF * NC
                - 6 * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * CF * NC * pow(omx, -1)
                + 6 * ln(z) * CF * NC * pow(omz, -1)
                + ln(z) * CF * NC
                + 4 * ln(z) * z * CF * NC * pow(omx, -1)
                - 6 * ln(z) * z * CF * NC
                - 6 * ln(z) * x * CF * NC
                - pow(ln(z), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                - pow(ln(z), 2) * z * CF * NC
                + 1.0 / 2.0 * pow(ln(z), 2) * x * CF * NC * pow(omz, -1)
                - pow(ln(z), 2) * x * CF * NC
                - 4 * ln(z) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                + 2 * ln(z) * ln(omx) * CF * NC * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                - 4 * ln(z) * ln(omx) * z * CF * NC
                + 2 * ln(z) * ln(omx) * x * CF * NC * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * x * CF * NC
                - 6 * ln(z) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                + 3 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
                + 3 * ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 6 * ln(z) * ln(omz) * z * CF * NC
                + 3 * ln(z) * ln(omz) * x * CF * NC * pow(omz, -1)
                - 6 * ln(z) * ln(omz) * x * CF * NC
            )
            tmp += (
                -12 * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 4 * ln(omx) * CF * NC * pow(omx, -1)
                + 12 * ln(omx) * CF * NC * pow(omz, -1)
                + 2 * ln(omx) * CF * NC
                + 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                - 12 * ln(omx) * z * CF * NC
                - 12 * ln(omx) * x * CF * NC
                - 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * CF * NC * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                - 4 * pow(ln(omx), 2) * z * CF * NC
                + 2 * pow(ln(omx), 2) * x * CF * NC * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * x * CF * NC
                - 8 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                + 4 * ln(omx) * ln(omz) * CF * NC * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 8 * ln(omx) * ln(omz) * z * CF * NC
                + 4 * ln(omx) * ln(omz) * x * CF * NC * pow(omz, -1)
                - 8 * ln(omx) * ln(omz) * x * CF * NC
                - 12 * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 4 * ln(omz) * CF * NC * pow(omx, -1)
                + 12 * ln(omz) * CF * NC * pow(omz, -1)
                + 2 * ln(omz) * CF * NC
                + 8 * ln(omz) * z * CF * NC * pow(omx, -1)
                - 12 * ln(omz) * z * CF * NC
                - 12 * ln(omz) * x * CF * NC
                + 2 * ln(omz) * ln(-omxmz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - ln(omz) * ln(-omxmz) * CF * NC * pow(omx, -1)
                - ln(omz) * ln(-omxmz) * CF * NC * pow(omz, -1)
                - ln(omz) * ln(-omxmz) * z * CF * NC * pow(omx, -1)
                + 2 * ln(omz) * ln(-omxmz) * z * CF * NC
                - ln(omz) * ln(-omxmz) * x * CF * NC * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * x * CF * NC
                - 4 * pow(ln(omz), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(omz), 2) * CF * NC * pow(omx, -1)
                + 2 * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
                + 2 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                - 4 * pow(ln(omz), 2) * z * CF * NC
            )
            tmp += (
                +2 * pow(ln(omz), 2) * x * CF * NC * pow(omz, -1)
                - 4 * pow(ln(omz), 2) * x * CF * NC
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * NC * pow(omx, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * CF * NC * pow(omz, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * NC * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * z * CF * NC
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * CF * NC * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * x * CF * NC
                - 2 * Li2(pow(z, -1) * omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + Li2(pow(z, -1) * omx) * CF * NC * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * CF * NC * pow(omz, -1)
                + Li2(pow(z, -1) * omx) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(pow(z, -1) * omx) * z * CF * NC
                + Li2(pow(z, -1) * omx) * x * CF * NC * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * x * CF * NC
                - 2 * Li2(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * CF * NC * pow(omx, -1)
                + Li2(z) * CF * NC * pow(omz, -1)
                + Li2(z) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(z) * z * CF * NC
                + Li2(z) * x * CF * NC * pow(omz, -1)
                - 2 * Li2(z) * x * CF * NC
            )

            res += tmp

        if round(z, ndecimals) != round(x, ndecimals) and round(z, ndecimals) != round(1.0 - x, ndecimals):

            tmp = 0.0
            tmp = (
                -12 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 12 * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * pow(z, -1) * CF * pow(NC, -1)
                - 4 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                + 2 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2)
                - 6 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                + 2 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                - 113.0 / 36.0 * pow(z, -1) * CF
                - 5.0 / 2.0 * pow(z, -1) * LMUF * CF
                + 1.0 / 3.0 * pow(z, -1) * LMUA * CF
                - CF * pow(NC, -1) * pow(poly2, -1)
                + 4 * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 4 * CF * pow(NC, -1) * pow(omx, -1)
                + 10 * CF * pow(NC, -1) * pow(omz, -1)
                - 10 * CF * pow(NC, -1)
                - 8 * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                + 4 * CF * pow(NC, -1) * pow(rln2, 2)
                - 6 * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                + 6 * CF * pow(NC, -1) * sqrtxz1 * rln2
                + 47.0 / 3.0 * CF
                + 6 * CF * pow(rln2, 2) * pow(omx, -1)
                - 4 * CF * pow(rln2, 2)
                + 6 * CF * sqrtxz1 * rln2 * pow(omx, -1)
                - 4 * CF * sqrtxz1 * rln2
                + 2.0 / 3.0 * CF * NF
                + 4 * CF * NC * pow(omx, -1) * pow(omz, -1)
                + CF * NC * pow(omx, -1)
                - 7 * CF * NC * pow(omz, -1)
                - 14.0 / 3.0 * CF * NC
                + 16 * pow(CF, 2)
                + LMUF * CF * pow(NC, -1)
                + 5 * LMUF * CF
                - LMUF * CF * NC
                + 3 * LMUA * CF * pow(NC, -1)
                + 3.0 / 2.0 * LMUA * CF
                - 3 * LMUA * CF * NC
                + 4 * LMUA * pow(CF, 2)
                - 1.0 / 2.0 * LMUA * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * LMUA * LMUF * CF * NC
                + 12 * z * CF * pow(NC, -1) * pow(omx, -1)
                - 1.0 / 2.0 * z * CF * pow(NC, -1) * pow(omxmz, -1)
                - 11 * z * CF * pow(NC, -1)
                - 4 * z * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                + 4 * z * CF * pow(NC, -1) * pow(rln2, 2)
                - 11.0 / 12.0 * z * CF
                + 4 * z * CF * pow(rln2, 2) * pow(omx, -1)
                - 10.0 / 9.0 * z * CF * NF
                - 5 * z * CF * NC * pow(omx, -1)
            )
            tmp += (
                +1.0 / 2.0 * z * CF * NC * pow(omxmz, -1)
                + 76.0 / 9.0 * z * CF * NC
                - 8 * z * pow(CF, 2)
                - 2.0 / 3.0 * z * LMUR * CF * NF
                + 11.0 / 3.0 * z * LMUR * CF * NC
                + 3.0 / 2.0 * z * LMUF * CF * pow(NC, -1)
                - 3.0 / 2.0 * z * LMUF * CF * NC
                + 3.0 / 2.0 * z * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * z * LMUA * CF
                - 3.0 / 2.0 * z * LMUA * CF * NC
                + 4 * z * LMUA * pow(CF, 2)
                - 1.0 / 2.0 * z * LMUA * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * z * LMUA * LMUF * CF * NC
                - 65.0 / 18.0 * pow(z, 2) * CF
                + 16 * pow(z, 2) * CF * pow(rln2, 2) * pow(omx, -1)
                - 16 * pow(z, 2) * CF * pow(rln2, 2)
                - 4.0 / 3.0 * pow(z, 2) * LMUA * CF
                + 4 * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 19.0 / 2.0 * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * x * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2)
                + 4 * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                + 127.0 / 36.0 * x * pow(z, -1) * CF
                + 5.0 / 2.0 * x * pow(z, -1) * LMUF * CF
                + 1.0 / 3.0 * x * pow(z, -1) * LMUA * CF
                + x * CF * pow(NC, -1) * pow(poly2, -1)
                - 14 * x * CF * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * x * CF * pow(NC, -1) * pow(xmz, -1)
                + 22 * x * CF * pow(NC, -1)
                + 4 * x * CF * pow(NC, -1) * pow(rln2, 2)
                - 25.0 / 3.0 * x * CF
                - 16.0 / 9.0 * x * CF * NF
                + 3 * x * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * x * CF * NC * pow(xmz, -1)
                + 46.0 / 9.0 * x * CF * NC
                - 16 * x * pow(CF, 2)
                - 2.0 / 3.0 * x * LMUR * CF * NF
                + 11.0 / 3.0 * x * LMUR * CF * NC
                - 1.0 / 2.0 * x * LMUF * CF * pow(NC, -1)
                - 5 * x * LMUF * CF
                + 1.0 / 2.0 * x * LMUF * CF * NC
                - 1.0 / 2.0 * x * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * x * LMUA * CF
                + 1.0 / 2.0 * x * LMUA * CF * NC
                - 4 * x * LMUA * pow(CF, 2)
                - 1.0 / 2.0 * x * LMUA * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * x * LMUA * LMUF * CF * NC
                + 6 * x * z * CF * pow(NC, -1)
                - 47.0 / 12.0 * x * z * CF
                - 8 * x * z * CF * pow(rln2, 2)
                - 9.0 / 2.0 * x * z * CF * NC
                + 8 * x * z * pow(CF, 2)
                + x * z * LMUF * CF * pow(NC, -1)
                - x * z * LMUF * CF * NC
                - x * z * LMUA * CF * pow(NC, -1)
                - 3.0 / 2.0 * x * z * LMUA * CF
            )
            tmp += (
                +x * z * LMUA * CF * NC
                - 4 * x * z * LMUA * pow(CF, 2)
                - 1.0 / 2.0 * x * z * LMUA * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * x * z * LMUA * LMUF * CF * NC
                + 31.0 / 18.0 * x * pow(z, 2) * CF
                + 2.0 / 3.0 * x * pow(z, 2) * LMUA * CF
                - pow(x, 2) * CF * pow(NC, -1) * pow(poly2, -1)
                - pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -1)
                - pow(x, 2) * CF * NC * pow(xmz, -1)
                + pow(x, 3) * CF * pow(NC, -1) * pow(poly2, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(opx, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF * pow(NC, -1)
                - 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF * pow(NC, -1)
                + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF
                + 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF
                + 4.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 4.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                + 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * pow(z, -1) * CF
                + 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                - 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                + 11.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
                - 5.0 / 6.0 * pow(pi, 2) * CF * pow(omx, -1)
                + 2.0 / 3.0 * pow(pi, 2) * CF * pow(opx, -1)
                - 1.0 / 6.0 * pow(pi, 2) * CF
                - pow(pi, 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(pi, 2) * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * pow(pi, 2) * CF * NC * pow(omz, -1)
                - 1.0 / 6.0 * pow(pi, 2) * CF * NC
                - 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                + pow(pi, 2) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 13.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(omx, -1)
                - 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(opx, -1)
                - pow(pi, 2) * z * CF
                + 1.0 / 2.0 * pow(pi, 2) * z * CF * NC * pow(omx, -1)
                - 13.0 / 6.0 * pow(pi, 2) * z * CF * NC
                - 2 * pow(pi, 2) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * pow(pi, 2) * pow(z, 2) * CF * pow(opx, -1)
                + 4.0 / 3.0 * pow(pi, 2) * pow(z, 2) * CF
                - 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                + 2.0 / 3.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF
                + 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                - 5.0 / 6.0 * pow(pi, 2) * x * CF
                + 1.0 / 2.0 * pow(pi, 2) * x * CF * NC * pow(omz, -1)
                - 13.0 / 6.0 * pow(pi, 2) * x * CF * NC
                + 1.0 / 6.0 * pow(pi, 2) * x * z * CF * pow(NC, -1)
                + 2.0 / 3.0 * pow(pi, 2) * x * z * CF
                - 1.0 / 6.0 * pow(pi, 2) * x * z * CF * NC
                + 4 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                + 6 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
            )
            tmp += (
                +8 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * rln2
                + 6 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                - 6 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * sqrtxz1
                - 8 * ln(1 + sqrtxz1 - z) * CF * rln2 * pow(omx, -1)
                + 6 * ln(1 + sqrtxz1 - z) * CF * rln2
                - 6 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1 * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1
                + 4 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * rln2
                - 4 * ln(1 + sqrtxz1 - z) * z * CF * rln2
                - 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                + 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2
                - 2 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                - 4 * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                - 4 * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * rln2
                - 2 * ln(1 + sqrtxz1 - z) * x * CF * rln2
                + 12 * ln(1 + sqrtxz1 - z) * x * z * CF * rln2
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(omx, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(omx, -1)
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF
                + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * CF
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                +4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1)
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF
                + 4 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                + 8 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * rln2
                - 4 * ln(1 + sqrtxz1 + z) * CF * rln2 * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 + z) * CF * rln2
                + 4 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * rln2
                - 8 * ln(1 + sqrtxz1 + z) * z * CF * rln2 * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 + z) * z * CF * rln2
                - 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                + 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2
                - 2 * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
            )
            tmp += (
                -4 * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * rln2
                + 2 * ln(1 + sqrtxz1 + z) * x * CF * rln2
                + 4 * ln(1 + sqrtxz1 + z) * x * z * CF * rln2
                - 6 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                + 2 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                - 6 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                - 8 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * sqrtxz3
                - 6 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                - 4 * ln(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                + 8 * ln(x) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                - 8 * ln(x) * pow(x, -2) * CF * pow(NC, -1)
                - 4 * ln(x) * pow(x, -2) * CF * pow(opx, -1)
                + 4 * ln(x) * pow(x, -2) * CF
                + 8 * ln(x) * pow(x, -2) * z * CF * pow(opx, -1)
                - 8 * ln(x) * pow(x, -2) * z * CF
                - 4 * ln(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                + 8 * ln(x) * pow(x, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * pow(x, -1) * CF
                + 8 * ln(x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 8 * ln(x) * pow(x, -1) * z * CF * pow(NC, -1)
                + 8 * ln(x) * pow(x, -1) * z * CF
                + 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF
                + 48 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 87.0 / 2.0 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 32 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 33 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2
                - 3 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
            )
            tmp += (
                +ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                - 4.0 / 3.0 * ln(x) * pow(z, -1) * CF * pow(omx, -1)
                - 7.0 / 3.0 * ln(x) * pow(z, -1) * CF
                - ln(x) * pow(z, -1) * LMUF * CF
                - 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(poly2, -2)
                + ln(x) * CF * pow(NC, -1) * pow(poly2, -1)
                - 12 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(xmz, -1)
                - 20 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                - 8 * ln(x) * CF * pow(NC, -1) * pow(opx, -1)
                - 3.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(xmz, -1)
                + 1.0 / 2.0 * ln(x) * CF * pow(NC, -1) * pow(omxmz, -1)
                + 15 * ln(x) * CF * pow(NC, -1)
                - 4 * ln(x) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + 2 * ln(x) * CF * pow(NC, -1) * rln2
                - 3 * ln(x) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                + 3 * ln(x) * CF * pow(NC, -1) * sqrtxz1
                - 9.0 / 2.0 * ln(x) * CF * pow(omx, -1)
                + 4 * ln(x) * CF * pow(opx, -1)
                + 25.0 / 2.0 * ln(x) * CF
                + 5 * ln(x) * CF * rln2 * pow(omx, -1)
                - 4 * ln(x) * CF * rln2
                + 3 * ln(x) * CF * sqrtxz1 * pow(omx, -1)
                - 2 * ln(x) * CF * sqrtxz1
                + ln(x) * CF * NF * pow(omx, -1)
                - 18 * ln(x) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(x) * CF * NC * pow(omx, -1) * pow(xmz, -1)
                + 7.0 / 2.0 * ln(x) * CF * NC * pow(omx, -1)
                + 18 * ln(x) * CF * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * CF * NC * pow(xmz, -1)
                - 3.0 / 2.0 * ln(x) * CF * NC * pow(omxmz, -1)
                - 1.0 / 2.0 * ln(x) * CF * NC
                + 4 * ln(x) * pow(CF, 2) * opx
                + ln(x) * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * LMUF * CF * pow(NC, -1)
                + 2 * ln(x) * LMUF * CF
                - ln(x) * LMUF * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * ln(x) * LMUF * CF * NC
                + ln(x) * LMUA * CF * pow(NC, -1) * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * LMUA * CF * pow(NC, -1)
                - ln(x) * LMUA * CF * NC * pow(omx, -1)
            )
            tmp += (
                +1.0 / 2.0 * ln(x) * LMUA * CF * NC
                - 73.0 / 2.0 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * ln(x) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * ln(x) * z * CF * pow(NC, -1) * pow(omxmz, -2)
                + 3.0 / 2.0 * ln(x) * z * CF * pow(NC, -1) * pow(omxmz, -1)
                + 79.0 / 2.0 * ln(x) * z * CF * pow(NC, -1)
                - 2 * ln(x) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + 2 * ln(x) * z * CF * pow(NC, -1) * rln2
                + 11.0 / 2.0 * ln(x) * z * CF * pow(omx, -1)
                - 8 * ln(x) * z * CF * pow(opx, -1)
                - 3 * ln(x) * z * CF
                - 2 * ln(x) * z * CF * rln2 * pow(omx, -1)
                + 4 * ln(x) * z * CF * rln2
                + ln(x) * z * CF * NF * pow(omx, -1)
                - 4.0 / 3.0 * ln(x) * z * CF * NF
                + 17.0 / 2.0 * ln(x) * z * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * ln(x) * z * CF * NC * pow(omxmz, -2)
                - 1.0 / 2.0 * ln(x) * z * CF * NC * pow(omxmz, -1)
                - 67.0 / 6.0 * ln(x) * z * CF * NC
                - 4 * ln(x) * z * pow(CF, 2) * opx
                + ln(x) * z * LMUF * CF * pow(NC, -1) * pow(omx, -1)
                - 3.0 / 2.0 * ln(x) * z * LMUF * CF * pow(NC, -1)
                - ln(x) * z * LMUF * CF * NC * pow(omx, -1)
                + 3.0 / 2.0 * ln(x) * z * LMUF * CF * NC
                + ln(x) * z * LMUA * CF * pow(NC, -1) * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * z * LMUA * CF * pow(NC, -1)
                - ln(x) * z * LMUA * CF * NC * pow(omx, -1)
                + 1.0 / 2.0 * ln(x) * z * LMUA * CF * NC
                + 1.0 / 2.0 * ln(x) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF * pow(omx, -1)
                + 16 * ln(x) * pow(z, 2) * CF * pow(opx, -1)
                - 8.0 / 3.0 * ln(x) * pow(z, 2) * CF
                + 16 * ln(x) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                - 16 * ln(x) * pow(z, 2) * CF * rln2
                - 1.0 / 2.0 * ln(x) * pow(z, 2) * CF * NC * pow(omxmz, -2)
                - 16 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                + 16 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1)
                + ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                + 2 * ln(x) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                + 11.0 / 3.0 * ln(x) * x * pow(z, -1) * CF
            )
            tmp += (
                -ln(x) * x * pow(z, -1) * LMUF * CF
                + 3.0 / 2.0 * ln(x) * x * CF * pow(NC, -1) * pow(poly2, -2)
                + 16 * ln(x) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(x) * x * CF * pow(NC, -1) * pow(xmz, -1)
                + 11 * ln(x) * x * CF * pow(NC, -1)
                + 2 * ln(x) * x * CF * pow(NC, -1) * rln2
                - ln(x) * x * CF * pow(xmz, -1)
                - 9.0 / 2.0 * ln(x) * x * CF
                + 2 * ln(x) * x * CF * rln2
                - 4.0 / 3.0 * ln(x) * x * CF * NF
                + 3.0 / 2.0 * ln(x) * x * CF * NC * pow(xmz, -1)
                - 79.0 / 6.0 * ln(x) * x * CF * NC
                - 3.0 / 2.0 * ln(x) * x * LMUF * CF * pow(NC, -1)
                + 2 * ln(x) * x * LMUF * CF
                + 3.0 / 2.0 * ln(x) * x * LMUF * CF * NC
                - 1.0 / 2.0 * ln(x) * x * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * x * LMUA * CF * NC
                - 3.0 / 2.0 * ln(x) * x * z * CF * pow(NC, -1)
                - 3 * ln(x) * x * z * CF
                - 8 * ln(x) * x * z * CF * rln2
                + 3.0 / 2.0 * ln(x) * x * z * CF * NC
                - 1.0 / 2.0 * ln(x) * x * z * LMUF * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * x * z * LMUF * CF * NC
                - 1.0 / 2.0 * ln(x) * x * z * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(x) * x * z * LMUA * CF * NC
                + 4.0 / 3.0 * ln(x) * x * pow(z, 2) * CF
                - 1.0 / 2.0 * ln(x) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -2)
                - 3 * ln(x) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -1)
                + 2 * ln(x) * pow(x, 2) * CF * pow(xmz, -1)
                - 1.0 / 2.0 * ln(x) * pow(x, 2) * CF * NC * pow(xmz, -2)
                + ln(x) * pow(x, 2) * CF * NC * pow(xmz, -1)
                + ln(x) * pow(x, 3) * CF * pow(NC, -1) * pow(poly2, -1)
                + ln(x) * pow(x, 3) * CF * pow(NC, -1) * pow(xmz, -2)
                + ln(x) * pow(x, 3) * CF * NC * pow(xmz, -2)
                + 3.0 / 2.0 * ln(x) * pow(x, 4) * CF * pow(NC, -1) * pow(poly2, -2)
                - 3.0 / 2.0 * ln(x) * pow(x, 5) * CF * pow(NC, -1) * pow(poly2, -2)
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                - 2 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                + 3 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 4 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
            )
            tmp += (
                -3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 4 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                + 2 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                - 3 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 4 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 4 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
            )
            tmp += (
                +2 * ln(x) * ln(1 + sqrtxz1 - z) * CF
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF
                - 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * CF
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                - 3 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                - ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * CF
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
            )
            tmp += (
                +ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                + ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * CF * pow(NC, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * x * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF
                + 4 * ln(x) * ln(1 + x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x) * pow(z, -1) * CF * pow(NC, -1)
                - 8 * ln(x) * ln(1 + x) * CF * pow(NC, -1) * pow(opx, -1)
                + 8 * ln(x) * ln(1 + x) * CF * pow(NC, -1)
                + 4 * ln(x) * ln(1 + x) * CF * pow(opx, -1)
                - 6 * ln(x) * ln(1 + x) * CF
                + 4 * ln(x) * ln(1 + x) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x) * z * CF * pow(NC, -1)
            )
            tmp += (
                -8 * ln(x) * ln(1 + x) * z * CF * pow(opx, -1)
                + 12 * ln(x) * ln(1 + x) * z * CF
                + 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF
                - 2 * ln(x) * ln(1 + x) * x * CF
                + 4 * ln(x) * ln(1 + x) * x * z * CF
                + ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1)
                + ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                - ln(x) * ln(1 + x * z) * pow(x, -2) * CF
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF
                + ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1)
                + ln(x) * ln(1 + x * z) * pow(x, -1) * CF
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF
                - 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                - 2 * ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(1 + x * z) * CF * pow(omx, -1)
                + ln(x) * ln(1 + x * z) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * CF
                - 2 * ln(x) * ln(1 + x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(x) * ln(1 + x * z) * z * CF * pow(omx, -1)
            )
            tmp += (
                -2 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF
                + 2 * ln(x) * ln(1 + x * z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(1 + x * z) * x * z * CF
                + 2 * ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(x) * ln(z + x) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(z + x) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(z + x) * CF * pow(omx, -1)
                + ln(x) * ln(z + x) * CF
                + 2 * ln(x) * ln(z + x) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(x) * ln(z + x) * z * CF * pow(NC, -1)
                - 4 * ln(x) * ln(z + x) * z * CF * pow(omx, -1)
                + 2 * ln(x) * ln(z + x) * z * CF
                - 4 * ln(x) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                + 4 * ln(x) * ln(z + x) * pow(z, 2) * CF
                - ln(x) * ln(z + x) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(z + x) * x * CF * pow(NC, -1)
                + ln(x) * ln(z + x) * x * CF
                + 2 * ln(x) * ln(z + x) * x * z * CF
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                - 3 * pow(ln(x), 2) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 3 * pow(ln(x), 2) * pow(x, -2) * CF * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF * pow(opx, -1)
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF
                - 3 * pow(ln(x), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                + 3 * pow(ln(x), 2) * pow(x, -2) * z * CF
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                - 3 * pow(ln(x), 2) * pow(x, -1) * CF * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * CF
                - 3 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 3 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(NC, -1)
            )
            tmp += (
                -3 * pow(ln(x), 2) * pow(x, -1) * z * CF
                - 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF
                - 16 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 16 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 11 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 10 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                - pow(ln(x), 2) * pow(z, -1) * CF
                - pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 13 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + 5 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(opx, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1)
                - 2 * pow(ln(x), 2) * CF * pow(omx, -1)
                - 5.0 / 2.0 * pow(ln(x), 2) * CF * pow(opx, -1)
                + 5 * pow(ln(x), 2) * CF
                + 8 * pow(ln(x), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 5 * pow(ln(x), 2) * CF * NC * pow(omx, -1)
                - 4 * pow(ln(x), 2) * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(x), 2) * CF * NC
                + 13 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 31.0 / 2.0 * pow(ln(x), 2) * z * CF * pow(NC, -1)
                + 4 * pow(ln(x), 2) * z * CF * pow(omx, -1)
                + 5 * pow(ln(x), 2) * z * CF * pow(opx, -1)
                - 6 * pow(ln(x), 2) * z * CF
                - 5 * pow(ln(x), 2) * z * CF * NC * pow(omx, -1)
                + 17.0 / 2.0 * pow(ln(x), 2) * z * CF * NC
                - 2 * pow(ln(x), 2) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * pow(ln(x), 2) * pow(z, 2) * CF
                + 5 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 5 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -pow(ln(x), 2) * x * pow(z, -1) * CF
                - 1.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 17.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                + 4 * pow(ln(x), 2) * x * CF
                - 4 * pow(ln(x), 2) * x * CF * NC * pow(omz, -1)
                + 17.0 / 2.0 * pow(ln(x), 2) * x * CF * NC
                - 1.0 / 2.0 * pow(ln(x), 2) * x * z * CF * pow(NC, -1)
                - 4 * pow(ln(x), 2) * x * z * CF
                + 1.0 / 2.0 * pow(ln(x), 2) * x * z * CF * NC
                - ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + ln(x) * ln(z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(z) * pow(x, -2) * CF * pow(NC, -1)
                - ln(x) * ln(z) * pow(x, -2) * CF * pow(opx, -1)
                + ln(x) * ln(z) * pow(x, -2) * CF
                + 2 * ln(x) * ln(z) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(z) * pow(x, -2) * z * CF
                - ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(z) * pow(x, -1) * CF * pow(NC, -1)
                - ln(x) * ln(z) * pow(x, -1) * CF
                + 2 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(NC, -1)
                + 2 * ln(x) * ln(z) * pow(x, -1) * z * CF
                + 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF
                + 16 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 16 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 10 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 12 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                + ln(x) * ln(z) * pow(z, -1) * CF
                + 4 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 23.0 / 2.0 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +2 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(z) * CF * pow(NC, -1)
                + ln(x) * ln(z) * CF * pow(omx, -1)
                - ln(x) * ln(z) * CF * pow(opx, -1)
                - 8 * ln(x) * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(x) * ln(z) * CF * NC * pow(omx, -1)
                + 4 * ln(x) * ln(z) * CF * NC * pow(omz, -1)
                - 27.0 / 2.0 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 19 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                - 7 * ln(x) * ln(z) * z * CF * pow(omx, -1)
                + 2 * ln(x) * ln(z) * z * CF * pow(opx, -1)
                + 6 * ln(x) * ln(z) * z * CF
                + 7.0 / 2.0 * ln(x) * ln(z) * z * CF * NC * pow(omx, -1)
                - 5 * ln(x) * ln(z) * z * CF * NC
                + 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * ln(x) * ln(z) * pow(z, 2) * CF
                - 6 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * ln(x) * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                + ln(x) * ln(z) * x * pow(z, -1) * CF
                + 9 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                + 2 * ln(x) * ln(z) * x * CF
                + 4 * ln(x) * ln(z) * x * CF * NC * pow(omz, -1)
                - 5 * ln(x) * ln(z) * x * CF * NC
                - 2 * ln(x) * ln(z) * x * z * CF
                + 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * pow(x, -2) * CF
                - 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF
                + 2 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(x) * ln(omx) * pow(x, -1) * CF * pow(NC, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -1) * CF
                - 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(NC, -1)
            )
            tmp += (
                -4 * ln(x) * ln(omx) * pow(x, -1) * z * CF
                - 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF
                - 8 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                + 28 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 17 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                - 21 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(opx, -1)
                + 15 * ln(x) * ln(omx) * CF * pow(NC, -1)
                + 3 * ln(x) * ln(omx) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(omx) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(omx) * CF
                - 10 * ln(x) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(omx) * CF * NC * pow(omx, -1)
                + 5 * ln(x) * ln(omx) * CF * NC * pow(omz, -1)
                - ln(x) * ln(omx) * CF * NC
                - 17 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 23 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                - 6 * ln(x) * ln(omx) * z * CF * pow(omx, -1)
                + 4 * ln(x) * ln(omx) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * z * CF
                + 8 * ln(x) * ln(omx) * z * CF * NC * pow(omx, -1)
                - 13 * ln(x) * ln(omx) * z * CF * NC
                + 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * ln(x) * ln(omx) * pow(z, 2) * CF
                + 4 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                - 7 * ln(x) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +9 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                + 5 * ln(x) * ln(omx) * x * CF * NC * pow(omz, -1)
                - 13 * ln(x) * ln(omx) * x * CF * NC
                + ln(x) * ln(omx) * x * z * CF * pow(NC, -1)
                - ln(x) * ln(omx) * x * z * CF * NC
                + ln(x) * ln(omz) * pow(z, -1) * CF
                + 18 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 16 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                - 12 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                + 7 * ln(x) * ln(omz) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(omz) * CF
                - 12 * ln(x) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(omz) * CF * NC * pow(omx, -1)
                + 6 * ln(x) * ln(omz) * CF * NC * pow(omz, -1)
                - ln(x) * ln(omz) * CF * NC
                - 16 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 20 * ln(x) * ln(omz) * z * CF * pow(NC, -1)
                + 8 * ln(x) * ln(omz) * z * CF * NC * pow(omx, -1)
                - 14 * ln(x) * ln(omz) * z * CF * NC
                + ln(x) * ln(omz) * x * pow(z, -1) * CF
                - 6 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 14 * ln(x) * ln(omz) * x * CF * pow(NC, -1)
                - 2 * ln(x) * ln(omz) * x * CF
                + 6 * ln(x) * ln(omz) * x * CF * NC * pow(omz, -1)
                - 14 * ln(x) * ln(omz) * x * CF * NC
                + ln(x) * ln(omz) * x * z * CF * pow(NC, -1)
                - ln(x) * ln(omz) * x * z * CF * NC
                - 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(x, -2) * CF
                + 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF
                - 2 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(x) * ln(opx) * pow(x, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -2 * ln(x) * ln(opx) * pow(x, -1) * CF
                + 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(NC, -1)
                + 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF
                + 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF
                - 2 * ln(x) * ln(opx) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(x) * ln(opx) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * CF * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * CF
                + 4 * ln(x) * ln(opx) * z * CF * pow(NC, -1)
                + 4 * ln(x) * ln(opx) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * z * CF
                + 8 * ln(x) * ln(opx) * pow(z, 2) * CF
                - 2 * ln(x) * ln(opx) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(x) * ln(opx) * x * CF * pow(NC, -1)
                - 2 * ln(x) * ln(opx) * x * CF
                + 4 * ln(x) * ln(opx) * x * z * CF
                - 24 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 27 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                - 6 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + 3 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                - 3 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                + ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                + 13.0 / 6.0 * ln(z) * pow(z, -1) * CF
                - 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(poly2, -2)
                + ln(z) * CF * pow(NC, -1) * pow(poly2, -1)
                + 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(xmz, -1)
                + 18 * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 12 * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                +3.0 / 2.0 * ln(z) * CF * pow(NC, -1) * pow(xmz, -1)
                - 45.0 / 2.0 * ln(z) * CF * pow(NC, -1)
                - 12 * ln(z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + 6 * ln(z) * CF * pow(NC, -1) * rln2
                - 3 * ln(z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                + 3 * ln(z) * CF * pow(NC, -1) * sqrtxz1
                - 3 * ln(z) * CF * pow(omx, -1)
                + ln(z) * CF * pow(omz, -1)
                + 7 * ln(z) * CF * rln2 * pow(omx, -1)
                - 4 * ln(z) * CF * rln2
                + 3 * ln(z) * CF * sqrtxz1 * pow(omx, -1)
                - 2 * ln(z) * CF * sqrtxz1
                + 9.0 / 2.0 * ln(z) * CF * NC * pow(omx, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * CF * NC * pow(omx, -1) * pow(xmz, -1)
                - 2 * ln(z) * CF * NC * pow(omx, -1)
                - 9 * ln(z) * CF * NC * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * CF * NC * pow(xmz, -1)
                + 3 * ln(z) * CF * NC
                + 8 * ln(z) * pow(CF, 2) * pow(omz, -1)
                - 4 * ln(z) * pow(CF, 2)
                - ln(z) * LMUF * CF * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * LMUF * CF * pow(NC, -1)
                + ln(z) * LMUF * CF * NC * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * LMUF * CF * NC
                + ln(z) * LMUA * CF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * LMUA * CF * pow(NC, -1)
                + ln(z) * LMUA * CF
                - ln(z) * LMUA * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * LMUA * CF * NC
                + 23 * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 32 * ln(z) * z * CF * pow(NC, -1)
                - 6 * ln(z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                + 6 * ln(z) * z * CF * pow(NC, -1) * rln2
                - 3 * ln(z) * z * CF * pow(omx, -1)
                + 7.0 / 2.0 * ln(z) * z * CF
                + 10 * ln(z) * z * CF * rln2 * pow(omx, -1)
                - 4 * ln(z) * z * CF * rln2
                - 4 * ln(z) * z * CF * NC * pow(omx, -1)
                + 11 * ln(z) * z * CF * NC
                - 4 * ln(z) * z * pow(CF, 2)
                + 1.0 / 2.0 * ln(z) * z * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * z * LMUF * CF * NC
                - 3.0 / 2.0 * ln(z) * z * LMUA * CF * pow(NC, -1)
                + 2 * ln(z) * z * LMUA * CF
                + 3.0 / 2.0 * ln(z) * z * LMUA * CF * NC
                + 4.0 / 3.0 * ln(z) * pow(z, 2) * CF
                + 16 * ln(z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
            )
            tmp += (
                -16 * ln(z) * pow(z, 2) * CF * rln2
                + 8 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 11 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1)
                + 3 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * rln2
                + 2 * ln(z) * x * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                - 17.0 / 6.0 * ln(z) * x * pow(z, -1) * CF
                - 3.0 / 2.0 * ln(z) * x * CF * pow(NC, -1) * pow(poly2, -2)
                - 12 * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * x * CF * pow(NC, -1) * pow(xmz, -1)
                - 11.0 / 2.0 * ln(z) * x * CF * pow(NC, -1)
                + 6 * ln(z) * x * CF * pow(NC, -1) * rln2
                - ln(z) * x * CF * pow(omz, -1)
                + ln(z) * x * CF * pow(xmz, -1)
                + 4 * ln(z) * x * CF
                - 2 * ln(z) * x * CF * rln2
                + 3 * ln(z) * x * CF * NC * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * x * CF * NC * pow(xmz, -1)
                + 6 * ln(z) * x * CF * NC
                - 8 * ln(z) * x * pow(CF, 2) * pow(omz, -1)
                + 4 * ln(z) * x * pow(CF, 2)
                - ln(z) * x * LMUF * CF * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * x * LMUF * CF * pow(NC, -1)
                + ln(z) * x * LMUF * CF * NC * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * x * LMUF * CF * NC
                + ln(z) * x * LMUA * CF * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * x * LMUA * CF * pow(NC, -1)
                + ln(z) * x * LMUA * CF
                - ln(z) * x * LMUA * CF * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * x * LMUA * CF * NC
                + 2 * ln(z) * x * z * CF * pow(NC, -1)
                + 3.0 / 2.0 * ln(z) * x * z * CF
                - 8 * ln(z) * x * z * CF * rln2
                - 2 * ln(z) * x * z * CF * NC
                + 4 * ln(z) * x * z * pow(CF, 2)
                + 1.0 / 2.0 * ln(z) * x * z * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(z) * x * z * LMUF * CF * NC
                - 1.0 / 2.0 * ln(z) * x * z * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * x * z * LMUA * CF * NC
                - 2.0 / 3.0 * ln(z) * x * pow(z, 2) * CF
                + 1.0 / 2.0 * ln(z) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -2)
                + 3 * ln(z) * pow(x, 2) * CF * pow(NC, -1) * pow(xmz, -1)
                - 2 * ln(z) * pow(x, 2) * CF * pow(xmz, -1)
                + 1.0 / 2.0 * ln(z) * pow(x, 2) * CF * NC * pow(xmz, -2)
                - ln(z) * pow(x, 2) * CF * NC * pow(xmz, -1)
            )
            tmp += (
                -ln(z) * pow(x, 3) * CF * pow(NC, -1) * pow(poly2, -1)
                - ln(z) * pow(x, 3) * CF * pow(NC, -1) * pow(xmz, -2)
                - ln(z) * pow(x, 3) * CF * NC * pow(xmz, -2)
                + 3.0 / 2.0 * ln(z) * pow(x, 4) * CF * pow(NC, -1) * pow(poly2, -2)
                + 3.0 / 2.0 * ln(z) * pow(x, 5) * CF * pow(NC, -1) * pow(poly2, -2)
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1)
                - 3 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                - ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                + 8 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF
            )
            tmp += (
                -8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1)
            )
            tmp += (
                -ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                - ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * CF * pow(NC, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * x * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF
                + ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(NC, -1)
                + ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                - ln(z) * ln(1 + x * z) * pow(x, -2) * CF
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF
                + ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1)
                + ln(z) * ln(1 + x * z) * pow(x, -1) * CF
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF
                - 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                - 2 * ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1) * pow(opx, -1)
            )
            tmp += (
                +4 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + x * z) * CF * pow(omx, -1)
                + ln(z) * ln(1 + x * z) * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * CF
                - 2 * ln(z) * ln(1 + x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * ln(z) * ln(1 + x * z) * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1)
                + 4 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF
                + 2 * ln(z) * ln(1 + x * z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(z) * ln(1 + x * z) * x * z * CF
                - 2 * ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * ln(z) * ln(z + x) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(z) * ln(z + x) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(z + x) * CF * pow(omx, -1)
                - ln(z) * ln(z + x) * CF
                - 2 * ln(z) * ln(z + x) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * ln(z) * ln(z + x) * z * CF * pow(NC, -1)
                + 4 * ln(z) * ln(z + x) * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(z + x) * z * CF
                + 4 * ln(z) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * ln(z) * ln(z + x) * pow(z, 2) * CF
                + ln(z) * ln(z + x) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(z + x) * x * CF * pow(NC, -1)
                - ln(z) * ln(z + x) * x * CF
                - 2 * ln(z) * ln(z + x) * x * z * CF
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                + pow(ln(z), 2) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                - pow(ln(z), 2) * pow(x, -2) * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF
                + pow(ln(z), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                - pow(ln(z), 2) * pow(x, -2) * z * CF
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                +pow(ln(z), 2) * pow(x, -1) * CF * pow(NC, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * CF
                + pow(ln(z), 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                - pow(ln(z), 2) * pow(x, -1) * z * CF * pow(NC, -1)
                + pow(ln(z), 2) * pow(x, -1) * z * CF
                + 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF
                - 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                - 3 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 3 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omz, -1)
                + pow(ln(z), 2) * CF * pow(NC, -1) * pow(opx, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1)
                - pow(ln(z), 2) * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(opx, -1)
                + pow(ln(z), 2) * CF
                + 2 * pow(ln(z), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - pow(ln(z), 2) * CF * NC * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * CF * NC
                + 3 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                + 2 * pow(ln(z), 2) * z * CF * pow(omx, -1)
                + pow(ln(z), 2) * z * CF * pow(opx, -1)
                - 6 * pow(ln(z), 2) * z * CF
                - pow(ln(z), 2) * z * CF * NC * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * z * CF * NC
                - 2 * pow(ln(z), 2) * pow(z, 2) * CF * pow(omx, -1)
                + 4 * pow(ln(z), 2) * pow(z, 2) * CF
                + pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * x * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -1.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * x * CF * pow(NC, -1)
                - 2 * pow(ln(z), 2) * x * CF
                - 1.0 / 2.0 * pow(ln(z), 2) * x * CF * NC
                + 1.0 / 2.0 * pow(ln(z), 2) * x * z * CF * pow(NC, -1)
                + 2 * pow(ln(z), 2) * x * z * CF
                - 1.0 / 2.0 * pow(ln(z), 2) * x * z * CF * NC
                - 12 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 8 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 9 * ln(z) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(z) * ln(omx) * CF * pow(NC, -1)
                - ln(z) * ln(omx) * CF
                + 4 * ln(z) * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(omx) * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(omx) * CF * NC * pow(omz, -1)
                + 8 * ln(z) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 11 * ln(z) * ln(omx) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(omx) * z * CF
                - 2 * ln(z) * ln(omx) * z * CF * NC * pow(omx, -1)
                + 3 * ln(z) * ln(omx) * z * CF * NC
                + 3 * ln(z) * ln(omx) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(z) * ln(omx) * x * CF * pow(NC, -1)
                - ln(z) * ln(omx) * x * CF
                - 2 * ln(z) * ln(omx) * x * CF * NC * pow(omz, -1)
                + 3 * ln(z) * ln(omx) * x * CF * NC
                - 14 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 13 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 11 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 6 * ln(z) * ln(omz) * CF * pow(NC, -1)
                + ln(z) * ln(omz) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omz) * CF
                + 2 * ln(z) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - ln(z) * ln(omz) * CF * NC * pow(omx, -1)
                - 2 * ln(z) * ln(omz) * CF * NC * pow(omz, -1)
                + 13 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 18 * ln(z) * ln(omz) * z * CF * pow(NC, -1)
                - 2 * ln(z) * ln(omz) * z * CF * pow(omx, -1)
                + 4 * ln(z) * ln(omz) * z * CF
                - ln(z) * ln(omz) * z * CF * NC * pow(omx, -1)
            )
            tmp += (
                +6 * ln(z) * ln(omz) * z * CF * NC
                + 5 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 12 * ln(z) * ln(omz) * x * CF * pow(NC, -1)
                - 2 * ln(z) * ln(omz) * x * CF * NC * pow(omz, -1)
                + 6 * ln(z) * ln(omz) * x * CF * NC
                + 6 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                - 2 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                + 6 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                + 8 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * sqrtxz3
                + 6 * ln(sqrtxz3) * ArcTan(sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                + 13.0 / 6.0 * ln(omx) * pow(z, -1) * CF
                - 18 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 8 * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                - 23.0 / 2.0 * ln(omx) * CF * pow(NC, -1)
                - 13.0 / 2.0 * ln(omx) * CF
                + 12 * ln(omx) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(omx) * CF * NC * pow(omx, -1)
                - 12 * ln(omx) * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * ln(omx) * CF * NC
                - 4 * ln(omx) * pow(CF, 2)
                + 1.0 / 2.0 * ln(omx) * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * LMUF * CF * NC
                + 1.0 / 2.0 * ln(omx) * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * LMUA * CF * NC
                + 14 * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 39.0 / 2.0 * ln(omx) * z * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omx) * z * CF
                + 2.0 / 3.0 * ln(omx) * z * CF * NF
                - 8 * ln(omx) * z * CF * NC * pow(omx, -1)
                + 59.0 / 6.0 * ln(omx) * z * CF * NC
                - 4 * ln(omx) * z * pow(CF, 2)
                + 5.0 / 2.0 * ln(omx) * z * LMUF * CF * pow(NC, -1)
                - 5.0 / 2.0 * ln(omx) * z * LMUF * CF * NC
                + 1.0 / 2.0 * ln(omx) * z * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * z * LMUA * CF * NC
                + 4.0 / 3.0 * ln(omx) * pow(z, 2) * CF
                - 17.0 / 6.0 * ln(omx) * x * pow(z, -1) * CF
                - 5.0 / 2.0 * ln(omx) * x * CF * pow(NC, -1)
                + 9.0 / 2.0 * ln(omx) * x * CF
            )
            tmp += (
                +2.0 / 3.0 * ln(omx) * x * CF * NF
                + 35.0 / 6.0 * ln(omx) * x * CF * NC
                + 4 * ln(omx) * x * pow(CF, 2)
                + 5.0 / 2.0 * ln(omx) * x * LMUF * CF * pow(NC, -1)
                - 5.0 / 2.0 * ln(omx) * x * LMUF * CF * NC
                + 1.0 / 2.0 * ln(omx) * x * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * x * LMUA * CF * NC
                + 3.0 / 2.0 * ln(omx) * x * z * CF * pow(NC, -1)
                + 3.0 / 2.0 * ln(omx) * x * z * CF
                - 3.0 / 2.0 * ln(omx) * x * z * CF * NC
                + 4 * ln(omx) * x * z * pow(CF, 2)
                + 1.0 / 2.0 * ln(omx) * x * z * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * x * z * LMUF * CF * NC
                + 1.0 / 2.0 * ln(omx) * x * z * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omx) * x * z * LMUA * CF * NC
                - 2.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF
                - 5 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 3 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1) * pow(omz, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * CF * pow(NC, -1)
                + 4 * pow(ln(omx), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 2 * pow(ln(omx), 2) * CF * NC * pow(omx, -1)
                - 2 * pow(ln(omx), 2) * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * CF * NC
                + 3 * pow(ln(omx), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 13.0 / 2.0 * pow(ln(omx), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(omx), 2) * z * CF * NC * pow(omx, -1)
                + 11.0 / 2.0 * pow(ln(omx), 2) * z * CF * NC
                + 1.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(omx), 2) * x * CF * pow(NC, -1)
                - 2 * pow(ln(omx), 2) * x * CF * NC * pow(omz, -1)
                + 11.0 / 2.0 * pow(ln(omx), 2) * x * CF * NC
                - 1.0 / 2.0 * pow(ln(omx), 2) * x * z * CF * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * x * z * CF * NC
                - 8 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 6 * ln(omx) * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 5 * ln(omx) * ln(omz) * CF * pow(NC, -1)
            )
            tmp += (
                +8 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(omx) * ln(omz) * CF * NC * pow(omx, -1)
                - 4 * ln(omx) * ln(omz) * CF * NC * pow(omz, -1)
                + ln(omx) * ln(omz) * CF * NC
                + 6 * ln(omx) * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 11 * ln(omx) * ln(omz) * z * CF * pow(NC, -1)
                - 4 * ln(omx) * ln(omz) * z * CF * NC * pow(omx, -1)
                + 11 * ln(omx) * ln(omz) * z * CF * NC
                + 2 * ln(omx) * ln(omz) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 7 * ln(omx) * ln(omz) * x * CF * pow(NC, -1)
                - 4 * ln(omx) * ln(omz) * x * CF * NC * pow(omz, -1)
                + 11 * ln(omx) * ln(omz) * x * CF * NC
                - ln(omx) * ln(omz) * x * z * CF * pow(NC, -1)
                + ln(omx) * ln(omz) * x * z * CF * NC
                + 13.0 / 6.0 * ln(omz) * pow(z, -1) * CF
                - 18 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 10 * ln(omz) * CF * pow(NC, -1) * pow(omx, -1)
                + 18 * ln(omz) * CF * pow(NC, -1) * pow(omz, -1)
                - 1.0 / 2.0 * ln(omz) * CF * pow(NC, -1) * pow(omxmz, -1)
                - 14 * ln(omz) * CF * pow(NC, -1)
                - 13.0 / 2.0 * ln(omz) * CF
                + 12 * ln(omz) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(omz) * CF * NC * pow(omx, -1)
                - 12 * ln(omz) * CF * NC * pow(omz, -1)
                + 3.0 / 2.0 * ln(omz) * CF * NC * pow(omxmz, -1)
                + 2 * ln(omz) * CF * NC
                - 4 * ln(omz) * pow(CF, 2)
                + 1.0 / 2.0 * ln(omz) * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * LMUF * CF * NC
                + 1.0 / 2.0 * ln(omz) * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * LMUA * CF * NC
                + 16 * ln(omz) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 1.0 / 2.0 * ln(omz) * z * CF * pow(NC, -1) * pow(omxmz, -2)
                - 3.0 / 2.0 * ln(omz) * z * CF * pow(NC, -1) * pow(omxmz, -1)
                - 18 * ln(omz) * z * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(omz) * z * CF
                + 2.0 / 3.0 * ln(omz) * z * CF * NF
                - 8 * ln(omz) * z * CF * NC * pow(omx, -1)
                - 1.0 / 2.0 * ln(omz) * z * CF * NC * pow(omxmz, -2)
                + 1.0 / 2.0 * ln(omz) * z * CF * NC * pow(omxmz, -1)
            )
            tmp += (
                +25.0 / 3.0 * ln(omz) * z * CF * NC
                - 4 * ln(omz) * z * pow(CF, 2)
                + 1.0 / 2.0 * ln(omz) * z * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * z * LMUF * CF * NC
                + 5.0 / 2.0 * ln(omz) * z * LMUA * CF * pow(NC, -1)
                - 5.0 / 2.0 * ln(omz) * z * LMUA * CF * NC
                - 1.0 / 2.0 * ln(omz) * pow(z, 2) * CF * pow(NC, -1) * pow(omxmz, -2)
                + 4.0 / 3.0 * ln(omz) * pow(z, 2) * CF
                + 1.0 / 2.0 * ln(omz) * pow(z, 2) * CF * NC * pow(omxmz, -2)
                - 17.0 / 6.0 * ln(omz) * x * pow(z, -1) * CF
                - 2 * ln(omz) * x * CF * pow(NC, -1)
                + 9.0 / 2.0 * ln(omz) * x * CF
                + 2.0 / 3.0 * ln(omz) * x * CF * NF
                + 13.0 / 3.0 * ln(omz) * x * CF * NC
                + 4 * ln(omz) * x * pow(CF, 2)
                + 1.0 / 2.0 * ln(omz) * x * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * x * LMUF * CF * NC
                + 5.0 / 2.0 * ln(omz) * x * LMUA * CF * pow(NC, -1)
                - 5.0 / 2.0 * ln(omz) * x * LMUA * CF * NC
                + 3.0 / 2.0 * ln(omz) * x * z * CF
                + 4 * ln(omz) * x * z * pow(CF, 2)
                + 1.0 / 2.0 * ln(omz) * x * z * LMUF * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * x * z * LMUF * CF * NC
                + 1.0 / 2.0 * ln(omz) * x * z * LMUA * CF * pow(NC, -1)
                - 1.0 / 2.0 * ln(omz) * x * z * LMUA * CF * NC
                - 2.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF
                - 5 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 9.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * CF * pow(NC, -1)
                + 4 * pow(ln(omz), 2) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - 2 * pow(ln(omz), 2) * CF * NC * pow(omx, -1)
                - 2 * pow(ln(omz), 2) * CF * NC * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * CF * NC
                + 9.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 13.0 / 2.0 * pow(ln(omz), 2) * z * CF * pow(NC, -1)
                - 2 * pow(ln(omz), 2) * z * CF * NC * pow(omx, -1)
                + 11.0 / 2.0 * pow(ln(omz), 2) * z * CF * NC
                + 2 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(omz, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * x * CF * pow(NC, -1)
            )
            tmp += (
                -2 * pow(ln(omz), 2) * x * CF * NC * pow(omz, -1)
                + 11.0 / 2.0 * pow(ln(omz), 2) * x * CF * NC
                - 1.0 / 2.0 * pow(ln(omz), 2) * x * z * CF * pow(NC, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * x * z * CF * NC
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
            )
            tmp += (
                +2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
            )
            tmp += (
                +3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1)
                + 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1)
            )
            tmp += (
                -Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1)
                - 6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
            )
            tmp += (
                -3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
            )
            tmp += (
                +2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1)
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(NC, -1) * pow(sqrtxz2, -1)
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1)
                - 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 6) * CF * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
            )
            tmp += (
                -Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1)
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * CF * pow(NC, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1)
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF
            )
            tmp += (
                +Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, -1) * CF * pow(NC, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * CF * pow(NC, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * CF
                + 8 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 8 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                - 6 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                + 6 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 6 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * Li2(1 - x * pow(z, -1)) * CF * pow(NC, -1)
                - Li2(1 - x * pow(z, -1)) * CF * pow(omx, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * CF
                + 2 * Li2(1 - x * pow(z, -1)) * CF * NC * pow(omx, -1) * pow(omz, -1)
                - Li2(1 - x * pow(z, -1)) * CF * NC * pow(omx, -1)
                - Li2(1 - x * pow(z, -1)) * CF * NC * pow(omz, -1)
                - 6 * Li2(1 - x * pow(z, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 8 * Li2(1 - x * pow(z, -1)) * z * CF * pow(NC, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * z * CF * pow(omx, -1)
                - 4 * Li2(1 - x * pow(z, -1)) * z * CF
                - Li2(1 - x * pow(z, -1)) * z * CF * NC * pow(omx, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * CF * pow(NC, -1)
                + Li2(1 - x * pow(z, -1)) * x * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * Li2(1 - x * pow(z, -1)) * x * CF * pow(NC, -1)
                - Li2(1 - x * pow(z, -1)) * x * CF * NC * pow(omz, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -2 * Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(NC, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                - Li2(-x * pow(z, -1)) * pow(x, -2) * CF
                - 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF
                + Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -1) * CF
                - 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF
                - 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(-x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(-x * pow(z, -1)) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * CF * pow(omx, -1)
                + Li2(-x * pow(z, -1)) * CF * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * Li2(-x * pow(z, -1)) * z * CF * pow(NC, -1)
                - 4 * Li2(-x * pow(z, -1)) * z * CF * pow(omx, -1)
                - 2 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1)
                + 4 * Li2(-x * pow(z, -1)) * z * CF
                - 4 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * Li2(-x * pow(z, -1)) * x * CF * pow(NC, -1)
                + 2 * Li2(-x * pow(z, -1)) * x * CF
                - 2 * Li2(-x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
            )
            tmp += (
                +2 * Li2(-x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(-x) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * Li2(-x) * pow(x, -2) * CF * pow(NC, -1)
                - 2 * Li2(-x) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * Li2(-x) * pow(x, -2) * CF
                + 4 * Li2(-x) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * Li2(-x) * pow(x, -2) * z * CF
                - 2 * Li2(-x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(-x) * pow(x, -1) * CF * pow(NC, -1)
                - 2 * Li2(-x) * pow(x, -1) * CF
                + 4 * Li2(-x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * Li2(-x) * pow(x, -1) * z * CF * pow(NC, -1)
                + 4 * Li2(-x) * pow(x, -1) * z * CF
                + 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF
                + 2 * Li2(-x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(-x) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(-x) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * Li2(-x) * CF * pow(NC, -1)
                + 2 * Li2(-x) * CF * pow(opx, -1)
                - 4 * Li2(-x) * CF
                + 4 * Li2(-x) * z * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * Li2(-x) * z * CF * pow(opx, -1)
                + 8 * Li2(-x) * z * CF
                + 8 * Li2(-x) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * Li2(-x) * x * pow(z, -1) * CF * pow(NC, -1)
                + 4 * Li2(-x) * x * CF * pow(NC, -1)
                - 4 * Li2(-x) * x * CF
                + 8 * Li2(-x) * x * z * CF
                + Li2(-x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - Li2(-x * z) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                - 2 * Li2(-x * z) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(x, -2) * CF * pow(NC, -1)
                + Li2(-x * z) * pow(x, -2) * CF * pow(opx, -1)
                - Li2(-x * z) * pow(x, -2) * CF
                - 2 * Li2(-x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(x, -2) * z * CF
                + Li2(-x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
            )
            tmp += (
                -2 * Li2(-x * z) * pow(x, -1) * CF * pow(NC, -1)
                + Li2(-x * z) * pow(x, -1) * CF
                - 2 * Li2(-x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                - 2 * Li2(-x * z) * pow(x, -1) * z * CF
                - 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF
                - 2 * Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * Li2(-x * z) * CF * pow(NC, -1) * pow(omx, -1)
                - 2 * Li2(-x * z) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * Li2(-x * z) * CF * pow(NC, -1)
                + 2 * Li2(-x * z) * CF * pow(omx, -1)
                + Li2(-x * z) * CF * pow(opx, -1)
                - 2 * Li2(-x * z) * CF
                - 2 * Li2(-x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(-x * z) * z * CF * pow(omx, -1)
                - 2 * Li2(-x * z) * z * CF * pow(opx, -1)
                + 4 * Li2(-x * z) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * Li2(-x * z) * pow(z, 2) * CF
                + 2 * Li2(-x * z) * x * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(-x * z) * x * z * CF
                + 2 * Li2(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 2 * Li2(x) * pow(x, -2) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(x) * pow(x, -2) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * Li2(x) * pow(x, -2) * CF * pow(NC, -1)
                + 2 * Li2(x) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * Li2(x) * pow(x, -2) * CF
                - 4 * Li2(x) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * Li2(x) * pow(x, -2) * z * CF
                + 2 * Li2(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                - 4 * Li2(x) * pow(x, -1) * CF * pow(NC, -1)
                + 2 * Li2(x) * pow(x, -1) * CF
                - 4 * Li2(x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * Li2(x) * pow(x, -1) * z * CF * pow(NC, -1)
                - 4 * Li2(x) * pow(x, -1) * z * CF
                - 8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
            )
            tmp += (
                +8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF
                - 8 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 8 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                + 4 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                - 4 * Li2(x) * pow(z, -1) * CF * pow(NC, -1)
                - Li2(x) * pow(z, -1) * CF
                + 12 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                - 3 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
                - 8 * Li2(x) * CF * pow(NC, -1) * pow(omz, -1)
                + 4 * Li2(x) * CF * pow(NC, -1) * pow(opx, -1)
                + 4 * Li2(x) * CF * pow(NC, -1)
                + 3 * Li2(x) * CF * pow(omx, -1)
                - 2 * Li2(x) * CF * pow(opx, -1)
                - 3 * Li2(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 4 * Li2(x) * z * CF * pow(NC, -1) * pow(opx, -1)
                + 3 * Li2(x) * z * CF * pow(NC, -1)
                - 6 * Li2(x) * z * CF * pow(omx, -1)
                + 4 * Li2(x) * z * CF * pow(opx, -1)
                + 4 * Li2(x) * z * CF
                + Li2(x) * z * CF * NC
                + 8 * Li2(x) * pow(z, 2) * CF * pow(omx, -1)
                - 8 * Li2(x) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * Li2(x) * pow(z, 2) * CF
                + 4 * Li2(x) * x * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                - 4 * Li2(x) * x * pow(z, -1) * CF * pow(NC, -1)
                - Li2(x) * x * pow(z, -1) * CF
                - 4 * Li2(x) * x * CF * pow(NC, -1) * pow(omz, -1)
                - Li2(x) * x * CF * pow(NC, -1)
                + 2 * Li2(x) * x * CF
                + Li2(x) * x * CF * NC
                - 4 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1) * pow(omz, -1)
                + 5 * Li2(z) * CF * pow(NC, -1) * pow(omx, -1)
                + 3 * Li2(z) * CF * pow(NC, -1) * pow(omz, -1)
                - 2 * Li2(z) * CF * pow(NC, -1)
                + Li2(z) * CF * pow(omx, -1)
                - Li2(z) * CF
                + 5 * Li2(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                - 7 * Li2(z) * z * CF * pow(NC, -1)
                - 2 * Li2(z) * z * CF * pow(omx, -1)
                + 6 * Li2(z) * z * CF
                + 3 * Li2(z) * z * CF * NC
                + Li2(z) * x * CF * pow(NC, -1) * pow(omz, -1)
            )
            tmp += (
                -5 * Li2(z) * x * CF * pow(NC, -1)
                + Li2(z) * x * CF
                + 3 * Li2(z) * x * CF * NC
                + 3 * InvTanInt(-sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                - InvTanInt(-sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                + 3 * InvTanInt(-sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                + 4 * InvTanInt(-sqrtxz3) * z * CF * sqrtxz3
                + 3 * InvTanInt(-sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                + 6 * InvTanInt(z * sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                - 2 * InvTanInt(z * sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                + 6 * InvTanInt(z * sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                + 8 * InvTanInt(z * sqrtxz3) * z * CF * sqrtxz3
                + 6 * InvTanInt(z * sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
                - 3 * InvTanInt(sqrtxz3) * pow(x, -1) * CF * pow(NC, -1) * sqrtxz3
                + InvTanInt(sqrtxz3) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz3
                - 3 * InvTanInt(sqrtxz3) * z * CF * pow(NC, -1) * sqrtxz3
                - 4 * InvTanInt(sqrtxz3) * z * CF * sqrtxz3
                - 3 * InvTanInt(sqrtxz3) * x * CF * pow(NC, -1) * sqrtxz3
            )

            res += tmp

        return res


def c2p_q2q_eq(x, z, rsl, order, f=C2Pq2qEq_DR0123_scheme):
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
