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

def cl_nnlo_q2qp_eq(x, z, orders, rsl):

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
            result = 0
            if z != x and z != 1.-x:
                result += - 4*CF + 2*z*CF + 2*pow(z,2)*CF + 7*x*CF - 1./3.*x*pow(pi,2)*CF - 2./3.*x*z*pow(pi,2)*CF\
           - 7*x*pow(z,2)*CF  + 8*ln(x)*x*CF - 4*\
          ln(x)*x*z*CF - 4*ln(x)*x*pow(z,2)*CF + 4*ln(x)*ln(z)*x*CF + 8*ln(x)*ln(z)*x*z*CF - 2*ln(z)*CF\
           - 4*ln(z)*z*CF - 2*ln(z)*x*CF + 8*ln(z)*x*z*CF + 2*ln(z)*x*pow(z,2)*CF - 2*pow(ln(z),2)*x*CF - 4*pow(ln(z),2)*x*z*CF - 2*ln(z)*ln(omx)*x*CF\
           - 4*ln(z)*ln(omx)*x*z*CF - 4*ln(omx)*x*CF + 2*ln(omx)*x*z*CF + 2*ln(omx)*x*pow(z,2)*CF - 4*\
          ln(omz)*x*CF + 2*ln(omz)*x*z*CF + 2*ln(omz)*x*pow(z,2)*CF + 2*Li2(z)*x*CF + 4*Li2(z)*x*z*CF
        else:
            result = 0
    elif orders == '001':
        if rsl == 'rr':
            result = 0
            if z != x and z != 1.-x:
                result += + 4*LMUA*x*CF - 2*LMUA*x*z*CF - 2*LMUA*x*pow(z,2)*CF + 2*ln(z)*LMUA*x*CF + 4*ln(z)*LMUA*x*z*CF
        else:
            result = 0
    else:
        result = 0
    
    return result
    