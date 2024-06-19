from configs.eh import *


def C2Tq2gEq_DR0123_scheme(inx: float, inz: float, cx: str, cz: str, order: str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA):
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
                +(-1) * 5 * pow(NC, -1) * pow(z, -1) * zeta3 * CF
                + (-1) * 1.0 / 4.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                + 3 * pow(NC, -1) * CF
                + 3 * pow(NC, -1) * zeta3 * CF
                + 2.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                + 13.0 / 8.0 * pow(NC, -1) * z * CF
                + (-1) * 3.0 / 2.0 * pow(NC, -1) * z * zeta3 * CF
                + (-1) * 1.0 / 8.0 * pow(NC, -1) * z * pow(pi, 2) * CF
                + 1169.0 / 54.0 * NC * pow(z, -1) * CF
                + (-1) * 14 * NC * pow(z, -1) * zeta3 * CF
                + 4.0 / 3.0 * NC * pow(z, -1) * pow(rln2, 3) * CF
                + (-1) * 1.0 / 4.0 * NC * pow(z, -1) * pow(pi, 2) * CF
                + (-1) * 2.0 / 3.0 * NC * pow(z, -1) * pow(pi, 2) * rln2 * CF
                + (-1) * 295.0 / 18.0 * NC * CF
                + 4.0 / 3.0 * NC * pow(rln2, 3) * CF
                + (-1) * 5.0 / 3.0 * NC * pow(pi, 2) * CF
                + (-1) * 2.0 / 3.0 * NC * pow(pi, 2) * rln2 * CF
                + (-1) * 389.0 / 72.0 * NC * z * CF
                + (-1) * 12 * NC * z * zeta3 * CF
                + 2.0 / 3.0 * NC * z * pow(rln2, 3) * CF
                + 7.0 / 24.0 * NC * z * pow(pi, 2) * CF
                + (-1) * 1.0 / 3.0 * NC * z * pow(pi, 2) * rln2 * CF
                + (-1) * 269.0 / 54.0 * NC * pow(z, 2) * CF
                + 0
            )
            res += (
                +(-1) * 2 * ln(1 + z) * NC * pow(z, -1) * pow(rln2, 2) * CF
                + 1.0 / 3.0 * ln(1 + z) * NC * pow(z, -1) * pow(pi, 2) * CF
                + (-1) * 2 * ln(1 + z) * NC * pow(rln2, 2) * CF
                + 1.0 / 3.0 * ln(1 + z) * NC * pow(pi, 2) * CF
                + (-1) * ln(1 + z) * NC * z * pow(rln2, 2) * CF
                + 1.0 / 6.0 * ln(1 + z) * NC * z * pow(pi, 2) * CF
                + 9.0 / 2.0 * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                + 1.0 / 3.0 * ln(z) * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                + (-1) * 67.0 / 8.0 * ln(z) * pow(NC, -1) * CF
                + (-1) * 1.0 / 2.0 * ln(z) * pow(NC, -1) * pow(pi, 2) * CF
                + 45.0 / 8.0 * ln(z) * pow(NC, -1) * z * CF
                + 1.0 / 4.0 * ln(z) * pow(NC, -1) * z * pow(pi, 2) * CF
                + 71.0 / 18.0 * ln(z) * NC * pow(z, -1) * CF
                + (-1) * ln(z) * NC * pow(z, -1) * pow(pi, 2) * CF
                + 247.0 / 8.0 * ln(z) * NC * CF
                + (-1) * 1.0 / 6.0 * ln(z) * NC * pow(pi, 2) * CF
                + 31.0 / 8.0 * ln(z) * NC * z * CF
                + (-1) * 11.0 / 12.0 * ln(z) * NC * z * pow(pi, 2) * CF
                + 31.0 / 9.0 * ln(z) * NC * pow(z, 2) * CF
                + 0
            )
            res += (
                +ln(z) * ln(1 + z) * NC * z * CF
                + pow(ln(z), 2) * pow(NC, -1) * CF
                + (-1) * 13.0 / 16.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF
                + (-1) * 20.0 / 3.0 * pow(ln(z), 2) * NC * pow(z, -1) * CF
                + (-1) * 5 * pow(ln(z), 2) * NC * CF
                + (-1) * 7.0 / 16.0 * pow(ln(z), 2) * NC * z * CF
                + 3 * pow(ln(z), 2) * ln(1 + z) * NC * pow(z, -1) * CF
                + 3 * pow(ln(z), 2) * ln(1 + z) * NC * CF
                + 3.0 / 2.0 * pow(ln(z), 2) * ln(1 + z) * NC * z * CF
                + (-1) * 5.0 / 12.0 * pow(ln(z), 3) * pow(NC, -1) * CF
                + 5.0 / 24.0 * pow(ln(z), 3) * pow(NC, -1) * z * CF
                + 0
            )
            res += (
                +(-1) * 10.0 / 3.0 * pow(ln(z), 3) * NC * pow(z, -1) * CF
                + (-1) * 5.0 / 4.0 * pow(ln(z), 3) * NC * CF
                + (-1) * 65.0 / 24.0 * pow(ln(z), 3) * NC * z * CF
                + 2 * pow(ln(z), 2) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 2 * pow(ln(z), 2) * ln(omz) * pow(NC, -1) * CF
                + pow(ln(z), 2) * ln(omz) * pow(NC, -1) * z * CF
                + pow(ln(z), 2) * ln(omz) * NC * pow(z, -1) * CF
                + (-1) * pow(ln(z), 2) * ln(omz) * NC * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * ln(omz) * NC * z * CF
                + 3 * ln(z) * ln(omz) * NC * z * CF
                + 4 * ln(z) * ln(omz) * ln(1 + z) * NC * pow(z, -1) * CF
                + 4 * ln(z) * ln(omz) * ln(1 + z) * NC * CF
                + 2 * ln(z) * ln(omz) * ln(1 + z) * NC * z * CF
                + 2 * ln(z) * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * pow(NC, -1) * CF
                + 3.0 / 4.0 * ln(z) * pow(ln(omz), 2) * pow(NC, -1) * z * CF
                + 5 * ln(z) * pow(ln(omz), 2) * NC * pow(z, -1) * CF
                + (-1) * 3.0 / 2.0 * ln(z) * pow(ln(omz), 2) * NC * CF
                + 15.0 / 4.0 * ln(z) * pow(ln(omz), 2) * NC * z * CF
                + 2 * ln(z) * Li2(-z) * NC * pow(z, -1) * CF
                + 2 * ln(z) * Li2(-z) * NC * CF
                + ln(z) * Li2(-z) * NC * z * CF
                + 6 * ln(z) * Li2(z) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 6 * ln(z) * Li2(z) * pow(NC, -1) * CF
                + 3 * ln(z) * Li2(z) * pow(NC, -1) * z * CF
                + (-1) * 4 * ln(z) * Li2(z) * NC * pow(z, -1) * CF
                + 4 * ln(z) * Li2(z) * NC * CF
                + (-1) * 2 * ln(z) * Li2(z) * NC * z * CF
                + 9.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                + 1.0 / 3.0 * ln(omz) * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                + (-1) * 9.0 / 2.0 * ln(omz) * pow(NC, -1) * CF
                + (-1) * 1.0 / 2.0 * ln(omz) * pow(NC, -1) * pow(pi, 2) * CF
                + 5.0 / 2.0 * ln(omz) * pow(NC, -1) * z * CF
                + 0
            )
            res += (
                +1.0 / 4.0 * ln(omz) * pow(NC, -1) * z * pow(pi, 2) * CF
                + (-1) * 55.0 / 18.0 * ln(omz) * NC * pow(z, -1) * CF
                + (-1) * 2 * ln(omz) * NC * pow(z, -1) * pow(rln2, 2) * CF
                + (-1) * ln(omz) * NC * pow(z, -1) * pow(pi, 2) * CF
                + 23.0 / 3.0 * ln(omz) * NC * CF
                + (-1) * 2 * ln(omz) * NC * pow(rln2, 2) * CF
                + 1.0 / 2.0 * ln(omz) * NC * pow(pi, 2) * CF
                + (-1) * 31.0 / 6.0 * ln(omz) * NC * z * CF
                + (-1) * ln(omz) * NC * z * pow(rln2, 2) * CF
                + (-1) * 11.0 / 12.0 * ln(omz) * NC * z * pow(pi, 2) * CF
                + (-1) * 13.0 / 9.0 * ln(omz) * NC * pow(z, 2) * CF
                + 4 * ln(omz) * ln(1 + z) * NC * pow(z, -1) * rln2 * CF
                + 4 * ln(omz) * ln(1 + z) * NC * rln2 * CF
                + 2 * ln(omz) * ln(1 + z) * NC * z * rln2 * CF
                + 0
            )
            res += (
                +(-1) * 2 * ln(omz) * pow(ln(1 + z), 2) * NC * pow(z, -1) * CF
                + (-1) * 2 * ln(omz) * pow(ln(1 + z), 2) * NC * CF
                + (-1) * ln(omz) * pow(ln(1 + z), 2) * NC * z * CF
                + 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * CF
                + 1.0 / 8.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF
                + (-1) * 20.0 / 3.0 * pow(ln(omz), 2) * NC * pow(z, -1) * CF
                + 6 * pow(ln(omz), 2) * NC * CF
                + (-1) * 1.0 / 8.0 * pow(ln(omz), 2) * NC * z * CF
                + 2.0 / 3.0 * pow(ln(omz), 2) * NC * pow(z, 2) * CF
                + (-1) * 5.0 / 6.0 * pow(ln(omz), 3) * pow(NC, -1) * pow(z, -1) * CF
                + 5.0 / 6.0 * pow(ln(omz), 3) * pow(NC, -1) * CF
                + (-1) * 5.0 / 12.0 * pow(ln(omz), 3) * pow(NC, -1) * z * CF
                + 7.0 / 6.0 * pow(ln(omz), 3) * NC * pow(z, -1) * CF
                + (-1) * 7.0 / 6.0 * pow(ln(omz), 3) * NC * CF
                + 7.0 / 12.0 * pow(ln(omz), 3) * NC * z * CF
                + 4 * ln(omz) * Li2(-z) * NC * pow(z, -1) * CF
                + 4 * ln(omz) * Li2(-z) * NC * CF
                + 2 * ln(omz) * Li2(-z) * NC * z * CF
                + 5 * ln(omz) * Li2(z) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 4 * ln(omz) * Li2(z) * pow(NC, -1) * CF
                + 2 * ln(omz) * Li2(z) * pow(NC, -1) * z * CF
                + 5 * ln(omz) * Li2(z) * NC * pow(z, -1) * CF
                + 2 * ln(omz) * Li2(z) * NC * CF
                + 5 * ln(omz) * Li2(z) * NC * z * CF
                + 2.0 / 3.0 * ln(opz) * NC * pow(z, -1) * pow(pi, 2) * CF
                + 2.0 / 3.0 * ln(opz) * NC * pow(pi, 2) * CF
                + 1.0 / 3.0 * ln(opz) * NC * z * pow(pi, 2) * CF
                + (-1) * 4 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * NC * pow(z, -1) * CF
                + (-1) * 4 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * NC * CF
                + (-1) * 2 * Li3(1.0 / 2.0 - 1.0 / 2.0 * z) * NC * z * CF
                + (-1) * 4 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * NC * pow(z, -1) * CF
                + (-1) * 4 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * NC * CF
                + 0
            )
            res += (
                +(-1) * 2 * Li3(1.0 / 2.0 + 1.0 / 2.0 * z) * NC * z * CF
                + 3 * Li3(1 - z) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 2 * Li3(1 - z) * pow(NC, -1) * CF
                + Li3(1 - z) * pow(NC, -1) * z * CF
                + 7 * Li3(1 - z) * NC * pow(z, -1) * CF
                + 8 * Li3(1 - z) * NC * CF
                + 6 * Li3(1 - z) * NC * z * CF
                + 2 * Li3(-z) * NC * pow(z, -1) * CF
                + 2 * Li3(-z) * NC * CF
                + Li3(-z) * NC * z * CF
                + 4 * Li3(1 / (1 + z)) * NC * pow(z, -1) * CF
                + 4 * Li3(1 / (1 + z)) * NC * CF
                + 2 * Li3(1 / (1 + z)) * NC * z * CF
                + (-1) * 4 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * NC * pow(z, -1) * CF
                + (-1) * 4 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * NC * CF
                + (-1) * 2 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * NC * z * CF
                + (-1) * 6 * Li3(z) * pow(NC, -1) * pow(z, -1) * CF
                + 8 * Li3(z) * pow(NC, -1) * CF
                + (-1) * 4 * Li3(z) * pow(NC, -1) * z * CF
                + 20 * Li3(z) * NC * pow(z, -1) * CF
                + (-1) * 2 * Li3(z) * NC * CF
                + 15 * Li3(z) * NC * z * CF
                + Li2(-z) * NC * z * CF
                + (-1) * 3.0 / 2.0 * Li2(z) * pow(NC, -1) * pow(z, -1) * CF
                + Li2(z) * pow(NC, -1) * z * CF
                + 89.0 / 6.0 * Li2(z) * NC * pow(z, -1) * CF
                + (-1) * 2 * Li2(z) * NC * CF
                + Li2(z) * NC * z * CF
                + (-1) * 4.0 / 3.0 * Li2(z) * NC * pow(z, 2) * CF
                + 0
            )
        if "001" == order:
            res += (
                (-1) * 9.0 / 2.0 * LMUA * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 1.0 / 3.0 * LMUA * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                + 17.0 / 4.0 * LMUA * pow(NC, -1) * CF
                + 1.0 / 2.0 * LMUA * pow(NC, -1) * pow(pi, 2) * CF
                + (-1) * 7.0 / 4.0 * LMUA * pow(NC, -1) * z * CF
                + (-1) * 1.0 / 4.0 * LMUA * pow(NC, -1) * z * pow(pi, 2) * CF
                + 55.0 / 18.0 * LMUA * NC * pow(z, -1) * CF
                + 1.0 / 3.0 * LMUA * NC * pow(z, -1) * pow(pi, 2) * CF
                + (-1) * 95.0 / 12.0 * LMUA * NC * CF
                + 1.0 / 6.0 * LMUA * NC * pow(pi, 2) * CF
                + 31.0 / 12.0 * LMUA * NC * z * CF
                + 7.0 / 12.0 * LMUA * NC * z * pow(pi, 2) * CF
                + 13.0 / 9.0 * LMUA * NC * pow(z, 2) * CF
                + 0
            )
            res += 1.0 / 3.0 * LMUA * NF * z * CF + 0
            res += (
                (-1) * 3.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * CF
                + 3.0 / 4.0 * ln(z) * LMUA * pow(NC, -1) * z * CF
                + 29.0 / 3.0 * ln(z) * LMUA * NC * pow(z, -1) * CF
                + 19.0 / 6.0 * ln(z) * LMUA * NC * CF
                + (-1) * 55.0 / 12.0 * ln(z) * LMUA * NC * z * CF
                + (-1) * 4.0 / 3.0 * ln(z) * LMUA * NC * pow(z, 2) * CF
                + 2.0 / 3.0 * ln(z) * LMUA * NF * pow(z, -1) * CF
                + (-1) * 2.0 / 3.0 * ln(z) * LMUA * NF * CF
                + 1.0 / 3.0 * ln(z) * LMUA * NF * z * CF
                + (-1) * 4 * ln(z) * ln(1 + z) * LMUA * NC * pow(z, -1) * CF
                + (-1) * 4 * ln(z) * ln(1 + z) * LMUA * NC * CF
                + (-1) * 2 * ln(z) * ln(1 + z) * LMUA * NC * z * CF
                + pow(ln(z), 2) * LMUA * pow(NC, -1) * CF
                + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * LMUA * pow(NC, -1) * z * CF
                + 6 * pow(ln(z), 2) * LMUA * NC * pow(z, -1) * CF
                + 3 * pow(ln(z), 2) * LMUA * NC * CF
                + 11.0 / 2.0 * pow(ln(z), 2) * LMUA * NC * z * CF
                + 0
            )
            res += (-1) * 2 * ln(z) * ln(omz) * LMUA * pow(NC, -1) * pow(z, -1) * CF + 2 * ln(z) * ln(omz) * LMUA * pow(NC, -1) * CF + (-1) * ln(z) * ln(omz) * LMUA * pow(NC, -1) * z * CF + (-1) * 6 * ln(z) * ln(omz) * LMUA * NC * pow(z, -1) * CF + 6 * ln(z) * ln(omz) * LMUA * NC * CF + (-1) * 3 * ln(z) * ln(omz) * LMUA * NC * z * CF + 0
            res += (
                (-1) * 3.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * pow(z, -1) * CF
                + 5.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * CF
                + 49.0 / 6.0 * ln(omz) * LMUA * NC * pow(z, -1) * CF
                + (-1) * 41.0 / 6.0 * ln(omz) * LMUA * NC * CF
                + (-1) * 17.0 / 6.0 * ln(omz) * LMUA * NC * z * CF
                + (-1) * 4.0 / 3.0 * ln(omz) * LMUA * NC * pow(z, 2) * CF
                + 2.0 / 3.0 * ln(omz) * LMUA * NF * pow(z, -1) * CF
                + (-1) * 2.0 / 3.0 * ln(omz) * LMUA * NF * CF
                + 1.0 / 3.0 * ln(omz) * LMUA * NF * z * CF
                + 0
            )
            res += 2 * pow(ln(omz), 2) * LMUA * pow(NC, -1) * pow(z, -1) * CF + (-1) * 2 * pow(ln(omz), 2) * LMUA * pow(NC, -1) * CF + pow(ln(omz), 2) * LMUA * pow(NC, -1) * z * CF + (-1) * 4 * pow(ln(omz), 2) * LMUA * NC * pow(z, -1) * CF + 4 * pow(ln(omz), 2) * LMUA * NC * CF + (-1) * 2 * pow(ln(omz), 2) * LMUA * NC * z * CF + 0
            res += (
                (-1) * 4 * Li2(-z) * LMUA * NC * pow(z, -1) * CF
                + (-1) * 4 * Li2(-z) * LMUA * NC * CF
                + (-1) * 2 * Li2(-z) * LMUA * NC * z * CF
                + (-1) * 6 * Li2(z) * LMUA * pow(NC, -1) * pow(z, -1) * CF
                + 5 * Li2(z) * LMUA * pow(NC, -1) * CF
                + (-1) * 5.0 / 2.0 * Li2(z) * LMUA * pow(NC, -1) * z * CF
                + (-1) * 6 * Li2(z) * LMUA * NC * pow(z, -1) * CF
                + (-1) * Li2(z) * LMUA * NC * CF
                + (-1) * 11.0 / 2.0 * Li2(z) * LMUA * NC * z * CF
                + 0
            )
        if "002" == order:
            res += (
                (-1) * 1.0 / 2.0 * pow(LMUA, 2) * pow(NC, -1) * CF
                + 1.0 / 8.0 * pow(LMUA, 2) * pow(NC, -1) * z * CF
                + (-1) * 3.0 / 2.0 * pow(LMUA, 2) * NC * pow(z, -1) * CF
                + 5.0 / 6.0 * pow(LMUA, 2) * NC * CF
                + 53.0 / 24.0 * pow(LMUA, 2) * NC * z * CF
                + 2.0 / 3.0 * pow(LMUA, 2) * NC * pow(z, 2) * CF
                + (-1) * 2.0 / 3.0 * pow(LMUA, 2) * NF * pow(z, -1) * CF
                + 2.0 / 3.0 * pow(LMUA, 2) * NF * CF
                + (-1) * 1.0 / 3.0 * pow(LMUA, 2) * NF * z * CF
                + 0
            )
            res += (-1) * 1.0 / 2.0 * ln(z) * pow(LMUA, 2) * pow(NC, -1) * CF + 1.0 / 4.0 * ln(z) * pow(LMUA, 2) * pow(NC, -1) * z * CF + (-1) * 2 * ln(z) * pow(LMUA, 2) * NC * pow(z, -1) * CF + (-1) * 3.0 / 2.0 * ln(z) * pow(LMUA, 2) * NC * CF + (-1) * 9.0 / 4.0 * ln(z) * pow(LMUA, 2) * NC * z * CF + 0
            res += (-1) * ln(omz) * pow(LMUA, 2) * pow(NC, -1) * pow(z, -1) * CF + ln(omz) * pow(LMUA, 2) * pow(NC, -1) * CF + (-1) * 1.0 / 2.0 * ln(omz) * pow(LMUA, 2) * pow(NC, -1) * z * CF + 3 * ln(omz) * pow(LMUA, 2) * NC * pow(z, -1) * CF + (-1) * 3 * ln(omz) * pow(LMUA, 2) * NC * CF + 3.0 / 2.0 * ln(omz) * pow(LMUA, 2) * NC * z * CF + 0
        if "010" == order:
            res += (
                (-1) * 1.0 / 3.0 * LMUF * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                + 1.0 / 3.0 * LMUF * pow(NC, -1) * pow(pi, 2) * CF
                + 3.0 / 4.0 * LMUF * pow(NC, -1) * z * CF
                + (-1) * 1.0 / 6.0 * LMUF * pow(NC, -1) * z * pow(pi, 2) * CF
                + 1.0 / 3.0 * LMUF * NC * pow(z, -1) * pow(pi, 2) * CF
                + (-1) * 1.0 / 3.0 * LMUF * NC * pow(pi, 2) * CF
                + (-1) * 3.0 / 4.0 * LMUF * NC * z * CF
                + 1.0 / 6.0 * LMUF * NC * z * pow(pi, 2) * CF
                + 0
            )
            res += 3.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * pow(z, -1) * CF + (-1) * 3.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * CF + 3.0 / 4.0 * ln(z) * LMUF * pow(NC, -1) * z * CF + (-1) * 3.0 / 2.0 * ln(z) * LMUF * NC * pow(z, -1) * CF + 3.0 / 2.0 * ln(z) * LMUF * NC * CF + (-1) * 3.0 / 4.0 * ln(z) * LMUF * NC * z * CF + 0
            res += 3.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * pow(z, -1) * CF + (-1) * 3.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * CF + 3.0 / 4.0 * ln(omz) * LMUF * pow(NC, -1) * z * CF + (-1) * 3.0 / 2.0 * ln(omz) * LMUF * NC * pow(z, -1) * CF + 3.0 / 2.0 * ln(omz) * LMUF * NC * CF + (-1) * 3.0 / 4.0 * ln(omz) * LMUF * NC * z * CF + 0
        if "011" == order:
            res += (-1) * 3.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * pow(z, -1) * CF + 3.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * CF + (-1) * 3.0 / 4.0 * LMUA * LMUF * pow(NC, -1) * z * CF + 3.0 / 2.0 * LMUA * LMUF * NC * pow(z, -1) * CF + (-1) * 3.0 / 2.0 * LMUA * LMUF * NC * CF + 3.0 / 4.0 * LMUA * LMUF * NC * z * CF + 0
        if "100" == order:
            res += 11.0 / 6.0 * LMUR * NC * z * CF + (-1) * 1.0 / 3.0 * LMUR * NF * z * CF + 0
            res += 11.0 / 3.0 * ln(z) * LMUR * NC * pow(z, -1) * CF + (-1) * 11.0 / 3.0 * ln(z) * LMUR * NC * CF + 11.0 / 6.0 * ln(z) * LMUR * NC * z * CF + 0
            res += (-1) * 2.0 / 3.0 * ln(z) * LMUR * NF * pow(z, -1) * CF + 2.0 / 3.0 * ln(z) * LMUR * NF * CF + (-1) * 1.0 / 3.0 * ln(z) * LMUR * NF * z * CF + 0
            res += 11.0 / 3.0 * ln(omz) * LMUR * NC * pow(z, -1) * CF + (-1) * 11.0 / 3.0 * ln(omz) * LMUR * NC * CF + 11.0 / 6.0 * ln(omz) * LMUR * NC * z * CF + (-1) * 2.0 / 3.0 * ln(omz) * LMUR * NF * pow(z, -1) * CF + 2.0 / 3.0 * ln(omz) * LMUR * NF * CF + (-1) * 1.0 / 3.0 * ln(omz) * LMUR * NF * z * CF + 0
        if "101" == order:
            res += (-1) * 11.0 / 3.0 * LMUA * LMUR * NC * pow(z, -1) * CF + 11.0 / 3.0 * LMUA * LMUR * NC * CF + (-1) * 11.0 / 6.0 * LMUA * LMUR * NC * z * CF + 2.0 / 3.0 * LMUA * LMUR * NF * pow(z, -1) * CF + (-1) * 2.0 / 3.0 * LMUA * LMUR * NF * CF + 1.0 / 3.0 * LMUA * LMUR * NF * z * CF + 0
        return res

    if cx == "0" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += (
                9.0 / 2.0 * pow(NC, -1) * pow(z, -1) * CF
                + 2.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                + (-1) * 17.0 / 4.0 * pow(NC, -1) * CF
                + (-1) * 5.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF
                + 5.0 / 2.0 * pow(NC, -1) * z * CF
                + 5.0 / 12.0 * pow(NC, -1) * z * pow(pi, 2) * CF
                + (-1) * 55.0 / 18.0 * NC * pow(z, -1) * CF
                + (-1) * 2.0 / 3.0 * NC * pow(z, -1) * pow(pi, 2) * CF
                + 95.0 / 12.0 * NC * CF
                + 1.0 / 6.0 * NC * pow(pi, 2) * CF
                + (-1) * 31.0 / 6.0 * NC * z * CF
                + (-1) * 3.0 / 4.0 * NC * z * pow(pi, 2) * CF
                + (-1) * 13.0 / 9.0 * NC * pow(z, 2) * CF
                + 3.0 / 2.0 * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 89.0 / 6.0 * ln(z) * NC * pow(z, -1) * CF
                + 2 * ln(z) * NC * CF
                + 2 * ln(z) * NC * z * CF
                + 4.0 / 3.0 * ln(z) * NC * pow(z, 2) * CF
                + 0
            )
            res += (
                +4 * ln(z) * ln(1 + z) * NC * pow(z, -1) * CF
                + 4 * ln(z) * ln(1 + z) * NC * CF
                + 2 * ln(z) * ln(1 + z) * NC * z * CF
                + (-1) * pow(ln(z), 2) * pow(NC, -1) * CF
                + 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF
                + (-1) * 6 * pow(ln(z), 2) * NC * pow(z, -1) * CF
                + (-1) * 3 * pow(ln(z), 2) * NC * CF
                + (-1) * 11.0 / 2.0 * pow(ln(z), 2) * NC * z * CF
                + 2 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 2 * ln(z) * ln(omz) * pow(NC, -1) * CF
                + ln(z) * ln(omz) * pow(NC, -1) * z * CF
                + 6 * ln(z) * ln(omz) * NC * pow(z, -1) * CF
                + (-1) * 6 * ln(z) * ln(omz) * NC * CF
                + 3 * ln(z) * ln(omz) * NC * z * CF
                + 3 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 4 * ln(omz) * pow(NC, -1) * CF
                + 3.0 / 4.0 * ln(omz) * pow(NC, -1) * z * CF
                + (-1) * 40.0 / 3.0 * ln(omz) * NC * pow(z, -1) * CF
                + 12 * ln(omz) * NC * CF
                + 1.0 / 4.0 * ln(omz) * NC * z * CF
                + 4.0 / 3.0 * ln(omz) * NC * pow(z, 2) * CF
                + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                + 2 * pow(ln(omz), 2) * pow(NC, -1) * CF
                + (-1) * pow(ln(omz), 2) * pow(NC, -1) * z * CF
                + 4 * pow(ln(omz), 2) * NC * pow(z, -1) * CF
                + (-1) * 4 * pow(ln(omz), 2) * NC * CF
                + 2 * pow(ln(omz), 2) * NC * z * CF
                + 4 * Li2(-z) * NC * pow(z, -1) * CF
                + 4 * Li2(-z) * NC * CF
                + 2 * Li2(-z) * NC * z * CF
                + 0
            )
            res += +6 * Li2(z) * pow(NC, -1) * pow(z, -1) * CF + (-1) * 5 * Li2(z) * pow(NC, -1) * CF + 5.0 / 2.0 * Li2(z) * pow(NC, -1) * z * CF + 6 * Li2(z) * NC * pow(z, -1) * CF + Li2(z) * NC * CF + 11.0 / 2.0 * Li2(z) * NC * z * CF + 0
        if "001" == order:
            res += (
                (-1) * 3.0 / 2.0 * LMUA * pow(NC, -1) * pow(z, -1) * CF
                + 5.0 / 2.0 * LMUA * pow(NC, -1) * CF
                + (-1) * LMUA * pow(NC, -1) * z * CF
                + 49.0 / 6.0 * LMUA * NC * pow(z, -1) * CF
                + (-1) * 41.0 / 6.0 * LMUA * NC * CF
                + (-1) * 11.0 / 6.0 * LMUA * NC * z * CF
                + (-1) * 4.0 / 3.0 * LMUA * NC * pow(z, 2) * CF
                + 2.0 / 3.0 * LMUA * NF * pow(z, -1) * CF
                + (-1) * 2.0 / 3.0 * LMUA * NF * CF
                + 1.0 / 3.0 * LMUA * NF * z * CF
                + ln(z) * LMUA * pow(NC, -1) * CF
                + 0
            )
            res += (
                (-1) * 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * z * CF
                + 4 * ln(z) * LMUA * NC * pow(z, -1) * CF
                + 3 * ln(z) * LMUA * NC * CF
                + 9.0 / 2.0 * ln(z) * LMUA * NC * z * CF
                + 2 * ln(omz) * LMUA * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 2 * ln(omz) * LMUA * pow(NC, -1) * CF
                + ln(omz) * LMUA * pow(NC, -1) * z * CF
                + (-1) * 6 * ln(omz) * LMUA * NC * pow(z, -1) * CF
                + 6 * ln(omz) * LMUA * NC * CF
                + (-1) * 3 * ln(omz) * LMUA * NC * z * CF
                + 0
            )
        if "010" == order:
            res += (
                3.0 / 2.0 * LMUF * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 3.0 / 2.0 * LMUF * pow(NC, -1) * CF
                + 7.0 / 4.0 * LMUF * pow(NC, -1) * z * CF
                + (-1) * 3.0 / 2.0 * LMUF * NC * pow(z, -1) * CF
                + 3.0 / 2.0 * LMUF * NC * CF
                + (-1) * 7.0 / 4.0 * LMUF * NC * z * CF
                + 2 * ln(z) * LMUF * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 2 * ln(z) * LMUF * pow(NC, -1) * CF
                + ln(z) * LMUF * pow(NC, -1) * z * CF
                + (-1) * 2 * ln(z) * LMUF * NC * pow(z, -1) * CF
                + 2 * ln(z) * LMUF * NC * CF
                + (-1) * ln(z) * LMUF * NC * z * CF
                + 0
            )
            res += 2 * ln(omz) * LMUF * pow(NC, -1) * pow(z, -1) * CF + (-1) * 2 * ln(omz) * LMUF * pow(NC, -1) * CF + ln(omz) * LMUF * pow(NC, -1) * z * CF + (-1) * 2 * ln(omz) * LMUF * NC * pow(z, -1) * CF + 2 * ln(omz) * LMUF * NC * CF + (-1) * ln(omz) * LMUF * NC * z * CF + 0
        if "011" == order:
            res += (-1) * 2 * LMUA * LMUF * pow(NC, -1) * pow(z, -1) * CF + 2 * LMUA * LMUF * pow(NC, -1) * CF + (-1) * LMUA * LMUF * pow(NC, -1) * z * CF + 2 * LMUA * LMUF * NC * pow(z, -1) * CF + (-1) * 2 * LMUA * LMUF * NC * CF + LMUA * LMUF * NC * z * CF + 0
        if "100" == order:
            res += 11.0 / 3.0 * LMUR * NC * pow(z, -1) * CF + (-1) * 11.0 / 3.0 * LMUR * NC * CF + 11.0 / 6.0 * LMUR * NC * z * CF + (-1) * 2.0 / 3.0 * LMUR * NF * pow(z, -1) * CF + 2.0 / 3.0 * LMUR * NF * CF + (-1) * 1.0 / 3.0 * LMUR * NF * z * CF + 0
        return res

    if cx == "1" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += (
                3 * pow(NC, -1) * pow(z, -1) * CF
                + (-1) * 4 * pow(NC, -1) * CF
                + 3.0 / 4.0 * pow(NC, -1) * z * CF
                + (-1) * 40.0 / 3.0 * NC * pow(z, -1) * CF
                + 12 * NC * CF
                + 1.0 / 4.0 * NC * z * CF
                + 4.0 / 3.0 * NC * pow(z, 2) * CF
                + (-1) * 2 * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                + ln(z) * pow(NC, -1) * CF
                + (-1) * 1.0 / 2.0 * ln(z) * pow(NC, -1) * z * CF
                + (-1) * 2 * ln(z) * NC * pow(z, -1) * CF
                + (-1) * 5 * ln(z) * NC * CF
                + (-1) * 7.0 / 2.0 * ln(z) * NC * z * CF
                + (-1) * 4 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                + 4 * ln(omz) * pow(NC, -1) * CF
                + (-1) * 2 * ln(omz) * pow(NC, -1) * z * CF
                + 8 * ln(omz) * NC * pow(z, -1) * CF
                + (-1) * 8 * ln(omz) * NC * CF
                + 4 * ln(omz) * NC * z * CF
                + 0
            )
        if "001" == order:
            res += 2 * LMUA * pow(NC, -1) * pow(z, -1) * CF + (-1) * 2 * LMUA * pow(NC, -1) * CF + LMUA * pow(NC, -1) * z * CF + (-1) * 2 * LMUA * NC * pow(z, -1) * CF + 2 * LMUA * NC * CF + (-1) * LMUA * NC * z * CF + 0
        if "010" == order:
            res += 4 * LMUF * pow(NC, -1) * pow(z, -1) * CF + (-1) * 4 * LMUF * pow(NC, -1) * CF + 2 * LMUF * pow(NC, -1) * z * CF + (-1) * 4 * LMUF * NC * pow(z, -1) * CF + 4 * LMUF * NC * CF + (-1) * 2 * LMUF * NC * z * CF + 0
        return res

    if cx == "2" and cz == "R":

        z = inz
        omz = 1.0 - z
        opz = 1.0 + z
        # Split orders:
        res = 0
        if "000" == order:
            res += +(-1) * 3 * pow(NC, -1) * pow(z, -1) * CF + 3 * pow(NC, -1) * CF + (-1) * 3.0 / 2.0 * pow(NC, -1) * z * CF + 3 * NC * pow(z, -1) * CF + (-1) * 3 * NC * CF + 3.0 / 2.0 * NC * z * CF + 0
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
            res += 0 + 0
        return res

    if cx == "R" and cz == "0":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
        return res

    if cx == "R" and cz == "1":

        x = inx
        omx = 1.0 - x
        opx = 1.0 + x
        op6xpxsq = 1.0 + 6.0 * x + x * x
        # Split orders:
        res = 0
        if "000" == order:
            res += 0 + 0
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
                tmp += (
                    4 * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 5.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + 1.0 / 6.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * CF
                    + 2 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                    + 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * pow(NC, -1) * x * pow(z, -1) * CF
                    + 3.0 / 2.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 3 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 5.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * x * CF
                    + 12 * ln(x) * pow(NC, -1) * x * z * CF
                    + 13 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 19 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * pow(ln(x), 2) * pow(NC, -1) * CF
                    + 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 10 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 20 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 13 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 16 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 5 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                    + 26 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 10 * ln(x) * ln(z) * pow(NC, -1) * CF
                    + (-1) * 13 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 11 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 22 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 16 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 20 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +28 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * ln(omx) * pow(NC, -1) * CF
                    + (-1) * 14 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 16 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 32 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 20 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 22 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 5 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 32 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 10 * ln(x) * ln(omz) * pow(NC, -1) * CF
                    + (-1) * 16 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 17 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 34 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 22 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * CF
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF
                    + (-1) * 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF
                    + 3 * ln(x) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(x) * ln(omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(z) * pow(NC, -1) * x * z * CF
                    + 5 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 9 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * pow(ln(z), 2) * pow(NC, -1) * CF
                    + 9.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 3 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 5 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + 8 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 12 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(omx) * pow(NC, -1) * CF
                    + 6 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 12 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 20 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 8 * ln(z) * ln(omz) * pow(NC, -1) * CF
                    + 10 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 16 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(z) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + ln(z) * ln(xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF
                    + 0
                )
                tmp += (
                    +2 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * z * CF
                    + 5 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + pow(ln(omx), 2) * pow(NC, -1) * CF
                    + 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 9 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 5 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + 16 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 22 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                    + 11 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 13 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 26 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 8 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 8 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * z * CF
                    + 8 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 11 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 3 * pow(ln(omz), 2) * pow(NC, -1) * CF
                    + 11.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 13.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 13 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 8 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(omz) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 6 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF
                    + (-1) * 3 * ln(omz) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 3 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF
                    + 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + (-1) * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +(-1) * 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF
                    + Li2(z * pow(omx, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF
                    + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + 2 * Li2(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    4 * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 5.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + 1.0 / 6.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * CF
                    + 2 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                    + 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * pow(NC, -1) * x * pow(z, -1) * CF
                    + 3.0 / 2.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 3 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 5.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * x * CF
                    + 12 * ln(x) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF
                    + 3 * ln(x) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + 13 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 20 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 7 * pow(ln(x), 2) * pow(NC, -1) * CF
                    + 10 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 19.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 19 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 13 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 20 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +6 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                    + 32 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * ln(z) * pow(NC, -1) * CF
                    + (-1) * 16 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 14 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 28 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 20 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 16 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 3 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 22 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * pow(NC, -1) * CF
                    + (-1) * 11 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 13 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 26 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 16 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 22 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 34 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * ln(omz) * pow(NC, -1) * CF
                    + (-1) * 17 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 16 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 32 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 22 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * ln(x) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * CF
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF
                    + (-1) * 2 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(z) * pow(NC, -1) * x * z * CF
                    + 5 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 9 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * pow(ln(z), 2) * pow(NC, -1) * CF
                    + 9.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 3 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 5 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + 8 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 12 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(omx) * pow(NC, -1) * CF
                    + 6 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 16 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 26 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 10 * ln(z) * ln(omz) * pow(NC, -1) * CF
                    + 13 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 11 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 22 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 16 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(z) * ln(xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * ln(z) * ln(xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + ln(z) * ln(xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF
                    + 0
                )
                tmp += (
                    +2 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * z * CF
                    + 5 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + pow(ln(omx), 2) * pow(NC, -1) * CF
                    + 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 9 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 5 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 16 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                    + 8 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 10 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 20 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 8 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 8 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 6 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF
                    + 0
                )
                tmp += (
                    +(-1) * 3 * ln(omz) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 3 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + 8 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 12 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * pow(ln(omz), 2) * pow(NC, -1) * CF
                    + 6 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 8 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * CF
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * z * CF
                    + Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF
                    + (-1) * Li2(pow(z, -1) * omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + 2 * Li2(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) < round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    4 * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 3 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + 5.0 / 6.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * CF
                    + 14.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 5.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                    + 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 7.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * pow(NC, -1) * x * pow(z, -1) * CF
                    + 13.0 / 6.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 13.0 / 3.0 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 3 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * x * CF
                    + 12 * ln(x) * pow(NC, -1) * x * z * CF
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * CF
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF
                    + (-1) * 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + 14 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 21 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 7 * pow(ln(x), 2) * pow(NC, -1) * CF
                    + 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 21.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 21 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 14 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 18 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +6 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                    + 30 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * ln(z) * pow(NC, -1) * CF
                    + (-1) * 15 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 24 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 18 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 18 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 3 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 24 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * pow(NC, -1) * CF
                    + (-1) * 12 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 15 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 30 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 18 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 24 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 36 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * ln(omz) * pow(NC, -1) * CF
                    + (-1) * 18 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 18 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 36 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 24 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * CF
                    + 3 * ln(x) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(x) * ln(omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +6 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(z) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + ln(z) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF
                    + 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + 6 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 11 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 5 * pow(ln(z), 2) * pow(NC, -1) * CF
                    + 11.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 7 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 6 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + 6 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(omx) * pow(NC, -1) * CF
                    + 4 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 5 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 10 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 14 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 24 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 10 * ln(z) * ln(omz) * pow(NC, -1) * CF
                    + 12 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 9 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 18 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 14 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * z * CF
                    + 7 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 10 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 3 * pow(ln(omx), 2) * pow(NC, -1) * CF
                    + 5 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 11 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 7 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 14 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                    + 7 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 11 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 22 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 8 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 8 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * z * CF
                    + 10 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 15 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +5 * pow(ln(omz), 2) * pow(NC, -1) * CF
                    + 15.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 15.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 15 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 10 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(omz) * ln(omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 6 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * CF
                    + (-1) * 3 * ln(omz) * ln(omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 3 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF
                    + 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * CF
                    + Li2(z * pow(omx, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * CF
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * z * CF
                    + 2 * Li2(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(1.0 - x, ndecimals) and round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    4 * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 5.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + 1.0 / 6.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * CF
                    + 2 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF
                    + 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 4 * pow(NC, -1) * x * pow(z, -1) * CF
                    + 3.0 / 2.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 3 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + 5.0 / 3.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 12 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 12 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * x * CF
                    + 12 * ln(x) * pow(NC, -1) * x * z * CF
                    + 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * CF
                    + 3 * ln(x) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + (-1) * 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * ln(x) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * CF
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF
                    + (-1) * 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + 12 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 3 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 18 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * pow(ln(x), 2) * pow(NC, -1) * CF
                    + 9 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 9 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 18 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + (-1) * 12 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 18 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 5 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                    + 28 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 10 * ln(x) * ln(z) * pow(NC, -1) * CF
                    + (-1) * 14 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 13 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 26 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + 18 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 18 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 26 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(x) * ln(omx) * pow(NC, -1) * CF
                    + (-1) * 13 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 14 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 28 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 18 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 20 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 5 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 30 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 10 * ln(x) * ln(omz) * pow(NC, -1) * CF
                    + (-1) * 15 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 15 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 30 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + 20 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(z) * ln(-xmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * ln(z) * ln(-xmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + ln(z) * ln(-xmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF
                    + 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF
                    + 4 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 7 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 3 * pow(ln(z), 2) * pow(NC, -1) * CF
                    + 7.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 5 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + (-1) * 4 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + 10 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 16 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(z) * ln(omx) * pow(NC, -1) * CF
                    + 8 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 7 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 14 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 10 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 14 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 22 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 8 * ln(z) * ln(omz) * pow(NC, -1) * CF
                    + 11 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 10 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +20 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 14 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 6 * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 6 * ln(omx) * pow(NC, -1) * x * CF
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * x * z * CF
                    + 5 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + pow(ln(omx), 2) * pow(NC, -1) * CF
                    + 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 9.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 9 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + (-1) * 5 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 16 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                    + 8 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 10 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 20 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 12 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 8 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 8 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 8 * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(z, -1) * CF
                    + 6 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * CF
                    + 0
                )
                tmp += (
                    +(-1) * 3 * ln(omz) * ln(-omxmz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 3 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF
                    + 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF
                    + 8 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 12 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * pow(ln(omz), 2) * pow(NC, -1) * CF
                    + 6 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 6 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 12 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + (-1) * 8 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * CF
                    + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + 2 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + 0
                )
                tmp += (
                    +Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * CF
                    + (-1) * Li2(pow(z, -1) * omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * CF
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF
                    + 2 * Li2(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(z) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) > round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    +(-1) * NC * pow(z, -1) * CF
                    + NC * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * NC * pow(z, -1) * pow(pi, 2) * CF
                    + 3 * NC * CF
                    + (-1) * NC * pow(pi, 2) * CF * pow(omx, -1)
                    + NC * pow(pi, 2) * CF
                    + (-1) * NC * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * NC * z * pow(pi, 2) * CF * pow(omx, -1)
                    + NC * x * pow(z, -1) * CF
                    + (-1) * 1.0 / 2.0 * NC * x * pow(z, -1) * pow(pi, 2) * CF
                    + NC * x * pow(pi, 2) * CF
                    + (-1) * NC * x * z * pow(pi, 2) * CF
                    + 6 * ln(x) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * NC * CF * pow(omx, -1)
                    + 9 * ln(x) * NC * CF
                    + 6 * ln(x) * NC * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * NC * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * NC * x * z * CF
                    + (-1) * 2 * ln(x) * ln(-xmz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + ln(x) * ln(-xmz) * NC * pow(z, -1) * CF
                    + 2 * ln(x) * ln(-xmz) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(-xmz) * NC * CF
                    + (-1) * ln(x) * ln(-xmz) * NC * z * CF * pow(omx, -1)
                    + ln(x) * ln(-xmz) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * ln(-xmz) * NC * x * CF
                    + 2 * ln(x) * ln(-xmz) * NC * x * z * CF
                    + (-1) * 7 * pow(ln(x), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 7.0 / 2.0 * pow(ln(x), 2) * NC * pow(z, -1) * CF
                    + 7 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
                    + (-1) * 7 * pow(ln(x), 2) * NC * CF
                    + (-1) * 7.0 / 2.0 * pow(ln(x), 2) * NC * z * CF * pow(omx, -1)
                    + 7.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * 7 * pow(ln(x), 2) * NC * x * CF
                    + 7 * pow(ln(x), 2) * NC * x * z * CF
                    + 12 * ln(x) * ln(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(z) * NC * pow(z, -1) * CF
                    + (-1) * 12 * ln(x) * ln(z) * NC * CF * pow(omx, -1)
                    + 12 * ln(x) * ln(z) * NC * CF
                    + 6 * ln(x) * ln(z) * NC * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(z) * NC * x * pow(z, -1) * CF
                    + 12 * ln(x) * ln(z) * NC * x * CF
                    + (-1) * 12 * ln(x) * ln(z) * NC * x * z * CF
                    + 12 * ln(x) * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * NC * pow(z, -1) * CF
                    + (-1) * 12 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +12 * ln(x) * ln(omx) * NC * CF
                    + 6 * ln(x) * ln(omx) * NC * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * ln(omx) * NC * x * pow(z, -1) * CF
                    + 12 * ln(x) * ln(omx) * NC * x * CF
                    + (-1) * 12 * ln(x) * ln(omx) * NC * x * z * CF
                    + 6 * ln(x) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(omz) * NC * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * ln(omz) * NC * CF * pow(omx, -1)
                    + 6 * ln(x) * ln(omz) * NC * CF
                    + 3 * ln(x) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + (-1) * 3 * ln(x) * ln(omz) * NC * x * pow(z, -1) * CF
                    + 6 * ln(x) * ln(omz) * NC * x * CF
                    + (-1) * 6 * ln(x) * ln(omz) * NC * x * z * CF
                    + (-1) * 4 * ln(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(z) * NC * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * NC * CF
                    + (-1) * 4 * ln(z) * NC * z * CF * pow(omx, -1)
                    + 4 * ln(z) * NC * x * pow(z, -1) * CF
                    + 4 * ln(z) * NC * x * z * CF
                    + 2 * ln(z) * ln(-xmz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(-xmz) * NC * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * NC * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(-xmz) * NC * CF
                    + ln(z) * ln(-xmz) * NC * z * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(-xmz) * NC * x * pow(z, -1) * CF
                    + 2 * ln(z) * ln(-xmz) * NC * x * CF
                    + (-1) * 2 * ln(z) * ln(-xmz) * NC * x * z * CF
                    + (-1) * 5 * pow(ln(z), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * NC * pow(z, -1) * CF
                    + 5 * pow(ln(z), 2) * NC * CF * pow(omx, -1)
                    + (-1) * 5 * pow(ln(z), 2) * NC * CF
                    + (-1) * 5.0 / 2.0 * pow(ln(z), 2) * NC * z * CF * pow(omx, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * 5 * pow(ln(z), 2) * NC * x * CF
                    + 5 * pow(ln(z), 2) * NC * x * z * CF
                    + (-1) * 10 * ln(z) * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 5 * ln(z) * ln(omx) * NC * pow(z, -1) * CF
                    + 10 * ln(z) * ln(omx) * NC * CF * pow(omx, -1)
                    + (-1) * 10 * ln(z) * ln(omx) * NC * CF
                    + (-1) * 5 * ln(z) * ln(omx) * NC * z * CF * pow(omx, -1)
                    + 5 * ln(z) * ln(omx) * NC * x * pow(z, -1) * CF
                    + (-1) * 10 * ln(z) * ln(omx) * NC * x * CF
                    + 0
                )
                tmp += (
                    +10 * ln(z) * ln(omx) * NC * x * z * CF
                    + (-1) * 2 * ln(z) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + ln(z) * ln(omz) * NC * pow(z, -1) * CF
                    + 2 * ln(z) * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(omz) * NC * CF
                    + (-1) * ln(z) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + ln(z) * ln(omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(omz) * NC * x * CF
                    + 2 * ln(z) * ln(omz) * NC * x * z * CF
                    + (-1) * 4 * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(omx) * NC * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * NC * CF
                    + (-1) * 4 * ln(omx) * NC * z * CF * pow(omx, -1)
                    + 4 * ln(omx) * NC * x * pow(z, -1) * CF
                    + 4 * ln(omx) * NC * x * z * CF
                    + (-1) * 4 * pow(ln(omx), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * pow(ln(omx), 2) * NC * pow(z, -1) * CF
                    + 4 * pow(ln(omx), 2) * NC * CF * pow(omx, -1)
                    + (-1) * 4 * pow(ln(omx), 2) * NC * CF
                    + (-1) * 2 * pow(ln(omx), 2) * NC * z * CF * pow(omx, -1)
                    + 2 * pow(ln(omx), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * pow(ln(omx), 2) * NC * x * CF
                    + 4 * pow(ln(omx), 2) * NC * x * z * CF
                    + (-1) * 4 * ln(omx) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * ln(omx) * ln(omz) * NC * pow(z, -1) * CF
                    + 4 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * NC * CF
                    + (-1) * 2 * ln(omx) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(omx) * ln(omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * ln(omx) * ln(omz) * NC * x * CF
                    + 4 * ln(omx) * ln(omz) * NC * x * z * CF
                    + (-1) * 2 * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 3 * ln(omz) * NC * CF
                    + (-1) * 2 * ln(omz) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(omz) * NC * x * pow(z, -1) * CF
                    + 2 * ln(omz) * NC * x * z * CF
                    + (-1) * pow(ln(omz), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * NC * pow(z, -1) * CF
                    + pow(ln(omz), 2) * NC * CF * pow(omx, -1)
                    + (-1) * pow(ln(omz), 2) * NC * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * NC * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +1.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * pow(ln(omz), 2) * NC * x * CF
                    + pow(ln(omz), 2) * NC * x * z * CF
                    + 2 * Li2(pow(omx, -1) * omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * NC * pow(z, -1) * CF
                    + (-1) * 2 * Li2(pow(omx, -1) * omz) * NC * CF * pow(omx, -1)
                    + 2 * Li2(pow(omx, -1) * omz) * NC * CF
                    + Li2(pow(omx, -1) * omz) * NC * z * CF * pow(omx, -1)
                    + (-1) * Li2(pow(omx, -1) * omz) * NC * x * pow(z, -1) * CF
                    + 2 * Li2(pow(omx, -1) * omz) * NC * x * CF
                    + (-1) * 2 * Li2(pow(omx, -1) * omz) * NC * x * z * CF
                    + (-1) * 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * pow(z, -1) * CF
                    + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * CF
                    + (-1) * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * z * CF * pow(omx, -1)
                    + Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * x * CF
                    + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * x * z * CF
                    + 2 * Li2(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(z) * NC * pow(z, -1) * CF
                    + (-1) * 2 * Li2(z) * NC * CF * pow(omx, -1)
                    + 2 * Li2(z) * NC * CF
                    + Li2(z) * NC * z * CF * pow(omx, -1)
                    + (-1) * Li2(z) * NC * x * pow(z, -1) * CF
                    + 2 * Li2(z) * NC * x * CF
                    + (-1) * 2 * Li2(z) * NC * x * z * CF
                    + 0
                )
            res += tmp

        if round(z, ndecimals) < round(x, ndecimals):

            tmp = 0.0
            # Split orders:
            tmp = 0
            if "000" == order:
                tmp += (
                    +(-1) * NC * pow(z, -1) * CF
                    + NC * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * NC * pow(z, -1) * pow(pi, 2) * CF
                    + 3 * NC * CF
                    + (-1) * NC * pow(pi, 2) * CF * pow(omx, -1)
                    + NC * pow(pi, 2) * CF
                    + (-1) * NC * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * NC * z * pow(pi, 2) * CF * pow(omx, -1)
                    + NC * x * pow(z, -1) * CF
                    + (-1) * 1.0 / 2.0 * NC * x * pow(z, -1) * pow(pi, 2) * CF
                    + NC * x * pow(pi, 2) * CF
                    + (-1) * NC * x * z * pow(pi, 2) * CF
                    + 6 * ln(x) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * NC * CF * pow(omx, -1)
                    + 9 * ln(x) * NC * CF
                    + 6 * ln(x) * NC * z * CF * pow(omx, -1)
                    + (-1) * 6 * ln(x) * NC * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * NC * x * z * CF
                    + (-1) * 6 * pow(ln(x), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 3 * pow(ln(x), 2) * NC * pow(z, -1) * CF
                    + 6 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
                    + (-1) * 6 * pow(ln(x), 2) * NC * CF
                    + (-1) * 3 * pow(ln(x), 2) * NC * z * CF * pow(omx, -1)
                    + 3 * pow(ln(x), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * 6 * pow(ln(x), 2) * NC * x * CF
                    + 6 * pow(ln(x), 2) * NC * x * z * CF
                    + 10 * ln(x) * ln(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(z) * NC * pow(z, -1) * CF
                    + (-1) * 10 * ln(x) * ln(z) * NC * CF * pow(omx, -1)
                    + 10 * ln(x) * ln(z) * NC * CF
                    + 5 * ln(x) * ln(z) * NC * z * CF * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(z) * NC * x * pow(z, -1) * CF
                    + 10 * ln(x) * ln(z) * NC * x * CF
                    + (-1) * 10 * ln(x) * ln(z) * NC * x * z * CF
                    + 10 * ln(x) * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(omx) * NC * pow(z, -1) * CF
                    + (-1) * 10 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
                    + 10 * ln(x) * ln(omx) * NC * CF
                    + 5 * ln(x) * ln(omx) * NC * z * CF * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(omx) * NC * x * pow(z, -1) * CF
                    + 10 * ln(x) * ln(omx) * NC * x * CF
                    + (-1) * 10 * ln(x) * ln(omx) * NC * x * z * CF
                    + 8 * ln(x) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * NC * pow(z, -1) * CF
                    + (-1) * 8 * ln(x) * ln(omz) * NC * CF * pow(omx, -1)
                    + 8 * ln(x) * ln(omz) * NC * CF
                    + 0
                )
                tmp += (
                    +4 * ln(x) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + (-1) * 4 * ln(x) * ln(omz) * NC * x * pow(z, -1) * CF
                    + 8 * ln(x) * ln(omz) * NC * x * CF
                    + (-1) * 8 * ln(x) * ln(omz) * NC * x * z * CF
                    + (-1) * 2 * ln(x) * ln(xmz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + ln(x) * ln(xmz) * NC * pow(z, -1) * CF
                    + 2 * ln(x) * ln(xmz) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(xmz) * NC * CF
                    + (-1) * ln(x) * ln(xmz) * NC * z * CF * pow(omx, -1)
                    + ln(x) * ln(xmz) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * ln(xmz) * NC * x * CF
                    + 2 * ln(x) * ln(xmz) * NC * x * z * CF
                    + (-1) * 4 * ln(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(z) * NC * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * NC * CF
                    + (-1) * 4 * ln(z) * NC * z * CF * pow(omx, -1)
                    + 4 * ln(z) * NC * x * pow(z, -1) * CF
                    + 4 * ln(z) * NC * x * z * CF
                    + (-1) * 4 * pow(ln(z), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * pow(ln(z), 2) * NC * pow(z, -1) * CF
                    + 4 * pow(ln(z), 2) * NC * CF * pow(omx, -1)
                    + (-1) * 4 * pow(ln(z), 2) * NC * CF
                    + (-1) * 2 * pow(ln(z), 2) * NC * z * CF * pow(omx, -1)
                    + 2 * pow(ln(z), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * pow(ln(z), 2) * NC * x * CF
                    + 4 * pow(ln(z), 2) * NC * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(omx) * NC * pow(z, -1) * CF
                    + 8 * ln(z) * ln(omx) * NC * CF * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(omx) * NC * CF
                    + (-1) * 4 * ln(z) * ln(omx) * NC * z * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(omx) * NC * x * pow(z, -1) * CF
                    + (-1) * 8 * ln(z) * ln(omx) * NC * x * CF
                    + 8 * ln(z) * ln(omx) * NC * x * z * CF
                    + (-1) * 4 * ln(z) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(omz) * NC * pow(z, -1) * CF
                    + 4 * ln(z) * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(omz) * NC * CF
                    + (-1) * 2 * ln(z) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * ln(z) * ln(omz) * NC * x * CF
                    + 4 * ln(z) * ln(omz) * NC * x * z * CF
                    + 2 * ln(z) * ln(xmz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * ln(z) * ln(xmz) * NC * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * NC * CF * pow(omx, -1)
                    + 2 * ln(z) * ln(xmz) * NC * CF
                    + ln(z) * ln(xmz) * NC * z * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(xmz) * NC * x * pow(z, -1) * CF
                    + 2 * ln(z) * ln(xmz) * NC * x * CF
                    + (-1) * 2 * ln(z) * ln(xmz) * NC * x * z * CF
                    + (-1) * 4 * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(omx) * NC * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omx) * NC * CF
                    + (-1) * 4 * ln(omx) * NC * z * CF * pow(omx, -1)
                    + 4 * ln(omx) * NC * x * pow(z, -1) * CF
                    + 4 * ln(omx) * NC * x * z * CF
                    + (-1) * 4 * pow(ln(omx), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * pow(ln(omx), 2) * NC * pow(z, -1) * CF
                    + 4 * pow(ln(omx), 2) * NC * CF * pow(omx, -1)
                    + (-1) * 4 * pow(ln(omx), 2) * NC * CF
                    + (-1) * 2 * pow(ln(omx), 2) * NC * z * CF * pow(omx, -1)
                    + 2 * pow(ln(omx), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * pow(ln(omx), 2) * NC * x * CF
                    + 4 * pow(ln(omx), 2) * NC * x * z * CF
                    + (-1) * 4 * ln(omx) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * ln(omx) * ln(omz) * NC * pow(z, -1) * CF
                    + 4 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 4 * ln(omx) * ln(omz) * NC * CF
                    + (-1) * 2 * ln(omx) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(omx) * ln(omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * ln(omx) * ln(omz) * NC * x * CF
                    + 4 * ln(omx) * ln(omz) * NC * x * z * CF
                    + (-1) * 2 * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 3 * ln(omz) * NC * CF
                    + (-1) * 2 * ln(omz) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(omz) * NC * x * pow(z, -1) * CF
                    + 2 * ln(omz) * NC * x * z * CF
                    + (-1) * pow(ln(omz), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * NC * pow(z, -1) * CF
                    + pow(ln(omz), 2) * NC * CF * pow(omx, -1)
                    + (-1) * pow(ln(omz), 2) * NC * CF
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * NC * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * pow(ln(omz), 2) * NC * x * CF
                    + pow(ln(omz), 2) * NC * x * z * CF
                    + 0
                )
                tmp += (
                    +2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * pow(z, -1) * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * CF * pow(omx, -1)
                    + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * CF
                    + Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * z * CF * pow(omx, -1)
                    + (-1) * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * x * pow(z, -1) * CF
                    + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * x * CF
                    + (-1) * 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * x * z * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(omx * pow(omz, -1)) * NC * pow(z, -1) * CF
                    + 2 * Li2(omx * pow(omz, -1)) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * NC * CF
                    + (-1) * Li2(omx * pow(omz, -1)) * NC * z * CF * pow(omx, -1)
                    + Li2(omx * pow(omz, -1)) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(omx * pow(omz, -1)) * NC * x * CF
                    + 2 * Li2(omx * pow(omz, -1)) * NC * x * z * CF
                    + 2 * Li2(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(z) * NC * pow(z, -1) * CF
                    + (-1) * 2 * Li2(z) * NC * CF * pow(omx, -1)
                    + 2 * Li2(z) * NC * CF
                    + Li2(z) * NC * z * CF * pow(omx, -1)
                    + (-1) * Li2(z) * NC * x * pow(z, -1) * CF
                    + 2 * Li2(z) * NC * x * CF
                    + (-1) * 2 * Li2(z) * NC * x * z * CF
                    + 0
                )
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
                    +(-1) * 9 * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * pow(NC, -1) * pow(z, -1) * pow(rln2, 2) * CF * pow(omx, -1)
                    + 2 * pow(NC, -1) * pow(z, -1) * pow(rln2, 2) * CF
                    + (-1) * 6 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * CF * pow(omx, -1)
                    + 4 * pow(NC, -1) * pow(z, -1) * sqrtxz1 * rln2 * CF
                    + 8.0 / 3.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 13.0 / 12.0 * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF
                    + 41.0 / 4.0 * pow(NC, -1) * CF
                    + 4 * pow(NC, -1) * pow(rln2, 2) * CF * pow(omx, -1)
                    + 2 * pow(NC, -1) * sqrtxz1 * rln2 * CF * pow(omx, -1)
                    + (-1) * 10.0 / 3.0 * pow(NC, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + 7.0 / 6.0 * pow(NC, -1) * pow(pi, 2) * CF
                    + (-1) * 4 * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(NC, -1) * z * CF
                    + (-1) * 2 * pow(NC, -1) * z * pow(rln2, 2) * CF * pow(omx, -1)
                    + 5.0 / 3.0 * pow(NC, -1) * z * pow(pi, 2) * CF * pow(omx, -1)
                    + (-1) * 1.0 / 6.0 * pow(NC, -1) * z * pow(pi, 2) * CF
                    + 4 * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * pow(NC, -1) * x * pow(z, -1) * pow(rln2, 2) * CF
                    + 2 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF
                    + (-1) * 29.0 / 12.0 * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 2 * pow(NC, -1) * x * CF * pow(omxmz, -1)
                    + 23.0 / 4.0 * pow(NC, -1) * x * CF
                    + 2 * pow(NC, -1) * x * sqrtxz1 * rln2 * CF
                    + 25.0 / 6.0 * pow(NC, -1) * x * pow(pi, 2) * CF
                    + (-1) * 11.0 / 2.0 * pow(NC, -1) * x * z * CF
                    + (-1) * 5.0 / 2.0 * pow(NC, -1) * x * z * pow(pi, 2) * CF
                    + 2 * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1)
                    + (-1) * 2 * pow(NC, -1) * pow(x, 2) * CF
                    + (-1) * 2 * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1)
                    + 215.0 / 18.0 * NC * pow(z, -1) * CF
                    + (-1) * 2 * NC * pow(z, -1) * pow(pi, 2) * CF * pow(omx, -1)
                    + 17.0 / 12.0 * NC * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 163.0 / 12.0 * NC * CF
                    + (-1) * 8 * NC * pow(rln2, 2) * CF * pow(omx, -1)
                    + 4 * NC * pow(rln2, 2) * CF
                    + (-1) * 4 * NC * sqrtxz1 * rln2 * CF * pow(omx, -1)
                    + 4.0 / 3.0 * NC * pow(pi, 2) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 1.0 / 2.0 * NC * pow(pi, 2) * CF
                    + NC * z * CF * pow(omx, -1)
                    + 4.0 / 3.0 * NC * z * CF
                    + (-1) * NC * z * pow(pi, 2) * CF * pow(omx, -1)
                    + 1.0 / 6.0 * NC * z * pow(pi, 2) * CF
                    + (-1) * 31.0 / 9.0 * NC * pow(z, 2) * CF
                    + (-1) * 43.0 / 18.0 * NC * x * pow(z, -1) * CF
                    + 17.0 / 12.0 * NC * x * pow(z, -1) * pow(pi, 2) * CF
                    + (-1) * 37.0 / 12.0 * NC * x * CF
                    + 4 * NC * x * pow(rln2, 2) * CF
                    + 4 * NC * x * sqrtxz1 * rln2 * CF
                    + (-1) * 5.0 / 6.0 * NC * x * pow(pi, 2) * CF
                    + 1.0 / 3.0 * NC * x * z * CF
                    + 4 * NC * x * z * pow(rln2, 2) * CF
                    + 5.0 / 2.0 * NC * x * z * pow(pi, 2) * CF
                    + 53.0 / 9.0 * NC * x * pow(z, 2) * CF
                    + 0
                )
                tmp += (
                    +8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * rln2 * CF * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * rln2 * CF
                    + 6 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF
                    + (-1) * 8 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * rln2 * CF * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * sqrtxz1 * CF * pow(omx, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * rln2 * CF * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * sqrtxz1 * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * NC * pow(z, -1) * rln2 * CF * pow(omx, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * NC * pow(z, -1) * rln2 * CF
                    + 12 * ln(1 + sqrtxz1 - z) * NC * rln2 * CF * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * NC * rln2 * CF
                    + 4 * ln(1 + sqrtxz1 - z) * NC * sqrtxz1 * CF * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * NC * z * rln2 * CF * pow(omx, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1) * rln2 * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * NC * x * rln2 * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * NC * x * sqrtxz1 * CF
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(1 + sqrtxz1 - z) * NC * x * z * rln2 * CF
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * pow(z, -1) * CF
                    + (-1) * 4 * pow(ln(1 + sqrtxz1 - z), 2) * NC * CF * pow(omx, -1)
                    + 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * z * CF * pow(omx, -1)
                    + (-1) * 2 * pow(ln(1 + sqrtxz1 - z), 2) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1) * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * CF * pow(omx, -1)
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * CF
                    + (-1) * 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * pow(z, -1) * CF
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * CF
                    + 4 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * z * CF
                    + 4 * ln(1 + sqrtxz1 + z) * NC * pow(z, -1) * rln2 * CF * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * NC * pow(z, -1) * rln2 * CF
                    + 4 * ln(1 + sqrtxz1 + z) * NC * rln2 * CF * pow(omx, -1)
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * NC * rln2 * CF
                    + 2 * ln(1 + sqrtxz1 + z) * NC * z * rln2 * CF * pow(omx, -1)
                    + (-1) * 2 * ln(1 + sqrtxz1 + z) * NC * x * pow(z, -1) * rln2 * CF
                    + (-1) * 4 * ln(1 + sqrtxz1 + z) * NC * x * rln2 * CF
                    + 0
                )
                tmp += (
                    +(-1) * 4 * ln(1 + sqrtxz1 + z) * NC * x * z * rln2 * CF
                    + 12 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 1.0 / 4.0 * ln(x) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 6 * ln(x) * pow(NC, -1) * pow(z, -1) * rln2 * CF * pow(omx, -1)
                    + 3 * ln(x) * pow(NC, -1) * pow(z, -1) * rln2 * CF
                    + (-1) * 3 * ln(x) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF * pow(omx, -1)
                    + 2 * ln(x) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF
                    + (-1) * 12 * ln(x) * pow(NC, -1) * CF * pow(omx, -1)
                    + ln(x) * pow(NC, -1) * CF
                    + 6 * ln(x) * pow(NC, -1) * rln2 * CF * pow(omx, -1)
                    + ln(x) * pow(NC, -1) * sqrtxz1 * CF * pow(omx, -1)
                    + 51.0 / 4.0 * ln(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * pow(NC, -1) * z * CF
                    + (-1) * 3 * ln(x) * pow(NC, -1) * z * rln2 * CF * pow(omx, -1)
                    + (-1) * 43.0 / 4.0 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 3 * ln(x) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF
                    + ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                    + 4 * ln(x) * pow(NC, -1) * x * CF
                    + 4 * ln(x) * pow(NC, -1) * x * CF * omx
                    + ln(x) * pow(NC, -1) * x * sqrtxz1 * CF
                    + (-1) * 15.0 / 2.0 * ln(x) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * ln(x) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -2)
                    + 2 * ln(x) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1)
                    + 2 * ln(x) * pow(NC, -1) * pow(x, 2) * CF
                    + 2 * ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -2)
                    + (-1) * 4 * ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1)
                    + (-1) * 2 * ln(x) * pow(NC, -1) * pow(x, 4) * CF * pow(omxmz, -2)
                    + 35.0 / 3.0 * ln(x) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 163.0 / 12.0 * ln(x) * NC * pow(z, -1) * CF
                    + 4 * ln(x) * NC * pow(z, -1) * rln2 * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * NC * pow(z, -1) * rln2 * CF
                    + (-1) * 4 * ln(x) * NC * CF * pow(omx, -1)
                    + ln(x) * NC * CF
                    + (-1) * 8 * ln(x) * NC * rln2 * CF * pow(omx, -1)
                    + 2 * ln(x) * NC * rln2 * CF
                    + (-1) * 2 * ln(x) * NC * sqrtxz1 * CF * pow(omx, -1)
                    + (-1) * 51.0 / 4.0 * ln(x) * NC * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +13.0 / 2.0 * ln(x) * NC * z * CF
                    + 2 * ln(x) * NC * z * rln2 * CF * pow(omx, -1)
                    + (-1) * 8.0 / 3.0 * ln(x) * NC * pow(z, 2) * CF * pow(omx, -1)
                    + (-1) * 8.0 / 3.0 * ln(x) * NC * pow(z, 2) * CF
                    + (-1) * 67.0 / 12.0 * ln(x) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * NC * x * pow(z, -1) * rln2 * CF
                    + 5 * ln(x) * NC * x * CF
                    + 2 * ln(x) * NC * x * rln2 * CF
                    + 2 * ln(x) * NC * x * sqrtxz1 * CF
                    + 13.0 / 2.0 * ln(x) * NC * x * z * CF
                    + 2 * ln(x) * NC * x * z * rln2 * CF
                    + 16.0 / 3.0 * ln(x) * NC * x * pow(z, 2) * CF
                    + 0
                )
                tmp += (
                    +4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * pow(z, -1) * CF
                    + 4 * ln(x) * ln(1 + sqrtxz1 - z) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(x) * ln(1 + sqrtxz1 - z) * NC * x * pow(z, -1) * CF
                    + 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * CF * pow(omx, -1)
                    + ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * ln(x) * ln(1 + sqrtxz1 + z) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * CF
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * CF
                    + (-1) * 2 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * z * CF
                    + (-1) * 17 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 11.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + 24 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 9 * pow(ln(x), 2) * pow(NC, -1) * CF
                    + (-1) * 12 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +1.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * z * CF
                    + 25.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 23 * pow(ln(x), 2) * pow(NC, -1) * x * CF
                    + 31.0 / 2.0 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF
                    + 10 * pow(ln(x), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 11.0 / 2.0 * pow(ln(x), 2) * NC * pow(z, -1) * CF
                    + (-1) * 10 * pow(ln(x), 2) * NC * CF * pow(omx, -1)
                    + 9 * pow(ln(x), 2) * NC * CF
                    + 5 * pow(ln(x), 2) * NC * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(x), 2) * NC * z * CF
                    + (-1) * 11.0 / 2.0 * pow(ln(x), 2) * NC * x * pow(z, -1) * CF
                    + 9 * pow(ln(x), 2) * NC * x * CF
                    + (-1) * 17.0 / 2.0 * pow(ln(x), 2) * NC * x * z * CF
                    + 16 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 25 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + 10 * ln(x) * ln(z) * pow(NC, -1) * CF
                    + 25.0 / 2.0 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 11 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 20 * ln(x) * ln(z) * pow(NC, -1) * x * CF
                    + (-1) * 17 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF
                    + (-1) * 6 * ln(x) * ln(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 3 * ln(x) * ln(z) * NC * pow(z, -1) * CF
                    + 19 * ln(x) * ln(z) * NC * CF * pow(omx, -1)
                    + (-1) * 18 * ln(x) * ln(z) * NC * CF
                    + 7.0 / 2.0 * ln(x) * ln(z) * NC * z * CF * pow(omx, -1)
                    + 3 * ln(x) * ln(z) * NC * x * pow(z, -1) * CF
                    + (-1) * 16 * ln(x) * ln(z) * NC * x * CF
                    + (-1) * ln(x) * ln(z) * NC * x * z * CF
                    + 20 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 26 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 10 * ln(x) * ln(omx) * pow(NC, -1) * CF
                    + 13 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(omx) * pow(NC, -1) * z * CF
                    + (-1) * 15 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 30 * ln(x) * ln(omx) * pow(NC, -1) * x * CF
                    + 0
                )
                tmp += (
                    +(-1) * 19 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF
                    + (-1) * 16 * ln(x) * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 8 * ln(x) * ln(omx) * NC * pow(z, -1) * CF
                    + 16 * ln(x) * ln(omx) * NC * CF * pow(omx, -1)
                    + (-1) * 16 * ln(x) * ln(omx) * NC * CF
                    + (-1) * 8 * ln(x) * ln(omx) * NC * z * CF * pow(omx, -1)
                    + ln(x) * ln(omx) * NC * z * CF
                    + 8 * ln(x) * ln(omx) * NC * x * pow(z, -1) * CF
                    + (-1) * 16 * ln(x) * ln(omx) * NC * x * CF
                    + 15 * ln(x) * ln(omx) * NC * x * z * CF
                    + 24 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 15.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 34 * ln(x) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + 13 * ln(x) * ln(omz) * pow(NC, -1) * CF
                    + 17 * ln(x) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(x) * ln(omz) * pow(NC, -1) * z * CF
                    + (-1) * 35.0 / 2.0 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 33 * ln(x) * ln(omz) * pow(NC, -1) * x * CF
                    + (-1) * 22 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF
                    + (-1) * 14 * ln(x) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 15.0 / 2.0 * ln(x) * ln(omz) * NC * pow(z, -1) * CF
                    + 14 * ln(x) * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 13 * ln(x) * ln(omz) * NC * CF
                    + (-1) * 7 * ln(x) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + ln(x) * ln(omz) * NC * z * CF
                    + 15.0 / 2.0 * ln(x) * ln(omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 13 * ln(x) * ln(omz) * NC * x * CF
                    + 12 * ln(x) * ln(omz) * NC * x * z * CF
                    + (-1) * 3 * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * ln(z) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * pow(NC, -1) * pow(z, -1) * rln2 * CF * pow(omx, -1)
                    + ln(z) * pow(NC, -1) * pow(z, -1) * rln2 * CF
                    + (-1) * 3 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF * pow(omx, -1)
                    + 2 * ln(z) * pow(NC, -1) * pow(z, -1) * sqrtxz1 * CF
                    + 8 * ln(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * pow(NC, -1) * CF
                    + 2 * ln(z) * pow(NC, -1) * rln2 * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +ln(z) * pow(NC, -1) * sqrtxz1 * CF * pow(omx, -1)
                    + (-1) * 7 * ln(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(z) * pow(NC, -1) * z * CF
                    + (-1) * ln(z) * pow(NC, -1) * z * rln2 * CF * pow(omx, -1)
                    + 5 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + ln(z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF
                    + ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF
                    + (-1) * 7 * ln(z) * pow(NC, -1) * x * CF
                    + ln(z) * pow(NC, -1) * x * sqrtxz1 * CF
                    + 9 * ln(z) * pow(NC, -1) * x * z * CF
                    + 4 * ln(z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 44.0 / 3.0 * ln(z) * NC * pow(z, -1) * CF
                    + (-1) * 4 * ln(z) * NC * pow(z, -1) * rln2 * CF * pow(omx, -1)
                    + 2 * ln(z) * NC * pow(z, -1) * rln2 * CF
                    + (-1) * 2 * ln(z) * NC * CF * pow(omx, -1)
                    + 14 * ln(z) * NC * CF
                    + (-1) * 8 * ln(z) * NC * rln2 * CF * pow(omx, -1)
                    + 6 * ln(z) * NC * rln2 * CF
                    + (-1) * 2 * ln(z) * NC * sqrtxz1 * CF * pow(omx, -1)
                    + 6 * ln(z) * NC * z * CF * pow(omx, -1)
                    + 2 * ln(z) * NC * z * CF
                    + (-1) * 2 * ln(z) * NC * z * rln2 * CF * pow(omx, -1)
                    + 4.0 / 3.0 * ln(z) * NC * pow(z, 2) * CF
                    + 11.0 / 3.0 * ln(z) * NC * x * pow(z, -1) * CF
                    + 2 * ln(z) * NC * x * pow(z, -1) * rln2 * CF
                    + (-1) * 2 * ln(z) * NC * x * CF
                    + 6 * ln(z) * NC * x * rln2 * CF
                    + 2 * ln(z) * NC * x * sqrtxz1 * CF
                    + (-1) * 13 * ln(z) * NC * x * z * CF
                    + 6 * ln(z) * NC * x * z * rln2 * CF
                    + (-1) * 8.0 / 3.0 * ln(z) * NC * x * pow(z, 2) * CF
                    + 0
                )
                tmp += (
                    +2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * CF * pow(omx, -1)
                    + ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * ln(z) * ln(1 + sqrtxz1 - z) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * CF
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * CF
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * z * CF
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * pow(z, -1) * CF
                    + 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * CF
                    + 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * z * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * pow(z, -1) * CF
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * CF
                    + (-1) * 4 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * z * CF
                    + (-1) * 4 * ln(z) * ln(1 + z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 4 * ln(z) * ln(1 + z) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * ln(z) * ln(1 + z) * NC * z * CF * pow(omx, -1)
                    + (-1) * 3 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + 6 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 4 * pow(ln(z), 2) * pow(NC, -1) * CF
                    + (-1) * 3 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * z * CF
                    + 0
                )
                tmp += (
                    +2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * pow(ln(z), 2) * pow(NC, -1) * x * CF
                    + 9.0 / 2.0 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF
                    + pow(ln(z), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 5.0 / 2.0 * pow(ln(z), 2) * NC * pow(z, -1) * CF
                    + (-1) * 3 * pow(ln(z), 2) * NC * CF * pow(omx, -1)
                    + 9 * pow(ln(z), 2) * NC * CF
                    + 1.0 / 2.0 * pow(ln(z), 2) * NC * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(z), 2) * NC * z * CF
                    + 5.0 / 2.0 * pow(ln(z), 2) * NC * x * pow(z, -1) * CF
                    + 7 * pow(ln(z), 2) * NC * x * CF
                    + 15.0 / 2.0 * pow(ln(z), 2) * NC * x * z * CF
                    + (-1) * 8 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 3 * ln(z) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 12 * ln(z) * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 6 * ln(z) * ln(omx) * pow(NC, -1) * CF
                    + (-1) * 6 * ln(z) * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 7 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(z) * ln(omx) * pow(NC, -1) * x * CF
                    + 9 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF
                    + 8 * ln(z) * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3 * ln(z) * ln(omx) * NC * pow(z, -1) * CF
                    + (-1) * 8 * ln(z) * ln(omx) * NC * CF * pow(omx, -1)
                    + 14 * ln(z) * ln(omx) * NC * CF
                    + 4 * ln(z) * ln(omx) * NC * z * CF * pow(omx, -1)
                    + (-1) * 3 * ln(z) * ln(omx) * NC * x * pow(z, -1) * CF
                    + 12 * ln(z) * ln(omx) * NC * x * CF
                    + (-1) * ln(z) * ln(omx) * NC * x * z * CF
                    + (-1) * 12 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 20 * ln(z) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(z) * ln(omz) * pow(NC, -1) * CF
                    + (-1) * 10 * ln(z) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 6 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 12 * ln(z) * ln(omz) * pow(NC, -1) * x * CF
                    + 10 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(z) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 5 * ln(z) * ln(omz) * NC * pow(z, -1) * CF
                    + (-1) * 4 * ln(z) * ln(omz) * NC * CF * pow(omx, -1)
                    + 10 * ln(z) * ln(omz) * NC * CF
                    + 2 * ln(z) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + (-1) * 5 * ln(z) * ln(omz) * NC * x * pow(z, -1) * CF
                    + 10 * ln(z) * ln(omz) * NC * x * CF
                    + (-1) * 10 * ln(z) * ln(omz) * NC * x * z * CF
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 11.0 / 4.0 * ln(omx) * pow(NC, -1) * pow(z, -1) * CF
                    + 6 * ln(omx) * pow(NC, -1) * CF * pow(omx, -1)
                    + 4 * ln(omx) * pow(NC, -1) * CF
                    + (-1) * 6 * ln(omx) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * ln(omx) * pow(NC, -1) * z * CF
                    + 17.0 / 4.0 * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 3 * ln(omx) * pow(NC, -1) * x * CF
                    + 4 * ln(omx) * pow(NC, -1) * x * z * CF
                    + 4 * ln(omx) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 125.0 / 12.0 * ln(omx) * NC * pow(z, -1) * CF
                    + (-1) * 4 * ln(omx) * NC * CF * pow(omx, -1)
                    + (-1) * 3 * ln(omx) * NC * CF
                    + 4 * ln(omx) * NC * z * CF * pow(omx, -1)
                    + (-1) * 7.0 / 2.0 * ln(omx) * NC * z * CF
                    + 4.0 / 3.0 * ln(omx) * NC * pow(z, 2) * CF
                    + 41.0 / 12.0 * ln(omx) * NC * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(omx) * NC * x * CF
                    + (-1) * 3 * ln(omx) * NC * x * z * CF
                    + (-1) * 8.0 / 3.0 * ln(omx) * NC * x * pow(z, 2) * CF
                    + 0
                )
                tmp += (
                    +(-1) * 5 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * pow(ln(omx), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + 6 * pow(ln(omx), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 3 * pow(ln(omx), 2) * pow(NC, -1) * CF
                    + (-1) * 3 * pow(ln(omx), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * z * CF
                    + 6 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 11 * pow(ln(omx), 2) * pow(NC, -1) * x * CF
                    + 13.0 / 2.0 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF
                    + 4 * pow(ln(omx), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 7.0 / 2.0 * pow(ln(omx), 2) * NC * pow(z, -1) * CF
                    + (-1) * 4 * pow(ln(omx), 2) * NC * CF * pow(omx, -1)
                    + 6 * pow(ln(omx), 2) * NC * CF
                    + 2 * pow(ln(omx), 2) * NC * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omx), 2) * NC * z * CF
                    + (-1) * 7.0 / 2.0 * pow(ln(omx), 2) * NC * x * pow(z, -1) * CF
                    + 6 * pow(ln(omx), 2) * NC * x * CF
                    + (-1) * 11.0 / 2.0 * pow(ln(omx), 2) * NC * x * z * CF
                    + (-1) * 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 5 * ln(omx) * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 16 * ln(omx) * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 8 * ln(omx) * ln(omz) * pow(NC, -1) * CF
                    + (-1) * 8 * ln(omx) * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + ln(omx) * ln(omz) * pow(NC, -1) * z * CF
                    + 11 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 20 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF
                    + 13 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF
                    + 4 * ln(omx) * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 0
                )
                tmp += (
                    +(-1) * 6 * ln(omx) * ln(omz) * NC * pow(z, -1) * CF
                    + (-1) * 4 * ln(omx) * ln(omz) * NC * CF * pow(omx, -1)
                    + 10 * ln(omx) * ln(omz) * NC * CF
                    + 2 * ln(omx) * ln(omz) * NC * z * CF * pow(omx, -1)
                    + (-1) * ln(omx) * ln(omz) * NC * z * CF
                    + (-1) * 6 * ln(omx) * ln(omz) * NC * x * pow(z, -1) * CF
                    + 10 * ln(omx) * ln(omz) * NC * x * CF
                    + (-1) * 9 * ln(omx) * ln(omz) * NC * x * z * CF
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 11.0 / 4.0 * ln(omz) * pow(NC, -1) * pow(z, -1) * CF
                    + 8 * ln(omz) * pow(NC, -1) * CF * pow(omx, -1)
                    + ln(omz) * pow(NC, -1) * CF
                    + (-1) * 8 * ln(omz) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 2 * ln(omz) * pow(NC, -1) * z * CF
                    + 25.0 / 4.0 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * ln(omz) * pow(NC, -1) * x * CF * omx
                    + 9.0 / 2.0 * ln(omz) * pow(NC, -1) * x * z * CF
                    + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -2)
                    + (-1) * 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1)
                    + (-1) * 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF
                    + (-1) * 2 * ln(omz) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -2)
                    + 4 * ln(omz) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1)
                    + 2 * ln(omz) * pow(NC, -1) * pow(x, 4) * CF * pow(omxmz, -2)
                    + 2 * ln(omz) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 125.0 / 12.0 * ln(omz) * NC * pow(z, -1) * CF
                    + (-1) * 2 * ln(omz) * NC * CF * pow(omx, -1)
                    + (-1) * 6 * ln(omz) * NC * CF
                    + 2 * ln(omz) * NC * z * CF * pow(omx, -1)
                    + (-1) * 5 * ln(omz) * NC * z * CF
                    + 4.0 / 3.0 * ln(omz) * NC * pow(z, 2) * CF
                    + 65.0 / 12.0 * ln(omz) * NC * x * pow(z, -1) * CF
                    + (-1) * 6 * ln(omz) * NC * x * CF
                    + 1.0 / 2.0 * ln(omz) * NC * x * z * CF
                    + (-1) * 8.0 / 3.0 * ln(omz) * NC * x * pow(z, 2) * CF
                    + 0
                )
                tmp += (
                    +(-1) * 8 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 3 * pow(ln(omz), 2) * pow(NC, -1) * pow(z, -1) * CF
                    + 12 * pow(ln(omz), 2) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 5 * pow(ln(omz), 2) * pow(NC, -1) * CF
                    + (-1) * 6 * pow(ln(omz), 2) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * z * CF
                    + 7 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 13 * pow(ln(omz), 2) * pow(NC, -1) * x * CF
                    + 17.0 / 2.0 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF
                    + pow(ln(omz), 2) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 5.0 / 2.0 * pow(ln(omz), 2) * NC * pow(z, -1) * CF
                    + (-1) * pow(ln(omz), 2) * NC * CF * pow(omx, -1)
                    + 4 * pow(ln(omz), 2) * NC * CF
                    + 1.0 / 2.0 * pow(ln(omz), 2) * NC * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * pow(ln(omz), 2) * NC * z * CF
                    + (-1) * 5.0 / 2.0 * pow(ln(omz), 2) * NC * x * pow(z, -1) * CF
                    + 4 * pow(ln(omz), 2) * NC * x * CF
                    + (-1) * 7.0 / 2.0 * pow(ln(omz), 2) * NC * x * z * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF
                    + 0
                )
                tmp += (
                    +(-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(z, -1) * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * z * CF * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * pow(z, -1) * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * z * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(z, -1) * CF
                    + 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * pow(z, -1) * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * CF
                    + 0
                )
                tmp += (
                    +2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 + 1.0 / 2.0 * pow(z, -1) - 1.0 / 2.0 * pow(z, -1) * sqrtxz1) * NC * x * z * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * CF * pow(omx, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 - 1.0 / 2.0 * z) * NC * x * z * CF
                    + (-1) * 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * pow(z, -1) * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 4 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * CF * pow(omx, -1)
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * CF
                    + 2 * Li2(1.0 / 2.0 - 1.0 / 2.0 * sqrtxz1 + 1.0 / 2.0 * z) * NC * x * z * CF
                    + 0
                )
                tmp += (
                    +2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * CF * pow(omx, -1)
                    + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * CF
                    + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * CF
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * z * CF
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + Li2(1 - x * pow(z, -1)) * NC * pow(z, -1) * CF
                    + 2 * Li2(1 - x * pow(z, -1)) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * NC * CF
                    + (-1) * Li2(1 - x * pow(z, -1)) * NC * z * CF * pow(omx, -1)
                    + Li2(1 - x * pow(z, -1)) * NC * x * pow(z, -1) * CF
                    + (-1) * 2 * Li2(1 - x * pow(z, -1)) * NC * x * CF
                    + 2 * Li2(1 - x * pow(z, -1)) * NC * x * z * CF
                    + (-1) * 4 * Li2(-z) * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 4 * Li2(-z) * NC * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(-z) * NC * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 3.0 / 2.0 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF
                    + 2 * Li2(x) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * Li2(x) * pow(NC, -1) * CF
                    + (-1) * Li2(x) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 3.0 / 2.0 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * Li2(x) * pow(NC, -1) * x * CF
                    + Li2(x) * pow(NC, -1) * x * z * CF
                    + (-1) * 1.0 / 2.0 * Li2(x) * NC * pow(z, -1) * CF
                    + (-1) * Li2(x) * NC * CF
                    + (-1) * 1.0 / 2.0 * Li2(x) * NC * x * pow(z, -1) * CF
                    + (-1) * Li2(x) * NC * x * CF
                    + Li2(x) * NC * x * z * CF
                    + (-1) * 4 * Li2(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 6 * Li2(z) * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 3 * Li2(z) * pow(NC, -1) * z * CF * pow(omx, -1)
                    + (-1) * 2 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF
                    + 2 * Li2(z) * pow(NC, -1) * x * CF
                    + 0
                )
                tmp += +(-1) * Li2(z) * pow(NC, -1) * x * z * CF + (-1) * 3 * Li2(z) * NC * pow(z, -1) * CF + (-1) * 2 * Li2(z) * NC * CF + (-1) * 3 * Li2(z) * NC * x * pow(z, -1) * CF + (-1) * 11 * Li2(z) * NC * x * z * CF + 0
            if "001" == order:
                tmp += (
                    3 * LMUA * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * 5.0 / 2.0 * LMUA * pow(NC, -1) * CF
                    + (-1) * 3.0 / 2.0 * LMUA * pow(NC, -1) * x * CF
                    + LMUA * pow(NC, -1) * x * z * CF
                    + (-1) * 53.0 / 6.0 * LMUA * NC * pow(z, -1) * CF
                    + 29.0 / 6.0 * LMUA * NC * CF
                    + 3 * LMUA * NC * z * CF
                    + (-1) * 4.0 / 3.0 * LMUA * NC * pow(z, 2) * CF
                    + (-1) * 23.0 / 6.0 * LMUA * NC * x * pow(z, -1) * CF
                    + (-1) * 1.0 / 6.0 * LMUA * NC * x * CF
                    + 11.0 / 3.0 * LMUA * NC * x * z * CF
                    + 8.0 / 3.0 * LMUA * NC * x * pow(z, 2) * CF
                    + (-1) * 1.0 / 3.0 * LMUA * NF * pow(z, -1) * CF
                    + 2.0 / 3.0 * LMUA * NF * CF
                    + (-1) * 1.0 / 3.0 * LMUA * NF * x * pow(z, -1) * CF
                    + 0
                )
                tmp += 2.0 / 3.0 * LMUA * NF * x * CF + (-1) * 2.0 / 3.0 * LMUA * NF * x * z * CF + 0
                tmp += (
                    (-1) * 2 * ln(x) * LMUA * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + ln(x) * LMUA * pow(NC, -1) * pow(z, -1) * CF
                    + 2 * ln(x) * LMUA * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * LMUA * pow(NC, -1) * CF
                    + (-1) * ln(x) * LMUA * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * z * CF
                    + ln(x) * LMUA * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * ln(x) * LMUA * pow(NC, -1) * x * CF
                    + 1.0 / 2.0 * ln(x) * LMUA * pow(NC, -1) * x * z * CF
                    + 2 * ln(x) * LMUA * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * ln(x) * LMUA * NC * pow(z, -1) * CF
                    + 0
                )
                tmp += (-1) * 2 * ln(x) * LMUA * NC * CF * pow(omx, -1) + ln(x) * LMUA * NC * CF + ln(x) * LMUA * NC * z * CF * pow(omx, -1) + (-1) * 1.0 / 2.0 * ln(x) * LMUA * NC * z * CF + (-1) * ln(x) * LMUA * NC * x * pow(z, -1) * CF + ln(x) * LMUA * NC * x * CF + (-1) * 1.0 / 2.0 * ln(x) * LMUA * NC * x * z * CF + 0
                tmp += ln(z) * LMUA * pow(NC, -1) * CF + 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * z * CF + (-1) * ln(z) * LMUA * pow(NC, -1) * x * CF + 0
                tmp += (-1) * 1.0 / 2.0 * ln(z) * LMUA * pow(NC, -1) * x * z * CF + (-1) * 2 * ln(z) * LMUA * NC * pow(z, -1) * CF + (-1) * 5 * ln(z) * LMUA * NC * CF + (-1) * 1.0 / 2.0 * ln(z) * LMUA * NC * z * CF + (-1) * 2 * ln(z) * LMUA * NC * x * pow(z, -1) * CF + (-1) * 3 * ln(z) * LMUA * NC * x * CF + (-1) * 15.0 / 2.0 * ln(z) * LMUA * NC * x * z * CF + 0
                tmp += (-1) * ln(omx) * LMUA * pow(NC, -1) * pow(z, -1) * CF + ln(omx) * LMUA * pow(NC, -1) * CF + (-1) * 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * z * CF + 0
                tmp += (
                    (-1) * ln(omx) * LMUA * pow(NC, -1) * x * pow(z, -1) * CF
                    + ln(omx) * LMUA * pow(NC, -1) * x * CF
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUA * pow(NC, -1) * x * z * CF
                    + ln(omx) * LMUA * NC * pow(z, -1) * CF
                    + (-1) * ln(omx) * LMUA * NC * CF
                    + 1.0 / 2.0 * ln(omx) * LMUA * NC * z * CF
                    + ln(omx) * LMUA * NC * x * pow(z, -1) * CF
                    + (-1) * ln(omx) * LMUA * NC * x * CF
                    + 1.0 / 2.0 * ln(omx) * LMUA * NC * x * z * CF
                    + 0
                )
                tmp += (
                    (-1) * ln(omz) * LMUA * pow(NC, -1) * pow(z, -1) * CF
                    + ln(omz) * LMUA * pow(NC, -1) * CF
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * z * CF
                    + (-1) * ln(omz) * LMUA * pow(NC, -1) * x * pow(z, -1) * CF
                    + ln(omz) * LMUA * pow(NC, -1) * x * CF
                    + (-1) * 1.0 / 2.0 * ln(omz) * LMUA * pow(NC, -1) * x * z * CF
                    + 3 * ln(omz) * LMUA * NC * pow(z, -1) * CF
                    + (-1) * 5 * ln(omz) * LMUA * NC * CF
                    + 1.0 / 2.0 * ln(omz) * LMUA * NC * z * CF
                    + 3 * ln(omz) * LMUA * NC * x * pow(z, -1) * CF
                    + (-1) * 5 * ln(omz) * LMUA * NC * x * CF
                    + 9.0 / 2.0 * ln(omz) * LMUA * NC * x * z * CF
                    + 0
                )
            if "010" == order:
                tmp += (
                    (-1) * 7.0 / 4.0 * LMUF * pow(NC, -1) * pow(z, -1) * CF
                    + 5.0 / 2.0 * LMUF * pow(NC, -1) * CF
                    + (-1) * 2 * LMUF * pow(NC, -1) * z * CF
                    + 1.0 / 4.0 * LMUF * pow(NC, -1) * x * pow(z, -1) * CF
                    + 1.0 / 2.0 * LMUF * pow(NC, -1) * x * CF
                    + (-1) * 1.0 / 2.0 * LMUF * pow(NC, -1) * x * z * CF
                    + 7.0 / 4.0 * LMUF * NC * pow(z, -1) * CF
                    + (-1) * 5.0 / 2.0 * LMUF * NC * CF
                    + 2 * LMUF * NC * z * CF
                    + (-1) * 1.0 / 4.0 * LMUF * NC * x * pow(z, -1) * CF
                    + (-1) * 1.0 / 2.0 * LMUF * NC * x * CF
                    + 1.0 / 2.0 * LMUF * NC * x * z * CF
                    + 0
                )
                tmp += (
                    (-1) * 2 * ln(x) * LMUF * pow(NC, -1) * pow(z, -1) * CF * pow(omx, -1)
                    + 3.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * pow(z, -1) * CF
                    + 2 * ln(x) * LMUF * pow(NC, -1) * CF * pow(omx, -1)
                    + (-1) * 2 * ln(x) * LMUF * pow(NC, -1) * CF
                    + (-1) * ln(x) * LMUF * pow(NC, -1) * z * CF * pow(omx, -1)
                    + 1.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * z * CF
                    + 3.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * LMUF * pow(NC, -1) * x * CF
                    + 3.0 / 2.0 * ln(x) * LMUF * pow(NC, -1) * x * z * CF
                    + 2 * ln(x) * LMUF * NC * pow(z, -1) * CF * pow(omx, -1)
                    + (-1) * 3.0 / 2.0 * ln(x) * LMUF * NC * pow(z, -1) * CF
                    + (-1) * 2 * ln(x) * LMUF * NC * CF * pow(omx, -1)
                    + 2 * ln(x) * LMUF * NC * CF
                    + ln(x) * LMUF * NC * z * CF * pow(omx, -1)
                    + (-1) * 1.0 / 2.0 * ln(x) * LMUF * NC * z * CF
                    + (-1) * 3.0 / 2.0 * ln(x) * LMUF * NC * x * pow(z, -1) * CF
                    + 2 * ln(x) * LMUF * NC * x * CF
                    + (-1) * 3.0 / 2.0 * ln(x) * LMUF * NC * x * z * CF
                    + 0
                )
                tmp += (
                    (-1) * ln(z) * LMUF * pow(NC, -1) * pow(z, -1) * CF
                    + ln(z) * LMUF * pow(NC, -1) * CF
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * z * CF
                    + (-1) * ln(z) * LMUF * pow(NC, -1) * x * pow(z, -1) * CF
                    + ln(z) * LMUF * pow(NC, -1) * x * CF
                    + (-1) * 1.0 / 2.0 * ln(z) * LMUF * pow(NC, -1) * x * z * CF
                    + ln(z) * LMUF * NC * pow(z, -1) * CF
                    + (-1) * ln(z) * LMUF * NC * CF
                    + 1.0 / 2.0 * ln(z) * LMUF * NC * z * CF
                    + ln(z) * LMUF * NC * x * pow(z, -1) * CF
                    + (-1) * ln(z) * LMUF * NC * x * CF
                    + 1.0 / 2.0 * ln(z) * LMUF * NC * x * z * CF
                    + 0
                )
                tmp += (
                    (-1) * 2 * ln(omx) * LMUF * pow(NC, -1) * pow(z, -1) * CF
                    + 3 * ln(omx) * LMUF * pow(NC, -1) * CF
                    + (-1) * 1.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * z * CF
                    + (-1) * 2 * ln(omx) * LMUF * pow(NC, -1) * x * pow(z, -1) * CF
                    + 3 * ln(omx) * LMUF * pow(NC, -1) * x * CF
                    + (-1) * 5.0 / 2.0 * ln(omx) * LMUF * pow(NC, -1) * x * z * CF
                    + 2 * ln(omx) * LMUF * NC * pow(z, -1) * CF
                    + (-1) * 3 * ln(omx) * LMUF * NC * CF
                    + 1.0 / 2.0 * ln(omx) * LMUF * NC * z * CF
                    + 2 * ln(omx) * LMUF * NC * x * pow(z, -1) * CF
                    + (-1) * 3 * ln(omx) * LMUF * NC * x * CF
                    + 5.0 / 2.0 * ln(omx) * LMUF * NC * x * z * CF
                    + 0
                )
                tmp += (-1) * ln(omz) * LMUF * pow(NC, -1) * pow(z, -1) * CF + ln(omz) * LMUF * pow(NC, -1) * CF + (-1) * 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * z * CF + (-1) * ln(omz) * LMUF * pow(NC, -1) * x * pow(z, -1) * CF + ln(omz) * LMUF * pow(NC, -1) * x * CF + (-1) * 1.0 / 2.0 * ln(omz) * LMUF * pow(NC, -1) * x * z * CF + 0
                tmp += ln(omz) * LMUF * NC * pow(z, -1) * CF + (-1) * ln(omz) * LMUF * NC * CF + 1.0 / 2.0 * ln(omz) * LMUF * NC * z * CF + ln(omz) * LMUF * NC * x * pow(z, -1) * CF + (-1) * ln(omz) * LMUF * NC * x * CF + 1.0 / 2.0 * ln(omz) * LMUF * NC * x * z * CF + 0
            if "011" == order:
                tmp += (
                    LMUA * LMUF * pow(NC, -1) * pow(z, -1) * CF
                    + (-1) * LMUA * LMUF * pow(NC, -1) * CF
                    + 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * z * CF
                    + LMUA * LMUF * pow(NC, -1) * x * pow(z, -1) * CF
                    + (-1) * LMUA * LMUF * pow(NC, -1) * x * CF
                    + 1.0 / 2.0 * LMUA * LMUF * pow(NC, -1) * x * z * CF
                    + (-1) * LMUA * LMUF * NC * pow(z, -1) * CF
                    + LMUA * LMUF * NC * CF
                    + (-1) * 1.0 / 2.0 * LMUA * LMUF * NC * z * CF
                    + (-1) * LMUA * LMUF * NC * x * pow(z, -1) * CF
                    + LMUA * LMUF * NC * x * CF
                    + (-1) * 1.0 / 2.0 * LMUA * LMUF * NC * x * z * CF
                    + 0
                )
            if "100" == order:
                tmp += (
                    (-1) * 11.0 / 6.0 * LMUR * NC * pow(z, -1) * CF
                    + 11.0 / 3.0 * LMUR * NC * CF
                    + (-1) * 11.0 / 6.0 * LMUR * NC * x * pow(z, -1) * CF
                    + 11.0 / 3.0 * LMUR * NC * x * CF
                    + (-1) * 11.0 / 3.0 * LMUR * NC * x * z * CF
                    + 1.0 / 3.0 * LMUR * NF * pow(z, -1) * CF
                    + (-1) * 2.0 / 3.0 * LMUR * NF * CF
                    + 1.0 / 3.0 * LMUR * NF * x * pow(z, -1) * CF
                    + (-1) * 2.0 / 3.0 * LMUR * NF * x * CF
                    + 2.0 / 3.0 * LMUR * NF * x * z * CF
                    + 0
                )
            res += tmp

        return res


def c2tq2g_eq(x, z, rsl, order, f=C2Tq2gEq_DR0123_scheme):
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
