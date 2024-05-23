def C1Pq2qEq(inx, inz, cx, cz,                Q, muR, muF, muA):
  res = (0.0)

  rln2 = (ln(2.0))

  LMUR = (2 * log(muR / Q))
  LMUF = (2 * log(muF / Q))
  LMUA = (2 * log(muA / Q))

  NC = (3.0)
  CF = (4.0 / 3.0)
  TR = (0.5)

  if cx == "D" and cz == "D":
  
    # Split orders:
    res = (0)
    # Order 000:
    res += ( +(-1) * 8 * CF + 0)
    # Order 010:
    res += ( (-1) * 3. / 2. * LMUF * CF + 0)
    # Order 001:
    res += ( (-1) * 3. / 2. * LMUA * CF + 0)

    return res
  
  if cx == "D" and cz == "0":
  
    # Split orders:
    res = (0)
    # Order 000:
    res += ( +0)
    # Order 001:
    res += ( (-1) * 2 * LMUA * CF + 0)

    return res
  
  if cx == "D" and cz == "1":
  
    res = (2 * CF)

    return res
  
  if cx == "D" and cz == "2":
  
    res = (0)

    return res
  
  if cx == "D" and cz == "3":
  
    res = (0)

    return res
  
  if cx == "0" and cz == "D":
  
    # Split orders:
    res = (0)
    # Order 000:
    res += ( +0)
    # Order 010:
    res += ( (-1) * 2 * LMUF * CF + 0)

    return res
  
  if cx == "0" and cz == "0":
  
    res = (2 * CF)

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
  
    res = (2 * CF)

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
    # Split orders:
    res = (0)
    # Order 000:
    res += ( CF + (-1) * z * CF + 2 * ln(z) * CF * pow(omz, +(-1) * 1) + (-1) * ln(z) * CF + (-1) * ln(z) * z * CF + (-1) * ln(omz) * CF + (-1) * ln(omz) * z * CF + 0)
    # Order 001:
    res += ( LMUA * CF + z * LMUA * CF + 0)

    return res
  
  if cx == "0" and cz == "R":
  
    z = (inz)
    omz = (1. - z)
    opz = (1. + z)
    res = (-CF - z * CF)

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
    res += ( CF + (-1) * x * CF + (-1) * 2 * ln(x) * CF * pow(omx, +(-1) * 1) + ln(x) * CF + ln(x) * x * CF + (-1) * ln(omx) * CF + (-1) * ln(omx) * x * CF + 0)
    # Order 010:
    res += ( LMUF * CF + x * LMUF * CF + 0)

    return res
  
  if cx == "R" and cz == "0":
  
    x = (inx)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    res = (-CF - x * CF)

    return res
  
  if cx == "R" and cz == "1":
  
    x = (inx)
    omx = (1. - x)
    opx = (1. + x)
    op6xpxsq = (1. + 6. * x + x * x)
    res = (0)

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
      tmp = (2 * z * CF + 2 * x * CF)

      res += ( tmp)
    
    return res
  
