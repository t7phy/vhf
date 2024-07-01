from configs.eh import *

LMUR = 1
LMUF = 1
LMUA = 1

def ct_nnlo_q2q_eq(x, z, rsl, orders):

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
            if z != x and z != round(1 - x, ndecimals):
                result += 1./3.*pow(NC,-1)*pow(x,-2)*pow(z,-1)*pow(pi,2)*CF*pow(opx,-1) - 1./3.*pow(NC,-1)*pow(\
      x,-2)*pow(z,-1)*pow(pi,2)*CF - 2./3.*pow(NC,-1)*pow(x,-2)*pow(pi,2)*CF*pow(opx,-1) + 2./3.*\
      pow(NC,-1)*pow(x,-2)*pow(pi,2)*CF + 2./3.*pow(NC,-1)*pow(x,-2)*z*pow(pi,2)*CF*pow(opx,-1) - 2.\
      /3.*pow(NC,-1)*pow(x,-2)*z*pow(pi,2)*CF + 1./3.*pow(NC,-1)*pow(x,-1)*pow(z,-1)*pow(pi,2)*CF\
       - 1./2.*pow(NC,-1)*pow(x,-1)*pow(poly2,-1)*CF + 1./2.*pow(NC,-1)*pow(x,-1)*CF - 2./3.*pow(\
      NC,-1)*pow(x,-1)*pow(pi,2)*CF + 2./3.*pow(NC,-1)*pow(x,-1)*z*pow(pi,2)*CF*pow(opx,-1) - 12*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) + 12*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 4*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1) - 4*pow(NC,-1)*pow(z,-1)*CF - 4*pow(NC,-1)*pow(z,-1)*pow(\
      rln2,2)*CF*pow(omx,-1) + 2*pow(NC,-1)*pow(z,-1)*pow(rln2,2)*CF - 6*pow(NC,-1)*pow(z,-1)*\
      sqrtxz1*rln2*CF*pow(omx,-1) + 4*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF + 4./3.*pow(NC,-1)*pow(\
      z,-1)*pow(pi,2)*CF*pow(omx,-1)*pow(omz,-1) - 4./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(\
      omx,-1) - 2./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omz,-1) - 2./3.*pow(NC,-1)*pow(z,-1)*\
      pow(pi,2)*CF*pow(opx,-1) + 2./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF + 1./2.*pow(NC,-1)*pow(\
      poly2,-1)*CF + 12*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 4*pow(NC,-1)*CF*pow(omx,-1) - 8*\
      pow(NC,-1)*CF*pow(omz,-1) - 1./2.*pow(NC,-1)*CF*pow(omxmz,-1) + 23*pow(NC,-1)*CF - 8*pow(\
      NC,-1)*pow(rln2,2)*CF*pow(omx,-1)
                result +=  + 4*pow(NC,-1)*pow(rln2,2)*CF - 6*pow(NC,-1)*sqrtxz1*rln2*CF*pow(omx,-1) + 1./3.*pow(\
      NC,-1)*pow(pi,2)*CF*pow(omx,-1)*pow(omz,-1) - 4./3.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1) + 1./\
      3.*pow(NC,-1)*pow(pi,2)*CF*pow(omz,-1) + 4./3.*pow(NC,-1)*pow(pi,2)*CF*pow(opx,-1) + 3./2.*\
      pow(NC,-1)*pow(pi,2)*CF + 4*pow(NC,-1)*z*CF*pow(omx,-1) - 16*pow(NC,-1)*z*CF - 4*pow(NC,-1)*z\
      *pow(rln2,2)*CF*pow(omx,-1) - 4./3.*pow(NC,-1)*z*pow(pi,2)*CF*pow(omx,-1) - 1./3.*pow(NC,-1)*\
      z*pow(pi,2)*CF*pow(opx,-1) + 1./6.*pow(NC,-1)*z*pow(pi,2)*CF + 8*pow(NC,-1)*x*pow(z,-1)*CF*\
      pow(omz,-1) - 15./2.*pow(NC,-1)*x*pow(z,-1)*CF + 2*pow(NC,-1)*x*pow(z,-1)*pow(rln2,2)*CF + 2*\
      pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF - 2./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*CF*pow(\
      omz,-1) + 1./3.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*CF - pow(NC,-1)*x*pow(poly2,-1)*CF - 4*pow(\
      NC,-1)*x*CF*pow(omz,-1) - 1./2.*pow(NC,-1)*x*CF*pow(xmz,-1) + 1./2.*pow(NC,-1)*x*CF*pow(\
      omxmz,-1) - 19./2.*pow(NC,-1)*x*CF + 4*pow(NC,-1)*x*pow(rln2,2)*CF + 6*pow(NC,-1)*x*sqrtxz1*\
      rln2*CF - 2./3.*pow(NC,-1)*x*pow(pi,2)*CF*pow(omz,-1) + 11./6.*pow(NC,-1)*x*pow(pi,2)*CF + 25\
      *pow(NC,-1)*x*z*CF + 4*pow(NC,-1)*x*z*pow(rln2,2)*CF + 13./6.*pow(NC,-1)*x*z*pow(pi,2)*CF + \
      pow(NC,-1)*pow(x,2)*pow(poly2,-1)*CF + pow(NC,-1)*pow(x,2)*CF*pow(xmz,-1) + 1./2.*pow(NC,-1)*\
      pow(x,2)*CF - 1./2.*pow(NC,-1)*pow(x,3)*pow(poly2,-1)*CF - pow(NC,-1)*pow(x,3)*CF*pow(xmz,-1)\
       + 1./2.*pow(NC,-1)*pow(x,4)*pow(poly2,-1)*CF
                result +=  + 1./3.*pow(x,-2)*pow(pi,2)*CF*pow(opx,-1) - 1./3.*pow(x,-2)*pow(pi,2)*CF - 2./3.*\
      pow(x,-2)*z*pow(pi,2)*CF*pow(opx,-1) + 2./3.*pow(x,-2)*z*pow(pi,2)*CF + 4./3.*pow(x,-2)*pow(\
      z,2)*pow(pi,2)*CF*pow(opx,-1) - 4./3.*pow(x,-2)*pow(z,2)*pow(pi,2)*CF + 13./9.*pow(x,-1)*pow(\
      z,-1)*CF - 26./9.*pow(x,-1)*CF + 1./3.*pow(x,-1)*pow(pi,2)*CF - 2./3.*pow(x,-1)*z*pow(pi,2)*\
      CF + 4./3.*pow(x,-1)*pow(z,2)*pow(pi,2)*CF*pow(opx,-1) - 71./36.*pow(z,-1)*CF + 1./6.*pow(\
      z,-1)*pow(pi,2)*CF + 10./3.*CF + 6*pow(rln2,2)*CF*pow(omx,-1) + 6*sqrtxz1*rln2*CF*pow(omx,-1)\
       - 5./6.*pow(pi,2)*CF*pow(omx,-1) - 2./3.*pow(pi,2)*CF*pow(opx,-1) - 5./6.*pow(pi,2)*CF + 37./\
      12.*z*CF + 4*z*pow(rln2,2)*CF*pow(omx,-1) - 8*z*pow(rln2,2)*CF + 5./3.*z*pow(pi,2)*CF*pow(\
      omx,-1) + 4./3.*z*pow(pi,2)*CF*pow(opx,-1) + 2./3.*z*pow(pi,2)*CF + 43./18.*pow(z,2)*CF + 16*\
      pow(z,2)*pow(rln2,2)*CF*pow(omx,-1) - 2*pow(z,2)*pow(pi,2)*CF*pow(omx,-1) - 2./3.*pow(z,2)*\
      pow(pi,2)*CF*pow(opx,-1) + 121./36.*x*pow(z,-1)*CF + 1./6.*x*pow(z,-1)*pow(pi,2)*CF + 2*x*CF\
       - 4*x*pow(rln2,2)*CF - 4*x*sqrtxz1*rln2*CF - 1./6.*x*pow(pi,2)*CF - 95./12.*x*z*CF - x*z*\
      pow(pi,2)*CF - 77./18.*x*pow(z,2)*CF - 16*x*pow(z,2)*pow(rln2,2)*CF + 4./3.*x*pow(z,2)*pow(\
      pi,2)*CF - 22./9.*pow(x,2)*pow(z,-1)*CF + 44./9.*pow(x,2)*CF + NC*CF*pow(omx,-1) + NC*CF*pow(\
      omz,-1) + 1./2.*NC*CF*pow(omxmz,-1) - 37./18.*NC*CF - NC*pow(pi,2)*CF*pow(omx,-1)*pow(omz,-1)\
       + 1./2.*NC*pow(pi,2)*CF*pow(omx,-1)
                result +=  + 1./2.*NC*pow(pi,2)*CF*pow(omz,-1) - 13./6.*NC*pow(pi,2)*CF - NC*z*CF*pow(omx,-1) - \
      8./3.*NC*z*CF + 1./2.*NC*z*pow(pi,2)*CF*pow(omx,-1) - 1./6.*NC*z*pow(pi,2)*CF - NC*x*CF*pow(\
      omz,-1) - 1./2.*NC*x*CF*pow(xmz,-1) - 1./2.*NC*x*CF*pow(omxmz,-1) - NC*x*CF + 1./2.*NC*x*pow(\
      pi,2)*CF*pow(omz,-1) - 1./6.*NC*x*pow(pi,2)*CF + 47./18.*NC*x*z*CF - 13./6.*NC*x*z*pow(pi,2)*\
      CF + NC*pow(x,2)*CF*pow(xmz,-1) + NC*pow(x,2)*CF - NC*pow(x,3)*CF*pow(xmz,-1) - 10./9.*NF*CF\
       + 2./3.*NF*z*CF - 16./9.*NF*x*z*CF
                result += - 9*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(NC,-1)*pow(x,-1)*z*sqrtxz3*CF + ArcTan(z*sqrtxz3)*ln(z*\
      sqrtxz3)*pow(NC,-1)*sqrtxz3*CF + 5*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(NC,-1)*pow(z,2)*\
      sqrtxz3*CF - 9*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(NC,-1)*x*z*sqrtxz3*CF + 3*ArcTan(z*sqrtxz3\
      )*ln(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 3*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*sqrtxz3*CF - 23*\
      ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(z,2)*sqrtxz3*CF + 3*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*x*z*\
      sqrtxz3*CF + 9*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(NC,-1)*pow(x,-1)*z*sqrtxz3*CF - ArcTan(sqrtxz3\
      )*ln(sqrtxz3)*pow(NC,-1)*sqrtxz3*CF - 5*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(NC,-1)*pow(z,2)*\
      sqrtxz3*CF + 9*ArcTan(sqrtxz3)*ln(sqrtxz3)*pow(NC,-1)*x*z*sqrtxz3*CF - 3*ArcTan(sqrtxz3)*ln(\
      sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 3*ArcTan(sqrtxz3)*ln(sqrtxz3)*sqrtxz3*CF + 23*ArcTan(\
      sqrtxz3)*ln(sqrtxz3)*pow(z,2)*sqrtxz3*CF - 3*ArcTan(sqrtxz3)*ln(sqrtxz3)*x*z*sqrtxz3*CF + 9./\
      2.*InvTanInt( - sqrtxz3)*pow(NC,-1)*pow(x,-1)*z*sqrtxz3*CF - 1./2.*InvTanInt( - sqrtxz3)*pow(\
      NC,-1)*sqrtxz3*CF - 5./2.*InvTanInt( - sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3*CF + 9./2.*\
      InvTanInt( - sqrtxz3)*pow(NC,-1)*x*z*sqrtxz3*CF - 3./2.*InvTanInt( - sqrtxz3)*pow(x,-1)*z*\
      sqrtxz3*CF + 3./2.*InvTanInt( - sqrtxz3)*sqrtxz3*CF + 23./2.*InvTanInt( - sqrtxz3)*pow(z,2)*\
      sqrtxz3*CF
                result +=  - 3./2.*InvTanInt( - sqrtxz3)*x*z*sqrtxz3*CF + 9*InvTanInt(z*sqrtxz3)*pow(NC,-1)*pow(\
      x,-1)*z*sqrtxz3*CF - InvTanInt(z*sqrtxz3)*pow(NC,-1)*sqrtxz3*CF - 5*InvTanInt(z*sqrtxz3)*pow(\
      NC,-1)*pow(z,2)*sqrtxz3*CF + 9*InvTanInt(z*sqrtxz3)*pow(NC,-1)*x*z*sqrtxz3*CF - 3*InvTanInt(z\
      *sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 3*InvTanInt(z*sqrtxz3)*sqrtxz3*CF + 23*InvTanInt(z*sqrtxz3\
      )*pow(z,2)*sqrtxz3*CF - 3*InvTanInt(z*sqrtxz3)*x*z*sqrtxz3*CF - 9./2.*InvTanInt(sqrtxz3)*pow(\
      NC,-1)*pow(x,-1)*z*sqrtxz3*CF + 1./2.*InvTanInt(sqrtxz3)*pow(NC,-1)*sqrtxz3*CF + 5./2.*\
      InvTanInt(sqrtxz3)*pow(NC,-1)*pow(z,2)*sqrtxz3*CF - 9./2.*InvTanInt(sqrtxz3)*pow(NC,-1)*x*z*\
      sqrtxz3*CF + 3./2.*InvTanInt(sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - 3./2.*InvTanInt(sqrtxz3)*\
      sqrtxz3*CF - 23./2.*InvTanInt(sqrtxz3)*pow(z,2)*sqrtxz3*CF + 3./2.*InvTanInt(sqrtxz3)*x*z*\
      sqrtxz3*CF + 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) - 2*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*CF + 6*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*\
      sqrtxz1*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF + 8*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*rln2*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*rln2*CF + 6*\
      ln(1 + sqrtxz1 - z)*pow(NC,-1)*sqrtxz1*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*\
      rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF - 2*ln(1 + sqrtxz1\
       - z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF
                result +=  - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*rln2*CF - 6*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*\
      sqrtxz1*CF - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*rln2*CF - 8*ln(1 + sqrtxz1 - z)*rln2*CF*\
      pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*rln2*CF - 6*ln(1 + sqrtxz1 - z)*sqrtxz1*CF*pow(omx,-1) + \
      12*ln(1 + sqrtxz1 - z)*z*rln2*CF - 24*ln(1 + sqrtxz1 - z)*pow(z,2)*rln2*CF*pow(omx,-1) + 6*\
      ln(1 + sqrtxz1 - z)*x*rln2*CF + 4*ln(1 + sqrtxz1 - z)*x*sqrtxz1*CF - 4*ln(1 + sqrtxz1 - z)*x*\
      z*rln2*CF + 24*ln(1 + sqrtxz1 - z)*x*pow(z,2)*rln2*CF + 2*pow(ln(1 + sqrtxz1 - z),2)*CF*pow(\
      omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*CF - 4*pow(ln(1 + sqrtxz1 - z),2)*z*CF*pow(omx,-1) - 4\
      *pow(ln(1 + sqrtxz1 - z),2)*z*CF + 8*pow(ln(1 + sqrtxz1 - z),2)*pow(z,2)*CF*pow(omx,-1) - 2*\
      pow(ln(1 + sqrtxz1 - z),2)*x*CF + 4*pow(ln(1 + sqrtxz1 - z),2)*x*z*CF - 8*pow(ln(1 + sqrtxz1\
       - z),2)*x*pow(z,2)*CF - 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF*\
      pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF - 8*ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1 - z)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*CF - 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*CF + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*x*z*CF
                result +=  + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*\
      ln(1 + sqrtxz1 + z)*CF + 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*z*CF*pow(omx,-1) - 4*ln(1\
       + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*z*CF + 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*pow(z,2)\
      *CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*x*CF - 4*ln(1 + sqrtxz1 - z)*ln(1\
       + sqrtxz1 + z)*x*z*CF - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*x*pow(z,2)*CF + 4*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
      z,-1)*rln2*CF + 8*ln(1 + sqrtxz1 + z)*pow(NC,-1)*rln2*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*rln2*CF + 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) - 2*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF - 4*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*rln2*CF - 4*\
      ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*z*rln2*CF - 4*ln(1 + sqrtxz1 + z)*rln2*CF*pow(omx,-1) + 2*\
      ln(1 + sqrtxz1 + z)*rln2*CF - 8*ln(1 + sqrtxz1 + z)*z*rln2*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1\
       + z)*z*rln2*CF - 8*ln(1 + sqrtxz1 + z)*pow(z,2)*rln2*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 + z)*\
      x*rln2*CF + 4*ln(1 + sqrtxz1 + z)*x*z*rln2*CF + 8*ln(1 + sqrtxz1 + z)*x*pow(z,2)*rln2*CF + 4*\
      ln(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) - 4*ln(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*\
      CF - 8*ln(x)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) + 8*ln(x)*pow(NC,-1)*pow(x,-2)*CF + 8*ln(x)*\
      pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1)
                result +=  - 8*ln(x)*pow(NC,-1)*pow(x,-2)*z*CF + 4*ln(x)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF - 3./\
      4.*ln(x)*pow(NC,-1)*pow(x,-1)*pow(poly2,-2)*CF + 7./4.*ln(x)*pow(NC,-1)*pow(x,-1)*pow(\
      poly2,-1)*CF - 9*ln(x)*pow(NC,-1)*pow(x,-1)*CF + 8*ln(x)*pow(NC,-1)*pow(x,-1)*z*CF*pow(\
      opx,-1) + 48*ln(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) - 87./2.*ln(x)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) - 16*ln(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1) - 4*ln(x)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(opx,-1) + 13*ln(x)*pow(NC,-1)*pow(z,-1)*CF - 2*ln(x)*pow(NC,-1)*pow(z,-1)*\
      rln2*CF*pow(omx,-1) + ln(x)*pow(NC,-1)*pow(z,-1)*rln2*CF - 3*ln(x)*pow(NC,-1)*pow(z,-1)*\
      sqrtxz1*CF*pow(omx,-1) + 2*ln(x)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF + 3./4.*ln(x)*pow(NC,-1)*\
      pow(poly2,-2)*CF - 5./4.*ln(x)*pow(NC,-1)*pow(poly2,-1)*CF - 36*ln(x)*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) + 3./2.*ln(x)*pow(NC,-1)*CF*pow(omx,-1)*pow(xmz,-1) - 2*ln(x)*pow(NC,-1)*\
      CF*pow(omx,-1) + 16*ln(x)*pow(NC,-1)*CF*pow(omz,-1) + 8*ln(x)*pow(NC,-1)*CF*pow(opx,-1) - 3./\
      2.*ln(x)*pow(NC,-1)*CF*pow(xmz,-1) + 3./2.*ln(x)*pow(NC,-1)*CF*pow(omxmz,-1) + 9*ln(x)*pow(\
      NC,-1)*CF - 4*ln(x)*pow(NC,-1)*rln2*CF*pow(omx,-1) + 2*ln(x)*pow(NC,-1)*rln2*CF - 3*ln(x)*\
      pow(NC,-1)*sqrtxz1*CF*pow(omx,-1) - 37./2.*ln(x)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(x)*pow(\
      NC,-1)*z*CF - 2*ln(x)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) - 32*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF*\
      pow(omz,-1)
                result +=  + 30*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF + ln(x)*pow(NC,-1)*x*pow(z,-1)*rln2*CF + ln(x)*\
      pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 3./4.*ln(x)*pow(NC,-1)*x*pow(poly2,-2)*CF + 1./2.*ln(x)*\
      pow(NC,-1)*x*pow(poly2,-1)*CF + 20*ln(x)*pow(NC,-1)*x*CF*pow(omz,-1) - 3./2.*ln(x)*pow(NC,-1)\
      *x*CF*pow(xmz,-1) - 1./2.*ln(x)*pow(NC,-1)*x*CF*pow(omxmz,-2) - 1./2.*ln(x)*pow(NC,-1)*x*CF*\
      pow(omxmz,-1) + 5*ln(x)*pow(NC,-1)*x*CF + 2*ln(x)*pow(NC,-1)*x*rln2*CF + 3*ln(x)*pow(NC,-1)*x\
      *sqrtxz1*CF + 10*ln(x)*pow(NC,-1)*x*z*CF + 2*ln(x)*pow(NC,-1)*x*z*rln2*CF - 2*ln(x)*pow(\
      NC,-1)*x*pow(z,3)*CF*pow(xmz,-2) + 3./4.*ln(x)*pow(NC,-1)*pow(x,2)*pow(poly2,-2)*CF + 1./2.*\
      ln(x)*pow(NC,-1)*pow(x,2)*pow(poly2,-1)*CF + 1./2.*ln(x)*pow(NC,-1)*pow(x,2)*CF*pow(xmz,-2)\
       + 1./2.*ln(x)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-2) + 5*ln(x)*pow(NC,-1)*pow(x,2)*CF + 3./4.*\
      ln(x)*pow(NC,-1)*pow(x,3)*pow(poly2,-2)*CF - 5./4.*ln(x)*pow(NC,-1)*pow(x,3)*pow(poly2,-1)*CF\
       - ln(x)*pow(NC,-1)*pow(x,3)*CF*pow(xmz,-2) - 9*ln(x)*pow(NC,-1)*pow(x,3)*CF*pow(xmz,-1) - 3./\
      4.*ln(x)*pow(NC,-1)*pow(x,4)*pow(poly2,-2)*CF + 7./4.*ln(x)*pow(NC,-1)*pow(x,4)*pow(poly2,-1)\
      *CF + 3*ln(x)*pow(NC,-1)*pow(x,4)*CF*pow(xmz,-2) + 3./4.*ln(x)*pow(NC,-1)*pow(x,5)*pow(\
      poly2,-2)*CF - 3./4.*ln(x)*pow(NC,-1)*pow(x,6)*pow(poly2,-2)*CF + 4*ln(x)*pow(x,-2)*CF*pow(\
      opx,-1) - 4*ln(x)*pow(x,-2)*CF - 8*ln(x)*pow(x,-2)*z*CF*pow(opx,-1) + 8*ln(x)*pow(x,-2)*z*CF\
       + 16*ln(x)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1)
                result +=  - 16*ln(x)*pow(x,-2)*pow(z,2)*CF + 4*ln(x)*pow(x,-1)*CF - 8*ln(x)*pow(x,-1)*z*CF + 16\
      *ln(x)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - 4./3.*ln(x)*pow(z,-1)*CF*pow(omx,-1) + 5./3.*ln(x)\
      *pow(z,-1)*CF - 9./2.*ln(x)*CF*pow(omx,-1) - 4*ln(x)*CF*pow(opx,-1) - 4*ln(x)*CF + 5*ln(x)*\
      rln2*CF*pow(omx,-1) + 2*ln(x)*rln2*CF + 3*ln(x)*sqrtxz1*CF*pow(omx,-1) + 11./2.*ln(x)*z*CF*\
      pow(omx,-1) + 8*ln(x)*z*CF*pow(opx,-1) + 3./2.*ln(x)*z*CF - 2*ln(x)*z*rln2*CF*pow(omx,-1) - 8\
      *ln(x)*z*rln2*CF + 4./3.*ln(x)*pow(z,2)*CF*pow(omx,-1) + 4./3.*ln(x)*pow(z,2)*CF + 16*ln(x)*\
      pow(z,2)*rln2*CF*pow(omx,-1) + 11./3.*ln(x)*x*pow(z,-1)*CF + ln(x)*x*CF*pow(xmz,-1) - 3*ln(x)\
      *x*CF - 4*ln(x)*x*rln2*CF - 2*ln(x)*x*sqrtxz1*CF + 3./2.*ln(x)*x*z*CF + 4*ln(x)*x*z*rln2*CF\
       - 8./3.*ln(x)*x*pow(z,2)*CF - 16*ln(x)*x*pow(z,2)*rln2*CF + 2*ln(x)*pow(x,2)*pow(z,-1)*CF - \
      2*ln(x)*pow(x,2)*CF*pow(xmz,-1) - 6*ln(x)*pow(x,2)*CF + 2*ln(x)*pow(x,3)*CF*pow(xmz,-1) - 6*\
      ln(x)*NC*CF*pow(omx,-1)*pow(omz,-1) - 3./2.*ln(x)*NC*CF*pow(omx,-1)*pow(xmz,-1) - 5./2.*ln(x)\
      *NC*CF*pow(omx,-1) + 3./2.*ln(x)*NC*CF*pow(xmz,-1) - 3./2.*ln(x)*NC*CF*pow(omxmz,-1) - 31./6.\
      *ln(x)*NC*CF + 5./2.*ln(x)*NC*z*CF*pow(omx,-1) - 1./2.*ln(x)*NC*z*CF + 6*ln(x)*NC*x*CF*pow(\
      omz,-1) + 3./2.*ln(x)*NC*x*CF*pow(xmz,-1) + 1./2.*ln(x)*NC*x*CF*pow(omxmz,-2) - 1./2.*ln(x)*\
      NC*x*CF*pow(omxmz,-1) + 9./2.*ln(x)*NC*x*CF + 11./6.*ln(x)*NC*x*z*CF + 1./2.*ln(x)*NC*pow(\
      x,2)*CF*pow(xmz,-2)
                result +=  + 2*ln(x)*NC*pow(x,2)*CF*pow(xmz,-1) - 1./2.*ln(x)*NC*pow(x,2)*CF*pow(omxmz,-2) - ln(\
      x)*NC*pow(x,3)*CF*pow(xmz,-2) - ln(x)*NC*pow(x,3)*CF*pow(xmz,-1) + ln(x)*NC*pow(x,4)*CF*pow(\
      xmz,-2) + ln(x)*NF*CF*pow(omx,-1) - 4./3.*ln(x)*NF*CF + ln(x)*NF*z*CF*pow(omx,-1) - 4./3.*ln(\
      x)*NF*x*z*CF - 3./8.*ln(x)*ln(1 - sqrtxz2 + x)*\
      pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF + ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*\
      pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 5./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(\
      x,-1)*pow(sqrtxz2,-1)*CF
                result +=  - 3*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1)*CF + 3*ln(x)*ln(1\
       - sqrtxz2 + x)*pow(NC,-1)*pow(sqrtxz2,-1)*CF*pow(omz,-1) + 9./2.*ln(x)*ln(1 - sqrtxz2 + x)*\
      pow(NC,-1)*pow(sqrtxz2,-1)*CF - 9*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*z*pow(sqrtxz2,-1)*CF\
       - 2*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1)*CF - 2*ln(x)*ln(1 - \
      sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF*pow(omz,-1) + 51./4.*ln(x)*ln(1 - sqrtxz2 + x)*\
      pow(NC,-1)*x*pow(sqrtxz2,-1)*CF - 18*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*x*z*pow(sqrtxz2,-1)\
      *CF + 18*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 3*ln(x)*ln(1 - \
      sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1)*CF + 3*ln(x)*ln(1 - sqrtxz2 + x)*\
      pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*CF*pow(omz,-1) + 9./2.*ln(x)*ln(1 - sqrtxz2 + x)*pow(\
      NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*CF - 9*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz2,-1)*CF + 3./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(\
      poly2,-2)*CF - 5./8.*ln(x)*ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*CF + ln(x)\
      *ln(1 - sqrtxz2 + x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 3./8.*ln(x)*ln(1\
       - sqrtxz2 + x)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF - 4*ln(x)*ln(1 - sqrtxz2\
       + x)*pow(sqrtxz2,-1)*CF + 8*ln(x)*ln(1 - sqrtxz2 + x)*z*pow(sqrtxz2,-1)*CF - 2*ln(x)*ln(1 - \
      sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF
                result +=  + 16*ln(x)*ln(1 - sqrtxz2 + x)*x*z*pow(sqrtxz2,-1)*CF - 16*ln(x)*ln(1 - sqrtxz2 + x)*\
      x*pow(z,2)*pow(sqrtxz2,-1)*CF - 4*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,2)*pow(sqrtxz2,-1)*CF + 8*\
      ln(x)*ln(1 - sqrtxz2 + x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 3./8.*ln(x)*ln(1 + sqrtxz2 + x)*\
      pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF - ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*\
      pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 5./8.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(\
      x,-1)*pow(sqrtxz2,-1)*CF + 3*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1)*\
      CF - 3*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(sqrtxz2,-1)*CF*pow(omz,-1) - 9./2.*ln(x)*ln(1\
       + sqrtxz2 + x)*pow(NC,-1)*pow(sqrtxz2,-1)*CF + 9*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*z*pow(\
      sqrtxz2,-1)*CF + 2*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1)*CF + 2*\
      ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF*pow(omz,-1) - 51./4.*ln(x)*ln(1 + \
      sqrtxz2 + x)*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF + 18*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*z*\
      pow(sqrtxz2,-1)*CF - 18*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + \
      3*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1)*CF - 3*ln(x)*ln(1\
       + sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*CF*pow(omz,-1) - 9./2.*ln(x)*ln(1 + \
      sqrtxz2 + x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*CF + 9*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*\
      pow(x,2)*z*pow(sqrtxz2,-1)*CF
                result +=  - 3./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-2)*\
      CF + 5./8.*ln(x)*ln(1 + sqrtxz2 + x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*CF - ln(x)*ln(1 + \
      sqrtxz2 + x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 3./8.*ln(x)*ln(1 + \
      sqrtxz2 + x)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF + 4*ln(x)*ln(1 + sqrtxz2 + \
      x)*pow(sqrtxz2,-1)*CF - 8*ln(x)*ln(1 + sqrtxz2 + x)*z*pow(sqrtxz2,-1)*CF + 2*ln(x)*ln(1 + \
      sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF - 16*ln(x)*ln(1 + sqrtxz2 + x)*x*z*pow(sqrtxz2,-1)*CF + 16*\
      ln(x)*ln(1 + sqrtxz2 + x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 4*ln(x)*ln(1 + sqrtxz2 + x)*pow(\
      x,2)*pow(sqrtxz2,-1)*CF - 8*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 2*ln(x)\
      *ln(1 + sqrtxz1 - z)*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 - z)*CF + 4*ln(x)*ln(1 + sqrtxz1\
       - z)*z*CF*pow(omx,-1) + 4*ln(x)*ln(1 + sqrtxz1 - z)*z*CF - 8*ln(x)*ln(1 + sqrtxz1 - z)*pow(\
      z,2)*CF*pow(omx,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*x*CF - 4*ln(x)*ln(1 + sqrtxz1 - z)*x*z*CF\
       + 8*ln(x)*ln(1 + sqrtxz1 - z)*x*pow(z,2)*CF + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) - ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(x)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*CF + 2*ln(x)*\
      ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*pow(\
      z,-1)*CF
                result +=  - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*CF - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(\
      NC,-1)*x*z*CF - 3*ln(x)*ln(1 + sqrtxz1 + z)*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*z*CF\
      *pow(omx,-1) + 4*ln(x)*ln(1 + sqrtxz1 + z)*z*CF - 8*ln(x)*ln(1 + sqrtxz1 + z)*pow(z,2)*CF*\
      pow(omx,-1) + 2*ln(x)*ln(1 + sqrtxz1 + z)*x*CF + 8*ln(x)*ln(1 + sqrtxz1 + z)*x*pow(z,2)*CF - \
      ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + ln(x)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*\
      CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF - 2*ln(x)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(\
      x,-2)*z*CF - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF + 2*ln(x)*ln(1 + x*\
      pow(z,-1))*pow(NC,-1)*pow(x,-1)*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*z*CF*\
      pow(opx,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + ln(x)*ln(1 + x*\
      pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*CF*pow(opx,-1) - \
      2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*z*CF*pow(\
      opx,-1) - ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*\
      pow(NC,-1)*x*CF - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*z*CF - ln(x)*ln(1 + x*pow(z,-1))*\
      pow(x,-2)*CF*pow(opx,-1)
                result +=  + ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*z*CF\
      *pow(opx,-1) - 2*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*z*CF - 4*ln(x)*ln(1 + x*pow(z,-1))*pow(\
      x,-2)*pow(z,2)*CF*pow(opx,-1) + 4*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF - ln(x)*ln(\
      1 + x*pow(z,-1))*pow(x,-1)*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-1)*z*CF - 4*ln(x)*ln(1 + x\
      *pow(z,-1))*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - ln(x)*ln(1 + x*pow(z,-1))*CF*pow(opx,-1) + \
      ln(x)*ln(1 + x*pow(z,-1))*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*z*CF*pow(opx,-1) - 2*ln(x)*ln(1 + \
      x*pow(z,-1))*z*CF - 4*ln(x)*ln(1 + x*pow(z,-1))*pow(z,2)*CF*pow(opx,-1) - ln(x)*ln(1 + x*pow(\
      z,-1))*x*CF + 2*ln(x)*ln(1 + x*pow(z,-1))*x*z*CF - 4*ln(x)*ln(1 + x*pow(z,-1))*x*pow(z,2)*CF\
       - 4*ln(x)*ln(1 + x)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 8*ln(x)*ln(1 + x)*pow(NC,-1)*CF*\
      pow(opx,-1) - 4*ln(x)*ln(1 + x)*pow(NC,-1)*z*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x)*pow(NC,-1)*x*\
      pow(z,-1)*CF + 8*ln(x)*ln(1 + x)*pow(NC,-1)*x*CF - 4*ln(x)*ln(1 + x)*pow(NC,-1)*x*z*CF - 4*\
      ln(x)*ln(1 + x)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x)*CF + 8*ln(x)*ln(1 + x)*z*CF*pow(opx,-1) + \
      4*ln(x)*ln(1 + x)*z*CF - 8*ln(x)*ln(1 + x)*pow(z,2)*CF*pow(opx,-1) - 6*ln(x)*ln(1 + x)*x*CF\
       + 12*ln(x)*ln(1 + x)*x*z*CF - 8*ln(x)*ln(1 + x)*x*pow(z,2)*CF - ln(x)*ln(1 + x*z)*pow(NC,-1)\
      *pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 2\
      *ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1)
                result +=  - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*CF - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(\
      x,-2)*z*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z*CF - ln(x)*ln(1 + x*z)*\
      pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF + 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*CF - 2*ln(x)*ln(\
      1 + x*z)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF*\
      pow(omx,-1) - ln(x)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(x)*ln(1 + x*z)*\
      pow(NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln(1 + x*z)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x)*ln(1 + x*z)\
      *pow(NC,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*ln(x)*ln(1\
       + x*z)*pow(NC,-1)*z*CF*pow(opx,-1) + 4*ln(x)*ln(1 + x*z)*pow(NC,-1)*x*CF - ln(x)*ln(1 + x*z)\
      *pow(x,-2)*CF*pow(opx,-1) + ln(x)*ln(1 + x*z)*pow(x,-2)*CF + 2*ln(x)*ln(1 + x*z)*pow(x,-2)*z*\
      CF*pow(opx,-1) - 2*ln(x)*ln(1 + x*z)*pow(x,-2)*z*CF - 4*ln(x)*ln(1 + x*z)*pow(x,-2)*pow(z,2)*\
      CF*pow(opx,-1) + 4*ln(x)*ln(1 + x*z)*pow(x,-2)*pow(z,2)*CF - ln(x)*ln(1 + x*z)*pow(x,-1)*CF\
       + 2*ln(x)*ln(1 + x*z)*pow(x,-1)*z*CF - 4*ln(x)*ln(1 + x*z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1)\
       + 2*ln(x)*ln(1 + x*z)*CF*pow(omx,-1) - ln(x)*ln(1 + x*z)*CF*pow(opx,-1) + 4*ln(x)*ln(1 + x*z\
      )*z*CF*pow(omx,-1) + 2*ln(x)*ln(1 + x*z)*z*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x*z)*z*CF + 4*ln(x\
      )*ln(1 + x*z)*pow(z,2)*CF*pow(omx,-1) - 4*ln(x)*ln(1 + x*z)*pow(z,2)*CF*pow(opx,-1) - 2*ln(x)\
      *ln(1 + x*z)*x*CF
                result +=  - 8*ln(x)*ln(1 + x*z)*x*pow(z,2)*CF + 2*ln(x)*ln(z + x)*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) - ln(x)*ln(z + x)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(x)*ln(z + x)*pow(NC,-1)*CF*pow(\
      omx,-1) - 2*ln(x)*ln(z + x)*pow(NC,-1)*CF + 2*ln(x)*ln(z + x)*pow(NC,-1)*z*CF*pow(omx,-1) - \
      ln(x)*ln(z + x)*pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(x)*ln(z + x)*pow(NC,-1)*x*CF - 2*ln(x)*ln(z\
       + x)*pow(NC,-1)*x*z*CF - 2*ln(x)*ln(z + x)*CF*pow(omx,-1) + ln(x)*ln(z + x)*CF - 4*ln(x)*ln(\
      z + x)*z*CF*pow(omx,-1) + 2*ln(x)*ln(z + x)*z*CF - 4*ln(x)*ln(z + x)*pow(z,2)*CF*pow(omx,-1)\
       + ln(x)*ln(z + x)*x*CF + 2*ln(x)*ln(z + x)*x*z*CF + 4*ln(x)*ln(z + x)*x*pow(z,2)*CF - 3./2.*\
      pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + 3./2.*pow(ln(x),2)*pow(NC,-1)*\
      pow(x,-2)*pow(z,-1)*CF + 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 3*pow(ln(x),2)*\
      pow(NC,-1)*pow(x,-2)*CF - 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 3*pow(ln(x),\
      2)*pow(NC,-1)*pow(x,-2)*z*CF - 3./2.*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF + 3*pow(\
      ln(x),2)*pow(NC,-1)*pow(x,-1)*CF - 3*pow(ln(x),2)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) - 16*\
      pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) + 16*pow(ln(x),2)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) + 5*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1) + 5./2.*pow(ln(\
      x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 5*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF - pow(ln(x\
      ),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)
                result +=  + 13*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) - 1./2.*pow(ln(x),2)*pow(NC,-1)*CF*pow(\
      omz,-1) - 5*pow(ln(x),2)*pow(NC,-1)*CF*pow(opx,-1) - 17./2.*pow(ln(x),2)*pow(NC,-1)*CF + 13*\
      pow(ln(x),2)*pow(NC,-1)*z*CF*pow(omx,-1) + pow(ln(x),2)*pow(NC,-1)*z*CF*pow(opx,-1) - 1./2.*\
      pow(ln(x),2)*pow(NC,-1)*z*CF + 11*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 10*\
      pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF + 3./2.*pow(ln(x),2)*pow(NC,-1)*x*CF*pow(omz,-1) - 21./\
      2.*pow(ln(x),2)*pow(NC,-1)*x*CF - 31./2.*pow(ln(x),2)*pow(NC,-1)*x*z*CF - 3./2.*pow(ln(x),2)*\
      pow(x,-2)*CF*pow(opx,-1) + 3./2.*pow(ln(x),2)*pow(x,-2)*CF + 3*pow(ln(x),2)*pow(x,-2)*z*CF*\
      pow(opx,-1) - 3*pow(ln(x),2)*pow(x,-2)*z*CF - 6*pow(ln(x),2)*pow(x,-2)*pow(z,2)*CF*pow(\
      opx,-1) + 6*pow(ln(x),2)*pow(x,-2)*pow(z,2)*CF - 3./2.*pow(ln(x),2)*pow(x,-1)*CF + 3*pow(ln(x\
      ),2)*pow(x,-1)*z*CF - 6*pow(ln(x),2)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - pow(ln(x),2)*pow(\
      z,-1)*CF - 2*pow(ln(x),2)*CF*pow(omx,-1) + 5./2.*pow(ln(x),2)*CF*pow(opx,-1) + 4*pow(ln(x),2)\
      *CF + 4*pow(ln(x),2)*z*CF*pow(omx,-1) - 5*pow(ln(x),2)*z*CF*pow(opx,-1) - 4*pow(ln(x),2)*z*CF\
       - 2*pow(ln(x),2)*pow(z,2)*CF*pow(omx,-1) + 2*pow(ln(x),2)*pow(z,2)*CF*pow(opx,-1) - pow(ln(x\
      ),2)*x*pow(z,-1)*CF + 5*pow(ln(x),2)*x*CF - 6*pow(ln(x),2)*x*z*CF + 4*pow(ln(x),2)*x*pow(z,2)\
      *CF + 8*pow(ln(x),2)*NC*CF*pow(omx,-1)*pow(omz,-1) - 5*pow(ln(x),2)*NC*CF*pow(omx,-1) - 4*\
      pow(ln(x),2)*NC*CF*pow(omz,-1)
                result +=  + 17./2.*pow(ln(x),2)*NC*CF - 5*pow(ln(x),2)*NC*z*CF*pow(omx,-1) + 1./2.*pow(ln(x),2)\
      *NC*z*CF - 4*pow(ln(x),2)*NC*x*CF*pow(omz,-1) + 1./2.*pow(ln(x),2)*NC*x*CF + 17./2.*pow(ln(x)\
      ,2)*NC*x*z*CF + ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) - ln(x)*ln(z)*pow(\
      NC,-1)*pow(x,-2)*pow(z,-1)*CF - 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) + 2*ln(x)*\
      ln(z)*pow(NC,-1)*pow(x,-2)*CF + 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) - 2*ln(x)\
      *ln(z)*pow(NC,-1)*pow(x,-2)*z*CF + ln(x)*ln(z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF - 2*ln(x)*\
      ln(z)*pow(NC,-1)*pow(x,-1)*CF + 2*ln(x)*ln(z)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + 16*ln(x\
      )*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) - 16*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)\
      *CF*pow(omx,-1) - 6*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1) + ln(x)*ln(z)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(opx,-1) + 6*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(x)*ln(z)*pow(NC,-1)*\
      CF*pow(omx,-1)*pow(omz,-1) - 23./2.*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(x)*ln(z)*\
      pow(NC,-1)*CF*pow(opx,-1) + 9*ln(x)*ln(z)*pow(NC,-1)*CF - 27./2.*ln(x)*ln(z)*pow(NC,-1)*z*CF*\
      pow(omx,-1) + 2*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(opx,-1) - 10*ln(x)*ln(z)*pow(NC,-1)*x*pow(\
      z,-1)*CF*pow(omz,-1) + 12*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF - 4*ln(x)*ln(z)*pow(NC,-1)*x*\
      CF*pow(omz,-1) + 4*ln(x)*ln(z)*pow(NC,-1)*x*CF + 19*ln(x)*ln(z)*pow(NC,-1)*x*z*CF + ln(x)*ln(\
      z)*pow(x,-2)*CF*pow(opx,-1)
                result +=  - ln(x)*ln(z)*pow(x,-2)*CF - 2*ln(x)*ln(z)*pow(x,-2)*z*CF*pow(opx,-1) + 2*ln(x)*ln(z)\
      *pow(x,-2)*z*CF + 4*ln(x)*ln(z)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 4*ln(x)*ln(z)*pow(x,-2)*\
      pow(z,2)*CF + ln(x)*ln(z)*pow(x,-1)*CF - 2*ln(x)*ln(z)*pow(x,-1)*z*CF + 4*ln(x)*ln(z)*pow(\
      x,-1)*pow(z,2)*CF*pow(opx,-1) + ln(x)*ln(z)*pow(z,-1)*CF + ln(x)*ln(z)*CF*pow(omx,-1) + ln(x)\
      *ln(z)*CF*pow(opx,-1) + 2*ln(x)*ln(z)*CF - 7*ln(x)*ln(z)*z*CF*pow(omx,-1) - 2*ln(x)*ln(z)*z*\
      CF*pow(opx,-1) - 2*ln(x)*ln(z)*z*CF + 8*ln(x)*ln(z)*pow(z,2)*CF*pow(omx,-1) + 4*ln(x)*ln(z)*\
      pow(z,2)*CF*pow(opx,-1) + ln(x)*ln(z)*x*pow(z,-1)*CF + 6*ln(x)*ln(z)*x*z*CF - 4*ln(x)*ln(z)*x\
      *pow(z,2)*CF - 8*ln(x)*ln(z)*NC*CF*pow(omx,-1)*pow(omz,-1) + 7./2.*ln(x)*ln(z)*NC*CF*pow(\
      omx,-1) + 4*ln(x)*ln(z)*NC*CF*pow(omz,-1) - 5*ln(x)*ln(z)*NC*CF + 7./2.*ln(x)*ln(z)*NC*z*CF*\
      pow(omx,-1) + 4*ln(x)*ln(z)*NC*x*CF*pow(omz,-1) - 5*ln(x)*ln(z)*NC*x*z*CF - 2*ln(x)*ln(omx)*\
      pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*pow(\
      z,-1)*CF + 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 4*ln(x)*ln(omx)*pow(NC,-1)*\
      pow(x,-2)*CF - 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 4*ln(x)*ln(omx)*pow(\
      NC,-1)*pow(x,-2)*z*CF - 2*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF + 4*ln(x)*ln(omx)*\
      pow(NC,-1)*pow(x,-1)*CF - 4*ln(x)*ln(omx)*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) - 8*ln(x)*ln(\
      omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1)
                result +=  + 8*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 4*ln(x)*ln(omx)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omz,-1) + 2*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 4*ln(x)*ln(\
      omx)*pow(NC,-1)*pow(z,-1)*CF + 28*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 17*\
      ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) - 7*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) - 4*ln(x)\
      *ln(omx)*pow(NC,-1)*CF*pow(opx,-1) + 9*ln(x)*ln(omx)*pow(NC,-1)*CF - 17*ln(x)*ln(omx)*pow(\
      NC,-1)*z*CF*pow(omx,-1) + ln(x)*ln(omx)*pow(NC,-1)*z*CF + 4*ln(x)*ln(omx)*pow(NC,-1)*x*pow(\
      z,-1)*CF*pow(omz,-1) - 4*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 21*ln(x)*ln(omx)*pow(\
      NC,-1)*x*CF*pow(omz,-1) + 15*ln(x)*ln(omx)*pow(NC,-1)*x*CF + 23*ln(x)*ln(omx)*pow(NC,-1)*x*z*\
      CF - 2*ln(x)*ln(omx)*pow(x,-2)*CF*pow(opx,-1) + 2*ln(x)*ln(omx)*pow(x,-2)*CF + 4*ln(x)*ln(omx\
      )*pow(x,-2)*z*CF*pow(opx,-1) - 4*ln(x)*ln(omx)*pow(x,-2)*z*CF - 8*ln(x)*ln(omx)*pow(x,-2)*\
      pow(z,2)*CF*pow(opx,-1) + 8*ln(x)*ln(omx)*pow(x,-2)*pow(z,2)*CF - 2*ln(x)*ln(omx)*pow(x,-1)*\
      CF + 4*ln(x)*ln(omx)*pow(x,-1)*z*CF - 8*ln(x)*ln(omx)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 3*\
      ln(x)*ln(omx)*CF*pow(omx,-1) + 2*ln(x)*ln(omx)*CF*pow(opx,-1) - 6*ln(x)*ln(omx)*z*CF*pow(\
      omx,-1) - 4*ln(x)*ln(omx)*z*CF*pow(opx,-1) + 8*ln(x)*ln(omx)*pow(z,2)*CF*pow(omx,-1) - 2*ln(x\
      )*ln(omx)*x*CF + 4*ln(x)*ln(omx)*x*z*CF - 8*ln(x)*ln(omx)*x*pow(z,2)*CF - 10*ln(x)*ln(omx)*NC\
      *CF*pow(omx,-1)*pow(omz,-1)
                result +=  + 8*ln(x)*ln(omx)*NC*CF*pow(omx,-1) + 5*ln(x)*ln(omx)*NC*CF*pow(omz,-1) - 13*ln(x)*\
      ln(omx)*NC*CF + 8*ln(x)*ln(omx)*NC*z*CF*pow(omx,-1) - ln(x)*ln(omx)*NC*z*CF + 5*ln(x)*ln(omx)\
      *NC*x*CF*pow(omz,-1) - ln(x)*ln(omx)*NC*x*CF - 13*ln(x)*ln(omx)*NC*x*z*CF + 18*ln(x)*ln(omz)*\
      pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 16*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 6*ln(x)*\
      ln(omz)*pow(NC,-1)*CF*pow(omz,-1) + 14*ln(x)*ln(omz)*pow(NC,-1)*CF - 16*ln(x)*ln(omz)*pow(\
      NC,-1)*z*CF*pow(omx,-1) + ln(x)*ln(omz)*pow(NC,-1)*z*CF - 12*ln(x)*ln(omz)*pow(NC,-1)*x*CF*\
      pow(omz,-1) + 7*ln(x)*ln(omz)*pow(NC,-1)*x*CF + 20*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + ln(x)*\
      ln(omz)*pow(z,-1)*CF - 2*ln(x)*ln(omz)*CF + ln(x)*ln(omz)*x*pow(z,-1)*CF - 2*ln(x)*ln(omz)*x*\
      CF - 12*ln(x)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) + 8*ln(x)*ln(omz)*NC*CF*pow(omx,-1) + 6*\
      ln(x)*ln(omz)*NC*CF*pow(omz,-1) - 14*ln(x)*ln(omz)*NC*CF + 8*ln(x)*ln(omz)*NC*z*CF*pow(\
      omx,-1) - ln(x)*ln(omz)*NC*z*CF + 6*ln(x)*ln(omz)*NC*x*CF*pow(omz,-1) - ln(x)*ln(omz)*NC*x*CF\
       - 14*ln(x)*ln(omz)*NC*x*z*CF + 2*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1)\
       - 2*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*\
      CF*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*CF + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(\
      x,-2)*z*CF*pow(opx,-1) - 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-2)*z*CF + 2*ln(x)*ln(opx)*pow(\
      NC,-1)*pow(x,-1)*pow(z,-1)*CF
                result +=  - 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*CF + 4*ln(x)*ln(opx)*pow(NC,-1)*pow(x,-1)*z*CF\
      *pow(opx,-1) + 2*ln(x)*ln(opx)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 2*ln(x)*ln(opx)*pow(\
      NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln(opx)*pow(NC,-1)*CF*pow(opx,-1) + 4*ln(x)*ln(opx)*pow(NC,-1)*\
      CF + 4*ln(x)*ln(opx)*pow(NC,-1)*z*CF*pow(opx,-1) + 2*ln(x)*ln(opx)*pow(NC,-1)*x*pow(z,-1)*CF\
       - 4*ln(x)*ln(opx)*pow(NC,-1)*x*CF + 4*ln(x)*ln(opx)*pow(NC,-1)*x*z*CF + 2*ln(x)*ln(opx)*pow(\
      x,-2)*CF*pow(opx,-1) - 2*ln(x)*ln(opx)*pow(x,-2)*CF - 4*ln(x)*ln(opx)*pow(x,-2)*z*CF*pow(\
      opx,-1) + 4*ln(x)*ln(opx)*pow(x,-2)*z*CF + 8*ln(x)*ln(opx)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1)\
       - 8*ln(x)*ln(opx)*pow(x,-2)*pow(z,2)*CF + 2*ln(x)*ln(opx)*pow(x,-1)*CF - 4*ln(x)*ln(opx)*\
      pow(x,-1)*z*CF + 8*ln(x)*ln(opx)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 2*ln(x)*ln(opx)*CF*pow(\
      opx,-1) - 2*ln(x)*ln(opx)*CF - 4*ln(x)*ln(opx)*z*CF*pow(opx,-1) + 4*ln(x)*ln(opx)*z*CF + 8*\
      ln(x)*ln(opx)*pow(z,2)*CF*pow(opx,-1) + 2*ln(x)*ln(opx)*x*CF - 4*ln(x)*ln(opx)*x*z*CF + 8*ln(\
      x)*ln(opx)*x*pow(z,2)*CF - 3./4.*ln(z)*pow(NC,-1)*pow(x,-1)*pow(poly2,-2)*CF + 7./4.*ln(z)*\
      pow(NC,-1)*pow(x,-1)*pow(poly2,-1)*CF - ln(z)*pow(NC,-1)*pow(x,-1)*CF - 24*ln(z)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) + 27*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 8*ln(z)\
      *pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1) - 10*ln(z)*pow(NC,-1)*pow(z,-1)*CF - 6*ln(z)*pow(NC,-1)*\
      pow(z,-1)*rln2*CF*pow(omx,-1)
                result +=  + 3*ln(z)*pow(NC,-1)*pow(z,-1)*rln2*CF - 3*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(\
      omx,-1) + 2*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF - 3./4.*ln(z)*pow(NC,-1)*pow(poly2,-2)*CF\
       + 5./4.*ln(z)*pow(NC,-1)*pow(poly2,-1)*CF + 35./2.*ln(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) - 3./2.*ln(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(xmz,-1) + 6*ln(z)*pow(NC,-1)*CF*pow(\
      omx,-1) - 8*ln(z)*pow(NC,-1)*CF*pow(omz,-1) + 3./2.*ln(z)*pow(NC,-1)*CF*pow(xmz,-1) + 11./2.*\
      ln(z)*pow(NC,-1)*CF - 12*ln(z)*pow(NC,-1)*rln2*CF*pow(omx,-1) + 6*ln(z)*pow(NC,-1)*rln2*CF - \
      3*ln(z)*pow(NC,-1)*sqrtxz1*CF*pow(omx,-1) + 11*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 7./2.*ln(z\
      )*pow(NC,-1)*z*CF - 6*ln(z)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) + 16*ln(z)*pow(NC,-1)*x*pow(\
      z,-1)*CF*pow(omz,-1) - 17*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 3*ln(z)*pow(NC,-1)*x*pow(z,-1)*\
      rln2*CF + ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 3./4.*ln(z)*pow(NC,-1)*x*pow(poly2,-2)*CF\
       + 1./2.*ln(z)*pow(NC,-1)*x*pow(poly2,-1)*CF - 8*ln(z)*pow(NC,-1)*x*CF*pow(omz,-1) + 3./2.*\
      ln(z)*pow(NC,-1)*x*CF*pow(xmz,-1) - 23./2.*ln(z)*pow(NC,-1)*x*CF + 6*ln(z)*pow(NC,-1)*x*rln2*\
      CF + 3*ln(z)*pow(NC,-1)*x*sqrtxz1*CF - 25./2.*ln(z)*pow(NC,-1)*x*z*CF + 6*ln(z)*pow(NC,-1)*x*\
      z*rln2*CF + 2*ln(z)*pow(NC,-1)*x*pow(z,3)*CF*pow(xmz,-2) - 3./4.*ln(z)*pow(NC,-1)*pow(x,2)*\
      pow(poly2,-2)*CF - 1./2.*ln(z)*pow(NC,-1)*pow(x,2)*pow(poly2,-1)*CF - 1./2.*ln(z)*pow(NC,-1)*\
      pow(x,2)*CF*pow(xmz,-2)
                result +=  - 5*ln(z)*pow(NC,-1)*pow(x,2)*CF + 3./4.*ln(z)*pow(NC,-1)*pow(x,3)*pow(poly2,-2)*CF\
       - 5./4.*ln(z)*pow(NC,-1)*pow(x,3)*pow(poly2,-1)*CF + ln(z)*pow(NC,-1)*pow(x,3)*CF*pow(\
      xmz,-2) + 9*ln(z)*pow(NC,-1)*pow(x,3)*CF*pow(xmz,-1) + 3./4.*ln(z)*pow(NC,-1)*pow(x,4)*pow(\
      poly2,-2)*CF - 7./4.*ln(z)*pow(NC,-1)*pow(x,4)*pow(poly2,-1)*CF - 3*ln(z)*pow(NC,-1)*pow(x,4)\
      *CF*pow(xmz,-2) + 3./4.*ln(z)*pow(NC,-1)*pow(x,5)*pow(poly2,-2)*CF + 3./4.*ln(z)*pow(NC,-1)*\
      pow(x,6)*pow(poly2,-2)*CF + 2./3.*ln(z)*pow(x,-1)*pow(z,-1)*CF + 2./3.*ln(z)*pow(x,-1)*CF*\
      pow(omz,-1) - 4./3.*ln(z)*pow(x,-1)*CF + 1./6.*ln(z)*pow(z,-1)*CF - 3*ln(z)*CF*pow(omx,-1) - \
      ln(z)*CF*pow(omz,-1) + 3./2.*ln(z)*CF + 7*ln(z)*rln2*CF*pow(omx,-1) - 2*ln(z)*rln2*CF + 3*ln(\
      z)*sqrtxz1*CF*pow(omx,-1) - 3*ln(z)*z*CF*pow(omx,-1) + 4*ln(z)*z*CF + 10*ln(z)*z*rln2*CF*pow(\
      omx,-1) - 8*ln(z)*z*rln2*CF - 2./3.*ln(z)*pow(z,2)*CF + 16*ln(z)*pow(z,2)*rln2*CF*pow(omx,-1)\
       - 5./6.*ln(z)*x*pow(z,-1)*CF + ln(z)*x*CF*pow(omz,-1) - ln(z)*x*CF*pow(xmz,-1) + 1./2.*ln(z)\
      *x*CF - 4*ln(z)*x*rln2*CF - 2*ln(z)*x*sqrtxz1*CF + ln(z)*x*z*CF - 4*ln(z)*x*z*rln2*CF + 4./3.\
      *ln(z)*x*pow(z,2)*CF - 16*ln(z)*x*pow(z,2)*rln2*CF - 2./3.*ln(z)*pow(x,2)*pow(z,-1)*CF - 2./3.\
      *ln(z)*pow(x,2)*CF*pow(omz,-1) + 2*ln(z)*pow(x,2)*CF*pow(xmz,-1) + 10./3.*ln(z)*pow(x,2)*CF\
       - 2*ln(z)*pow(x,3)*CF*pow(xmz,-1) + 1./2.*ln(z)*NC*CF*pow(omx,-1)*pow(omz,-1) + 3./2.*ln(z)*\
      NC*CF*pow(omx,-1)*pow(xmz,-1)
                result +=  + ln(z)*NC*CF*pow(omz,-1) - 3./2.*ln(z)*NC*CF*pow(xmz,-1) + 4*ln(z)*NC*CF - 2*ln(z)*\
      NC*z*CF*pow(omx,-1) - ln(z)*NC*z*CF - 3*ln(z)*NC*x*CF*pow(omz,-1) - 3./2.*ln(z)*NC*x*CF*pow(\
      xmz,-1) + ln(z)*NC*x*CF + 6*ln(z)*NC*x*z*CF - 1./2.*ln(z)*NC*pow(x,2)*CF*pow(xmz,-2) - 2*ln(z\
      )*NC*pow(x,2)*CF*pow(xmz,-1) + ln(z)*NC*pow(x,3)*CF*pow(xmz,-2) + ln(z)*NC*pow(x,3)*CF*pow(\
      xmz,-1) - ln(z)*NC*pow(x,4)*CF*pow(xmz,-2) + 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(z)\
      *ln(1 + sqrtxz1 - z)*pow(NC,-1)*CF*pow(omx,-1)
                result +=  - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*CF + 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*\
      z*CF*pow(omx,-1) - ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(z)*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*x*CF - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*z*CF - 3*ln(z)*ln(1\
       + sqrtxz1 - z)*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 - z)*z*CF*pow(omx,-1) + 4*ln(z)*ln(1\
       + sqrtxz1 - z)*z*CF - 8*ln(z)*ln(1 + sqrtxz1 - z)*pow(z,2)*CF*pow(omx,-1) + 2*ln(z)*ln(1 + \
      sqrtxz1 - z)*x*CF + 8*ln(z)*ln(1 + sqrtxz1 - z)*x*pow(z,2)*CF + 4*ln(z)*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF + 8\
      *ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*CF*pow(omx,-1) - 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)\
      *CF + 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*\
      pow(NC,-1)*x*pow(z,-1)*CF - 4*ln(z)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*CF - 4*ln(z)*ln(1 + \
      sqrtxz1 + z)*pow(NC,-1)*x*z*CF - 4*ln(z)*ln(1 + sqrtxz1 + z)*CF*pow(omx,-1) + 2*ln(z)*ln(1 + \
      sqrtxz1 + z)*CF - 8*ln(z)*ln(1 + sqrtxz1 + z)*z*CF*pow(omx,-1) + 4*ln(z)*ln(1 + sqrtxz1 + z)*\
      z*CF - 8*ln(z)*ln(1 + sqrtxz1 + z)*pow(z,2)*CF*pow(omx,-1) + 2*ln(z)*ln(1 + sqrtxz1 + z)*x*CF\
       + 4*ln(z)*ln(1 + sqrtxz1 + z)*x*z*CF + 8*ln(z)*ln(1 + sqrtxz1 + z)*x*pow(z,2)*CF + ln(z)*ln(\
      1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*\
      pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF
                result +=  - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*\
      pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z*CF*\
      pow(opx,-1) - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z*CF + ln(z)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*\
      CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) + ln(z)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*\
      CF - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(\
      NC,-1)*CF + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*z*CF*pow(opx,-1) + ln(z)*ln(1 + x*pow(\
      z,-1))*pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(NC,-1)*x*CF + 2*ln(z)*ln(1\
       + x*pow(z,-1))*pow(NC,-1)*x*z*CF + ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*CF*pow(opx,-1) - ln(z\
      )*ln(1 + x*pow(z,-1))*pow(x,-2)*CF - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*z*CF*pow(opx,-1)\
       + 2*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*z*CF + 4*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*pow(\
      z,2)*CF*pow(opx,-1) - 4*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF + ln(z)*ln(1 + x*pow(\
      z,-1))*pow(x,-1)*CF - 2*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-1)*z*CF + 4*ln(z)*ln(1 + x*pow(z,-1)\
      )*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*CF*pow(opx,-1) - ln(z)*ln(1\
       + x*pow(z,-1))*CF
                result +=  - 2*ln(z)*ln(1 + x*pow(z,-1))*z*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*pow(z,-1))*z*CF + 4\
      *ln(z)*ln(1 + x*pow(z,-1))*pow(z,2)*CF*pow(opx,-1) + ln(z)*ln(1 + x*pow(z,-1))*x*CF - 2*ln(z)\
      *ln(1 + x*pow(z,-1))*x*z*CF + 4*ln(z)*ln(1 + x*pow(z,-1))*x*pow(z,2)*CF - ln(z)*ln(1 + x*z)*\
      pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*pow(\
      z,-1)*CF + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(\
      NC,-1)*pow(x,-2)*CF - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 2*ln(z)*ln(\
      1 + x*z)*pow(NC,-1)*pow(x,-2)*z*CF - ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF + 2*\
      ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*CF - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(x,-1)*z*CF*\
      pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(z)*ln(1 + x*z)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(z)*\
      ln(1 + x*z)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*CF*pow(opx,-1) - 2*ln(\
      z)*ln(1 + x*z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*ln(z)*ln(1 + x*z)*pow(NC,-1)*z*CF*pow(opx,-1)\
       + 4*ln(z)*ln(1 + x*z)*pow(NC,-1)*x*CF - ln(z)*ln(1 + x*z)*pow(x,-2)*CF*pow(opx,-1) + ln(z)*\
      ln(1 + x*z)*pow(x,-2)*CF + 2*ln(z)*ln(1 + x*z)*pow(x,-2)*z*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*\
      z)*pow(x,-2)*z*CF - 4*ln(z)*ln(1 + x*z)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) + 4*ln(z)*ln(1 + x*\
      z)*pow(x,-2)*pow(z,2)*CF
                result +=  - ln(z)*ln(1 + x*z)*pow(x,-1)*CF + 2*ln(z)*ln(1 + x*z)*pow(x,-1)*z*CF - 4*ln(z)*ln(1\
       + x*z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 2*ln(z)*ln(1 + x*z)*CF*pow(omx,-1) - ln(z)*ln(1\
       + x*z)*CF*pow(opx,-1) + 4*ln(z)*ln(1 + x*z)*z*CF*pow(omx,-1) + 2*ln(z)*ln(1 + x*z)*z*CF*pow(\
      opx,-1) - 4*ln(z)*ln(1 + x*z)*z*CF + 4*ln(z)*ln(1 + x*z)*pow(z,2)*CF*pow(omx,-1) - 4*ln(z)*\
      ln(1 + x*z)*pow(z,2)*CF*pow(opx,-1) - 2*ln(z)*ln(1 + x*z)*x*CF - 8*ln(z)*ln(1 + x*z)*x*pow(\
      z,2)*CF - 2*ln(z)*ln(z + x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + ln(z)*ln(z + x)*pow(NC,-1)*\
      pow(z,-1)*CF - 4*ln(z)*ln(z + x)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(z)*ln(z + x)*pow(NC,-1)*CF\
       - 2*ln(z)*ln(z + x)*pow(NC,-1)*z*CF*pow(omx,-1) + ln(z)*ln(z + x)*pow(NC,-1)*x*pow(z,-1)*CF\
       + 2*ln(z)*ln(z + x)*pow(NC,-1)*x*CF + 2*ln(z)*ln(z + x)*pow(NC,-1)*x*z*CF + 2*ln(z)*ln(z + x\
      )*CF*pow(omx,-1) - ln(z)*ln(z + x)*CF + 4*ln(z)*ln(z + x)*z*CF*pow(omx,-1) - 2*ln(z)*ln(z + x\
      )*z*CF + 4*ln(z)*ln(z + x)*pow(z,2)*CF*pow(omx,-1) - ln(z)*ln(z + x)*x*CF - 2*ln(z)*ln(z + x)\
      *x*z*CF - 4*ln(z)*ln(z + x)*x*pow(z,2)*CF + 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)\
      *CF*pow(opx,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - pow(ln(z),2)*pow(\
      NC,-1)*pow(x,-2)*CF*pow(opx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*CF + pow(ln(z),2)*pow(\
      NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) - pow(ln(z),2)*pow(NC,-1)*pow(x,-2)*z*CF + 1./2.*pow(ln(z),\
      2)*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF
                result +=  - pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*CF + pow(ln(z),2)*pow(NC,-1)*pow(x,-1)*z*CF*pow(\
      opx,-1) - 2*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) + 2*pow(ln(z),2)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1) + 1./2.\
      *pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 3./2.*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*\
      CF - 3*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 3*pow(ln(z),2)*pow(NC,-1)*CF*pow(\
      omx,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1) - pow(ln(z),2)*pow(NC,-1)*CF*pow(\
      opx,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*CF + 3*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) + \
      pow(ln(z),2)*pow(NC,-1)*z*CF*pow(opx,-1) + 1./2.*pow(ln(z),2)*pow(NC,-1)*z*CF + pow(ln(z),2)*\
      pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 1./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF + 1./2.*\
      pow(ln(z),2)*pow(NC,-1)*x*CF*pow(omz,-1) - 3./2.*pow(ln(z),2)*pow(NC,-1)*x*CF - 1./2.*pow(ln(\
      z),2)*pow(NC,-1)*x*z*CF + 1./2.*pow(ln(z),2)*pow(x,-2)*CF*pow(opx,-1) - 1./2.*pow(ln(z),2)*\
      pow(x,-2)*CF - pow(ln(z),2)*pow(x,-2)*z*CF*pow(opx,-1) + pow(ln(z),2)*pow(x,-2)*z*CF + 2*pow(\
      ln(z),2)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 2*pow(ln(z),2)*pow(x,-2)*pow(z,2)*CF + 1./2.*\
      pow(ln(z),2)*pow(x,-1)*CF - pow(ln(z),2)*pow(x,-1)*z*CF + 2*pow(ln(z),2)*pow(x,-1)*pow(z,2)*\
      CF*pow(opx,-1) - pow(ln(z),2)*CF*pow(omx,-1) + 1./2.*pow(ln(z),2)*CF*pow(opx,-1) - 2*pow(ln(z\
      ),2)*CF
                result +=  + 2*pow(ln(z),2)*z*CF*pow(omx,-1) - pow(ln(z),2)*z*CF*pow(opx,-1) + 2*pow(ln(z),2)*z*\
      CF - 2*pow(ln(z),2)*pow(z,2)*CF*pow(omx,-1) + 2*pow(ln(z),2)*pow(z,2)*CF*pow(opx,-1) + pow(\
      ln(z),2)*x*CF - 6*pow(ln(z),2)*x*z*CF + 4*pow(ln(z),2)*x*pow(z,2)*CF + 2*pow(ln(z),2)*NC*CF*\
      pow(omx,-1)*pow(omz,-1) - pow(ln(z),2)*NC*CF*pow(omx,-1) - 1./2.*pow(ln(z),2)*NC*CF - pow(ln(\
      z),2)*NC*z*CF*pow(omx,-1) - 1./2.*pow(ln(z),2)*NC*z*CF - 1./2.*pow(ln(z),2)*NC*x*CF - 1./2.*\
      pow(ln(z),2)*NC*x*z*CF - 12*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 8*ln(z)*ln(\
      omx)*pow(NC,-1)*CF*pow(omx,-1) + 3*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) - 5*ln(z)*ln(omx)*\
      pow(NC,-1)*CF + 8*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 9*ln(z)*ln(omx)*pow(NC,-1)*x*CF\
      *pow(omz,-1) - 6*ln(z)*ln(omx)*pow(NC,-1)*x*CF - 11*ln(z)*ln(omx)*pow(NC,-1)*x*z*CF - ln(z)*\
      ln(omx)*CF - ln(z)*ln(omx)*x*CF - 2*ln(z)*ln(omx)*x*z*CF + 4*ln(z)*ln(omx)*NC*CF*pow(omx,-1)*\
      pow(omz,-1) - 2*ln(z)*ln(omx)*NC*CF*pow(omx,-1) - 2*ln(z)*ln(omx)*NC*CF*pow(omz,-1) + 3*ln(z)\
      *ln(omx)*NC*CF - 2*ln(z)*ln(omx)*NC*z*CF*pow(omx,-1) - 2*ln(z)*ln(omx)*NC*x*CF*pow(omz,-1) + \
      3*ln(z)*ln(omx)*NC*x*z*CF - 14*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 13*ln(z)\
      *ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 5*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) - 12*ln(z)*ln(\
      omz)*pow(NC,-1)*CF + 13*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + 11*ln(z)*ln(omz)*pow(\
      NC,-1)*x*CF*pow(omz,-1)
                result +=  - 6*ln(z)*ln(omz)*pow(NC,-1)*x*CF - 18*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF + ln(z)*ln(omz\
      )*CF*pow(omx,-1) - 2*ln(z)*ln(omz)*z*CF*pow(omx,-1) - 2*ln(z)*ln(omz)*x*CF + 4*ln(z)*ln(omz)*\
      x*z*CF + 2*ln(z)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) - ln(z)*ln(omz)*NC*CF*pow(omx,-1) - 2*\
      ln(z)*ln(omz)*NC*CF*pow(omz,-1) + 6*ln(z)*ln(omz)*NC*CF - ln(z)*ln(omz)*NC*z*CF*pow(omx,-1)\
       - 2*ln(z)*ln(omz)*NC*x*CF*pow(omz,-1) + 6*ln(z)*ln(omz)*NC*x*z*CF - 6*ln(omx)*pow(NC,-1)*CF*\
      pow(omx,-1)*pow(omz,-1) + 3./2.*ln(omx)*pow(NC,-1)*CF + 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1)\
       - 1./2.*ln(omx)*pow(NC,-1)*z*CF + 6*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) - 3./2.*ln(omx)*pow(\
      NC,-1)*x*CF - 11./2.*ln(omx)*pow(NC,-1)*x*z*CF + 2./3.*ln(omx)*pow(x,-1)*pow(z,-1)*CF - 4./3.\
      *ln(omx)*pow(x,-1)*CF + 1./6.*ln(omx)*pow(z,-1)*CF - 3./2.*ln(omx)*CF + 3./2.*ln(omx)*z*CF - \
      2./3.*ln(omx)*pow(z,2)*CF - 5./6.*ln(omx)*x*pow(z,-1)*CF - 1./2.*ln(omx)*x*CF + 1./2.*ln(omx)\
      *x*z*CF + 4./3.*ln(omx)*x*pow(z,2)*CF - 2./3.*ln(omx)*pow(x,2)*pow(z,-1)*CF + 4./3.*ln(omx)*\
      pow(x,2)*CF + 4*ln(omx)*NC*CF*pow(omx,-1)*pow(omz,-1) + 11./6.*ln(omx)*NC*CF - 4*ln(omx)*NC*z\
      *CF*pow(omx,-1) + 1./2.*ln(omx)*NC*z*CF - 4*ln(omx)*NC*x*CF*pow(omz,-1) - 7./2.*ln(omx)*NC*x*\
      CF - 1./6.*ln(omx)*NC*x*z*CF + 2./3.*ln(omx)*NF*CF + 2./3.*ln(omx)*NF*x*z*CF
                result +=  - 5*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 3*pow(ln(omx),\
      2)*pow(NC,-1)*CF*pow(omx,-1) + 1./2.*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omz,-1) - 5./2.*pow(ln(\
      omx),2)*pow(NC,-1)*CF + 3*pow(ln(omx),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*pow(ln(omx),2)*\
      pow(NC,-1)*z*CF + 9./2.*pow(ln(omx),2)*pow(NC,-1)*x*CF*pow(omz,-1) - 9./2.*pow(ln(omx),2)*\
      pow(NC,-1)*x*CF - 13./2.*pow(ln(omx),2)*pow(NC,-1)*x*z*CF + 4*pow(ln(omx),2)*NC*CF*pow(\
      omx,-1)*pow(omz,-1) - 2*pow(ln(omx),2)*NC*CF*pow(omx,-1) - 2*pow(ln(omx),2)*NC*CF*pow(omz,-1)\
       + 11./2.*pow(ln(omx),2)*NC*CF - 2*pow(ln(omx),2)*NC*z*CF*pow(omx,-1) + 1./2.*pow(ln(omx),2)*\
      NC*z*CF - 2*pow(ln(omx),2)*NC*x*CF*pow(omz,-1) + 1./2.*pow(ln(omx),2)*NC*x*CF + 11./2.*pow(\
      ln(omx),2)*NC*x*z*CF - 8*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 6*ln(omx)*\
      ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) - 7*ln(omx)*\
      ln(omz)*pow(NC,-1)*CF + 6*ln(omx)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(omx)*ln(omz)*pow(\
      NC,-1)*z*CF
                result +=  + 6*ln(omx)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) - 5*ln(omx)*ln(omz)*pow(NC,-1)*x*CF\
       - 11*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF + 8*ln(omx)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) - 4\
      *ln(omx)*ln(omz)*NC*CF*pow(omx,-1) - 4*ln(omx)*ln(omz)*NC*CF*pow(omz,-1) + 11*ln(omx)*ln(omz)\
      *NC*CF - 4*ln(omx)*ln(omz)*NC*z*CF*pow(omx,-1) + ln(omx)*ln(omz)*NC*z*CF - 4*ln(omx)*ln(omz)*\
      NC*x*CF*pow(omz,-1) + ln(omx)*ln(omz)*NC*x*CF + 11*ln(omx)*ln(omz)*NC*x*z*CF - 6*ln(omz)*pow(\
      NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 3./2.*ln(omz)*pow(NC,-1)*CF*pow(omxmz,-1) + 3*ln(omz)*\
      pow(NC,-1)*CF + 6*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*ln(omz)*pow(NC,-1)*z*CF + 6*ln(omz)\
      *pow(NC,-1)*x*CF*pow(omz,-1) + 1./2.*ln(omz)*pow(NC,-1)*x*CF*pow(omxmz,-2) + 1./2.*ln(omz)*\
      pow(NC,-1)*x*CF*pow(omxmz,-1) - 2*ln(omz)*pow(NC,-1)*x*CF - 4*ln(omz)*pow(NC,-1)*x*z*CF - 1./\
      2.*ln(omz)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-2) + 2./3.*ln(omz)*pow(x,-1)*pow(z,-1)*CF - 4./3.\
      *ln(omz)*pow(x,-1)*CF + 1./6.*ln(omz)*pow(z,-1)*CF - 3./2.*ln(omz)*CF + 3./2.*ln(omz)*z*CF - \
      2./3.*ln(omz)*pow(z,2)*CF - 5./6.*ln(omz)*x*pow(z,-1)*CF - 1./2.*ln(omz)*x*CF + 1./2.*ln(omz)\
      *x*z*CF + 4./3.*ln(omz)*x*pow(z,2)*CF - 2./3.*ln(omz)*pow(x,2)*pow(z,-1)*CF + 4./3.*ln(omz)*\
      pow(x,2)*CF + 4*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) + 3./2.*ln(omz)*NC*CF*pow(omxmz,-1) + 1.\
      /3.*ln(omz)*NC*CF - 4*ln(omz)*NC*z*CF*pow(omx,-1) + 2*ln(omz)*NC*z*CF - 4*ln(omz)*NC*x*CF*\
      pow(omz,-1)
                result +=  - 1./2.*ln(omz)*NC*x*CF*pow(omxmz,-2) + 1./2.*ln(omz)*NC*x*CF*pow(omxmz,-1) - 2*ln(\
      omz)*NC*x*CF - 5./3.*ln(omz)*NC*x*z*CF + 1./2.*ln(omz)*NC*pow(x,2)*CF*pow(omxmz,-2) + 2./3.*\
      ln(omz)*NF*CF + 2./3.*ln(omz)*NF*x*z*CF - 5*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 9./2.*pow(ln(omz),2\
      )*pow(NC,-1)*CF*pow(omx,-1) + 2*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omz,-1) - 11./2.*pow(ln(omz)\
      ,2)*pow(NC,-1)*CF + 9./2.*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*pow(ln(omz),2)*\
      pow(NC,-1)*z*CF + 3*pow(ln(omz),2)*pow(NC,-1)*x*CF*pow(omz,-1) - 3./2.*pow(ln(omz),2)*pow(\
      NC,-1)*x*CF - 13./2.*pow(ln(omz),2)*pow(NC,-1)*x*z*CF + 4*pow(ln(omz),2)*NC*CF*pow(omx,-1)*\
      pow(omz,-1) - 2*pow(ln(omz),2)*NC*CF*pow(omx,-1) - 2*pow(ln(omz),2)*NC*CF*pow(omz,-1) + 11./2.\
      *pow(ln(omz),2)*NC*CF - 2*pow(ln(omz),2)*NC*z*CF*pow(omx,-1) + 1./2.*pow(ln(omz),2)*NC*z*CF\
       - 2*pow(ln(omz),2)*NC*x*CF*pow(omz,-1)
                result +=  + 1./2.*pow(ln(omz),2)*NC*x*CF + 11./2.*pow(ln(omz),2)*NC*x*z*CF - 3./8.*Li2(1./2. - \
      1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2)\
      *CF + Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF - 5./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*\
      pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*CF - 3*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1)*CF + 3*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(\
      x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1)*CF*pow(omz,-1) + 9./2.*Li2(1./2. - 1./2.*pow(x,-1)\
       - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1)*CF - 9*Li2(1./2. - 1./2.*pow(x,-1) - 1.\
      /2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*z*pow(sqrtxz2,-1)*CF - 2*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.\
      *pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1)*CF - 2*Li2(1./2. - 1./2.*pow(x,-1)\
       - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF*pow(omz,-1) + 51./4.*Li2(1./2. - \
      1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF - 18*Li2(1./2. - 1.\
      /2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*z*pow(sqrtxz2,-1)*CF + 18*Li2(1./2. - 1.\
      /2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 3*Li2(1./\
      2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1)\
      *CF
                result +=  + 3*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz2,-1)*CF*pow(omz,-1) + 9./2.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*\
      pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*CF - 9*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 3./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.\
      *pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF - 5./8.*Li2(1./2. - \
      1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*CF + Li2(1./2.\
       - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(\
      poly2,-1)*CF - 3./8.*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(\
      x,7)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF - 4*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(sqrtxz2,-1)*CF + 8*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*z*pow(\
      sqrtxz2,-1)*CF - 2*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*\
      CF + 16*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*z*pow(sqrtxz2,-1)*CF - 16*\
      Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 4*Li2(\
      1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*pow(sqrtxz2,-1)*CF + 8*Li2(1./2.\
       - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 3./8.*Li2(1./2.\
       - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(\
      poly2,-2)*CF
                result +=  - Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,-1)*pow(\
      sqrtxz2,-1)*pow(poly2,-1)*CF + 5./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*\
      pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*CF + 3*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1)*CF - 3*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
      x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1)*CF*pow(omz,-1) - 9./2.*Li2(1./2. - 1./2.*pow(x,-1)\
       + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(sqrtxz2,-1)*CF + 9*Li2(1./2. - 1./2.*pow(x,-1) + 1.\
      /2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*z*pow(sqrtxz2,-1)*CF + 2*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.\
      *pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1)*CF + 2*Li2(1./2. - 1./2.*pow(x,-1)\
       + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF*pow(omz,-1) - 51./4.*Li2(1./2. - \
      1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF + 18*Li2(1./2. - 1.\
      /2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*z*pow(sqrtxz2,-1)*CF - 18*Li2(1./2. - 1.\
      /2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 3*Li2(1./\
      2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(sqrtxz2,-1)\
      *CF - 3*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz2,-1)*CF*pow(omz,-1) - 9./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*\
      pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*CF
                result +=  + 9*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,2)*z*pow(\
      sqrtxz2,-1)*CF - 3./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(\
      x,3)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF + 5./8.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*CF - Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(\
      x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 3./8.*Li2(1./2. - 1./2.\
      *pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF + \
      4*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(sqrtxz2,-1)*CF - 8*Li2(1./2. - 1.\
      /2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*z*pow(sqrtxz2,-1)*CF + 2*Li2(1./2. - 1./2.*pow(x,-1)\
       + 1./2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*CF - 16*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*\
      pow(x,-1)*sqrtxz2)*x*z*pow(sqrtxz2,-1)*CF + 16*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 4*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(x,2)*pow(sqrtxz2,-1)*CF - 8*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*\
      sqrtxz2)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
      pow(NC,-1)*CF*pow(omx,-1)
                result +=  + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*CF - 2*Li2(1./2.\
       - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(1./2. - 1./2.\
      *pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(1./2. - 1./2.*pow(\
      z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*CF + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(\
      z,-1)*sqrtxz1)*pow(NC,-1)*x*z*CF + Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*CF*\
      pow(omx,-1) - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*CF + 6*Li2(1./2. - 1./\
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*z*CF*pow(omx,-1) - 4*Li2(1./2. - 1./2.*pow(z,-1) - 1./\
      2.*pow(z,-1)*sqrtxz1)*x*z*CF + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(\
      NC,-1)*pow(z,-1)*CF + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*CF*\
      pow(omx,-1) - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*CF + 2*Li2(\
      1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(1./2. + \
      1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*CF - 2*Li2(1./2. + 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*CF - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*\
      pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*z*CF - Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)\
      *CF*pow(omx,-1)
                result +=  + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*CF - 6*Li2(1./2. + 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*z*CF*pow(omx,-1) + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.\
      *pow(z,-1)*sqrtxz1)*x*z*CF + 3./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*\
      pow(sqrtxz2,-1)*pow(poly2,-2)*CF - Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*\
      pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 5./8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(\
      x,-1)*pow(sqrtxz2,-1)*CF + 3*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(z,-1)*pow(\
      sqrtxz2,-1)*CF - 3*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1)*CF*pow(\
      omz,-1) - 9./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1)*CF + 9*Li2(1./\
      2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*z*pow(sqrtxz2,-1)*CF + 2*Li2(1./2. - 1./2.*sqrtxz2\
       - 1./2.*x)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1)*CF + 2*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x\
      )*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF*pow(omz,-1) - 51./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*\
      pow(NC,-1)*x*pow(sqrtxz2,-1)*CF + 18*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*z*pow(\
      sqrtxz2,-1)*CF - 18*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(z,2)*pow(\
      sqrtxz2,-1)*CF + 3*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      sqrtxz2,-1)*CF - 3*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*\
      CF*pow(omz,-1)
                result +=  - 9./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*CF\
       + 9*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 3./4.*\
      Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF + 5.\
      /8.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*CF - Li2(1./2.\
       - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 3./8.*Li2(\
      1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF + 4*\
      Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(sqrtxz2,-1)*CF - 8*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.\
      *x)*z*pow(sqrtxz2,-1)*CF + 2*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*CF - 16*\
      Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*z*pow(sqrtxz2,-1)*CF + 16*Li2(1./2. - 1./2.*sqrtxz2 - \
      1./2.*x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 4*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*pow(\
      sqrtxz2,-1)*CF - 8*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 3./8.\
      *Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-2)*CF\
       + Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF\
       - 5./8.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,-1)*pow(sqrtxz2,-1)*CF - 3*\
      Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(z,-1)*pow(sqrtxz2,-1)*CF + 3*Li2(1./2. + \
      1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1)*CF*pow(omz,-1)
                result +=  + 9./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(sqrtxz2,-1)*CF - 9*Li2(1./\
      2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*z*pow(sqrtxz2,-1)*CF - 2*Li2(1./2. + 1./2.*sqrtxz2\
       - 1./2.*x)*pow(NC,-1)*x*pow(z,-1)*pow(sqrtxz2,-1)*CF - 2*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x\
      )*pow(NC,-1)*x*pow(sqrtxz2,-1)*CF*pow(omz,-1) + 51./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*\
      pow(NC,-1)*x*pow(sqrtxz2,-1)*CF - 18*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*z*pow(\
      sqrtxz2,-1)*CF + 18*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*x*pow(z,2)*pow(\
      sqrtxz2,-1)*CF - 3*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(z,-1)*pow(\
      sqrtxz2,-1)*CF + 3*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(sqrtxz2,-1)*\
      CF*pow(omz,-1) + 9./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*pow(\
      sqrtxz2,-1)*CF - 9*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,2)*z*pow(sqrtxz2,-1)\
      *CF + 3./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)*pow(\
      poly2,-2)*CF - 5./8.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,3)*pow(sqrtxz2,-1)\
      *CF + Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*\
      CF - 3./8.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(NC,-1)*pow(x,7)*pow(sqrtxz2,-1)*pow(\
      poly2,-2)*CF - 4*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(sqrtxz2,-1)*CF + 8*Li2(1./2. + 1./2.\
      *sqrtxz2 - 1./2.*x)*z*pow(sqrtxz2,-1)*CF
                result +=  - 2*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*CF + 16*Li2(1./2. + 1./2.*\
      sqrtxz2 - 1./2.*x)*x*z*pow(sqrtxz2,-1)*CF - 16*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(\
      z,2)*pow(sqrtxz2,-1)*CF - 4*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*pow(sqrtxz2,-1)*CF\
       + 8*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 2*Li2(1./2. - 1./2.\
      *sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z\
      )*pow(NC,-1)*pow(z,-1)*CF + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*CF*pow(omx,-1)\
       - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*CF + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.\
      *z)*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)\
      *CF - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*CF - 2*Li2(1./2. - 1./2.*sqrtxz1 - \
      1./2.*z)*pow(NC,-1)*x*z*CF - 3*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*CF*pow(omx,-1) - 2*Li2(1./\
      2. - 1./2.*sqrtxz1 - 1./2.*z)*z*CF*pow(omx,-1) + 4*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*z*CF\
       - 8*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(z,2)*CF*pow(omx,-1) + 2*Li2(1./2. - 1./2.*\
      sqrtxz1 - 1./2.*z)*x*CF + 8*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*x*pow(z,2)*CF - 2*Li2(1./2.\
       - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + Li2(1./2. - 1./2.*sqrtxz1\
       + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*CF*\
      pow(omx,-1)
                result +=  + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*CF - 2*Li2(1./2. - 1./2.*sqrtxz1\
       + 1./2.*z)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*\
      pow(z,-1)*CF + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*CF + 2*Li2(1./2. - 1./2.*\
      sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*z*CF + 3*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*CF*pow(omx,-1)\
       + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*z*CF*pow(omx,-1) - 4*Li2(1./2. - 1./2.*sqrtxz1 + 1./\
      2.*z)*z*CF + 8*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(z,2)*CF*pow(omx,-1) - 2*Li2(1./2. - 1.\
      /2.*sqrtxz1 + 1./2.*z)*x*CF - 8*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*x*pow(z,2)*CF + 8*Li2(1\
       - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) - 8*Li2(1 - x*pow(z,-1))*pow(\
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1)\
       + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF - 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) - 6*Li2(1 - x*pow(z,-1))*pow(NC,-1)*CF*pow(omx,-1) + Li2(1 - x*pow(z,-1))\
      *pow(NC,-1)*CF*pow(omz,-1) + 4*Li2(1 - x*pow(z,-1))*pow(NC,-1)*CF - 6*Li2(1 - x*pow(z,-1))*\
      pow(NC,-1)*z*CF*pow(omx,-1) - 6*Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) + \
      6*Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF + Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*CF*pow(\
      omz,-1) + 4*Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*CF + 8*Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*z*CF\
       - Li2(1 - x*pow(z,-1))*CF*pow(omx,-1)
                result +=  + 2*Li2(1 - x*pow(z,-1))*z*CF*pow(omx,-1) + 2*Li2(1 - x*pow(z,-1))*x*CF - 4*Li2(1 - x\
      *pow(z,-1))*x*z*CF + 2*Li2(1 - x*pow(z,-1))*NC*CF*pow(omx,-1)*pow(omz,-1) - Li2(1 - x*pow(\
      z,-1))*NC*CF*pow(omx,-1) - Li2(1 - x*pow(z,-1))*NC*CF*pow(omz,-1) - Li2(1 - x*pow(z,-1))*NC*z\
      *CF*pow(omx,-1) - Li2(1 - x*pow(z,-1))*NC*x*CF*pow(omz,-1) - Li2( - x*pow(z,-1))*pow(NC,-1)*\
      pow(x,-2)*pow(z,-1)*CF*pow(opx,-1) + Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + \
      2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*\
      pow(x,-2)*CF - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 2*Li2( - x*pow(\
      z,-1))*pow(NC,-1)*pow(x,-2)*z*CF - Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF + 2*\
      Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*CF - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(x,-1)*z*CF\
      *pow(opx,-1) + 2*Li2( - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2( - x*pow(z,-1)\
      )*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 4*Li2( - x*pow(z,-1))*pow(NC,-1)*CF*pow(omx,-1) + 2*\
      Li2( - x*pow(z,-1))*pow(NC,-1)*CF*pow(opx,-1) - 4*Li2( - x*pow(z,-1))*pow(NC,-1)*CF + 2*Li2(\
       - x*pow(z,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*z*CF*pow(\
      opx,-1) - 2*Li2( - x*pow(z,-1))*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2( - x*pow(z,-1))*pow(NC,-1)*\
      x*z*CF - Li2( - x*pow(z,-1))*pow(x,-2)*CF*pow(opx,-1) + Li2( - x*pow(z,-1))*pow(x,-2)*CF + 2*\
      Li2( - x*pow(z,-1))*pow(x,-2)*z*CF*pow(opx,-1)
                result +=  - 2*Li2( - x*pow(z,-1))*pow(x,-2)*z*CF - 4*Li2( - x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF*\
      pow(opx,-1) + 4*Li2( - x*pow(z,-1))*pow(x,-2)*pow(z,2)*CF - Li2( - x*pow(z,-1))*pow(x,-1)*CF\
       + 2*Li2( - x*pow(z,-1))*pow(x,-1)*z*CF - 4*Li2( - x*pow(z,-1))*pow(x,-1)*pow(z,2)*CF*pow(\
      opx,-1) - 2*Li2( - x*pow(z,-1))*CF*pow(omx,-1) - Li2( - x*pow(z,-1))*CF*pow(opx,-1) + 2*Li2(\
       - x*pow(z,-1))*CF - 4*Li2( - x*pow(z,-1))*z*CF*pow(omx,-1) + 2*Li2( - x*pow(z,-1))*z*CF*pow(\
      opx,-1) - 4*Li2( - x*pow(z,-1))*pow(z,2)*CF*pow(omx,-1) - 4*Li2( - x*pow(z,-1))*pow(z,2)*CF*\
      pow(opx,-1) + 4*Li2( - x*pow(z,-1))*x*z*CF + 2*Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF*\
      pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF - 4*Li2( - x)*pow(NC,-1)*pow(\
      x,-2)*CF*pow(opx,-1) + 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*CF + 4*Li2( - x)*pow(NC,-1)*pow(x,-2)\
      *z*CF*pow(opx,-1) - 4*Li2( - x)*pow(NC,-1)*pow(x,-2)*z*CF + 2*Li2( - x)*pow(NC,-1)*pow(x,-1)*\
      pow(z,-1)*CF - 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*CF + 4*Li2( - x)*pow(NC,-1)*pow(x,-1)*z*CF*\
      pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) - 2*Li2( - x)*pow(NC,-1)*pow(\
      z,-1)*CF + 4*Li2( - x)*pow(NC,-1)*CF*pow(opx,-1) + 4*Li2( - x)*pow(NC,-1)*CF - 2*Li2( - x)*\
      pow(NC,-1)*x*pow(z,-1)*CF + 4*Li2( - x)*pow(NC,-1)*x*CF + 2*Li2( - x)*pow(x,-2)*CF*pow(\
      opx,-1) - 2*Li2( - x)*pow(x,-2)*CF - 4*Li2( - x)*pow(x,-2)*z*CF*pow(opx,-1) + 4*Li2( - x)*\
      pow(x,-2)*z*CF
                result +=  + 8*Li2( - x)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) - 8*Li2( - x)*pow(x,-2)*pow(z,2)*CF\
       + 2*Li2( - x)*pow(x,-1)*CF - 4*Li2( - x)*pow(x,-1)*z*CF + 8*Li2( - x)*pow(x,-1)*pow(z,2)*CF*\
      pow(opx,-1) - 2*Li2( - x)*CF*pow(opx,-1) - 4*Li2( - x)*CF + 4*Li2( - x)*z*CF*pow(opx,-1) + 8*\
      Li2( - x)*z*CF - 4*Li2( - x)*x*CF + 8*Li2( - x)*x*z*CF - Li2( - x*z)*pow(NC,-1)*pow(x,-2)*\
      pow(z,-1)*CF*pow(opx,-1) + Li2( - x*z)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 2*Li2( - x*z)*pow(\
      NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*CF - 2*Li2( - x*z)*pow(\
      NC,-1)*pow(x,-2)*z*CF*pow(opx,-1) + 2*Li2( - x*z)*pow(NC,-1)*pow(x,-2)*z*CF - Li2( - x*z)*\
      pow(NC,-1)*pow(x,-1)*pow(z,-1)*CF + 2*Li2( - x*z)*pow(NC,-1)*pow(x,-1)*CF - 2*Li2( - x*z)*\
      pow(NC,-1)*pow(x,-1)*z*CF*pow(opx,-1) - 2*Li2( - x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - \
      Li2( - x*z)*pow(NC,-1)*pow(z,-1)*CF*pow(opx,-1) + 2*Li2( - x*z)*pow(NC,-1)*pow(z,-1)*CF - 4*\
      Li2( - x*z)*pow(NC,-1)*CF*pow(omx,-1) + 2*Li2( - x*z)*pow(NC,-1)*CF*pow(opx,-1) - 2*Li2( - x*\
      z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2( - x*z)*pow(NC,-1)*z*CF*pow(opx,-1) + 4*Li2( - x*z)*\
      pow(NC,-1)*x*CF - Li2( - x*z)*pow(x,-2)*CF*pow(opx,-1) + Li2( - x*z)*pow(x,-2)*CF + 2*Li2( - \
      x*z)*pow(x,-2)*z*CF*pow(opx,-1) - 2*Li2( - x*z)*pow(x,-2)*z*CF - 4*Li2( - x*z)*pow(x,-2)*pow(\
      z,2)*CF*pow(opx,-1) + 4*Li2( - x*z)*pow(x,-2)*pow(z,2)*CF - Li2( - x*z)*pow(x,-1)*CF + 2*Li2(\
       - x*z)*pow(x,-1)*z*CF
                result +=  - 4*Li2( - x*z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 2*Li2( - x*z)*CF*pow(omx,-1) - \
      Li2( - x*z)*CF*pow(opx,-1) + 4*Li2( - x*z)*z*CF*pow(omx,-1) + 2*Li2( - x*z)*z*CF*pow(opx,-1)\
       - 4*Li2( - x*z)*z*CF + 4*Li2( - x*z)*pow(z,2)*CF*pow(omx,-1) - 4*Li2( - x*z)*pow(z,2)*CF*\
      pow(opx,-1) - 2*Li2( - x*z)*x*CF - 8*Li2( - x*z)*x*pow(z,2)*CF - 2*Li2(x)*pow(NC,-1)*pow(\
      x,-2)*pow(z,-1)*CF*pow(opx,-1) + 2*Li2(x)*pow(NC,-1)*pow(x,-2)*pow(z,-1)*CF + 4*Li2(x)*pow(\
      NC,-1)*pow(x,-2)*CF*pow(opx,-1) - 4*Li2(x)*pow(NC,-1)*pow(x,-2)*CF - 4*Li2(x)*pow(NC,-1)*pow(\
      x,-2)*z*CF*pow(opx,-1) + 4*Li2(x)*pow(NC,-1)*pow(x,-2)*z*CF - 2*Li2(x)*pow(NC,-1)*pow(x,-1)*\
      pow(z,-1)*CF + 4*Li2(x)*pow(NC,-1)*pow(x,-1)*CF - 4*Li2(x)*pow(NC,-1)*pow(x,-1)*z*CF*pow(\
      opx,-1) - 8*Li2(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)*pow(omz,-1) + 8*Li2(x)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) + 4*Li2(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omz,-1) + 2*Li2(x)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(opx,-1) - 4*Li2(x)*pow(NC,-1)*pow(z,-1)*CF + 12*Li2(x)*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) - 3*Li2(x)*pow(NC,-1)*CF*pow(omx,-1) - 4*Li2(x)*pow(NC,-1)*CF*pow(omz,-1)\
       - 4*Li2(x)*pow(NC,-1)*CF*pow(opx,-1) - Li2(x)*pow(NC,-1)*CF - 3*Li2(x)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 4*Li2(x)*pow(NC,-1)*x*pow(z,-1)*CF*pow(omz,-1) - 4*Li2(x)*pow(NC,-1)*x*pow(z,-1)*CF\
       - 8*Li2(x)*pow(NC,-1)*x*CF*pow(omz,-1) + 4*Li2(x)*pow(NC,-1)*x*CF + 3*Li2(x)*pow(NC,-1)*x*z*\
      CF
                result +=  - 2*Li2(x)*pow(x,-2)*CF*pow(opx,-1) + 2*Li2(x)*pow(x,-2)*CF + 4*Li2(x)*pow(x,-2)*z*CF\
      *pow(opx,-1) - 4*Li2(x)*pow(x,-2)*z*CF - 8*Li2(x)*pow(x,-2)*pow(z,2)*CF*pow(opx,-1) + 8*Li2(x\
      )*pow(x,-2)*pow(z,2)*CF - 2*Li2(x)*pow(x,-1)*CF + 4*Li2(x)*pow(x,-1)*z*CF - 8*Li2(x)*pow(\
      x,-1)*pow(z,2)*CF*pow(opx,-1) - Li2(x)*pow(z,-1)*CF + 3*Li2(x)*CF*pow(omx,-1) + 2*Li2(x)*CF*\
      pow(opx,-1) + 2*Li2(x)*CF - 6*Li2(x)*z*CF*pow(omx,-1) - 4*Li2(x)*z*CF*pow(opx,-1) + 8*Li2(x)*\
      pow(z,2)*CF*pow(omx,-1) - Li2(x)*x*pow(z,-1)*CF + 4*Li2(x)*x*z*CF - 8*Li2(x)*x*pow(z,2)*CF + \
      Li2(x)*NC*CF + Li2(x)*NC*x*z*CF - 4*Li2(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 5*Li2(z)*\
      pow(NC,-1)*CF*pow(omx,-1) + Li2(z)*pow(NC,-1)*CF*pow(omz,-1) - 5*Li2(z)*pow(NC,-1)*CF + 5*\
      Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 3*Li2(z)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(z)*pow(\
      NC,-1)*x*CF - 7*Li2(z)*pow(NC,-1)*x*z*CF + Li2(z)*CF*pow(omx,-1) + Li2(z)*CF - 2*Li2(z)*z*CF*\
      pow(omx,-1) - Li2(z)*x*CF + 6*Li2(z)*x*z*CF + 3*Li2(z)*NC*CF + 3*Li2(z)*NC*x*z*CF
            if z < round(1 - x, ndecimals) and z < x:
                result += 4*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(NC,-1)*CF*pow(omz,-1) - 6*pow(NC,-1)*CF - 4./3.*pow(\
      NC,-1)*pow(pi,2)*CF*pow(omx,-1)*pow(omz,-1) + 5./6.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1) + 1./\
      6.*pow(NC,-1)*pow(pi,2)*CF*pow(omz,-1) - 1./3.*pow(NC,-1)*pow(pi,2)*CF - 4*pow(NC,-1)*z*CF*\
      pow(omx,-1) + 5./6.*pow(NC,-1)*z*pow(pi,2)*CF*pow(omx,-1) - 4*pow(NC,-1)*x*CF*pow(omz,-1) + 7.\
      /6.*pow(NC,-1)*x*pow(pi,2)*CF*pow(omz,-1) - pow(NC,-1)*x*pow(pi,2)*CF - 4./3.*pow(NC,-1)*x*z*\
      pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 12*ln(x)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 12*ln(x)*pow(NC,-1)*x*CF*pow(omz,-1) - 12*ln(x)*pow(NC,-1)*x*z*CF + 12*pow(ln(x),2)\
      *pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 9*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) - 3*pow(ln(\
      x),2)*pow(NC,-1)*CF*pow(omz,-1) + 6*pow(ln(x),2)*pow(NC,-1)*CF - 9*pow(ln(x),2)*pow(NC,-1)*z*\
      CF*pow(omx,-1) - 9*pow(ln(x),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*pow(ln(x),2)*pow(NC,-1)*x*CF\
       + 12*pow(ln(x),2)*pow(NC,-1)*x*z*CF - 20*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)\
       + 15*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 5*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omz,-1) - 10*\
      ln(x)*ln(z)*pow(NC,-1)*CF + 15*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 15*ln(x)*ln(z)*pow(\
      NC,-1)*x*CF*pow(omz,-1) - 10*ln(x)*ln(z)*pow(NC,-1)*x*CF - 20*ln(x)*ln(z)*pow(NC,-1)*x*z*CF\
       - 18*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 13*ln(x)*ln(omx)*pow(NC,-1)*CF*\
      pow(omx,-1)
                result +=  + 4*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) - 8*ln(x)*ln(omx)*pow(NC,-1)*CF + 13*ln(x\
      )*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 14*ln(x)*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) - 10*ln(\
      x)*ln(omx)*pow(NC,-1)*x*CF - 18*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 18*ln(x)*ln(omz)*pow(NC,-1)\
      *CF*pow(omx,-1)*pow(omz,-1) + 14*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 5*ln(x)*ln(omz)*\
      pow(NC,-1)*CF*pow(omz,-1) - 10*ln(x)*ln(omz)*pow(NC,-1)*CF + 14*ln(x)*ln(omz)*pow(NC,-1)*z*CF\
      *pow(omx,-1) + 13*ln(x)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) - 8*ln(x)*ln(omz)*pow(NC,-1)*x*CF\
       - 18*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + 4*ln(x)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)\
       - 3*ln(x)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1) - ln(x)*ln(xmz)*pow(NC,-1)*CF*pow(omz,-1) + 2*\
      ln(x)*ln(xmz)*pow(NC,-1)*CF - 3*ln(x)*ln(xmz)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*ln(x)*ln(xmz)*\
      pow(NC,-1)*x*CF*pow(omz,-1) + 2*ln(x)*ln(xmz)*pow(NC,-1)*x*CF + 4*ln(x)*ln(xmz)*pow(NC,-1)*x*\
      z*CF + 2*ln(x)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 2*ln(x)*ln(omxmz)*pow(NC,-1)\
      *CF*pow(omx,-1) - ln(x)*ln(omxmz)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(x)*ln(omxmz)*pow(NC,-1)*CF\
       - 2*ln(x)*ln(omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln(omxmz)*pow(NC,-1)*x*CF*pow(\
      omz,-1) + 2*ln(x)*ln(omxmz)*pow(NC,-1)*x*z*CF + 8*ln(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)\
       - 8*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(z)*pow(NC,-1)*x*CF*pow(omz,-1) + 8*ln(z)*pow(\
      NC,-1)*x*z*CF
                result +=  + 8*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 6*pow(ln(z),2)*pow(NC,-1)*CF\
      *pow(omx,-1) - 2*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1) + 4*pow(ln(z),2)*pow(NC,-1)*CF - 6*\
      pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*pow(ln(z),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 4*\
      pow(ln(z),2)*pow(NC,-1)*x*CF + 8*pow(ln(z),2)*pow(NC,-1)*x*z*CF + 12*ln(z)*ln(omx)*pow(NC,-1)\
      *CF*pow(omx,-1)*pow(omz,-1) - 8*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(omx)*\
      pow(NC,-1)*CF*pow(omz,-1) + 4*ln(z)*ln(omx)*pow(NC,-1)*CF - 8*ln(z)*ln(omx)*pow(NC,-1)*z*CF*\
      pow(omx,-1) - 10*ln(z)*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) + 8*ln(z)*ln(omx)*pow(NC,-1)*x*CF\
       + 12*ln(z)*ln(omx)*pow(NC,-1)*x*z*CF + 12*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) - 10*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 4*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(\
      omz,-1) + 8*ln(z)*ln(omz)*pow(NC,-1)*CF - 10*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*\
      ln(z)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 4*ln(z)*ln(omz)*pow(NC,-1)*x*CF + 12*ln(z)*ln(omz\
      )*pow(NC,-1)*x*z*CF - 4*ln(z)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 3*ln(z)*ln(xmz)\
      *pow(NC,-1)*CF*pow(omx,-1) + ln(z)*ln(xmz)*pow(NC,-1)*CF*pow(omz,-1) - 2*ln(z)*ln(xmz)*pow(\
      NC,-1)*CF + 3*ln(z)*ln(xmz)*pow(NC,-1)*z*CF*pow(omx,-1) + 3*ln(z)*ln(xmz)*pow(NC,-1)*x*CF*\
      pow(omz,-1) - 2*ln(z)*ln(xmz)*pow(NC,-1)*x*CF - 4*ln(z)*ln(xmz)*pow(NC,-1)*x*z*CF + 6*ln(omx)\
      *pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)
                result +=  - 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*\
      ln(omx)*pow(NC,-1)*x*z*CF + 5*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 3*pow(\
      ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) - 1./2.*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omz,-1) + pow(\
      ln(omx),2)*pow(NC,-1)*CF - 3*pow(ln(omx),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 9./2.*pow(ln(omx),2\
      )*pow(NC,-1)*x*CF*pow(omz,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*x*CF + 5*pow(ln(omx),2)*pow(\
      NC,-1)*x*z*CF + 10*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 8*ln(omx)*ln(omz)*\
      pow(NC,-1)*CF*pow(omx,-1) - 3*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) + 6*ln(omx)*ln(omz)*\
      pow(NC,-1)*CF - 8*ln(omx)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 7*ln(omx)*ln(omz)*pow(NC,-1)*\
      x*CF*pow(omz,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)*x*CF + 10*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF\
       + 6*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - \
      6*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*ln(omz)*pow(NC,-1)*x*z*CF + 4*pow(ln(omz),2)*pow(\
      NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 7./2.*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) - 3./2.*\
      pow(ln(omz),2)*pow(NC,-1)*CF*pow(omz,-1) + 3*pow(ln(omz),2)*pow(NC,-1)*CF - 7./2.*pow(ln(omz)\
      ,2)*pow(NC,-1)*z*CF*pow(omx,-1) - 5./2.*pow(ln(omz),2)*pow(NC,-1)*x*CF*pow(omz,-1) + pow(ln(\
      omz),2)*pow(NC,-1)*x*CF + 4*pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 2*ln(omz)*ln(omxmz)*pow(NC,-1)\
      *CF*pow(omx,-1)*pow(omz,-1)
                result +=  + 2*ln(omz)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*CF*\
      pow(omz,-1) - 2*ln(omz)*ln(omxmz)*pow(NC,-1)*CF + 2*ln(omz)*ln(omxmz)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(omz)*ln(omxmz)*pow(NC,-1)*x*z*\
      CF - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 2*Li2(pow(\
      x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1) + Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(\
      NC,-1)*CF*pow(omz,-1) - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF + 2*Li2(pow(x,-1)*z*\
      pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*x*\
      CF*pow(omz,-1) - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*x*z*CF - 2*Li2(pow(x,-1)*z*omx\
      *pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(\
      NC,-1)*CF*pow(omx,-1) + Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) + 2*Li2(\
      pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))\
      *pow(NC,-1)*x*CF - 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x*z*CF + Li2(omx*pow(omz,-1)\
      )*pow(NC,-1)*CF*pow(omx,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omz,-1) - 2*Li2(omx*pow(\
      omz,-1))*pow(NC,-1)*CF + Li2(omx*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(omx*pow(\
      omz,-1))*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*x*CF + 2*Li2(z*pow(\
      omx,-1))*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)
                result +=  - 2*Li2(z*pow(omx,-1))*pow(NC,-1)*CF*pow(omx,-1) - Li2(z*pow(omx,-1))*pow(NC,-1)*CF*\
      pow(omz,-1) + 2*Li2(z*pow(omx,-1))*pow(NC,-1)*CF - 2*Li2(z*pow(omx,-1))*pow(NC,-1)*z*CF*pow(\
      omx,-1) - Li2(z*pow(omx,-1))*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(z*pow(omx,-1))*pow(NC,-1)*x*\
      z*CF - 2*Li2(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + Li2(z)*pow(NC,-1)*CF*pow(omx,-1) + \
      Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 2*Li2(z)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(z)*pow(\
      NC,-1)*x*CF - 2*Li2(z)*pow(NC,-1)*x*z*CF
            if z > round(1 - x, ndecimals) and z < x:
                result += 4*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(NC,-1)*CF*pow(omz,-1) - 6*pow(NC,-1)*CF - 4./3.*pow(\
      NC,-1)*pow(pi,2)*CF*pow(omx,-1)*pow(omz,-1) + 5./6.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1) + 1./\
      6.*pow(NC,-1)*pow(pi,2)*CF*pow(omz,-1) - 1./3.*pow(NC,-1)*pow(pi,2)*CF - 4*pow(NC,-1)*z*CF*\
      pow(omx,-1) + 5./6.*pow(NC,-1)*z*pow(pi,2)*CF*pow(omx,-1) - 4*pow(NC,-1)*x*CF*pow(omz,-1) + 7.\
      /6.*pow(NC,-1)*x*pow(pi,2)*CF*pow(omz,-1) - pow(NC,-1)*x*pow(pi,2)*CF - 4./3.*pow(NC,-1)*x*z*\
      pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 12*ln(x)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 12*ln(x)*pow(NC,-1)*x*CF*pow(omz,-1) - 12*ln(x)*pow(NC,-1)*x*z*CF + 2*ln(x)*ln( - \
      omxmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 2*ln(x)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1)\
       - ln(x)*ln( - omxmz)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(x)*ln( - omxmz)*pow(NC,-1)*CF - 2*ln(x\
      )*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln( - omxmz)*pow(NC,-1)*x*CF*pow(omz,-1)\
       + 2*ln(x)*ln( - omxmz)*pow(NC,-1)*x*z*CF + 13*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) - 10*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) - 7./2.*pow(ln(x),2)*pow(NC,-1)*CF*pow(\
      omz,-1) + 7*pow(ln(x),2)*pow(NC,-1)*CF - 10*pow(ln(x),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 19./2.\
      *pow(ln(x),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*pow(ln(x),2)*pow(NC,-1)*x*CF + 13*pow(ln(x),2)*\
      pow(NC,-1)*x*z*CF - 22*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 17*ln(x)*ln(z)*\
      pow(NC,-1)*CF*pow(omx,-1)
                result +=  + 6*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omz,-1) - 12*ln(x)*ln(z)*pow(NC,-1)*CF + 17*ln(x)*\
      ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 16*ln(x)*ln(z)*pow(NC,-1)*x*CF*pow(omz,-1) - 10*ln(x)*ln(\
      z)*pow(NC,-1)*x*CF - 22*ln(x)*ln(z)*pow(NC,-1)*x*z*CF - 16*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) + 11*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 3*ln(x)*ln(omx)*pow(NC,-1)\
      *CF*pow(omz,-1) - 6*ln(x)*ln(omx)*pow(NC,-1)*CF + 11*ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 13*ln(x)*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) - 10*ln(x)*ln(omx)*pow(NC,-1)*x*CF - \
      16*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 20*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)\
       + 16*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) - \
      12*ln(x)*ln(omz)*pow(NC,-1)*CF + 16*ln(x)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + 14*ln(x)*ln(\
      omz)*pow(NC,-1)*x*CF*pow(omz,-1) - 8*ln(x)*ln(omz)*pow(NC,-1)*x*CF - 20*ln(x)*ln(omz)*pow(\
      NC,-1)*x*z*CF + 4*ln(x)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 3*ln(x)*ln(xmz)*pow(\
      NC,-1)*CF*pow(omx,-1) - ln(x)*ln(xmz)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(x)*ln(xmz)*pow(NC,-1)*\
      CF - 3*ln(x)*ln(xmz)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*ln(x)*ln(xmz)*pow(NC,-1)*x*CF*pow(\
      omz,-1) + 2*ln(x)*ln(xmz)*pow(NC,-1)*x*CF + 4*ln(x)*ln(xmz)*pow(NC,-1)*x*z*CF + 8*ln(z)*pow(\
      NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 8*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(z)*pow(NC,-1)*\
      x*CF*pow(omz,-1)
                result +=  + 8*ln(z)*pow(NC,-1)*x*z*CF + 8*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - \
      6*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) - 2*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1) + 4*pow(\
      ln(z),2)*pow(NC,-1)*CF - 6*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*pow(ln(z),2)*pow(\
      NC,-1)*x*CF*pow(omz,-1) + 4*pow(ln(z),2)*pow(NC,-1)*x*CF + 8*pow(ln(z),2)*pow(NC,-1)*x*z*CF\
       + 12*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 8*ln(z)*ln(omx)*pow(NC,-1)*CF*\
      pow(omx,-1) - 2*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) + 4*ln(z)*ln(omx)*pow(NC,-1)*CF - 8*\
      ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 10*ln(z)*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) + 8*\
      ln(z)*ln(omx)*pow(NC,-1)*x*CF + 12*ln(z)*ln(omx)*pow(NC,-1)*x*z*CF + 14*ln(z)*ln(omz)*pow(\
      NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 12*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 5*ln(z)*ln(\
      omz)*pow(NC,-1)*CF*pow(omz,-1) + 10*ln(z)*ln(omz)*pow(NC,-1)*CF - 12*ln(z)*ln(omz)*pow(NC,-1)\
      *z*CF*pow(omx,-1) - 9*ln(z)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 4*ln(z)*ln(omz)*pow(NC,-1)*\
      x*CF + 14*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF - 4*ln(z)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) + 3*ln(z)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1) + ln(z)*ln(xmz)*pow(NC,-1)*CF*pow(omz,-1)\
       - 2*ln(z)*ln(xmz)*pow(NC,-1)*CF + 3*ln(z)*ln(xmz)*pow(NC,-1)*z*CF*pow(omx,-1) + 3*ln(z)*ln(\
      xmz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(z)*ln(xmz)*pow(NC,-1)*x*CF - 4*ln(z)*ln(xmz)*pow(\
      NC,-1)*x*z*CF
                result +=  + 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(omx)*pow(NC,-1)*z*CF*pow(\
      omx,-1) - 6*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*ln(omx)*pow(NC,-1)*x*z*CF + 5*pow(ln(omx)\
      ,2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 3*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) - 1./2.\
      *pow(ln(omx),2)*pow(NC,-1)*CF*pow(omz,-1) + pow(ln(omx),2)*pow(NC,-1)*CF - 3*pow(ln(omx),2)*\
      pow(NC,-1)*z*CF*pow(omx,-1) - 9./2.*pow(ln(omx),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 4*pow(ln(omx\
      ),2)*pow(NC,-1)*x*CF + 5*pow(ln(omx),2)*pow(NC,-1)*x*z*CF + 8*ln(omx)*ln(omz)*pow(NC,-1)*CF*\
      pow(omx,-1)*pow(omz,-1) - 6*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(omx)*ln(omz)*\
      pow(NC,-1)*CF*pow(omz,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)*CF - 6*ln(omx)*ln(omz)*pow(NC,-1)*z*\
      CF*pow(omx,-1) - 6*ln(omx)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)\
      *x*CF + 8*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF + 6*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)\
       - 6*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*ln(omz)*\
      pow(NC,-1)*x*z*CF - 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 2*ln(omz)*\
      ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1) + ln(omz)*ln( - omxmz)*pow(NC,-1)*CF*pow(omz,-1) - 2*\
      ln(omz)*ln( - omxmz)*pow(NC,-1)*CF + 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) + ln(\
      omz)*ln( - omxmz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*x*z*CF + 5*\
      pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)
                result +=  - 9./2.*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) - 2*pow(ln(omz),2)*pow(NC,-1)*CF*\
      pow(omz,-1) + 4*pow(ln(omz),2)*pow(NC,-1)*CF - 9./2.*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(\
      omx,-1) - 3*pow(ln(omz),2)*pow(NC,-1)*x*CF*pow(omz,-1) + pow(ln(omz),2)*pow(NC,-1)*x*CF + 5*\
      pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) + Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) + Li2(pow(\
      x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) + 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*\
      pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x*CF - 2*Li2(pow(\
      x,-1)*z*omx*pow(omz,-1))*pow(NC,-1)*x*z*CF - 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*CF*pow(omx,-1)*\
      pow(omz,-1) + 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*CF*pow(omx,-1) + Li2(pow(z,-1)*omx)*pow(NC,-1)*\
      CF*pow(omz,-1) - 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*CF + 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*z*CF*\
      pow(omx,-1) + Li2(pow(z,-1)*omx)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(pow(z,-1)*omx)*pow(\
      NC,-1)*x*z*CF + Li2(omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) + Li2(omx*pow(omz,-1))*pow(\
      NC,-1)*CF*pow(omz,-1) - 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*CF + Li2(omx*pow(omz,-1))*pow(\
      NC,-1)*z*CF*pow(omx,-1) - Li2(omx*pow(omz,-1))*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(omx*pow(\
      omz,-1))*pow(NC,-1)*x*CF + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1)
                result +=  - 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) - Li2(x*pow(z,-1)*omx*\
      pow(omz,-1))*pow(NC,-1)*CF*pow(omz,-1) + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF - 2\
      *Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*x*z*CF\
       - 2*Li2(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + Li2(z)*pow(NC,-1)*CF*pow(omx,-1) + Li2(z)\
      *pow(NC,-1)*z*CF*pow(omx,-1) + 2*Li2(z)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(z)*pow(NC,-1)*x*\
      CF - 2*Li2(z)*pow(NC,-1)*x*z*CF
            if z < round(1 - x, ndecimals) and z > x:
                result += 4*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(NC,-1)*CF*pow(omz,-1) - 6*pow(NC,-1)*CF - 8./3.*pow(\
      NC,-1)*pow(pi,2)*CF*pow(omx,-1)*pow(omz,-1) + 13./6.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1) + 5./\
      6.*pow(NC,-1)*pow(pi,2)*CF*pow(omz,-1) - 5./3.*pow(NC,-1)*pow(pi,2)*CF - 4*pow(NC,-1)*z*CF*\
      pow(omx,-1) + 13./6.*pow(NC,-1)*z*pow(pi,2)*CF*pow(omx,-1) - 4*pow(NC,-1)*x*CF*pow(omz,-1) + \
      11./6.*pow(NC,-1)*x*pow(pi,2)*CF*pow(omz,-1) - pow(NC,-1)*x*pow(pi,2)*CF - 8./3.*pow(NC,-1)*x\
      *z*pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 12*ln(x)*pow(NC,-1)*z*CF*\
      pow(omx,-1) + 12*ln(x)*pow(NC,-1)*x*CF*pow(omz,-1) - 12*ln(x)*pow(NC,-1)*x*z*CF + 4*ln(x)*ln(\
       - xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 3*ln(x)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1)\
       - ln(x)*ln( - xmz)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(x)*ln( - xmz)*pow(NC,-1)*CF - 3*ln(x)*\
      ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*ln(x)*ln( - xmz)*pow(NC,-1)*x*CF*pow(omz,-1) + 2*\
      ln(x)*ln( - xmz)*pow(NC,-1)*x*CF + 4*ln(x)*ln( - xmz)*pow(NC,-1)*x*z*CF + 14*pow(ln(x),2)*\
      pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 21./2.*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) - 7./2.\
      *pow(ln(x),2)*pow(NC,-1)*CF*pow(omz,-1) + 7*pow(ln(x),2)*pow(NC,-1)*CF - 21./2.*pow(ln(x),2)*\
      pow(NC,-1)*z*CF*pow(omx,-1) - 21./2.*pow(ln(x),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 7*pow(ln(x),2\
      )*pow(NC,-1)*x*CF + 14*pow(ln(x),2)*pow(NC,-1)*x*z*CF - 24*ln(x)*ln(z)*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1)
                result +=  + 18*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omz,-1)\
       - 12*ln(x)*ln(z)*pow(NC,-1)*CF + 18*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 18*ln(x)*ln(z)\
      *pow(NC,-1)*x*CF*pow(omz,-1) - 12*ln(x)*ln(z)*pow(NC,-1)*x*CF - 24*ln(x)*ln(z)*pow(NC,-1)*x*z\
      *CF - 18*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 12*ln(x)*ln(omx)*pow(NC,-1)*CF\
      *pow(omx,-1) + 3*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) - 6*ln(x)*ln(omx)*pow(NC,-1)*CF + 12\
      *ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 15*ln(x)*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) - \
      12*ln(x)*ln(omx)*pow(NC,-1)*x*CF - 18*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 18*ln(x)*ln(omz)*pow(\
      NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 15*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(x)*ln(\
      omz)*pow(NC,-1)*CF*pow(omz,-1) - 12*ln(x)*ln(omz)*pow(NC,-1)*CF + 15*ln(x)*ln(omz)*pow(NC,-1)\
      *z*CF*pow(omx,-1) + 12*ln(x)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) - 6*ln(x)*ln(omz)*pow(NC,-1)\
      *x*CF - 18*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + 2*ln(x)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) - 2*ln(x)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1) - ln(x)*ln(omxmz)*pow(NC,-1)*CF*pow(\
      omz,-1) + 2*ln(x)*ln(omxmz)*pow(NC,-1)*CF - 2*ln(x)*ln(omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - \
      ln(x)*ln(omxmz)*pow(NC,-1)*x*CF*pow(omz,-1) + 2*ln(x)*ln(omxmz)*pow(NC,-1)*x*z*CF + 8*ln(z)*\
      pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 8*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(z)*pow(\
      NC,-1)*x*CF*pow(omz,-1)
                result +=  + 8*ln(z)*pow(NC,-1)*x*z*CF - 4*ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) + 3*ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1) + ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(\
      omz,-1) - 2*ln(z)*ln( - xmz)*pow(NC,-1)*CF + 3*ln(z)*ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 3*ln(z)*ln( - xmz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(z)*ln( - xmz)*pow(NC,-1)*x*CF - 4*\
      ln(z)*ln( - xmz)*pow(NC,-1)*x*z*CF + 10*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - \
      15./2.*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) - 5./2.*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1)\
       + 5*pow(ln(z),2)*pow(NC,-1)*CF - 15./2.*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 15./2.*\
      pow(ln(z),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 5*pow(ln(z),2)*pow(NC,-1)*x*CF + 10*pow(ln(z),2)*\
      pow(NC,-1)*x*z*CF + 12*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 7*ln(z)*ln(omx)*\
      pow(NC,-1)*CF*pow(omx,-1) - ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(z)*ln(omx)*pow(\
      NC,-1)*CF - 7*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 11*ln(z)*ln(omx)*pow(NC,-1)*x*CF*\
      pow(omz,-1) + 10*ln(z)*ln(omx)*pow(NC,-1)*x*CF + 12*ln(z)*ln(omx)*pow(NC,-1)*x*z*CF + 12*ln(z\
      )*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 11*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)\
       - 5*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) + 10*ln(z)*ln(omz)*pow(NC,-1)*CF - 11*ln(z)*ln(\
      omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 7*ln(z)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 2*ln(z)*ln(\
      omz)*pow(NC,-1)*x*CF
                result +=  + 12*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF + 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) - 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*\
      ln(omx)*pow(NC,-1)*x*z*CF + 7*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 5*pow(\
      ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) - 3./2.*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omz,-1) + 3*\
      pow(ln(omx),2)*pow(NC,-1)*CF - 5*pow(ln(omx),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 11./2.*pow(ln(\
      omx),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*x*CF + 7*pow(ln(omx),2)*\
      pow(NC,-1)*x*z*CF + 6*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 4*ln(omx)*ln(\
      omz)*pow(NC,-1)*CF*pow(omx,-1) - ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(omx)*ln(omz\
      )*pow(NC,-1)*CF - 4*ln(omx)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 5*ln(omx)*ln(omz)*pow(\
      NC,-1)*x*CF*pow(omz,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)*x*CF + 6*ln(omx)*ln(omz)*pow(NC,-1)*x*\
      z*CF + 6*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(omz)*pow(NC,-1)*z*CF*pow(\
      omx,-1) - 6*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*ln(omz)*pow(NC,-1)*x*z*CF + 6*pow(ln(omz)\
      ,2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 11./2.*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1)\
       - 5./2.*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omz,-1) + 5*pow(ln(omz),2)*pow(NC,-1)*CF - 11./2.*\
      pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 7./2.*pow(ln(omz),2)*pow(NC,-1)*x*CF*pow(omz,-1)\
       + pow(ln(omz),2)*pow(NC,-1)*x*CF
                result +=  + 6*pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 2*ln(omz)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1)*\
      pow(omz,-1) + 2*ln(omz)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*CF\
      *pow(omz,-1) - 2*ln(omz)*ln(omxmz)*pow(NC,-1)*CF + 2*ln(omz)*ln(omxmz)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(omz)*ln(omxmz)*pow(NC,-1)*x*z*\
      CF - Li2(pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(\
      omz,-1) + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*CF - Li2(pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(pow(omx,-1)*omz)*pow(\
      NC,-1)*x*CF + 2*Li2(z*pow(omx,-1))*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 2*Li2(z*pow(\
      omx,-1))*pow(NC,-1)*CF*pow(omx,-1) - Li2(z*pow(omx,-1))*pow(NC,-1)*CF*pow(omz,-1) + 2*Li2(z*\
      pow(omx,-1))*pow(NC,-1)*CF - 2*Li2(z*pow(omx,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(z*pow(\
      omx,-1))*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(z*pow(omx,-1))*pow(NC,-1)*x*z*CF + 2*Li2(x*pow(\
      z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*\
      omz)*pow(NC,-1)*CF*pow(omx,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1)\
       - 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(x*pow(z,-1)*pow(\
      omx,-1)*omz)*pow(NC,-1)*x*CF + 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*x*z*CF + 2*Li2(x\
      *pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1)
                result +=  - 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) - Li2(x*pow(z,-1)*omx*\
      pow(omz,-1))*pow(NC,-1)*CF*pow(omz,-1) + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF - 2\
      *Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*x*z*CF\
       - 2*Li2(z)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + Li2(z)*pow(NC,-1)*CF*pow(omx,-1) + Li2(z)\
      *pow(NC,-1)*z*CF*pow(omx,-1) + 2*Li2(z)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(z)*pow(NC,-1)*x*\
      CF - 2*Li2(z)*pow(NC,-1)*x*z*CF
            if z > round(1 - x, ndecimals) and z > x:
                result += 4*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(NC,-1)*CF*pow(omz,-1) - 6*pow(NC,-1)*CF - 4./3.*pow(\
      NC,-1)*pow(pi,2)*CF*pow(omx,-1)*pow(omz,-1) + 5./6.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1) + 1./\
      6.*pow(NC,-1)*pow(pi,2)*CF*pow(omz,-1) - 1./3.*pow(NC,-1)*pow(pi,2)*CF - 4*pow(NC,-1)*z*CF*\
      pow(omx,-1) + 5./6.*pow(NC,-1)*z*pow(pi,2)*CF*pow(omx,-1) - 4*pow(NC,-1)*x*CF*pow(omz,-1) + 7.\
      /6.*pow(NC,-1)*x*pow(pi,2)*CF*pow(omz,-1) - pow(NC,-1)*x*pow(pi,2)*CF - 4./3.*pow(NC,-1)*x*z*\
      pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 12*ln(x)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 12*ln(x)*pow(NC,-1)*x*CF*pow(omz,-1) - 12*ln(x)*pow(NC,-1)*x*z*CF + 2*ln(x)*ln( - \
      omxmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 2*ln(x)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1)\
       - ln(x)*ln( - omxmz)*pow(NC,-1)*CF*pow(omz,-1) + 2*ln(x)*ln( - omxmz)*pow(NC,-1)*CF - 2*ln(x\
      )*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln( - omxmz)*pow(NC,-1)*x*CF*pow(omz,-1)\
       + 2*ln(x)*ln( - omxmz)*pow(NC,-1)*x*z*CF + 4*ln(x)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) - 3*ln(x)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1) - ln(x)*ln( - xmz)*pow(NC,-1)*CF*pow(\
      omz,-1) + 2*ln(x)*ln( - xmz)*pow(NC,-1)*CF - 3*ln(x)*ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1)\
       - 3*ln(x)*ln( - xmz)*pow(NC,-1)*x*CF*pow(omz,-1) + 2*ln(x)*ln( - xmz)*pow(NC,-1)*x*CF + 4*\
      ln(x)*ln( - xmz)*pow(NC,-1)*x*z*CF + 13*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - \
      19./2.*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1)
                result +=  - 3*pow(ln(x),2)*pow(NC,-1)*CF*pow(omz,-1) + 6*pow(ln(x),2)*pow(NC,-1)*CF - 19./2.*\
      pow(ln(x),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 10*pow(ln(x),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 7*\
      pow(ln(x),2)*pow(NC,-1)*x*CF + 13*pow(ln(x),2)*pow(NC,-1)*x*z*CF - 22*ln(x)*ln(z)*pow(NC,-1)*\
      CF*pow(omx,-1)*pow(omz,-1) + 16*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 5*ln(x)*ln(z)*pow(\
      NC,-1)*CF*pow(omz,-1) - 10*ln(x)*ln(z)*pow(NC,-1)*CF + 16*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 17*ln(x)*ln(z)*pow(NC,-1)*x*CF*pow(omz,-1) - 12*ln(x)*ln(z)*pow(NC,-1)*x*CF - 22*\
      ln(x)*ln(z)*pow(NC,-1)*x*z*CF - 20*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 14*\
      ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 4*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) - 8*ln(x)\
      *ln(omx)*pow(NC,-1)*CF + 14*ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 16*ln(x)*ln(omx)*pow(\
      NC,-1)*x*CF*pow(omz,-1) - 12*ln(x)*ln(omx)*pow(NC,-1)*x*CF - 20*ln(x)*ln(omx)*pow(NC,-1)*x*z*\
      CF - 16*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 13*ln(x)*ln(omz)*pow(NC,-1)*CF*\
      pow(omx,-1) + 5*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) - 10*ln(x)*ln(omz)*pow(NC,-1)*CF + 13\
      *ln(x)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + 11*ln(x)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) - 6\
      *ln(x)*ln(omz)*pow(NC,-1)*x*CF - 16*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + 8*ln(z)*pow(NC,-1)*CF*\
      pow(omx,-1)*pow(omz,-1) - 8*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(z)*pow(NC,-1)*x*CF*pow(\
      omz,-1)
                result +=  + 8*ln(z)*pow(NC,-1)*x*z*CF - 4*ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) + 3*ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1) + ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(\
      omz,-1) - 2*ln(z)*ln( - xmz)*pow(NC,-1)*CF + 3*ln(z)*ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 3*ln(z)*ln( - xmz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*ln(z)*ln( - xmz)*pow(NC,-1)*x*CF - 4*\
      ln(z)*ln( - xmz)*pow(NC,-1)*x*z*CF + 8*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - \
      11./2.*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) - 3./2.*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1)\
       + 3*pow(ln(z),2)*pow(NC,-1)*CF - 11./2.*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 13./2.*\
      pow(ln(z),2)*pow(NC,-1)*x*CF*pow(omz,-1) + 5*pow(ln(z),2)*pow(NC,-1)*x*CF + 8*pow(ln(z),2)*\
      pow(NC,-1)*x*z*CF + 16*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 11*ln(z)*ln(omx)\
      *pow(NC,-1)*CF*pow(omx,-1) - 3*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omz,-1) + 6*ln(z)*ln(omx)*pow(\
      NC,-1)*CF - 11*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 13*ln(z)*ln(omx)*pow(NC,-1)*x*CF*\
      pow(omz,-1) + 10*ln(z)*ln(omx)*pow(NC,-1)*x*CF + 16*ln(z)*ln(omx)*pow(NC,-1)*x*z*CF + 10*ln(z\
      )*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 9*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)\
       - 4*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) + 8*ln(z)*ln(omz)*pow(NC,-1)*CF - 9*ln(z)*ln(omz\
      )*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(z)*ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 2*ln(z)*ln(omz)\
      *pow(NC,-1)*x*CF
                result +=  + 10*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF + 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(\
      omz,-1) - 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*\
      ln(omx)*pow(NC,-1)*x*z*CF + 5*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 3*pow(\
      ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) - 1./2.*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omz,-1) + pow(\
      ln(omx),2)*pow(NC,-1)*CF - 3*pow(ln(omx),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 9./2.*pow(ln(omx),2\
      )*pow(NC,-1)*x*CF*pow(omz,-1) + 4*pow(ln(omx),2)*pow(NC,-1)*x*CF + 5*pow(ln(omx),2)*pow(\
      NC,-1)*x*z*CF + 8*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(omx)*ln(omz)*\
      pow(NC,-1)*CF*pow(omx,-1) - 2*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1) + 4*ln(omx)*ln(omz)*\
      pow(NC,-1)*CF - 6*ln(omx)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*ln(omz)*pow(NC,-1)*\
      x*CF*pow(omz,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)*x*CF + 8*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF + \
      6*ln(omz)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*\
      ln(omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 6*ln(omz)*pow(NC,-1)*x*z*CF - 2*ln(omz)*ln( - omxmz)*\
      pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1) + \
      ln(omz)*ln( - omxmz)*pow(NC,-1)*CF*pow(omz,-1) - 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*CF + 2*ln(\
      omz)*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) + ln(omz)*ln( - omxmz)*pow(NC,-1)*x*CF*pow(\
      omz,-1)
                result +=  - 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*x*z*CF + 5*pow(ln(omz),2)*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) - 9./2.*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) - 2*pow(ln(omz),2)*pow(\
      NC,-1)*CF*pow(omz,-1) + 4*pow(ln(omz),2)*pow(NC,-1)*CF - 9./2.*pow(ln(omz),2)*pow(NC,-1)*z*CF\
      *pow(omx,-1) - 3*pow(ln(omz),2)*pow(NC,-1)*x*CF*pow(omz,-1) + pow(ln(omz),2)*pow(NC,-1)*x*CF\
       + 5*pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) + 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1) + Li2(pow(\
      x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omz,-1) - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(\
      NC,-1)*CF + 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(pow(x,-1)*z*\
      pow(omx,-1)*omz)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*\
      x*z*CF - 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*CF*pow(omx,-1)*pow(omz,-1) + 2*Li2(pow(z,-1)*omx)*\
      pow(NC,-1)*CF*pow(omx,-1) + Li2(pow(z,-1)*omx)*pow(NC,-1)*CF*pow(omz,-1) - 2*Li2(pow(z,-1)*\
      omx)*pow(NC,-1)*CF + 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(pow(z,-1)*omx)*\
      pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*x*z*CF - Li2(pow(omx,-1)*omz)*\
      pow(NC,-1)*CF*pow(omx,-1) - Li2(pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omz,-1) + 2*Li2(pow(\
      omx,-1)*omz)*pow(NC,-1)*CF - Li2(pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(pow(\
      omx,-1)*omz)*pow(NC,-1)*x*CF*pow(omz,-1)
                result +=  - 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*CF + 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(\
      NC,-1)*CF*pow(omx,-1)*pow(omz,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(\
      omx,-1) - Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(x*pow(z,-1)*\
      pow(omx,-1)*omz)*pow(NC,-1)*x*CF*pow(omz,-1) + 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*\
      x*CF + 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*pow(NC,-1)*x*z*CF - 2*Li2(z)*pow(NC,-1)*CF*pow(\
      omx,-1)*pow(omz,-1) + Li2(z)*pow(NC,-1)*CF*pow(omx,-1) + Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 2*Li2(z)*pow(NC,-1)*x*CF*pow(omz,-1) - 2*Li2(z)*pow(NC,-1)*x*CF - 2*Li2(z)*pow(NC,-1)*x*z*\
      CF
            if z < round(1 - x, ndecimals):
                result += - NC*CF*pow(omx,-1) - NC*CF*pow(omz,-1) + 3*NC*CF + 4./3.*NC*pow(pi,2)*CF*pow(omx,-1)*\
      pow(omz,-1) - 2./3.*NC*pow(pi,2)*CF*pow(omx,-1) - 2./3.*NC*pow(pi,2)*CF*pow(omz,-1) + 4./3.*\
      NC*pow(pi,2)*CF + NC*z*CF*pow(omx,-1) - 2./3.*NC*z*pow(pi,2)*CF*pow(omx,-1) + NC*x*CF*pow(\
      omz,-1) - 2./3.*NC*x*pow(pi,2)*CF*pow(omz,-1) + 4./3.*NC*x*z*pow(pi,2)*CF + 6*ln(x)*NC*CF*\
      pow(omx,-1)*pow(omz,-1) + 9*ln(x)*NC*CF - 6*ln(x)*NC*z*CF*pow(omx,-1) - 6*ln(x)*NC*x*CF*pow(\
      omz,-1) - 6*ln(x)*NC*x*CF + 6*ln(x)*NC*x*z*CF - 7*pow(ln(x),2)*NC*CF*pow(omx,-1)*pow(omz,-1)\
       + 7./2.*pow(ln(x),2)*NC*CF*pow(omx,-1) + 7./2.*pow(ln(x),2)*NC*CF*pow(omz,-1) - 7*pow(ln(x),\
      2)*NC*CF + 7./2.*pow(ln(x),2)*NC*z*CF*pow(omx,-1) + 7./2.*pow(ln(x),2)*NC*x*CF*pow(omz,-1) - \
      7*pow(ln(x),2)*NC*x*z*CF + 6*ln(x)*ln(z)*NC*CF*pow(omx,-1)*pow(omz,-1) - 3*ln(x)*ln(z)*NC*CF*\
      pow(omx,-1) - 3*ln(x)*ln(z)*NC*CF*pow(omz,-1) + 6*ln(x)*ln(z)*NC*CF - 3*ln(x)*ln(z)*NC*z*CF*\
      pow(omx,-1) - 3*ln(x)*ln(z)*NC*x*CF*pow(omz,-1) + 6*ln(x)*ln(z)*NC*x*z*CF + 12*ln(x)*ln(omx)*\
      NC*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(x)*ln(omx)*NC*CF*pow(omx,-1) - 6*ln(x)*ln(omx)*NC*CF*\
      pow(omz,-1) + 12*ln(x)*ln(omx)*NC*CF - 6*ln(x)*ln(omx)*NC*z*CF*pow(omx,-1) - 6*ln(x)*ln(omx)*\
      NC*x*CF*pow(omz,-1) + 12*ln(x)*ln(omx)*NC*x*z*CF + 12*ln(x)*ln(omz)*NC*CF*pow(omx,-1)*pow(\
      omz,-1) - 6*ln(x)*ln(omz)*NC*CF*pow(omx,-1) - 6*ln(x)*ln(omz)*NC*CF*pow(omz,-1) + 12*ln(x)*\
      ln(omz)*NC*CF
                result +=  - 6*ln(x)*ln(omz)*NC*z*CF*pow(omx,-1) - 6*ln(x)*ln(omz)*NC*x*CF*pow(omz,-1) + 12*ln(x\
      )*ln(omz)*NC*x*z*CF - 2*ln(x)*ln(omxmz)*NC*CF*pow(omx,-1)*pow(omz,-1) + ln(x)*ln(omxmz)*NC*CF\
      *pow(omx,-1) + ln(x)*ln(omxmz)*NC*CF*pow(omz,-1) - 2*ln(x)*ln(omxmz)*NC*CF + ln(x)*ln(omxmz)*\
      NC*z*CF*pow(omx,-1) + ln(x)*ln(omxmz)*NC*x*CF*pow(omz,-1) - 2*ln(x)*ln(omxmz)*NC*x*z*CF - 2*\
      ln(z)*NC*CF*pow(omx,-1)*pow(omz,-1) - 3*ln(z)*NC*CF + 2*ln(z)*NC*z*CF*pow(omx,-1) + 2*ln(z)*\
      NC*x*CF*pow(omz,-1) + 2*ln(z)*NC*x*CF - 2*ln(z)*NC*x*z*CF - pow(ln(z),2)*NC*CF*pow(omx,-1)*\
      pow(omz,-1) + 1./2.*pow(ln(z),2)*NC*CF*pow(omx,-1) + 1./2.*pow(ln(z),2)*NC*CF*pow(omz,-1) - \
      pow(ln(z),2)*NC*CF + 1./2.*pow(ln(z),2)*NC*z*CF*pow(omx,-1) + 1./2.*pow(ln(z),2)*NC*x*CF*pow(\
      omz,-1) - pow(ln(z),2)*NC*x*z*CF - 4*ln(z)*ln(omx)*NC*CF*pow(omx,-1)*pow(omz,-1) + 2*ln(z)*\
      ln(omx)*NC*CF*pow(omx,-1) + 2*ln(z)*ln(omx)*NC*CF*pow(omz,-1) - 4*ln(z)*ln(omx)*NC*CF + 2*ln(\
      z)*ln(omx)*NC*z*CF*pow(omx,-1) + 2*ln(z)*ln(omx)*NC*x*CF*pow(omz,-1) - 4*ln(z)*ln(omx)*NC*x*z\
      *CF - 4*ln(z)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) + 2*ln(z)*ln(omz)*NC*CF*pow(omx,-1) + 2*\
      ln(z)*ln(omz)*NC*CF*pow(omz,-1) - 4*ln(z)*ln(omz)*NC*CF + 2*ln(z)*ln(omz)*NC*z*CF*pow(omx,-1)\
       + 2*ln(z)*ln(omz)*NC*x*CF*pow(omz,-1) - 4*ln(z)*ln(omz)*NC*x*z*CF - 4*ln(omx)*NC*CF*pow(\
      omx,-1)*pow(omz,-1) - 6*ln(omx)*NC*CF + 4*ln(omx)*NC*z*CF*pow(omx,-1) + 4*ln(omx)*NC*x*CF*\
      pow(omz,-1)
                result +=  + 4*ln(omx)*NC*x*CF - 4*ln(omx)*NC*x*z*CF - 4*pow(ln(omx),2)*NC*CF*pow(omx,-1)*pow(\
      omz,-1) + 2*pow(ln(omx),2)*NC*CF*pow(omx,-1) + 2*pow(ln(omx),2)*NC*CF*pow(omz,-1) - 4*pow(ln(\
      omx),2)*NC*CF + 2*pow(ln(omx),2)*NC*z*CF*pow(omx,-1) + 2*pow(ln(omx),2)*NC*x*CF*pow(omz,-1)\
       - 4*pow(ln(omx),2)*NC*x*z*CF - 10*ln(omx)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) + 5*ln(omx)*\
      ln(omz)*NC*CF*pow(omx,-1) + 5*ln(omx)*ln(omz)*NC*CF*pow(omz,-1) - 10*ln(omx)*ln(omz)*NC*CF + \
      5*ln(omx)*ln(omz)*NC*z*CF*pow(omx,-1) + 5*ln(omx)*ln(omz)*NC*x*CF*pow(omz,-1) - 10*ln(omx)*\
      ln(omz)*NC*x*z*CF - 4*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(omz)*NC*CF + 4*ln(omz)*NC*\
      z*CF*pow(omx,-1) + 4*ln(omz)*NC*x*CF*pow(omz,-1) + 4*ln(omz)*NC*x*CF - 4*ln(omz)*NC*x*z*CF - \
      5*pow(ln(omz),2)*NC*CF*pow(omx,-1)*pow(omz,-1) + 5./2.*pow(ln(omz),2)*NC*CF*pow(omx,-1) + 5./\
      2.*pow(ln(omz),2)*NC*CF*pow(omz,-1) - 5*pow(ln(omz),2)*NC*CF + 5./2.*pow(ln(omz),2)*NC*z*CF*\
      pow(omx,-1) + 5./2.*pow(ln(omz),2)*NC*x*CF*pow(omz,-1) - 5*pow(ln(omz),2)*NC*x*z*CF + 2*ln(\
      omz)*ln(omxmz)*NC*CF*pow(omx,-1)*pow(omz,-1) - ln(omz)*ln(omxmz)*NC*CF*pow(omx,-1) - ln(omz)*\
      ln(omxmz)*NC*CF*pow(omz,-1) + 2*ln(omz)*ln(omxmz)*NC*CF - ln(omz)*ln(omxmz)*NC*z*CF*pow(\
      omx,-1) - ln(omz)*ln(omxmz)*NC*x*CF*pow(omz,-1) + 2*ln(omz)*ln(omxmz)*NC*x*z*CF + 2*Li2(z*\
      pow(omx,-1))*NC*CF*pow(omx,-1)*pow(omz,-1) - Li2(z*pow(omx,-1))*NC*CF*pow(omx,-1) - Li2(z*\
      pow(omx,-1))*NC*CF*pow(omz,-1)
                result +=  + 2*Li2(z*pow(omx,-1))*NC*CF - Li2(z*pow(omx,-1))*NC*z*CF*pow(omx,-1) - Li2(z*pow(\
      omx,-1))*NC*x*CF*pow(omz,-1) + 2*Li2(z*pow(omx,-1))*NC*x*z*CF - 2*Li2(x*z*pow(omx,-1)*pow(\
      omz,-1))*NC*CF*pow(omx,-1)*pow(omz,-1) + Li2(x*z*pow(omx,-1)*pow(omz,-1))*NC*CF*pow(omx,-1)\
       + Li2(x*z*pow(omx,-1)*pow(omz,-1))*NC*CF*pow(omz,-1) - 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*NC\
      *CF + Li2(x*z*pow(omx,-1)*pow(omz,-1))*NC*z*CF*pow(omx,-1) + Li2(x*z*pow(omx,-1)*pow(omz,-1))\
      *NC*x*CF*pow(omz,-1) - 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*NC*x*z*CF - 2*Li2(z)*NC*CF*pow(\
      omx,-1)*pow(omz,-1) + Li2(z)*NC*CF*pow(omx,-1) + Li2(z)*NC*CF*pow(omz,-1) - 2*Li2(z)*NC*CF + \
      Li2(z)*NC*z*CF*pow(omx,-1) + Li2(z)*NC*x*CF*pow(omz,-1) - 2*Li2(z)*NC*x*z*CF
            if z > round(1 - x, ndecimals):
                result += - NC*CF*pow(omx,-1) - NC*CF*pow(omz,-1) + 3*NC*CF + 4./3.*NC*pow(pi,2)*CF*pow(omx,-1)*\
      pow(omz,-1) - 2./3.*NC*pow(pi,2)*CF*pow(omx,-1) - 2./3.*NC*pow(pi,2)*CF*pow(omz,-1) + 4./3.*\
      NC*pow(pi,2)*CF + NC*z*CF*pow(omx,-1) - 2./3.*NC*z*pow(pi,2)*CF*pow(omx,-1) + NC*x*CF*pow(\
      omz,-1) - 2./3.*NC*x*pow(pi,2)*CF*pow(omz,-1) + 4./3.*NC*x*z*pow(pi,2)*CF + 6*ln(x)*NC*CF*\
      pow(omx,-1)*pow(omz,-1) + 9*ln(x)*NC*CF - 6*ln(x)*NC*z*CF*pow(omx,-1) - 6*ln(x)*NC*x*CF*pow(\
      omz,-1) - 6*ln(x)*NC*x*CF + 6*ln(x)*NC*x*z*CF - 2*ln(x)*ln( - omxmz)*NC*CF*pow(omx,-1)*pow(\
      omz,-1) + ln(x)*ln( - omxmz)*NC*CF*pow(omx,-1) + ln(x)*ln( - omxmz)*NC*CF*pow(omz,-1) - 2*ln(\
      x)*ln( - omxmz)*NC*CF + ln(x)*ln( - omxmz)*NC*z*CF*pow(omx,-1) + ln(x)*ln( - omxmz)*NC*x*CF*\
      pow(omz,-1) - 2*ln(x)*ln( - omxmz)*NC*x*z*CF - 6*pow(ln(x),2)*NC*CF*pow(omx,-1)*pow(omz,-1)\
       + 3*pow(ln(x),2)*NC*CF*pow(omx,-1) + 3*pow(ln(x),2)*NC*CF*pow(omz,-1) - 6*pow(ln(x),2)*NC*CF\
       + 3*pow(ln(x),2)*NC*z*CF*pow(omx,-1) + 3*pow(ln(x),2)*NC*x*CF*pow(omz,-1) - 6*pow(ln(x),2)*\
      NC*x*z*CF + 8*ln(x)*ln(z)*NC*CF*pow(omx,-1)*pow(omz,-1) - 4*ln(x)*ln(z)*NC*CF*pow(omx,-1) - 4\
      *ln(x)*ln(z)*NC*CF*pow(omz,-1) + 8*ln(x)*ln(z)*NC*CF - 4*ln(x)*ln(z)*NC*z*CF*pow(omx,-1) - 4*\
      ln(x)*ln(z)*NC*x*CF*pow(omz,-1) + 8*ln(x)*ln(z)*NC*x*z*CF + 10*ln(x)*ln(omx)*NC*CF*pow(\
      omx,-1)*pow(omz,-1) - 5*ln(x)*ln(omx)*NC*CF*pow(omx,-1) - 5*ln(x)*ln(omx)*NC*CF*pow(omz,-1)\
       + 10*ln(x)*ln(omx)*NC*CF
                result +=  - 5*ln(x)*ln(omx)*NC*z*CF*pow(omx,-1) - 5*ln(x)*ln(omx)*NC*x*CF*pow(omz,-1) + 10*ln(x\
      )*ln(omx)*NC*x*z*CF + 10*ln(x)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) - 5*ln(x)*ln(omz)*NC*CF*\
      pow(omx,-1) - 5*ln(x)*ln(omz)*NC*CF*pow(omz,-1) + 10*ln(x)*ln(omz)*NC*CF - 5*ln(x)*ln(omz)*NC\
      *z*CF*pow(omx,-1) - 5*ln(x)*ln(omz)*NC*x*CF*pow(omz,-1) + 10*ln(x)*ln(omz)*NC*x*z*CF - 2*ln(z\
      )*NC*CF*pow(omx,-1)*pow(omz,-1) - 3*ln(z)*NC*CF + 2*ln(z)*NC*z*CF*pow(omx,-1) + 2*ln(z)*NC*x*\
      CF*pow(omz,-1) + 2*ln(z)*NC*x*CF - 2*ln(z)*NC*x*z*CF - pow(ln(z),2)*NC*CF*pow(omx,-1)*pow(\
      omz,-1) + 1./2.*pow(ln(z),2)*NC*CF*pow(omx,-1) + 1./2.*pow(ln(z),2)*NC*CF*pow(omz,-1) - pow(\
      ln(z),2)*NC*CF + 1./2.*pow(ln(z),2)*NC*z*CF*pow(omx,-1) + 1./2.*pow(ln(z),2)*NC*x*CF*pow(\
      omz,-1) - pow(ln(z),2)*NC*x*z*CF - 4*ln(z)*ln(omx)*NC*CF*pow(omx,-1)*pow(omz,-1) + 2*ln(z)*\
      ln(omx)*NC*CF*pow(omx,-1) + 2*ln(z)*ln(omx)*NC*CF*pow(omz,-1) - 4*ln(z)*ln(omx)*NC*CF + 2*ln(\
      z)*ln(omx)*NC*z*CF*pow(omx,-1) + 2*ln(z)*ln(omx)*NC*x*CF*pow(omz,-1) - 4*ln(z)*ln(omx)*NC*x*z\
      *CF - 6*ln(z)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) + 3*ln(z)*ln(omz)*NC*CF*pow(omx,-1) + 3*\
      ln(z)*ln(omz)*NC*CF*pow(omz,-1) - 6*ln(z)*ln(omz)*NC*CF + 3*ln(z)*ln(omz)*NC*z*CF*pow(omx,-1)\
       + 3*ln(z)*ln(omz)*NC*x*CF*pow(omz,-1) - 6*ln(z)*ln(omz)*NC*x*z*CF - 4*ln(omx)*NC*CF*pow(\
      omx,-1)*pow(omz,-1) - 6*ln(omx)*NC*CF + 4*ln(omx)*NC*z*CF*pow(omx,-1) + 4*ln(omx)*NC*x*CF*\
      pow(omz,-1)
                result +=  + 4*ln(omx)*NC*x*CF - 4*ln(omx)*NC*x*z*CF - 4*pow(ln(omx),2)*NC*CF*pow(omx,-1)*pow(\
      omz,-1) + 2*pow(ln(omx),2)*NC*CF*pow(omx,-1) + 2*pow(ln(omx),2)*NC*CF*pow(omz,-1) - 4*pow(ln(\
      omx),2)*NC*CF + 2*pow(ln(omx),2)*NC*z*CF*pow(omx,-1) + 2*pow(ln(omx),2)*NC*x*CF*pow(omz,-1)\
       - 4*pow(ln(omx),2)*NC*x*z*CF - 8*ln(omx)*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) + 4*ln(omx)*\
      ln(omz)*NC*CF*pow(omx,-1) + 4*ln(omx)*ln(omz)*NC*CF*pow(omz,-1) - 8*ln(omx)*ln(omz)*NC*CF + 4\
      *ln(omx)*ln(omz)*NC*z*CF*pow(omx,-1) + 4*ln(omx)*ln(omz)*NC*x*CF*pow(omz,-1) - 8*ln(omx)*ln(\
      omz)*NC*x*z*CF - 4*ln(omz)*NC*CF*pow(omx,-1)*pow(omz,-1) - 6*ln(omz)*NC*CF + 4*ln(omz)*NC*z*\
      CF*pow(omx,-1) + 4*ln(omz)*NC*x*CF*pow(omz,-1) + 4*ln(omz)*NC*x*CF - 4*ln(omz)*NC*x*z*CF + 2*\
      ln(omz)*ln( - omxmz)*NC*CF*pow(omx,-1)*pow(omz,-1) - ln(omz)*ln( - omxmz)*NC*CF*pow(omx,-1)\
       - ln(omz)*ln( - omxmz)*NC*CF*pow(omz,-1) + 2*ln(omz)*ln( - omxmz)*NC*CF - ln(omz)*ln( - \
      omxmz)*NC*z*CF*pow(omx,-1) - ln(omz)*ln( - omxmz)*NC*x*CF*pow(omz,-1) + 2*ln(omz)*ln( - omxmz\
      )*NC*x*z*CF - 4*pow(ln(omz),2)*NC*CF*pow(omx,-1)*pow(omz,-1) + 2*pow(ln(omz),2)*NC*CF*pow(\
      omx,-1) + 2*pow(ln(omz),2)*NC*CF*pow(omz,-1) - 4*pow(ln(omz),2)*NC*CF + 2*pow(ln(omz),2)*NC*z\
      *CF*pow(omx,-1) + 2*pow(ln(omz),2)*NC*x*CF*pow(omz,-1) - 4*pow(ln(omz),2)*NC*x*z*CF + 2*Li2(\
      pow(x,-1)*pow(z,-1)*omx*omz)*NC*CF*pow(omx,-1)*pow(omz,-1) - Li2(pow(x,-1)*pow(z,-1)*omx*omz)\
      *NC*CF*pow(omx,-1)
                result +=  - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*NC*CF*pow(omz,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*omx*\
      omz)*NC*CF - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*NC*z*CF*pow(omx,-1) - Li2(pow(x,-1)*pow(z,-1)*\
      omx*omz)*NC*x*CF*pow(omz,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*NC*x*z*CF - 2*Li2(pow(z,-1)\
      *omx)*NC*CF*pow(omx,-1)*pow(omz,-1) + Li2(pow(z,-1)*omx)*NC*CF*pow(omx,-1) + Li2(pow(z,-1)*\
      omx)*NC*CF*pow(omz,-1) - 2*Li2(pow(z,-1)*omx)*NC*CF + Li2(pow(z,-1)*omx)*NC*z*CF*pow(omx,-1)\
       + Li2(pow(z,-1)*omx)*NC*x*CF*pow(omz,-1) - 2*Li2(pow(z,-1)*omx)*NC*x*z*CF - 2*Li2(z)*NC*CF*\
      pow(omx,-1)*pow(omz,-1) + Li2(z)*NC*CF*pow(omx,-1) + Li2(z)*NC*CF*pow(omz,-1) - 2*Li2(z)*NC*\
      CF + Li2(z)*NC*z*CF*pow(omx,-1) + Li2(z)*NC*x*CF*pow(omz,-1) - 2*Li2(z)*NC*x*z*CF
        elif orders == '001':
            if z != x and z != round(1 - x, ndecimals):
                result += + 1./2.*LMUA*pow(NC,-1)*CF + 2*LMUA*pow(NC,-1)*x*CF + 1./2.*LMUA*pow(NC,-1)*x*z*CF + 1./3.*\
      LMUA*pow(z,-1)*CF + 1./2.*LMUA*CF - 3./2.*LMUA*z*CF + 2./3.*LMUA*pow(z,2)*CF + 1./3.*LMUA*x*\
      pow(z,-1)*CF + 3./2.*LMUA*x*CF - 1./2.*LMUA*x*z*CF - 4./3.*LMUA*x*pow(z,2)*CF - 1./2.*LMUA*NC\
      *CF - 2*LMUA*NC*x*CF - 1./2.*LMUA*NC*x*z*CF + ln(x)*LMUA*pow(NC,-1)*CF*pow(omx,-1) - 1./2.*ln(x)*LMUA*\
      pow(NC,-1)*CF + ln(x)*LMUA*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*ln(x)*LMUA*pow(NC,-1)*z*CF - 1.\
      /2.*ln(x)*LMUA*pow(NC,-1)*x*CF - 1./2.*ln(x)*LMUA*pow(NC,-1)*x*z*CF - ln(x)*LMUA*NC*CF*pow(\
      omx,-1) + 1./2.*ln(x)*LMUA*NC*CF - ln(x)*LMUA*NC*z*CF*pow(omx,-1) + 1./2.*ln(x)*LMUA*NC*z*CF\
       + 1./2.*ln(x)*LMUA*NC*x*CF + 1./2.*ln(x)*LMUA*NC*x*z*CF + ln(z)*LMUA*pow(NC,-1)*\
      CF*pow(omz,-1) - 3./2.*ln(z)*LMUA*pow(NC,-1)*CF - 1./2.*ln(z)*LMUA*pow(NC,-1)*z*CF + ln(z)*\
      LMUA*pow(NC,-1)*x*CF*pow(omz,-1) - 1./2.*ln(z)*LMUA*pow(NC,-1)*x*CF - 3./2.*ln(z)*LMUA*pow(\
      NC,-1)*x*z*CF + ln(z)*LMUA*CF + ln(z)*LMUA*x*CF + 2*ln(z)*LMUA*x*z*CF - ln(z)*LMUA*NC*CF*pow(\
      omz,-1) + 3./2.*ln(z)*LMUA*NC*CF + 1./2.*ln(z)*LMUA*NC*z*CF - ln(z)*LMUA*NC*x*CF*pow(omz,-1)\
       + 1./2.*ln(z)*LMUA*NC*x*CF + 3./2.*ln(z)*LMUA*NC*x*z*CF + 1./2.*ln(omx)*LMUA*pow(NC,-1)*CF + 1./2.*ln(omx)*LMUA*pow(\
      NC,-1)*z*CF + 1./2.*ln(omx)*LMUA*pow(NC,-1)*x*CF + 1./2.*ln(omx)*LMUA*pow(NC,-1)*x*z*CF - 1./\
      2.*ln(omx)*LMUA*NC*CF - 1./2.*ln(omx)*LMUA*NC*z*CF - 1./2.*ln(omx)*LMUA*NC*x*CF - 1./2.*ln(\
      omx)*LMUA*NC*x*z*CF + 5./2.*ln(omz)*LMUA*pow(NC,-1)*CF + 1./2.*ln(omz)*LMUA*pow(NC,-1)*\
      z*CF + 1./2.*ln(omz)*LMUA*pow(NC,-1)*x*CF + 5./2.*ln(omz)*LMUA*pow(NC,-1)*x*z*CF - 5./2.*ln(\
      omz)*LMUA*NC*CF - 1./2.*ln(omz)*LMUA*NC*z*CF - 1./2.*ln(omz)*LMUA*NC*x*CF - 5./2.*ln(omz)*\
      LMUA*NC*x*z*CF
        elif orders == '010':
            if z != x and z != round(1 - x, ndecimals):
                result += + 1./2.*LMUF*pow(NC,-1)*CF + 2*LMUF*pow(NC,-1)*z*CF + 1./2.*LMUF\
      *pow(NC,-1)*x*z*CF - 2./3.*LMUF*pow(x,-1)*pow(z,-1)*CF + 4./3.*LMUF*pow(x,-1)*CF - 1./2.*LMUF\
      *pow(z,-1)*CF + LMUF*CF + 1./2.*LMUF*x*pow(z,-1)*CF - LMUF*x*CF + 2./3.*LMUF*pow(x,2)*pow(\
      z,-1)*CF - 4./3.*LMUF*pow(x,2)*CF - 1./2.*LMUF*NC*CF - 2*LMUF*NC*z*CF - 1./2.*LMUF*NC*x*z*CF \
      + ln(x)*LMUF*pow(NC,-1)*CF*pow(omx,-1) - 3./2.*ln(x)*LMUF*pow(NC,-1)*CF + ln(x)*\
      LMUF*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*ln(x)*LMUF*pow(NC,-1)*z*CF - 1./2.*ln(x)*LMUF*pow(\
      NC,-1)*x*CF - 3./2.*ln(x)*LMUF*pow(NC,-1)*x*z*CF - ln(x)*LMUF*pow(z,-1)*CF + 2*ln(x)*LMUF*CF\
       - ln(x)*LMUF*x*pow(z,-1)*CF + 2*ln(x)*LMUF*x*CF - ln(x)*LMUF*NC*CF*pow(omx,-1) + 3./2.*ln(x)\
      *LMUF*NC*CF - ln(x)*LMUF*NC*z*CF*pow(omx,-1) + 1./2.*ln(x)*LMUF*NC*z*CF + 1./2.*ln(x)*LMUF*NC\
      *x*CF + 3./2.*ln(x)*LMUF*NC*x*z*CF - ln(z)*LMUF*pow(NC,-1)*CF*pow(omz,-1) + 1./2.*ln(\
      z)*LMUF*pow(NC,-1)*CF + 1./2.*ln(z)*LMUF*pow(NC,-1)*z*CF - ln(z)*LMUF*pow(NC,-1)*x*CF*pow(\
      omz,-1) + 1./2.*ln(z)*LMUF*pow(NC,-1)*x*CF + 1./2.*ln(z)*LMUF*pow(NC,-1)*x*z*CF + ln(z)*LMUF*\
      NC*CF*pow(omz,-1) - 1./2.*ln(z)*LMUF*NC*CF - 1./2.*ln(z)*LMUF*NC*z*CF + ln(z)*LMUF*NC*x*CF*\
      pow(omz,-1) - 1./2.*ln(z)*LMUF*NC*x*CF - 1./2.*ln(z)*LMUF*NC*x*z*CF + 5./2.*ln(omx)*\
      LMUF*pow(NC,-1)*CF + 1./2.*ln(omx)*LMUF*pow(NC,-1)*z*CF + 1./2.*ln(omx)*LMUF*pow(NC,-1)*x*CF\
       + 5./2.*ln(omx)*LMUF*pow(NC,-1)*x*z*CF - 5./2.*ln(omx)*LMUF*NC*CF - 1./2.*ln(omx)*LMUF*NC*z*CF - 1./2.*ln(omx)*LMUF*NC*x*CF\
       - 5./2.*ln(omx)*LMUF*NC*x*z*CF + 1./2.*ln(omz)*LMUF*pow(NC,-1)*CF + 1./2.*ln(omz)*\
      LMUF*pow(NC,-1)*z*CF + 1./2.*ln(omz)*LMUF*pow(NC,-1)*x*CF + 1./2.*ln(omz)*LMUF*pow(NC,-1)*x*z\
      *CF - 1./2.*ln(omz)*LMUF*NC*CF - 1./2.*ln(omz)*LMUF*NC*z*CF - 1./2.*ln(omz)*LMUF*NC*x*CF - 1./\
      2.*ln(omz)*LMUF*NC*x*z*CF
        elif orders == '100':
            if z != x and z != round(1 - x, ndecimals):
                result += + 11./3.*LMUR*NC*CF + 11./3.*LMUR*NC*x*z*CF - 2./3.*LMUR*NF*CF - 2./3.*LMUR*NF*x*z*CF
        elif orders == '011':
            if z != x and z != round(1 - x, ndecimals):
                result += - 1./2.*LMUA*LMUF*pow(NC,-1)*CF - 1./2.*LMUA*LMUF*pow(NC,-1)*z*CF - 1./2.*LMUA*LMUF*pow(NC,-1)*x*CF - 1./2.*LMUA*LMUF*pow(NC,-1)*x*z*CF + 1./2.*LMUA*LMUF*NC*CF + 1./2.*LMUA*LMUF*NC*z*CF + 1./2.*LMUA*LMUF*NC*x*CF + 1./2.*LMUA*LMUF*NC*x*z*CF
        return result
    elif rsl == 'rs':
        result = 0
        if orders == '000':
            result_r0 = - pow(NC,-1)*CF - 5./12.*pow(NC,-1)*pow(pi,2)*CF - 7*pow(NC,-1)*x*CF - 5./12.*pow(NC,-1)*x\
      *pow(pi,2)*CF + 13./9.*pow(x,-1)*CF - 11./6.*CF + 1./6.*pow(pi,2)*CF + 17./6.*x*CF + 1./6.*x*\
      pow(pi,2)*CF - 22./9.*pow(x,2)*CF + 19./9.*NC*CF + 7./12.*NC*pow(pi,2)*CF - 14./9.*NC*x*CF + \
      7./12.*NC*x*pow(pi,2)*CF + 2./9.*NF*CF + 8./9.*NF*x*CF + 3./2.*ln(x)*pow(NC,-1)*CF*pow(omx,-1)\
       + 3./2.*ln(x)*pow(NC,-1)*x*CF + ln(x)*CF + 3*ln(x)*x*CF + 2*ln(x)*pow(x,2)*CF + 35./6.*ln(x)\
      *NC*CF*pow(omx,-1) - 8./3.*ln(x)*NC*CF - 25./6.*ln(x)*NC*x*CF - 4./3.*ln(x)*NF*CF*pow(omx,-1)\
       + 2./3.*ln(x)*NF*CF + 2./3.*ln(x)*NF*x*CF - pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) + \
      pow(ln(x),2)*pow(NC,-1)*CF + pow(ln(x),2)*pow(NC,-1)*x*CF - pow(ln(x),2)*CF - pow(ln(x),2)*x*\
      CF + 2*pow(ln(x),2)*NC*CF*pow(omx,-1) - 3./2.*pow(ln(x),2)*NC*CF - 3./2.*pow(ln(x),2)*NC*x*CF\
       + 6*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) - 3*ln(x)*ln(omx)*pow(NC,-1)*CF - 3*ln(x)*ln(omx\
      )*pow(NC,-1)*x*CF - 6*ln(x)*ln(omx)*NC*CF*pow(omx,-1) + 3*ln(x)*ln(omx)*NC*CF + 3*ln(x)*ln(\
      omx)*NC*x*CF + 2./3.*ln(omx)*pow(x,-1)*CF + 1./2.*ln(omx)*CF - 1./2.*ln(omx)*x*CF - 2./3.*ln(\
      omx)*pow(x,2)*CF + 11./6.*ln(omx)*NC*CF + 11./6.*ln(omx)*NC*x*CF - 1./3.*ln(omx)*NF*CF - 1./3.\
      *ln(omx)*NF*x*CF + 3./2.*pow(ln(omx),2)*pow(NC,-1)*CF + 3./2.*\
      pow(ln(omx),2)*pow(NC,-1)*x*CF - 3./2.*pow(ln(omx),2)*NC*CF - 3./2.*pow(ln(omx),2)*NC*x*CF + \
      1./2.*Li2(x)*pow(NC,-1)*CF + 1./2.*Li2(x)*pow(NC,-1)*x*CF - Li2(x)*CF - Li2(x)*x*CF - 1./2.*\
      Li2(x)*NC*CF - 1./2.*Li2(x)*NC*x*CF
            result_r1 = 2./3.*pow(x,-1)*CF + 1./2.*CF - 1./2.*x*CF - 2./3.*pow(x,2)*CF + 11./6.*NC*CF + 11./6.*NC*x\
      *CF - 1./3.*NF*CF - 1./3.*NF*x*CF + 4*ln(x)*pow(NC,-1)*CF*pow(omx,-1) - 5./2.*ln(x)*pow(NC,-1)*CF - 5./2.*ln(x)*pow(NC,-1)*x*\
      CF + ln(x)*CF + ln(x)*x*CF - 4*ln(x)*NC*CF*pow(omx,-1) + 5./2.*ln(x)*NC*CF + 5./2.*ln(x)*NC*x\
      *CF + 3*ln(omx)*pow(NC,-1)*CF + 3*ln(omx)*pow(NC,-1)*x*CF - 3*ln(omx)*NC*CF - 3*ln(omx)*NC*x*CF
            result_r2 = 3./2.*pow(NC,-1)*CF + 3./2.*pow(NC,-1)*x*CF - 3./2.*NC*CF - 3./2.*NC*x*CF
            result += result_r0*1/(1-z) + result_r1*ln(1-z)/(1-z) + result_r2*ln(1-z)*ln(1-z)/(1-z)
        elif orders == '001':
            result_r0 = - ln(omx)*LMUA*pow(NC,-1)*CF - ln(omx)*LMUA*pow(NC,-1)*x*CF + ln(omx)*LMUA*NC*CF + ln(omx)*LMUA*NC*x*CF - ln(x)*LMUA*NC*CF - ln(x)*LMUA*NC*x*CF\
      + 1./4.*LMUA*pow(NC,-1)*CF - 7./4.*LMUA*pow(NC,-1)*x*CF - 1./4.*LMUA*NC*CF + 7./4.*LMUA*NC*x*CF - 2*ln(x)*LMUA*pow(NC,-1)*CF*pow(omx,-1) + ln(x)*LMUA*pow(NC,-1)*CF + ln(x)*LMUA*pow(NC,-1)*x*CF + 2*ln(x)*LMUA*NC*CF*pow(omx,-1)
            result_r1 = - 2*LMUA*pow(NC,-1)*CF - 2*LMUA*pow(NC,-1)*x*CF + 2*LMUA*NC*CF + 2*LMUA*NC*x*CF
            result += result_r0*1/(1-z) + result_r1*ln(1-z)/(1-z)
        elif orders == '010':
            result_r0 = - 2*ln(omx)*LMUF*pow(NC,-1)*CF - 2*ln(omx)*LMUF*pow(NC,-1)*x*CF + 2*ln(omx)*\
      LMUF*NC*CF + 2*ln(omx)*LMUF*NC*x*CF - 7./4.*LMUF*pow(NC,-1)*CF + 1./4.*LMUF*pow(\
      NC,-1)*x*CF - 2./3.*LMUF*pow(x,-1)*CF - 1./2.*LMUF*CF + 1./2.*LMUF*x*CF + 2./3.*LMUF*pow(x,2)\
      *CF + 7./4.*LMUF*NC*CF - 1./4.*LMUF*NC*x*CF - 2*ln(x)*LMUF*pow(NC,-1)*CF*pow(omx,-1) + 3./2.*\
      ln(x)*LMUF*pow(NC,-1)*CF + 3./2.*ln(x)*LMUF*pow(NC,-1)*x*CF - ln(x)*LMUF*CF - ln(x)*LMUF*x*CF\
       + 2*ln(x)*LMUF*NC*CF*pow(omx,-1) - 3./2.*ln(x)*LMUF*NC*CF - 3./2.*ln(x)*LMUF*NC*x*CF
            result_r1 = - LMUF*pow(NC,-1)*CF - LMUF*pow(NC,-1)*x*CF + LMUF*NC*CF + LMUF*NC*x*CF
            result += result_r0*1/(1-z) + result_r1*ln(1-z)/(1-z)
        elif orders == '100':
            result_r0 = - 11./6.*LMUR*NC*CF - 11./6.*LMUR*NC*x*CF + 1./3.*LMUR*NF*CF + 1./3.*LMUR*NF*x*CF
            result += result_r0*1/(1-z)
        elif orders == '011':
            result_r0 = + LMUA*LMUF*pow(NC,-1)*CF + LMUA*LMUF*pow(NC,-1)*x*CF - LMUA*LMUF*NC*CF - LMUA*LMUF*NC*x*CF
            result += result_r0*1/(1-z)
        return result
    elif rsl == 'rl':
        result = 0
        if orders == '000':
            result += 29./4.*pow(NC,-1)*CF - 7*pow(NC,-1)*zeta3*CF*pow(omx,-1) + 11./2.*pow(NC,-1)*zeta3*CF + 1./\
      4.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1) - 1./6.*pow(NC,-1)*pow(pi,2)*CF - 31./4.*pow(NC,-1)*x*\
      CF + 11./2.*pow(NC,-1)*x*zeta3*CF + 5./12.*pow(NC,-1)*x*pow(pi,2)*CF + 52./27.*pow(x,-1)*CF\
       - 41./36.*CF + 1./6.*pow(pi,2)*CF + 17./36.*x*CF + 1./2.*x*pow(pi,2)*CF - 34./27.*pow(x,2)*\
      CF + 1./3.*pow(x,2)*pow(pi,2)*CF - 91./108.*NC*CF + 5*NC*zeta3*CF*pow(omx,-1) - 8*NC*zeta3*CF\
       + 13./36.*NC*pow(pi,2)*CF*pow(omx,-1) - 13./36.*NC*pow(pi,2)*CF + 845./108.*NC*x*CF - 8*NC*x\
      *zeta3*CF - 7./9.*NC*x*pow(pi,2)*CF - 37./54.*NF*CF - 1./9.*NF*pow(pi,2)*CF*pow(omx,-1) + 1./\
      9.*NF*pow(pi,2)*CF - 19./54.*NF*x*CF + 1./9.*NF*x*pow(pi,2)*CF
            result +=  - 10*ln(x)*pow(NC,-1)*CF*pow(omx,-1) + 21./4.*ln(x)*pow(NC,-1)*CF - ln(x)*pow(NC,-1)*pow(pi,2)*CF*\
      pow(omx,-1) + 2./3.*ln(x)*pow(NC,-1)*pow(pi,2)*CF + 11*ln(x)*pow(NC,-1)*x*CF + 2./3.*ln(x)*\
      pow(NC,-1)*x*pow(pi,2)*CF + 23./6.*ln(x)*CF - 1./3.*ln(x)*pow(pi,2)*CF - 5./6.*ln(x)*x*CF - 1.\
      /3.*ln(x)*x*pow(pi,2)*CF + 38./9.*ln(x)*pow(x,2)*CF - 5./3.*ln(x)*NC*CF*pow(omx,-1) + 1./12.*\
      ln(x)*NC*CF + 5./3.*ln(x)*NC*pow(pi,2)*CF*pow(omx,-1) - ln(x)*NC*pow(pi,2)*CF + 13./6.*ln(x)*\
      NC*x*CF - ln(x)*NC*x*pow(pi,2)*CF + 5./3.*ln(x)*NF*CF*pow(omx,-1) - 5./6.*ln(x)*NF*CF - 7./6.\
      *ln(x)*NF*x*CF
            result += - 9./8.*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) + 1./4.*pow(ln(x),2)*pow(NC,-1)*CF - 3.\
      /2.*pow(ln(x),2)*pow(NC,-1)*x*CF - 13./8.*pow(ln(x),2)*CF - 13./8.*pow(ln(x),2)*x*CF - 5./3.*\
      pow(ln(x),2)*pow(x,2)*CF - 83./24.*pow(ln(x),2)*NC*CF*pow(omx,-1) + 49./24.*pow(ln(x),2)*NC*\
      CF + 55./24.*pow(ln(x),2)*NC*x*CF + 5./6.*pow(ln(x),2)*NF*CF*pow(omx,-1) - 5./12.*pow(ln(x),2\
      )*NF*CF - 5./12.*pow(ln(x),2)*NF*x*CF
            result +=  - 5./24.*pow(ln(x),3)*pow(NC,-1)*CF - 5./24.*pow(ln(x),3)*pow(NC,-1)*x*CF + 5./12.*\
      pow(ln(x),3)*CF + 5./12.*pow(ln(x),3)*x*CF - 1./2.*pow(ln(x),3)*NC*CF*pow(omx,-1) + 11./24.*\
      pow(ln(x),3)*NC*CF + 11./24.*pow(ln(x),3)*NC*x*CF - 9./2.*pow(ln(x),2)*ln(omx)*pow(NC,-1)*CF*\
      pow(omx,-1) + 9./4.*pow(ln(x),2)*ln(omx)*pow(NC,-1)*CF + 9./4.*pow(ln(x),2)*ln(omx)*pow(\
      NC,-1)*x*CF + 5./2.*pow(ln(x),2)*ln(omx)*NC*CF*pow(omx,-1) - 5./4.*pow(ln(x),2)*ln(omx)*NC*CF\
       - 5./4.*pow(ln(x),2)*ln(omx)*NC*x*CF + 1./2.*ln(x)*ln(omx)*pow(NC,-1)*CF - 1./2.*ln(x)*ln(\
      omx)*pow(NC,-1)*x*CF - 2./3.*ln(x)*ln(omx)*pow(x,-1)*CF - 1./2.*ln(x)*ln(omx)*CF + 1./2.*ln(x\
      )*ln(omx)*x*CF + 2./3.*ln(x)*ln(omx)*pow(x,2)*CF + 11./3.*ln(x)*ln(omx)*NC*CF*pow(omx,-1) - 7.\
      /3.*ln(x)*ln(omx)*NC*CF - 4./3.*ln(x)*ln(omx)*NC*x*CF - 2./3.*ln(x)*ln(omx)*NF*CF*pow(omx,-1)\
       + 1./3.*ln(x)*ln(omx)*NF*CF + 1./3.*ln(x)*ln(omx)*NF*x*CF + 5./2.*ln(x)*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) - ln(x)*pow(ln(omx),2)*pow(\
      NC,-1)*CF - ln(x)*pow(ln(omx),2)*pow(NC,-1)*x*CF - 1./2.*ln(x)*pow(ln(omx),2)*CF - 1./2.*ln(x\
      )*pow(ln(omx),2)*x*CF - 9./2.*ln(x)*pow(ln(omx),2)*NC*CF*pow(omx,-1) + 2*ln(x)*pow(ln(omx),2)\
      *NC*CF
            result +=  + 2*ln(x)*pow(ln(omx),2)*NC*x*CF - 5*ln(x)*Li2(x)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x)\
      *Li2(x)*pow(NC,-1)*CF + 2*ln(x)*Li2(x)*pow(NC,-1)*x*CF + ln(x)*Li2(x)*CF + ln(x)*Li2(x)*x*CF\
       + ln(x)*Li2(x)*NC*CF*pow(omx,-1) - ln(omx)*pow(NC,-1)*CF + 1./6.*ln(omx)*pow(NC,-1)*pow(\
      pi,2)*CF*pow(omx,-1) - 1./2.*ln(omx)*pow(NC,-1)*pow(pi,2)*CF - 27./4.*ln(omx)*pow(NC,-1)*x*CF\
       - 1./2.*ln(omx)*pow(NC,-1)*x*pow(pi,2)*CF + 13./9.*ln(omx)*pow(x,-1)*CF - 11./6.*ln(omx)*CF\
       + 1./6.*ln(omx)*pow(pi,2)*CF + 17./6.*ln(omx)*x*CF + 1./6.*ln(omx)*x*pow(pi,2)*CF - 22./9.*\
      ln(omx)*pow(x,2)*CF + 19./9.*ln(omx)*NC*CF + 1./6.*ln(omx)*NC*pow(pi,2)*CF*pow(omx,-1) + 1./2.\
      *ln(omx)*NC*pow(pi,2)*CF - 47./36.*ln(omx)*NC*x*CF + 1./2.*ln(omx)*NC*x*pow(pi,2)*CF + 2./9.*\
      ln(omx)*NF*CF + 8./9.*ln(omx)*NF*x*CF
            result +=  + 1./3.*pow(ln(omx),2)*pow(x,-1)*CF + 1./4.*pow(ln(omx),2)*CF - 1./4.*pow(ln(omx),2)*\
      x*CF - 1./3.*pow(ln(omx),2)*pow(x,2)*CF + 11./12.*pow(ln(omx),2)*NC*CF + 11./12.*pow(ln(omx),\
      2)*NC*x*CF - 1./6.*pow(ln(omx),2)*NF*CF - 1./6.*pow(ln(omx),2)*NF*x*CF + 1./2.*pow(ln(omx),3)*pow(NC,-1)*CF + 1./2.*pow(\
      ln(omx),3)*pow(NC,-1)*x*CF - 1./2.*pow(ln(omx),3)*NC*CF - 1./2.*pow(ln(omx),3)*NC*x*CF - ln(\
      omx)*Li2(x)*pow(NC,-1)*CF*pow(omx,-1) + ln(omx)*Li2(x)*pow(NC,-1)*CF + ln(omx)*Li2(x)*pow(\
      NC,-1)*x*CF - ln(omx)*Li2(x)*CF - ln(omx)*Li2(x)*x*CF - ln(omx)*Li2(x)*NC*CF*pow(omx,-1) - 3*\
      Li3(1 - x)*pow(NC,-1)*CF*pow(omx,-1) + 2*Li3(1 - x)*pow(NC,-1)*CF + 2*Li3(1 - x)*pow(NC,-1)*x\
      *CF - Li3(1 - x)*CF - Li3(1 - x)*x*CF - 5*Li3(1 - x)*NC*CF*pow(omx,-1) + 2*Li3(1 - x)*NC*CF\
       + 2*Li3(1 - x)*NC*x*CF + 7*Li3(x)*pow(NC,-1)*CF*pow(omx,-1) - 7./2.*Li3(x)*pow(NC,-1)*CF - 7.\
      /2.*Li3(x)*pow(NC,-1)*x*CF - 5*Li3(x)*NC*CF*pow(omx,-1) + 5./2.*Li3(x)*NC*CF + 5./2.*Li3(x)*\
      NC*x*CF - 3./2.*Li2(x)*pow(NC,-1)*CF*pow(omx,-1) - 3./2.*Li2(x)*pow(NC,-1)*x*CF - 2./3.*Li2(x\
      )*pow(x,-1)*CF - 3./2.*Li2(x)*CF - 5./2.*Li2(x)*x*CF - 4./3.*Li2(x)*pow(x,2)*CF - 13./6.*Li2(\
      x)*NC*CF*pow(omx,-1) + 5./6.*Li2(x)*NC*CF + 7./3.*Li2(x)*NC*x*CF + 2./3.*Li2(x)*NF*CF*pow(\
      omx,-1) - 1./3.*Li2(x)*NF*CF - 1./3.*Li2(x)*NF*x*CF
            result_r0 = - pow(NC,-1)*CF - 5./12.*pow(NC,-1)*pow(pi,2)*CF - 7*pow(NC,-1)*x*CF - 5./12.*pow(NC,-1)*x\
      *pow(pi,2)*CF + 13./9.*pow(x,-1)*CF - 11./6.*CF + 1./6.*pow(pi,2)*CF + 17./6.*x*CF + 1./6.*x*\
      pow(pi,2)*CF - 22./9.*pow(x,2)*CF + 19./9.*NC*CF + 7./12.*NC*pow(pi,2)*CF - 14./9.*NC*x*CF + \
      7./12.*NC*x*pow(pi,2)*CF + 2./9.*NF*CF + 8./9.*NF*x*CF + 3./2.*ln(x)*pow(NC,-1)*CF*pow(omx,-1)\
       + 3./2.*ln(x)*pow(NC,-1)*x*CF + ln(x)*CF + 3*ln(x)*x*CF + 2*ln(x)*pow(x,2)*CF + 35./6.*ln(x)\
      *NC*CF*pow(omx,-1) - 8./3.*ln(x)*NC*CF - 25./6.*ln(x)*NC*x*CF - 4./3.*ln(x)*NF*CF*pow(omx,-1)\
       + 2./3.*ln(x)*NF*CF + 2./3.*ln(x)*NF*x*CF - pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) + \
      pow(ln(x),2)*pow(NC,-1)*CF + pow(ln(x),2)*pow(NC,-1)*x*CF - pow(ln(x),2)*CF - pow(ln(x),2)*x*\
      CF + 2*pow(ln(x),2)*NC*CF*pow(omx,-1) - 3./2.*pow(ln(x),2)*NC*CF - 3./2.*pow(ln(x),2)*NC*x*CF\
       + 6*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) - 3*ln(x)*ln(omx)*pow(NC,-1)*CF - 3*ln(x)*ln(omx\
      )*pow(NC,-1)*x*CF - 6*ln(x)*ln(omx)*NC*CF*pow(omx,-1) + 3*ln(x)*ln(omx)*NC*CF + 3*ln(x)*ln(\
      omx)*NC*x*CF + 2./3.*ln(omx)*pow(x,-1)*CF + 1./2.*ln(omx)*CF - 1./2.*ln(omx)*x*CF - 2./3.*ln(\
      omx)*pow(x,2)*CF + 11./6.*ln(omx)*NC*CF + 11./6.*ln(omx)*NC*x*CF - 1./3.*ln(omx)*NF*CF - 1./3.\
      *ln(omx)*NF*x*CF + 3./2.*pow(ln(omx),2)*pow(NC,-1)*CF + 3./2.*\
      pow(ln(omx),2)*pow(NC,-1)*x*CF - 3./2.*pow(ln(omx),2)*NC*CF - 3./2.*pow(ln(omx),2)*NC*x*CF + \
      1./2.*Li2(x)*pow(NC,-1)*CF + 1./2.*Li2(x)*pow(NC,-1)*x*CF - Li2(x)*CF - Li2(x)*x*CF - 1./2.*\
      Li2(x)*NC*CF - 1./2.*Li2(x)*NC*x*CF
            result_r1 = 2./3.*pow(x,-1)*CF + 1./2.*CF - 1./2.*x*CF - 2./3.*pow(x,2)*CF + 11./6.*NC*CF + 11./6.*NC*x\
      *CF - 1./3.*NF*CF - 1./3.*NF*x*CF + 4*ln(x)*pow(NC,-1)*CF*pow(omx,-1) - 5./2.*ln(x)*pow(NC,-1)*CF - 5./2.*ln(x)*pow(NC,-1)*x*\
      CF + ln(x)*CF + ln(x)*x*CF - 4*ln(x)*NC*CF*pow(omx,-1) + 5./2.*ln(x)*NC*CF + 5./2.*ln(x)*NC*x\
      *CF + 3*ln(omx)*pow(NC,-1)*CF + 3*ln(omx)*pow(NC,-1)*x*CF - 3*ln(omx)*NC*CF - 3*ln(omx)*NC*x*CF
            result_r2 = 3./2.*pow(NC,-1)*CF + 3./2.*pow(NC,-1)*x*CF - 3./2.*NC*CF - 3./2.*NC*x*CF
            result += result_r0*ln(1-z) + result_r1*ln(1-z)*ln(1-z)/2 + result_r2*ln(1-z)*ln(1-z)*ln(1-z)/3
        elif orders == '001':
            result += + 3./4.*LMUA*pow(NC,-1)*CF + 1./6.*LMUA*pow(NC,-1)*pow(pi,2)*CF - 3./4.*LMUA*\
      pow(NC,-1)*x*CF + 1./6.*LMUA*pow(NC,-1)*x*pow(pi,2)*CF - 3./4.*LMUA*NC*CF - 1./6.*LMUA*NC*\
      pow(pi,2)*CF + 3./4.*LMUA*NC*x*CF - 1./6.*LMUA*NC*x*pow(pi,2)*CF - 3./4.*ln(omx)*LMUA*pow(\
      NC,-1)*CF - 3./4.*ln(omx)*LMUA*pow(NC,-1)*x*CF + 3./4.*ln(omx)*LMUA*NC*CF + 3./4.*ln(omx)*\
      LMUA*NC*x*CF - 3./2.*ln(x)*LMUA*pow(NC,-1)*CF*pow(omx,-1) + 3./4.*ln(x)*LMUA*pow(NC,-1)*CF + 3./4.*ln(x)*LMUA*pow(\
      NC,-1)*x*CF + 3./2.*ln(x)*LMUA*NC*CF*pow(omx,-1) - 3./4.*ln(x)*LMUA*NC*CF - 3./4.*ln(x)*LMUA*NC*x*CF
            result_r0 = - ln(omx)*LMUA*pow(NC,-1)*CF - ln(omx)*LMUA*pow(NC,-1)*x*CF + ln(omx)*LMUA*NC*CF + ln(omx)*LMUA*NC*x*CF - ln(x)*LMUA*NC*CF - ln(x)*LMUA*NC*x*CF\
      + 1./4.*LMUA*pow(NC,-1)*CF - 7./4.*LMUA*pow(NC,-1)*x*CF - 1./4.*LMUA*NC*CF + 7./4.*LMUA*NC*x*CF - 2*ln(x)*LMUA*pow(NC,-1)*CF*pow(omx,-1) + ln(x)*LMUA*pow(NC,-1)*CF + ln(x)*LMUA*pow(NC,-1)*x*CF + 2*ln(x)*LMUA*NC*CF*pow(omx,-1)
            result_r1 = - 2*LMUA*pow(NC,-1)*CF - 2*LMUA*pow(NC,-1)*x*CF + 2*LMUA*NC*CF + 2*LMUA*NC*x*CF
            result += result_r0*ln(1-z) + result_r1*ln(1-z)*ln(1-z)/2
        elif orders == '010':
            result += - 1./2.*Li2(x)*LMUF*pow(NC,-1)*CF - 1./2.*Li2(x)*LMUF*pow(NC,-1)*x*CF + Li2(x)*LMUF*CF + Li2(x)*LMUF*x*CF + 1./2.*Li2(x)*LMUF*NC*CF + \
      1./2.*Li2(x)*LMUF*NC*x*CF - 3./2.*pow(ln(omx),2)*LMUF*pow(NC,-1)*CF - 3./2.*pow(ln(omx),2)*LMUF*pow(NC,-1)*x*CF + 3./2.*pow(ln(omx),2)*LMUF*\
      NC*CF + 3./2.*pow(ln(omx),2)*LMUF*NC*x*CF + 7./4.*LMUF*pow(NC,-1)*CF + 1./4.*LMUF*\
      pow(NC,-1)*pow(pi,2)*CF + 25./4.*LMUF*pow(NC,-1)*x*CF + 1./4.*LMUF*pow(NC,-1)*x*pow(pi,2)*CF\
       - 13./9.*LMUF*pow(x,-1)*CF + 11./6.*LMUF*CF - 1./6.*LMUF*pow(pi,2)*CF - 17./6.*LMUF*x*CF - 1.\
      /6.*LMUF*x*pow(pi,2)*CF + 22./9.*LMUF*pow(x,2)*CF - 169./36.*LMUF*NC*CF - 5./12.*LMUF*NC*pow(\
      pi,2)*CF + 149./36.*LMUF*NC*x*CF - 5./12.*LMUF*NC*x*pow(pi,2)*CF + 1./9.*LMUF*NF*CF - 11./9.*\
      LMUF*NF*x*CF - 3./4.*ln(omx)*LMUF*pow(NC,-1)*CF\
       - 3./4.*ln(omx)*LMUF*pow(NC,-1)*x*CF - 2./3.*ln(omx)*LMUF*pow(x,-1)*CF - 1./2.*ln(omx)*LMUF*\
      CF + 1./2.*ln(omx)*LMUF*x*CF + 2./3.*ln(omx)*LMUF*pow(x,2)*CF + 3./4.*ln(omx)*LMUF*NC*CF + 3./\
      4.*ln(omx)*LMUF*NC*x*CF - 6*ln(x)*ln(omx)*LMUF*pow(NC,-1)*\
      CF*pow(omx,-1) + 3*ln(x)*ln(omx)*LMUF*pow(NC,-1)*CF + 3*ln(x)*ln(omx)*LMUF*pow(NC,-1)*x*CF + \
      6*ln(x)*ln(omx)*LMUF*NC*CF*pow(omx,-1) - 3*ln(x)*ln(omx)*LMUF*NC*CF - 3*ln(x)*ln(omx)*LMUF*NC\
      *x*CF - 3*ln(x)*LMUF*pow(NC,-1)*CF*pow(omx,-1) + 3./4.*ln(x)*LMUF*pow(NC,-1)*CF - 3./4.\
      *ln(x)*LMUF*pow(NC,-1)*x*CF - ln(x)*LMUF*CF - 3*ln(x)*LMUF*x*CF - 2*ln(x)*LMUF*pow(x,2)*CF - 2./3.*ln(x)*LMUF*NC*\
      CF*pow(omx,-1) + 1./12.*ln(x)*LMUF*NC*CF + 19./12.*ln(x)*LMUF*NC*x*CF + 2./3.*ln(x)*LMUF*NF*\
      CF*pow(omx,-1) - 1./3.*ln(x)*LMUF*NF*CF - 1./3.*ln(x)*LMUF*NF*x*CF + pow(ln(x),2)*LMUF*pow(NC,-1)*CF*pow(omx,-1) - pow(ln(\
      x),2)*LMUF*pow(NC,-1)*CF - pow(ln(x),2)*LMUF*pow(NC,-1)*x*CF + pow(ln(x),2)*LMUF*CF + pow(ln(\
      x),2)*LMUF*x*CF - 2*pow(ln(x),2)*LMUF*NC*CF*pow(omx,-1) + 3./2.*pow(ln(x),2)*LMUF*NC*CF + 3./2.*pow(ln(x),2)*LMUF*NC*x*CF
            result_r0 = - 2*ln(omx)*LMUF*pow(NC,-1)*CF - 2*ln(omx)*LMUF*pow(NC,-1)*x*CF + 2*ln(omx)*\
      LMUF*NC*CF + 2*ln(omx)*LMUF*NC*x*CF - 7./4.*LMUF*pow(NC,-1)*CF + 1./4.*LMUF*pow(\
      NC,-1)*x*CF - 2./3.*LMUF*pow(x,-1)*CF - 1./2.*LMUF*CF + 1./2.*LMUF*x*CF + 2./3.*LMUF*pow(x,2)\
      *CF + 7./4.*LMUF*NC*CF - 1./4.*LMUF*NC*x*CF - 2*ln(x)*LMUF*pow(NC,-1)*CF*pow(omx,-1) + 3./2.*\
      ln(x)*LMUF*pow(NC,-1)*CF + 3./2.*ln(x)*LMUF*pow(NC,-1)*x*CF - ln(x)*LMUF*CF - ln(x)*LMUF*x*CF\
       + 2*ln(x)*LMUF*NC*CF*pow(omx,-1) - 3./2.*ln(x)*LMUF*NC*CF - 3./2.*ln(x)*LMUF*NC*x*CF
            result_r1 = - LMUF*pow(NC,-1)*CF - LMUF*pow(NC,-1)*x*CF + LMUF*NC*CF + LMUF*NC*x*CF
            result += result_r0*ln(1-z) + result_r1*ln(1-z)*ln(1-z)/2
        elif orders == '100':
            result += + 11./6.*LMUR*NC*CF - 11./6.*LMUR*NC*x*CF - 1./3.*LMUR*NF*CF + 1./3.*LMUR*NF*x*CF - 11./6.*ln(omx)*LMUR*NC*CF - 11./6.*ln(omx)*LMUR*NC*x*\
      CF + 1./3.*ln(omx)*LMUR*NF*CF + 1./3.*ln(omx)*LMUR*NF*x*CF - 11./3.*ln(x)*LMUR*NC*CF*pow(omx,-1) + 11./6.*ln(x)*LMUR*NC*CF + 11./6.*ln(x)\
      *LMUR*NC*x*CF + 2./3.*ln(x)*LMUR*NF*CF*pow(omx,-1) - 1./3.*ln(x)*LMUR*NF*CF - 1./3.*ln(x)*LMUR*NF*x*CF
            result_r0 = - 11./6.*LMUR*NC*CF - 11./6.*LMUR*NC*x*CF + 1./3.*LMUR*NF*CF + 1./3.*LMUR*NF*x*CF
            result += result_r0*ln(1-z)
        elif orders == '011':
            result += + 3./4.*LMUA*LMUF*pow(NC,-1)*CF + 3./4.*LMUA*LMUF*pow(NC,-1)*x*CF - 3./4.*LMUA*LMUF*NC*CF - 3./4.*LMUA*LMUF*NC*x*CF
            result_r0 = + LMUA*LMUF*pow(NC,-1)*CF + LMUA*LMUF*pow(NC,-1)*x*CF - LMUA*LMUF*NC*CF - LMUA*LMUF*NC*x*CF
            result += result_r0*ln(1-z)
        elif orders == '110':
            result += + 11./6.*LMUF*LMUR*NC*CF + 11./6.*LMUF*LMUR*NC*x*CF - 1./3.*LMUF*LMUR*NF*CF - 1./3.*LMUF*LMUR*NF*x*CF
        elif orders == '020':
            result += + ln(omx)*pow(LMUF,2)*pow(NC,-1)*CF + ln(omx)*pow(LMUF,2)*pow(NC,-1)*x*CF - ln(omx)*pow(LMUF,2)*NC*CF - ln(omx)*pow(LMUF,2)*NC*x*CF\
      + 5./4.*pow(LMUF,2)*pow(NC,-1)*CF + 1./4.*pow(LMUF,2)*pow(NC,-1)*x*CF + 1./3.*pow(LMUF,2)*pow(x,-1)*CF\
      + ln(x)*pow(LMUF,2)*pow(NC,-1)*CF*pow(omx,-1) - 3./4.*ln(x)*pow(LMUF,2)*pow(NC,-1)*CF - 3./4.*ln(x)*pow(LMUF,2)*pow(\
      NC,-1)*x*CF + 1./2.*ln(x)*pow(LMUF,2)*CF + 1./2.*ln(x)*pow(LMUF,2)*x*CF - ln(x)*pow(LMUF,2)*\
      NC*CF*pow(omx,-1) + 3./4.*ln(x)*pow(LMUF,2)*NC*CF + 3./4.*ln(x)*pow(LMUF,2)*NC*x*CF + 1./4.*pow(LMUF,2)*CF - 1./4.*pow(LMUF,2)*x*CF - 1./3.*pow(LMUF,2)*pow(x,2)*CF - 13./\
      6.*pow(LMUF,2)*NC*CF - 7./6.*pow(LMUF,2)*NC*x*CF + 1./6.*pow(LMUF,2)*NF*CF + 1./6.*pow(LMUF,2)*NF*x*CF
        return result
    elif rsl == 'sr':
        result = 0
        if orders == '000':
            result_0r = - pow(NC,-1)*CF - 5./12.*pow(NC,-1)*pow(pi,2)*CF - 7*pow(NC,-1)*z*CF - 5./12.*pow(NC,-1)*z\
      *pow(pi,2)*CF - 7./18.*pow(z,-1)*CF - 10./3.*CF + 1./6.*pow(pi,2)*CF + 7./3.*z*CF + 1./6.*z*\
      pow(pi,2)*CF + 25./18.*pow(z,2)*CF + 19./9.*NC*CF + 7./12.*NC*pow(pi,2)*CF - 14./9.*NC*z*CF\
       + 7./12.*NC*z*pow(pi,2)*CF + 2./9.*NF*CF + 8./9.*NF*z*CF - 3./2.*ln(z)*pow(NC,-1)*CF*pow(omz,-1) + 7.\
      /2.*ln(z)*pow(NC,-1)*CF + ln(z)*pow(NC,-1)*z*CF + 2./3.*ln(z)*pow(z,-1)*CF - 1./2.*ln(z)*CF\
       - 2*ln(z)*z*CF - 2./3.*ln(z)*pow(z,2)*CF + 3./2.*ln(z)*NC*CF*pow(omz,-1) - 5./2.*ln(z)*NC*CF + 3*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1) - 2*pow(ln(z),2)*pow(NC,-1)*CF - 2*pow(ln(\
      z),2)*pow(NC,-1)*z*CF + pow(ln(z),2)*CF + pow(ln(z),2)*z*CF - 2*pow(ln(z),2)*NC*CF*pow(\
      omz,-1) + 3./2.*pow(ln(z),2)*NC*CF + 3./2.*pow(ln(z),2)*NC*z*CF - 2*ln(z)*ln(omz)*pow(NC,-1)*\
      CF*pow(omz,-1) + ln(z)*ln(omz)*pow(NC,-1)*CF + ln(z)*ln(omz)*pow(NC,-1)*z*CF + 2*ln(z)*ln(omz\
      )*NC*CF*pow(omz,-1) - ln(z)*ln(omz)*NC*CF - ln(z)*ln(omz)*NC*z*CF + 2./3.*ln(omz)*pow(z,-1)*\
      CF + 1./2.*ln(omz)*CF - 1./2.*ln(omz)*z*CF - 2./3.*ln(omz)*pow(z,2)*CF + 11./6.*ln(omz)*NC*CF\
       + 11./6.*ln(omz)*NC*z*CF - 1./3.*ln(omz)*NF*CF - 1./3.*ln(omz)*NF*z*CF + 3./2.*pow(ln(omz),2)*pow(NC,-1)*CF + 3./2.*pow(ln(omz),2)*pow(NC,-1)*z*CF - 3./\
      2.*pow(ln(omz),2)*NC*CF - 3./2.*pow(ln(omz),2)*NC*z*CF + 1./2.*Li2(z)*pow(NC,-1)*CF + 1./2.*\
      Li2(z)*pow(NC,-1)*z*CF - Li2(z)*CF - Li2(z)*z*CF - 1./2.*Li2(z)*NC*CF - 1./2.*Li2(z)*NC*z*CF
            result_1r = 2./3.*pow(z,-1)*CF + 1./2.*CF - 1./2.*z*CF - 2./3.*pow(z,2)*CF + 11./6.*NC*CF + 11./6.*NC*z\
      *CF - 1./3.*NF*CF - 1./3.*NF*z*CF - 1./2.*ln(z)*pow(NC,-1)*CF - 1./2.*ln(z)*pow(NC,-1)*z*CF + ln(z)*CF + ln(z)*z*CF + 1./2.*\
      ln(z)*NC*CF + 1./2.*ln(z)*NC*z*CF + 3*ln(omz)*pow(NC,-1)*CF + 3*ln(omz)*pow(NC,-1)*z*CF - 3*\
      ln(omz)*NC*CF - 3*ln(omz)*NC*z*CF
            result_2r = 3./2.*pow(NC,-1)*CF + 3./2.*pow(NC,-1)*z*CF - 3./2.*NC*CF - 3./2.*NC*z*CF
            result += result_0r*1/(1-x) + result_1r*ln(1-x)/(1-x) + result_2r*ln(1-x)*ln(1-x)/(1-x)
        elif orders == '001':
            result_0r = - 7./4.*LMUA*pow(NC,-1)*CF + 1./4.*LMUA*pow(NC,-1)*z*CF - 2./3.*LMUA*pow(z,-1)*CF - 1./2.*LMUA*CF + 1./2.*LMUA*z*CF + 2./3.*LMUA*pow(\
      z,2)*CF + 7./4.*LMUA*NC*CF - 1./4.*LMUA*NC*z*CF - 2*ln(z)*LMUA*\
      pow(NC,-1)*CF*pow(omz,-1) + 3./2.*ln(z)*LMUA*pow(NC,-1)*CF + 3./2.*ln(z)*LMUA*pow(NC,-1)*z*CF\
       - ln(z)*LMUA*CF - ln(z)*LMUA*z*CF + 2*ln(z)*LMUA*NC*CF*pow(omz,-1) - 3./2.*ln(z)*LMUA*NC*CF\
       - 3./2.*ln(z)*LMUA*NC*z*CF - 2*ln(omz)*LMUA*pow(NC,-1)*CF - 2*ln(omz)*LMUA*pow(NC,-1)*z*CF + 2*ln(omz)*LMUA*NC*CF + 2*ln(omz)*LMUA*NC*z*CF
            result_1r = - LMUA*pow(NC,-1)*CF - LMUA*pow(NC,-1)*z*CF + LMUA*NC*CF + LMUA*NC*z*CF
            result += result_0r*1/(1-x) + result_1r*ln(1-x)/(1-x)
        elif orders == '010':
            result_0r = + 1./4.*LMUF*pow(NC,-1)*CF - 7./4.*LMUF*pow(NC,-1)*z*CF - 1./4.*LMUF*NC*CF + 7./4.*LMUF*NC*z*CF\
      + 2*ln(z)*LMUF*pow(NC,-1)*CF*pow(omz,-1) - ln(z)*LMUF*pow(NC,-1)*CF - ln(z)*LMUF*pow(NC,-1)*\
      z*CF - 2*ln(z)*LMUF*NC*CF*pow(omz,-1) + ln(z)*LMUF*NC*CF + ln(z)*LMUF*NC*z*CF - ln(omz)*LMUF*pow(\
      NC,-1)*CF - ln(omz)*LMUF*pow(NC,-1)*z*CF + ln(omz)*LMUF*NC*CF + ln(omz)*LMUF*NC*z*CF
            result_1r = - 2*LMUF*pow(NC,-1)*CF - 2*LMUF*pow(NC,-1)*z*CF + 2*LMUF*NC*CF + 2*LMUF*NC*z*CF
            result += result_0r*1/(1-x) + result_1r*ln(1-x)/(1-x)
        elif orders == '100':
            result_0r = - 11./6.*LMUR*NC*CF - 11./6.*LMUR*NC*z*CF + 1./3.*LMUR*NF*CF + 1./3.*LMUR*NF*z*CF
            result += result_0r*1/(1-x)
        elif orders == '011':
            result_0r = + LMUA*LMUF*pow(NC,-1)*CF + LMUA*LMUF*pow(NC,-1)*z*CF - LMUA*LMUF*NC*CF - LMUA*LMUF*NC*z*CF
            result += result_0r*1/(1-x)
        return result
    elif rsl == 'ss':
        result = 0
        if orders == '000':
            result_00 = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_01 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_02 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result_10 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_11 = - 6*pow(NC,-1)*CF + 6*NC*CF
            result_20 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result += result_00*(1/(1-x))*(1/(1-z)) + result_01*(1/(1-x))*(ln(1-z)/(1-z)) + result_02*(1/(1-x))*(ln(1-z)*ln(1-z)/(1-z)) + result_10*(ln(1-x)/(1-x))*(1/(1-z)) + result_11*(ln(1-x)/(1-x))*(ln(1-z)/(1-z)) + result_20*(ln(1-x)*ln(1-x)/(1-x))*(1/(1-z))
        elif orders == '001':
            result_00 = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result_01 = + 4*LMUA*pow(NC,-1)*CF - 4*LMUA*NC*CF
            result_10 = + 2*LMUA*pow(NC,-1)*CF - 2*LMUA*NC*CF
            result += result_00*(1/(1-x))*(1/(1-z)) + result_01*(1/(1-x))*(ln(1-z)/(1-z)) + result_10*(ln(1-x)/(1-x))*(1/(1-z))
        elif orders == '010':
            result_00 = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result_01 = + 2*LMUF*pow(NC,-1)*CF - 2*LMUF*NC*CF
            result_10 = + 4*LMUF*pow(NC,-1)*CF - 4*LMUF*NC*CF
            result += result_00*(1/(1-x))*(1/(1-z)) + result_01*(1/(1-x))*(ln(1-z)/(1-z)) + result_10*(ln(1-x)/(1-x))*(1/(1-z))
        elif orders == '100':
            result_00 = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_00*(1/(1-x))*(1/(1-z))
        elif orders == '011':
            result_00 = - 2*LMUA*LMUF*pow(NC,-1)*CF + 2*LMUA*LMUF*NC*CF
            result += result_00*(1/(1-x))*(1/(1-z))
        return result
    elif rsl == 'sl':
        result = 0
        if orders == '000':
            result_0l = - 4*pow(NC,-1)*zeta3*CF - 202./27.*NC*CF + 11*NC*zeta3*CF + 11./18.*NC*pow(pi,2)*CF + 28./27.*NF*CF - 1./9.*NF*pow(pi,2)*CF
            result_1l = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_2l = - 11./6.*NC*CF + 1./3.*NF*CF
            result_3l = - pow(NC,-1)*CF + NC*CF
            result += result_0l*1/(1-x) + result_1l*ln(1-x)/(1-x) + result_2l*ln(1-x)*ln(1-x)/(1-x) + result_3l*ln(1-x)*ln(1-x)*ln(1-x)/(1-x)
            result_00 = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_01 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_02 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result_10 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_11 = - 6*pow(NC,-1)*CF + 6*NC*CF
            result_20 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result += result_00*(1/(1-x))*(ln(1-z)) + result_01*(1/(1-x))*(ln(1-z)*ln(1-z)/2) + result_02*(1/(1-x))*(ln(1-z)*ln(1-z)*ln(1-z)/3) + result_10*(ln(1-x)/(1-x))*(ln(1-z)) + result_11*(ln(1-x)/(1-x))*(ln(1-z)*ln(1-z)/2) + result_20*(ln(1-x)*ln(1-x)/(1-x))*(ln(1-z))
        elif orders == '001':
            result_0l = - 1./3.*LMUA*pow(NC,-1)*pow(pi,2)*CF + 1./3.*LMUA*NC*pow(pi,2)*CF
            result_1l = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result += result_0l*1/(1-x) + result_1l*ln(1-x)/(1-x)
            result_00 = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result_01 = + 4*LMUA*pow(NC,-1)*CF - 4*LMUA*NC*CF
            result_10 = + 2*LMUA*pow(NC,-1)*CF - 2*LMUA*NC*CF
            result += result_00*(1/(1-x))*(ln(1-z)) + result_01*(1/(1-x))*(ln(1-z)*ln(1-z)/2) + result_10*(ln(1-x)/(1-x))*(ln(1-z))
        elif orders == '010':
            result_0l = - 8*LMUF*pow(NC,-1)*CF - 1./3.*LMUF*pow(NC,-1)*pow(pi,2)*CF + 5./9.*LMUF*NC*CF + 2./3.*LMUF*NC*pow(pi,2)*CF + 10./9.*LMUF*NF*CF
            result_1l = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result_2d = + 3*LMUF*pow(NC,-1)*CF - 3*LMUF*NC*CF
            result += result_0l*1/(1-x) + result_1l*ln(1-x)/(1-x) + result_2d*ln(1-x)*ln(1-x)/(1-x)
            result_00 = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result_01 = + 2*LMUF*pow(NC,-1)*CF - 2*LMUF*NC*CF
            result_10 = + 4*LMUF*pow(NC,-1)*CF - 4*LMUF*NC*CF
            result += result_00*(1/(1-x))*(ln(1-z)) + result_01*(1/(1-x))*(ln(1-z)*ln(1-z)/2) + result_10*(ln(1-x)/(1-x))*(ln(1-z))
        elif orders == '100':
            result_1l = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_1l*ln(1-x)/(1-x)
            result_00 = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_00*(1/(1-x))*(ln(1-z))
        elif orders == '011':
            result_0l = - 3./2.*LMUA*LMUF*pow(NC,-1)*CF + 3./2.*LMUA*LMUF*NC*CF
            result += result_0l*1/(1-x)
            result_00 = - 2*LMUA*LMUF*pow(NC,-1)*CF + 2*LMUA*LMUF*NC*CF
            result += result_00*(1/(1-x))*(ln(1-z))
        elif orders == '110':
            result_0l = - 11./3.*LMUF*LMUR*NC*CF + 2./3.*LMUF*LMUR*NF*CF
            result += result_0l*1/(1-x)
        elif orders == '020':
            result_0l = - 3./2.*pow(LMUF,2)*pow(NC,-1)*CF + 10./3.*pow(LMUF,2)*NC*CF - 1./3.*pow(LMUF,2)*NF*CF
            result_1l = - 2*pow(LMUF,2)*pow(NC,-1)*CF + 2*pow(LMUF,2)*NC*CF
            result += result_0l*1/(1-x) + result_1l*ln(1-x)/(1-x)
        return result
    elif rsl == 'lr':
        result = 0
        if orders == '000':
            result += - 1./4.*pow(NC,-1)*CF + 10*pow(NC,-1)*zeta3*CF*pow(omz,-1) - 4*pow(NC,-1)*zeta3*CF - 1./4.\
      *pow(NC,-1)*pow(pi,2)*CF*pow(omz,-1) + 7./12.*pow(NC,-1)*pow(pi,2)*CF + 1./4.*pow(NC,-1)*z*CF\
       - 4*pow(NC,-1)*z*zeta3*CF + 1./6.*pow(NC,-1)*z*pow(pi,2)*CF - 107./108.*pow(z,-1)*CF - 11./9.\
      *CF + 2*zeta3*CF - 1./6.*pow(pi,2)*CF - 4./9.*z*CF + 2*z*zeta3*CF - 1./4.*z*pow(pi,2)*CF + \
      287./108.*pow(z,2)*CF + 197./108.*NC*CF - 14*NC*zeta3*CF*pow(omz,-1) + 5./2.*NC*zeta3*CF + 1./\
      4.*NC*pow(pi,2)*CF*pow(omz,-1) - 29./36.*NC*pow(pi,2)*CF + 611./108.*NC*z*CF + 5./2.*NC*z*\
      zeta3*CF - 2./9.*NC*z*pow(pi,2)*CF - 19./54.*NF*CF + 1./18.*NF*pow(pi,2)*CF - 37./54.*NF*z*CF\
       + 1./18.*NF*z*pow(pi,2)*CF
            result += + 19./2.*ln(z)*pow(NC,-1)*CF*pow(omz,-1) - 15./4.*ln(z)*pow(NC,-1)*CF + 1./2.*ln(z)*pow(NC,-1)*pow(\
      pi,2)*CF*pow(omz,-1) - 1./3.*ln(z)*pow(NC,-1)*pow(pi,2)*CF - 29./4.*ln(z)*pow(NC,-1)*z*CF - 1.\
      /3.*ln(z)*pow(NC,-1)*z*pow(pi,2)*CF - 7./18.*ln(z)*pow(z,-1)*CF - 5*ln(z)*CF + 1./6.*ln(z)*\
      pow(pi,2)*CF - 9./2.*ln(z)*z*CF + 1./6.*ln(z)*z*pow(pi,2)*CF - 31./18.*ln(z)*pow(z,2)*CF - \
      113./18.*ln(z)*NC*CF*pow(omz,-1) + 233./36.*ln(z)*NC*CF - 5./6.*ln(z)*NC*pow(pi,2)*CF*pow(\
      omz,-1) + 1./2.*ln(z)*NC*pow(pi,2)*CF + 101./36.*ln(z)*NC*z*CF + 1./2.*ln(z)*NC*z*pow(pi,2)*\
      CF - 5./9.*ln(z)*NF*CF*pow(omz,-1) - 1./18.*ln(z)*NF*CF + 11./18.*ln(z)*NF*z*CF
            result +=  - 9./8.*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1) + 21./8.*pow(ln(z\
      ),2)*pow(NC,-1)*CF + 7./8.*pow(ln(z),2)*pow(NC,-1)*z*CF + 1./3.*pow(ln(z),2)*pow(z,-1)*CF - 1.\
      /8.*pow(ln(z),2)*CF - 5./8.*pow(ln(z),2)*z*CF + 49./24.*pow(ln(z),2)*NC*CF*pow(omz,-1) - 25./\
      12.*pow(ln(z),2)*NC*CF - 5./6.*pow(ln(z),2)*NC*z*CF - 1./6.*pow(ln(z),2)*NF*CF*pow(omz,-1) + \
      1./12.*pow(ln(z),2)*NF*CF + 1./12.*pow(ln(z),2)*NF*z*CF
            result +=  + 5./3.*pow(ln(z),3)*pow(NC,-1)*CF*pow(omz,-1)\
       - 25./24.*pow(ln(z),3)*pow(NC,-1)*CF - 25./24.*pow(ln(z),3)*pow(NC,-1)*z*CF + 5./12.*pow(ln(\
      z),3)*CF + 5./12.*pow(ln(z),3)*z*CF - 5./6.*pow(ln(z),3)*NC*CF*pow(omz,-1) + 5./8.*pow(ln(z),\
      3)*NC*CF + 5./8.*pow(ln(z),3)*NC*z*CF + 1./2.*pow(ln(z),2)*ln(omz)*pow(NC,-1)*CF*pow(omz,-1)\
       - 1./4.*pow(ln(z),2)*ln(omz)*pow(NC,-1)*CF - 1./4.*pow(ln(z),2)*ln(omz)*pow(NC,-1)*z*CF - 1./\
      2.*pow(ln(z),2)*ln(omz)*NC*CF*pow(omz,-1) + 1./4.*pow(ln(z),2)*ln(omz)*NC*CF + 1./4.*pow(ln(z\
      ),2)*ln(omz)*NC*z*CF - 3./2.*ln(z)*ln(omz)*pow(NC,-1)*CF + 3./2.*ln(z)*ln(omz)*pow(NC,-1)*z*\
      CF + 3./2.*ln(z)*ln(omz)*NC*CF - 3./2.*ln(z)*ln(omz)*NC*z*CF - 1./2.*ln(z)*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omz,-1) + 1./2.*ln(z)*pow(ln(omz),2)*pow(\
      NC,-1)*CF + 1./2.*ln(z)*pow(ln(omz),2)*pow(NC,-1)*z*CF - 1./2.*ln(z)*pow(ln(omz),2)*CF - 1./2.\
      *ln(z)*pow(ln(omz),2)*z*CF + 5./2.*ln(z)*pow(ln(omz),2)*NC*CF*pow(omz,-1) - 3./2.*ln(z)*pow(\
      ln(omz),2)*NC*CF - 3./2.*ln(z)*pow(ln(omz),2)*NC*z*CF + 4*ln(z)*Li2(z)*pow(NC,-1)*CF*pow(\
      omz,-1)
            result +=  - 2*ln(z)*Li2(z)*pow(NC,-1)*CF - 2*ln(z)*Li2(z)*pow(NC,-1)*z*CF - 6*ln(z)*Li2(z)*NC*\
      CF*pow(omz,-1) + 3*ln(z)*Li2(z)*NC*CF + 3*ln(z)*Li2(z)*NC*z*CF - 5./4.*ln(omz)*pow(NC,-1)*CF\
       - 1./6.*ln(omz)*pow(NC,-1)*pow(pi,2)*CF*pow(omz,-1) - 1./3.*ln(omz)*pow(NC,-1)*pow(pi,2)*CF\
       - 7*ln(omz)*pow(NC,-1)*z*CF - 1./3.*ln(omz)*pow(NC,-1)*z*pow(pi,2)*CF - 7./18.*ln(omz)*pow(\
      z,-1)*CF - 10./3.*ln(omz)*CF + 1./6.*ln(omz)*pow(pi,2)*CF + 7./3.*ln(omz)*z*CF + 1./6.*ln(omz\
      )*z*pow(pi,2)*CF + 25./18.*ln(omz)*pow(z,2)*CF + 67./36.*ln(omz)*NC*CF - 1./6.*ln(omz)*NC*\
      pow(pi,2)*CF*pow(omz,-1) + 2./3.*ln(omz)*NC*pow(pi,2)*CF - 14./9.*ln(omz)*NC*z*CF + 2./3.*ln(\
      omz)*NC*z*pow(pi,2)*CF + 2./9.*ln(omz)*NF*CF + 8./9.*ln(omz)*NF*z*CF   \
      + 1./3.*pow(ln(omz),2)*pow(z,-1)*CF + 1./4.*pow(\
      ln(omz),2)*CF
            result +=  - 1./4.*pow(ln(omz),2)*z*CF - 1./3.*pow(ln(omz),2)*pow(z,2)*CF + 11./12.*pow(ln(omz),\
      2)*NC*CF + 11./12.*pow(ln(omz),2)*NC*z*CF - 1./6.*pow(ln(omz),2)*NF*CF - 1./6.*pow(ln(omz),2)\
      *NF*z*CF + 1./2.*pow(ln(omz),\
      3)*pow(NC,-1)*CF + 1./2.*pow(ln(omz),3)*pow(NC,-1)*z*CF - 1./2.*pow(ln(omz),3)*NC*CF - 1./2.*\
      pow(ln(omz),3)*NC*z*CF + ln(omz)*Li2(z)*pow(NC,-1)*CF*pow(omz,-1) - ln(omz)*Li2(z)*CF - ln(\
      omz)*Li2(z)*z*CF + ln(omz)*Li2(z)*NC*CF*pow(omz,-1) - ln(omz)*Li2(z)*NC*CF - ln(omz)*Li2(z)*\
      NC*z*CF + 3*Li3(1 - z)*pow(NC,-1)*CF*pow(omz,-1) - Li3(1 - z)*pow(NC,-1)*CF - Li3(1 - z)*pow(\
      NC,-1)*z*CF - Li3(1 - z)*CF - Li3(1 - z)*z*CF + 3*Li3(1 - z)*NC*CF*pow(omz,-1) - 2*Li3(1 - z)\
      *NC*CF - 2*Li3(1 - z)*NC*z*CF - 10*Li3(z)*pow(NC,-1)*CF*pow(omz,-1) + 6*Li3(z)*pow(NC,-1)*CF\
       + 6*Li3(z)*pow(NC,-1)*z*CF - 2*Li3(z)*CF - 2*Li3(z)*z*CF + 14*Li3(z)*NC*CF*pow(omz,-1) - 8*\
      Li3(z)*NC*CF - 8*Li3(z)*NC*z*CF + 3./2.*Li2(z)*pow(NC,-1)*CF*pow(omz,-1) - 9./2.*Li2(z)*pow(\
      NC,-1)*CF - 2./3.*Li2(z)*pow(z,-1)*CF + 1./2.*Li2(z)*CF + 2*Li2(z)*z*CF + 2./3.*Li2(z)*pow(\
      z,2)*CF - 3./2.*Li2(z)*NC*CF*pow(omz,-1) + 7./2.*Li2(z)*NC*CF - Li2(z)*NC*z*CF
            result_0r = - pow(NC,-1)*CF - 5./12.*pow(NC,-1)*pow(pi,2)*CF - 7*pow(NC,-1)*z*CF - 5./12.*pow(NC,-1)*z\
      *pow(pi,2)*CF - 7./18.*pow(z,-1)*CF - 10./3.*CF + 1./6.*pow(pi,2)*CF + 7./3.*z*CF + 1./6.*z*\
      pow(pi,2)*CF + 25./18.*pow(z,2)*CF + 19./9.*NC*CF + 7./12.*NC*pow(pi,2)*CF - 14./9.*NC*z*CF\
       + 7./12.*NC*z*pow(pi,2)*CF + 2./9.*NF*CF + 8./9.*NF*z*CF - 3./2.*ln(z)*pow(NC,-1)*CF*pow(omz,-1) + 7.\
      /2.*ln(z)*pow(NC,-1)*CF + ln(z)*pow(NC,-1)*z*CF + 2./3.*ln(z)*pow(z,-1)*CF - 1./2.*ln(z)*CF\
       - 2*ln(z)*z*CF - 2./3.*ln(z)*pow(z,2)*CF + 3./2.*ln(z)*NC*CF*pow(omz,-1) - 5./2.*ln(z)*NC*CF + 3*pow(ln(z),2)*pow(NC,-1)*CF*pow(omz,-1) - 2*pow(ln(z),2)*pow(NC,-1)*CF - 2*pow(ln(\
      z),2)*pow(NC,-1)*z*CF + pow(ln(z),2)*CF + pow(ln(z),2)*z*CF - 2*pow(ln(z),2)*NC*CF*pow(\
      omz,-1) + 3./2.*pow(ln(z),2)*NC*CF + 3./2.*pow(ln(z),2)*NC*z*CF - 2*ln(z)*ln(omz)*pow(NC,-1)*\
      CF*pow(omz,-1) + ln(z)*ln(omz)*pow(NC,-1)*CF + ln(z)*ln(omz)*pow(NC,-1)*z*CF + 2*ln(z)*ln(omz\
      )*NC*CF*pow(omz,-1) - ln(z)*ln(omz)*NC*CF - ln(z)*ln(omz)*NC*z*CF + 2./3.*ln(omz)*pow(z,-1)*\
      CF + 1./2.*ln(omz)*CF - 1./2.*ln(omz)*z*CF - 2./3.*ln(omz)*pow(z,2)*CF + 11./6.*ln(omz)*NC*CF\
       + 11./6.*ln(omz)*NC*z*CF - 1./3.*ln(omz)*NF*CF - 1./3.*ln(omz)*NF*z*CF + 3./2.*pow(ln(omz),2)*pow(NC,-1)*CF + 3./2.*pow(ln(omz),2)*pow(NC,-1)*z*CF - 3./\
      2.*pow(ln(omz),2)*NC*CF - 3./2.*pow(ln(omz),2)*NC*z*CF + 1./2.*Li2(z)*pow(NC,-1)*CF + 1./2.*\
      Li2(z)*pow(NC,-1)*z*CF - Li2(z)*CF - Li2(z)*z*CF - 1./2.*Li2(z)*NC*CF - 1./2.*Li2(z)*NC*z*CF
            result_1r = 2./3.*pow(z,-1)*CF + 1./2.*CF - 1./2.*z*CF - 2./3.*pow(z,2)*CF + 11./6.*NC*CF + 11./6.*NC*z\
      *CF - 1./3.*NF*CF - 1./3.*NF*z*CF - 1./2.*ln(z)*pow(NC,-1)*CF - 1./2.*ln(z)*pow(NC,-1)*z*CF + ln(z)*CF + ln(z)*z*CF + 1./2.*\
      ln(z)*NC*CF + 1./2.*ln(z)*NC*z*CF + 3*ln(omz)*pow(NC,-1)*CF + 3*ln(omz)*pow(NC,-1)*z*CF - 3*\
      ln(omz)*NC*CF - 3*ln(omz)*NC*z*CF
            result_2r = 3./2.*pow(NC,-1)*CF + 3./2.*pow(NC,-1)*z*CF - 3./2.*NC*CF - 3./2.*NC*z*CF
            result += result_0r*ln(1-x) + result_1r*ln(1-x)*ln(1-x)/2 + result_2r*ln(1-x)*ln(1-x)*ln(1-x)/3
        elif orders == '001':
            result += - 1./2.*Li2(z)*LMUA*pow(NC,-1)*CF - 1./2.*Li2(z)*LMUA*pow(NC,-1)*z*CF + Li2(z)*LMUA*CF + Li2(z)*LMUA*z*CF\
       + 1./2.*Li2(z)*LMUA*NC*CF + 1./2.*Li2(z)*LMUA*NC*z*CF - 3./2.*pow(ln(omz),2)*LMUA*pow(NC,-1)*CF \
       - 3./2.*pow(ln(omz),2)*LMUA*pow(NC,-1)*z*CF + 3./2.*pow(ln(omz),2)*LMUA*NC*CF + 3./2.*pow(ln(omz),2)*LMUA*NC*z*CF\
       + 7./4.*LMUA*pow(NC,-1)*CF + 1./4.*LMUA*pow(NC,-1)*pow(pi,2)*CF + 25./4.*LMUA*pow(NC,-1)*z*CF + 1./4.*LMUA*pow(NC,-1)*z\
      *pow(pi,2)*CF + 7./18.*LMUA*pow(z,-1)*CF + 10./3.*LMUA*CF - 1./6.*LMUA*pow(pi,2)*CF - 7./3.*\
      LMUA*z*CF - 1./6.*LMUA*z*pow(pi,2)*CF - 25./18.*LMUA*pow(z,2)*CF - 169./36.*LMUA*NC*CF - 5./\
      12.*LMUA*NC*pow(pi,2)*CF + 149./36.*LMUA*NC*z*CF - 5./12.*LMUA*NC*z*pow(pi,2)*CF + 1./9.*LMUA*NF*CF\
      - 3./4.*ln(omz)*LMUA*pow(NC,-1)*CF - 3./4.*ln(omz)*LMUA*pow(\
      NC,-1)*z*CF - 2./3.*ln(omz)*LMUA*pow(z,-1)*CF - 1./2.*ln(omz)*LMUA*CF + 1./2.*ln(omz)*LMUA*z*\
      CF + 2./3.*ln(omz)*LMUA*pow(z,2)*CF + 3./4.*ln(omz)*LMUA*NC*CF + 3./4.*ln(omz)*LMUA*NC*z*CF\
      + 2*ln(z)*ln(omz)*LMUA*pow(NC,-1)*CF*pow(omz,-1) - ln(z)*ln(omz)*LMUA*pow(NC,-1)*CF - ln(z)*ln(omz)*LMUA*pow(NC,-1)*z*CF\
       - 2*ln(z)*ln(omz)*LMUA*NC*CF*pow(omz,-1) + ln(z)*ln(omz)*LMUA*NC*CF + ln(z)*ln(omz)*LMUA*NC*z*CF\
       - 3*pow(ln(z),2)*LMUA*pow(NC,-1)*CF*pow(omz,-1) + 2*pow(ln(z),2)*LMUA*pow(NC,-1)*CF + 2*pow(ln(z),2)*LMUA*pow(NC,-1)*z*CF \
       - pow(ln(z),2)*LMUA*CF - pow(ln(z),2)*LMUA*z*CF + 2*pow(ln(z),2)*LMUA*NC*CF*pow(omz,-1) - 3./2.*pow(ln(z),2)\
       *LMUA*NC*CF - 3./2.*pow(ln(z),2)*LMUA*NC*z*CF + 3*ln(z)*LMUA*\
       pow(NC,-1)*CF*pow(omz,-1) - 17./4.*ln(z)*LMUA*pow(NC,-1)*CF - 7./4.*ln(z)*LMUA*pow(NC,-1)*z*\
       CF - 2./3.*ln(z)*LMUA*pow(z,-1)*CF + 1./2.*ln(z)*LMUA*CF + 2*ln(z)*LMUA*z*CF + 2./3.*ln(z)*\
       LMUA*pow(z,2)*CF - 20./3.*ln(z)*LMUA*NC*CF*pow(omz,-1) + 61./12.*ln(z)*LMUA*NC*CF + 31./12.*\
       ln(z)*LMUA*NC*z*CF + 2./3.*ln(z)*LMUA*NF*CF*pow(omz,-1) - 1./3.*ln(z)*LMUA*NF*CF - 1./3.*ln(z\
       )*LMUA*NF*z*CF - 11./9.*LMUA*NF*z*CF
            result_0r = - 7./4.*LMUA*pow(NC,-1)*CF + 1./4.*LMUA*pow(NC,-1)*z*CF - 2./3.*LMUA*pow(z,-1)*CF - 1./2.*LMUA*CF + 1./2.*LMUA*z*CF + 2./3.*LMUA*pow(\
      z,2)*CF + 7./4.*LMUA*NC*CF - 1./4.*LMUA*NC*z*CF - 2*ln(z)*LMUA*\
      pow(NC,-1)*CF*pow(omz,-1) + 3./2.*ln(z)*LMUA*pow(NC,-1)*CF + 3./2.*ln(z)*LMUA*pow(NC,-1)*z*CF\
       - ln(z)*LMUA*CF - ln(z)*LMUA*z*CF + 2*ln(z)*LMUA*NC*CF*pow(omz,-1) - 3./2.*ln(z)*LMUA*NC*CF\
       - 3./2.*ln(z)*LMUA*NC*z*CF - 2*ln(omz)*LMUA*pow(NC,-1)*CF - 2*ln(omz)*LMUA*pow(NC,-1)*z*CF + 2*ln(omz)*LMUA*NC*CF + 2*ln(omz)*LMUA*NC*z*CF
            result_1r = - LMUA*pow(NC,-1)*CF - LMUA*pow(NC,-1)*z*CF + LMUA*NC*CF + LMUA*NC*z*CF
            result += result_0r*ln(1-x) + result_1r*ln(1-x)*ln(1-x)/2
        elif orders == '010':
            result += + 3./4.*LMUF*pow(NC,-1)*CF + 1./6.*LMUF*pow(NC,-1)*pow(pi,2)*CF - 3./4.*LMUF*\
      pow(NC,-1)*z*CF + 1./6.*LMUF*pow(NC,-1)*z*pow(pi,2)*CF - 3./4.*LMUF*NC*CF - 1./6.*LMUF*NC*\
      pow(pi,2)*CF + 3./4.*LMUF*NC*z*CF - 1./6.*LMUF*NC*z*pow(pi,2)*CF - 3.\
      /4.*ln(omz)*LMUF*pow(NC,-1)*CF - 3./4.*ln(omz)*LMUF*pow(NC,-1)*z*CF + 3./4.*ln(omz)*LMUF*NC*\
      CF + 3./4.*ln(omz)*LMUF*NC*z*CF - 3./4.*ln(z)*LMUF*pow(NC,-1)*CF - 3./4.*ln(z)*LMUF*pow(NC,-1)*z*CF - 3./2.*ln(z)*\
      LMUF*NC*CF*pow(omz,-1) + 3./4.*ln(z)*LMUF*NC*CF + 3./4.*ln(z)*LMUF*NC*z*CF + 3./2.*ln(z)*LMUF*pow(NC,-1)*CF*pow(omz,-1)
            result_0r = + 1./4.*LMUF*pow(NC,-1)*CF - 7./4.*LMUF*pow(NC,-1)*z*CF - 1./4.*LMUF*NC*CF + 7./4.*LMUF*NC*z*CF\
      + 2*ln(z)*LMUF*pow(NC,-1)*CF*pow(omz,-1) - ln(z)*LMUF*pow(NC,-1)*CF - ln(z)*LMUF*pow(NC,-1)*\
      z*CF - 2*ln(z)*LMUF*NC*CF*pow(omz,-1) + ln(z)*LMUF*NC*CF + ln(z)*LMUF*NC*z*CF - ln(omz)*LMUF*pow(\
      NC,-1)*CF - ln(omz)*LMUF*pow(NC,-1)*z*CF + ln(omz)*LMUF*NC*CF + ln(omz)*LMUF*NC*z*CF
            result_1r = - 2*LMUF*pow(NC,-1)*CF - 2*LMUF*pow(NC,-1)*z*CF + 2*LMUF*NC*CF + 2*LMUF*NC*z*CF
            result += result_0r*ln(1-x) + result_1r*ln(1-x)*ln(1-x)/2
        elif orders == '100':
            result += + 11./6.*LMUR*NC*CF - 11./6.*LMUR*NC*z*CF - 1./3.*LMUR*NF*CF + 1./3.*LMUR*NF*z*CF - 11./6.*ln(omz)*LMUR*NC\
      *CF - 11./6.*ln(omz)*LMUR*NC*z*CF + 1./3.*ln(omz)*LMUR*NF*CF + 1./3.*ln(omz)*LMUR*NF*z*CF + 11./3.*ln(z\
      )*LMUR*NC*CF*pow(omz,-1) - 11./6.*ln(z)*LMUR*NC*CF - 11./6.*ln(z)*LMUR*NC*z*CF - 2./3.*ln(z)*\
      LMUR*NF*CF*pow(omz,-1) + 1./3.*ln(z)*LMUR*NF*CF + 1./3.*ln(z)*LMUR*NF*z*CF
            result_0r = - 11./6.*LMUR*NC*CF - 11./6.*LMUR*NC*z*CF + 1./3.*LMUR*NF*CF + 1./3.*LMUR*NF*z*CF
            result += result_0r*ln(1-x)            
        elif orders == '011':
            result += + 3./4.*LMUA*LMUF*pow(NC,-1)*CF + 3./4.*LMUA*LMUF*pow(NC,-1)*z*CF - 3./4.*LMUA*LMUF*NC*CF - 3./4.*LMUA*LMUF*NC*z*CF
            result_0r = + LMUA*LMUF*pow(NC,-1)*CF + LMUA*LMUF*pow(NC,-1)*z*CF - LMUA*LMUF*NC*CF - LMUA*LMUF*NC*z*CF
            result += result_0r*ln(1-x)
        elif orders == '101':
            result += + 11./6.*LMUA*LMUR*NC*CF + 11./6.*LMUA*LMUR*NC*z*CF - 1./3.*LMUA*LMUR*NF*CF - 1./3.*LMUA*LMUR*NF*z*CF
        elif orders == '002':
            result += + 5./4.*pow(LMUA,2)*pow(NC,-1)*CF + 1./4.*pow(LMUA,2)*pow(NC,-1)*z*CF + 1./3.*pow(LMUA,2)*pow(z,-1)*CF + 1./4.*pow(\
      LMUA,2)*CF - 1./4.*pow(LMUA,2)*z*CF - 1./3.*pow(LMUA,2)*pow(z,2)*CF - 13./6.*pow(LMUA,2)*NC*\
      CF - 7./6.*pow(LMUA,2)*NC*z*CF + 1./6.*pow(LMUA,2)*NF*CF + 1./6.*pow(LMUA,2)*NF*z*CF \
      + ln(omz)*pow(LMUA,2)*pow(NC,-1)*CF + ln(omz)*pow(LMUA,2)*pow(NC,-1)*z*CF - ln(omz)*pow(\
      LMUA,2)*NC*CF - ln(omz)*pow(LMUA,2)*NC*z*CF + ln(z)*pow(LMUA,2)*pow(NC,-1)*CF*pow(omz,-1) - 3./4.*ln(z)*pow(LMUA,2)*pow(\
        NC,-1)*CF - 3./4.*ln(z)*pow(LMUA,2)*pow(NC,-1)*z*CF + 1./2.*ln(z)*pow(LMUA,2)*CF + 1./2.*ln(z\
        )*pow(LMUA,2)*z*CF - ln(z)*pow(LMUA,2)*NC*CF*pow(omz,-1) + 3./4.*ln(z)*pow(LMUA,2)*NC*CF + 3./\
        4.*ln(z)*pow(LMUA,2)*NC*z*CF
        return result
    elif rsl == 'ls':
        result = 0
        if orders == '000':
            result_l0 = - 4*pow(NC,-1)*zeta3*CF - 202./27.*NC*CF + 11*NC*zeta3*CF + 11./18.*NC*pow(pi,2)*CF + 28./27.*NF*CF - 1./9.*NF*pow(pi,2)*CF
            result_l1 = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_l2 = - 11./6.*NC*CF + 1./3.*NF*CF
            result_l3 = - pow(NC,-1)*CF + NC*CF
            result += result_l0*1/(1-z) + result_l1*ln(1-z)/(1-z) + result_l2*ln(1-z)*ln(1-z)/(1-z) + result_l3*ln(1-z)*ln(1-z)*ln(1-z)/(1-z)
            result_00 = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_01 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_02 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result_10 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_11 = - 6*pow(NC,-1)*CF + 6*NC*CF
            result_20 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result += result_00*(ln(1-x))*(1/(1-z)) + result_01*(ln(1-x))*(ln(1-z)/(1-z)) + result_02*(ln(1-x))*(ln(1-z)*ln(1-z)/(1-z)) + result_10*(ln(1-x)*ln(1-x)/2)*(1/(1-z)) + result_11*(ln(1-x)*ln(1-x)/2)*(ln(1-z)/(1-z)) + result_20*(ln(1-x)*ln(1-x)*ln(1-x)/3)*(1/(1-z))
        elif orders == '001':
            result_l0 = - 8*LMUA*pow(NC,-1)*CF - 1./3.*LMUA*pow(NC,-1)*pow(pi,2)*CF + 5./9.*LMUA*NC*CF + 2./3.*LMUA*NC*pow(pi,2)*CF + 10./9.*LMUA*NF*CF
            result_l1 = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result_l2 = + 3*LMUA*pow(NC,-1)*CF - 3*LMUA*NC*CF
            result += result_l0*1/(1-z) + result_l1*ln(1-z)/(1-z) + result_l2*ln(1-z)*ln(1-z)/(1-z)
            result_00 = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result_01 = + 4*LMUA*pow(NC,-1)*CF - 4*LMUA*NC*CF
            result_10 = + 2*LMUA*pow(NC,-1)*CF - 2*LMUA*NC*CF
            result += result_00*(ln(1-x))*(1/(1-z)) + result_01*(ln(1-x))*(ln(1-z)/(1-z)) + result_10*(ln(1-x)*ln(1-x)/2)*(1/(1-z))
        elif orders == '010':
            result_l0 = - 1./3.*LMUF*pow(NC,-1)*pow(pi,2)*CF + 1./3.*LMUF*NC*pow(pi,2)*CF
            result_l1 = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result += result_l0*1/(1-z) + result_l1*ln(1-z)/(1-z)
            result_00 = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result_01 = + 2*LMUF*pow(NC,-1)*CF - 2*LMUF*NC*CF
            result_10 = + 4*LMUF*pow(NC,-1)*CF - 4*LMUF*NC*CF
            result += result_00*(ln(1-x))*(1/(1-z)) + result_01*(ln(1-x))*(ln(1-z)/(1-z)) + result_10*(ln(1-x)*ln(1-x)/2)*(1/(1-z))
        elif orders == '100':
            result_l1 = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_l1*ln(1-z)/(1-z)
            result_00 = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_00*(ln(1-x))*(1/(1-z))
        elif orders == '011':
            result_l0 = - 3./2.*LMUA*LMUF*pow(NC,-1)*CF + 3./2.*LMUA*LMUF*NC*CF
            result += result_l0*1/(1-z)
            result_00 = - 2*LMUA*LMUF*pow(NC,-1)*CF + 2*LMUA*LMUF*NC*CF
            result += result_00*(ln(1-x))*(1/(1-z))
        elif orders == '101':
            result_l0 = - 11./3.*LMUA*LMUR*NC*CF + 2./3.*LMUA*LMUR*NF*CF
            result += result_l0*1/(1-z)
        elif orders == '002':
            result_l0 = + 10./3.*pow(LMUA,2)*NC*CF - 1./3.*pow(LMUA,2)*NF*CF - 3./2.*pow(LMUA,2)*pow(NC,-1)*CF
            result_l1 = - 2*pow(LMUA,2)*pow(NC,-1)*CF + 2*pow(LMUA,2)*NC*CF
            result += result_l0*1/(1-z) + result_l1*ln(1-z)/(1-z)
        return result
    elif rsl == 'll':
        result = 0
        if orders == '000':
            result += - 511./32.*pow(NC,-1)*CF + 15./2.*pow(NC,-1)*zeta3*CF - 29./24.*pow(NC,-1)*pow(pi,2)*CF + \
      7./180.*pow(NC,-1)*pow(pi,4)*CF - 1537./96.*NC*CF + 41./6.*NC*zeta3*CF - 277./216.*NC*pow(\
      pi,2)*CF + 1./18.*NC*pow(pi,4)*CF + 127./24.*NF*CF + 2./3.*NF*zeta3*CF + 19./54.*NF*pow(pi,2)*CF
            result_0l = - 4*pow(NC,-1)*zeta3*CF - 202./27.*NC*CF + 11*NC*zeta3*CF + 11./18.*NC*pow(pi,2)*CF + 28./27.*NF*CF - 1./9.*NF*pow(pi,2)*CF
            result_1l = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_2l = - 11./6.*NC*CF + 1./3.*NF*CF
            result_3l = - pow(NC,-1)*CF + NC*CF
            result += result_0l*ln(1-x) + result_1l*ln(1-x)*ln(1-x)/2 + result_2l*ln(1-x)*ln(1-x)*ln(1-x)/3 + result_3l*ln(1-x)*ln(1-x)*ln(1-x)*ln(1-x)/4
            result_l0 = - 4*pow(NC,-1)*zeta3*CF - 202./27.*NC*CF + 11*NC*zeta3*CF + 11./18.*NC*pow(pi,2)*CF + 28./27.*NF*CF - 1./9.*NF*pow(pi,2)*CF
            result_l1 = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_l2 = - 11./6.*NC*CF + 1./3.*NF*CF
            result_l3 = - pow(NC,-1)*CF + NC*CF
            result += result_l0*ln(1-z) + result_l1*ln(1-z)*ln(1-z)/2 + result_l2*ln(1-z)*ln(1-z)*ln(1-z)/3 + result_l3*ln(1-z)*ln(1-z)*ln(1-z)*ln(1-z)/4
            result_00 = 8*pow(NC,-1)*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF - 5./9.*NC*CF - NC*pow(pi,2)*CF - 10./9.*NF*CF
            result_01 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_02 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result_10 = - 11./3.*NC*CF + 2./3.*NF*CF
            result_11 = - 6*pow(NC,-1)*CF + 6*NC*CF
            result_20 = - 3*pow(NC,-1)*CF + 3*NC*CF
            result += result_00*(ln(1-x))*(ln(1-z)) + result_01*(ln(1-x))*(ln(1-z)*ln(1-z)/2) + result_02*(ln(1-x))*(ln(1-z)*ln(1-z)*ln(1-z)/3) + result_10*(ln(1-x)*ln(1-x)/2)*(ln(1-z)) + result_11*(ln(1-x)*ln(1-x)/2)*(ln(1-z)*ln(1-z)/2) + result_20*(ln(1-x)*ln(1-x)*ln(1-x)/3)*(ln(1-z))
        elif orders == '001':
            result += - 93./16.*LMUA*pow(NC,-1)*CF + 5*LMUA*pow(NC,-1)*zeta3*CF - 1./4.*LMUA*pow(\
      NC,-1)*pow(pi,2)*CF + 245./48.*LMUA*NC*CF - 2*LMUA*NC*zeta3*CF - 13./36.*LMUA*NC*pow(pi,2)*CF\
       + 1./12.*LMUA*NF*CF + 1./9.*LMUA*NF*pow(pi,2)*CF
            result_0l = - 1./3.*LMUA*pow(NC,-1)*pow(pi,2)*CF + 1./3.*LMUA*NC*pow(pi,2)*CF
            result_1l = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result += result_0l*ln(1-x) + result_1l*ln(1-x)*ln(1-x)/2
            result_l0 = - 8*LMUA*pow(NC,-1)*CF - 1./3.*LMUA*pow(NC,-1)*pow(pi,2)*CF + 5./9.*LMUA*NC*CF + 2./3.*LMUA*NC*pow(pi,2)*CF + 10./9.*LMUA*NF*CF
            result_l1 = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result_l2 = + 3*LMUA*pow(NC,-1)*CF - 3*LMUA*NC*CF
            result += result_l0*ln(1-z) + result_l1*ln(1-z)*ln(1-z)/2 + result_l2*ln(1-z)*ln(1-z)*ln(1-z)/3
            result_00 = + 3./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*NC*CF
            result_01 = + 4*LMUA*pow(NC,-1)*CF - 4*LMUA*NC*CF
            result_10 = + 2*LMUA*pow(NC,-1)*CF - 2*LMUA*NC*CF
            result += result_00*(ln(1-x))*(ln(1-z)) + result_01*(ln(1-x))*(ln(1-z)*ln(1-z)/2) + result_10*(ln(1-x)*ln(1-x)/2)*(ln(1-z))
        elif orders == '010':
            result += - 93./16.*LMUF*pow(NC,-1)*CF + 5*LMUF*pow(NC,-1)*\
      zeta3*CF - 1./4.*LMUF*pow(NC,-1)*pow(pi,2)*CF + 245./48.*LMUF*NC*CF - 2*LMUF*NC*zeta3*CF - 13.\
      /36.*LMUF*NC*pow(pi,2)*CF + 1./12.*LMUF*NF*CF + 1./9.*LMUF*NF*pow(pi,2)*CF
            result_0l = - 8*LMUF*pow(NC,-1)*CF - 1./3.*LMUF*pow(NC,-1)*pow(pi,2)*CF + 5./9.*LMUF*NC*CF + 2./3.*LMUF*NC*pow(pi,2)*CF + 10./9.*LMUF*NF*CF
            result_1l = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result_2d = + 3*LMUF*pow(NC,-1)*CF - 3*LMUF*NC*CF
            result += result_0l*ln(1-x) + result_1l*ln(1-x)*ln(1-x)/2 + result_2d*ln(1-x)*ln(1-x)*ln(1-x)/3
            result_l0 = - 1./3.*LMUF*pow(NC,-1)*pow(pi,2)*CF + 1./3.*LMUF*NC*pow(pi,2)*CF
            result_l1 = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result += result_l0*ln(1-z) + result_l1*ln(1-z)*ln(1-z)/2
            result_00 = + 3./2.*LMUF*pow(NC,-1)*CF - 3./2.*LMUF*NC*CF
            result_01 = + 2*LMUF*pow(NC,-1)*CF - 2*LMUF*NC*CF
            result_10 = + 4*LMUF*pow(NC,-1)*CF - 4*LMUF*NC*CF
            result += result_00*(ln(1-x))*(ln(1-z)) + result_01*(ln(1-x))*(ln(1-z)*ln(1-z)/2) + result_10*(ln(1-x)*ln(1-x)/2)*(ln(1-z))
        elif orders == '100':
            result += - 44./3.*LMUR*NC*CF + 8./3.*LMUR*NF*CF
            result_1l = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_1l*ln(1-x)*ln(1-x)/2
            result_l1 = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_l1*ln(1-z)*ln(1-z)/2
            result_00 = + 11./3.*LMUR*NC*CF - 2./3.*LMUR*NF*CF
            result += result_00*(ln(1-x))*(ln(1-z))
        elif orders == '011':
            result += - 9./8.*LMUA*LMUF*pow(NC,-1)*CF + 9./8.*LMUA*LMUF*NC*CF
            result_0l = - 3./2.*LMUA*LMUF*pow(NC,-1)*CF + 3./2.*LMUA*LMUF*NC*CF
            result += result_0l*ln(1-x)
            result_l0 = - 3./2.*LMUA*LMUF*pow(NC,-1)*CF + 3./2.*LMUA*LMUF*NC*CF
            result += result_l0*ln(1-z)
            result_00 = - 2*LMUA*LMUF*pow(NC,-1)*CF + 2*LMUA*LMUF*NC*CF
            result += result_00*(ln(1-x))*(ln(1-z))
        elif orders == '101':
            result += - 11./4.*LMUA*LMUR*NC*CF + 1./2.*LMUA*LMUR*NF*CF
            result_l0 = - 11./3.*LMUA*LMUR*NC*CF + 2./3.*LMUA*LMUR*NF*CF
            result += result_l0*ln(1-z)
        elif orders == '110':
            result += - 11./4.*LMUF*LMUR*NC*CF + 1./2.*LMUF*LMUR*NF*CF
            result_0l = - 11./3.*LMUF*LMUR*NC*CF + 2./3.*LMUF*LMUR*NF*CF
            result += result_0l*ln(1-x)
        elif orders == '002':
            result += - 9./16.*pow(LMUA,2)*pow(NC,-1)*CF + 1./6.*pow(LMUA,2)*pow(NC,-1)*pow(pi,2)*CF + 31./16.*pow(LMUA,2)*NC*CF - 1./6.*pow(LMUA,2)*NC*pow(pi,2)*CF - 1./4.*pow(LMUA,2)*NF*CF
            result_l0 = + 10./3.*pow(LMUA,2)*NC*CF - 1./3.*pow(LMUA,2)*NF*CF - 3./2.*pow(LMUA,2)*pow(NC,-1)*CF
            result_l1 = - 2*pow(LMUA,2)*pow(NC,-1)*CF + 2*pow(LMUA,2)*NC*CF
            result += result_l0*ln(1-z) + result_l1*ln(1-z)*ln(1-z)/2
        elif orders == '020':
            result += - 9./16.*pow(LMUF,2)*pow(NC,-1)*CF + 1./6.*pow(LMUF,2)*pow(NC,-1)*pow(pi,2)*CF + 31./16.*pow(LMUF,2)*NC*CF - 1./6.*pow(LMUF,2)*NC*pow(pi,2)*CF - 1./4.*pow(LMUF,2)*NF*CF
            result_0l = - 3./2.*pow(LMUF,2)*pow(NC,-1)*CF + 10./3.*pow(LMUF,2)*NC*CF - 1./3.*pow(LMUF,2)*NF*CF
            result_1l = - 2*pow(LMUF,2)*pow(NC,-1)*CF + 2*pow(LMUF,2)*NC*CF
            result += result_0l*ln(1-x) + result_1l*ln(1-x)*ln(1-x)/2
        return result
    else:
        raise ValueError('Invalid rsl value')
