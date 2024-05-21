from configs.eh import CF, NC, NF, TR, Li2, Li3
from configs.eh import ln2 as rln2
from configs.eh import atanint as InvTanInt
from configs.eh import ZETA2 as zeta2
from configs.eh import ZETA3 as zeta3
from numpy import sqrt, pi
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan

LMUR = 1
LMUF = 1
LMUA = 1

def ct_nnlo_g2q_eq(x, z, rsl, orders):

    omz = 1.-z
    opz = 1.+z
    omx = 1.-x
    opx = 1.+x
    op6xpxsq = 1.+6.*x+x*x
    xmz = x-z
    omxmz = 1.-x-z
    poly2 = 1 + 2*x + x*x - 4*x*z
    sqrtxz1 = sqrt(1 - 2*z + z*z + 4*x*z)
    sqrtxz2 = sqrt(poly2)
    sqrtxz3 = sqrt(x/z)

    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != 1.-x:
                result += - 1./16.*pow(NC,-1)*pow(x,-1)*pow(poly2,-1) + 1./16.*pow(NC,-1)*pow(x,-1) - 2*pow(NC,-1)\
      *pow(z,-1)*pow(omz,-1) + 9./16.*pow(NC,-1)*pow(z,-1) + 3./4.*pow(NC,-1)*pow(z,-1)*pow(pi,2)\
       + 1./16.*pow(NC,-1)*pow(poly2,-1) + 1./2.*pow(NC,-1)*pow(omz,-1) - 1./4.*pow(NC,-1)*pow(\
      omxmz,-1) - 21./16.*pow(NC,-1) + 3./4.*pow(NC,-1)*pow(pi,2)*pow(omz,-1) - 5./12.*pow(NC,-1)*\
      pow(pi,2) + 7./16.*pow(NC,-1)*z - 1./12.*pow(NC,-1)*z*pow(pi,2) + 4*pow(NC,-1)*x*pow(z,-1)*\
      pow(omz,-1) - 3*pow(NC,-1)*x*pow(z,-1) - 13./6.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2) - 4*pow(\
      NC,-1)*x*pow(omz,-1) + 3./4.*pow(NC,-1)*x*pow(omxmz,-1) - 7./16.*pow(NC,-1)*x - 3./2.*pow(\
      NC,-1)*x*pow(pi,2)*pow(omz,-1) + 5./3.*pow(NC,-1)*x*pow(pi,2) + pow(NC,-1)*x*z - 1./3.*pow(\
      NC,-1)*x*z*pow(pi,2) - 2*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + 11./4.*pow(NC,-1)*pow(\
      x,2)*pow(z,-1) + pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(pi,2) + 3*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       - pow(NC,-1)*pow(x,2)*pow(omxmz,-1) - 7./16.*pow(NC,-1)*pow(x,2) + pow(NC,-1)*pow(x,2)*pow(\
      pi,2)*pow(omz,-1) - 4./3.*pow(NC,-1)*pow(x,2)*pow(pi,2) - 3./2.*pow(NC,-1)*pow(x,2)*z - 1./6.\
      *pow(NC,-1)*pow(x,2)*z*pow(pi,2) + 1./16.*pow(NC,-1)*pow(x,3)*pow(poly2,-1) + 1./2.*pow(\
      NC,-1)*pow(x,3)*pow(omxmz,-1) - 1./16.*pow(NC,-1)*pow(x,4)*pow(poly2,-1) + 13./9.*NC*pow(\
      x,-1)*pow(z,-1) + 1./16.*NC*pow(x,-1)*pow(poly2,-1) - 425./144.*NC*pow(x,-1) + 2*NC*pow(z,-1)\
      *pow(omz,-1)
                result +=  - 199./48.*NC*pow(z,-1) - 1./3.*NC*pow(z,-1)*pow(pi,2)*pow(omz,-1) + 1./6.*NC*pow(\
      z,-1)*pow(pi,2) - 1./16.*NC*pow(poly2,-1) - 2*NC*pow(omz,-1) + 1./4.*NC*pow(omxmz,-1) + 71./\
      48.*NC + 1./6.*NC*pow(pi,2)*pow(omz,-1) + 1./4.*NC*pow(pi,2) + 153./16.*NC*z + 1./12.*NC*z*\
      pow(pi,2) - 4*NC*x*pow(z,-1)*pow(omz,-1) + 28./3.*NC*x*pow(z,-1) + 2./3.*NC*x*pow(z,-1)*pow(\
      pi,2)*pow(omz,-1) + 2./3.*NC*x*pow(z,-1)*pow(pi,2) + 4*NC*x*pow(omz,-1) - 3./4.*NC*x*pow(\
      omxmz,-1) - 155./48.*NC*x - 1./3.*NC*x*pow(pi,2)*pow(omz,-1) - 3*NC*x*pow(pi,2) - 11*NC*x*z\
       + 1./3.*NC*x*z*pow(pi,2) + 4*NC*pow(x,2)*pow(z,-1)*pow(omz,-1) - 161./18.*NC*pow(x,2)*pow(\
      z,-1) - 2./3.*NC*pow(x,2)*pow(z,-1)*pow(pi,2)*pow(omz,-1) - 4*NC*pow(x,2)*pow(omz,-1) + NC*\
      pow(x,2)*pow(omxmz,-1) + 1127./144.*NC*pow(x,2) + 1./3.*NC*pow(x,2)*pow(pi,2)*pow(omz,-1) + 5.\
      /3.*NC*pow(x,2)*pow(pi,2) + 3./2.*NC*pow(x,2)*z + 1./6.*NC*pow(x,2)*z*pow(pi,2) - 1./16.*NC*\
      pow(x,3)*pow(poly2,-1) - 1./2.*NC*pow(x,3)*pow(omxmz,-1) + 1./16.*NC*pow(x,4)*pow(poly2,-1)
                result +=   - 3./32.*ln(x)*pow(NC,-1)*pow(x,-1)*pow(poly2,-2) + 5./32.*ln(x)*pow(NC,-1)*pow(x,-1)*pow(poly2,-1) - \
      1./16.*ln(x)*pow(NC,-1)*pow(x,-1) + 8*ln(x)*pow(NC,-1)*pow(z,-1)*pow(omz,-1) - 53./8.*ln(x)*\
      pow(NC,-1)*pow(z,-1) + 3./32.*ln(x)*pow(NC,-1)*pow(poly2,-2) - 3./32.*ln(x)*pow(NC,-1)*pow(\
      poly2,-1) - 13./2.*ln(x)*pow(NC,-1)*pow(omz,-1) + 3./4.*ln(x)*pow(NC,-1)*pow(omxmz,-1) - 53./\
      16.*ln(x)*pow(NC,-1)
                result +=  + 3./8.*ln(x)*pow(NC,-1)*z - 16*ln(x)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + 69./4.*ln(\
      x)*pow(NC,-1)*x*pow(z,-1) + 3./32.*ln(x)*pow(NC,-1)*x*pow(poly2,-2) - 15./16.*ln(x)*pow(\
      NC,-1)*x*pow(poly2,-1) + 16*ln(x)*pow(NC,-1)*x*pow(omz,-1) + 1./2.*ln(x)*pow(NC,-1)*x*pow(\
      xmz,-1) - 1./4.*ln(x)*pow(NC,-1)*x*pow(omxmz,-2) - 3./2.*ln(x)*pow(NC,-1)*x*pow(omxmz,-1) - 1.\
      /2.*ln(x)*pow(NC,-1)*x + 1./8.*ln(x)*pow(NC,-1)*x*z + 1./2.*ln(x)*pow(NC,-1)*x*pow(z,3)*pow(\
      xmz,-2) + 8*ln(x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) - 13./2.*ln(x)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1) - 3./32.*ln(x)*pow(NC,-1)*pow(x,2)*pow(poly2,-2) + 15./16.*ln(x)*pow(NC,-1)*\
      pow(x,2)*pow(poly2,-1) - 5*ln(x)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*pow(NC,-1)*pow(x,2)*\
      pow(xmz,-1) + 3./4.*ln(x)*pow(NC,-1)*pow(x,2)*pow(omxmz,-2) + 1./2.*ln(x)*pow(NC,-1)*pow(x,2)\
      *pow(omxmz,-1) + 1./2.*ln(x)*pow(NC,-1)*pow(x,2) - 1./2.*ln(x)*pow(NC,-1)*pow(x,2)*z + 3./32.\
      *ln(x)*pow(NC,-1)*pow(x,3)*pow(poly2,-2) + 9./32.*ln(x)*pow(NC,-1)*pow(x,3)*pow(poly2,-1) + 5.\
      /2.*ln(x)*pow(NC,-1)*pow(x,3)*pow(xmz,-1) - ln(x)*pow(NC,-1)*pow(x,3)*pow(omxmz,-2) - 3./32.*\
      ln(x)*pow(NC,-1)*pow(x,4)*pow(poly2,-2) - 11./32.*ln(x)*pow(NC,-1)*pow(x,4)*pow(poly2,-1) - 1.\
      /2.*ln(x)*pow(NC,-1)*pow(x,4)*pow(xmz,-2) + 1./2.*ln(x)*pow(NC,-1)*pow(x,4)*pow(omxmz,-2) - 3.\
      /32.*ln(x)*pow(NC,-1)*pow(x,5)*pow(poly2,-2) + 3./32.*ln(x)*pow(NC,-1)*pow(x,6)*pow(poly2,-2)\
       + 3./32.*ln(x)*NC*pow(x,-1)*pow(poly2,-2)
                result +=  + 3./32.*ln(x)*NC*pow(x,-1)*pow(poly2,-1) - 3./16.*ln(x)*NC*pow(x,-1) - 8*ln(x)*NC*\
      pow(z,-1)*pow(omz,-1) + 61./8.*ln(x)*NC*pow(z,-1) - 3./32.*ln(x)*NC*pow(poly2,-2) - 5./32.*\
      ln(x)*NC*pow(poly2,-1) + 13./2.*ln(x)*NC*pow(omz,-1) - 3./4.*ln(x)*NC*pow(omxmz,-1) + 1./16.*\
      ln(x)*NC + 37./8.*ln(x)*NC*z + 16*ln(x)*NC*x*pow(z,-1)*pow(omz,-1) - 69./4.*ln(x)*NC*x*pow(\
      z,-1) - 3./32.*ln(x)*NC*x*pow(poly2,-2) + 23./16.*ln(x)*NC*x*pow(poly2,-1) - 16*ln(x)*NC*x*\
      pow(omz,-1) + 1./4.*ln(x)*NC*x*pow(omxmz,-2) + 2*ln(x)*NC*x*pow(omxmz,-1) + 19./4.*ln(x)*NC*x\
       + 39./8.*ln(x)*NC*x*z - 1./2.*ln(x)*NC*x*pow(z,3)*pow(xmz,-2) - 16*ln(x)*NC*pow(x,2)*pow(\
      z,-1)*pow(omz,-1) + 30*ln(x)*NC*pow(x,2)*pow(z,-1) + 3./32.*ln(x)*NC*pow(x,2)*pow(poly2,-2)\
       - 23./16.*ln(x)*NC*pow(x,2)*pow(poly2,-1) + 16*ln(x)*NC*pow(x,2)*pow(omz,-1) - 3./4.*ln(x)*\
      NC*pow(x,2)*pow(omxmz,-2) - 3./2.*ln(x)*NC*pow(x,2)*pow(omxmz,-1) - 129./4.*ln(x)*NC*pow(x,2)\
       + 1./2.*ln(x)*NC*pow(x,2)*z - 3./32.*ln(x)*NC*pow(x,3)*pow(poly2,-2) - 1./32.*ln(x)*NC*pow(\
      x,3)*pow(poly2,-1) - 3./2.*ln(x)*NC*pow(x,3)*pow(xmz,-1) + ln(x)*NC*pow(x,3)*pow(omxmz,-2) + \
      ln(x)*NC*pow(x,3)*pow(omxmz,-1) + 3./32.*ln(x)*NC*pow(x,4)*pow(poly2,-2) + 3./32.*ln(x)*NC*\
      pow(x,4)*pow(poly2,-1) + 1./2.*ln(x)*NC*pow(x,4)*pow(xmz,-2) - 1./2.*ln(x)*NC*pow(x,4)*pow(\
      omxmz,-2) + 3./32.*ln(x)*NC*pow(x,5)*pow(poly2,-2) - 3./32.*ln(x)*NC*pow(x,6)*pow(poly2,-2)
                result +=   - 3./64.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,-1)*pow(\
      sqrtxz2,-1)*pow(poly2,-2) + 3./32.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,-1)*pow(\
      sqrtxz2,-1)*pow(poly2,-1) - 3./64.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,-1)*pow(\
      sqrtxz2,-1) - ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1) + ln(x)*ln(1 - \
      sqrtxz2 + x)*pow(NC,-1)*pow(sqrtxz2,-1)*pow(omz,-1) + 1./2.*ln(x)*ln(1 - sqrtxz2 + x)*pow(\
      NC,-1)*pow(sqrtxz2,-1) - ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*z*pow(sqrtxz2,-1) - 3*ln(x)*ln(\
      1 - sqrtxz2 + x)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1) + 3./32.*ln(x)*ln(1 - sqrtxz2 + x)*\
      pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(poly2,-2)
                result +=  - 1./2.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(poly2,-1) - 3*ln(x\
      )*ln(1 - sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(omz,-1) + 259./32.*ln(x)*ln(1 - \
      sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1) - 11./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*x*z*\
      pow(sqrtxz2,-1) + 11./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1) - 3*\
      ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1) + 3*ln(x)*ln(1 - \
      sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) + 29./16.*ln(x)*ln(1 - sqrtxz2\
       + x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1) - 29./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(\
      x,2)*z*pow(sqrtxz2,-1) - ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(z,-1)*pow(\
      sqrtxz2,-1) + 19./32.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(\
      poly2,-1) - ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(omz,-1) + 73./\
      64.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1) - 3./32.*ln(x)*ln(1 - \
      sqrtxz2 + x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) - 3./16.*ln(x)*ln(1 - sqrtxz2\
       + x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./64.*ln(x)*ln(1 - sqrtxz2 + x)*\
      pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2) + 3./64.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(\
      x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2) + 1./32.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,-1)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)
                result +=  - 5./64.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,-1)*pow(sqrtxz2,-1) + 1./2.*ln(x)*ln(1 - \
      sqrtxz2 + x)*NC*pow(z,-1)*pow(sqrtxz2,-1) - 1./2.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(\
      sqrtxz2,-1)*pow(omz,-1) - 9./4.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(sqrtxz2,-1) + 9./2.*ln(x)*\
      ln(1 - sqrtxz2 + x)*NC*z*pow(sqrtxz2,-1) + 3./2.*ln(x)*ln(1 - sqrtxz2 + x)*NC*x*pow(z,-1)*\
      pow(sqrtxz2,-1) - 3./32.*ln(x)*ln(1 - sqrtxz2 + x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-2) + 5./8.\
      *ln(x)*ln(1 - sqrtxz2 + x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./2.*ln(x)*ln(1 - sqrtxz2 + \
      x)*NC*x*pow(sqrtxz2,-1)*pow(omz,-1) - 211./32.*ln(x)*ln(1 - sqrtxz2 + x)*NC*x*pow(sqrtxz2,-1)\
       + 51./4.*ln(x)*ln(1 - sqrtxz2 + x)*NC*x*z*pow(sqrtxz2,-1) - 51./4.*ln(x)*ln(1 - sqrtxz2 + x)\
      *NC*x*pow(z,2)*pow(sqrtxz2,-1) + 2*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,2)*pow(z,-1)*pow(\
      sqrtxz2,-1) - 2*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) - 129./16.*\
      ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,2)*pow(sqrtxz2,-1) + 129./8.*ln(x)*ln(1 - sqrtxz2 + x)*NC*\
      pow(x,2)*z*pow(sqrtxz2,-1) + ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1)\
       - 23./32.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1) + ln(x)*ln(1\
       - sqrtxz2 + x)*NC*pow(x,3)*pow(sqrtxz2,-1)*pow(omz,-1) - 193./64.*ln(x)*ln(1 - sqrtxz2 + x)*\
      NC*pow(x,3)*pow(sqrtxz2,-1) + 3./32.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,5)*pow(sqrtxz2,-1)*\
      pow(poly2,-2)
                result +=  + 1./16.*ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) - 3./64.\
      *ln(x)*ln(1 - sqrtxz2 + x)*NC*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2) + 3./64.*ln(x)*ln(1 + \
      sqrtxz2 + x)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2) - 3./32.*ln(x)*ln(1 + sqrtxz2\
       + x)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./64.*ln(x)*ln(1 + sqrtxz2 + x)*\
      pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1) + ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(z,-1)*pow(\
      sqrtxz2,-1) - ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(sqrtxz2,-1)*pow(omz,-1) - 1./2.*ln(x)*\
      ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(sqrtxz2,-1) + ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*z*pow(\
      sqrtxz2,-1) + 3*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1) - 3./32.*ln(\
      x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(poly2,-2) + 1./2.*ln(x)*ln(1 + \
      sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(poly2,-1) + 3*ln(x)*ln(1 + sqrtxz2 + x)*pow(\
      NC,-1)*x*pow(sqrtxz2,-1)*pow(omz,-1) - 259./32.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*pow(\
      sqrtxz2,-1) + 11./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*z*pow(sqrtxz2,-1) - 11./4.*ln(x)*\
      ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1) + 3*ln(x)*ln(1 + sqrtxz2 + x)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1) - 3*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*\
      pow(sqrtxz2,-1)*pow(omz,-1) - 29./16.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz2,-1)
                result +=  + 29./8.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz2,-1) + ln(x)*ln(1\
       + sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1) - 19./32.*ln(x)*ln(1 + sqrtxz2\
       + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1) + ln(x)*ln(1 + sqrtxz2 + x)*pow(\
      NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(omz,-1) - 73./64.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*\
      pow(x,3)*pow(sqrtxz2,-1) + 3./32.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,5)*pow(\
      sqrtxz2,-1)*pow(poly2,-2) + 3./16.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,5)*pow(\
      sqrtxz2,-1)*pow(poly2,-1) - 3./64.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,7)*pow(\
      sqrtxz2,-1)*pow(poly2,-2) - 3./64.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,-1)*pow(sqrtxz2,-1)*\
      pow(poly2,-2) - 1./32.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)\
       + 5./64.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,-1)*pow(sqrtxz2,-1) - 1./2.*ln(x)*ln(1 + sqrtxz2\
       + x)*NC*pow(z,-1)*pow(sqrtxz2,-1) + 1./2.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(sqrtxz2,-1)*pow(\
      omz,-1) + 9./4.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(sqrtxz2,-1) - 9./2.*ln(x)*ln(1 + sqrtxz2 + x\
      )*NC*z*pow(sqrtxz2,-1) - 3./2.*ln(x)*ln(1 + sqrtxz2 + x)*NC*x*pow(z,-1)*pow(sqrtxz2,-1) + 3./\
      32.*ln(x)*ln(1 + sqrtxz2 + x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-2) - 5./8.*ln(x)*ln(1 + sqrtxz2\
       + x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-1) - 3./2.*ln(x)*ln(1 + sqrtxz2 + x)*NC*x*pow(\
      sqrtxz2,-1)*pow(omz,-1)
                result +=  + 211./32.*ln(x)*ln(1 + sqrtxz2 + x)*NC*x*pow(sqrtxz2,-1) - 51./4.*ln(x)*ln(1 + \
      sqrtxz2 + x)*NC*x*z*pow(sqrtxz2,-1) + 51./4.*ln(x)*ln(1 + sqrtxz2 + x)*NC*x*pow(z,2)*pow(\
      sqrtxz2,-1) - 2*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1) + 2*ln(x)*ln(\
      1 + sqrtxz2 + x)*NC*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) + 129./16.*ln(x)*ln(1 + sqrtxz2 + x)\
      *NC*pow(x,2)*pow(sqrtxz2,-1) - 129./8.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,2)*z*pow(\
      sqrtxz2,-1) - ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1) + 23./32.*ln(x)\
      *ln(1 + sqrtxz2 + x)*NC*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1) - ln(x)*ln(1 + sqrtxz2 + x)*NC\
      *pow(x,3)*pow(sqrtxz2,-1)*pow(omz,-1) + 193./64.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,3)*pow(\
      sqrtxz2,-1) - 3./32.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) - 1./\
      16.*ln(x)*ln(1 + sqrtxz2 + x)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./64.*ln(x)*ln(1\
       + sqrtxz2 + x)*NC*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2) - 2*ln(x)*ln(1 + x)*pow(NC,-1)*pow(\
      z,-1) + 2*ln(x)*ln(1 + x)*pow(NC,-1) - ln(x)*ln(1 + x)*pow(NC,-1)*z - 4*ln(x)*ln(1 + x)*pow(\
      NC,-1)*x*pow(z,-1) + 4*ln(x)*ln(1 + x)*pow(NC,-1)*x - 2*ln(x)*ln(1 + x)*pow(NC,-1)*x*z - 2*\
      ln(x)*ln(1 + x)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(x)*ln(1 + x)*pow(NC,-1)*pow(x,2) - 2*ln(\
      x)*ln(1 + x)*pow(NC,-1)*pow(x,2)*z - ln(x)*ln(1 + x)*NC + ln(x)*ln(1 + x)*NC*z - 2*ln(x)*ln(1\
       + x)*NC*x
                result +=  + 2*ln(x)*ln(1 + x)*NC*x*z + 2*ln(x)*ln(1 + x)*NC*pow(x,2)*z - 3*pow(ln(x),2)*pow(\
      NC,-1)*pow(z,-1)*pow(omz,-1) - 7./4.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1) - 3*pow(ln(x),2)*pow(\
      NC,-1)*pow(omz,-1) + 13./4.*pow(ln(x),2)*pow(NC,-1) + pow(ln(x),2)*pow(NC,-1)*z + 6*pow(ln(x)\
      ,2)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + 11./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1) + 6*pow(\
      ln(x),2)*pow(NC,-1)*x*pow(omz,-1) - 19./2.*pow(ln(x),2)*pow(NC,-1)*x - 3*pow(ln(x),2)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) - 7./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 5*\
      pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 7*pow(ln(x),2)*pow(NC,-1)*pow(x,2) + 2*pow(ln(\
      x),2)*pow(NC,-1)*pow(x,2)*z + 5./2.*pow(ln(x),2)*NC*pow(z,-1)*pow(omz,-1) - 2*pow(ln(x),2)*NC\
      *pow(z,-1) - 1./4.*pow(ln(x),2)*NC*pow(omz,-1) - 5./4.*pow(ln(x),2)*NC - pow(ln(x),2)*NC*z - \
      5*pow(ln(x),2)*NC*x*pow(z,-1)*pow(omz,-1) - 2*pow(ln(x),2)*NC*x*pow(z,-1) + 1./2.*pow(ln(x),2\
      )*NC*x*pow(omz,-1) + 33./2.*pow(ln(x),2)*NC*x + 5*pow(ln(x),2)*NC*pow(x,2)*pow(z,-1)*pow(\
      omz,-1) - 2*pow(ln(x),2)*NC*pow(x,2)*pow(z,-1) - 1./2.*pow(ln(x),2)*NC*pow(x,2)*pow(omz,-1)\
       - 7*pow(ln(x),2)*NC*pow(x,2) - 2*pow(ln(x),2)*NC*pow(x,2)*z + 2*ln(x)*ln(z)*pow(NC,-1)*pow(\
      z,-1)*pow(omz,-1) + 17./4.*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1) + 4*ln(x)*ln(z)*pow(NC,-1)*pow(\
      omz,-1) - 9./2.*ln(x)*ln(z)*pow(NC,-1) - 4*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) - 9.\
      /2.*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)
                result +=  - 8*ln(x)*ln(z)*pow(NC,-1)*x*pow(omz,-1) + 5*ln(x)*ln(z)*pow(NC,-1)*x + ln(x)*ln(z)*\
      pow(NC,-1)*x*z + 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + 6*ln(x)*ln(z)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) + 6*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7*ln(x)*ln(z)*\
      pow(NC,-1)*pow(x,2) - 3*ln(x)*ln(z)*NC*pow(z,-1)*pow(omz,-1) + 5./4.*ln(x)*ln(z)*NC*pow(z,-1)\
       + 1./2.*ln(x)*ln(z)*NC*pow(omz,-1) + 9./2.*ln(x)*ln(z)*NC + 6*ln(x)*ln(z)*NC*x*pow(z,-1)*\
      pow(omz,-1) + 3./2.*ln(x)*ln(z)*NC*x*pow(z,-1) + ln(x)*ln(z)*NC*x*pow(omz,-1) - 11*ln(x)*ln(z\
      )*NC*x - ln(x)*ln(z)*NC*x*z - 6*ln(x)*ln(z)*NC*pow(x,2)*pow(z,-1)*pow(omz,-1) + ln(x)*ln(z)*\
      NC*pow(x,2)*pow(z,-1) + ln(x)*ln(z)*NC*pow(x,2)*pow(omz,-1) + 9*ln(x)*ln(z)*NC*pow(x,2) + 8*\
      ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1) + 19./2.*ln(x)*ln(omx)*pow(NC,-1)*pow(omz,-1) - 13./2.*ln(\
      x)*ln(omx)*pow(NC,-1) - ln(x)*ln(omx)*pow(NC,-1)*z - 16*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)\
       - 19*ln(x)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) + 13*ln(x)*ln(omx)*pow(NC,-1)*x + 2*ln(x)*ln(omx\
      )*pow(NC,-1)*x*z + 11*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 12*ln(x)*ln(omx)*pow(\
      NC,-1)*pow(x,2)*pow(omz,-1) - 12*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2) - 2*ln(x)*ln(omx)*pow(\
      NC,-1)*pow(x,2)*z + 2*ln(x)*ln(omx)*NC*pow(z,-1)*pow(omz,-1) - 4*ln(x)*ln(omx)*NC*pow(z,-1)\
       - 7./2.*ln(x)*ln(omx)*NC*pow(omz,-1) + 11./2.*ln(x)*ln(omx)*NC + ln(x)*ln(omx)*NC*z - 4*ln(x\
      )*ln(omx)*NC*x*pow(z,-1)*pow(omz,-1)
                result +=  + 8*ln(x)*ln(omx)*NC*x*pow(z,-1) + 7*ln(x)*ln(omx)*NC*x*pow(omz,-1) - 11*ln(x)*ln(omx\
      )*NC*x - 2*ln(x)*ln(omx)*NC*x*z + 4*ln(x)*ln(omx)*NC*pow(x,2)*pow(z,-1)*pow(omz,-1) - 8*ln(x)\
      *ln(omx)*NC*pow(x,2)*pow(z,-1) - 7*ln(x)*ln(omx)*NC*pow(x,2)*pow(omz,-1) + 10*ln(x)*ln(omx)*\
      NC*pow(x,2) + 2*ln(x)*ln(omx)*NC*pow(x,2)*z + 7*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1) + 6*ln(x)*\
      ln(omz)*pow(NC,-1)*pow(omz,-1) - 5*ln(x)*ln(omz)*pow(NC,-1) - 1./2.*ln(x)*ln(omz)*pow(NC,-1)*\
      z - 14*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 12*ln(x)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) + 11*\
      ln(x)*ln(omz)*pow(NC,-1)*x + 9*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 9*ln(x)*ln(omz)*\
      pow(NC,-1)*pow(x,2)*pow(omz,-1) - 11*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2) - ln(x)*ln(omz)*pow(\
      NC,-1)*pow(x,2)*z - 2*ln(x)*ln(omz)*NC*pow(z,-1) - 3*ln(x)*ln(omz)*NC*pow(omz,-1) + 4*ln(x)*\
      ln(omz)*NC + 1./2.*ln(x)*ln(omz)*NC*z + 10*ln(x)*ln(omz)*NC*x*pow(z,-1) + 6*ln(x)*ln(omz)*NC*\
      x*pow(omz,-1) - 21*ln(x)*ln(omz)*NC*x - 6*ln(x)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 6*ln(x)*ln(\
      omz)*NC*pow(x,2)*pow(omz,-1) + 13*ln(x)*ln(omz)*NC*pow(x,2) + ln(x)*ln(omz)*NC*pow(x,2)*z - 3.\
      /32.*ln(z)*pow(NC,-1)*pow(x,-1)*pow(poly2,-2) + 5./32.*ln(z)*pow(NC,-1)*pow(x,-1)*pow(\
      poly2,-1) - 1./16.*ln(z)*pow(NC,-1)*pow(x,-1) - 4*ln(z)*pow(NC,-1)*pow(z,-1)*pow(omz,-1) + 23.\
      /8.*ln(z)*pow(NC,-1)*pow(z,-1) - 3./32.*ln(z)*pow(NC,-1)*pow(poly2,-2) + 3./32.*ln(z)*pow(\
      NC,-1)*pow(poly2,-1)
                result +=  + 7./2.*ln(z)*pow(NC,-1)*pow(omz,-1) + 27./16.*ln(z)*pow(NC,-1) - 3./4.*ln(z)*pow(\
      NC,-1)*z + 8*ln(z)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) - 15./2.*ln(z)*pow(NC,-1)*x*pow(z,-1)\
       + 3./32.*ln(z)*pow(NC,-1)*x*pow(poly2,-2) - 15./16.*ln(z)*pow(NC,-1)*x*pow(poly2,-1) - 9*ln(\
      z)*pow(NC,-1)*x*pow(omz,-1) - 1./2.*ln(z)*pow(NC,-1)*x*pow(xmz,-1) - 11./8.*ln(z)*pow(NC,-1)*\
      x + 17./8.*ln(z)*pow(NC,-1)*x*z - 1./2.*ln(z)*pow(NC,-1)*x*pow(z,3)*pow(xmz,-2) - 4*ln(z)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + 3*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 3./32.*\
      ln(z)*pow(NC,-1)*pow(x,2)*pow(poly2,-2) - 15./16.*ln(z)*pow(NC,-1)*pow(x,2)*pow(poly2,-1) + 3\
      *ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + ln(z)*pow(NC,-1)*pow(x,2)*pow(xmz,-1) + 11./4.*ln(z)\
      *pow(NC,-1)*pow(x,2) - ln(z)*pow(NC,-1)*pow(x,2)*z + 3./32.*ln(z)*pow(NC,-1)*pow(x,3)*pow(\
      poly2,-2) + 9./32.*ln(z)*pow(NC,-1)*pow(x,3)*pow(poly2,-1) - 5./2.*ln(z)*pow(NC,-1)*pow(x,3)*\
      pow(xmz,-1) + 3./32.*ln(z)*pow(NC,-1)*pow(x,4)*pow(poly2,-2) + 11./32.*ln(z)*pow(NC,-1)*pow(\
      x,4)*pow(poly2,-1) + 1./2.*ln(z)*pow(NC,-1)*pow(x,4)*pow(xmz,-2) - 3./32.*ln(z)*pow(NC,-1)*\
      pow(x,5)*pow(poly2,-2) - 3./32.*ln(z)*pow(NC,-1)*pow(x,6)*pow(poly2,-2) + 2./3.*ln(z)*NC*pow(\
      x,-1)*pow(z,-1) + 3./32.*ln(z)*NC*pow(x,-1)*pow(poly2,-2) + 3./32.*ln(z)*NC*pow(x,-1)*pow(\
      poly2,-1) + 2./3.*ln(z)*NC*pow(x,-1)*pow(omz,-1) - 73./48.*ln(z)*NC*pow(x,-1) + 4*ln(z)*NC*\
      pow(z,-1)*pow(omz,-1)
                result +=  - 19./8.*ln(z)*NC*pow(z,-1) + 3./32.*ln(z)*NC*pow(poly2,-2) + 5./32.*ln(z)*NC*pow(\
      poly2,-1) - 4*ln(z)*NC*pow(omz,-1) - 63./16.*ln(z)*NC + 23./4.*ln(z)*NC*z - 8*ln(z)*NC*x*pow(\
      z,-1)*pow(omz,-1) + 23./2.*ln(z)*NC*x*pow(z,-1) - 3./32.*ln(z)*NC*x*pow(poly2,-2) + 23./16.*\
      ln(z)*NC*x*pow(poly2,-1) + 13*ln(z)*NC*x*pow(omz,-1) - 91./8.*ln(z)*NC*x - 57./8.*ln(z)*NC*x*\
      z + 1./2.*ln(z)*NC*x*pow(z,3)*pow(xmz,-2) + 8*ln(z)*NC*pow(x,2)*pow(z,-1)*pow(omz,-1) - 79./6.\
      *ln(z)*NC*pow(x,2)*pow(z,-1) - 3./32.*ln(z)*NC*pow(x,2)*pow(poly2,-2) + 23./16.*ln(z)*NC*pow(\
      x,2)*pow(poly2,-1) - 38./3.*ln(z)*NC*pow(x,2)*pow(omz,-1) + 77./6.*ln(z)*NC*pow(x,2) + ln(z)*\
      NC*pow(x,2)*z - 3./32.*ln(z)*NC*pow(x,3)*pow(poly2,-2) - 1./32.*ln(z)*NC*pow(x,3)*pow(\
      poly2,-1) + 3./2.*ln(z)*NC*pow(x,3)*pow(xmz,-1) - 3./32.*ln(z)*NC*pow(x,4)*pow(poly2,-2) - 3./\
      32.*ln(z)*NC*pow(x,4)*pow(poly2,-1) - 1./2.*ln(z)*NC*pow(x,4)*pow(xmz,-2) + 3./32.*ln(z)*NC*\
      pow(x,5)*pow(poly2,-2) + 3./32.*ln(z)*NC*pow(x,6)*pow(poly2,-2)
                result +=   - 5./4.*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)\
       - pow(ln(z),2)*pow(NC,-1)*pow(omz,-1) + 1./4.*pow(ln(z),2)*pow(NC,-1) - 1./4.*pow(ln(z),2)*\
      pow(NC,-1)*z + 5./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1) + 2*pow(ln(z),2)*pow(NC,-1)*x*pow(\
      omz,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*x + 1./2.*pow(ln(z),2)*pow(NC,-1)*x*z - 2*pow(ln(z),2\
      )*pow(NC,-1)*pow(x,2)*pow(z,-1) - pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 1./2.*pow(\
      ln(z),2)*pow(NC,-1)*pow(x,2) - 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*z + 1./2.*pow(ln(z),2)*\
      NC*pow(z,-1)*pow(omz,-1) + 1./4.*pow(ln(z),2)*NC*pow(z,-1) - 1./4.*pow(ln(z),2)*NC*pow(\
      omz,-1)
                result +=  - 1./2.*pow(ln(z),2)*NC + 1./4.*pow(ln(z),2)*NC*z - pow(ln(z),2)*NC*x*pow(z,-1)*pow(\
      omz,-1) - 1./2.*pow(ln(z),2)*NC*x*pow(z,-1) + 1./2.*pow(ln(z),2)*NC*x*pow(omz,-1) + pow(ln(z)\
      ,2)*NC*x - 1./2.*pow(ln(z),2)*NC*x*z + pow(ln(z),2)*NC*pow(x,2)*pow(z,-1)*pow(omz,-1) + 1./2.\
      *pow(ln(z),2)*NC*pow(x,2)*pow(z,-1) - 1./2.*pow(ln(z),2)*NC*pow(x,2)*pow(omz,-1) - pow(ln(z),\
      2)*NC*pow(x,2) + 1./2.*pow(ln(z),2)*NC*pow(x,2)*z - 7./2.*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)\
       - 4*ln(z)*ln(omx)*pow(NC,-1)*pow(omz,-1) + 2*ln(z)*ln(omx)*pow(NC,-1) + 7*ln(z)*ln(omx)*pow(\
      NC,-1)*x*pow(z,-1) + 8*ln(z)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) - 4*ln(z)*ln(omx)*pow(NC,-1)*x\
       - 5*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 5*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) + 4*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2) + 3./2.*ln(z)*ln(omx)*NC*pow(z,-1) + 3./2.*ln(z\
      )*ln(omx)*NC*pow(omz,-1) - 5./2.*ln(z)*ln(omx)*NC - 3*ln(z)*ln(omx)*NC*x*pow(z,-1) - 3*ln(z)*\
      ln(omx)*NC*x*pow(omz,-1) + 5*ln(z)*ln(omx)*NC*x + 3*ln(z)*ln(omx)*NC*pow(x,2)*pow(z,-1) + 3*\
      ln(z)*ln(omx)*NC*pow(x,2)*pow(omz,-1) - 5*ln(z)*ln(omx)*NC*pow(x,2) - 3*ln(z)*ln(omz)*pow(\
      NC,-1)*pow(z,-1) - 4*ln(z)*ln(omz)*pow(NC,-1)*pow(omz,-1) + 7./2.*ln(z)*ln(omz)*pow(NC,-1) + \
      6*ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1) + 8*ln(z)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) - 7*ln(z)*\
      ln(omz)*pow(NC,-1)*x - 5*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 5*ln(z)*ln(omz)*pow(\
      NC,-1)*pow(x,2)*pow(omz,-1)
                result +=  + 7*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2) + 5./2.*ln(z)*ln(omz)*NC*pow(z,-1) + 5./2.*ln(z\
      )*ln(omz)*NC*pow(omz,-1) - 11./2.*ln(z)*ln(omz)*NC - 5*ln(z)*ln(omz)*NC*x*pow(z,-1) - 5*ln(z)\
      *ln(omz)*NC*x*pow(omz,-1) + 11*ln(z)*ln(omz)*NC*x + 5*ln(z)*ln(omz)*NC*pow(x,2)*pow(z,-1) + 5\
      *ln(z)*ln(omz)*NC*pow(x,2)*pow(omz,-1) - 11*ln(z)*ln(omz)*NC*pow(x,2) - 1./4.*ln(omx)*pow(\
      NC,-1)*pow(z,-1) - ln(omx)*pow(NC,-1)*pow(omz,-1) + 7./4.*ln(omx)*pow(NC,-1) - 3./8.*ln(omx)*\
      pow(NC,-1)*z - 3./2.*ln(omx)*pow(NC,-1)*x*pow(z,-1) + 3./2.*ln(omx)*pow(NC,-1)*x + 1./4.*ln(\
      omx)*pow(NC,-1)*x*z - 1./2.*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 2*ln(omx)*pow(NC,-1)*pow(\
      x,2)*pow(omz,-1) - 11./4.*ln(omx)*pow(NC,-1)*pow(x,2) + 1./2.*ln(omx)*pow(NC,-1)*pow(x,2)*z\
       + 2./3.*ln(omx)*NC*pow(x,-1)*pow(z,-1) - 4./3.*ln(omx)*NC*pow(x,-1) + 1./4.*ln(omx)*NC*pow(\
      z,-1) + 1./2.*ln(omx)*NC*pow(omz,-1) - 5./4.*ln(omx)*NC + 3./8.*ln(omx)*NC*z + 11./2.*ln(omx)\
      *NC*x*pow(z,-1) - 27./2.*ln(omx)*NC*x - 1./4.*ln(omx)*NC*x*z - 20./3.*ln(omx)*NC*pow(x,2)*\
      pow(z,-1) + 193./12.*ln(omx)*NC*pow(x,2) - 1./2.*ln(omx)*NC*pow(x,2)*z
                result +=   - 3*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1) - 3*pow(ln(\
      omx),2)*pow(NC,-1)*pow(omz,-1) + 9./4.*pow(ln(omx),2)*pow(NC,-1) + 1./4.*pow(ln(omx),2)*pow(\
      NC,-1)*z + 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1) + 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(\
      omz,-1) - 9./2.*pow(ln(omx),2)*pow(NC,-1)*x - 1./2.*pow(ln(omx),2)*pow(NC,-1)*x*z - 4*pow(ln(\
      omx),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 4*pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 9./\
      2.*pow(ln(omx),2)*pow(NC,-1)*pow(x,2) + 1./2.*pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*z + 3./4.*\
      pow(ln(omx),2)*NC*pow(z,-1) + 1./4.*pow(ln(omx),2)*NC*pow(omz,-1) - 7./4.*pow(ln(omx),2)*NC\
       - 1./4.*pow(ln(omx),2)*NC*z - 3./2.*pow(ln(omx),2)*NC*x*pow(z,-1) - 1./2.*pow(ln(omx),2)*NC*\
      x*pow(omz,-1) + 7./2.*pow(ln(omx),2)*NC*x + 1./2.*pow(ln(omx),2)*NC*x*z + 3./2.*pow(ln(omx),2\
      )*NC*pow(x,2)*pow(z,-1)
                result +=  + 1./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(omz,-1) - 7./2.*pow(ln(omx),2)*NC*pow(x,2) - 1.\
      /2.*pow(ln(omx),2)*NC*pow(x,2)*z - 9./2.*ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1) - 4*ln(omx)*ln(\
      omz)*pow(NC,-1)*pow(omz,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1) + 1./2.*ln(omx)*ln(omz)*pow(NC,-1)\
      *z + 9*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1) + 8*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) - \
      8*ln(omx)*ln(omz)*pow(NC,-1)*x - ln(omx)*ln(omz)*pow(NC,-1)*x*z - 6*ln(omx)*ln(omz)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) - 6*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 8*ln(omx)*ln(\
      omz)*pow(NC,-1)*pow(x,2) + ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*z + 2*ln(omx)*ln(omz)*NC*pow(\
      z,-1) + ln(omx)*ln(omz)*NC*pow(omz,-1) - 9./2.*ln(omx)*ln(omz)*NC - 1./2.*ln(omx)*ln(omz)*NC*\
      z - 4*ln(omx)*ln(omz)*NC*x*pow(z,-1) - 2*ln(omx)*ln(omz)*NC*x*pow(omz,-1) + 9*ln(omx)*ln(omz)\
      *NC*x + ln(omx)*ln(omz)*NC*x*z + 4*ln(omx)*ln(omz)*NC*pow(x,2)*pow(z,-1) + 2*ln(omx)*ln(omz)*\
      NC*pow(x,2)*pow(omz,-1) - 9*ln(omx)*ln(omz)*NC*pow(x,2) - ln(omx)*ln(omz)*NC*pow(x,2)*z + 1./\
      4.*ln(omz)*pow(NC,-1)*pow(z,-1) - ln(omz)*pow(NC,-1)*pow(omz,-1) - 3./4.*ln(omz)*pow(NC,-1)*\
      pow(omxmz,-1) + 1./2.*ln(omz)*pow(NC,-1) - 3./8.*ln(omz)*pow(NC,-1)*z - 3./2.*ln(omz)*pow(\
      NC,-1)*x*pow(z,-1) + 1./4.*ln(omz)*pow(NC,-1)*x*pow(omxmz,-2) + 3./2.*ln(omz)*pow(NC,-1)*x*\
      pow(omxmz,-1) + 3*ln(omz)*pow(NC,-1)*x + 1./4.*ln(omz)*pow(NC,-1)*x*z - 1./2.*ln(omz)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)
                result +=  - ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 3./4.*ln(omz)*pow(NC,-1)*pow(x,2)*pow(\
      omxmz,-2) - 1./2.*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omxmz,-1) - 13./4.*ln(omz)*pow(NC,-1)*pow(\
      x,2) + 1./2.*ln(omz)*pow(NC,-1)*pow(x,2)*z + ln(omz)*pow(NC,-1)*pow(x,3)*pow(omxmz,-2) - 1./2.\
      *ln(omz)*pow(NC,-1)*pow(x,4)*pow(omxmz,-2) + 2./3.*ln(omz)*NC*pow(x,-1)*pow(z,-1) - 4./3.*ln(\
      omz)*NC*pow(x,-1) + 3./4.*ln(omz)*NC*pow(z,-1) + ln(omz)*NC*pow(omz,-1) + 3./4.*ln(omz)*NC*\
      pow(omxmz,-1) - 7./2.*ln(omz)*NC + 3./8.*ln(omz)*NC*z + 11./2.*ln(omz)*NC*x*pow(z,-1) - 1./4.\
      *ln(omz)*NC*x*pow(omxmz,-2) - 2*ln(omz)*NC*x*pow(omxmz,-1) - 14*ln(omz)*NC*x - 1./4.*ln(omz)*\
      NC*x*z - 20./3.*ln(omz)*NC*pow(x,2)*pow(z,-1) + 3./4.*ln(omz)*NC*pow(x,2)*pow(omxmz,-2) + 3./\
      2.*ln(omz)*NC*pow(x,2)*pow(omxmz,-1) + 199./12.*ln(omz)*NC*pow(x,2) - 1./2.*ln(omz)*NC*pow(\
      x,2)*z - ln(omz)*NC*pow(x,3)*pow(omxmz,-2) - ln(omz)*NC*pow(x,3)*pow(omxmz,-1) + 1./2.*ln(omz\
      )*NC*pow(x,4)*pow(omxmz,-2)
                result +=   - 5./2.*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1) - 3./2.*pow(ln(omz),2)*pow(NC,-1)*pow(omz,-1) + 2*\
      pow(ln(omz),2)*pow(NC,-1) + 1./4.*pow(ln(omz),2)*pow(NC,-1)*z + 5*pow(ln(omz),2)*pow(NC,-1)*x\
      *pow(z,-1) + 3*pow(ln(omz),2)*pow(NC,-1)*x*pow(omz,-1) - 4*pow(ln(omz),2)*pow(NC,-1)*x - 1./2.\
      *pow(ln(omz),2)*pow(NC,-1)*x*z - 3*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 5./2.*pow(\
      ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 4*pow(ln(omz),2)*pow(NC,-1)*pow(x,2) + 1./2.*\
      pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*z + 5./4.*pow(ln(omz),2)*NC*pow(z,-1) + pow(ln(omz),2)*NC*\
      pow(omz,-1) - 11./4.*pow(ln(omz),2)*NC - 1./4.*pow(ln(omz),2)*NC*z - 5./2.*pow(ln(omz),2)*NC*\
      x*pow(z,-1) - 2*pow(ln(omz),2)*NC*x*pow(omz,-1) + 11./2.*pow(ln(omz),2)*NC*x + 1./2.*pow(ln(\
      omz),2)*NC*x*z + 5./2.*pow(ln(omz),2)*NC*pow(x,2)*pow(z,-1) + 2*pow(ln(omz),2)*NC*pow(x,2)*\
      pow(omz,-1)
                result +=  - 11./2.*pow(ln(omz),2)*NC*pow(x,2) - 1./2.*pow(ln(omz),2)*NC*pow(x,2)*z - 3./64.*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*\
      pow(poly2,-2) + 3./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(\
      x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1) - 3./64.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1) - Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)\
      *sqrtxz2)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1) + Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(\
      x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1)*pow(omz,-1) + 1./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1.\
      /2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1) - Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(\
      x,-1)*sqrtxz2)*pow(NC,-1)*z*pow(sqrtxz2,-1) - 3*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)\
      *sqrtxz2)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1) + 3./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.\
      *pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(poly2,-2) - 1./2.*Li2(1./2. - 1./2.*pow(\
      x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(poly2,-1) - 3*Li2(1./2. - 1.\
      /2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(omz,-1) + 259./32.*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1) - 11./4.*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*z*pow(sqrtxz2,-1) + 11./4.\
      *Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1)
                result +=  - 3*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(\
      z,-1)*pow(sqrtxz2,-1) + 3*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*\
      pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) + 29./16.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1) - 29./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*\
      pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz2,-1) - Li2(1./2. - 1./2.*pow(x,-1) - 1./2.\
      *pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1) + 19./32.*Li2(1./2. - 1./2.\
      *pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1) - \
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*\
      pow(omz,-1) + 73./64.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(\
      x,3)*pow(sqrtxz2,-1) - 3./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(\
      NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) - 3./16.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*\
      pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./64.*Li2(1./2. - 1./\
      2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2) + 3.\
      /64.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,-1)*pow(sqrtxz2,-1)*pow(\
      poly2,-2) + 1./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,-1)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)
                result +=  - 5./64.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,-1)*pow(\
      sqrtxz2,-1) + 1./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(z,-1)*pow(\
      sqrtxz2,-1) - 1./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(sqrtxz2,-1)\
      *pow(omz,-1) - 9./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(\
      sqrtxz2,-1) + 9./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*z*pow(\
      sqrtxz2,-1) + 3./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*x*pow(z,-1)*\
      pow(sqrtxz2,-1) - 3./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*x*pow(\
      sqrtxz2,-1)*pow(poly2,-2) + 5./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*x\
      *pow(sqrtxz2,-1)*pow(poly2,-1) + 3./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)\
      *NC*x*pow(sqrtxz2,-1)*pow(omz,-1) - 211./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*\
      sqrtxz2)*NC*x*pow(sqrtxz2,-1) + 51./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)\
      *NC*x*z*pow(sqrtxz2,-1) - 51./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*x*\
      pow(z,2)*pow(sqrtxz2,-1) + 2*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(\
      x,2)*pow(z,-1)*pow(sqrtxz2,-1) - 2*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*\
      pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) - 129./16.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)\
      *sqrtxz2)*NC*pow(x,2)*pow(sqrtxz2,-1)
                result +=  + 129./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,2)*z*pow(\
      sqrtxz2,-1) + Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,3)*pow(z,-1)*\
      pow(sqrtxz2,-1) - 23./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,3)*\
      pow(sqrtxz2,-1)*pow(poly2,-1) + Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*\
      pow(x,3)*pow(sqrtxz2,-1)*pow(omz,-1) - 193./64.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)\
      *sqrtxz2)*NC*pow(x,3)*pow(sqrtxz2,-1) + 3./32.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*\
      sqrtxz2)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) + 1./16.*Li2(1./2. - 1./2.*pow(x,-1) - 1./\
      2.*pow(x,-1)*sqrtxz2)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) - 3./64.*Li2(1./2. - 1./2.*\
      pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2) + 3./64.*Li2(1.\
      /2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(\
      poly2,-2) - 3./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(\
      x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./64.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1) + Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)\
      *sqrtxz2)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1) - Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
      x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1)*pow(omz,-1) - 1./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1.\
      /2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1)
                result +=  + Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*z*pow(sqrtxz2,-1)\
       + 3*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(z,-1)*pow(\
      sqrtxz2,-1) - 3./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(\
      sqrtxz2,-1)*pow(poly2,-2) + 1./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(\
      NC,-1)*x*pow(sqrtxz2,-1)*pow(poly2,-1) + 3*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(omz,-1) - 259./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./\
      2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1) + 11./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./\
      2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*z*pow(sqrtxz2,-1) - 11./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1.\
      /2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1) + 3*Li2(1./2. - 1./2.*pow(x,-1)\
       + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1) - 3*Li2(1./2. - 1./\
      2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) - 29./\
      16.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz2,-1) + 29./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(\
      x,2)*z*pow(sqrtxz2,-1) + Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*\
      pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1) - 19./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)
                result +=  + Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz2,-1)*pow(omz,-1) - 73./64.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(\
      NC,-1)*pow(x,3)*pow(sqrtxz2,-1) + 3./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) + 3./16.*Li2(1./2. - 1./2.*pow(\
      x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) - 3./64.*\
      Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*\
      pow(poly2,-2) - 3./64.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,-1)*\
      pow(sqrtxz2,-1)*pow(poly2,-2) - 1./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)\
      *NC*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1) + 5./64.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
      x,-1)*sqrtxz2)*NC*pow(x,-1)*pow(sqrtxz2,-1) - 1./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
      x,-1)*sqrtxz2)*NC*pow(z,-1)*pow(sqrtxz2,-1) + 1./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
      x,-1)*sqrtxz2)*NC*pow(sqrtxz2,-1)*pow(omz,-1) + 9./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*\
      pow(x,-1)*sqrtxz2)*NC*pow(sqrtxz2,-1) - 9./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*NC*z*pow(sqrtxz2,-1) - 3./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*\
      NC*x*pow(z,-1)*pow(sqrtxz2,-1) + 3./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2\
      )*NC*x*pow(sqrtxz2,-1)*pow(poly2,-2)
                result +=  - 5./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*x*pow(sqrtxz2,-1)*\
      pow(poly2,-1) - 3./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*x*pow(\
      sqrtxz2,-1)*pow(omz,-1) + 211./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*\
      x*pow(sqrtxz2,-1) - 51./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*x*z*pow(\
      sqrtxz2,-1) + 51./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*x*pow(z,2)*\
      pow(sqrtxz2,-1) - 2*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,2)*pow(\
      z,-1)*pow(sqrtxz2,-1) + 2*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,2)*\
      pow(sqrtxz2,-1)*pow(omz,-1) + 129./16.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)\
      *NC*pow(x,2)*pow(sqrtxz2,-1) - 129./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)\
      *NC*pow(x,2)*z*pow(sqrtxz2,-1) - Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*\
      pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1) + 23./32.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*NC*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1) - Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
      x,-1)*sqrtxz2)*NC*pow(x,3)*pow(sqrtxz2,-1)*pow(omz,-1) + 193./64.*Li2(1./2. - 1./2.*pow(x,-1)\
       + 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,3)*pow(sqrtxz2,-1) - 3./32.*Li2(1./2. - 1./2.*pow(x,-1)\
       + 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) - 1./16.*Li2(1./2. - 1./\
      2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)
                result +=  + 3./64.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*NC*pow(x,7)*pow(\
      sqrtxz2,-1)*pow(poly2,-2) + 3./64.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*\
      pow(sqrtxz2,-1)*pow(poly2,-2) - 3./32.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(\
      x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./64.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*\
      pow(x,-1)*pow(sqrtxz2,-1) + Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(z,-1)*pow(\
      sqrtxz2,-1) - Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1)*pow(omz,-1) - 1.\
      /2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1) + Li2(1./2. - 1./2.*\
      sqrtxz2 - 1./2.*x)*pow(NC,-1)*z*pow(sqrtxz2,-1) + 3*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(\
      NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1) - 3./32.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x\
      *pow(sqrtxz2,-1)*pow(poly2,-2) + 1./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(\
      sqrtxz2,-1)*pow(poly2,-1) + 3*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(\
      sqrtxz2,-1)*pow(omz,-1) - 259./32.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(\
      sqrtxz2,-1) + 11./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*z*pow(sqrtxz2,-1) - 11.\
      /4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1) + 3*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1) - 3*Li2(1./2. - 1./\
      2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1)
                result +=  - 29./16.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1) + \
      29./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz2,-1) + Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1) - 19./32.*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1) + Li2(1./2. - 1.\
      /2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(omz,-1) - 73./64.*Li2(1./2. - \
      1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1) + 3./32.*Li2(1./2. - 1./2.*\
      sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) + 3./16.*Li2(1./2. - 1./\
      2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) - 3./64.*Li2(1./2. - \
      1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2) - 3./64.*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2) - 1./32.*Li2(1./2. - 1.\
      /2.*sqrtxz2 - 1./2.*x)*NC*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1) + 5./64.*Li2(1./2. - 1./2.*\
      sqrtxz2 - 1./2.*x)*NC*pow(x,-1)*pow(sqrtxz2,-1) - 1./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*\
      NC*pow(z,-1)*pow(sqrtxz2,-1) + 1./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(sqrtxz2,-1)*\
      pow(omz,-1) + 9./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(sqrtxz2,-1) - 9./2.*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*NC*z*pow(sqrtxz2,-1) - 3./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)\
      *NC*x*pow(z,-1)*pow(sqrtxz2,-1)
                result +=  + 3./32.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-2) - 5./\
      8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-1) - 3./2.*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*NC*x*pow(sqrtxz2,-1)*pow(omz,-1) + 211./32.*Li2(1./2. - 1./2.*\
      sqrtxz2 - 1./2.*x)*NC*x*pow(sqrtxz2,-1) - 51./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*x*z*\
      pow(sqrtxz2,-1) + 51./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*x*pow(z,2)*pow(sqrtxz2,-1)\
       - 2*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1) + 2*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) + 129./16.*Li2(1./2. - 1./\
      2.*sqrtxz2 - 1./2.*x)*NC*pow(x,2)*pow(sqrtxz2,-1) - 129./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.\
      *x)*NC*pow(x,2)*z*pow(sqrtxz2,-1) - Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,3)*pow(\
      z,-1)*pow(sqrtxz2,-1) + 23./32.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,3)*pow(\
      sqrtxz2,-1)*pow(poly2,-1) - Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,3)*pow(sqrtxz2,-1)*\
      pow(omz,-1) + 193./64.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,3)*pow(sqrtxz2,-1) - 3./\
      32.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2) - 1./16.*\
      Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1) + 3./64.*Li2(1.\
      /2. - 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2) - 3./64.*Li2(1./2.\
       + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2)
                result +=  + 3./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*\
      pow(poly2,-1) - 3./64.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*pow(\
      sqrtxz2,-1) - Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1) + \
      Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1)*pow(omz,-1) + 1./2.*Li2(1./2.\
       + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1) - Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)\
      *pow(NC,-1)*z*pow(sqrtxz2,-1) - 3*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(z,-1)\
      *pow(sqrtxz2,-1) + 3./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*\
      pow(poly2,-2) - 1./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(\
      poly2,-1) - 3*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*pow(omz,-1)\
       + 259./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(sqrtxz2,-1) - 11./4.*Li2(1./\
      2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*z*pow(sqrtxz2,-1) + 11./4.*Li2(1./2. + 1./2.*\
      sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1) - 3*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.\
      *x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1) + 3*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*\
      pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1) + 29./16.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x\
      )*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1) - 29./8.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(\
      NC,-1)*pow(x,2)*z*pow(sqrtxz2,-1)
                result +=  - Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1)\
       + 19./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(\
      poly2,-1) - Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(\
      omz,-1) + 73./64.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1) - \
      3./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-2)\
       - 3./16.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(\
      poly2,-1) + 3./64.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*\
      pow(poly2,-2) + 3./64.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,-1)*pow(sqrtxz2,-1)*pow(\
      poly2,-2) + 1./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,-1)*pow(sqrtxz2,-1)*pow(\
      poly2,-1) - 5./64.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,-1)*pow(sqrtxz2,-1) + 1./2.*\
      Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(z,-1)*pow(sqrtxz2,-1) - 1./2.*Li2(1./2. + 1./2.*\
      sqrtxz2 - 1./2.*x)*NC*pow(sqrtxz2,-1)*pow(omz,-1) - 9./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x\
      )*NC*pow(sqrtxz2,-1) + 9./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*z*pow(sqrtxz2,-1) + 3./2.\
      *Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*x*pow(z,-1)*pow(sqrtxz2,-1) - 3./32.*Li2(1./2. + 1./\
      2.*sqrtxz2 - 1./2.*x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-2) + 5./8.*Li2(1./2. + 1./2.*sqrtxz2 - \
      1./2.*x)*NC*x*pow(sqrtxz2,-1)*pow(poly2,-1)
                result +=  + 3./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*x*pow(sqrtxz2,-1)*pow(omz,-1) - 211./\
      32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*x*pow(sqrtxz2,-1) + 51./4.*Li2(1./2. + 1./2.*\
      sqrtxz2 - 1./2.*x)*NC*x*z*pow(sqrtxz2,-1) - 51./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*x*\
      pow(z,2)*pow(sqrtxz2,-1) + 2*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,2)*pow(z,-1)*pow(\
      sqrtxz2,-1) - 2*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,2)*pow(sqrtxz2,-1)*pow(omz,-1)\
       - 129./16.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,2)*pow(sqrtxz2,-1) + 129./8.*Li2(1./\
      2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,2)*z*pow(sqrtxz2,-1) + Li2(1./2. + 1./2.*sqrtxz2 - 1./\
      2.*x)*NC*pow(x,3)*pow(z,-1)*pow(sqrtxz2,-1) - 23./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC\
      *pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1) + Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,3)*\
      pow(sqrtxz2,-1)*pow(omz,-1) - 193./64.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,3)*pow(\
      sqrtxz2,-1) + 3./32.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(\
      poly2,-2) + 1./16.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,5)*pow(sqrtxz2,-1)*pow(\
      poly2,-1) - 3./64.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*NC*pow(x,7)*pow(sqrtxz2,-1)*pow(\
      poly2,-2) + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*pow(omz,-1) - 3./2.*Li2(1 - x*pow(\
      z,-1))*pow(NC,-1)*pow(z,-1) - 1./2.*Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(omz,-1) - 1./2.*Li2(1\
       - x*pow(z,-1))*pow(NC,-1)
                result +=  - 4*Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + 3*Li2(1 - x*pow(z,-1))*\
      pow(NC,-1)*x*pow(z,-1) + Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*pow(omz,-1) + Li2(1 - x*pow(z,-1))\
      *pow(NC,-1)*x + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) - Li2(1 - x*\
      pow(z,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) - Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(x,2) - Li2(1 - x*pow(z,-1))*NC*pow(z,-1)*pow(\
      omz,-1) + 1./2.*Li2(1 - x*pow(z,-1))*NC*pow(z,-1) + 1./2.*Li2(1 - x*pow(z,-1))*NC*pow(omz,-1)\
       + 3./2.*Li2(1 - x*pow(z,-1))*NC + 2*Li2(1 - x*pow(z,-1))*NC*x*pow(z,-1)*pow(omz,-1) - Li2(1\
       - x*pow(z,-1))*NC*x*pow(z,-1) - Li2(1 - x*pow(z,-1))*NC*x*pow(omz,-1) - 3*Li2(1 - x*pow(\
      z,-1))*NC*x - 2*Li2(1 - x*pow(z,-1))*NC*pow(x,2)*pow(z,-1)*pow(omz,-1) + Li2(1 - x*pow(z,-1))\
      *NC*pow(x,2)*pow(z,-1) + Li2(1 - x*pow(z,-1))*NC*pow(x,2)*pow(omz,-1) + 3*Li2(1 - x*pow(z,-1)\
      )*NC*pow(x,2) - 2*Li2( - x)*pow(NC,-1)*pow(z,-1) + 2*Li2( - x)*pow(NC,-1) - Li2( - x)*pow(\
      NC,-1)*z - 4*Li2( - x)*pow(NC,-1)*x*pow(z,-1) + 4*Li2( - x)*pow(NC,-1)*x - 2*Li2( - x)*pow(\
      NC,-1)*x*z - 2*Li2( - x)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*Li2( - x)*pow(NC,-1)*pow(x,2) - 2*\
      Li2( - x)*pow(NC,-1)*pow(x,2)*z - Li2( - x)*NC + Li2( - x)*NC*z - 2*Li2( - x)*NC*x + 2*Li2(\
       - x)*NC*x*z + 2*Li2( - x)*NC*pow(x,2)*z + 1./2.*Li2(x)*pow(NC,-1)*pow(z,-1) + 2*Li2(x)*pow(\
      NC,-1)*pow(omz,-1)
                result +=  - 3./2.*Li2(x)*pow(NC,-1) - 1./2.*Li2(x)*pow(NC,-1)*z - Li2(x)*pow(NC,-1)*x*pow(z,-1)\
       - 4*Li2(x)*pow(NC,-1)*x*pow(omz,-1) + 2*Li2(x)*pow(NC,-1)*x + 2*Li2(x)*pow(NC,-1)*x*z + Li2(\
      x)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*Li2(x)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - Li2(x)*pow(\
      NC,-1)*pow(x,2) - Li2(x)*pow(NC,-1)*pow(x,2)*z + 2*Li2(x)*NC*pow(z,-1)*pow(omz,-1) - 5./2.*\
      Li2(x)*NC*pow(z,-1) - 2*Li2(x)*NC*pow(omz,-1) + 5./2.*Li2(x)*NC + 1./2.*Li2(x)*NC*z - 4*Li2(x\
      )*NC*x*pow(z,-1)*pow(omz,-1) - Li2(x)*NC*x*pow(z,-1) + 4*Li2(x)*NC*x*pow(omz,-1) + 8*Li2(x)*\
      NC*x - 2*Li2(x)*NC*x*z + 4*Li2(x)*NC*pow(x,2)*pow(z,-1)*pow(omz,-1) - 3*Li2(x)*NC*pow(x,2)*\
      pow(z,-1) - 4*Li2(x)*NC*pow(x,2)*pow(omz,-1) - Li2(x)*NC*pow(x,2) + Li2(x)*NC*pow(x,2)*z - \
      Li2(z)*pow(NC,-1)*pow(omz,-1) + 2*Li2(z)*pow(NC,-1) + 2*Li2(z)*pow(NC,-1)*x*pow(omz,-1) - 4*\
      Li2(z)*pow(NC,-1)*x - Li2(z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(z)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) + 4*Li2(z)*pow(NC,-1)*pow(x,2) + 1./2.*Li2(z)*NC*pow(z,-1) + 1./2.*Li2(z)*NC*pow(\
      omz,-1) - 2*Li2(z)*NC - Li2(z)*NC*x*pow(z,-1) - Li2(z)*NC*x*pow(omz,-1) + 4*Li2(z)*NC*x + \
      Li2(z)*NC*pow(x,2)*pow(z,-1) + Li2(z)*NC*pow(x,2)*pow(omz,-1) - 4*Li2(z)*NC*pow(x,2)
            if z < 1.-x and z < x:
                result += 3./2.*pow(NC,-1)*pow(z,-1) - 11./12.*pow(NC,-1)*pow(z,-1)*pow(pi,2) + 3./2.*pow(NC,-1)*\
      pow(omz,-1) - 5./6.*pow(NC,-1)*pow(pi,2)*pow(omz,-1) + 7./12.*pow(NC,-1)*pow(pi,2) + 11./6.*\
      pow(NC,-1)*x*pow(z,-1)*pow(pi,2) + 5./3.*pow(NC,-1)*x*pow(pi,2)*pow(omz,-1) - 7./6.*pow(\
      NC,-1)*x*pow(pi,2) - pow(NC,-1)*pow(x,2)*pow(z,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      pi,2) - pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(omz,-1) + 7.\
      /6.*pow(NC,-1)*pow(x,2)*pow(pi,2) + 1./12.*NC*pow(z,-1)*pow(pi,2) - 2*NC + 1./12.*NC*pow(\
      pi,2)*pow(omz,-1) - 1./6.*NC*pow(pi,2) - 1./6.*NC*x*pow(z,-1)*pow(pi,2) - 2*NC*x - 1./6.*NC*x\
      *pow(pi,2)*pow(omz,-1) + 1./3.*NC*x*pow(pi,2) + 1./6.*NC*pow(x,2)*pow(z,-1)*pow(pi,2) + 2*NC*\
      pow(x,2) + 1./6.*NC*pow(x,2)*pow(pi,2)*pow(omz,-1) - 1./3.*NC*pow(x,2)*pow(pi,2) - 3./2.*ln(x\
      )*pow(NC,-1)*pow(z,-1) - 3./2.*ln(x)*pow(NC,-1)*pow(omz,-1) + 3*ln(x)*pow(NC,-1) - 3*ln(x)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) - 3*ln(x)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 3./2.*ln(x)*NC*pow(\
      z,-1) + 3./2.*ln(x)*NC*pow(omz,-1) - 9./2.*ln(x)*NC - 6*ln(x)*NC*x + 6*ln(x)*NC*pow(x,2) + 5*\
      pow(ln(x),2)*pow(NC,-1)*pow(z,-1) + 19./4.*pow(ln(x),2)*pow(NC,-1)*pow(omz,-1) - 13./4.*pow(\
      ln(x),2)*pow(NC,-1) - 10*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1) - 19./2.*pow(ln(x),2)*pow(NC,-1)\
      *x*pow(omz,-1) + 13./2.*pow(ln(x),2)*pow(NC,-1)*x + 13./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*\
      pow(z,-1)
                result +=  + 13./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 13./2.*pow(ln(x),2)*pow(\
      NC,-1)*pow(x,2) - 3./2.*pow(ln(x),2)*NC*pow(z,-1) - 3./2.*pow(ln(x),2)*NC*pow(omz,-1) + 3*\
      pow(ln(x),2)*NC + 3*pow(ln(x),2)*NC*x*pow(z,-1) + 3*pow(ln(x),2)*NC*x*pow(omz,-1) - 6*pow(ln(\
      x),2)*NC*x - 3*pow(ln(x),2)*NC*pow(x,2)*pow(z,-1) - 3*pow(ln(x),2)*NC*pow(x,2)*pow(omz,-1) + \
      6*pow(ln(x),2)*NC*pow(x,2) - 11./2.*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1) - 13./2.*ln(x)*ln(z)*\
      pow(NC,-1)*pow(omz,-1) + 4*ln(x)*ln(z)*pow(NC,-1) + 11*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1) + \
      13*ln(x)*ln(z)*pow(NC,-1)*x*pow(omz,-1) - 8*ln(x)*ln(z)*pow(NC,-1)*x - 8*ln(x)*ln(z)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) - 8*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 8*ln(x)*ln(z)*\
      pow(NC,-1)*pow(x,2) + 5./2.*ln(x)*ln(z)*NC*pow(z,-1) + 5./2.*ln(x)*ln(z)*NC*pow(omz,-1) - 5*\
      ln(x)*ln(z)*NC - 5*ln(x)*ln(z)*NC*x*pow(z,-1) - 5*ln(x)*ln(z)*NC*x*pow(omz,-1) + 10*ln(x)*ln(\
      z)*NC*x + 5*ln(x)*ln(z)*NC*pow(x,2)*pow(z,-1) + 5*ln(x)*ln(z)*NC*pow(x,2)*pow(omz,-1) - 10*\
      ln(x)*ln(z)*NC*pow(x,2) - 17./2.*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1) - 8*ln(x)*ln(omx)*pow(\
      NC,-1)*pow(omz,-1) + 11./2.*ln(x)*ln(omx)*pow(NC,-1) + 17*ln(x)*ln(omx)*pow(NC,-1)*x*pow(\
      z,-1) + 16*ln(x)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) - 11*ln(x)*ln(omx)*pow(NC,-1)*x - 11*ln(x)*\
      ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 11*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 11\
      *ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)
                result +=  + 2*ln(x)*ln(omx)*NC*pow(z,-1) + 2*ln(x)*ln(omx)*NC*pow(omz,-1) - 4*ln(x)*ln(omx)*NC\
       - 4*ln(x)*ln(omx)*NC*x*pow(z,-1) - 4*ln(x)*ln(omx)*NC*x*pow(omz,-1) + 8*ln(x)*ln(omx)*NC*x\
       + 4*ln(x)*ln(omx)*NC*pow(x,2)*pow(z,-1) + 4*ln(x)*ln(omx)*NC*pow(x,2)*pow(omz,-1) - 8*ln(x)*\
      ln(omx)*NC*pow(x,2) - 8*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1) - 7*ln(x)*ln(omz)*pow(NC,-1)*pow(\
      omz,-1) + 5*ln(x)*ln(omz)*pow(NC,-1) + 16*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1) + 14*ln(x)*ln(\
      omz)*pow(NC,-1)*x*pow(omz,-1) - 10*ln(x)*ln(omz)*pow(NC,-1)*x - 10*ln(x)*ln(omz)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1) - 10*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 10*ln(x)*ln(omz)*pow(\
      NC,-1)*pow(x,2) + 5./2.*ln(x)*ln(omz)*NC*pow(z,-1) + 5./2.*ln(x)*ln(omz)*NC*pow(omz,-1) - 5*\
      ln(x)*ln(omz)*NC - 5*ln(x)*ln(omz)*NC*x*pow(z,-1) - 5*ln(x)*ln(omz)*NC*x*pow(omz,-1) + 10*ln(\
      x)*ln(omz)*NC*x + 5*ln(x)*ln(omz)*NC*pow(x,2)*pow(z,-1) + 5*ln(x)*ln(omz)*NC*pow(x,2)*pow(\
      omz,-1) - 10*ln(x)*ln(omz)*NC*pow(x,2) + 1./2.*ln(x)*ln(xmz)*pow(NC,-1)*pow(z,-1) + ln(x)*ln(\
      xmz)*pow(NC,-1)*pow(omz,-1) - 1./2.*ln(x)*ln(xmz)*pow(NC,-1) - ln(x)*ln(xmz)*pow(NC,-1)*x*\
      pow(z,-1) - 2*ln(x)*ln(xmz)*pow(NC,-1)*x*pow(omz,-1) + ln(x)*ln(xmz)*pow(NC,-1)*x + ln(x)*ln(\
      xmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + ln(x)*ln(xmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*\
      ln(xmz)*pow(NC,-1)*pow(x,2) - 1./2.*ln(x)*ln(xmz)*NC*pow(z,-1) - 1./2.*ln(x)*ln(xmz)*NC*pow(\
      omz,-1)
                result +=  + ln(x)*ln(xmz)*NC + ln(x)*ln(xmz)*NC*x*pow(z,-1) + ln(x)*ln(xmz)*NC*x*pow(omz,-1) - \
      2*ln(x)*ln(xmz)*NC*x - ln(x)*ln(xmz)*NC*pow(x,2)*pow(z,-1) - ln(x)*ln(xmz)*NC*pow(x,2)*pow(\
      omz,-1) + 2*ln(x)*ln(xmz)*NC*pow(x,2) + ln(x)*ln(omxmz)*pow(NC,-1)*pow(z,-1) + 1./2.*ln(x)*\
      ln(omxmz)*pow(NC,-1)*pow(omz,-1) - 1./2.*ln(x)*ln(omxmz)*pow(NC,-1) - 2*ln(x)*ln(omxmz)*pow(\
      NC,-1)*x*pow(z,-1) - ln(x)*ln(omxmz)*pow(NC,-1)*x*pow(omz,-1) + ln(x)*ln(omxmz)*pow(NC,-1)*x\
       + ln(x)*ln(omxmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + ln(x)*ln(omxmz)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) - ln(x)*ln(omxmz)*pow(NC,-1)*pow(x,2) - 1./2.*ln(x)*ln(omxmz)*NC*pow(z,-1) - 1./2.*\
      ln(x)*ln(omxmz)*NC*pow(omz,-1) + ln(x)*ln(omxmz)*NC + ln(x)*ln(omxmz)*NC*x*pow(z,-1) + ln(x)*\
      ln(omxmz)*NC*x*pow(omz,-1) - 2*ln(x)*ln(omxmz)*NC*x - ln(x)*ln(omxmz)*NC*pow(x,2)*pow(z,-1)\
       - ln(x)*ln(omxmz)*NC*pow(x,2)*pow(omz,-1) + 2*ln(x)*ln(omxmz)*NC*pow(x,2) + ln(z)*pow(NC,-1)\
      *pow(z,-1) + 1./2.*ln(z)*pow(NC,-1)*pow(omz,-1) - 3./2.*ln(z)*pow(NC,-1) + ln(z)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1) + 2*ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(z)*NC*pow(z,-1) - ln(z)*NC*\
      pow(omz,-1) + 3*ln(z)*NC + 4*ln(z)*NC*x - 4*ln(z)*NC*pow(x,2) + 3./2.*pow(ln(z),2)*pow(NC,-1)\
      *pow(z,-1) + 9./4.*pow(ln(z),2)*pow(NC,-1)*pow(omz,-1) - 5./4.*pow(ln(z),2)*pow(NC,-1) - 3*\
      pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1) - 9./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(omz,-1) + 5./2.*\
      pow(ln(z),2)*pow(NC,-1)*x
                result +=  + 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 5./2.*pow(ln(z),2)*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) - 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2) - pow(ln(z),2)*NC*pow(z,-1) - \
      pow(ln(z),2)*NC*pow(omz,-1) + 2*pow(ln(z),2)*NC + 2*pow(ln(z),2)*NC*x*pow(z,-1) + 2*pow(ln(z)\
      ,2)*NC*x*pow(omz,-1) - 4*pow(ln(z),2)*NC*x - 2*pow(ln(z),2)*NC*pow(x,2)*pow(z,-1) - 2*pow(ln(\
      z),2)*NC*pow(x,2)*pow(omz,-1) + 4*pow(ln(z),2)*NC*pow(x,2) + 4*ln(z)*ln(omx)*pow(NC,-1)*pow(\
      z,-1) + 5*ln(z)*ln(omx)*pow(NC,-1)*pow(omz,-1) - 3*ln(z)*ln(omx)*pow(NC,-1) - 8*ln(z)*ln(omx)\
      *pow(NC,-1)*x*pow(z,-1) - 10*ln(z)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) + 6*ln(z)*ln(omx)*pow(\
      NC,-1)*x + 6*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 6*ln(z)*ln(omx)*pow(NC,-1)*pow(\
      x,2)*pow(omz,-1) - 6*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2) - ln(z)*ln(omx)*NC*pow(z,-1) - ln(z)*\
      ln(omx)*NC*pow(omz,-1) + 2*ln(z)*ln(omx)*NC + 2*ln(z)*ln(omx)*NC*x*pow(z,-1) + 2*ln(z)*ln(omx\
      )*NC*x*pow(omz,-1) - 4*ln(z)*ln(omx)*NC*x - 2*ln(z)*ln(omx)*NC*pow(x,2)*pow(z,-1) - 2*ln(z)*\
      ln(omx)*NC*pow(x,2)*pow(omz,-1) + 4*ln(z)*ln(omx)*NC*pow(x,2) + 3*ln(z)*ln(omz)*pow(NC,-1)*\
      pow(z,-1) + 3*ln(z)*ln(omz)*pow(NC,-1)*pow(omz,-1) - 2*ln(z)*ln(omz)*pow(NC,-1) - 6*ln(z)*ln(\
      omz)*pow(NC,-1)*x*pow(z,-1) - 6*ln(z)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) + 4*ln(z)*ln(omz)*pow(\
      NC,-1)*x + 4*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 4*ln(z)*ln(omz)*pow(NC,-1)*pow(\
      x,2)*pow(omz,-1)
                result +=  - 4*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2) - 2*ln(z)*ln(omz)*NC*pow(z,-1) - 2*ln(z)*ln(omz\
      )*NC*pow(omz,-1) + 4*ln(z)*ln(omz)*NC + 4*ln(z)*ln(omz)*NC*x*pow(z,-1) + 4*ln(z)*ln(omz)*NC*x\
      *pow(omz,-1) - 8*ln(z)*ln(omz)*NC*x - 4*ln(z)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 4*ln(z)*ln(omz)\
      *NC*pow(x,2)*pow(omz,-1) + 8*ln(z)*ln(omz)*NC*pow(x,2) - 1./2.*ln(z)*ln(xmz)*pow(NC,-1)*pow(\
      z,-1) - ln(z)*ln(xmz)*pow(NC,-1)*pow(omz,-1) + 1./2.*ln(z)*ln(xmz)*pow(NC,-1) + ln(z)*ln(xmz)\
      *pow(NC,-1)*x*pow(z,-1) + 2*ln(z)*ln(xmz)*pow(NC,-1)*x*pow(omz,-1) - ln(z)*ln(xmz)*pow(NC,-1)\
      *x - ln(z)*ln(xmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(z)*ln(xmz)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) + ln(z)*ln(xmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(z)*ln(xmz)*NC*pow(z,-1) + 1./2.*ln(z)*\
      ln(xmz)*NC*pow(omz,-1) - ln(z)*ln(xmz)*NC - ln(z)*ln(xmz)*NC*x*pow(z,-1) - ln(z)*ln(xmz)*NC*x\
      *pow(omz,-1) + 2*ln(z)*ln(xmz)*NC*x + ln(z)*ln(xmz)*NC*pow(x,2)*pow(z,-1) + ln(z)*ln(xmz)*NC*\
      pow(x,2)*pow(omz,-1) - 2*ln(z)*ln(xmz)*NC*pow(x,2) + ln(omx)*pow(NC,-1)*pow(z,-1) + ln(omx)*\
      pow(NC,-1)*pow(omz,-1) - 2*ln(omx)*pow(NC,-1) + 2*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*\
      ln(omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 1./2.*ln(omx)*NC*pow(z,-1) - 1./2.*ln(omx)*NC*pow(\
      omz,-1) + 3./2.*ln(omx)*NC + 2*ln(omx)*NC*x - 2*ln(omx)*NC*pow(x,2) + 3*pow(ln(omx),2)*pow(\
      NC,-1)*pow(z,-1) + 3*pow(ln(omx),2)*pow(NC,-1)*pow(omz,-1) - 2*pow(ln(omx),2)*pow(NC,-1) - 6*\
      pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1)
                result +=  - 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(omz,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*x + 4*pow(\
      ln(omx),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       - 4*pow(ln(omx),2)*pow(NC,-1)*pow(x,2) - 1./4.*pow(ln(omx),2)*NC*pow(z,-1) - 1./4.*pow(ln(\
      omx),2)*NC*pow(omz,-1) + 1./2.*pow(ln(omx),2)*NC + 1./2.*pow(ln(omx),2)*NC*x*pow(z,-1) + 1./2.\
      *pow(ln(omx),2)*NC*x*pow(omz,-1) - pow(ln(omx),2)*NC*x - 1./2.*pow(ln(omx),2)*NC*pow(x,2)*\
      pow(z,-1) - 1./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(omz,-1) + pow(ln(omx),2)*NC*pow(x,2) + 6*ln(\
      omx)*ln(omz)*pow(NC,-1)*pow(z,-1) + 9./2.*ln(omx)*ln(omz)*pow(NC,-1)*pow(omz,-1) - 7./2.*ln(\
      omx)*ln(omz)*pow(NC,-1) - 12*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 9*ln(omx)*ln(omz)*pow(\
      NC,-1)*x*pow(omz,-1) + 7*ln(omx)*ln(omz)*pow(NC,-1)*x + 7*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)\
      *pow(z,-1) + 7*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7*ln(omx)*ln(omz)*pow(NC,-1)\
      *pow(x,2) - 3./2.*ln(omx)*ln(omz)*NC*pow(z,-1) - 3./2.*ln(omx)*ln(omz)*NC*pow(omz,-1) + 3*ln(\
      omx)*ln(omz)*NC + 3*ln(omx)*ln(omz)*NC*x*pow(z,-1) + 3*ln(omx)*ln(omz)*NC*x*pow(omz,-1) - 6*\
      ln(omx)*ln(omz)*NC*x - 3*ln(omx)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 3*ln(omx)*ln(omz)*NC*pow(\
      x,2)*pow(omz,-1) + 6*ln(omx)*ln(omz)*NC*pow(x,2) + 1./2.*ln(omz)*pow(NC,-1)*pow(z,-1) + ln(\
      omz)*pow(NC,-1)*pow(omz,-1) - 3./2.*ln(omz)*pow(NC,-1) + 2*ln(omz)*pow(NC,-1)*pow(x,2)*pow(\
      z,-1)
                result +=  + ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(omz)*NC*pow(z,-1) - ln(omz)*NC*pow(\
      omz,-1) + 3*ln(omz)*NC + 4*ln(omz)*NC*x - 4*ln(omz)*NC*pow(x,2) + 11./4.*pow(ln(omz),2)*pow(\
      NC,-1)*pow(z,-1) + 7./4.*pow(ln(omz),2)*pow(NC,-1)*pow(omz,-1) - 3./2.*pow(ln(omz),2)*pow(\
      NC,-1) - 11./2.*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1) - 7./2.*pow(ln(omz),2)*pow(NC,-1)*x*\
      pow(omz,-1) + 3*pow(ln(omz),2)*pow(NC,-1)*x + 3*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)\
       + 3*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 3*pow(ln(omz),2)*pow(NC,-1)*pow(x,2) - \
      3./4.*pow(ln(omz),2)*NC*pow(z,-1) - 3./4.*pow(ln(omz),2)*NC*pow(omz,-1) + 3./2.*pow(ln(omz),2\
      )*NC + 3./2.*pow(ln(omz),2)*NC*x*pow(z,-1) + 3./2.*pow(ln(omz),2)*NC*x*pow(omz,-1) - 3*pow(\
      ln(omz),2)*NC*x - 3./2.*pow(ln(omz),2)*NC*pow(x,2)*pow(z,-1) - 3./2.*pow(ln(omz),2)*NC*pow(\
      x,2)*pow(omz,-1) + 3*pow(ln(omz),2)*NC*pow(x,2) - ln(omz)*ln(omxmz)*pow(NC,-1)*pow(z,-1) - 1./\
      2.*ln(omz)*ln(omxmz)*pow(NC,-1)*pow(omz,-1) + 1./2.*ln(omz)*ln(omxmz)*pow(NC,-1) + 2*ln(omz)*\
      ln(omxmz)*pow(NC,-1)*x*pow(z,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*x*pow(omz,-1) - ln(omz)*ln(\
      omxmz)*pow(NC,-1)*x - ln(omz)*ln(omxmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(omz)*ln(omxmz)*\
      pow(NC,-1)*pow(x,2)*pow(omz,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(omz)*ln(\
      omxmz)*NC*pow(z,-1) + 1./2.*ln(omz)*ln(omxmz)*NC*pow(omz,-1) - ln(omz)*ln(omxmz)*NC - ln(omz)\
      *ln(omxmz)*NC*x*pow(z,-1)
                result +=  - ln(omz)*ln(omxmz)*NC*x*pow(omz,-1) + 2*ln(omz)*ln(omxmz)*NC*x + ln(omz)*ln(omxmz)*\
      NC*pow(x,2)*pow(z,-1) + ln(omz)*ln(omxmz)*NC*pow(x,2)*pow(omz,-1) - 2*ln(omz)*ln(omxmz)*NC*\
      pow(x,2) + 1./2.*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*pow(z,-1) + 1./2.*Li2(pow(x,-1)*z*pow(\
      omx,-1)*omz)*NC*pow(omz,-1) - Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC - Li2(pow(x,-1)*z*pow(\
      omx,-1)*omz)*NC*x*pow(z,-1) - Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*x*pow(omz,-1) + 2*Li2(pow(\
      x,-1)*z*pow(omx,-1)*omz)*NC*x + Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*pow(x,2)*pow(z,-1) + Li2(\
      pow(x,-1)*z*pow(omx,-1)*omz)*NC*pow(x,2)*pow(omz,-1) - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*\
      pow(x,2) - 1./2.*Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1) - Li2(pow(x,-1)*z*omx*\
      pow(omz,-1))*pow(NC,-1)*pow(omz,-1) + 1./2.*Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1) + \
      Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1) + 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*\
      pow(NC,-1)*x*pow(omz,-1) - Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x - Li2(pow(x,-1)*z*\
      omx*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) + Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*pow(x,2) + 1./2.*Li2(omx*\
      pow(omz,-1))*pow(NC,-1)*pow(z,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(omz,-1) - 1./2.*Li2(\
      omx*pow(omz,-1))*pow(NC,-1) - Li2(omx*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1) - 2*Li2(omx*pow(\
      omz,-1))*pow(NC,-1)*x*pow(omz,-1)
                result +=  + Li2(omx*pow(omz,-1))*pow(NC,-1)*x + Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(\
      z,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(omz,-1) - Li2(omx*pow(omz,-1))*pow(\
      NC,-1)*pow(x,2) + 1./2.*Li2(omx*pow(omz,-1))*NC*pow(z,-1) + 1./2.*Li2(omx*pow(omz,-1))*NC*\
      pow(omz,-1) - Li2(omx*pow(omz,-1))*NC - Li2(omx*pow(omz,-1))*NC*x*pow(z,-1) - Li2(omx*pow(\
      omz,-1))*NC*x*pow(omz,-1) + 2*Li2(omx*pow(omz,-1))*NC*x + Li2(omx*pow(omz,-1))*NC*pow(x,2)*\
      pow(z,-1) + Li2(omx*pow(omz,-1))*NC*pow(x,2)*pow(omz,-1) - 2*Li2(omx*pow(omz,-1))*NC*pow(x,2)\
       - Li2(z*pow(omx,-1))*pow(NC,-1)*pow(z,-1) - 1./2.*Li2(z*pow(omx,-1))*pow(NC,-1)*pow(omz,-1)\
       + 1./2.*Li2(z*pow(omx,-1))*pow(NC,-1) + 2*Li2(z*pow(omx,-1))*pow(NC,-1)*x*pow(z,-1) + Li2(z*\
      pow(omx,-1))*pow(NC,-1)*x*pow(omz,-1) - Li2(z*pow(omx,-1))*pow(NC,-1)*x - Li2(z*pow(omx,-1))*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(z*pow(omx,-1))*pow(NC,-1)*pow(x,2)*pow(omz,-1) + Li2(z*\
      pow(omx,-1))*pow(NC,-1)*pow(x,2) - 1./2.*Li2(z*pow(omx,-1))*NC*pow(z,-1) - 1./2.*Li2(z*pow(\
      omx,-1))*NC*pow(omz,-1) + Li2(z*pow(omx,-1))*NC + Li2(z*pow(omx,-1))*NC*x*pow(z,-1) + Li2(z*\
      pow(omx,-1))*NC*x*pow(omz,-1) - 2*Li2(z*pow(omx,-1))*NC*x - Li2(z*pow(omx,-1))*NC*pow(x,2)*\
      pow(z,-1) - Li2(z*pow(omx,-1))*NC*pow(x,2)*pow(omz,-1) + 2*Li2(z*pow(omx,-1))*NC*pow(x,2) + \
      Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*pow(z,-1) + 1./2.*Li2(x*z*pow(omx,-1)*pow(omz,-1)\
      )*pow(NC,-1)*pow(omz,-1)
                result +=  - 1./2.*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1) - 2*Li2(x*z*pow(omx,-1)*pow(\
      omz,-1))*pow(NC,-1)*x*pow(z,-1) - Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x*pow(omz,-1)\
       + Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x + Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) + Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       - Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*pow(x,2) + 1./2.*Li2(z)*pow(NC,-1)*pow(z,-1)\
       - 1./2.*Li2(z)*pow(NC,-1)*pow(omz,-1) - Li2(z)*pow(NC,-1)*x*pow(z,-1) + Li2(z)*pow(NC,-1)*x*\
      pow(omz,-1)
            if z > 1.-x and z  < x:
                3./2.*pow(NC,-1)*pow(z,-1) - 11./12.*pow(NC,-1)*pow(z,-1)*pow(pi,2) + 3./2.*pow(NC,-1)*\
      pow(omz,-1) - 5./6.*pow(NC,-1)*pow(pi,2)*pow(omz,-1) + 7./12.*pow(NC,-1)*pow(pi,2) + 11./6.*\
      pow(NC,-1)*x*pow(z,-1)*pow(pi,2) + 5./3.*pow(NC,-1)*x*pow(pi,2)*pow(omz,-1) - 7./6.*pow(\
      NC,-1)*x*pow(pi,2) - pow(NC,-1)*pow(x,2)*pow(z,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      pi,2) - pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(omz,-1) + 7.\
      /6.*pow(NC,-1)*pow(x,2)*pow(pi,2) + 1./12.*NC*pow(z,-1)*pow(pi,2) - 2*NC + 1./12.*NC*pow(\
      pi,2)*pow(omz,-1) - 1./6.*NC*pow(pi,2) - 1./6.*NC*x*pow(z,-1)*pow(pi,2) - 2*NC*x - 1./6.*NC*x\
      *pow(pi,2)*pow(omz,-1) + 1./3.*NC*x*pow(pi,2) + 1./6.*NC*pow(x,2)*pow(z,-1)*pow(pi,2) + 2*NC*\
      pow(x,2) + 1./6.*NC*pow(x,2)*pow(pi,2)*pow(omz,-1) - 1./3.*NC*pow(x,2)*pow(pi,2) - 3./2.*ln(x\
      )*pow(NC,-1)*pow(z,-1) - 3./2.*ln(x)*pow(NC,-1)*pow(omz,-1) + 3*ln(x)*pow(NC,-1) - 3*ln(x)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) - 3*ln(x)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 3./2.*ln(x)*NC*pow(\
      z,-1) + 3./2.*ln(x)*NC*pow(omz,-1) - 9./2.*ln(x)*NC - 6*ln(x)*NC*x + 6*ln(x)*NC*pow(x,2) + \
      ln(x)*ln( - omxmz)*pow(NC,-1)*pow(z,-1) + 1./2.*ln(x)*ln( - omxmz)*pow(NC,-1)*pow(omz,-1) - 1.\
      /2.*ln(x)*ln( - omxmz)*pow(NC,-1) - 2*ln(x)*ln( - omxmz)*pow(NC,-1)*x*pow(z,-1) - ln(x)*ln(\
       - omxmz)*pow(NC,-1)*x*pow(omz,-1) + ln(x)*ln( - omxmz)*pow(NC,-1)*x + ln(x)*ln( - omxmz)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1)
                result +=  + ln(x)*ln( - omxmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*ln( - omxmz)*pow(NC,-1)*\
      pow(x,2) - 1./2.*ln(x)*ln( - omxmz)*NC*pow(z,-1) - 1./2.*ln(x)*ln( - omxmz)*NC*pow(omz,-1) + \
      ln(x)*ln( - omxmz)*NC + ln(x)*ln( - omxmz)*NC*x*pow(z,-1) + ln(x)*ln( - omxmz)*NC*x*pow(\
      omz,-1) - 2*ln(x)*ln( - omxmz)*NC*x - ln(x)*ln( - omxmz)*NC*pow(x,2)*pow(z,-1) - ln(x)*ln( - \
      omxmz)*NC*pow(x,2)*pow(omz,-1) + 2*ln(x)*ln( - omxmz)*NC*pow(x,2) + 9./2.*pow(ln(x),2)*pow(\
      NC,-1)*pow(z,-1) + 9./2.*pow(ln(x),2)*pow(NC,-1)*pow(omz,-1) - 3*pow(ln(x),2)*pow(NC,-1) - 9*\
      pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1) - 9*pow(ln(x),2)*pow(NC,-1)*x*pow(omz,-1) + 6*pow(ln(x),2\
      )*pow(NC,-1)*x + 6*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 6*pow(ln(x),2)*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) - 6*pow(ln(x),2)*pow(NC,-1)*pow(x,2) - 7./4.*pow(ln(x),2)*NC*pow(z,-1)\
       - 7./4.*pow(ln(x),2)*NC*pow(omz,-1) + 7./2.*pow(ln(x),2)*NC + 7./2.*pow(ln(x),2)*NC*x*pow(\
      z,-1) + 7./2.*pow(ln(x),2)*NC*x*pow(omz,-1) - 7*pow(ln(x),2)*NC*x - 7./2.*pow(ln(x),2)*NC*\
      pow(x,2)*pow(z,-1) - 7./2.*pow(ln(x),2)*NC*pow(x,2)*pow(omz,-1) + 7*pow(ln(x),2)*NC*pow(x,2)\
       - 13./2.*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1) - 7*ln(x)*ln(z)*pow(NC,-1)*pow(omz,-1) + 9./2.*ln(\
      x)*ln(z)*pow(NC,-1) + 13*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1) + 14*ln(x)*ln(z)*pow(NC,-1)*x*\
      pow(omz,-1) - 9*ln(x)*ln(z)*pow(NC,-1)*x - 9*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 9*\
      ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1)
                result +=  + 9*ln(x)*ln(z)*pow(NC,-1)*pow(x,2) + 3*ln(x)*ln(z)*NC*pow(z,-1) + 3*ln(x)*ln(z)*NC*\
      pow(omz,-1) - 6*ln(x)*ln(z)*NC - 6*ln(x)*ln(z)*NC*x*pow(z,-1) - 6*ln(x)*ln(z)*NC*x*pow(\
      omz,-1) + 12*ln(x)*ln(z)*NC*x + 6*ln(x)*ln(z)*NC*pow(x,2)*pow(z,-1) + 6*ln(x)*ln(z)*NC*pow(\
      x,2)*pow(omz,-1) - 12*ln(x)*ln(z)*NC*pow(x,2) - 15./2.*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1) - \
      15./2.*ln(x)*ln(omx)*pow(NC,-1)*pow(omz,-1) + 5*ln(x)*ln(omx)*pow(NC,-1) + 15*ln(x)*ln(omx)*\
      pow(NC,-1)*x*pow(z,-1) + 15*ln(x)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) - 10*ln(x)*ln(omx)*pow(\
      NC,-1)*x - 10*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 10*ln(x)*ln(omx)*pow(NC,-1)*pow(\
      x,2)*pow(omz,-1) + 10*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2) + 3./2.*ln(x)*ln(omx)*NC*pow(z,-1) + \
      3./2.*ln(x)*ln(omx)*NC*pow(omz,-1) - 3*ln(x)*ln(omx)*NC - 3*ln(x)*ln(omx)*NC*x*pow(z,-1) - 3*\
      ln(x)*ln(omx)*NC*x*pow(omz,-1) + 6*ln(x)*ln(omx)*NC*x + 3*ln(x)*ln(omx)*NC*pow(x,2)*pow(z,-1)\
       + 3*ln(x)*ln(omx)*NC*pow(x,2)*pow(omz,-1) - 6*ln(x)*ln(omx)*NC*pow(x,2) - 7*ln(x)*ln(omz)*\
      pow(NC,-1)*pow(z,-1) - 13./2.*ln(x)*ln(omz)*pow(NC,-1)*pow(omz,-1) + 9./2.*ln(x)*ln(omz)*pow(\
      NC,-1) + 14*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1) + 13*ln(x)*ln(omz)*pow(NC,-1)*x*pow(omz,-1)\
       - 9*ln(x)*ln(omz)*pow(NC,-1)*x - 9*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 9*ln(x)*ln(\
      omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 9*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2) + 3*ln(x)*ln(omz)*\
      NC*pow(z,-1)
                result +=  + 3*ln(x)*ln(omz)*NC*pow(omz,-1) - 6*ln(x)*ln(omz)*NC - 6*ln(x)*ln(omz)*NC*x*pow(\
      z,-1) - 6*ln(x)*ln(omz)*NC*x*pow(omz,-1) + 12*ln(x)*ln(omz)*NC*x + 6*ln(x)*ln(omz)*NC*pow(\
      x,2)*pow(z,-1) + 6*ln(x)*ln(omz)*NC*pow(x,2)*pow(omz,-1) - 12*ln(x)*ln(omz)*NC*pow(x,2) + 1./\
      2.*ln(x)*ln(xmz)*pow(NC,-1)*pow(z,-1) + ln(x)*ln(xmz)*pow(NC,-1)*pow(omz,-1) - 1./2.*ln(x)*\
      ln(xmz)*pow(NC,-1) - ln(x)*ln(xmz)*pow(NC,-1)*x*pow(z,-1) - 2*ln(x)*ln(xmz)*pow(NC,-1)*x*pow(\
      omz,-1) + ln(x)*ln(xmz)*pow(NC,-1)*x + ln(x)*ln(xmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + ln(x)*\
      ln(xmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*ln(xmz)*pow(NC,-1)*pow(x,2) - 1./2.*ln(x)*ln(\
      xmz)*NC*pow(z,-1) - 1./2.*ln(x)*ln(xmz)*NC*pow(omz,-1) + ln(x)*ln(xmz)*NC + ln(x)*ln(xmz)*NC*\
      x*pow(z,-1) + ln(x)*ln(xmz)*NC*x*pow(omz,-1) - 2*ln(x)*ln(xmz)*NC*x - ln(x)*ln(xmz)*NC*pow(\
      x,2)*pow(z,-1) - ln(x)*ln(xmz)*NC*pow(x,2)*pow(omz,-1) + 2*ln(x)*ln(xmz)*NC*pow(x,2) + ln(z)*\
      pow(NC,-1)*pow(z,-1) + 1./2.*ln(z)*pow(NC,-1)*pow(omz,-1) - 3./2.*ln(z)*pow(NC,-1) + ln(z)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(z)*NC*pow(z,-1)\
       - ln(z)*NC*pow(omz,-1) + 3*ln(z)*NC + 4*ln(z)*NC*x - 4*ln(z)*NC*pow(x,2) + 3./2.*pow(ln(z),2\
      )*pow(NC,-1)*pow(z,-1) + 9./4.*pow(ln(z),2)*pow(NC,-1)*pow(omz,-1) - 5./4.*pow(ln(z),2)*pow(\
      NC,-1) - 3*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1) - 9./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(omz,-1)\
       + 5./2.*pow(ln(z),2)*pow(NC,-1)*x
                result +=  + 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 5./2.*pow(ln(z),2)*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) - 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2) - pow(ln(z),2)*NC*pow(z,-1) - \
      pow(ln(z),2)*NC*pow(omz,-1) + 2*pow(ln(z),2)*NC + 2*pow(ln(z),2)*NC*x*pow(z,-1) + 2*pow(ln(z)\
      ,2)*NC*x*pow(omz,-1) - 4*pow(ln(z),2)*NC*x - 2*pow(ln(z),2)*NC*pow(x,2)*pow(z,-1) - 2*pow(ln(\
      z),2)*NC*pow(x,2)*pow(omz,-1) + 4*pow(ln(z),2)*NC*pow(x,2) + 4*ln(z)*ln(omx)*pow(NC,-1)*pow(\
      z,-1) + 5*ln(z)*ln(omx)*pow(NC,-1)*pow(omz,-1) - 3*ln(z)*ln(omx)*pow(NC,-1) - 8*ln(z)*ln(omx)\
      *pow(NC,-1)*x*pow(z,-1) - 10*ln(z)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) + 6*ln(z)*ln(omx)*pow(\
      NC,-1)*x + 6*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 6*ln(z)*ln(omx)*pow(NC,-1)*pow(\
      x,2)*pow(omz,-1) - 6*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2) - ln(z)*ln(omx)*NC*pow(z,-1) - ln(z)*\
      ln(omx)*NC*pow(omz,-1) + 2*ln(z)*ln(omx)*NC + 2*ln(z)*ln(omx)*NC*x*pow(z,-1) + 2*ln(z)*ln(omx\
      )*NC*x*pow(omz,-1) - 4*ln(z)*ln(omx)*NC*x - 2*ln(z)*ln(omx)*NC*pow(x,2)*pow(z,-1) - 2*ln(z)*\
      ln(omx)*NC*pow(x,2)*pow(omz,-1) + 4*ln(z)*ln(omx)*NC*pow(x,2) + 4*ln(z)*ln(omz)*pow(NC,-1)*\
      pow(z,-1) + 7./2.*ln(z)*ln(omz)*pow(NC,-1)*pow(omz,-1) - 5./2.*ln(z)*ln(omz)*pow(NC,-1) - 8*\
      ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 7*ln(z)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) + 5*ln(z)*ln(\
      omz)*pow(NC,-1)*x + 5*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 5*ln(z)*ln(omz)*pow(\
      NC,-1)*pow(x,2)*pow(omz,-1)
                result +=  - 5*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2) - 5./2.*ln(z)*ln(omz)*NC*pow(z,-1) - 5./2.*ln(z\
      )*ln(omz)*NC*pow(omz,-1) + 5*ln(z)*ln(omz)*NC + 5*ln(z)*ln(omz)*NC*x*pow(z,-1) + 5*ln(z)*ln(\
      omz)*NC*x*pow(omz,-1) - 10*ln(z)*ln(omz)*NC*x - 5*ln(z)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 5*ln(\
      z)*ln(omz)*NC*pow(x,2)*pow(omz,-1) + 10*ln(z)*ln(omz)*NC*pow(x,2) - 1./2.*ln(z)*ln(xmz)*pow(\
      NC,-1)*pow(z,-1) - ln(z)*ln(xmz)*pow(NC,-1)*pow(omz,-1) + 1./2.*ln(z)*ln(xmz)*pow(NC,-1) + \
      ln(z)*ln(xmz)*pow(NC,-1)*x*pow(z,-1) + 2*ln(z)*ln(xmz)*pow(NC,-1)*x*pow(omz,-1) - ln(z)*ln(\
      xmz)*pow(NC,-1)*x - ln(z)*ln(xmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(z)*ln(xmz)*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) + ln(z)*ln(xmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(z)*ln(xmz)*NC*pow(z,-1)\
       + 1./2.*ln(z)*ln(xmz)*NC*pow(omz,-1) - ln(z)*ln(xmz)*NC - ln(z)*ln(xmz)*NC*x*pow(z,-1) - ln(\
      z)*ln(xmz)*NC*x*pow(omz,-1) + 2*ln(z)*ln(xmz)*NC*x + ln(z)*ln(xmz)*NC*pow(x,2)*pow(z,-1) + \
      ln(z)*ln(xmz)*NC*pow(x,2)*pow(omz,-1) - 2*ln(z)*ln(xmz)*NC*pow(x,2) + ln(omx)*pow(NC,-1)*pow(\
      z,-1) + ln(omx)*pow(NC,-1)*pow(omz,-1) - 2*ln(omx)*pow(NC,-1) + 2*ln(omx)*pow(NC,-1)*pow(x,2)\
      *pow(z,-1) + 2*ln(omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 1./2.*ln(omx)*NC*pow(z,-1) - 1./2.*\
      ln(omx)*NC*pow(omz,-1) + 3./2.*ln(omx)*NC + 2*ln(omx)*NC*x - 2*ln(omx)*NC*pow(x,2) + 3*pow(\
      ln(omx),2)*pow(NC,-1)*pow(z,-1) + 3*pow(ln(omx),2)*pow(NC,-1)*pow(omz,-1) - 2*pow(ln(omx),2)*\
      pow(NC,-1)
                result +=  - 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1) - 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(omz,-1)\
       + 4*pow(ln(omx),2)*pow(NC,-1)*x + 4*pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 4*pow(ln(\
      omx),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 4*pow(ln(omx),2)*pow(NC,-1)*pow(x,2) - 1./4.*pow(\
      ln(omx),2)*NC*pow(z,-1) - 1./4.*pow(ln(omx),2)*NC*pow(omz,-1) + 1./2.*pow(ln(omx),2)*NC + 1./\
      2.*pow(ln(omx),2)*NC*x*pow(z,-1) + 1./2.*pow(ln(omx),2)*NC*x*pow(omz,-1) - pow(ln(omx),2)*NC*\
      x - 1./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(z,-1) - 1./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(omz,-1)\
       + pow(ln(omx),2)*NC*pow(x,2) + 5*ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1) + 4*ln(omx)*ln(omz)*\
      pow(NC,-1)*pow(omz,-1) - 3*ln(omx)*ln(omz)*pow(NC,-1) - 10*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(\
      z,-1) - 8*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) + 6*ln(omx)*ln(omz)*pow(NC,-1)*x + 6*ln(\
      omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 6*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) - 6*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2) - ln(omx)*ln(omz)*NC*pow(z,-1) - ln(omx)*ln(\
      omz)*NC*pow(omz,-1) + 2*ln(omx)*ln(omz)*NC + 2*ln(omx)*ln(omz)*NC*x*pow(z,-1) + 2*ln(omx)*ln(\
      omz)*NC*x*pow(omz,-1) - 4*ln(omx)*ln(omz)*NC*x - 2*ln(omx)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 2*\
      ln(omx)*ln(omz)*NC*pow(x,2)*pow(omz,-1) + 4*ln(omx)*ln(omz)*NC*pow(x,2) + 1./2.*ln(omz)*pow(\
      NC,-1)*pow(z,-1) + ln(omz)*pow(NC,-1)*pow(omz,-1) - 3./2.*ln(omz)*pow(NC,-1) + 2*ln(omz)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)
                result +=  + ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(omz)*NC*pow(z,-1) - ln(omz)*NC*pow(\
      omz,-1) + 3*ln(omz)*NC + 4*ln(omz)*NC*x - 4*ln(omz)*NC*pow(x,2) - ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*pow(z,-1) - 1./2.*ln(omz)*ln( - omxmz)*pow(NC,-1)*pow(omz,-1) + 1./2.*ln(omz)*ln( - \
      omxmz)*pow(NC,-1) + 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*x*pow(z,-1) + ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*x*pow(omz,-1) - ln(omz)*ln( - omxmz)*pow(NC,-1)*x - ln(omz)*ln( - omxmz)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1) - ln(omz)*ln( - omxmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + ln(omz)*ln( - \
      omxmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(omz)*ln( - omxmz)*NC*pow(z,-1) + 1./2.*ln(omz)*ln( - \
      omxmz)*NC*pow(omz,-1) - ln(omz)*ln( - omxmz)*NC - ln(omz)*ln( - omxmz)*NC*x*pow(z,-1) - ln(\
      omz)*ln( - omxmz)*NC*x*pow(omz,-1) + 2*ln(omz)*ln( - omxmz)*NC*x + ln(omz)*ln( - omxmz)*NC*\
      pow(x,2)*pow(z,-1) + ln(omz)*ln( - omxmz)*NC*pow(x,2)*pow(omz,-1) - 2*ln(omz)*ln( - omxmz)*NC\
      *pow(x,2) + 9./4.*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1) + 3./2.*pow(ln(omz),2)*pow(NC,-1)*pow(\
      omz,-1) - 5./4.*pow(ln(omz),2)*pow(NC,-1) - 9./2.*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1) - 3*\
      pow(ln(omz),2)*pow(NC,-1)*x*pow(omz,-1) + 5./2.*pow(ln(omz),2)*pow(NC,-1)*x + 5./2.*pow(ln(\
      omz),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 5./2.*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       - 5./2.*pow(ln(omz),2)*pow(NC,-1)*pow(x,2) - pow(ln(omz),2)*NC*pow(z,-1) - pow(ln(omz),2)*NC\
      *pow(omz,-1)
                result +=  + 2*pow(ln(omz),2)*NC + 2*pow(ln(omz),2)*NC*x*pow(z,-1) + 2*pow(ln(omz),2)*NC*x*pow(\
      omz,-1) - 4*pow(ln(omz),2)*NC*x - 2*pow(ln(omz),2)*NC*pow(x,2)*pow(z,-1) - 2*pow(ln(omz),2)*\
      NC*pow(x,2)*pow(omz,-1) + 4*pow(ln(omz),2)*NC*pow(x,2) - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*\
      pow(NC,-1)*pow(z,-1) - 1./2.*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(omz,-1) + 1./2.*\
      Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x\
      *pow(z,-1) + Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x*pow(omz,-1) - Li2(pow(x,-1)*pow(\
      z,-1)*omx*omz)*pow(NC,-1)*x - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)\
       - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + Li2(pow(x,-1)*pow(z,-1)\
      *omx*omz)*pow(NC,-1)*pow(x,2) - 1./2.*Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1)\
       - Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*pow(omz,-1) + 1./2.*Li2(pow(x,-1)*z*omx*pow(\
      omz,-1))*pow(NC,-1) + Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1) + 2*Li2(pow(\
      x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x*pow(omz,-1) - Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(\
      NC,-1)*x - Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(pow(x,-1)*z*\
      omx*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(omz,-1) + Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(\
      NC,-1)*pow(x,2) + Li2(pow(z,-1)*omx)*pow(NC,-1)*pow(z,-1) + 1./2.*Li2(pow(z,-1)*omx)*pow(\
      NC,-1)*pow(omz,-1)
                result +=  - 1./2.*Li2(pow(z,-1)*omx)*pow(NC,-1) - 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*x*pow(z,-1)\
       - Li2(pow(z,-1)*omx)*pow(NC,-1)*x*pow(omz,-1) + Li2(pow(z,-1)*omx)*pow(NC,-1)*x + Li2(pow(\
      z,-1)*omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + Li2(pow(z,-1)*omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       - Li2(pow(z,-1)*omx)*pow(NC,-1)*pow(x,2) + 1./2.*Li2(pow(z,-1)*omx)*NC*pow(z,-1) + 1./2.*\
      Li2(pow(z,-1)*omx)*NC*pow(omz,-1) - Li2(pow(z,-1)*omx)*NC - Li2(pow(z,-1)*omx)*NC*x*pow(z,-1)\
       - Li2(pow(z,-1)*omx)*NC*x*pow(omz,-1) + 2*Li2(pow(z,-1)*omx)*NC*x + Li2(pow(z,-1)*omx)*NC*\
      pow(x,2)*pow(z,-1) + Li2(pow(z,-1)*omx)*NC*pow(x,2)*pow(omz,-1) - 2*Li2(pow(z,-1)*omx)*NC*\
      pow(x,2) + 1./2.*Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*\
      pow(omz,-1) - 1./2.*Li2(omx*pow(omz,-1))*pow(NC,-1) - Li2(omx*pow(omz,-1))*pow(NC,-1)*x*pow(\
      z,-1) - 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*x*pow(omz,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*x\
       + Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(\
      x,2)*pow(omz,-1) - Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(x,2) + 1./2.*Li2(omx*pow(omz,-1))*NC*\
      pow(z,-1) + 1./2.*Li2(omx*pow(omz,-1))*NC*pow(omz,-1) - Li2(omx*pow(omz,-1))*NC - Li2(omx*\
      pow(omz,-1))*NC*x*pow(z,-1) - Li2(omx*pow(omz,-1))*NC*x*pow(omz,-1) + 2*Li2(omx*pow(omz,-1))*\
      NC*x + Li2(omx*pow(omz,-1))*NC*pow(x,2)*pow(z,-1) + Li2(omx*pow(omz,-1))*NC*pow(x,2)*pow(\
      omz,-1)
                result +=  - 2*Li2(omx*pow(omz,-1))*NC*pow(x,2) - 1./2.*Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(\
      z,-1) - 1./2.*Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(omz,-1) + Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*NC + Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*x*pow(z,-1) + Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*NC*x*pow(omz,-1) - 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*x - Li2(x*pow(z,-1)*omx*\
      pow(omz,-1))*NC*pow(x,2)*pow(z,-1) - Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(x,2)*pow(omz,-1)\
       + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(x,2) + 1./2.*Li2(z)*pow(NC,-1)*pow(z,-1) - 1./2.\
      *Li2(z)*pow(NC,-1)*pow(omz,-1) - Li2(z)*pow(NC,-1)*x*pow(z,-1) + Li2(z)*pow(NC,-1)*x*pow(\
      omz,-1)
            if z < 1.-x and z > x:
                result += 3./2.*pow(NC,-1)*pow(z,-1) - 11./12.*pow(NC,-1)*pow(z,-1)*pow(pi,2) + 3./2.*pow(NC,-1)*\
      pow(omz,-1) - 5./6.*pow(NC,-1)*pow(pi,2)*pow(omz,-1) + 7./12.*pow(NC,-1)*pow(pi,2) + 11./6.*\
      pow(NC,-1)*x*pow(z,-1)*pow(pi,2) + 5./3.*pow(NC,-1)*x*pow(pi,2)*pow(omz,-1) - 7./6.*pow(\
      NC,-1)*x*pow(pi,2) - pow(NC,-1)*pow(x,2)*pow(z,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      pi,2) - pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(omz,-1) + 7.\
      /6.*pow(NC,-1)*pow(x,2)*pow(pi,2) + 5./12.*NC*pow(z,-1)*pow(pi,2) - 2*NC + 5./12.*NC*pow(\
      pi,2)*pow(omz,-1) - 5./6.*NC*pow(pi,2) - 5./6.*NC*x*pow(z,-1)*pow(pi,2) - 2*NC*x - 5./6.*NC*x\
      *pow(pi,2)*pow(omz,-1) + 5./3.*NC*x*pow(pi,2) + 5./6.*NC*pow(x,2)*pow(z,-1)*pow(pi,2) + 2*NC*\
      pow(x,2) + 5./6.*NC*pow(x,2)*pow(pi,2)*pow(omz,-1) - 5./3.*NC*pow(x,2)*pow(pi,2) - 3./2.*ln(x\
      )*pow(NC,-1)*pow(z,-1) - 3./2.*ln(x)*pow(NC,-1)*pow(omz,-1) + 3*ln(x)*pow(NC,-1) - 3*ln(x)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) - 3*ln(x)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 3./2.*ln(x)*NC*pow(\
      z,-1) + 3./2.*ln(x)*NC*pow(omz,-1) - 9./2.*ln(x)*NC - 6*ln(x)*NC*x + 6*ln(x)*NC*pow(x,2) + 1./\
      2.*ln(x)*ln( - xmz)*pow(NC,-1)*pow(z,-1) + ln(x)*ln( - xmz)*pow(NC,-1)*pow(omz,-1) - 1./2.*\
      ln(x)*ln( - xmz)*pow(NC,-1) - ln(x)*ln( - xmz)*pow(NC,-1)*x*pow(z,-1) - 2*ln(x)*ln( - xmz)*\
      pow(NC,-1)*x*pow(omz,-1) + ln(x)*ln( - xmz)*pow(NC,-1)*x + ln(x)*ln( - xmz)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)
                result +=  + ln(x)*ln( - xmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*ln( - xmz)*pow(NC,-1)*pow(\
      x,2) - 1./2.*ln(x)*ln( - xmz)*NC*pow(z,-1) - 1./2.*ln(x)*ln( - xmz)*NC*pow(omz,-1) + ln(x)*\
      ln( - xmz)*NC + ln(x)*ln( - xmz)*NC*x*pow(z,-1) + ln(x)*ln( - xmz)*NC*x*pow(omz,-1) - 2*ln(x)\
      *ln( - xmz)*NC*x - ln(x)*ln( - xmz)*NC*pow(x,2)*pow(z,-1) - ln(x)*ln( - xmz)*NC*pow(x,2)*pow(\
      omz,-1) + 2*ln(x)*ln( - xmz)*NC*pow(x,2) + 21./4.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1) + 21./4.*\
      pow(ln(x),2)*pow(NC,-1)*pow(omz,-1) - 7./2.*pow(ln(x),2)*pow(NC,-1) - 21./2.*pow(ln(x),2)*\
      pow(NC,-1)*x*pow(z,-1) - 21./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(omz,-1) + 7*pow(ln(x),2)*pow(\
      NC,-1)*x + 7*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 7*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*\
      pow(omz,-1) - 7*pow(ln(x),2)*pow(NC,-1)*pow(x,2) - 7./4.*pow(ln(x),2)*NC*pow(z,-1) - 7./4.*\
      pow(ln(x),2)*NC*pow(omz,-1) + 7./2.*pow(ln(x),2)*NC + 7./2.*pow(ln(x),2)*NC*x*pow(z,-1) + 7./\
      2.*pow(ln(x),2)*NC*x*pow(omz,-1) - 7*pow(ln(x),2)*NC*x - 7./2.*pow(ln(x),2)*NC*pow(x,2)*pow(\
      z,-1) - 7./2.*pow(ln(x),2)*NC*pow(x,2)*pow(omz,-1) + 7*pow(ln(x),2)*NC*pow(x,2) - 6*ln(x)*ln(\
      z)*pow(NC,-1)*pow(z,-1) - 15./2.*ln(x)*ln(z)*pow(NC,-1)*pow(omz,-1) + 9./2.*ln(x)*ln(z)*pow(\
      NC,-1) + 12*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1) + 15*ln(x)*ln(z)*pow(NC,-1)*x*pow(omz,-1) - 9*\
      ln(x)*ln(z)*pow(NC,-1)*x - 9*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 9*ln(x)*ln(z)*pow(\
      NC,-1)*pow(x,2)*pow(omz,-1)
                result +=  + 9*ln(x)*ln(z)*pow(NC,-1)*pow(x,2) + 3*ln(x)*ln(z)*NC*pow(z,-1) + 3*ln(x)*ln(z)*NC*\
      pow(omz,-1) - 6*ln(x)*ln(z)*NC - 6*ln(x)*ln(z)*NC*x*pow(z,-1) - 6*ln(x)*ln(z)*NC*x*pow(\
      omz,-1) + 12*ln(x)*ln(z)*NC*x + 6*ln(x)*ln(z)*NC*pow(x,2)*pow(z,-1) + 6*ln(x)*ln(z)*NC*pow(\
      x,2)*pow(omz,-1) - 12*ln(x)*ln(z)*NC*pow(x,2) - 9*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1) - 9*ln(x\
      )*ln(omx)*pow(NC,-1)*pow(omz,-1) + 6*ln(x)*ln(omx)*pow(NC,-1) + 18*ln(x)*ln(omx)*pow(NC,-1)*x\
      *pow(z,-1) + 18*ln(x)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) - 12*ln(x)*ln(omx)*pow(NC,-1)*x - 12*\
      ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 12*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) + 12*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2) + 3./2.*ln(x)*ln(omx)*NC*pow(z,-1) + 3./2.*ln(\
      x)*ln(omx)*NC*pow(omz,-1) - 3*ln(x)*ln(omx)*NC - 3*ln(x)*ln(omx)*NC*x*pow(z,-1) - 3*ln(x)*ln(\
      omx)*NC*x*pow(omz,-1) + 6*ln(x)*ln(omx)*NC*x + 3*ln(x)*ln(omx)*NC*pow(x,2)*pow(z,-1) + 3*ln(x\
      )*ln(omx)*NC*pow(x,2)*pow(omz,-1) - 6*ln(x)*ln(omx)*NC*pow(x,2) - 15./2.*ln(x)*ln(omz)*pow(\
      NC,-1)*pow(z,-1) - 6*ln(x)*ln(omz)*pow(NC,-1)*pow(omz,-1) + 9./2.*ln(x)*ln(omz)*pow(NC,-1) + \
      15*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1) + 12*ln(x)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) - 9*ln(x)\
      *ln(omz)*pow(NC,-1)*x - 9*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 9*ln(x)*ln(omz)*pow(\
      NC,-1)*pow(x,2)*pow(omz,-1) + 9*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2) + 3*ln(x)*ln(omz)*NC*pow(\
      z,-1)
                result +=  + 3*ln(x)*ln(omz)*NC*pow(omz,-1) - 6*ln(x)*ln(omz)*NC - 6*ln(x)*ln(omz)*NC*x*pow(\
      z,-1) - 6*ln(x)*ln(omz)*NC*x*pow(omz,-1) + 12*ln(x)*ln(omz)*NC*x + 6*ln(x)*ln(omz)*NC*pow(\
      x,2)*pow(z,-1) + 6*ln(x)*ln(omz)*NC*pow(x,2)*pow(omz,-1) - 12*ln(x)*ln(omz)*NC*pow(x,2) + ln(\
      x)*ln(omxmz)*pow(NC,-1)*pow(z,-1) + 1./2.*ln(x)*ln(omxmz)*pow(NC,-1)*pow(omz,-1) - 1./2.*ln(x\
      )*ln(omxmz)*pow(NC,-1) - 2*ln(x)*ln(omxmz)*pow(NC,-1)*x*pow(z,-1) - ln(x)*ln(omxmz)*pow(\
      NC,-1)*x*pow(omz,-1) + ln(x)*ln(omxmz)*pow(NC,-1)*x + ln(x)*ln(omxmz)*pow(NC,-1)*pow(x,2)*\
      pow(z,-1) + ln(x)*ln(omxmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*ln(omxmz)*pow(NC,-1)*pow(\
      x,2) - 1./2.*ln(x)*ln(omxmz)*NC*pow(z,-1) - 1./2.*ln(x)*ln(omxmz)*NC*pow(omz,-1) + ln(x)*ln(\
      omxmz)*NC + ln(x)*ln(omxmz)*NC*x*pow(z,-1) + ln(x)*ln(omxmz)*NC*x*pow(omz,-1) - 2*ln(x)*ln(\
      omxmz)*NC*x - ln(x)*ln(omxmz)*NC*pow(x,2)*pow(z,-1) - ln(x)*ln(omxmz)*NC*pow(x,2)*pow(omz,-1)\
       + 2*ln(x)*ln(omxmz)*NC*pow(x,2) + ln(z)*pow(NC,-1)*pow(z,-1) + 1./2.*ln(z)*pow(NC,-1)*pow(\
      omz,-1) - 3./2.*ln(z)*pow(NC,-1) + ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(z)*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) - ln(z)*NC*pow(z,-1) - ln(z)*NC*pow(omz,-1) + 3*ln(z)*NC + 4*ln(z)*NC*x\
       - 4*ln(z)*NC*pow(x,2) - 1./2.*ln(z)*ln( - xmz)*pow(NC,-1)*pow(z,-1) - ln(z)*ln( - xmz)*pow(\
      NC,-1)*pow(omz,-1) + 1./2.*ln(z)*ln( - xmz)*pow(NC,-1) + ln(z)*ln( - xmz)*pow(NC,-1)*x*pow(\
      z,-1)
                result +=  + 2*ln(z)*ln( - xmz)*pow(NC,-1)*x*pow(omz,-1) - ln(z)*ln( - xmz)*pow(NC,-1)*x - ln(z)\
      *ln( - xmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(z)*ln( - xmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       + ln(z)*ln( - xmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(z)*ln( - xmz)*NC*pow(z,-1) + 1./2.*ln(z)*\
      ln( - xmz)*NC*pow(omz,-1) - ln(z)*ln( - xmz)*NC - ln(z)*ln( - xmz)*NC*x*pow(z,-1) - ln(z)*ln(\
       - xmz)*NC*x*pow(omz,-1) + 2*ln(z)*ln( - xmz)*NC*x + ln(z)*ln( - xmz)*NC*pow(x,2)*pow(z,-1)\
       + ln(z)*ln( - xmz)*NC*pow(x,2)*pow(omz,-1) - 2*ln(z)*ln( - xmz)*NC*pow(x,2) + 7./4.*pow(ln(z\
      ),2)*pow(NC,-1)*pow(z,-1) + 11./4.*pow(ln(z),2)*pow(NC,-1)*pow(omz,-1) - 3./2.*pow(ln(z),2)*\
      pow(NC,-1) - 7./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1) - 11./2.*pow(ln(z),2)*pow(NC,-1)*x*\
      pow(omz,-1) + 3*pow(ln(z),2)*pow(NC,-1)*x + 3*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 3*\
      pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 3*pow(ln(z),2)*pow(NC,-1)*pow(x,2) - 5./4.*\
      pow(ln(z),2)*NC*pow(z,-1) - 5./4.*pow(ln(z),2)*NC*pow(omz,-1) + 5./2.*pow(ln(z),2)*NC + 5./2.\
      *pow(ln(z),2)*NC*x*pow(z,-1) + 5./2.*pow(ln(z),2)*NC*x*pow(omz,-1) - 5*pow(ln(z),2)*NC*x - 5./\
      2.*pow(ln(z),2)*NC*pow(x,2)*pow(z,-1) - 5./2.*pow(ln(z),2)*NC*pow(x,2)*pow(omz,-1) + 5*pow(\
      ln(z),2)*NC*pow(x,2) + 9./2.*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1) + 6*ln(z)*ln(omx)*pow(NC,-1)*\
      pow(omz,-1) - 7./2.*ln(z)*ln(omx)*pow(NC,-1) - 9*ln(z)*ln(omx)*pow(NC,-1)*x*pow(z,-1) - 12*\
      ln(z)*ln(omx)*pow(NC,-1)*x*pow(omz,-1)
                result +=  + 7*ln(z)*ln(omx)*pow(NC,-1)*x + 7*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 7*\
      ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2) - 1./2.*\
      ln(z)*ln(omx)*NC*pow(z,-1) - 1./2.*ln(z)*ln(omx)*NC*pow(omz,-1) + ln(z)*ln(omx)*NC + ln(z)*\
      ln(omx)*NC*x*pow(z,-1) + ln(z)*ln(omx)*NC*x*pow(omz,-1) - 2*ln(z)*ln(omx)*NC*x - ln(z)*ln(omx\
      )*NC*pow(x,2)*pow(z,-1) - ln(z)*ln(omx)*NC*pow(x,2)*pow(omz,-1) + 2*ln(z)*ln(omx)*NC*pow(x,2)\
       + 5./2.*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1) + 2*ln(z)*ln(omz)*pow(NC,-1)*pow(omz,-1) - 3./2.*\
      ln(z)*ln(omz)*pow(NC,-1) - 5*ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 4*ln(z)*ln(omz)*pow(\
      NC,-1)*x*pow(omz,-1) + 3*ln(z)*ln(omz)*pow(NC,-1)*x + 3*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*\
      pow(z,-1) + 3*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 3*ln(z)*ln(omz)*pow(NC,-1)*pow(\
      x,2) - 5./2.*ln(z)*ln(omz)*NC*pow(z,-1) - 5./2.*ln(z)*ln(omz)*NC*pow(omz,-1) + 5*ln(z)*ln(omz\
      )*NC + 5*ln(z)*ln(omz)*NC*x*pow(z,-1) + 5*ln(z)*ln(omz)*NC*x*pow(omz,-1) - 10*ln(z)*ln(omz)*\
      NC*x - 5*ln(z)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 5*ln(z)*ln(omz)*NC*pow(x,2)*pow(omz,-1) + 10*\
      ln(z)*ln(omz)*NC*pow(x,2) + ln(omx)*pow(NC,-1)*pow(z,-1) + ln(omx)*pow(NC,-1)*pow(omz,-1) - 2\
      *ln(omx)*pow(NC,-1) + 2*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(omx)*pow(NC,-1)*pow(x,2)\
      *pow(omz,-1) - 1./2.*ln(omx)*NC*pow(z,-1) - 1./2.*ln(omx)*NC*pow(omz,-1) + 3./2.*ln(omx)*NC\
       + 2*ln(omx)*NC*x
                result +=  - 2*ln(omx)*NC*pow(x,2) + 3*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1) + 3*pow(ln(omx),2)*\
      pow(NC,-1)*pow(omz,-1) - 2*pow(ln(omx),2)*pow(NC,-1) - 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(\
      z,-1) - 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(omz,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*x + 4*pow(ln(\
      omx),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 4*\
      pow(ln(omx),2)*pow(NC,-1)*pow(x,2) - 3./4.*pow(ln(omx),2)*NC*pow(z,-1) - 3./4.*pow(ln(omx),2)\
      *NC*pow(omz,-1) + 3./2.*pow(ln(omx),2)*NC + 3./2.*pow(ln(omx),2)*NC*x*pow(z,-1) + 3./2.*pow(\
      ln(omx),2)*NC*x*pow(omz,-1) - 3*pow(ln(omx),2)*NC*x - 3./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(\
      z,-1) - 3./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(omz,-1) + 3*pow(ln(omx),2)*NC*pow(x,2) + 6*ln(\
      omx)*ln(omz)*pow(NC,-1)*pow(z,-1) + 9./2.*ln(omx)*ln(omz)*pow(NC,-1)*pow(omz,-1) - 7./2.*ln(\
      omx)*ln(omz)*pow(NC,-1) - 12*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 9*ln(omx)*ln(omz)*pow(\
      NC,-1)*x*pow(omz,-1) + 7*ln(omx)*ln(omz)*pow(NC,-1)*x + 7*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)\
      *pow(z,-1) + 7*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7*ln(omx)*ln(omz)*pow(NC,-1)\
      *pow(x,2) - 1./2.*ln(omx)*ln(omz)*NC*pow(z,-1) - 1./2.*ln(omx)*ln(omz)*NC*pow(omz,-1) + ln(\
      omx)*ln(omz)*NC + ln(omx)*ln(omz)*NC*x*pow(z,-1) + ln(omx)*ln(omz)*NC*x*pow(omz,-1) - 2*ln(\
      omx)*ln(omz)*NC*x - ln(omx)*ln(omz)*NC*pow(x,2)*pow(z,-1) - ln(omx)*ln(omz)*NC*pow(x,2)*pow(\
      omz,-1)
                result +=  + 2*ln(omx)*ln(omz)*NC*pow(x,2) + 1./2.*ln(omz)*pow(NC,-1)*pow(z,-1) + ln(omz)*pow(\
      NC,-1)*pow(omz,-1) - 3./2.*ln(omz)*pow(NC,-1) + 2*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + ln(\
      omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(omz)*NC*pow(z,-1) - ln(omz)*NC*pow(omz,-1) + 3*ln(\
      omz)*NC + 4*ln(omz)*NC*x - 4*ln(omz)*NC*pow(x,2) + 11./4.*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)\
       + 7./4.*pow(ln(omz),2)*pow(NC,-1)*pow(omz,-1) - 3./2.*pow(ln(omz),2)*pow(NC,-1) - 11./2.*\
      pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1) - 7./2.*pow(ln(omz),2)*pow(NC,-1)*x*pow(omz,-1) + 3*\
      pow(ln(omz),2)*pow(NC,-1)*x + 3*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 3*pow(ln(omz),\
      2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 3*pow(ln(omz),2)*pow(NC,-1)*pow(x,2) - 5./4.*pow(ln(omz)\
      ,2)*NC*pow(z,-1) - 5./4.*pow(ln(omz),2)*NC*pow(omz,-1) + 5./2.*pow(ln(omz),2)*NC + 5./2.*pow(\
      ln(omz),2)*NC*x*pow(z,-1) + 5./2.*pow(ln(omz),2)*NC*x*pow(omz,-1) - 5*pow(ln(omz),2)*NC*x - 5.\
      /2.*pow(ln(omz),2)*NC*pow(x,2)*pow(z,-1) - 5./2.*pow(ln(omz),2)*NC*pow(x,2)*pow(omz,-1) + 5*\
      pow(ln(omz),2)*NC*pow(x,2) - ln(omz)*ln(omxmz)*pow(NC,-1)*pow(z,-1) - 1./2.*ln(omz)*ln(omxmz)\
      *pow(NC,-1)*pow(omz,-1) + 1./2.*ln(omz)*ln(omxmz)*pow(NC,-1) + 2*ln(omz)*ln(omxmz)*pow(NC,-1)\
      *x*pow(z,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*x*pow(omz,-1) - ln(omz)*ln(omxmz)*pow(NC,-1)*x - \
      ln(omz)*ln(omxmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(omz)*ln(omxmz)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1)
                result +=  + ln(omz)*ln(omxmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(omz)*ln(omxmz)*NC*pow(z,-1) + 1./2.\
      *ln(omz)*ln(omxmz)*NC*pow(omz,-1) - ln(omz)*ln(omxmz)*NC - ln(omz)*ln(omxmz)*NC*x*pow(z,-1)\
       - ln(omz)*ln(omxmz)*NC*x*pow(omz,-1) + 2*ln(omz)*ln(omxmz)*NC*x + ln(omz)*ln(omxmz)*NC*pow(\
      x,2)*pow(z,-1) + ln(omz)*ln(omxmz)*NC*pow(x,2)*pow(omz,-1) - 2*ln(omz)*ln(omxmz)*NC*pow(x,2)\
       - 1./2.*Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(\
      omz,-1) + 1./2.*Li2(pow(omx,-1)*omz)*pow(NC,-1) + Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*pow(z,-1)\
       + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*pow(omz,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*x - Li2(\
      pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2)*\
      pow(omz,-1) + Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2) - 1./2.*Li2(pow(omx,-1)*omz)*NC*pow(\
      z,-1) - 1./2.*Li2(pow(omx,-1)*omz)*NC*pow(omz,-1) + Li2(pow(omx,-1)*omz)*NC + Li2(pow(omx,-1)\
      *omz)*NC*x*pow(z,-1) + Li2(pow(omx,-1)*omz)*NC*x*pow(omz,-1) - 2*Li2(pow(omx,-1)*omz)*NC*x - \
      Li2(pow(omx,-1)*omz)*NC*pow(x,2)*pow(z,-1) - Li2(pow(omx,-1)*omz)*NC*pow(x,2)*pow(omz,-1) + 2\
      *Li2(pow(omx,-1)*omz)*NC*pow(x,2) - Li2(z*pow(omx,-1))*pow(NC,-1)*pow(z,-1) - 1./2.*Li2(z*\
      pow(omx,-1))*pow(NC,-1)*pow(omz,-1) + 1./2.*Li2(z*pow(omx,-1))*pow(NC,-1) + 2*Li2(z*pow(\
      omx,-1))*pow(NC,-1)*x*pow(z,-1) + Li2(z*pow(omx,-1))*pow(NC,-1)*x*pow(omz,-1) - Li2(z*pow(\
      omx,-1))*pow(NC,-1)*x
                result +=  - Li2(z*pow(omx,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(z*pow(omx,-1))*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) + Li2(z*pow(omx,-1))*pow(NC,-1)*pow(x,2) - 1./2.*Li2(z*pow(omx,-1))*NC*\
      pow(z,-1) - 1./2.*Li2(z*pow(omx,-1))*NC*pow(omz,-1) + Li2(z*pow(omx,-1))*NC + Li2(z*pow(\
      omx,-1))*NC*x*pow(z,-1) + Li2(z*pow(omx,-1))*NC*x*pow(omz,-1) - 2*Li2(z*pow(omx,-1))*NC*x - \
      Li2(z*pow(omx,-1))*NC*pow(x,2)*pow(z,-1) - Li2(z*pow(omx,-1))*NC*pow(x,2)*pow(omz,-1) + 2*\
      Li2(z*pow(omx,-1))*NC*pow(x,2) + 1./2.*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1)\
       + Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*pow(omz,-1) - 1./2.*Li2(x*pow(z,-1)*pow(\
      omx,-1)*omz)*pow(NC,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*x*pow(z,-1) - 2*Li2(x*\
      pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*x*pow(omz,-1) + Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(\
      NC,-1)*x + Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + Li2(x*pow(z,-1)*\
      pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(\
      NC,-1)*pow(x,2) - 1./2.*Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(z,-1) - 1./2.*Li2(x*pow(z,-1)\
      *omx*pow(omz,-1))*NC*pow(omz,-1) + Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC + Li2(x*pow(z,-1)*omx*\
      pow(omz,-1))*NC*x*pow(z,-1) + Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*x*pow(omz,-1) - 2*Li2(x*\
      pow(z,-1)*omx*pow(omz,-1))*NC*x - Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(x,2)*pow(z,-1) - \
      Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(x,2)*pow(omz,-1)
                result +=  + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*NC*pow(x,2) + Li2(x*z*pow(omx,-1)*pow(omz,-1))*\
      pow(NC,-1)*pow(z,-1) + 1./2.*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*pow(omz,-1) - 1./2.*\
      Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1) - 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x\
      *pow(z,-1) - Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x*pow(omz,-1) + Li2(x*z*pow(omx,-1)*\
      pow(omz,-1))*pow(NC,-1)*x + Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) + \
      Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(omz,-1) - Li2(x*z*pow(omx,-1)*pow(\
      omz,-1))*pow(NC,-1)*pow(x,2) + 1./2.*Li2(z)*pow(NC,-1)*pow(z,-1) - 1./2.*Li2(z)*pow(NC,-1)*\
      pow(omz,-1) - Li2(z)*pow(NC,-1)*x*pow(z,-1) + Li2(z)*pow(NC,-1)*x*pow(omz,-1)
            if z > 1.-x and z > x:
                result += 3./2.*pow(NC,-1)*pow(z,-1) - 11./12.*pow(NC,-1)*pow(z,-1)*pow(pi,2) + 3./2.*pow(NC,-1)*\
      pow(omz,-1) - 5./6.*pow(NC,-1)*pow(pi,2)*pow(omz,-1) + 7./12.*pow(NC,-1)*pow(pi,2) + 11./6.*\
      pow(NC,-1)*x*pow(z,-1)*pow(pi,2) + 5./3.*pow(NC,-1)*x*pow(pi,2)*pow(omz,-1) - 7./6.*pow(\
      NC,-1)*x*pow(pi,2) - pow(NC,-1)*pow(x,2)*pow(z,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      pi,2) - pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7./6.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(omz,-1) + 7.\
      /6.*pow(NC,-1)*pow(x,2)*pow(pi,2) + 1./12.*NC*pow(z,-1)*pow(pi,2) - 2*NC + 1./12.*NC*pow(\
      pi,2)*pow(omz,-1) - 1./6.*NC*pow(pi,2) - 1./6.*NC*x*pow(z,-1)*pow(pi,2) - 2*NC*x - 1./6.*NC*x\
      *pow(pi,2)*pow(omz,-1) + 1./3.*NC*x*pow(pi,2) + 1./6.*NC*pow(x,2)*pow(z,-1)*pow(pi,2) + 2*NC*\
      pow(x,2) + 1./6.*NC*pow(x,2)*pow(pi,2)*pow(omz,-1) - 1./3.*NC*pow(x,2)*pow(pi,2) - 3./2.*ln(x\
      )*pow(NC,-1)*pow(z,-1) - 3./2.*ln(x)*pow(NC,-1)*pow(omz,-1) + 3*ln(x)*pow(NC,-1) - 3*ln(x)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) - 3*ln(x)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 3./2.*ln(x)*NC*pow(\
      z,-1) + 3./2.*ln(x)*NC*pow(omz,-1) - 9./2.*ln(x)*NC - 6*ln(x)*NC*x + 6*ln(x)*NC*pow(x,2) + \
      ln(x)*ln( - omxmz)*pow(NC,-1)*pow(z,-1) + 1./2.*ln(x)*ln( - omxmz)*pow(NC,-1)*pow(omz,-1) - 1.\
      /2.*ln(x)*ln( - omxmz)*pow(NC,-1) - 2*ln(x)*ln( - omxmz)*pow(NC,-1)*x*pow(z,-1) - ln(x)*ln(\
       - omxmz)*pow(NC,-1)*x*pow(omz,-1) + ln(x)*ln( - omxmz)*pow(NC,-1)*x + ln(x)*ln( - omxmz)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1)
                result +=  + ln(x)*ln( - omxmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*ln( - omxmz)*pow(NC,-1)*\
      pow(x,2) - 1./2.*ln(x)*ln( - omxmz)*NC*pow(z,-1) - 1./2.*ln(x)*ln( - omxmz)*NC*pow(omz,-1) + \
      ln(x)*ln( - omxmz)*NC + ln(x)*ln( - omxmz)*NC*x*pow(z,-1) + ln(x)*ln( - omxmz)*NC*x*pow(\
      omz,-1) - 2*ln(x)*ln( - omxmz)*NC*x - ln(x)*ln( - omxmz)*NC*pow(x,2)*pow(z,-1) - ln(x)*ln( - \
      omxmz)*NC*pow(x,2)*pow(omz,-1) + 2*ln(x)*ln( - omxmz)*NC*pow(x,2) + 1./2.*ln(x)*ln( - xmz)*\
      pow(NC,-1)*pow(z,-1) + ln(x)*ln( - xmz)*pow(NC,-1)*pow(omz,-1) - 1./2.*ln(x)*ln( - xmz)*pow(\
      NC,-1) - ln(x)*ln( - xmz)*pow(NC,-1)*x*pow(z,-1) - 2*ln(x)*ln( - xmz)*pow(NC,-1)*x*pow(\
      omz,-1) + ln(x)*ln( - xmz)*pow(NC,-1)*x + ln(x)*ln( - xmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + \
      ln(x)*ln( - xmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*ln( - xmz)*pow(NC,-1)*pow(x,2) - 1./\
      2.*ln(x)*ln( - xmz)*NC*pow(z,-1) - 1./2.*ln(x)*ln( - xmz)*NC*pow(omz,-1) + ln(x)*ln( - xmz)*\
      NC + ln(x)*ln( - xmz)*NC*x*pow(z,-1) + ln(x)*ln( - xmz)*NC*x*pow(omz,-1) - 2*ln(x)*ln( - xmz)\
      *NC*x - ln(x)*ln( - xmz)*NC*pow(x,2)*pow(z,-1) - ln(x)*ln( - xmz)*NC*pow(x,2)*pow(omz,-1) + 2\
      *ln(x)*ln( - xmz)*NC*pow(x,2) + 19./4.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1) + 5*pow(ln(x),2)*\
      pow(NC,-1)*pow(omz,-1) - 13./4.*pow(ln(x),2)*pow(NC,-1) - 19./2.*pow(ln(x),2)*pow(NC,-1)*x*\
      pow(z,-1) - 10*pow(ln(x),2)*pow(NC,-1)*x*pow(omz,-1) + 13./2.*pow(ln(x),2)*pow(NC,-1)*x + 13./\
      2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)
                result +=  + 13./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 13./2.*pow(ln(x),2)*pow(\
      NC,-1)*pow(x,2) - 3./2.*pow(ln(x),2)*NC*pow(z,-1) - 3./2.*pow(ln(x),2)*NC*pow(omz,-1) + 3*\
      pow(ln(x),2)*NC + 3*pow(ln(x),2)*NC*x*pow(z,-1) + 3*pow(ln(x),2)*NC*x*pow(omz,-1) - 6*pow(ln(\
      x),2)*NC*x - 3*pow(ln(x),2)*NC*pow(x,2)*pow(z,-1) - 3*pow(ln(x),2)*NC*pow(x,2)*pow(omz,-1) + \
      6*pow(ln(x),2)*NC*pow(x,2) - 7*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1) - 8*ln(x)*ln(z)*pow(NC,-1)*\
      pow(omz,-1) + 5*ln(x)*ln(z)*pow(NC,-1) + 14*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1) + 16*ln(x)*ln(\
      z)*pow(NC,-1)*x*pow(omz,-1) - 10*ln(x)*ln(z)*pow(NC,-1)*x - 10*ln(x)*ln(z)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1) - 10*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 10*ln(x)*ln(z)*pow(NC,-1)*\
      pow(x,2) + 5./2.*ln(x)*ln(z)*NC*pow(z,-1) + 5./2.*ln(x)*ln(z)*NC*pow(omz,-1) - 5*ln(x)*ln(z)*\
      NC - 5*ln(x)*ln(z)*NC*x*pow(z,-1) - 5*ln(x)*ln(z)*NC*x*pow(omz,-1) + 10*ln(x)*ln(z)*NC*x + 5*\
      ln(x)*ln(z)*NC*pow(x,2)*pow(z,-1) + 5*ln(x)*ln(z)*NC*pow(x,2)*pow(omz,-1) - 10*ln(x)*ln(z)*NC\
      *pow(x,2) - 8*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1) - 17./2.*ln(x)*ln(omx)*pow(NC,-1)*pow(\
      omz,-1) + 11./2.*ln(x)*ln(omx)*pow(NC,-1) + 16*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1) + 17*ln(x\
      )*ln(omx)*pow(NC,-1)*x*pow(omz,-1) - 11*ln(x)*ln(omx)*pow(NC,-1)*x - 11*ln(x)*ln(omx)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) - 11*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 11*ln(x)*ln(\
      omx)*pow(NC,-1)*pow(x,2)
                result +=  + 2*ln(x)*ln(omx)*NC*pow(z,-1) + 2*ln(x)*ln(omx)*NC*pow(omz,-1) - 4*ln(x)*ln(omx)*NC\
       - 4*ln(x)*ln(omx)*NC*x*pow(z,-1) - 4*ln(x)*ln(omx)*NC*x*pow(omz,-1) + 8*ln(x)*ln(omx)*NC*x\
       + 4*ln(x)*ln(omx)*NC*pow(x,2)*pow(z,-1) + 4*ln(x)*ln(omx)*NC*pow(x,2)*pow(omz,-1) - 8*ln(x)*\
      ln(omx)*NC*pow(x,2) - 13./2.*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1) - 11./2.*ln(x)*ln(omz)*pow(\
      NC,-1)*pow(omz,-1) + 4*ln(x)*ln(omz)*pow(NC,-1) + 13*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1) + \
      11*ln(x)*ln(omz)*pow(NC,-1)*x*pow(omz,-1) - 8*ln(x)*ln(omz)*pow(NC,-1)*x - 8*ln(x)*ln(omz)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) - 8*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 8*ln(x)*ln(\
      omz)*pow(NC,-1)*pow(x,2) + 5./2.*ln(x)*ln(omz)*NC*pow(z,-1) + 5./2.*ln(x)*ln(omz)*NC*pow(\
      omz,-1) - 5*ln(x)*ln(omz)*NC - 5*ln(x)*ln(omz)*NC*x*pow(z,-1) - 5*ln(x)*ln(omz)*NC*x*pow(\
      omz,-1) + 10*ln(x)*ln(omz)*NC*x + 5*ln(x)*ln(omz)*NC*pow(x,2)*pow(z,-1) + 5*ln(x)*ln(omz)*NC*\
      pow(x,2)*pow(omz,-1) - 10*ln(x)*ln(omz)*NC*pow(x,2) + ln(z)*pow(NC,-1)*pow(z,-1) + 1./2.*ln(z\
      )*pow(NC,-1)*pow(omz,-1) - 3./2.*ln(z)*pow(NC,-1) + ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*\
      ln(z)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(z)*NC*pow(z,-1) - ln(z)*NC*pow(omz,-1) + 3*ln(z)*\
      NC + 4*ln(z)*NC*x - 4*ln(z)*NC*pow(x,2) - 1./2.*ln(z)*ln( - xmz)*pow(NC,-1)*pow(z,-1) - ln(z)\
      *ln( - xmz)*pow(NC,-1)*pow(omz,-1) + 1./2.*ln(z)*ln( - xmz)*pow(NC,-1) + ln(z)*ln( - xmz)*\
      pow(NC,-1)*x*pow(z,-1)
                result +=  + 2*ln(z)*ln( - xmz)*pow(NC,-1)*x*pow(omz,-1) - ln(z)*ln( - xmz)*pow(NC,-1)*x - ln(z)\
      *ln( - xmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(z)*ln( - xmz)*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       + ln(z)*ln( - xmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(z)*ln( - xmz)*NC*pow(z,-1) + 1./2.*ln(z)*\
      ln( - xmz)*NC*pow(omz,-1) - ln(z)*ln( - xmz)*NC - ln(z)*ln( - xmz)*NC*x*pow(z,-1) - ln(z)*ln(\
       - xmz)*NC*x*pow(omz,-1) + 2*ln(z)*ln( - xmz)*NC*x + ln(z)*ln( - xmz)*NC*pow(x,2)*pow(z,-1)\
       + ln(z)*ln( - xmz)*NC*pow(x,2)*pow(omz,-1) - 2*ln(z)*ln( - xmz)*NC*pow(x,2) + 7./4.*pow(ln(z\
      ),2)*pow(NC,-1)*pow(z,-1) + 11./4.*pow(ln(z),2)*pow(NC,-1)*pow(omz,-1) - 3./2.*pow(ln(z),2)*\
      pow(NC,-1) - 7./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1) - 11./2.*pow(ln(z),2)*pow(NC,-1)*x*\
      pow(omz,-1) + 3*pow(ln(z),2)*pow(NC,-1)*x + 3*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 3*\
      pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 3*pow(ln(z),2)*pow(NC,-1)*pow(x,2) - 3./4.*\
      pow(ln(z),2)*NC*pow(z,-1) - 3./4.*pow(ln(z),2)*NC*pow(omz,-1) + 3./2.*pow(ln(z),2)*NC + 3./2.\
      *pow(ln(z),2)*NC*x*pow(z,-1) + 3./2.*pow(ln(z),2)*NC*x*pow(omz,-1) - 3*pow(ln(z),2)*NC*x - 3./\
      2.*pow(ln(z),2)*NC*pow(x,2)*pow(z,-1) - 3./2.*pow(ln(z),2)*NC*pow(x,2)*pow(omz,-1) + 3*pow(\
      ln(z),2)*NC*pow(x,2) + 9./2.*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1) + 6*ln(z)*ln(omx)*pow(NC,-1)*\
      pow(omz,-1) - 7./2.*ln(z)*ln(omx)*pow(NC,-1) - 9*ln(z)*ln(omx)*pow(NC,-1)*x*pow(z,-1) - 12*\
      ln(z)*ln(omx)*pow(NC,-1)*x*pow(omz,-1)
                result +=  + 7*ln(z)*ln(omx)*pow(NC,-1)*x + 7*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 7*\
      ln(z)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 7*ln(z)*ln(omx)*pow(NC,-1)*pow(x,2) - 3./2.*\
      ln(z)*ln(omx)*NC*pow(z,-1) - 3./2.*ln(z)*ln(omx)*NC*pow(omz,-1) + 3*ln(z)*ln(omx)*NC + 3*ln(z\
      )*ln(omx)*NC*x*pow(z,-1) + 3*ln(z)*ln(omx)*NC*x*pow(omz,-1) - 6*ln(z)*ln(omx)*NC*x - 3*ln(z)*\
      ln(omx)*NC*pow(x,2)*pow(z,-1) - 3*ln(z)*ln(omx)*NC*pow(x,2)*pow(omz,-1) + 6*ln(z)*ln(omx)*NC*\
      pow(x,2) + 7./2.*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1) + 5./2.*ln(z)*ln(omz)*pow(NC,-1)*pow(\
      omz,-1) - 2*ln(z)*ln(omz)*pow(NC,-1) - 7*ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 5*ln(z)*ln(\
      omz)*pow(NC,-1)*x*pow(omz,-1) + 4*ln(z)*ln(omz)*pow(NC,-1)*x + 4*ln(z)*ln(omz)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1) + 4*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 4*ln(z)*ln(omz)*pow(\
      NC,-1)*pow(x,2) - 2*ln(z)*ln(omz)*NC*pow(z,-1) - 2*ln(z)*ln(omz)*NC*pow(omz,-1) + 4*ln(z)*ln(\
      omz)*NC + 4*ln(z)*ln(omz)*NC*x*pow(z,-1) + 4*ln(z)*ln(omz)*NC*x*pow(omz,-1) - 8*ln(z)*ln(omz)\
      *NC*x - 4*ln(z)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 4*ln(z)*ln(omz)*NC*pow(x,2)*pow(omz,-1) + 8*\
      ln(z)*ln(omz)*NC*pow(x,2) + ln(omx)*pow(NC,-1)*pow(z,-1) + ln(omx)*pow(NC,-1)*pow(omz,-1) - 2\
      *ln(omx)*pow(NC,-1) + 2*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(omx)*pow(NC,-1)*pow(x,2)\
      *pow(omz,-1) - 1./2.*ln(omx)*NC*pow(z,-1) - 1./2.*ln(omx)*NC*pow(omz,-1) + 3./2.*ln(omx)*NC\
       + 2*ln(omx)*NC*x
                result +=  - 2*ln(omx)*NC*pow(x,2) + 3*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1) + 3*pow(ln(omx),2)*\
      pow(NC,-1)*pow(omz,-1) - 2*pow(ln(omx),2)*pow(NC,-1) - 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(\
      z,-1) - 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(omz,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*x + 4*pow(ln(\
      omx),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 4*\
      pow(ln(omx),2)*pow(NC,-1)*pow(x,2) - 1./4.*pow(ln(omx),2)*NC*pow(z,-1) - 1./4.*pow(ln(omx),2)\
      *NC*pow(omz,-1) + 1./2.*pow(ln(omx),2)*NC + 1./2.*pow(ln(omx),2)*NC*x*pow(z,-1) + 1./2.*pow(\
      ln(omx),2)*NC*x*pow(omz,-1) - pow(ln(omx),2)*NC*x - 1./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(\
      z,-1) - 1./2.*pow(ln(omx),2)*NC*pow(x,2)*pow(omz,-1) + pow(ln(omx),2)*NC*pow(x,2) + 5*ln(omx)\
      *ln(omz)*pow(NC,-1)*pow(z,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)*pow(omz,-1) - 3*ln(omx)*ln(omz)*\
      pow(NC,-1) - 10*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 8*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(\
      omz,-1) + 6*ln(omx)*ln(omz)*pow(NC,-1)*x + 6*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + \
      6*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 6*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2) - \
      ln(omx)*ln(omz)*NC*pow(z,-1) - ln(omx)*ln(omz)*NC*pow(omz,-1) + 2*ln(omx)*ln(omz)*NC + 2*ln(\
      omx)*ln(omz)*NC*x*pow(z,-1) + 2*ln(omx)*ln(omz)*NC*x*pow(omz,-1) - 4*ln(omx)*ln(omz)*NC*x - 2\
      *ln(omx)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 2*ln(omx)*ln(omz)*NC*pow(x,2)*pow(omz,-1) + 4*ln(omx\
      )*ln(omz)*NC*pow(x,2)
                result +=  + 1./2.*ln(omz)*pow(NC,-1)*pow(z,-1) + ln(omz)*pow(NC,-1)*pow(omz,-1) - 3./2.*ln(omz)\
      *pow(NC,-1) + 2*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + ln(omz)*pow(NC,-1)*pow(x,2)*pow(\
      omz,-1) - ln(omz)*NC*pow(z,-1) - ln(omz)*NC*pow(omz,-1) + 3*ln(omz)*NC + 4*ln(omz)*NC*x - 4*\
      ln(omz)*NC*pow(x,2) - ln(omz)*ln( - omxmz)*pow(NC,-1)*pow(z,-1) - 1./2.*ln(omz)*ln( - omxmz)*\
      pow(NC,-1)*pow(omz,-1) + 1./2.*ln(omz)*ln( - omxmz)*pow(NC,-1) + 2*ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*x*pow(z,-1) + ln(omz)*ln( - omxmz)*pow(NC,-1)*x*pow(omz,-1) - ln(omz)*ln( - omxmz)*\
      pow(NC,-1)*x - ln(omz)*ln( - omxmz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*pow(x,2)*pow(omz,-1) + ln(omz)*ln( - omxmz)*pow(NC,-1)*pow(x,2) + 1./2.*ln(omz)*ln( - \
      omxmz)*NC*pow(z,-1) + 1./2.*ln(omz)*ln( - omxmz)*NC*pow(omz,-1) - ln(omz)*ln( - omxmz)*NC - \
      ln(omz)*ln( - omxmz)*NC*x*pow(z,-1) - ln(omz)*ln( - omxmz)*NC*x*pow(omz,-1) + 2*ln(omz)*ln(\
       - omxmz)*NC*x + ln(omz)*ln( - omxmz)*NC*pow(x,2)*pow(z,-1) + ln(omz)*ln( - omxmz)*NC*pow(\
      x,2)*pow(omz,-1) - 2*ln(omz)*ln( - omxmz)*NC*pow(x,2) + 9./4.*pow(ln(omz),2)*pow(NC,-1)*pow(\
      z,-1) + 3./2.*pow(ln(omz),2)*pow(NC,-1)*pow(omz,-1) - 5./4.*pow(ln(omz),2)*pow(NC,-1) - 9./2.\
      *pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1) - 3*pow(ln(omz),2)*pow(NC,-1)*x*pow(omz,-1) + 5./2.*\
      pow(ln(omz),2)*pow(NC,-1)*x + 5./2.*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 5./2.*pow(\
      ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1)
                result +=  - 5./2.*pow(ln(omz),2)*pow(NC,-1)*pow(x,2) - pow(ln(omz),2)*NC*pow(z,-1) - pow(ln(omz\
      ),2)*NC*pow(omz,-1) + 2*pow(ln(omz),2)*NC + 2*pow(ln(omz),2)*NC*x*pow(z,-1) + 2*pow(ln(omz),2\
      )*NC*x*pow(omz,-1) - 4*pow(ln(omz),2)*NC*x - 2*pow(ln(omz),2)*NC*pow(x,2)*pow(z,-1) - 2*pow(\
      ln(omz),2)*NC*pow(x,2)*pow(omz,-1) + 4*pow(ln(omz),2)*NC*pow(x,2) - Li2(pow(x,-1)*pow(z,-1)*\
      omx*omz)*pow(NC,-1)*pow(z,-1) - 1./2.*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(omz,-1)\
       + 1./2.*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*\
      pow(NC,-1)*x*pow(z,-1) + Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x*pow(omz,-1) - Li2(pow(\
      x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(x,2)*\
      pow(z,-1) - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + Li2(pow(x,-1)*\
      pow(z,-1)*omx*omz)*pow(NC,-1)*pow(x,2) + 1./2.*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*pow(z,-1)\
       + 1./2.*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*pow(omz,-1) - Li2(pow(x,-1)*z*pow(omx,-1)*omz)*\
      NC - Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*x*pow(z,-1) - Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*x*\
      pow(omz,-1) + 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*x + Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*\
      pow(x,2)*pow(z,-1) + Li2(pow(x,-1)*z*pow(omx,-1)*omz)*NC*pow(x,2)*pow(omz,-1) - 2*Li2(pow(\
      x,-1)*z*pow(omx,-1)*omz)*NC*pow(x,2) + Li2(pow(z,-1)*omx)*pow(NC,-1)*pow(z,-1) + 1./2.*Li2(\
      pow(z,-1)*omx)*pow(NC,-1)*pow(omz,-1)
                result +=  - 1./2.*Li2(pow(z,-1)*omx)*pow(NC,-1) - 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*x*pow(z,-1)\
       - Li2(pow(z,-1)*omx)*pow(NC,-1)*x*pow(omz,-1) + Li2(pow(z,-1)*omx)*pow(NC,-1)*x + Li2(pow(\
      z,-1)*omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + Li2(pow(z,-1)*omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1)\
       - Li2(pow(z,-1)*omx)*pow(NC,-1)*pow(x,2) + 1./2.*Li2(pow(z,-1)*omx)*NC*pow(z,-1) + 1./2.*\
      Li2(pow(z,-1)*omx)*NC*pow(omz,-1) - Li2(pow(z,-1)*omx)*NC - Li2(pow(z,-1)*omx)*NC*x*pow(z,-1)\
       - Li2(pow(z,-1)*omx)*NC*x*pow(omz,-1) + 2*Li2(pow(z,-1)*omx)*NC*x + Li2(pow(z,-1)*omx)*NC*\
      pow(x,2)*pow(z,-1) + Li2(pow(z,-1)*omx)*NC*pow(x,2)*pow(omz,-1) - 2*Li2(pow(z,-1)*omx)*NC*\
      pow(x,2) - 1./2.*Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*\
      pow(omz,-1) + 1./2.*Li2(pow(omx,-1)*omz)*pow(NC,-1) + Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*pow(\
      z,-1) + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*pow(omz,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*x\
       - Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(\
      x,2)*pow(omz,-1) + Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2) - 1./2.*Li2(pow(omx,-1)*omz)*NC*\
      pow(z,-1) - 1./2.*Li2(pow(omx,-1)*omz)*NC*pow(omz,-1) + Li2(pow(omx,-1)*omz)*NC + Li2(pow(\
      omx,-1)*omz)*NC*x*pow(z,-1) + Li2(pow(omx,-1)*omz)*NC*x*pow(omz,-1) - 2*Li2(pow(omx,-1)*omz)*\
      NC*x - Li2(pow(omx,-1)*omz)*NC*pow(x,2)*pow(z,-1) - Li2(pow(omx,-1)*omz)*NC*pow(x,2)*pow(\
      omz,-1)
                result +=  + 2*Li2(pow(omx,-1)*omz)*NC*pow(x,2) + 1./2.*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(\
      NC,-1)*pow(z,-1) + Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*pow(omz,-1) - 1./2.*Li2(x*pow(\
      z,-1)*pow(omx,-1)*omz)*pow(NC,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*x*pow(z,-1)\
       - 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*x*pow(omz,-1) + Li2(x*pow(z,-1)*pow(omx,-1)*\
      omz)*pow(NC,-1)*x + Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + Li2(x*\
      pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*omz)\
      *pow(NC,-1)*pow(x,2) + 1./2.*Li2(z)*pow(NC,-1)*pow(z,-1) - 1./2.*Li2(z)*pow(NC,-1)*pow(\
      omz,-1) - Li2(z)*pow(NC,-1)*x*pow(z,-1) + Li2(z)*pow(NC,-1)*x*pow(omz,-1)
        elif orders == '001':
            if z != x and z != 1.-x:
                result += - 1./4.*LMUA*pow(NC,-1) - 1./8.*LMUA*pow(NC,-1)*z - 1./4.*LMUA*pow(NC,-1)*x*z + 1./4.*LMUA*pow(NC,-1)\
      *pow(x,2)*z + 1./4.*LMUA*NC + 1./8.*LMUA*NC*z + 1./4.*LMUA*NC*x*z - 1./4.*LMUA*NC*pow(x,2)*z + 1./2.*ln(omz)*LMUA*pow(NC,-1)*pow(z,-1) - 5.\
      /4.*ln(omz)*LMUA*pow(NC,-1) - 1./4.*ln(omz)*LMUA*pow(NC,-1)*z - ln(omz)*LMUA*pow(NC,-1)*x*pow(z,-1) + 5./2.*ln(\
        omz)*LMUA*pow(NC,-1)*x + 1./2.*ln(omz)*LMUA*pow(NC,-1)*x*z + ln(omz)*LMUA*pow(NC,-1)*pow(x,2)\
        *pow(z,-1) - 5./2.*ln(omz)*LMUA*pow(NC,-1)*pow(x,2) - 1./2.*ln(omz)*LMUA*pow(NC,-1)*pow(x,2)*\
        z - 1./2.*ln(omz)*LMUA*NC*pow(z,-1) + 5./4.*ln(omz)*LMUA*NC + 1./4.*ln(omz)*LMUA*NC*z + ln(\
        omz)*LMUA*NC*x*pow(z,-1) - 5./2.*ln(omz)*LMUA*NC*x - 1./2.*ln(omz)*LMUA*NC*x*z - ln(omz)*LMUA\
        *NC*pow(x,2)*pow(z,-1) + 5./2.*ln(omz)*LMUA*NC*pow(x,2) + 1./2.*ln(omz)*LMUA*NC*pow(x,2)*z - 1./4.*ln(omx)*LMUA*pow(NC,-1) - 1./4.*ln(omx)*LMUA*pow(NC,-1)*z + 1./2.*ln(\
            omx)*LMUA*pow(NC,-1)*x + 1./2.*ln(omx)*LMUA*pow(NC,-1)*x*z - 1./2.*ln(omx)*LMUA*pow(NC,-1)*\
            pow(x,2) - 1./2.*ln(omx)*LMUA*pow(NC,-1)*pow(x,2)*z + 1./4.*ln(omx)*LMUA*NC + 1./4.*ln(omx)*\
            LMUA*NC*z - 1./2.*ln(omx)*LMUA*NC*x - 1./2.*ln(omx)*LMUA*NC*x*z + 1./2.*ln(omx)*LMUA*NC*pow(\
            x,2) + 1./2.*ln(omx)*LMUA*NC*pow(x,2)*z + 1./4.*ln(x)*LMUA*pow(NC,-1) + 1./4.*ln(x)*LMUA*pow(NC,-1)\
            *z - 1./2.*ln(x)*LMUA*pow(NC,-1)*x - 1./2.*ln(x)*LMUA*pow(NC,-1)*x*z + 1./2.*ln(x)*LMUA*pow(\
            NC,-1)*pow(x,2) + 1./2.*ln(x)*LMUA*pow(NC,-1)*pow(x,2)*z - 1./4.*ln(x)*LMUA*NC - 1./4.*ln(x)*\
            LMUA*NC*z + 1./2.*ln(x)*LMUA*NC*x + 1./2.*ln(x)*LMUA*NC*x*z - 1./2.*ln(x)*LMUA*NC*pow(x,2) - \
            1./2.*ln(x)*LMUA*NC*pow(x,2)*z - 1./2.*ln(z)*LMUA*pow(NC,-1)*pow(omz,-1) + 3./4.*ln(z)*LMUA*pow(NC,-1) + 1./4.*ln(z)*LMUA\
            *pow(NC,-1)*z + ln(z)*LMUA*pow(NC,-1)*x*pow(omz,-1) - 3./2.*ln(z)*LMUA*pow(NC,-1)*x - 1./2.*\
            ln(z)*LMUA*pow(NC,-1)*x*z - ln(z)*LMUA*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 3./2.*ln(z)*LMUA*\
            pow(NC,-1)*pow(x,2) + 1./2.*ln(z)*LMUA*pow(NC,-1)*pow(x,2)*z + 1./2.*ln(z)*LMUA*NC*pow(\
            omz,-1) - 3./4.*ln(z)*LMUA*NC - 1./4.*ln(z)*LMUA*NC*z - ln(z)*LMUA*NC*x*pow(omz,-1) + 3./2.*\
            ln(z)*LMUA*NC*x + 1./2.*ln(z)*LMUA*NC*x*z + ln(z)*LMUA*NC*pow(x,2)*pow(omz,-1) - 3./2.*ln(z)*\
            LMUA*NC*pow(x,2) - 1./2.*ln(z)*LMUA*NC*pow(x,2)*z
        elif orders == '010':                
            if z != x and z != 1.-x:
                result += + 1./2.*LMUF*pow(NC,-1)*z - 1./2.*LMUF*pow(NC,-1)*x + 3./4.*LMUF*\
      pow(NC,-1)*pow(x,2) - 3./4.*LMUF*pow(NC,-1)*pow(x,2)*z - 2./3.*LMUF*NC*pow(x,-1)*pow(z,-1) + 4./3.*LMUF*\
      NC*pow(x,-1) - 17./12.*LMUF*NC*pow(z,-1) + 17./6.*LMUF*NC - 1./2.*LMUF*NC*z - 13./6.*LMUF*NC*\
      x*pow(z,-1) + 29./6.*LMUF*NC*x + 10./3.*LMUF*NC*pow(x,2)*pow(z,-1) - 89./12.*LMUF*NC*pow(x,2)\
       + 3./4.*LMUF*NC*pow(x,2)*z + 1./6.*LMUF*NF*pow(z,-1) - 1./3.*LMUF*NF - 1./3.*LMUF*NF*x*pow(\
      z,-1) + 2./3.*LMUF*NF*x + 1./3.*LMUF*NF*pow(x,2)*pow(z,-1) - 2./3.*LMUF*NF*pow(x,2) - 1./4.*ln(x)*LMUF*pow(NC,-1) \
      + 1./4.*ln(x)*LMUF*pow(NC,-1)*z - 1./2.*ln(x)*LMUF*pow(NC,-1)*x + 1./2.*ln(x)*LMUF*\
      pow(NC,-1)*x*z + 1./2.*ln(x)*LMUF*pow(NC,-1)*pow(x,2) + 1./2.*ln(x)*LMUF*pow(NC,-1)*pow(x,2)*\
      z - ln(x)*LMUF*NC*pow(z,-1) + 9./4.*ln(x)*LMUF*NC - 1./4.*ln(x)*LMUF*NC*z - 4*ln(x)*LMUF*NC*x\
      *pow(z,-1) + 17./2.*ln(x)*LMUF*NC*x - 1./2.*ln(x)*LMUF*NC*x*z - 1./2.*ln(x)*LMUF*NC*pow(x,2)\
       - 1./2.*ln(x)*LMUF*NC*pow(x,2)*z  + 1./2.*ln(z)*LMUF*pow(NC,-1)\
      *pow(omz,-1) - 1./4.*ln(z)*LMUF*pow(NC,-1) - 1./4.*ln(z)*LMUF*pow(NC,-1)*z - ln(z)*LMUF*pow(\
      NC,-1)*x*pow(omz,-1) + 1./2.*ln(z)*LMUF*pow(NC,-1)*x + 1./2.*ln(z)*LMUF*pow(NC,-1)*x*z + ln(z\
      )*LMUF*pow(NC,-1)*pow(x,2)*pow(omz,-1) - 1./2.*ln(z)*LMUF*pow(NC,-1)*pow(x,2) - 1./2.*ln(z)*\
      LMUF*pow(NC,-1)*pow(x,2)*z - 1./2.*ln(z)*LMUF*NC*pow(omz,-1) + 1./4.*ln(z)*LMUF*NC + 1./4.*\
      ln(z)*LMUF*NC*z + ln(z)*LMUF*NC*x*pow(omz,-1) - 1./2.*ln(z)*LMUF*NC*x - 1./2.*ln(z)*LMUF*NC*x*z - ln(\
        z)*LMUF*NC*pow(x,2)*pow(omz,-1) + 1./2.*ln(z)*LMUF*NC*pow(x,2) + 1./2.*ln(z)*LMUF*NC*pow(x,2)\
        *z  - 1./4.*ln(omx)*LMUF*\
        pow(NC,-1) - 1./4.*ln(omx)*LMUF*pow(NC,-1)*z + 1./2.*ln(omx)*LMUF*pow(NC,-1)*x + 1./2.*ln(omx\
        )*LMUF*pow(NC,-1)*x*z - 1./2.*ln(omx)*LMUF*pow(NC,-1)*pow(x,2) - 1./2.*ln(omx)*LMUF*pow(\
        NC,-1)*pow(x,2)*z - ln(omx)*LMUF*NC*pow(z,-1) + 9./4.*ln(omx)*LMUF*NC + 1./4.*ln(omx)*LMUF*NC\
        *z + 2*ln(omx)*LMUF*NC*x*pow(z,-1) - 9./2.*ln(omx)*LMUF*NC*x - 1./2.*ln(omx)*LMUF*NC*x*z\
        - 2*ln(omx)*LMUF*NC*pow(x,2)*pow(z,-1) + 9./2.*ln(omx)*LMUF*NC*pow(x,2) + 1./2.*ln(omx)*LMUF\
       *NC*pow(x,2)*z  - 1./4.*ln(omz)*LMUF*pow(NC,-1) - 1./4.*ln(omz)*LMUF*pow(NC,-1)*z\
       + 1./2.*ln(omz)*LMUF*pow(NC,-1)*x + 1./2.*ln(omz)*LMUF*pow(NC,-1)*x*z - 1./2.*ln(omz)*LMUF*\
      pow(NC,-1)*pow(x,2) - 1./2.*ln(omz)*LMUF*pow(NC,-1)*pow(x,2)*z + 1./4.*ln(omz)*LMUF*NC + 1./4.\
      *ln(omz)*LMUF*NC*z - 1./2.*ln(omz)*LMUF*NC*x - 1./2.*ln(omz)*LMUF*NC*x*z + 1./2.*ln(omz)*LMUF\
      *NC*pow(x,2) + 1./2.*ln(omz)*LMUF*NC*pow(x,2)*z
        elif orders == '100':
            if z != x and z != 1.-x:
                result += + 11./12.*LMUR*NC*pow(z,-1) - 11./6.*LMUR*NC - 11./6.*LMUR*NC*x*pow(z,-1) + 11./3.*LMUR*NC*x\
       + 11./6.*LMUR*NC*pow(x,2)*pow(z,-1) - 11./3.*LMUR*NC*pow(x,2) - 1./6.*LMUR*NF*pow(z,-1) + 1./\
      3.*LMUR*NF + 1./3.*LMUR*NF*x*pow(z,-1) - 2./3.*LMUR*NF*x - 1./3.*LMUR*NF*pow(x,2)*pow(z,-1)\
       + 2./3.*LMUR*NF*pow(x,2) 
        elif orders == '011':
            if z != x and z != 1.-x:
                result += + 1./4.*LMUA*LMUF*pow(NC,-1) + 1./4.*LMUA*LMUF*pow(NC,-1)*z - 1./2.*LMUA*LMUF*pow(NC,-1)*x\
       - 1./2.*LMUA*LMUF*pow(NC,-1)*x*z + 1./2.*LMUA*LMUF*pow(NC,-1)*pow(x,2) + 1./2.*LMUA*LMUF*\
      pow(NC,-1)*pow(x,2)*z - 1./4.*LMUA*LMUF*NC - 1./4.*LMUA*LMUF*NC*z + 1./2.*LMUA*LMUF*NC*x + 1./\
      2.*LMUA*LMUF*NC*x*z - 1./2.*LMUA*LMUF*NC*pow(x,2) - 1./2.*LMUA*LMUF*NC*pow(x,2)*z 
        return result
    elif rsl == 'rs':
        result = 0
        if orders == '000':
            result_r0 = 3./8.*pow(NC,-1) + 1./8.*pow(NC,-1)*pow(pi,2) + 11./8.*pow(NC,-1)*x - 1./4.*pow(NC,-1)*x*\
      pow(pi,2) - 3./8.*pow(NC,-1)*pow(x,2) + 1./3.*pow(NC,-1)*pow(x,2)*pow(pi,2) + 13./9.*NC*pow(\
      x,-1) - 59./24.*NC - 1./8.*NC*pow(pi,2) + 119./24.*NC*x + 11./12.*NC*x*pow(pi,2) - 347./72.*\
      NC*pow(x,2) - 2./3.*NC*pow(x,2)*pow(pi,2)  - 3./4.*ln(x)*pow(NC,-1) + 3*ln(x)*pow(\
      NC,-1)*x - 5./2.*ln(x)*pow(NC,-1)*pow(x,2) + 7./4.*ln(x)*NC - 3*ln(x)*NC*x + 15*ln(x)*NC*pow(\
      x,2) - ln(x)*ln(1 + x)*NC - 2*ln(x)*ln(1 + x)*\
      NC*x - 2*ln(x)*ln(1 + x)*NC*pow(x,2) - 1./4.*pow(ln(x),2)*pow(NC,-1) + 1./2.*pow(ln(x),2)*\
      pow(NC,-1)*x - pow(ln(x),2)*pow(NC,-1)*pow(x,2) - 3./4.*pow(ln(x),2)*NC - 7./2.*pow(ln(x),2)*\
      NC*x + pow(ln(x),2)*NC*pow(x,2) + ln(x)*ln(omx)*pow(NC,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*x + 2\
      *ln(x)*ln(omx)*pow(NC,-1)*pow(x,2) - 2*ln(x)*ln(omx)*NC + 4*ln(x)*ln(omx)*NC*x - 4*ln(x)*ln(\
      omx)*NC*pow(x,2) + 7./8.*ln(omx)*pow(NC,-1) - 3*ln(omx)*pow(NC,-1)*x + 5./2.*ln(omx)*pow(\
      NC,-1)*pow(x,2) + 2./3.*ln(omx)*NC*pow(x,-1) - 3./8.*ln(omx)*NC + 7*ln(omx)*NC*x - 23./3.*ln(\
      omx)*NC*pow(x,2)  - 1./2.*pow(\
      ln(omx),2)*pow(NC,-1) + pow(ln(omx),2)*pow(NC,-1)*x - pow(ln(omx),2)*pow(NC,-1)*pow(x,2) + \
      pow(ln(omx),2)*NC - 2*pow(ln(omx),2)*NC*x + 2*pow(ln(omx),2)*NC*pow(x,2) - Li2( - x)*NC - 2*\
      Li2( - x)*NC*x - 2*Li2( - x)*NC*pow(x,2) + 1./4.*Li2(x)*pow(NC,-1) - 1./2.*Li2(x)*pow(NC,-1)*\
      x - 5./4.*Li2(x)*NC - 7./2.*Li2(x)*NC*x
            result_r1 = 7./8.*pow(NC,-1) - 3*pow(NC,-1)*x + 5./2.*pow(NC,-1)*pow(x,2) + 2./3.*NC*pow(x,-1) - 3./8.*\
      NC + 7*NC*x - 23./3.*NC*pow(x,2)  + 3./4.\
      *ln(x)*pow(NC,-1) - 3./2.*ln(x)*pow(NC,-1)*x + 2*ln(x)*pow(NC,-1)*pow(x,2) + 1./4.*ln(x)*NC\
       + 11./2.*ln(x)*NC*x - 2*ln(x)*NC*pow(x,2) - ln(omx)*pow(NC,-1) + 2*ln(omx)*pow(NC,-1)*x - 2*\
      ln(omx)*pow(NC,-1)*pow(x,2) + 2*ln(omx)*NC - 4*ln(omx)*NC*x + 4*ln(omx)*NC*pow(x,2)
            result_r2 = - 3./4.*pow(NC,-1) + 3./2.*pow(NC,-1)*x - 3./2.*pow(NC,-1)*pow(x,2) + 3./4.*NC - 3./2.*NC*x + 3./2.*NC*pow(x,2)
            result += result_r0 * 1/(1-z) + result_r1 * ln(1-z)/(1-z) + result_r2 * ln(1-z)*ln(1-z)/(1-z)
        elif orders == '001':
            result_r0 = + 3./8.*LMUA*pow(NC,-1) + 1./4.*LMUA*pow(NC,-1)*x - 1./4.*\
      LMUA*pow(NC,-1)*pow(x,2) - 3./8.*LMUA*NC - 1./4.*LMUA*NC*x + 1./4.*LMUA*NC*pow(x,2) - 1./2.*ln(x)\
      *LMUA*pow(NC,-1) + ln(x)*LMUA*pow(NC,-1)*x - ln(x)*LMUA*pow(NC,-1)*pow(x,2) + 1./2.*ln(x)*\
      LMUA*NC - ln(x)*LMUA*NC*x + ln(x)*LMUA*NC*pow(x,2) + 1./2.*ln(omx)*LMUA*pow(NC,-1) - ln(omx)*LMUA*pow(NC,-1)*x + ln(omx)*LMUA*pow(NC,-1)*\
      pow(x,2) - 1./2.*ln(omx)*LMUA*NC + ln(omx)*LMUA*NC*x - ln(omx)*LMUA*NC*pow(x,2)
            result_r1 = + LMUA*pow(NC,-1) - 2*LMUA*pow(NC,-1)*x + 2*LMUA*pow(NC,-1)*pow(x,2) - LMUA*NC + 2*LMUA*NC*x - 2*LMUA*NC*pow(x,2)
            result += result_r0 * 1/(1-z) + result_r1 * ln(1-z)/(1-z)
        elif orders == '010':
            result_r0 = - 1./2.*LMUF*pow(NC,-1) + 5./4.*LMUF*pow(NC,-1)*x - 3./4.*LMUF*pow(NC,-1)*pow(x,2) - 2./3.*LMUF*NC*pow(x,-1)\
       - 11./12.*LMUF*NC - 41./12.*LMUF*NC*x + 49./12.*LMUF*NC*pow(x,2) + 1./6.*LMUF*NF - 1./3.*\
      LMUF*NF*x + 1./3.*LMUF*NF*pow(x,2) - 1./4.*ln(x)*LMUF*pow(NC,-1) + 1./2.*ln(x)*LMUF*pow(NC,-1)*x - ln(x)*LMUF*pow(NC,-1)*\
      pow(x,2) - 3./4.*ln(x)*LMUF*NC - 9./2.*ln(x)*LMUF*NC*x + ln(x)*LMUF*NC*pow(x,2)  + 1./2.*ln(omx)*LMUF*pow(NC,-1) - ln(omx)*LMUF*pow(NC,-1)*x + ln(omx)*LMUF*\
      pow(NC,-1)*pow(x,2) - 3./2.*ln(omx)*LMUF*NC + 3*ln(omx)*LMUF*NC*x - 3*ln(omx)*LMUF*NC*pow(x,2) 
            result_r1 = + 1./2.*LMUF*pow(NC,-1) - LMUF*pow(NC,-1)*x + LMUF*pow(NC,-1)*pow(x,2) - 1./2.*LMUF*NC + LMUF*NC*x - LMUF*NC*pow(x,2)
            result += result_r0 * 1/(1-z) + result_r1 * ln(1-z)/(1-z)
        elif orders == '100':
            result_r0 = + 11./12.*LMUR*NC - 11./6.*LMUR*NC*x + 11./6.*LMUR*NC*pow(x,2) - 1./6.*LMUR*NF + 1./3.*LMUR*NF*x - 1./3.*LMUR*NF*pow(x,2)
            result += result_r0 * 1/(1-z)
        elif orders == '011':
            result_r0 = - 1./2.*LMUA*LMUF*pow(NC,-1) + LMUA*LMUF*pow(NC,-1)*x - LMUA*LMUF*pow(NC,-1)*pow(x,2) + 1./2.*LMUA*LMUF*NC - LMUA*LMUF*NC*x + LMUA*LMUF*NC*pow(x,2) 
            result += result_r0 * 1/(1-z)
        return result
    elif rsl == 'rl':
        result = 0
        if orders == '000': 
            result += 17./8.*pow(NC,-1) - 4*pow(NC,-1)*zeta3 - 1./8.*pow(NC,-1)*pow(pi,2) - 81./16.*pow(NC,-1)*x\
       + 8*pow(NC,-1)*x*zeta3 + 5./12.*pow(NC,-1)*x*pow(pi,2) + 57./16.*pow(NC,-1)*pow(x,2) - 8*\
      pow(NC,-1)*pow(x,2)*zeta3 - 1./3.*pow(NC,-1)*pow(x,2)*pow(pi,2) + 52./27.*NC*pow(x,-1) - 43./\
      18.*NC + 9./4.*NC*zeta3 - 1./3.*NC*pow(rln2,3) + 7./24.*NC*pow(pi,2) + 1./6.*NC*pow(pi,2)*\
      rln2 + 1049./144.*NC*x - 13./2.*NC*x*zeta3 - 2./3.*NC*x*pow(rln2,3) - 1./4.*NC*x*pow(pi,2) + \
      1./3.*NC*x*pow(pi,2)*rln2 - 3433./432.*NC*pow(x,2) + 9./2.*NC*pow(x,2)*zeta3 - 2./3.*NC*pow(\
      x,2)*pow(rln2,3) + 29./12.*NC*pow(x,2)*pow(pi,2) + 1./3.*NC*pow(x,2)*pow(pi,2)*rln2
            result +=   + 1./2.*ln(1 + x)*NC*pow(rln2,2) + 1./12.*ln(1 + x)*NC*pow(pi,2) + ln(1 + x)*NC*x*\
      pow(rln2,2) + 1./6.*ln(1 + x)*NC*x*pow(pi,2) + ln(1 + x)*NC*pow(x,2)*pow(rln2,2) + 1./6.*ln(1\
       + x)*NC*pow(x,2)*pow(pi,2) - 1./6.*pow(ln(1 + x),3)*NC - 1./3.*pow(ln(1 + x),3)*NC*x - 1./3.\
      *pow(ln(1 + x),3)*NC*pow(x,2) - 3./4.*ln(x)*pow(NC,-1) - 1./4.*ln(x)*pow(NC,-1)*pow(pi,2) - \
      37./16.*ln(x)*pow(NC,-1)*x + 1./2.*ln(x)*pow(NC,-1)*x*pow(pi,2) + 7./8.*ln(x)*pow(NC,-1)*pow(\
      x,2) - 2./3.*ln(x)*pow(NC,-1)*pow(x,2)*pow(pi,2) + 29./6.*ln(x)*NC + 1./12.*ln(x)*NC*pow(\
      pi,2) + 143./48.*ln(x)*NC*x - 3./2.*ln(x)*NC*x*pow(pi,2) + 583./72.*ln(x)*NC*pow(x,2) + ln(x)\
      *NC*pow(x,2)*pow(pi,2)
            result +=   + ln(x)*ln(1 + x)*NC*x + ln(x)*ln(1 + x)*NC*pow(x,2)  + 7./32.*pow(ln(x),2)*\
      pow(NC,-1) - 15./8.*pow(ln(x),2)*pow(NC,-1)*x + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2) - 59./\
      32.*pow(ln(x),2)*NC + 19./8.*pow(ln(x),2)*NC*x - 137./12.*pow(ln(x),2)*NC*pow(x,2)  + pow(ln(x),2)*ln(1 + x)*NC + 2*pow(ln(x),2)*ln(1 + x)*NC*x + 2*pow(ln(x),2)\
      *ln(1 + x)*NC*pow(x,2)
            result +=  + 1./48.*pow(ln(x),3)*pow(NC,-1) - 1./24.*pow(ln(x),3)*pow(NC,-1)*x + 1./4.*pow(ln(x)\
      ,3)*pow(NC,-1)*pow(x,2) + 19./48.*pow(ln(x),3)*NC + 29./24.*pow(ln(x),3)*NC*x - 1./4.*pow(ln(\
      x),3)*NC*pow(x,2) - 3./8.*pow(ln(x),2)*ln(omx)*pow(NC,-1) + 3./4.*pow(ln(x),2)*ln(omx)*pow(\
      NC,-1)*x - 3./4.*pow(ln(x),2)*ln(omx)*pow(NC,-1)*pow(x,2) + 11./8.*pow(ln(x),2)*ln(omx)*NC - \
      11./4.*pow(ln(x),2)*ln(omx)*NC*x + 11./4.*pow(ln(x),2)*ln(omx)*NC*pow(x,2) - 7./8.*ln(x)*ln(\
      omx)*pow(NC,-1) + 7./2.*ln(x)*ln(omx)*pow(NC,-1)*x - 3*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2) - 2./\
      3.*ln(x)*ln(omx)*NC*pow(x,-1) + 3./8.*ln(x)*ln(omx)*NC - 15./2.*ln(x)*ln(omx)*NC*x + 49./6.*\
      ln(x)*ln(omx)*NC*pow(x,2)  - ln(x)*ln(omx)*ln(1 + x)*NC - 2*ln(x)*ln(omx)*ln(1\
       + x)*NC*x - 2*ln(x)*ln(omx)*ln(1 + x)*NC*pow(x,2) + ln(x)*pow(ln(omx),2)*pow(NC,-1) - 2*ln(x\
      )*pow(ln(omx),2)*pow(NC,-1)*x + 7./4.*ln(x)*pow(ln(omx),2)*pow(NC,-1)*pow(x,2) - 3./2.*ln(x)*\
      pow(ln(omx),2)*NC - 7./4.*ln(x)*pow(ln(omx),2)*NC*pow(x,2) + ln(x)*Li2( - x)*NC + 2*ln(x)*\
      Li2( - x)*NC*x + 2*ln(x)*Li2( - x)*NC*pow(x,2) - 1./2.*ln(x)*Li2(x)*pow(NC,-1) + ln(x)*Li2(x)\
      *pow(NC,-1)*x - 1./2.*ln(x)*Li2(x)*pow(NC,-1)*pow(x,2) + 5./2.*ln(x)*Li2(x)*NC + ln(x)*Li2(x)\
      *NC*x
            result +=  + 5./2.*ln(x)*Li2(x)*NC*pow(x,2) + 3./8.*ln(omx)*pow(NC,-1) + 1./12.*ln(omx)*pow(\
      NC,-1)*pow(pi,2) + 7./4.*ln(omx)*pow(NC,-1)*x - 1./6.*ln(omx)*pow(NC,-1)*x*pow(pi,2) - 7./8.*\
      ln(omx)*pow(NC,-1)*pow(x,2) + 1./4.*ln(omx)*pow(NC,-1)*pow(x,2)*pow(pi,2) + 13./9.*ln(omx)*NC\
      *pow(x,-1) - 59./24.*ln(omx)*NC + 1./2.*ln(omx)*NC*pow(rln2,2) - 1./6.*ln(omx)*NC*pow(pi,2)\
       + 16./3.*ln(omx)*NC*x + ln(omx)*NC*x*pow(rln2,2) + ln(omx)*NC*x*pow(pi,2) - 383./72.*ln(omx)\
      *NC*pow(x,2) + ln(omx)*NC*pow(x,2)*pow(rln2,2) - 3./4.*ln(omx)*NC*pow(x,2)*pow(pi,2)
            result +=   - ln(omx)*ln(1 + x)*NC*rln2 - 2*ln(omx)*ln(1 + x)*NC\
      *x*rln2 - 2*ln(omx)*ln(1 + x)*NC*pow(x,2)*rln2 + 1./2.*ln(omx)*pow(ln(1 + x),2)*NC + ln(omx)*\
      pow(ln(1 + x),2)*NC*x + ln(omx)*pow(ln(1 + x),2)*NC*pow(x,2) + 7./16.*pow(ln(omx),2)*pow(\
      NC,-1) - 7./4.*pow(ln(omx),2)*pow(NC,-1)*x + 3./2.*pow(ln(omx),2)*pow(NC,-1)*pow(x,2) + 1./3.\
      *pow(ln(omx),2)*NC*pow(x,-1) - 3./16.*pow(ln(omx),2)*NC + 13./4.*pow(ln(omx),2)*NC*x - 43./12.\
      *pow(ln(omx),2)*NC*pow(x,2)  - 5./24.*pow(ln(omx),3)*pow(NC,-1) + 5./12.*\
      pow(ln(omx),3)*pow(NC,-1)*x - 5./12.*pow(ln(omx),3)*pow(NC,-1)*pow(x,2) + 7./24.*pow(ln(omx),\
      3)*NC - 7./12.*pow(ln(omx),3)*NC*x + 7./12.*pow(ln(omx),3)*NC*pow(x,2) - ln(omx)*Li2( - x)*NC\
       - 2*ln(omx)*Li2( - x)*NC*x - 2*ln(omx)*Li2( - x)*NC*pow(x,2) + 1./2.*ln(omx)*Li2(x)*pow(\
      NC,-1) - ln(omx)*Li2(x)*pow(NC,-1)*x + 1./2.*ln(omx)*Li2(x)*pow(NC,-1)*pow(x,2) - ln(omx)*\
      Li2(x)*NC - 4*ln(omx)*Li2(x)*NC*x + 1./2.*ln(omx)*Li2(x)*NC*pow(x,2) - 1./4.*ln(opx)*NC*pow(\
      pi,2) - 1./2.*ln(opx)*NC*x*pow(pi,2) - 1./2.*ln(opx)*NC*pow(x,2)*pow(pi,2) + Li3(1./2. - 1./2.\
      *x)*NC + 2*Li3(1./2. - 1./2.*x)*NC*x + 2*Li3(1./2. - 1./2.*x)*NC*pow(x,2) + Li3(1./2. + 1./2.\
      *x)*NC
            result +=  + 2*Li3(1./2. + 1./2.*x)*NC*x + 2*Li3(1./2. + 1./2.*x)*NC*pow(x,2) + 3./2.*Li3(1 - x)\
      *pow(NC,-1) - 3*Li3(1 - x)*pow(NC,-1)*x + 5./2.*Li3(1 - x)*pow(NC,-1)*pow(x,2) - 3./2.*Li3(1\
       - x)*NC - 7*Li3(1 - x)*NC*x - 1./2.*Li3(1 - x)*NC*pow(x,2) + Li3(1/(1 + x) - 1/(1 + x)*x)*NC\
       + 2*Li3(1/(1 + x) - 1/(1 + x)*x)*NC*x + 2*Li3(1/(1 + x) - 1/(1 + x)*x)*NC*pow(x,2) + 5./4.*\
      Li3(x)*pow(NC,-1) - 5./2.*Li3(x)*pow(NC,-1)*x + 5./2.*Li3(x)*pow(NC,-1)*pow(x,2) - 9./4.*Li3(\
      x)*NC + 5./2.*Li3(x)*NC*x - 9./2.*Li3(x)*NC*pow(x,2) + Li2( - x)*NC*x + Li2( - x)*NC*pow(x,2)\
      - 1./8.*Li2(x)*pow(NC,-1) - 2./3.*Li2(x)*NC*pow(x,-1) - 11./8.*Li2(x)*NC - 4*Li2(x)*NC*x - 22./3.*Li2(x)*NC*\
      pow(x,2)
            result_r0 = 3./8.*pow(NC,-1) + 1./8.*pow(NC,-1)*pow(pi,2) + 11./8.*pow(NC,-1)*x - 1./4.*pow(NC,-1)*x*\
      pow(pi,2) - 3./8.*pow(NC,-1)*pow(x,2) + 1./3.*pow(NC,-1)*pow(x,2)*pow(pi,2) + 13./9.*NC*pow(\
      x,-1) - 59./24.*NC - 1./8.*NC*pow(pi,2) + 119./24.*NC*x + 11./12.*NC*x*pow(pi,2) - 347./72.*\
      NC*pow(x,2) - 2./3.*NC*pow(x,2)*pow(pi,2)  - 3./4.*ln(x)*pow(NC,-1) + 3*ln(x)*pow(\
      NC,-1)*x - 5./2.*ln(x)*pow(NC,-1)*pow(x,2) + 7./4.*ln(x)*NC - 3*ln(x)*NC*x + 15*ln(x)*NC*pow(\
      x,2) - ln(x)*ln(1 + x)*NC - 2*ln(x)*ln(1 + x)*\
      NC*x - 2*ln(x)*ln(1 + x)*NC*pow(x,2) - 1./4.*pow(ln(x),2)*pow(NC,-1) + 1./2.*pow(ln(x),2)*\
      pow(NC,-1)*x - pow(ln(x),2)*pow(NC,-1)*pow(x,2) - 3./4.*pow(ln(x),2)*NC - 7./2.*pow(ln(x),2)*\
      NC*x + pow(ln(x),2)*NC*pow(x,2) + ln(x)*ln(omx)*pow(NC,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*x + 2\
      *ln(x)*ln(omx)*pow(NC,-1)*pow(x,2) - 2*ln(x)*ln(omx)*NC + 4*ln(x)*ln(omx)*NC*x - 4*ln(x)*ln(\
      omx)*NC*pow(x,2) + 7./8.*ln(omx)*pow(NC,-1) - 3*ln(omx)*pow(NC,-1)*x + 5./2.*ln(omx)*pow(\
      NC,-1)*pow(x,2) + 2./3.*ln(omx)*NC*pow(x,-1) - 3./8.*ln(omx)*NC + 7*ln(omx)*NC*x - 23./3.*ln(\
      omx)*NC*pow(x,2)  - 1./2.*pow(\
      ln(omx),2)*pow(NC,-1) + pow(ln(omx),2)*pow(NC,-1)*x - pow(ln(omx),2)*pow(NC,-1)*pow(x,2) + \
      pow(ln(omx),2)*NC - 2*pow(ln(omx),2)*NC*x + 2*pow(ln(omx),2)*NC*pow(x,2) - Li2( - x)*NC - 2*\
      Li2( - x)*NC*x - 2*Li2( - x)*NC*pow(x,2) + 1./4.*Li2(x)*pow(NC,-1) - 1./2.*Li2(x)*pow(NC,-1)*\
      x - 5./4.*Li2(x)*NC - 7./2.*Li2(x)*NC*x
            result_r1 = 7./8.*pow(NC,-1) - 3*pow(NC,-1)*x + 5./2.*pow(NC,-1)*pow(x,2) + 2./3.*NC*pow(x,-1) - 3./8.*\
      NC + 7*NC*x - 23./3.*NC*pow(x,2)  + 3./4.\
      *ln(x)*pow(NC,-1) - 3./2.*ln(x)*pow(NC,-1)*x + 2*ln(x)*pow(NC,-1)*pow(x,2) + 1./4.*ln(x)*NC\
       + 11./2.*ln(x)*NC*x - 2*ln(x)*NC*pow(x,2) - ln(omx)*pow(NC,-1) + 2*ln(omx)*pow(NC,-1)*x - 2*\
      ln(omx)*pow(NC,-1)*pow(x,2) + 2*ln(omx)*NC - 4*ln(omx)*NC*x + 4*ln(omx)*NC*pow(x,2)
            result_r2 = - 3./4.*pow(NC,-1) + 3./2.*pow(NC,-1)*x - 3./2.*pow(NC,-1)*pow(x,2) + 3./4.*NC - 3./2.*NC*x + 3./2.*NC*pow(x,2)
            result += result_r0 * ln(1-z) + result_r1 * (1/2)*ln(1-z)*ln(1-z) + result_r2 * (1/3)*ln(1-z)*ln(1-z)*ln(1-z)
        elif orders == '001':
            result += - 1./12.*LMUA*pow(NC,-1)*pow(pi,2) + 3./4.*LMUA*pow(NC,-1)*x + 1./6.*LMUA*pow(NC,-1)*x*pow(pi,2) - 3./4.*\
      LMUA*pow(NC,-1)*pow(x,2) - 1./6.*LMUA*pow(NC,-1)*pow(x,2)*pow(pi,2) + 1./12.*LMUA*NC*pow(\
      pi,2) - 3./4.*LMUA*NC*x - 1./6.*LMUA*NC*x*pow(pi,2) + 3./4.*LMUA*NC*pow(x,2) + 1./6.*LMUA*NC*\
      pow(x,2)*pow(pi,2) - 3./8.*LMUA*LMUF*pow(NC,-1) + 3./4.*LMUA*LMUF*pow(NC,-1)*x - 3./4.*LMUA*\
      LMUF*pow(NC,-1)*pow(x,2) + 3./8.*LMUA*LMUF*NC - 3./4.*LMUA*LMUF*NC*x + 3./4.*LMUA*LMUF*NC*\
      pow(x,2) - 3./8.*ln(x)*LMUA*pow(NC,-1) + 3./4.*ln(x)*LMUA*pow(NC,-1)*x - 3./4.\
      *ln(x)*LMUA*pow(NC,-1)*pow(x,2) + 3./8.*ln(x)*LMUA*NC - 3./4.*ln(x)*LMUA*NC*x + 3./4.*ln(x)*\
      LMUA*NC*pow(x,2) + 3./8.*ln(omx)*LMUA*pow(NC,-1) - 3./\
      4.*ln(omx)*LMUA*pow(NC,-1)*x + 3./4.*ln(omx)*LMUA*pow(NC,-1)*pow(x,2) - 3./8.*ln(omx)*LMUA*NC\
       + 3./4.*ln(omx)*LMUA*NC*x - 3./4.*ln(omx)*LMUA*NC*pow(x,2)
            result_r0 = + 3./8.*LMUA*pow(NC,-1) + 1./4.*LMUA*pow(NC,-1)*x - 1./4.*\
      LMUA*pow(NC,-1)*pow(x,2) - 3./8.*LMUA*NC - 1./4.*LMUA*NC*x + 1./4.*LMUA*NC*pow(x,2) - 1./2.*ln(x)\
      *LMUA*pow(NC,-1) + ln(x)*LMUA*pow(NC,-1)*x - ln(x)*LMUA*pow(NC,-1)*pow(x,2) + 1./2.*ln(x)*\
      LMUA*NC - ln(x)*LMUA*NC*x + ln(x)*LMUA*NC*pow(x,2) + 1./2.*ln(omx)*LMUA*pow(NC,-1) - ln(omx)*LMUA*pow(NC,-1)*x + ln(omx)*LMUA*pow(NC,-1)*\
      pow(x,2) - 1./2.*ln(omx)*LMUA*NC + ln(omx)*LMUA*NC*x - ln(omx)*LMUA*NC*pow(x,2)
            result_r1 = + LMUA*pow(NC,-1) - 2*LMUA*pow(NC,-1)*x + 2*LMUA*pow(NC,-1)*pow(x,2) - LMUA*NC + 2*LMUA*NC*x - 2*LMUA*NC*pow(x,2)
            result += result_r0 * ln(1-z) + result_r1 * (1/2)*ln(1-z)*ln(1-z)
        elif orders == '010':
            result += - 3./8.*LMUF*pow(NC,-1) - 1./24.*LMUF*pow(NC,-1)*pow(pi,2) - 5./8.*LMUF*pow(NC,-1)*x + 1./12.*LMUF*pow(\
      NC,-1)*x*pow(pi,2) - 3./8.*LMUF*pow(NC,-1)*pow(x,2) - 1./6.*LMUF*pow(NC,-1)*pow(x,2)*pow(\
      pi,2) - 13./9.*LMUF*NC*pow(x,-1) + 59./24.*LMUF*NC + 1./24.*LMUF*NC*pow(pi,2) - 181./24.*LMUF\
      *NC*x - 3./4.*LMUF*NC*x*pow(pi,2) + 533./72.*LMUF*NC*pow(x,2) + 1./2.*LMUF*NC*pow(x,2)*pow(\
      pi,2) + 1./3.*LMUF*NF*x - 1./3.*LMUF*NF*pow(x,2) - 9./4.*ln(x)*LMUF*pow(NC,-1)*x + 7./4.*ln(x)*LMUF*pow(NC,-1)*pow(x,2)\
      - 11./24.*ln(x)*LMUF*NC + 5./12.*ln(x)*LMUF*NC*x - 149./12.*ln(x)*LMUF*NC*pow(x,2) - 1./6.*\
     ln(x)*LMUF*NF + 1./3.*ln(x)*LMUF*NF*x - 1./3.*ln(x)*LMUF*NF*pow(x,2) - 1./2.*ln(omx)*LMUF*pow(\
        NC,-1) + 9./4.*ln(omx)*LMUF*pow(NC,-1)*x - 7./4.*ln(omx)*LMUF*pow(NC,-1)*pow(x,2) - 2./3.*ln(\
        omx)*LMUF*NC*pow(x,-1) - 11./12.*ln(omx)*LMUF*NC - 53./12.*ln(omx)*LMUF*NC*x + 61./12.*ln(omx\
        )*LMUF*NC*pow(x,2) + 1./6.*ln(omx)*LMUF*NF - 1./3.*ln(omx)*LMUF*NF*x + 1./3.*ln(omx)*LMUF*NF*\
        pow(x,2) + 1./2.*pow(ln(omx),2)*LMUF*pow(NC,-1) - pow(ln(omx),2)*LMUF*pow(\
            NC,-1)*x + pow(ln(omx),2)*LMUF*pow(NC,-1)*pow(x,2) - pow(ln(omx),2)*LMUF*NC + 2*pow(ln(omx),2\
            )*LMUF*NC*x - 2*pow(ln(omx),2)*LMUF*NC*pow(x,2) + Li2( - x)*LMUF*NC + 2*Li2( - x)*LMUF*NC*x + 2*Li2( - x)*LMUF*NC*pow(x,2) \
            - 1./4.*Li2(x)*LMUF*pow(NC,-1) + 1./2.*Li2(x)*LMUF*pow(NC,-1)*x + 5./4.*Li2(x)*LMUF*\
            NC + 7./2.*Li2(x)*LMUF*NC*x + ln(x)*ln(1 + x)*LMUF*NC + 2*ln(x)*ln(1 + x)*LMUF*NC*x + 2*ln(x)*ln(1 + x)*LMUF*NC*pow(x,2) + 1./4.*\
            pow(ln(x),2)*LMUF*pow(NC,-1) - 1./2.*pow(ln(x),2)*LMUF*pow(NC,-1)*x + pow(ln(x),2)*LMUF*pow(\
            NC,-1)*pow(x,2) + 3./4.*pow(ln(x),2)*LMUF*NC + 7./2.*pow(ln(x),2)*LMUF*NC*x - pow(ln(x),2)*\
            LMUF*NC*pow(x,2) - ln(x)*ln(omx)*LMUF*pow(NC,-1) + 2*ln(x)*ln(omx)*LMUF*pow(NC,-1)*x\
            - 2*ln(x)*ln(omx)*LMUF*pow(NC,-1)*pow(x,2) + 2*ln(x)*ln(omx)*LMUF*NC - 4*ln(x)*ln(omx)*LMUF*\
           NC*x + 4*ln(x)*ln(omx)*LMUF*NC*pow(x,2) - 1./2.*ln(omx)*LMUF*pow(\
            NC,-1) + 9./4.*ln(omx)*LMUF*pow(NC,-1)*x - 7./4.*ln(omx)*LMUF*pow(NC,-1)*pow(x,2) - 2./3.*ln(\
            omx)*LMUF*NC*pow(x,-1) - 11./12.*ln(omx)*LMUF*NC - 53./12.*ln(omx)*LMUF*NC*x + 61./12.*ln(omx\
            )*LMUF*NC*pow(x,2) + 1./6.*ln(omx)*LMUF*NF - 1./3.*ln(omx)*LMUF*NF*x + 1./3.*ln(omx)*LMUF*NF*\
            pow(x,2) + 3./8.*ln(x)*LMUF*pow(NC,-1)
            result_r0 = - 1./2.*LMUF*pow(NC,-1) + 5./4.*LMUF*pow(NC,-1)*x - 3./4.*LMUF*pow(NC,-1)*pow(x,2) - 2./3.*LMUF*NC*pow(x,-1)\
       - 11./12.*LMUF*NC - 41./12.*LMUF*NC*x + 49./12.*LMUF*NC*pow(x,2) + 1./6.*LMUF*NF - 1./3.*\
      LMUF*NF*x + 1./3.*LMUF*NF*pow(x,2) - 1./4.*ln(x)*LMUF*pow(NC,-1) + 1./2.*ln(x)*LMUF*pow(NC,-1)*x - ln(x)*LMUF*pow(NC,-1)*\
      pow(x,2) - 3./4.*ln(x)*LMUF*NC - 9./2.*ln(x)*LMUF*NC*x + ln(x)*LMUF*NC*pow(x,2)  + 1./2.*ln(omx)*LMUF*pow(NC,-1) - ln(omx)*LMUF*pow(NC,-1)*x + ln(omx)*LMUF*\
      pow(NC,-1)*pow(x,2) - 3./2.*ln(omx)*LMUF*NC + 3*ln(omx)*LMUF*NC*x - 3*ln(omx)*LMUF*NC*pow(x,2) 
            result_r1 = + 1./2.*LMUF*pow(NC,-1) - LMUF*pow(NC,-1)*x + LMUF*pow(NC,-1)*pow(x,2) - 1./2.*LMUF*NC + LMUF*NC*x - LMUF*NC*pow(x,2)
            result += result_r0 * ln(1-z) + result_r1 * (1/2)*ln(1-z)*ln(1-z)
        elif orders == '100':
            result += + 11./6.*LMUR*NC*x - 11./6.*LMUR*NC*pow(x,2) - 1./3.*LMUR*NF*x + 1./3.*LMUR*NF*pow(x,2) - 11./12.*ln(x)*LMUR*NC + 11./6.*ln(x)*LMUR*NC*x - 11./6.*ln(x)*LMUR*\
                      NC*pow(x,2) + 1./6.*ln(x)*LMUR*NF - 1./3.*ln(x)*LMUR*NF*x + 1./3.*ln(x)*LMUR*NF*pow(x,2) + 11./12.\
                      *ln(omx)*LMUR*NC - 11./6.*ln(omx)*LMUR*NC*x + 11./6.*ln(omx)*LMUR*NC*pow(x,2) - 1./6.*ln(omx)\
                      *LMUR*NF + 1./3.*ln(omx)*LMUR*NF*x - 1./3.*ln(omx)*LMUR*NF*pow(x,2) + 11./12.\
                      *ln(omx)*LMUR*NC - 11./6.*ln(omx)*LMUR*NC*x + 11./6.*ln(omx)*LMUR*NC*pow(x,2) - 1./6.*ln(omx)\
                      *LMUR*NF + 1./3.*ln(omx)*LMUR*NF*x - 1./3.*ln(omx)*LMUR*NF*pow(x,2)
            result_r0 = + 11./12.*LMUR*NC - 11./6.*LMUR*NC*x + 11./6.*LMUR*NC*pow(x,2) - 1./6.*LMUR*NF + 1./3.*LMUR*NF*x - 1./3.*LMUR*NF*pow(x,2)
            result += result_r0 * ln(1-z)
        elif orders == '011':
            result_r0 = - 1./2.*LMUA*LMUF*pow(NC,-1) + LMUA*LMUF*pow(NC,-1)*x - LMUA*LMUF*pow(NC,-1)*pow(x,2) + 1./2.*LMUA*LMUF*NC - LMUA*LMUF*NC*x + LMUA*LMUF*NC*pow(x,2) 
            result += result_r0 * ln(1-z)
        elif orders == '020':
            result += + 1./16.*pow(LMUF,2)*pow(NC,-1) - 1./4.*pow(LMUF,2)*pow(NC,-1)*x + 1./3.*\
                      pow(LMUF,2)*NC*pow(x,-1) + 53./48.*pow(LMUF,2)*NC + 5./12.*pow(LMUF,2)*NC*x - 3./4.*pow(LMUF,2)*NC*pow(x,2) - \
                      1./6.*pow(LMUF,2)*NF + 1./3.*pow(LMUF,2)*NF*x - 1./3.*pow(LMUF,2)*NF*pow(x,2)     + 1./8.*ln(x)*pow(LMUF,2)*pow(NC,-1) - 1./4.*ln(x)*pow(LMUF,2)*pow(NC,-1)*x + 1./2.*ln(x)*pow(LMUF,2)*pow(\
                      NC,-1)*pow(x,2) + 3./8.*ln(x)*pow(LMUF,2)*NC + 9./4.*ln(x)*pow(LMUF,2)*NC*x - 1./2.*ln(x)*\
                      pow(LMUF,2)*NC*pow(x,2)     - 1./4.*ln(omx)*pow(LMUF,2)*pow(NC,-1) + 1./2.*ln(omx)*pow(LMUF,2)*pow(NC,-1)*x - 1./\
                     2.*ln(omx)*pow(LMUF,2)*pow(NC,-1)*pow(x,2) + 3./4.*ln(omx)*pow(LMUF,2)*NC - 3./2.*ln(omx)*\
                     pow(LMUF,2)*NC*x + 3./2.*ln(omx)*pow(LMUF,2)*NC*pow(x,2)
        elif orders == '110':
            result += - 11./12.*LMUF*LMUR*NC + 11./6.*LMUF*LMUR*NC*x - 11./6.*LMUF*LMUR*NC*pow(x,2) + 1./6.*LMUF*LMUR*NF - 1./3.*LMUF*LMUR*NF*x + 1./3.*LMUF*LMUR*NF*pow(x,2)
        return result
    elif rsl == 'sr':
        result = 0
        return result
    elif rsl == 'ss':
        result = 0
        return result
    elif rsl == 'sl':
        result = 0
        return result
    elif rsl == 'lr':
        result = 0
        return result
    elif rsl == 'ls':
        result = 0
        return result
    elif rsl == 'll':
        result = 0
        return result
    else:
        raise ValueError('Invalid rsl value')
