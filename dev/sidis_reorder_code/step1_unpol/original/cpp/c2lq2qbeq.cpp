double C2Lq2qbEq(double inx, double inz, std::string cx, std::string cz,
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
      tmp = -4. / 3. * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omz, -1) * pow(opx, -1) + 4. / 3. * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omz, -1) + 4. / 3. * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(opx, -1) - 4. / 3. * pow(NC, -1) * pow(x, -1) * pow(z, -1) * pow(pi, 2) * CF + 4. / 3. * pow(NC, -1) * pow(x, -1) * pow(pi, 2) * CF * pow(opx, -1) - 4. / 3. * pow(NC, -1) * pow(x, -1) * pow(pi, 2) * CF + 4. / 3. * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2) * CF * pow(opx, -1) - 4. / 3. * pow(NC, -1) * pow(x, -1) * z * pow(pi, 2) * CF - 4. / 3. * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(omz, -1) * pow(opx, -1) + 4. / 3. * pow(NC, -1) * pow(z, -1) * pow(pi, 2) * CF * pow(opx, -1) - 12 * pow(NC, -1) * CF + 4. / 3. * pow(NC, -1) * pow(pi, 2) * CF * pow(opx, -1) + 20 * pow(NC, -1) * z * CF + 4. / 3. * pow(NC, -1) * z * pow(pi, 2) * CF * pow(opx, -1) - 16 * pow(NC, -1) * x * pow(z, -1) * pow(rln2, 2) * CF * pow(opz, -1) + 16 * pow(NC, -1) * x * pow(z, -1) * pow(rln2, 2) * CF - 32 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF * pow(opz, -1) + 32 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF - 24 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(rln2, 2) * CF * pow(opz, -1) + 24 * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * pow(rln2, 2) * CF - 4. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF * pow(omz, -1) + 4. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * CF - 4. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * sqrtxz1 * CF * pow(opz, -1) + 4. / 3. * pow(NC, -1) * x * pow(z, -1) * pow(pi, 2) * sqrtxz1 * CF - 96 * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) + 64 * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF - 72 * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(rln2, 2) * CF * pow(opz, -1);
      tmp += +48 * pow(NC, -1) * x * pow(sqrtxz1, -1) * pow(rln2, 2) * CF + 12 * pow(NC, -1) * x * CF - 16 * pow(NC, -1) * x * pow(rln2, 2) * CF - 4 * pow(NC, -1) * x * pow(pi, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 8. / 3. * pow(NC, -1) * x * pow(pi, 2) * pow(sqrtxz1, -1) * CF + 4. / 3. * pow(NC, -1) * x * pow(pi, 2) * CF * pow(omz, -1) + 2. / 3. * pow(NC, -1) * x * pow(pi, 2) * CF + 32 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 32 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF + 24 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(rln2, 2) * CF * pow(opz, -1) - 24 * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * pow(rln2, 2) * CF - 20 * pow(NC, -1) * x * z * CF + 16 * pow(NC, -1) * x * z * pow(rln2, 2) * CF + 4. / 3. * pow(NC, -1) * x * z * pow(pi, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 4. / 3. * pow(NC, -1) * x * z * pow(pi, 2) * pow(sqrtxz1, -1) * CF - 4. / 3. * pow(NC, -1) * x * z * pow(pi, 2) * CF + 128 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 128 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF + 96 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(rln2, 2) * CF * pow(opz, -1) - 96 * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * pow(rln2, 2) * CF + 16. / 3. * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16. / 3. * pow(NC, -1) * pow(x, 2) * pow(pi, 2) * pow(sqrtxz1, -1) * CF + 20. / 9. * pow(x, -1) * CF + 4. / 3. * pow(x, -1) * z * pow(pi, 2) * CF * pow(opx, -1) - 4. / 3. * pow(x, -1) * z * pow(pi, 2) * CF - 8. / 3. * pow(x, -1) * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1) + 8. / 3. * pow(x, -1) * pow(z, 2) * pow(pi, 2) * CF - 68. / 3. * CF + 24 * z * CF + 4. / 3. * z * pow(pi, 2) * CF * pow(opx, -1) + 2 * pow(z, 2) * CF - 8. / 3. * pow(z, 2) * pow(pi, 2) * CF * pow(opx, -1);
      tmp += +41. / 3. * x * CF + 8 * x * sqrtxz1 * rln2 * CF - x * pow(pi, 2) * CF - 22 * x * z * CF + 2. / 3. * x * z * pow(pi, 2) * CF - 7 * x * pow(z, 2) * CF + 32 * x * pow(z, 2) * pow(rln2, 2) * CF - 8. / 3. * x * pow(z, 2) * pow(pi, 2) * CF +
             88. / 9. * pow(x, 2) * CF - 4. / 3. * LMUF * pow(x, -1) * CF + 4 * LMUF * CF - 8. / 3. * LMUF * pow(x, 2) * CF + 4 * LMUA * x * CF - 2 * LMUA * x * z * CF - 2 * LMUA * x * pow(z, 2) * CF + 16 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF + 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 2 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * sqrtxz3 * CF + 46 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF -
             6 * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * z * sqrtxz3 * CF - 16 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF - 2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 2 * ArcTan(sqrtxz3) * ln(sqrtxz3) * sqrtxz3 * CF - 46 * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 6 * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * z * sqrtxz3 * CF - 8 * InvTanInt(-sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF - InvTanInt(-sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + InvTanInt(-sqrtxz3) * sqrtxz3 * CF - 23 * InvTanInt(-sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3 * InvTanInt(-sqrtxz3) * x * z * sqrtxz3 * CF - 16 * InvTanInt(z * sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF - 2 * InvTanInt(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 2 * InvTanInt(z * sqrtxz3) * sqrtxz3 * CF - 46 * InvTanInt(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 6 * InvTanInt(z * sqrtxz3) * x * z * sqrtxz3 * CF + 8 * InvTanInt(sqrtxz3) * pow(NC, -1) * pow(z, 2) * sqrtxz3 * CF;
      tmp += +InvTanInt(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - InvTanInt(sqrtxz3) * sqrtxz3 * CF + 23 * InvTanInt(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 3 * InvTanInt(sqrtxz3) * x * z * sqrtxz3 * CF + 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF * pow(opz, -1) - 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF + 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) -
             32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF * pow(opz, -1) - 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF + 96 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 64 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 96 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 64 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF + 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * rln2 * CF - 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) + 32 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF - 16 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * rln2 * CF -
             128 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 128 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 128 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1);
      tmp += +128 * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF - 8 * ln(1 + sqrtxz1 - z) * x * sqrtxz1 * CF + 8 * ln(1 + sqrtxz1 - z) * x * z * rln2 * CF - 48 * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * rln2 * CF - 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 24 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 32 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * pow(ln(1 + sqrtxz1 - z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 8 * pow(ln(1 + sqrtxz1 - z), 2) * x * z * CF + 16 * pow(ln(1 + sqrtxz1 - z), 2) * x * pow(z, 2) * CF - 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) + 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF - 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 48 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * CF;
      tmp += +16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * CF + 64 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 64 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 8 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * z * CF + 16 * ln(1 + sqrtxz1 - z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF + 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF * pow(opz, -1) - 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF + 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF * pow(opz, -1) -
             16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF + 48 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 32 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF + 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * rln2 * CF - 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) + 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF - 16 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * rln2 * CF - 64 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) + 64 * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF - 8 * ln(1 + sqrtxz1 + z) * x * z * rln2 * CF - 16 * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * rln2 * CF;
      tmp += -2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 6 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 4 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 2 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 8 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * pow(ln(1 - 2 * z + pow(z, 2) + 4 * x * z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 16 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 16 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) + 16 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) - 16 * ln(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF + 16 * ln(x) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) - 16 * ln(x) * pow(NC, -1) * pow(x, -1) * CF + 16 * ln(x) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) - 16 * ln(x) * pow(NC, -1) * pow(x, -1) * z * CF - 16 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 16 * ln(x) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) + 16 * ln(x) * pow(NC, -1) * CF * pow(opx, -1) - 4 * ln(x) * pow(NC, -1) * CF + 16 * ln(x) * pow(NC, -1) * z * CF * pow(opx, -1) + 8 * ln(x) * pow(NC, -1) * z * CF - 16 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) + 16 * ln(x) * pow(NC, -1) * x * pow(z, -1) * CF;
      tmp += -8 * ln(x) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF * pow(opz, -1) + 8 * ln(x) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF - 16 * ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 16 * ln(x) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 48 * ln(x) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * ln(x) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 16 * ln(x) * pow(NC, -1) * x * CF * pow(omz, -1) - 4 * ln(x) * pow(NC, -1) * x * CF - 8 * ln(x) * pow(NC, -1) * x * rln2 * CF + 16 * ln(x) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * ln(x) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 8 * ln(x) * pow(NC, -1) * x * z * CF + 8 * ln(x) * pow(NC, -1) * x * z * rln2 * CF + 64 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 64 * ln(x) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - ln(x) * pow(x, -1) * pow(poly2, -1) * CF + ln(x) * pow(x, -1) * CF + 16 * ln(x) * pow(x, -1) * z * CF * pow(opx, -1) - 16 * ln(x) * pow(x, -1) * z * CF - 32 * ln(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 32 * ln(x) * pow(x, -1) * pow(z, 2) * CF + ln(x) * pow(poly2, -1) * CF - 2 * ln(x) * CF + 16 * ln(x) * z * CF * pow(opx, -1) + 11 * ln(x) * z * CF - 32 * ln(x) * pow(z, 2) * CF * pow(opx, -1) + 2 * ln(x) * x * pow(poly2, -1) * CF - 14 * ln(x) * x * CF + 4 * ln(x) * x * sqrtxz1 * CF + 11 * ln(x) * x * z * CF - 8 * ln(x) * x * z * rln2 * CF - 4 * ln(x) * x * pow(z, 2) * CF + 32 * ln(x) * x * pow(z, 2) * rln2 * CF - 2 * ln(x) * pow(x, 2) * pow(poly2, -1) * CF + 4 * ln(x) * pow(x, 2) * CF * pow(xmz, -1) - 5 * ln(x) * pow(x, 2) * CF - ln(x) * pow(x, 3) * pow(poly2, -1) * CF - 4 * ln(x) * pow(x, 3) * CF * pow(xmz, -1) + ln(x) * pow(x, 4) * pow(poly2, -1) * CF + 4 * ln(x) * LMUF * x * CF - 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF;
      tmp += +1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - ln(x) * ln(1 - sqrtxz2 + x) * pow(sqrtxz2, -1) * CF + 2 * ln(x) * ln(1 - sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF + 3. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 8 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF - 8 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 2 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF -
             1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + ln(x) * ln(1 + sqrtxz2 + x) * pow(sqrtxz2, -1) * CF - 2 * ln(x) * ln(1 + sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF - 3. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF + 8 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 2 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF -
             1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF;
      tmp += -8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 24 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) -
             8 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 32 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * ln(x) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 8 * ln(x) * ln(1 + sqrtxz1 - z) * x * z * CF - 16 * ln(x) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 24 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * CF - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 8 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * CF - 32 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * ln(x) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF;
      tmp += -16 * ln(x) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * CF * pow(opx, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * CF - 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF + 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF - 4 * ln(x) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1);
      tmp += -4 * ln(x) * ln(1 + x * pow(z, -1)) * x * z * CF + 8 * ln(x) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF - 8 * ln(x) * ln(1 + x) * pow(NC, -1) * x * z * CF + 8 * ln(x) * ln(1 + x) * x * CF - 24 * ln(x) * ln(1 + x) * x * z * CF + 16 * ln(x) * ln(1 + x) * x * pow(z, 2) * CF + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * CF - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * CF + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * CF * pow(opx, -1) - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 4 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * ln(x) * ln(1 + x * z) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(x) * ln(1 + x * z) * pow(x, -1) * z * CF + 8 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(x) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF - 4 * ln(x) * ln(1 + x * z) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1) + 16 * ln(x) * ln(1 + x * z) * x * pow(z, 2) * CF;
      tmp += +4 * ln(x) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 4 * ln(x) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * CF + 4 * ln(x) * ln(z + x) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(z + x) * pow(NC, -1) * x * z * CF - 4 * ln(x) * ln(z + x) * x * z * CF - 8 * ln(x) * ln(z + x) * x * pow(z, 2) * CF + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * CF - 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(x, -1) * z * CF + 6 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 6 * pow(ln(x), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) - 6 * pow(ln(x), 2) * pow(NC, -1) * CF * pow(opx, -1) - 6 * pow(ln(x), 2) * pow(NC, -1) * z * CF * pow(opx, -1) + 6 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 6 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * CF + 6 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 6 * pow(ln(x), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 18 * pow(ln(x), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 12 * pow(ln(x), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 6 * pow(ln(x), 2) * pow(NC, -1) * x * CF * pow(omz, -1) + 2 * pow(ln(x), 2) * pow(NC, -1) * x * CF - 6 * pow(ln(x), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 6 * pow(ln(x), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF;
      tmp += -24 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 24 * pow(ln(x), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 6 * pow(ln(x), 2) * pow(x, -1) * z * CF * pow(opx, -1) + 6 * pow(ln(x), 2) * pow(x, -1) * z * CF + 12 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 12 * pow(ln(x), 2) * pow(x, -1) * pow(z, 2) * CF - 6 * pow(ln(x), 2) * z * CF * pow(opx, -1) + 12 * pow(ln(x), 2) * pow(z, 2) * CF * pow(opx, -1) + 12 * pow(ln(x), 2) * x * z * CF - 8 * pow(ln(x), 2) * x * pow(z, 2) * CF - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * CF + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(x, -1) * z * CF - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 4 * ln(x) * ln(z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) + 4 * ln(x) * ln(z) * pow(NC, -1) * CF * pow(opx, -1) + 4 * ln(x) * ln(z) * pow(NC, -1) * z * CF * pow(opx, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) + 8 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * CF + 4 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 12 * ln(x) * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1);
      tmp += -8 * ln(x) * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 4 * ln(x) * ln(z) * pow(NC, -1) * x * CF * pow(omz, -1) - 4 * ln(x) * ln(z) * pow(NC, -1) * x * CF - 4 * ln(x) * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 4 * ln(x) * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 8 * ln(x) * ln(z) * pow(NC, -1) * x * z * CF - 16 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * ln(x) * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 4 * ln(x) * ln(z) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(x) * ln(z) * pow(x, -1) * z * CF - 8 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(z) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(x) * ln(z) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(z) * pow(z, 2) * CF * pow(opx, -1) + 2 * ln(x) * ln(z) * x * CF + 4 * ln(x) * ln(z) * x * z * CF + 8 * ln(x) * ln(z) * x * pow(z, 2) * CF + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * CF - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(x, -1) * z * CF + 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 8 * ln(x) * ln(omx) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) -
             8 * ln(x) * ln(omx) * pow(NC, -1) * CF * pow(opx, -1) - 8 * ln(x) * ln(omx) * pow(NC, -1) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1);
      tmp += -8 * ln(x) * ln(omx) * pow(NC, -1) * x * pow(z, -1) * CF - 8 * ln(x) * ln(omx) * pow(NC, -1) * x * CF * pow(omz, -1) - 4 * ln(x) * ln(omx) * pow(NC, -1) * x * CF + 4 * ln(x) * ln(omx) * pow(NC, -1) * x * z * CF - 8 * ln(x) * ln(omx) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * ln(x) * ln(omx) * pow(x, -1) * z * CF + 16 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 16 * ln(x) * ln(omx) * pow(x, -1) * pow(z, 2) * CF - 8 * ln(x) * ln(omx) * z * CF * pow(opx, -1) + 16 * ln(x) * ln(omx) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(x) * ln(omx) * x * z * CF + 16 * ln(x) * ln(omx) * x * pow(z, 2) * CF - 8 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 8 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 24 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * ln(x) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * ln(x) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * ln(x) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 32 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * ln(x) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 4 * ln(x) * ln(omz) * x * CF - 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) + 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) - 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF + 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) - 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * CF + 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1);
      tmp += -8 * ln(x) * ln(opx) * pow(NC, -1) * pow(x, -1) * z * CF - 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 8 * ln(x) * ln(opx) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) + 8 * ln(x) * ln(opx) * pow(NC, -1) * CF * pow(opx, -1) + 8 * ln(x) * ln(opx) * pow(NC, -1) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(opx) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) + 8 * ln(x) * ln(opx) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * ln(x) * ln(opx) * pow(NC, -1) * x * CF + 8 * ln(x) * ln(opx) * pow(NC, -1) * x * z * CF + 8 * ln(x) * ln(opx) * pow(x, -1) * z * CF * pow(opx, -1) - 8 * ln(x) * ln(opx) * pow(x, -1) * z * CF - 16 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 16 * ln(x) * ln(opx) * pow(x, -1) * pow(z, 2) * CF + 8 * ln(x) * ln(opx) * z * CF * pow(opx, -1) - 16 * ln(x) * ln(opx) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(x) * ln(opx) * x * z * CF - 16 * ln(x) * ln(opx) * x * pow(z, 2) * CF + 4 * ln(z) * pow(NC, -1) * z * CF - 24 * ln(z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF * pow(opz, -1) + 24 * ln(z) * pow(NC, -1) * x * pow(z, -1) * rln2 * CF - 16 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 16 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 32 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF * pow(opz, -1) + 32 * ln(z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF - 48 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 96 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) + 64 * ln(z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF - 24 * ln(z) * pow(NC, -1) * x * rln2 * CF + 16 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF;
      tmp += +32 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 32 * ln(z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF - 4 * ln(z) * pow(NC, -1) * x * z * CF + 24 * ln(z) * pow(NC, -1) * x * z * rln2 * CF + 64 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 64 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 128 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 128 * ln(z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF - ln(z) * pow(x, -1) * pow(poly2, -1) * CF + 7. / 3. * ln(z) * pow(x, -1) * CF - ln(z) * pow(poly2, -1) * CF - 10 * ln(z) * CF + 7 * ln(z) * z * CF + 2 * ln(z) * x * pow(poly2, -1) * CF + 4 * ln(z) * x * sqrtxz1 * CF - 7 * ln(z) * x * z * CF + 8 * ln(z) * x * z * rln2 * CF + 2 * ln(z) * x * pow(z, 2) * CF + 32 * ln(z) * x * pow(z, 2) * rln2 * CF + 2 * ln(z) * pow(x, 2) * pow(poly2, -1) * CF - 4 * ln(z) * pow(x, 2) * CF * pow(xmz, -1) - 1. / 3. * ln(z) * pow(x, 2) * CF - ln(z) * pow(x, 3) * pow(poly2, -1) * CF + 4 * ln(z) * pow(x, 3) * CF * pow(xmz, -1) - ln(z) * pow(x, 4) * pow(poly2, -1) * CF + 2 * ln(z) * LMUA * x * CF + 4 * ln(z) * LMUA * x * z * CF + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * CF + 16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 48 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * CF - 16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1);
      tmp += +16 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 8 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * CF - 64 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 64 * ln(z) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 16 * ln(z) * ln(1 + sqrtxz1 - z) * x * pow(z, 2) * CF + 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * CF + 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 48 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF +
             16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * CF - 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 16 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * x * z * CF - 64 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 64 * ln(z) * ln(1 + sqrtxz1 + z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 8 * ln(z) * ln(1 + sqrtxz1 + z) * x * z * CF - 16 * ln(z) * ln(1 + sqrtxz1 + z) * x * pow(z, 2) * CF - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1);
      tmp += -4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * CF + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(NC, -1) * x * z * CF + 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * z * CF - 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF + 4 * ln(z) * ln(1 + x * pow(z, -1)) * z * CF * pow(opx, -1) - 8 * ln(z) * ln(1 + x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * pow(z, -1)) * x * z * CF - 8 * ln(z) * ln(1 + x * pow(z, -1)) * x * pow(z, 2) * CF + 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1);
      tmp += +4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * CF - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(x, -1) * z * CF + 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * CF * pow(opx, -1) - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * z * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 4 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * ln(z) * ln(1 + x * z) * pow(NC, -1) * x * CF - 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * ln(z) * ln(1 + x * z) * pow(x, -1) * z * CF + 8 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 8 * ln(z) * ln(1 + x * z) * pow(x, -1) * pow(z, 2) * CF - 4 * ln(z) * ln(1 + x * z) * z * CF * pow(opx, -1) + 8 * ln(z) * ln(1 + x * z) * pow(z, 2) * CF * pow(opx, -1) + 16 * ln(z) * ln(1 + x * z) * x * pow(z, 2) * CF - 4 * ln(z) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) + 4 * ln(z) * ln(z + x) * pow(NC, -1) * x * pow(z, -1) * CF - 4 * ln(z) * ln(z + x) * pow(NC, -1) * x * CF + 4 * ln(z) * ln(z + x) * pow(NC, -1) * x * z * CF + 4 * ln(z) * ln(z + x) * x * z * CF + 8 * ln(z) * ln(z + x) * x * pow(z, 2) * CF - 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1);
      tmp += -2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) - 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * CF + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) - 2 * pow(ln(z), 2) * pow(NC, -1) * pow(x, -1) * z * CF - 2 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 2 * pow(ln(z), 2) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) + 2 * pow(ln(z), 2) * pow(NC, -1) * CF * pow(opx, -1) + 2 * pow(ln(z), 2) * pow(NC, -1) * z * CF * pow(opx, -1) - 2 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 4 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) + 6 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * CF - 10 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 10 * pow(ln(z), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 30 * pow(ln(z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 20 * pow(ln(z), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 2 * pow(ln(z), 2) * pow(NC, -1) * x * CF + 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 10 * pow(ln(z), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 6 * pow(ln(z), 2) * pow(NC, -1) * x * z * CF + 40 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) -
             40 * pow(ln(z), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 2 * pow(ln(z), 2) * pow(x, -1) * z * CF * pow(opx, -1) - 2 * pow(ln(z), 2) * pow(x, -1) * z * CF - 4 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) +
             4 * pow(ln(z), 2) * pow(x, -1) * pow(z, 2) * CF + 2 * pow(ln(z), 2) * z * CF * pow(opx, -1) - 4 * pow(ln(z), 2) * pow(z, 2) * CF * pow(opx, -1);
      tmp += -4 * pow(ln(z), 2) * x * CF + 4 * pow(ln(z), 2) * x * z * CF - 8 * pow(ln(z), 2) * x * pow(z, 2) * CF - 2 * ln(z) * ln(omx) * x * CF - 4 * ln(z) * ln(omx) * x * z * CF - 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 8 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 24 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * ln(z) * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * ln(z) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * ln(z) * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 32 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * ln(z) * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 4 * ln(z) * ln(omz) * x * CF - 8 * ln(z) * ln(omz) * x * z * CF + 4. / 3. * ln(omx) * pow(x, -1) * CF - 4 * ln(omx) * CF - 4 * ln(omx) * x * CF + 2 * ln(omx) * x * z * CF + 2 * ln(omx) * x * pow(z, 2) * CF + 8. / 3. * ln(omx) * pow(x, 2) * CF - 16 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF * pow(opz, -1) + 16 * ln(omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * rln2 * CF - 48 * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) + 32 * ln(omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * rln2 * CF + 16 * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 16 * ln(omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * rln2 * CF + 64 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF * pow(opz, -1) - 64 * ln(omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * rln2 * CF + 4. / 3. * ln(omz) * pow(x, -1) * CF - 4 * ln(omz) * CF - 4 * ln(omz) * x * CF + 2 * ln(omz) * x * z * CF + 2 * ln(omz) * x * pow(z, 2) * CF + 8. / 3. * ln(omz) * pow(x, 2) * CF;
      tmp += +16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 48 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 64 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 64 * ln(omz) * ln(1 + sqrtxz1 - z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 24 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 8 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 32 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) +
             32 * ln(omz) * ln(1 - 2 * z + pow(z, 2) + 4 * x * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 8 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF;
      tmp += -24 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * pow(ln(omz), 2) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * pow(ln(omz), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * pow(ln(omz), 2) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 32 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * pow(ln(omz), 2) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF + 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF + 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF;
      tmp += +1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF - 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF - 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) + 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF;
      tmp += -8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) *
                 sqrtxz1 * CF * pow(opz, -1) +
             8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) *
                 x * pow(z, -1) * sqrtxz1 * CF -
             24 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * CF + 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * CF + 32 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * x * z * CF + 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * CF - 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF;
      tmp += -24 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * CF + 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * x * z * CF + 32 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 32 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 8 * Li2(1. / 2. + 1. / 2. * pow(z, -1) - 1. / 2. * pow(z, -1) * sqrtxz1) * x * z * CF + 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(sqrtxz2, -1) * CF - 2 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * z * pow(sqrtxz2, -1) * CF - 3. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(sqrtxz2, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF;
      tmp += +2 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 3. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(sqrtxz2, -1) * CF + 2 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * z * pow(sqrtxz2, -1) * CF + 3. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 8 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(sqrtxz2, -1) * CF - 8 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 2 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 3. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1);
      tmp += -8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 24 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * CF - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * x * z * CF - 32 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 16 * Li2(1. / 2. - 1. / 2. * sqrtxz1 - 1. / 2. * z) * x * pow(z, 2) * CF - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF + 24 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * CF - 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF;
      tmp += +8 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * x * z * CF - 32 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 16 * Li2(1. / 2. - 1. / 2. * sqrtxz1 + 1. / 2. * z) * x * pow(z, 2) * CF - 4 * Li2(1 - x * pow(z, -1)) * x * CF + 8 * Li2(1 - x * pow(z, -1)) * x * z * CF - 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 48 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 64 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 64 * Li2(pow(sqrtxz1, -1) * omz) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF - 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 48 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 32 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 16 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 64 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1);
      tmp += -64 * Li2(-sqrtxz1 * pow(omz, -1)) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * CF - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(x, -1) * z * CF + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * CF * pow(opx, -1) - 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * z * CF * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) + 4 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * pow(z, -1) * CF - 8 * Li2(-x * pow(z, -1)) * pow(NC, -1) * x * z * CF - 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * Li2(-x * pow(z, -1)) * pow(x, -1) * z * CF + 8 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 8 * Li2(-x * pow(z, -1)) * pow(x, -1) * pow(z, 2) * CF - 4 * Li2(-x * pow(z, -1)) * z * CF * pow(opx, -1) + 8 * Li2(-x * pow(z, -1)) * pow(z, 2) * CF * pow(opx, -1) - 8 * Li2(-x * pow(z, -1)) * x * z * CF - 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1);
      tmp += +8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) + 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) - 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF + 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) - 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * CF + 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) - 8 * Li2(-x) * pow(NC, -1) * pow(x, -1) * z * CF - 8 * Li2(-x) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) + 8 * Li2(-x) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) + 8 * Li2(-x) * pow(NC, -1) * CF * pow(opx, -1) + 8 * Li2(-x) * pow(NC, -1) * z * CF * pow(opx, -1) - 8 * Li2(-x) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) + 8 * Li2(-x) * pow(NC, -1) * x * pow(z, -1) * CF + 8 * Li2(-x) * pow(NC, -1) * x * CF + 8 * Li2(-x) * pow(x, -1) * z * CF * pow(opx, -1) - 8 * Li2(-x) * pow(x, -1) * z * CF - 16 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) + 16 * Li2(-x) * pow(x, -1) * pow(z, 2) * CF + 8 * Li2(-x) * z * CF * pow(opx, -1) - 16 * Li2(-x) * pow(z, 2) * CF * pow(opx, -1) + 8 * Li2(-x) * x * CF - 16 * Li2(-x) * x * z * CF + 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) -
             4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) + 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * CF - 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * Li2(-x * z) * pow(NC, -1) * pow(x, -1) * z * CF + 4 * Li2(-x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1);
      tmp += -4 * Li2(-x * z) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) - 4 * Li2(-x * z) * pow(NC, -1) * CF * pow(opx, -1) - 4 * Li2(-x * z) * pow(NC, -1) * z * CF * pow(opx, -1) + 4 * Li2(-x * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 4 * Li2(-x * z) * pow(NC, -1) * x * pow(z, -1) * CF * pow(opz, -1) - 8 * Li2(-x * z) * pow(NC, -1) * x * CF - 4 * Li2(-x * z) * pow(x, -1) * z * CF * pow(opx, -1) + 4 * Li2(-x * z) * pow(x, -1) * z * CF + 8 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 8 * Li2(-x * z) * pow(x, -1) * pow(z, 2) * CF - 4 * Li2(-x * z) * z * CF * pow(opx, -1) + 8 * Li2(-x * z) * pow(z, 2) * CF * pow(opx, -1) + 16 * Li2(-x * z) * x * pow(z, 2) * CF - 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF * pow(opz, -1) + 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(z, -1) * sqrtxz1 * CF - 24 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF * pow(opz, -1) + 16 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * pow(sqrtxz1, -1) * CF + 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF * pow(opz, -1) - 8 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * x * z * pow(sqrtxz1, -1) * CF + 32 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF * pow(opz, -1);
      tmp += -32 * Li2(-1 / (1 + sqrtxz1 - z) + 1 / (1 + sqrtxz1 - z) * sqrtxz1 + 1 / (1 + sqrtxz1 - z) * z) * pow(NC, -1) * pow(x, 2) * pow(sqrtxz1, -1) * CF + 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(omz, -1) - 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF * pow(opx, -1) + 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * pow(z, -1) * CF - 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * CF * pow(opx, -1) + 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * CF - 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * Li2(x) * pow(NC, -1) * pow(x, -1) * z * CF + 8 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF * pow(omz, -1) * pow(opx, -1) - 8 * Li2(x) * pow(NC, -1) * pow(z, -1) * CF * pow(opx, -1) - 8 * Li2(x) * pow(NC, -1) * CF * pow(opx, -1) - 8 * Li2(x) * pow(NC, -1) * z * CF * pow(opx, -1) + 8 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * CF * pow(omz, -1) - 8 * Li2(x) * pow(NC, -1) * x * pow(z, -1) * CF - 8 * Li2(x) * pow(NC, -1) * x * CF * pow(omz, -1) - 4 * Li2(x) * pow(NC, -1) * x * CF + 4 * Li2(x) * pow(NC, -1) * x * z * CF - 8 * Li2(x) * pow(x, -1) * z * CF * pow(opx, -1) + 8 * Li2(x) * pow(x, -1) * z * CF + 16 * Li2(x) * pow(x, -1) * pow(z, 2) * CF * pow(opx, -1) - 16 * Li2(x) * pow(x, -1) * pow(z, 2) * CF - 8 * Li2(x) * z * CF * pow(opx, -1) + 16 * Li2(x) * pow(z, 2) * CF * pow(opx, -1) + 4 * Li2(x) * x * CF - 8 * Li2(x) * x * z * CF + 16 * Li2(x) * x * pow(z, 2) * CF + 6 * Li2(z) * x * CF - 4 * Li2(z) * x * z * CF;

      res += tmp;
    }
    return res;
  }
}