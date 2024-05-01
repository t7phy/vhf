from core.definitions import CF, NC, NF, TR
from core.definitions import ln2 as rln2
from core.miscfunc import atanint as InvTanInt
from core.miscfunc import Li2, Li3
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan
from numpy import sqrt, pi

LMUA = 1
LMUF = 1
LMUR = 1

def ct_nnlo_g2g_eq(x, z, orders, rsl):

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

    if orders == '000':
        if rsl == 'rr':
            result = - 1./3.*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(pi,2)*pow(omz,-1)*pow(opx,-1) + 1./3.*pow(\
      NC,-1)*pow(x,-2)*pow(z,-1)*pow(pi,2)*pow(omz,-1) + 1./3.*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(\
      pi,2)*pow(opx,-1) - 1./3.*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(pi,2) + 1./6.*pow(NC,-1)*pow(\
      x,-2)*pow(pi,2)*pow(opx,-1) - 1./6.*pow(NC,-1)*pow(x,-2)*pow(pi,2) + 1./6.*pow(NC,-1)*pow(\
      x,-2)*z*pow(pi,2)*pow(opx,-1) - 1./6.*pow(NC,-1)*pow(x,-2)*z*pow(pi,2) - pow(NC,-1)*pow(x,-1)\
      *pow(z,-1)*pow(pi,2)*pow(omz,-1)*pow(opx,-1) + 2./3.*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(pi,2)\
      *pow(omz,-1) + pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(pi,2)*pow(opx,-1) - 2./3.*pow(NC,-1)*pow(\
      x,-1)*pow(z,-1)*pow(pi,2) + 1./2.*pow(NC,-1)*pow(x,-1)*pow(pi,2)*pow(opx,-1) - 1./3.*pow(\
      NC,-1)*pow(x,-1)*pow(pi,2) + 1./2.*pow(NC,-1)*pow(x,-1)*z*pow(pi,2)*pow(opx,-1) - 1./3.*pow(\
      NC,-1)*pow(x,-1)*z*pow(pi,2) + 13./16.*pow(NC,-1)*pow(z,-1) + 4*pow(NC,-1)*pow(z,-1)*pow(\
      rln2,2)*pow(opz,-1) - 4*pow(NC,-1)*pow(z,-1)*pow(rln2,2) + 8*pow(NC,-1)*pow(z,-1)*sqrtxz1*\
      rln2*pow(opz,-1) - 8*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2 + 6*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(\
      rln2,2)*pow(opz,-1) - 6*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(rln2,2) - pow(NC,-1)*pow(z,-1)*pow(\
      pi,2)*pow(omz,-1)*pow(opx,-1) + pow(NC,-1)*pow(z,-1)*pow(pi,2)*pow(opx,-1) + 7./24.*pow(\
      NC,-1)*pow(z,-1)*pow(pi,2) + 1./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*sqrtxz1*pow(opz,-1) - 1./3.\
      *pow(NC,-1)*pow(z,-1)*pow(pi,2)*sqrtxz1
            result +=  + 24*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 16*pow(NC,-1)*pow(sqrtxz1,-1)*rln2\
       + 18*pow(NC,-1)*pow(sqrtxz1,-1)*pow(rln2,2)*pow(opz,-1) - 12*pow(NC,-1)*pow(sqrtxz1,-1)*pow(\
      rln2,2) + 1./8.*pow(NC,-1) + 4*pow(NC,-1)*pow(rln2,2) + pow(NC,-1)*pow(pi,2)*pow(sqrtxz1,-1)*\
      pow(opz,-1) - 2./3.*pow(NC,-1)*pow(pi,2)*pow(sqrtxz1,-1) + 1./3.*pow(NC,-1)*pow(pi,2)*pow(\
      omz,-1) + 1./3.*pow(NC,-1)*pow(pi,2)*pow(opx,-1) - 1./4.*pow(NC,-1)*pow(pi,2) - 8*pow(NC,-1)*\
      z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 8*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2 - 6*pow(NC,-1)*z*\
      pow(sqrtxz1,-1)*pow(rln2,2)*pow(opz,-1) + 6*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(rln2,2) - 27./16.\
      *pow(NC,-1)*z - 2*pow(NC,-1)*z*pow(rln2,2) - 1./3.*pow(NC,-1)*z*pow(pi,2)*pow(sqrtxz1,-1)*\
      pow(opz,-1) + 1./3.*pow(NC,-1)*z*pow(pi,2)*pow(sqrtxz1,-1) + 2./3.*pow(NC,-1)*z*pow(pi,2)*\
      pow(opx,-1) - 1./12.*pow(NC,-1)*z*pow(pi,2) + 1./4.*pow(NC,-1)*x*pow(z,-1) - 8*pow(NC,-1)*x*\
      pow(z,-1)*pow(rln2,2)*pow(opz,-1) + 8*pow(NC,-1)*x*pow(z,-1)*pow(rln2,2) - 16*pow(NC,-1)*x*\
      pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) + 16*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2 - 12*pow(NC,-1)*x\
      *pow(z,-1)*sqrtxz1*pow(rln2,2)*pow(opz,-1) + 12*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(rln2,2) - \
      1./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*pow(omz,-1)*pow(opx,-1) - 2./3.*pow(NC,-1)*x*pow(z,-1)\
      *pow(pi,2)*pow(omz,-1) + 1./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*pow(opx,-1) + 1./12.*pow(\
      NC,-1)*x*pow(z,-1)*pow(pi,2)
            result +=  - 2./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*sqrtxz1*pow(opz,-1) + 2./3.*pow(NC,-1)*x*\
      pow(z,-1)*pow(pi,2)*sqrtxz1 - 80*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 64*pow(\
      NC,-1)*x*pow(sqrtxz1,-1)*rln2 - 60*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(rln2,2)*pow(opz,-1) + 48*\
      pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(rln2,2) + 1./2.*pow(NC,-1)*x - 8*pow(NC,-1)*x*pow(rln2,2) - \
      10./3.*pow(NC,-1)*x*pow(pi,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 8./3.*pow(NC,-1)*x*pow(pi,2)*pow(\
      sqrtxz1,-1) + 2./3.*pow(NC,-1)*x*pow(pi,2)*pow(omz,-1) + 1./2.*pow(NC,-1)*x*pow(pi,2) + 16*\
      pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 16*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2 + 12\
      *pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(rln2,2)*pow(opz,-1) - 12*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*\
      pow(rln2,2) + 1./4.*pow(NC,-1)*x*z + 4*pow(NC,-1)*x*z*pow(rln2,2) + 2./3.*pow(NC,-1)*x*z*pow(\
      pi,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 2./3.*pow(NC,-1)*x*z*pow(pi,2)*pow(sqrtxz1,-1) + 1./3.*\
      pow(NC,-1)*x*z*pow(pi,2)*pow(opx,-1) - 1./3.*pow(NC,-1)*x*z*pow(pi,2) + 1./2.*pow(NC,-1)*pow(\
      x,2)*pow(z,-1) + 4*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(rln2,2)*pow(opz,-1) - 4*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)*pow(rln2,2) + 8*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) - 8*\
      pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2 + 6*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(\
      rln2,2)*pow(opz,-1) - 6*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(rln2,2) - 1./3.*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*pow(pi,2)*pow(omz,-1)
            result +=  + pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(pi,2) + 1./3.*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      pi,2)*sqrtxz1*pow(opz,-1) - 1./3.*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(pi,2)*sqrtxz1 + 88*pow(\
      NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 80*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*\
      rln2 + 66*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(rln2,2)*pow(opz,-1) - 60*pow(NC,-1)*pow(\
      x,2)*pow(sqrtxz1,-1)*pow(rln2,2) - 9./4.*pow(NC,-1)*pow(x,2) + 4*pow(NC,-1)*pow(x,2)*pow(\
      rln2,2) + 11./3.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 10./3.*pow(\
      NC,-1)*pow(x,2)*pow(pi,2)*pow(sqrtxz1,-1) + 1./3.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(omz,-1)\
       - 1./3.*pow(NC,-1)*pow(x,2)*pow(pi,2) - 8*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2*pow(\
      opz,-1) + 8*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2 - 6*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1)*pow(rln2,2)*pow(opz,-1) + 6*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(rln2,2) + 3.\
      /2.*pow(NC,-1)*pow(x,2)*z - 4*pow(NC,-1)*pow(x,2)*z*pow(rln2,2) - 1./3.*pow(NC,-1)*pow(x,2)*z\
      *pow(pi,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 1./3.*pow(NC,-1)*pow(x,2)*z*pow(pi,2)*pow(\
      sqrtxz1,-1) + 1./2.*pow(NC,-1)*pow(x,2)*z*pow(pi,2) - 32*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*\
      rln2*pow(opz,-1) + 32*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*rln2 - 24*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz1,-1)*pow(rln2,2)*pow(opz,-1) + 24*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(rln2,2) - 4./\
      3.*pow(NC,-1)*pow(x,3)*pow(pi,2)*pow(sqrtxz1,-1)*pow(opz,-1)
            result +=  + 4./3.*pow(NC,-1)*pow(x,3)*pow(pi,2)*pow(sqrtxz1,-1) - 1./6.*NC*pow(x,-2)*pow(z,-1)*\
      pow(pi,2)*pow(opx,-1) + 1./6.*NC*pow(x,-2)*pow(z,-1)*pow(pi,2) - 1./6.*NC*pow(x,-2)*z*pow(\
      pi,2)*pow(opx,-1) + 1./6.*NC*pow(x,-2)*z*pow(pi,2) - 5./16.*NC*pow(x,-1)*pow(z,-1) - 1./2.*NC\
      *pow(x,-1)*pow(z,-1)*pow(pi,2)*pow(opx,-1) + 1./3.*NC*pow(x,-1)*pow(z,-1)*pow(pi,2) + 5./16.*\
      NC*pow(x,-1) - 1./2.*NC*pow(x,-1)*z*pow(pi,2)*pow(opx,-1) + 1./3.*NC*pow(x,-1)*z*pow(pi,2) - \
      5./16.*NC*pow(z,-2) - 11./16.*NC*pow(z,-1) + 2*NC*pow(z,-1)*pow(rln2,2) + 2*NC*pow(z,-1)*\
      sqrtxz1*rln2 - 2./3.*NC*pow(z,-1)*pow(pi,2)*pow(opx,-1) + 1./24.*NC*pow(z,-1)*pow(pi,2) - 1./\
      4.*NC - 2*NC*pow(rln2,2) + 1./3.*NC*pow(pi,2)*pow(opx,-1) - 1./12.*NC*pow(pi,2) + 2*NC*z + 2*\
      NC*z*pow(rln2,2) - 2./3.*NC*z*pow(pi,2)*pow(opx,-1) + 1./12.*NC*z*pow(pi,2) + 5./16.*NC*x*\
      pow(z,-2) - 47./8.*NC*x*pow(z,-1) - 4*NC*x*pow(z,-1)*pow(rln2,2) - 4*NC*x*pow(z,-1)*sqrtxz1*\
      rln2 - 1./3.*NC*x*pow(z,-1)*pow(pi,2)*pow(opx,-1) + 7./12.*NC*x*pow(z,-1)*pow(pi,2) + 41./8.*\
      NC*x + 4*NC*x*pow(rln2,2) + 1./3.*NC*x*pow(pi,2)*pow(opx,-1) - 1./2.*NC*x*pow(pi,2) - 9./16.*\
      NC*x*z - 4*NC*x*z*pow(rln2,2) - 1./3.*NC*x*z*pow(pi,2)*pow(opx,-1) + 1./3.*NC*x*z*pow(pi,2)\
       + 117./16.*NC*pow(x,2)*pow(z,-1) + 4*NC*pow(x,2)*pow(z,-1)*pow(rln2,2) + 4*NC*pow(x,2)*pow(\
      z,-1)*sqrtxz1*rln2 - 2./3.*NC*pow(x,2)*pow(z,-1)*pow(pi,2) - 89./16.*NC*pow(x,2) + 1./3.*NC*\
      pow(x,2)*pow(pi,2)
            result +=  - 3./2.*NC*pow(x,2)*z + 4*NC*pow(x,2)*z*pow(rln2,2) - 1./2.*NC*pow(x,2)*z*pow(pi,2)
            result +=   - 3./2.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(\
      NC,-1)*pow(x,-1)*z*sqrtxz3 + 3./2.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(NC,-1)*sqrtxz3 + 3./2.\
      *ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3 - 15./2.*ArcTan(z*sqrtxz3)*ln(z*\
      sqrtxz3)*pow(NC,-1)*x*z*sqrtxz3 + 5./16.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*NC*pow(x,-2)*sqrtxz3\
       + 9./8.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*NC*pow(x,-1)*pow(z,-1)*sqrtxz3 + 21./8.*ArcTan(z*\
      sqrtxz3)*ln(z*sqrtxz3)*NC*pow(x,-1)*z*sqrtxz3 + 5./16.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*NC*\
      pow(z,-2)*sqrtxz3 + 5./4.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*NC*sqrtxz3 - 19./16.*ArcTan(z*\
      sqrtxz3)*ln(z*sqrtxz3)*NC*pow(z,2)*sqrtxz3 + 45./8.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*NC*x*pow(\
      z,-1)*sqrtxz3 + 105./8.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*NC*x*z*sqrtxz3 - 35./16.*ArcTan(z*\
      sqrtxz3)*ln(z*sqrtxz3)*NC*pow(x,2)*sqrtxz3 + 3./2.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(NC,-1)*\
      pow(x,-1)*z*sqrtxz3 - 3./2.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(NC,-1)*sqrtxz3 - 3./2.*ArcTan(\
      sqrtxz3)*ln(sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3 + 15./2.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(\
      NC,-1)*x*z*sqrtxz3 - 5./16.*ArcTan(sqrtxz3)*ln(sqrtxz3)*NC*pow(x,-2)*sqrtxz3 - 9./8.*ArcTan(\
      sqrtxz3)*ln(sqrtxz3)*NC*pow(x,-1)*pow(z,-1)*sqrtxz3 - 21./8.*ArcTan(sqrtxz3)*ln(sqrtxz3)*NC*\
      pow(x,-1)*z*sqrtxz3
            result +=  - 5./16.*ArcTan(sqrtxz3)*ln(sqrtxz3)*NC*pow(z,-2)*sqrtxz3 - 5./4.*ArcTan(sqrtxz3)*ln(\
      sqrtxz3)*NC*sqrtxz3 + 19./16.*ArcTan(sqrtxz3)*ln(sqrtxz3)*NC*pow(z,2)*sqrtxz3 - 45./8.*\
      ArcTan(sqrtxz3)*ln(sqrtxz3)*NC*x*pow(z,-1)*sqrtxz3 - 105./8.*ArcTan(sqrtxz3)*ln(sqrtxz3)*NC*x\
      *z*sqrtxz3 + 35./16.*ArcTan(sqrtxz3)*ln(sqrtxz3)*NC*pow(x,2)*sqrtxz3 + 3./4.*InvTanInt( - \
      sqrtxz3)*pow(NC,-1)*pow(x,-1)*z*sqrtxz3 - 3./4.*InvTanInt( - sqrtxz3)*pow(NC,-1)*sqrtxz3 - 3./\
      4.*InvTanInt( - sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3 + 15./4.*InvTanInt( - sqrtxz3)*pow(\
      NC,-1)*x*z*sqrtxz3 - 5./32.*InvTanInt( - sqrtxz3)*NC*pow(x,-2)*sqrtxz3 - 9./16.*InvTanInt( - \
      sqrtxz3)*NC*pow(x,-1)*pow(z,-1)*sqrtxz3 - 21./16.*InvTanInt( - sqrtxz3)*NC*pow(x,-1)*z*\
      sqrtxz3 - 5./32.*InvTanInt( - sqrtxz3)*NC*pow(z,-2)*sqrtxz3 - 5./8.*InvTanInt( - sqrtxz3)*NC*\
      sqrtxz3 + 19./32.*InvTanInt( - sqrtxz3)*NC*pow(z,2)*sqrtxz3 - 45./16.*InvTanInt( - sqrtxz3)*\
      NC*x*pow(z,-1)*sqrtxz3 - 105./16.*InvTanInt( - sqrtxz3)*NC*x*z*sqrtxz3 + 35./32.*InvTanInt(\
       - sqrtxz3)*NC*pow(x,2)*sqrtxz3 + 3./2.*InvTanInt(z*sqrtxz3)*pow(NC,-1)*pow(x,-1)*z*sqrtxz3\
       - 3./2.*InvTanInt(z*sqrtxz3)*pow(NC,-1)*sqrtxz3 - 3./2.*InvTanInt(z*sqrtxz3)*pow(NC,-1)*pow(\
      z,2)*sqrtxz3 + 15./2.*InvTanInt(z*sqrtxz3)*pow(NC,-1)*x*z*sqrtxz3 - 5./16.*InvTanInt(z*\
      sqrtxz3)*NC*pow(x,-2)*sqrtxz3 - 9./8.*InvTanInt(z*sqrtxz3)*NC*pow(x,-1)*pow(z,-1)*sqrtxz3 - \
      21./8.*InvTanInt(z*sqrtxz3)*NC*pow(x,-1)*z*sqrtxz3
            result +=  - 5./16.*InvTanInt(z*sqrtxz3)*NC*pow(z,-2)*sqrtxz3 - 5./4.*InvTanInt(z*sqrtxz3)*NC*\
      sqrtxz3 + 19./16.*InvTanInt(z*sqrtxz3)*NC*pow(z,2)*sqrtxz3 - 45./8.*InvTanInt(z*sqrtxz3)*NC*x\
      *pow(z,-1)*sqrtxz3 - 105./8.*InvTanInt(z*sqrtxz3)*NC*x*z*sqrtxz3 + 35./16.*InvTanInt(z*\
      sqrtxz3)*NC*pow(x,2)*sqrtxz3 - 3./4.*InvTanInt(sqrtxz3)*pow(NC,-1)*pow(x,-1)*z*sqrtxz3 + 3./4.\
      *InvTanInt(sqrtxz3)*pow(NC,-1)*sqrtxz3 + 3./4.*InvTanInt(sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3\
       - 15./4.*InvTanInt(sqrtxz3)*pow(NC,-1)*x*z*sqrtxz3 + 5./32.*InvTanInt(sqrtxz3)*NC*pow(x,-2)*\
      sqrtxz3 + 9./16.*InvTanInt(sqrtxz3)*NC*pow(x,-1)*pow(z,-1)*sqrtxz3 + 21./16.*InvTanInt(\
      sqrtxz3)*NC*pow(x,-1)*z*sqrtxz3 + 5./32.*InvTanInt(sqrtxz3)*NC*pow(z,-2)*sqrtxz3 + 5./8.*\
      InvTanInt(sqrtxz3)*NC*sqrtxz3 - 19./32.*InvTanInt(sqrtxz3)*NC*pow(z,2)*sqrtxz3 + 45./16.*\
      InvTanInt(sqrtxz3)*NC*x*pow(z,-1)*sqrtxz3 + 105./16.*InvTanInt(sqrtxz3)*NC*x*z*sqrtxz3 - 35./\
      32.*InvTanInt(sqrtxz3)*NC*pow(x,2)*sqrtxz3 - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*\
      pow(opz,-1) + 5*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2 - 8*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 8\
      *ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) + 8*ln(1 + sqrtxz1 - z)*\
      pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2 - 24*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(\
      opz,-1)
            result +=  + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1) - 24*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*\
      rln2 - 6*ln(1 + sqrtxz1 - z)*pow(NC,-1)*rln2 + 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1) + 8*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)\
      *z*pow(sqrtxz1,-1)*rln2 + 3*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*rln2 + 8*ln(1 + sqrtxz1 - z)*\
      pow(NC,-1)*x*pow(z,-1)*rln2*pow(opz,-1) - 10*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*rln2\
       + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) - 16*ln(1 + sqrtxz1 - z)\
      *pow(NC,-1)*x*pow(z,-1)*sqrtxz1 + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*\
      pow(opz,-1) - 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2 + 80*ln(1 + sqrtxz1\
       - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(\
      sqrtxz1,-1) + 80*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 64*ln(1\
       + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2 + 12*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*rln2\
       - 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) + 16*ln(1 + sqrtxz1 - z)\
      *pow(NC,-1)*x*z*pow(sqrtxz1,-1) - 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*\
      pow(opz,-1)
            result +=  + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2 - 6*ln(1 + sqrtxz1 - z)*\
      pow(NC,-1)*x*z*rln2 - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*rln2*pow(opz,-1) + \
      6*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*rln2 - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*\
      sqrtxz1 - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) + 8*\
      ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2 - 88*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 80*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1) - 88*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + \
      80*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2 - 6*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(x,2)*rln2 + 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(\
      opz,-1) - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) + 8*ln(1 + sqrtxz1 - z)\
      *pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*\
      pow(x,2)*z*pow(sqrtxz1,-1)*rln2 + 6*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z*rln2 + 32*ln(1\
       + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) - 32*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(x,3)*pow(sqrtxz1,-1) + 32*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*\
      rln2*pow(opz,-1)
            result +=  - 32*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*rln2 - 3*ln(1 + sqrtxz1\
       - z)*NC*pow(z,-1)*rln2 - 2*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)*sqrtxz1 + 4*ln(1 + sqrtxz1 - z)*\
      NC*rln2 - 3*ln(1 + sqrtxz1 - z)*NC*z*rln2 + 6*ln(1 + sqrtxz1 - z)*NC*x*pow(z,-1)*rln2 + 4*ln(\
      1 + sqrtxz1 - z)*NC*x*pow(z,-1)*sqrtxz1 - 8*ln(1 + sqrtxz1 - z)*NC*x*rln2 + 6*ln(1 + sqrtxz1\
       - z)*NC*x*z*rln2 - 6*ln(1 + sqrtxz1 - z)*NC*pow(x,2)*pow(z,-1)*rln2 - 4*ln(1 + sqrtxz1 - z)*\
      NC*pow(x,2)*pow(z,-1)*sqrtxz1 + 2*ln(1 + sqrtxz1 - z)*NC*pow(x,2)*rln2 - 6*ln(1 + sqrtxz1 - z\
      )*NC*pow(x,2)*z*rln2 - pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(z,-1) + 2*pow(ln(1 + sqrtxz1\
       - z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*\
      pow(z,-1)*sqrtxz1 + 6*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 4*\
      pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(sqrtxz1,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(\
      NC,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*pow(ln(1\
       + sqrtxz1 - z),2)*pow(NC,-1)*z*pow(sqrtxz1,-1) - pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*z + 2\
      *pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(z,-1) - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*\
      x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1\
       - 20*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 16*pow(ln(1 + \
      sqrtxz1 - z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)
            result +=  - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x + 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)\
      *x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*z - 2*pow(ln(1 + sqrtxz1 - z),2)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 22\
      *pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 20*pow(ln(1 + \
      sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)\
      *pow(x,2) - 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + \
      2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - 2*pow(ln(1 + sqrtxz1 - z\
      ),2)*pow(NC,-1)*pow(x,2)*z - 8*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)\
      *pow(opz,-1) + 8*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) + pow(ln(1 + \
      sqrtxz1 - z),2)*NC*pow(z,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*NC + pow(ln(1 + sqrtxz1 - z),2)*\
      NC*z - 2*pow(ln(1 + sqrtxz1 - z),2)*NC*x*pow(z,-1) + 4*pow(ln(1 + sqrtxz1 - z),2)*NC*x - 2*\
      pow(ln(1 + sqrtxz1 - z),2)*NC*x*z + 2*pow(ln(1 + sqrtxz1 - z),2)*NC*pow(x,2)*pow(z,-1) - 2*\
      pow(ln(1 + sqrtxz1 - z),2)*NC*pow(x,2) + 2*pow(ln(1 + sqrtxz1 - z),2)*NC*pow(x,2)*z + 4*ln(1\
       + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*pow(opz,-1)
            result +=  - 3*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1) + 4*ln(1 + sqrtxz1\
       - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*ln(1 + sqrtxz1 - z)*\
      ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 12*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)\
      *pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*pow(sqrtxz1,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1) - 4*ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(1 + sqrtxz1\
       - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1) - ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1\
       + z)*pow(NC,-1)*z - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*pow(\
      opz,-1) + 6*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1) - 8*ln(1 + sqrtxz1\
       - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 8*ln(1 + sqrtxz1 - z)*\
      ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 - 40*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + \
      z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 32*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*x*pow(sqrtxz1,-1) - 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x + 8*ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1\
       + sqrtxz1 + z)*pow(NC,-1)*x*z
            result +=  + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1)\
       - 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 4*ln(1 + sqrtxz1\
       - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 44*ln(1 + sqrtxz1 - \
      z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 40*ln(1 + sqrtxz1 - \
      z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(x,2) - 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
      x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
      pow(x,2)*z*pow(sqrtxz1,-1) - 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*z\
       - 16*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1)\
       + 16*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) + ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*pow(z,-1) + ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*z\
       - 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1) - 2*ln(1 + sqrtxz1 - z)*ln(1 + \
      sqrtxz1 + z)*NC*x*z + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*pow(x,2)*pow(z,-1) + 2*ln(\
      1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*pow(x,2) + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*\
      NC*pow(x,2)*z
            result +=  - 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*rln2*pow(opz,-1) + 3*ln(1 + sqrtxz1 + z)\
      *pow(NC,-1)*pow(z,-1)*rln2 - 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*pow(\
      opz,-1) + 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2 - 12*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
      sqrtxz1,-1)*rln2 - 2*ln(1 + sqrtxz1 + z)*pow(NC,-1)*rln2 + 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z\
      *pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2\
       + ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*rln2 + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*rln2*\
      pow(opz,-1) - 6*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*rln2 + 8*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) - 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1*rln2 + 40*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 32*ln(1\
       + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2 + 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*rln2\
       - 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 8*ln(1 + sqrtxz1\
       + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2 - 2*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*rln2 - 4*ln(\
      1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*rln2*pow(opz,-1) + 2*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*rln2 - 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*\
      rln2*pow(opz,-1)
            result +=  + 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2 - 44*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 40*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2 - 2*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*rln2 + 4\
      *ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 4*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2 + 2*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
      pow(x,2)*z*rln2 + 16*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*rln2*pow(opz,-1)\
       - 16*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*rln2 - ln(1 + sqrtxz1 + z)*NC*\
      pow(z,-1)*rln2 - ln(1 + sqrtxz1 + z)*NC*z*rln2 + 2*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1)*rln2 + \
      2*ln(1 + sqrtxz1 + z)*NC*x*z*rln2 - 2*ln(1 + sqrtxz1 + z)*NC*pow(x,2)*pow(z,-1)*rln2 - 2*ln(1\
       + sqrtxz1 + z)*NC*pow(x,2)*rln2 - 2*ln(1 + sqrtxz1 + z)*NC*pow(x,2)*z*rln2 + 1./2.*pow(ln(1\
       - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 1./2.*pow(ln(1 - 2*z\
       + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 3./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*\
      z),2)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(\
      NC,-1)*pow(sqrtxz1,-1) - 1./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 1./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1)
            result +=  - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + \
      pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 - 5*pow(ln(1 - 2*z + \
      pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 4*pow(ln(1 - 2*z + pow(z,2)\
       + 4*x*z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1) + pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*\
      x*z*pow(sqrtxz1,-1)*pow(opz,-1) - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1) + 1./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) - 1./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*pow(\
      z,-1)*sqrtxz1 + 11./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 5*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1) - 1./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 1./2.*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*z*\
      pow(sqrtxz1,-1) - 2*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)\
      *pow(opz,-1) + 2*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - \
      4*ln(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 4*ln(x)*pow(NC,-1)*pow(x,-2)\
      *pow(z,-1)*pow(omz,-1) + 4*ln(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) - 4*ln(x)*pow(\
      NC,-1)*pow(x,-2)*pow(z,-1)
            result +=  + 2*ln(x)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) - 2*ln(x)*pow(NC,-1)*pow(x,-2) + 2*ln(x)*\
      pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) - 2*ln(x)*pow(NC,-1)*pow(x,-2)*z - 12*ln(x)*pow(NC,-1)*\
      pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 8*ln(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(\
      omz,-1) + 12*ln(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) - 8*ln(x)*pow(NC,-1)*pow(x,-1)*\
      pow(z,-1) + 6*ln(x)*pow(NC,-1)*pow(x,-1)*pow(opx,-1) - 4*ln(x)*pow(NC,-1)*pow(x,-1) + 6*ln(x)\
      *pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) - 4*ln(x)*pow(NC,-1)*pow(x,-1)*z - 12*ln(x)*pow(NC,-1)*\
      pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 12*ln(x)*pow(NC,-1)*pow(z,-1)*pow(opx,-1) - 7./4.*ln(x)*\
      pow(NC,-1)*pow(z,-1) + 2*ln(x)*pow(NC,-1)*pow(z,-1)*rln2*pow(opz,-1) - 3*ln(x)*pow(NC,-1)*\
      pow(z,-1)*rln2 + 4*ln(x)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*ln(x)*pow(NC,-1)*pow(\
      z,-1)*sqrtxz1 + 12*ln(x)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(x)*pow(NC,-1)*pow(\
      sqrtxz1,-1) + 4*ln(x)*pow(NC,-1)*pow(omz,-1) + 4*ln(x)*pow(NC,-1)*pow(opx,-1) + 9./4.*ln(x)*\
      pow(NC,-1) + 4*ln(x)*pow(NC,-1)*rln2 - 4*ln(x)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*\
      ln(x)*pow(NC,-1)*z*pow(sqrtxz1,-1) + 8*ln(x)*pow(NC,-1)*z*pow(opx,-1) - 5*ln(x)*pow(NC,-1)*z\
       - 2*ln(x)*pow(NC,-1)*z*rln2 - 4*ln(x)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 8*ln(\
      x)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + 4*ln(x)*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) + 13*ln(x)\
      *pow(NC,-1)*x*pow(z,-1)
            result +=  - 4*ln(x)*pow(NC,-1)*x*pow(z,-1)*rln2*pow(opz,-1) + 6*ln(x)*pow(NC,-1)*x*pow(z,-1)*\
      rln2 - 8*ln(x)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 8*ln(x)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1 - 40*ln(x)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 32*ln(x)*pow(NC,-1)*x*pow(\
      sqrtxz1,-1) + 8*ln(x)*pow(NC,-1)*x*pow(omz,-1) - 11./4.*ln(x)*pow(NC,-1)*x - 8*ln(x)*pow(\
      NC,-1)*x*rln2 + 8*ln(x)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(x)*pow(NC,-1)*x*z*\
      pow(sqrtxz1,-1) + 4*ln(x)*pow(NC,-1)*x*z*pow(opx,-1) - 5./4.*ln(x)*pow(NC,-1)*x*z + 4*ln(x)*\
      pow(NC,-1)*x*z*rln2 - 4*ln(x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) - 1./2.*ln(x)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*rln2*pow(opz,-1) - 4*ln(x)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1)*rln2 + 4*ln(x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(\
      opz,-1) - 4*ln(x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 44*ln(x)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 40*ln(x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + 4*ln(x)*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) + 7./2.*ln(x)*pow(NC,-1)*pow(x,2) + 4*ln(x)*pow(NC,-1)*pow(x,2)*rln2 - 4\
      *ln(x)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(x)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1) + 1./2.*ln(x)*pow(NC,-1)*pow(x,2)*z - 4*ln(x)*pow(NC,-1)*pow(x,2)*z*rln2 - 16*ln(\
      x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) + 16*ln(x)*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz1,-1)
            result +=  - 2*ln(x)*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) + 2*ln(x)*NC*pow(x,-2)*pow(z,-1) - 2*ln(\
      x)*NC*pow(x,-2)*z*pow(opx,-1) + 2*ln(x)*NC*pow(x,-2)*z - 6*ln(x)*NC*pow(x,-1)*pow(z,-1)*pow(\
      opx,-1) + 133./32.*ln(x)*NC*pow(x,-1)*pow(z,-1) - 5./32.*ln(x)*NC*pow(x,-1) - 6*ln(x)*NC*pow(\
      x,-1)*z*pow(opx,-1) + 4*ln(x)*NC*pow(x,-1)*z - 5./32.*ln(x)*NC*pow(z,-2) - 8*ln(x)*NC*pow(\
      z,-1)*pow(opx,-1) + 59./16.*ln(x)*NC*pow(z,-1) + 2*ln(x)*NC*pow(z,-1)*rln2 + ln(x)*NC*pow(\
      z,-1)*sqrtxz1 + 4*ln(x)*NC*pow(opx,-1) - 67./16.*ln(x)*NC - 3*ln(x)*NC*rln2 - 8*ln(x)*NC*z*\
      pow(opx,-1) + 165./32.*ln(x)*NC*z + 2*ln(x)*NC*z*rln2 - 5./32.*ln(x)*NC*x*pow(z,-2) - 4*ln(x)\
      *NC*x*pow(z,-1)*pow(opx,-1) - 109./16.*ln(x)*NC*x*pow(z,-1) - 4*ln(x)*NC*x*pow(z,-1)*rln2 - 2\
      *ln(x)*NC*x*pow(z,-1)*sqrtxz1 + 4*ln(x)*NC*x*pow(opx,-1) + 73./16.*ln(x)*NC*x + 6*ln(x)*NC*x*\
      rln2 - 4*ln(x)*NC*x*z*pow(opx,-1) + 45./32.*ln(x)*NC*x*z - 4*ln(x)*NC*x*z*rln2 + 109./32.*ln(\
      x)*NC*pow(x,2)*pow(z,-1) + 4*ln(x)*NC*pow(x,2)*pow(z,-1)*rln2 + 2*ln(x)*NC*pow(x,2)*pow(z,-1)\
      *sqrtxz1 - 77./32.*ln(x)*NC*pow(x,2) - 2*ln(x)*NC*pow(x,2)*rln2 - 1./2.*ln(x)*NC*pow(x,2)*z\
       + 4*ln(x)*NC*pow(x,2)*z*rln2 
            result +=   + ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1) + 2*\
      ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*ln(x)*ln(1 + sqrtxz1\
       - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 6*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*\
      pow(opz,-1) - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1) - 2*ln(x)*ln(1 + sqrtxz1\
       - z)*pow(NC,-1) - 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*\
      ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1) + ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)\
      *z - 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1) - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1)
            result +=  + 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 - 20*ln(x)*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 16*ln(x)*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*x*pow(sqrtxz1,-1) + 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x + 4*ln(x)*ln(1 + sqrtxz1\
       - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z\
      *pow(sqrtxz1,-1) - 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z + 2*ln(x)*ln(1 + sqrtxz1 - z)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) - 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 22*\
      ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 20*ln(x)*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*\
      pow(x,2) - 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*\
      ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)\
      *pow(NC,-1)*pow(x,2)*z - 8*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(\
      opz,-1) + 8*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - ln(x)*ln(1 + \
      sqrtxz1 - z)*NC*pow(z,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*NC - ln(x)*ln(1 + sqrtxz1 - z)*NC*z\
       + 2*ln(x)*ln(1 + sqrtxz1 - z)*NC*x*pow(z,-1) - 4*ln(x)*ln(1 + sqrtxz1 - z)*NC*x + 2*ln(x)*\
      ln(1 + sqrtxz1 - z)*NC*x*z
            result +=  - 2*ln(x)*ln(1 + sqrtxz1 - z)*NC*pow(x,2)*pow(z,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*NC*\
      pow(x,2) - 2*ln(x)*ln(1 + sqrtxz1 - z)*NC*pow(x,2)*z - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)\
      *pow(z,-1)*pow(opz,-1) + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1) - 2*ln(x)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*pow(z,-1)*sqrtxz1 - 6*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1)\
       + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1) + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 2*ln(x)*ln(1\
       + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1) + ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z + 4*ln(\
      x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*pow(opz,-1) - 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*x*pow(z,-1) + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1)\
       - 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 + 20*ln(x)*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - 16*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(\
      sqrtxz1,-1) + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x - 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1)
            result +=  + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 2*ln(x)*ln(1 + sqrtxz1\
       + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 - 22*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 20*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - \
      2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2) + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
      x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1) + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*z + 8*ln(x)*ln(1 + sqrtxz1 + z)\
      *pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
      pow(x,3)*pow(sqrtxz1,-1) - ln(x)*ln(1 + sqrtxz1 + z)*NC*pow(z,-1) + ln(x)*ln(1 + sqrtxz1 + z)\
      *NC - ln(x)*ln(1 + sqrtxz1 + z)*NC*z + 2*ln(x)*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1) - 2*ln(x)*\
      ln(1 + sqrtxz1 + z)*NC*x + 2*ln(x)*ln(1 + sqrtxz1 + z)*NC*x*z - 2*ln(x)*ln(1 + sqrtxz1 + z)*\
      NC*pow(x,2)*pow(z,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*NC*pow(x,2)*z + ln(x)*ln(1 + x*pow(z,-1))\
      *pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(\
      NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(\
      z,-1)*pow(opx,-1) + ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1) - 1./2.*ln(x)*\
      ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(opx,-1)
            result +=  + 1./2.*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2) - 1./2.*ln(x)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) + 1./2.*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(\
      x,-2)*z + 3*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1)\
       - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1) - 3*ln(x)*ln(1 + x*\
      pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(\
      NC,-1)*pow(x,-1)*pow(z,-1) - 3./2.*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(opx,-1)\
       + ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1) - 3./2.*ln(x)*ln(1 + x*pow(z,-1))*pow(\
      NC,-1)*pow(x,-1)*z*pow(opx,-1) + ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*z + 3*ln(x)*\
      ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 3*ln(x)*ln(1 + x*pow(z,-1)\
      )*pow(NC,-1)*pow(z,-1)*pow(opx,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(opx,-1) - 1./2.\
      *ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1) - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*z*pow(opx,-1)\
       + 1./2.*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*z + ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(\
      z,-1)*pow(omz,-1)*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*pow(\
      omz,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) - 2*ln(x)*ln(1 + x*\
      pow(z,-1))*pow(NC,-1)*x*pow(z,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x - ln(x)*ln(1 + x*\
      pow(z,-1))*pow(NC,-1)*x*z*pow(opx,-1)
            result +=  - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*z + ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*pow(omz,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) - \
      ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,2)*z + 1./2.*ln(x)*ln(1 + x*pow(z,-1))*NC*pow(\
      x,-2)*pow(z,-1)*pow(opx,-1) - 1./2.*ln(x)*ln(1 + x*pow(z,-1))*NC*pow(x,-2)*pow(z,-1) + 1./2.*\
      ln(x)*ln(1 + x*pow(z,-1))*NC*pow(x,-2)*z*pow(opx,-1) - 1./2.*ln(x)*ln(1 + x*pow(z,-1))*NC*\
      pow(x,-2)*z + 3./2.*ln(x)*ln(1 + x*pow(z,-1))*NC*pow(x,-1)*pow(z,-1)*pow(opx,-1) - ln(x)*ln(1\
       + x*pow(z,-1))*NC*pow(x,-1)*pow(z,-1) + 3./2.*ln(x)*ln(1 + x*pow(z,-1))*NC*pow(x,-1)*z*pow(\
      opx,-1) - ln(x)*ln(1 + x*pow(z,-1))*NC*pow(x,-1)*z + 2*ln(x)*ln(1 + x*pow(z,-1))*NC*pow(z,-1)\
      *pow(opx,-1) - 1./2.*ln(x)*ln(1 + x*pow(z,-1))*NC*pow(z,-1) - ln(x)*ln(1 + x*pow(z,-1))*NC*\
      pow(opx,-1) + ln(x)*ln(1 + x*pow(z,-1))*NC + 2*ln(x)*ln(1 + x*pow(z,-1))*NC*z*pow(opx,-1) - 1.\
      /2.*ln(x)*ln(1 + x*pow(z,-1))*NC*z + ln(x)*ln(1 + x*pow(z,-1))*NC*x*pow(z,-1)*pow(opx,-1) + \
      ln(x)*ln(1 + x*pow(z,-1))*NC*x*pow(z,-1) - ln(x)*ln(1 + x*pow(z,-1))*NC*x*pow(opx,-1) + ln(x)\
      *ln(1 + x*pow(z,-1))*NC*x*z*pow(opx,-1) + ln(x)*ln(1 + x*pow(z,-1))*NC*x*z + ln(x)*ln(1 + x*\
      pow(z,-1))*NC*pow(x,2)*pow(z,-1) - ln(x)*ln(1 + x*pow(z,-1))*NC*pow(x,2) + ln(x)*ln(1 + x*\
      pow(z,-1))*NC*pow(x,2)*z + ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(\
      opx,-1)
            result +=  - ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) - ln(x)*ln(1 + x*z)*\
      pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) + ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)\
       - 1./2.*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) + 1./2.*ln(x)*ln(1 + x*z)*pow(\
      NC,-1)*pow(x,-2) - 1./2.*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) + 1./2.*ln(x)*\
      ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z + 3*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(\
      omz,-1)*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1) - 3*ln(x\
      )*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*\
      pow(x,-1)*pow(z,-1) - 3./2.*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(opx,-1) + ln(x)*ln(1\
       + x*z)*pow(NC,-1)*pow(x,-1) - 3./2.*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) + \
      ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*z + 3*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*pow(\
      omz,-1)*pow(opx,-1) - 3*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*pow(opx,-1) + ln(x)*ln(1 + x*z\
      )*pow(NC,-1)*pow(z,-1)*pow(opz,-1) - ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1) - ln(x)*ln(1 + x*\
      z)*pow(NC,-1)*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*z*pow(opx,-1) + ln(x)*ln(1 + x*z)*\
      pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*x*pow(z,-1)*\
      pow(omz,-1) - ln(x)*ln(1 + x*z)*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(\
      NC,-1)*x*pow(z,-1)*pow(opz,-1)
            result +=  - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*x - ln(x)*ln(1 + x*z)*pow(NC,-1)*x*z*pow(opx,-1) + \
      ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + ln(x)*ln(1 + x*z)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*pow(opz,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 2*ln(x)*\
      ln(1 + x*z)*pow(NC,-1)*pow(x,2)*z + 1./2.*ln(x)*ln(1 + x*z)*NC*pow(x,-2)*pow(z,-1)*pow(\
      opx,-1) - 1./2.*ln(x)*ln(1 + x*z)*NC*pow(x,-2)*pow(z,-1) + 1./2.*ln(x)*ln(1 + x*z)*NC*pow(\
      x,-2)*z*pow(opx,-1) - 1./2.*ln(x)*ln(1 + x*z)*NC*pow(x,-2)*z + 3./2.*ln(x)*ln(1 + x*z)*NC*\
      pow(x,-1)*pow(z,-1)*pow(opx,-1) - ln(x)*ln(1 + x*z)*NC*pow(x,-1)*pow(z,-1) + 3./2.*ln(x)*ln(1\
       + x*z)*NC*pow(x,-1)*z*pow(opx,-1) - ln(x)*ln(1 + x*z)*NC*pow(x,-1)*z + 2*ln(x)*ln(1 + x*z)*\
      NC*pow(z,-1)*pow(opx,-1) - ln(x)*ln(1 + x*z)*NC*pow(opx,-1) + ln(x)*ln(1 + x*z)*NC + 2*ln(x)*\
      ln(1 + x*z)*NC*z*pow(opx,-1) + ln(x)*ln(1 + x*z)*NC*x*pow(z,-1)*pow(opx,-1) - ln(x)*ln(1 + x*\
      z)*NC*x*pow(opx,-1) + ln(x)*ln(1 + x*z)*NC*x*z*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*NC*pow(x,2)*\
      pow(z,-1) + 2*ln(x)*ln(1 + x*z)*NC*pow(x,2)*z - ln(x)*ln(z + x)*pow(NC,-1)*pow(z,-1)*pow(\
      opz,-1) + ln(x)*ln(z + x)*pow(NC,-1)*pow(z,-1) - 1./2.*ln(x)*ln(z + x)*pow(NC,-1) + 1./2.*ln(\
      x)*ln(z + x)*pow(NC,-1)*z + 2*ln(x)*ln(z + x)*pow(NC,-1)*x*pow(z,-1)*pow(opz,-1) - 2*ln(x)*\
      ln(z + x)*pow(NC,-1)*x*pow(z,-1) + ln(x)*ln(z + x)*pow(NC,-1)*x - ln(x)*ln(z + x)*pow(NC,-1)*\
      x*z
            result +=  - ln(x)*ln(z + x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) + ln(x)*ln(z + x)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1) + ln(x)*ln(z + x)*pow(NC,-1)*pow(x,2)*z - 1./2.*ln(x)*ln(z + x)*NC*\
      pow(z,-1) - 1./2.*ln(x)*ln(z + x)*NC*z + ln(x)*ln(z + x)*NC*x*pow(z,-1) + ln(x)*ln(z + x)*NC*\
      x*z - ln(x)*ln(z + x)*NC*pow(x,2)*pow(z,-1) - ln(x)*ln(z + x)*NC*pow(x,2) - ln(x)*ln(z + x)*\
      NC*pow(x,2)*z + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 3.\
      /2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) - 3./2.*pow(ln(x),2)*pow(NC,-1)*\
      pow(x,-2)*pow(z,-1)*pow(opx,-1) + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1) - 3./4.*\
      pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) + 3./4.*pow(ln(x),2)*pow(NC,-1)*pow(x,-2) - 3./\
      4.*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) + 3./4.*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*\
      z + 9./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 3*pow(ln(x),2\
      )*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1) - 9./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*pow(\
      z,-1)*pow(opx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1) - 9./4.*pow(ln(x),2)*pow(\
      NC,-1)*pow(x,-1)*pow(opx,-1) + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-1) - 9./4.*pow(ln(x),2)*\
      pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*z + 9./2.*pow(\
      ln(x),2)*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 9./2.*pow(ln(x),2)*pow(NC,-1)*pow(\
      z,-1)*pow(opx,-1)
            result +=  - 1./2.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1) - 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 9./2.*pow(ln(x),2)*\
      pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) + 3*pow(ln(x),2)*pow(NC,-1)*pow(sqrtxz1,-1) - 3./2.*\
      pow(ln(x),2)*pow(NC,-1)*pow(omz,-1) - 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(opx,-1) + 1./2.*pow(\
      ln(x),2)*pow(NC,-1) + 3./2.*pow(ln(x),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 3./2.*\
      pow(ln(x),2)*pow(NC,-1)*z*pow(sqrtxz1,-1) - 3*pow(ln(x),2)*pow(NC,-1)*z*pow(opx,-1) + pow(ln(\
      x),2)*pow(NC,-1)*z + 3./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 3*\
      pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) - 3./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*\
      pow(opx,-1) - 2*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1) + 3*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) - 3*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 + 15*pow(ln(x),2)*pow(\
      NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - 12*pow(ln(x),2)*pow(NC,-1)*x*pow(sqrtxz1,-1) - 3*pow(\
      ln(x),2)*pow(NC,-1)*x*pow(omz,-1) - pow(ln(x),2)*pow(NC,-1)*x - 3*pow(ln(x),2)*pow(NC,-1)*x*z\
      *pow(sqrtxz1,-1)*pow(opz,-1) + 3*pow(ln(x),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) - 3./2.*pow(ln(x\
      ),2)*pow(NC,-1)*x*z*pow(opx,-1) + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      omz,-1) - 3*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1)
            result +=  + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 - 33./2.*pow(ln(x),2)*pow(\
      NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 15*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1) - 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(omz,-1) + 3./2.*pow(ln(x),2)*pow(\
      NC,-1)*pow(x,2) + 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 3./2.\
      *pow(ln(x),2)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - pow(ln(x),2)*pow(NC,-1)*pow(x,2)*z + 6*\
      pow(ln(x),2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) - 6*pow(ln(x),2)*pow(NC,-1)*pow(\
      x,3)*pow(sqrtxz1,-1) + 3./4.*pow(ln(x),2)*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) - 3./4.*pow(ln(x\
      ),2)*NC*pow(x,-2)*pow(z,-1) + 3./4.*pow(ln(x),2)*NC*pow(x,-2)*z*pow(opx,-1) - 3./4.*pow(ln(x)\
      ,2)*NC*pow(x,-2)*z + 9./4.*pow(ln(x),2)*NC*pow(x,-1)*pow(z,-1)*pow(opx,-1) - 3./2.*pow(ln(x),\
      2)*NC*pow(x,-1)*pow(z,-1) + 9./4.*pow(ln(x),2)*NC*pow(x,-1)*z*pow(opx,-1) - 3./2.*pow(ln(x),2\
      )*NC*pow(x,-1)*z + 3*pow(ln(x),2)*NC*pow(z,-1)*pow(opx,-1) - pow(ln(x),2)*NC*pow(z,-1) - 3./2.\
      *pow(ln(x),2)*NC*pow(opx,-1) + pow(ln(x),2)*NC + 3*pow(ln(x),2)*NC*z*pow(opx,-1) - pow(ln(x),\
      2)*NC*z + 3./2.*pow(ln(x),2)*NC*x*pow(z,-1)*pow(opx,-1) - pow(ln(x),2)*NC*x*pow(z,-1) - 3./2.\
      *pow(ln(x),2)*NC*x*pow(opx,-1) + pow(ln(x),2)*NC*x + 3./2.*pow(ln(x),2)*NC*x*z*pow(opx,-1) + \
      3./2.*pow(ln(x),2)*NC*pow(x,2)*pow(z,-1) - 3./2.*pow(ln(x),2)*NC*pow(x,2) + pow(ln(x),2)*NC*\
      pow(x,2)*z
            result +=  - ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + ln(x)*ln(z)*\
      pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) + ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(\
      opx,-1) - ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*pow(z,-1) + 1./2.*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)\
      *pow(opx,-1) - 1./2.*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2) + 1./2.*ln(x)*ln(z)*pow(NC,-1)*pow(\
      x,-2)*z*pow(opx,-1) - 1./2.*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*z - 3*ln(x)*ln(z)*pow(NC,-1)*\
      pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*\
      pow(omz,-1) + 3*ln(x)*ln(z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) - 2*ln(x)*ln(z)*pow(\
      NC,-1)*pow(x,-1)*pow(z,-1) + 3./2.*ln(x)*ln(z)*pow(NC,-1)*pow(x,-1)*pow(opx,-1) - ln(x)*ln(z)\
      *pow(NC,-1)*pow(x,-1) + 3./2.*ln(x)*ln(z)*pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) - ln(x)*ln(z)*\
      pow(NC,-1)*pow(x,-1)*z - 3*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 3*ln(x)\
      *ln(z)*pow(NC,-1)*pow(z,-1)*pow(opx,-1) + ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) - 5./4.\
      *ln(x)*ln(z)*pow(NC,-1)*pow(z,-1) - ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + \
      ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 3*ln(x)*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(\
      opz,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1) + ln(x)*ln(z)*pow(NC,-1)*pow(omz,-1) + ln(\
      x)*ln(z)*pow(NC,-1)*pow(opx,-1) + ln(x)*ln(z)*pow(NC,-1) + ln(x)*ln(z)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1)
            result +=  - ln(x)*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*z*pow(opx,-1)\
       - 3./2.*ln(x)*ln(z)*pow(NC,-1)*z - ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(\
      opx,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + ln(x)*ln(z)*pow(NC,-1)*x*pow(\
      z,-1)*pow(opx,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*pow(opz,-1) + 9./2.*ln(x)*ln(z)*pow(\
      NC,-1)*x*pow(z,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*ln(x)*ln(z)\
      *pow(NC,-1)*x*pow(z,-1)*sqrtxz1 + 10*ln(x)*ln(z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - 8\
      *ln(x)*ln(z)*pow(NC,-1)*x*pow(sqrtxz1,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*x*pow(omz,-1) - 2*ln(x)*\
      ln(z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1) + ln(x)*ln(z)*pow(NC,-1)*x*z*pow(opx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*x*z - ln(x)*\
      ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*\
      pow(opz,-1) - ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) + ln(x)*ln(z)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 - 11*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*\
      pow(opz,-1) + 10*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + ln(x)*ln(z)*pow(NC,-1)*\
      pow(x,2)*pow(omz,-1) + ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - ln(x)*\
      ln(z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*z + 4*ln(x)*ln(\
      z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1)
            result +=  - 4*ln(x)*ln(z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - 1./2.*ln(x)*ln(z)*NC*pow(x,-2)*\
      pow(z,-1)*pow(opx,-1) + 1./2.*ln(x)*ln(z)*NC*pow(x,-2)*pow(z,-1) - 1./2.*ln(x)*ln(z)*NC*pow(\
      x,-2)*z*pow(opx,-1) + 1./2.*ln(x)*ln(z)*NC*pow(x,-2)*z - 3./2.*ln(x)*ln(z)*NC*pow(x,-1)*pow(\
      z,-1)*pow(opx,-1) + ln(x)*ln(z)*NC*pow(x,-1)*pow(z,-1) - 3./2.*ln(x)*ln(z)*NC*pow(x,-1)*z*\
      pow(opx,-1) + ln(x)*ln(z)*NC*pow(x,-1)*z - 2*ln(x)*ln(z)*NC*pow(z,-1)*pow(opx,-1) + 3./4.*ln(\
      x)*ln(z)*NC*pow(z,-1) + ln(x)*ln(z)*NC*pow(opx,-1) - 5./2.*ln(x)*ln(z)*NC - 2*ln(x)*ln(z)*NC*\
      z*pow(opx,-1) + 3./2.*ln(x)*ln(z)*NC*z - ln(x)*ln(z)*NC*x*pow(z,-1)*pow(opx,-1) - 7./2.*ln(x)\
      *ln(z)*NC*x*pow(z,-1) + ln(x)*ln(z)*NC*x*pow(opx,-1) - 3*ln(x)*ln(z)*NC*x - ln(x)*ln(z)*NC*x*\
      z*pow(opx,-1) - 2*ln(x)*ln(z)*NC*x*z + ln(x)*ln(z)*NC*pow(x,2)*pow(z,-1) + ln(x)*ln(z)*NC*\
      pow(x,2) + ln(x)*ln(z)*NC*pow(x,2)*z + 2*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(\
      omz,-1)*pow(opx,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) - 2*ln(x)*\
      ln(omx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) + 2*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*\
      pow(z,-1) - ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) + ln(x)*ln(omx)*pow(NC,-1)*pow(\
      x,-2) - ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) + ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)\
      *z + 6*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 4*ln(x)*ln(omx)\
      *pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)
            result +=  - 6*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) + 4*ln(x)*ln(omx)*pow(\
      NC,-1)*pow(x,-1)*pow(z,-1) - 3*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*pow(opx,-1) + 2*ln(x)*ln(\
      omx)*pow(NC,-1)*pow(x,-1) - 3*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) + 2*ln(x)*ln(\
      omx)*pow(NC,-1)*pow(x,-1)*z + 6*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - \
      6*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*pow(opx,-1) + 1./2.*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)\
       - 2*ln(x)*ln(omx)*pow(NC,-1)*pow(omz,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*pow(opx,-1) - 4*ln(x)*\
      ln(omx)*pow(NC,-1)*z*pow(opx,-1) + 2*ln(x)*ln(omx)*pow(NC,-1)*z + 2*ln(x)*ln(omx)*pow(NC,-1)*\
      x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 4*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) - 2*\
      ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) - 5*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1) - 4\
      *ln(x)*ln(omx)*pow(NC,-1)*x*pow(omz,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*x*z*pow(opx,-1) + 2*ln(x\
      )*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) - ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(\
      z,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)*pow(omz,-1) - ln(x)*ln(omx)*pow(NC,-1)*pow(x,2)\
       + ln(x)*ln(omx)*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) - ln(x)*ln(omx)*NC*pow(x,-2)*pow(z,-1) + \
      ln(x)*ln(omx)*NC*pow(x,-2)*z*pow(opx,-1) - ln(x)*ln(omx)*NC*pow(x,-2)*z + 3*ln(x)*ln(omx)*NC*\
      pow(x,-1)*pow(z,-1)*pow(opx,-1) - 2*ln(x)*ln(omx)*NC*pow(x,-1)*pow(z,-1) + 3*ln(x)*ln(omx)*NC\
      *pow(x,-1)*z*pow(opx,-1)
            result +=  - 2*ln(x)*ln(omx)*NC*pow(x,-1)*z + 4*ln(x)*ln(omx)*NC*pow(z,-1)*pow(opx,-1) - 5./2.*\
      ln(x)*ln(omx)*NC*pow(z,-1) - 2*ln(x)*ln(omx)*NC*pow(opx,-1) + 2*ln(x)*ln(omx)*NC + 4*ln(x)*\
      ln(omx)*NC*z*pow(opx,-1) - 2*ln(x)*ln(omx)*NC*z + 2*ln(x)*ln(omx)*NC*x*pow(z,-1)*pow(opx,-1)\
       + ln(x)*ln(omx)*NC*x*pow(z,-1) - 2*ln(x)*ln(omx)*NC*x*pow(opx,-1) + 2*ln(x)*ln(omx)*NC*x*z*\
      pow(opx,-1) - ln(x)*ln(omx)*NC*pow(x,2)*pow(z,-1) + ln(x)*ln(omx)*NC*pow(x,2) + 3./4.*ln(x)*\
      ln(omz)*pow(NC,-1)*pow(z,-1) + 2*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*\
      ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 6*ln(x)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(\
      opz,-1) - 4*ln(x)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1) - 1./2.*ln(x)*ln(omz)*pow(NC,-1) - 2*ln(\
      x)*ln(omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*ln(x)*ln(omz)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1) + 1./2.*ln(x)*ln(omz)*pow(NC,-1)*z - 3./2.*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1)\
       - 4*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*ln(x)*ln(omz)*pow(NC,-1)*x*\
      pow(z,-1)*sqrtxz1 - 20*ln(x)*ln(omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 16*ln(x)*ln(\
      omz)*pow(NC,-1)*x*pow(sqrtxz1,-1) + ln(x)*ln(omz)*pow(NC,-1)*x + 4*ln(x)*ln(omz)*pow(NC,-1)*x\
      *z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(x)*ln(omz)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 2*ln(x)*ln(\
      omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*\
      pow(opz,-1)
            result +=  - 2*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 22*ln(x)*ln(omz)*pow(NC,-1)\
      *pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 20*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)\
       - 2*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2) - 2*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 2*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) + ln(x)*ln(\
      omz)*pow(NC,-1)*pow(x,2)*z - 8*ln(x)*ln(omz)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1)\
       + 8*ln(x)*ln(omz)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - 3./4.*ln(x)*ln(omz)*NC*pow(z,-1) + 1.\
      /2.*ln(x)*ln(omz)*NC - 1./2.*ln(x)*ln(omz)*NC*z + 3./2.*ln(x)*ln(omz)*NC*x*pow(z,-1) - ln(x)*\
      ln(omz)*NC*x - 2*ln(x)*ln(omz)*NC*pow(x,2)*pow(z,-1) + 2*ln(x)*ln(omz)*NC*pow(x,2) - ln(x)*\
      ln(omz)*NC*pow(x,2)*z - 2*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(\
      opx,-1) + 2*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) + 2*ln(x)*ln(opx)*pow(\
      NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) - 2*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(z,-1) + ln(\
      x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) - ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2) + ln(x)*ln(\
      opx)*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) - ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*z - 6*ln(x)*ln(\
      opx)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(\
      x,-1)*pow(z,-1)*pow(omz,-1) + 6*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) - 4*\
      ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*pow(z,-1)
            result +=  + 3*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*pow(opx,-1) - 2*ln(x)*ln(opx)*pow(NC,-1)*pow(\
      x,-1) + 3*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) - 2*ln(x)*ln(opx)*pow(NC,-1)*pow(\
      x,-1)*z - 6*ln(x)*ln(opx)*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 6*ln(x)*ln(opx)*pow(\
      NC,-1)*pow(z,-1)*pow(opx,-1) + 2*ln(x)*ln(opx)*pow(NC,-1)*pow(opx,-1) + ln(x)*ln(opx)*pow(\
      NC,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*z*pow(opx,-1) - ln(x)*ln(opx)*pow(NC,-1)*z - 2*ln(x)*ln(\
      opx)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 4*ln(x)*ln(opx)*pow(NC,-1)*x*pow(z,-1)*\
      pow(omz,-1) + 2*ln(x)*ln(opx)*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)\
      *x*pow(z,-1) + 2*ln(x)*ln(opx)*pow(NC,-1)*x + 2*ln(x)*ln(opx)*pow(NC,-1)*x*z*pow(opx,-1) + 2*\
      ln(x)*ln(opx)*pow(NC,-1)*x*z - 2*ln(x)*ln(opx)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + 2*\
      ln(x)*ln(opx)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(x)*ln(opx)*pow(NC,-1)*pow(x,2)*z - ln(x)*\
      ln(opx)*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) + ln(x)*ln(opx)*NC*pow(x,-2)*pow(z,-1) - ln(x)*ln(\
      opx)*NC*pow(x,-2)*z*pow(opx,-1) + ln(x)*ln(opx)*NC*pow(x,-2)*z - 3*ln(x)*ln(opx)*NC*pow(x,-1)\
      *pow(z,-1)*pow(opx,-1) + 2*ln(x)*ln(opx)*NC*pow(x,-1)*pow(z,-1) - 3*ln(x)*ln(opx)*NC*pow(\
      x,-1)*z*pow(opx,-1) + 2*ln(x)*ln(opx)*NC*pow(x,-1)*z - 4*ln(x)*ln(opx)*NC*pow(z,-1)*pow(\
      opx,-1) + ln(x)*ln(opx)*NC*pow(z,-1) + 2*ln(x)*ln(opx)*NC*pow(opx,-1) - 2*ln(x)*ln(opx)*NC - \
      4*ln(x)*ln(opx)*NC*z*pow(opx,-1)
            result +=  + ln(x)*ln(opx)*NC*z - 2*ln(x)*ln(opx)*NC*x*pow(z,-1)*pow(opx,-1) - 2*ln(x)*ln(opx)*\
      NC*x*pow(z,-1) + 2*ln(x)*ln(opx)*NC*x*pow(opx,-1) - 2*ln(x)*ln(opx)*NC*x*z*pow(opx,-1) - 2*\
      ln(x)*ln(opx)*NC*x*z - 2*ln(x)*ln(opx)*NC*pow(x,2)*pow(z,-1) + 2*ln(x)*ln(opx)*NC*pow(x,2) - \
      2*ln(x)*ln(opx)*NC*pow(x,2)*z + 23./8.*ln(z)*pow(NC,-1)*pow(z,-1) + 6*ln(z)*pow(NC,-1)*pow(\
      z,-1)*rln2*pow(opz,-1) - 5*ln(z)*pow(NC,-1)*pow(z,-1)*rln2 + 4*ln(z)*pow(NC,-1)*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) - 4*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 8*ln(z)*pow(NC,-1)*pow(z,-1)*\
      sqrtxz1*rln2*pow(opz,-1) - 8*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2 + 12*ln(z)*pow(NC,-1)*\
      pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1) + 24*ln(z)*pow(NC,-1)*pow(\
      sqrtxz1,-1)*rln2*pow(opz,-1) - 16*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2 + ln(z)*pow(NC,-1) + \
      4*ln(z)*pow(NC,-1)*rln2 - 4*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(z)*pow(\
      NC,-1)*z*pow(sqrtxz1,-1) - 8*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 8*ln(z)*\
      pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2 + 1./8.*ln(z)*pow(NC,-1)*z - 2*ln(z)*pow(NC,-1)*z*rln2 - 7*\
      ln(z)*pow(NC,-1)*x*pow(z,-1) - 12*ln(z)*pow(NC,-1)*x*pow(z,-1)*rln2*pow(opz,-1) + 10*ln(z)*\
      pow(NC,-1)*x*pow(z,-1)*rln2 - 8*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 8*ln(z)*\
      pow(NC,-1)*x*pow(z,-1)*sqrtxz1 - 16*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) + \
      16*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2
            result +=  - 40*ln(z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 32*ln(z)*pow(NC,-1)*x*pow(\
      sqrtxz1,-1) - 80*ln(z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 64*ln(z)*pow(NC,-1)*x*\
      pow(sqrtxz1,-1)*rln2 - 3./4.*ln(z)*pow(NC,-1)*x - 8*ln(z)*pow(NC,-1)*x*rln2 + 8*ln(z)*pow(\
      NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 16*ln(z)*\
      pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 16*ln(z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*\
      rln2 - ln(z)*pow(NC,-1)*x*z + 4*ln(z)*pow(NC,-1)*x*z*rln2 + 13./2.*ln(z)*pow(NC,-1)*pow(x,2)*\
      pow(z,-1) + 6*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*rln2*pow(opz,-1) - 4*ln(z)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)*rln2 + 4*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*ln(z)*\
      pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 8*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2*\
      pow(opz,-1) - 8*ln(z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2 + 44*ln(z)*pow(NC,-1)*pow(\
      x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 40*ln(z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + 88*ln(z)*\
      pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 80*ln(z)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1)*rln2 + 1./2.*ln(z)*pow(NC,-1)*pow(x,2) + 4*ln(z)*pow(NC,-1)*pow(x,2)*rln2 - 4*ln(\
      z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(z)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1) - 8*ln(z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 8*ln(z)*pow(\
      NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2
            result +=  + ln(z)*pow(NC,-1)*pow(x,2)*z - 4*ln(z)*pow(NC,-1)*pow(x,2)*z*rln2 - 16*ln(z)*pow(\
      NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) + 16*ln(z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - \
      32*ln(z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 32*ln(z)*pow(NC,-1)*pow(x,3)*\
      pow(sqrtxz1,-1)*rln2 - 5./32.*ln(z)*NC*pow(x,-1)*pow(z,-1) - 5./32.*ln(z)*NC*pow(x,-1) + 5./\
      32.*ln(z)*NC*pow(z,-2) - 63./16.*ln(z)*NC*pow(z,-1) + 2*ln(z)*NC*pow(z,-1)*rln2 + ln(z)*NC*\
      pow(z,-1)*sqrtxz1 - 33./16.*ln(z)*NC - ln(z)*NC*rln2 + 1./32.*ln(z)*NC*z + 2*ln(z)*NC*z*rln2\
       - 5./32.*ln(z)*NC*x*pow(z,-2) + 93./16.*ln(z)*NC*x*pow(z,-1) - 4*ln(z)*NC*x*pow(z,-1)*rln2\
       - 2*ln(z)*NC*x*pow(z,-1)*sqrtxz1 - 7./16.*ln(z)*NC*x + 2*ln(z)*NC*x*rln2 + 27./32.*ln(z)*NC*\
      x*z - 4*ln(z)*NC*x*z*rln2 - 131./32.*ln(z)*NC*pow(x,2)*pow(z,-1) + 4*ln(z)*NC*pow(x,2)*pow(\
      z,-1)*rln2 + 2*ln(z)*NC*pow(x,2)*pow(z,-1)*sqrtxz1 + 61./32.*ln(z)*NC*pow(x,2) + 2*ln(z)*NC*\
      pow(x,2)*rln2 - ln(z)*NC*pow(x,2)*z + 4*ln(z)*NC*pow(x,2)*z*rln2
            result +=   - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) + 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(z,-1) - 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*\
      ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 12*ln(z)*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) + 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)\
       - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1) + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1) + ln(z)*\
      ln(1 + sqrtxz1 - z)*pow(NC,-1)*z + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*pow(\
      opz,-1)
            result +=  - 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1) + 8*ln(z)*ln(1 + sqrtxz1 - z)*\
      pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) - 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(\
      z,-1)*sqrtxz1 + 40*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - 32*\
      ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1) + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*x - 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) + 8*ln(z)*\
      ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x\
      *z - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) + 2*ln(z)*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*\
      pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*\
      sqrtxz1 - 44*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 40*\
      ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - 2*ln(z)*ln(1 + sqrtxz1 - z)*\
      pow(NC,-1)*pow(x,2) + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(\
      opz,-1) - 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) + 2*ln(z)*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*z + 16*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 16*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - \
      ln(z)*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)
            result +=  + ln(z)*ln(1 + sqrtxz1 - z)*NC - ln(z)*ln(1 + sqrtxz1 - z)*NC*z + 2*ln(z)*ln(1 + \
      sqrtxz1 - z)*NC*x*pow(z,-1) - 2*ln(z)*ln(1 + sqrtxz1 - z)*NC*x + 2*ln(z)*ln(1 + sqrtxz1 - z)*\
      NC*x*z - 2*ln(z)*ln(1 + sqrtxz1 - z)*NC*pow(x,2)*pow(z,-1) - 2*ln(z)*ln(1 + sqrtxz1 - z)*NC*\
      pow(x,2)*z - 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) + 3*ln(z)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(z,-1) - 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*\
      pow(opz,-1) + 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 12*ln(z)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
      pow(sqrtxz1,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1) + 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1) + ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)\
      *x*pow(z,-1)*pow(opz,-1) - 6*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1) + 8*ln(z)*ln(1\
       + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*x*pow(z,-1)*sqrtxz1 + 40*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(\
      opz,-1) - 32*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1) + 4*ln(z)*ln(1 + sqrtxz1\
       + z)*pow(NC,-1)*x - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1)\
       + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)
            result +=  - 2*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z - 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)\
      *pow(x,2)*pow(z,-1)*pow(opz,-1) + 2*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)\
       - 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*ln(z)*\
      ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 - 44*ln(z)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 40*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
      x,2)*pow(sqrtxz1,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2) + 4*ln(z)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(z)*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) + 2*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*z + \
      16*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) - 16*ln(z)*ln(1\
       + sqrtxz1 + z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - ln(z)*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)\
       - ln(z)*ln(1 + sqrtxz1 + z)*NC*z + 2*ln(z)*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1) + 2*ln(z)*ln(1\
       + sqrtxz1 + z)*NC*x*z - 2*ln(z)*ln(1 + sqrtxz1 + z)*NC*pow(x,2)*pow(z,-1) - 2*ln(z)*ln(1 + \
      sqrtxz1 + z)*NC*pow(x,2) - 2*ln(z)*ln(1 + sqrtxz1 + z)*NC*pow(x,2)*z - ln(z)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*\
      pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) + ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*\
      pow(z,-1)*pow(opx,-1)
            result +=  - ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1) + 1./2.*ln(z)*ln(1 + x*\
      pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(opx,-1) - 1./2.*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(\
      x,-2) + 1./2.*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) - 1./2.*ln(z)*ln(1\
       + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z - 3*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*\
      pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(\
      z,-1)*pow(omz,-1) + 3*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) - \
      2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1) + 3./2.*ln(z)*ln(1 + x*pow(z,-1))*\
      pow(NC,-1)*pow(x,-1)*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1) + 3./2.*ln(\
      z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*pow(\
      NC,-1)*pow(x,-1)*z - 3*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1)\
       + 3*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*\
      pow(NC,-1)*pow(opx,-1) + 1./2.*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1) + 2*ln(z)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*z*pow(opx,-1) - 1./2.*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*z - ln(z)*ln(1\
       + x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 2*ln(z)*ln(1 + x*pow(z,-1))*\
      pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*pow(\
      opx,-1)
            result +=  + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1) + ln(z)*ln(1 + x*pow(z,-1))*pow(\
      NC,-1)*x + ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*z*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*\
      pow(NC,-1)*x*z - ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + ln(z)*\
      ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1) + ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(\
      x,2)*z - 1./2.*ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) + 1./2.*ln(z)*ln(\
      1 + x*pow(z,-1))*NC*pow(x,-2)*pow(z,-1) - 1./2.*ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,-2)*z*pow(\
      opx,-1) + 1./2.*ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,-2)*z - 3./2.*ln(z)*ln(1 + x*pow(z,-1))*NC\
      *pow(x,-1)*pow(z,-1)*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,-1)*pow(z,-1) - 3./2.*\
      ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,-1)*z*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,-1)\
      *z - 2*ln(z)*ln(1 + x*pow(z,-1))*NC*pow(z,-1)*pow(opx,-1) + 1./2.*ln(z)*ln(1 + x*pow(z,-1))*\
      NC*pow(z,-1) + ln(z)*ln(1 + x*pow(z,-1))*NC*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*NC - 2*\
      ln(z)*ln(1 + x*pow(z,-1))*NC*z*pow(opx,-1) + 1./2.*ln(z)*ln(1 + x*pow(z,-1))*NC*z - ln(z)*ln(\
      1 + x*pow(z,-1))*NC*x*pow(z,-1)*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*NC*x*pow(z,-1) + ln(z\
      )*ln(1 + x*pow(z,-1))*NC*x*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*NC*x*z*pow(opx,-1) - ln(z)\
      *ln(1 + x*pow(z,-1))*NC*x*z - ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,2)*pow(z,-1) + ln(z)*ln(1 + \
      x*pow(z,-1))*NC*pow(x,2)
            result +=  - ln(z)*ln(1 + x*pow(z,-1))*NC*pow(x,2)*z + ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*\
      pow(z,-1)*pow(omz,-1)*pow(opx,-1) - ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(\
      omz,-1) - ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) + ln(z)*ln(1 + x*z)*\
      pow(NC,-1)*pow(x,-2)*pow(z,-1) - 1./2.*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) + 1.\
      /2.*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2) - 1./2.*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z*\
      pow(opx,-1) + 1./2.*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z + 3*ln(z)*ln(1 + x*z)*pow(NC,-1)\
      *pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(\
      z,-1)*pow(omz,-1) - 3*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) + 2*ln(z)*\
      ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1) - 3./2.*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*\
      pow(opx,-1) + ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1) - 3./2.*ln(z)*ln(1 + x*z)*pow(NC,-1)*\
      pow(x,-1)*z*pow(opx,-1) + ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*z + 3*ln(z)*ln(1 + x*z)*pow(\
      NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 3*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*pow(\
      opx,-1) + ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) - ln(z)*ln(1 + x*z)*pow(NC,-1)*\
      pow(z,-1) - ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*z*pow(\
      opx,-1) + ln(z)*ln(1 + x*z)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 2*ln(z)*ln(1 + x\
      *z)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)
            result +=  - ln(z)*ln(1 + x*z)*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(\
      NC,-1)*x*pow(z,-1)*pow(opz,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*x - ln(z)*ln(1 + x*z)*pow(\
      NC,-1)*x*z*pow(opx,-1) + ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + ln(z)*\
      ln(1 + x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,2)*z + 1./2.*ln(z)*ln(1 + x*z)*NC*pow(\
      x,-2)*pow(z,-1)*pow(opx,-1) - 1./2.*ln(z)*ln(1 + x*z)*NC*pow(x,-2)*pow(z,-1) + 1./2.*ln(z)*\
      ln(1 + x*z)*NC*pow(x,-2)*z*pow(opx,-1) - 1./2.*ln(z)*ln(1 + x*z)*NC*pow(x,-2)*z + 3./2.*ln(z)\
      *ln(1 + x*z)*NC*pow(x,-1)*pow(z,-1)*pow(opx,-1) - ln(z)*ln(1 + x*z)*NC*pow(x,-1)*pow(z,-1) + \
      3./2.*ln(z)*ln(1 + x*z)*NC*pow(x,-1)*z*pow(opx,-1) - ln(z)*ln(1 + x*z)*NC*pow(x,-1)*z + 2*ln(\
      z)*ln(1 + x*z)*NC*pow(z,-1)*pow(opx,-1) - ln(z)*ln(1 + x*z)*NC*pow(opx,-1) + ln(z)*ln(1 + x*z\
      )*NC + 2*ln(z)*ln(1 + x*z)*NC*z*pow(opx,-1) + ln(z)*ln(1 + x*z)*NC*x*pow(z,-1)*pow(opx,-1) - \
      ln(z)*ln(1 + x*z)*NC*x*pow(opx,-1) + ln(z)*ln(1 + x*z)*NC*x*z*pow(opx,-1) + 2*ln(z)*ln(1 + x*\
      z)*NC*pow(x,2)*pow(z,-1) + 2*ln(z)*ln(1 + x*z)*NC*pow(x,2)*z + ln(z)*ln(z + x)*pow(NC,-1)*\
      pow(z,-1)*pow(opz,-1) - ln(z)*ln(z + x)*pow(NC,-1)*pow(z,-1) + 1./2.*ln(z)*ln(z + x)*pow(\
      NC,-1) - 1./2.*ln(z)*ln(z + x)*pow(NC,-1)*z - 2*ln(z)*ln(z + x)*pow(NC,-1)*x*pow(z,-1)*pow(\
      opz,-1)
            result +=  + 2*ln(z)*ln(z + x)*pow(NC,-1)*x*pow(z,-1) - ln(z)*ln(z + x)*pow(NC,-1)*x + ln(z)*ln(\
      z + x)*pow(NC,-1)*x*z + ln(z)*ln(z + x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) - ln(z)*ln(\
      z + x)*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(z)*ln(z + x)*pow(NC,-1)*pow(x,2)*z + 1./2.*ln(z)*\
      ln(z + x)*NC*pow(z,-1) + 1./2.*ln(z)*ln(z + x)*NC*z - ln(z)*ln(z + x)*NC*x*pow(z,-1) - ln(z)*\
      ln(z + x)*NC*x*z + ln(z)*ln(z + x)*NC*pow(x,2)*pow(z,-1) + ln(z)*ln(z + x)*NC*pow(x,2) + ln(z\
      )*ln(z + x)*NC*pow(x,2)*z - 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*\
      pow(opx,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) + 1./2.*pow(ln(z)\
      ,2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(\
      z,-1) + 1./4.*pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) - 1./4.*pow(ln(z),2)*pow(NC,-1)*\
      pow(x,-2) + 1./4.*pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) - 1./4.*pow(ln(z),2)*pow(\
      NC,-1)*pow(x,-2)*z - 3./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(\
      opx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1) + 3./2.*pow(ln(z),2)*pow(\
      NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) - pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1) + 3./4.*\
      pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*pow(opx,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-1) + 3./\
      4.*pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*\
      z
            result +=  - 3./2.*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 3./2.*pow(ln(z),2\
      )*pow(NC,-1)*pow(z,-1)*pow(opx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) + 1./2.*\
      pow(ln(z),2)*pow(NC,-1)*pow(z,-1) + 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(\
      opz,-1) - 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 15./2.*pow(ln(z),2)*pow(NC,-1)*\
      pow(sqrtxz1,-1)*pow(opz,-1) - 5*pow(ln(z),2)*pow(NC,-1)*pow(sqrtxz1,-1) + 1./2.*pow(ln(z),2)*\
      pow(NC,-1)*pow(omz,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(opx,-1) + 1./2.*pow(ln(z),2)*pow(\
      NC,-1) - 5./2.*pow(ln(z),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 5./2.*pow(ln(z),2)*\
      pow(NC,-1)*z*pow(sqrtxz1,-1) + pow(ln(z),2)*pow(NC,-1)*z*pow(opx,-1) + 1./4.*pow(ln(z),2)*\
      pow(NC,-1)*z - 1./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - pow(ln(z),\
      2)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1)\
       - 2*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*pow(opz,-1) - 5*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) + 5*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 - 25*pow(ln(z),2)*pow(\
      NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 20*pow(ln(z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1) - pow(ln(\
      z),2)*pow(NC,-1)*x*pow(omz,-1) + 5*pow(ln(z),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - \
      5*pow(ln(z),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*x*z*pow(opx,-1)\
       - 1./2.*pow(ln(z),2)*pow(NC,-1)*x*z
            result +=  - 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + pow(ln(z),2)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) + 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 5./\
      2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 5./2.*pow(ln(z),2)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 55./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*\
      pow(opz,-1) - 25*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + 1./2.*pow(ln(z),2)*pow(\
      NC,-1)*pow(x,2)*pow(omz,-1) + pow(ln(z),2)*pow(NC,-1)*pow(x,2) - 5./2.*pow(ln(z),2)*pow(\
      NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 5./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1) + 3./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*z - 10*pow(ln(z),2)*pow(NC,-1)*pow(x,3)*\
      pow(sqrtxz1,-1)*pow(opz,-1) + 10*pow(ln(z),2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - 1./4.*\
      pow(ln(z),2)*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) + 1./4.*pow(ln(z),2)*NC*pow(x,-2)*pow(z,-1)\
       - 1./4.*pow(ln(z),2)*NC*pow(x,-2)*z*pow(opx,-1) + 1./4.*pow(ln(z),2)*NC*pow(x,-2)*z - 3./4.*\
      pow(ln(z),2)*NC*pow(x,-1)*pow(z,-1)*pow(opx,-1) + 1./2.*pow(ln(z),2)*NC*pow(x,-1)*pow(z,-1)\
       - 3./4.*pow(ln(z),2)*NC*pow(x,-1)*z*pow(opx,-1) + 1./2.*pow(ln(z),2)*NC*pow(x,-1)*z - pow(\
      ln(z),2)*NC*pow(z,-1)*pow(opx,-1) - 1./2.*pow(ln(z),2)*NC*pow(z,-1) + 1./2.*pow(ln(z),2)*NC*\
      pow(opx,-1) - 1./2.*pow(ln(z),2)*NC - pow(ln(z),2)*NC*z*pow(opx,-1) - 1./4.*pow(ln(z),2)*NC*z\
       - 1./2.*pow(ln(z),2)*NC*x*pow(z,-1)*pow(opx,-1)
            result +=  + pow(ln(z),2)*NC*x*pow(z,-1) + 1./2.*pow(ln(z),2)*NC*x*pow(opx,-1) - 1./2.*pow(ln(z)\
      ,2)*NC*x*z*pow(opx,-1) + 1./2.*pow(ln(z),2)*NC*x*z - 2*pow(ln(z),2)*NC*pow(x,2)*pow(z,-1) - 3.\
      /2.*pow(ln(z),2)*NC*pow(x,2)*z + ln(z)*ln(omx)*pow(NC,-1) - 2*ln(z)*ln(omx)*pow(NC,-1)*x + 2*\
      ln(z)*ln(omx)*pow(NC,-1)*pow(x,2) - ln(z)*ln(omx)*NC + 2*ln(z)*ln(omx)*NC*x - 2*ln(z)*ln(omx)\
      *NC*pow(x,2) + 2*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*ln(z)*ln(omz)*\
      pow(NC,-1)*pow(z,-1)*sqrtxz1 + 6*ln(z)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(\
      z)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1) - 2*ln(z)*ln(omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(\
      opz,-1) + 2*ln(z)*ln(omz)*pow(NC,-1)*z*pow(sqrtxz1,-1) - 4*ln(z)*ln(omz)*pow(NC,-1)*x*pow(\
      z,-1)*sqrtxz1*pow(opz,-1) + 4*ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 - 20*ln(z)*ln(omz)\
      *pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 16*ln(z)*ln(omz)*pow(NC,-1)*x*pow(sqrtxz1,-1) + 4\
      *ln(z)*ln(omz)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(z)*ln(omz)*pow(NC,-1)*x*z*\
      pow(sqrtxz1,-1) + 2*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*ln(z)\
      *ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 22*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 20*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - 2*ln(z)*ln(\
      omz)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*\
      z*pow(sqrtxz1,-1)
            result +=  - 8*ln(z)*ln(omz)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) + 8*ln(z)*ln(omz)*\
      pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) + 15./8.*ln(omx)*pow(NC,-1)*pow(z,-1) - 7./4.*ln(omx)*\
      pow(NC,-1) + 3./8.*ln(omx)*pow(NC,-1)*z - 5*ln(omx)*pow(NC,-1)*x*pow(z,-1) + 4*ln(omx)*pow(\
      NC,-1)*x - 1./4.*ln(omx)*pow(NC,-1)*x*z + 9./2.*ln(omx)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 7./2.\
      *ln(omx)*pow(NC,-1)*pow(x,2) - 1./2.*ln(omx)*pow(NC,-1)*pow(x,2)*z - 15./8.*ln(omx)*NC*pow(\
      z,-1) + 7./4.*ln(omx)*NC - 3./8.*ln(omx)*NC*z + 5*ln(omx)*NC*x*pow(z,-1) - 4*ln(omx)*NC*x + 1.\
      /4.*ln(omx)*NC*x*z - 9./2.*ln(omx)*NC*pow(x,2)*pow(z,-1) + 7./2.*ln(omx)*NC*pow(x,2) + 1./2.*\
      ln(omx)*NC*pow(x,2)*z 
            result +=   - 1./2.*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1) + 1./2.*pow(ln(omx),2)*pow(NC,-1) - 1./4.*pow(ln(omx),\
      2)*pow(NC,-1)*z + pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1) - pow(ln(omx),2)*pow(NC,-1)*x + 1./2.\
      *pow(ln(omx),2)*pow(NC,-1)*x*z - pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + pow(ln(omx),2\
      )*pow(NC,-1)*pow(x,2) - 1./2.*pow(ln(omx),2)*pow(NC,-1)*pow(x,2)*z + 1./2.*pow(ln(omx),2)*NC*\
      pow(z,-1) - 1./2.*pow(ln(omx),2)*NC + 1./4.*pow(ln(omx),2)*NC*z - pow(ln(omx),2)*NC*x*pow(\
      z,-1) + pow(ln(omx),2)*NC*x - 1./2.*pow(ln(omx),2)*NC*x*z + pow(ln(omx),2)*NC*pow(x,2)*pow(\
      z,-1) - pow(ln(omx),2)*NC*pow(x,2) + 1./2.*pow(ln(omx),2)*NC*pow(x,2)*z - ln(omx)*ln(omz)*\
      pow(NC,-1)*pow(z,-1) + ln(omx)*ln(omz)*pow(NC,-1) - 1./2.*ln(omx)*ln(omz)*pow(NC,-1)*z + 2*\
      ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1) - 2*ln(omx)*ln(omz)*pow(NC,-1)*x + ln(omx)*ln(omz)*\
      pow(NC,-1)*x*z - 2*ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*ln(omx)*ln(omz)*pow(\
      NC,-1)*pow(x,2)
            result +=  - ln(omx)*ln(omz)*pow(NC,-1)*pow(x,2)*z + ln(omx)*ln(omz)*NC*pow(z,-1) - ln(omx)*ln(\
      omz)*NC + 1./2.*ln(omx)*ln(omz)*NC*z - 2*ln(omx)*ln(omz)*NC*x*pow(z,-1) + 2*ln(omx)*ln(omz)*\
      NC*x - ln(omx)*ln(omz)*NC*x*z + 2*ln(omx)*ln(omz)*NC*pow(x,2)*pow(z,-1) - 2*ln(omx)*ln(omz)*\
      NC*pow(x,2) + ln(omx)*ln(omz)*NC*pow(x,2)*z + 15./8.*ln(omz)*pow(NC,-1)*pow(z,-1) + 4*ln(omz)\
      *pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) - 4*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2\
       + 12*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 8*ln(omz)*pow(NC,-1)*pow(\
      sqrtxz1,-1)*rln2 - 7./4.*ln(omz)*pow(NC,-1) - 4*ln(omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*\
      pow(opz,-1) + 4*ln(omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2 + 3./8.*ln(omz)*pow(NC,-1)*z - 5*\
      ln(omz)*pow(NC,-1)*x*pow(z,-1) - 8*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) + \
      8*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2 - 40*ln(omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*\
      pow(opz,-1) + 32*ln(omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2 + 4*ln(omz)*pow(NC,-1)*x + 8*ln(\
      omz)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) - 8*ln(omz)*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1)*rln2 - 1./4.*ln(omz)*pow(NC,-1)*x*z + 9./2.*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)\
       + 4*ln(omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*rln2*pow(opz,-1) - 4*ln(omz)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*sqrtxz1*rln2 + 44*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*pow(\
      opz,-1)
            result +=  - 40*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2 - 7./2.*ln(omz)*pow(NC,-1)*pow(\
      x,2) - 4*ln(omz)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 4*ln(omz)*pow(\
      NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*rln2 - 1./2.*ln(omz)*pow(NC,-1)*pow(x,2)*z - 16*ln(omz)*\
      pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*rln2*pow(opz,-1) + 16*ln(omz)*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz1,-1)*rln2 - 15./8.*ln(omz)*NC*pow(z,-1) + 7./4.*ln(omz)*NC - 3./8.*ln(omz)*NC*z + 5*\
      ln(omz)*NC*x*pow(z,-1) - 4*ln(omz)*NC*x + 1./4.*ln(omz)*NC*x*z - 9./2.*ln(omz)*NC*pow(x,2)*\
      pow(z,-1) + 7./2.*ln(omz)*NC*pow(x,2) + 1./2.*ln(omz)*NC*pow(x,2)*z
            result +=  - 4*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)\
      *sqrtxz1 - 12*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) + 8*ln(omz)*\
      ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1) + 4*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*\
      pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1) + 8*\
      ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) - 8*ln(omz)*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 + 40*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*\
      pow(sqrtxz1,-1)*pow(opz,-1) - 32*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1) - 8\
      *ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) + 8*ln(omz)*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) - 4*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(\
      z,-1)*sqrtxz1
            result +=  - 44*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 40\
      *ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + 4*ln(omz)*ln(1 + sqrtxz1\
       - z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*ln(omz)*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) + 16*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 16*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)\
       - 2*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 2*ln(\
      omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 6*ln(omz)*ln(1 - 2*z + \
      pow(z,2) + 4*x*z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(omz)*ln(1 - 2*z + pow(z,2) + \
      4*x*z)*pow(NC,-1)*pow(sqrtxz1,-1) + 2*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*z*\
      pow(sqrtxz1,-1)*pow(opz,-1) - 2*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1) + 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(\
      opz,-1) - 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 + 20*ln(omz\
      )*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - 16*ln(omz)*ln(1\
       - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(sqrtxz1,-1) - 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4\
      *x*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*\
      pow(NC,-1)*x*z*pow(sqrtxz1,-1)
            result +=  - 2*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(\
      opz,-1) + 2*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 - 22\
      *ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 20*\
      ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) + 2*ln(omz)*ln(1\
       - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 2*ln(omz)*ln(1\
       - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) + 8*ln(omz)*ln(1 - 2*z + \
      pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) - 8*ln(omz)*ln(1 - 2*z + \
      pow(z,2) + 4*x*z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - 1./2.*pow(ln(omz),2)*pow(NC,-1)*pow(\
      z,-1) + 2*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*pow(ln(omz),2)*pow(\
      NC,-1)*pow(z,-1)*sqrtxz1 + 6*pow(ln(omz),2)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 4*pow(\
      ln(omz),2)*pow(NC,-1)*pow(sqrtxz1,-1) + 1./2.*pow(ln(omz),2)*pow(NC,-1) - 2*pow(ln(omz),2)*\
      pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*pow(ln(omz),2)*pow(NC,-1)*z*pow(sqrtxz1,-1) - 1./\
      4.*pow(ln(omz),2)*pow(NC,-1)*z + pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1) - 4*pow(ln(omz),2)*\
      pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1\
       - 20*pow(ln(omz),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 16*pow(ln(omz),2)*pow(NC,-1)*\
      x*pow(sqrtxz1,-1)
            result +=  - pow(ln(omz),2)*pow(NC,-1)*x + 4*pow(ln(omz),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(\
      opz,-1) - 4*pow(ln(omz),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 1./2.*pow(ln(omz),2)*pow(NC,-1)*x\
      *z - pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(\
      z,-1)*sqrtxz1*pow(opz,-1) - 2*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 22*pow(\
      ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 20*pow(ln(omz),2)*pow(NC,-1)*\
      pow(x,2)*pow(sqrtxz1,-1) + pow(ln(omz),2)*pow(NC,-1)*pow(x,2) - 2*pow(ln(omz),2)*pow(NC,-1)*\
      pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1) - 1./2.*pow(ln(omz),2)*pow(NC,-1)*pow(x,2)*z - 8*pow(ln(omz),2)*pow(NC,-1)*pow(\
      x,3)*pow(sqrtxz1,-1)*pow(opz,-1) + 8*pow(ln(omz),2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) + 1./\
      2.*pow(ln(omz),2)*NC*pow(z,-1) - 1./2.*pow(ln(omz),2)*NC + 1./4.*pow(ln(omz),2)*NC*z - pow(\
      ln(omz),2)*NC*x*pow(z,-1) + pow(ln(omz),2)*NC*x - 1./2.*pow(ln(omz),2)*NC*x*z + pow(ln(omz),2\
      )*NC*pow(x,2)*pow(z,-1) - pow(ln(omz),2)*NC*pow(x,2) + 1./2.*pow(ln(omz),2)*NC*pow(x,2)*z + 2\
      *Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) - \
      Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1) + 2*Li2(1./2. - 1.\
      /2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*Li2(1./\
      2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*sqrtxz1
            result +=  + 6*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)\
      *pow(opz,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(\
      sqrtxz1,-1) - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)\
      *z*pow(sqrtxz1,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*\
      pow(z,-1)*pow(opz,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x\
      *pow(z,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*\
      pow(z,-1)*sqrtxz1 - 20*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*\
      pow(sqrtxz1,-1)*pow(opz,-1) + 16*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*x*pow(sqrtxz1,-1) + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*\
      pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*Li2(1./2. - 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1
            result +=  + 22*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 20*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
      pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*\
      pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - 8*Li2(1./2. - 1./2.*pow(z,-1) - 1./\
      2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) + 8*Li2(1./2. - 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) + Li2(1./2. - 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*NC*x + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(x,2) - 2*Li2(\
      1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) + Li2(1./\
      2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1) + 2*Li2(1./2. + 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*Li2(1./2.\
       + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 6*Li2(1./2. + 1./\
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 4*Li2(1./2.\
       + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1) - 2*Li2(1./2. + 1./2.\
      *pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1)
            result +=  + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1) + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)\
      *pow(opz,-1) - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(\
      z,-1) - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*\
      pow(z,-1)*sqrtxz1 - 20*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*\
      pow(sqrtxz1,-1)*pow(opz,-1) + 16*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*x*pow(sqrtxz1,-1) + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1) - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*\
      pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*Li2(1./2. + 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 22*Li2(1./2. + 1.\
      /2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 20\
      *Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)\
       - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1)
            result +=  + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz1,-1) - 8*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,3)*\
      pow(sqrtxz1,-1)*pow(opz,-1) + 8*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*pow(x,3)*pow(sqrtxz1,-1) - Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC\
       + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x - 2*Li2(1./2. + 1./2.*pow(\
      z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(x,2) - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(\
      NC,-1)*pow(z,-1)*pow(opz,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1) - \
      2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 2*Li2(1./2.\
       - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 6*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.\
      *z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(\
      NC,-1)*pow(sqrtxz1,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1) + 2*Li2(1./2. - 1./\
      2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1\
       - 1./2.*z)*pow(NC,-1)*z*pow(sqrtxz1,-1) + Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*z\
       + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*pow(opz,-1) - 4*Li2(1./2. - \
      1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(\
      NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1)
            result +=  - 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 + 20*Li2(1./2.\
       - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - 16*Li2(1./2. - 1./2.*\
      sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(sqrtxz1,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(\
      NC,-1)*x - 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(opz,-1)\
       + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) - 2*Li2(1./2. - 1./2.\
      *sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*z - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)*pow(opz,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(\
      z,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(\
      opz,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 - 22*\
      Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) + 20*\
      Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - 2*Li2(1./2. - 1./2.\
      *sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,2) + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*\
      pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*\
      pow(x,2)*z*pow(sqrtxz1,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,2)*z + 8\
      *Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) - 8*\
      Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)
            result +=  - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*pow(z,-1) + Li2(1./2. - 1./2.*sqrtxz1 - 1./\
      2.*z)*NC - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*z + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)\
      *NC*x*pow(z,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*x + 2*Li2(1./2. - 1./2.*sqrtxz1\
       - 1./2.*z)*NC*x*z - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*pow(x,2)*pow(z,-1) - 2*Li2(1./\
      2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*pow(x,2)*z + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(\
      NC,-1)*pow(z,-1)*pow(opz,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1) - \
      2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 2*Li2(1./2.\
       - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1 - 6*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.\
      *z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(\
      NC,-1)*pow(sqrtxz1,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1) + 2*Li2(1./2. - 1./\
      2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1\
       + 1./2.*z)*pow(NC,-1)*z*pow(sqrtxz1,-1) - Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*z\
       - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*pow(opz,-1) + 4*Li2(1./2. - \
      1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(\
      NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*\
      pow(z,-1)*sqrtxz1
            result +=  + 20*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) - \
      16*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(sqrtxz1,-1) - 4*Li2(1./2. - 1./2.*\
      sqrtxz1 + 1./2.*z)*pow(NC,-1)*x - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*z + 2*Li2(1./2. - 1./2.*\
      sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 + \
      1./2.*z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*sqrtxz1 - 22*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 20*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2) + 2*Li2(1./2. - 1./2.\
      *sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) - 2*Li2(1./2. - 1./2.*\
      sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.\
      *z)*pow(NC,-1)*pow(x,2)*z + 8*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 8*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,3)*pow(\
      sqrtxz1,-1)
            result +=  + Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*pow(z,-1) - Li2(1./2. - 1./2.*sqrtxz1 + 1./\
      2.*z)*NC + Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*z - 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)\
      *NC*x*pow(z,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*x - 2*Li2(1./2. - 1./2.*sqrtxz1\
       + 1./2.*z)*NC*x*z + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*pow(x,2)*pow(z,-1) + 2*Li2(1./\
      2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*pow(x,2)*z + 4*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(z,-1)\
      *sqrtxz1*pow(opz,-1) - 4*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 12*Li2(pow(\
      sqrtxz1,-1)*omz)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 8*Li2(pow(sqrtxz1,-1)*omz)*pow(\
      NC,-1)*pow(sqrtxz1,-1) - 4*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1)\
       + 4*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*z*pow(sqrtxz1,-1) - 8*Li2(pow(sqrtxz1,-1)*omz)*pow(\
      NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 8*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1 - 40*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 32*Li2(pow(\
      sqrtxz1,-1)*omz)*pow(NC,-1)*x*pow(sqrtxz1,-1) + 8*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*z*\
      pow(sqrtxz1,-1)*pow(opz,-1) - 8*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 4*\
      Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*Li2(pow(\
      sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 44*Li2(pow(sqrtxz1,-1)*omz)*pow(\
      NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1)
            result +=  - 40*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - 4*Li2(pow(\
      sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*Li2(pow(sqrtxz1,-1)*\
      omz)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - 16*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,3)*\
      pow(sqrtxz1,-1)*pow(opz,-1) + 16*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1)\
       + 4*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*Li2( - sqrtxz1*\
      pow(omz,-1))*pow(NC,-1)*pow(z,-1)*sqrtxz1 + 12*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(sqrtxz1,-1) - 4*Li2(\
       - sqrtxz1*pow(omz,-1))*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*Li2( - sqrtxz1*pow(\
      omz,-1))*pow(NC,-1)*z*pow(sqrtxz1,-1) - 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1*pow(opz,-1) + 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1)*sqrtxz1 - 40*Li2(\
       - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 32*Li2( - sqrtxz1*pow(\
      omz,-1))*pow(NC,-1)*x*pow(sqrtxz1,-1) + 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) - 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 4*\
      Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 4*Li2( - \
      sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1 + 44*Li2( - sqrtxz1*pow(omz,-1))*\
      pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1)
            result +=  - 40*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1) - 4*Li2( - \
      sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 4*Li2( - sqrtxz1*\
      pow(omz,-1))*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - 16*Li2( - sqrtxz1*pow(omz,-1))*pow(\
      NC,-1)*pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1) + 16*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(\
      x,3)*pow(sqrtxz1,-1) + Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(\
      opx,-1) - Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) - Li2( - x*pow(z,-1)\
      )*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) + Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(\
      z,-1) - 1./2.*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(opx,-1) + 1./2.*Li2( - x*pow(z,-1)\
      )*pow(NC,-1)*pow(x,-2) - 1./2.*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) + 1./2.\
      *Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z + 3*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(\
      z,-1)*pow(omz,-1)*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(\
      omz,-1) - 3*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) + 2*Li2( - x*pow(\
      z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1) - 3./2.*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(\
      opx,-1) + Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1) - 3./2.*Li2( - x*pow(z,-1))*pow(NC,-1)*\
      pow(x,-1)*z*pow(opx,-1) + Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*z + 3*Li2( - x*pow(z,-1))*\
      pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1)
            result +=  - 3*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*pow(opx,-1) - Li2( - x*pow(z,-1))*pow(\
      NC,-1)*pow(z,-1)*pow(opz,-1) + Li2( - x*pow(z,-1))*pow(NC,-1)*pow(z,-1) - Li2( - x*pow(z,-1))\
      *pow(NC,-1)*pow(opx,-1) - Li2( - x*pow(z,-1))*pow(NC,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*z\
      *pow(opx,-1) + Li2( - x*pow(z,-1))*pow(NC,-1)*z + Li2( - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*\
      pow(omz,-1)*pow(opx,-1) + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) - Li2( - x\
      *pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)\
      *pow(opz,-1) - 4*Li2( - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1) - Li2( - x*pow(z,-1))*pow(NC,-1)*\
      x*z*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*x*z + Li2( - x*pow(z,-1))*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)*pow(omz,-1) - Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1) + \
      1./2.*Li2( - x*pow(z,-1))*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) - 1./2.*Li2( - x*pow(z,-1))*NC*\
      pow(x,-2)*pow(z,-1) + 1./2.*Li2( - x*pow(z,-1))*NC*pow(x,-2)*z*pow(opx,-1) - 1./2.*Li2( - x*\
      pow(z,-1))*NC*pow(x,-2)*z + 3./2.*Li2( - x*pow(z,-1))*NC*pow(x,-1)*pow(z,-1)*pow(opx,-1) - \
      Li2( - x*pow(z,-1))*NC*pow(x,-1)*pow(z,-1) + 3./2.*Li2( - x*pow(z,-1))*NC*pow(x,-1)*z*pow(\
      opx,-1) - Li2( - x*pow(z,-1))*NC*pow(x,-1)*z + 2*Li2( - x*pow(z,-1))*NC*pow(z,-1)*pow(opx,-1)\
       - Li2( - x*pow(z,-1))*NC*pow(z,-1) - Li2( - x*pow(z,-1))*NC*pow(opx,-1) + Li2( - x*pow(z,-1)\
      )*NC
            result +=  + 2*Li2( - x*pow(z,-1))*NC*z*pow(opx,-1) - Li2( - x*pow(z,-1))*NC*z + Li2( - x*pow(\
      z,-1))*NC*x*pow(z,-1)*pow(opx,-1) + 2*Li2( - x*pow(z,-1))*NC*x*pow(z,-1) - Li2( - x*pow(z,-1)\
      )*NC*x*pow(opx,-1) + Li2( - x*pow(z,-1))*NC*x*z*pow(opx,-1) + 2*Li2( - x*pow(z,-1))*NC*x*z - \
      2*Li2( - x*pow(z,-1))*NC*pow(x,2) - 2*Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*\
      pow(opx,-1) + 2*Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) + 2*Li2( - x)*pow(NC,-1)\
      *pow(x,-2)*pow(z,-1)*pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1) + Li2( - x)*\
      pow(NC,-1)*pow(x,-2)*pow(opx,-1) - Li2( - x)*pow(NC,-1)*pow(x,-2) + Li2( - x)*pow(NC,-1)*pow(\
      x,-2)*z*pow(opx,-1) - Li2( - x)*pow(NC,-1)*pow(x,-2)*z - 6*Li2( - x)*pow(NC,-1)*pow(x,-1)*\
      pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1) + \
      6*Li2( - x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(opx,-1) - 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*\
      pow(z,-1) + 3*Li2( - x)*pow(NC,-1)*pow(x,-1)*pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*pow(x,-1)\
       + 3*Li2( - x)*pow(NC,-1)*pow(x,-1)*z*pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*pow(x,-1)*z - 6*\
      Li2( - x)*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 6*Li2( - x)*pow(NC,-1)*pow(z,-1)*\
      pow(opx,-1) + 2*Li2( - x)*pow(NC,-1)*pow(opx,-1) + Li2( - x)*pow(NC,-1) + 4*Li2( - x)*pow(\
      NC,-1)*z*pow(opx,-1) - Li2( - x)*pow(NC,-1)*z - 2*Li2( - x)*pow(NC,-1)*x*pow(z,-1)*pow(\
      omz,-1)*pow(opx,-1)
            result +=  - 4*Li2( - x)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) + 2*Li2( - x)*pow(NC,-1)*x*pow(z,-1)\
      *pow(opx,-1) + 4*Li2( - x)*pow(NC,-1)*x*pow(z,-1) + 2*Li2( - x)*pow(NC,-1)*x + 2*Li2( - x)*\
      pow(NC,-1)*x*z*pow(opx,-1) + 2*Li2( - x)*pow(NC,-1)*x*z - 2*Li2( - x)*pow(NC,-1)*pow(x,2)*\
      pow(z,-1)*pow(omz,-1) + 2*Li2( - x)*pow(NC,-1)*pow(x,2)*pow(z,-1) + 2*Li2( - x)*pow(NC,-1)*\
      pow(x,2)*z - Li2( - x)*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) + Li2( - x)*NC*pow(x,-2)*pow(z,-1)\
       - Li2( - x)*NC*pow(x,-2)*z*pow(opx,-1) + Li2( - x)*NC*pow(x,-2)*z - 3*Li2( - x)*NC*pow(x,-1)\
      *pow(z,-1)*pow(opx,-1) + 2*Li2( - x)*NC*pow(x,-1)*pow(z,-1) - 3*Li2( - x)*NC*pow(x,-1)*z*pow(\
      opx,-1) + 2*Li2( - x)*NC*pow(x,-1)*z - 4*Li2( - x)*NC*pow(z,-1)*pow(opx,-1) + Li2( - x)*NC*\
      pow(z,-1) + 2*Li2( - x)*NC*pow(opx,-1) - 2*Li2( - x)*NC - 4*Li2( - x)*NC*z*pow(opx,-1) + Li2(\
       - x)*NC*z - 2*Li2( - x)*NC*x*pow(z,-1)*pow(opx,-1) - 2*Li2( - x)*NC*x*pow(z,-1) + 2*Li2( - x\
      )*NC*x*pow(opx,-1) - 2*Li2( - x)*NC*x*z*pow(opx,-1) - 2*Li2( - x)*NC*x*z - 2*Li2( - x)*NC*\
      pow(x,2)*pow(z,-1) + 2*Li2( - x)*NC*pow(x,2) - 2*Li2( - x)*NC*pow(x,2)*z + Li2( - x*z)*pow(\
      NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - Li2( - x*z)*pow(NC,-1)*pow(x,-2)*pow(\
      z,-1)*pow(omz,-1) - Li2( - x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(opx,-1) + Li2( - x*z)*pow(\
      NC,-1)*pow(x,-2)*pow(z,-1) - 1./2.*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*pow(opx,-1) + 1./2.*Li2(\
       - x*z)*pow(NC,-1)*pow(x,-2)
            result +=  - 1./2.*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*z*pow(opx,-1) + 1./2.*Li2( - x*z)*pow(NC,-1)\
      *pow(x,-2)*z + 3*Li2( - x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 2*Li2(\
       - x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1) - 3*Li2( - x*z)*pow(NC,-1)*pow(x,-1)*pow(\
      z,-1)*pow(opx,-1) + 2*Li2( - x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1) - 3./2.*Li2( - x*z)*pow(\
      NC,-1)*pow(x,-1)*pow(opx,-1) + Li2( - x*z)*pow(NC,-1)*pow(x,-1) - 3./2.*Li2( - x*z)*pow(\
      NC,-1)*pow(x,-1)*z*pow(opx,-1) + Li2( - x*z)*pow(NC,-1)*pow(x,-1)*z + 3*Li2( - x*z)*pow(\
      NC,-1)*pow(z,-1)*pow(omz,-1)*pow(opx,-1) - 3*Li2( - x*z)*pow(NC,-1)*pow(z,-1)*pow(opx,-1) + \
      Li2( - x*z)*pow(NC,-1)*pow(z,-1)*pow(opz,-1) - Li2( - x*z)*pow(NC,-1)*pow(z,-1) - Li2( - x*z)\
      *pow(NC,-1)*pow(opx,-1) - 2*Li2( - x*z)*pow(NC,-1)*z*pow(opx,-1) + Li2( - x*z)*pow(NC,-1)*x*\
      pow(z,-1)*pow(omz,-1)*pow(opx,-1) + 2*Li2( - x*z)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) - Li2(\
       - x*z)*pow(NC,-1)*x*pow(z,-1)*pow(opx,-1) - 2*Li2( - x*z)*pow(NC,-1)*x*pow(z,-1)*pow(opz,-1)\
       - 2*Li2( - x*z)*pow(NC,-1)*x - Li2( - x*z)*pow(NC,-1)*x*z*pow(opx,-1) + Li2( - x*z)*pow(\
      NC,-1)*pow(x,2)*pow(z,-1)*pow(omz,-1) + Li2( - x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(opz,-1)\
       - 2*Li2( - x*z)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(x,2)*z + 1./2.*\
      Li2( - x*z)*NC*pow(x,-2)*pow(z,-1)*pow(opx,-1) - 1./2.*Li2( - x*z)*NC*pow(x,-2)*pow(z,-1) + 1.\
      /2.*Li2( - x*z)*NC*pow(x,-2)*z*pow(opx,-1)
            result +=  - 1./2.*Li2( - x*z)*NC*pow(x,-2)*z + 3./2.*Li2( - x*z)*NC*pow(x,-1)*pow(z,-1)*pow(\
      opx,-1) - Li2( - x*z)*NC*pow(x,-1)*pow(z,-1) + 3./2.*Li2( - x*z)*NC*pow(x,-1)*z*pow(opx,-1)\
       - Li2( - x*z)*NC*pow(x,-1)*z + 2*Li2( - x*z)*NC*pow(z,-1)*pow(opx,-1) - Li2( - x*z)*NC*pow(\
      opx,-1) + Li2( - x*z)*NC + 2*Li2( - x*z)*NC*z*pow(opx,-1) + Li2( - x*z)*NC*x*pow(z,-1)*pow(\
      opx,-1) - Li2( - x*z)*NC*x*pow(opx,-1) + Li2( - x*z)*NC*x*z*pow(opx,-1) + 2*Li2( - x*z)*NC*\
      pow(x,2)*pow(z,-1) + 2*Li2( - x*z)*NC*pow(x,2)*z + 2*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + \
      sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*\
      Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*\
      pow(z,-1)*sqrtxz1 + 6*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + \
      sqrtxz1 - z)*z)*pow(NC,-1)*pow(sqrtxz1,-1)*pow(opz,-1) - 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1\
       + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(sqrtxz1,-1) - 2*Li2( - 1/(1\
       + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*z*pow(\
      sqrtxz1,-1)*pow(opz,-1) + 2*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1\
       + sqrtxz1 - z)*z)*pow(NC,-1)*z*pow(sqrtxz1,-1) - 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + \
      sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(opz,-1) + 4*\
      Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*\
      x*pow(z,-1)*sqrtxz1
            result +=  - 20*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z\
      )*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(opz,-1) + 16*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1\
       - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*x*pow(sqrtxz1,-1) + 4*Li2( - 1/(1 + sqrtxz1\
       - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*\
      pow(opz,-1) - 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z\
      )*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1) + 2*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*\
      sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(x,2)*pow(z,-1)*sqrtxz1*pow(opz,-1) - 2*Li2(\
       - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(\
      x,2)*pow(z,-1)*sqrtxz1 + 22*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1\
       + sqrtxz1 - z)*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(opz,-1) - 20*Li2( - 1/(1 + sqrtxz1\
       - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz1,-1) - 2*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z\
      )*z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1)*pow(opz,-1) + 2*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1\
       + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz1,-1) - 8*\
      Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*\
      pow(x,3)*pow(sqrtxz1,-1)*pow(opz,-1)
            result +=  + 8*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)\
      *pow(NC,-1)*pow(x,3)*pow(sqrtxz1,-1) + 2*Li2(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1)*\
      pow(opx,-1) - 2*Li2(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(omz,-1) - 2*Li2(x)*pow(NC,-1)*pow(\
      x,-2)*pow(z,-1)*pow(opx,-1) + 2*Li2(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1) - Li2(x)*pow(NC,-1)*\
      pow(x,-2)*pow(opx,-1) + Li2(x)*pow(NC,-1)*pow(x,-2) - Li2(x)*pow(NC,-1)*pow(x,-2)*z*pow(\
      opx,-1) + Li2(x)*pow(NC,-1)*pow(x,-2)*z + 6*Li2(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1)\
      *pow(opx,-1) - 4*Li2(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(omz,-1) - 6*Li2(x)*pow(NC,-1)*pow(\
      x,-1)*pow(z,-1)*pow(opx,-1) + 4*Li2(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1) - 3*Li2(x)*pow(NC,-1)*\
      pow(x,-1)*pow(opx,-1) + 2*Li2(x)*pow(NC,-1)*pow(x,-1) - 3*Li2(x)*pow(NC,-1)*pow(x,-1)*z*pow(\
      opx,-1) + 2*Li2(x)*pow(NC,-1)*pow(x,-1)*z + 6*Li2(x)*pow(NC,-1)*pow(z,-1)*pow(omz,-1)*pow(\
      opx,-1) - 6*Li2(x)*pow(NC,-1)*pow(z,-1)*pow(opx,-1) - 1./4.*Li2(x)*pow(NC,-1)*pow(z,-1) - 2*\
      Li2(x)*pow(NC,-1)*pow(omz,-1) - 2*Li2(x)*pow(NC,-1)*pow(opx,-1) + 1./2.*Li2(x)*pow(NC,-1) - 4\
      *Li2(x)*pow(NC,-1)*z*pow(opx,-1) + 3./2.*Li2(x)*pow(NC,-1)*z + 2*Li2(x)*pow(NC,-1)*x*pow(\
      z,-1)*pow(omz,-1)*pow(opx,-1) + 4*Li2(x)*pow(NC,-1)*x*pow(z,-1)*pow(omz,-1) - 2*Li2(x)*pow(\
      NC,-1)*x*pow(z,-1)*pow(opx,-1) - 7./2.*Li2(x)*pow(NC,-1)*x*pow(z,-1) - 4*Li2(x)*pow(NC,-1)*x*\
      pow(omz,-1)
            result +=  - Li2(x)*pow(NC,-1)*x - 2*Li2(x)*pow(NC,-1)*x*z*pow(opx,-1) + 2*Li2(x)*pow(NC,-1)*\
      pow(x,2)*pow(z,-1)*pow(omz,-1) - 3*Li2(x)*pow(NC,-1)*pow(x,2)*pow(z,-1) - 2*Li2(x)*pow(NC,-1)\
      *pow(x,2)*pow(omz,-1) + Li2(x)*pow(NC,-1)*pow(x,2) - Li2(x)*pow(NC,-1)*pow(x,2)*z + Li2(x)*NC\
      *pow(x,-2)*pow(z,-1)*pow(opx,-1) - Li2(x)*NC*pow(x,-2)*pow(z,-1) + Li2(x)*NC*pow(x,-2)*z*pow(\
      opx,-1) - Li2(x)*NC*pow(x,-2)*z + 3*Li2(x)*NC*pow(x,-1)*pow(z,-1)*pow(opx,-1) - 2*Li2(x)*NC*\
      pow(x,-1)*pow(z,-1) + 3*Li2(x)*NC*pow(x,-1)*z*pow(opx,-1) - 2*Li2(x)*NC*pow(x,-1)*z + 4*Li2(x\
      )*NC*pow(z,-1)*pow(opx,-1) - 7./4.*Li2(x)*NC*pow(z,-1) - 2*Li2(x)*NC*pow(opx,-1) + 3./2.*Li2(\
      x)*NC + 4*Li2(x)*NC*z*pow(opx,-1) - 3./2.*Li2(x)*NC*z + 2*Li2(x)*NC*x*pow(z,-1)*pow(opx,-1)\
       - 1./2.*Li2(x)*NC*x*pow(z,-1) - 2*Li2(x)*NC*x*pow(opx,-1) + Li2(x)*NC*x + 2*Li2(x)*NC*x*z*\
      pow(opx,-1) + Li2(x)*NC*pow(x,2)*pow(z,-1) - Li2(x)*NC*pow(x,2) + Li2(x)*NC*pow(x,2)*z - Li2(\
      z)*pow(NC,-1) + 2*Li2(z)*pow(NC,-1)*x - 2*Li2(z)*pow(NC,-1)*pow(x,2) + Li2(z)*NC - 2*Li2(z)*\
      NC*x + 2*Li2(z)*NC*pow(x,2)
        else:
            result = 0
    elif orders == '001':
        if rsl == 'rr':
            result = - 11./8.*LMUA*pow(NC,-1)*pow(z,-1) + 5./4.*LMUA*pow(NC,-1) + 1./8.*\
            LMUA*pow(NC,-1)*z + 15./4.*LMUA*pow(NC,-1)*x*pow(z,-1) - 7./2.*LMUA*pow(NC,-1)*x + 1./4.*LMUA\
            *pow(NC,-1)*x*z - 15./4.*LMUA*pow(NC,-1)*pow(x,2)*pow(z,-1) + 7./2.*LMUA*pow(NC,-1)*pow(x,2)\
            - 1./4.*LMUA*pow(NC,-1)*pow(x,2)*z + 11./8.*LMUA*NC*pow(z,-1) - 5./4.*LMUA*NC - 1./8.*LMUA*\
            NC*z - 15./4.*LMUA*NC*x*pow(z,-1) + 7./2.*LMUA*NC*x - 1./4.*LMUA*NC*x*z + 15./4.*LMUA*NC*pow(\
            x,2)*pow(z,-1) - 7./2.*LMUA*NC*pow(x,2) + 1./4.*LMUA*NC*pow(x,2)*z - 1./2.*ln(x)*LMUA*pow(NC,-1)*pow(z,-1) + 1./2.*ln(x)*LMUA*\
            pow(NC,-1) - 1./4.*ln(x)*LMUA*pow(NC,-1)*z + ln(x)*LMUA*pow(NC,-1)*x*pow(z,-1) - ln(x)*LMUA*\
            pow(NC,-1)*x + 1./2.*ln(x)*LMUA*pow(NC,-1)*x*z - ln(x)*LMUA*pow(NC,-1)*pow(x,2)*pow(z,-1) + \
            ln(x)*LMUA*pow(NC,-1)*pow(x,2) - 1./2.*ln(x)*LMUA*pow(NC,-1)*pow(x,2)*z + 1./2.*ln(x)*LMUA*NC\
            *pow(z,-1) - 1./2.*ln(x)*LMUA*NC + 1./4.*ln(x)*LMUA*NC*z - ln(x)*LMUA*NC*x*pow(z,-1) + ln(x)*\
            LMUA*NC*x - 1./2.*ln(x)*LMUA*NC*x*z + ln(x)*LMUA*NC*pow(x,2)*pow(z,-1) - ln(x)*LMUA*NC*pow(\
            x,2) + 1./2.*ln(x)*LMUA*NC*pow(x,2)*z - 1./2.*ln(z)\
            *LMUA*pow(NC,-1)*pow(z,-1) - 1./2.*ln(z)*LMUA*pow(NC,-1) - 1./4.*ln(z)*LMUA*pow(NC,-1)*z + \
            ln(z)*LMUA*pow(NC,-1)*x*pow(z,-1) + ln(z)*LMUA*pow(NC,-1)*x + 1./2.*ln(z)*LMUA*pow(NC,-1)*x*z\
            - ln(z)*LMUA*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(z)*LMUA*pow(NC,-1)*pow(x,2) - 1./2.*ln(z)*\
            LMUA*pow(NC,-1)*pow(x,2)*z + 1./2.*ln(z)*LMUA*NC*pow(z,-1) + 1./2.*ln(z)*LMUA*NC + 1./4.*ln(z\
            )*LMUA*NC*z - ln(z)*LMUA*NC*x*pow(z,-1) - ln(z)*LMUA*NC*x - 1./2.*ln(z)*LMUA*NC*x*z + ln(z)*\
            LMUA*NC*pow(x,2)*pow(z,-1) + ln(z)*LMUA*NC*pow(x,2) + 1./2.*ln(z)*LMUA*NC*pow(x,2)*z + 1./2.*ln(omx)*LMUA*pow(\
            NC,-1)*pow(z,-1) - 1./2.*ln(omx)*LMUA*pow(NC,-1) + 1./4.*ln(omx)*LMUA*pow(NC,-1)*z - ln(omx)*\
            LMUA*pow(NC,-1)*x*pow(z,-1) + ln(omx)*LMUA*pow(NC,-1)*x - 1./2.*ln(omx)*LMUA*pow(NC,-1)*x*z + ln(omx)*LMUA*pow(\
            NC,-1)*pow(x,2)*pow(z,-1) - ln(omx)*LMUA*pow(NC,-1)*pow(x,2) + 1./2.*ln(omx)*LMUA*pow(NC,-1)*\
            pow(x,2)*z - 1./2.*ln(omx)*LMUA*NC*pow(z,-1) + 1./2.*ln(omx)*LMUA*NC - 1./4.*ln(omx)*LMUA*NC*\
            z + ln(omx)*LMUA*NC*x*pow(z,-1) - ln(omx)*LMUA*NC*x + 1./2.*ln(omx)*LMUA*NC*x*z - ln(omx)*\
            LMUA*NC*pow(x,2)*pow(z,-1) + ln(omx)*LMUA*NC*pow(x,2) - 1./2.*ln(omx)*LMUA*NC*pow(x,2)*z \
            + 1./2.*ln(omz)*LMUA*pow(NC,-1)*pow(z,-1) - 1./2.*ln(omz)*LMUA*pow(NC,-1) + 1./\
            4.*ln(omz)*LMUA*pow(NC,-1)*z - ln(omz)*LMUA*pow(NC,-1)*x*pow(z,-1) + ln(omz)*LMUA*pow(NC,-1)*\
            x - 1./2.*ln(omz)*LMUA*pow(NC,-1)*x*z + ln(omz)*LMUA*pow(NC,-1)*pow(x,2)*pow(z,-1) - \
            ln(omz)*LMUA*pow(NC,-1)*pow(x,2) + 1./2.*ln(omz)*LMUA*pow(NC,-1)*pow(x,2)*z - 1./2.*ln(omz)*\
            LMUA*NC*pow(z,-1) + 1./2.*ln(omz)*LMUA*NC - 1./4.*ln(omz)*LMUA*NC*z + ln(omz)*LMUA*NC*x*pow(\
            z,-1) - ln(omz)*LMUA*NC*x + 1./2.*ln(omz)*LMUA*NC*x*z - ln(omz)*LMUA*NC*pow(x,2)*pow(z,-1) + \
            ln(omz)*LMUA*NC*pow(x,2) - 1./2.*ln(omz)*LMUA*NC*pow(x,2)*z
        else:
            result = 0
    elif orders == '010':
        if rsl == 'rr':
            result =  - 1./2.*LMUF*pow(NC,-1)*pow(z,-1) + 1./2.*LMUF*pow(NC,-1) - 1./2.*LMUF*pow(NC,-1)*z + 5./4.*\
            LMUF*pow(NC,-1)*x*pow(z,-1) - 1./2.*LMUF*pow(NC,-1)*x - 3./4.*LMUF*pow(NC,-1)*pow(x,2)*pow(\
            z,-1) + 3./4.*LMUF*pow(NC,-1)*pow(x,2)*z + 1./2.*LMUF*NC*pow(z,-1) - 1./2.*LMUF*NC + 1./2.*\
            LMUF*NC*z - 5./4.*LMUF*NC*x*pow(z,-1) + 1./2.*LMUF*NC*x + 3./4.*LMUF*NC*pow(x,2)*pow(z,-1) - \
            3./4.*LMUF*NC*pow(x,2)*z - 1./4.*ln(x)*LMUF*pow(NC,-1)*pow(z,-1) - 1./4.*ln(x)*LMUF*pow(\
            NC,-1)*z + 1./2.*ln(x)*LMUF*pow(NC,-1)*x*pow(z,-1) - 1./2.*ln(x)*LMUF*pow(NC,-1)*x*z - ln(x)*\
            LMUF*pow(NC,-1)*pow(x,2)*pow(z,-1) + ln(x)*LMUF*pow(NC,-1)*pow(x,2) - 1./2.*ln(x)*LMUF*pow(\
            NC,-1)*pow(x,2)*z + 1./4.*ln(x)*LMUF*NC*pow(z,-1) + 1./4.*ln(x)*LMUF*NC*z - 1./2.*ln(x)*LMUF*NC*x*pow(\
            z,-1) + 1./2.*ln(x)*LMUF*NC*x*z + ln(x)*LMUF*NC*pow(x,2)*pow(z,-1) - ln(x)*LMUF*NC*pow(x,2)\
            + 1./2.*ln(x)*LMUF*NC*pow(x,2)*z   + 1./2.*ln(z)*LMUF*pow(\
            NC,-1)*pow(z,-1) - 1./2.*ln(z)*LMUF*pow(NC,-1) + 1./4.*ln(z)*LMUF*pow(NC,-1)*z - ln(z)*LMUF*\
            pow(NC,-1)*x*pow(z,-1) + ln(z)*LMUF*pow(NC,-1)*x - 1./2.*ln(z)*LMUF*pow(NC,-1)*x*z + ln(z)*\
            LMUF*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(z)*LMUF*pow(NC,-1)*pow(x,2) + 1./2.*ln(z)*LMUF*pow(\
            NC,-1)*pow(x,2)*z - 1./2.*ln(z)*LMUF*NC*pow(z,-1) + 1./2.*ln(z)*LMUF*NC - 1./4.*ln(z)*LMUF*NC\
            *z + ln(z)*LMUF*NC*x*pow(z,-1) - ln(z)*LMUF*NC*x + 1./2.*ln(z)*LMUF*NC*x*z - ln(z)*LMUF*\
            NC*pow(x,2)*pow(z,-1) + ln(z)*LMUF*NC*pow(x,2) - 1./2.*ln(z)*LMUF*NC*pow(x,2)*z  + 1./2.*ln(omx)*LMUF*pow(NC,-1)*pow(z,-1) - 1./2.*ln(omx)*LMUF*pow(\
            NC,-1) + 1./4.*ln(omx)*LMUF*pow(NC,-1)*z - ln(omx)*LMUF*pow(NC,-1)*x*pow(z,-1) + ln(omx)*LMUF\
            *pow(NC,-1)*x - 1./2.*ln(omx)*LMUF*pow(NC,-1)*x*z + ln(omx)*LMUF*pow(NC,-1)*pow(x,2)*pow(\
            z,-1) - ln(omx)*LMUF*pow(NC,-1)*pow(x,2) + 1./2.*ln(omx)*LMUF*pow(NC,-1)*pow(x,2)*z - 1./2.*\
            ln(omx)*LMUF*NC*pow(z,-1) + 1./2.*ln(omx)*LMUF*NC - 1./4.*ln(omx)*LMUF*NC*z + ln(omx)*LMUF*NC\
            *x*pow(z,-1) - ln(omx)*LMUF*NC*x + 1./2.*ln(omx)*LMUF*NC*x*z - ln(omx)*LMUF*NC*pow(x,2)*pow(\
            z,-1) + ln(omx)*LMUF*NC*pow(x,2) - 1./2.*ln(omx)*LMUF*NC*pow(x,2)*z  + 1./2.*ln(omz)*LMUF*pow(\
            NC,-1)*pow(z,-1) - 1./2.*ln(omz)*LMUF*pow(NC,-1) + 1./4.*ln(omz)*LMUF*pow(NC,-1)*z - ln(omz)*\
            LMUF*pow(NC,-1)*x*pow(z,-1) + ln(omz)*LMUF*pow(NC,-1)*x - 1./2.*ln(omz)*LMUF*pow(NC,-1)*x*z\
            + ln(omz)*LMUF*pow(NC,-1)*pow(x,2)*pow(z,-1) - ln(omz)*LMUF*pow(NC,-1)*pow(x,2) + 1./2.*ln(\
            omz)*LMUF*pow(NC,-1)*pow(x,2)*z - 1./2.*ln(omz)*LMUF*NC*pow(z,-1) + 1./2.*ln(omz)*LMUF*NC - 1.\
            /4.*ln(omz)*LMUF*NC*z + ln(omz)*LMUF*NC*x*pow(z,-1) - ln(omz)*LMUF*NC*x + 1./2.*ln(omz)*LMUF*\
            NC*x*z - ln(omz)*LMUF*NC*pow(x,2)*pow(z,-1) + ln(omz)*LMUF*NC*pow(x,2) - 1./2.*ln(omz)*LMUF*\
            NC*pow(x,2)*z
        else:
            result = 0
    elif orders == '011':
        if rsl == 'rr':
            result = - 1./2.*LMUA*LMUF*pow(\
            NC,-1)*pow(z,-1) + 1./2.*LMUA*LMUF*pow(NC,-1) - 1./4.*LMUA*LMUF*pow(NC,-1)*z + LMUA*LMUF*pow(\
            NC,-1)*x*pow(z,-1) - LMUA*LMUF*pow(NC,-1)*x + 1./2.*LMUA*LMUF*pow(NC,-1)*x*z - LMUA*LMUF*pow(\
            NC,-1)*pow(x,2)*pow(z,-1) + LMUA*LMUF*pow(NC,-1)*pow(x,2) - 1./2.*LMUA*LMUF*pow(NC,-1)*pow(\
            x,2)*z + 1./2.*LMUA*LMUF*NC*pow(z,-1) - 1./2.*LMUA*LMUF*NC + 1./4.*LMUA*LMUF*NC*z - LMUA*LMUF\
            *NC*x*pow(z,-1) + LMUA*LMUF*NC*x - 1./2.*LMUA*LMUF*NC*x*z + LMUA*LMUF*NC*pow(x,2)*pow(z,-1) \
            - LMUA*LMUF*NC*pow(x,2) + 1./2.*LMUA*LMUF*NC*pow(x,2)*z
        else:
            result = 0
    else:
        result = 0

    return result
