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

def cl_nnlo_q2q_eqp(x, z, orders, rsl):

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
                result += 3./4.*pow(x,-1)*pow(z,-1)*CF - 3./4.*pow(x,-1)*CF + 3./4.*pow(z,-2)*CF - 7./2.*pow(z,-1)*\
          CF + 3./2.*CF + 5./4.*z*CF - 3./4.*x*pow(z,-2)*CF + 3./2.*x*pow(z,-1)*CF + 1./2.*x*CF - 5./4.\
          *x*z*CF + 5./4.*pow(x,2)*pow(z,-1)*CF - 5./4.*pow(x,2)*CF - 3./4.*ArcTan(z*sqrtxz3)*ln(z*\
          sqrtxz3)*pow(x,-2)*sqrtxz3*CF + 1./2.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,-1)*pow(z,-1)*\
          sqrtxz3*CF - 3./2.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 3./4.*ArcTan(z*\
          sqrtxz3)*ln(z*sqrtxz3)*pow(z,-2)*sqrtxz3*CF + ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*sqrtxz3*CF + 5./\
          4.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(z,2)*sqrtxz3*CF - 3./2.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3\
          )*x*pow(z,-1)*sqrtxz3*CF + 9./2.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*x*z*sqrtxz3*CF + 5./4.*\
          ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,2)*sqrtxz3*CF + 3./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(\
          x,-2)*sqrtxz3*CF - 1./2.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(x,-1)*pow(z,-1)*sqrtxz3*CF + 3./2.*\
          ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 3./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(\
          z,-2)*sqrtxz3*CF - ArcTan(sqrtxz3)*ln(sqrtxz3)*sqrtxz3*CF - 5./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)\
          *pow(z,2)*sqrtxz3*CF + 3./2.*ArcTan(sqrtxz3)*ln(sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF - 9./2.*\
          ArcTan(sqrtxz3)*ln(sqrtxz3)*x*z*sqrtxz3*CF - 5./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(x,2)*\
          sqrtxz3*CF + 3./8.*InvTanInt( - sqrtxz3)*pow(x,-2)*sqrtxz3*CF - 1./4.*InvTanInt( - sqrtxz3)*\
          pow(x,-1)*pow(z,-1)*sqrtxz3*CF
                result +=  + 3./4.*InvTanInt( - sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 3./8.*InvTanInt( - sqrtxz3)*\
          pow(z,-2)*sqrtxz3*CF - 1./2.*InvTanInt( - sqrtxz3)*sqrtxz3*CF - 5./8.*InvTanInt( - sqrtxz3)*\
          pow(z,2)*sqrtxz3*CF + 3./4.*InvTanInt( - sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF - 9./4.*InvTanInt(\
           - sqrtxz3)*x*z*sqrtxz3*CF - 5./8.*InvTanInt( - sqrtxz3)*pow(x,2)*sqrtxz3*CF + 3./4.*\
          InvTanInt(z*sqrtxz3)*pow(x,-2)*sqrtxz3*CF - 1./2.*InvTanInt(z*sqrtxz3)*pow(x,-1)*pow(z,-1)*\
          sqrtxz3*CF + 3./2.*InvTanInt(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 3./4.*InvTanInt(z*sqrtxz3)*\
          pow(z,-2)*sqrtxz3*CF - InvTanInt(z*sqrtxz3)*sqrtxz3*CF - 5./4.*InvTanInt(z*sqrtxz3)*pow(z,2)*\
          sqrtxz3*CF + 3./2.*InvTanInt(z*sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF - 9./2.*InvTanInt(z*sqrtxz3)*x\
          *z*sqrtxz3*CF - 5./4.*InvTanInt(z*sqrtxz3)*pow(x,2)*sqrtxz3*CF - 3./8.*InvTanInt(sqrtxz3)*\
          pow(x,-2)*sqrtxz3*CF + 1./4.*InvTanInt(sqrtxz3)*pow(x,-1)*pow(z,-1)*sqrtxz3*CF - 3./4.*\
          InvTanInt(sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 3./8.*InvTanInt(sqrtxz3)*pow(z,-2)*sqrtxz3*CF + 1.\
          /2.*InvTanInt(sqrtxz3)*sqrtxz3*CF + 5./8.*InvTanInt(sqrtxz3)*pow(z,2)*sqrtxz3*CF - 3./4.*\
          InvTanInt(sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF + 9./4.*InvTanInt(sqrtxz3)*x*z*sqrtxz3*CF + 5./8.*\
          InvTanInt(sqrtxz3)*pow(x,2)*sqrtxz3*CF - 3./8.*ln(x)*pow(x,-1)*pow(z,-1)*CF + 3./8.*ln(x)*\
          pow(x,-1)*CF + 3./8.*ln(x)*pow(z,-2)*CF - 1./4.*ln(x)*pow(z,-1)*CF - 3./4.*ln(x)*CF + 5./8.*\
          ln(x)*z*CF
                result +=  + 3./8.*ln(x)*x*pow(z,-2)*CF - 13./4.*ln(x)*x*pow(z,-1)*CF + 9./4.*ln(x)*x*CF + 5./8.\
          *ln(x)*x*z*CF + 5./8.*ln(x)*pow(x,2)*pow(z,-1)*CF - 5./8.*ln(x)*pow(x,2)*CF - 4*ln(x)*ln(z)*x\
          *CF + 3./8.*ln(z)*pow(x,-1)*pow(z,-1)*CF + 3./8.*ln(z)*pow(x,-1)*CF - 3./8.*ln(z)*pow(z,-2)*\
          CF - 1./4.*ln(z)*pow(z,-1)*CF - 13./4.*ln(z)*CF + 5./8.*ln(z)*z*CF + 3./8.*ln(z)*x*pow(z,-2)*\
          CF - 3./4.*ln(z)*x*pow(z,-1)*CF + 9./4.*ln(z)*x*CF - 5./8.*ln(z)*x*z*CF + 5./8.*ln(z)*pow(\
          x,2)*pow(z,-1)*CF + 5./8.*ln(z)*pow(x,2)*CF
        else:
            result = 0
    else:
        result = 0

    return result
