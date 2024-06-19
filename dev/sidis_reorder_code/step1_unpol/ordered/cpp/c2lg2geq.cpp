double C2Lg2gEq(double inx, double inz, std::string cx, std::string cz,
                double Q, double muR, double muF, double muA)
{
  double res = 0.0;

  double rln2 = ln(2.0);

  double LMUR = 2 * log(muR / Q);
  double LMUF = 2 * log(muF / Q);
  double LMUA = 2 * log(muA / Q);

  double NC = 3.0;
  double CF = 4.0 / 3.0;
  double TR = 0.5;

  if (cx == "D" && cz == "D")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "D" && cz == "0")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "D" && cz == "1")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "D" && cz == "2")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "D" && cz == "3")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "0" && cz == "D")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "0" && cz == "0")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "0" && cz == "1")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "0" && cz == "2")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "0" && cz == "3")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "1" && cz == "D")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "1" && cz == "0")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "1" && cz == "1")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "1" && cz == "2")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "1" && cz == "3")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "2" && cz == "D")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "2" && cz == "0")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "2" && cz == "1")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "2" && cz == "2")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "2" && cz == "3")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "3" && cz == "D")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "3" && cz == "0")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "3" && cz == "1")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "3" && cz == "2")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "3" && cz == "3")
  {
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "D" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "0" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "1" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "2" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "3" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "R" && cz == "D")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "R" && cz == "0")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "R" && cz == "1")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "R" && cz == "2")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "R" && cz == "3")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    // Split orders:
    res = 0;
    // Order 000:
    res += 0 + 0;
    return res;
  }
  if (cx == "R" && cz == "R")
  {
    double x = inx;
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    double xmz = x - z;
    double omxmz = 1. - x - z;
    double poly2 = 1 + 2 * x + x * x - 4 * x * z;
    double sqrtxz1 = mysqrt(1 - 2 * z + z * z + 4 * x * z);
    double sqrtxz2 = mysqrt(poly2);
    double sqrtxz3 = mysqrt(x / z);
    if (z < 1. - x && z < x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z > 1. - x && z < x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z < 1. - x && z > x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z > 1. - x && z > x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z > x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z < x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z < 1. - x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z > 1. - x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 0 + 0;
      res += tmp;
    }
    if (z != x && z != 1. - x)
    {
      double tmp = 0.0;
      // Split orders:
      tmp = 0;
      // Order 000:
      tmp += 2. / 3. * pow(NC,-1) * pow(x,-1) * z * pow(pi, 2) * pow(opx,-1) + (-1)* 2. / 3. * pow(NC,-1) * pow(x,-1) * z * pow(pi, 2) + 2 * pow(NC,-1) + (-1)* 2 * pow(NC,-1) * z + 4. / 3. * pow(NC,-1) * z * pow(pi, 2) * pow(opx,-1) + (-1)* 2. / 3. * pow(NC,-1) * z * pow(pi, 2) + (-1)* 8 * pow(NC,-1) * x * pow(z,-1) + 14 * pow(NC,-1) * x + (-1)* 8 * pow(NC,-1) * x * pow(rln2, 2) + (-1)* 1. / 3. * pow(NC,-1) * x * pow(pi, 2) + (-1)* 6 * pow(NC,-1) * x * z + 8 * pow(NC,-1) * x * z * pow(rln2, 2) + 2. / 3. * pow(NC,-1) * x * z * pow(pi, 2) * pow(opx,-1) + (-1)* 1. / 3. * pow(NC,-1) * x * z * pow(pi, 2) + 8 * pow(NC,-1) * pow(x, 2) * pow(z,-1) + (-1)* 16 * pow(NC,-1) * pow(x, 2) + 8 * pow(NC,-1) * pow(x, 2) * pow(rln2, 2) + 8 * pow(NC,-1) * pow(x, 2) * z + (-1)* 8 * pow(NC,-1) * pow(x, 2) * z * pow(rln2, 2) + 2. / 3. * pow(NC,-1) * pow(x, 2) * z * pow(pi, 2) + 3. / 8. * NC * pow(x,-1) * pow(z,-1) + (-1)* 3. / 8. * NC * pow(x,-1) + 2. / 3. * NC * pow(x,-1) * pow(pi, 2) * pow(opx,-1) + (-1)* 2. / 3. * NC * pow(x,-1) * pow(pi, 2) + (-1)* 2. / 3. * NC * pow(x,-1) * z * pow(pi, 2) * pow(opx,-1) + 2. / 3. * NC * pow(x,-1) * z * pow(pi, 2) + 3. / 8. * NC * pow(z,-2) + (-1)* 7. / 4. * NC * pow(z,-1) + (-1)* 5. / 4. * NC + 4. / 3. * NC * pow(pi, 2) * pow(opx,-1) + (-1)* 2. / 3. * NC * pow(pi, 2) + 21. / 8. * NC * z + (-1)* 4. / 3. * NC * z * pow(pi, 2) * pow(opx,-1) + 2. / 3. * NC * z * pow(pi, 2) + (-1)* 3. / 8. * NC * x * pow(z,-2) + (-1)* 25. / 4. * NC * x * pow(z,-1) + (-1)* 8 * NC * x * pow(z,-1) * sqrtxz1 * rln2 + 5. / 4. * NC * x + 2. / 3. * NC * x * pow(pi, 2) * pow(opx,-1) + 1. / 3. * NC * x * pow(pi, 2) + 43. / 8. * NC * x * z + (-1)* 8 * NC * x * z * pow(rln2, 2) + (-1)* 2. / 3. * NC * x * z * pow(pi, 2) * pow(opx,-1) + 1. / 3. * NC * x * z * pow(pi, 2) + 61. / 8. * NC * pow(x, 2) * pow(z,-1) + 8 * NC * pow(x, 2) * pow(z,-1) * sqrtxz1 * rln2 + 3. / 8. * NC * pow(x, 2) + (-1)* 8 * NC * pow(x, 2) * z + 8 * NC * pow(x, 2) * z * pow(rln2, 2) + 0;
      tmp +=  + (-1)*2. / 3. * NC * pow(x, 2) * z * pow(pi, 2) + ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC,-1) * pow(x,-1) * z * sqrtxz3 + (-1)* ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC,-1) * sqrtxz3 + 3 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC,-1) * pow(z, 2) * sqrtxz3 + (-1)* 15 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC,-1) * x * z * sqrtxz3 + (-1)* 3. / 8. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x,-2) * sqrtxz3 + 1. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x,-1) * pow(z,-1) * sqrtxz3 + (-1)* 7. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x,-1) * z * sqrtxz3 + (-1)* 3. / 8. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z,-2) * sqrtxz3 + (-1)* 7. / 2. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * sqrtxz3 + (-1)* 19. / 8. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + (-1)* 15. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * pow(z,-1) * sqrtxz3 + 105. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * x * z * sqrtxz3 + (-1)* 35. / 8. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3 + 0;
      tmp +=  + (-1)*ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC,-1) * pow(x,-1) * z * sqrtxz3 + ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC,-1) * sqrtxz3 + (-1)* 3 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC,-1) * pow(z, 2) * sqrtxz3 + 15 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC,-1) * x * z * sqrtxz3 + 3. / 8. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x,-2) * sqrtxz3 + (-1)* 1. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x,-1) * pow(z,-1) * sqrtxz3 + 7. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x,-1) * z * sqrtxz3 + 3. / 8. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z,-2) * sqrtxz3 + 7. / 2. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * sqrtxz3 + 19. / 8. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + 15. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * pow(z,-1) * sqrtxz3 + (-1)*             105. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * x * z * sqrtxz3 + 35. / 8. * ArcTan(sqrtxz3) * ln(sqrtxz3) * NC * pow(x, 2) * sqrtxz3 + (-1)* 1. / 2. * InvTanInt(-sqrtxz3) * pow(NC,-1) * pow(x,-1) * z * sqrtxz3 + 1. / 2. * InvTanInt(-sqrtxz3) * pow(NC,-1) * sqrtxz3 + (-1)* 3. / 2. * InvTanInt(-sqrtxz3) * pow(NC,-1) * pow(z, 2) * sqrtxz3 + 15. / 2. * InvTanInt(-sqrtxz3) * pow(NC,-1) * x * z * sqrtxz3 + 3. / 16. * InvTanInt(-sqrtxz3) * NC * pow(x,-2) * sqrtxz3 + (-1)* 1. / 8. * InvTanInt(-sqrtxz3) * NC * pow(x,-1) * pow(z,-1) * sqrtxz3 + 7. / 8. * InvTanInt(-sqrtxz3) * NC * pow(x,-1) * z * sqrtxz3 + 3. / 16. * InvTanInt(-sqrtxz3) * NC * pow(z,-2) * sqrtxz3 + 7. / 4. * InvTanInt(-sqrtxz3) * NC * sqrtxz3 + 19. / 16. * InvTanInt(-sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + 15. / 8. * InvTanInt(-sqrtxz3) * NC * x * pow(z,-1) * sqrtxz3 + (-1)* 105. / 8. * InvTanInt(-sqrtxz3) * NC * x * z * sqrtxz3 + 0;
      tmp +=  + 35. / 16. * InvTanInt(-sqrtxz3) * NC * pow(x, 2) * sqrtxz3 + (-1)* InvTanInt(z * sqrtxz3) * pow(NC,-1) * pow(x,-1) * z * sqrtxz3 + InvTanInt(z * sqrtxz3) * pow(NC,-1) * sqrtxz3 + (-1)* 3 * InvTanInt(z * sqrtxz3) * pow(NC,-1) * pow(z, 2) * sqrtxz3 + 15 * InvTanInt(z * sqrtxz3) * pow(NC,-1) * x * z * sqrtxz3 + 3. / 8. * InvTanInt(z * sqrtxz3) * NC * pow(x,-2) * sqrtxz3 + (-1)* 1. / 4. * InvTanInt(z * sqrtxz3) * NC * pow(x,-1) * pow(z,-1) * sqrtxz3 + 7. / 4. * InvTanInt(z * sqrtxz3) * NC * pow(x,-1) * z * sqrtxz3 + 3. / 8. * InvTanInt(z * sqrtxz3) * NC * pow(z,-2) * sqrtxz3 + 7. / 2. * InvTanInt(z * sqrtxz3) * NC * sqrtxz3 + 19. / 8. * InvTanInt(z * sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + 15. / 4. * InvTanInt(z * sqrtxz3) * NC * x * pow(z,-1) * sqrtxz3 + (-1)* 105. / 4. * InvTanInt(z * sqrtxz3) * NC * x * z * sqrtxz3 + 35. / 8. * InvTanInt(z * sqrtxz3) * NC * pow(x, 2) * sqrtxz3 + 1. / 2. * InvTanInt(sqrtxz3) * pow(NC,-1) * pow(x,-1) * z * sqrtxz3 + (-1)* 1. / 2. * InvTanInt(sqrtxz3) * pow(NC,-1) * sqrtxz3 + 3. / 2. * InvTanInt(sqrtxz3) * pow(NC,-1) * pow(z, 2) * sqrtxz3 + (-1)* 15. / 2. * InvTanInt(sqrtxz3) * pow(NC,-1) * x * z * sqrtxz3 + (-1)* 3. / 16. * InvTanInt(sqrtxz3) * NC * pow(x,-2) * sqrtxz3 + 1. / 8. * InvTanInt(sqrtxz3) * NC * pow(x,-1) * pow(z,-1) * sqrtxz3 + (-1)* 7. / 8. * InvTanInt(sqrtxz3) * NC * pow(x,-1) * z * sqrtxz3 + (-1)* 3. / 16. * InvTanInt(sqrtxz3) * NC * pow(z,-2) * sqrtxz3 + (-1)* 7. / 4. * InvTanInt(sqrtxz3) * NC * sqrtxz3 + (-1)* 19. / 16. * InvTanInt(sqrtxz3) * NC * pow(z, 2) * sqrtxz3 + (-1)* 15. / 8. * InvTanInt(sqrtxz3) * NC * x * pow(z,-1) * sqrtxz3 + 105. / 8. * InvTanInt(sqrtxz3) * NC * x * z * sqrtxz3 + (-1)* 35. / 16. * InvTanInt(sqrtxz3) * NC * pow(x, 2) * sqrtxz3 + 12 * ln(1+sqrtxz1- z) * pow(NC,-1) * x * rln2 + 0;
      tmp +=  + (-1)*12 * ln(1+sqrtxz1- z) * pow(NC,-1) * x * z * rln2 + (-1)* 12 * ln(1+sqrtxz1- z) * pow(NC,-1) * pow(x, 2) * rln2 + 12 * ln(1+sqrtxz1- z) * pow(NC,-1) * pow(x, 2) * z * rln2 + 8 * ln(1+sqrtxz1- z) * NC * x * pow(z,-1) * sqrtxz1 + (-1)* 4 * ln(1+sqrtxz1- z) * NC * x * rln2 + 12 * ln(1+sqrtxz1- z) * NC * x * z * rln2 + (-1)* 8 * ln(1+sqrtxz1- z) * NC * pow(x, 2) * pow(z,-1) * sqrtxz1 + 4 * ln(1+sqrtxz1- z) * NC * pow(x, 2) * rln2 + (-1)*             12 * ln(1+sqrtxz1- z) * NC * pow(x, 2) * z * rln2 + (-1)* 4 * pow(ln(1+sqrtxz1- z), 2) * pow(NC,-1) * x + 4 * pow(ln(1+sqrtxz1- z), 2) * pow(NC,-1) * x * z + 4 * pow(ln(1+sqrtxz1- z), 2) * pow(NC,-1) * pow(x, 2) + (-1)* 4 * pow(ln(1+sqrtxz1- z), 2) * pow(NC,-1) * pow(x, 2) * z + 4 * pow(ln(1+sqrtxz1- z), 2) * NC * x + (-1)* 4 * pow(ln(1+sqrtxz1- z), 2) * NC * x * z + (-1)* 4 * pow(ln(1+sqrtxz1- z), 2) * NC * pow(x, 2) + 4 * pow(ln(1+sqrtxz1- z), 2) * NC * pow(x, 2) * z + (-1)* 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * pow(NC,-1) * x + 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * pow(NC,-1) * x * z + 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) + (-1)* 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) * z + (-1)* 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * NC * x + (-1)* 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * NC * x * z + 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * NC * pow(x, 2) + 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * NC * pow(x, 2) * z + 4 * ln(1+sqrtxz1+z) * pow(NC,-1) * x * rln2 + (-1)* 4 * ln(1+sqrtxz1+z) * pow(NC,-1) * x * z * rln2 + (-1)* 4 * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) * rln2 + 4 * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) * z * rln2 + 0;
      tmp +=  + 4 * ln(1+sqrtxz1+z) * NC * x * rln2 + 4 * ln(1+sqrtxz1+z) * NC * x * z * rln2 + (-1)* 4 * ln(1+sqrtxz1+z) * NC * pow(x, 2) * rln2 + (-1)* 4 * ln(1+sqrtxz1+z) * NC * pow(x, 2) * z * rln2 + 8 * ln(x) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + (-1)* 8 * ln(x) * pow(NC,-1) * pow(x,-1) * z + 3. / 2. * ln(x) * pow(NC,-1) + 16 * ln(x) * pow(NC,-1) * z * pow(opx,-1) + (-1)* 19. / 2. * ln(x) * pow(NC,-1) * z + 4 * ln(x) * pow(NC,-1) * x * pow(z,-1) + 5. / 2. * ln(x) * pow(NC,-1) * x + (-1)* 8 * ln(x) * pow(NC,-1) * x * rln2 + 8 * ln(x) * pow(NC,-1) * x * z * pow(opx,-1) + (-1)* 13. / 2. * ln(x) * pow(NC,-1) * x * z + 8 * ln(x) * pow(NC,-1) * x * z * rln2 + (-1)* 4 * ln(x) * pow(NC,-1) * pow(x, 2) * pow(z,-1) + 8 * ln(x) * pow(NC,-1) * pow(x, 2) * rln2 + 4 * ln(x) * pow(NC,-1) * pow(x, 2) * z + (-1)* 8 * ln(x) * pow(NC,-1) * pow(x, 2) * z * rln2 + (-1)* 3. / 16. * ln(x) * NC * pow(x,-1) * pow(z,-1) + 8 * ln(x) * NC * pow(x,-1) * pow(opx,-1) + (-1)* 125. / 16. * ln(x) * NC * pow(x,-1) + (-1)* 8 * ln(x) * NC * pow(x,-1) * z * pow(opx,-1) + 8 * ln(x) * NC * pow(x,-1) * z + 3. / 16. * ln(x) * NC * pow(z,-2) + (-1)* 1. / 8. * ln(x) * NC * pow(z,-1) + 16 * ln(x) * NC * pow(opx,-1) + (-1)* 79. / 8. * ln(x) * NC + (-1)*             16 * ln(x) * NC * z * pow(opx,-1) + 157. / 16. * ln(x) * NC * z + 3. / 16. * ln(x) * NC * x * pow(z,-2) + (-1)* 49. / 8. * ln(x) * NC * x * pow(z,-1) + (-1)* 4 * ln(x) * NC * x * pow(z,-1) * sqrtxz1 + 8 * ln(x) * NC * x * pow(opx,-1) + (-1)* 7. / 8. * ln(x) * NC * x + 4 * ln(x) * NC * x * rln2 + (-1)* 8 * ln(x) * NC * x * z * pow(opx,-1) + 109. / 16. * ln(x) * NC * x * z + (-1)* 8 * ln(x) * NC * x * z * rln2 + 29. / 16. * ln(x) * NC * pow(x, 2) * pow(z,-1) + 4 * ln(x) * NC * pow(x, 2) * pow(z,-1) * sqrtxz1 + 35. / 16. * ln(x) * NC * pow(x, 2) + (-1)* 4 * ln(x) * NC * pow(x, 2) * rln2 + (-1)* 4 * ln(x) * NC * pow(x, 2) * z + 8 * ln(x) * NC * pow(x, 2) * z * rln2 + 0;
      tmp +=  + 4 * ln(x) * ln(1+sqrtxz1- z) * pow(NC,-1) * x + (-1)* 4 * ln(x) * ln(1+sqrtxz1- z) * pow(NC,-1) * x * z + (-1)* 4 * ln(x) * ln(1+sqrtxz1- z) * pow(NC,-1) * pow(x, 2) + 4 * ln(x) * ln(1+sqrtxz1- z) * pow(NC,-1) * pow(x, 2) * z + (-1)* 4 * ln(x) * ln(1+sqrtxz1- z) * NC * x + 4 * ln(x) * ln(1+sqrtxz1- z) * NC * x * z + 4 * ln(x) * ln(1+sqrtxz1- z) * NC * pow(x, 2) + (-1)* 4 * ln(x) * ln(1+sqrtxz1- z) * NC * pow(x, 2) * z + 4 * ln(x) * ln(1+sqrtxz1+z) * pow(NC,-1) * x + (-1)* 4 * ln(x) * ln(1+sqrtxz1+z) * pow(NC,-1) * x * z + (-1)* 4 * ln(x) * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) + 4 * ln(x) * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) * z + 4 * ln(x) * ln(1+sqrtxz1+z) * NC * x * z + (-1)* 4 * ln(x) * ln(1+sqrtxz1+z) * NC * pow(x, 2) * z + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(NC,-1) * pow(x,-1) * z + (-1)* 4 * ln(x) * ln(1+x * pow(z,-1)) * pow(NC,-1) * z * pow(opx,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(NC,-1) * z + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(NC,-1) * x * z * pow(opx,-1) + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(NC,-1) * x * z + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(NC,-1) * pow(x, 2) * z + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) * pow(opx,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) * z + (-1)* 4 * ln(x) * ln(1+x * pow(z,-1)) * NC * pow(opx,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * NC + 4 * ln(x) * ln(1+x * pow(z,-1)) * NC * z * pow(opx,-1) + 0;
      tmp +=  + (-1)*2 * ln(x) * ln(1+x * pow(z,-1)) * NC * z + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * x * pow(opx,-1) + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * x + 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * x * z * pow(opx,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * x * z + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * pow(x, 2) + 2 * ln(x) * ln(1+x * pow(z,-1)) * NC * pow(x, 2) * z + (-1)* 2 * ln(x) * ln(1+x * z) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 2 * ln(x) * ln(1+x * z) * pow(NC,-1) * pow(x,-1) * z + (-1)* 4 * ln(x) * ln(1+x * z) * pow(NC,-1) * z * pow(opx,-1) + 2 * ln(x) * ln(1+x * z) * pow(NC,-1) * z + (-1)* 2 * ln(x) * ln(1+x * z) * pow(NC,-1) * x * z * pow(opx,-1) + (-1)* 4 * ln(x) * ln(1+x * z) * pow(NC,-1) * pow(x, 2) * z + (-1)* 2 * ln(x) * ln(1+x * z) * NC * pow(x,-1) * pow(opx,-1) + 2 * ln(x) * ln(1+x * z) * NC * pow(x,-1) + 2 * ln(x) * ln(1+x * z) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 2 * ln(x) * ln(1+x * z) * NC * pow(x,-1) * z + (-1)* 4 * ln(x) * ln(1+x * z) * NC * pow(opx,-1) + 2 * ln(x) * ln(1+x * z) * NC + 4 * ln(x) * ln(1+x * z) * NC * z * pow(opx,-1) + (-1)* 2 * ln(x) * ln(1+x * z) * NC * z + (-1)* 2 * ln(x) * ln(1+x * z) * NC * x * pow(opx,-1) + (-1)* 4 * ln(x) * ln(1+x * z) * NC * x + 2 * ln(x) * ln(1+x * z) * NC * x * z * pow(opx,-1) + 4 * ln(x) * ln(1+x * z) * NC * pow(x, 2) * z + (-1)* 2 * ln(x) * ln(z+x) * pow(NC,-1) * x * z + 2 * ln(x) * ln(z+x) * pow(NC,-1) * pow(x, 2) * z + 2 * ln(x) * ln(z+x) * NC * x + 2 * ln(x) * ln(z+x) * NC * x * z + (-1)* 2 * ln(x) * ln(z+x) * NC * pow(x, 2) + (-1)* 2 * ln(x) * ln(z+x) * NC * pow(x, 2) * z + (-1)* 3 * pow(ln(x), 2) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 3 * pow(ln(x), 2) * pow(NC,-1) * pow(x,-1) * z + (-1)* 6 * pow(ln(x), 2) * pow(NC,-1) * z * pow(opx,-1) + 3 * pow(ln(x), 2) * pow(NC,-1) * z + pow(ln(x), 2) * pow(NC,-1) * x + 0;
      tmp +=  + (-1)*3 * pow(ln(x), 2) * pow(NC,-1) * x * z * pow(opx,-1) + (-1)* pow(ln(x), 2) * pow(NC,-1) * x * z + pow(ln(x), 2) * pow(NC,-1) * pow(x, 2) + (-1)* pow(ln(x), 2) * pow(NC,-1) * pow(x, 2) * z + (-1)* 3 * pow(ln(x), 2) * NC * pow(x,-1) * pow(opx,-1) + 3 * pow(ln(x), 2) * NC * pow(x,-1) + 3 * pow(ln(x), 2) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 3 * pow(ln(x), 2) * NC * pow(x,-1) * z + (-1)* 6 * pow(ln(x), 2) * NC * pow(opx,-1) + 3 * pow(ln(x), 2) * NC + 6 * pow(ln(x), 2) * NC * z * pow(opx,-1) + (-1)* 3 * pow(ln(x), 2) * NC * z + (-1)* 3 * pow(ln(x), 2) * NC * x * pow(opx,-1) + (-1)* pow(ln(x), 2) * NC * x + 3 * pow(ln(x), 2) * NC * x * z * pow(opx,-1) + pow(ln(x), 2) * NC * x * z + (-1)* pow(ln(x), 2) * NC * pow(x, 2) + pow(ln(x), 2) * NC * pow(x, 2) * z + 2 * ln(x) * ln(z) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + (-1)* 2 * ln(x) * ln(z) * pow(NC,-1) * pow(x,-1) * z + 4 * ln(x) * ln(z) * pow(NC,-1) * z * pow(opx,-1) + (-1)* 2 * ln(x) * ln(z) * pow(NC,-1) * z + 2 * ln(x) * ln(z) * pow(NC,-1) * x + 2 * ln(x) * ln(z) * pow(NC,-1) * x * z * pow(opx,-1) + 4 * ln(x) * ln(z) * pow(NC,-1) * x * z + (-1)* 2 * ln(x) * ln(z) * pow(NC,-1) * pow(x, 2) * z + 2 * ln(x) * ln(z) * NC * pow(x,-1) * pow(opx,-1) + (-1)* 2 * ln(x) * ln(z) * NC * pow(x,-1) + (-1)* 2 * ln(x) * ln(z) * NC * pow(x,-1) * z * pow(opx,-1) + 2 * ln(x) * ln(z) * NC * pow(x,-1) * z + 4 * ln(x) * ln(z) * NC * pow(opx,-1) + (-1)* 2 * ln(x) * ln(z) * NC + (-1)* 4 * ln(x) * ln(z) * NC * z * pow(opx,-1) + 2 * ln(x) * ln(z) * NC * z + 2 * ln(x) * ln(z) * NC * x * pow(opx,-1) + (-1)* 8 * ln(x) * ln(z) * NC * x + (-1)* 2 * ln(x) * ln(z) * NC * x * z * pow(opx,-1) + (-1)* 4 * ln(x) * ln(z) * NC * x * z + 2 * ln(x) * ln(z) * NC * pow(x, 2) + 2 * ln(x) * ln(z) * NC * pow(x, 2) * z + (-1)* 4 * ln(x) * ln(omx) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 4 * ln(x) * ln(omx) * pow(NC,-1) * pow(x,-1) * z + 0;
      tmp +=  + (-1)*8 * ln(x) * ln(omx) * pow(NC,-1) * z * pow(opx,-1) + 4 * ln(x) * ln(omx) * pow(NC,-1) * z + (-1)* 2 * ln(x) * ln(omx) * pow(NC,-1) * x + (-1)* 4 * ln(x) * ln(omx) * pow(NC,-1) * x * z * pow(opx,-1) + 2 * ln(x) * ln(omx) * pow(NC,-1) * x * z + 2 * ln(x) * ln(omx) * pow(NC,-1) * pow(x, 2) + (-1)* 2 * ln(x) * ln(omx) * pow(NC,-1) * pow(x, 2) * z + (-1)* 4 * ln(x) * ln(omx) * NC * pow(x,-1) * pow(opx,-1) + 4 * ln(x) * ln(omx) * NC * pow(x,-1) + 4 * ln(x) * ln(omx) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 4 * ln(x) * ln(omx) * NC * pow(x,-1) * z + (-1)* 8 * ln(x) * ln(omx) * NC * pow(opx,-1) + 4 * ln(x) * ln(omx) * NC + 8 * ln(x) * ln(omx) * NC * z * pow(opx,-1) + (-1)* 4 * ln(x) * ln(omx) * NC * z + (-1)* 4 * ln(x) * ln(omx) * NC * x * pow(opx,-1) + 2 * ln(x) * ln(omx) * NC * x + 4 * ln(x) * ln(omx) * NC * x * z * pow(opx,-1) + (-1)* 2 * ln(x) * ln(omx) * NC * x * z + (-1)* 2 * ln(x) * ln(omx) * NC * pow(x, 2) + 2 * ln(x) * ln(omx) * NC * pow(x, 2) * z + (-1)* 2 * ln(x) * ln(omz) * pow(NC,-1) * x + 2 * ln(x) * ln(omz) * pow(NC,-1) * x * z + 2 * ln(x) * ln(omz) * NC * x + (-1)* 2 * ln(x) * ln(omz) * NC * x * z + 4 * ln(x) * ln(opx) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + (-1)* 4 * ln(x) * ln(opx) * pow(NC,-1) * pow(x,-1) * z + 8 * ln(x) * ln(opx) * pow(NC,-1) * z * pow(opx,-1) + (-1)* 4 * ln(x) * ln(opx) * pow(NC,-1) * z + 4 * ln(x) * ln(opx) * pow(NC,-1) * x * z * pow(opx,-1) + 4 * ln(x) * ln(opx) * pow(NC,-1) * x * z + 4 * ln(x) * ln(opx) * pow(NC,-1) * pow(x, 2) * z + 4 * ln(x) * ln(opx) * NC * pow(x,-1) * pow(opx,-1) + (-1)* 4 * ln(x) * ln(opx) * NC * pow(x,-1) + (-1)* 4 * ln(x) * ln(opx) * NC * pow(x,-1) * z * pow(opx,-1) + 4 * ln(x) * ln(opx) * NC * pow(x,-1) * z + 8 * ln(x) * ln(opx) * NC * pow(opx,-1) + (-1)* 4 * ln(x) * ln(opx) * NC + (-1)* 8 * ln(x) * ln(opx) * NC * z * pow(opx,-1) + 4 * ln(x) * ln(opx) * NC * z + 4 * ln(x) * ln(opx) * NC * x * pow(opx,-1) + 0;
      tmp +=  + 4 * ln(x) * ln(opx) * NC * x + (-1)* 4 * ln(x) * ln(opx) * NC * x * z * pow(opx,-1) + (-1)* 4 * ln(x) * ln(opx) * NC * x * z + 4 * ln(x) * ln(opx) * NC * pow(x, 2) + (-1)* 4 * ln(x) * ln(opx) * NC * pow(x, 2) * z + 1. / 2. * ln(z) * pow(NC,-1) + 1. / 2. * ln(z) * pow(NC,-1) * z + (-1)* 8 * ln(z) * pow(NC,-1) * x * pow(z,-1) + (-1)* 9. / 2. * ln(z) * pow(NC,-1) * x + (-1)* 8 * ln(z) * pow(NC,-1) * x * rln2 + (-1)* 1. / 2. * ln(z) * pow(NC,-1) * x * z + 8 * ln(z) * pow(NC,-1) * x * z * rln2 + 8 * ln(z) * pow(NC,-1) * pow(x, 2) * pow(z,-1) + 4 * ln(z) * pow(NC,-1) * pow(x, 2) + 8 * ln(z) * pow(NC,-1) * pow(x, 2) * rln2 + (-1)*             8 * ln(z) * pow(NC,-1) * pow(x, 2) * z * rln2 + 3. / 16. * ln(z) * NC * pow(x,-1) * pow(z,-1) + 3. / 16. * ln(z) * NC * pow(x,-1) + (-1)* 3. / 16. * ln(z) * NC * pow(z,-2) + (-1)* 1. / 8. * ln(z) * NC * pow(z,-1) + (-1)* 17. / 8. * ln(z) * NC + (-1)* 3. / 16. * ln(z) * NC * z + 3. / 16. * ln(z) * NC * x * pow(z,-2) + 49. / 8. * ln(z) * NC * x * pow(z,-1) + (-1)* 4 * ln(z) * NC * x * pow(z,-1) * sqrtxz1 + 1. / 8. * ln(z) * NC * x + (-1)* 4 * ln(z) * NC * x * rln2 + 3. / 16. * ln(z) * NC * x * z + (-1)* 8 * ln(z) * NC * x * z * rln2 + (-1)* 99. / 16. * ln(z) * NC * pow(x, 2) * pow(z,-1) + 4 * ln(z) * NC * pow(x, 2) * pow(z,-1) * sqrtxz1 + 29. / 16. * ln(z) * NC * pow(x, 2) + 4 * ln(z) * NC * pow(x, 2) * rln2 + 8 * ln(z) * NC * pow(x, 2) * z * rln2 + 4 * ln(z) * ln(1+sqrtxz1- z) * pow(NC,-1) * x + (-1)* 4 * ln(z) * ln(1+sqrtxz1- z) * pow(NC,-1) * x * z + (-1)* 4 * ln(z) * ln(1+sqrtxz1- z) * pow(NC,-1) * pow(x, 2) + 4 * ln(z) * ln(1+sqrtxz1- z) * pow(NC,-1) * pow(x, 2) * z + 4 * ln(z) * ln(1+sqrtxz1- z) * NC * x * z + (-1)* 4 * ln(z) * ln(1+sqrtxz1- z) * NC * pow(x, 2) * z + 4 * ln(z) * ln(1+sqrtxz1+z) * pow(NC,-1) * x + 0;
      tmp +=  + (-1)*4 * ln(z) * ln(1+sqrtxz1+z) * pow(NC,-1) * x * z + (-1)* 4 * ln(z) * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) + 4 * ln(z) * ln(1+sqrtxz1+z) * pow(NC,-1) * pow(x, 2) * z + 4 * ln(z) * ln(1+sqrtxz1+z) * NC * x + 4 * ln(z) * ln(1+sqrtxz1+z) * NC * x * z + (-1)* 4 * ln(z) * ln(1+sqrtxz1+z) * NC * pow(x, 2) + (-1)* 4 * ln(z) * ln(1+sqrtxz1+z) * NC * pow(x, 2) * z + 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(NC,-1) * pow(x,-1) * z + 4 * ln(z) * ln(1+x * pow(z,-1)) * pow(NC,-1) * z * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(NC,-1) * z + 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(NC,-1) * x * z * pow(opx,-1) + 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(NC,-1) * x * z + 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(NC,-1) * pow(x, 2) * z + 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) * z * pow(opx,-1) + 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * pow(x,-1) * z + 4 * ln(z) * ln(1+x * pow(z,-1)) * NC * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * NC + (-1)* 4 * ln(z) * ln(1+x * pow(z,-1)) * NC * z * pow(opx,-1) + 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * z + 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * x * pow(opx,-1) + 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * x + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * x * z * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * x * z + 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * pow(x, 2) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * NC * pow(x, 2) * z + (-1)* 2 * ln(z) * ln(1+x * z) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 2 * ln(z) * ln(1+x * z) * pow(NC,-1) * pow(x,-1) * z + 0;
      tmp +=  + (-1)*4 * ln(z) * ln(1+x * z) * pow(NC,-1) * z * pow(opx,-1) + 2 * ln(z) * ln(1+x * z) * pow(NC,-1) * z + (-1)* 2 * ln(z) * ln(1+x * z) * pow(NC,-1) * x * z * pow(opx,-1) + (-1)* 4 * ln(z) * ln(1+x * z) * pow(NC,-1) * pow(x, 2) * z + (-1)* 2 * ln(z) * ln(1+x * z) * NC * pow(x,-1) * pow(opx,-1) + 2 * ln(z) * ln(1+x * z) * NC * pow(x,-1) + 2 * ln(z) * ln(1+x * z) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * z) * NC * pow(x,-1) * z + (-1)* 4 * ln(z) * ln(1+x * z) * NC * pow(opx,-1) + 2 * ln(z) * ln(1+x * z) * NC + 4 * ln(z) * ln(1+x * z) * NC * z * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * z) * NC * z + (-1)* 2 * ln(z) * ln(1+x * z) * NC * x * pow(opx,-1) + (-1)* 4 * ln(z) * ln(1+x * z) * NC * x + 2 * ln(z) * ln(1+x * z) * NC * x * z * pow(opx,-1) + 4 * ln(z) * ln(1+x * z) * NC * pow(x, 2) * z + 2 * ln(z) * ln(z+x) * pow(NC,-1) * x * z + (-1)* 2 * ln(z) * ln(z+x) * pow(NC,-1) * pow(x, 2) * z + (-1)* 2 * ln(z) * ln(z+x) * NC * x + (-1)* 2 * ln(z) * ln(z+x) * NC * x * z + 2 * ln(z) * ln(z+x) * NC * pow(x, 2) + 2 * ln(z) * ln(z+x) * NC * pow(x, 2) * z + pow(ln(z), 2) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + (-1)* pow(ln(z), 2) * pow(NC,-1) * pow(x,-1) * z + 2 * pow(ln(z), 2) * pow(NC,-1) * z * pow(opx,-1) + (-1)* pow(ln(z), 2) * pow(NC,-1) * z + (-1)* 4 * pow(ln(z), 2) * pow(NC,-1) * x + pow(ln(z), 2) * pow(NC,-1) * x * z * pow(opx,-1) + 4 * pow(ln(z), 2) * pow(NC,-1) * pow(x, 2) + 2 * pow(ln(z), 2) * pow(NC,-1) * pow(x, 2) * z + pow(ln(z), 2) * NC * pow(x,-1) * pow(opx,-1) + (-1)* pow(ln(z), 2) * NC * pow(x,-1) + (-1)* pow(ln(z), 2) * NC * pow(x,-1) * z * pow(opx,-1) + pow(ln(z), 2) * NC * pow(x,-1) * z + 2 * pow(ln(z), 2) * NC * pow(opx,-1) + (-1)* pow(ln(z), 2) * NC + (-1)* 2 * pow(ln(z), 2) * NC * z * pow(opx,-1) + pow(ln(z), 2) * NC * z + pow(ln(z), 2) * NC * x * pow(opx,-1) + 0;
      tmp +=  + 4 * pow(ln(z), 2) * NC * x + (-1)* pow(ln(z), 2) * NC * x * z * pow(opx,-1) + (-1)* 2 * pow(ln(z), 2) * NC * pow(x, 2) + (-1)* 2 * pow(ln(z), 2) * NC * pow(x, 2) * z + (-1)* 4 * ln(z) * ln(omx) * pow(NC,-1) * x + 4 * ln(z) * ln(omx) * pow(NC,-1) * pow(x, 2) + 4 * ln(z) * ln(omx) * NC * x + (-1)* 4 * ln(z) * ln(omx) * NC * pow(x, 2) + (-1)* ln(omx) * pow(NC,-1) + ln(omx) * pow(NC,-1) * z + (-1)* 4 * ln(omx) * pow(NC,-1) * x * pow(z,-1) + ln(omx) * pow(NC,-1) * x + 3 * ln(omx) * pow(NC,-1) * x * z + 4 * ln(omx) * pow(NC,-1) * pow(x, 2) * pow(z,-1) + (-1)* 4 * ln(omx) * pow(NC,-1) * pow(x, 2) * z + ln(omx) * NC + (-1)* ln(omx) * NC * z + 4 * ln(omx) * NC * x * pow(z,-1) + (-1)* ln(omx) * NC * x + (-1)* 3 * ln(omx) * NC * x * z + (-1)* 4 * ln(omx) * NC * pow(x, 2) * pow(z,-1) + 4 * ln(omx) * NC * pow(x, 2) * z + (-1)* ln(omz) * pow(NC,-1) + ln(omz) * pow(NC,-1) * z + (-1)* 4 * ln(omz) * pow(NC,-1) * x * pow(z,-1) + ln(omz) * pow(NC,-1) * x + 3 * ln(omz) * pow(NC,-1) * x * z + 4 * ln(omz) * pow(NC,-1) * pow(x, 2) * pow(z,-1) + (-1)* 4 * ln(omz) * pow(NC,-1) * pow(x, 2) * z + ln(omz) * NC + (-1)* ln(omz) * NC * z + 4 * ln(omz) * NC * x * pow(z,-1) + (-1)* ln(omz) * NC * x + (-1)* 3 * ln(omz) * NC * x * z + (-1)* 4 * ln(omz) * NC * pow(x, 2) * pow(z,-1) + 4 * ln(omz) * NC * pow(x, 2) * z + (-1)* 4 * Li2(1. / 2.- 1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * NC * x + 4 * Li2(1. / 2.- 1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * NC * pow(x, 2) + 4 * Li2(1. / 2.+1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * NC * x + (-1)* 4 * Li2(1. / 2.+1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * NC * pow(x, 2) + 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * pow(NC,-1) * x + (-1)* 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * pow(NC,-1) * x * z + (-1)* 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * pow(NC,-1) * pow(x, 2) + 0;
      tmp +=  + 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * pow(NC,-1) * pow(x, 2) * z + 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * NC * x * z + (-1)* 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * NC * pow(x, 2) * z + (-1)* 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * pow(NC,-1) * x + 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * pow(NC,-1) * x * z + 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * pow(NC,-1) * pow(x, 2) + (-1)* 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * pow(NC,-1) * pow(x, 2) * z + (-1)* 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * NC * x * z + 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * NC * pow(x, 2) * z + (-1)* 2 * Li2(-x * pow(z,-1)) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 2 * Li2(-x * pow(z,-1)) * pow(NC,-1) * pow(x,-1) * z + (-1)* 4 * Li2(-x * pow(z,-1)) * pow(NC,-1) * z * pow(opx,-1) + 2 * Li2(-x * pow(z,-1)) * pow(NC,-1) * z + (-1)* 2 * Li2(-x * pow(z,-1)) * pow(NC,-1) * x * z * pow(opx,-1) + (-1)* 4 * Li2(-x * pow(z,-1)) * pow(NC,-1) * x * z + (-1)* 2 * Li2(-x * pow(z,-1)) * NC * pow(x,-1) * pow(opx,-1) + 2 * Li2(-x * pow(z,-1)) * NC * pow(x,-1) + 2 * Li2(-x * pow(z,-1)) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 2 * Li2(-x * pow(z,-1)) * NC * pow(x,-1) * z + (-1)* 4 * Li2(-x * pow(z,-1)) * NC * pow(opx,-1) + 2 * Li2(-x * pow(z,-1)) * NC + 4 * Li2(-x * pow(z,-1)) * NC * z * pow(opx,-1) + (-1)* 2 * Li2(-x * pow(z,-1)) * NC * z + (-1)* 2 * Li2(-x * pow(z,-1)) * NC * x * pow(opx,-1) + 2 * Li2(-x * pow(z,-1)) * NC * x * z * pow(opx,-1) + 4 * Li2(-x * pow(z,-1)) * NC * x * z + (-1)* 4 * Li2(-x * pow(z,-1)) * NC * pow(x, 2) + 4 * Li2(-x) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + (-1)* 4 * Li2(-x) * pow(NC,-1) * pow(x,-1) * z + 8 * Li2(-x) * pow(NC,-1) * z * pow(opx,-1) + 0;
      tmp +=  + (-1)*4 * Li2(-x) * pow(NC,-1) * z + 4 * Li2(-x) * pow(NC,-1) * x * z * pow(opx,-1) + 4 * Li2(-x) * pow(NC,-1) * x * z + 4 * Li2(-x) * pow(NC,-1) * pow(x, 2) * z + 4 * Li2(-x) * NC * pow(x,-1) * pow(opx,-1) + (-1)* 4 * Li2(-x) * NC * pow(x,-1) + (-1)* 4 * Li2(-x) * NC * pow(x,-1) * z * pow(opx,-1) + 4 * Li2(-x) * NC * pow(x,-1) * z + 8 * Li2(-x) * NC * pow(opx,-1) + (-1)* 4 * Li2(-x) * NC + (-1)* 8 * Li2(-x) * NC * z * pow(opx,-1) + 4 * Li2(-x) * NC * z + 4 * Li2(-x) * NC * x * pow(opx,-1) + 4 * Li2(-x) * NC * x + (-1)* 4 * Li2(-x) * NC * x * z * pow(opx,-1) + (-1)* 4 * Li2(-x) * NC * x * z + 4 * Li2(-x) * NC * pow(x, 2) + (-1)* 4 * Li2(-x) * NC * pow(x, 2) * z + (-1)* 2 * Li2(-x * z) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 2 * Li2(-x * z) * pow(NC,-1) * pow(x,-1) * z + (-1)* 4 * Li2(-x * z) * pow(NC,-1) * z * pow(opx,-1) + 2 * Li2(-x * z) * pow(NC,-1) * z + (-1)* 2 * Li2(-x * z) * pow(NC,-1) * x * z * pow(opx,-1) + (-1)* 4 * Li2(-x * z) * pow(NC,-1) * pow(x, 2) * z + (-1)* 2 * Li2(-x * z) * NC * pow(x,-1) * pow(opx,-1) + 2 * Li2(-x * z) * NC * pow(x,-1) + 2 * Li2(-x * z) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 2 * Li2(-x * z) * NC * pow(x,-1) * z + (-1)* 4 * Li2(-x * z) * NC * pow(opx,-1) + 2 * Li2(-x * z) * NC + 4 * Li2(-x * z) * NC * z * pow(opx,-1) + (-1)* 2 * Li2(-x * z) * NC * z + (-1)* 2 * Li2(-x * z) * NC * x * pow(opx,-1) + (-1)* 4 * Li2(-x * z) * NC * x + 2 * Li2(-x * z) * NC * x * z * pow(opx,-1) + 4 * Li2(-x * z) * NC * pow(x, 2) * z + (-1)* 4 * Li2(x) * pow(NC,-1) * pow(x,-1) * z * pow(opx,-1) + 4 * Li2(x) * pow(NC,-1) * pow(x,-1) * z + (-1)* 8 * Li2(x) * pow(NC,-1) * z * pow(opx,-1) + 4 * Li2(x) * pow(NC,-1) * z + (-1)* 4 * Li2(x) * pow(NC,-1) * x * z * pow(opx,-1) + 2 * Li2(x) * pow(NC,-1) * pow(x, 2) + (-1)* 2 * Li2(x) * pow(NC,-1) * pow(x, 2) * z + (-1)* 4 * Li2(x) * NC * pow(x,-1) * pow(opx,-1) + 0;
      tmp +=  + 4 * Li2(x) * NC * pow(x,-1) + 4 * Li2(x) * NC * pow(x,-1) * z * pow(opx,-1) + (-1)* 4 * Li2(x) * NC * pow(x,-1) * z + (-1)* 8 * Li2(x) * NC * pow(opx,-1) + 4 * Li2(x) * NC + 8 * Li2(x) * NC * z * pow(opx,-1) + (-1)* 4 * Li2(x) * NC * z + (-1)* 4 * Li2(x) * NC * x * pow(opx,-1) + 4 * Li2(x) * NC * x * z * pow(opx,-1) + (-1)* 2 * Li2(x) * NC * pow(x, 2) + 2 * Li2(x) * NC * pow(x, 2) * z + 4 * Li2(z) * pow(NC,-1) * x + (-1)* 4 * Li2(z) * pow(NC,-1) * pow(x, 2) + (-1)* 4 * Li2(z) * NC * x + 4 * Li2(z) * NC * pow(x, 2) + 0;
      // Order 001:
      tmp += 4 * LMUA * pow(NC,-1) * x * pow(z,-1) + (-1)* 2 * LMUA * pow(NC,-1) * x + (-1)* 2 * LMUA * pow(NC,-1) * x * z + (-1)* 4 * LMUA * pow(NC,-1) * pow(x, 2) * pow(z,-1) + 2 * LMUA * pow(NC,-1) * pow(x, 2) + 2 * LMUA * pow(NC,-1) * pow(x, 2) * z + (-1)* 4 * LMUA * NC * x * pow(z,-1) + 2 * LMUA * NC * x + 2 * LMUA * NC * x * z + 4 * LMUA * NC * pow(x, 2) * pow(z,-1) + (-1)* 2 * LMUA * NC * pow(x, 2) + (-1)* 2 * LMUA * NC * pow(x, 2) * z + 0;
      tmp += 4 * ln(z) * LMUA * pow(NC,-1) * x + (-1)* 4 * ln(z) * LMUA * pow(NC,-1) * pow(x, 2) + (-1)* 4 * ln(z) * LMUA * NC * x + 4 * ln(z) * LMUA * NC * pow(x, 2) + 0;
      // Order 010:
      tmp += LMUF * pow(NC,-1) + (-1)* LMUF * pow(NC,-1) * z + LMUF * pow(NC,-1) * x + (-1)* LMUF * pow(NC,-1) * x * z + (-1)* 2 * LMUF * pow(NC,-1) * pow(x, 2) + 2 * LMUF * pow(NC,-1) * pow(x, 2) * z + (-1)*             LMUF * NC + LMUF * NC * z + (-1)* LMUF * NC * x + LMUF * NC * x * z + 2 * LMUF * NC * pow(x, 2) + (-1)* 2 * LMUF * NC * pow(x, 2) * z + 0;
      tmp += 2 * ln(x) * LMUF * pow(NC,-1) * x + (-1)* 2 * ln(x) * LMUF * pow(NC,-1) * x * z + (-1)* 2 * ln(x) * LMUF * NC * x + 2 * ln(x) * LMUF * NC * x * z + 0;
      res += tmp;
    }
    return res;
  }
}