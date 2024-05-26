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

def ct_nnlo_q2qb_eq(x, z, rsl, orders):

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
                result += - 2./3.*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(pi,2)*CF*pow(omz,-1)*pow(opx,-1) + 2./3.*pow(\
          NC,-1)*pow(x,-2)*pow(z,-1)*pow(pi,2)*CF*pow(omz,-1) + 2./3.*pow(NC,-1)*pow(x,-2)*pow(z,-1)*\
          pow(pi,2)*CF*pow(opx,-1) - 2./3.*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(pi,2)*CF + 2./3.*pow(\
          NC,-1)*pow(x,-2)*pow(pi,2)*CF*pow(opx,-1) - 2./3.*pow(NC,-1)*pow(x,-2)*pow(pi,2)*CF + 2./3.*\
          pow(NC,-1)*pow(x,-2)*z*pow(pi,2)*CF*pow(opx,-1) - 2./3.*pow(NC,-1)*pow(x,-2)*z*pow(pi,2)*CF\
           - 2./3.*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omz,-1)*pow(opx,-1) + 2./3.*pow(\
          NC,-1)*pow(x,-1)*pow(z,-1)*pow(pi,2)*CF*pow(opx,-1) + 2./3.*pow(NC,-1)*pow(x,-1)*pow(pi,2)*CF\
          *pow(opx,-1) + 2./3.*pow(NC,-1)*pow(x,-1)*z*pow(pi,2)*CF*pow(opx,-1) + 4*pow(NC,-1)*pow(z,-1)\
          *CF + 8*pow(NC,-1)*pow(z,-1)*pow(rln2,2)*CF*pow(omx,-1)*pow(opz,-1) - 8*pow(NC,-1)*pow(z,-1)*\
          pow(rln2,2)*CF*pow(omx,-1) + 16*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1)*pow(opz,-1)\
           - 16*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1) + 12*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(\
          rln2,2)*CF*pow(omx,-1)*pow(opz,-1) - 12*pow(NC,-1)*pow(z,-1)*sqrtxz1*pow(rln2,2)*CF*pow(\
          omx,-1) + 1./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) - 2./3.*pow(NC,-1)*pow(z,-1)*\
          pow(pi,2)*CF*pow(omz,-1)*pow(opx,-1) + 2./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(opx,-1) - \
          1./6.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF + 2./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*sqrtxz1*CF*\
          pow(omx,-1)*pow(opz,-1)
                result +=  - 2./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*sqrtxz1*CF*pow(omx,-1) - 16*pow(NC,-1)*pow(\
          sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) + 32*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(\
          omx,-1) + 64*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 64*pow(NC,-1)*pow(sqrtxz1,-1)*\
          rln2*CF - 12*pow(NC,-1)*pow(sqrtxz1,-1)*pow(rln2,2)*CF*pow(omx,-1)*pow(opz,-1) + 24*pow(\
          NC,-1)*pow(sqrtxz1,-1)*pow(rln2,2)*CF*pow(omx,-1) + 48*pow(NC,-1)*pow(sqrtxz1,-1)*pow(rln2,2)\
          *CF*pow(opz,-1) - 48*pow(NC,-1)*pow(sqrtxz1,-1)*pow(rln2,2)*CF - 8*pow(NC,-1)*CF + 6*pow(\
          NC,-1)*pow(rln2,2)*CF*pow(omx,-1) - 2*pow(NC,-1)*sqrtxz1*rln2*CF*pow(omx,-1) - 2./3.*pow(\
          NC,-1)*pow(pi,2)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4./3.*pow(NC,-1)*pow(pi,2)*pow(\
          sqrtxz1,-1)*CF*pow(omx,-1) + 8./3.*pow(NC,-1)*pow(pi,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8./3.\
          *pow(NC,-1)*pow(pi,2)*pow(sqrtxz1,-1)*CF - 1./3.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1)*pow(\
          opz,-1) - 1./2.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1) + 2./3.*pow(NC,-1)*pow(pi,2)*CF*pow(\
          omz,-1)*pow(opx,-1) - 1./3.*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) + 2./3.*pow(NC,-1)*pow(pi,2)*\
          CF - 16*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) + 16*pow(NC,-1)*z*pow(\
          sqrtxz1,-1)*rln2*CF*pow(omx,-1) - 12*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(rln2,2)*CF*pow(omx,-1)*\
          pow(opz,-1) + 12*pow(NC,-1)*z*pow(sqrtxz1,-1)*pow(rln2,2)*CF*pow(omx,-1) + 10*pow(NC,-1)*z*CF\
           - 6*pow(NC,-1)*z*pow(rln2,2)*CF*pow(omx,-1)
                result +=  - 2./3.*pow(NC,-1)*z*pow(pi,2)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 2./3.*\
          pow(NC,-1)*z*pow(pi,2)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 1./6.*pow(NC,-1)*z*pow(pi,2)*CF*pow(\
          omx,-1) - 1./3.*pow(NC,-1)*z*pow(pi,2)*CF*pow(opx,-1) - 7./2.*pow(NC,-1)*x*pow(z,-1)*CF - 8*\
          pow(NC,-1)*x*pow(z,-1)*pow(rln2,2)*CF*pow(opz,-1) + 8*pow(NC,-1)*x*pow(z,-1)*pow(rln2,2)*CF\
           - 16*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF*pow(opz,-1) + 16*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*\
          rln2*CF - 12*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*pow(rln2,2)*CF*pow(opz,-1) + 12*pow(NC,-1)*x*pow(\
          z,-1)*sqrtxz1*pow(rln2,2)*CF - 2./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*CF*pow(omz,-1) + 1./2.*\
          pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*CF - 2./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*sqrtxz1*CF*pow(\
          opz,-1) + 2./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*sqrtxz1*CF - 48*pow(NC,-1)*x*pow(sqrtxz1,-1)\
          *rln2*CF*pow(opz,-1) + 32*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*CF - 36*pow(NC,-1)*x*pow(\
          sqrtxz1,-1)*pow(rln2,2)*CF*pow(opz,-1) + 24*pow(NC,-1)*x*pow(sqrtxz1,-1)*pow(rln2,2)*CF + 7*\
          pow(NC,-1)*x*CF - 8*pow(NC,-1)*x*pow(rln2,2)*CF - 2*pow(NC,-1)*x*pow(pi,2)*pow(sqrtxz1,-1)*CF\
          *pow(opz,-1) + 4./3.*pow(NC,-1)*x*pow(pi,2)*pow(sqrtxz1,-1)*CF + 2./3.*pow(NC,-1)*x*pow(pi,2)\
          *CF*pow(omz,-1) + 1./3.*pow(NC,-1)*x*pow(pi,2)*CF + 16*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*CF\
          *pow(opz,-1) - 16*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*CF + 12*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*\
          pow(rln2,2)*CF*pow(opz,-1)
                result +=  - 12*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*pow(rln2,2)*CF - 19./2.*pow(NC,-1)*x*z*CF + 8*\
          pow(NC,-1)*x*z*pow(rln2,2)*CF + 2./3.*pow(NC,-1)*x*z*pow(pi,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1)\
           - 2./3.*pow(NC,-1)*x*z*pow(pi,2)*pow(sqrtxz1,-1)*CF - 2./3.*pow(NC,-1)*x*z*pow(pi,2)*CF + 64\
          *pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 64*pow(NC,-1)*pow(x,2)*pow(\
          sqrtxz1,-1)*rln2*CF + 48*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(rln2,2)*CF*pow(opz,-1) - 48*\
          pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*pow(rln2,2)*CF + 8./3.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) - 8./3.*pow(NC,-1)*pow(x,2)*pow(pi,2)*pow(sqrtxz1,-1)*CF - 1./3.*\
          pow(x,-2)*pow(pi,2)*CF*pow(opx,-1) + 1./3.*pow(x,-2)*pow(pi,2)*CF + 2./3.*pow(x,-2)*z*pow(\
          pi,2)*CF*pow(opx,-1) - 2./3.*pow(x,-2)*z*pow(pi,2)*CF - 4./3.*pow(x,-2)*pow(z,2)*pow(pi,2)*CF\
          *pow(opx,-1) + 4./3.*pow(x,-2)*pow(z,2)*pow(pi,2)*CF + 13./9.*pow(x,-1)*pow(z,-1)*CF - 26./9.\
          *pow(x,-1)*CF - 1./3.*pow(x,-1)*pow(pi,2)*CF + 2./3.*pow(x,-1)*z*pow(pi,2)*CF - 4./3.*pow(\
          x,-1)*pow(z,2)*pow(pi,2)*CF*pow(opx,-1) - 71./36.*pow(z,-1)*CF + 1./6.*pow(z,-1)*pow(pi,2)*CF\
           - 26./3.*CF - 6*pow(rln2,2)*CF*pow(omx,-1) - 6*sqrtxz1*rln2*CF*pow(omx,-1) + 5./6.*pow(pi,2)\
          *CF*pow(omx,-1) + 2./3.*pow(pi,2)*CF*pow(opx,-1) - 1./6.*pow(pi,2)*CF + 157./12.*z*CF - 4*z*\
          pow(rln2,2)*CF*pow(omx,-1) + 8*z*pow(rln2,2)*CF - 5./3.*z*pow(pi,2)*CF*pow(omx,-1) - 4./3.*z*\
          pow(pi,2)*CF*pow(opx,-1)
                result +=  - 2./3.*z*pow(pi,2)*CF + 43./18.*pow(z,2)*CF - 16*pow(z,2)*pow(rln2,2)*CF*pow(omx,-1)\
           + 2*pow(z,2)*pow(pi,2)*CF*pow(omx,-1) + 2./3.*pow(z,2)*pow(pi,2)*CF*pow(opx,-1) + 121./36.*x\
          *pow(z,-1)*CF + 1./6.*x*pow(z,-1)*pow(pi,2)*CF + 4*x*CF + 4*x*pow(rln2,2)*CF + 4*x*sqrtxz1*\
          rln2*CF - 5./6.*x*pow(pi,2)*CF - 119./12.*x*z*CF + 1./3.*x*z*pow(pi,2)*CF - 77./18.*x*pow(\
          z,2)*CF + 16*x*pow(z,2)*pow(rln2,2)*CF - 4./3.*x*pow(z,2)*pow(pi,2)*CF - 22./9.*pow(x,2)*pow(\
          z,-1)*CF + 44./9.*pow(x,2)*CF + 8*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(NC,-1)*pow(\
          z,2)*sqrtxz3*CF - 3*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 3*ArcTan(z*\
          sqrtxz3)*ln(z*sqrtxz3)*sqrtxz3*CF + 23*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(z,2)*sqrtxz3*CF - \
          3*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*x*z*sqrtxz3*CF - 8*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(NC,-1)*\
          pow(z,2)*sqrtxz3*CF + 3*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 3*ArcTan(sqrtxz3\
          )*ln(sqrtxz3)*sqrtxz3*CF - 23*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(z,2)*sqrtxz3*CF + 3*ArcTan(\
          sqrtxz3)*ln(sqrtxz3)*x*z*sqrtxz3*CF
                result +=  - 4*InvTanInt( - sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3*CF + 3./2.*InvTanInt( - sqrtxz3\
          )*pow(x,-1)*z*sqrtxz3*CF - 3./2.*InvTanInt( - sqrtxz3)*sqrtxz3*CF - 23./2.*InvTanInt( - \
          sqrtxz3)*pow(z,2)*sqrtxz3*CF + 3./2.*InvTanInt( - sqrtxz3)*x*z*sqrtxz3*CF - 8*InvTanInt(z*\
          sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3*CF + 3*InvTanInt(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 3*\
          InvTanInt(z*sqrtxz3)*sqrtxz3*CF - 23*InvTanInt(z*sqrtxz3)*pow(z,2)*sqrtxz3*CF + 3*InvTanInt(z\
          *sqrtxz3)*x*z*sqrtxz3*CF + 4*InvTanInt(sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3*CF - 3./2.*\
          InvTanInt(sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 3./2.*InvTanInt(sqrtxz3)*sqrtxz3*CF + 23./2.*\
          InvTanInt(sqrtxz3)*pow(z,2)*sqrtxz3*CF - 3./2.*InvTanInt(sqrtxz3)*x*z*sqrtxz3*CF - 8*ln(1 + \
          sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) + 8*ln(1 + sqrtxz1 - z)*\
          pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) - 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*\
          sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*\
          pow(omx,-1) - 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1)*pow(\
          opz,-1) + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1) + 16*ln(1\
           + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 32*ln(1 + sqrtxz1 - z\
          )*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1)
                result +=  + 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF + 16*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) - 32*ln(1 + sqrtxz1 - z)*pow(NC,-1)*\
          pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1) - 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*\
          CF*pow(opz,-1) + 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF - 6*ln(1 + sqrtxz1\
           - z)*pow(NC,-1)*rln2*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*sqrtxz1*CF*pow(\
          omx,-1) + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 16\
          *ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 16*ln(1 + sqrtxz1 - z)*\
          pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) - 16*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*z*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1) + 6*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*rln2*CF*\
          pow(omx,-1) + 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF*pow(opz,-1) - 8*ln(1 + \
          sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*\
          sqrtxz1*CF*pow(opz,-1) - 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 16*ln(1\
           + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF*pow(opz,-1) - 16*ln(1 + sqrtxz1 - z)*\
          pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF + 48*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*\
          CF*pow(opz,-1) - 32*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 48*ln(1 + sqrtxz1\
           - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1)
                result +=  - 32*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*CF + 8*ln(1 + sqrtxz1 - z)\
          *pow(NC,-1)*x*rln2*CF - 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1)\
           + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF - 16*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) + 16*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*rln2*CF - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*rln2*CF - 64*ln(1 + sqrtxz1 - z)*\
          pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(\
          x,2)*pow(sqrtxz1,-1)*CF - 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*CF*\
          pow(opz,-1) + 64*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*CF + 8*ln(1 + \
          sqrtxz1 - z)*rln2*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*rln2*CF + 6*ln(1 + sqrtxz1 - z)*\
          sqrtxz1*CF*pow(omx,-1) - 12*ln(1 + sqrtxz1 - z)*z*rln2*CF + 24*ln(1 + sqrtxz1 - z)*pow(z,2)*\
          rln2*CF*pow(omx,-1) - 6*ln(1 + sqrtxz1 - z)*x*rln2*CF - 4*ln(1 + sqrtxz1 - z)*x*sqrtxz1*CF + \
          4*ln(1 + sqrtxz1 - z)*x*z*rln2*CF - 24*ln(1 + sqrtxz1 - z)*x*pow(z,2)*rln2*CF + 4*pow(ln(1 + \
          sqrtxz1 - z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 4*pow(ln(1 + \
          sqrtxz1 - z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*pow(ln(1 + sqrtxz1 - z),2)*\
          pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 8*pow(ln(1 + sqrtxz1 - z),2)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)
                result +=  + 16*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*pow(\
          ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(\
          NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)\
          *z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(z,-1)*\
          sqrtxz1*CF*pow(opz,-1) + 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 12*\
          pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*pow(ln(1 + sqrtxz1\
           - z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF\
           + 16*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*pow(\
          ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - 2*pow(ln(1 + sqrtxz1 - z),2)*\
          CF*pow(omx,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*CF + 4*pow(ln(1 + sqrtxz1 - z),2)*z*CF*pow(\
          omx,-1) + 4*pow(ln(1 + sqrtxz1 - z),2)*z*CF - 8*pow(ln(1 + sqrtxz1 - z),2)*pow(z,2)*CF*pow(\
          omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*x*CF - 4*pow(ln(1 + sqrtxz1 - z),2)*x*z*CF + 8*pow(ln(\
          1 + sqrtxz1 - z),2)*x*pow(z,2)*CF + 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
          z,-1)*CF*pow(omx,-1)*pow(opz,-1) - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
          z,-1)*CF*pow(omx,-1)
                result +=  + 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(\
          omx,-1)*pow(opz,-1) - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*\
          CF*pow(omx,-1) - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(\
          omx,-1)*pow(opz,-1) + 16*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*\
          CF*pow(omx,-1) + 32*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*\
          pow(opz,-1) - 32*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF + 6*\
          ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*CF*pow(omx,-1) - 8*ln(1 + sqrtxz1 - z)*ln(\
          1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 8*ln(1 + sqrtxz1\
           - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 6*ln(1 + sqrtxz1 - z)\
          *ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*\
          pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) + 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
          x*pow(z,-1)*CF - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*\
          pow(opz,-1) + 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - \
          24*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*\
          ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF - 8*ln(1 + sqrtxz1 - \
          z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*CF
                result +=  + 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 8*ln(\
          1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*CF + 32*ln(1 + sqrtxz1 - z)*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 32*ln(1 + sqrtxz1 - z)*ln(1\
           + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1\
           + z)*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*CF - 8*ln(1 + sqrtxz1 - z)*\
          ln(1 + sqrtxz1 + z)*z*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*z*CF - 8*ln(\
          1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(z,2)*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + \
          sqrtxz1 + z)*x*CF + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*x*z*CF + 8*ln(1 + sqrtxz1 - z)*\
          ln(1 + sqrtxz1 + z)*x*pow(z,2)*CF - 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(\
          omx,-1)*pow(opz,-1) + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) - 8*ln(1\
           + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1)*pow(opz,-1) + 8*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1) + 8*ln(1 + sqrtxz1 + z)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) - 16*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
          pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1) - 32*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*\
          CF*pow(opz,-1)
                result +=  + 32*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF - 6*ln(1 + sqrtxz1 + z)*\
          pow(NC,-1)*rln2*CF*pow(omx,-1) + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*CF*\
          pow(omx,-1)*pow(opz,-1) - 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*CF*pow(\
          omx,-1) + 6*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) + 8*ln(1 + sqrtxz1 + z)*pow(\
          NC,-1)*x*pow(z,-1)*rln2*CF*pow(opz,-1) - 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF\
           + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF*pow(opz,-1) - 8*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF + 24*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*\
          pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 16*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*\
          rln2*CF + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*rln2*CF - 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*\
          pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*\
          rln2*CF - 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*rln2*CF - 32*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
          pow(x,2)*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) + 32*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*\
          pow(sqrtxz1,-1)*rln2*CF + 4*ln(1 + sqrtxz1 + z)*rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 + z)*\
          rln2*CF + 8*ln(1 + sqrtxz1 + z)*z*rln2*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 + z)*z*rln2*CF + 8*\
          ln(1 + sqrtxz1 + z)*pow(z,2)*rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 + z)*x*rln2*CF - 4*ln(1\
           + sqrtxz1 + z)*x*z*rln2*CF
                result +=  - 8*ln(1 + sqrtxz1 + z)*x*pow(z,2)*rln2*CF + pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*\
          pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),\
          2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 2*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*\
          pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 4*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*\
          pow(sqrtxz1,-1)*CF - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*\
          pow(omx,-1)*pow(opz,-1) + pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*\
          CF*pow(omx,-1) - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(\
          opz,-1) + pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 3*pow(ln(\
          1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 2*pow(ln(1 - 2*z\
           + pow(z,2) + 4*x*z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + pow(ln(1 - 2*z + pow(z,2) + 4*x*z),\
          2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(\
          NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 4*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*\
          pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*pow(ln(1 - 2*z + pow(z,2) + 4*x*z),2)*pow(NC,-1)*pow(x,2)*\
          pow(sqrtxz1,-1)*CF
                result +=  - 8*ln(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 8*ln(x)*pow(\
          NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) + 8*ln(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(\
          opx,-1) - 8*ln(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 8*ln(x)*pow(NC,-1)*pow(x,-2)*CF*pow(\
          opx,-1) - 8*ln(x)*pow(NC,-1)*pow(x,-2)*CF + 8*ln(x)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) - 8\
          *ln(x)*pow(NC,-1)*pow(x,-2)*z*CF - 8*ln(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(\
          opx,-1) + 8*ln(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) + 8*ln(x)*pow(NC,-1)*pow(\
          x,-1)*CF*pow(opx,-1) + 8*ln(x)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 3./2.*ln(x)*pow(NC,-1)\
          *pow(z,-1)*CF*pow(omx,-1) - 8*ln(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 8*ln(x)\
          *pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + ln(x)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(x)*pow(NC,-1)*\
          pow(z,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) - 4*ln(x)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1)\
           + 8*ln(x)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 8*ln(x)*pow(NC,-1)*pow(\
          z,-1)*sqrtxz1*CF*pow(omx,-1) - 8*ln(x)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1)\
           + 16*ln(x)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 32*ln(x)*pow(NC,-1)*pow(sqrtxz1,-1)*\
          CF*pow(opz,-1) - 32*ln(x)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 2*ln(x)*pow(NC,-1)*CF*pow(omx,-1)\
           + 8*ln(x)*pow(NC,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*ln(x)*pow(NC,-1)*CF + 3*ln(x)*pow(NC,-1)\
          *rln2*CF*pow(omx,-1)
                result +=  - ln(x)*pow(NC,-1)*sqrtxz1*CF*pow(omx,-1) - 8*ln(x)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*\
          pow(omx,-1)*pow(opz,-1) + 8*ln(x)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 1./2.*ln(x)*\
          pow(NC,-1)*z*CF*pow(omx,-1) + 4*ln(x)*pow(NC,-1)*z*CF - 3*ln(x)*pow(NC,-1)*z*rln2*CF*pow(\
          omx,-1) - 8*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) + 9*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF\
           - 4*ln(x)*pow(NC,-1)*x*pow(z,-1)*rln2*CF*pow(opz,-1) + 4*ln(x)*pow(NC,-1)*x*pow(z,-1)*rln2*\
          CF - 8*ln(x)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) + 8*ln(x)*pow(NC,-1)*x*pow(z,-1)*\
          sqrtxz1*CF - 24*ln(x)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*ln(x)*pow(NC,-1)*x*\
          pow(sqrtxz1,-1)*CF + 8*ln(x)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(x)*pow(NC,-1)*x*CF - 4*ln(x)*\
          pow(NC,-1)*x*rln2*CF + 8*ln(x)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*ln(x)*pow(\
          NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 4*ln(x)*pow(NC,-1)*x*z*CF + 4*ln(x)*pow(NC,-1)*x*z*rln2*CF + \
          32*ln(x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 32*ln(x)*pow(NC,-1)*pow(x,2)*\
          pow(sqrtxz1,-1)*CF - 4*ln(x)*pow(x,-2)*CF*pow(opx,-1) + 4*ln(x)*pow(x,-2)*CF + 8*ln(x)*pow(\
          x,-2)*z*CF*pow(opx,-1) - 8*ln(x)*pow(x,-2)*z*CF - 16*ln(x)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1)\
           + 16*ln(x)*pow(x,-2)*pow(z,2)*CF + 1./2.*ln(x)*pow(x,-1)*pow(poly2,-1)*CF - 9./2.*ln(x)*pow(\
          x,-1)*CF + 8*ln(x)*pow(x,-1)*z*CF - 16*ln(x)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - 4./3.*ln(x)*\
          pow(z,-1)*CF*pow(omx,-1)
                result +=  + 5./3.*ln(x)*pow(z,-1)*CF - 1./2.*ln(x)*pow(poly2,-1)*CF - 1./2.*ln(x)*CF*pow(\
          omx,-1) + 4*ln(x)*CF*pow(opx,-1) - 7./2.*ln(x)*CF - 5*ln(x)*rln2*CF*pow(omx,-1) - 2*ln(x)*\
          rln2*CF - 3*ln(x)*sqrtxz1*CF*pow(omx,-1) - 1./2.*ln(x)*z*CF*pow(omx,-1) - 8*ln(x)*z*CF*pow(\
          opx,-1) + 5./2.*ln(x)*z*CF + 2*ln(x)*z*rln2*CF*pow(omx,-1) + 8*ln(x)*z*rln2*CF + 4./3.*ln(x)*\
          pow(z,2)*CF*pow(omx,-1) + 4./3.*ln(x)*pow(z,2)*CF - 16*ln(x)*pow(z,2)*rln2*CF*pow(omx,-1) + \
          11./3.*ln(x)*x*pow(z,-1)*CF - ln(x)*x*CF*pow(xmz,-1) - 17./2.*ln(x)*x*CF + 4*ln(x)*x*rln2*CF\
           + 2*ln(x)*x*sqrtxz1*CF + 13./2.*ln(x)*x*z*CF - 4*ln(x)*x*z*rln2*CF - 8./3.*ln(x)*x*pow(z,2)*\
          CF + 16*ln(x)*x*pow(z,2)*rln2*CF + 2*ln(x)*pow(x,2)*pow(z,-1)*CF + 2*ln(x)*pow(x,2)*CF*pow(\
          xmz,-1) - 5./2.*ln(x)*pow(x,2)*CF - 1./2.*ln(x)*pow(x,3)*pow(poly2,-1)*CF - 2*ln(x)*pow(x,3)*\
          CF*pow(xmz,-1) + 1./2.*ln(x)*pow(x,4)*pow(poly2,-1)*CF + 1./4.*ln(x)*ln(1 - sqrtxz2 + x)*\
          pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,-1)*pow(\
          sqrtxz2,-1)*CF + 1./2.*ln(x)*ln(1 - sqrtxz2 + x)*pow(sqrtxz2,-1)*CF - ln(x)*ln(1 - sqrtxz2 + \
          x)*z*pow(sqrtxz2,-1)*CF - 1./4.*ln(x)*ln(1 - sqrtxz2 + x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF\
           + 3./2.*ln(x)*ln(1 - sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF + 4*ln(x)*ln(1 - sqrtxz2 + x)*x*z*\
          pow(sqrtxz2,-1)*CF
                result +=  - 4*ln(x)*ln(1 - sqrtxz2 + x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 1./2.*ln(x)*ln(1 - \
          sqrtxz2 + x)*pow(x,2)*pow(sqrtxz2,-1)*CF - ln(x)*ln(1 - sqrtxz2 + x)*pow(x,2)*z*pow(\
          sqrtxz2,-1)*CF - 1./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - \
          1./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*CF + 1./4.*ln(x)*ln(1 - sqrtxz2 + x)\
          *pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,-1)*pow(\
          sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,-1)*pow(sqrtxz2,-1)*CF\
           - 1./2.*ln(x)*ln(1 + sqrtxz2 + x)*pow(sqrtxz2,-1)*CF + ln(x)*ln(1 + sqrtxz2 + x)*z*pow(\
          sqrtxz2,-1)*CF + 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 3./2.*\
          ln(x)*ln(1 + sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF - 4*ln(x)*ln(1 + sqrtxz2 + x)*x*z*pow(\
          sqrtxz2,-1)*CF + 4*ln(x)*ln(1 + sqrtxz2 + x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 1./2.*ln(x)*ln(1\
           + sqrtxz2 + x)*pow(x,2)*pow(sqrtxz2,-1)*CF + ln(x)*ln(1 + sqrtxz2 + x)*pow(x,2)*z*pow(\
          sqrtxz2,-1)*CF + 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + \
          1./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*CF - 1./4.*ln(x)*ln(1 + sqrtxz2 + x)\
          *pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)\
          *sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*\
          sqrtxz1*CF*pow(omx,-1)
                result +=  - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1)\
           + 8*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 16*ln(x)*ln(1 + \
          sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(x)*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(\
          omx,-1)*pow(opz,-1) + 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)\
           - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) + 4*ln(x)*ln(1\
           + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 12*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x\
          *pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF\
           + 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*ln(x)*ln(1\
           + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 16*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*\
          pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*\
          pow(sqrtxz1,-1)*CF + 2*ln(x)*ln(1 + sqrtxz1 - z)*CF*pow(omx,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)\
          *CF - 4*ln(x)*ln(1 + sqrtxz1 - z)*z*CF*pow(omx,-1) - 4*ln(x)*ln(1 + sqrtxz1 - z)*z*CF + 8*ln(\
          x)*ln(1 + sqrtxz1 - z)*pow(z,2)*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 - z)*x*CF + 4*ln(x)*\
          ln(1 + sqrtxz1 - z)*x*z*CF - 8*ln(x)*ln(1 + sqrtxz1 - z)*x*pow(z,2)*CF - 4*ln(x)*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1)
                result +=  + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 4*ln(x)*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) + 4*ln(x)*ln(1 + sqrtxz1\
           + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
          pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 8*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF*pow(omx,-1) - 16*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) + 16*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 3*ln(x)*ln(1 + sqrtxz1\
           + z)*pow(NC,-1)*CF*pow(omx,-1) + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF\
          *pow(omx,-1)*pow(opz,-1) - 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(\
          omx,-1) + 3*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*CF*pow(omx,-1) + 4*ln(x)*ln(1 + sqrtxz1 + \
          z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) - 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)\
          *CF + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) - 4*ln(x)*ln(\
          1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 12*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*\
          x*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*\
          CF + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*CF - 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z\
          *pow(sqrtxz1,-1)*CF*pow(opz,-1) + 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*\
          CF
                result +=  - 4*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*CF - 16*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
          NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
          x,2)*pow(sqrtxz1,-1)*CF + 3*ln(x)*ln(1 + sqrtxz1 + z)*CF*pow(omx,-1) + 2*ln(x)*ln(1 + sqrtxz1\
           + z)*z*CF*pow(omx,-1) - 4*ln(x)*ln(1 + sqrtxz1 + z)*z*CF + 8*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
          z,2)*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*x*CF - 8*ln(x)*ln(1 + sqrtxz1 + z)*x*pow(\
          z,2)*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(\
          opx,-1) - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) - 2*ln(x)\
          *ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(\
          z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*\
          CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF - 2*ln(x)*ln(1 + x*pow(\
          z,-1))*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(\
          x,-2)*z*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(\
          opx,-1) - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) - 2*ln(x)\
          *ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(\
          NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(\
          omz,-1)*pow(opx,-1)
                result +=  - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*\
          pow(z,-1))*pow(NC,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*z*CF*pow(\
          opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 2*ln(x)*ln(1 + \
          x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*CF - 2*ln(x\
          )*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*z*CF + ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*CF*pow(opx,-1)\
           - ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*z*CF*pow(\
          opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*z*CF + 4*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*\
          pow(z,2)*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF + ln(x)*ln(1 + x*\
          pow(z,-1))*pow(x,-1)*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-1)*z*CF + 4*ln(x)*ln(1 + x*pow(\
          z,-1))*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + ln(x)*ln(1 + x*pow(z,-1))*CF*pow(opx,-1) - ln(x)*\
          ln(1 + x*pow(z,-1))*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(\
          z,-1))*z*CF + 4*ln(x)*ln(1 + x*pow(z,-1))*pow(z,2)*CF*pow(opx,-1) + ln(x)*ln(1 + x*pow(z,-1))\
          *x*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*x*z*CF + 4*ln(x)*ln(1 + x*pow(z,-1))*x*pow(z,2)*CF - 4*\
          ln(x)*ln(1 + x)*pow(NC,-1)*CF*pow(opx,-1) + 4*ln(x)*ln(1 + x)*pow(NC,-1)*CF - 4*ln(x)*ln(1 + \
          x)*pow(NC,-1)*z*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x)*pow(NC,-1)*x*z*CF + 4*ln(x)*ln(1 + x)*CF*\
          pow(opx,-1)
                result +=  + 2*ln(x)*ln(1 + x)*CF - 8*ln(x)*ln(1 + x)*z*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x)*z*CF\
           + 8*ln(x)*ln(1 + x)*pow(z,2)*CF*pow(opx,-1) + 6*ln(x)*ln(1 + x)*x*CF - 12*ln(x)*ln(1 + x)*x*\
          z*CF + 8*ln(x)*ln(1 + x)*x*pow(z,2)*CF + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*\
          CF*pow(omz,-1)*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(\
          omz,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(x)*ln(1 + \
          x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*CF*pow(\
          opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*CF - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(\
          x,-2)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z*CF + 2*ln(x)*ln(1 + x*z)*\
          pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*\
          pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1)\
           - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)\
          *pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(\
          omx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*ln(x)*ln(1\
           + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*CF*pow(omx,-1)\
           - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*z*CF*pow(\
          omx,-1)
                result +=  - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*x*\
          pow(z,-1)*CF*pow(omz,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) - 4*ln(x\
          )*ln(1 + x*z)*pow(NC,-1)*x*CF + ln(x)*ln(1 + x*z)*pow(x,-2)*CF*pow(opx,-1) - ln(x)*ln(1 + x*z\
          )*pow(x,-2)*CF - 2*ln(x)*ln(1 + x*z)*pow(x,-2)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(\
          x,-2)*z*CF + 4*ln(x)*ln(1 + x*z)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x*z)*pow(\
          x,-2)*pow(z,2)*CF + ln(x)*ln(1 + x*z)*pow(x,-1)*CF - 2*ln(x)*ln(1 + x*z)*pow(x,-1)*z*CF + 4*\
          ln(x)*ln(1 + x*z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*CF*pow(omx,-1) + \
          ln(x)*ln(1 + x*z)*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x*z)*z*CF*pow(omx,-1) - 2*ln(x)*ln(1 + x*z)\
          *z*CF*pow(opx,-1) + 4*ln(x)*ln(1 + x*z)*z*CF - 4*ln(x)*ln(1 + x*z)*pow(z,2)*CF*pow(omx,-1) + \
          4*ln(x)*ln(1 + x*z)*pow(z,2)*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*x*CF + 8*ln(x)*ln(1 + x*z)*\
          x*pow(z,2)*CF - 2*ln(x)*ln(z + x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1) + 2*ln(x)*\
          ln(z + x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*ln(x)*ln(z + x)*pow(NC,-1)*CF*pow(omx,-1)\
           + 2*ln(x)*ln(z + x)*pow(NC,-1)*z*CF*pow(omx,-1) + 2*ln(x)*ln(z + x)*pow(NC,-1)*x*pow(z,-1)*\
          CF*pow(opz,-1) - 2*ln(x)*ln(z + x)*pow(NC,-1)*x*pow(z,-1)*CF + 2*ln(x)*ln(z + x)*pow(NC,-1)*x\
          *CF - 2*ln(x)*ln(z + x)*pow(NC,-1)*x*z*CF + 2*ln(x)*ln(z + x)*CF*pow(omx,-1) - ln(x)*ln(z + x\
          )*CF
                result +=  + 4*ln(x)*ln(z + x)*z*CF*pow(omx,-1) - 2*ln(x)*ln(z + x)*z*CF + 4*ln(x)*ln(z + x)*\
          pow(z,2)*CF*pow(omx,-1) - ln(x)*ln(z + x)*x*CF - 2*ln(x)*ln(z + x)*x*z*CF - 4*ln(x)*ln(z + x)\
          *x*pow(z,2)*CF + 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 3\
          *pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) - 3*pow(ln(x),2)*pow(NC,-1)*pow(\
          x,-2)*pow(z,-1)*CF*pow(opx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 3*pow(ln(\
          x),2)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*CF - 3*pow(\
          ln(x),2)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*z*CF + 3\
          *pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 3*pow(ln(x),2)*pow(\
          NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) - 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*CF*pow(\
          opx,-1) - 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + pow(ln(x),2)*pow(NC,-1)*pow(\
          z,-1)*CF*pow(omx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 3*\
          pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 1./2.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF\
           - 3*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) + 3*pow(ln(x),2)*\
          pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*\
          pow(omx,-1)*pow(opz,-1) - 6*pow(ln(x),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 12*pow(\
          ln(x),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1)
                result +=  + 12*pow(ln(x),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 2*pow(ln(x),2)*pow(NC,-1)*CF*pow(\
          omx,-1) - 3*pow(ln(x),2)*pow(NC,-1)*CF*pow(omz,-1)*pow(opx,-1) + pow(ln(x),2)*pow(NC,-1)*CF*\
          pow(opx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 3*pow(\
          ln(x),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) + pow(ln(x),2)*pow(NC,-1)*z*CF*pow(\
          omx,-1) + pow(ln(x),2)*pow(NC,-1)*z*CF*pow(opx,-1) + 3*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF\
          *pow(omz,-1) - 7./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF + 3*pow(ln(x),2)*pow(NC,-1)*x*\
          pow(z,-1)*sqrtxz1*CF*pow(opz,-1) - 3*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 9*pow(\
          ln(x),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 6*pow(ln(x),2)*pow(NC,-1)*x*pow(\
          sqrtxz1,-1)*CF - 3*pow(ln(x),2)*pow(NC,-1)*x*CF*pow(omz,-1) + pow(ln(x),2)*pow(NC,-1)*x*CF - \
          3*pow(ln(x),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 3*pow(ln(x),2)*pow(NC,-1)*x*z*\
          pow(sqrtxz1,-1)*CF - 12*pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 12*\
          pow(ln(x),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + 3./2.*pow(ln(x),2)*pow(x,-2)*CF*pow(\
          opx,-1) - 3./2.*pow(ln(x),2)*pow(x,-2)*CF - 3*pow(ln(x),2)*pow(x,-2)*z*CF*pow(opx,-1) + 3*\
          pow(ln(x),2)*pow(x,-2)*z*CF + 6*pow(ln(x),2)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 6*pow(ln(x),\
          2)*pow(x,-2)*pow(z,2)*CF + 3./2.*pow(ln(x),2)*pow(x,-1)*CF - 3*pow(ln(x),2)*pow(x,-1)*z*CF + \
          6*pow(ln(x),2)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1)
                result +=  - pow(ln(x),2)*pow(z,-1)*CF + 2*pow(ln(x),2)*CF*pow(omx,-1) - 5./2.*pow(ln(x),2)*CF*\
          pow(opx,-1) - 4*pow(ln(x),2)*z*CF*pow(omx,-1) + 5*pow(ln(x),2)*z*CF*pow(opx,-1) + 4*pow(ln(x)\
          ,2)*z*CF + 2*pow(ln(x),2)*pow(z,2)*CF*pow(omx,-1) - 2*pow(ln(x),2)*pow(z,2)*CF*pow(opx,-1) - \
          pow(ln(x),2)*x*pow(z,-1)*CF - pow(ln(x),2)*x*CF + 6*pow(ln(x),2)*x*z*CF - 4*pow(ln(x),2)*x*\
          pow(z,2)*CF - 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 2*ln(\
          x)*ln(z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*\
          pow(z,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 2*ln(x)*ln(z)*\
          pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*CF + 2*ln(x)*ln(z)*\
          pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*z*CF - 2*ln(x)*ln(\
          z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*pow(\
          x,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) + 2*ln(x)*\
          ln(z)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(\
          omx,-1)*pow(opz,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*ln(x)*ln(z)*pow(\
          NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(\
          opx,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) + 2*ln(x)*ln(\
          z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)
                result +=  + 2*ln(x)*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 4*ln(x)*ln(z)\
          *pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 8*ln(x)*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) + 8*ln(x)*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF + 2*ln(x)*ln(z)*pow(NC,-1)*CF*pow(\
          omx,-1) + ln(x)*ln(z)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*CF*pow(opx,-1) - 2\
          *ln(x)*ln(z)*pow(NC,-1)*CF + 2*ln(x)*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(\
          opz,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 2*ln(x)*ln(z)*pow(\
          NC,-1)*z*CF*pow(omx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(opx,-1) - 2*ln(x)*ln(z)*pow(\
          NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) + 4*\
          ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 2*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(\
          opz,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 6*ln(x)*ln(z)*pow(NC,-1)*x*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) - 4*ln(x)*ln(z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + ln(x)*ln(z)*pow(\
          NC,-1)*x*CF*pow(omz,-1) - 2*ln(x)*ln(z)*pow(NC,-1)*x*CF - 2*ln(x)*ln(z)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 4*ln(x)*ln(z)*\
          pow(NC,-1)*x*z*CF - 8*ln(x)*ln(z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*ln(x\
          )*ln(z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - ln(x)*ln(z)*pow(x,-2)*CF*pow(opx,-1) + ln(x)\
          *ln(z)*pow(x,-2)*CF
                result +=  + 2*ln(x)*ln(z)*pow(x,-2)*z*CF*pow(opx,-1) - 2*ln(x)*ln(z)*pow(x,-2)*z*CF - 4*ln(x)*\
          ln(z)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) + 4*ln(x)*ln(z)*pow(x,-2)*pow(z,2)*CF - ln(x)*ln(z)*\
          pow(x,-1)*CF + 2*ln(x)*ln(z)*pow(x,-1)*z*CF - 4*ln(x)*ln(z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1)\
           + ln(x)*ln(z)*pow(z,-1)*CF - 7*ln(x)*ln(z)*CF*pow(omx,-1) - ln(x)*ln(z)*CF*pow(opx,-1) + ln(\
          x)*ln(z)*z*CF*pow(omx,-1) + 2*ln(x)*ln(z)*z*CF*pow(opx,-1) + 2*ln(x)*ln(z)*z*CF - 8*ln(x)*ln(\
          z)*pow(z,2)*CF*pow(omx,-1) - 4*ln(x)*ln(z)*pow(z,2)*CF*pow(opx,-1) + ln(x)*ln(z)*x*pow(z,-1)*\
          CF + 2*ln(x)*ln(z)*x*CF + 2*ln(x)*ln(z)*x*z*CF + 4*ln(x)*ln(z)*x*pow(z,2)*CF + 4*ln(x)*ln(omx\
          )*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 4*ln(x)*ln(omx)*pow(NC,-1)*pow(\
          x,-2)*pow(z,-1)*CF*pow(omz,-1) - 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(\
          opx,-1) + 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 4*ln(x)*ln(omx)*pow(NC,-1)*pow(\
          x,-2)*CF*pow(opx,-1) + 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*CF - 4*ln(x)*ln(omx)*pow(NC,-1)*\
          pow(x,-2)*z*CF*pow(opx,-1) + 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*z*CF + 4*ln(x)*ln(omx)*pow(\
          NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*\
          pow(z,-1)*CF*pow(opx,-1) - 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) - 4*ln(x)*ln(\
          omx)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(\
          omx,-1)
                result +=  + 4*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 4*ln(x)*ln(omx)*\
          pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(x)*ln(omx)\
          *pow(NC,-1)*CF*pow(omx,-1) - 4*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*ln(x)*\
          ln(omx)*pow(NC,-1)*CF - 2*ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 4*ln(x)*ln(omx)*pow(\
          NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 3*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 4*ln(x)*ln(\
          omx)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(x)*ln(omx)*pow(NC,-1)*x*CF + 2*ln(x)*ln(omx)*pow(\
          NC,-1)*x*z*CF + 2*ln(x)*ln(omx)*pow(x,-2)*CF*pow(opx,-1) - 2*ln(x)*ln(omx)*pow(x,-2)*CF - 4*\
          ln(x)*ln(omx)*pow(x,-2)*z*CF*pow(opx,-1) + 4*ln(x)*ln(omx)*pow(x,-2)*z*CF + 8*ln(x)*ln(omx)*\
          pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 8*ln(x)*ln(omx)*pow(x,-2)*pow(z,2)*CF + 2*ln(x)*ln(omx)*\
          pow(x,-1)*CF - 4*ln(x)*ln(omx)*pow(x,-1)*z*CF + 8*ln(x)*ln(omx)*pow(x,-1)*pow(z,2)*CF*pow(\
          opx,-1) - 3*ln(x)*ln(omx)*CF*pow(omx,-1) - 2*ln(x)*ln(omx)*CF*pow(opx,-1) + 6*ln(x)*ln(omx)*z\
          *CF*pow(omx,-1) + 4*ln(x)*ln(omx)*z*CF*pow(opx,-1) - 8*ln(x)*ln(omx)*pow(z,2)*CF*pow(omx,-1)\
           + 2*ln(x)*ln(omx)*x*CF - 4*ln(x)*ln(omx)*x*z*CF + 8*ln(x)*ln(omx)*x*pow(z,2)*CF + 4*ln(x)*\
          ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 4*ln(x)*ln(omz)*pow(NC,-1)*\
          pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*ln(x)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*\
          pow(opz,-1)
                result +=  + 8*ln(x)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 16*ln(x)*ln(omz)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(x)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 4*\
          ln(x)*ln(omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4*ln(x)*ln(omz)*pow(\
          NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 4*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*\
          pow(opz,-1) + 4*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 12*ln(x)*ln(omz)*pow(NC,-1)\
          *x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*ln(x)*ln(omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 4*ln(x)\
          *ln(omz)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*ln(x)*ln(omz)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*CF + 16*ln(x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(\
          x)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + ln(x)*ln(omz)*pow(z,-1)*CF - 2*ln(x)*ln(\
          omz)*CF + ln(x)*ln(omz)*x*pow(z,-1)*CF - 2*ln(x)*ln(omz)*x*CF - 4*ln(x)*ln(opx)*pow(NC,-1)*\
          pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(\
          z,-1)*CF*pow(omz,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) - 4*ln(x\
          )*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*CF*pow(\
          opx,-1) - 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*CF + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*z*CF\
          *pow(opx,-1) - 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*z*CF - 4*ln(x)*ln(opx)*pow(NC,-1)*pow(\
          x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1)
                result +=  + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) + 4*ln(x)*ln(opx)*\
          pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1)\
           - 4*ln(x)*ln(opx)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(\
          NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*CF*pow(opx,-1) + 4*ln(x)*ln(opx)\
          *pow(NC,-1)*z*CF*pow(opx,-1) - 4*ln(x)*ln(opx)*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) + 4*ln(x\
          )*ln(opx)*pow(NC,-1)*x*pow(z,-1)*CF + 4*ln(x)*ln(opx)*pow(NC,-1)*x*CF + 4*ln(x)*ln(opx)*pow(\
          NC,-1)*x*z*CF - 2*ln(x)*ln(opx)*pow(x,-2)*CF*pow(opx,-1) + 2*ln(x)*ln(opx)*pow(x,-2)*CF + 4*\
          ln(x)*ln(opx)*pow(x,-2)*z*CF*pow(opx,-1) - 4*ln(x)*ln(opx)*pow(x,-2)*z*CF - 8*ln(x)*ln(opx)*\
          pow(x,-2)*pow(z,2)*CF*pow(opx,-1) + 8*ln(x)*ln(opx)*pow(x,-2)*pow(z,2)*CF - 2*ln(x)*ln(opx)*\
          pow(x,-1)*CF + 4*ln(x)*ln(opx)*pow(x,-1)*z*CF - 8*ln(x)*ln(opx)*pow(x,-1)*pow(z,2)*CF*pow(\
          opx,-1) - 2*ln(x)*ln(opx)*CF*pow(opx,-1) + 2*ln(x)*ln(opx)*CF + 4*ln(x)*ln(opx)*z*CF*pow(\
          opx,-1) - 4*ln(x)*ln(opx)*z*CF - 8*ln(x)*ln(opx)*pow(z,2)*CF*pow(opx,-1) - 2*ln(x)*ln(opx)*x*\
          CF + 4*ln(x)*ln(opx)*x*z*CF - 8*ln(x)*ln(opx)*x*pow(z,2)*CF + 12*ln(z)*pow(NC,-1)*pow(z,-1)*\
          rln2*CF*pow(omx,-1)*pow(opz,-1) - 12*ln(z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) + 8*ln(z)\
          *pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 8*ln(z)*pow(NC,-1)*pow(z,-1)*\
          sqrtxz1*CF*pow(omx,-1)
                result +=  + 16*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1)*pow(opz,-1) - 16*ln(z)*\
          pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1) - 8*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(\
          omx,-1)*pow(opz,-1) + 16*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 32*ln(z)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 32*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 16*ln(z)*\
          pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) + 32*ln(z)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*rln2*CF*pow(omx,-1) + 64*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - \
          64*ln(z)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF + ln(z)*pow(NC,-1)*CF*pow(omx,-1) - ln(z)*pow(\
          NC,-1)*CF*pow(omz,-1) - ln(z)*pow(NC,-1)*CF + 9*ln(z)*pow(NC,-1)*rln2*CF*pow(omx,-1) - ln(z)*\
          pow(NC,-1)*sqrtxz1*CF*pow(omx,-1) - 8*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(\
          opz,-1) + 8*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 16*ln(z)*pow(NC,-1)*z*pow(\
          sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) + 16*ln(z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*CF*\
          pow(omx,-1) + ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 2*ln(z)*pow(NC,-1)*z*CF - 9*ln(z)*pow(\
          NC,-1)*z*rln2*CF*pow(omx,-1) - 12*ln(z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF*pow(opz,-1) + 12*ln(z)\
          *pow(NC,-1)*x*pow(z,-1)*rln2*CF - 8*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) + 8*\
          ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 16*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF*\
          pow(opz,-1)
                result +=  + 16*ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF - 24*ln(z)*pow(NC,-1)*x*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) + 16*ln(z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF - 48*ln(z)*pow(NC,-1)*x\
          *pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) + 32*ln(z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*CF + ln(z)*\
          pow(NC,-1)*x*CF*pow(omz,-1) + ln(z)*pow(NC,-1)*x*CF - 12*ln(z)*pow(NC,-1)*x*rln2*CF + 8*ln(z)\
          *pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*ln(z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + \
          16*ln(z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 16*ln(z)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*rln2*CF - 2*ln(z)*pow(NC,-1)*x*z*CF + 12*ln(z)*pow(NC,-1)*x*z*rln2*CF + 32*ln(z)*\
          pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 32*ln(z)*pow(NC,-1)*pow(x,2)*pow(\
          sqrtxz1,-1)*CF + 64*ln(z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 64*ln(z)*\
          pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*CF + 2./3.*ln(z)*pow(x,-1)*pow(z,-1)*CF + 1./2.*ln(z\
          )*pow(x,-1)*pow(poly2,-1)*CF + 2./3.*ln(z)*pow(x,-1)*CF*pow(omz,-1) - 11./6.*ln(z)*pow(x,-1)*\
          CF + 1./6.*ln(z)*pow(z,-1)*CF + 1./2.*ln(z)*pow(poly2,-1)*CF + 3*ln(z)*CF*pow(omx,-1) - ln(z)\
          *CF*pow(omz,-1) - 7*ln(z)*CF - 7*ln(z)*rln2*CF*pow(omx,-1) + 2*ln(z)*rln2*CF - 3*ln(z)*\
          sqrtxz1*CF*pow(omx,-1) + 3*ln(z)*z*CF*pow(omx,-1) + 5*ln(z)*z*CF - 10*ln(z)*z*rln2*CF*pow(\
          omx,-1) + 8*ln(z)*z*rln2*CF - 2./3.*ln(z)*pow(z,2)*CF - 16*ln(z)*pow(z,2)*rln2*CF*pow(omx,-1)\
           - 5./6.*ln(z)*x*pow(z,-1)*CF
                result +=  + ln(z)*x*CF*pow(omz,-1) + ln(z)*x*CF*pow(xmz,-1) + ln(z)*x*CF + 4*ln(z)*x*rln2*CF + \
          2*ln(z)*x*sqrtxz1*CF - 4*ln(z)*x*z*CF + 4*ln(z)*x*z*rln2*CF + 4./3.*ln(z)*x*pow(z,2)*CF + 16*\
          ln(z)*x*pow(z,2)*rln2*CF - 2./3.*ln(z)*pow(x,2)*pow(z,-1)*CF - 2./3.*ln(z)*pow(x,2)*CF*pow(\
          omz,-1) - 2*ln(z)*pow(x,2)*CF*pow(xmz,-1) - 1./6.*ln(z)*pow(x,2)*CF - 1./2.*ln(z)*pow(x,3)*\
          pow(poly2,-1)*CF + 2*ln(z)*pow(x,3)*CF*pow(xmz,-1) - 1./2.*ln(z)*pow(x,4)*pow(poly2,-1)*CF - 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(\
          z,-1)*CF*pow(omx,-1) - 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(\
          omx,-1)*pow(opz,-1) + 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)\
           + 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 16*ln(\
          z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 32*ln(z)*ln(1 + sqrtxz1 - \
          z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 32*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF - 3*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(z)*ln(1 + \
          sqrtxz1 - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 8*ln(z)*ln(1 + sqrtxz1\
           - z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 3*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*\
          CF*pow(omx,-1)
                result +=  + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) - 4*ln(z)*ln(1 + \
          sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*CF + 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*\
          sqrtxz1*CF*pow(opz,-1) - 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 24*\
          ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(z)*ln(1 + \
          sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*CF - \
          8*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*ln(z)*ln(1 + \
          sqrtxz1 - z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF - 4*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*\
          CF - 32*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 32*ln(\
          z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + 3*ln(z)*ln(1 + sqrtxz1 - z)*\
          CF*pow(omx,-1) + 2*ln(z)*ln(1 + sqrtxz1 - z)*z*CF*pow(omx,-1) - 4*ln(z)*ln(1 + sqrtxz1 - z)*z\
          *CF + 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(z,2)*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 - z)*x*CF\
           - 8*ln(z)*ln(1 + sqrtxz1 - z)*x*pow(z,2)*CF - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
          z,-1)*CF*pow(omx,-1)*pow(opz,-1) + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF*pow(\
          omx,-1) - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1)\
           + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 8*ln(z)*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1)
                result +=  - 16*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 32*ln(z)*\
          ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 32*ln(z)*ln(1 + sqrtxz1 + z)*\
          pow(NC,-1)*pow(sqrtxz1,-1)*CF - 6*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(\
          z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 8*ln(z)*ln(1\
           + sqrtxz1 + z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 6*ln(z)*ln(1 + sqrtxz1 + z)*\
          pow(NC,-1)*z*CF*pow(omx,-1) + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(\
          opz,-1) - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*CF + 8*ln(z)*ln(1 + sqrtxz1 + z)\
          *pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*\
          pow(z,-1)*sqrtxz1*CF + 24*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) - 16*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 8*ln(z)*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*x*CF - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*\
          pow(opz,-1) + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF - 8*ln(z)*ln(1 + \
          sqrtxz1 + z)*pow(NC,-1)*x*z*CF - 32*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) + 32*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)\
          *CF + 4*ln(z)*ln(1 + sqrtxz1 + z)*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*CF + 8*ln(z)*\
          ln(1 + sqrtxz1 + z)*z*CF*pow(omx,-1)
                result +=  - 4*ln(z)*ln(1 + sqrtxz1 + z)*z*CF + 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(z,2)*CF*pow(\
          omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*x*CF - 4*ln(z)*ln(1 + sqrtxz1 + z)*x*z*CF - 8*ln(z)*ln(\
          1 + sqrtxz1 + z)*x*pow(z,2)*CF - 4*ln(z)*ln(1 + z)*pow(NC,-1)*CF*pow(omx,-1)*pow(opz,-1) + 2*\
          ln(z)*ln(1 + z)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(1 + z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2\
          *ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 2*ln(z\
          )*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) + 2*ln(z)*ln(1 + x*pow(\
          z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)\
          *pow(x,-2)*pow(z,-1)*CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 2\
          *ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*\
          pow(x,-2)*z*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z*CF - 2*ln(z)*\
          ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 2*ln(z)*ln(1\
           + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*pow(z,-1))*\
          pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*z*CF*\
          pow(opx,-1) - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 2\
          *ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*pow(z,-1))*\
          pow(NC,-1)*CF*pow(opx,-1)
                result +=  + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*z*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*pow(\
          z,-1))*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(\
          z,-1)*CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(\
          NC,-1)*x*z*CF - ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*CF*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1)\
          )*pow(x,-2)*CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*z*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*\
          pow(z,-1))*pow(x,-2)*z*CF - 4*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) + 4\
          *ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF - ln(z)*ln(1 + x*pow(z,-1))*pow(x,-1)*CF + 2\
          *ln(z)*ln(1 + x*pow(z,-1))*pow(x,-1)*z*CF - 4*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-1)*pow(z,2)*CF\
          *pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*CF*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*CF + 2*\
          ln(z)*ln(1 + x*pow(z,-1))*z*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*pow(z,-1))*z*CF - 4*ln(z)*ln(1\
           + x*pow(z,-1))*pow(z,2)*CF*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*x*CF + 2*ln(z)*ln(1 + x*\
          pow(z,-1))*x*z*CF - 4*ln(z)*ln(1 + x*pow(z,-1))*x*pow(z,2)*CF + 2*ln(z)*ln(1 + x*z)*pow(\
          NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(\
          x,-2)*pow(z,-1)*CF*pow(omz,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(\
          opx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 2*ln(z)*ln(1 + x*z)*pow(\
          NC,-1)*pow(x,-2)*CF*pow(opx,-1)
                result +=  + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*CF - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(\
          x,-2)*z*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z*CF + 2*ln(z)*ln(1 + x*z)*\
          pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*\
          pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1)\
           - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)\
          *pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(\
          omx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*ln(z)*ln(1\
           + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*CF*pow(omx,-1)\
           - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*z*CF*pow(\
          omx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*z*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*x*\
          pow(z,-1)*CF*pow(omz,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) - 4*ln(z\
          )*ln(1 + x*z)*pow(NC,-1)*x*CF + ln(z)*ln(1 + x*z)*pow(x,-2)*CF*pow(opx,-1) - ln(z)*ln(1 + x*z\
          )*pow(x,-2)*CF - 2*ln(z)*ln(1 + x*z)*pow(x,-2)*z*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*z)*pow(\
          x,-2)*z*CF + 4*ln(z)*ln(1 + x*z)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 4*ln(z)*ln(1 + x*z)*pow(\
          x,-2)*pow(z,2)*CF + ln(z)*ln(1 + x*z)*pow(x,-1)*CF - 2*ln(z)*ln(1 + x*z)*pow(x,-1)*z*CF + 4*\
          ln(z)*ln(1 + x*z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1)
                result +=  - 2*ln(z)*ln(1 + x*z)*CF*pow(omx,-1) + ln(z)*ln(1 + x*z)*CF*pow(opx,-1) - 4*ln(z)*ln(\
          1 + x*z)*z*CF*pow(omx,-1) - 2*ln(z)*ln(1 + x*z)*z*CF*pow(opx,-1) + 4*ln(z)*ln(1 + x*z)*z*CF\
           - 4*ln(z)*ln(1 + x*z)*pow(z,2)*CF*pow(omx,-1) + 4*ln(z)*ln(1 + x*z)*pow(z,2)*CF*pow(opx,-1)\
           + 2*ln(z)*ln(1 + x*z)*x*CF + 8*ln(z)*ln(1 + x*z)*x*pow(z,2)*CF + 2*ln(z)*ln(z + x)*pow(\
          NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1) - 2*ln(z)*ln(z + x)*pow(NC,-1)*pow(z,-1)*CF*pow(\
          omx,-1) + 2*ln(z)*ln(z + x)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(z + x)*pow(NC,-1)*z*CF*\
          pow(omx,-1) - 2*ln(z)*ln(z + x)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) + 2*ln(z)*ln(z + x)*\
          pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(z)*ln(z + x)*pow(NC,-1)*x*CF + 2*ln(z)*ln(z + x)*pow(NC,-1)*\
          x*z*CF - 2*ln(z)*ln(z + x)*CF*pow(omx,-1) + ln(z)*ln(z + x)*CF - 4*ln(z)*ln(z + x)*z*CF*pow(\
          omx,-1) + 2*ln(z)*ln(z + x)*z*CF - 4*ln(z)*ln(z + x)*pow(z,2)*CF*pow(omx,-1) + ln(z)*ln(z + x\
          )*x*CF + 2*ln(z)*ln(z + x)*x*z*CF + 4*ln(z)*ln(z + x)*x*pow(z,2)*CF - pow(ln(z),2)*pow(NC,-1)\
          *pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)\
          *CF*pow(omz,-1) + pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) - pow(ln(z),2)*\
          pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) - pow(\
          ln(z),2)*pow(NC,-1)*pow(x,-2)*CF + pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) - pow(\
          ln(z),2)*pow(NC,-1)*pow(x,-2)*z*CF
                result +=  - pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + pow(ln(z),\
          2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*CF*pow(\
          opx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 2*pow(ln(z),2)*pow(NC,-1)*pow(\
          z,-1)*CF*pow(omx,-1)*pow(opz,-1) - 2*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - pow(\
          ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*\
          CF*pow(opx,-1) + 5*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 5*\
          pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 5*pow(ln(z),2)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 10*pow(ln(z),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(\
          omx,-1) + 20*pow(ln(z),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 20*pow(ln(z),2)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF + pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(opz,-1) + 1./2.*pow(\
          ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) + pow(ln(z),2)*pow(NC,-1)*CF*pow(opx,-1) - 5*pow(ln(z),2)*\
          pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 5*pow(ln(z),2)*pow(NC,-1)*z*pow(\
          sqrtxz1,-1)*CF*pow(omx,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) + pow(ln(z),2)*\
          pow(NC,-1)*z*CF*pow(opx,-1) - pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 2*pow(ln(z\
          ),2)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) + 3*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF - 5*\
          pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1)
                result +=  + 5*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 15*pow(ln(z),2)*pow(NC,-1)*x*\
          pow(sqrtxz1,-1)*CF*pow(opz,-1) + 10*pow(ln(z),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF - pow(ln(z),\
          2)*pow(NC,-1)*x*CF + 5*pow(ln(z),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 5*pow(ln(\
          z),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 3*pow(ln(z),2)*pow(NC,-1)*x*z*CF + 20*pow(ln(z),2)*\
          pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 20*pow(ln(z),2)*pow(NC,-1)*pow(x,2)*pow(\
          sqrtxz1,-1)*CF - 1./2.*pow(ln(z),2)*pow(x,-2)*CF*pow(opx,-1) + 1./2.*pow(ln(z),2)*pow(x,-2)*\
          CF + pow(ln(z),2)*pow(x,-2)*z*CF*pow(opx,-1) - pow(ln(z),2)*pow(x,-2)*z*CF - 2*pow(ln(z),2)*\
          pow(x,-2)*pow(z,2)*CF*pow(opx,-1) + 2*pow(ln(z),2)*pow(x,-2)*pow(z,2)*CF - 1./2.*pow(ln(z),2)\
          *pow(x,-1)*CF + pow(ln(z),2)*pow(x,-1)*z*CF - 2*pow(ln(z),2)*pow(x,-1)*pow(z,2)*CF*pow(\
          opx,-1) + pow(ln(z),2)*CF*pow(omx,-1) - 1./2.*pow(ln(z),2)*CF*pow(opx,-1) - 2*pow(ln(z),2)*z*\
          CF*pow(omx,-1) + pow(ln(z),2)*z*CF*pow(opx,-1) - 2*pow(ln(z),2)*z*CF + 2*pow(ln(z),2)*pow(\
          z,2)*CF*pow(omx,-1) - 2*pow(ln(z),2)*pow(z,2)*CF*pow(opx,-1) - 3*pow(ln(z),2)*x*CF + 2*pow(\
          ln(z),2)*x*z*CF - 4*pow(ln(z),2)*x*pow(z,2)*CF - ln(z)*ln(omx)*CF - ln(z)*ln(omx)*x*CF - 2*\
          ln(z)*ln(omx)*x*z*CF + 4*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(\
          opz,-1) - 4*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*ln(z)*ln(omz)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1)
                result +=  + 8*ln(z)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 16*ln(z)*ln(omz)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(z)*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 4*\
          ln(z)*ln(omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4*ln(z)*ln(omz)*pow(\
          NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 4*ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*\
          pow(opz,-1) + 4*ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 12*ln(z)*ln(omz)*pow(NC,-1)\
          *x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*ln(z)*ln(omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 4*ln(z)\
          *ln(omz)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*ln(z)*ln(omz)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*CF + 16*ln(z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(\
          z)*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - ln(z)*ln(omz)*CF*pow(omx,-1) + 2*ln(z)*\
          ln(omz)*z*CF*pow(omx,-1) + 2*ln(z)*ln(omz)*x*CF - 4*ln(z)*ln(omz)*x*z*CF + 2./3.*ln(omx)*pow(\
          x,-1)*pow(z,-1)*CF - 4./3.*ln(omx)*pow(x,-1)*CF + 1./6.*ln(omx)*pow(z,-1)*CF - 3./2.*ln(omx)*\
          CF + 3./2.*ln(omx)*z*CF - 2./3.*ln(omx)*pow(z,2)*CF - 5./6.*ln(omx)*x*pow(z,-1)*CF - 1./2.*\
          ln(omx)*x*CF + 1./2.*ln(omx)*x*z*CF + 4./3.*ln(omx)*x*pow(z,2)*CF - 2./3.*ln(omx)*pow(x,2)*\
          pow(z,-1)*CF + 4./3.*ln(omx)*pow(x,2)*CF + 8*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*\
          pow(omx,-1)*pow(opz,-1) - 8*ln(omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1) - 8*ln(\
          omz)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1)
                result +=  + 16*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1) + 32*ln(omz)*pow(NC,-1)*\
          pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 32*ln(omz)*pow(NC,-1)*pow(sqrtxz1,-1)*rln2*CF - 8*ln(\
          omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1)*pow(opz,-1) + 8*ln(omz)*pow(NC,-1)*z*\
          pow(sqrtxz1,-1)*rln2*CF*pow(omx,-1) - 8*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF*pow(\
          opz,-1) + 8*ln(omz)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF - 24*ln(omz)*pow(NC,-1)*x*pow(\
          sqrtxz1,-1)*rln2*CF*pow(opz,-1) + 16*ln(omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*rln2*CF + 8*ln(omz)\
          *pow(NC,-1)*x*z*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 8*ln(omz)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*rln2*CF + 32*ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*CF*pow(opz,-1) - 32\
          *ln(omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*rln2*CF + 2./3.*ln(omz)*pow(x,-1)*pow(z,-1)*CF\
           - 4./3.*ln(omz)*pow(x,-1)*CF + 1./6.*ln(omz)*pow(z,-1)*CF - 3./2.*ln(omz)*CF + 3./2.*ln(omz)\
          *z*CF - 2./3.*ln(omz)*pow(z,2)*CF - 5./6.*ln(omz)*x*pow(z,-1)*CF - 1./2.*ln(omz)*x*CF + 1./2.\
          *ln(omz)*x*z*CF + 4./3.*ln(omz)*x*pow(z,2)*CF - 2./3.*ln(omz)*pow(x,2)*pow(z,-1)*CF + 4./3.*\
          ln(omz)*pow(x,2)*CF - 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(\
          omx,-1)*pow(opz,-1) + 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(\
          omx,-1) + 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1)\
           - 16*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)
                result +=  - 32*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 32*ln(\
          omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF + 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(\
          z,-1)*sqrtxz1*CF*pow(opz,-1) - 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*\
          CF + 24*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*ln(omz)*\
          ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF - 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(\
          NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*CF - 32*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) + 32*ln(omz)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - 4*ln(omz)*\
          ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) + 4*\
          ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 4*ln(omz\
          )*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 8*\
          ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 16*ln(omz)\
          *ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*ln(omz)*ln(1\
           - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF
                result +=  + 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(\
          omx,-1)*pow(opz,-1) - 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*\
          CF*pow(omx,-1) + 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*\
          pow(opz,-1) - 4*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 12\
          *ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*ln(\
          omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF - 4*ln(omz)*ln(1 - 2*z + \
          pow(z,2) + 4*x*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 4*ln(omz)*ln(1 - 2*z + pow(\
          z,2) + 4*x*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF - 16*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z)*\
          pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*ln(omz)*ln(1 - 2*z + pow(z,2) + 4*x*z\
          )*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + 4*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*\
          pow(omx,-1)*pow(opz,-1) - 4*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*\
          pow(ln(omz),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 8*pow(ln(omz),2)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 16*pow(ln(omz),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) - 16*pow(ln(omz),2)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 4*pow(ln(omz),2)*pow(NC,-1)*z*\
          pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4*pow(ln(omz),2)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF\
          *pow(omx,-1)
                result +=  - 4*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) + 4*pow(ln(omz),2)*\
          pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 12*pow(ln(omz),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) + 8*pow(ln(omz),2)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 4*pow(ln(omz),2)*pow(NC,-1)*x*z*\
          pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*pow(ln(omz),2)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 16*pow(\
          ln(omz),2)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*pow(ln(omz),2)*pow(NC,-1)*\
          pow(x,2)*pow(sqrtxz1,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*\
          pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(\
          x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*CF + 1./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(\
          x,-1)*sqrtxz2)*pow(sqrtxz2,-1)*CF - Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*z*\
          pow(sqrtxz2,-1)*CF - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(\
          sqrtxz2,-1)*pow(poly2,-1)*CF + 3./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x\
          *pow(sqrtxz2,-1)*CF + 4*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*z*pow(\
          sqrtxz2,-1)*CF - 4*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(z,2)*pow(\
          sqrtxz2,-1)*CF + 1./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*pow(\
          sqrtxz2,-1)*CF - Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*z*pow(\
          sqrtxz2,-1)*CF
                result +=  - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(\
          sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*\
          pow(x,3)*pow(sqrtxz2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*\
          pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
          x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1)\
           + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*CF - 1./2.*Li2(1./2. - 1./2.*pow(x,-1)\
           + 1./2.*pow(x,-1)*sqrtxz2)*pow(sqrtxz2,-1)*CF + Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
          x,-1)*sqrtxz2)*z*pow(sqrtxz2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
          sqrtxz2)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 3./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
          x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*CF - 4*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2\
          )*x*z*pow(sqrtxz2,-1)*CF + 4*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*pow(\
          z,2)*pow(sqrtxz2,-1)*CF - 1./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(\
          x,2)*pow(sqrtxz2,-1)*CF + Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*z*\
          pow(sqrtxz2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*\
          pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
          sqrtxz2)*pow(x,3)*pow(sqrtxz2,-1)*CF
                result +=  - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,5)*pow(\
          sqrtxz2,-1)*pow(poly2,-1)*CF + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)\
          *sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(\
          z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 4*Li2(1./2. - 1./2.*\
          pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*Li2(1./2.\
           - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(\
          opz,-1) + 8*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)\
          *CF*pow(omx,-1) + 16*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) - 16*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF + 3*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*CF*pow(omx,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z\
          *pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)\
          *sqrtxz1)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 3*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.\
          *pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*CF*pow(omx,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(\
          z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1)
                result +=  + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*CF\
           - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF\
          *pow(opz,-1) + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(\
          z,-1)*sqrtxz1*CF - 12*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*\
          pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
          pow(NC,-1)*x*pow(sqrtxz1,-1)*CF - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
          pow(NC,-1)*x*CF + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*z*\
          pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
          pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
          pow(NC,-1)*x*z*CF + 16*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(\
          x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
          sqrtxz1)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(\
          z,-1)*sqrtxz1)*CF*pow(omx,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*CF\
           - 6*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*z*CF*pow(omx,-1) + 4*Li2(1./2. - \
          1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*x*z*CF - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*\
          pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1)
                result +=  + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*\
          pow(omx,-1) + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*\
          sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)\
          *pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(\
          z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 8*Li2(1./2. + 1./2.*\
          pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 16*Li2(1./2.\
           + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*\
          Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 3*Li2(\
          1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*CF*pow(omx,-1) - 4*Li2(1./2. + \
          1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(\
          opz,-1) + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*pow(\
          sqrtxz1,-1)*CF*pow(omx,-1) + 3*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*z*CF*pow(omx,-1) + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)\
          *x*pow(z,-1)*CF*pow(opz,-1) - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*x*pow(z,-1)*CF - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x\
          *pow(z,-1)*sqrtxz1*CF*pow(opz,-1)
                result +=  + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*\
          sqrtxz1*CF - 12*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) + 8*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*x*pow(sqrtxz1,-1)*CF + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*x*CF + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*x*z*pow(sqrtxz1,-1)*CF - 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
          NC,-1)*x*z*CF + 16*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(x,2)\
          *pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
          pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
          sqrtxz1)*CF*pow(omx,-1) - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*CF + 6*\
          Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*z*CF*pow(omx,-1) - 4*Li2(1./2. + 1./2.\
          *pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*x*z*CF - 1./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*\
          pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(\
          x,-1)*pow(sqrtxz2,-1)*CF - 1./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(sqrtxz2,-1)*CF + \
          Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*z*pow(sqrtxz2,-1)*CF
                result +=  + 1./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 3./\
          2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*CF - 4*Li2(1./2. - 1./2.*sqrtxz2 - \
          1./2.*x)*x*z*pow(sqrtxz2,-1)*CF + 4*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(z,2)*pow(\
          sqrtxz2,-1)*CF - 1./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*pow(sqrtxz2,-1)*CF + \
          Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*\
          sqrtxz2 - 1./2.*x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*\
          sqrtxz2 - 1./2.*x)*pow(x,3)*pow(sqrtxz2,-1)*CF - 1./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*\
          pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(\
          x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,-1)\
          *pow(sqrtxz2,-1)*CF + 1./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(sqrtxz2,-1)*CF - Li2(1./\
          2. + 1./2.*sqrtxz2 - 1./2.*x)*z*pow(sqrtxz2,-1)*CF - 1./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*\
          x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 3./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(\
          sqrtxz2,-1)*CF + 4*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*z*pow(sqrtxz2,-1)*CF - 4*Li2(1./2.\
           + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 1./2.*Li2(1./2. + 1./2.*sqrtxz2\
           - 1./2.*x)*pow(x,2)*pow(sqrtxz2,-1)*CF - Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*z*\
          pow(sqrtxz2,-1)*CF
                result +=  - 1./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*\
          CF - 1./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,3)*pow(sqrtxz2,-1)*CF + 1./4.*Li2(1./2.\
           + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 4*Li2(1./2. - 1./2.*\
          sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1) + 4*Li2(1./2. - 1./2.*\
          sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*\
          z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./\
          2.*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*\
          pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 8*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z\
          )*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 16*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*\
          pow(sqrtxz1,-1)*CF - 3*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*CF*pow(omx,-1) + 4*\
          Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1)\
           - 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 3*\
          Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*z*CF*pow(omx,-1) + 4*Li2(1./2. - 1./2.*\
          sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) - 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.\
          *z)*pow(NC,-1)*x*pow(z,-1)*CF
                result +=  + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(\
          opz,-1) - 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 12*Li2(1.\
          /2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*Li2(1./2. - 1./\
          2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z\
          )*pow(NC,-1)*x*CF - 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*\
          pow(opz,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF - 4*\
          Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*z*CF - 16*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.\
          *z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.\
          *z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + 3*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*CF*pow(\
          omx,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*z*CF*pow(omx,-1) - 4*Li2(1./2. - 1./2.*\
          sqrtxz1 - 1./2.*z)*z*CF + 8*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(z,2)*CF*pow(omx,-1) - 2*\
          Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*x*CF - 8*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*x*pow(z,2)\
          *CF + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(opz,-1)\
           - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 4*Li2(1./2.\
           - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) + 4*Li2(1.\
          /2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)
                result +=  + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*\
          pow(opz,-1) - 8*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(\
          omx,-1) - 16*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1)\
           + 16*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF + 3*Li2(1./2. - 1./2.\
          *sqrtxz1 + 1./2.*z)*pow(NC,-1)*CF*pow(omx,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(\
          NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*\
          pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 3*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(\
          NC,-1)*z*CF*pow(omx,-1) - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*CF*\
          pow(opz,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*Li2(1./2.\
           - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) - 4*Li2(1./2. - 1./\
          2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 12*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.\
          *z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(\
          NC,-1)*x*pow(sqrtxz1,-1)*CF - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*CF - 4*Li2(\
          1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 4*Li2(1./2.\
           - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 4*Li2(1./2. - 1./2.*sqrtxz1\
           + 1./2.*z)*pow(NC,-1)*x*z*CF
                result +=  - 16*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) + 16*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - 3*\
          Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*CF*pow(omx,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*\
          z*CF*pow(omx,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*z*CF - 8*Li2(1./2. - 1./2.*sqrtxz1\
           + 1./2.*z)*pow(z,2)*CF*pow(omx,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*x*CF + 8*Li2(1./\
          2. - 1./2.*sqrtxz1 + 1./2.*z)*x*pow(z,2)*CF + Li2(1 - x*pow(z,-1))*CF*pow(omx,-1) - 2*Li2(1\
           - x*pow(z,-1))*z*CF*pow(omx,-1) - 2*Li2(1 - x*pow(z,-1))*x*CF + 4*Li2(1 - x*pow(z,-1))*x*z*\
          CF + 8*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 8*\
          Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 8*Li2(pow(sqrtxz1,-1)*\
          omz)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 16*Li2(pow(sqrtxz1,-1)*omz)*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 32*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) - 32*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 8*\
          Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 8*Li2(pow(\
          sqrtxz1,-1)*omz)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 8*Li2(pow(sqrtxz1,-1)*omz)*\
          pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) + 8*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*pow(\
          z,-1)*sqrtxz1*CF
                result +=  - 24*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*Li2(\
          pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF + 8*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*\
          x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*x*z*pow(\
          sqrtxz1,-1)*CF + 32*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(\
          opz,-1) - 32*Li2(pow(sqrtxz1,-1)*omz)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + 8*Li2( - \
          sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 8*Li2( - \
          sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 8*Li2( - sqrtxz1*pow(\
          omz,-1))*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 16*Li2( - sqrtxz1*pow(\
          omz,-1))*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 32*Li2( - sqrtxz1*pow(omz,-1))*pow(\
          NC,-1)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 32*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF - 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*\
          pow(opz,-1) + 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 8*\
          Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1) + 8*Li2( - sqrtxz1*\
          pow(omz,-1))*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 24*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*\
          pow(sqrtxz1,-1)*CF*pow(opz,-1) + 16*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*pow(sqrtxz1,-1)*\
          CF
                result +=  + 8*Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 8*\
          Li2( - sqrtxz1*pow(omz,-1))*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 32*Li2( - sqrtxz1*pow(omz,-1)\
          )*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 32*Li2( - sqrtxz1*pow(omz,-1))*pow(\
          NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF - 4*Li2( - z)*pow(NC,-1)*CF*pow(omx,-1)*pow(opz,-1) + 2*\
          Li2( - z)*pow(NC,-1)*CF*pow(omx,-1) - 2*Li2( - z)*pow(NC,-1)*z*CF*pow(omx,-1) + 2*Li2( - x*\
          pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*\
          pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*\
          pow(z,-1)*CF*pow(opx,-1) + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 2*Li2(\
           - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(\
          x,-2)*CF - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 2*Li2( - x*pow(z,-1)\
          )*pow(NC,-1)*pow(x,-2)*z*CF + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(\
          omz,-1)*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1) - 2\
          *Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*\
          pow(x,-1)*z*CF*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(\
          opz,-1) + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 2*Li2( - x*pow(z,-1))*\
          pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1)
                result +=  - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*\
          pow(NC,-1)*CF*pow(omx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*CF*pow(opx,-1) + 2*Li2( - x*pow(\
          z,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*z*CF*pow(opx,-1) + 2*\
          Li2( - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*\
          x*pow(z,-1)*CF*pow(opz,-1) - 4*Li2( - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2( - x*\
          pow(z,-1))*pow(NC,-1)*x*z*CF + Li2( - x*pow(z,-1))*pow(x,-2)*CF*pow(opx,-1) - Li2( - x*pow(\
          z,-1))*pow(x,-2)*CF - 2*Li2( - x*pow(z,-1))*pow(x,-2)*z*CF*pow(opx,-1) + 2*Li2( - x*pow(z,-1)\
          )*pow(x,-2)*z*CF + 4*Li2( - x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 4*Li2( - x*pow(\
          z,-1))*pow(x,-2)*pow(z,2)*CF + Li2( - x*pow(z,-1))*pow(x,-1)*CF - 2*Li2( - x*pow(z,-1))*pow(\
          x,-1)*z*CF + 4*Li2( - x*pow(z,-1))*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 2*Li2( - x*pow(z,-1))*\
          CF*pow(omx,-1) + Li2( - x*pow(z,-1))*CF*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*CF + 4*Li2( - x*\
          pow(z,-1))*z*CF*pow(omx,-1) - 2*Li2( - x*pow(z,-1))*z*CF*pow(opx,-1) + 4*Li2( - x*pow(z,-1))*\
          pow(z,2)*CF*pow(omx,-1) + 4*Li2( - x*pow(z,-1))*pow(z,2)*CF*pow(opx,-1) - 4*Li2( - x*pow(\
          z,-1))*x*z*CF - 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 4*\
          Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) + 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*\
          pow(z,-1)*CF*pow(opx,-1)
                result +=  - 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*CF\
          *pow(opx,-1) - 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*CF + 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*z*CF*\
          pow(opx,-1) - 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*z*CF - 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*pow(\
          z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1)\
           + 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) + 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*z*CF*\
          pow(opx,-1) - 4*Li2( - x)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) + 4*Li2( - x)*pow(\
          NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 4*Li2( - x)*pow(NC,-1)*CF - 4*Li2( - x)*pow(NC,-1)*x*pow(\
          z,-1)*CF*pow(omz,-1) + 4*Li2( - x)*pow(NC,-1)*x*pow(z,-1)*CF + 4*Li2( - x)*pow(NC,-1)*x*CF - \
          2*Li2( - x)*pow(x,-2)*CF*pow(opx,-1) + 2*Li2( - x)*pow(x,-2)*CF + 4*Li2( - x)*pow(x,-2)*z*CF*\
          pow(opx,-1) - 4*Li2( - x)*pow(x,-2)*z*CF - 8*Li2( - x)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) + 8*\
          Li2( - x)*pow(x,-2)*pow(z,2)*CF - 2*Li2( - x)*pow(x,-1)*CF + 4*Li2( - x)*pow(x,-1)*z*CF - 8*\
          Li2( - x)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 2*Li2( - x)*CF*pow(opx,-1) + 4*Li2( - x)*CF - 4\
          *Li2( - x)*z*CF*pow(opx,-1) - 8*Li2( - x)*z*CF + 4*Li2( - x)*x*CF - 8*Li2( - x)*x*z*CF + 2*\
          Li2( - x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*Li2( - x*z)*pow(\
          NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(omz,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*\
          pow(opx,-1)
                result +=  + 2*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 2*Li2( - x*z)*pow(NC,-1)*pow(\
          x,-2)*CF*pow(opx,-1) + 2*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*CF - 2*Li2( - x*z)*pow(NC,-1)*pow(\
          x,-2)*z*CF*pow(opx,-1) + 2*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*z*CF + 2*Li2( - x*z)*pow(NC,-1)*\
          pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)\
          *CF*pow(opx,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) - 2*Li2( - x*z)*pow(\
          NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 2*Li2( - x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(\
          opz,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 2*Li2( - x*z)*pow(NC,-1)*pow(\
          z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*Li2(\
           - x*z)*pow(NC,-1)*CF*pow(omx,-1) - 2*Li2( - x*z)*pow(NC,-1)*CF*pow(opx,-1) - 2*Li2( - x*z)*\
          pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2( - x*z)*pow(NC,-1)*z*CF*pow(opx,-1) + 2*Li2( - x*z)*pow(\
          NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 2*Li2( - x*z)*pow(NC,-1)*x*pow(z,-1)*CF*pow(opz,-1) - 4*\
          Li2( - x*z)*pow(NC,-1)*x*CF + Li2( - x*z)*pow(x,-2)*CF*pow(opx,-1) - Li2( - x*z)*pow(x,-2)*CF\
           - 2*Li2( - x*z)*pow(x,-2)*z*CF*pow(opx,-1) + 2*Li2( - x*z)*pow(x,-2)*z*CF + 4*Li2( - x*z)*\
          pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 4*Li2( - x*z)*pow(x,-2)*pow(z,2)*CF + Li2( - x*z)*pow(\
          x,-1)*CF - 2*Li2( - x*z)*pow(x,-1)*z*CF + 4*Li2( - x*z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - 2\
          *Li2( - x*z)*CF*pow(omx,-1)
                result +=  + Li2( - x*z)*CF*pow(opx,-1) - 4*Li2( - x*z)*z*CF*pow(omx,-1) - 2*Li2( - x*z)*z*CF*\
          pow(opx,-1) + 4*Li2( - x*z)*z*CF - 4*Li2( - x*z)*pow(z,2)*CF*pow(omx,-1) + 4*Li2( - x*z)*pow(\
          z,2)*CF*pow(opx,-1) + 2*Li2( - x*z)*x*CF + 8*Li2( - x*z)*x*pow(z,2)*CF + 4*Li2( - 1/(1 + \
          sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(z,-1)*\
          sqrtxz1*CF*pow(omx,-1)*pow(opz,-1) - 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*\
          sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*Li2( - 1/(1\
           + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF*pow(omx,-1)*pow(opz,-1) + 8*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*\
          sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF*pow(omx,-1) + 16*Li2( - 1/(1\
           + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(\
          sqrtxz1,-1)*CF*pow(opz,-1) - 16*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + \
          1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(sqrtxz1,-1)*CF - 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + \
          sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1)*\
          pow(opz,-1) + 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z\
          )*z)*pow(NC,-1)*z*pow(sqrtxz1,-1)*CF*pow(omx,-1) - 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + \
          sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF*pow(opz,-1)
                result +=  + 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)\
          *pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 12*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*\
          sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*x*pow(sqrtxz1,-1)*CF*pow(opz,-1) + 8*Li2( - 1/(1\
           + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*x*pow(\
          sqrtxz1,-1)*CF + 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1\
           - z)*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 4*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1\
           + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*x*z*pow(sqrtxz1,-1)*CF + 16*Li2(\
           - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(\
          x,2)*pow(sqrtxz1,-1)*CF*pow(opz,-1) - 16*Li2( - 1/(1 + sqrtxz1 - z) + 1/(1 + sqrtxz1 - z)*\
          sqrtxz1 + 1/(1 + sqrtxz1 - z)*z)*pow(NC,-1)*pow(x,2)*pow(sqrtxz1,-1)*CF + 4*Li2(x)*pow(NC,-1)\
          *pow(x,-2)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 4*Li2(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*\
          pow(omz,-1) - 4*Li2(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + 4*Li2(x)*pow(NC,-1)*\
          pow(x,-2)*pow(z,-1)*CF - 4*Li2(x)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) + 4*Li2(x)*pow(NC,-1)*\
          pow(x,-2)*CF - 4*Li2(x)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 4*Li2(x)*pow(NC,-1)*pow(x,-2)\
          *z*CF + 4*Li2(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(omz,-1)*pow(opx,-1) - 4*Li2(x)*pow(\
          NC,-1)*pow(x,-1)*pow(z,-1)*CF*pow(opx,-1)
                result +=  - 4*Li2(x)*pow(NC,-1)*pow(x,-1)*CF*pow(opx,-1) - 4*Li2(x)*pow(NC,-1)*pow(x,-1)*z*CF*\
          pow(opx,-1) - 2*Li2(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 4*Li2(x)*pow(NC,-1)*pow(z,-1)*CF\
          *pow(omz,-1)*pow(opx,-1) - 4*Li2(x)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + Li2(x)*pow(NC,-1)*\
          pow(z,-1)*CF + 4*Li2(x)*pow(NC,-1)*CF*pow(omx,-1) - 4*Li2(x)*pow(NC,-1)*CF*pow(omz,-1)*pow(\
          opx,-1) - 2*Li2(x)*pow(NC,-1)*CF - 2*Li2(x)*pow(NC,-1)*z*CF*pow(omx,-1) + 4*Li2(x)*pow(NC,-1)\
          *x*pow(z,-1)*CF*pow(omz,-1) - 3*Li2(x)*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2(x)*pow(NC,-1)*x*CF*\
          pow(omz,-1) - 2*Li2(x)*pow(NC,-1)*x*CF + 2*Li2(x)*pow(NC,-1)*x*z*CF + 2*Li2(x)*pow(x,-2)*CF*\
          pow(opx,-1) - 2*Li2(x)*pow(x,-2)*CF - 4*Li2(x)*pow(x,-2)*z*CF*pow(opx,-1) + 4*Li2(x)*pow(\
          x,-2)*z*CF + 8*Li2(x)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 8*Li2(x)*pow(x,-2)*pow(z,2)*CF + 2*\
          Li2(x)*pow(x,-1)*CF - 4*Li2(x)*pow(x,-1)*z*CF + 8*Li2(x)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - \
          Li2(x)*pow(z,-1)*CF - 3*Li2(x)*CF*pow(omx,-1) - 2*Li2(x)*CF*pow(opx,-1) + 2*Li2(x)*CF + 6*\
          Li2(x)*z*CF*pow(omx,-1) + 4*Li2(x)*z*CF*pow(opx,-1) - 8*Li2(x)*pow(z,2)*CF*pow(omx,-1) - Li2(\
          x)*x*pow(z,-1)*CF + 4*Li2(x)*x*CF - 4*Li2(x)*x*z*CF + 8*Li2(x)*x*pow(z,2)*CF - Li2(z)*CF*pow(\
          omx,-1) + Li2(z)*CF + 2*Li2(z)*z*CF*pow(omx,-1) + 3*Li2(z)*x*CF - 2*Li2(z)*x*z*CF
        elif orders == '001':
            if z != x and z != 1.-x:
                result += + ln(z)*LMUA*CF + ln(z)*LMUA*x*CF + 2*ln(z)*LMUA*x*z*CF + 1./3.*LMUA*pow(z,-1)*CF + 1./2.*LMUA*CF - 3./2.*LMUA*z*CF + 2./3.*LMUA*pow(z,2)*CF + 1./3.*LMUA*x*pow(z,-1)*CF + 3./2.*LMUA*x*CF - 1./2.*LMUA*x*z*CF - 4./3.*LMUA*x*pow(z,2)*CF
        elif orders == '010':
            if z != x and z != 1.-x:
                result += - ln(x)*LMUF*pow(z,-1)*CF + 2*ln(x)*LMUF*CF - ln(x)*LMUF*x*pow(z,-1)*CF + 2*ln(x)*LMUF*x*CF - 2./3.*LMUF*pow(x,-1)*pow(z,-1)*CF + 4./3.*LMUF*pow(x,-1)*CF - 1./2.*LMUF*pow(z,-1)*CF + LMUF*CF + 1./2.*LMUF*x*pow(z,-1)*CF - LMUF*x*CF + 2./3.*LMUF*pow(x,2)*pow(z,-1)*CF - 4./3.*LMUF*pow(x,2)*CF
        return result
    elif rsl == 'rs':
        result = 0
        if orders == '000':
            result_r0 = - 2*pow(NC,-1)*CF + 1./3.*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) - 1./6.*pow(NC,-1)*pow(pi,2)\
      *CF + 2*pow(NC,-1)*x*CF + 1./6.*pow(NC,-1)*x*pow(pi,2)*CF + 13./9.*pow(x,-1)*CF - 11./6.*CF\
       + 1./6.*pow(pi,2)*CF + 17./6.*x*CF + 1./6.*x*pow(pi,2)*CF - 22./9.*pow(x,2)*CF - ln(x)*pow(NC,-1)*CF\
       - ln(x)*pow(NC,-1)*x*CF + ln(x)*CF + 3*ln(x)*x*CF + 2*ln(x)*pow(x,2)*CF + 4*ln(x)*ln(1 + x)*pow(NC,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x)*pow(NC,-1)*\
      CF + 2*ln(x)*ln(1 + x)*pow(NC,-1)*x*CF - pow(ln(x),2)*pow(NC,-1)*CF*pow(opx,-1) + 1./2.*pow(\
      ln(x),2)*pow(NC,-1)*CF - 1./2.*pow(ln(x),2)*pow(NC,-1)*x*CF - pow(ln(x),2)*CF - pow(ln(x),2)*\
      x*CF + 2./3.*ln(omx)*pow(x,-1)*CF + 1./2.*ln(omx)*CF - 1./2.*ln(omx)*x*CF - 2./3.*ln(omx)*\
      pow(x,2)*CF + 4*Li2( - x)*pow(NC,-1)*CF*pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*CF + 2*Li2( - x)\
      *pow(NC,-1)*x*CF - Li2(x)*CF - Li2(x)*x*CF
            result_r1 = 2./3.*pow(x,-1)*CF + 1./2.*CF - 1./2.*x*CF - 2./3.*pow(x,2)*CF + ln(x)*CF + ln(x)*x*CF
            result += result_r0*1/(1-z) + result_r1*ln(1-z)/(1-z)
        elif orders == '010':
            result_r0 = - 2./3.*LMUF*pow(x,-1)*CF - 1./2.*LMUF*CF + 1./2.*LMUF*x*CF + 2./3.*LMUF*pow(x,2)*CF - ln(x)*LMUF*CF - ln(x)*LMUF*x*CF
            result += result_r0*1/(1-z)
        return result
    elif rsl == 'rl':
        result = 0
        if orders == '000':
            result += - 15./4.*pow(NC,-1)*CF + 2*pow(NC,-1)*zeta3*CF*pow(opx,-1) - pow(NC,-1)*zeta3*CF + 4./3.*\
      pow(NC,-1)*pow(rln2,3)*CF*pow(opx,-1) - 2./3.*pow(NC,-1)*pow(rln2,3)*CF - 1./12.*pow(NC,-1)*\
      pow(pi,2)*CF - 2./3.*pow(NC,-1)*pow(pi,2)*rln2*CF*pow(opx,-1) + 1./3.*pow(NC,-1)*pow(pi,2)*\
      rln2*CF + 15./4.*pow(NC,-1)*x*CF + pow(NC,-1)*x*zeta3*CF + 2./3.*pow(NC,-1)*x*pow(rln2,3)*CF\
       - 1./12.*pow(NC,-1)*x*pow(pi,2)*CF - 1./3.*pow(NC,-1)*x*pow(pi,2)*rln2*CF + 52./27.*pow(\
      x,-1)*CF - 41./36.*CF + 1./6.*pow(pi,2)*CF + 17./36.*x*CF + 1./2.*x*pow(pi,2)*CF - 34./27.*\
      pow(x,2)*CF + 1./3.*pow(x,2)*pow(pi,2)*CF - 2*ln(1 + x)*pow(NC,-1)*pow(rln2,2)*CF*pow(opx,-1) + ln(1 + x)*pow(NC,-1)*pow(\
      rln2,2)*CF - 1./3.*ln(1 + x)*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) + 1./6.*ln(1 + x)*pow(NC,-1)\
      *pow(pi,2)*CF - ln(1 + x)*pow(NC,-1)*x*pow(rln2,2)*CF - 1./6.*ln(1 + x)*pow(NC,-1)*x*pow(\
      pi,2)*CF + 2./3.*pow(ln(1 + x),3)*pow(NC,-1)*CF*pow(opx,-1) - 1./3.*pow(ln(1 + x),3)*pow(\
      NC,-1)*CF
            result +=  + 1./3.*pow(ln(1 + x),3)*pow(NC,-1)*x*CF - 3./4.*ln(x)*pow(NC,-1)*CF - 2./3.*ln(x)*\
      pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) + 1./3.*ln(x)*pow(NC,-1)*pow(pi,2)*CF - 19./4.*ln(x)*pow(\
      NC,-1)*x*CF - 1./3.*ln(x)*pow(NC,-1)*x*pow(pi,2)*CF + 23./6.*ln(x)*CF - 1./3.*ln(x)*pow(pi,2)\
      *CF - 5./6.*ln(x)*x*CF - 1./3.*ln(x)*x*pow(pi,2)*CF + 38./9.*ln(x)*pow(x,2)*CF + ln(x)*ln(1 + x)*\
      pow(NC,-1)*CF + ln(x)*ln(1 + x)*pow(NC,-1)*x*CF + pow(ln(x),2)*pow(NC,-1)*x*CF - 13./8.*pow(ln(x),2)*CF - 13./8.*pow(ln(x),2)*x*CF - 5./3.*pow(\
      ln(x),2)*pow(x,2)*CF - 4*pow(ln(x),2)*ln(1 + x)*pow(NC,-1)*CF*pow(opx,-1) + 2*pow(ln(x),2)*ln(1 + x)*\
      pow(NC,-1)*CF - 2*pow(ln(x),2)*ln(1 + x)*pow(NC,-1)*x*CF + 1./2.*pow(ln(x),3)*pow(NC,-1)*CF*\
      pow(opx,-1) - 1./4.*pow(ln(x),3)*pow(NC,-1)*CF + 1./4.*pow(ln(x),3)*pow(NC,-1)*x*CF + 5./12.*\
      pow(ln(x),3)*CF + 5./12.*pow(ln(x),3)*x*CF - 2./3.*ln(x)*ln(omx)*pow(x,-1)*CF - 1./2.*ln(x)*\
      ln(omx)*CF
            result +=  + 1./2.*ln(x)*ln(omx)*x*CF + 2./3.*ln(x)*ln(omx)*pow(x,2)*CF + 4*ln(x)*ln(omx)*ln(1\
       + x)*pow(NC,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(omx)*ln(1 + x)*pow(NC,-1)*CF + 2*ln(x)*ln(omx)*\
      ln(1 + x)*pow(NC,-1)*x*CF - 1./2.*ln(x)*pow(ln(omx),2)*CF - 1./2.*ln(x)*pow(ln(omx),2)*x*CF\
       - 4*ln(x)*Li2( - x)*pow(NC,-1)*CF*pow(opx,-1) + 2*ln(x)*Li2( - x)*pow(NC,-1)*CF - 2*ln(x)*\
      Li2( - x)*pow(NC,-1)*x*CF + ln(x)*Li2(x)*CF + ln(x)*Li2(x)*x*CF - 2*ln(omx)*pow(NC,-1)*CF - 2\
      *ln(omx)*pow(NC,-1)*pow(rln2,2)*CF*pow(opx,-1) + ln(omx)*pow(NC,-1)*pow(rln2,2)*CF + 1./3.*\
      ln(omx)*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) - 1./6.*ln(omx)*pow(NC,-1)*pow(pi,2)*CF + 2*ln(\
      omx)*pow(NC,-1)*x*CF - ln(omx)*pow(NC,-1)*x*pow(rln2,2)*CF + 1./6.*ln(omx)*pow(NC,-1)*x*pow(\
      pi,2)*CF + 13./9.*ln(omx)*pow(x,-1)*CF - 11./6.*ln(omx)*CF + 1./6.*ln(omx)*pow(pi,2)*CF + 17./\
      6.*ln(omx)*x*CF + 1./6.*ln(omx)*x*pow(pi,2)*CF - 22./9.*ln(omx)*pow(x,2)*CF + 4*ln(omx)*ln(1 + x)*pow(NC,-1)*rln2*CF*pow(opx,-1) - 2*ln(omx)*ln(1 + x)*pow(NC,-1)\
      *rln2*CF + 2*ln(omx)*ln(1 + x)*pow(NC,-1)*x*rln2*CF - 2*ln(omx)*pow(ln(1 + x),2)*pow(NC,-1)*\
      CF*pow(opx,-1) + ln(omx)*pow(ln(1 + x),2)*pow(NC,-1)*CF - ln(omx)*pow(ln(1 + x),2)*pow(NC,-1)\
      *x*CF + 1./3.*pow(ln(omx),2)*pow(x,-1)*CF + 1./4.*pow(ln(omx),2)*CF - 1./4.*pow(ln(omx),2)*x*\
      CF
            result +=  - 1./3.*pow(ln(omx),2)*pow(x,2)*CF + 4*ln(omx)*Li2( - x)*pow(NC,-1)*CF*pow(opx,-1) - \
      2*ln(omx)*Li2( - x)*pow(NC,-1)*CF + 2*ln(omx)*Li2( - x)*pow(NC,-1)*x*CF - ln(omx)*Li2(x)*CF\
       - ln(omx)*Li2(x)*x*CF + ln(opx)*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) - 1./2.*ln(opx)*pow(\
      NC,-1)*pow(pi,2)*CF + 1./2.*ln(opx)*pow(NC,-1)*x*pow(pi,2)*CF - 4*Li3(1./2. - 1./2.*x)*pow(\
      NC,-1)*CF*pow(opx,-1) + 2*Li3(1./2. - 1./2.*x)*pow(NC,-1)*CF - 2*Li3(1./2. - 1./2.*x)*pow(\
      NC,-1)*x*CF - 4*Li3(1./2. + 1./2.*x)*pow(NC,-1)*CF*pow(opx,-1) + 2*Li3(1./2. + 1./2.*x)*pow(\
      NC,-1)*CF - 2*Li3(1./2. + 1./2.*x)*pow(NC,-1)*x*CF + 4*Li3(1 - x)*pow(NC,-1)*CF*pow(opx,-1)\
       - 2*Li3(1 - x)*pow(NC,-1)*CF + 2*Li3(1 - x)*pow(NC,-1)*x*CF - Li3(1 - x)*CF - Li3(1 - x)*x*\
      CF - 4*Li3(1/(1 + x) - 1/(1 + x)*x)*pow(NC,-1)*CF*pow(opx,-1) + 2*Li3(1/(1 + x) - 1/(1 + x)*x\
      )*pow(NC,-1)*CF - 2*Li3(1/(1 + x) - 1/(1 + x)*x)*pow(NC,-1)*x*CF + 2*Li3(x)*pow(NC,-1)*CF*\
      pow(opx,-1) - Li3(x)*pow(NC,-1)*CF + Li3(x)*pow(NC,-1)*x*CF + Li2( - x)*pow(NC,-1)*CF + Li2(\
       - x)*pow(NC,-1)*x*CF + Li2(x)*pow(NC,-1)*CF + Li2(x)*pow(NC,-1)*x*CF\
       - 2./3.*Li2(x)*pow(x,-1)*CF - 3./2.*Li2(x)*CF - 5./2.*Li2(x)*x*CF - 4./3.*Li2(x)*pow(x,2)*CF
            result_r0 = - 2*pow(NC,-1)*CF + 1./3.*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) - 1./6.*pow(NC,-1)*pow(pi,2)\
      *CF + 2*pow(NC,-1)*x*CF + 1./6.*pow(NC,-1)*x*pow(pi,2)*CF + 13./9.*pow(x,-1)*CF - 11./6.*CF\
       + 1./6.*pow(pi,2)*CF + 17./6.*x*CF + 1./6.*x*pow(pi,2)*CF - 22./9.*pow(x,2)*CF - ln(x)*pow(NC,-1)*CF\
       - ln(x)*pow(NC,-1)*x*CF + ln(x)*CF + 3*ln(x)*x*CF + 2*ln(x)*pow(x,2)*CF + 4*ln(x)*ln(1 + x)*pow(NC,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x)*pow(NC,-1)*\
      CF + 2*ln(x)*ln(1 + x)*pow(NC,-1)*x*CF - pow(ln(x),2)*pow(NC,-1)*CF*pow(opx,-1) + 1./2.*pow(\
      ln(x),2)*pow(NC,-1)*CF - 1./2.*pow(ln(x),2)*pow(NC,-1)*x*CF - pow(ln(x),2)*CF - pow(ln(x),2)*\
      x*CF + 2./3.*ln(omx)*pow(x,-1)*CF + 1./2.*ln(omx)*CF - 1./2.*ln(omx)*x*CF - 2./3.*ln(omx)*\
      pow(x,2)*CF + 4*Li2( - x)*pow(NC,-1)*CF*pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*CF + 2*Li2( - x)\
      *pow(NC,-1)*x*CF - Li2(x)*CF - Li2(x)*x*CF
            result_r1 = 2./3.*pow(x,-1)*CF + 1./2.*CF - 1./2.*x*CF - 2./3.*pow(x,2)*CF + ln(x)*CF + ln(x)*x*CF
            result += result_r0*ln(1-z) + result_r1*ln(1-z)*ln(1-z)/2
        elif orders == '010':
            result += + 2*LMUF*pow(NC,-1)*CF - 1./3.*LMUF*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) + 1./6.*LMUF*pow(NC,-1)*pow(pi,2)*CF - 2*LMUF*pow(NC,-1)*x*CF - 1./6.*\
      LMUF*pow(NC,-1)*x*pow(pi,2)*CF - 13./9.*LMUF*pow(x,-1)*CF + 11./6.*LMUF*CF - 1./6.*LMUF*pow(\
      pi,2)*CF - 17./6.*LMUF*x*CF - 1./6.*LMUF*x*pow(pi,2)*CF + 22./9.*LMUF*pow(x,2)*CF - 4*Li2( - x)*LMUF*pow(NC,-1)*CF*pow(opx,-1) + 2*Li2( - x)*LMUF*pow(\
      NC,-1)*CF - 2*Li2( - x)*LMUF*pow(NC,-1)*x*CF + Li2(x)*LMUF*CF + Li2(x)*LMUF*x*CF - 2./3.*ln(omx)*\
      LMUF*pow(x,-1)*CF - 1./2.*ln(omx)*LMUF*CF + 1./2.*ln(omx)*LMUF*x*CF + 2./3.*ln(omx)*LMUF*pow(x,2)*CF\
      + ln(x)*LMUF*pow(NC,-1)*CF + ln(x)*LMUF*pow(NC,-1)*x*CF - ln(x)*LMUF*CF - 3*ln(x)*LMUF*x*CF - 2*ln(x)*LMUF\
      *pow(x,2)*CF - 4*ln(x)*ln(1 + x)*LMUF*pow(NC,-1)*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x)*LMUF*pow(NC,-1)*CF - 2*ln(x)*ln(1 + x)*LMUF*pow(NC,-1)*x*CF\
      + pow(ln(x),2)*LMUF*pow(NC,-1)*CF*pow(opx,-1) - 1./2.*pow(ln(x),2)*LMUF*\
      pow(NC,-1)*CF + 1./2.*pow(ln(x),2)*LMUF*pow(NC,-1)*x*CF + pow(ln(x),2)*LMUF*CF + pow(ln(x),2)*LMUF*x*CF
            result_r0 = - 2./3.*LMUF*pow(x,-1)*CF - 1./2.*LMUF*CF + 1./2.*LMUF*x*CF + 2./3.*LMUF*pow(x,2)*CF - ln(x)*LMUF*CF - ln(x)*LMUF*x*CF
            result += result_r0*ln(1-z)
        elif orders == '020':
            result += + 1./3.*pow(LMUF,2)*pow(x,-1)*CF + 1./4.*pow(LMUF,2)*CF - 1./4.*pow(LMUF,2)*x*CF - 1./3.*pow(LMUF,2)*pow(x,2)*CF + 1./2.*ln(x)*pow(LMUF,2)*CF + 1./2.*ln(x)*pow(LMUF,2)*x*CF
        return result
    elif rsl == 'sr':
        result = 0
        if orders == '000':
            result_0r = - 2*pow(NC,-1)*CF + 1./3.*pow(NC,-1)*pow(pi,2)*CF*pow(opz,-1) - 1./6.*pow(NC,-1)*pow(pi,2)\
      *CF + 2*pow(NC,-1)*z*CF + 1./6.*pow(NC,-1)*z*pow(pi,2)*CF - 7./18.*pow(z,-1)*CF - 10./3.*CF\
       + 1./6.*pow(pi,2)*CF + 7./3.*z*CF + 1./6.*z*pow(pi,2)*CF + 25./18.*pow(z,2)*CF - ln(z)*pow(NC,-1)*CF\
       - ln(z)*pow(NC,-1)*z*CF + 2./3.*ln(z)*pow(z,-1)*CF - 1./2.*ln(z)*CF - 2*ln(z)*z*CF - 2./3.*\
      ln(z)*pow(z,2)*CF + 4*ln(z)*ln(1 + z)*pow(NC,-1)*CF*pow(\
      opz,-1) - 2*ln(z)*ln(1 + z)*pow(NC,-1)*CF + 2*ln(z)*ln(1 + z)*pow(NC,-1)*z*CF - pow(ln(z),2)*\
      pow(NC,-1)*CF*pow(opz,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*CF - 1./2.*pow(ln(z),2)*pow(NC,-1)*\
      z*CF + pow(ln(z),2)*CF + pow(ln(z),2)*z*CF + 2./3.*ln(omz)*pow(z,-1)*CF + 1./2.*ln(omz)*CF - \
      1./2.*ln(omz)*z*CF - 2./3.*ln(omz)*pow(z,2)*CF + 4*Li2( - z)*pow(NC,-1)*CF*pow(opz,-1) - 2*\
      Li2( - z)*pow(NC,-1)*CF + 2*Li2( - z)*pow(NC,-1)*z*CF - Li2(z)*CF - Li2(z)*z*CF
            result_1r = 2./3.*pow(z,-1)*CF + 1./2.*CF - 1./2.*z*CF - 2./3.*pow(z,2)*CF + ln(z)*CF + ln(z)*z*CF
            result += result_0r*1/(1-x) + result_1r*ln(1-x)/(1-x)
        elif orders == '001':
            result_0r = - 2./3.*LMUA*pow(z,-1)*CF - 1./2.*LMUA*CF + 1./2.*LMUA*z*CF + 2./3.*LMUA*pow(z,2)*CF - ln(z)*LMUA*CF - ln(z)*LMUA*z*CF
            result += result_0r*1/(1-x)
        return result
    elif rsl == 'ss':
        result = 0
        return result
    elif rsl == 'sl':
        result = 0
        return result
    elif rsl == 'lr':
        result = 0
        if orders == '000':
            result += 1./4.*pow(NC,-1)*CF + 4./3.*pow(NC,-1)*pow(rln2,3)*CF*pow(opz,-1) - 2./3.*pow(NC,-1)*pow(\
      rln2,3)*CF - 1./12.*pow(NC,-1)*pow(pi,2)*CF - 2./3.*pow(NC,-1)*pow(pi,2)*rln2*CF*pow(opz,-1)\
       + 1./3.*pow(NC,-1)*pow(pi,2)*rln2*CF - 1./4.*pow(NC,-1)*z*CF + 2./3.*pow(NC,-1)*z*pow(\
      rln2,3)*CF - 1./12.*pow(NC,-1)*z*pow(pi,2)*CF - 1./3.*pow(NC,-1)*z*pow(pi,2)*rln2*CF - 107./\
      108.*pow(z,-1)*CF - 11./9.*CF + 2*zeta3*CF - 1./6.*pow(pi,2)*CF - 4./9.*z*CF + 2*z*zeta3*CF\
       - 1./4.*z*pow(pi,2)*CF + 287./108.*pow(z,2)*CF - 2*ln(1 + z)*pow(NC,-1)*pow(rln2,2)*CF*pow(opz,-1) + ln(1 + z)*pow(\
      NC,-1)*pow(rln2,2)*CF + 1./3.*ln(1 + z)*pow(NC,-1)*pow(pi,2)*CF*pow(opz,-1) - 1./6.*ln(1 + z)\
      *pow(NC,-1)*pow(pi,2)*CF - ln(1 + z)*pow(NC,-1)*z*pow(rln2,2)*CF + 1./6.*ln(1 + z)*pow(NC,-1)\
      *z*pow(pi,2)*CF - 7./4.*ln(z)*pow(NC,-1)*CF + 1./4.*ln(z)*pow(NC,-1)*z*CF - 7./18.*ln(z)*pow(\
      z,-1)*CF - 5*ln(z)*CF + 1./6.*ln(z)*pow(pi,2)*CF - 9./2.*ln(z)*z*CF + 1./6.*ln(z)*z*pow(pi,2)\
      *CF
            result +=  - 31./18.*ln(z)*pow(z,2)*CF + ln(z)*ln(1 + z)*\
      pow(NC,-1)*CF + ln(z)*ln(1 + z)*pow(NC,-1)*z*CF - pow(ln(z),2)*pow(NC,-1)*CF - pow(ln(z),2)*pow(NC,-1)*z*CF + 1./3.*pow(ln(z),2)*pow(z,-1)*CF\
       - 1./8.*pow(ln(z),2)*CF - 5./8.*pow(ln(z),2)*z*CF + 3*pow(ln(z),2)*ln(1 + z)*pow(NC,-1)*CF*pow(\
      opz,-1) - 3./2.*pow(ln(z),2)*ln(1 + z)*pow(NC,-1)*CF + 3./2.*pow(ln(z),2)*ln(1 + z)*pow(\
      NC,-1)*z*CF - 5./6.*pow(ln(z),3)*pow(NC,-1)*CF*pow(opz,-1) + 5./12.*pow(ln(z),3)*pow(NC,-1)*\
      CF - 5./12.*pow(ln(z),3)*pow(NC,-1)*z*CF + 5./12.*pow(ln(z),3)*CF + 5./12.*pow(ln(z),3)*z*CF\
       + 4*ln(z)*ln(omz)*ln(1 + z)*pow(NC,-1)*CF*pow(opz,-1) - 2*ln(z)*ln(omz)*ln(1 + z)*pow(NC,-1)\
      *CF + 2*ln(z)*ln(omz)*ln(1 + z)*pow(NC,-1)*z*CF - 1./2.*ln(z)*pow(ln(omz),2)*CF - 1./2.*ln(z)\
      *pow(ln(omz),2)*z*CF + 2*ln(z)*Li2( - z)*pow(NC,-1)*CF*pow(opz,-1) - ln(z)*Li2( - z)*pow(\
      NC,-1)*CF
            result +=  + ln(z)*Li2( - z)*pow(NC,-1)*z*CF - 2*ln(omz)*pow(NC,-1)*CF - 2*ln(omz)*pow(NC,-1)*\
      pow(rln2,2)*CF*pow(opz,-1) + ln(omz)*pow(NC,-1)*pow(rln2,2)*CF + 1./3.*ln(omz)*pow(NC,-1)*\
      pow(pi,2)*CF*pow(opz,-1) - 1./6.*ln(omz)*pow(NC,-1)*pow(pi,2)*CF + 2*ln(omz)*pow(NC,-1)*z*CF\
       - ln(omz)*pow(NC,-1)*z*pow(rln2,2)*CF + 1./6.*ln(omz)*pow(NC,-1)*z*pow(pi,2)*CF - 7./18.*ln(\
      omz)*pow(z,-1)*CF - 10./3.*ln(omz)*CF + 1./6.*ln(omz)*pow(pi,2)*CF + 7./3.*ln(omz)*z*CF + 1./\
      6.*ln(omz)*z*pow(pi,2)*CF + 25./18.*ln(omz)*pow(z,2)*CF + 4*ln(omz)*ln(1 + z)*pow(NC,-1)*rln2*CF*pow(opz,-1) - 2*ln(omz)*ln(1 + z)*pow(NC,-1)*rln2*CF + 2*ln(omz)\
      *ln(1 + z)*pow(NC,-1)*z*rln2*CF - 2*ln(omz)*pow(ln(1 + z),2)*pow(NC,-1)*CF*pow(opz,-1) + ln(\
      omz)*pow(ln(1 + z),2)*pow(NC,-1)*CF - ln(omz)*pow(ln(1 + z),2)*pow(NC,-1)*z*CF + 1./3.*pow(\
      ln(omz),2)*pow(z,-1)*CF + 1./4.*pow(ln(omz),2)*CF - 1./4.*pow(ln(omz),2)*z*CF - 1./3.*pow(ln(\
      omz),2)*pow(z,2)*CF + 4*ln(omz)*Li2( - z)*pow(NC,-1)*CF*pow(opz,-1) - 2*ln(omz)*Li2( - z)*\
      pow(NC,-1)*CF + 2*ln(omz)*Li2( - z)*pow(NC,-1)*z*CF - ln(omz)*Li2(z)*CF - ln(omz)*Li2(z)*z*CF\
       + 2./3.*ln(opz)*pow(NC,-1)*pow(pi,2)*CF*pow(opz,-1) - 1./3.*ln(opz)*pow(NC,-1)*pow(pi,2)*CF\
       + 1./3.*ln(opz)*pow(NC,-1)*z*pow(pi,2)*CF - 4*Li3(1./2. - 1./2.*z)*pow(NC,-1)*CF*pow(opz,-1)\
       + 2*Li3(1./2. - 1./2.*z)*pow(NC,-1)*CF
            result +=  - 2*Li3(1./2. - 1./2.*z)*pow(NC,-1)*z*CF - 4*Li3(1./2. + 1./2.*z)*pow(NC,-1)*CF*pow(\
      opz,-1) + 2*Li3(1./2. + 1./2.*z)*pow(NC,-1)*CF - 2*Li3(1./2. + 1./2.*z)*pow(NC,-1)*z*CF + 4*\
      Li3(1 - z)*pow(NC,-1)*CF*pow(opz,-1) - 2*Li3(1 - z)*pow(NC,-1)*CF + 2*Li3(1 - z)*pow(NC,-1)*z\
      *CF - Li3(1 - z)*CF - Li3(1 - z)*z*CF + 2*Li3( - z)*pow(NC,-1)*CF*pow(opz,-1) - Li3( - z)*\
      pow(NC,-1)*CF + Li3( - z)*pow(NC,-1)*z*CF + 4*Li3(1/(1 + z))*pow(NC,-1)*CF*pow(opz,-1) - 2*\
      Li3(1/(1 + z))*pow(NC,-1)*CF + 2*Li3(1/(1 + z))*pow(NC,-1)*z*CF - 4*Li3(1/(1 + z) - 1/(1 + z)\
      *z)*pow(NC,-1)*CF*pow(opz,-1) + 2*Li3(1/(1 + z) - 1/(1 + z)*z)*pow(NC,-1)*CF - 2*Li3(1/(1 + z\
      ) - 1/(1 + z)*z)*pow(NC,-1)*z*CF + 2*Li3(z)*pow(NC,-1)*CF*pow(opz,-1) - Li3(z)*pow(NC,-1)*CF\
       + Li3(z)*pow(NC,-1)*z*CF - 2*Li3(z)*CF - 2*Li3(z)*z*CF + Li2( - z)*pow(NC,-1)*CF + Li2( - z)\
      *pow(NC,-1)*z*CF + Li2(z)*pow(NC,-1)*CF + Li2(z)*pow(NC,-1)*z*CF - 2./3.\
      *Li2(z)*pow(z,-1)*CF + 1./2.*Li2(z)*CF + 2*Li2(z)*z*CF + 2./3.*Li2(z)*pow(z,2)*CF
            result_0r = - 2*pow(NC,-1)*CF + 1./3.*pow(NC,-1)*pow(pi,2)*CF*pow(opz,-1) - 1./6.*pow(NC,-1)*pow(pi,2)\
      *CF + 2*pow(NC,-1)*z*CF + 1./6.*pow(NC,-1)*z*pow(pi,2)*CF - 7./18.*pow(z,-1)*CF - 10./3.*CF\
       + 1./6.*pow(pi,2)*CF + 7./3.*z*CF + 1./6.*z*pow(pi,2)*CF + 25./18.*pow(z,2)*CF - ln(z)*pow(NC,-1)*CF\
       - ln(z)*pow(NC,-1)*z*CF + 2./3.*ln(z)*pow(z,-1)*CF - 1./2.*ln(z)*CF - 2*ln(z)*z*CF - 2./3.*\
      ln(z)*pow(z,2)*CF + 4*ln(z)*ln(1 + z)*pow(NC,-1)*CF*pow(\
      opz,-1) - 2*ln(z)*ln(1 + z)*pow(NC,-1)*CF + 2*ln(z)*ln(1 + z)*pow(NC,-1)*z*CF - pow(ln(z),2)*\
      pow(NC,-1)*CF*pow(opz,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*CF - 1./2.*pow(ln(z),2)*pow(NC,-1)*\
      z*CF + pow(ln(z),2)*CF + pow(ln(z),2)*z*CF + 2./3.*ln(omz)*pow(z,-1)*CF + 1./2.*ln(omz)*CF - \
      1./2.*ln(omz)*z*CF - 2./3.*ln(omz)*pow(z,2)*CF + 4*Li2( - z)*pow(NC,-1)*CF*pow(opz,-1) - 2*\
      Li2( - z)*pow(NC,-1)*CF + 2*Li2( - z)*pow(NC,-1)*z*CF - Li2(z)*CF - Li2(z)*z*CF
            result_1r = 2./3.*pow(z,-1)*CF + 1./2.*CF - 1./2.*z*CF - 2./3.*pow(z,2)*CF + ln(z)*CF + ln(z)*z*CF
            result += result_0r*ln(1-x) + result_1r*ln(1-x)*ln(1-x)/2
        elif orders == '001':
            result += - 4*Li2( - z)*LMUA*pow(NC,-1)*CF*pow(opz,-1) + 2*Li2( - z)*LMUA*pow(NC,-1)*\
      CF - 2*Li2( - z)*LMUA*pow(NC,-1)*z*CF + Li2(z)*\
      LMUA*CF + Li2(z)*LMUA*z*CF - 2./3.*ln(omz)*LMUA*pow(z,-1)*CF - 1.\
      /2.*ln(omz)*LMUA*CF + 1./2.*ln(omz)*LMUA*z*CF + 2./3.*ln(omz)*LMUA*pow(z,2)*CF \
      + ln(z)*LMUA*pow(NC,-1)*CF + ln(z)*LMUA*pow(NC,-1)*z*CF\
       - 2./3.*ln(z)*LMUA*pow(z,-1)*CF + 1./2.*ln(z)*LMUA*CF + 2*ln(z)*LMUA*z*CF + 2./3.*ln(z)*LMUA\
      *pow(z,2)*CF - 4*ln(z)*ln(1 + z)*LMUA*pow(NC,-1)*CF*pow(\
      opz,-1) + 2*ln(z)*ln(1 + z)*LMUA*pow(NC,-1)*CF - 2*ln(z)*ln(1 + z)*LMUA*pow(NC,-1)*z*CF\
      + 2*LMUA*pow(NC,-1)*CF - 1./3.*LMUA*pow(NC,-1)*pow(pi,2)*CF*pow(opz,-1) + 1./6.*LMUA*pow(NC,-1)*pow(pi,2)*CF - 2*LMUA*pow(NC,-1)*z*CF\
       - 1./6.*LMUA*pow(NC,-1)*z*pow(pi,2)*CF + 7./18.*LMUA*pow(z,-1)*CF + 10./3.*LMUA*CF - 1./6.*\
      LMUA*pow(pi,2)*CF - 7./3.*LMUA*z*CF - 1./6.*LMUA*z*pow(pi,2)*CF - 25./18.*LMUA*pow(z,2)*CF\
      + pow(ln(z),2)*LMUA*pow(NC,-1)*CF*pow(opz,-1) - 1./2.*pow(ln(z),2)*LMUA*pow(NC,-1)*CF + 1./2.*pow(ln(z),2)*LMUA*pow(NC,-1)*z*CF - pow(ln(z),2)*LMUA*CF - pow(ln(z),2)*LMUA*z*CF
            result_0r = - 2./3.*LMUA*pow(z,-1)*CF - 1./2.*LMUA*CF + 1./2.*LMUA*z*CF + 2./3.*LMUA*pow(z,2)*CF - ln(z)*LMUA*CF - ln(z)*LMUA*z*CF
            result += result_0r*ln(1-x)
        elif orders == '002':
            result += + 1./3.*pow(LMUA,2)*pow(z,-1)*CF + 1./4.*pow(LMUA,2)*CF - 1./4.*pow(LMUA,2)*z*CF - 1./3.*pow(LMUA,2)*pow(z,2)*CF + 1./2.*ln(z)*pow(LMUA,2)*CF + 1./2.*ln(z)*pow(LMUA,2)*z*CF
        return result
    elif rsl == 'ls':
        result = 0
        return result
    elif rsl == 'll':
        result = 0
        return result
    else:
        raise ValueError('Invalid rsl value')
