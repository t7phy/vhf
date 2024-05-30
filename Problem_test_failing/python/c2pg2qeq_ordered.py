from core.definitions import CF, NC, TR, NF, ZETA3, ZETA2
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi
def C2Pg2qEq(inx, inz, cx, cz, Q, muR, muF, muA, order):
      res = (0.0)

      rln2 = (ln(2.0))

      LMUR = (2 * ln(muR / Q))
      LMUF = (2 * ln(muF / Q))
      LMUA = (2 * ln(muA / Q))

      NC = (3.0)
      CF = (4.0 / 3.0)
      TR = (0.5)

      if cx == "R" and cz == "R":
      
            x = (inx)
            z = (inz)
            omz = (1. - z)
            opz = (1. + z)
            omx = (1. - x)
            opx = (1. + x)
            op6xpxsq = (1. + 6. * x + x * x)
            xmz = (x - z)
            omxmz = (1. - x - z)
            poly2 = (1 + 2 * x + x * x - 4 * x * z)
            sqrtxz1 = (sqrt(1 - 2 * z + z * z + 4 * x * z))
            sqrtxz2 = (sqrt(poly2))
            sqrtxz3 = (sqrt(x / z))

            if z != x and z != 1. - x:
            
                  tmp = (0.0)
                  # Split orders:
                  tmp = (0)
                  if (order == "000") or (order == "all"):

	                  tmp += ( +13. / 2. * ln(omz) * x * NC + 3. / 4. * ln(omz) * x * z * pow(NC, -1) + (-1) * 3. / 4. * ln(omz) * x * z * NC + 3. / 2. * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -2) + (-1) * 3. / 2. * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -1) + (-1) * 3. / 2. * ln(omz) * pow(x, 2) * NC * pow(omxmz, -2) + 3. / 2. * ln(omz) * pow(x, 2) * NC * pow(omxmz, -1) + (-1) * 1. / 2. * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(omxmz, -2) + 1. / 2. * ln(omz) * pow(x, 3) * NC * pow(omxmz, -2) + 5. / 2. * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1) + (-1) * 5. / 4. * pow(ln(omz), 2) * pow(z, -1) * NC + 3. / 2. * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1) + (-1) * 2 * pow(ln(omz), 2) * pow(NC, -1) + (-1) * pow(ln(omz), 2) * NC * pow(omz, -1) + 11. / 4. * pow(ln(omz), 2) * NC + (-1) * 1. / 4. * pow(ln(omz), 2) * z * pow(NC, -1) + 1. / 4. * pow(ln(omz), 2) * z * NC + (-1) * 5 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1) + 5. / 2. * pow(ln(omz), 2) * x * pow(z, -1) * NC + (-1) * 3 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1) + 4 * pow(ln(omz), 2) * x * pow(NC, -1) + 2 * pow(ln(omz), 2) * x * NC * pow(omz, -1) + (-1) * 11. / 2. * pow(ln(omz), 2) * x * NC + 1. / 2. * pow(ln(omz), 2) * x * z * pow(NC, -1) + (-1) * 1. / 2. * pow(ln(omz), 2) * x * z * NC + 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 1. / 2. * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + (-1) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * NC * pow(sqrtxz2, -1) + 0)
                  if (order == "010") or (order == "all"):

	                  tmp += ( (-1) * 1. / 2. * ln(omz) * x * LMUF * pow(NC, -1) + 1. / 2. * ln(omz) * x * LMUF * NC + (-1) * 1. / 2. * ln(omz) * x * z * LMUF * pow(NC, -1) + 1. / 2. * ln(omz) * x * z * LMUF * NC + 0)
                  if (order == "001") or (order == "all"):

	                  tmp += ( (-1) * 5. / 2. * ln(omz) * x * LMUA * pow(NC, -1) + 5. / 2. * ln(omz) * x * LMUA * NC + (-1) * 1. / 2. * ln(omz) * x * z * LMUA * pow(NC, -1) + 1. / 2. * ln(omz) * x * z * LMUA * NC + 0)

                  res += ( tmp)
            
            return res
      
