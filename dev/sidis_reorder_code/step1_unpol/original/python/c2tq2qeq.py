from configs.eh import *


def C2Tq2qEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
    res = 0.0

    if cx == "D" and cz == "D":

        res = (
            -511.0 / 32.0 * pow(NC, -1) * CF
            + 15.0 / 2.0 * pow(NC, -1) * zeta3 * CF
            - 29.0 / 24.0 * pow(NC, -1) * pow(pi, 2) * CF
            + 7.0 / 180.0 * pow(NC, -1) * pow(pi, 4) * CF
            - 1537.0 / 96.0 * NC * CF
            + 41.0 / 6.0 * NC * zeta3 * CF
            - 277.0 / 216.0 * NC * pow(pi, 2) * CF
            + 1.0 / 18.0 * NC * pow(pi, 4) * CF
            + 127.0 / 24.0 * NF * CF
            + 2.0 / 3.0 * NF * zeta3 * CF
            + 19.0 / 54.0 * NF * pow(pi, 2) * CF
            - 44.0 / 3.0 * LMUR * NC * CF
            + 8.0 / 3.0 * LMUR * NF * CF
            - 93.0 / 16.0 * LMUF * pow(NC, -1) * CF
            + 5 * LMUF * pow(NC, -1) * zeta3 * CF
            - 1.0 / 4.0 * LMUF * pow(NC, -1) * pow(pi, 2) * CF
            + 245.0 / 48.0 * LMUF * NC * CF
            - 2 * LMUF * NC * zeta3 * CF
            - 13.0 / 36.0 * LMUF * NC * pow(pi, 2) * CF
            + 1.0 / 12.0 * LMUF * NF * CF
            + 1.0 / 9.0 * LMUF * NF * pow(pi, 2) * CF
            - 11.0 / 4.0 * LMUF * LMUR * NC * CF
            + 1.0 / 2.0 * LMUF * LMUR * NF * CF
            - 9.0 / 16.0 * pow(LMUF, 2) * pow(NC, -1) * CF
            + 1.0 / 6.0 * pow(LMUF, 2) * pow(NC, -1) * pow(pi, 2) * CF
            + 31.0 / 16.0 * pow(LMUF, 2) * NC * CF
            - 1.0 / 6.0 * pow(LMUF, 2) * NC * pow(pi, 2) * CF
            - 1.0 / 4.0 * pow(LMUF, 2) * NF * CF
            - 93.0 / 16.0 * LMUA * pow(NC, -1) * CF
            + 5 * LMUA * pow(NC, -1) * zeta3 * CF
            - 1.0 / 4.0 * LMUA * pow(NC, -1) * pow(pi, 2) * CF
            + 245.0 / 48.0 * LMUA * NC * CF
            - 2 * LMUA * NC * zeta3 * CF
            - 13.0 / 36.0 * LMUA * NC * pow(pi, 2) * CF
            + 1.0 / 12.0 * LMUA * NF * CF
            + 1.0 / 9.0 * LMUA * NF * pow(pi, 2) * CF
            - 11.0 / 4.0 * LMUA * LMUR * NC * CF
            + 1.0 / 2.0 * LMUA * LMUR * NF * CF
            - 9.0 / 8.0 * LMUA * LMUF * pow(NC, -1) * CF
            + 9.0 / 8.0 * LMUA * LMUF * NC * CF
            - 9.0 / 16.0 * pow(LMUA, 2) * pow(NC, -1) * CF
            + 1.0 / 6.0 * pow(LMUA, 2) * pow(NC, -1) * pow(pi, 2) * CF
            + 31.0 / 16.0 * pow(LMUA, 2) * NC * CF
            - 1.0 / 6.0 * pow(LMUA, 2) * NC * pow(pi, 2) * CF
            - 1.0 / 4.0 * pow(LMUA, 2) * NF * CF
        )

        return res

    if cx == "D" and cz == "0":

        res = (
            -4 * pow(NC, -1) * zeta3 * CF
            - 202.0 / 27.0 * NC * CF
            + 11 * NC * zeta3 * CF
            + 11.0 / 18.0 * NC * pow(pi, 2) * CF
            + 28.0 / 27.0 * NF * CF
            - 1.0 / 9.0 * NF * pow(pi, 2) * CF
            - 1.0 / 3.0 * LMUF * pow(NC, -1) * pow(pi, 2) * CF
            + 1.0 / 3.0 * LMUF * NC * pow(pi, 2) * CF
            - 8 * LMUA * pow(NC, -1) * CF
            - 1.0 / 3.0 * LMUA * pow(NC, -1) * pow(pi, 2) * CF
            + 5.0 / 9.0 * LMUA * NC * CF
            + 2.0 / 3.0 * LMUA * NC * pow(pi, 2) * CF
            + 10.0 / 9.0 * LMUA * NF * CF
            - 11.0 / 3.0 * LMUA * LMUR * NC * CF
            + 2.0 / 3.0 * LMUA * LMUR * NF * CF
            - 3.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * CF
            + 3.0 / 2.0 * LMUA * LMUF * NC * CF
            - 3.0 / 2.0 * pow(LMUA, 2) * pow(NC, -1) * CF
            + 10.0 / 3.0 * pow(LMUA, 2) * NC * CF
            - 1.0 / 3.0 * pow(LMUA, 2) * NF * CF
        )

        return res

    if cx == "D" and cz == "1":

        res = (
            8 * pow(NC, -1) * CF
            + 2.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
            - 5.0 / 9.0 * NC * CF
            - NC * pow(pi, 2) * CF
            - 10.0 / 9.0 * NF * CF
            + 11.0 / 3.0 * LMUR * NC * CF
            - 2.0 / 3.0 * LMUR * NF * CF
            + 3.0 / 2.0 * LMUF * pow(NC, -1) * CF
            - 3.0 / 2.0 * LMUF * NC * CF
            + 3.0 / 2.0 * LMUA * pow(NC, -1) * CF
            - 3.0 / 2.0 * LMUA * NC * CF
            - 2 * pow(LMUA, 2) * pow(NC, -1) * CF
            + 2 * pow(LMUA, 2) * NC * CF
        )

        return res

    if cx == "D" and cz == "2":

        res = -11.0 / 6.0 * NC * CF + 1.0 / 3.0 * NF * CF + 3 * LMUA * pow(NC, -1) * CF - 3 * LMUA * NC * CF

        return res

    if cx == "D" and cz == "3":

        res = -pow(NC, -1) * CF + NC * CF

        return res

    if cx == "0" and cz == "D":

        res = (
            -4 * pow(NC, -1) * zeta3 * CF
            - 202.0 / 27.0 * NC * CF
            + 11 * NC * zeta3 * CF
            + 11.0 / 18.0 * NC * pow(pi, 2) * CF
            + 28.0 / 27.0 * NF * CF
            - 1.0 / 9.0 * NF * pow(pi, 2) * CF
            - 8 * LMUF * pow(NC, -1) * CF
            - 1.0 / 3.0 * LMUF * pow(NC, -1) * pow(pi, 2) * CF
            + 5.0 / 9.0 * LMUF * NC * CF
            + 2.0 / 3.0 * LMUF * NC * pow(pi, 2) * CF
            + 10.0 / 9.0 * LMUF * NF * CF
            - 11.0 / 3.0 * LMUF * LMUR * NC * CF
            + 2.0 / 3.0 * LMUF * LMUR * NF * CF
            - 3.0 / 2.0 * pow(LMUF, 2) * pow(NC, -1) * CF
            + 10.0 / 3.0 * pow(LMUF, 2) * NC * CF
            - 1.0 / 3.0 * pow(LMUF, 2) * NF * CF
            - 1.0 / 3.0 * LMUA * pow(NC, -1) * pow(pi, 2) * CF
            + 1.0 / 3.0 * LMUA * NC * pow(pi, 2) * CF
            - 3.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * CF
            + 3.0 / 2.0 * LMUA * LMUF * NC * CF
        )

        return res

    if cx == "0" and cz == "0":

        res = (
            8 * pow(NC, -1) * CF
            + 2.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
            - 5.0 / 9.0 * NC * CF
            - NC * pow(pi, 2) * CF
            - 10.0 / 9.0 * NF * CF
            + 11.0 / 3.0 * LMUR * NC * CF
            - 2.0 / 3.0 * LMUR * NF * CF
            + 3.0 / 2.0 * LMUF * pow(NC, -1) * CF
            - 3.0 / 2.0 * LMUF * NC * CF
            + 3.0 / 2.0 * LMUA * pow(NC, -1) * CF
            - 3.0 / 2.0 * LMUA * NC * CF
            - 2 * LMUA * LMUF * pow(NC, -1) * CF
            + 2 * LMUA * LMUF * NC * CF
        )

        return res

    if cx == "0" and cz == "1":

        res = -11.0 / 3.0 * NC * CF + 2.0 / 3.0 * NF * CF + 2 * LMUF * pow(NC, -1) * CF - 2 * LMUF * NC * CF + 4 * LMUA * pow(NC, -1) * CF - 4 * LMUA * NC * CF

        return res

    if cx == "0" and cz == "2":

        res = -3 * pow(NC, -1) * CF + 3 * NC * CF

        return res

    if cx == "0" and cz == "3":

        res = 0

        return res

    if cx == "1" and cz == "D":

        res = (
            8 * pow(NC, -1) * CF
            + 2.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
            - 5.0 / 9.0 * NC * CF
            - NC * pow(pi, 2) * CF
            - 10.0 / 9.0 * NF * CF
            + 11.0 / 3.0 * LMUR * NC * CF
            - 2.0 / 3.0 * LMUR * NF * CF
            + 3.0 / 2.0 * LMUF * pow(NC, -1) * CF
            - 3.0 / 2.0 * LMUF * NC * CF
            - 2 * pow(LMUF, 2) * pow(NC, -1) * CF
            + 2 * pow(LMUF, 2) * NC * CF
            + 3.0 / 2.0 * LMUA * pow(NC, -1) * CF
            - 3.0 / 2.0 * LMUA * NC * CF
        )

        return res

    if cx == "1" and cz == "0":

        res = -11.0 / 3.0 * NC * CF + 2.0 / 3.0 * NF * CF + 4 * LMUF * pow(NC, -1) * CF - 4 * LMUF * NC * CF + 2 * LMUA * pow(NC, -1) * CF - 2 * LMUA * NC * CF

        return res

    if cx == "1" and cz == "1":

        res = -6 * pow(NC, -1) * CF + 6 * NC * CF

        return res

    if cx == "1" and cz == "2":

        res = 0

        return res

    if cx == "1" and cz == "3":

        res = 0

        return res

    if cx == "2" and cz == "D":

        res = -11.0 / 6.0 * NC * CF + 1.0 / 3.0 * NF * CF + 3 * LMUF * pow(NC, -1) * CF - 3 * LMUF * NC * CF

        return res

    if cx == "2" and cz == "0":

        res = -3 * pow(NC, -1) * CF + 3 * NC * CF

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

        res = -pow(NC, -1) * CF + NC * CF

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
            -1.0 / 4.0 * pow(NC, -1) * CF
            + 10 * pow(NC, -1) * zeta3 * CF * pow(omz, -1)
            - 4 * pow(NC, -1) * zeta3 * CF
            - 1.0 / 4.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
            + 7.0 / 12.0 * pow(NC, -1) * pow(pi, 2) * CF
            + 1.0 / 4.0 * pow(NC, -1) * z * CF
            - 4 * pow(NC, -1) * z * zeta3 * CF
            + 1.0 / 6.0 * pow(NC, -1) * z * pow(pi, 2) * CF
            - 107.0 / 108.0 * pow(z, -1) * CF
            - 11.0 / 9.0 * CF
            + 2 * zeta3 * CF
            - 1.0 / 6.0 * pow(pi, 2) * CF
            - 4.0 / 9.0 * z * CF
            + 2 * z * zeta3 * CF
            - 1.0 / 4.0 * z * pow(pi, 2) * CF
            + 287.0 / 108.0 * pow(z, 2) * CF
            + 197.0 / 108.0 * NC * CF
            - 14 * NC * zeta3 * CF * pow(omz, -1)
            + 5.0 / 2.0 * NC * zeta3 * CF
            + 1.0 / 4.0 * NC * pow(pi, 2) * CF * pow(omz, -1)
            - 29.0 / 36.0 * NC * pow(pi, 2) * CF
            + 611.0 / 108.0 * NC * z * CF
            + 5.0 / 2.0 * NC * z * zeta3 * CF
            - 2.0 / 9.0 * NC * z * pow(pi, 2) * CF
            - 19.0 / 54.0 * NF * CF
            + 1.0 / 18.0 * NF * pow(pi, 2) * CF
            - 37.0 / 54.0 * NF * z * CF
            + 1.0 / 18.0 * NF * z * pow(pi, 2) * CF
            + 11.0 / 6.0 * LMUR * NC * CF
            - 11.0 / 6.0 * LMUR * NC * z * CF
            - 1.0 / 3.0 * LMUR * NF * CF
            + 1.0 / 3.0 * LMUR * NF * z * CF
            + 3.0 / 4.0 * LMUF * pow(NC, -1) * CF
            + 1.0 / 6.0 * LMUF * pow(NC, -1) * pow(pi, 2) * CF
            - 3.0 / 4.0 * LMUF * pow(NC, -1) * z * CF
            + 1.0 / 6.0 * LMUF * pow(NC, -1) * z * pow(pi, 2) * CF
            - 3.0 / 4.0 * LMUF * NC * CF
            - 1.0 / 6.0 * LMUF * NC * pow(pi, 2) * CF
            + 3.0 / 4.0 * LMUF * NC * z * CF
            - 1.0 / 6.0 * LMUF * NC * z * pow(pi, 2) * CF
            + 7.0 / 4.0 * LMUA * pow(NC, -1) * CF
            + 1.0 / 4.0 * LMUA * pow(NC, -1) * pow(pi, 2) * CF
            + 25.0 / 4.0 * LMUA * pow(NC, -1) * z * CF
            + 1.0 / 4.0 * LMUA * pow(NC, -1) * z * pow(pi, 2) * CF
            + 7.0 / 18.0 * LMUA * pow(z, -1) * CF
            + 10.0 / 3.0 * LMUA * CF
            - 1.0 / 6.0 * LMUA * pow(pi, 2) * CF
            - 7.0 / 3.0 * LMUA * z * CF
            - 1.0 / 6.0 * LMUA * z * pow(pi, 2) * CF
            - 25.0 / 18.0 * LMUA * pow(z, 2) * CF
            - 169.0 / 36.0 * LMUA * NC * CF
            - 5.0 / 12.0 * LMUA * NC * pow(pi, 2) * CF
            + 149.0 / 36.0 * LMUA * NC * z * CF
            - 5.0 / 12.0 * LMUA * NC * z * pow(pi, 2) * CF
            + 1.0 / 9.0 * LMUA * NF * CF
        )
        res += (
            -11.0 / 9.0 * LMUA * NF * z * CF
            + 11.0 / 6.0 * LMUA * LMUR * NC * CF
            + 11.0 / 6.0 * LMUA * LMUR * NC * z * CF
            - 1.0 / 3.0 * LMUA * LMUR * NF * CF
            - 1.0 / 3.0 * LMUA * LMUR * NF * z * CF
            + 3.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * CF
            + 3.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * z * CF
            - 3.0 / 4.0 * LMUA * LMUF * NC * CF
            - 3.0 / 4.0 * LMUA * LMUF * NC * z * CF
            + 5.0 / 4.0 * pow(LMUA, 2) * pow(NC, -1) * CF
            + 1.0 / 4.0 * pow(LMUA, 2) * pow(NC, -1) * z * CF
            + 1.0 / 3.0 * pow(LMUA, 2) * pow(z, -1) * CF
            + 1.0 / 4.0 * pow(LMUA, 2) * CF
            - 1.0 / 4.0 * pow(LMUA, 2) * z * CF
            - 1.0 / 3.0 * pow(LMUA, 2) * pow(z, 2) * CF
            - 13.0 / 6.0 * pow(LMUA, 2) * NC * CF
            - 7.0 / 6.0 * pow(LMUA, 2) * NC * z * CF
            + 1.0 / 6.0 * pow(LMUA, 2) * NF * CF
            + 1.0 / 6.0 * pow(LMUA, 2) * NF * z * CF
            + 19.0 / 2.0 * ln(z) * pow(NC, -1) * CF * pow(omz, -1)
            - 15.0 / 4.0 * ln(z) * pow(NC, -1) * CF
            + 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
            - 1.0 / 3.0 * ln(z) * pow(NC, -1) * pow(pi, 2) * CF
            - 29.0 / 4.0 * ln(z) * pow(NC, -1) * z * CF
            - 1.0 / 3.0 * ln(z) * pow(NC, -1) * z * pow(pi, 2) * CF
            - 7.0 / 18.0 * ln(z) * pow(z, -1) * CF
            - 5 * ln(z) * CF
            + 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF
            - 9.0 / 2.0 * ln(z) * z * CF
            + 1.0 / 6.0 * ln(z) * z * pow(pi, 2) * CF
            - 31.0 / 18.0 * ln(z) * pow(z, 2) * CF
            - 113.0 / 18.0 * ln(z) * NC * CF * pow(omz, -1)
            + 233.0 / 36.0 * ln(z) * NC * CF
            - 5.0 / 6.0 * ln(z) * NC * pow(pi, 2) * CF * pow(omz, -1)
            + 1.0 / 2.0 * ln(z) * NC * pow(pi, 2) * CF
            + 101.0 / 36.0 * ln(z) * NC * z * CF
            + 1.0 / 2.0 * ln(z) * NC * z * pow(pi, 2) * CF
            - 5.0 / 9.0 * ln(z) * NF * CF * pow(omz, -1)
            - 1.0 / 18.0 * ln(z) * NF * CF
            + 11.0 / 18.0 * ln(z) * NF * z * CF
            + 11.0 / 3.0 * ln(z) * LMUR * NC * CF * pow(omz, -1)
            - 11.0 / 6.0 * ln(z) * LMUR * NC * CF
            - 11.0 / 6.0 * ln(z) * LMUR * NC * z * CF
            - 2.0 / 3.0 * ln(z) * LMUR * NF * CF * pow(omz, -1)
            + 1.0 / 3.0 * ln(z) * LMUR * NF * CF
            + 1.0 / 3.0 * ln(z) * LMUR * NF * z * CF
            + 3.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * CF * pow(omz, -1)
        )
        res += (
            -3.0 / 4.0 * ln(z) * LMUF * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(z) * LMUF * pow(NC, -1) * z * CF
            - 3.0 / 2.0 * ln(z) * LMUF * NC * CF * pow(omz, -1)
            + 3.0 / 4.0 * ln(z) * LMUF * NC * CF
            + 3.0 / 4.0 * ln(z) * LMUF * NC * z * CF
            + 3 * ln(z) * LMUA * pow(NC, -1) * CF * pow(omz, -1)
            - 17.0 / 4.0 * ln(z) * LMUA * pow(NC, -1) * CF
            - 7.0 / 4.0 * ln(z) * LMUA * pow(NC, -1) * z * CF
            - 2.0 / 3.0 * ln(z) * LMUA * pow(z, -1) * CF
            + 1.0 / 2.0 * ln(z) * LMUA * CF
            + 2 * ln(z) * LMUA * z * CF
            + 2.0 / 3.0 * ln(z) * LMUA * pow(z, 2) * CF
            - 20.0 / 3.0 * ln(z) * LMUA * NC * CF * pow(omz, -1)
            + 61.0 / 12.0 * ln(z) * LMUA * NC * CF
            + 31.0 / 12.0 * ln(z) * LMUA * NC * z * CF
            + 2.0 / 3.0 * ln(z) * LMUA * NF * CF * pow(omz, -1)
            - 1.0 / 3.0 * ln(z) * LMUA * NF * CF
            - 1.0 / 3.0 * ln(z) * LMUA * NF * z * CF
            + ln(z) * pow(LMUA, 2) * pow(NC, -1) * CF * pow(omz, -1)
            - 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * pow(NC, -1) * z * CF
            + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF
            + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * z * CF
            - ln(z) * pow(LMUA, 2) * NC * CF * pow(omz, -1)
            + 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * NC * CF
            + 3.0 / 4.0 * ln(z) * pow(LMUA, 2) * NC * z * CF
            - 9.0 / 8.0 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omz, -1)
            + 21.0 / 8.0 * pow(ln(z), 2) * pow(NC, -1) * CF
            + 7.0 / 8.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF
            + 1.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF
            - 1.0 / 8.0 * pow(ln(z), 2) * CF
            - 5.0 / 8.0 * pow(ln(z), 2) * z * CF
            + 49.0 / 24.0 * pow(ln(z), 2) * NC * CF * pow(omz, -1)
            - 25.0 / 12.0 * pow(ln(z), 2) * NC * CF
            - 5.0 / 6.0 * pow(ln(z), 2) * NC * z * CF
            - 1.0 / 6.0 * pow(ln(z), 2) * NF * CF * pow(omz, -1)
            + 1.0 / 12.0 * pow(ln(z), 2) * NF * CF
            + 1.0 / 12.0 * pow(ln(z), 2) * NF * z * CF
            - 3 * pow(ln(z), 2) * LMUA * pow(NC, -1) * CF * pow(omz, -1)
            + 2 * pow(ln(z), 2) * LMUA * pow(NC, -1) * CF
            + 2 * pow(ln(z), 2) * LMUA * pow(NC, -1) * z * CF
            - pow(ln(z), 2) * LMUA * CF
        )
        res += (
            -pow(ln(z), 2) * LMUA * z * CF
            + 2 * pow(ln(z), 2) * LMUA * NC * CF * pow(omz, -1)
            - 3.0 / 2.0 * pow(ln(z), 2) * LMUA * NC * CF
            - 3.0 / 2.0 * pow(ln(z), 2) * LMUA * NC * z * CF
            + 5.0 / 3.0 * pow(ln(z), 3) * pow(NC, -1) * CF * pow(omz, -1)
            - 25.0 / 24.0 * pow(ln(z), 3) * pow(NC, -1) * CF
            - 25.0 / 24.0 * pow(ln(z), 3) * pow(NC, -1) * z * CF
            + 5.0 / 12.0 * pow(ln(z), 3) * CF
            + 5.0 / 12.0 * pow(ln(z), 3) * z * CF
            - 5.0 / 6.0 * pow(ln(z), 3) * NC * CF * pow(omz, -1)
            + 5.0 / 8.0 * pow(ln(z), 3) * NC * CF
            + 5.0 / 8.0 * pow(ln(z), 3) * NC * z * CF
            + 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
            - 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * pow(NC, -1) * CF
            - 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * pow(NC, -1) * z * CF
            - 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * NC * CF * pow(omz, -1)
            + 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * NC * CF
            + 1.0 / 4.0 * pow(ln(z), 2) * ln(omz) * NC * z * CF
            - 3.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * CF
            + 3.0 / 2.0 * ln(z) * ln(omz) * pow(NC, -1) * z * CF
            + 3.0 / 2.0 * ln(z) * ln(omz) * NC * CF
            - 3.0 / 2.0 * ln(z) * ln(omz) * NC * z * CF
            + 2 * ln(z) * ln(omz) * LMUA * pow(NC, -1) * CF * pow(omz, -1)
            - ln(z) * ln(omz) * LMUA * pow(NC, -1) * CF
            - ln(z) * ln(omz) * LMUA * pow(NC, -1) * z * CF
            - 2 * ln(z) * ln(omz) * LMUA * NC * CF * pow(omz, -1)
            + ln(z) * ln(omz) * LMUA * NC * CF
            + ln(z) * ln(omz) * LMUA * NC * z * CF
            - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omz, -1)
            + 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * pow(NC, -1) * CF
            + 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * pow(NC, -1) * z * CF
            - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF
            - 1.0 / 2.0 * ln(z) * pow(ln(omz), 2) * z * CF
            + 5.0 / 2.0 * ln(z) * pow(ln(omz), 2) * NC * CF * pow(omz, -1)
            - 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * NC * CF
            - 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * NC * z * CF
            + 4 * ln(z) * Li2(z) * pow(NC, -1) * CF * pow(omz, -1)
        )
        res += (
            -2 * ln(z) * Li2(z) * pow(NC, -1) * CF
            - 2 * ln(z) * Li2(z) * pow(NC, -1) * z * CF
            - 6 * ln(z) * Li2(z) * NC * CF * pow(omz, -1)
            + 3 * ln(z) * Li2(z) * NC * CF
            + 3 * ln(z) * Li2(z) * NC * z * CF
            - 5.0 / 4.0 * ln(omz) * pow(NC, -1) * CF
            - 1.0 / 6.0 * ln(omz) * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
            - 1.0 / 3.0 * ln(omz) * pow(NC, -1) * pow(pi, 2) * CF
            - 7 * ln(omz) * pow(NC, -1) * z * CF
            - 1.0 / 3.0 * ln(omz) * pow(NC, -1) * z * pow(pi, 2) * CF
            - 7.0 / 18.0 * ln(omz) * pow(z, -1) * CF
            - 10.0 / 3.0 * ln(omz) * CF
            + 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF
            + 7.0 / 3.0 * ln(omz) * z * CF
            + 1.0 / 6.0 * ln(omz) * z * pow(pi, 2) * CF
            + 25.0 / 18.0 * ln(omz) * pow(z, 2) * CF
            + 67.0 / 36.0 * ln(omz) * NC * CF
            - 1.0 / 6.0 * ln(omz) * NC * pow(pi, 2) * CF * pow(omz, -1)
            + 2.0 / 3.0 * ln(omz) * NC * pow(pi, 2) * CF
            - 14.0 / 9.0 * ln(omz) * NC * z * CF
            + 2.0 / 3.0 * ln(omz) * NC * z * pow(pi, 2) * CF
            + 2.0 / 9.0 * ln(omz) * NF * CF
            + 8.0 / 9.0 * ln(omz) * NF * z * CF
            - 11.0 / 6.0 * ln(omz) * LMUR * NC * CF
            - 11.0 / 6.0 * ln(omz) * LMUR * NC * z * CF
            + 1.0 / 3.0 * ln(omz) * LMUR * NF * CF
            + 1.0 / 3.0 * ln(omz) * LMUR * NF * z * CF
            - 3.0 / 4.0 * ln(omz) * LMUF * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(omz) * LMUF * pow(NC, -1) * z * CF
            + 3.0 / 4.0 * ln(omz) * LMUF * NC * CF
            + 3.0 / 4.0 * ln(omz) * LMUF * NC * z * CF
            - 3.0 / 4.0 * ln(omz) * LMUA * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(omz) * LMUA * pow(NC, -1) * z * CF
            - 2.0 / 3.0 * ln(omz) * LMUA * pow(z, -1) * CF
            - 1.0 / 2.0 * ln(omz) * LMUA * CF
            + 1.0 / 2.0 * ln(omz) * LMUA * z * CF
            + 2.0 / 3.0 * ln(omz) * LMUA * pow(z, 2) * CF
            + 3.0 / 4.0 * ln(omz) * LMUA * NC * CF
            + 3.0 / 4.0 * ln(omz) * LMUA * NC * z * CF
            + ln(omz) * pow(LMUA, 2) * pow(NC, -1) * CF
            + ln(omz) * pow(LMUA, 2) * pow(NC, -1) * z * CF
            - ln(omz) * pow(LMUA, 2) * NC * CF
            - ln(omz) * pow(LMUA, 2) * NC * z * CF
            + 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF
            + 1.0 / 4.0 * pow(ln(omz), 2) * CF
        )
        res += (
            -1.0 / 4.0 * pow(ln(omz), 2) * z * CF
            - 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF
            + 11.0 / 12.0 * pow(ln(omz), 2) * NC * CF
            + 11.0 / 12.0 * pow(ln(omz), 2) * NC * z * CF
            - 1.0 / 6.0 * pow(ln(omz), 2) * NF * CF
            - 1.0 / 6.0 * pow(ln(omz), 2) * NF * z * CF
            - 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * pow(NC, -1) * CF
            - 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * pow(NC, -1) * z * CF
            + 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * NC * CF
            + 3.0 / 2.0 * pow(ln(omz), 2) * LMUA * NC * z * CF
            + 1.0 / 2.0 * pow(ln(omz), 3) * pow(NC, -1) * CF
            + 1.0 / 2.0 * pow(ln(omz), 3) * pow(NC, -1) * z * CF
            - 1.0 / 2.0 * pow(ln(omz), 3) * NC * CF
            - 1.0 / 2.0 * pow(ln(omz), 3) * NC * z * CF
            + ln(omz) * Li2(z) * pow(NC, -1) * CF * pow(omz, -1)
            - ln(omz) * Li2(z) * CF
            - ln(omz) * Li2(z) * z * CF
            + ln(omz) * Li2(z) * NC * CF * pow(omz, -1)
            - ln(omz) * Li2(z) * NC * CF
            - ln(omz) * Li2(z) * NC * z * CF
            + 3 * Li3(1 - z) * pow(NC, -1) * CF * pow(omz, -1)
            - Li3(1 - z) * pow(NC, -1) * CF
            - Li3(1 - z) * pow(NC, -1) * z * CF
            - Li3(1 - z) * CF
            - Li3(1 - z) * z * CF
            + 3 * Li3(1 - z) * NC * CF * pow(omz, -1)
            - 2 * Li3(1 - z) * NC * CF
            - 2 * Li3(1 - z) * NC * z * CF
            - 10 * Li3(z) * pow(NC, -1) * CF * pow(omz, -1)
            + 6 * Li3(z) * pow(NC, -1) * CF
            + 6 * Li3(z) * pow(NC, -1) * z * CF
            - 2 * Li3(z) * CF
            - 2 * Li3(z) * z * CF
            + 14 * Li3(z) * NC * CF * pow(omz, -1)
            - 8 * Li3(z) * NC * CF
            - 8 * Li3(z) * NC * z * CF
            + 3.0 / 2.0 * Li2(z) * pow(NC, -1) * CF * pow(omz, -1)
            - 9.0 / 2.0 * Li2(z) * pow(NC, -1) * CF
            - 2.0 / 3.0 * Li2(z) * pow(z, -1) * CF
            + 1.0 / 2.0 * Li2(z) * CF
            + 2 * Li2(z) * z * CF
            + 2.0 / 3.0 * Li2(z) * pow(z, 2) * CF
            - 3.0 / 2.0 * Li2(z) * NC * CF * pow(omz, -1)
            + 7.0 / 2.0 * Li2(z) * NC * CF
            - Li2(z) * NC * z * CF
            - 1.0 / 2.0 * Li2(z) * LMUA * pow(NC, -1) * CF
            - 1.0 / 2.0 * Li2(z) * LMUA * pow(NC, -1) * z * CF
            + Li2(z) * LMUA * CF
            + Li2(z) * LMUA * z * CF
            + 1.0 / 2.0 * Li2(z) * LMUA * NC * CF
        )
        res += +1.0 / 2.0 * Li2(z) * LMUA * NC * z * CF

        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = (
            -pow(NC, -1) * CF
            - 5.0 / 12.0 * pow(NC, -1) * pow(pi, 2) * CF
            - 7 * pow(NC, -1) * z * CF
            - 5.0 / 12.0 * pow(NC, -1) * z * pow(pi, 2) * CF
            - 7.0 / 18.0 * pow(z, -1) * CF
            - 10.0 / 3.0 * CF
            + 1.0 / 6.0 * pow(pi, 2) * CF
            + 7.0 / 3.0 * z * CF
            + 1.0 / 6.0 * z * pow(pi, 2) * CF
            + 25.0 / 18.0 * pow(z, 2) * CF
            + 19.0 / 9.0 * NC * CF
            + 7.0 / 12.0 * NC * pow(pi, 2) * CF
            - 14.0 / 9.0 * NC * z * CF
            + 7.0 / 12.0 * NC * z * pow(pi, 2) * CF
            + 2.0 / 9.0 * NF * CF
            + 8.0 / 9.0 * NF * z * CF
            - 11.0 / 6.0 * LMUR * NC * CF
            - 11.0 / 6.0 * LMUR * NC * z * CF
            + 1.0 / 3.0 * LMUR * NF * CF
            + 1.0 / 3.0 * LMUR * NF * z * CF
            + 1.0 / 4.0 * LMUF * pow(NC, -1) * CF
            - 7.0 / 4.0 * LMUF * pow(NC, -1) * z * CF
            - 1.0 / 4.0 * LMUF * NC * CF
            + 7.0 / 4.0 * LMUF * NC * z * CF
            - 7.0 / 4.0 * LMUA * pow(NC, -1) * CF
            + 1.0 / 4.0 * LMUA * pow(NC, -1) * z * CF
            - 2.0 / 3.0 * LMUA * pow(z, -1) * CF
            - 1.0 / 2.0 * LMUA * CF
            + 1.0 / 2.0 * LMUA * z * CF
            + 2.0 / 3.0 * LMUA * pow(z, 2) * CF
            + 7.0 / 4.0 * LMUA * NC * CF
            - 1.0 / 4.0 * LMUA * NC * z * CF
            + LMUA * LMUF * pow(NC, -1) * CF
            + LMUA * LMUF * pow(NC, -1) * z * CF
            - LMUA * LMUF * NC * CF
            - LMUA * LMUF * NC * z * CF
            - 3.0 / 2.0 * ln(z) * pow(NC, -1) * CF * pow(omz, -1)
            + 7.0 / 2.0 * ln(z) * pow(NC, -1) * CF
            + ln(z) * pow(NC, -1) * z * CF
            + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF
            - 1.0 / 2.0 * ln(z) * CF
            - 2 * ln(z) * z * CF
            - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF
            + 3.0 / 2.0 * ln(z) * NC * CF * pow(omz, -1)
            - 5.0 / 2.0 * ln(z) * NC * CF
            + 2 * ln(z) * LMUF * pow(NC, -1) * CF * pow(omz, -1)
            - ln(z) * LMUF * pow(NC, -1) * CF
            - ln(z) * LMUF * pow(NC, -1) * z * CF
            - 2 * ln(z) * LMUF * NC * CF * pow(omz, -1)
            + ln(z) * LMUF * NC * CF
            + ln(z) * LMUF * NC * z * CF
            - 2 * ln(z) * LMUA * pow(NC, -1) * CF * pow(omz, -1)
            + 3.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * CF
            + 3.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * z * CF
            - ln(z) * LMUA * CF
            - ln(z) * LMUA * z * CF
            + 2 * ln(z) * LMUA * NC * CF * pow(omz, -1)
            - 3.0 / 2.0 * ln(z) * LMUA * NC * CF
            - 3.0 / 2.0 * ln(z) * LMUA * NC * z * CF
        )
        res += (
            +3 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omz, -1)
            - 2 * pow(ln(z), 2) * pow(NC, -1) * CF
            - 2 * pow(ln(z), 2) * pow(NC, -1) * z * CF
            + pow(ln(z), 2) * CF
            + pow(ln(z), 2) * z * CF
            - 2 * pow(ln(z), 2) * NC * CF * pow(omz, -1)
            + 3.0 / 2.0 * pow(ln(z), 2) * NC * CF
            + 3.0 / 2.0 * pow(ln(z), 2) * NC * z * CF
            - 2 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
            + ln(z) * ln(omz) * pow(NC, -1) * CF
            + ln(z) * ln(omz) * pow(NC, -1) * z * CF
            + 2 * ln(z) * ln(omz) * NC * CF * pow(omz, -1)
            - ln(z) * ln(omz) * NC * CF
            - ln(z) * ln(omz) * NC * z * CF
            + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF
            + 1.0 / 2.0 * ln(omz) * CF
            - 1.0 / 2.0 * ln(omz) * z * CF
            - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF
            + 11.0 / 6.0 * ln(omz) * NC * CF
            + 11.0 / 6.0 * ln(omz) * NC * z * CF
            - 1.0 / 3.0 * ln(omz) * NF * CF
            - 1.0 / 3.0 * ln(omz) * NF * z * CF
            - ln(omz) * LMUF * pow(NC, -1) * CF
            - ln(omz) * LMUF * pow(NC, -1) * z * CF
            + ln(omz) * LMUF * NC * CF
            + ln(omz) * LMUF * NC * z * CF
            - 2 * ln(omz) * LMUA * pow(NC, -1) * CF
            - 2 * ln(omz) * LMUA * pow(NC, -1) * z * CF
            + 2 * ln(omz) * LMUA * NC * CF
            + 2 * ln(omz) * LMUA * NC * z * CF
            + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF
            + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF
            - 3.0 / 2.0 * pow(ln(omz), 2) * NC * CF
            - 3.0 / 2.0 * pow(ln(omz), 2) * NC * z * CF
            + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * CF
            + 1.0 / 2.0 * Li2(z) * pow(NC, -1) * z * CF
            - Li2(z) * CF
            - Li2(z) * z * CF
            - 1.0 / 2.0 * Li2(z) * NC * CF
            - 1.0 / 2.0 * Li2(z) * NC * z * CF
        )

        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = (
            2.0 / 3.0 * pow(z, -1) * CF
            + 1.0 / 2.0 * CF
            - 1.0 / 2.0 * z * CF
            - 2.0 / 3.0 * pow(z, 2) * CF
            + 11.0 / 6.0 * NC * CF
            + 11.0 / 6.0 * NC * z * CF
            - 1.0 / 3.0 * NF * CF
            - 1.0 / 3.0 * NF * z * CF
            - 2 * LMUF * pow(NC, -1) * CF
            - 2 * LMUF * pow(NC, -1) * z * CF
            + 2 * LMUF * NC * CF
            + 2 * LMUF * NC * z * CF
            - LMUA * pow(NC, -1) * CF
            - LMUA * pow(NC, -1) * z * CF
            + LMUA * NC * CF
            + LMUA * NC * z * CF
            - 1.0 / 2.0 * ln(z) * pow(NC, -1) * CF
            - 1.0 / 2.0 * ln(z) * pow(NC, -1) * z * CF
            + ln(z) * CF
            + ln(z) * z * CF
            + 1.0 / 2.0 * ln(z) * NC * CF
            + 1.0 / 2.0 * ln(z) * NC * z * CF
            + 3 * ln(omz) * pow(NC, -1) * CF
            + 3 * ln(omz) * pow(NC, -1) * z * CF
            - 3 * ln(omz) * NC * CF
            - 3 * ln(omz) * NC * z * CF
        )

        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        res = 3.0 / 2.0 * pow(NC, -1) * CF + 3.0 / 2.0 * pow(NC, -1) * z * CF - 3.0 / 2.0 * NC * CF - 3.0 / 2.0 * NC * z * CF

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
            29.0 / 4.0 * pow(NC, -1) * CF
            - 7 * pow(NC, -1) * zeta3 * CF * pow(omx, -1)
            + 11.0 / 2.0 * pow(NC, -1) * zeta3 * CF
            + 1.0 / 4.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
            - 1.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF
            - 31.0 / 4.0 * pow(NC, -1) * x * CF
            + 11.0 / 2.0 * pow(NC, -1) * x * zeta3 * CF
            + 5.0 / 12.0 * pow(NC, -1) * x * pow(pi, 2) * CF
            + 52.0 / 27.0 * pow(x, -1) * CF
            - 41.0 / 36.0 * CF
            + 1.0 / 6.0 * pow(pi, 2) * CF
            + 17.0 / 36.0 * x * CF
            + 1.0 / 2.0 * x * pow(pi, 2) * CF
            - 34.0 / 27.0 * pow(x, 2) * CF
            + 1.0 / 3.0 * pow(x, 2) * pow(pi, 2) * CF
            - 91.0 / 108.0 * NC * CF
            + 5 * NC * zeta3 * CF * pow(omx, -1)
            - 8 * NC * zeta3 * CF
            + 13.0 / 36.0 * NC * pow(pi, 2) * CF * pow(omx, -1)
            - 13.0 / 36.0 * NC * pow(pi, 2) * CF
            + 845.0 / 108.0 * NC * x * CF
            - 8 * NC * x * zeta3 * CF
            - 7.0 / 9.0 * NC * x * pow(pi, 2) * CF
            - 37.0 / 54.0 * NF * CF
            - 1.0 / 9.0 * NF * pow(pi, 2) * CF * pow(omx, -1)
            + 1.0 / 9.0 * NF * pow(pi, 2) * CF
            - 19.0 / 54.0 * NF * x * CF
            + 1.0 / 9.0 * NF * x * pow(pi, 2) * CF
            + 11.0 / 6.0 * LMUR * NC * CF
            - 11.0 / 6.0 * LMUR * NC * x * CF
            - 1.0 / 3.0 * LMUR * NF * CF
            + 1.0 / 3.0 * LMUR * NF * x * CF
            + 7.0 / 4.0 * LMUF * pow(NC, -1) * CF
            + 1.0 / 4.0 * LMUF * pow(NC, -1) * pow(pi, 2) * CF
            + 25.0 / 4.0 * LMUF * pow(NC, -1) * x * CF
            + 1.0 / 4.0 * LMUF * pow(NC, -1) * x * pow(pi, 2) * CF
            - 13.0 / 9.0 * LMUF * pow(x, -1) * CF
            + 11.0 / 6.0 * LMUF * CF
            - 1.0 / 6.0 * LMUF * pow(pi, 2) * CF
            - 17.0 / 6.0 * LMUF * x * CF
            - 1.0 / 6.0 * LMUF * x * pow(pi, 2) * CF
            + 22.0 / 9.0 * LMUF * pow(x, 2) * CF
            - 169.0 / 36.0 * LMUF * NC * CF
            - 5.0 / 12.0 * LMUF * NC * pow(pi, 2) * CF
            + 149.0 / 36.0 * LMUF * NC * x * CF
            - 5.0 / 12.0 * LMUF * NC * x * pow(pi, 2) * CF
            + 1.0 / 9.0 * LMUF * NF * CF
            - 11.0 / 9.0 * LMUF * NF * x * CF
            + 11.0 / 6.0 * LMUF * LMUR * NC * CF
            + 11.0 / 6.0 * LMUF * LMUR * NC * x * CF
            - 1.0 / 3.0 * LMUF * LMUR * NF * CF
            - 1.0 / 3.0 * LMUF * LMUR * NF * x * CF
            + 5.0 / 4.0 * pow(LMUF, 2) * pow(NC, -1) * CF
            + 1.0 / 4.0 * pow(LMUF, 2) * pow(NC, -1) * x * CF
            + 1.0 / 3.0 * pow(LMUF, 2) * pow(x, -1) * CF
        )
        res += (
            +1.0 / 4.0 * pow(LMUF, 2) * CF
            - 1.0 / 4.0 * pow(LMUF, 2) * x * CF
            - 1.0 / 3.0 * pow(LMUF, 2) * pow(x, 2) * CF
            - 13.0 / 6.0 * pow(LMUF, 2) * NC * CF
            - 7.0 / 6.0 * pow(LMUF, 2) * NC * x * CF
            + 1.0 / 6.0 * pow(LMUF, 2) * NF * CF
            + 1.0 / 6.0 * pow(LMUF, 2) * NF * x * CF
            + 3.0 / 4.0 * LMUA * pow(NC, -1) * CF
            + 1.0 / 6.0 * LMUA * pow(NC, -1) * pow(pi, 2) * CF
            - 3.0 / 4.0 * LMUA * pow(NC, -1) * x * CF
            + 1.0 / 6.0 * LMUA * pow(NC, -1) * x * pow(pi, 2) * CF
            - 3.0 / 4.0 * LMUA * NC * CF
            - 1.0 / 6.0 * LMUA * NC * pow(pi, 2) * CF
            + 3.0 / 4.0 * LMUA * NC * x * CF
            - 1.0 / 6.0 * LMUA * NC * x * pow(pi, 2) * CF
            + 3.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * CF
            + 3.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * x * CF
            - 3.0 / 4.0 * LMUA * LMUF * NC * CF
            - 3.0 / 4.0 * LMUA * LMUF * NC * x * CF
            - 10 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
            + 21.0 / 4.0 * ln(x) * pow(NC, -1) * CF
            - ln(x) * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
            + 2.0 / 3.0 * ln(x) * pow(NC, -1) * pow(pi, 2) * CF
            + 11 * ln(x) * pow(NC, -1) * x * CF
            + 2.0 / 3.0 * ln(x) * pow(NC, -1) * x * pow(pi, 2) * CF
            + 23.0 / 6.0 * ln(x) * CF
            - 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF
            - 5.0 / 6.0 * ln(x) * x * CF
            - 1.0 / 3.0 * ln(x) * x * pow(pi, 2) * CF
            + 38.0 / 9.0 * ln(x) * pow(x, 2) * CF
            - 5.0 / 3.0 * ln(x) * NC * CF * pow(omx, -1)
            + 1.0 / 12.0 * ln(x) * NC * CF
            + 5.0 / 3.0 * ln(x) * NC * pow(pi, 2) * CF * pow(omx, -1)
            - ln(x) * NC * pow(pi, 2) * CF
            + 13.0 / 6.0 * ln(x) * NC * x * CF
            - ln(x) * NC * x * pow(pi, 2) * CF
            + 5.0 / 3.0 * ln(x) * NF * CF * pow(omx, -1)
            - 5.0 / 6.0 * ln(x) * NF * CF
            - 7.0 / 6.0 * ln(x) * NF * x * CF
            - 11.0 / 3.0 * ln(x) * LMUR * NC * CF * pow(omx, -1)
            + 11.0 / 6.0 * ln(x) * LMUR * NC * CF
            + 11.0 / 6.0 * ln(x) * LMUR * NC * x * CF
            + 2.0 / 3.0 * ln(x) * LMUR * NF * CF * pow(omx, -1)
            - 1.0 / 3.0 * ln(x) * LMUR * NF * CF
            - 1.0 / 3.0 * ln(x) * LMUR * NF * x * CF
            - 3 * ln(x) * LMUF * pow(NC, -1) * CF * pow(omx, -1)
            + 3.0 / 4.0 * ln(x) * LMUF * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(x) * LMUF * pow(NC, -1) * x * CF
        )
        res += (
            -ln(x) * LMUF * CF
            - 3 * ln(x) * LMUF * x * CF
            - 2 * ln(x) * LMUF * pow(x, 2) * CF
            - 2.0 / 3.0 * ln(x) * LMUF * NC * CF * pow(omx, -1)
            + 1.0 / 12.0 * ln(x) * LMUF * NC * CF
            + 19.0 / 12.0 * ln(x) * LMUF * NC * x * CF
            + 2.0 / 3.0 * ln(x) * LMUF * NF * CF * pow(omx, -1)
            - 1.0 / 3.0 * ln(x) * LMUF * NF * CF
            - 1.0 / 3.0 * ln(x) * LMUF * NF * x * CF
            + ln(x) * pow(LMUF, 2) * pow(NC, -1) * CF * pow(omx, -1)
            - 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * pow(NC, -1) * x * CF
            + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * CF
            + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * x * CF
            - ln(x) * pow(LMUF, 2) * NC * CF * pow(omx, -1)
            + 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * NC * CF
            + 3.0 / 4.0 * ln(x) * pow(LMUF, 2) * NC * x * CF
            - 3.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * CF * pow(omx, -1)
            + 3.0 / 4.0 * ln(x) * LMUA * pow(NC, -1) * CF
            + 3.0 / 4.0 * ln(x) * LMUA * pow(NC, -1) * x * CF
            + 3.0 / 2.0 * ln(x) * LMUA * NC * CF * pow(omx, -1)
            - 3.0 / 4.0 * ln(x) * LMUA * NC * CF
            - 3.0 / 4.0 * ln(x) * LMUA * NC * x * CF
            - 9.0 / 8.0 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
            + 1.0 / 4.0 * pow(ln(x), 2) * pow(NC, -1) * CF
            - 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * CF
            - 13.0 / 8.0 * pow(ln(x), 2) * CF
            - 13.0 / 8.0 * pow(ln(x), 2) * x * CF
            - 5.0 / 3.0 * pow(ln(x), 2) * pow(x, 2) * CF
            - 83.0 / 24.0 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
            + 49.0 / 24.0 * pow(ln(x), 2) * NC * CF
            + 55.0 / 24.0 * pow(ln(x), 2) * NC * x * CF
            + 5.0 / 6.0 * pow(ln(x), 2) * NF * CF * pow(omx, -1)
            - 5.0 / 12.0 * pow(ln(x), 2) * NF * CF
            - 5.0 / 12.0 * pow(ln(x), 2) * NF * x * CF
            + pow(ln(x), 2) * LMUF * pow(NC, -1) * CF * pow(omx, -1)
            - pow(ln(x), 2) * LMUF * pow(NC, -1) * CF
            - pow(ln(x), 2) * LMUF * pow(NC, -1) * x * CF
            + pow(ln(x), 2) * LMUF * CF
            + pow(ln(x), 2) * LMUF * x * CF
            - 2 * pow(ln(x), 2) * LMUF * NC * CF * pow(omx, -1)
            + 3.0 / 2.0 * pow(ln(x), 2) * LMUF * NC * CF
            + 3.0 / 2.0 * pow(ln(x), 2) * LMUF * NC * x * CF
        )
        res += (
            -5.0 / 24.0 * pow(ln(x), 3) * pow(NC, -1) * CF
            - 5.0 / 24.0 * pow(ln(x), 3) * pow(NC, -1) * x * CF
            + 5.0 / 12.0 * pow(ln(x), 3) * CF
            + 5.0 / 12.0 * pow(ln(x), 3) * x * CF
            - 1.0 / 2.0 * pow(ln(x), 3) * NC * CF * pow(omx, -1)
            + 11.0 / 24.0 * pow(ln(x), 3) * NC * CF
            + 11.0 / 24.0 * pow(ln(x), 3) * NC * x * CF
            - 9.0 / 2.0 * pow(ln(x), 2) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
            + 9.0 / 4.0 * pow(ln(x), 2) * ln(omx) * pow(NC, -1) * CF
            + 9.0 / 4.0 * pow(ln(x), 2) * ln(omx) * pow(NC, -1) * x * CF
            + 5.0 / 2.0 * pow(ln(x), 2) * ln(omx) * NC * CF * pow(omx, -1)
            - 5.0 / 4.0 * pow(ln(x), 2) * ln(omx) * NC * CF
            - 5.0 / 4.0 * pow(ln(x), 2) * ln(omx) * NC * x * CF
            + 1.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * CF
            - 1.0 / 2.0 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
            - 2.0 / 3.0 * ln(x) * ln(omx) * pow(x, -1) * CF
            - 1.0 / 2.0 * ln(x) * ln(omx) * CF
            + 1.0 / 2.0 * ln(x) * ln(omx) * x * CF
            + 2.0 / 3.0 * ln(x) * ln(omx) * pow(x, 2) * CF
            + 11.0 / 3.0 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
            - 7.0 / 3.0 * ln(x) * ln(omx) * NC * CF
            - 4.0 / 3.0 * ln(x) * ln(omx) * NC * x * CF
            - 2.0 / 3.0 * ln(x) * ln(omx) * NF * CF * pow(omx, -1)
            + 1.0 / 3.0 * ln(x) * ln(omx) * NF * CF
            + 1.0 / 3.0 * ln(x) * ln(omx) * NF * x * CF
            - 6 * ln(x) * ln(omx) * LMUF * pow(NC, -1) * CF * pow(omx, -1)
            + 3 * ln(x) * ln(omx) * LMUF * pow(NC, -1) * CF
            + 3 * ln(x) * ln(omx) * LMUF * pow(NC, -1) * x * CF
            + 6 * ln(x) * ln(omx) * LMUF * NC * CF * pow(omx, -1)
            - 3 * ln(x) * ln(omx) * LMUF * NC * CF
            - 3 * ln(x) * ln(omx) * LMUF * NC * x * CF
            + 5.0 / 2.0 * ln(x) * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
            - ln(x) * pow(ln(omx), 2) * pow(NC, -1) * CF
            - ln(x) * pow(ln(omx), 2) * pow(NC, -1) * x * CF
            - 1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF
            - 1.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF
            - 9.0 / 2.0 * ln(x) * pow(ln(omx), 2) * NC * CF * pow(omx, -1)
            + 2 * ln(x) * pow(ln(omx), 2) * NC * CF
        )
        res += (
            +2 * ln(x) * pow(ln(omx), 2) * NC * x * CF
            - 5 * ln(x) * Li2(x) * pow(NC, -1) * CF * pow(omx, -1)
            + 2 * ln(x) * Li2(x) * pow(NC, -1) * CF
            + 2 * ln(x) * Li2(x) * pow(NC, -1) * x * CF
            + ln(x) * Li2(x) * CF
            + ln(x) * Li2(x) * x * CF
            + ln(x) * Li2(x) * NC * CF * pow(omx, -1)
            - ln(omx) * pow(NC, -1) * CF
            + 1.0 / 6.0 * ln(omx) * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
            - 1.0 / 2.0 * ln(omx) * pow(NC, -1) * pow(pi, 2) * CF
            - 27.0 / 4.0 * ln(omx) * pow(NC, -1) * x * CF
            - 1.0 / 2.0 * ln(omx) * pow(NC, -1) * x * pow(pi, 2) * CF
            + 13.0 / 9.0 * ln(omx) * pow(x, -1) * CF
            - 11.0 / 6.0 * ln(omx) * CF
            + 1.0 / 6.0 * ln(omx) * pow(pi, 2) * CF
            + 17.0 / 6.0 * ln(omx) * x * CF
            + 1.0 / 6.0 * ln(omx) * x * pow(pi, 2) * CF
            - 22.0 / 9.0 * ln(omx) * pow(x, 2) * CF
            + 19.0 / 9.0 * ln(omx) * NC * CF
            + 1.0 / 6.0 * ln(omx) * NC * pow(pi, 2) * CF * pow(omx, -1)
            + 1.0 / 2.0 * ln(omx) * NC * pow(pi, 2) * CF
            - 47.0 / 36.0 * ln(omx) * NC * x * CF
            + 1.0 / 2.0 * ln(omx) * NC * x * pow(pi, 2) * CF
            + 2.0 / 9.0 * ln(omx) * NF * CF
            + 8.0 / 9.0 * ln(omx) * NF * x * CF
            - 11.0 / 6.0 * ln(omx) * LMUR * NC * CF
            - 11.0 / 6.0 * ln(omx) * LMUR * NC * x * CF
            + 1.0 / 3.0 * ln(omx) * LMUR * NF * CF
            + 1.0 / 3.0 * ln(omx) * LMUR * NF * x * CF
            - 3.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(omx) * LMUF * pow(NC, -1) * x * CF
            - 2.0 / 3.0 * ln(omx) * LMUF * pow(x, -1) * CF
            - 1.0 / 2.0 * ln(omx) * LMUF * CF
            + 1.0 / 2.0 * ln(omx) * LMUF * x * CF
            + 2.0 / 3.0 * ln(omx) * LMUF * pow(x, 2) * CF
            + 3.0 / 4.0 * ln(omx) * LMUF * NC * CF
            + 3.0 / 4.0 * ln(omx) * LMUF * NC * x * CF
            + ln(omx) * pow(LMUF, 2) * pow(NC, -1) * CF
            + ln(omx) * pow(LMUF, 2) * pow(NC, -1) * x * CF
            - ln(omx) * pow(LMUF, 2) * NC * CF
            - ln(omx) * pow(LMUF, 2) * NC * x * CF
            - 3.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1) * CF
            - 3.0 / 4.0 * ln(omx) * LMUA * pow(NC, -1) * x * CF
            + 3.0 / 4.0 * ln(omx) * LMUA * NC * CF
            + 3.0 / 4.0 * ln(omx) * LMUA * NC * x * CF
        )
        res += (
            +1.0 / 3.0 * pow(ln(omx), 2) * pow(x, -1) * CF
            + 1.0 / 4.0 * pow(ln(omx), 2) * CF
            - 1.0 / 4.0 * pow(ln(omx), 2) * x * CF
            - 1.0 / 3.0 * pow(ln(omx), 2) * pow(x, 2) * CF
            + 11.0 / 12.0 * pow(ln(omx), 2) * NC * CF
            + 11.0 / 12.0 * pow(ln(omx), 2) * NC * x * CF
            - 1.0 / 6.0 * pow(ln(omx), 2) * NF * CF
            - 1.0 / 6.0 * pow(ln(omx), 2) * NF * x * CF
            - 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * pow(NC, -1) * CF
            - 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * pow(NC, -1) * x * CF
            + 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * NC * CF
            + 3.0 / 2.0 * pow(ln(omx), 2) * LMUF * NC * x * CF
            + 1.0 / 2.0 * pow(ln(omx), 3) * pow(NC, -1) * CF
            + 1.0 / 2.0 * pow(ln(omx), 3) * pow(NC, -1) * x * CF
            - 1.0 / 2.0 * pow(ln(omx), 3) * NC * CF
            - 1.0 / 2.0 * pow(ln(omx), 3) * NC * x * CF
            - ln(omx) * Li2(x) * pow(NC, -1) * CF * pow(omx, -1)
            + ln(omx) * Li2(x) * pow(NC, -1) * CF
            + ln(omx) * Li2(x) * pow(NC, -1) * x * CF
            - ln(omx) * Li2(x) * CF
            - ln(omx) * Li2(x) * x * CF
            - ln(omx) * Li2(x) * NC * CF * pow(omx, -1)
            - 3 * Li3(1 - x) * pow(NC, -1) * CF * pow(omx, -1)
            + 2 * Li3(1 - x) * pow(NC, -1) * CF
            + 2 * Li3(1 - x) * pow(NC, -1) * x * CF
            - Li3(1 - x) * CF
            - Li3(1 - x) * x * CF
            - 5 * Li3(1 - x) * NC * CF * pow(omx, -1)
            + 2 * Li3(1 - x) * NC * CF
            + 2 * Li3(1 - x) * NC * x * CF
            + 7 * Li3(x) * pow(NC, -1) * CF * pow(omx, -1)
            - 7.0 / 2.0 * Li3(x) * pow(NC, -1) * CF
            - 7.0 / 2.0 * Li3(x) * pow(NC, -1) * x * CF
            - 5 * Li3(x) * NC * CF * pow(omx, -1)
            + 5.0 / 2.0 * Li3(x) * NC * CF
            + 5.0 / 2.0 * Li3(x) * NC * x * CF
            - 3.0 / 2.0 * Li2(x) * pow(NC, -1) * CF * pow(omx, -1)
            - 3.0 / 2.0 * Li2(x) * pow(NC, -1) * x * CF
            - 2.0 / 3.0 * Li2(x) * pow(x, -1) * CF
            - 3.0 / 2.0 * Li2(x) * CF
            - 5.0 / 2.0 * Li2(x) * x * CF
            - 4.0 / 3.0 * Li2(x) * pow(x, 2) * CF
            - 13.0 / 6.0 * Li2(x) * NC * CF * pow(omx, -1)
            + 5.0 / 6.0 * Li2(x) * NC * CF
            + 7.0 / 3.0 * Li2(x) * NC * x * CF
            + 2.0 / 3.0 * Li2(x) * NF * CF * pow(omx, -1)
        )
        res += -1.0 / 3.0 * Li2(x) * NF * CF - 1.0 / 3.0 * Li2(x) * NF * x * CF - 1.0 / 2.0 * Li2(x) * LMUF * pow(NC, -1) * CF - 1.0 / 2.0 * Li2(x) * LMUF * pow(NC, -1) * x * CF + Li2(x) * LMUF * CF + Li2(x) * LMUF * x * CF + 1.0 / 2.0 * Li2(x) * LMUF * NC * CF + 1.0 / 2.0 * Li2(x) * LMUF * NC * x * CF

        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            -pow(NC, -1) * CF
            - 5.0 / 12.0 * pow(NC, -1) * pow(pi, 2) * CF
            - 7 * pow(NC, -1) * x * CF
            - 5.0 / 12.0 * pow(NC, -1) * x * pow(pi, 2) * CF
            + 13.0 / 9.0 * pow(x, -1) * CF
            - 11.0 / 6.0 * CF
            + 1.0 / 6.0 * pow(pi, 2) * CF
            + 17.0 / 6.0 * x * CF
            + 1.0 / 6.0 * x * pow(pi, 2) * CF
            - 22.0 / 9.0 * pow(x, 2) * CF
            + 19.0 / 9.0 * NC * CF
            + 7.0 / 12.0 * NC * pow(pi, 2) * CF
            - 14.0 / 9.0 * NC * x * CF
            + 7.0 / 12.0 * NC * x * pow(pi, 2) * CF
            + 2.0 / 9.0 * NF * CF
            + 8.0 / 9.0 * NF * x * CF
            - 11.0 / 6.0 * LMUR * NC * CF
            - 11.0 / 6.0 * LMUR * NC * x * CF
            + 1.0 / 3.0 * LMUR * NF * CF
            + 1.0 / 3.0 * LMUR * NF * x * CF
            - 7.0 / 4.0 * LMUF * pow(NC, -1) * CF
            + 1.0 / 4.0 * LMUF * pow(NC, -1) * x * CF
            - 2.0 / 3.0 * LMUF * pow(x, -1) * CF
            - 1.0 / 2.0 * LMUF * CF
            + 1.0 / 2.0 * LMUF * x * CF
            + 2.0 / 3.0 * LMUF * pow(x, 2) * CF
            + 7.0 / 4.0 * LMUF * NC * CF
            - 1.0 / 4.0 * LMUF * NC * x * CF
            + 1.0 / 4.0 * LMUA * pow(NC, -1) * CF
            - 7.0 / 4.0 * LMUA * pow(NC, -1) * x * CF
            - 1.0 / 4.0 * LMUA * NC * CF
            + 7.0 / 4.0 * LMUA * NC * x * CF
            + LMUA * LMUF * pow(NC, -1) * CF
            + LMUA * LMUF * pow(NC, -1) * x * CF
            - LMUA * LMUF * NC * CF
            - LMUA * LMUF * NC * x * CF
            + 3.0 / 2.0 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
            + 3.0 / 2.0 * ln(x) * pow(NC, -1) * x * CF
            + ln(x) * CF
            + 3 * ln(x) * x * CF
            + 2 * ln(x) * pow(x, 2) * CF
            + 35.0 / 6.0 * ln(x) * NC * CF * pow(omx, -1)
            - 8.0 / 3.0 * ln(x) * NC * CF
            - 25.0 / 6.0 * ln(x) * NC * x * CF
            - 4.0 / 3.0 * ln(x) * NF * CF * pow(omx, -1)
            + 2.0 / 3.0 * ln(x) * NF * CF
            + 2.0 / 3.0 * ln(x) * NF * x * CF
            - 2 * ln(x) * LMUF * pow(NC, -1) * CF * pow(omx, -1)
            + 3.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * CF
            + 3.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * CF
            - ln(x) * LMUF * CF
            - ln(x) * LMUF * x * CF
            + 2 * ln(x) * LMUF * NC * CF * pow(omx, -1)
            - 3.0 / 2.0 * ln(x) * LMUF * NC * CF
            - 3.0 / 2.0 * ln(x) * LMUF * NC * x * CF
            - 2 * ln(x) * LMUA * pow(NC, -1) * CF * pow(omx, -1)
            + ln(x) * LMUA * pow(NC, -1) * CF
            + ln(x) * LMUA * pow(NC, -1) * x * CF
            + 2 * ln(x) * LMUA * NC * CF * pow(omx, -1)
        )
        res += (
            -ln(x) * LMUA * NC * CF
            - ln(x) * LMUA * NC * x * CF
            - pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
            + pow(ln(x), 2) * pow(NC, -1) * CF
            + pow(ln(x), 2) * pow(NC, -1) * x * CF
            - pow(ln(x), 2) * CF
            - pow(ln(x), 2) * x * CF
            + 2 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
            - 3.0 / 2.0 * pow(ln(x), 2) * NC * CF
            - 3.0 / 2.0 * pow(ln(x), 2) * NC * x * CF
            + 6 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
            - 3 * ln(x) * ln(omx) * pow(NC, -1) * CF
            - 3 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
            - 6 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
            + 3 * ln(x) * ln(omx) * NC * CF
            + 3 * ln(x) * ln(omx) * NC * x * CF
            + 2.0 / 3.0 * ln(omx) * pow(x, -1) * CF
            + 1.0 / 2.0 * ln(omx) * CF
            - 1.0 / 2.0 * ln(omx) * x * CF
            - 2.0 / 3.0 * ln(omx) * pow(x, 2) * CF
            + 11.0 / 6.0 * ln(omx) * NC * CF
            + 11.0 / 6.0 * ln(omx) * NC * x * CF
            - 1.0 / 3.0 * ln(omx) * NF * CF
            - 1.0 / 3.0 * ln(omx) * NF * x * CF
            - 2 * ln(omx) * LMUF * pow(NC, -1) * CF
            - 2 * ln(omx) * LMUF * pow(NC, -1) * x * CF
            + 2 * ln(omx) * LMUF * NC * CF
            + 2 * ln(omx) * LMUF * NC * x * CF
            - ln(omx) * LMUA * pow(NC, -1) * CF
            - ln(omx) * LMUA * pow(NC, -1) * x * CF
            + ln(omx) * LMUA * NC * CF
            + ln(omx) * LMUA * NC * x * CF
            + 3.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * CF
            + 3.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
            - 3.0 / 2.0 * pow(ln(omx), 2) * NC * CF
            - 3.0 / 2.0 * pow(ln(omx), 2) * NC * x * CF
            + 1.0 / 2.0 * Li2(x) * pow(NC, -1) * CF
            + 1.0 / 2.0 * Li2(x) * pow(NC, -1) * x * CF
            - Li2(x) * CF
            - Li2(x) * x * CF
            - 1.0 / 2.0 * Li2(x) * NC * CF
            - 1.0 / 2.0 * Li2(x) * NC * x * CF
        )

        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = (
            2.0 / 3.0 * pow(x, -1) * CF
            + 1.0 / 2.0 * CF
            - 1.0 / 2.0 * x * CF
            - 2.0 / 3.0 * pow(x, 2) * CF
            + 11.0 / 6.0 * NC * CF
            + 11.0 / 6.0 * NC * x * CF
            - 1.0 / 3.0 * NF * CF
            - 1.0 / 3.0 * NF * x * CF
            - LMUF * pow(NC, -1) * CF
            - LMUF * pow(NC, -1) * x * CF
            + LMUF * NC * CF
            + LMUF * NC * x * CF
            - 2 * LMUA * pow(NC, -1) * CF
            - 2 * LMUA * pow(NC, -1) * x * CF
            + 2 * LMUA * NC * CF
            + 2 * LMUA * NC * x * CF
            + 4 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
            - 5.0 / 2.0 * ln(x) * pow(NC, -1) * CF
            - 5.0 / 2.0 * ln(x) * pow(NC, -1) * x * CF
            + ln(x) * CF
            + ln(x) * x * CF
            - 4 * ln(x) * NC * CF * pow(omx, -1)
            + 5.0 / 2.0 * ln(x) * NC * CF
            + 5.0 / 2.0 * ln(x) * NC * x * CF
            + 3 * ln(omx) * pow(NC, -1) * CF
            + 3 * ln(omx) * pow(NC, -1) * x * CF
            - 3 * ln(omx) * NC * CF
            - 3 * ln(omx) * NC * x * CF
        )

        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        res = 3.0 / 2.0 * pow(NC, -1) * CF + 3.0 / 2.0 * pow(NC, -1) * x * CF - 3.0 / 2.0 * NC * CF - 3.0 / 2.0 * NC * x * CF

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
                4 * pow(NC, -1) * CF * pow(omx, -1)
                + 4 * pow(NC, -1) * CF * pow(omz, -1)
                - 6 * pow(NC, -1) * CF
                - 4.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                + 1.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
                - 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                - 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                + 5.0 / 6.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                - 4 * pow(NC, -1) * x * CF * pow(omz, -1)
                + 7.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2) * CF * pow(omz, -1)
                - pow(NC, -1) * x * pow(pi, 2) * CF
                - 4.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                - 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 12 * ln(x) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * pow(NC, -1) * x * z * CF
                + 12 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 9 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 3 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 6 * pow(ln(x), 2) * pow(NC, -1) * CF
                - 9 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 9 * pow(ln(x), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                + 12 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                - 20 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 15 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                + 5 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omz, -1)
                - 10 * ln(x) * ln(z) * pow(NC, -1) * CF
                + 15 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 15 * ln(x) * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 10 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                - 20 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                - 18 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 13 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
            )
            tmp += (
                +4 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * pow(NC, -1) * CF
                + 13 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 14 * ln(x) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 10 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                - 18 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                - 18 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 14 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                + 5 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * pow(NC, -1) * CF
                + 14 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 13 * ln(x) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 8 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                - 18 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                + 4 * ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * pow(NC, -1) * CF
                - 3 * ln(x) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 3 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF
                + 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF
                + 8 * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 8 * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 8 * ln(z) * pow(NC, -1) * x * z * CF
            )
            tmp += (
                +8 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * pow(ln(z), 2) * pow(NC, -1) * CF
                - 6 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * pow(ln(z), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                + 8 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * pow(NC, -1) * CF
                - 8 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 10 * ln(z) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 8 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                + 12 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 10 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 4 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * pow(NC, -1) * CF
                - 10 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 8 * ln(z) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                + 12 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                - 4 * ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * pow(NC, -1) * CF
                + 3 * ln(z) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 3 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF
                - 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF
                + 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omx) * pow(NC, -1) * x * z * CF
                + 5 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + pow(ln(omx), 2) * pow(NC, -1) * CF
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                + 5 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                + 10 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 3 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                - 8 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 7 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                + 10 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                + 6 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omz) * pow(NC, -1) * x * z * CF
                + 4 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * CF
                - 7.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + pow(ln(omz), 2) * pow(NC, -1) * x * CF
                + 4 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                +2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF
                + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF
                - 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * z * CF
                - 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * Li2(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(z) * pow(NC, -1) * x * CF
                - 2 * Li2(z) * pow(NC, -1) * x * z * CF
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            tmp = (
                4 * pow(NC, -1) * CF * pow(omx, -1)
                + 4 * pow(NC, -1) * CF * pow(omz, -1)
                - 6 * pow(NC, -1) * CF
                - 4.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                + 1.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
                - 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                - 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                + 5.0 / 6.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                - 4 * pow(NC, -1) * x * CF * pow(omz, -1)
                + 7.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2) * CF * pow(omz, -1)
                - pow(NC, -1) * x * pow(pi, 2) * CF
                - 4.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                - 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 12 * ln(x) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * pow(NC, -1) * x * z * CF
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                + 13 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 10 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 7 * pow(ln(x), 2) * pow(NC, -1) * CF
                - 10 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                + 13 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                - 22 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 17 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
            )
            tmp += (
                +6 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omz, -1)
                - 12 * ln(x) * ln(z) * pow(NC, -1) * CF
                + 17 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 16 * ln(x) * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 10 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                - 22 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                - 16 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 11 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                + 3 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * pow(NC, -1) * CF
                + 11 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 13 * ln(x) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 10 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                - 16 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                - 20 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 16 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                + 6 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * pow(NC, -1) * CF
                + 16 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 14 * ln(x) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 8 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                - 20 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                + 4 * ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * pow(NC, -1) * CF
                - 3 * ln(x) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 3 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF
                + 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF
                + 8 * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 8 * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
            )
            tmp += (
                +8 * ln(z) * pow(NC, -1) * x * z * CF
                + 8 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * pow(ln(z), 2) * pow(NC, -1) * CF
                - 6 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * pow(ln(z), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                + 8 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * ln(z) * ln(omx) * pow(NC, -1) * CF
                - 8 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 10 * ln(z) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 8 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                + 14 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 12 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 5 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * pow(NC, -1) * CF
                - 12 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 9 * ln(z) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                + 14 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                - 4 * ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * pow(NC, -1) * CF
                + 3 * ln(z) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 3 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF
                - 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF
            )
            tmp += (
                +6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omx) * pow(NC, -1) * x * z * CF
                + 5 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + pow(ln(omx), 2) * pow(NC, -1) * CF
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                + 5 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                + 8 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                + 8 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                + 6 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omz) * pow(NC, -1) * x * z * CF
                - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * pow(NC, -1) * CF
                - 9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 3 * pow(ln(omz), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + pow(ln(omz), 2) * pow(NC, -1) * x * CF
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF
                + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * z * CF
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF
                + Li2(omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                - 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * Li2(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(z) * pow(NC, -1) * x * CF
                - 2 * Li2(z) * pow(NC, -1) * x * z * CF
            )

            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                4 * pow(NC, -1) * CF * pow(omx, -1)
                + 4 * pow(NC, -1) * CF * pow(omz, -1)
                - 6 * pow(NC, -1) * CF
                - 8.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                + 13.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                + 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
                - 5.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                - 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                + 13.0 / 6.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                - 4 * pow(NC, -1) * x * CF * pow(omz, -1)
                + 11.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2) * CF * pow(omz, -1)
                - pow(NC, -1) * x * pow(pi, 2) * CF
                - 8.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                - 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 12 * ln(x) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * pow(NC, -1) * x * z * CF
                + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * CF
                - 3 * ln(x) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 3 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF
                + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF
                + 14 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 7.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 7 * pow(ln(x), 2) * pow(NC, -1) * CF
                - 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 7 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                + 14 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                - 24 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                +18 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                + 6 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omz, -1)
                - 12 * ln(x) * ln(z) * pow(NC, -1) * CF
                + 18 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 18 * ln(x) * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                - 24 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                - 18 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 12 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                + 3 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * pow(NC, -1) * CF
                + 12 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 15 * ln(x) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                - 18 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                - 18 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 15 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                + 6 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 12 * ln(x) * ln(omz) * pow(NC, -1) * CF
                + 15 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 12 * ln(x) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                - 18 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF
                - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(x) * ln(omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF
                + 8 * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 8 * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
            )
            tmp += (
                +8 * ln(z) * pow(NC, -1) * x * z * CF
                - 4 * ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * CF
                + 3 * ln(z) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 3 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF
                - 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF
                + 10 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 15.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 5 * pow(ln(z), 2) * pow(NC, -1) * CF
                - 15.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 15.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 5 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                + 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 7 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * pow(NC, -1) * CF
                - 7 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 11 * ln(z) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 10 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                + 12 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                + 12 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 11 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 5 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 10 * ln(z) * ln(omz) * pow(NC, -1) * CF
                - 11 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 7 * ln(z) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
            )
            tmp += (
                +12 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                + 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omx) * pow(NC, -1) * x * z * CF
                + 7 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 5 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 3.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * CF
                - 5 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 11.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                + 7 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                - 4 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 5 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                + 6 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omz) * pow(NC, -1) * x * z * CF
                + 6 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * CF
                - 11.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 7.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + pow(ln(omz), 2) * pow(NC, -1) * x * CF
            )
            tmp += (
                +6 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF
                + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF
                - 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * z * CF
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                -2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF
                - 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                - 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * Li2(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(z) * pow(NC, -1) * x * CF
                - 2 * Li2(z) * pow(NC, -1) * x * z * CF
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            tmp = (
                4 * pow(NC, -1) * CF * pow(omx, -1)
                + 4 * pow(NC, -1) * CF * pow(omz, -1)
                - 6 * pow(NC, -1) * CF
                - 4.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                + 1.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
                - 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                - 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                + 5.0 / 6.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                - 4 * pow(NC, -1) * x * CF * pow(omz, -1)
                + 7.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2) * CF * pow(omz, -1)
                - pow(NC, -1) * x * pow(pi, 2) * CF
                - 4.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                - 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 12 * ln(x) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * pow(NC, -1) * x * z * CF
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF
                - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                - ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * CF
                - 3 * ln(x) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 3 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF
                + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF
                + 13 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
            )
            tmp += (
                -3 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 6 * pow(ln(x), 2) * pow(NC, -1) * CF
                - 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 10 * pow(ln(x), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 7 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                + 13 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                - 22 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 16 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                + 5 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omz, -1)
                - 10 * ln(x) * ln(z) * pow(NC, -1) * CF
                + 16 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 17 * ln(x) * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                - 22 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                - 20 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 14 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 8 * ln(x) * ln(omx) * pow(NC, -1) * CF
                + 14 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 16 * ln(x) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 12 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                - 20 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                - 16 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 13 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                + 5 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 10 * ln(x) * ln(omz) * pow(NC, -1) * CF
                + 13 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 11 * ln(x) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                - 16 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                + 8 * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 8 * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
            )
            tmp += (
                +8 * ln(z) * pow(NC, -1) * x * z * CF
                - 4 * ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * CF
                + 3 * ln(z) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 3 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF
                - 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF
                + 8 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 11.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 3 * pow(ln(z), 2) * pow(NC, -1) * CF
                - 11.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 13.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 5 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                + 8 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                + 16 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 11 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                - 3 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                + 6 * ln(z) * ln(omx) * pow(NC, -1) * CF
                - 11 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 13 * ln(z) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 10 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                + 16 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                + 10 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 9 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 4 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 8 * ln(z) * ln(omz) * pow(NC, -1) * CF
                - 9 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(z) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
            )
            tmp += (
                +10 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                + 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omx) * pow(NC, -1) * x * z * CF
                + 5 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + pow(ln(omx), 2) * pow(NC, -1) * CF
                - 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                + 5 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                + 8 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                + 8 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                + 6 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 6 * ln(omz) * pow(NC, -1) * x * z * CF
                - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF
                + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF * pow(omz, -1)
            )
            tmp += (
                -2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * pow(ln(omz), 2) * pow(NC, -1) * CF
                - 9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 3 * pow(ln(omz), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                + pow(ln(omz), 2) * pow(NC, -1) * x * CF
                + 5 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF
                + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF
                + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * z * CF
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF
                - Li2(pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF * pow(omz, -1)
            )
            tmp += (
                -2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                - Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                - 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * Li2(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(z) * pow(NC, -1) * x * CF
                - 2 * Li2(z) * pow(NC, -1) * x * z * CF
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
                -NC * CF * pow(omx, -1)
                - NC * CF * pow(omz, -1)
                + 3 * NC * CF
                + 4.0 / 3.0 * NC * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                - 2.0 / 3.0 * NC * pow(pi, 2) * CF * pow(omx, -1)
                - 2.0 / 3.0 * NC * pow(pi, 2) * CF * pow(omz, -1)
                + 4.0 / 3.0 * NC * pow(pi, 2) * CF
                + NC * z * CF * pow(omx, -1)
                - 2.0 / 3.0 * NC * z * pow(pi, 2) * CF * pow(omx, -1)
                + NC * x * CF * pow(omz, -1)
                - 2.0 / 3.0 * NC * x * pow(pi, 2) * CF * pow(omz, -1)
                + 4.0 / 3.0 * NC * x * z * pow(pi, 2) * CF
                + 6 * ln(x) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 9 * ln(x) * NC * CF
                - 6 * ln(x) * NC * z * CF * pow(omx, -1)
                - 6 * ln(x) * NC * x * CF * pow(omz, -1)
                - 6 * ln(x) * NC * x * CF
                + 6 * ln(x) * NC * x * z * CF
                - 7 * pow(ln(x), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * CF * pow(omz, -1)
                - 7 * pow(ln(x), 2) * NC * CF
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * z * CF * pow(omx, -1)
                + 7.0 / 2.0 * pow(ln(x), 2) * NC * x * CF * pow(omz, -1)
                - 7 * pow(ln(x), 2) * NC * x * z * CF
                + 6 * ln(x) * ln(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(x) * ln(z) * NC * CF * pow(omx, -1)
                - 3 * ln(x) * ln(z) * NC * CF * pow(omz, -1)
                + 6 * ln(x) * ln(z) * NC * CF
                - 3 * ln(x) * ln(z) * NC * z * CF * pow(omx, -1)
                - 3 * ln(x) * ln(z) * NC * x * CF * pow(omz, -1)
                + 6 * ln(x) * ln(z) * NC * x * z * CF
                + 12 * ln(x) * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
                - 6 * ln(x) * ln(omx) * NC * CF * pow(omz, -1)
                + 12 * ln(x) * ln(omx) * NC * CF
                - 6 * ln(x) * ln(omx) * NC * z * CF * pow(omx, -1)
                - 6 * ln(x) * ln(omx) * NC * x * CF * pow(omz, -1)
                + 12 * ln(x) * ln(omx) * NC * x * z * CF
                + 12 * ln(x) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(x) * ln(omz) * NC * CF * pow(omx, -1)
                - 6 * ln(x) * ln(omz) * NC * CF * pow(omz, -1)
                + 12 * ln(x) * ln(omz) * NC * CF
            )
            tmp += (
                -6 * ln(x) * ln(omz) * NC * z * CF * pow(omx, -1)
                - 6 * ln(x) * ln(omz) * NC * x * CF * pow(omz, -1)
                + 12 * ln(x) * ln(omz) * NC * x * z * CF
                - 2 * ln(x) * ln(omxmz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + ln(x) * ln(omxmz) * NC * CF * pow(omx, -1)
                + ln(x) * ln(omxmz) * NC * CF * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * NC * CF
                + ln(x) * ln(omxmz) * NC * z * CF * pow(omx, -1)
                + ln(x) * ln(omxmz) * NC * x * CF * pow(omz, -1)
                - 2 * ln(x) * ln(omxmz) * NC * x * z * CF
                - 2 * ln(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(z) * NC * CF
                + 2 * ln(z) * NC * z * CF * pow(omx, -1)
                + 2 * ln(z) * NC * x * CF * pow(omz, -1)
                + 2 * ln(z) * NC * x * CF
                - 2 * ln(z) * NC * x * z * CF
                - pow(ln(z), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * CF * pow(omz, -1)
                - pow(ln(z), 2) * NC * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * x * CF * pow(omz, -1)
                - pow(ln(z), 2) * NC * x * z * CF
                - 4 * ln(z) * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * NC * CF * pow(omx, -1)
                + 2 * ln(z) * ln(omx) * NC * CF * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * NC * CF
                + 2 * ln(z) * ln(omx) * NC * z * CF * pow(omx, -1)
                + 2 * ln(z) * ln(omx) * NC * x * CF * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * NC * x * z * CF
                - 4 * ln(z) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omz) * NC * CF * pow(omx, -1)
                + 2 * ln(z) * ln(omz) * NC * CF * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * NC * CF
                + 2 * ln(z) * ln(omz) * NC * z * CF * pow(omx, -1)
                + 2 * ln(z) * ln(omz) * NC * x * CF * pow(omz, -1)
                - 4 * ln(z) * ln(omz) * NC * x * z * CF
                - 4 * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * NC * CF
                + 4 * ln(omx) * NC * z * CF * pow(omx, -1)
                + 4 * ln(omx) * NC * x * CF * pow(omz, -1)
            )
            tmp += (
                +4 * ln(omx) * NC * x * CF
                - 4 * ln(omx) * NC * x * z * CF
                - 4 * pow(ln(omx), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * NC * CF * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * NC * CF * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * NC * CF
                + 2 * pow(ln(omx), 2) * NC * z * CF * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * NC * x * CF * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * NC * x * z * CF
                - 10 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 5 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1)
                + 5 * ln(omx) * ln(omz) * NC * CF * pow(omz, -1)
                - 10 * ln(omx) * ln(omz) * NC * CF
                + 5 * ln(omx) * ln(omz) * NC * z * CF * pow(omx, -1)
                + 5 * ln(omx) * ln(omz) * NC * x * CF * pow(omz, -1)
                - 10 * ln(omx) * ln(omz) * NC * x * z * CF
                - 4 * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omz) * NC * CF
                + 4 * ln(omz) * NC * z * CF * pow(omx, -1)
                + 4 * ln(omz) * NC * x * CF * pow(omz, -1)
                + 4 * ln(omz) * NC * x * CF
                - 4 * ln(omz) * NC * x * z * CF
                - 5 * pow(ln(omz), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC * CF * pow(omx, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC * CF * pow(omz, -1)
                - 5 * pow(ln(omz), 2) * NC * CF
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC * z * CF * pow(omx, -1)
                + 5.0 / 2.0 * pow(ln(omz), 2) * NC * x * CF * pow(omz, -1)
                - 5 * pow(ln(omz), 2) * NC * x * z * CF
                + 2 * ln(omz) * ln(omxmz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - ln(omz) * ln(omxmz) * NC * CF * pow(omx, -1)
                - ln(omz) * ln(omxmz) * NC * CF * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * NC * CF
                - ln(omz) * ln(omxmz) * NC * z * CF * pow(omx, -1)
                - ln(omz) * ln(omxmz) * NC * x * CF * pow(omz, -1)
                + 2 * ln(omz) * ln(omxmz) * NC * x * z * CF
                + 2 * Li2(z * pow(omx, -1)) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - Li2(z * pow(omx, -1)) * NC * CF * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * NC * CF * pow(omz, -1)
            )
            tmp += (
                +2 * Li2(z * pow(omx, -1)) * NC * CF
                - Li2(z * pow(omx, -1)) * NC * z * CF * pow(omx, -1)
                - Li2(z * pow(omx, -1)) * NC * x * CF * pow(omz, -1)
                + 2 * Li2(z * pow(omx, -1)) * NC * x * z * CF
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * NC * CF * pow(omx, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * NC * CF * pow(omz, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * NC * CF
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * NC * z * CF * pow(omx, -1)
                + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * NC * x * CF * pow(omz, -1)
                - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * NC * x * z * CF
                - 2 * Li2(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * NC * CF * pow(omx, -1)
                + Li2(z) * NC * CF * pow(omz, -1)
                - 2 * Li2(z) * NC * CF
                + Li2(z) * NC * z * CF * pow(omx, -1)
                + Li2(z) * NC * x * CF * pow(omz, -1)
                - 2 * Li2(z) * NC * x * z * CF
            )

            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals):

            tmp = 0.0
            tmp = (
                -NC * CF * pow(omx, -1)
                - NC * CF * pow(omz, -1)
                + 3 * NC * CF
                + 4.0 / 3.0 * NC * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                - 2.0 / 3.0 * NC * pow(pi, 2) * CF * pow(omx, -1)
                - 2.0 / 3.0 * NC * pow(pi, 2) * CF * pow(omz, -1)
                + 4.0 / 3.0 * NC * pow(pi, 2) * CF
                + NC * z * CF * pow(omx, -1)
                - 2.0 / 3.0 * NC * z * pow(pi, 2) * CF * pow(omx, -1)
                + NC * x * CF * pow(omz, -1)
                - 2.0 / 3.0 * NC * x * pow(pi, 2) * CF * pow(omz, -1)
                + 4.0 / 3.0 * NC * x * z * pow(pi, 2) * CF
                + 6 * ln(x) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 9 * ln(x) * NC * CF
                - 6 * ln(x) * NC * z * CF * pow(omx, -1)
                - 6 * ln(x) * NC * x * CF * pow(omz, -1)
                - 6 * ln(x) * NC * x * CF
                + 6 * ln(x) * NC * x * z * CF
                - 2 * ln(x) * ln(-omxmz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + ln(x) * ln(-omxmz) * NC * CF * pow(omx, -1)
                + ln(x) * ln(-omxmz) * NC * CF * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * NC * CF
                + ln(x) * ln(-omxmz) * NC * z * CF * pow(omx, -1)
                + ln(x) * ln(-omxmz) * NC * x * CF * pow(omz, -1)
                - 2 * ln(x) * ln(-omxmz) * NC * x * z * CF
                - 6 * pow(ln(x), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
                + 3 * pow(ln(x), 2) * NC * CF * pow(omz, -1)
                - 6 * pow(ln(x), 2) * NC * CF
                + 3 * pow(ln(x), 2) * NC * z * CF * pow(omx, -1)
                + 3 * pow(ln(x), 2) * NC * x * CF * pow(omz, -1)
                - 6 * pow(ln(x), 2) * NC * x * z * CF
                + 8 * ln(x) * ln(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(x) * ln(z) * NC * CF * pow(omx, -1)
                - 4 * ln(x) * ln(z) * NC * CF * pow(omz, -1)
                + 8 * ln(x) * ln(z) * NC * CF
                - 4 * ln(x) * ln(z) * NC * z * CF * pow(omx, -1)
                - 4 * ln(x) * ln(z) * NC * x * CF * pow(omz, -1)
                + 8 * ln(x) * ln(z) * NC * x * z * CF
                + 10 * ln(x) * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 5 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
                - 5 * ln(x) * ln(omx) * NC * CF * pow(omz, -1)
                + 10 * ln(x) * ln(omx) * NC * CF
            )
            tmp += (
                -5 * ln(x) * ln(omx) * NC * z * CF * pow(omx, -1)
                - 5 * ln(x) * ln(omx) * NC * x * CF * pow(omz, -1)
                + 10 * ln(x) * ln(omx) * NC * x * z * CF
                + 10 * ln(x) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 5 * ln(x) * ln(omz) * NC * CF * pow(omx, -1)
                - 5 * ln(x) * ln(omz) * NC * CF * pow(omz, -1)
                + 10 * ln(x) * ln(omz) * NC * CF
                - 5 * ln(x) * ln(omz) * NC * z * CF * pow(omx, -1)
                - 5 * ln(x) * ln(omz) * NC * x * CF * pow(omz, -1)
                + 10 * ln(x) * ln(omz) * NC * x * z * CF
                - 2 * ln(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * ln(z) * NC * CF
                + 2 * ln(z) * NC * z * CF * pow(omx, -1)
                + 2 * ln(z) * NC * x * CF * pow(omz, -1)
                + 2 * ln(z) * NC * x * CF
                - 2 * ln(z) * NC * x * z * CF
                - pow(ln(z), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * CF * pow(omz, -1)
                - pow(ln(z), 2) * NC * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * NC * x * CF * pow(omz, -1)
                - pow(ln(z), 2) * NC * x * z * CF
                - 4 * ln(z) * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * ln(z) * ln(omx) * NC * CF * pow(omx, -1)
                + 2 * ln(z) * ln(omx) * NC * CF * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * NC * CF
                + 2 * ln(z) * ln(omx) * NC * z * CF * pow(omx, -1)
                + 2 * ln(z) * ln(omx) * NC * x * CF * pow(omz, -1)
                - 4 * ln(z) * ln(omx) * NC * x * z * CF
                - 6 * ln(z) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * ln(z) * ln(omz) * NC * CF * pow(omx, -1)
                + 3 * ln(z) * ln(omz) * NC * CF * pow(omz, -1)
                - 6 * ln(z) * ln(omz) * NC * CF
                + 3 * ln(z) * ln(omz) * NC * z * CF * pow(omx, -1)
                + 3 * ln(z) * ln(omz) * NC * x * CF * pow(omz, -1)
                - 6 * ln(z) * ln(omz) * NC * x * z * CF
                - 4 * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omx) * NC * CF
                + 4 * ln(omx) * NC * z * CF * pow(omx, -1)
                + 4 * ln(omx) * NC * x * CF * pow(omz, -1)
            )
            tmp += (
                +4 * ln(omx) * NC * x * CF
                - 4 * ln(omx) * NC * x * z * CF
                - 4 * pow(ln(omx), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(omx), 2) * NC * CF * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * NC * CF * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * NC * CF
                + 2 * pow(ln(omx), 2) * NC * z * CF * pow(omx, -1)
                + 2 * pow(ln(omx), 2) * NC * x * CF * pow(omz, -1)
                - 4 * pow(ln(omx), 2) * NC * x * z * CF
                - 8 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 4 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1)
                + 4 * ln(omx) * ln(omz) * NC * CF * pow(omz, -1)
                - 8 * ln(omx) * ln(omz) * NC * CF
                + 4 * ln(omx) * ln(omz) * NC * z * CF * pow(omx, -1)
                + 4 * ln(omx) * ln(omz) * NC * x * CF * pow(omz, -1)
                - 8 * ln(omx) * ln(omz) * NC * x * z * CF
                - 4 * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * ln(omz) * NC * CF
                + 4 * ln(omz) * NC * z * CF * pow(omx, -1)
                + 4 * ln(omz) * NC * x * CF * pow(omz, -1)
                + 4 * ln(omz) * NC * x * CF
                - 4 * ln(omz) * NC * x * z * CF
                + 2 * ln(omz) * ln(-omxmz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - ln(omz) * ln(-omxmz) * NC * CF * pow(omx, -1)
                - ln(omz) * ln(-omxmz) * NC * CF * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * NC * CF
                - ln(omz) * ln(-omxmz) * NC * z * CF * pow(omx, -1)
                - ln(omz) * ln(-omxmz) * NC * x * CF * pow(omz, -1)
                + 2 * ln(omz) * ln(-omxmz) * NC * x * z * CF
                - 4 * pow(ln(omz), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(omz), 2) * NC * CF * pow(omx, -1)
                + 2 * pow(ln(omz), 2) * NC * CF * pow(omz, -1)
                - 4 * pow(ln(omz), 2) * NC * CF
                + 2 * pow(ln(omz), 2) * NC * z * CF * pow(omx, -1)
                + 2 * pow(ln(omz), 2) * NC * x * CF * pow(omz, -1)
                - 4 * pow(ln(omz), 2) * NC * x * z * CF
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * NC * CF * pow(omx, -1)
            )
            tmp += (
                -Li2(pow(x, -1) * pow(z, -1) * omx * omz) * NC * CF * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * NC * CF
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * NC * z * CF * pow(omx, -1)
                - Li2(pow(x, -1) * pow(z, -1) * omx * omz) * NC * x * CF * pow(omz, -1)
                + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * NC * x * z * CF
                - 2 * Li2(pow(z, -1) * omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(pow(z, -1) * omx) * NC * CF * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * NC * CF * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * NC * CF
                + Li2(pow(z, -1) * omx) * NC * z * CF * pow(omx, -1)
                + Li2(pow(z, -1) * omx) * NC * x * CF * pow(omz, -1)
                - 2 * Li2(pow(z, -1) * omx) * NC * x * z * CF
                - 2 * Li2(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + Li2(z) * NC * CF * pow(omx, -1)
                + Li2(z) * NC * CF * pow(omz, -1)
                - 2 * Li2(z) * NC * CF
                + Li2(z) * NC * z * CF * pow(omx, -1)
                + Li2(z) * NC * x * CF * pow(omz, -1)
                - 2 * Li2(z) * NC * x * z * CF
            )

            res += tmp

        if round(z, ndecimals) != round(x, ndecimals) and round(z, ndecimals) != round(1.0 - x, ndecimals):

            tmp = 0.0
            tmp = (
                1.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(pi, 2) * CF * pow(opx, -1)
                - 1.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(z, -1) * pow(pi, 2) * CF
                - 2.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(pi, 2) * CF * pow(opx, -1)
                + 2.0 / 3.0 * pow(NC, -1) * pow(x, -2) * pow(pi, 2) * CF
                + 2.0 / 3.0 * pow(NC, -1) * pow(x, -2) * z * pow(pi, 2) * CF * pow(opx, -1)
                - 2.0 / 3.0 * pow(NC, -1) * pow(x, -2) * z * pow(pi, 2) * CF
                + 1.0 / 3.0 * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * CF
                - 1.0 / 2.0 * pow(NC, -1) * pow(x, -1) * pow(poly2, -1) * CF
                + 1.0 / 2.0 * pow(NC, -1) * pow(x, -1) * CF
                - 2.0 / 3.0 * pow(NC, -1) * pow(x, -1) * pow(pi, 2) * CF
                + 2.0 / 3.0 * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2) * CF * pow(opx, -1)
                - 12 * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 12 * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + 4 * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                - 4 * pow(NC, -1) * pow(z, -1) * CF
                - 4 * pow(NC, -1) * pow(z, -1) * pow(rln2, 2) * CF * pow(omx, -1)
                + 2 * pow(NC, -1) * pow(z, -1) * pow(rln2, 2) * CF
                - 6 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * CF * pow(omx, -1)
                + 4 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * CF
                + 4.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                - 4.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                - 2.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omz, -1)
                - 2.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(opx, -1)
                + 2.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                + 1.0 / 2.0 * pow(NC, -1) * pow(poly2, -1) * CF
                + 12 * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 4 * pow(NC, -1) * CF * pow(omx, -1)
                - 8 * pow(NC, -1) * CF * pow(omz, -1)
                - 1.0 / 2.0 * pow(NC, -1) * CF * pow(omxmz, -1)
                + 23 * pow(NC, -1) * CF
                - 8 * pow(NC, -1) * pow(rln2, 2) * CF * pow(omx, -1)
            )
            tmp += (
                +4 * pow(NC, -1) * pow(rln2, 2) * CF
                - 6 * pow(NC, -1) * sqrtxz1 * rln2 * CF * pow(omx, -1)
                + 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                - 4.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                + 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omz, -1)
                + 4.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(opx, -1)
                + 3.0 / 2.0 * pow(NC, -1) * pow(pi, 2) * CF
                + 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                - 16 * pow(NC, -1) * z * CF
                - 4 * pow(NC, -1) * z * pow(rln2, 2) * CF * pow(omx, -1)
                - 4.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                - 1.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(opx, -1)
                + 1.0 / 6.0 * pow(NC, -1) * z * pow(pi, 2) * CF
                + 8 * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                - 15.0 / 2.0 * pow(NC, -1) * x * pow(z, -1) * CF
                + 2 * pow(NC, -1) * x * pow(z, -1) * pow(rln2, 2) * CF
                + 2 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF
                - 2.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF * pow(omz, -1)
                + 1.0 / 3.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                - pow(NC, -1) * x * pow(poly2, -1) * CF
                - 4 * pow(NC, -1) * x * CF * pow(omz, -1)
                - 1.0 / 2.0 * pow(NC, -1) * x * CF * pow(xmz, -1)
                + 1.0 / 2.0 * pow(NC, -1) * x * CF * pow(omxmz, -1)
                - 19.0 / 2.0 * pow(NC, -1) * x * CF
                + 4 * pow(NC, -1) * x * pow(rln2, 2) * CF
                + 6 * pow(NC, -1) * x * sqrtxz1 * rln2 * CF
                - 2.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * CF * pow(omz, -1)
                + 11.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2) * CF
                + 25 * pow(NC, -1) * x * z * CF
                + 4 * pow(NC, -1) * x * z * pow(rln2, 2) * CF
                + 13.0 / 6.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                + pow(NC, -1) * pow(x, 2) * pow(poly2, -1) * CF
                + pow(NC, -1) * pow(x, 2) * CF * pow(xmz, -1)
                + 1.0 / 2.0 * pow(NC, -1) * pow(x, 2) * CF
                - 1.0 / 2.0 * pow(NC, -1) * pow(x, 3) * pow(poly2, -1) * CF
                - pow(NC, -1) * pow(x, 3) * CF * pow(xmz, -1)
                + 1.0 / 2.0 * pow(NC, -1) * pow(x, 4) * pow(poly2, -1) * CF
            )
            tmp += (
                +1.0 / 3.0 * pow(x, -2) * pow(pi, 2) * CF * pow(opx, -1)
                - 1.0 / 3.0 * pow(x, -2) * pow(pi, 2) * CF
                - 2.0 / 3.0 * pow(x, -2) * z * pow(pi, 2) * CF * pow(opx, -1)
                + 2.0 / 3.0 * pow(x, -2) * z * pow(pi, 2) * CF
                + 4.0 / 3.0 * pow(x, -2) * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1)
                - 4.0 / 3.0 * pow(x, -2) * pow(z, 2) * pow(pi, 2) * CF
                + 13.0 / 9.0 * pow(x, -1) * pow(z, -1) * CF
                - 26.0 / 9.0 * pow(x, -1) * CF
                + 1.0 / 3.0 * pow(x, -1) * pow(pi, 2) * CF
                - 2.0 / 3.0 * pow(x, -1) * z * pow(pi, 2) * CF
                + 4.0 / 3.0 * pow(x, -1) * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1)
                - 71.0 / 36.0 * pow(z, -1) * CF
                + 1.0 / 6.0 * pow(z, -1) * pow(pi, 2) * CF
                + 10.0 / 3.0 * CF
                + 6 * pow(rln2, 2) * CF * pow(omx, -1)
                + 6 * sqrtxz1 * rln2 * CF * pow(omx, -1)
                - 5.0 / 6.0 * pow(pi, 2) * CF * pow(omx, -1)
                - 2.0 / 3.0 * pow(pi, 2) * CF * pow(opx, -1)
                - 5.0 / 6.0 * pow(pi, 2) * CF
                + 37.0 / 12.0 * z * CF
                + 4 * z * pow(rln2, 2) * CF * pow(omx, -1)
                - 8 * z * pow(rln2, 2) * CF
                + 5.0 / 3.0 * z * pow(pi, 2) * CF * pow(omx, -1)
                + 4.0 / 3.0 * z * pow(pi, 2) * CF * pow(opx, -1)
                + 2.0 / 3.0 * z * pow(pi, 2) * CF
                + 43.0 / 18.0 * pow(z, 2) * CF
                + 16 * pow(z, 2) * pow(rln2, 2) * CF * pow(omx, -1)
                - 2 * pow(z, 2) * pow(pi, 2) * CF * pow(omx, -1)
                - 2.0 / 3.0 * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1)
                + 121.0 / 36.0 * x * pow(z, -1) * CF
                + 1.0 / 6.0 * x * pow(z, -1) * pow(pi, 2) * CF
                + 2 * x * CF
                - 4 * x * pow(rln2, 2) * CF
                - 4 * x * sqrtxz1 * rln2 * CF
                - 1.0 / 6.0 * x * pow(pi, 2) * CF
                - 95.0 / 12.0 * x * z * CF
                - x * z * pow(pi, 2) * CF
                - 77.0 / 18.0 * x * pow(z, 2) * CF
                - 16 * x * pow(z, 2) * pow(rln2, 2) * CF
                + 4.0 / 3.0 * x * pow(z, 2) * pow(pi, 2) * CF
                - 22.0 / 9.0 * pow(x, 2) * pow(z, -1) * CF
                + 44.0 / 9.0 * pow(x, 2) * CF
                + NC * CF * pow(omx, -1)
                + NC * CF * pow(omz, -1)
                + 1.0 / 2.0 * NC * CF * pow(omxmz, -1)
                - 37.0 / 18.0 * NC * CF
                - NC * pow(pi, 2) * CF * pow(omx, -1) * pow(omz, -1)
                + 1.0 / 2.0 * NC * pow(pi, 2) * CF * pow(omx, -1)
            )
            tmp += (
                +1.0 / 2.0 * NC * pow(pi, 2) * CF * pow(omz, -1)
                - 13.0 / 6.0 * NC * pow(pi, 2) * CF
                - NC * z * CF * pow(omx, -1)
                - 8.0 / 3.0 * NC * z * CF
                + 1.0 / 2.0 * NC * z * pow(pi, 2) * CF * pow(omx, -1)
                - 1.0 / 6.0 * NC * z * pow(pi, 2) * CF
                - NC * x * CF * pow(omz, -1)
                - 1.0 / 2.0 * NC * x * CF * pow(xmz, -1)
                - 1.0 / 2.0 * NC * x * CF * pow(omxmz, -1)
                - NC * x * CF
                + 1.0 / 2.0 * NC * x * pow(pi, 2) * CF * pow(omz, -1)
                - 1.0 / 6.0 * NC * x * pow(pi, 2) * CF
                + 47.0 / 18.0 * NC * x * z * CF
                - 13.0 / 6.0 * NC * x * z * pow(pi, 2) * CF
                + NC * pow(x, 2) * CF * pow(xmz, -1)
                + NC * pow(x, 2) * CF
                - NC * pow(x, 3) * CF * pow(xmz, -1)
                - 10.0 / 9.0 * NF * CF
                + 2.0 / 3.0 * NF * z * CF
                - 16.0 / 9.0 * NF * x * z * CF
                + 11.0 / 3.0 * LMUR * NC * CF
                + 11.0 / 3.0 * LMUR * NC * x * z * CF
                - 2.0 / 3.0 * LMUR * NF * CF
                - 2.0 / 3.0 * LMUR * NF * x * z * CF
                + 1.0 / 2.0 * LMUF * pow(NC, -1) * CF
                + 2 * LMUF * pow(NC, -1) * z * CF
                + 1.0 / 2.0 * LMUF * pow(NC, -1) * x * z * CF
                - 2.0 / 3.0 * LMUF * pow(x, -1) * pow(z, -1) * CF
                + 4.0 / 3.0 * LMUF * pow(x, -1) * CF
                - 1.0 / 2.0 * LMUF * pow(z, -1) * CF
                + LMUF * CF
                + 1.0 / 2.0 * LMUF * x * pow(z, -1) * CF
                - LMUF * x * CF
                + 2.0 / 3.0 * LMUF * pow(x, 2) * pow(z, -1) * CF
                - 4.0 / 3.0 * LMUF * pow(x, 2) * CF
                - 1.0 / 2.0 * LMUF * NC * CF
                - 2 * LMUF * NC * z * CF
                - 1.0 / 2.0 * LMUF * NC * x * z * CF
                + 1.0 / 2.0 * LMUA * pow(NC, -1) * CF
                + 2 * LMUA * pow(NC, -1) * x * CF
                + 1.0 / 2.0 * LMUA * pow(NC, -1) * x * z * CF
                + 1.0 / 3.0 * LMUA * pow(z, -1) * CF
                + 1.0 / 2.0 * LMUA * CF
                - 3.0 / 2.0 * LMUA * z * CF
                + 2.0 / 3.0 * LMUA * pow(z, 2) * CF
                + 1.0 / 3.0 * LMUA * x * pow(z, -1) * CF
                + 3.0 / 2.0 * LMUA * x * CF
                - 1.0 / 2.0 * LMUA * x * z * CF
                - 4.0 / 3.0 * LMUA * x * pow(z, 2) * CF
                - 1.0 / 2.0 * LMUA * NC * CF
                - 2 * LMUA * NC * x * CF
                - 1.0 / 2.0 * LMUA * NC * x * z * CF
                - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * CF
                - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * z * CF
                - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * x * CF
                - 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * x * z * CF
                + 1.0 / 2.0 * LMUA * LMUF * NC * CF
            )
            tmp += (
                +1.0 / 2.0 * LMUA * LMUF * NC * z * CF
                + 1.0 / 2.0 * LMUA * LMUF * NC * x * CF
                + 1.0 / 2.0 * LMUA * LMUF * NC * x * z * CF
                - 9 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 * CF
                + ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * sqrtxz3 * CF
                + 5 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF
                - 9 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 * CF
                + 3 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF
                - 3 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * sqrtxz3 * CF
                - 23 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF
                + 3 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * z * sqrtxz3 * CF
                + 9 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 * CF
                - ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * sqrtxz3 * CF
                - 5 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF
                + 9 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 * CF
                - 3 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF
                + 3 * ArcTan(sqrtxz3) * ln(sqrtxz3) * sqrtxz3 * CF
                + 23 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF
                - 3 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * z * sqrtxz3 * CF
                + 9.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 * CF
                - 1.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * sqrtxz3 * CF
                - 5.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF
                + 9.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 * CF
                - 3.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF
                + 3.0 / 2.0 * InvTanInt(-sqrtxz3) * sqrtxz3 * CF
                + 23.0 / 2.0 * InvTanInt(-sqrtxz3) * pow(z, 2) * sqrtxz3 * CF
            )
            tmp += (
                -3.0 / 2.0 * InvTanInt(-sqrtxz3) * x * z * sqrtxz3 * CF
                + 9 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 * CF
                - InvTanInt(z * sqrtxz3) * pow(NC, -1) * sqrtxz3 * CF
                - 5 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF
                + 9 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 * CF
                - 3 * InvTanInt(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF
                + 3 * InvTanInt(z * sqrtxz3) * sqrtxz3 * CF
                + 23 * InvTanInt(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF
                - 3 * InvTanInt(z * sqrtxz3) * x * z * sqrtxz3 * CF
                - 9.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(x, -1) * z * sqrtxz3 * CF
                + 1.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * sqrtxz3 * CF
                + 5.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF
                - 9.0 / 2.0 * InvTanInt(sqrtxz3) * pow(NC, -1) * x * z * sqrtxz3 * CF
                + 3.0 / 2.0 * InvTanInt(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF
                - 3.0 / 2.0 * InvTanInt(sqrtxz3) * sqrtxz3 * CF
                - 23.0 / 2.0 * InvTanInt(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF
                + 3.0 / 2.0 * InvTanInt(sqrtxz3) * x * z * sqrtxz3 * CF
                + 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * rln2 * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * rln2 * CF
                + 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF
                + 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * rln2 * CF * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * rln2 * CF
                + 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * sqrtxz1 * CF * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * rln2 * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF
                - 2 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
            )
            tmp += (
                -4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * rln2 * CF
                - 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * sqrtxz1 * CF
                - 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * rln2 * CF
                - 8 * ln(1 + sqrtxz1 - z) * rln2 * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * rln2 * CF
                - 6 * ln(1 + sqrtxz1 - z) * sqrtxz1 * CF * pow(omx, -1)
                + 12 * ln(1 + sqrtxz1 - z) * z * rln2 * CF
                - 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * rln2 * CF * pow(omx, -1)
                + 6 * ln(1 + sqrtxz1 - z) * x * rln2 * CF
                + 4 * ln(1 + sqrtxz1 - z) * x * sqrtxz1 * CF
                - 4 * ln(1 + sqrtxz1 - z) * x * z * rln2 * CF
                + 24 * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * rln2 * CF
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(omx, -1)
                + 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(omx, -1)
                - 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF
                + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF * pow(omx, -1)
                - 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * CF
                + 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF
                - 8 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, 2) * CF
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * CF * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * CF
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * CF
                + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * CF
            )
            tmp += (
                +4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF
                + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF
                - 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF
                - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF
                + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * rln2 * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * rln2 * CF
                + 8 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * rln2 * CF * pow(omx, -1)
                - 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * rln2 * CF
                + 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * rln2 * CF * pow(omx, -1)
                - 2 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF
                - 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * rln2 * CF
                - 4 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * rln2 * CF
                - 4 * ln(1 + sqrtxz1 + z) * rln2 * CF * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 + z) * rln2 * CF
                - 8 * ln(1 + sqrtxz1 + z) * z * rln2 * CF * pow(omx, -1)
                + 4 * ln(1 + sqrtxz1 + z) * z * rln2 * CF
                - 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * rln2 * CF * pow(omx, -1)
                + 2 * ln(1 + sqrtxz1 + z) * x * rln2 * CF
                + 4 * ln(1 + sqrtxz1 + z) * x * z * rln2 * CF
                + 8 * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * rln2 * CF
                + 4 * ln(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                - 4 * ln(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                - 8 * ln(x) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                + 8 * ln(x) * pow(NC, -1) * pow(x, -2) * CF
                + 8 * ln(x) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
            )
            tmp += (
                -8 * ln(x) * pow(NC, -1) * pow(x, -2) * z * CF
                + 4 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                - 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2) * CF
                + 7.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1) * CF
                - 9 * ln(x) * pow(NC, -1) * pow(x, -1) * CF
                + 8 * ln(x) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                + 48 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 87.0 / 2.0 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - 16 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                - 4 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + 13 * ln(x) * pow(NC, -1) * pow(z, -1) * CF
                - 2 * ln(x) * pow(NC, -1) * pow(z, -1) * rln2 * CF * pow(omx, -1)
                + ln(x) * pow(NC, -1) * pow(z, -1) * rln2 * CF
                - 3 * ln(x) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF * pow(omx, -1)
                + 2 * ln(x) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF
                + 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(poly2, -2) * CF
                - 5.0 / 4.0 * ln(x) * pow(NC, -1) * pow(poly2, -1) * CF
                - 36 * ln(x) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * pow(NC, -1) * CF * pow(omx, -1) * pow(xmz, -1)
                - 2 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
                + 16 * ln(x) * pow(NC, -1) * CF * pow(omz, -1)
                + 8 * ln(x) * pow(NC, -1) * CF * pow(opx, -1)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * CF * pow(xmz, -1)
                + 3.0 / 2.0 * ln(x) * pow(NC, -1) * CF * pow(omxmz, -1)
                + 9 * ln(x) * pow(NC, -1) * CF
                - 4 * ln(x) * pow(NC, -1) * rln2 * CF * pow(omx, -1)
                + 2 * ln(x) * pow(NC, -1) * rln2 * CF
                - 3 * ln(x) * pow(NC, -1) * sqrtxz1 * CF * pow(omx, -1)
                - 37.0 / 2.0 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * ln(x) * pow(NC, -1) * z * CF
                - 2 * ln(x) * pow(NC, -1) * z * rln2 * CF * pow(omx, -1)
                - 32 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
            )
            tmp += (
                +30 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF
                + ln(x) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF
                + ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                - 3.0 / 4.0 * ln(x) * pow(NC, -1) * x * pow(poly2, -2) * CF
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * x * pow(poly2, -1) * CF
                + 20 * ln(x) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 3.0 / 2.0 * ln(x) * pow(NC, -1) * x * CF * pow(xmz, -1)
                - 1.0 / 2.0 * ln(x) * pow(NC, -1) * x * CF * pow(omxmz, -2)
                - 1.0 / 2.0 * ln(x) * pow(NC, -1) * x * CF * pow(omxmz, -1)
                + 5 * ln(x) * pow(NC, -1) * x * CF
                + 2 * ln(x) * pow(NC, -1) * x * rln2 * CF
                + 3 * ln(x) * pow(NC, -1) * x * sqrtxz1 * CF
                + 10 * ln(x) * pow(NC, -1) * x * z * CF
                + 2 * ln(x) * pow(NC, -1) * x * z * rln2 * CF
                - 2 * ln(x) * pow(NC, -1) * x * pow(z, 3) * CF * pow(xmz, -2)
                + 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2) * CF
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1) * CF
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * CF * pow(xmz, -2)
                + 1.0 / 2.0 * ln(x) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -2)
                + 5 * ln(x) * pow(NC, -1) * pow(x, 2) * CF
                + 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2) * CF
                - 5.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1) * CF
                - ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(xmz, -2)
                - 9 * ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(xmz, -1)
                - 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2) * CF
                + 7.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1) * CF
                + 3 * ln(x) * pow(NC, -1) * pow(x, 4) * CF * pow(xmz, -2)
                + 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2) * CF
                - 3.0 / 4.0 * ln(x) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2) * CF
                + 4 * ln(x) * pow(x, -2) * CF * pow(opx, -1)
                - 4 * ln(x) * pow(x, -2) * CF
                - 8 * ln(x) * pow(x, -2) * z * CF * pow(opx, -1)
                + 8 * ln(x) * pow(x, -2) * z * CF
                + 16 * ln(x) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
            )
            tmp += (
                -16 * ln(x) * pow(x, -2) * pow(z, 2) * CF
                + 4 * ln(x) * pow(x, -1) * CF
                - 8 * ln(x) * pow(x, -1) * z * CF
                + 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 4.0 / 3.0 * ln(x) * pow(z, -1) * CF * pow(omx, -1)
                + 5.0 / 3.0 * ln(x) * pow(z, -1) * CF
                - 9.0 / 2.0 * ln(x) * CF * pow(omx, -1)
                - 4 * ln(x) * CF * pow(opx, -1)
                - 4 * ln(x) * CF
                + 5 * ln(x) * rln2 * CF * pow(omx, -1)
                + 2 * ln(x) * rln2 * CF
                + 3 * ln(x) * sqrtxz1 * CF * pow(omx, -1)
                + 11.0 / 2.0 * ln(x) * z * CF * pow(omx, -1)
                + 8 * ln(x) * z * CF * pow(opx, -1)
                + 3.0 / 2.0 * ln(x) * z * CF
                - 2 * ln(x) * z * rln2 * CF * pow(omx, -1)
                - 8 * ln(x) * z * rln2 * CF
                + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF * pow(omx, -1)
                + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF
                + 16 * ln(x) * pow(z, 2) * rln2 * CF * pow(omx, -1)
                + 11.0 / 3.0 * ln(x) * x * pow(z, -1) * CF
                + ln(x) * x * CF * pow(xmz, -1)
                - 3 * ln(x) * x * CF
                - 4 * ln(x) * x * rln2 * CF
                - 2 * ln(x) * x * sqrtxz1 * CF
                + 3.0 / 2.0 * ln(x) * x * z * CF
                + 4 * ln(x) * x * z * rln2 * CF
                - 8.0 / 3.0 * ln(x) * x * pow(z, 2) * CF
                - 16 * ln(x) * x * pow(z, 2) * rln2 * CF
                + 2 * ln(x) * pow(x, 2) * pow(z, -1) * CF
                - 2 * ln(x) * pow(x, 2) * CF * pow(xmz, -1)
                - 6 * ln(x) * pow(x, 2) * CF
                + 2 * ln(x) * pow(x, 3) * CF * pow(xmz, -1)
                - 6 * ln(x) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(x) * NC * CF * pow(omx, -1) * pow(xmz, -1)
                - 5.0 / 2.0 * ln(x) * NC * CF * pow(omx, -1)
                + 3.0 / 2.0 * ln(x) * NC * CF * pow(xmz, -1)
                - 3.0 / 2.0 * ln(x) * NC * CF * pow(omxmz, -1)
                - 31.0 / 6.0 * ln(x) * NC * CF
                + 5.0 / 2.0 * ln(x) * NC * z * CF * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * NC * z * CF
                + 6 * ln(x) * NC * x * CF * pow(omz, -1)
                + 3.0 / 2.0 * ln(x) * NC * x * CF * pow(xmz, -1)
                + 1.0 / 2.0 * ln(x) * NC * x * CF * pow(omxmz, -2)
                - 1.0 / 2.0 * ln(x) * NC * x * CF * pow(omxmz, -1)
                + 9.0 / 2.0 * ln(x) * NC * x * CF
                + 11.0 / 6.0 * ln(x) * NC * x * z * CF
                + 1.0 / 2.0 * ln(x) * NC * pow(x, 2) * CF * pow(xmz, -2)
            )
            tmp += (
                +2 * ln(x) * NC * pow(x, 2) * CF * pow(xmz, -1)
                - 1.0 / 2.0 * ln(x) * NC * pow(x, 2) * CF * pow(omxmz, -2)
                - ln(x) * NC * pow(x, 3) * CF * pow(xmz, -2)
                - ln(x) * NC * pow(x, 3) * CF * pow(xmz, -1)
                + ln(x) * NC * pow(x, 4) * CF * pow(xmz, -2)
                + ln(x) * NF * CF * pow(omx, -1)
                - 4.0 / 3.0 * ln(x) * NF * CF
                + ln(x) * NF * z * CF * pow(omx, -1)
                - 4.0 / 3.0 * ln(x) * NF * x * z * CF
                + ln(x) * LMUF * pow(NC, -1) * CF * pow(omx, -1)
                - 3.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * CF
                + ln(x) * LMUF * pow(NC, -1) * z * CF * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * z * CF
                - 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * CF
                - 3.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * z * CF
                - ln(x) * LMUF * pow(z, -1) * CF
                + 2 * ln(x) * LMUF * CF
                - ln(x) * LMUF * x * pow(z, -1) * CF
                + 2 * ln(x) * LMUF * x * CF
                - ln(x) * LMUF * NC * CF * pow(omx, -1)
                + 3.0 / 2.0 * ln(x) * LMUF * NC * CF
                - ln(x) * LMUF * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * ln(x) * LMUF * NC * z * CF
                + 1.0 / 2.0 * ln(x) * LMUF * NC * x * CF
                + 3.0 / 2.0 * ln(x) * LMUF * NC * x * z * CF
                + ln(x) * LMUA * pow(NC, -1) * CF * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * CF
                + ln(x) * LMUA * pow(NC, -1) * z * CF * pow(omx, -1)
                - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * z * CF
                - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * x * CF
                - 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * x * z * CF
                - ln(x) * LMUA * NC * CF * pow(omx, -1)
                + 1.0 / 2.0 * ln(x) * LMUA * NC * CF
                - ln(x) * LMUA * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * ln(x) * LMUA * NC * z * CF
                + 1.0 / 2.0 * ln(x) * LMUA * NC * x * CF
                + 1.0 / 2.0 * ln(x) * LMUA * NC * x * z * CF
                - 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                - 5.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * CF
            )
            tmp += (
                -3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF
                - 9 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1) * CF
                - 2 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 2 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 51.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF
                - 18 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) * CF
                + 18 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 9.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                - 9 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                + 3.0 / 4.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - 5.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * CF
                + ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                - 3.0 / 8.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - 4 * ln(x) * ln(1 - sqrtxz2 + x) * pow(sqrtxz2, -1) * CF
                + 8 * ln(x) * ln(1 - sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF
                - 2 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF
            )
            tmp += (
                +16 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF
                - 16 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                - 4 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                + 8 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                + 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                + 5.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * CF
                + 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF
                + 9 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1) * CF
                + 2 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 2 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 51.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF
                + 18 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) * CF
                - 18 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                + 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 9.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                + 9 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
            )
            tmp += (
                -3.0 / 4.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + 5.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * CF
                - ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                + 3.0 / 8.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + 4 * ln(x) * ln(1 + sqrtxz2 + x) * pow(sqrtxz2, -1) * CF
                - 8 * ln(x) * ln(1 + sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF
                + 2 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF
                - 16 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF
                + 16 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                + 4 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                - 8 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 - z) * CF
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF
                - 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * CF
                - 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF
                + 8 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * CF
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF
            )
            tmp += (
                -2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * CF
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * CF
                - 3 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                + 4 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF
                - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * ln(x) * ln(1 + sqrtxz1 + z) * x * CF
                + 8 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * CF
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
            )
            tmp += (
                +ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, 2) * CF
                - ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * pow(z, -1)) * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1)
                - ln(x) * ln(1 + x * pow(z, -1)) * x * CF
                + 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF
                - 4 * ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF
                - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + 8 * ln(x) * ln(1 + x) * pow(NC, -1) * CF * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x * pow(z, -1) * CF
                + 8 * ln(x) * ln(1 + x) * pow(NC, -1) * x * CF
                - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x * z * CF
                - 4 * ln(x) * ln(1 + x) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x) * CF
                + 8 * ln(x) * ln(1 + x) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x) * z * CF
                - 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF * pow(opx, -1)
                - 6 * ln(x) * ln(1 + x) * x * CF
                + 12 * ln(x) * ln(1 + x) * x * z * CF
                - 8 * ln(x) * ln(1 + x) * x * pow(z, 2) * CF
                - ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
            )
            tmp += (
                -2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * CF
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z * CF
                - ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * CF
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF
                - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * CF * pow(omx, -1)
                + 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * CF
                - ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                + ln(x) * ln(1 + x * z) * pow(x, -2) * CF
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF
                - 4 * ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * z) * pow(x, -2) * pow(z, 2) * CF
                - ln(x) * ln(1 + x * z) * pow(x, -1) * CF
                + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF
                - 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x * z) * CF * pow(omx, -1)
                - ln(x) * ln(1 + x * z) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(1 + x * z) * z * CF * pow(omx, -1)
                + 2 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(1 + x * z) * z * CF
                + 4 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(1 + x * z) * x * CF
            )
            tmp += (
                -8 * ln(x) * ln(1 + x * z) * x * pow(z, 2) * CF
                + 2 * ln(x) * ln(z + x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - ln(x) * ln(z + x) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * ln(x) * ln(z + x) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(z + x) * pow(NC, -1) * CF
                + 2 * ln(x) * ln(z + x) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(x) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * CF
                - 2 * ln(x) * ln(z + x) * pow(NC, -1) * x * CF
                - 2 * ln(x) * ln(z + x) * pow(NC, -1) * x * z * CF
                - 2 * ln(x) * ln(z + x) * CF * pow(omx, -1)
                + ln(x) * ln(z + x) * CF
                - 4 * ln(x) * ln(z + x) * z * CF * pow(omx, -1)
                + 2 * ln(x) * ln(z + x) * z * CF
                - 4 * ln(x) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                + ln(x) * ln(z + x) * x * CF
                + 2 * ln(x) * ln(z + x) * x * z * CF
                + 4 * ln(x) * ln(z + x) * x * pow(z, 2) * CF
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * CF
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -2) * z * CF
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * CF
                - 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 16 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 16 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + 5 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                + 5.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                - 5 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF
                - pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                +13 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omz, -1)
                - 5 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(opx, -1)
                - 17.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * CF
                + 13 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                + pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * CF
                + 11 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                - 10 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                - 31.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF * pow(opx, -1)
                + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF
                + 3 * pow(ln(x), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                - 3 * pow(ln(x), 2) * pow(x, -2) * z * CF
                - 6 * pow(ln(x), 2) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 6 * pow(ln(x), 2) * pow(x, -2) * pow(z, 2) * CF
                - 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * CF
                + 3 * pow(ln(x), 2) * pow(x, -1) * z * CF
                - 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - pow(ln(x), 2) * pow(z, -1) * CF
                - 2 * pow(ln(x), 2) * CF * pow(omx, -1)
                + 5.0 / 2.0 * pow(ln(x), 2) * CF * pow(opx, -1)
                + 4 * pow(ln(x), 2) * CF
                + 4 * pow(ln(x), 2) * z * CF * pow(omx, -1)
                - 5 * pow(ln(x), 2) * z * CF * pow(opx, -1)
                - 4 * pow(ln(x), 2) * z * CF
                - 2 * pow(ln(x), 2) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1)
                - pow(ln(x), 2) * x * pow(z, -1) * CF
                + 5 * pow(ln(x), 2) * x * CF
                - 6 * pow(ln(x), 2) * x * z * CF
                + 4 * pow(ln(x), 2) * x * pow(z, 2) * CF
                + 8 * pow(ln(x), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 5 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
                - 4 * pow(ln(x), 2) * NC * CF * pow(omz, -1)
            )
            tmp += (
                +17.0 / 2.0 * pow(ln(x), 2) * NC * CF
                - 5 * pow(ln(x), 2) * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(x), 2) * NC * z * CF
                - 4 * pow(ln(x), 2) * NC * x * CF * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(x), 2) * NC * x * CF
                + 17.0 / 2.0 * pow(ln(x), 2) * NC * x * z * CF
                + ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                - ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                - 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * CF
                + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -2) * z * CF
                + ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                - 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * CF
                + 2 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                + 16 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 16 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - 6 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                + ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + 6 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 23.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(opx, -1)
                + 9 * ln(x) * ln(z) * pow(NC, -1) * CF
                - 27.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 2 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(opx, -1)
                - 10 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                - 4 * ln(x) * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                + 19 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                + ln(x) * ln(z) * pow(x, -2) * CF * pow(opx, -1)
            )
            tmp += (
                -ln(x) * ln(z) * pow(x, -2) * CF
                - 2 * ln(x) * ln(z) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(z) * pow(x, -2) * z * CF
                + 4 * ln(x) * ln(z) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * ln(x) * ln(z) * pow(x, -2) * pow(z, 2) * CF
                + ln(x) * ln(z) * pow(x, -1) * CF
                - 2 * ln(x) * ln(z) * pow(x, -1) * z * CF
                + 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + ln(x) * ln(z) * pow(z, -1) * CF
                + ln(x) * ln(z) * CF * pow(omx, -1)
                + ln(x) * ln(z) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(z) * CF
                - 7 * ln(x) * ln(z) * z * CF * pow(omx, -1)
                - 2 * ln(x) * ln(z) * z * CF * pow(opx, -1)
                - 2 * ln(x) * ln(z) * z * CF
                + 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(omx, -1)
                + 4 * ln(x) * ln(z) * pow(z, 2) * CF * pow(opx, -1)
                + ln(x) * ln(z) * x * pow(z, -1) * CF
                + 6 * ln(x) * ln(z) * x * z * CF
                - 4 * ln(x) * ln(z) * x * pow(z, 2) * CF
                - 8 * ln(x) * ln(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 7.0 / 2.0 * ln(x) * ln(z) * NC * CF * pow(omx, -1)
                + 4 * ln(x) * ln(z) * NC * CF * pow(omz, -1)
                - 5 * ln(x) * ln(z) * NC * CF
                + 7.0 / 2.0 * ln(x) * ln(z) * NC * z * CF * pow(omx, -1)
                + 4 * ln(x) * ln(z) * NC * x * CF * pow(omz, -1)
                - 5 * ln(x) * ln(z) * NC * x * z * CF
                - 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * CF
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -2) * z * CF
                - 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * CF
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                +8 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                + 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                + 28 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 17 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                - 7 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(opx, -1)
                + 9 * ln(x) * ln(omx) * pow(NC, -1) * CF
                - 17 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + ln(x) * ln(omx) * pow(NC, -1) * z * CF
                + 4 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                - 4 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                - 21 * ln(x) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 15 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                + 23 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                - 2 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * pow(x, -2) * CF
                + 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF
                - 8 * ln(x) * ln(omx) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 8 * ln(x) * ln(omx) * pow(x, -2) * pow(z, 2) * CF
                - 2 * ln(x) * ln(omx) * pow(x, -1) * CF
                + 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF
                - 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 3 * ln(x) * ln(omx) * CF * pow(omx, -1)
                + 2 * ln(x) * ln(omx) * CF * pow(opx, -1)
                - 6 * ln(x) * ln(omx) * z * CF * pow(omx, -1)
                - 4 * ln(x) * ln(omx) * z * CF * pow(opx, -1)
                + 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(omx, -1)
                - 2 * ln(x) * ln(omx) * x * CF
                + 4 * ln(x) * ln(omx) * x * z * CF
                - 8 * ln(x) * ln(omx) * x * pow(z, 2) * CF
                - 10 * ln(x) * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
            )
            tmp += (
                +8 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
                + 5 * ln(x) * ln(omx) * NC * CF * pow(omz, -1)
                - 13 * ln(x) * ln(omx) * NC * CF
                + 8 * ln(x) * ln(omx) * NC * z * CF * pow(omx, -1)
                - ln(x) * ln(omx) * NC * z * CF
                + 5 * ln(x) * ln(omx) * NC * x * CF * pow(omz, -1)
                - ln(x) * ln(omx) * NC * x * CF
                - 13 * ln(x) * ln(omx) * NC * x * z * CF
                + 18 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 16 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                - 6 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                + 14 * ln(x) * ln(omz) * pow(NC, -1) * CF
                - 16 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + ln(x) * ln(omz) * pow(NC, -1) * z * CF
                - 12 * ln(x) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 7 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                + 20 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                + ln(x) * ln(omz) * pow(z, -1) * CF
                - 2 * ln(x) * ln(omz) * CF
                + ln(x) * ln(omz) * x * pow(z, -1) * CF
                - 2 * ln(x) * ln(omz) * x * CF
                - 12 * ln(x) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 8 * ln(x) * ln(omz) * NC * CF * pow(omx, -1)
                + 6 * ln(x) * ln(omz) * NC * CF * pow(omz, -1)
                - 14 * ln(x) * ln(omz) * NC * CF
                + 8 * ln(x) * ln(omz) * NC * z * CF * pow(omx, -1)
                - ln(x) * ln(omz) * NC * z * CF
                + 6 * ln(x) * ln(omz) * NC * x * CF * pow(omz, -1)
                - ln(x) * ln(omz) * NC * x * CF
                - 14 * ln(x) * ln(omz) * NC * x * z * CF
                + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                - 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * CF
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -2) * z * CF
                + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
            )
            tmp += (
                -4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * CF
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(NC, -1) * pow(z, -1) * CF
                - 4 * ln(x) * ln(opx) * pow(NC, -1) * CF * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * CF
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * z * CF * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * pow(NC, -1) * x * pow(z, -1) * CF
                - 4 * ln(x) * ln(opx) * pow(NC, -1) * x * CF
                + 4 * ln(x) * ln(opx) * pow(NC, -1) * x * z * CF
                + 2 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * pow(x, -2) * CF
                - 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF
                + 8 * ln(x) * ln(opx) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * ln(x) * ln(opx) * pow(x, -2) * pow(z, 2) * CF
                + 2 * ln(x) * ln(opx) * pow(x, -1) * CF
                - 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF
                + 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * CF * pow(opx, -1)
                - 2 * ln(x) * ln(opx) * CF
                - 4 * ln(x) * ln(opx) * z * CF * pow(opx, -1)
                + 4 * ln(x) * ln(opx) * z * CF
                + 8 * ln(x) * ln(opx) * pow(z, 2) * CF * pow(opx, -1)
                + 2 * ln(x) * ln(opx) * x * CF
                - 4 * ln(x) * ln(opx) * x * z * CF
                + 8 * ln(x) * ln(opx) * x * pow(z, 2) * CF
                - 3.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2) * CF
                + 7.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1) * CF
                - ln(z) * pow(NC, -1) * pow(x, -1) * CF
                - 24 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 27 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + 8 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                - 10 * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                - 6 * ln(z) * pow(NC, -1) * pow(z, -1) * rln2 * CF * pow(omx, -1)
            )
            tmp += (
                +3 * ln(z) * pow(NC, -1) * pow(z, -1) * rln2 * CF
                - 3 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF * pow(omx, -1)
                + 2 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF
                - 3.0 / 4.0 * ln(z) * pow(NC, -1) * pow(poly2, -2) * CF
                + 5.0 / 4.0 * ln(z) * pow(NC, -1) * pow(poly2, -1) * CF
                + 35.0 / 2.0 * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(xmz, -1)
                + 6 * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                - 8 * ln(z) * pow(NC, -1) * CF * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * pow(NC, -1) * CF * pow(xmz, -1)
                + 11.0 / 2.0 * ln(z) * pow(NC, -1) * CF
                - 12 * ln(z) * pow(NC, -1) * rln2 * CF * pow(omx, -1)
                + 6 * ln(z) * pow(NC, -1) * rln2 * CF
                - 3 * ln(z) * pow(NC, -1) * sqrtxz1 * CF * pow(omx, -1)
                + 11 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 7.0 / 2.0 * ln(z) * pow(NC, -1) * z * CF
                - 6 * ln(z) * pow(NC, -1) * z * rln2 * CF * pow(omx, -1)
                + 16 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                - 17 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                + 3 * ln(z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF
                + ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                - 3.0 / 4.0 * ln(z) * pow(NC, -1) * x * pow(poly2, -2) * CF
                + 1.0 / 2.0 * ln(z) * pow(NC, -1) * x * pow(poly2, -1) * CF
                - 8 * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * pow(NC, -1) * x * CF * pow(xmz, -1)
                - 23.0 / 2.0 * ln(z) * pow(NC, -1) * x * CF
                + 6 * ln(z) * pow(NC, -1) * x * rln2 * CF
                + 3 * ln(z) * pow(NC, -1) * x * sqrtxz1 * CF
                - 25.0 / 2.0 * ln(z) * pow(NC, -1) * x * z * CF
                + 6 * ln(z) * pow(NC, -1) * x * z * rln2 * CF
                + 2 * ln(z) * pow(NC, -1) * x * pow(z, 3) * CF * pow(xmz, -2)
                - 3.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2) * CF
                - 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1) * CF
                - 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(x, 2) * CF * pow(xmz, -2)
            )
            tmp += (
                -5 * ln(z) * pow(NC, -1) * pow(x, 2) * CF
                + 3.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2) * CF
                - 5.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1) * CF
                + ln(z) * pow(NC, -1) * pow(x, 3) * CF * pow(xmz, -2)
                + 9 * ln(z) * pow(NC, -1) * pow(x, 3) * CF * pow(xmz, -1)
                + 3.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2) * CF
                - 7.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1) * CF
                - 3 * ln(z) * pow(NC, -1) * pow(x, 4) * CF * pow(xmz, -2)
                + 3.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2) * CF
                + 3.0 / 4.0 * ln(z) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2) * CF
                + 2.0 / 3.0 * ln(z) * pow(x, -1) * pow(z, -1) * CF
                + 2.0 / 3.0 * ln(z) * pow(x, -1) * CF * pow(omz, -1)
                - 4.0 / 3.0 * ln(z) * pow(x, -1) * CF
                + 1.0 / 6.0 * ln(z) * pow(z, -1) * CF
                - 3 * ln(z) * CF * pow(omx, -1)
                - ln(z) * CF * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * CF
                + 7 * ln(z) * rln2 * CF * pow(omx, -1)
                - 2 * ln(z) * rln2 * CF
                + 3 * ln(z) * sqrtxz1 * CF * pow(omx, -1)
                - 3 * ln(z) * z * CF * pow(omx, -1)
                + 4 * ln(z) * z * CF
                + 10 * ln(z) * z * rln2 * CF * pow(omx, -1)
                - 8 * ln(z) * z * rln2 * CF
                - 2.0 / 3.0 * ln(z) * pow(z, 2) * CF
                + 16 * ln(z) * pow(z, 2) * rln2 * CF * pow(omx, -1)
                - 5.0 / 6.0 * ln(z) * x * pow(z, -1) * CF
                + ln(z) * x * CF * pow(omz, -1)
                - ln(z) * x * CF * pow(xmz, -1)
                + 1.0 / 2.0 * ln(z) * x * CF
                - 4 * ln(z) * x * rln2 * CF
                - 2 * ln(z) * x * sqrtxz1 * CF
                + ln(z) * x * z * CF
                - 4 * ln(z) * x * z * rln2 * CF
                + 4.0 / 3.0 * ln(z) * x * pow(z, 2) * CF
                - 16 * ln(z) * x * pow(z, 2) * rln2 * CF
                - 2.0 / 3.0 * ln(z) * pow(x, 2) * pow(z, -1) * CF
                - 2.0 / 3.0 * ln(z) * pow(x, 2) * CF * pow(omz, -1)
                + 2 * ln(z) * pow(x, 2) * CF * pow(xmz, -1)
                + 10.0 / 3.0 * ln(z) * pow(x, 2) * CF
                - 2 * ln(z) * pow(x, 3) * CF * pow(xmz, -1)
                + 1.0 / 2.0 * ln(z) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * NC * CF * pow(omx, -1) * pow(xmz, -1)
            )
            tmp += (
                +ln(z) * NC * CF * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * NC * CF * pow(xmz, -1)
                + 4 * ln(z) * NC * CF
                - 2 * ln(z) * NC * z * CF * pow(omx, -1)
                - ln(z) * NC * z * CF
                - 3 * ln(z) * NC * x * CF * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * NC * x * CF * pow(xmz, -1)
                + ln(z) * NC * x * CF
                + 6 * ln(z) * NC * x * z * CF
                - 1.0 / 2.0 * ln(z) * NC * pow(x, 2) * CF * pow(xmz, -2)
                - 2 * ln(z) * NC * pow(x, 2) * CF * pow(xmz, -1)
                + ln(z) * NC * pow(x, 3) * CF * pow(xmz, -2)
                + ln(z) * NC * pow(x, 3) * CF * pow(xmz, -1)
                - ln(z) * NC * pow(x, 4) * CF * pow(xmz, -2)
                - ln(z) * LMUF * pow(NC, -1) * CF * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * CF
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * z * CF
                - ln(z) * LMUF * pow(NC, -1) * x * CF * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * x * CF
                + 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * x * z * CF
                + ln(z) * LMUF * NC * CF * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * LMUF * NC * CF
                - 1.0 / 2.0 * ln(z) * LMUF * NC * z * CF
                + ln(z) * LMUF * NC * x * CF * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * LMUF * NC * x * CF
                - 1.0 / 2.0 * ln(z) * LMUF * NC * x * z * CF
                + ln(z) * LMUA * pow(NC, -1) * CF * pow(omz, -1)
                - 3.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * CF
                - 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * z * CF
                + ln(z) * LMUA * pow(NC, -1) * x * CF * pow(omz, -1)
                - 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * x * CF
                - 3.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * x * z * CF
                + ln(z) * LMUA * CF
                + ln(z) * LMUA * x * CF
                + 2 * ln(z) * LMUA * x * z * CF
                - ln(z) * LMUA * NC * CF * pow(omz, -1)
                + 3.0 / 2.0 * ln(z) * LMUA * NC * CF
                + 1.0 / 2.0 * ln(z) * LMUA * NC * z * CF
                - ln(z) * LMUA * NC * x * CF * pow(omz, -1)
                + 1.0 / 2.0 * ln(z) * LMUA * NC * x * CF
                + 3.0 / 2.0 * ln(z) * LMUA * NC * x * z * CF
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * CF * pow(omx, -1)
            )
            tmp += (
                -2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * CF
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * CF
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * CF
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * CF
                - 3 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF
                - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 - z) * x * CF
                + 8 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF
                + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * CF * pow(omx, -1)
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * CF
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * CF
                - 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * CF
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF
                - 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF
                + 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF
                + 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
            )
            tmp += (
                -2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * CF
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * pow(z, 2) * CF
                + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                - ln(z) * ln(1 + x * pow(z, -1)) * CF
            )
            tmp += (
                -2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * pow(z, -1)) * x * CF
                - 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF
                + 4 * ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF
                - ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * CF
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -2) * z * CF
                - ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * CF
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF
                - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z * CF * pow(opx, -1)
                + 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * CF
                - ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                + ln(z) * ln(1 + x * z) * pow(x, -2) * CF
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF
                - 4 * ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * ln(z) * ln(1 + x * z) * pow(x, -2) * pow(z, 2) * CF
            )
            tmp += (
                -ln(z) * ln(1 + x * z) * pow(x, -1) * CF
                + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF
                - 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 2 * ln(z) * ln(1 + x * z) * CF * pow(omx, -1)
                - ln(z) * ln(1 + x * z) * CF * pow(opx, -1)
                + 4 * ln(z) * ln(1 + x * z) * z * CF * pow(omx, -1)
                + 2 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1)
                - 4 * ln(z) * ln(1 + x * z) * z * CF
                + 4 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * ln(z) * ln(1 + x * z) * x * CF
                - 8 * ln(z) * ln(1 + x * z) * x * pow(z, 2) * CF
                - 2 * ln(z) * ln(z + x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + ln(z) * ln(z + x) * pow(NC, -1) * pow(z, -1) * CF
                - 4 * ln(z) * ln(z + x) * pow(NC, -1) * CF * pow(omx, -1)
                + 2 * ln(z) * ln(z + x) * pow(NC, -1) * CF
                - 2 * ln(z) * ln(z + x) * pow(NC, -1) * z * CF * pow(omx, -1)
                + ln(z) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * CF
                + 2 * ln(z) * ln(z + x) * pow(NC, -1) * x * CF
                + 2 * ln(z) * ln(z + x) * pow(NC, -1) * x * z * CF
                + 2 * ln(z) * ln(z + x) * CF * pow(omx, -1)
                - ln(z) * ln(z + x) * CF
                + 4 * ln(z) * ln(z + x) * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(z + x) * z * CF
                + 4 * ln(z) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                - ln(z) * ln(z + x) * x * CF
                - 2 * ln(z) * ln(z + x) * x * z * CF
                - 4 * ln(z) * ln(z + x) * x * pow(z, 2) * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                - pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                + pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * CF
                + pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                - pow(ln(z), 2) * pow(NC, -1) * pow(x, -2) * z * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
            )
            tmp += (
                -pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * CF
                + pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 2 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF
                - 3 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omz, -1)
                - pow(ln(z), 2) * pow(NC, -1) * CF * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * CF
                + 3 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                + pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF
                + pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF * pow(opx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF
                - pow(ln(z), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                + pow(ln(z), 2) * pow(x, -2) * z * CF
                + 2 * pow(ln(z), 2) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * pow(ln(z), 2) * pow(x, -2) * pow(z, 2) * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * CF
                - pow(ln(z), 2) * pow(x, -1) * z * CF
                + 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - pow(ln(z), 2) * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(opx, -1)
                - 2 * pow(ln(z), 2) * CF
            )
            tmp += (
                +2 * pow(ln(z), 2) * z * CF * pow(omx, -1)
                - pow(ln(z), 2) * z * CF * pow(opx, -1)
                + 2 * pow(ln(z), 2) * z * CF
                - 2 * pow(ln(z), 2) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * pow(ln(z), 2) * pow(z, 2) * CF * pow(opx, -1)
                + pow(ln(z), 2) * x * CF
                - 6 * pow(ln(z), 2) * x * z * CF
                + 4 * pow(ln(z), 2) * x * pow(z, 2) * CF
                + 2 * pow(ln(z), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - pow(ln(z), 2) * NC * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * CF
                - pow(ln(z), 2) * NC * z * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * z * CF
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * x * CF
                - 1.0 / 2.0 * pow(ln(z), 2) * NC * x * z * CF
                - 12 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 8 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                + 3 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omz, -1)
                - 5 * ln(z) * ln(omx) * pow(NC, -1) * CF
                + 8 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 9 * ln(z) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 6 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                - 11 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                - ln(z) * ln(omx) * CF
                - ln(z) * ln(omx) * x * CF
                - 2 * ln(z) * ln(omx) * x * z * CF
                + 4 * ln(z) * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * ln(z) * ln(omx) * NC * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omx) * NC * CF * pow(omz, -1)
                + 3 * ln(z) * ln(omx) * NC * CF
                - 2 * ln(z) * ln(omx) * NC * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omx) * NC * x * CF * pow(omz, -1)
                + 3 * ln(z) * ln(omx) * NC * x * z * CF
                - 14 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 13 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                + 5 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 12 * ln(z) * ln(omz) * pow(NC, -1) * CF
                + 13 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 11 * ln(z) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
            )
            tmp += (
                -6 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                - 18 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                + ln(z) * ln(omz) * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omz) * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omz) * x * CF
                + 4 * ln(z) * ln(omz) * x * z * CF
                + 2 * ln(z) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - ln(z) * ln(omz) * NC * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omz) * NC * CF * pow(omz, -1)
                + 6 * ln(z) * ln(omz) * NC * CF
                - ln(z) * ln(omz) * NC * z * CF * pow(omx, -1)
                - 2 * ln(z) * ln(omz) * NC * x * CF * pow(omz, -1)
                + 6 * ln(z) * ln(omz) * NC * x * z * CF
                - 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(omx) * pow(NC, -1) * CF
                + 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 1.0 / 2.0 * ln(omx) * pow(NC, -1) * z * CF
                + 6 * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 3.0 / 2.0 * ln(omx) * pow(NC, -1) * x * CF
                - 11.0 / 2.0 * ln(omx) * pow(NC, -1) * x * z * CF
                + 2.0 / 3.0 * ln(omx) * pow(x, -1) * pow(z, -1) * CF
                - 4.0 / 3.0 * ln(omx) * pow(x, -1) * CF
                + 1.0 / 6.0 * ln(omx) * pow(z, -1) * CF
                - 3.0 / 2.0 * ln(omx) * CF
                + 3.0 / 2.0 * ln(omx) * z * CF
                - 2.0 / 3.0 * ln(omx) * pow(z, 2) * CF
                - 5.0 / 6.0 * ln(omx) * x * pow(z, -1) * CF
                - 1.0 / 2.0 * ln(omx) * x * CF
                + 1.0 / 2.0 * ln(omx) * x * z * CF
                + 4.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF
                - 2.0 / 3.0 * ln(omx) * pow(x, 2) * pow(z, -1) * CF
                + 4.0 / 3.0 * ln(omx) * pow(x, 2) * CF
                + 4 * ln(omx) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 11.0 / 6.0 * ln(omx) * NC * CF
                - 4 * ln(omx) * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * ln(omx) * NC * z * CF
                - 4 * ln(omx) * NC * x * CF * pow(omz, -1)
                - 7.0 / 2.0 * ln(omx) * NC * x * CF
                - 1.0 / 6.0 * ln(omx) * NC * x * z * CF
                + 2.0 / 3.0 * ln(omx) * NF * CF
                + 2.0 / 3.0 * ln(omx) * NF * x * z * CF
                + 5.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * CF
                + 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * z * CF
                + 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * x * CF
                + 5.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * x * z * CF
            )
            tmp += (
                -5.0 / 2.0 * ln(omx) * LMUF * NC * CF
                - 1.0 / 2.0 * ln(omx) * LMUF * NC * z * CF
                - 1.0 / 2.0 * ln(omx) * LMUF * NC * x * CF
                - 5.0 / 2.0 * ln(omx) * LMUF * NC * x * z * CF
                + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * CF
                + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * z * CF
                + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * x * CF
                + 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * x * z * CF
                - 1.0 / 2.0 * ln(omx) * LMUA * NC * CF
                - 1.0 / 2.0 * ln(omx) * LMUA * NC * z * CF
                - 1.0 / 2.0 * ln(omx) * LMUA * NC * x * CF
                - 1.0 / 2.0 * ln(omx) * LMUA * NC * x * z * CF
                - 5 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omz, -1)
                - 5.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * CF
                + 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * z * CF
                + 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                - 13.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                + 4 * pow(ln(omx), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * pow(ln(omx), 2) * NC * CF * pow(omx, -1)
                - 2 * pow(ln(omx), 2) * NC * CF * pow(omz, -1)
                + 11.0 / 2.0 * pow(ln(omx), 2) * NC * CF
                - 2 * pow(ln(omx), 2) * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * z * CF
                - 2 * pow(ln(omx), 2) * NC * x * CF * pow(omz, -1)
                + 1.0 / 2.0 * pow(ln(omx), 2) * NC * x * CF
                + 11.0 / 2.0 * pow(ln(omx), 2) * NC * x * z * CF
                - 8 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                + 2 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omz, -1)
                - 7 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                + 6 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - ln(omx) * ln(omz) * pow(NC, -1) * z * CF
            )
            tmp += (
                +6 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 5 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                - 11 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                + 8 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 4 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1)
                - 4 * ln(omx) * ln(omz) * NC * CF * pow(omz, -1)
                + 11 * ln(omx) * ln(omz) * NC * CF
                - 4 * ln(omx) * ln(omz) * NC * z * CF * pow(omx, -1)
                + ln(omx) * ln(omz) * NC * z * CF
                - 4 * ln(omx) * ln(omz) * NC * x * CF * pow(omz, -1)
                + ln(omx) * ln(omz) * NC * x * CF
                + 11 * ln(omx) * ln(omz) * NC * x * z * CF
                - 6 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3.0 / 2.0 * ln(omz) * pow(NC, -1) * CF * pow(omxmz, -1)
                + 3 * ln(omz) * pow(NC, -1) * CF
                + 6 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * ln(omz) * pow(NC, -1) * z * CF
                + 6 * ln(omz) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1) * x * CF * pow(omxmz, -2)
                + 1.0 / 2.0 * ln(omz) * pow(NC, -1) * x * CF * pow(omxmz, -1)
                - 2 * ln(omz) * pow(NC, -1) * x * CF
                - 4 * ln(omz) * pow(NC, -1) * x * z * CF
                - 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -2)
                + 2.0 / 3.0 * ln(omz) * pow(x, -1) * pow(z, -1) * CF
                - 4.0 / 3.0 * ln(omz) * pow(x, -1) * CF
                + 1.0 / 6.0 * ln(omz) * pow(z, -1) * CF
                - 3.0 / 2.0 * ln(omz) * CF
                + 3.0 / 2.0 * ln(omz) * z * CF
                - 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF
                - 5.0 / 6.0 * ln(omz) * x * pow(z, -1) * CF
                - 1.0 / 2.0 * ln(omz) * x * CF
                + 1.0 / 2.0 * ln(omz) * x * z * CF
                + 4.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF
                - 2.0 / 3.0 * ln(omz) * pow(x, 2) * pow(z, -1) * CF
                + 4.0 / 3.0 * ln(omz) * pow(x, 2) * CF
                + 4 * ln(omz) * NC * CF * pow(omx, -1) * pow(omz, -1)
                + 3.0 / 2.0 * ln(omz) * NC * CF * pow(omxmz, -1)
                + 1.0 / 3.0 * ln(omz) * NC * CF
                - 4 * ln(omz) * NC * z * CF * pow(omx, -1)
                + 2 * ln(omz) * NC * z * CF
                - 4 * ln(omz) * NC * x * CF * pow(omz, -1)
            )
            tmp += (
                -1.0 / 2.0 * ln(omz) * NC * x * CF * pow(omxmz, -2)
                + 1.0 / 2.0 * ln(omz) * NC * x * CF * pow(omxmz, -1)
                - 2 * ln(omz) * NC * x * CF
                - 5.0 / 3.0 * ln(omz) * NC * x * z * CF
                + 1.0 / 2.0 * ln(omz) * NC * pow(x, 2) * CF * pow(omxmz, -2)
                + 2.0 / 3.0 * ln(omz) * NF * CF
                + 2.0 / 3.0 * ln(omz) * NF * x * z * CF
                + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * CF
                + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * z * CF
                + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * x * CF
                + 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * x * z * CF
                - 1.0 / 2.0 * ln(omz) * LMUF * NC * CF
                - 1.0 / 2.0 * ln(omz) * LMUF * NC * z * CF
                - 1.0 / 2.0 * ln(omz) * LMUF * NC * x * CF
                - 1.0 / 2.0 * ln(omz) * LMUF * NC * x * z * CF
                + 5.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * CF
                + 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * z * CF
                + 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * x * CF
                + 5.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * x * z * CF
                - 5.0 / 2.0 * ln(omz) * LMUA * NC * CF
                - 1.0 / 2.0 * ln(omz) * LMUA * NC * z * CF
                - 1.0 / 2.0 * ln(omz) * LMUA * NC * x * CF
                - 5.0 / 2.0 * ln(omz) * LMUA * NC * x * z * CF
                - 5 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                + 2 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omz, -1)
                - 11.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * CF
                + 9.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF
                + 3 * pow(ln(omz), 2) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                - 13.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                + 4 * pow(ln(omz), 2) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - 2 * pow(ln(omz), 2) * NC * CF * pow(omx, -1)
                - 2 * pow(ln(omz), 2) * NC * CF * pow(omz, -1)
                + 11.0 / 2.0 * pow(ln(omz), 2) * NC * CF
                - 2 * pow(ln(omz), 2) * NC * z * CF * pow(omx, -1)
                + 1.0 / 2.0 * pow(ln(omz), 2) * NC * z * CF
                - 2 * pow(ln(omz), 2) * NC * x * CF * pow(omz, -1)
            )
            tmp += (
                +1.0 / 2.0 * pow(ln(omz), 2) * NC * x * CF
                + 11.0 / 2.0 * pow(ln(omz), 2) * NC * x * z * CF
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                - 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * CF
                - 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF
                - 18 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) * CF
                + 18 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1) * CF
            )
            tmp += (
                +3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                - 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                + 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * CF
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                - 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF
                + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF
                - 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
            )
            tmp += (
                -Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                + 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * CF
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * CF
                + 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF
                + 18 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) * CF
                - 18 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF
            )
            tmp += (
                +9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * CF
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF
                - 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF
                + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * CF * pow(omx, -1)
            )
            tmp += (
                +2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * CF
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF
                + 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * CF
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * CF
                + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * CF
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * CF
                - Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
            )
            tmp += (
                +2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF
                - 6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * z * CF
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                + 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * CF
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF
                + 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * z * pow(sqrtxz2, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                - 51.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF
                + 18 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) * CF
                - 18 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
            )
            tmp += (
                -9.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                + 9 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                - 3.0 / 4.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + 5.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * CF
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                + 3.0 / 8.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF
                - 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF
                + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                - 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                - 5.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
            )
            tmp += (
                +9.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(sqrtxz2, -1) * CF
                - 9 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * z * pow(sqrtxz2, -1) * CF
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, -1) * pow(sqrtxz2, -1) * CF
                - 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 51.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * CF
                - 18 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) * CF
                + 18 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                - 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) * pow(sqrtxz2, -1) * CF
                + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF * pow(omz, -1)
                + 9.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                - 9 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                + 3.0 / 4.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - 5.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * CF
                + Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF
                - 3.0 / 8.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) * CF
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(sqrtxz2, -1) * CF
                + 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * z * pow(sqrtxz2, -1) * CF
            )
            tmp += (
                -2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(sqrtxz2, -1) * CF
                + 16 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * pow(sqrtxz2, -1) * CF
                - 16 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF
                - 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF
                + 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * z * CF
                - 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * CF
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * pow(z, 2) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * CF * pow(omx, -1)
            )
            tmp += (
                +2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * CF
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * CF
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * z * CF
                + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(omx, -1)
                + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                - 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF
                + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                - 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * CF
                - 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * pow(z, 2) * CF
                + 8 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 8 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF
                - 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 6 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(1 - x * pow(z, -1)) * pow(NC, -1) * CF * pow(omz, -1)
                + 4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * CF
                - 6 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 6 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                + 6 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                + Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * CF
                + 8 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * z * CF
                - Li2(1 - x * pow(z, -1)) * CF * pow(omx, -1)
            )
            tmp += (
                +2 * Li2(1 - x * pow(z, -1)) * z * CF * pow(omx, -1)
                + 2 * Li2(1 - x * pow(z, -1)) * x * CF
                - 4 * Li2(1 - x * pow(z, -1)) * x * z * CF
                + 2 * Li2(1 - x * pow(z, -1)) * NC * CF * pow(omx, -1) * pow(omz, -1)
                - Li2(1 - x * pow(z, -1)) * NC * CF * pow(omx, -1)
                - Li2(1 - x * pow(z, -1)) * NC * CF * pow(omz, -1)
                - Li2(1 - x * pow(z, -1)) * NC * z * CF * pow(omx, -1)
                - Li2(1 - x * pow(z, -1)) * NC * x * CF * pow(omz, -1)
                - Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * CF
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -2) * z * CF
                - Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * CF * pow(opx, -1)
                - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z * CF
                - Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                + Li2(-x * pow(z, -1)) * pow(x, -2) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
            )
            tmp += (
                -2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF
                - 4 * Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * Li2(-x * pow(z, -1)) * pow(x, -2) * pow(z, 2) * CF
                - Li2(-x * pow(z, -1)) * pow(x, -1) * CF
                + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF
                - 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * Li2(-x * pow(z, -1)) * CF * pow(omx, -1)
                - Li2(-x * pow(z, -1)) * CF * pow(opx, -1)
                + 2 * Li2(-x * pow(z, -1)) * CF
                - 4 * Li2(-x * pow(z, -1)) * z * CF * pow(omx, -1)
                + 2 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1)
                - 4 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * Li2(-x * pow(z, -1)) * x * z * CF
                + 2 * Li2(-x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                - 2 * Li2(-x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                - 4 * Li2(-x) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                + 4 * Li2(-x) * pow(NC, -1) * pow(x, -2) * CF
                + 4 * Li2(-x) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * Li2(-x) * pow(NC, -1) * pow(x, -2) * z * CF
                + 2 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                - 4 * Li2(-x) * pow(NC, -1) * pow(x, -1) * CF
                + 4 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 2 * Li2(-x) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                - 2 * Li2(-x) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * Li2(-x) * pow(NC, -1) * CF * pow(opx, -1)
                + 4 * Li2(-x) * pow(NC, -1) * CF
                - 2 * Li2(-x) * pow(NC, -1) * x * pow(z, -1) * CF
                + 4 * Li2(-x) * pow(NC, -1) * x * CF
                + 2 * Li2(-x) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * Li2(-x) * pow(x, -2) * CF
                - 4 * Li2(-x) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * Li2(-x) * pow(x, -2) * z * CF
            )
            tmp += (
                +8 * Li2(-x) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                - 8 * Li2(-x) * pow(x, -2) * pow(z, 2) * CF
                + 2 * Li2(-x) * pow(x, -1) * CF
                - 4 * Li2(-x) * pow(x, -1) * z * CF
                + 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * Li2(-x) * CF * pow(opx, -1)
                - 4 * Li2(-x) * CF
                + 4 * Li2(-x) * z * CF * pow(opx, -1)
                + 8 * Li2(-x) * z * CF
                - 4 * Li2(-x) * x * CF
                + 8 * Li2(-x) * x * z * CF
                - Li2(-x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + Li2(-x * z) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                - 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * CF
                - 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -2) * z * CF
                - Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * CF
                - 2 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 2 * Li2(-x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                - Li2(-x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                + 2 * Li2(-x * z) * pow(NC, -1) * pow(z, -1) * CF
                - 4 * Li2(-x * z) * pow(NC, -1) * CF * pow(omx, -1)
                + 2 * Li2(-x * z) * pow(NC, -1) * CF * pow(opx, -1)
                - 2 * Li2(-x * z) * pow(NC, -1) * z * CF * pow(omx, -1)
                - 2 * Li2(-x * z) * pow(NC, -1) * z * CF * pow(opx, -1)
                + 4 * Li2(-x * z) * pow(NC, -1) * x * CF
                - Li2(-x * z) * pow(x, -2) * CF * pow(opx, -1)
                + Li2(-x * z) * pow(x, -2) * CF
                + 2 * Li2(-x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                - 2 * Li2(-x * z) * pow(x, -2) * z * CF
                - 4 * Li2(-x * z) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 4 * Li2(-x * z) * pow(x, -2) * pow(z, 2) * CF
                - Li2(-x * z) * pow(x, -1) * CF
                + 2 * Li2(-x * z) * pow(x, -1) * z * CF
            )
            tmp += (
                -4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                + 2 * Li2(-x * z) * CF * pow(omx, -1)
                - Li2(-x * z) * CF * pow(opx, -1)
                + 4 * Li2(-x * z) * z * CF * pow(omx, -1)
                + 2 * Li2(-x * z) * z * CF * pow(opx, -1)
                - 4 * Li2(-x * z) * z * CF
                + 4 * Li2(-x * z) * pow(z, 2) * CF * pow(omx, -1)
                - 4 * Li2(-x * z) * pow(z, 2) * CF * pow(opx, -1)
                - 2 * Li2(-x * z) * x * CF
                - 8 * Li2(-x * z) * x * pow(z, 2) * CF
                - 2 * Li2(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF * pow(opx, -1)
                + 2 * Li2(x) * pow(NC, -1) * pow(x, -2) * pow(z, -1) * CF
                + 4 * Li2(x) * pow(NC, -1) * pow(x, -2) * CF * pow(opx, -1)
                - 4 * Li2(x) * pow(NC, -1) * pow(x, -2) * CF
                - 4 * Li2(x) * pow(NC, -1) * pow(x, -2) * z * CF * pow(opx, -1)
                + 4 * Li2(x) * pow(NC, -1) * pow(x, -2) * z * CF
                - 2 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF
                + 4 * Li2(x) * pow(NC, -1) * pow(x, -1) * CF
                - 4 * Li2(x) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1)
                - 8 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 8 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                + 4 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1)
                + 2 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1)
                - 4 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF
                + 12 * Li2(x) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                - 3 * Li2(x) * pow(NC, -1) * CF * pow(omx, -1)
                - 4 * Li2(x) * pow(NC, -1) * CF * pow(omz, -1)
                - 4 * Li2(x) * pow(NC, -1) * CF * pow(opx, -1)
                - Li2(x) * pow(NC, -1) * CF
                - 3 * Li2(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 4 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1)
                - 4 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * CF
                - 8 * Li2(x) * pow(NC, -1) * x * CF * pow(omz, -1)
                + 4 * Li2(x) * pow(NC, -1) * x * CF
                + 3 * Li2(x) * pow(NC, -1) * x * z * CF
            )
            tmp += (
                -2 * Li2(x) * pow(x, -2) * CF * pow(opx, -1)
                + 2 * Li2(x) * pow(x, -2) * CF
                + 4 * Li2(x) * pow(x, -2) * z * CF * pow(opx, -1)
                - 4 * Li2(x) * pow(x, -2) * z * CF
                - 8 * Li2(x) * pow(x, -2) * pow(z, 2) * CF * pow(opx, -1)
                + 8 * Li2(x) * pow(x, -2) * pow(z, 2) * CF
                - 2 * Li2(x) * pow(x, -1) * CF
                + 4 * Li2(x) * pow(x, -1) * z * CF
                - 8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                - Li2(x) * pow(z, -1) * CF
                + 3 * Li2(x) * CF * pow(omx, -1)
                + 2 * Li2(x) * CF * pow(opx, -1)
                + 2 * Li2(x) * CF
                - 6 * Li2(x) * z * CF * pow(omx, -1)
                - 4 * Li2(x) * z * CF * pow(opx, -1)
                + 8 * Li2(x) * pow(z, 2) * CF * pow(omx, -1)
                - Li2(x) * x * pow(z, -1) * CF
                + 4 * Li2(x) * x * z * CF
                - 8 * Li2(x) * x * pow(z, 2) * CF
                + Li2(x) * NC * CF
                + Li2(x) * NC * x * z * CF
                - 4 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1) * pow(omz, -1)
                + 5 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                + Li2(z) * pow(NC, -1) * CF * pow(omz, -1)
                - 5 * Li2(z) * pow(NC, -1) * CF
                + 5 * Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                + 3 * Li2(z) * pow(NC, -1) * x * CF * pow(omz, -1)
                - 2 * Li2(z) * pow(NC, -1) * x * CF
                - 7 * Li2(z) * pow(NC, -1) * x * z * CF
                + Li2(z) * CF * pow(omx, -1)
                + Li2(z) * CF
                - 2 * Li2(z) * z * CF * pow(omx, -1)
                - Li2(z) * x * CF
                + 6 * Li2(z) * x * z * CF
                + 3 * Li2(z) * NC * CF
                + 3 * Li2(z) * NC * x * z * CF
            )

            res += tmp

        return res


def c2tq2q_eq(x, z, rsl, order, f=C2Tq2qEq_DR0123_scheme):
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
