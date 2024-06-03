double C2Pq2qpEs(double inx, double inz, std::string cx, std::string cz,
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
      tmp += 5 * CF + 6 * CF * pow(rln2, 2) * pow(omx,-1) + (-1)* 4 * CF * pow(rln2, 2) + 6 * CF * sqrtxz1 * rln2 * pow(omx,-1) + (-1)*            4 * CF * sqrtxz1 * rln2 + (-1)* 4 * z * CF + 4 * z * CF * pow(rln2, 2) * pow(omx,-1) + 16 * pow(z, 2) * CF * pow(rln2, 2) * pow(omx,-1) + (-1)* 16 * pow(z, 2) * CF * pow(rln2, 2) + (-1)* 8 * x * z * CF * pow(rln2, 2) + (-1)* 1. / 3. * pow(pi, 2) * pow(x,-2) * CF * pow(opx,-1) + 1. / 3. * pow(pi, 2) * pow(x,-2) * CF + 2. / 3. * pow(pi, 2) * pow(x,-2) * z * CF * pow(opx,-1) + (-1)* 2. / 3. * pow(pi, 2) * pow(x,-2) * z * CF + (-1)* 1. / 3. * pow(pi, 2) * pow(x,-1) * CF + 2. / 3. * pow(pi, 2) * pow(x,-1) * z * CF + 4. / 3. * pow(pi, 2) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 4. / 3. * pow(pi, 2) * pow(x,-1) * pow(z, 2) * CF + (-1)* 5. / 6. * pow(pi, 2) * CF * pow(omx,-1) + 2. / 3. * pow(pi, 2) * CF * pow(opx,-1) + 1. / 3. * pow(pi, 2) * CF + 5. / 3. * pow(pi, 2) * z * CF * pow(omx,-1) + (-1)* 4. / 3. * pow(pi, 2) * z * CF * pow(opx,-1) + (-1)* 2. / 3. * pow(pi, 2) * z * CF + (-1)* 2 * pow(pi, 2) * pow(z, 2) * CF * pow(omx,-1) + 2 * pow(pi, 2) * pow(z, 2) * CF * pow(opx,-1) + 4. / 3. * pow(pi, 2) * pow(z, 2) * CF + (-1)* 1. / 3. * pow(pi, 2) * x * CF + 2. / 3. * pow(pi, 2) * x * z * CF + (-1)* 8 * ln(1+sqrtxz1- z) * CF * rln2 * pow(omx,-1) + 6 * ln(1+sqrtxz1- z) * CF * rln2 + (-1)* 6 * ln(1+sqrtxz1- z) * CF * sqrtxz1 * pow(omx,-1) + 4 * ln(1+sqrtxz1- z) * CF * sqrtxz1 + (-1)* 4 * ln(1+sqrtxz1- z) * z * CF * rln2 + (-1)* 24 * ln(1+sqrtxz1- z) * pow(z, 2) * CF * rln2 * pow(omx,-1) + 24 * ln(1+sqrtxz1- z) * pow(z, 2) * CF * rln2 + (-1)* 2 * ln(1+sqrtxz1- z) * x * CF * rln2 + 12 * ln(1+sqrtxz1- z) * x * z * CF * rln2 + 2 * pow(ln(1+sqrtxz1- z), 2) * CF * pow(omx,-1) + (-1)* 2 * pow(ln(1+sqrtxz1- z), 2) * CF + (-1)* 4 * pow(ln(1+sqrtxz1- z), 2) * z * CF * pow(omx,-1) + 4 * pow(ln(1+sqrtxz1- z), 2) * z * CF + 0;
      tmp +=  + 8 * pow(ln(1+sqrtxz1- z), 2) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * pow(ln(1+sqrtxz1- z), 2) * pow(z, 2) * CF + 2 * pow(ln(1+sqrtxz1- z), 2) * x * CF + (-1)* 4 * pow(ln(1+sqrtxz1- z), 2) * x * z * CF + 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * CF * pow(omx,-1) + (-1)* 2 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * CF + 8 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * z * CF * pow(omx,-1) + (-1)* 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * z * CF + 8 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * pow(z, 2) * CF + (-1)* 2 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * x * CF + (-1)* 4 * ln(1+sqrtxz1- z) * ln(1+sqrtxz1+z) * x * z * CF + (-1)* 4 * ln(1+sqrtxz1+z) * CF * rln2 * pow(omx,-1) + 2 * ln(1+sqrtxz1+z) * CF * rln2 + (-1)* 8 * ln(1+sqrtxz1+z) * z * CF * rln2 * pow(omx,-1) + 4 * ln(1+sqrtxz1+z) * z * CF * rln2 + (-1)* 8 * ln(1+sqrtxz1+z) * pow(z, 2) * CF * rln2 * pow(omx,-1) + 8 * ln(1+sqrtxz1+z) * pow(z, 2) * CF * rln2 + 2 * ln(1+sqrtxz1+z) * x * CF * rln2 + 4 * ln(1+sqrtxz1+z) * x * z * CF * rln2 + (-1)* 8 * ln(z * sqrtxz3) * ArcTan(z * sqrtxz3) * z * CF * sqrtxz3 + (-1)* 4 * ln(x) * pow(x,-2) * CF * pow(opx,-1) + 4 * ln(x) * pow(x,-2) * CF + 8 * ln(x) * pow(x,-2) * z * CF * pow(opx,-1) + (-1)* 8 * ln(x) * pow(x,-2) * z * CF + (-1)* 4 * ln(x) * pow(x,-1) * CF + 8 * ln(x) * pow(x,-1) * z * CF + 16 * ln(x) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 16 * ln(x) * pow(x,-1) * pow(z, 2) * CF + (-1)* 1. / 2. * ln(x) * CF * pow(poly2,-1) + (-1)* 2 * ln(x) * CF * pow(omx,-1) + 4 * ln(x) * CF * pow(opx,-1) + 3. / 2. * ln(x) * CF + 5 * ln(x) * CF * rln2 * pow(omx,-1) + (-1)* 4 * ln(x) * CF * rln2 + 0;
      tmp +=  + 3 * ln(x) * CF * sqrtxz1 * pow(omx,-1) + (-1)* 2 * ln(x) * CF * sqrtxz1 + 3 * ln(x) * z * CF * pow(omx,-1) + (-1)* 8 * ln(x) * z * CF * pow(opx,-1) + (-1)* 2 * ln(x) * z * CF + (-1)* 2 * ln(x) * z * CF * rln2 * pow(omx,-1) + 4 * ln(x) * z * CF * rln2 + 16 * ln(x) * pow(z, 2) * CF * pow(opx,-1) + 16 * ln(x) * pow(z, 2) * CF * rln2 * pow(omx,-1) + (-1)* 16 * ln(x) * pow(z, 2) * CF * rln2 + 1. / 2. * ln(x) * x * CF * pow(poly2,-1) + (-1)* ln(x) * x * CF * pow(xmz,-1) + (-1)* 3. / 2. * ln(x) * x * CF + 2 * ln(x) * x * CF * rln2 + (-1)* 8 * ln(x) * x * z * CF * rln2 + 1. / 2. * ln(x) * pow(x, 2) * CF * pow(poly2,-1) + 2 * ln(x) * pow(x, 2) * CF * pow(xmz,-1) + (-1)* 1. / 2. * ln(x) * pow(x, 3) * CF * pow(poly2,-1) + (-1)* 1. / 4. * ln(x) * ln(1- sqrtxz2+x) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * ln(x) * ln(1- sqrtxz2+x) * CF * pow(sqrtxz2,-1) + (-1)* 5. / 2. * ln(x) * ln(1- sqrtxz2+x) * x * CF * pow(sqrtxz2,-1) + 5 * ln(x) * ln(1- sqrtxz2+x) * x * z * CF * pow(sqrtxz2,-1) + 1. / 2. * ln(x) * ln(1- sqrtxz2+x) * pow(x, 2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * ln(x) * ln(1- sqrtxz2+x) * pow(x, 2) * CF * pow(sqrtxz2,-1) + (-1)* 1. / 4. * ln(x) * ln(1- sqrtxz2+x) * pow(x, 4) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * ln(x) * ln(1+sqrtxz2+x) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 1. / 4. * ln(x) * ln(1+sqrtxz2+x) * CF * pow(sqrtxz2,-1) + 5. / 2. * ln(x) * ln(1+sqrtxz2+x) * x * CF * pow(sqrtxz2,-1) + (-1)* 5 * ln(x) * ln(1+sqrtxz2+x) * x * z * CF * pow(sqrtxz2,-1) + (-1)* 1. / 2. * ln(x) * ln(1+sqrtxz2+x) * pow(x, 2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 1. / 4. * ln(x) * ln(1+sqrtxz2+x) * pow(x, 2) * CF * pow(sqrtxz2,-1) + 1. / 4. * ln(x) * ln(1+sqrtxz2+x) * pow(x, 4) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 0;
      tmp +=  + (-1)*2 * ln(x) * ln(1+sqrtxz1- z) * CF * pow(omx,-1) + 2 * ln(x) * ln(1+sqrtxz1- z) * CF + 4 * ln(x) * ln(1+sqrtxz1- z) * z * CF * pow(omx,-1) + (-1)* 4 * ln(x) * ln(1+sqrtxz1- z) * z * CF + (-1)* 8 * ln(x) * ln(1+sqrtxz1- z) * pow(z, 2) * CF * pow(omx,-1) + 8 * ln(x) * ln(1+sqrtxz1- z) * pow(z, 2) * CF + (-1)* 2 * ln(x) * ln(1+sqrtxz1- z) * x * CF + 4 * ln(x) * ln(1+sqrtxz1- z) * x * z * CF + (-1)* 3 * ln(x) * ln(1+sqrtxz1+z) * CF * pow(omx,-1) + 2 * ln(x) * ln(1+sqrtxz1+z) * CF + (-1)* 2 * ln(x) * ln(1+sqrtxz1+z) * z * CF * pow(omx,-1) + (-1)* 8 * ln(x) * ln(1+sqrtxz1+z) * pow(z, 2) * CF * pow(omx,-1) + 8 * ln(x) * ln(1+sqrtxz1+z) * pow(z, 2) * CF + 4 * ln(x) * ln(1+sqrtxz1+z) * x * z * CF + ln(x) * ln(1+x * pow(z,-1)) * pow(x,-2) * CF * pow(opx,-1) + (-1)* ln(x) * ln(1+x * pow(z,-1)) * pow(x,-2) * CF + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(x,-2) * z * CF * pow(opx,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(x,-2) * z * CF + ln(x) * ln(1+x * pow(z,-1)) * pow(x,-1) * CF + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * pow(x,-1) * z * CF + (-1)* 4 * ln(x) * ln(1+x * pow(z,-1)) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 4 * ln(x) * ln(1+x * pow(z,-1)) * pow(x,-1) * pow(z, 2) * CF + ln(x) * ln(1+x * pow(z,-1)) * CF * pow(opx,-1) + (-1)* ln(x) * ln(1+x * pow(z,-1)) * CF + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * z * CF * pow(opx,-1) + 2 * ln(x) * ln(1+x * pow(z,-1)) * z * CF + (-1)* 4 * ln(x) * ln(1+x * pow(z,-1)) * pow(z, 2) * CF + ln(x) * ln(1+x * pow(z,-1)) * x * CF + (-1)* 2 * ln(x) * ln(1+x * pow(z,-1)) * x * z * CF + 4 * ln(x) * ln(1+x) * CF * pow(opx,-1) + (-1)* 6 * ln(x) * ln(1+x) * CF + (-1)* 8 * ln(x) * ln(1+x) * z * CF * pow(opx,-1) + 12 * ln(x) * ln(1+x) * z * CF + 8 * ln(x) * ln(1+x) * pow(z, 2) * CF * pow(opx,-1) + 0;
      tmp +=  + (-1)*8 * ln(x) * ln(1+x) * pow(z, 2) * CF + (-1)* 2 * ln(x) * ln(1+x) * x * CF + 4 * ln(x) * ln(1+x) * x * z * CF + ln(x) * ln(1+x * z) * pow(x,-2) * CF * pow(opx,-1) + (-1)* ln(x) * ln(1+x * z) * pow(x,-2) * CF + (-1)* 2 * ln(x) * ln(1+x * z) * pow(x,-2) * z * CF * pow(opx,-1) + 2 * ln(x) * ln(1+x * z) * pow(x,-2) * z * CF + ln(x) * ln(1+x * z) * pow(x,-1) * CF + (-1)* 2 * ln(x) * ln(1+x * z) * pow(x,-1) * z * CF + (-1)* 4 * ln(x) * ln(1+x * z) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 4 * ln(x) * ln(1+x * z) * pow(x,-1) * pow(z, 2) * CF + 2 * ln(x) * ln(1+x * z) * CF * pow(omx,-1) + ln(x) * ln(1+x * z) * CF * pow(opx,-1) + (-1)* 2 * ln(x) * ln(1+x * z) * CF + 4 * ln(x) * ln(1+x * z) * z * CF * pow(omx,-1) + (-1)* 2 * ln(x) * ln(1+x * z) * z * CF * pow(opx,-1) + 4 * ln(x) * ln(1+x * z) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * ln(x) * ln(1+x * z) * pow(z, 2) * CF + (-1)* 4 * ln(x) * ln(1+x * z) * x * z * CF + (-1)* 2 * ln(x) * ln(z+x) * CF * pow(omx,-1) + ln(x) * ln(z+x) * CF + (-1)* 4 * ln(x) * ln(z+x) * z * CF * pow(omx,-1) + 2 * ln(x) * ln(z+x) * z * CF + (-1)*             4 * ln(x) * ln(z+x) * pow(z, 2) * CF * pow(omx,-1) + 4 * ln(x) * ln(z+x) * pow(z, 2) * CF + ln(x) * ln(z+x) * x * CF + 2 * ln(x) * ln(z+x) * x * z * CF + 3. / 2. * pow(ln(x), 2) * pow(x,-2) * CF * pow(opx,-1) + (-1)* 3. / 2. * pow(ln(x), 2) * pow(x,-2) * CF + (-1)* 3 * pow(ln(x), 2) * pow(x,-2) * z * CF * pow(opx,-1) + 3 * pow(ln(x), 2) * pow(x,-2) * z * CF + 3. / 2. * pow(ln(x), 2) * pow(x,-1) * CF + (-1)* 3 * pow(ln(x), 2) * pow(x,-1) * z * CF + (-1)* 6 * pow(ln(x), 2) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 6 * pow(ln(x), 2) * pow(x,-1) * pow(z, 2) * CF + (-1)* 2 * pow(ln(x), 2) * CF * pow(omx,-1) + (-1)* 5. / 2. * pow(ln(x), 2) * CF * pow(opx,-1) + 3 * pow(ln(x), 2) * CF + 4 * pow(ln(x), 2) * z * CF * pow(omx,-1) + 0;
      tmp +=  + 5 * pow(ln(x), 2) * z * CF * pow(opx,-1) + (-1)* 6 * pow(ln(x), 2) * z * CF + (-1)* 2 * pow(ln(x), 2) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx,-1) + 4 * pow(ln(x), 2) * pow(z, 2) * CF + 2 * pow(ln(x), 2) * x * CF + (-1)* 4 * pow(ln(x), 2) * x * z * CF + (-1)* ln(x) * ln(z) * pow(x,-2) * CF * pow(opx,-1) + ln(x) * ln(z) * pow(x,-2) * CF + 2 * ln(x) * ln(z) * pow(x,-2) * z * CF * pow(opx,-1) + (-1)* 2 * ln(x) * ln(z) * pow(x,-2) * z * CF + (-1)* ln(x) * ln(z) * pow(x,-1) * CF + 2 * ln(x) * ln(z) * pow(x,-1) * z * CF + 4 * ln(x) * ln(z) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 4 * ln(x) * ln(z) * pow(x,-1) * pow(z, 2) * CF + 4 * ln(x) * ln(z) * CF * pow(omx,-1) + (-1)* ln(x) * ln(z) * CF * pow(opx,-1) + (-1)* ln(x) * ln(z) * CF + (-1)* 4 * ln(x) * ln(z) * z * CF * pow(omx,-1) + 2 * ln(x) * ln(z) * z * CF * pow(opx,-1) + 2 * ln(x) * ln(z) * z * CF + 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 4 * ln(x) * ln(z) * pow(z, 2) * CF + ln(x) * ln(z) * x * CF + (-1)* 2 * ln(x) * ln(z) * x * z * CF + 2 * ln(x) * ln(omx) * pow(x,-2) * CF * pow(opx,-1) + (-1)* 2 * ln(x) * ln(omx) * pow(x,-2) * CF + (-1)* 4 * ln(x) * ln(omx) * pow(x,-2) * z * CF * pow(opx,-1) + 4 * ln(x) * ln(omx) * pow(x,-2) * z * CF + 2 * ln(x) * ln(omx) * pow(x,-1) * CF + (-1)* 4 * ln(x) * ln(omx) * pow(x,-1) * z * CF + (-1)* 8 * ln(x) * ln(omx) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 8 * ln(x) * ln(omx) * pow(x,-1) * pow(z, 2) * CF + 3 * ln(x) * ln(omx) * CF * pow(omx,-1) + (-1)* 2 * ln(x) * ln(omx) * CF * pow(opx,-1) + (-1)* 2 * ln(x) * ln(omx) * CF + (-1)* 6 * ln(x) * ln(omx) * z * CF * pow(omx,-1) + 4 * ln(x) * ln(omx) * z * CF * pow(opx,-1) + 4 * ln(x) * ln(omx) * z * CF + 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 8 * ln(x) * ln(omx) * pow(z, 2) * CF + 0;
      tmp +=  + (-1)*2 * ln(x) * ln(opx) * pow(x,-2) * CF * pow(opx,-1) + 2 * ln(x) * ln(opx) * pow(x,-2) * CF + 4 * ln(x) * ln(opx) * pow(x,-2) * z * CF * pow(opx,-1) + (-1)* 4 * ln(x) * ln(opx) * pow(x,-2) * z * CF + (-1)* 2 * ln(x) * ln(opx) * pow(x,-1) * CF + 4 * ln(x) * ln(opx) * pow(x,-1) * z * CF + 8 * ln(x) * ln(opx) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 8 * ln(x) * ln(opx) * pow(x,-1) * pow(z, 2) * CF + (-1)* 2 * ln(x) * ln(opx) * CF * pow(opx,-1) + 2 * ln(x) * ln(opx) * CF + 4 * ln(x) * ln(opx) * z * CF * pow(opx,-1) + (-1)* 4 * ln(x) * ln(opx) * z * CF + 8 * ln(x) * ln(opx) * pow(z, 2) * CF + (-1)*             2 * ln(x) * ln(opx) * x * CF + 4 * ln(x) * ln(opx) * x * z * CF + (-1)* 1. / 2. * ln(z) * CF * pow(poly2,-1) + (-1)* 3 * ln(z) * CF * pow(omx,-1) + 9. / 2. * ln(z) * CF + 7 * ln(z) * CF * rln2 * pow(omx,-1) + (-1)* 4 * ln(z) * CF * rln2 + 3 * ln(z) * CF * sqrtxz1 * pow(omx,-1) + (-1)* 2 * ln(z) * CF * sqrtxz1 + (-1)* 3 * ln(z) * z * CF * pow(omx,-1) + 2 * ln(z) * z * CF + 10 * ln(z) * z * CF * rln2 * pow(omx,-1) + (-1)* 4 * ln(z) * z * CF * rln2 + 16 * ln(z) * pow(z, 2) * CF * rln2 * pow(omx,-1) + (-1)* 16 * ln(z) * pow(z, 2) * CF * rln2 + (-1)* 1. / 2. * ln(z) * x * CF * pow(poly2,-1) + ln(z) * x * CF * pow(xmz,-1) + 3. / 2. * ln(z) * x * CF + (-1)* 2 * ln(z) * x * CF * rln2 + (-1)* 8 * ln(z) * x * z * CF * rln2 + 1. / 2. * ln(z) * pow(x, 2) * CF * pow(poly2,-1) + (-1)* 2 * ln(z) * pow(x, 2) * CF * pow(xmz,-1) + 1. / 2. * ln(z) * pow(x, 3) * CF * pow(poly2,-1) + (-1)* 3 * ln(z) * ln(1+sqrtxz1- z) * CF * pow(omx,-1) + 2 * ln(z) * ln(1+sqrtxz1- z) * CF + (-1)* 2 * ln(z) * ln(1+sqrtxz1- z) * z * CF * pow(omx,-1) + (-1)* 8 * ln(z) * ln(1+sqrtxz1- z) * pow(z, 2) * CF * pow(omx,-1) + 8 * ln(z) * ln(1+sqrtxz1- z) * pow(z, 2) * CF + 4 * ln(z) * ln(1+sqrtxz1- z) * x * z * CF + (-1)* 4 * ln(z) * ln(1+sqrtxz1+z) * CF * pow(omx,-1) + 2 * ln(z) * ln(1+sqrtxz1+z) * CF + 0;
      tmp +=  + (-1)*8 * ln(z) * ln(1+sqrtxz1+z) * z * CF * pow(omx,-1) + 4 * ln(z) * ln(1+sqrtxz1+z) * z * CF + (-1)* 8 * ln(z) * ln(1+sqrtxz1+z) * pow(z, 2) * CF * pow(omx,-1) + 8 * ln(z) * ln(1+sqrtxz1+z) * pow(z, 2) * CF + 2 * ln(z) * ln(1+sqrtxz1+z) * x * CF + 4 * ln(z) * ln(1+sqrtxz1+z) * x * z * CF + (-1)* ln(z) * ln(1+x * pow(z,-1)) * pow(x,-2) * CF * pow(opx,-1) + ln(z) * ln(1+x * pow(z,-1)) * pow(x,-2) * CF + 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(x,-2) * z * CF * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(x,-2) * z * CF + (-1)* ln(z) * ln(1+x * pow(z,-1)) * pow(x,-1) * CF + 2 * ln(z) * ln(1+x * pow(z,-1)) * pow(x,-1) * z * CF + 4 * ln(z) * ln(1+x * pow(z,-1)) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 4 * ln(z) * ln(1+x * pow(z,-1)) * pow(x,-1) * pow(z, 2) * CF + (-1)* ln(z) * ln(1+x * pow(z,-1)) * CF * pow(opx,-1) + ln(z) * ln(1+x * pow(z,-1)) * CF + 2 * ln(z) * ln(1+x * pow(z,-1)) * z * CF * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * pow(z,-1)) * z * CF + 4 * ln(z) * ln(1+x * pow(z,-1)) * pow(z, 2) * CF + (-1)* ln(z) * ln(1+x * pow(z,-1)) * x * CF + 2 * ln(z) * ln(1+x * pow(z,-1)) * x * z * CF + ln(z) * ln(1+x * z) * pow(x,-2) * CF * pow(opx,-1) + (-1)* ln(z) * ln(1+x * z) * pow(x,-2) * CF + (-1)* 2 * ln(z) * ln(1+x * z) * pow(x,-2) * z * CF * pow(opx,-1) + 2 * ln(z) * ln(1+x * z) * pow(x,-2) * z * CF + ln(z) * ln(1+x * z) * pow(x,-1) * CF + (-1)* 2 * ln(z) * ln(1+x * z) * pow(x,-1) * z * CF + (-1)* 4 * ln(z) * ln(1+x * z) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 4 * ln(z) * ln(1+x * z) * pow(x,-1) * pow(z, 2) * CF + 2 * ln(z) * ln(1+x * z) * CF * pow(omx,-1) + ln(z) * ln(1+x * z) * CF * pow(opx,-1) + (-1)* 2 * ln(z) * ln(1+x * z) * CF + 4 * ln(z) * ln(1+x * z) * z * CF * pow(omx,-1) + 0;
      tmp +=  + (-1)*2 * ln(z) * ln(1+x * z) * z * CF * pow(opx,-1) + 4 * ln(z) * ln(1+x * z) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * ln(z) * ln(1+x * z) * pow(z, 2) * CF + (-1)* 4 * ln(z) * ln(1+x * z) * x * z * CF + 2 * ln(z) * ln(z+x) * CF * pow(omx,-1) + (-1)* ln(z) * ln(z+x) * CF + 4 * ln(z) * ln(z+x) * z * CF * pow(omx,-1) + (-1)* 2 * ln(z) * ln(z+x) * z * CF + 4 * ln(z) * ln(z+x) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 4 * ln(z) * ln(z+x) * pow(z, 2) * CF + (-1)* ln(z) * ln(z+x) * x * CF + (-1)* 2 * ln(z) * ln(z+x) * x * z * CF + (-1)* 1. / 2. * pow(ln(z), 2) * pow(x,-2) * CF * pow(opx,-1) + 1. / 2. * pow(ln(z), 2) * pow(x,-2) * CF + pow(ln(z), 2) * pow(x,-2) * z * CF * pow(opx,-1) + (-1)* pow(ln(z), 2) * pow(x,-2) * z * CF + (-1)* 1. / 2. * pow(ln(z), 2) * pow(x,-1) * CF + pow(ln(z), 2) * pow(x,-1) * z * CF + 2 * pow(ln(z), 2) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 2 * pow(ln(z), 2) * pow(x,-1) * pow(z, 2) * CF + (-1)* pow(ln(z), 2) * CF * pow(omx,-1) + (-1)* 1. / 2. * pow(ln(z), 2) * CF * pow(opx,-1) + 2 * pow(ln(z), 2) * CF + 2 * pow(ln(z), 2) * z * CF * pow(omx,-1) + pow(ln(z), 2) * z * CF * pow(opx,-1) + (-1)* 4 * pow(ln(z), 2) * z * CF + (-1)* 2 * pow(ln(z), 2) * pow(z, 2) * CF * pow(omx,-1) + 4 * pow(ln(z), 2) * pow(z, 2) * CF + (-1)* pow(ln(z), 2) * x * CF + 2 * pow(ln(z), 2) * x * z * CF + ln(z) * ln(omz) * CF * pow(omx,-1) + (-1)* 2 * ln(z) * ln(omz) * CF + (-1)* 2 * ln(z) * ln(omz) * z * CF * pow(omx,-1) + 4 * ln(z) * ln(omz) * z * CF + 8 * ln(sqrtxz3) * ArcTan(sqrtxz3) * z * CF * sqrtxz3 + (-1)* 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)- 1. / 2. * pow(x,-1) * sqrtxz2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)- 1. / 2. * pow(x,-1) * sqrtxz2) * CF * pow(sqrtxz2,-1) + (-1)* 5. / 2. * Li2(1. / 2.- 1. / 2. * pow(x,-1)- 1. / 2. * pow(x,-1) * sqrtxz2) * x * CF * pow(sqrtxz2,-1) + 0;
      tmp +=  + 5 * Li2(1. / 2.- 1. / 2. * pow(x,-1)- 1. / 2. * pow(x,-1) * sqrtxz2) * x * z * CF * pow(sqrtxz2,-1) + 1. / 2. * Li2(1. / 2.- 1. / 2. * pow(x,-1)- 1. / 2. * pow(x,-1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)- 1. / 2. * pow(x,-1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2,-1) + (-1)* 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)- 1. / 2. * pow(x,-1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)+1. / 2. * pow(x,-1) * sqrtxz2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)+1. / 2. * pow(x,-1) * sqrtxz2) * CF * pow(sqrtxz2,-1) + 5. / 2. * Li2(1. / 2.- 1. / 2. * pow(x,-1)+1. / 2. * pow(x,-1) * sqrtxz2) * x * CF * pow(sqrtxz2,-1) + (-1)* 5 * Li2(1. / 2.- 1. / 2. * pow(x,-1)+1. / 2. * pow(x,-1) * sqrtxz2) * x * z * CF * pow(sqrtxz2,-1) + (-1)* 1. / 2. * Li2(1. / 2.- 1. / 2. * pow(x,-1)+1. / 2. * pow(x,-1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)+1. / 2. * pow(x,-1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2,-1) + 1. / 4. * Li2(1. / 2.- 1. / 2. * pow(x,-1)+1. / 2. * pow(x,-1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + Li2(1. / 2.- 1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * CF * pow(omx,-1) + 6 * Li2(1. / 2.- 1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * z * CF * pow(omx,-1) + (-1)* 4 * Li2(1. / 2.- 1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * z * CF + (-1)* 2 * Li2(1. / 2.- 1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * x * CF + (-1)* Li2(1. / 2.+1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * CF * pow(omx,-1) + 0;
      tmp +=  + (-1)*6 * Li2(1. / 2.+1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * z * CF * pow(omx,-1) + 4 * Li2(1. / 2.+1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * z * CF + 2 * Li2(1. / 2.+1. / 2. * pow(z,-1)- 1. / 2. * pow(z,-1) * sqrtxz1) * x * CF + 1. / 4. * Li2(1. / 2.- 1. / 2. * sqrtxz2- 1. / 2. * x) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 1. / 4. * Li2(1. / 2.- 1. / 2. * sqrtxz2- 1. / 2. * x) * CF * pow(sqrtxz2,-1) + 5. / 2. * Li2(1. / 2.- 1. / 2. * sqrtxz2- 1. / 2. * x) * x * CF * pow(sqrtxz2,-1) + (-1)* 5 * Li2(1. / 2.- 1. / 2. * sqrtxz2- 1. / 2. * x) * x * z * CF * pow(sqrtxz2,-1) + (-1)* 1. / 2. * Li2(1. / 2.- 1. / 2. * sqrtxz2- 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 1. / 4. * Li2(1. / 2.- 1. / 2. * sqrtxz2- 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2,-1) + 1. / 4. * Li2(1. / 2.- 1. / 2. * sqrtxz2- 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 1. / 4. * Li2(1. / 2.+1. / 2. * sqrtxz2- 1. / 2. * x) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * Li2(1. / 2.+1. / 2. * sqrtxz2- 1. / 2. * x) * CF * pow(sqrtxz2,-1) + (-1)* 5. / 2. * Li2(1. / 2.+1. / 2. * sqrtxz2- 1. / 2. * x) * x * CF * pow(sqrtxz2,-1) + 5 * Li2(1. / 2.+1. / 2. * sqrtxz2- 1. / 2. * x) * x * z * CF * pow(sqrtxz2,-1) + 1. / 2. * Li2(1. / 2.+1. / 2. * sqrtxz2- 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + 1. / 4. * Li2(1. / 2.+1. / 2. * sqrtxz2- 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2,-1) + (-1)* 1. / 4. * Li2(1. / 2.+1. / 2. * sqrtxz2- 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2,-1) * pow(poly2,-1) + (-1)* 3 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * CF * pow(omx,-1) + 2 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * CF + (-1)* 2 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * z * CF * pow(omx,-1) + 0;
      tmp +=  + (-1)*8 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * pow(z, 2) * CF * pow(omx,-1) + 8 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * pow(z, 2) * CF + 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1- 1. / 2. * z) * x * z * CF + 3 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * CF * pow(omx,-1) + (-1)* 2 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * CF + 2 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * z * CF * pow(omx,-1) + 8 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * pow(z, 2) * CF + (-1)* 4 * Li2(1. / 2.- 1. / 2. * sqrtxz1+1. / 2. * z) * x * z * CF + (-1)* Li2(1- x * pow(z,-1)) * CF * pow(omx,-1) + 2 * Li2(1- x * pow(z,-1)) * CF + 2 * Li2(1- x * pow(z,-1)) * z * CF * pow(omx,-1) + (-1)* 4 * Li2(1- x * pow(z,-1)) * z * CF + Li2(-x * pow(z,-1)) * pow(x,-2) * CF * pow(opx,-1) + (-1)* Li2(-x * pow(z,-1)) * pow(x,-2) * CF + (-1)* 2 * Li2(-x * pow(z,-1)) * pow(x,-2) * z * CF * pow(opx,-1) + 2 * Li2(-x * pow(z,-1)) * pow(x,-2) * z * CF + Li2(-x * pow(z,-1)) * pow(x,-1) * CF + (-1)* 2 * Li2(-x * pow(z,-1)) * pow(x,-1) * z * CF + (-1)* 4 * Li2(-x * pow(z,-1)) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 4 * Li2(-x * pow(z,-1)) * pow(x,-1) * pow(z, 2) * CF + (-1)* 2 * Li2(-x * pow(z,-1)) * CF * pow(omx,-1) + Li2(-x * pow(z,-1)) * CF * pow(opx,-1) + (-1)* 4 * Li2(-x * pow(z,-1)) * z * CF * pow(omx,-1) + (-1)* 2 * Li2(-x * pow(z,-1)) * z * CF * pow(opx,-1) + 4 * Li2(-x * pow(z,-1)) * z * CF + (-1)* 4 * Li2(-x * pow(z,-1)) * pow(z, 2) * CF * pow(omx,-1) + 2 * Li2(-x * pow(z,-1)) * x * CF + (-1)* 2 * Li2(-x) * pow(x,-2) * CF * pow(opx,-1) + 2 * Li2(-x) * pow(x,-2) * CF + 4 * Li2(-x) * pow(x,-2) * z * CF * pow(opx,-1) + (-1)* 4 * Li2(-x) * pow(x,-2) * z * CF + 0;
      tmp +=  + (-1)*2 * Li2(-x) * pow(x,-1) * CF + 4 * Li2(-x) * pow(x,-1) * z * CF + 8 * Li2(-x) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 8 * Li2(-x) * pow(x,-1) * pow(z, 2) * CF + 2 * Li2(-x) * CF * pow(opx,-1) + (-1)* 4 * Li2(-x) * CF + (-1)* 4 * Li2(-x) * z * CF * pow(opx,-1) + 8 * Li2(-x) * z * CF + 8 * Li2(-x) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 4 * Li2(-x) * x * CF + 8 * Li2(-x) * x * z * CF + Li2(-x * z) * pow(x,-2) * CF * pow(opx,-1) + (-1)* Li2(-x * z) * pow(x,-2) * CF + (-1)* 2 * Li2(-x * z) * pow(x,-2) * z * CF * pow(opx,-1) + 2 * Li2(-x * z) * pow(x,-2) * z * CF + Li2(-x * z) * pow(x,-1) * CF + (-1)* 2 * Li2(-x * z) * pow(x,-1) * z * CF + (-1)* 4 * Li2(-x * z) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 4 * Li2(-x * z) * pow(x,-1) * pow(z, 2) * CF + 2 * Li2(-x * z) * CF * pow(omx,-1) + Li2(-x * z) * CF * pow(opx,-1) + (-1)* 2 * Li2(-x * z) * CF + 4 * Li2(-x * z) * z * CF * pow(omx,-1) + (-1)* 2 * Li2(-x * z) * z * CF * pow(opx,-1) + 4 * Li2(-x * z) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * Li2(-x * z) * pow(z, 2) * CF + (-1)* 4 * Li2(-x * z) * x * z * CF + 2 * Li2(x) * pow(x,-2) * CF * pow(opx,-1) + (-1)* 2 * Li2(x) * pow(x,-2) * CF + (-1)* 4 * Li2(x) * pow(x,-2) * z * CF * pow(opx,-1) + 4 * Li2(x) * pow(x,-2) * z * CF + 2 * Li2(x) * pow(x,-1) * CF + (-1)* 4 * Li2(x) * pow(x,-1) * z * CF + (-1)* 8 * Li2(x) * pow(x,-1) * pow(z, 2) * CF * pow(opx,-1) + 8 * Li2(x) * pow(x,-1) * pow(z, 2) * CF + 3 * Li2(x) * CF * pow(omx,-1) + (-1)* 2 * Li2(x) * CF * pow(opx,-1) + (-1)* 2 * Li2(x) * CF + (-1)* 6 * Li2(x) * z * CF * pow(omx,-1) + 4 * Li2(x) * z * CF * pow(opx,-1) + 4 * Li2(x) * z * CF + 8 * Li2(x) * pow(z, 2) * CF * pow(omx,-1) + (-1)* 8 * Li2(x) * pow(z, 2) * CF * pow(opx,-1) + (-1)* 8 * Li2(x) * pow(z, 2) * CF + Li2(z) * CF * pow(omx,-1) + (-1)* 2 * Li2(z) * CF + (-1)* 2 * Li2(z) * z * CF * pow(omx,-1) + 0;
      tmp +=  + 4 * Li2(z) * z * CF + 4 * InvTanInt(-sqrtxz3) * z * CF * sqrtxz3 + 8 * InvTanInt(z * sqrtxz3) * z * CF * sqrtxz3 + (-1)* 4 * InvTanInt(sqrtxz3) * z * CF * sqrtxz3 + 0;
      res += tmp;
    }
    return res;
  }
}