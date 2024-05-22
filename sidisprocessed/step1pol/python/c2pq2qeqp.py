def C2Pq2qEqp(inx, inz, cx, cz,                 Q, muR, muF, muA):
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
    omz = 1. - z
    opz = 1. + z
    res = 0

    return res
  
  if cx == "0" and cz == "R":
  
    z = inz
    omz = 1. - z
    opz = 1. + z
    res = 0

    return res
  
  if cx == "1" and cz == "R":
  
    z = inz
    omz = 1. - z
    opz = 1. + z
    res = 0

    return res
  
  if cx == "2" and cz == "R":
  
    z = inz
    omz = 1. - z
    opz = 1. + z
    res = 0

    return res
  
  if cx == "3" and cz == "R":
  
    z = inz
    omz = 1. - z
    opz = 1. + z
    res = 0

    return res
  
  if cx == "R" and cz == "D":
  
    x = inx
    omx = 1. - x
    opx = 1. + x
    op6xpxsq = 1. + 6. * x + x * x
    res = 0

    return res
  
  if cx == "R" and cz == "0":
  
    x = inx
    omx = 1. - x
    opx = 1. + x
    op6xpxsq = 1. + 6. * x + x * x
    res = 0

    return res
  
  if cx == "R" and cz == "1":
  
    x = inx
    omx = 1. - x
    opx = 1. + x
    op6xpxsq = 1. + 6. * x + x * x
    res = 0

    return res
  
  if cx == "R" and cz == "2":
  
    x = inx
    omx = 1. - x
    opx = 1. + x
    op6xpxsq = 1. + 6. * x + x * x
    res = 0

    return res
  
  if cx == "R" and cz == "3":
  
    x = inx
    omx = 1. - x
    opx = 1. + x
    op6xpxsq = 1. + 6. * x + x * x
    res = 0

    return res
  
  if cx == "R" and cz == "R":
  
    x = inx
    z = inz
    omz = 1. - z
    opz = 1. + z
    omx = 1. - x
    opx = 1. + x
    op6xpxsq = 1. + 6. * x + x * x
    xmz = x - z
    omxmz = 1. - x - z
    poly2 = 1 + 2 * x + x * x - 4 * x * z
    sqrtxz1 = mysqrt(1 - 2 * z + z * z + 4 * x * z)
    sqrtxz2 = mysqrt(poly2)
    sqrtxz3 = mysqrt(x / z)
    if z < 1. - x and z < x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z > 1. - x and z < x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z < 1. - x and z > x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z > 1. - x and z > x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z > x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z < x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z < 1. - x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z > 1. - x:
    
      tmp = 0.0
      tmp = 0

      res += tmp
    
    if z != x and z != 1. - x:
    
      tmp = 0.0
      tmp = -8 * pow(z, -1) * CF + 8 * CF + 8 * x * pow(z, -1) * CF - 8 * x * CF + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(x, -1) * CF * sqrtxz3 + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * pow(z, -1) * CF * sqrtxz3 + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * sqrtxz3 + 4 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * x * CF * sqrtxz3 - 3 * ln(x) * pow(z, -1) * CF + 3 * ln(x) * CF - 3 * ln(x) * x * pow(z, -1) * CF + 3 * ln(x) * x * CF - 2 * ln(x) * ln(z) * pow(z, -1) * CF - 2 * ln(x) * ln(z) * CF - 2 * ln(x) * ln(z) * x * pow(z, -1) * CF - 2 * ln(x) * ln(z) * x * CF - 3 * ln(z) * pow(z, -1) * CF - 3 * ln(z) * CF + 3 * ln(z) * x * pow(z, -1) * CF + 3 * ln(z) * x * CF - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(x, -1) * CF * sqrtxz3 - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * pow(z, -1) * CF * sqrtxz3 - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * sqrtxz3 - 4 * ln(sqrtxz3) * ArcTan(sqrtxz3) * x * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * pow(x, -1) * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * pow(z, -1) * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * z * CF * sqrtxz3 - 2 * InvTanInt(-sqrtxz3) * x * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * pow(x, -1) * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * pow(z, -1) * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * z * CF * sqrtxz3 - 4 * InvTanInt(z * sqrtxz3) * x * CF * sqrtxz3 + 2 * InvTanInt(sqrtxz3) * pow(x, -1) * CF * sqrtxz3 + 2 * InvTanInt(sqrtxz3) * pow(z, -1) * CF * sqrtxz3 + 2 * InvTanInt(sqrtxz3) * z * CF * sqrtxz3 +
            2 * InvTanInt(sqrtxz3) * x * CF * sqrtxz3

      res += tmp
    
    return res
  
