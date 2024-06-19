double C2Tq2qpEqp(double inx, double inz, std::string cx, std::string cz,
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
    res = 52. / 27. * pow(x, -1) * CF - 41. / 36. * CF + 1. / 6. * pow(pi, 2) * CF + 17. / 36. * x * CF + 1. / 2. * x * pow(pi, 2) * CF - 34. / 27. * pow(x, 2) * CF + 1. / 3. * pow(x, 2) * pow(pi, 2) * CF - 13. / 9. * LMUF * pow(x, -1) * CF + 11. / 6. * LMUF * CF - 1. / 6. * LMUF * pow(pi, 2) * CF - 17. / 6. * LMUF * x * CF - 1. / 6. * LMUF * x * pow(pi, 2) * CF + 22. / 9. * LMUF * pow(x, 2) * CF + 1. / 3. * pow(LMUF, 2) * pow(x, -1) * CF + 1. / 4. * pow(LMUF, 2) * CF - 1. / 4. * pow(LMUF, 2) * x * CF - 1. / 3. * pow(LMUF, 2) * pow(x, 2) * CF + 23. / 6. * ln(x) * CF - 1. / 3. * ln(x) * pow(pi, 2) * CF - 5. / 6. * ln(x) * x * CF - 1. / 3. * ln(x) * x * pow(pi, 2) * CF + 38. / 9. * ln(x) * pow(x, 2) * CF - ln(x) * LMUF * CF - 3 * ln(x) * LMUF * x * CF - 2 * ln(x) * LMUF * pow(x, 2) * CF + 1. / 2. * ln(x) * pow(LMUF, 2) * CF + 1. / 2. * ln(x) * pow(LMUF, 2) * x * CF - 13. / 8. * pow(ln(x), 2) * CF - 13. / 8. * pow(ln(x), 2) * x * CF - 5. / 3. * pow(ln(x), 2) * pow(x, 2) * CF +
          pow(ln(x), 2) * LMUF * CF + pow(ln(x), 2) * LMUF * x * CF + 5. / 12. * pow(ln(x), 3) * CF + 5. / 12. * pow(ln(x), 3) * x * CF - 2. / 3. * ln(x) * ln(omx) * pow(x, -1) * CF - 1. / 2. * ln(x) * ln(omx) * CF + 1. / 2. * ln(x) * ln(omx) * x * CF + 2. / 3. * ln(x) * ln(omx) * pow(x, 2) * CF - 1. / 2. * ln(x) * pow(ln(omx), 2) * CF - 1. / 2. * ln(x) * pow(ln(omx), 2) * x * CF + ln(x) * Li2(x) * CF + ln(x) * Li2(x) * x * CF + 13. / 9. * ln(omx) * pow(x, -1) * CF - 11. / 6. * ln(omx) * CF + 1. / 6. * ln(omx) * pow(pi, 2) * CF + 17. / 6. * ln(omx) * x * CF + 1. / 6. * ln(omx) * x * pow(pi, 2) * CF - 22. / 9. * ln(omx) * pow(x, 2) * CF - 2. / 3. * ln(omx) * LMUF * pow(x, -1) * CF - 1. / 2. * ln(omx) * LMUF * CF + 1. / 2. * ln(omx) * LMUF * x * CF + 2. / 3. * ln(omx) * LMUF * pow(x, 2) * CF + 1. / 3. * pow(ln(omx), 2) * pow(x, -1) * CF + 1. / 4. * pow(ln(omx), 2) * CF;
    res += -1. / 4. * pow(ln(omx), 2) * x * CF - 1. / 3. * pow(ln(omx), 2) * pow(x, 2) * CF - ln(omx) * Li2(x) * CF -
           ln(omx) * Li2(x) * x * CF - Li3(1 - x) * CF - Li3(1 - x) * x * CF - 2. / 3. * Li2(x) * pow(x, -1) * CF - 3. / 2. * Li2(x) * CF - 5. / 2. * Li2(x) * x * CF - 4. / 3. * Li2(x) * pow(x, 2) * CF + Li2(x) * LMUF * CF + Li2(x) * LMUF * x * CF;

    return res;
  }
  if (cx == "R" && cz == "0")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    res = 13. / 9. * pow(x, -1) * CF - 11. / 6. * CF + 1. / 6. * pow(pi, 2) * CF + 17. / 6. * x * CF + 1. / 6. * x * pow(pi, 2) * CF - 22. / 9. * pow(x, 2) * CF - 2. / 3. * LMUF * pow(x, -1) * CF - 1. / 2. * LMUF * CF + 1. / 2. * LMUF * x * CF + 2. / 3. * LMUF * pow(x, 2) * CF + ln(x) * CF + 3 * ln(x) * x * CF + 2 * ln(x) * pow(x, 2) * CF - ln(x) * LMUF * CF - ln(x) * LMUF * x * CF - pow(ln(x), 2) * CF - pow(ln(x), 2) * x * CF + 2. / 3. * ln(omx) * pow(x, -1) * CF + 1. / 2. * ln(omx) * CF - 1. / 2. * ln(omx) * x * CF - 2. / 3. * ln(omx) * pow(x, 2) * CF - Li2(x) * CF - Li2(x) * x * CF;

    return res;
  }
  if (cx == "R" && cz == "1")
  {
    double x = inx;
    double omx = 1. - x;
    double opx = 1. + x;
    double op6xpxsq = 1. + 6. * x + x * x;
    res = 2. / 3. * pow(x, -1) * CF + 1. / 2. * CF - 1. / 2. * x * CF - 2. / 3. * pow(x, 2) * CF + ln(x) * CF + ln(x) * x * CF;

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
      tmp = 13. / 9. * pow(x, -1) * pow(z, -1) * CF - 26. / 9. * pow(x, -1) * CF - 11. / 6. * pow(z, -1) * CF + 1. / 6. * pow(z, -1) * pow(pi, 2) * CF - 7. / 3. * CF - 1. / 3. * pow(pi, 2) * CF + 10 * z * CF + 17. / 6. * x * pow(z, -1) * CF + 1. / 6. * x * pow(z, -1) * pow(pi, 2) * CF + 1. / 3. * x * CF - 1. / 3. * x * pow(pi, 2) * CF - 10 * x * z * CF - 22. / 9. * pow(x, 2) * pow(z, -1) * CF + 44. / 9. * pow(x, 2) * CF - 2. / 3. * LMUF * pow(x, -1) * pow(z, -1) * CF + 4. / 3. * LMUF * pow(x, -1) * CF - 1. / 2. * LMUF * pow(z, -1) * CF + LMUF * CF + 1. / 2. * LMUF * x * pow(z, -1) * CF - LMUF * x * CF + 2. / 3. * LMUF * pow(x, 2) * pow(z, -1) * CF - 4. / 3. * LMUF * pow(x, 2) * CF + 1. / 4. * ln(x) * pow(x, -1) * pow(poly2, -1) * CF - 1. / 4. * ln(x) * pow(x, -1) * CF + ln(x) * pow(z, -1) * CF - 1. / 4. * ln(x) * pow(poly2, -1) * CF - 19. / 4. * ln(x) * CF + 5 * ln(x) * z * CF + 3 * ln(x) * x * pow(z, -1) * CF - 35. / 4. * ln(x) * x * CF + 5 * ln(x) * x * z * CF + 2 * ln(x) * pow(x, 2) * pow(z, -1) * CF - 17. / 4. * ln(x) * pow(x, 2) * CF - 1. / 4. * ln(x) * pow(x, 3) * pow(poly2, -1) * CF + 1. / 4. * ln(x) * pow(x, 4) * pow(poly2, -1) * CF - ln(x) * LMUF * pow(z, -1) * CF + 2 * ln(x) * LMUF * CF - ln(x) * LMUF * x * pow(z, -1) * CF + 2 * ln(x) * LMUF * x * CF + 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(sqrtxz2, -1) * CF + 7. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF - 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF + 10 * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF - 10 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF;
      tmp += -7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF +
             1. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(sqrtxz2, -1) * CF - 7. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * z * pow(sqrtxz2, -1) * CF + 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(sqrtxz2, -1) * CF - 10 * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(sqrtxz2, -1) * CF + 10 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - pow(ln(x), 2) * pow(z, -1) * CF + 2 * pow(ln(x), 2) * CF - pow(ln(x), 2) * x * pow(z, -1) * CF + 2 * pow(ln(x), 2) * x * CF + ln(x) * ln(z) * pow(z, -1) * CF - ln(x) * ln(z) * CF + ln(x) * ln(z) * x * pow(z, -1) * CF - ln(x) * ln(z) * x * CF + ln(x) * ln(omz) * pow(z, -1) * CF;
      tmp += -2 * ln(x) * ln(omz) * CF + ln(x) * ln(omz) * x * pow(z, -1) * CF - 2 * ln(x) * ln(omz) * x * CF + 2. / 3. * ln(z) * pow(x, -1) * pow(z, -1) * CF + 1. / 4. * ln(z) * pow(x, -1) * pow(poly2, -1) * CF + 2. / 3. * ln(z) * pow(x, -1) * CF * pow(omz, -1) - 19. / 12. * ln(z) * pow(x, -1) * CF + 1. / 2. * ln(z) * pow(z, -1) * CF + 1. / 4. * ln(z) * pow(poly2, -1) * CF - ln(z) * CF * pow(omz, -1) - 5. / 4. * ln(z) * CF + 5 * ln(z) * z * CF - 1. / 2. * ln(z) * x * pow(z, -1) * CF + ln(z) * x * CF * pow(omz, -1) + 5. / 4. * ln(z) * x * CF - 5 * ln(z) * x * z * CF - 2. / 3. * ln(z) * pow(x, 2) * pow(z, -1) * CF - 2. / 3. * ln(z) * pow(x, 2) * CF * pow(omz, -1) + 19. / 12. * ln(z) * pow(x, 2) * CF - 1. / 4. * ln(z) * pow(x, 3) * pow(poly2, -1) * CF - 1. / 4. * ln(z) * pow(x, 4) * pow(poly2, -1) * CF + 2. / 3. * ln(omx) * pow(x, -1) * pow(z, -1) * CF - 4. / 3. * ln(omx) * pow(x, -1) * CF + 1. / 2. * ln(omx) * pow(z, -1) * CF - ln(omx) * CF - 1. / 2. * ln(omx) * x * pow(z, -1) * CF + ln(omx) * x * CF - 2. / 3. * ln(omx) * pow(x, 2) * pow(z, -1) * CF + 4. / 3. * ln(omx) * pow(x, 2) * CF + 2. / 3. * ln(omz) * pow(x, -1) * pow(z, -1) * CF - 4. / 3. * ln(omz) * pow(x, -1) * CF + 1. / 2. * ln(omz) * pow(z, -1) * CF - ln(omz) * CF - 1. / 2. * ln(omz) * x * pow(z, -1) * CF + ln(omz) * x * CF - 2. / 3. * ln(omz) * pow(x, 2) * pow(z, -1) * CF + 4. / 3. * ln(omz) * pow(x, 2) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF + 7. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF;
      tmp += -1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF + 10 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF - 10 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF - 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(sqrtxz2, -1) * CF - 7. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * z * pow(sqrtxz2, -1) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(sqrtxz2, -1) * CF;
      tmp += -10 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(sqrtxz2, -1) * CF +
             10 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF + 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(sqrtxz2, -1) * CF - 7. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * z * pow(sqrtxz2, -1) * CF + 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * CF - 10 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(sqrtxz2, -1) * CF + 10 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF + 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF - 7. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF;
      tmp += +1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) *
                 CF +
             1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF - 1. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF + 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, -1) * pow(sqrtxz2, -1) * CF - 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(sqrtxz2, -1) * CF + 7. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * z * pow(sqrtxz2, -1) * CF - 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(sqrtxz2, -1) * CF + 10 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(sqrtxz2, -1) * CF - 10 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, 2) * pow(sqrtxz2, -1) * CF -
             7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(sqrtxz2, -1) * CF + 7. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * z * pow(sqrtxz2, -1) * CF - 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(sqrtxz2, -1) * CF + 1. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 5) * pow(sqrtxz2, -1) * pow(poly2, -1) * CF - Li2(x) * pow(z, -1) * CF + 2 * Li2(x) * CF - Li2(x) * x * pow(z, -1) * CF + 2 * Li2(x) * x * CF;

      res += tmp;
    }
    return res;
  }
}