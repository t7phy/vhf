double C2Lq2qpEq(double inx, double inz, std::string cx, std::string cz,
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
      tmp = -4 * CF + 2 * z * CF + 2 * pow(z, 2) * CF + 7 * x * CF - 1. / 3. * x * pow(pi, 2) * CF - 2. / 3. * x * z * pow(pi, 2) * CF - 7 * x * pow(z, 2) * CF + 4 * LMUA * x * CF - 2 * LMUA * x * z * CF - 2 * LMUA * x * pow(z, 2) * CF + 8 * ln(x) * x * CF - 4 * ln(x) * x * z * CF - 4 * ln(x) * x * pow(z, 2) * CF + 4 * ln(x) * ln(z) * x * CF + 8 * ln(x) * ln(z) * x * z * CF - 2 * ln(z) * CF - 4 * ln(z) * z * CF - 2 * ln(z) * x * CF + 8 * ln(z) * x * z * CF + 2 * ln(z) * x * pow(z, 2) * CF + 2 * ln(z) * LMUA * x * CF + 4 * ln(z) * LMUA * x * z * CF - 2 * pow(ln(z), 2) * x * CF - 4 * pow(ln(z), 2) * x * z * CF - 2 * ln(z) * ln(omx) * x * CF - 4 * ln(z) * ln(omx) * x * z * CF - 4 * ln(omx) * x * CF + 2 * ln(omx) * x * z * CF + 2 * ln(omx) * x * pow(z, 2) * CF - 4 * ln(omz) * x * CF + 2 * ln(omz) * x * z * CF + 2 * ln(omz) * x * pow(z, 2) * CF + 2 * Li2(z) * x * CF + 4 * Li2(z) * x * z * CF;

      res += tmp;
    }
    return res;
  }
}