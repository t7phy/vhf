from configs.eh import CF, NC, TR, Li2, Li3
from configs.eh import ln2 as rln2
from configs.eh import atanint as InvTanInt
from numpy import sqrt, pi
from numpy import power as pow
from numpy import log as ln
from numpy import arctan as ArcTan

LMUR = 1
LMUF = 1
LMUA = 1

def ct_nnlo_q2q_eqp(x, z, rsl, orders):

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
                result += - 5./8.*pow(x,-1)*pow(z,-1)*CF + 5./8.*pow(x,-1)*CF - 5./8.*pow(z,-2)*CF - 15./4.*pow(\
          z,-1)*CF + 15./4.*CF + 5./8.*z*CF + 5./8.*x*pow(z,-2)*CF + 15./4.*x*pow(z,-1)*CF - 15./4.*x*\
          CF - 5./8.*x*z*CF + 5./8.*pow(x,2)*pow(z,-1)*CF - 5./8.*pow(x,2)*CF + 5./8.*ArcTan(z*sqrtxz3)\
          *ln(z*sqrtxz3)*pow(x,-2)*sqrtxz3*CF + 9./4.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,-1)*pow(\
          z,-1)*sqrtxz3*CF + 9./4.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 5./8.*\
          ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(z,-2)*sqrtxz3*CF + 13./2.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)\
          *sqrtxz3*CF + 5./8.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(z,2)*sqrtxz3*CF + 9./4.*ArcTan(z*\
          sqrtxz3)*ln(z*sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF + 9./4.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*x*z*\
          sqrtxz3*CF + 5./8.*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,2)*sqrtxz3*CF - 5./8.*ArcTan(sqrtxz3\
          )*ln(sqrtxz3)*pow(x,-2)*sqrtxz3*CF - 9./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(x,-1)*pow(z,-1)*\
          sqrtxz3*CF - 9./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 5./8.*ArcTan(sqrtxz3)\
          *ln(sqrtxz3)*pow(z,-2)*sqrtxz3*CF - 13./2.*ArcTan(sqrtxz3)*ln(sqrtxz3)*sqrtxz3*CF - 5./8.*\
          ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(z,2)*sqrtxz3*CF - 9./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)*x*pow(\
          z,-1)*sqrtxz3*CF - 9./4.*ArcTan(sqrtxz3)*ln(sqrtxz3)*x*z*sqrtxz3*CF - 5./8.*ArcTan(sqrtxz3)*\
          ln(sqrtxz3)*pow(x,2)*sqrtxz3*CF - 5./16.*InvTanInt( - sqrtxz3)*pow(x,-2)*sqrtxz3*CF - 9./8.*\
          InvTanInt( - sqrtxz3)*pow(x,-1)*pow(z,-1)*sqrtxz3*CF
                result +=  - 9./8.*InvTanInt( - sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 5./16.*InvTanInt( - sqrtxz3)*\
          pow(z,-2)*sqrtxz3*CF - 13./4.*InvTanInt( - sqrtxz3)*sqrtxz3*CF - 5./16.*InvTanInt( - sqrtxz3)\
          *pow(z,2)*sqrtxz3*CF - 9./8.*InvTanInt( - sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF - 9./8.*InvTanInt(\
           - sqrtxz3)*x*z*sqrtxz3*CF - 5./16.*InvTanInt( - sqrtxz3)*pow(x,2)*sqrtxz3*CF - 5./8.*\
          InvTanInt(z*sqrtxz3)*pow(x,-2)*sqrtxz3*CF - 9./4.*InvTanInt(z*sqrtxz3)*pow(x,-1)*pow(z,-1)*\
          sqrtxz3*CF - 9./4.*InvTanInt(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 5./8.*InvTanInt(z*sqrtxz3)*\
          pow(z,-2)*sqrtxz3*CF - 13./2.*InvTanInt(z*sqrtxz3)*sqrtxz3*CF - 5./8.*InvTanInt(z*sqrtxz3)*\
          pow(z,2)*sqrtxz3*CF - 9./4.*InvTanInt(z*sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF - 9./4.*InvTanInt(z*\
          sqrtxz3)*x*z*sqrtxz3*CF - 5./8.*InvTanInt(z*sqrtxz3)*pow(x,2)*sqrtxz3*CF + 5./16.*InvTanInt(\
          sqrtxz3)*pow(x,-2)*sqrtxz3*CF + 9./8.*InvTanInt(sqrtxz3)*pow(x,-1)*pow(z,-1)*sqrtxz3*CF + 9./\
          8.*InvTanInt(sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 5./16.*InvTanInt(sqrtxz3)*pow(z,-2)*sqrtxz3*CF\
           + 13./4.*InvTanInt(sqrtxz3)*sqrtxz3*CF + 5./16.*InvTanInt(sqrtxz3)*pow(z,2)*sqrtxz3*CF + 9./\
          8.*InvTanInt(sqrtxz3)*x*pow(z,-1)*sqrtxz3*CF + 9./8.*InvTanInt(sqrtxz3)*x*z*sqrtxz3*CF + 5./\
          16.*InvTanInt(sqrtxz3)*pow(x,2)*sqrtxz3*CF + 5./16.*ln(x)*pow(x,-1)*pow(z,-1)*CF - 5./16.*ln(\
          x)*pow(x,-1)*CF - 5./16.*ln(x)*pow(z,-2)*CF - 17./8.*ln(x)*pow(z,-1)*CF + 17./8.*ln(x)*CF + 5.\
          /16.*ln(x)*z*CF
                result +=  - 5./16.*ln(x)*x*pow(z,-2)*CF - 17./8.*ln(x)*x*pow(z,-1)*CF + 17./8.*ln(x)*x*CF + 5./\
          16.*ln(x)*x*z*CF + 5./16.*ln(x)*pow(x,2)*pow(z,-1)*CF - 5./16.*ln(x)*pow(x,2)*CF - 2*ln(x)*\
          ln(z)*pow(z,-1)*CF - 2*ln(x)*ln(z)*CF - 2*ln(x)*ln(z)*x*pow(z,-1)*CF - 2*ln(x)*ln(z)*x*CF - 5.\
          /16.*ln(z)*pow(x,-1)*pow(z,-1)*CF - 5./16.*ln(z)*pow(x,-1)*CF + 5./16.*ln(z)*pow(z,-2)*CF - \
          17./8.*ln(z)*pow(z,-1)*CF - 17./8.*ln(z)*CF + 5./16.*ln(z)*z*CF - 5./16.*ln(z)*x*pow(z,-2)*CF\
           + 17./8.*ln(z)*x*pow(z,-1)*CF + 17./8.*ln(z)*x*CF - 5./16.*ln(z)*x*z*CF + 5./16.*ln(z)*pow(\
          x,2)*pow(z,-1)*CF + 5./16.*ln(z)*pow(x,2)*CF
        return result
    elif rsl == 'rs':
        result = 0
        return result
    elif rsl == 'rl':
        result = 0
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
