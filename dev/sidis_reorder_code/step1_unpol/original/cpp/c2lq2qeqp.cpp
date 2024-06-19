double C2Lq2qEqp(double inx, double inz, std::string cx, std::string cz,
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
      tmp = 3. / 4. * pow(x, -1) * pow(z, -1) * CF - 3. / 4. * pow(x, -1) * CF + 3. / 4. * pow(z, -2) * CF - 7. / 2. * pow(z, -1) * CF + 3. / 2. * CF + 5. / 4. * z * CF - 3. / 4. * x * pow(z, -2) * CF + 3. / 2. * x * pow(z, -1) * CF + 1. / 2. * x * CF - 5. / 4. * x * z * CF + 5. / 4. * pow(x, 2) * pow(z, -1) * CF - 5. / 4. * pow(x, 2) * CF - 3. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -2) * sqrtxz3 * CF + 1. / 2. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF - 3. / 2. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 3. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, -2) * sqrtxz3 * CF + ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * sqrtxz3 * CF + 5. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 3. / 2. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF + 9. / 2. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * x * z * sqrtxz3 * CF + 5. / 4. * ArcTan(z * sqrtxz3) * ln(z * sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 3. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 1. / 2. * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF + 3. / 2. * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 3. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - ArcTan(sqrtxz3) * ln(sqrtxz3) * sqrtxz3 * CF - 5. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3. / 2. * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9. / 2. * ArcTan(sqrtxz3) * ln(sqrtxz3) * x * z * sqrtxz3 * CF - 5. / 4. * ArcTan(sqrtxz3) * ln(sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 3. / 8. * InvTanInt(-sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 1. / 4. * InvTanInt(-sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF;
      tmp += +3. / 4. * InvTanInt(-sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 3. / 8. * InvTanInt(-sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - 1. / 2. * InvTanInt(-sqrtxz3) * sqrtxz3 * CF - 5. / 8. * InvTanInt(-sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3. / 4. * InvTanInt(-sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9. / 4. * InvTanInt(-sqrtxz3) * x * z * sqrtxz3 * CF - 5. / 8. * InvTanInt(-sqrtxz3) * pow(x, 2) * sqrtxz3 * CF + 3. / 4. * InvTanInt(z * sqrtxz3) * pow(x, -2) * sqrtxz3 * CF - 1. / 2. * InvTanInt(z * sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF + 3. / 2. * InvTanInt(z * sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF + 3. / 4. * InvTanInt(z * sqrtxz3) * pow(z, -2) * sqrtxz3 * CF - InvTanInt(z * sqrtxz3) * sqrtxz3 * CF - 5. / 4. * InvTanInt(z * sqrtxz3) * pow(z, 2) * sqrtxz3 * CF + 3. / 2. * InvTanInt(z * sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF - 9. / 2. * InvTanInt(z * sqrtxz3) * x * z * sqrtxz3 * CF - 5. / 4. * InvTanInt(z * sqrtxz3) * pow(x, 2) * sqrtxz3 * CF - 3. / 8. * InvTanInt(sqrtxz3) * pow(x, -2) * sqrtxz3 * CF + 1. / 4. * InvTanInt(sqrtxz3) * pow(x, -1) * pow(z, -1) * sqrtxz3 * CF - 3. / 4. * InvTanInt(sqrtxz3) * pow(x, -1) * z * sqrtxz3 * CF - 3. / 8. * InvTanInt(sqrtxz3) * pow(z, -2) * sqrtxz3 * CF + 1. / 2. * InvTanInt(sqrtxz3) * sqrtxz3 * CF + 5. / 8. * InvTanInt(sqrtxz3) * pow(z, 2) * sqrtxz3 * CF - 3. / 4. * InvTanInt(sqrtxz3) * x * pow(z, -1) * sqrtxz3 * CF + 9. / 4. * InvTanInt(sqrtxz3) * x * z * sqrtxz3 * CF + 5. / 8. * InvTanInt(sqrtxz3) * pow(x, 2) * sqrtxz3 * CF - 3. / 8. * ln(x) * pow(x, -1) * pow(z, -1) * CF + 3. / 8. * ln(x) * pow(x, -1) * CF + 3. / 8. * ln(x) * pow(z, -2) * CF - 1. / 4. * ln(x) * pow(z, -1) * CF - 3. / 4. * ln(x) * CF + 5. / 8. * ln(x) * z * CF;
      tmp += +3. / 8. * ln(x) * x * pow(z, -2) * CF - 13. / 4. * ln(x) * x * pow(z, -1) * CF + 9. / 4. * ln(x) * x * CF + 5. / 8. * ln(x) * x * z * CF + 5. / 8. * ln(x) * pow(x, 2) * pow(z, -1) * CF - 5. / 8. * ln(x) * pow(x, 2) * CF - 4 * ln(x) * ln(z) * x * CF + 3. / 8. * ln(z) * pow(x, -1) * pow(z, -1) * CF + 3. / 8. * ln(z) * pow(x, -1) * CF - 3. / 8. * ln(z) * pow(z, -2) * CF - 1. / 4. * ln(z) * pow(z, -1) * CF - 13. / 4. * ln(z) * CF + 5. / 8. * ln(z) * z * CF + 3. / 8. * ln(z) * x * pow(z, -2) * CF - 3. / 4. * ln(z) * x * pow(z, -1) * CF + 9. / 4. * ln(z) * x * CF - 5. / 8. * ln(z) * x * z * CF + 5. / 8. * ln(z) * pow(x, 2) * pow(z, -1) * CF + 5. / 8. * ln(z) * pow(x, 2) * CF;

      res += tmp;
    }
    return res;
  }
}