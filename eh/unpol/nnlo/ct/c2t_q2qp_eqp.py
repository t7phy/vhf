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

def ct_nnlo_q2qp_eqp(x, z, rsl, orders):

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
                result += 13./9.*pow(x,-1)*pow(z,-1)*CF - 26./9.*pow(x,-1)*CF - 11./6.*pow(z,-1)*CF + 1./6.*pow(\
      z,-1)*pow(pi,2)*CF - 7./3.*CF - 1./3.*pow(pi,2)*CF + 10*z*CF + 17./6.*x*pow(z,-1)*CF + 1./6.*\
      x*pow(z,-1)*pow(pi,2)*CF + 1./3.*x*CF - 1./3.*x*pow(pi,2)*CF - 10*x*z*CF - 22./9.*pow(x,2)*\
      pow(z,-1)*CF + 44./9.*pow(x,2)*CF + 1./4.*ln(x)*pow(x,-1)*pow(poly2,-1)*CF - 1./\
      4.*ln(x)*pow(x,-1)*CF + ln(x)*pow(z,-1)*CF - 1./4.*ln(x)*pow(poly2,-1)*CF - 19./4.*ln(x)*CF\
       + 5*ln(x)*z*CF + 3*ln(x)*x*pow(z,-1)*CF - 35./4.*ln(x)*x*CF + 5*ln(x)*x*z*CF + 2*ln(x)*pow(\
      x,2)*pow(z,-1)*CF - 17./4.*ln(x)*pow(x,2)*CF - 1./4.*ln(x)*pow(x,3)*pow(poly2,-1)*CF + 1./4.*\
      ln(x)*pow(x,4)*pow(poly2,-1)*CF + 1./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,-1)*pow(sqrtxz2,-1)*\
      pow(poly2,-1)*CF - 1./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,-1)*pow(sqrtxz2,-1)*CF - 7./4.*ln(x)\
      *ln(1 - sqrtxz2 + x)*pow(sqrtxz2,-1)*CF + 7./2.*ln(x)*ln(1 - sqrtxz2 + x)*z*pow(sqrtxz2,-1)*\
      CF - 1./8.*ln(x)*ln(1 - sqrtxz2 + x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*ln(x)*ln(1 - \
      sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF + 10*ln(x)*ln(1 - sqrtxz2 + x)*x*z*pow(sqrtxz2,-1)*CF - 10*\
      ln(x)*ln(1 - sqrtxz2 + x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF
                result +=  - 7./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,2)*pow(sqrtxz2,-1)*CF + 7./2.*ln(x)*ln(1 - \
      sqrtxz2 + x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 1./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,3)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF - 1./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*CF + \
      1./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./8.*ln(x)*ln(1\
       + sqrtxz2 + x)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./8.*ln(x)*ln(1 + sqrtxz2 + x)*\
      pow(x,-1)*pow(sqrtxz2,-1)*CF + 7./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(sqrtxz2,-1)*CF - 7./2.*ln(\
      x)*ln(1 + sqrtxz2 + x)*z*pow(sqrtxz2,-1)*CF + 1./8.*ln(x)*ln(1 + sqrtxz2 + x)*x*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF - 10*ln(x\
      )*ln(1 + sqrtxz2 + x)*x*z*pow(sqrtxz2,-1)*CF + 10*ln(x)*ln(1 + sqrtxz2 + x)*x*pow(z,2)*pow(\
      sqrtxz2,-1)*CF + 7./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,2)*pow(sqrtxz2,-1)*CF - 7./2.*ln(x)*\
      ln(1 + sqrtxz2 + x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 1./8.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,3)*\
      pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./8.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*\
      CF - 1./8.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - pow(ln(x),2)\
      *pow(z,-1)*CF + 2*pow(ln(x),2)*CF - pow(ln(x),2)*x*pow(z,-1)*CF + 2*pow(ln(x),2)*x*CF + ln(x)\
      *ln(z)*pow(z,-1)*CF - ln(x)*ln(z)*CF + ln(x)*ln(z)*x*pow(z,-1)*CF - ln(x)*ln(z)*x*CF + ln(x)*\
      ln(omz)*pow(z,-1)*CF
                result +=  - 2*ln(x)*ln(omz)*CF + ln(x)*ln(omz)*x*pow(z,-1)*CF - 2*ln(x)*ln(omz)*x*CF + 2./3.*\
      ln(z)*pow(x,-1)*pow(z,-1)*CF + 1./4.*ln(z)*pow(x,-1)*pow(poly2,-1)*CF + 2./3.*ln(z)*pow(x,-1)\
      *CF*pow(omz,-1) - 19./12.*ln(z)*pow(x,-1)*CF + 1./2.*ln(z)*pow(z,-1)*CF + 1./4.*ln(z)*pow(\
      poly2,-1)*CF - ln(z)*CF*pow(omz,-1) - 5./4.*ln(z)*CF + 5*ln(z)*z*CF - 1./2.*ln(z)*x*pow(z,-1)\
      *CF + ln(z)*x*CF*pow(omz,-1) + 5./4.*ln(z)*x*CF - 5*ln(z)*x*z*CF - 2./3.*ln(z)*pow(x,2)*pow(\
      z,-1)*CF - 2./3.*ln(z)*pow(x,2)*CF*pow(omz,-1) + 19./12.*ln(z)*pow(x,2)*CF - 1./4.*ln(z)*pow(\
      x,3)*pow(poly2,-1)*CF - 1./4.*ln(z)*pow(x,4)*pow(poly2,-1)*CF + 2./3.*ln(omx)*pow(x,-1)*pow(\
      z,-1)*CF - 4./3.*ln(omx)*pow(x,-1)*CF + 1./2.*ln(omx)*pow(z,-1)*CF - ln(omx)*CF - 1./2.*ln(\
      omx)*x*pow(z,-1)*CF + ln(omx)*x*CF - 2./3.*ln(omx)*pow(x,2)*pow(z,-1)*CF + 4./3.*ln(omx)*pow(\
      x,2)*CF + 2./3.*ln(omz)*pow(x,-1)*pow(z,-1)*CF - 4./3.*ln(omz)*pow(x,-1)*CF + 1./2.*ln(omz)*\
      pow(z,-1)*CF - ln(omz)*CF - 1./2.*ln(omz)*x*pow(z,-1)*CF + ln(omz)*x*CF - 2./3.*ln(omz)*pow(\
      x,2)*pow(z,-1)*CF + 4./3.*ln(omz)*pow(x,2)*CF + 1./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*\
      pow(x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./8.*Li2(1./2. - 1./2.*pow(\
      x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*CF - 7./4.*Li2(1./2. - 1./2.*pow(\
      x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(sqrtxz2,-1)*CF + 7./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./\
      2.*pow(x,-1)*sqrtxz2)*z*pow(sqrtxz2,-1)*CF
                result +=  - 1./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*pow(\
      poly2,-1)*CF - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)\
      *CF + 10*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*z*pow(sqrtxz2,-1)*CF - 10*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 7./4.*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*pow(sqrtxz2,-1)*CF + 7./2.*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 1./8.*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)\
      *CF - 1./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(sqrtxz2,-1)*\
      CF + 1./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,5)*pow(sqrtxz2,-1)*\
      pow(poly2,-1)*CF - 1./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,-1)*\
      pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*CF + 7./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(sqrtxz2,-1)*CF - 7./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*z*\
      pow(sqrtxz2,-1)*CF + 1./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x\
      *pow(sqrtxz2,-1)*CF
                result +=  - 10*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*z*pow(sqrtxz2,-1)*CF + \
      10*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 7./\
      4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*pow(sqrtxz2,-1)*CF - 7./2.\
      *Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 1./8.\
      *Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(sqrtxz2,-1)*pow(\
      poly2,-1)*CF + 1./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(\
      sqrtxz2,-1)*CF - 1./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,5)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF - 1./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF + 1./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(\
      sqrtxz2,-1)*CF + 7./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(sqrtxz2,-1)*CF - 7./2.*Li2(1./\
      2. - 1./2.*sqrtxz2 - 1./2.*x)*z*pow(sqrtxz2,-1)*CF + 1./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*\
      x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(\
      sqrtxz2,-1)*CF - 10*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*z*pow(sqrtxz2,-1)*CF + 10*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 7./4.*Li2(1./2. - 1./2.*sqrtxz2\
       - 1./2.*x)*pow(x,2)*pow(sqrtxz2,-1)*CF - 7./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)\
      *z*pow(sqrtxz2,-1)*CF
                result +=  + 1./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*\
      CF + 1./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,3)*pow(sqrtxz2,-1)*CF - 1./8.*Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./8.*Li2(1./2. + 1./\
      2.*sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./8.*Li2(1./2. + 1./2.*\
      sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(sqrtxz2,-1)*CF - 7./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*\
      pow(sqrtxz2,-1)*CF + 7./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*z*pow(sqrtxz2,-1)*CF - 1./8.*\
      Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2. + 1.\
      /2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*CF + 10*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*z*\
      pow(sqrtxz2,-1)*CF - 10*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - \
      7./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*pow(sqrtxz2,-1)*CF + 7./2.*Li2(1./2. + 1./\
      2.*sqrtxz2 - 1./2.*x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 1./8.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.\
      *x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./8.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*\
      pow(x,3)*pow(sqrtxz2,-1)*CF + 1./8.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,5)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF - Li2(x)*pow(z,-1)*CF + 2*Li2(x)*CF - Li2(x)*x*pow(z,-1)*CF + 2*\
      Li2(x)*x*CF
        elif orders == '010':
            if z != x and z != 1.-x:
                result += - 2./3.*LMUF*pow(x,-1)*pow(z,-1)*CF + 4./3.*LMUF*pow(x,-1)*\
      CF - 1./2.*LMUF*pow(z,-1)*CF + LMUF*CF + 1./2.*LMUF*x*pow(z,-1)*CF - LMUF*x*CF + 2./3.*LMUF*\
      pow(x,2)*pow(z,-1)*CF - 4./3.*LMUF*pow(x,2)*CF - ln(x)*LMUF*pow(z,-1)*CF + 2*ln(x)*LMUF*CF - ln(x)*LMUF*x*\
      pow(z,-1)*CF + 2*ln(x)*LMUF*x*CF
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
