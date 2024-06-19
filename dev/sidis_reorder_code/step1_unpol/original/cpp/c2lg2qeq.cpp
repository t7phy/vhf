double C2Lg2qEq(double inx, double inz, std::string cx, std::string cz,
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
      tmp = 2 * pow(NC, -1) * x * pow(z, -1) + 2 * pow(NC, -1) * x * pow(omz, -1) - 7. / 3. * pow(NC, -1) * x * pow(pi, 2) - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 7. / 3. * pow(NC, -1) * pow(x, 2) * pow(pi, 2) - 4 * NC * x + 2. / 3. * NC * x * pow(pi, 2) + 4 * NC * pow(x, 2) - 2. / 3. * NC * pow(x, 2) * pow(pi, 2) + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1) + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - 12 * ln(x) * NC * x + 12 * ln(x) * NC * pow(x, 2) + 13 * pow(ln(x), 2) * pow(NC, -1) * x - 13 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) - 12 * pow(ln(x), 2) * NC * x + 12 * pow(ln(x), 2) * NC * pow(x, 2) - 16 * ln(x) * ln(z) * pow(NC, -1) * x + 16 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) + 20 * ln(x) * ln(z) * NC * x - 20 * ln(x) * ln(z) * NC * pow(x, 2) - 22 * ln(x) * ln(omx) * pow(NC, -1) * x + 22 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) + 16 * ln(x) * ln(omx) * NC * x - 16 * ln(x) * ln(omx) * NC * pow(x, 2) - 20 * ln(x) * ln(omz) * pow(NC, -1) * x + 20 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) + 20 * ln(x) * ln(omz) * NC * x -
            20 * ln(x) * ln(omz) * NC * pow(x, 2) + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x - 2 * ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(xmz) * NC * x + 4 * ln(x) * ln(xmz) * NC * pow(x, 2) + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x -
            2 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(omxmz) * NC * x + 4 * ln(x) * ln(omxmz) * NC * pow(x, 2) - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1) + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(z) * NC * x - 8 * ln(z) * NC * pow(x, 2);
      tmp += +5 * pow(ln(z), 2) * pow(NC, -1) * x - 5 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) - 8 * pow(ln(z), 2) * NC * x + 8 * pow(ln(z), 2) * NC * pow(x, 2) + 12 * ln(z) * ln(omx) * pow(NC, -1) * x - 12 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) - 8 * ln(z) * ln(omx) * NC * x + 8 * ln(z) * ln(omx) * NC * pow(x, 2) + 8 * ln(z) * ln(omz) * pow(NC, -1) * x - 8 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) - 16 * ln(z) * ln(omz) * NC * x + 16 * ln(z) * ln(omz) * NC * pow(x, 2) - 2 * ln(z) * ln(xmz) * pow(NC, -1) * x + 2 * ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2) + 4 * ln(z) * ln(xmz) * NC * x - 4 * ln(z) * ln(xmz) * NC * pow(x, 2) - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 4 * ln(omx) * NC * x - 4 * ln(omx) * NC * pow(x, 2) + 8 * pow(ln(omx), 2) * pow(NC, -1) * x - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) - 2 * pow(ln(omx), 2) * NC * x + 2 * pow(ln(omx), 2) * NC * pow(x, 2) +
             14 * ln(omx) * ln(omz) * pow(NC, -1) * x - 14 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) - 12 * ln(omx) * ln(omz) * NC * x + 12 * ln(omx) * ln(omz) * NC * pow(x, 2) - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1) - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(omz) * NC * x - 8 * ln(omz) * NC * pow(x, 2) + 6 * pow(ln(omz), 2) * pow(NC, -1) * x - 6 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) - 6 * pow(ln(omz), 2) * NC * x + 6 * pow(ln(omz), 2) * NC * pow(x, 2) -
             2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2) + 4 * ln(omz) * ln(omxmz) * NC * x;
      tmp += -4 * ln(omz) * ln(omxmz) * NC * pow(x, 2) + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x - 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2) - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x +
             2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) + 4 * Li2(omx * pow(omz, -1)) * NC * x - 4 * Li2(omx * pow(omz, -1)) * NC * pow(x, 2) - 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2) - 4 * Li2(z * pow(omx, -1)) * NC * x + 4 * Li2(z * pow(omx, -1)) * NC * pow(x, 2) + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2);

      res += tmp;
    }
    if (z > 1. - x && z < x)
    {
      double tmp = 0.0;
      tmp = 2 * pow(NC, -1) * x * pow(z, -1) + 2 * pow(NC, -1) * x * pow(omz, -1) - 7. / 3. * pow(NC, -1) * x * pow(pi, 2) - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 7. / 3. * pow(NC, -1) * pow(x, 2) * pow(pi, 2) - 4 * NC * x + 2. / 3. * NC * x * pow(pi, 2) + 4 * NC * pow(x, 2) - 2. / 3. * NC * pow(x, 2) * pow(pi, 2) + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1) + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - 12 * ln(x) * NC * x + 12 * ln(x) * NC * pow(x, 2) + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(-omxmz) * NC * x + 4 * ln(x) * ln(-omxmz) * NC * pow(x, 2) + 12 * pow(ln(x), 2) * pow(NC, -1) * x - 12 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) - 14 * pow(ln(x), 2) * NC * x + 14 * pow(ln(x), 2) * NC * pow(x, 2) - 18 * ln(x) * ln(z) * pow(NC, -1) * x + 18 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) + 24 * ln(x) * ln(z) * NC * x - 24 * ln(x) * ln(z) * NC * pow(x, 2) - 20 * ln(x) * ln(omx) * pow(NC, -1) * x + 20 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) + 12 * ln(x) * ln(omx) * NC * x - 12 * ln(x) * ln(omx) * NC * pow(x, 2) - 18 * ln(x) * ln(omz) * pow(NC, -1) * x + 18 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) + 24 * ln(x) * ln(omz) * NC * x - 24 * ln(x) * ln(omz) * NC * pow(x, 2) + 2 * ln(x) * ln(xmz) * pow(NC, -1) * x - 2 * ln(x) * ln(xmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(xmz) * NC * x + 4 * ln(x) * ln(xmz) * NC * pow(x, 2) - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1) + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(z) * NC * x - 8 * ln(z) * NC * pow(x, 2);
      tmp += +5 * pow(ln(z), 2) * pow(NC, -1) * x - 5 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) - 8 * pow(ln(z), 2) * NC * x + 8 * pow(ln(z), 2) * NC * pow(x, 2) + 12 * ln(z) * ln(omx) * pow(NC, -1) * x - 12 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) - 8 * ln(z) * ln(omx) * NC * x + 8 * ln(z) * ln(omx) * NC * pow(x, 2) + 10 * ln(z) * ln(omz) * pow(NC, -1) * x - 10 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) - 20 * ln(z) * ln(omz) * NC * x + 20 * ln(z) * ln(omz) * NC * pow(x, 2) - 2 * ln(z) * ln(xmz) * pow(NC, -1) * x + 2 * ln(z) * ln(xmz) * pow(NC, -1) * pow(x, 2) + 4 * ln(z) * ln(xmz) * NC * x - 4 * ln(z) * ln(xmz) * NC * pow(x, 2) - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 4 * ln(omx) * NC * x - 4 * ln(omx) * NC * pow(x, 2) + 8 * pow(ln(omx), 2) * pow(NC, -1) * x - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) - 2 * pow(ln(omx), 2) * NC * x + 2 * pow(ln(omx), 2) * NC * pow(x, 2) +
             12 * ln(omx) * ln(omz) * pow(NC, -1) * x - 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) - 8 * ln(omx) * ln(omz) * NC * x + 8 * ln(omx) * ln(omz) * NC * pow(x, 2) - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1) - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(omz) * NC * x - 8 * ln(omz) * NC * pow(x, 2) - 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) + 4 * ln(omz) * ln(-omxmz) * NC * x - 4 * ln(omz) * ln(-omxmz) * NC * pow(x, 2) + 5 * pow(ln(omz), 2) * pow(NC, -1) * x - 5 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) - 8 * pow(ln(omz), 2) * NC * x;
      tmp += +8 * pow(ln(omz), 2) * NC * pow(x, 2) - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2) - 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * x + 2 * Li2(pow(x, -1) * z * omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2) + 4 * Li2(pow(z, -1) * omx) * NC * x - 4 * Li2(pow(z, -1) * omx) * NC * pow(x, 2) + 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * x - 2 * Li2(omx * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) + 4 * Li2(omx * pow(omz, -1)) * NC * x - 4 * Li2(omx * pow(omz, -1)) * NC * pow(x, 2) - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2);

      res += tmp;
    }
    if (z < 1. - x && z > x)
    {
      double tmp = 0.0;
      tmp = 2 * pow(NC, -1) * x * pow(z, -1) + 2 * pow(NC, -1) * x * pow(omz, -1) - 7. / 3. * pow(NC, -1) * x * pow(pi, 2) - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 7. / 3. * pow(NC, -1) * pow(x, 2) * pow(pi, 2) - 4 * NC * x + 10. / 3. * NC * x * pow(pi, 2) + 4 * NC * pow(x, 2) - 10. / 3. * NC * pow(x, 2) * pow(pi, 2) +
            6 * ln(x) * pow(NC, -1) * x * pow(z, -1) + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - 12 * ln(x) * NC * x + 12 * ln(x) * NC * pow(x, 2) + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x - 2 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(-xmz) * NC * x + 4 * ln(x) * ln(-xmz) * NC * pow(x, 2) + 14 * pow(ln(x), 2) * pow(NC, -1) * x - 14 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) - 14 * pow(ln(x), 2) * NC * x + 14 * pow(ln(x), 2) * NC * pow(x, 2) - 18 * ln(x) * ln(z) * pow(NC, -1) * x + 18 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) + 24 * ln(x) * ln(z) * NC * x - 24 * ln(x) * ln(z) * NC * pow(x, 2) - 24 * ln(x) * ln(omx) * pow(NC, -1) * x + 24 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) + 12 * ln(x) * ln(omx) * NC * x - 12 * ln(x) * ln(omx) * NC * pow(x, 2) - 18 * ln(x) * ln(omz) * pow(NC, -1) * x + 18 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) + 24 * ln(x) * ln(omz) * NC * x - 24 * ln(x) * ln(omz) * NC * pow(x, 2) + 2 * ln(x) * ln(omxmz) * pow(NC, -1) * x - 2 * ln(x) * ln(omxmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(omxmz) * NC * x + 4 * ln(x) * ln(omxmz) * NC * pow(x, 2) - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1) + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(z) * NC * x;
      tmp += -8 * ln(z) * NC * pow(x, 2) - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x + 2 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2) + 4 * ln(z) * ln(-xmz) * NC * x - 4 * ln(z) * ln(-xmz) * NC * pow(x, 2) + 6 * pow(ln(z), 2) * pow(NC, -1) * x - 6 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) - 10 * pow(ln(z), 2) * NC * x + 10 * pow(ln(z), 2) * NC * pow(x, 2) + 14 * ln(z) * ln(omx) * pow(NC, -1) * x - 14 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) - 4 * ln(z) * ln(omx) * NC * x + 4 * ln(z) * ln(omx) * NC * pow(x, 2) + 6 * ln(z) * ln(omz) * pow(NC, -1) * x - 6 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) - 20 * ln(z) * ln(omz) * NC * x + 20 * ln(z) * ln(omz) * NC * pow(x, 2) - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 4 * ln(omx) * NC * x - 4 * ln(omx) * NC * pow(x, 2) +
             8 * pow(ln(omx), 2) * pow(NC, -1) * x - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) - 6 * pow(ln(omx), 2) * NC * x + 6 * pow(ln(omx), 2) * NC * pow(x, 2) + 14 * ln(omx) * ln(omz) * pow(NC, -1) * x - 14 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) - 4 * ln(omx) * ln(omz) * NC * x + 4 * ln(omx) * ln(omz) * NC * pow(x, 2) - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1) - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(omz) * NC * x - 8 * ln(omz) * NC * pow(x, 2) +
             6 * pow(ln(omz), 2) * pow(NC, -1) * x - 6 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) - 10 * pow(ln(omz), 2) * NC * x + 10 * pow(ln(omz), 2) * NC * pow(x, 2) - 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * x + 2 * ln(omz) * ln(omxmz) * pow(NC, -1) * pow(x, 2);
      tmp += +4 * ln(omz) * ln(omxmz) * NC * x - 4 * ln(omz) * ln(omxmz) * NC * pow(x, 2) - 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) - 4 * Li2(pow(omx, -1) * omz) * NC * x + 4 * Li2(pow(omx, -1) * omz) * NC * pow(x, 2) - 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * x + 2 * Li2(z * pow(omx, -1)) * pow(NC, -1) * pow(x, 2) - 4 * Li2(z * pow(omx, -1)) * NC * x + 4 * Li2(z * pow(omx, -1)) * NC * pow(x, 2) + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) - 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * x + 4 * Li2(x * pow(z, -1) * omx * pow(omz, -1)) * NC * pow(x, 2) + 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * x - 2 * Li2(x * z * pow(omx, -1) * pow(omz, -1)) * pow(NC, -1) * pow(x, 2);

      res += tmp;
    }
    if (z > 1. - x && z > x)
    {
      double tmp = 0.0;
      tmp = 2 * pow(NC, -1) * x * pow(z, -1) + 2 * pow(NC, -1) * x * pow(omz, -1) - 7. / 3. * pow(NC, -1) * x * pow(pi, 2) - 2 * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 7. / 3. * pow(NC, -1) * pow(x, 2) * pow(pi, 2) - 4 * NC * x + 2. / 3. * NC * x * pow(pi, 2) + 4 * NC * pow(x, 2) - 2. / 3. * NC * pow(x, 2) * pow(pi, 2) + 6 * ln(x) * pow(NC, -1) * x * pow(z, -1) + 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - 12 * ln(x) * NC * x + 12 * ln(x) * NC * pow(x, 2) + 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * x - 2 * ln(x) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(-omxmz) * NC * x + 4 * ln(x) * ln(-omxmz) * NC * pow(x, 2) + 2 * ln(x) * ln(-xmz) * pow(NC, -1) * x - 2 * ln(x) * ln(-xmz) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(-xmz) * NC * x + 4 * ln(x) * ln(-xmz) * NC * pow(x, 2) +
            13 * pow(ln(x), 2) * pow(NC, -1) * x - 13 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) - 12 * pow(ln(x), 2) * NC * x +
            12 * pow(ln(x), 2) * NC * pow(x, 2) - 20 * ln(x) * ln(z) * pow(NC, -1) * x + 20 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) + 20 * ln(x) * ln(z) * NC * x - 20 * ln(x) * ln(z) * NC * pow(x, 2) - 22 * ln(x) * ln(omx) * pow(NC, -1) * x + 22 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) + 16 * ln(x) * ln(omx) * NC * x - 16 * ln(x) * ln(omx) * NC * pow(x, 2) - 16 * ln(x) * ln(omz) * pow(NC, -1) * x + 16 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) + 20 * ln(x) * ln(omz) * NC * x -
            20 * ln(x) * ln(omz) * NC * pow(x, 2) - 2 * ln(z) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1) + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(z) * NC * x;
      tmp += -8 * ln(z) * NC * pow(x, 2) - 2 * ln(z) * ln(-xmz) * pow(NC, -1) * x + 2 * ln(z) * ln(-xmz) * pow(NC, -1) * pow(x, 2) + 4 * ln(z) * ln(-xmz) * NC * x - 4 * ln(z) * ln(-xmz) * NC * pow(x, 2) + 6 * pow(ln(z), 2) * pow(NC, -1) * x - 6 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) - 6 * pow(ln(z), 2) * NC * x + 6 * pow(ln(z), 2) * NC * pow(x, 2) + 14 * ln(z) * ln(omx) * pow(NC, -1) * x - 14 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) - 12 * ln(z) * ln(omx) * NC * x + 12 * ln(z) * ln(omx) * NC * pow(x, 2) + 8 * ln(z) * ln(omz) * pow(NC, -1) * x - 8 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) - 16 * ln(z) * ln(omz) * NC * x + 16 * ln(z) * ln(omz) * NC * pow(x, 2) - 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1) - 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 4 * ln(omx) * NC * x - 4 * ln(omx) * NC * pow(x, 2) +
             8 * pow(ln(omx), 2) * pow(NC, -1) * x - 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) - 2 * pow(ln(omx), 2) * NC * x + 2 * pow(ln(omx), 2) * NC * pow(x, 2) + 12 * ln(omx) * ln(omz) * pow(NC, -1) * x - 12 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) - 8 * ln(omx) * ln(omz) * NC * x + 8 * ln(omx) * ln(omz) * NC * pow(x, 2) - 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1) - 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1) + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 8 * ln(omz) * NC * x - 8 * ln(omz) * NC * pow(x, 2) -
             2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * x + 2 * ln(omz) * ln(-omxmz) * pow(NC, -1) * pow(x, 2) + 4 * ln(omz) * ln(-omxmz) * NC * x - 4 * ln(omz) * ln(-omxmz) * NC * pow(x, 2) + 5 * pow(ln(omz), 2) * pow(NC, -1) * x - 5 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2);
      tmp += -8 * pow(ln(omz), 2) * NC * x + 8 * pow(ln(omz), 2) * NC * pow(x, 2) - 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * x + 2 * Li2(pow(x, -1) * pow(z, -1) * omx * omz) * pow(NC, -1) * pow(x, 2) + 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * x - 4 * Li2(pow(x, -1) * z * pow(omx, -1) * omz) * NC * pow(x, 2) + 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * x - 2 * Li2(pow(z, -1) * omx) * pow(NC, -1) * pow(x, 2) + 4 * Li2(pow(z, -1) * omx) * NC * x - 4 * Li2(pow(z, -1) * omx) * NC * pow(x, 2) - 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * x + 2 * Li2(pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2) - 4 * Li2(pow(omx, -1) * omz) * NC * x + 4 * Li2(pow(omx, -1) * omz) * NC * pow(x, 2) + 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * x - 2 * Li2(x * pow(z, -1) * pow(omx, -1) * omz) * pow(NC, -1) * pow(x, 2);

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
      tmp = 1. / 8. * pow(NC, -1) * pow(x, -1) * pow(poly2, -1) - 1. / 8. * pow(NC, -1) * pow(x, -1) - 1. / 2. * pow(NC, -1) * pow(z, -1) - 1. / 8. * pow(NC, -1) * pow(poly2, -1) + 3. / 8. * pow(NC, -1) - 1. / 2. * pow(NC, -1) * z - 5. / 2. * pow(NC, -1) * x * pow(z, -1) - 1. / 4. * pow(NC, -1) * x * pow(poly2, -1) - 2 * pow(NC, -1) * x * pow(omz, -1) + pow(NC, -1) * x * pow(omxmz, -1) + 37. / 8. * pow(NC, -1) * x + 3 * pow(NC, -1) * x * pow(pi, 2) + 17. / 2. * pow(NC, -1) * x * z - pow(NC, -1) * x * z * pow(pi, 2) + 3 * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 1. / 4. * pow(NC, -1) * pow(x, 2) * pow(poly2, -1) + 2 * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - 2 * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1) - 39. / 8. * pow(NC, -1) * pow(x, 2) - 7. / 3. * pow(NC, -1) * pow(x, 2) * pow(pi, 2) - 8 * pow(NC, -1) * pow(x, 2) * z + 1. / 8. * pow(NC, -1) * pow(x, 3) * pow(poly2, -1) + pow(NC, -1) * pow(x, 3) * pow(omxmz, -1) - 1. / 8. * pow(NC, -1) * pow(x, 4) * pow(poly2, -1) - 1. / 8. * NC * pow(x, -1) * pow(poly2, -1) + 169. / 72. * NC * pow(x, -1) + 1. / 2. * NC * pow(z, -1) + 1. / 8. * NC * pow(poly2, -1) - 409. / 24. * NC + 41. / 2. * NC * z + 1. / 2. * NC * x * pow(z, -1) + 1. / 4. * NC * x * pow(poly2, -1) - NC * x * pow(omxmz, -1) - 95. / 24. * NC * x - 17. / 3. * NC * x * pow(pi, 2) - 57. / 2. * NC * x * z + NC * x * z * pow(pi, 2) - NC * pow(x, 2) * pow(z, -1) - 1. / 4. * NC * pow(x, 2) * pow(poly2, -1) + 2 * NC * pow(x, 2) * pow(omxmz, -1) + 1343. / 72. * NC * pow(x, 2) + 3 * NC * pow(x, 2) * pow(pi, 2) + 8 * NC * pow(x, 2) * z - 1. / 8. * NC * pow(x, 3) * pow(poly2, -1) - NC * pow(x, 3) * pow(omxmz, -1) + 1. / 8. * NC * pow(x, 4) * pow(poly2, -1) + 22. / 3. * LMUR * NC * x - 22. / 3. * LMUR * NC * pow(x, 2) - 4. / 3. * LMUR * NF * x + 4. / 3. * LMUR * NF * pow(x, 2) + LMUF * pow(NC, -1) * z;
      tmp += +LMUF * pow(NC, -1) * x * z - 2 * LMUF * pow(NC, -1) * pow(x, 2) * z - 4. / 3. * LMUF * NC * pow(x, -1) + 4 * LMUF * NC - LMUF * NC * z + 38. / 3. * LMUF * NC * x - LMUF * NC * x * z - 46. / 3. * LMUF * NC * pow(x, 2) + 2 * LMUF * NC * pow(x, 2) * z + 4. / 3. * LMUF * NF * x - 4. / 3. * LMUF * NF * pow(x, 2) + LMUA * pow(NC, -1) * x + 2 * LMUA * pow(NC, -1) * x * z - LMUA * pow(NC, -1) * pow(x, 2) - 2 * LMUA * pow(NC, -1) * pow(x, 2) * z - LMUA * NC * x - 2 * LMUA * NC * x * z +
             LMUA * NC * pow(x, 2) + 2 * LMUA * NC * pow(x, 2) * z + 3. / 16. * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2) - 3. / 16. * ln(x) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1) - 3. / 16. * ln(x) * pow(NC, -1) * pow(poly2, -2) + 1. / 16. * ln(x) * pow(NC, -1) * pow(poly2, -1) + 1. / 2. * ln(x) * pow(NC, -1) + 1. / 4. * ln(x) * pow(NC, -1) * z - 7 * ln(x) * pow(NC, -1) * x * pow(z, -1) - 9. / 16. * ln(x) * pow(NC, -1) * x * pow(poly2, -2) - 3. / 8. * ln(x) * pow(NC, -1) * x * pow(poly2, -1) - 6 * ln(x) * pow(NC, -1) * x * pow(omz, -1) - ln(x) * pow(NC, -1) * x * pow(omxmz, -1) + ln(x) * pow(NC, -1) * x + 17. / 4. * ln(x) * pow(NC, -1) * x * z + ln(x) * pow(NC, -1) * x * pow(z, 3) * pow(xmz, -2) + 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(z, -1) + 9. / 16. * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2) + 5. / 8. * ln(x) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1) + 6 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - 2 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(xmz, -1) + ln(x) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -2) + ln(x) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1) - 7. / 2. * ln(x) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * pow(NC, -1) * pow(x, 2) * z + 9. / 16. * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2) + 9. / 16. * ln(x) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1) + 5 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(xmz, -1);
      tmp += -2 * ln(x) * pow(NC, -1) * pow(x, 3) * pow(omxmz, -2) - 9. / 16. * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2) - 11. / 16. * ln(x) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1) - ln(x) * pow(NC, -1) * pow(x, 4) * pow(xmz, -2) + ln(x) * pow(NC, -1) * pow(x, 4) * pow(omxmz, -2) - 3. / 16. * ln(x) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2) + 3. / 16. * ln(x) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2) - 3. / 16. * ln(x) * NC * pow(x, -1) * pow(poly2, -2) - 5. / 16. * ln(x) * NC * pow(x, -1) * pow(poly2, -1) + 1. / 2. * ln(x) * NC * pow(x, -1) + 3. / 16. * ln(x) * NC * pow(poly2, -2) + 7. / 16. * ln(x) * NC * pow(poly2, -1) - 2 * ln(x) * NC + 39. / 4. * ln(x) * NC * z + ln(x) * NC * x * pow(z, -1) + 9. / 16. * ln(x) * NC * x * pow(poly2, -2) + 3. / 8. * ln(x) * NC * x * pow(poly2, -1) + ln(x) * NC * x * pow(omxmz, -1) + 19. / 2. * ln(x) * NC * x + 23. / 4. * ln(x) * NC * x * z - ln(x) * NC * x * pow(z, 3) * pow(xmz, -2) - 9. / 16. * ln(x) * NC * pow(x, 2) * pow(poly2, -2) - 5. / 8. * ln(x) * NC * pow(x, 2) * pow(poly2, -1) - ln(x) * NC * pow(x, 2) * pow(omxmz, -2) - 3 * ln(x) * NC * pow(x, 2) * pow(omxmz, -1) - 64 * ln(x) * NC * pow(x, 2) + 4 * ln(x) * NC * pow(x, 2) * z - 9. / 16. * ln(x) * NC * pow(x, 3) * pow(poly2, -2) - 1. / 16. * ln(x) * NC * pow(x, 3) * pow(poly2, -1) - 3 * ln(x) * NC * pow(x, 3) * pow(xmz, -1) + 2 * ln(x) * NC * pow(x, 3) * pow(omxmz, -2) + 2 * ln(x) * NC * pow(x, 3) * pow(omxmz, -1) + 9. / 16. * ln(x) * NC * pow(x, 4) * pow(poly2, -2) + 3. / 16. * ln(x) * NC * pow(x, 4) * pow(poly2, -1) + ln(x) * NC * pow(x, 4) * pow(xmz, -2) - ln(x) * NC * pow(x, 4) * pow(omxmz, -2) + 3. / 16. * ln(x) * NC * pow(x, 5) * pow(poly2, -2) - 3. / 16. * ln(x) * NC * pow(x, 6) * pow(poly2, -2) + 2 * ln(x) * LMUF * pow(NC, -1) * x * z;
      tmp += +16 * ln(x) * LMUF * NC * x - 2 * ln(x) * LMUF * NC * x * z + 3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) + 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) - 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1) - 3. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1) + 31. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) -
             11. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) + 11. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) + 29. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) - 29. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) + 9. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) + 5. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) + 73. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) - 3. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2);
      tmp += -3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) - 5. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) + 5. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * NC * z * pow(sqrtxz2, -1) + 3. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1) - 151. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) + 51. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * z * pow(sqrtxz2, -1) - 51. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1) - 129. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1) + 129. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1) - 9. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) - 193. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) +
             3. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1);
      tmp += -1. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) - 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) + 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * z * pow(sqrtxz2, -1) + 3. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1) - 31. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(sqrtxz2, -1) + 11. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) - 11. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) - 29. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) + 29. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) - 9. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) - 5. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) - 73. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) + 3. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) -
             7. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, -1) * pow(sqrtxz2, -1);
      tmp += +5. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) - 5. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * NC * z * pow(sqrtxz2, -1) - 3. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1) + 151. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(sqrtxz2, -1) - 51. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * z * pow(sqrtxz2, -1) + 51. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1) + 129. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * pow(sqrtxz2, -1) - 129. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1) + 9. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) + 193. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 3) * pow(sqrtxz2, -1) - 3. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) + 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * x * z + 4 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(x, 2) - 4 * ln(x) * ln(1 + x) * pow(NC, -1) * pow(x, 2) * z + 4 * ln(x) * ln(1 + x) * NC * x * z + 4 * ln(x) * ln(1 + x) * NC * pow(x, 2) * z - 15 * pow(ln(x), 2) * pow(NC, -1) * x + pow(ln(x), 2) * pow(NC, -1) * x * z + 13 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * z + 29 * pow(ln(x), 2) * NC * x;
      tmp += -pow(ln(x), 2) * NC * x * z - 13 * pow(ln(x), 2) * NC * pow(x, 2) - 3 * pow(ln(x), 2) * NC * pow(x, 2) * z +
             10 * ln(x) * ln(z) * pow(NC, -1) * x + 2 * ln(x) * ln(z) * pow(NC, -1) * x * z - 14 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) - 22 * ln(x) * ln(z) * NC * x - 2 * ln(x) * ln(z) * NC * x * z + 18 * ln(x) * ln(z) * NC * pow(x, 2) + 22 * ln(x) * ln(omx) * pow(NC, -1) * x + 2 * ln(x) * ln(omx) * pow(NC, -1) * x * z - 22 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) - 2 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, 2) * z - 18 * ln(x) * ln(omx) * NC * x - 2 * ln(x) * ln(omx) * NC * x * z + 18 * ln(x) * ln(omx) * NC * pow(x, 2) + 2 * ln(x) * ln(omx) * NC * pow(x, 2) * z + 20 * ln(x) * ln(omz) * pow(NC, -1) * x - 2 * ln(x) * ln(omz) * pow(NC, -1) * x * z - 20 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) - 40 * ln(x) * ln(omz) * NC * x + 2 * ln(x) * ln(omz) * NC * x * z + 24 * ln(x) * ln(omz) * NC * pow(x, 2) + 3. / 16. * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -2) - 3. / 16. * ln(z) * pow(NC, -1) * pow(x, -1) * pow(poly2, -1) + 3. / 16. * ln(z) * pow(NC, -1) * pow(poly2, -2) - 1. / 16. * ln(z) * pow(NC, -1) * pow(poly2, -1) + 1. / 4. * ln(z) * pow(NC, -1) - 7. / 4. * ln(z) * pow(NC, -1) * z + 2 * ln(z) * pow(NC, -1) * x * pow(z, -1) - 9. / 16. * ln(z) * pow(NC, -1) * x * pow(poly2, -2) - 3. / 8. * ln(z) * pow(NC, -1) * x * pow(poly2, -1) + 4 * ln(z) * pow(NC, -1) * x * pow(omz, -1) - 15. / 4. * ln(z) * pow(NC, -1) * x + 11. / 4. * ln(z) * pow(NC, -1) * x * z - ln(z) * pow(NC, -1) * x * pow(z, 3) * pow(xmz, -2) - 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 9. / 16. * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -2) - 5. / 8. * ln(z) * pow(NC, -1) * pow(x, 2) * pow(poly2, -1) - 4 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) + 2 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(xmz, -1);
      tmp += +11. / 2. * ln(z) * pow(NC, -1) * pow(x, 2) + 9. / 16. * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -2) + 9. / 16. * ln(z) * pow(NC, -1) * pow(x, 3) * pow(poly2, -1) - 5 * ln(z) * pow(NC, -1) * pow(x, 3) * pow(xmz, -1) + 9. / 16. * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -2) + 11. / 16. * ln(z) * pow(NC, -1) * pow(x, 4) * pow(poly2, -1) + ln(z) * pow(NC, -1) * pow(x, 4) * pow(xmz, -2) - 3. / 16. * ln(z) * pow(NC, -1) * pow(x, 5) * pow(poly2, -2) - 3. / 16. * ln(z) * pow(NC, -1) * pow(x, 6) * pow(poly2, -2) - 3. / 16. * ln(z) * NC * pow(x, -1) * pow(poly2, -2) - 5. / 16. * ln(z) * NC * pow(x, -1) * pow(poly2, -1) + 11. / 6. * ln(z) * NC * pow(x, -1) - 3. / 16. * ln(z) * NC * pow(poly2, -2) - 7. / 16. * ln(z) * NC * pow(poly2, -1) - 27. / 4. * ln(z) * NC + 47. / 4. * ln(z) * NC * z + 9. / 16. * ln(z) * NC * x * pow(poly2, -2) + 3. / 8. * ln(z) * NC * x * pow(poly2, -1) - 95. / 4. * ln(z) * NC * x - 51. / 4. * ln(z) * NC * x * z + ln(z) * NC * x * pow(z, 3) * pow(xmz, -2) + 9. / 16. * ln(z) * NC * pow(x, 2) * pow(poly2, -2) + 5. / 8. * ln(z) * NC * pow(x, 2) * pow(poly2, -1) + 80. / 3. * ln(z) * NC * pow(x, 2) - 9. / 16. * ln(z) * NC * pow(x, 3) * pow(poly2, -2) - 1. / 16. * ln(z) * NC * pow(x, 3) * pow(poly2, -1) + 3 * ln(z) * NC * pow(x, 3) * pow(xmz, -1) - 9. / 16. * ln(z) * NC * pow(x, 4) * pow(poly2, -2) - 3. / 16. * ln(z) * NC * pow(x, 4) * pow(poly2, -1) - ln(z) * NC * pow(x, 4) * pow(xmz, -2) + 3. / 16. * ln(z) * NC * pow(x, 5) * pow(poly2, -2) + 3. / 16. * ln(z) * NC * pow(x, 6) * pow(poly2, -2) - 2 * ln(z) * LMUA * pow(NC, -1) * x + 2 * ln(z) * LMUA * pow(NC, -1) * pow(x, 2) + 2 * ln(z) * LMUA * NC * x - 2 * ln(z) * LMUA * NC * pow(x, 2) - 2 * pow(ln(z), 2) * pow(NC, -1) * x + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2);
      tmp += +3 * pow(ln(z), 2) * NC * x - 3 * pow(ln(z), 2) * NC * pow(x, 2) - 8 * ln(z) * ln(omx) * pow(NC, -1) * x + 8 * ln(z) * ln(omx) * pow(NC, -1) * pow(x, 2) + 10 * ln(z) * ln(omx) * NC * x - 10 * ln(z) * ln(omx) * NC * pow(x, 2) -
             14 * ln(z) * ln(omz) * pow(NC, -1) * x + 14 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) + 22 * ln(z) * ln(omz) * NC * x - 22 * ln(z) * ln(omz) * NC * pow(x, 2) - ln(omx) * pow(NC, -1) * z + 4 * ln(omx) * pow(NC, -1) * x * pow(z, -1) + 4 * ln(omx) * pow(NC, -1) * x * pow(omz, -1) + ln(omx) * pow(NC, -1) * x - 3 * ln(omx) * pow(NC, -1) * x * z - 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - ln(omx) * pow(NC, -1) * pow(x, 2) + 4 * ln(omx) * pow(NC, -1) * pow(x, 2) * z + 4. / 3. * ln(omx) * NC * pow(x, -1) - 4 * ln(omx) * NC + ln(omx) * NC * z - 29 * ln(omx) * NC * x + 3 * ln(omx) * NC * x * z + 95. / 3. * ln(omx) * NC * pow(x, 2) - 4 * ln(omx) * NC * pow(x, 2) * z - 8 * ln(omx) * LMUF * NC * x + 8 * ln(omx) * LMUF * NC * pow(x, 2) - 8 * pow(ln(omx), 2) * pow(NC, -1) * x + 8 * pow(ln(omx), 2) * pow(NC, -1) * pow(x, 2) + 6 * pow(ln(omx), 2) * NC * x - 6 * pow(ln(omx), 2) * NC * pow(x, 2) - 14 * ln(omx) * ln(omz) * pow(NC, -1) * x + 14 * ln(omx) * ln(omz) * pow(NC, -1) * pow(x, 2) + 16 * ln(omx) * ln(omz) * NC * x - 16 * ln(omx) * ln(omz) * NC * pow(x, 2) - ln(omz) * pow(NC, -1) * z + 4 * ln(omz) * pow(NC, -1) * x * pow(z, -1) + 2 * ln(omz) * pow(NC, -1) * x * pow(omz, -1) + ln(omz) * pow(NC, -1) * x * pow(omxmz, -1) + 4 * ln(omz) * pow(NC, -1) * x - 3 * ln(omz) * pow(NC, -1) * x * z - 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(z, -1) - 2 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omz, -1) - ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -2) - ln(omz) * pow(NC, -1) * pow(x, 2) * pow(omxmz, -1);
      tmp += -4 * ln(omz) * pow(NC, -1) * pow(x, 2) + 4 * ln(omz) * pow(NC, -1) * pow(x, 2) * z + 2 * ln(omz) * pow(NC, -1) * pow(x, 3) * pow(omxmz, -2) - ln(omz) * pow(NC, -1) * pow(x, 4) * pow(omxmz, -2) + 4. / 3. * ln(omz) * NC * pow(x, -1) - 4 * ln(omz) * NC + ln(omz) * NC * z - ln(omz) * NC * x * pow(omxmz, -1) - 30 * ln(omz) * NC * x + 3 * ln(omz) * NC * x * z + ln(omz) * NC * pow(x, 2) * pow(omxmz, -2) + 3 * ln(omz) * NC * pow(x, 2) * pow(omxmz, -1) + 98. / 3. * ln(omz) * NC * pow(x, 2) - 4 * ln(omz) * NC * pow(x, 2) * z - 2 * ln(omz) * NC * pow(x, 3) * pow(omxmz, -2) - 2 * ln(omz) * NC * pow(x, 3) * pow(omxmz, -1) + ln(omz) * NC * pow(x, 4) * pow(omxmz, -2) + 4 * ln(omz) * LMUA * pow(NC, -1) * x - 4 * ln(omz) * LMUA * pow(NC, -1) * pow(x, 2) - 4 * ln(omz) * LMUA * NC * x + 4 * ln(omz) * LMUA * NC * pow(x, 2) - 7 * pow(ln(omz), 2) * pow(NC, -1) * x + 7 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) + 10 * pow(ln(omz), 2) * NC * x - 10 * pow(ln(omz), 2) * NC * pow(x, 2) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2);
      tmp += -1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1) + 31. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) - 11. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) + 11. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) + 29. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) - 29. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) + 9. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) + 5. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) + 73. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2);
      tmp += -1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) - 5. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) + 5. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * z * pow(sqrtxz2, -1) + 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1) - 151. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) + 51. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * z * pow(sqrtxz2, -1) - 51. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(z, 2) * pow(sqrtxz2, -1) - 129. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1) + 129. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * z * pow(sqrtxz2, -1) - 9. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) - 193. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) + 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2);
      tmp += +1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) +
             1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * z * pow(sqrtxz2, -1) + 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1) - 31. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(sqrtxz2, -1) + 11. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) - 11. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) - 29. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) + 29. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1);
      tmp += -9. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) *
                 pow(sqrtxz2, -1) * pow(poly2, -2) -
             5. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) *
                 pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) -
             73. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) + 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, -1) * pow(sqrtxz2, -1) + 5. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) - 5. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * z * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1) + 151. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(sqrtxz2, -1);
      tmp += -51. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * z * pow(sqrtxz2, -1) + 51. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * x * pow(z, 2) * pow(sqrtxz2, -1) + 129. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * pow(sqrtxz2, -1) - 129. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 2) * z * pow(sqrtxz2, -1) + 9. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) + 193. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 3) * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) - 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) + 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * z * pow(sqrtxz2, -1);
      tmp += +3. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1) - 31. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) + 11. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) - 11. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) - 29. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) + 29. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) - 9. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) - 5. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) - 73. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) + 3. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, -1) * pow(sqrtxz2, -1);
      tmp += +5. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) - 5. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * z * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1) + 151. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(sqrtxz2, -1) - 51. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * z * pow(sqrtxz2, -1) + 51. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1) + 129. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 2) * pow(sqrtxz2, -1) - 129. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1) + 9. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) + 193. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1);
      tmp += +1. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, -1) * pow(sqrtxz2, -1) +
             1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) - 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * z * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) * pow(poly2, -1) + 31. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(sqrtxz2, -1) - 11. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * z * pow(sqrtxz2, -1) + 11. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * x * pow(z, 2) * pow(sqrtxz2, -1) + 29. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz2, -1) - 29. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 2) * z * pow(sqrtxz2, -1) + 9. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) + 5. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) +
             73. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 3) * pow(sqrtxz2, -1) - 3. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) -
             3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -2);
      tmp += -1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, -1) * pow(sqrtxz2, -1) - 5. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) + 5. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * z * pow(sqrtxz2, -1) + 3. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(sqrtxz2, -1) * pow(poly2, -1) - 151. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(sqrtxz2, -1) + 51. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * z * pow(sqrtxz2, -1) - 51. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * x * pow(z, 2) * pow(sqrtxz2, -1) - 129. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 2) * pow(sqrtxz2, -1) + 129. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 2) * z * pow(sqrtxz2, -1) - 9. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) - 193. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 3) * pow(sqrtxz2, -1) + 3. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(x, 7) * pow(sqrtxz2, -1) * pow(poly2, -2) + 2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * x;
      tmp += -2 * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(x, 2) - 6 * Li2(1 - x * pow(z, -1)) * NC * x + 6 * Li2(1 - x * pow(z, -1)) * NC * pow(x, 2) + 4 * Li2(-x) * pow(NC, -1) * x - 4 * Li2(-x) * pow(NC, -1) * x * z + 4 * Li2(-x) * pow(NC, -1) * pow(x, 2) - 4 * Li2(-x) * pow(NC, -1) * pow(x, 2) * z + 4 * Li2(-x) * NC * x * z + 4 * Li2(-x) * NC * pow(x, 2) * z + 2 * Li2(x) * pow(NC, -1) * x + 4 * Li2(x) * pow(NC, -1) * x * z - 2 * Li2(x) * pow(NC, -1) * pow(x, 2) - 2 * Li2(x) * pow(NC, -1) * pow(x, 2) * z + 18 * Li2(x) * NC * x - 4 * Li2(x) * NC * x * z - 2 * Li2(x) * NC * pow(x, 2) + 2 * Li2(x) * NC * pow(x, 2) * z - 8 * Li2(z) * pow(NC, -1) * x + 8 * Li2(z) * pow(NC, -1) * pow(x, 2) + 8 * Li2(z) * NC * x - 8 * Li2(z) * NC * pow(x, 2);

      res += tmp;
    }
    return res;
  }
}