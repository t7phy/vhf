def C2Pq2qpEqp(inx, inz, cx, cz,                  Q, muR, muF, muA):
  res = (0.0)

  rln2 = (ln(2.0))

  LMUR = (2 * log(muR / Q))
  LMUF = (2 * log(muF / Q))
  LMUA = (2 * log(muA / Q))

  NC = (3.0)
  CF = (4.0 / 3.0)
  TR = (0.5)

  if cx == "D" and cz == "D":
  
    res = (0)

    return res
  
  if cx == "D" and cz == "0":
  
    res = (0)

    return res
  
  if cx == "D" and cz == "1":
  
    res = (0)

    return res
  
  if cx == "D" and cz == "2":
  
    res = (0)

    return res
  
  if cx == "D" and cz == "3":
  
    res = (0)

    return res
  
  if cx == "0" and cz == "D":
  
    res = (0)

    return res
  
  if cx == "0" and cz == "0":
  
    res = (0)

    return res
  
  if cx == "0" and cz == "1":
  
    res = (0)

    return res
  
  if cx == "0" and cz == "2":
  
    res = (0)

    return res
  
  if cx == "0" and cz == "3":
  
    res = (0)

    return res
  
  if cx == "1" and cz == "D":
  
    res = (0)

    return res
  
  if cx == "1" and cz == "0":
  
    res = (0)

    return res
  
  if cx == "1" and cz == "1":
  
    res = (0)

    return res
  
  if cx == "1" and cz == "2":
  
    res = (0)

    return res
  
  if cx == "1" and cz == "3":
  
    res = (0)

    return res
  
  if cx == "2" and cz == "D":
  
    res = (0)

    return res
  
  if cx == "2" and cz == "0":
  
    res = (0)

    return res
  
  if cx == "2" and cz == "1":
  
    res = (0)

    return res
  
  if cx == "2" and cz == "2":
  
    res = (0)

    return res
  
  if cx == "2" and cz == "3":
  
    res = (0)

    return res
  
  if cx == "3" and cz == "D":
  
    res = (0)

    return res
  
  if cx == "3" and cz == "0":
  
    res = (0)

    return res
  
  if cx == "3" and cz == "1":
  
    res = (0)

    return res
  
  if cx == "3" and cz == "2":
  
    res = (0)

    return res
  
  if cx == "3" and cz == "3":
  
    res = (0)

    return res
  
  if cx == "D" and cz == "R":
  
    z = (inz)
    omz = (1. - z)
    opz = (1. + z)
    res = (0)

    return res
  
  if cx == "0" and cz == "R":
  
    z = (inz)
    omz = (1. - z)
    opz = (1. + z)
    res = (0)

    return res
  
  if cx == "1" and cz == "R":
  
    z = (inz)
    omz = (1. - z)
    opz = (1. + z)
    res = (0)

    return res
  
  if cx == "2" and cz == "R":
  
    z = (inz)
    omz = (1. - z)
    opz = (1. + z)
    res = (0)

    return res
  
  if cx == "3" and cz == "R":
  
    z = (inz)
    omz = (1. - z)
    opz = (1. + z)
    res = (0)

    return res
  
  if cx == "R" and cz == "D":
  
    x = (inx)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    # Split orders:
    res = (0)
    # Order 000:
    res += ( 9 * CF + (-1) * 9 * x * CF + (-1) * 1. / 2. * pow(pi, 2) * CF + 1. / 2. * pow(pi, 2) * x * CF + 25. / 4. * ln(x) * CF + (-1) * 3. / 4. * ln(x) * x * CF + (-1) * 1. / 3. * ln(x) * pow(pi, 2) * CF + (-1) * 1. / 3. * ln(x) * pow(pi, 2) * x * CF + 17. / 8. * pow(ln(x), 2) * CF + (-1) * 15. / 8. * pow(ln(x), 2) * x * CF + 5. / 12. * pow(ln(x), 3) * CF + 5. / 12. * pow(ln(x), 3) * x * CF + (-1) * 5. / 2. * ln(x) * ln(omx) * CF + 5. / 2. * ln(x) * ln(omx) * x * CF + (-1) * 3. / 2. * ln(x) * pow(ln(omx), 2) * CF + (-1) * 3. / 2. * ln(x) * pow(ln(omx), 2) * x * CF + ln(x) * Li2(x) * CF + ln(x) * Li2(x) * x * CF + (-1) * 3 * ln(omx) * CF + 3 * ln(omx) * x * CF + 0)
    res += ( 1. / 3. * ln(omx) * pow(pi, 2) * CF + 1. / 3. * ln(omx) * pow(pi, 2) * x * CF + 5. / 4. * pow(ln(omx), 2) * CF + (-1) * 5. / 4. * pow(ln(omx), 2) * x * CF + (-1) * ln(omx) * Li2(1 - x) * CF + (-1) * ln(omx) * Li2(1 - x) * x * CF + (-1) * 2 * ln(omx) * Li2(x) * CF + (-1) * 2 * ln(omx) * Li2(x) * x * CF + (-1) * Li3(1 - x) * CF + (-1) * Li3(1 - x) * x * CF + 1. / 2. * Li2(x) * CF + (-1) * 1. / 2. * Li2(x) * x * CF + 0)
    # Order 010:
    res += ( 3 * LMUF * CF + (-1) * 3 * x * LMUF * CF + (-1) * 1. / 6. * pow(pi, 2) * LMUF * CF + (-1) * 1. / 6. * pow(pi, 2) * x * LMUF * CF + 3 * ln(x) * LMUF * CF + (-1) * 3 * ln(x) * x * LMUF * CF + pow(ln(x), 2) * LMUF * CF + pow(ln(x), 2) * x * LMUF * CF + (-1) * 5. / 2. * ln(omx) * LMUF * CF + 5. / 2. * ln(omx) * x * LMUF * CF + Li2(x) * LMUF * CF + Li2(x) * x * LMUF * CF + 0)
    # Order 020:
    res += ( 5. / 4. * pow(LMUF, 2) * CF + (-1) * 5. / 4. * x * pow(LMUF, 2) * CF + 1. / 2. * ln(x) * pow(LMUF, 2) * CF + 1. / 2. * ln(x) * x * pow(LMUF, 2) * CF + 0)

    return res
  
  if cx == "R" and cz == "0":
  
    x = (inx)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    # Split orders:
    res = (0)
    # Order 000:
    res += ( +(-1) * 3 * CF + 3 * x * CF + 1. / 6. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * CF + (-1) * 3 * ln(x) * CF + 3 * ln(x) * x * CF + (-1) * pow(ln(x), 2) * CF + (-1) * pow(ln(x), 2) * x * CF + 5. / 2. * ln(omx) * CF + (-1) * 5. / 2. * ln(omx) * x * CF + (-1) * Li2(x) * CF + (-1) * Li2(x) * x * CF + 0)
    # Order 010:
    res += ( (-1) * 5. / 2. * LMUF * CF + 5. / 2. * x * LMUF * CF + (-1) * ln(x) * LMUF * CF + (-1) * ln(x) * x * LMUF * CF + 0)

    return res
  
  if cx == "R" and cz == "1":
  
    x = (inx)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    res = (5. / 2. * CF - 5. / 2. * x * CF + ln(x) * CF + ln(x) * x * CF)

    return res
  
  if cx == "R" and cz == "2":
  
    x = (inx)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    res = (0)

    return res
  
  if cx == "R" and cz == "3":
  
    x = (inx)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    res = (0)

    return res
  
  if cx == "R" and cz == "R":
  
    x = (inx)
    z = (inz)
    omz = (1. - z)
    opz = (1. + z)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    xmz = (x - z)
    omxmz = (1. - x - z)
    poly2 = (1 + 2 * x + x * x - 4 * x * z)
    sqrtxz1 = (mysqrt(1 - 2 * z + z * z + 4 * x * z))
    sqrtxz2 = (mysqrt(poly2))
    sqrtxz3 = (mysqrt(x / z))
    if z < 1. - x and z < x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z > 1. - x and z < x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z < 1. - x and z > x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z > 1. - x and z > x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z > x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z < x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z < 1. - x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z > 1. - x:
    
      tmp = (0.0)
      tmp = (0)

      res += ( tmp)
    
    if z != x and z != 1. - x:
    
      tmp = (0.0)
      # Split orders:
      tmp = (0)
      # Order 000:
      tmp += ( +(-1) * 3 * pow(z, -1) * CF + 10 * CF + 3 * x * pow(z, -1) * CF + (-1) * 10 * x * CF + 1. / 6. * pow(pi, 2) * pow(z, -1) * CF + (-1) * 1. / 3. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * pow(z, -1) * CF + (-1) * 1. / 3. * pow(pi, 2) * x * CF + (-1) * 3 * ln(x) * pow(z, -1) * CF + 1. / 2. * ln(x) * CF * pow(poly2, -1) + 8 * ln(x) * CF + 3 * ln(x) * x * pow(z, -1) * CF + (-1) * 1. / 2. * ln(x) * x * CF * pow(poly2, -1) + (-1) * 4 * ln(x) * x * CF + (-1) * 1. / 2. * ln(x) * pow(x, 2) * CF * pow(poly2, -1) + 1. / 2. * ln(x) * pow(x, 3) * CF * pow(poly2, -1) + 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) + 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1) + 0)
      tmp += ( (-1) * ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1) + (-1) * 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) + (-1) * 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1) + ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + (-1) * 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * pow(ln(x), 2) * pow(z, -1) * CF + 2 * pow(ln(x), 2) * CF + (-1) * pow(ln(x), 2) * x * pow(z, -1) * CF + 2 * pow(ln(x), 2) * x * CF + ln(x) * ln(z) * pow(z, -1) * CF + (-1) * ln(x) * ln(z) * CF + ln(x) * ln(z) * x * pow(z, -1) * CF + (-1) * ln(x) * ln(z) * x * CF + ln(x) * ln(omz) * pow(z, -1) * CF + 0)
      tmp += ( (-1) * 2 * ln(x) * ln(omz) * CF + ln(x) * ln(omz) * x * pow(z, -1) * CF + (-1) * 2 * ln(x) * ln(omz) * x * CF + 5. / 2. * ln(z) * pow(z, -1) * CF + 1. / 2. * ln(z) * CF * pow(poly2, -1) + ln(z) * CF * pow(omz, -1) + (-1) * 2 * ln(z) * CF + (-1) * 5. / 2. * ln(z) * x * pow(z, -1) * CF + 1. / 2. * ln(z) * x * CF * pow(poly2, -1) + (-1) * ln(z) * x * CF * pow(omz, -1) + 2 * ln(z) * x * CF + (-1) * 1. / 2. * ln(z) * pow(x, 2) * CF * pow(poly2, -1) + (-1) * 1. / 2. * ln(z) * pow(x, 3) * CF * pow(poly2, -1) + 5. / 2. * ln(omx) * pow(z, -1) * CF + (-1) * 5 * ln(omx) * CF + (-1) * 5. / 2. * ln(omx) * x * pow(z, -1) * CF + 5 * ln(omx) * x * CF + 5. / 2. * ln(omz) * pow(z, -1) * CF + (-1) * 5 * ln(omz) * CF + (-1) * 5. / 2. * ln(omz) * x * pow(z, -1) * CF + 0)
      tmp += ( 5 * ln(omz) * x * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1) + (-1) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1) + (-1) * 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) + (-1) * 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) + (-1) * 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) + (-1) * 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * CF * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 0)
      tmp += ( (-1) * 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + (-1) * 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * CF * pow(sqrtxz2, -1) + (-1) * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * CF * pow(sqrtxz2, -1) + (-1) * 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + (-1) * Li2(x) * pow(z, -1) * CF + 2 * Li2(x) * CF + (-1) * Li2(x) * x * pow(z, -1) * CF + 2 * Li2(x) * x * CF + 0)
      # Order 010:
      tmp += ( (-1) * 5. / 2. * pow(z, -1) * LMUF * CF + 5 * LMUF * CF + 5. / 2. * x * pow(z, -1) * LMUF * CF + (-1) * 5 * x * LMUF * CF + (-1) * ln(x) * pow(z, -1) * LMUF * CF + 2 * ln(x) * LMUF * CF + (-1) * ln(x) * x * pow(z, -1) * LMUF * CF + 2 * ln(x) * x * LMUF * CF + 0)

      res += ( tmp)
    
    return res
  
