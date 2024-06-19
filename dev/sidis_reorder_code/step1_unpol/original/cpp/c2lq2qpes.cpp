double C2Lq2qpEs(double inx, double inz, std::string cx, std::string cz,
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
    res = 0;

    return res;
  }
  if (cx == "D" && cz == "0")
  {
    res = 0;

    return res;
  }
  if (cx == "D" && cz == "1")
  {
    res = 0;

    return res;
  }
  if (cx == "D" && cz == "2")
  {
    res = 0;

    return res;
  }
  if (cx == "D" && cz == "3")
  {
    res = 0;

    return res;
  }
  if (cx == "0" && cz == "D")
  {
    res = 0;

    return res;
  }
  if (cx == "0" && cz == "0")
  {
    res = 0;

    return res;
  }
  if (cx == "0" && cz == "1")
  {
    res = 0;

    return res;
  }
  if (cx == "0" && cz == "2")
  {
    res = 0;

    return res;
  }
  if (cx == "0" && cz == "3")
  {
    res = 0;

    return res;
  }
  if (cx == "1" && cz == "D")
  {
    res = 0;

    return res;
  }
  if (cx == "1" && cz == "0")
  {
    res = 0;

    return res;
  }
  if (cx == "1" && cz == "1")
  {
    res = 0;

    return res;
  }
  if (cx == "1" && cz == "2")
  {
    res = 0;

    return res;
  }
  if (cx == "1" && cz == "3")
  {
    res = 0;

    return res;
  }
  if (cx == "2" && cz == "D")
  {
    res = 0;

    return res;
  }
  if (cx == "2" && cz == "0")
  {
    res = 0;

    return res;
  }
  if (cx == "2" && cz == "1")
  {
    res = 0;

    return res;
  }
  if (cx == "2" && cz == "2")
  {
    res = 0;

    return res;
  }
  if (cx == "2" && cz == "3")
  {
    res = 0;

    return res;
  }
  if (cx == "3" && cz == "D")
  {
    res = 0;

    return res;
  }
  if (cx == "3" && cz == "0")
  {
    res = 0;

    return res;
  }
  if (cx == "3" && cz == "1")
  {
    res = 0;

    return res;
  }
  if (cx == "3" && cz == "2")
  {
    res = 0;

    return res;
  }
  if (cx == "3" && cz == "3")
  {
    res = 0;

    return res;
  }
  if (cx == "D" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    res = 0;

    return res;
  }
  if (cx == "0" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    res = 0;

    return res;
  }
  if (cx == "1" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    res = 0;

    return res;
  }
  if (cx == "2" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    res = 0;

    return res;
  }
  if (cx == "3" && cz == "R")
  {
    double z = inz;
    double omz = 1. - z;
    double opz = 1. + z;
    res = 0;

    return res;
  }
  if (cx == "R" && cz == "D")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    res = 0;

    return res;
  }
  if (cx == "R" && cz == "0")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    res = 0;

    return res;
  }
  if (cx == "R" && cz == "1")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    res = 0;

    return res;
  }
  if (cx == "R" && cz == "2")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    res = 0;

    return res;
  }
  if (cx == "R" && cz == "3")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    res = 0;

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
      tmp = 0;

      res += tmp;
    }
    if (z > 1. - x && z < x)
    {
      double tmp = 0.0;
      tmp = 0;

      res += tmp;
    }
    if (z < 1. - x && z > x)
    {
      double tmp = 0.0;
      tmp = 0;

      res += tmp;
    }
    if (z > 1. - x && z > x)
    {
      double tmp = 0.0;
      tmp = 0;

      res += tmp;
    }
    if (z > x)
    {
      double tmp = 0.0;
      tmp = 0;

      res += tmp;
    }
    if (z < x)
    {
      double tmp = 0.0;
      tmp = 0;

      res += tmp;
    }
    if (z < 1. - x)
    {
      double tmp = 0.0;
      tmp = 0;

      res += tmp;
    }
    if (z > 1. - x)
    {
      double tmp = 0.0;
      tmp = 0;

      res += tmp;
    }
    if (z != x && z != 1. - x)
    {
      double tmp = 0.0;
      tmp = -4. / 3. * pow(x, -1) * z * pow(pi, 2) * CF * pow(opx, -1) + 4. / 3. * pow(x, -1) * z * pow(pi, 2) * CF + 8. / 3. * pow(x, -1) * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1) - 8. / 3. * pow(x, -1) * pow(z, 2) * pow(pi, 2) * CF + 2 * CF -
            2 * z * CF - 4. / 3. * z * pow(pi, 2) * CF * pow(opx, -1) + 8. / 3. * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1) - 2 * x * CF - 8 * x * sqrtxz1 * rln2 * CF + 2 * x * z * CF - 4. / 3. * x * z * pow(pi, 2) * CF - 32 * x * pow(z, 2) * pow(rln2, 2) * CF + 8. / 3. * x * pow(z, 2) * pow(pi, 2) * CF - 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * sqrtxz3 * CF - 46 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 6 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * z * sqrtxz3 * CF + 2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * sqrtxz3 * CF + 46 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 6 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * z * sqrtxz3 * CF + InvTanInt(-sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - InvTanInt(-sqrtxz3) * sqrtxz3 * CF + 23 * InvTanInt(-sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 3 * InvTanInt(-sqrtxz3) * x * z * sqrtxz3 * CF + 2 * InvTanInt(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 2 * InvTanInt(z * sqrtxz3) * sqrtxz3 * CF + 46 * InvTanInt(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 6 * InvTanInt(z * sqrtxz3) * x * z * sqrtxz3 * CF - InvTanInt(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + InvTanInt(sqrtxz3) * sqrtxz3 * CF - 23 * InvTanInt(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3 * InvTanInt(sqrtxz3) * x * z * sqrtxz3 * CF + 8 * ln(1 + sqrtxz1 - z) * x * sqrtxz1 * CF - 8 * ln(1 + sqrtxz1 - z) * x * z * rln2 * CF;
      tmp += +48 * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * rln2 * CF + 8 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF -
             16 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, 2) * CF - 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF - 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF + 8 * ln(1 + sqrtxz1 + z) * x * z * rln2 * CF + 16 * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * rln2 * CF + 1. / 2. * ln(x) * pow(x, -1) * pow(poly2, -1) * CF - 1. / 2. * ln(x) * pow(x, -1) * CF - 16 * ln(x) * pow(x, -1) * z * CF * pow(opx, -1) + 16 * ln(x) * pow(x, -1) * z * CF + 32 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 32 * ln(x) * pow(x, -1) * pow(z, 2) * CF - 1. / 2. * ln(x) * pow(poly2, -1) * CF + 1. / 2. * ln(x) * CF - 16 * ln(x) * z * CF * pow(opx, -1) - ln(x) * z * CF + 32 * ln(x) * pow(z, 2) * CF * pow(opx, -1) - ln(x) * x * pow(poly2, -1) * CF + 11. / 2. * ln(x) * x * CF - 4 * ln(x) * x * sqrtxz1 * CF - 5 * ln(x) * x * z * CF + 8 * ln(x) * x * z * rln2 * CF - 32 * ln(x) * x * pow(z, 2) * rln2 * CF + ln(x) * pow(x, 2) * pow(poly2, -1) * CF - 4 * ln(x) * pow(x, 2) * CF * pow(xmz, -1) - 7. / 2. * ln(x) * pow(x, 2) * CF + 1. / 2. * ln(x) * pow(x, 3) * pow(poly2, -1) * CF + 4 * ln(x) * pow(x, 3) * CF * pow(xmz, -1) - 1. / 2. * ln(x) * pow(x, 4) * pow(poly2, -1) * CF + 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(sqrtxz2, -1) * CF - ln(x) * ln(1 - sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF - 3. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 4 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF + 12 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF;
      tmp += -12 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 9. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 9 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF +
             1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(sqrtxz2, -1) * CF + ln(x) * ln(1 + sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF + 3. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF - 12 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF + 12 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 9. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 9 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF + 16 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF + 16 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1);
      tmp += -4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF - 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF - 8 * ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF - 8 * ln(x) * ln(1 + x) * x * CF + 24 * ln(x) * ln(1 + x) * x * z * CF - 16 * ln(x) * ln(1 + x) * x * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF - 8 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1) - 16 * ln(x) * ln(1 + x * z) * x * pow(z, 2) * CF + 4 * ln(x) * ln(z + x) * x * z * CF + 8 * ln(x) * ln(z + x) * x * pow(z, 2) * CF + 6 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(opx, -1) - 6 * pow(ln(x), 2) * pow(x, -1) * z * CF - 12 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 12 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF + 6 * pow(ln(x), 2) * z * CF * pow(opx, -1) - 12 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1) + 4 * pow(ln(x), 2) * x * CF - 12 * pow(ln(x), 2) * x * z * CF + 8 * pow(ln(x), 2) * x * pow(z, 2) * CF - 4 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(z) * pow(x, -1) * z * CF + 8 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF - 4 * ln(x) * ln(z) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(opx, -1) + 4 * ln(x) * ln(z) * x * z * CF;
      tmp += -8 * ln(x) * ln(z) * x * pow(z, 2) * CF + 8 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(omx) * pow(x, -1) * z * CF - 16 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 16 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF + 8 * ln(x) * ln(omx) * z * CF * pow(opx, -1) - 16 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(omx) * x * z * CF - 16 * ln(x) * ln(omx) * x * pow(z, 2) * CF - 8 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(opx) * pow(x, -1) * z * CF + 16 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 16 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF - 8 * ln(x) * ln(opx) * z * CF * pow(opx, -1) + 16 * ln(x) * ln(opx) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(x) * ln(opx) * x * z * CF + 16 * ln(x) * ln(opx) * x * pow(z, 2) * CF + 1. / 2. * ln(z) * pow(x, -1) * pow(poly2, -1) * CF - 1. / 2. * ln(z) * pow(x, -1) * CF + 1. / 2. * ln(z) * pow(poly2, -1) * CF + 3. / 2. * ln(z) * CF - ln(z) * z * CF - ln(z) * x * pow(poly2, -1) * CF - 1. / 2. * ln(z) * x * CF - 4 * ln(z) * x * sqrtxz1 * CF + 5 * ln(z) * x * z * CF - 8 * ln(z) * x * z * rln2 * CF - 32 * ln(z) * x * pow(z, 2) * rln2 * CF - ln(z) * pow(x, 2) * pow(poly2, -1) * CF + 4 * ln(z) * pow(x, 2) * CF * pow(xmz, -1) + 7. / 2. * ln(z) * pow(x, 2) * CF + 1. / 2. * ln(z) * pow(x, 3) * pow(poly2, -1) * CF - 4 * ln(z) * pow(x, 3) * CF * pow(xmz, -1) + 1. / 2. * ln(z) * pow(x, 4) * pow(poly2, -1) * CF + 16 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF + 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF + 16 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF + 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1);
      tmp += -8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF - 4 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1) + 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF + 8 * ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF + 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF - 8 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1) - 8 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1) - 16 * ln(z) * ln(1 + x * z) * x * pow(z, 2) * CF -
             4 * ln(z) * ln(z + x) * x * z * CF - 8 * ln(z) * ln(z + x) * x * pow(z, 2) * CF - 2 * pow(ln(z), 2) * pow(x, -1) * z * CF * pow(opx, -1) + 2 * pow(ln(z), 2) * pow(x, -1) * z * CF + 4 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 4 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF - 2 * pow(ln(z), 2) * z * CF * pow(opx, -1) + 4 * pow(ln(z), 2) * pow(z, 2) * CF * pow(opx, -1) + 2 * pow(ln(z), 2) * x * CF - 8 * pow(ln(z), 2) * x * z * CF + 8 * pow(ln(z), 2) * x * pow(z, 2) * CF - 4 * ln(z) * ln(omz) * x * CF + 8 * ln(z) * ln(omz) * x * z * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF - 3. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF;
      tmp += -4 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF + 12 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF - 12 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 9. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 9 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF + 3. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF - 12 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF + 12 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF;
      tmp += +9. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 9 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * x * z * CF + 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * x * z * CF - 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(sqrtxz2, -1) * CF + Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * z * pow(sqrtxz2, -1) * CF +
             3. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 4 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * CF - 12 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(sqrtxz2, -1) * CF + 12 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 9. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 9 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF;
      tmp += -1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(sqrtxz2, -1) * CF - Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * z * pow(sqrtxz2, -1) * CF - 3. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 4 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * CF + 12 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(sqrtxz2, -1) * CF - 12 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 9. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 9 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 16 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * x * pow(z, 2) * CF - 16 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * x * pow(z, 2) * CF + 4 * Li2(1 - x * pow(z, -1)) * x * CF - 8 * Li2(1 - x * pow(z, -1)) * x * z * CF + 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF;
      tmp += -8 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF + 4 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1) - 8 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(-x * pow(z, -1)) * x * z * CF - 8 * Li2(-x) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * Li2(-x) * pow(x, -1) * z * CF + 16 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 16 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF - 8 * Li2(-x) * z * CF * pow(opx, -1) + 16 * Li2(-x) * pow(z, 2) * CF * pow(opx, -1) - 8 * Li2(-x) * x * CF + 16 * Li2(-x) * x * z * CF + 4 * Li2(-x * z) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * Li2(-x * z) * pow(x, -1) * z * CF - 8 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF + 4 * Li2(-x * z) * z * CF * pow(opx, -1) - 8 * Li2(-x * z) * pow(z, 2) * CF * pow(opx, -1) -
             16 * Li2(-x * z) * x * pow(z, 2) * CF + 8 * Li2(x) * pow(x, -1) * z * CF * pow(opx, -1) - 8 * Li2(x) * pow(x, -1) * z * CF - 16 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 16 * Li2(x) * pow(x, -1) * pow(z, 2) * CF + 8 * Li2(x) * z * CF * pow(opx, -1) - 16 * Li2(x) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(x) * x * z * CF - 16 * Li2(x) * x * pow(z, 2) * CF - 4 * Li2(z) * x * CF + 8 * Li2(z) * x * z * CF;

      res += tmp;
    }
    return res;
  }
}