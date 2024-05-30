double C2Pg2qEq(double inx, double inz, std::string cx, std::string cz,
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

            if (z != x && z != 1. - x)
            {
                  double tmp = 0.0;
                  // Split orders:
                  tmp = 0;
                  // Order 000:
                  tmp += +13. / 2. * ln(omz) * x * NC + 3. / 4. * ln(omz) * x * z * pow(NC, -1) + (-1) * 3. / 4. * ln(omz) * x * z * NC + 3. / 2. * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -2) + (-1) * 3. / 2. * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -1) + (-1) * 3. / 2. * ln(omz) * pow(x, 2) * NC * pow(omxmz, -2) + 3. / 2. * ln(omz) * pow(x, 2) * NC * pow(omxmz, -1) + (-1) * 1. / 2. * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(omxmz, -2) + 1. / 2. * ln(omz) * pow(x, 3) * NC * pow(omxmz, -2) + 5. / 2. * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1) + (-1) * 5. / 4. * pow(ln(omz), 2) * pow(z, -1) * NC + 3. / 2. * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1) + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) + (-1) * pow(ln(omz), 2) * NC * pow(omz, -1) + 11. / 4. * pow(ln(omz), 2) * NC + (-1) * 1. / 4. * pow(ln(omz), 2) * z * pow(NC, -1) + 1. / 4. * pow(ln(omz), 2) * z * NC + (-1) * 5 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1) + 5. / 2. * pow(ln(omz), 2) * x * pow(z, -1) * NC + (-1) * 3 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1) + 4 * pow(ln(omz), 2) * x * pow(NC, -1) + 2 * pow(ln(omz), 2) * x * NC * pow(omz, -1) + (-1) * 11. / 2. * pow(ln(omz), 2) * x * NC + 1. / 2. * pow(ln(omz), 2) * x * z * pow(NC, -1) + (-1) * 1. / 2. * pow(ln(omz), 2) * x * z * NC + 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 1. / 2. * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + (-1) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * NC * pow(sqrtxz2, -1) + 0;
                  // Order 010:
                  tmp += (-1) * 1. / 2. * ln(omz) * x * LMUF * pow(NC, -1) + 1. / 2. * ln(omz) * x * LMUF * NC + (-1) * 1. / 2. * ln(omz) * x * z * LMUF * pow(NC, -1) + 1. / 2. * ln(omz) * x * z * LMUF * NC + 0;
                  // Order 001:
                  tmp += (-1) * 5. / 2. * ln(omz) * x * LMUA * pow(NC, -1) + 5. / 2. * ln(omz) * x * LMUA * NC + (-1) * 1. / 2. * ln(omz) * x * z * LMUA * pow(NC, -1) + 1. / 2. * ln(omz) * x * z * LMUA * NC + 0;

                  res += tmp;
            }
            return res;
      }
}