from configs.eh import *


def C2Pq2qbEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
    res = 0.0

    if cx == "D" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "0" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "1" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "2" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "D":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "0":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "1":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "2":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "3":

        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "D" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += (
                +(-1) * 107.0 / 108.0 * pow(z, -1) * CF
                + 1.0 / 4.0 * CF * pow(NC, -1)
                + 4.0 / 3.0 * CF * pow(NC, -1) * pow(rln2, 3) * pow(opz, -1)
                + (-1) * 2.0 / 3.0 * CF * pow(NC, -1) * pow(rln2, 3)
                + (-1) * 11.0 / 9.0 * CF
                + (-1) * 1.0 / 4.0 * z * CF * pow(NC, -1)
                + 2.0 / 3.0 * z * CF * pow(NC, -1) * pow(rln2, 3)
                + (-1) * 4.0 / 9.0 * z * CF
                + 287.0 / 108.0 * pow(z, 2) * CF
                + 2 * zeta3 * CF
                + 2 * zeta3 * z * CF
                + (-1) * 1.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
                + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * rln2 * pow(opz, -1)
                + 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * rln2
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * CF
                + (-1) * 1.0 / 12.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + (-1) * 1.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * rln2
                + (-1) * 1.0 / 4.0 * pow(pi, 2) * z * CF
                + (-1) * 2 * ln(1 + z) * CF * pow(NC, -1) * pow(rln2, 2) * pow(opz, -1)
                + ln(1 + z) * CF * pow(NC, -1) * pow(rln2, 2)
                + (-1) * ln(1 + z) * z * CF * pow(NC, -1) * pow(rln2, 2)
                + 1.0 / 3.0 * ln(1 + z) * pow(pi, 2) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 1.0 / 6.0 * ln(1 + z) * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 6.0 * ln(1 + z) * pow(pi, 2) * z * CF * pow(NC, -1)
                + (-1) * 7.0 / 18.0 * ln(z) * pow(z, -1) * CF
                + (-1) * 7.0 / 4.0 * ln(z) * CF * pow(NC, -1)
                + (-1) * 5 * ln(z) * CF
                + 0
            )
            res += (
                +1.0 / 4.0 * ln(z) * z * CF * pow(NC, -1)
                + (-1) * 9.0 / 2.0 * ln(z) * z * CF
                + (-1) * 31.0 / 18.0 * ln(z) * pow(z, 2) * CF
                + 1.0 / 6.0 * ln(z) * pow(pi, 2) * CF
                + 1.0 / 6.0 * ln(z) * pow(pi, 2) * z * CF
                + ln(z) * ln(1 + z) * CF * pow(NC, -1)
                + ln(z) * ln(1 + z) * z * CF * pow(NC, -1)
                + 1.0 / 3.0 * pow(ln(z), 2) * pow(z, -1) * CF
                + (-1) * pow(ln(z), 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 8.0 * pow(ln(z), 2) * CF
                + (-1) * pow(ln(z), 2) * z * CF * pow(NC, -1)
                + (-1) * 5.0 / 8.0 * pow(ln(z), 2) * z * CF
                + 3 * pow(ln(z), 2) * ln(1 + z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * ln(1 + z) * CF * pow(NC, -1)
                + 3.0 / 2.0 * pow(ln(z), 2) * ln(1 + z) * z * CF * pow(NC, -1)
                + (-1) * 5.0 / 6.0 * pow(ln(z), 3) * CF * pow(NC, -1) * pow(opz, -1)
                + 5.0 / 12.0 * pow(ln(z), 3) * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(z), 3) * CF
                + (-1) * 5.0 / 12.0 * pow(ln(z), 3) * z * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(z), 3) * z * CF
                + 4 * ln(z) * ln(omz) * ln(1 + z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 2 * ln(z) * ln(omz) * ln(1 + z) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(omz) * ln(1 + z) * z * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * CF
                + (-1) * 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * z * CF
                + 2 * ln(z) * Li2(-z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * ln(z) * Li2(-z) * CF * pow(NC, -1)
                + ln(z) * Li2(-z) * z * CF * pow(NC, -1)
                + 0
            )
            res += (
                +(-1) * 7.0 / 18.0 * ln(omz) * pow(z, -1) * CF
                + (-1) * 2 * ln(omz) * CF * pow(NC, -1)
                + (-1) * 2 * ln(omz) * CF * pow(NC, -1) * pow(rln2, 2) * pow(opz, -1)
                + ln(omz) * CF * pow(NC, -1) * pow(rln2, 2)
                + (-1) * 10.0 / 3.0 * ln(omz) * CF
                + 2 * ln(omz) * z * CF * pow(NC, -1)
                + (-1) * ln(omz) * z * CF * pow(NC, -1) * pow(rln2, 2)
                + 7.0 / 3.0 * ln(omz) * z * CF
                + 25.0 / 18.0 * ln(omz) * pow(z, 2) * CF
                + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 1.0 / 6.0 * ln(omz) * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * CF
                + 1.0 / 6.0 * ln(omz) * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omz) * pow(pi, 2) * z * CF
                + 4 * ln(omz) * ln(1 + z) * CF * pow(NC, -1) * rln2 * pow(opz, -1)
                + (-1) * 2 * ln(omz) * ln(1 + z) * CF * pow(NC, -1) * rln2
                + 2 * ln(omz) * ln(1 + z) * z * CF * pow(NC, -1) * rln2
                + (-1) * 2 * ln(omz) * pow(ln(1 + z), 2) * CF * pow(NC, -1) * pow(opz, -1)
                + ln(omz) * pow(ln(1 + z), 2) * CF * pow(NC, -1)
                + (-1) * ln(omz) * pow(ln(1 + z), 2) * z * CF * pow(NC, -1)
                + 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, -1) * CF
                + 1.0 / 4.0 * pow(ln(omz), 2) * CF
                + (-1) * 1.0 / 4.0 * pow(ln(omz), 2) * z * CF
                + (-1) * 1.0 / 3.0 * pow(ln(omz), 2) * pow(z, 2) * CF
                + (-1) * ln(omz) * Li2(1 - z) * CF
                + (-1) * ln(omz) * Li2(1 - z) * z * CF
                + 4 * ln(omz) * Li2(-z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 2 * ln(omz) * Li2(-z) * CF * pow(NC, -1)
                + 2 * ln(omz) * Li2(-z) * z * CF * pow(NC, -1)
                + (-1) * 2 * ln(omz) * Li2(z) * CF
                + (-1) * 2 * ln(omz) * Li2(z) * z * CF
                + 2.0 / 3.0 * ln(opz) * pow(pi, 2) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 1.0 / 3.0 * ln(opz) * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(opz) * pow(pi, 2) * z * CF * pow(NC, -1)
                + (-1) * 4 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(opz, -1)
                + 0
            )
            res += (
                +2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * CF * pow(NC, -1)
                + (-1) * 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                + (-1) * 4 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(opz, -1)
                + 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * CF * pow(NC, -1)
                + (-1) * 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                + 4 * Li3(1 - z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 2 * Li3(1 - z) * CF * pow(NC, -1)
                + (-1) * Li3(1 - z) * CF
                + 2 * Li3(1 - z) * z * CF * pow(NC, -1)
                + (-1) * Li3(1 - z) * z * CF
                + 2 * Li3(-z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * Li3(-z) * CF * pow(NC, -1)
                + Li3(-z) * z * CF * pow(NC, -1)
                + 4 * Li3(1 / (1 + z)) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 2 * Li3(1 / (1 + z)) * CF * pow(NC, -1)
                + 2 * Li3(1 / (1 + z)) * z * CF * pow(NC, -1)
                + (-1) * 4 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * CF * pow(NC, -1) * pow(opz, -1)
                + 2 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * CF * pow(NC, -1)
                + (-1) * 2 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * z * CF * pow(NC, -1)
                + 2 * Li3(z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * Li3(z) * CF * pow(NC, -1)
                + (-1) * 2 * Li3(z) * CF
                + Li3(z) * z * CF * pow(NC, -1)
                + (-1) * 2 * Li3(z) * z * CF
                + Li2(-z) * CF * pow(NC, -1)
                + Li2(-z) * z * CF * pow(NC, -1)
                + (-1) * 2.0 / 3.0 * Li2(z) * pow(z, -1) * CF
                + Li2(z) * CF * pow(NC, -1)
                + 1.0 / 2.0 * Li2(z) * CF
                + Li2(z) * z * CF * pow(NC, -1)
                + 2 * Li2(z) * z * CF
                + 2.0 / 3.0 * Li2(z) * pow(z, 2) * CF
                + 0
            )
        if "001" == order:
            res += (
                7.0 / 18.0 * pow(z, -1) * LMUA * CF
                + 2 * LMUA * CF * pow(NC, -1)
                + 10.0 / 3.0 * LMUA * CF
                + (-1) * 2 * z * LMUA * CF * pow(NC, -1)
                + (-1) * 7.0 / 3.0 * z * LMUA * CF
                + (-1) * 25.0 / 18.0 * pow(z, 2) * LMUA * CF
                + (-1) * 1.0 / 3.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1) * pow(opz, -1)
                + 1.0 / 6.0 * pow(pi, 2) * LMUA * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUA * CF
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * z * LMUA * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * z * LMUA * CF
                + (-1) * 2.0 / 3.0 * ln(z) * pow(z, -1) * LMUA * CF
                + ln(z) * LMUA * CF * pow(NC, -1)
                + 1.0 / 2.0 * ln(z) * LMUA * CF
                + 0
            )
            res += (
                ln(z) * z * LMUA * CF * pow(NC, -1)
                + 2 * ln(z) * z * LMUA * CF
                + 2.0 / 3.0 * ln(z) * pow(z, 2) * LMUA * CF
                + (-1) * 4 * ln(z) * ln(1 + z) * LMUA * CF * pow(NC, -1) * pow(opz, -1)
                + 2 * ln(z) * ln(1 + z) * LMUA * CF * pow(NC, -1)
                + (-1) * 2 * ln(z) * ln(1 + z) * z * LMUA * CF * pow(NC, -1)
                + pow(ln(z), 2) * LMUA * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * LMUA * CF * pow(NC, -1)
                + (-1) * pow(ln(z), 2) * LMUA * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * z * LMUA * CF * pow(NC, -1)
                + (-1) * pow(ln(z), 2) * z * LMUA * CF
                + 0
            )
            res += (-1) * 2.0 / 3.0 * ln(omz) * pow(z, -1) * LMUA * CF + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * CF + 1.0 / 2.0 * ln(omz) * z * LMUA * CF + 2.0 / 3.0 * ln(omz) * pow(z, 2) * LMUA * CF + 0
            res += (-1) * 4 * Li2(-z) * LMUA * CF * pow(NC, -1) * pow(opz, -1) + 2 * Li2(-z) * LMUA * CF * pow(NC, -1) + (-1) * 2 * Li2(-z) * z * LMUA * CF * pow(NC, -1) + Li2(z) * LMUA * CF + Li2(z) * z * LMUA * CF + 0
        if "002" == order:
            res += 1.0 / 3.0 * pow(z, -1) * pow(LMUA, 2) * CF + 1.0 / 4.0 * pow(LMUA, 2) * CF + (-1) * 1.0 / 4.0 * z * pow(LMUA, 2) * CF + (-1) * 1.0 / 3.0 * pow(z, 2) * pow(LMUA, 2) * CF + 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * CF + 0
            res += 1.0 / 2.0 * ln(z) * z * pow(LMUA, 2) * CF + 0
        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += (
                +(-1) * 7.0 / 18.0 * pow(z, -1) * CF
                + (-1) * 2 * CF * pow(NC, -1)
                + (-1) * 10.0 / 3.0 * CF
                + 2 * z * CF * pow(NC, -1)
                + 7.0 / 3.0 * z * CF
                + 25.0 / 18.0 * pow(z, 2) * CF
                + 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * CF
                + 1.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * z * CF
                + 2.0 / 3.0 * ln(z) * pow(z, -1) * CF
                + (-1) * ln(z) * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * ln(z) * CF
                + (-1) * ln(z) * z * CF * pow(NC, -1)
                + (-1) * 2 * ln(z) * z * CF
                + (-1) * 2.0 / 3.0 * ln(z) * pow(z, 2) * CF
                + 4 * ln(z) * ln(1 + z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 2 * ln(z) * ln(1 + z) * CF * pow(NC, -1)
                + 2 * ln(z) * ln(1 + z) * z * CF * pow(NC, -1)
                + (-1) * pow(ln(z), 2) * CF * pow(NC, -1) * pow(opz, -1)
                + 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1)
                + pow(ln(z), 2) * CF
                + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                + pow(ln(z), 2) * z * CF
                + 2.0 / 3.0 * ln(omz) * pow(z, -1) * CF
                + 1.0 / 2.0 * ln(omz) * CF
                + (-1) * 1.0 / 2.0 * ln(omz) * z * CF
                + (-1) * 2.0 / 3.0 * ln(omz) * pow(z, 2) * CF
                + 4 * Li2(-z) * CF * pow(NC, -1) * pow(opz, -1)
                + (-1) * 2 * Li2(-z) * CF * pow(NC, -1)
                + 2 * Li2(-z) * z * CF * pow(NC, -1)
                + (-1) * Li2(z) * CF
                + (-1) * Li2(z) * z * CF
                + 0
            )
        if "001" == order:
            res += (-1) * 2.0 / 3.0 * pow(z, -1) * LMUA * CF + (-1) * 1.0 / 2.0 * LMUA * CF + 1.0 / 2.0 * z * LMUA * CF + 2.0 / 3.0 * pow(z, 2) * LMUA * CF + (-1) * ln(z) * LMUA * CF + (-1) * ln(z) * z * LMUA * CF + 0
        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 2.0 / 3.0 * pow(z, -1) * CF + 1.0 / 2.0 * CF + (-1) * 1.0 / 2.0 * z * CF + (-1) * 2.0 / 3.0 * pow(z, 2) * CF + ln(z) * CF + ln(z) * z * CF + 0
        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "3" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "D":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += (
                +(-1) * 13.0 / 4.0 * CF * pow(NC, -1)
                + (-1) * 4.0 / 3.0 * CF * pow(NC, -1) * pow(rln2, 3) * pow(opx, -1)
                + 2.0 / 3.0 * CF * pow(NC, -1) * pow(rln2, 3)
                + 9 * CF
                + 13.0 / 4.0 * x * CF * pow(NC, -1)
                + (-1) * 2.0 / 3.0 * x * CF * pow(NC, -1) * pow(rln2, 3)
                + (-1) * 9 * x * CF
                + (-1) * 2 * zeta3 * CF * pow(NC, -1) * pow(opx, -1)
                + zeta3 * CF * pow(NC, -1)
                + (-1) * zeta3 * x * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(pi, 2) * CF * pow(NC, -1)
                + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * rln2 * pow(opx, -1)
                + (-1) * 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * rln2
                + (-1) * 1.0 / 2.0 * pow(pi, 2) * CF
                + 5.0 / 12.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                + 1.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1) * rln2
                + 1.0 / 2.0 * pow(pi, 2) * x * CF
                + 2 * ln(1 + x) * CF * pow(NC, -1) * pow(rln2, 2) * pow(opx, -1)
                + (-1) * ln(1 + x) * CF * pow(NC, -1) * pow(rln2, 2)
                + ln(1 + x) * x * CF * pow(NC, -1) * pow(rln2, 2)
                + 1.0 / 3.0 * ln(1 + x) * pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 1.0 / 6.0 * ln(1 + x) * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 6.0 * ln(1 + x) * pow(pi, 2) * x * CF * pow(NC, -1)
                + (-1) * 2.0 / 3.0 * pow(ln(1 + x), 3) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 3.0 * pow(ln(1 + x), 3) * CF * pow(NC, -1)
                + (-1) * 1.0 / 3.0 * pow(ln(1 + x), 3) * x * CF * pow(NC, -1)
                + (-1) * 9.0 / 4.0 * ln(x) * CF * pow(NC, -1)
                + 25.0 / 4.0 * ln(x) * CF
                + 7.0 / 4.0 * ln(x) * x * CF * pow(NC, -1)
                + (-1) * 3.0 / 4.0 * ln(x) * x * CF
                + 0
            )
            res += (
                +2.0 / 3.0 * ln(x) * pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 3.0 * ln(x) * pow(pi, 2) * CF
                + 1.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF * pow(NC, -1)
                + (-1) * 1.0 / 3.0 * ln(x) * pow(pi, 2) * x * CF
                + 3 * ln(x) * ln(1 + x) * CF * pow(NC, -1)
                + 3 * ln(x) * ln(1 + x) * x * CF * pow(NC, -1)
                + (-1) * pow(ln(x), 2) * CF * pow(NC, -1)
                + 17.0 / 8.0 * pow(ln(x), 2) * CF
                + (-1) * 2 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                + (-1) * 15.0 / 8.0 * pow(ln(x), 2) * x * CF
                + 4 * pow(ln(x), 2) * ln(1 + x) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 2 * pow(ln(x), 2) * ln(1 + x) * CF * pow(NC, -1)
                + 2 * pow(ln(x), 2) * ln(1 + x) * x * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(x), 3) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 4.0 * pow(ln(x), 3) * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(x), 3) * CF
                + (-1) * 1.0 / 4.0 * pow(ln(x), 3) * x * CF * pow(NC, -1)
                + 5.0 / 12.0 * pow(ln(x), 3) * x * CF
                + (-1) * 5.0 / 2.0 * ln(x) * ln(omx) * CF
                + 5.0 / 2.0 * ln(x) * ln(omx) * x * CF
                + (-1) * 4 * ln(x) * ln(omx) * ln(1 + x) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(omx) * ln(1 + x) * CF * pow(NC, -1)
                + (-1) * 2 * ln(x) * ln(omx) * ln(1 + x) * x * CF * pow(NC, -1)
                + (-1) * 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * CF
                + (-1) * 3.0 / 2.0 * ln(x) * pow(ln(omx), 2) * x * CF
                + 4 * ln(x) * Li2(-x) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 2 * ln(x) * Li2(-x) * CF * pow(NC, -1)
                + 0
            )
            res += (
                +2 * ln(x) * Li2(-x) * x * CF * pow(NC, -1)
                + ln(x) * Li2(x) * CF
                + ln(x) * Li2(x) * x * CF
                + 2 * ln(omx) * CF * pow(NC, -1)
                + 2 * ln(omx) * CF * pow(NC, -1) * pow(rln2, 2) * pow(opx, -1)
                + (-1) * ln(omx) * CF * pow(NC, -1) * pow(rln2, 2)
                + (-1) * 3 * ln(omx) * CF
                + (-1) * 2 * ln(omx) * x * CF * pow(NC, -1)
                + ln(omx) * x * CF * pow(NC, -1) * pow(rln2, 2)
                + 3 * ln(omx) * x * CF
                + (-1) * 1.0 / 3.0 * ln(omx) * pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 6.0 * ln(omx) * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * CF
                + (-1) * 1.0 / 6.0 * ln(omx) * pow(pi, 2) * x * CF * pow(NC, -1)
                + 1.0 / 3.0 * ln(omx) * pow(pi, 2) * x * CF
                + (-1) * 4 * ln(omx) * ln(1 + x) * CF * pow(NC, -1) * rln2 * pow(opx, -1)
                + 2 * ln(omx) * ln(1 + x) * CF * pow(NC, -1) * rln2
                + (-1) * 2 * ln(omx) * ln(1 + x) * x * CF * pow(NC, -1) * rln2
                + 2 * ln(omx) * pow(ln(1 + x), 2) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * ln(omx) * pow(ln(1 + x), 2) * CF * pow(NC, -1)
                + ln(omx) * pow(ln(1 + x), 2) * x * CF * pow(NC, -1)
                + 5.0 / 4.0 * pow(ln(omx), 2) * CF
                + (-1) * 5.0 / 4.0 * pow(ln(omx), 2) * x * CF
                + (-1) * ln(omx) * Li2(1 - x) * CF
                + (-1) * ln(omx) * Li2(1 - x) * x * CF
                + (-1) * 4 * ln(omx) * Li2(-x) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(omx) * Li2(-x) * CF * pow(NC, -1)
                + (-1) * 2 * ln(omx) * Li2(-x) * x * CF * pow(NC, -1)
                + (-1) * 2 * ln(omx) * Li2(x) * CF
                + (-1) * 2 * ln(omx) * Li2(x) * x * CF
                + (-1) * ln(opx) * pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * ln(opx) * pow(pi, 2) * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * ln(opx) * pow(pi, 2) * x * CF * pow(NC, -1)
                + 4 * Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * CF * pow(NC, -1)
                + 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * x) * x * CF * pow(NC, -1)
                + 4 * Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * CF * pow(NC, -1) * pow(opx, -1)
                + 0
            )
            res += (
                +(-1) * 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * CF * pow(NC, -1)
                + 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * x) * x * CF * pow(NC, -1)
                + (-1) * 4 * Li3(1 - x) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * Li3(1 - x) * CF * pow(NC, -1)
                + (-1) * Li3(1 - x) * CF
                + (-1) * 2 * Li3(1 - x) * x * CF * pow(NC, -1)
                + (-1) * Li3(1 - x) * x * CF
                + 4 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 2 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * CF * pow(NC, -1)
                + 2 * Li3(1 / (1 + x) - 1 / (1 + x) * x) * x * CF * pow(NC, -1)
                + (-1) * 2 * Li3(x) * CF * pow(NC, -1) * pow(opx, -1)
                + Li3(x) * CF * pow(NC, -1)
                + (-1) * Li3(x) * x * CF * pow(NC, -1)
                + 3 * Li2(-x) * CF * pow(NC, -1)
                + 3 * Li2(-x) * x * CF * pow(NC, -1)
                + (-1) * Li2(x) * CF * pow(NC, -1)
                + 1.0 / 2.0 * Li2(x) * CF
                + (-1) * Li2(x) * x * CF * pow(NC, -1)
                + (-1) * 1.0 / 2.0 * Li2(x) * x * CF
                + 0
            )
        if "010" == order:
            res += (
                (-1) * 2 * LMUF * CF * pow(NC, -1)
                + 3 * LMUF * CF
                + 2 * x * LMUF * CF * pow(NC, -1)
                + (-1) * 3 * x * LMUF * CF
                + 1.0 / 3.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUF * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * LMUF * CF
                + 1.0 / 6.0 * pow(pi, 2) * x * LMUF * CF * pow(NC, -1)
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * LMUF * CF
                + (-1) * ln(x) * LMUF * CF * pow(NC, -1)
                + 3 * ln(x) * LMUF * CF
                + (-1) * ln(x) * x * LMUF * CF * pow(NC, -1)
                + 0
            )
            res += (
                (-1) * 3 * ln(x) * x * LMUF * CF
                + 4 * ln(x) * ln(1 + x) * LMUF * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 2 * ln(x) * ln(1 + x) * LMUF * CF * pow(NC, -1)
                + 2 * ln(x) * ln(1 + x) * x * LMUF * CF * pow(NC, -1)
                + (-1) * pow(ln(x), 2) * LMUF * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 2.0 * pow(ln(x), 2) * LMUF * CF * pow(NC, -1)
                + pow(ln(x), 2) * LMUF * CF
                + (-1) * 1.0 / 2.0 * pow(ln(x), 2) * x * LMUF * CF * pow(NC, -1)
                + pow(ln(x), 2) * x * LMUF * CF
                + 0
            )
            res += (-1) * 5.0 / 2.0 * ln(omx) * LMUF * CF + 5.0 / 2.0 * ln(omx) * x * LMUF * CF + 0
            res += 4 * Li2(-x) * LMUF * CF * pow(NC, -1) * pow(opx, -1) + (-1) * 2 * Li2(-x) * LMUF * CF * pow(NC, -1) + 2 * Li2(-x) * x * LMUF * CF * pow(NC, -1) + Li2(x) * LMUF * CF + Li2(x) * x * LMUF * CF + 0
        if "020" == order:
            res += 5.0 / 4.0 * pow(LMUF, 2) * CF + (-1) * 5.0 / 4.0 * x * pow(LMUF, 2) * CF + 1.0 / 2.0 * ln(x) * pow(LMUF, 2) * CF + 0
            res += 1.0 / 2.0 * ln(x) * x * pow(LMUF, 2) * CF + 0
        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += (
                2 * CF * pow(NC, -1)
                + (-1) * 3 * CF
                + (-1) * 2 * x * CF * pow(NC, -1)
                + 3 * x * CF
                + (-1) * 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                + 1.0 / 6.0 * pow(pi, 2) * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * CF
                + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                + 1.0 / 6.0 * pow(pi, 2) * x * CF
                + ln(x) * CF * pow(NC, -1)
                + (-1) * 3 * ln(x) * CF
                + ln(x) * x * CF * pow(NC, -1)
                + 3 * ln(x) * x * CF
                + (-1) * 4 * ln(x) * ln(1 + x) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * ln(x) * ln(1 + x) * CF * pow(NC, -1)
                + (-1) * 2 * ln(x) * ln(1 + x) * x * CF * pow(NC, -1)
                + pow(ln(x), 2) * CF * pow(NC, -1) * pow(opx, -1)
                + (-1) * 1.0 / 2.0 * pow(ln(x), 2) * CF * pow(NC, -1)
                + (-1) * pow(ln(x), 2) * CF
                + 1.0 / 2.0 * pow(ln(x), 2) * x * CF * pow(NC, -1)
                + (-1) * pow(ln(x), 2) * x * CF
                + 5.0 / 2.0 * ln(omx) * CF
                + (-1) * 5.0 / 2.0 * ln(omx) * x * CF
                + (-1) * 4 * Li2(-x) * CF * pow(NC, -1) * pow(opx, -1)
                + 2 * Li2(-x) * CF * pow(NC, -1)
                + (-1) * 2 * Li2(-x) * x * CF * pow(NC, -1)
                + (-1) * Li2(x) * CF
                + (-1) * Li2(x) * x * CF
                + 0
            )
        if "010" == order:
            res += (-1) * 5.0 / 2.0 * LMUF * CF + 5.0 / 2.0 * x * LMUF * CF + (-1) * ln(x) * LMUF * CF + (-1) * ln(x) * x * LMUF * CF + 0
        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 5.0 / 2.0 * CF + (-1) * 5.0 / 2.0 * x * CF + ln(x) * CF + ln(x) * x * CF + 0
        return res

    if cx == "R" and cz == "2":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "3":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
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
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += 0 + 0
            res += tmp

        if round(z, ndecimals) != round(x, ndecimals) and round(z, ndecimals) != round(1.0 - x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    4 * pow(z, -1) * CF * pow(NC, -1)
                    + 8 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                    + (-1) * 8 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2) * pow(opz, -1)
                    + 8 * pow(z, -1) * CF * pow(NC, -1) * pow(rln2, 2)
                    + 16 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 16 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + (-1) * 16 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 16 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + 12 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(rln2, 2) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 12 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(rln2, 2) * pow(omx, -1)
                    + (-1) * 12 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(rln2, 2) * pow(opz, -1)
                    + 12 * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(rln2, 2)
                    + (-1) * 113.0 / 36.0 * pow(z, -1) * CF
                    + (-1) * 16 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 32 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + 16 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 32 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 12 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(omx, -1) * pow(opz, -1)
                    + 24 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(omx, -1)
                    + 12 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 24 * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + (-1) * 12 * CF * pow(NC, -1)
                    + 6 * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                    + (-1) * 8 * CF * pow(NC, -1) * pow(rln2, 2)
                    + (-1) * 2 * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + 17.0 / 3.0 * CF
                    + (-1) * 6 * CF * pow(rln2, 2) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +4 * CF * pow(rln2, 2)
                    + (-1) * 6 * CF * sqrtxz1 * rln2 * pow(omx, -1)
                    + 4 * CF * sqrtxz1 * rln2
                    + (-1) * 16 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 16 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + 16 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 12 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(omx, -1) * pow(opz, -1)
                    + 12 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(omx, -1)
                    + 12 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 12 * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + 2 * z * CF * pow(NC, -1)
                    + (-1) * 6 * z * CF * pow(NC, -1) * pow(rln2, 2) * pow(omx, -1)
                    + 8 * z * CF * pow(NC, -1) * pow(rln2, 2)
                    + 85.0 / 12.0 * z * CF
                    + (-1) * 4 * z * CF * pow(rln2, 2) * pow(omx, -1)
                    + (-1) * 65.0 / 18.0 * pow(z, 2) * CF
                    + (-1) * 16 * pow(z, 2) * CF * pow(rln2, 2) * pow(omx, -1)
                    + 16 * pow(z, 2) * CF * pow(rln2, 2)
                    + (-1) * 7.0 / 2.0 * x * pow(z, -1) * CF * pow(NC, -1)
                    + 127.0 / 36.0 * x * pow(z, -1) * CF
                    + 64 * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 64 * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + 48 * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2) * pow(opz, -1)
                    + (-1) * 48 * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(rln2, 2)
                    + 11 * x * CF * pow(NC, -1)
                    + (-1) * 25.0 / 3.0 * x * CF
                    + (-1) * 3.0 / 2.0 * x * z * CF * pow(NC, -1)
                    + (-1) * 47.0 / 12.0 * x * z * CF
                    + 8 * x * z * CF * pow(rln2, 2)
                    + 31.0 / 18.0 * x * pow(z, 2) * CF
                    + 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 3.0 * pow(pi, 2) * pow(x, -2) * CF
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -2) * z * CF
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF * pow(NC, -1)
                    + 1.0 / 3.0 * pow(pi, 2) * pow(x, -1) * CF
                    + 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(x, -1) * z * CF
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * pow(x, -1) * pow(z, 2) * CF
                    + 1.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 1.0 / 2.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 1.0 / 6.0 * pow(pi, 2) * pow(z, -1) * CF
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 1.0 / 2.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(pi, 2) * CF * pow(NC, -1) * pow(opx, -1)
                    + 1.0 / 3.0 * pow(pi, 2) * CF * pow(NC, -1)
                    + 5.0 / 6.0 * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * CF * pow(opx, -1)
                    + (-1) * 5.0 / 6.0 * pow(pi, 2) * CF
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 1.0 / 6.0 * pow(pi, 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + pow(pi, 2) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * z * CF * pow(NC, -1)
                    + (-1) * 5.0 / 3.0 * pow(pi, 2) * z * CF * pow(omx, -1)
                    + 4.0 / 3.0 * pow(pi, 2) * z * CF * pow(opx, -1)
                    + 1.0 / 3.0 * pow(pi, 2) * z * CF
                    + 2 * pow(pi, 2) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(pi, 2) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4.0 / 3.0 * pow(pi, 2) * pow(z, 2) * CF
                    + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 1.0 / 6.0 * pow(pi, 2) * x * pow(z, -1) * CF
                    + 8.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2.0 / 3.0 * pow(pi, 2) * x * CF * pow(NC, -1)
                    + (-1) * 1.0 / 6.0 * pow(pi, 2) * x * CF
                    + (-1) * 2.0 / 3.0 * pow(pi, 2) * x * z * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 8 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + 16 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 32 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * rln2
                    + 2 * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * CF * rln2 * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(1 + sqrtxz1 - z) * CF * rln2
                    + 6 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1 * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * CF * sqrtxz1
                    + 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + 6 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * rln2
                    + 4 * ln(1 + sqrtxz1 - z) * z * CF * rln2
                    + 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + (-1) * 24 * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * rln2
                    + (-1) * 64 * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 64 * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 64 * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 64 * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + 2 * ln(1 + sqrtxz1 - z) * x * CF * rln2
                    + (-1) * 12 * ln(1 + sqrtxz1 - z) * x * z * CF * rln2
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF * pow(omx, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * CF
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF * pow(omx, -1)
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * z * CF
                    + (-1) * 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(z, 2) * CF
                    + 16 * pow(ln(1 + sqrtxz1 - z), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * pow(ln(1 + sqrtxz1 - z), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * x * CF
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 6 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * z * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                    + 32 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * CF
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + 8 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +16 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 6 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * rln2
                    + 4 * ln(1 + sqrtxz1 + z) * CF * rln2 * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * CF * rln2
                    + 8 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 8 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + 6 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * rln2
                    + 8 * ln(1 + sqrtxz1 + z) * z * CF * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * z * CF * rln2
                    + 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + (-1) * 8 * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * rln2
                    + (-1) * 32 * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + 32 * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * x * CF * rln2
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * x * z * CF * rln2
                    + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 8 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * sqrtxz3
                    + 4 * ln(x) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * pow(x, -2) * CF
                    + (-1) * 8 * ln(x) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 8 * ln(x) * pow(x, -2) * z * CF
                    + (-1) * 8 * ln(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 8 * ln(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 8 * ln(x) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(x, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * pow(x, -1) * CF
                    + 8 * ln(x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 8 * ln(x) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 8 * ln(x) * pow(x, -1) * z * CF
                    + (-1) * 16 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +16 * ln(x) * pow(x, -1) * pow(z, 2) * CF
                    + 3.0 / 2.0 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 9 * ln(x) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(opz, -1)
                    + 4 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + 8 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 8 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(x) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4.0 / 3.0 * ln(x) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 7.0 / 3.0 * ln(x) * pow(z, -1) * CF
                    + (-1) * 8 * ln(x) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 16 * ln(x) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * ln(x) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(x) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(x) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 8 * ln(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + 8 * ln(x) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * CF * pow(NC, -1)
                    + 3 * ln(x) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(x) * CF * pow(NC, -1) * rln2
                    + (-1) * ln(x) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + ln(x) * CF * pow(poly2, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(x) * CF * pow(opx, -1)
                    + 19.0 / 2.0 * ln(x) * CF
                    + (-1) * 5 * ln(x) * CF * rln2 * pow(omx, -1)
                    + 4 * ln(x) * CF * rln2
                    + (-1) * 3 * ln(x) * CF * sqrtxz1 * pow(omx, -1)
                    + 2 * ln(x) * CF * sqrtxz1
                    + 0
                )
                tmp += (
                    +(-1) * 8 * ln(x) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(x) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * ln(x) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * ln(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * ln(x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 3 * ln(x) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 4 * ln(x) * z * CF * pow(NC, -1) * rln2
                    + (-1) * 1.0 / 2.0 * ln(x) * z * CF * pow(omx, -1)
                    + 8 * ln(x) * z * CF * pow(opx, -1)
                    + ln(x) * z * CF
                    + 2 * ln(x) * z * CF * rln2 * pow(omx, -1)
                    + (-1) * 4 * ln(x) * z * CF * rln2
                    + 4.0 / 3.0 * ln(x) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 16 * ln(x) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8.0 / 3.0 * ln(x) * pow(z, 2) * CF
                    + (-1) * 16 * ln(x) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + 16 * ln(x) * pow(z, 2) * CF * rln2
                    + ln(x) * x * pow(z, -1) * CF * pow(NC, -1)
                    + 11.0 / 3.0 * ln(x) * x * pow(z, -1) * CF
                    + 32 * ln(x) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(x) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(x) * x * CF * pow(NC, -1)
                    + (-1) * ln(x) * x * CF * pow(poly2, -1)
                    + ln(x) * x * CF * pow(xmz, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * x * CF
                    + (-1) * 2 * ln(x) * x * CF * rln2
                    + (-1) * 3 * ln(x) * x * z * CF
                    + 8 * ln(x) * x * z * CF * rln2
                    + 4.0 / 3.0 * ln(x) * x * pow(z, 2) * CF
                    + (-1) * ln(x) * pow(x, 2) * CF * pow(poly2, -1)
                    + (-1) * 2 * ln(x) * pow(x, 2) * CF * pow(xmz, -1)
                    + ln(x) * pow(x, 3) * CF * pow(poly2, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                    + 3 * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                    + (-1) * 6 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1)
                    + (-1) * 3 * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1)
                    + 6 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1)
                    + ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * CF
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * z * CF
                    + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                    + 16 * ln(x) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(x) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * x * CF
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +8 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 3 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                    + 3 * ln(x) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * CF
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 3 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                    + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                    + (-1) * 16 * ln(x) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(x) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 + z) * x * z * CF
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                    + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                    + ln(x) * ln(1 + x * pow(z, -1)) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF
                    + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                    + (-1) * ln(x) * ln(1 + x * pow(z, -1)) * x * CF
                    + 2 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF
                    + 4 * ln(x) * ln(1 + x) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x) * CF * pow(opx, -1)
                    + 6 * ln(x) * ln(1 + x) * CF
                    + 4 * ln(x) * ln(1 + x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x) * z * CF * pow(NC, -1)
                    + 8 * ln(x) * ln(1 + x) * z * CF * pow(opx, -1)
                    + (-1) * 12 * ln(x) * ln(1 + x) * z * CF
                    + (-1) * 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF * pow(opx, -1)
                    + 8 * ln(x) * ln(1 + x) * pow(z, 2) * CF
                    + 4 * ln(x) * ln(1 + x) * x * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(1 + x) * x * CF
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(x) * ln(1 + x) * x * z * CF
                    + (-1) * ln(x) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                    + ln(x) * ln(1 + x * z) * pow(x, -2) * CF
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -2) * z * CF
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * pow(x, -1) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF
                    + 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x * z) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(1 + x * z) * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * CF
                    + (-1) * 2 * ln(x) * ln(1 + x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(1 + x * z) * z * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF
                    + 4 * ln(x) * ln(1 + x * z) * x * z * CF
                    + (-1) * 2 * ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(x) * ln(z + x) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(z + x) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(z + x) * CF
                    + 2 * ln(x) * ln(z + x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * z * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(z + x) * z * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z + x) * z * CF
                    + 4 * ln(x) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(z + x) * pow(z, 2) * CF
                    + (-1) * ln(x) * ln(z + x) * x * CF
                    + (-1) * 2 * ln(x) * ln(z + x) * x * z * CF
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF * pow(opx, -1)
                    + 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -2) * CF
                    + 3 * pow(ln(x), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -2) * z * CF
                    + 3 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(x), 2) * pow(x, -1) * CF
                    + (-1) * 3 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 3 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +3 * pow(ln(x), 2) * pow(x, -1) * z * CF
                    + 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 6 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF
                    + pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 3 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 3 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * pow(ln(x), 2) * pow(z, -1) * CF
                    + 3 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 6 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 3 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 6 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 3 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4 * pow(ln(x), 2) * CF * pow(NC, -1) * pow(opx, -1)
                    + pow(ln(x), 2) * CF * pow(NC, -1)
                    + 2 * pow(ln(x), 2) * CF * pow(omx, -1)
                    + 5.0 / 2.0 * pow(ln(x), 2) * CF * pow(opx, -1)
                    + (-1) * pow(ln(x), 2) * CF
                    + 3 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 3 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 3 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 3 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * pow(ln(x), 2) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * pow(ln(x), 2) * z * CF * pow(omx, -1)
                    + (-1) * 5 * pow(ln(x), 2) * z * CF * pow(opx, -1)
                    + 6 * pow(ln(x), 2) * z * CF
                    + 2 * pow(ln(x), 2) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * pow(ln(x), 2) * pow(z, 2) * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(x), 2) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * pow(ln(x), 2) * x * pow(z, -1) * CF
                    + (-1) * 12 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 12 * pow(ln(x), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * pow(ln(x), 2) * x * z * CF
                    + ln(x) * ln(z) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * ln(x) * ln(z) * pow(x, -2) * CF
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(z) * pow(x, -2) * z * CF
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(z) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -1) * CF * pow(NC, -1)
                    + ln(x) * ln(z) * pow(x, -1) * CF
                    + 2 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(x, -1) * z * CF
                    + (-1) * 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + ln(x) * ln(z) * pow(z, -1) * CF
                    + 2 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * ln(x) * ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(x) * ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * CF * pow(NC, -1)
                    + (-1) * 7 * ln(x) * ln(z) * CF * pow(omx, -1)
                    + ln(x) * ln(z) * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(z) * CF
                    + 2 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 2 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(z) * z * CF * pow(NC, -1)
                    + ln(x) * ln(z) * z * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(z) * z * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(z) * z * CF
                    + (-1) * 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(omx, -1)
                    + 4 * ln(x) * ln(z) * pow(z, 2) * CF
                    + ln(x) * ln(z) * x * pow(z, -1) * CF
                    + (-1) * 8 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + ln(x) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(x) * ln(z) * x * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(x) * ln(z) * x * z * CF
                    + (-1) * 2 * ln(x) * ln(omx) * pow(x, -2) * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * pow(x, -2) * CF
                    + 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -2) * z * CF
                    + 4 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * pow(x, -1) * CF
                    + (-1) * 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(omx) * pow(x, -1) * z * CF
                    + 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(x) * ln(omx) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * CF * pow(NC, -1)
                    + (-1) * 3 * ln(x) * ln(omx) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(omx) * CF * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * CF
                    + (-1) * 2 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(x) * ln(omx) * z * CF * pow(NC, -1)
                    + 6 * ln(x) * ln(omx) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(x) * ln(omx) * z * CF * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(omx) * z * CF
                    + (-1) * 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx, -1)
                    + 8 * ln(x) * ln(omx) * pow(z, 2) * CF
                    + ln(x) * ln(omx) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(x) * ln(omx) * x * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(x) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + ln(x) * ln(omz) * pow(z, -1) * CF
                    + (-1) * 4 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(x) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(omz) * CF
                    + (-1) * 4 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + ln(x) * ln(omz) * x * pow(z, -1) * CF
                    + 16 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(x) * ln(omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(x) * ln(omz) * x * CF
                    + 2 * ln(x) * ln(opx) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * pow(x, -2) * CF
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(opx) * pow(x, -2) * z * CF
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -1) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(opx) * pow(x, -1) * CF
                    + 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * pow(x, -1) * z * CF
                    + (-1) * 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 8 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 4 * ln(x) * ln(opx) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * ln(x) * ln(opx) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * ln(x) * ln(opx) * CF * pow(NC, -1)
                    + 2 * ln(x) * ln(opx) * CF * pow(opx, -1)
                    + (-1) * 2 * ln(x) * ln(opx) * CF
                    + 4 * ln(x) * ln(opx) * z * CF * pow(NC, -1)
                    + (-1) * 4 * ln(x) * ln(opx) * z * CF * pow(opx, -1)
                    + 4 * ln(x) * ln(opx) * z * CF
                    + (-1) * 8 * ln(x) * ln(opx) * pow(z, 2) * CF
                    + 2 * ln(x) * ln(opx) * x * CF
                    + (-1) * 4 * ln(x) * ln(opx) * x * z * CF
                    + 12 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 12 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 12 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2 * pow(opz, -1)
                    + 12 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * rln2
                    + 8 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 8 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + (-1) * 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 16 * ln(z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + 13.0 / 6.0 * ln(z) * pow(z, -1) * CF
                    + (-1) * 8 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 16 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 16 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 32 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + 16 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 32 * ln(z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + ln(z) * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(z) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3 * ln(z) * CF * pow(NC, -1)
                    + 9 * ln(z) * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + (-1) * 12 * ln(z) * CF * pow(NC, -1) * rln2
                    + (-1) * ln(z) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + ln(z) * CF * pow(poly2, -1)
                    + 3 * ln(z) * CF * pow(omx, -1)
                    + ln(z) * CF * pow(omz, -1)
                    + (-1) * 9 * ln(z) * CF
                    + (-1) * 7 * ln(z) * CF * rln2 * pow(omx, -1)
                    + 4 * ln(z) * CF * rln2
                    + (-1) * 3 * ln(z) * CF * sqrtxz1 * pow(omx, -1)
                    + 2 * ln(z) * CF * sqrtxz1
                    + (-1) * 8 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 16 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 16 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +16 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * ln(z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + ln(z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 9 * ln(z) * z * CF * pow(NC, -1) * rln2 * pow(omx, -1)
                    + 12 * ln(z) * z * CF * pow(NC, -1) * rln2
                    + 3 * ln(z) * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * ln(z) * z * CF
                    + (-1) * 10 * ln(z) * z * CF * rln2 * pow(omx, -1)
                    + 4 * ln(z) * z * CF * rln2
                    + 4.0 / 3.0 * ln(z) * pow(z, 2) * CF
                    + (-1) * 16 * ln(z) * pow(z, 2) * CF * rln2 * pow(omx, -1)
                    + 16 * ln(z) * pow(z, 2) * CF * rln2
                    + (-1) * 17.0 / 6.0 * ln(z) * x * pow(z, -1) * CF
                    + 32 * ln(z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * ln(z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 64 * ln(z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 64 * ln(z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * ln(z) * x * CF * pow(NC, -1) * pow(omz, -1)
                    + 3 * ln(z) * x * CF * pow(NC, -1)
                    + ln(z) * x * CF * pow(poly2, -1)
                    + (-1) * ln(z) * x * CF * pow(omz, -1)
                    + (-1) * ln(z) * x * CF * pow(xmz, -1)
                    + ln(z) * x * CF
                    + 2 * ln(z) * x * CF * rln2
                    + 3.0 / 2.0 * ln(z) * x * z * CF
                    + 8 * ln(z) * x * z * CF * rln2
                    + (-1) * 2.0 / 3.0 * ln(z) * x * pow(z, 2) * CF
                    + (-1) * ln(z) * pow(x, 2) * CF * pow(poly2, -1)
                    + 2 * ln(z) * pow(x, 2) * CF * pow(xmz, -1)
                    + (-1) * ln(z) * pow(x, 3) * CF * pow(poly2, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 3 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1)
                    + 3 * ln(z) * ln(1 + sqrtxz1 - z) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * CF
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 3 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + sqrtxz1 - z) * z * CF * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(z, 2) * CF
                    + (-1) * 32 * ln(z) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * ln(z) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(z) * ln(1 + sqrtxz1 - z) * x * z * CF
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 6 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(NC, -1)
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * CF
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +6 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(NC, -1)
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * z * CF
                    + 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(1 + sqrtxz1 + z) * pow(z, 2) * CF
                    + (-1) * 32 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 32 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * x * CF
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF
                    + (-1) * 4 * ln(z) * ln(1 + z) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(1 + z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -2) * z * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * CF
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF
                    + (-1) * 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(NC, -1)
                    + ln(z) * ln(1 + x * pow(z, -1)) * CF * pow(opx, -1)
                    + (-1) * ln(z) * ln(1 + x * pow(z, -1)) * CF
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF
                    + (-1) * 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF
                    + ln(z) * ln(1 + x * pow(z, -1)) * x * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF
                    + (-1) * ln(z) * ln(1 + x * z) * pow(x, -2) * CF * pow(opx, -1)
                    + ln(z) * ln(1 + x * z) * pow(x, -2) * CF
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -2) * z * CF
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * pow(x, -1) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +2 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF
                    + 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + x * z) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(1 + x * z) * CF * pow(opx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * CF
                    + (-1) * 2 * ln(z) * ln(1 + x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + x * z) * z * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF
                    + 4 * ln(z) * ln(1 + x * z) * x * z * CF
                    + 2 * ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2 * ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 2 * ln(z) * ln(z + x) * pow(z, -1) * CF * pow(NC, -1)
                    + 2 * ln(z) * ln(z + x) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(z + x) * CF * pow(NC, -1)
                    + (-1) * 2 * ln(z) * ln(z + x) * CF * pow(omx, -1)
                    + ln(z) * ln(z + x) * CF
                    + (-1) * 2 * ln(z) * ln(z + x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * ln(z) * ln(z + x) * z * CF * pow(NC, -1)
                    + (-1) * 4 * ln(z) * ln(z + x) * z * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(z + x) * z * CF
                    + (-1) * 4 * ln(z) * ln(z + x) * pow(z, 2) * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(z + x) * pow(z, 2) * CF
                    + 0
                )
                tmp += (
                    +ln(z) * ln(z + x) * x * CF
                    + 2 * ln(z) * ln(z + x) * x * z * CF
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -2) * CF
                    + (-1) * pow(ln(z), 2) * pow(x, -2) * z * CF * pow(opx, -1)
                    + pow(ln(z), 2) * pow(x, -2) * z * CF
                    + (-1) * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + pow(ln(z), 2) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(x, -1) * CF * pow(NC, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * pow(x, -1) * CF
                    + pow(ln(z), 2) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * pow(ln(z), 2) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * pow(ln(z), 2) * pow(x, -1) * z * CF
                    + (-1) * 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 2 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 3 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1)
                    + 5 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 5 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 5 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 5 * pow(ln(z), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 5 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 10 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +5 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 10 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * pow(ln(z), 2) * CF * pow(NC, -1)
                    + pow(ln(z), 2) * CF * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * CF * pow(opx, -1)
                    + (-1) * 3 * pow(ln(z), 2) * CF
                    + (-1) * 5 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 5 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 5 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 5 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 3 * pow(ln(z), 2) * z * CF * pow(NC, -1)
                    + (-1) * 2 * pow(ln(z), 2) * z * CF * pow(omx, -1)
                    + (-1) * pow(ln(z), 2) * z * CF * pow(opx, -1)
                    + 2 * pow(ln(z), 2) * z * CF
                    + 2 * pow(ln(z), 2) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * pow(ln(z), 2) * pow(z, 2) * CF
                    + 20 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 20 * pow(ln(z), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * pow(ln(z), 2) * x * z * CF
                    + (-1) * ln(z) * ln(omx) * CF
                    + (-1) * 2 * ln(z) * ln(omx) * z * CF
                    + (-1) * ln(z) * ln(omx) * x * CF
                    + 4 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * ln(z) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +4 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(z) * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * ln(z) * ln(omz) * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(omz) * CF
                    + (-1) * 4 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 2 * ln(z) * ln(omz) * z * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * z * CF
                    + 16 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(z) * ln(omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 8 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * sqrtxz3
                    + 13.0 / 6.0 * ln(omx) * pow(z, -1) * CF
                    + (-1) * 13.0 / 2.0 * ln(omx) * CF
                    + 1.0 / 2.0 * ln(omx) * z * CF
                    + 4.0 / 3.0 * ln(omx) * pow(z, 2) * CF
                    + (-1) * 17.0 / 6.0 * ln(omx) * x * pow(z, -1) * CF
                    + 9.0 / 2.0 * ln(omx) * x * CF
                    + 3.0 / 2.0 * ln(omx) * x * z * CF
                    + (-1) * 2.0 / 3.0 * ln(omx) * x * pow(z, 2) * CF
                    + 8 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2 * pow(opz, -1)
                    + 8 * ln(omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * rln2
                    + 13.0 / 6.0 * ln(omz) * pow(z, -1) * CF
                    + (-1) * 8 * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 16 * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + 8 * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 16 * ln(omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + (-1) * 13.0 / 2.0 * ln(omz) * CF
                    + (-1) * 8 * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +8 * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(omx, -1)
                    + 8 * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + 1.0 / 2.0 * ln(omz) * z * CF
                    + 4.0 / 3.0 * ln(omz) * pow(z, 2) * CF
                    + (-1) * 17.0 / 6.0 * ln(omz) * x * pow(z, -1) * CF
                    + 32 * ln(omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2 * pow(opz, -1)
                    + (-1) * 32 * ln(omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * rln2
                    + 9.0 / 2.0 * ln(omz) * x * CF
                    + 3.0 / 2.0 * ln(omz) * x * z * CF
                    + (-1) * 2.0 / 3.0 * ln(omz) * x * pow(z, 2) * CF
                    + (-1) * 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 16 * ln(omz) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(omz) * ln(1 + sqrtxz1 - z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(omz) * ln(1 + sqrtxz1 - z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 32 * ln(omz) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +32 * ln(omz) * ln(1 + sqrtxz1 - z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 16 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * pow(ln(omz), 2) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * pow(ln(omz), 2) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 16 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * pow(ln(omz), 2) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                    + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                    + (-1) * 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) - 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1)
                    + 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(x, -1) + 1.0 / 2.0 * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1)
                    + (-1) * 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                    + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(NC, -1)
                    + 6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * z * CF
                    + 16 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * x * CF
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                    + 6 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 3.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + (-1) * 1.0 / 2.0 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * CF * pow(sqrtxz2, -1)
                    + 3 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * CF * pow(sqrtxz2, -1)
                    + (-1) * 6 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * x * z * CF * pow(sqrtxz2, -1)
                    + (-1) * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + 3.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 2) * CF * pow(sqrtxz2, -1)
                    + 1.0 / 2.0 * Li2(1.0 / 2.0 + 1.0 / 2.0 * sqrtxz2 - 1.0 / 2.0 * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(NC, -1)
                    + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(z, 2) * CF
                    + (-1) * 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * x * z * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(NC, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 3 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * z * CF * pow(omx, -1)
                    + (-1) * 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(z, 2) * CF
                    + (-1) * 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + 16 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * x * z * CF
                    + Li2(1 - x * pow(z, -1)) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * CF
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * z * CF * pow(omx, -1)
                    + 4 * Li2(1 - x * pow(z, -1)) * z * CF
                    + 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * Li2(pow(sqrtxz1, -1) * omz) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 16 * Li2(pow(sqrtxz1, -1) * omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * Li2(pow(sqrtxz1, -1) * omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * Li2(pow(sqrtxz1, -1) * omz) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +8 * Li2(pow(sqrtxz1, -1) * omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * Li2(pow(sqrtxz1, -1) * omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(pow(sqrtxz1, -1) * omz) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 32 * Li2(pow(sqrtxz1, -1) * omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * Li2(pow(sqrtxz1, -1) * omz) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 16 * Li2(-sqrtxz1 * pow(omz, -1)) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * Li2(-sqrtxz1 * pow(omz, -1)) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 8 * Li2(-sqrtxz1 * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(-sqrtxz1 * pow(omz, -1)) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 32 * Li2(-sqrtxz1 * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 32 * Li2(-sqrtxz1 * pow(omz, -1)) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * Li2(-z) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 2 * Li2(-z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 2 * Li2(-z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(x, -2) * CF * pow(opx, -1)
                    + Li2(-x * pow(z, -1)) * pow(x, -2) * CF
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -2) * z * CF
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * Li2(-x * pow(z, -1)) * pow(x, -1) * CF
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF
                    + 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 2 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * Li2(-x * pow(z, -1)) * CF * pow(opx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * z * CF * pow(NC, -1)
                    + 4 * Li2(-x * pow(z, -1)) * z * CF * pow(omx, -1)
                    + 2 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(-x * pow(z, -1)) * z * CF
                    + 4 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(-x * pow(z, -1)) * x * CF
                    + 2 * Li2(-x) * pow(x, -2) * CF * pow(opx, -1)
                    + (-1) * 2 * Li2(-x) * pow(x, -2) * CF
                    + (-1) * 4 * Li2(-x) * pow(x, -2) * z * CF * pow(opx, -1)
                    + 4 * Li2(-x) * pow(x, -2) * z * CF
                    + (-1) * 4 * Li2(-x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + 4 * Li2(-x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * Li2(-x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(-x) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * pow(x, -1) * CF * pow(NC, -1)
                    + 2 * Li2(-x) * pow(x, -1) * CF
                    + 4 * Li2(-x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(-x) * pow(x, -1) * z * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(-x) * pow(x, -1) * z * CF
                    + (-1) * 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + 8 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 4 * Li2(-x) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + 4 * Li2(-x) * pow(z, -1) * CF * pow(NC, -1)
                    + 4 * Li2(-x) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(-x) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x) * CF * pow(opx, -1)
                    + 4 * Li2(-x) * CF
                    + 4 * Li2(-x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(-x) * z * CF * pow(opx, -1)
                    + (-1) * 8 * Li2(-x) * z * CF
                    + (-1) * 8 * Li2(-x) * pow(z, 2) * CF * pow(opx, -1)
                    + 4 * Li2(-x) * x * CF * pow(NC, -1)
                    + 0
                )
                tmp += (
                    +4 * Li2(-x) * x * CF
                    + (-1) * 8 * Li2(-x) * x * z * CF
                    + (-1) * Li2(-x * z) * pow(x, -2) * CF * pow(opx, -1)
                    + Li2(-x * z) * pow(x, -2) * CF
                    + 2 * Li2(-x * z) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(x, -2) * z * CF
                    + 2 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * Li2(-x * z) * pow(x, -1) * CF
                    + (-1) * 2 * Li2(-x * z) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 2 * Li2(-x * z) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 2 * Li2(-x * z) * pow(x, -1) * z * CF
                    + 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF
                    + 2 * Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1) * pow(opz, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 2 * Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 2 * Li2(-x * z) * pow(z, -1) * CF * pow(NC, -1) * pow(opz, -1)
                    + 2 * Li2(-x * z) * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(-x * z) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(-x * z) * CF * pow(omx, -1)
                    + (-1) * Li2(-x * z) * CF * pow(opx, -1)
                    + 2 * Li2(-x * z) * CF
                    + (-1) * 2 * Li2(-x * z) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(-x * z) * z * CF * pow(omx, -1)
                    + 2 * Li2(-x * z) * z * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(-x * z) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * Li2(-x * z) * pow(z, 2) * CF
                    + 4 * Li2(-x * z) * x * z * CF
                    + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1) * pow(opz, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(omx, -1)
                    + (-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1 * pow(opz, -1)
                    + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(z, -1) * CF * pow(NC, -1) * sqrtxz1
                    + (-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1) * pow(opz, -1)
                    + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(omx, -1)
                    + 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 4 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * z * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + 0
                )
                tmp += (
                    +16 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1) * pow(opz, -1)
                    + (-1) * 16 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * x * CF * pow(NC, -1) * pow(sqrtxz1, -1)
                    + (-1) * 2 * Li2(x) * pow(x, -2) * CF * pow(opx, -1)
                    + 2 * Li2(x) * pow(x, -2) * CF
                    + 4 * Li2(x) * pow(x, -2) * z * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(x) * pow(x, -2) * z * CF
                    + 4 * Li2(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4 * Li2(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(x) * pow(x, -1) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * 4 * Li2(x) * pow(x, -1) * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(x) * pow(x, -1) * CF * pow(NC, -1)
                    + (-1) * 2 * Li2(x) * pow(x, -1) * CF
                    + (-1) * 4 * Li2(x) * pow(x, -1) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 4 * Li2(x) * pow(x, -1) * z * CF * pow(NC, -1)
                    + 4 * Li2(x) * pow(x, -1) * z * CF
                    + 8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1)
                    + (-1) * 8 * Li2(x) * pow(x, -1) * pow(z, 2) * CF
                    + (-1) * 2 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(x) * pow(z, -1) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 3 * Li2(x) * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * Li2(x) * pow(z, -1) * CF
                    + 4 * Li2(x) * CF * pow(NC, -1) * pow(omx, -1)
                    + 4 * Li2(x) * CF * pow(NC, -1) * pow(omz, -1) * pow(opx, -1)
                    + (-1) * 4 * Li2(x) * CF * pow(NC, -1) * pow(omz, -1)
                    + (-1) * 4 * Li2(x) * CF * pow(NC, -1) * pow(opx, -1)
                    + (-1) * 2 * Li2(x) * CF * pow(NC, -1)
                    + (-1) * 3 * Li2(x) * CF * pow(omx, -1)
                    + 2 * Li2(x) * CF * pow(opx, -1)
                    + 4 * Li2(x) * CF
                    + (-1) * 2 * Li2(x) * z * CF * pow(NC, -1) * pow(omx, -1)
                    + (-1) * 4 * Li2(x) * z * CF * pow(NC, -1) * pow(opx, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(x) * z * CF * pow(NC, -1)
                    + 6 * Li2(x) * z * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(x) * z * CF * pow(opx, -1)
                    + (-1) * 4 * Li2(x) * z * CF
                    + (-1) * 8 * Li2(x) * pow(z, 2) * CF * pow(omx, -1)
                    + 8 * Li2(x) * pow(z, 2) * CF * pow(opx, -1)
                    + 8 * Li2(x) * pow(z, 2) * CF
                    + Li2(x) * x * pow(z, -1) * CF * pow(NC, -1)
                    + (-1) * Li2(x) * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(x) * x * CF * pow(NC, -1)
                    + 2 * Li2(x) * x * CF
                    + (-1) * Li2(z) * CF * pow(omx, -1)
                    + 3 * Li2(z) * CF
                    + 2 * Li2(z) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * z * CF
                    + Li2(z) * x * CF
                    + (-1) * 4 * InvTanInt(-sqrtxz3) * z * CF * sqrtxz3
                    + (-1) * 8 * InvTanInt(z * sqrtxz3) * z * CF * sqrtxz3
                    + 4 * InvTanInt(sqrtxz3) * z * CF * sqrtxz3
                    + 0
                )
            if "001" == order:
                tmp += 1.0 / 3.0 * pow(z, -1) * LMUA * CF + 0
                tmp += 3.0 / 2.0 * LMUA * CF + (-1) * 1.0 / 2.0 * z * LMUA * CF + (-1) * 4.0 / 3.0 * pow(z, 2) * LMUA * CF + 1.0 / 3.0 * x * pow(z, -1) * LMUA * CF + 1.0 / 2.0 * x * LMUA * CF + (-1) * 3.0 / 2.0 * x * z * LMUA * CF + 2.0 / 3.0 * x * pow(z, 2) * LMUA * CF + 0
                tmp += ln(z) * LMUA * CF + 0
                tmp += 2 * ln(z) * z * LMUA * CF + ln(z) * x * LMUA * CF + 0
            if "010" == order:
                tmp += (-1) * 5.0 / 2.0 * pow(z, -1) * LMUF * CF + 0
                tmp += 5 * LMUF * CF + 5.0 / 2.0 * x * pow(z, -1) * LMUF * CF + (-1) * 5 * x * LMUF * CF + 0
                tmp += (-1) * ln(x) * pow(z, -1) * LMUF * CF + 0
                tmp += 2 * ln(x) * LMUF * CF + (-1) * ln(x) * x * pow(z, -1) * LMUF * CF + 2 * ln(x) * x * LMUF * CF + 0
            res += tmp

        return res


def C2Pq2qbEq(x, z, rsl, order, f=C2Pq2qbEq_DR0123_scheme):
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
