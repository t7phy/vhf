double C2Lq2gEq(double inx, double inz, std::string cx, std::string cz,
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
      tmp = 8. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF - 6 * pow(NC, -1) * x * pow(pi, 2) * CF + 10. / 3. * pow(NC, -1) * x * z * pow(pi, 2) * CF - 24 * ln(x) * pow(NC, -1) * x * CF + 24 * ln(x) * pow(NC, -1) * x * z * CF - 14 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 40 * pow(ln(x), 2) * pow(NC, -1) * x * CF - 26 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF - 44 * ln(x) * ln(z) * pow(NC, -1) * x * CF + 32 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF + 24 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF - 64 * ln(x) * ln(omx) * pow(NC, -1) * x * CF + 40 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF + 24 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF - 68 * ln(x) * ln(omz) * pow(NC, -1) * x * CF + 44 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF + 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF - 4 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF + 12 * ln(x) * ln(omxmz) * pow(NC, -1) * x * CF - 8 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF + 12 * ln(z) * pow(NC, -1) * x * CF - 12 * ln(z) * pow(NC, -1) * x * z * CF - 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 12 * pow(ln(z), 2) * pow(NC, -1) * x * CF - 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF - 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF + 24 * ln(z) * ln(omx) * pow(NC, -1) * x * CF - 16 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF - 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 32 * ln(z) * ln(omz) * pow(NC, -1) * x * CF - 24 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF - 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF + 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF + 12 * ln(omx) * pow(NC, -1) * x * CF - 12 * ln(omx) * pow(NC, -1) * x * z * CF - 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF;
      tmp += +18 * pow(ln(omx), 2) * pow(NC, -1) * x * CF - 10 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF - 20 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 52 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF - 32 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF + 16 * ln(omz) * pow(NC, -1) * x * CF - 16 * ln(omz) * pow(NC, -1) * x * z * CF - 10 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 26 * pow(ln(omz), 2) * pow(NC, -1) * x * CF - 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF + 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF - 12 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF + 8 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF - 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF - 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF + 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF + 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1) * CF - 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF - 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * CF - 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * z * CF - 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(z) * pow(NC, -1) * x * CF - 4 * Li2(z) * pow(NC, -1) * x * z * CF;

      res += tmp;
    }
    if (z > 1. - x && z < x)
    {
      double tmp = 0.0;
      tmp = 8. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF - 6 * pow(NC, -1) * x * pow(pi, 2) * CF + 10. / 3. * pow(NC, -1) * x * z * pow(pi, 2) * CF - 24 * ln(x) * pow(NC, -1) * x * CF + 24 * ln(x) * pow(NC, -1) * x * z * CF - 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF + 12 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF - 8 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF - 12 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 38 * pow(ln(x), 2) * pow(NC, -1) * x * CF - 26 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF + 16 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF -
            56 * ln(x) * ln(z) * pow(NC, -1) * x * CF + 40 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF + 20 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF - 52 * ln(x) * ln(omx) * pow(NC, -1) * x * CF + 32 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF + 20 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF - 64 * ln(x) * ln(omz) * pow(NC, -1) * x * CF + 44 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF + 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(xmz) * pow(NC, -1) * x * z * CF + 12 * ln(z) * pow(NC, -1) * x * CF - 12 * ln(z) * pow(NC, -1) * x * z * CF - 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 12 * pow(ln(z), 2) * pow(NC, -1) * x * CF - 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF - 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF + 24 * ln(z) * ln(omx) * pow(NC, -1) * x * CF - 16 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF - 12 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 44 * ln(z) * ln(omz) * pow(NC, -1) * x * CF - 32 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF - 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * CF + 4 * ln(z) * ln(xmz) * pow(NC, -1) * x * z * CF + 12 * ln(omx) * pow(NC, -1) * x * CF - 12 * ln(omx) * pow(NC, -1) * x * z * CF - 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF;
      tmp += +18 * pow(ln(omx), 2) * pow(NC, -1) * x * CF - 10 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF - 16 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 40 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF - 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF + 16 * ln(omz) * pow(NC, -1) * x * CF - 16 * ln(omz) * pow(NC, -1) * x * z * CF + 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF - 12 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF + 8 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF - 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 24 * pow(ln(omz), 2) * pow(NC, -1) * x * CF - 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1) * CF - 8 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * CF + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * z * CF - 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1) * CF + 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF - 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * CF + 4 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF - 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(z) * pow(NC, -1) * x * CF - 4 * Li2(z) * pow(NC, -1) * x * z * CF;

      res += tmp;
    }
    if (z < 1. - x && z > x)
    {
      double tmp = 0.0;
      tmp = 8. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF - 26. / 3. * pow(NC, -1) * x * pow(pi, 2) * CF + 6 * pow(NC, -1) * x * z * pow(pi, 2) * CF - 24 * ln(x) * pow(NC, -1) * x * CF + 24 * ln(x) * pow(NC, -1) * x * z * CF + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF - 14 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 42 * pow(ln(x), 2) * pow(NC, -1) * x * CF - 28 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF - 48 * ln(x) * ln(z) * pow(NC, -1) * x * CF + 36 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF + 24 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF - 60 * ln(x) * ln(omx) * pow(NC, -1) * x * CF + 36 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF + 24 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF - 72 * ln(x) * ln(omz) * pow(NC, -1) * x * CF + 48 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF - 4 * ln(x) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF + 12 * ln(x) * ln(omxmz) * pow(NC, -1) * x * CF - 8 * ln(x) * ln(omxmz) * pow(NC, -1) * x * z * CF +
            12 * ln(z) * pow(NC, -1) * x * CF - 12 * ln(z) * pow(NC, -1) * x * z * CF - 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF +
            4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF - 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 14 * pow(ln(z), 2) * pow(NC, -1) * x * CF - 12 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF - 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF + 20 * ln(z) * ln(omx) * pow(NC, -1) * x * CF - 12 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF - 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 36 * ln(z) * ln(omz) * pow(NC, -1) * x * CF - 28 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF + 12 * ln(omx) * pow(NC, -1) * x * CF - 12 * ln(omx) * pow(NC, -1) * x * z * CF - 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF;
      tmp += +22 * pow(ln(omx), 2) * pow(NC, -1) * x * CF - 14 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF - 20 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 44 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF - 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF + 16 * ln(omz) * pow(NC, -1) * x * CF - 16 * ln(omz) * pow(NC, -1) * x * z * CF - 10 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 30 * pow(ln(omz), 2) * pow(NC, -1) * x * CF - 20 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF + 4 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * pow(z, -1) * CF - 12 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * CF + 8 * ln(omz) * ln(omxmz) * pow(NC, -1) * x * z * CF + 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF - 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF + 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * pow(z, -1) * CF - 4 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x * CF + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * CF - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * pow(NC, -1) * x * z * CF - 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * CF - 4 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x * z * CF - 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(z) * pow(NC, -1) * x * CF - 4 * Li2(z) * pow(NC, -1) * x * z * CF;

      res += tmp;
    }
    if (z > 1. - x && z > x)
    {
      double tmp = 0.0;
      tmp = 8. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF - 6 * pow(NC, -1) * x * pow(pi, 2) * CF + 10. / 3. * pow(NC, -1) * x * z * pow(pi, 2) * CF - 24 * ln(x) * pow(NC, -1) * x * CF + 24 * ln(x) * pow(NC, -1) * x * z * CF - 4 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF + 12 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * CF - 8 * ln(x) * ln(-omxmz) * pow(NC, -1) * x * z * CF + 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(-xmz) * pow(NC, -1) * x * z * CF - 12 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 36 * pow(ln(x), 2) * pow(NC, -1) * x * CF - 24 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF + 16 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF - 52 * ln(x) * ln(z) * pow(NC, -1) * x * CF + 36 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF + 20 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF - 56 * ln(x) * ln(omx) * pow(NC, -1) * x * CF + 36 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF + 20 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF - 60 * ln(x) * ln(omz) * pow(NC, -1) * x * CF + 40 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF + 12 * ln(z) * pow(NC, -1) * x * CF - 12 * ln(z) * pow(NC, -1) * x * z * CF - 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * CF + 4 * ln(z) * ln(-xmz) * pow(NC, -1) * x * z * CF - 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 10 * pow(ln(z), 2) * pow(NC, -1) * x * CF - 8 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF - 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF + 28 * ln(z) * ln(omx) * pow(NC, -1) * x * CF - 20 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF - 12 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 40 * ln(z) * ln(omz) * pow(NC, -1) * x * CF - 28 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF + 12 * ln(omx) * pow(NC, -1) * x * CF - 12 * ln(omx) * pow(NC, -1) * x * z * CF - 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF;
      tmp += +18 * pow(ln(omx), 2) * pow(NC, -1) * x * CF - 10 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF - 16 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 40 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF - 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF + 16 * ln(omz) * pow(NC, -1) * x * CF - 16 * ln(omz) * pow(NC, -1) * x * z * CF + 4 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * pow(z, -1) * CF - 12 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * CF + 8 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x * z * CF - 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 24 * pow(ln(omz), 2) * pow(NC, -1) * x * CF - 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * pow(z, -1) * CF - 8 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * CF + 4 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x * z * CF - 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * CF + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF - 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * pow(z, -1) * CF + 4 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x * CF + 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * CF - 4 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x * z * CF - 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(z) * pow(NC, -1) * x * CF - 4 * Li2(z) * pow(NC, -1) * x * z * CF;

      res += tmp;
    }
    if (z > x)
    {
      double tmp = 0.0;
      tmp = 2 * NC * x * pow(pi, 2) * CF - 2 * NC * x * z * pow(pi, 2) * CF - 12 * ln(x) * NC * x * z * CF - 4 * ln(x) * ln(-xmz) * NC * x * CF + 4 * ln(x) * ln(-xmz) * NC * x * z * CF - 14 * pow(ln(x), 2) * NC * x * CF + 14 * pow(ln(x), 2) * NC * x * z * CF +
            24 * ln(x) * ln(z) * NC * x * CF - 24 * ln(x) * ln(z) * NC * x * z * CF + 24 * ln(x) * ln(omx) * NC * x * CF - 24 * ln(x) * ln(omx) * NC * x * z * CF + 12 * ln(x) * ln(omz) * NC * x * CF - 12 * ln(x) * ln(omz) * NC * x * z * CF + 8 * ln(z) * NC * x * z * CF +
            4 * ln(z) * ln(-xmz) * NC * x * CF - 4 * ln(z) * ln(-xmz) * NC * x * z * CF - 10 * pow(ln(z), 2) * NC * x * CF + 10 * pow(ln(z), 2) * NC * x * z * CF - 20 * ln(z) * ln(omx) * NC * x * CF + 20 * ln(z) * ln(omx) * NC * x * z * CF - 4 * ln(z) * ln(omz) * NC * x * CF + 4 * ln(z) * ln(omz) * NC * x * z * CF + 8 * ln(omx) * NC * x * z * CF - 8 * pow(ln(omx), 2) * NC * x * CF + 8 * pow(ln(omx), 2) * NC * x * z * CF - 8 * ln(omx) * ln(omz) * NC * x * CF + 8 * ln(omx) * ln(omz) * NC * x * z * CF + 4 * ln(omz) * NC * x * z * CF - 2 * pow(ln(omz), 2) * NC * x * CF + 2 * pow(ln(omz), 2) * NC * x * z * CF + 4 * Li2(pow(omx, -1) * omz) * NC * x * CF - 4 * Li2(pow(omx, -1) * omz) * NC * x * z * CF - 4 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * x * CF + 4 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * NC * x * z * CF + 4 * Li2(z) * NC * x * CF - 4 * Li2(z) * NC * x * z * CF;

      res += tmp;
    }
    if (z < x)
    {
      double tmp = 0.0;
      tmp = 2 * NC * x * pow(pi, 2) * CF - 2 * NC * x * z * pow(pi, 2) * CF - 12 * ln(x) * NC * x * z * CF - 12 * pow(ln(x), 2) * NC * x * CF + 12 * pow(ln(x), 2) * NC * x * z * CF + 20 * ln(x) * ln(z) * NC * x * CF - 20 * ln(x) * ln(z) * NC * x * z * CF + 20 * ln(x) * ln(omx) * NC * x * CF - 20 * ln(x) * ln(omx) * NC * x * z * CF + 16 * ln(x) * ln(omz) * NC * x * CF - 16 * ln(x) * ln(omz) * NC * x * z * CF - 4 * ln(x) * ln(xmz) * NC * x * CF + 4 * ln(x) * ln(xmz) * NC * x * z * CF + 8 * ln(z) * NC * x * z * CF - 8 * pow(ln(z), 2) * NC * x * CF + 8 * pow(ln(z), 2) * NC * x * z * CF - 16 * ln(z) * ln(omx) * NC * x * CF + 16 * ln(z) * ln(omx) * NC * x * z * CF - 8 * ln(z) * ln(omz) * NC * x * CF + 8 * ln(z) * ln(omz) * NC * x * z * CF + 4 * ln(z) * ln(xmz) * NC * x * CF - 4 * ln(z) * ln(xmz) * NC * x * z * CF + 8 * ln(omx) * NC * x * z * CF - 8 * pow(ln(omx), 2) * NC * x * CF + 8 * pow(ln(omx), 2) * NC * x * z * CF - 8 * ln(omx) * ln(omz) * NC * x * CF + 8 * ln(omx) * ln(omz) * NC * x * z * CF + 4 * ln(omz) * NC * x * z * CF - 2 * pow(ln(omz), 2) * NC * x * CF + 2 * pow(ln(omz), 2) * NC * x * z * CF + 4 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * x * CF - 4 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * NC * x * z * CF - 4 * Li2(omx * pow(omz, -1)) * NC * x * CF + 4 * Li2(omx * pow(omz, -1)) * NC * x * z * CF + 4 * Li2(z) * NC * x * CF - 4 * Li2(z) * NC * x * z * CF;

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
      tmp = -pow(NC, -1) * pow(z, -1) * CF - 2 * pow(NC, -1) * CF + 3 * pow(NC, -1) * z * CF + pow(NC, -1) * x * pow(z, -1) * CF + 4 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF - 8. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF +
            17 * pow(NC, -1) * x * CF + 4 * pow(NC, -1) * x * sqrtxz1 * rln2 * CF + 23. / 3. * pow(NC, -1) * x * pow(pi, 2) * CF - 14 * pow(NC, -1) * x * z * CF - 14. / 3. * pow(NC, -1) * x * z * pow(pi, 2) * CF + 4 * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1) - 4 * pow(NC, -1) * pow(x, 2) * CF - 4 * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1) + NC * pow(z, -1) * CF + 10 * NC * CF - 7 * NC * z * CF - 4 * NC * pow(z, 2) * CF + 7 * NC * x * pow(z, -1) * CF - 23 * NC * x * CF + 8 * NC * x * pow(rln2, 2) * CF + 8 * NC * x * sqrtxz1 * rln2 * CF - NC * x * pow(pi, 2) * CF + 6 * NC * x * z * CF + 8 * NC * x * z * pow(rln2, 2) * CF + 14. / 3. * NC * x * z * pow(pi, 2) * CF + 10 * NC * x * pow(z, 2) * CF + 22. / 3. * LMUR * NC * x * CF - 22. / 3. * LMUR * NC * x * z * CF - 4. / 3. * LMUR * NF * x * CF + 4. / 3. * LMUR * NF * x * z * CF + 2 * LMUF * pow(NC, -1) * CF - 2 * LMUF * pow(NC, -1) * z * CF + LMUF * pow(NC, -1) * x * CF - LMUF * pow(NC, -1) * x * z * CF - 2 * LMUF * NC * CF + 2 * LMUF * NC * z * CF - LMUF * NC * x * CF + LMUF * NC * x * z * CF + 2 * LMUA * pow(NC, -1) * x * pow(z, -1) * CF - 4 * LMUA * pow(NC, -1) * x * CF + 2 * LMUA * pow(NC, -1) * x * z * CF - 6 * LMUA * NC * x * pow(z, -1) * CF - 22. / 3. * LMUA * NC * x * CF + 28. / 3. * LMUA * NC * x * z * CF + 4 * LMUA * NC * x * pow(z, 2) * CF + 4. / 3. * LMUA * NF * x * CF - 4. / 3. * LMUA * NF * x * z * CF - 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 4 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * sqrtxz1 * CF - 8 * ln(1 + sqrtxz1 - z) * NC * x * rln2 * CF - 8 * ln(1 + sqrtxz1 - z) * NC * x * sqrtxz1 * CF - 8 * ln(1 + sqrtxz1 - z) * NC * x * z * rln2 * CF;
      tmp += +8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * CF + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * NC * x * z * CF - 8 * ln(1 + sqrtxz1 + z) * NC * x * rln2 * CF - 8 * ln(1 + sqrtxz1 + z) * NC * x * z * rln2 * CF + 2 * ln(x) * pow(NC, -1) * CF - 2 * ln(x) * pow(NC, -1) * z * CF + ln(x) * pow(NC, -1) * x * pow(z, -1) * CF + 2 * ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 7 * ln(x) * pow(NC, -1) * x * CF + 8 * ln(x) * pow(NC, -1) * x * CF * omx + 2 * ln(x) * pow(NC, -1) * x * sqrtxz1 * CF - 16 * ln(x) * pow(NC, -1) * x * z * CF + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1) + 4 * ln(x) * pow(NC, -1) * pow(x, 2) * CF + 4 * ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -2) - 8 * ln(x) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1) - 4 * ln(x) * pow(NC, -1) * pow(x, 4) * CF * pow(omxmz, -2) - 2 * ln(x) * NC * CF + 2 * ln(x) * NC * z * CF - 7 * ln(x) * NC * x * pow(z, -1) * CF - 7 * ln(x) * NC * x * CF + 4 * ln(x) * NC * x * rln2 * CF + 4 * ln(x) * NC * x * sqrtxz1 * CF + 18 * ln(x) * NC * x * z * CF + 4 * ln(x) * NC * x * z * rln2 * CF + 8 * ln(x) * NC * x * pow(z, 2) * CF - 2 * ln(x) * LMUF * pow(NC, -1) * x * CF + 2 * ln(x) * LMUF * pow(NC, -1) * x * z * CF + 2 * ln(x) * LMUF * NC * x * CF - 2 * ln(x) * LMUF * NC * x * z * CF - 4 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * CF - 4 * ln(x) * ln(1 + sqrtxz1 + z) * NC * x * z * CF + 14 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF - 44 * pow(ln(x), 2) * pow(NC, -1) * x * CF + 30 * pow(ln(x), 2) * pow(NC, -1) * x * z * CF + 16 * pow(ln(x), 2) * NC * x * CF -
             16 * pow(ln(x), 2) * NC * x * z * CF - 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF + 40 * ln(x) * ln(z) * pow(NC, -1) * x * CF - 34 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF - 32 * ln(x) * ln(z) * NC * x * CF - 2 * ln(x) * ln(z) * NC * x * z * CF;
      tmp += -20 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF + 56 * ln(x) * ln(omx) * pow(NC, -1) * x * CF - 36 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF - 28 * ln(x) * ln(omx) * NC * x * CF + 28 * ln(x) * ln(omx) * NC * x * z * CF - 20 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + 62 * ln(x) * ln(omz) * pow(NC, -1) * x * CF - 42 * ln(x) * ln(omz) * pow(NC, -1) * x * z * CF - 22 * ln(x) * ln(omz) * NC * x * CF + 22 * ln(x) * ln(omz) * NC * x * z * CF - 4 * ln(z) * pow(NC, -1) * CF - 4 * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF + 2 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF -
             12 * ln(z) * pow(NC, -1) * x * CF + 2 * ln(z) * pow(NC, -1) * x * sqrtxz1 * CF + 18 * ln(z) * pow(NC, -1) * x * z * CF + 8 * ln(z) * NC * CF + 8 * ln(z) * NC * z * CF + 10 * ln(z) * NC * x * pow(z, -1) * CF + 4 * ln(z) * NC * x * CF + 12 * ln(z) * NC * x * rln2 * CF + 4 * ln(z) * NC * x * sqrtxz1 * CF - 28 * ln(z) * NC * x * z * CF + 12 * ln(z) * NC * x * z * rln2 * CF - 4 * ln(z) * NC * x * pow(z, 2) * CF - 2 * ln(z) * LMUA * pow(NC, -1) * x * z * CF - 8 * ln(z) * LMUA * NC * x * CF - 14 * ln(z) * LMUA * NC * x * z * CF - 4 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * CF - 4 * ln(z) * ln(1 + sqrtxz1 - z) * NC * x * z * CF - 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * CF - 8 * ln(z) * ln(1 + sqrtxz1 + z) * NC * x * z * CF + 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF - 10 * pow(ln(z), 2) * pow(NC, -1) * x * CF + 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF + 16 * pow(ln(z), 2) * NC * x * CF + 14 * pow(ln(z), 2) * NC * x * z * CF + 8 * ln(z) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF - 24 * ln(z) * ln(omx) * pow(NC, -1) * x * CF + 18 * ln(z) * ln(omx) * pow(NC, -1) * x * z * CF + 24 * ln(z) * ln(omx) * NC * x * CF - 2 * ln(z) * ln(omx) * NC * x * z * CF + 4 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF - 24 * ln(z) * ln(omz) * pow(NC, -1) * x * CF;
      tmp += +20 * ln(z) * ln(omz) * pow(NC, -1) * x * z * CF + 20 * ln(z) * ln(omz) * NC * x * CF - 20 * ln(z) * ln(omz) * NC * x * z * CF - 2 * ln(omx) * pow(NC, -1) * CF + 2 * ln(omx) * pow(NC, -1) * z * CF - 2 * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF - 7 * ln(omx) * pow(NC, -1) * x * CF + 9 * ln(omx) * pow(NC, -1) * x * z * CF + 2 * ln(omx) * NC * CF - 2 * ln(omx) * NC * z * CF + 6 * ln(omx) * NC * x * pow(z, -1) * CF - ln(omx) * NC * x * CF - 9 * ln(omx) * NC * x * z * CF - 4 * ln(omx) * NC * x * pow(z, 2) * CF + 4 * ln(omx) * LMUF * pow(NC, -1) * x * CF - 4 * ln(omx) * LMUF * pow(NC, -1) * x * z * CF - 4 * ln(omx) * LMUF * NC * x * CF + 4 * ln(omx) * LMUF * NC * x * z * CF + 8 * pow(ln(omx), 2) * pow(NC, -1) * x * pow(z, -1) * CF - 20 * pow(ln(omx), 2) * pow(NC, -1) * x * CF + 12 * pow(ln(omx), 2) * pow(NC, -1) * x * z * CF + 10 * pow(ln(omx), 2) * NC * x * CF - 10 * pow(ln(omx), 2) * NC * x * z * CF + 12 * ln(omx) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF - 36 * ln(omx) * ln(omz) * pow(NC, -1) * x * CF + 24 * ln(omx) * ln(omz) * pow(NC, -1) * x * z * CF + 16 * ln(omx) * ln(omz) * NC * x * CF - 16 * ln(omx) * ln(omz) * NC * x * z * CF - 2 * ln(omz) * pow(NC, -1) * CF + 2 * ln(omz) * pow(NC, -1) * z * CF - 2 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * CF + ln(omz) * pow(NC, -1) * x * CF - 8 * ln(omz) * pow(NC, -1) * x * CF * omx + 9 * ln(omz) * pow(NC, -1) * x * z * CF - 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF * pow(omxmz, -1) - 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * CF - 4 * ln(omz) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -2) + 8 * ln(omz) * pow(NC, -1) * pow(x, 3) * CF * pow(omxmz, -1) + 4 * ln(omz) * pow(NC, -1) * pow(x, 4) * CF * pow(omxmz, -2) + 2 * ln(omz) * NC * CF - 2 * ln(omz) * NC * z * CF + 6 * ln(omz) * NC * x * pow(z, -1) * CF - 5 * ln(omz) * NC * x * CF - ln(omz) * NC * x * z * CF;
      tmp += -4 * ln(omz) * NC * x * pow(z, 2) * CF - 8 * ln(omz) * LMUA * NC * x * CF + 8 * ln(omz) * LMUA * NC * x * z * CF + 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * CF - 24 * pow(ln(omz), 2) * pow(NC, -1) * x * CF + 16 * pow(ln(omz), 2) * pow(NC, -1) * x * z * CF + 6 * pow(ln(omz), 2) * NC * x * CF - 6 * pow(ln(omz), 2) * NC * x * z * CF + 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * NC * x * CF + 4 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * NC * x * z * CF - 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * NC * x * CF - 4 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * NC * x * z * CF - 4 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * NC * x * CF - 4 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * NC * x * z * CF + 4 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * NC * x * CF + 4 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * NC * x * z * CF + 4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * CF - 4 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x * z * CF - 4 * Li2(1 - x * pow(z, -1)) * NC * x * CF + 4 * Li2(1 - x * pow(z, -1)) * NC * x * z * CF - 2 * Li2(x) * pow(NC, -1) * x * CF + 2 * Li2(x) * pow(NC, -1) * x * z * CF - 2 * Li2(x) * NC * x * CF + 2 * Li2(x) * NC * x * z * CF - 4 * Li2(z) * pow(NC, -1) * x * pow(z, -1) * CF + 4 * Li2(z) * pow(NC, -1) * x * CF - 2 * Li2(z) * pow(NC, -1) * x * z * CF - 22 * Li2(z) * NC * x * z * CF;

      res += tmp;
    }
    return res;
  }
}