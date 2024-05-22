def C1Pq2gEq(inx, inz, cx, cz,                Q, muR, muF, muA):
    res = 0.0

    rln2 = ln(2.0)

    LMUR = 2 * log(muR / Q)
    LMUF = 2 * log(muF / Q)
    LMUA = 2 * log(muA / Q)

    NC = 3.0
    CF = 4.0 / 3.0
    TR = 0.5

    if cx == "D" and cz == "D":
    
        res = 0

        return res
    
    if cx == "D" and cz == "0":
    
        res = 0

        return res
    
