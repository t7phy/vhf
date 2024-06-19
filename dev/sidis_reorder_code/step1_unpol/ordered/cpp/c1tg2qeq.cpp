double C1Tg2qEq(double inx, double inz, std::string cx, std::string cz,
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
    res += 2 * x * TR + (-1)* 2 * pow(x, 2) * TR + (-1)* ln(x) * TR + 2 * ln(x) * x * TR + (-1)* 2 * ln(x) * pow(x, 2) * TR + ln(omx) * TR + (-1)* 2 * ln(omx) * x * TR + 2 * ln(omx) * pow(x, 2) * TR + 0;
    // Order 010:
    res += (-1)* LMUF * TR + 2 * LMUF * x * TR + (-1)* 2 * LMUF * pow(x, 2) * TR + 0;
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
    res += TR + (-1)* 2 * x * TR + 2 * pow(x, 2) * TR + 0;
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
      tmp += pow(z,-1) * TR + (-1)* 2 * TR + (-1)* 2 * x * pow(z,-1) * TR + 4 * x * TR + 2 * pow(x, 2) * pow(z,-1) * TR + (-1)* 4 * pow(x, 2) * TR + 0;
      res += tmp;
    }
    return res;
  }
}