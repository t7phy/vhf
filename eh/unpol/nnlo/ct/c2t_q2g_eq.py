from configs.eh import *

LMUR = 1
LMUF = 1
LMUA = 1

def ct_nnlo_q2g_eq(x, z, rsl, orders):

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
                result += - 9*pow(NC,-1)*pow(z,-1)*CF - 4*pow(NC,-1)*pow(z,-1)*pow(rln2,2)*CF*pow(omx,-1) + 2*pow(\
      NC,-1)*pow(z,-1)*pow(rln2,2)*CF - 6*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1) + 4*pow(\
      NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF + 8./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) - 13./\
      12.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF + 41./4.*pow(NC,-1)*CF + 4*pow(NC,-1)*pow(rln2,2)*CF*\
      pow(omx,-1) + 2*pow(NC,-1)*sqrtxz1*rln2*CF*pow(omx,-1) - 10./3.*pow(NC,-1)*pow(pi,2)*CF*pow(\
      omx,-1) + 7./6.*pow(NC,-1)*pow(pi,2)*CF - 4*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*pow(NC,-1)*z*\
      CF - 2*pow(NC,-1)*z*pow(rln2,2)*CF*pow(omx,-1) + 5./3.*pow(NC,-1)*z*pow(pi,2)*CF*pow(omx,-1)\
       - 1./6.*pow(NC,-1)*z*pow(pi,2)*CF + 4*pow(NC,-1)*x*pow(z,-1)*CF + 2*pow(NC,-1)*x*pow(z,-1)*\
      pow(rln2,2)*CF + 2*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF - 29./12.*pow(NC,-1)*x*pow(z,-1)*\
      pow(pi,2)*CF - 2*pow(NC,-1)*x*CF*pow(omxmz,-1) + 23./4.*pow(NC,-1)*x*CF + 2*pow(NC,-1)*x*\
      sqrtxz1*rln2*CF + 25./6.*pow(NC,-1)*x*pow(pi,2)*CF - 11./2.*pow(NC,-1)*x*z*CF - 5./2.*pow(\
      NC,-1)*x*z*pow(pi,2)*CF + 2*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-1) - 2*pow(NC,-1)*pow(x,2)*CF\
       - 2*pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-1) + 215./18.*NC*pow(z,-1)*CF - 2*NC*pow(z,-1)*pow(\
      pi,2)*CF*pow(omx,-1) + 17./12.*NC*pow(z,-1)*pow(pi,2)*CF - 163./12.*NC*CF - 8*NC*pow(rln2,2)*\
      CF*pow(omx,-1) + 4*NC*pow(rln2,2)*CF - 4*NC*sqrtxz1*rln2*CF*pow(omx,-1) + 4./3.*NC*pow(pi,2)*\
      CF*pow(omx,-1)
                result +=  - 1./2.*NC*pow(pi,2)*CF + NC*z*CF*pow(omx,-1) + 4./3.*NC*z*CF - NC*z*pow(pi,2)*CF*\
      pow(omx,-1) + 1./6.*NC*z*pow(pi,2)*CF - 31./9.*NC*pow(z,2)*CF - 43./18.*NC*x*pow(z,-1)*CF + \
      17./12.*NC*x*pow(z,-1)*pow(pi,2)*CF - 37./12.*NC*x*CF + 4*NC*x*pow(rln2,2)*CF + 4*NC*x*\
      sqrtxz1*rln2*CF - 5./6.*NC*x*pow(pi,2)*CF + 1./3.*NC*x*z*CF + 4*NC*x*z*pow(rln2,2)*CF + 5./2.\
      *NC*x*z*pow(pi,2)*CF + 53./9.*NC*x*pow(z,2)*CF
                result +=  + 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(\
      omx,-1) - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*CF + 6*ln(1 + sqrtxz1 - z)*pow(\
      NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*\
      CF - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*\
      sqrtxz1*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) - 4*ln(1 + \
      sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF - 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*\
      sqrtxz1*CF - 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*sqrtxz1*CF - 4*ln(1 + sqrtxz1 - z)*NC*pow(\
      z,-1)*rln2*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)*rln2*CF + 12*ln(1 + sqrtxz1 - \
      z)*NC*rln2*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 - z)*NC*rln2*CF + 4*ln(1 + sqrtxz1 - z)*NC*\
      sqrtxz1*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*NC*z*rln2*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - \
      z)*NC*x*pow(z,-1)*rln2*CF - 4*ln(1 + sqrtxz1 - z)*NC*x*rln2*CF - 4*ln(1 + sqrtxz1 - z)*NC*x*\
      sqrtxz1*CF
                result +=  - 4*ln(1 + sqrtxz1 - z)*NC*x*z*rln2*CF - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(z,-1)*CF + 4*pow(ln(1 + \
      sqrtxz1 - z),2)*pow(NC,-1)*CF*pow(omx,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(z,-1)*CF + 4*pow(ln(1 + sqrtxz1 - z),\
      2)*NC*pow(z,-1)*CF*pow(omx,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*NC*pow(z,-1)*CF - 4*pow(ln(1 + \
      sqrtxz1 - z),2)*NC*CF*pow(omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*NC*z*CF*pow(omx,-1) - 2*pow(\
      ln(1 + sqrtxz1 - z),2)*NC*x*pow(z,-1)*CF - 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*pow(\
      z,-1)*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*CF - 4*ln(1 + \
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z\
      )*NC*CF - 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*z*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - \
      z)*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1)*CF + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*x*CF\
       + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*x*z*CF + 4*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*\
      rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*rln2*CF + 4*ln(1 + sqrtxz1 + z)*NC*\
      rln2*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 + z)*NC*rln2*CF + 2*ln(1 + sqrtxz1 + z)*NC*z*rln2*CF*\
      pow(omx,-1) - 2*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1)*rln2*CF - 4*ln(1 + sqrtxz1 + z)*NC*x*rln2*\
      CF
                result +=  - 4*ln(1 + sqrtxz1 + z)*NC*x*z*rln2*CF + 12*ln(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       + 1./4.*ln(x)*pow(NC,-1)*pow(z,-1)*CF - 6*ln(x)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) + 3\
      *ln(x)*pow(NC,-1)*pow(z,-1)*rln2*CF - 3*ln(x)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 2\
      *ln(x)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF - 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1) + ln(x)*pow(\
      NC,-1)*CF + 6*ln(x)*pow(NC,-1)*rln2*CF*pow(omx,-1) + ln(x)*pow(NC,-1)*sqrtxz1*CF*pow(omx,-1)\
       + 51./4.*ln(x)*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*ln(x)*pow(NC,-1)*z*CF - 3*ln(x)*pow(\
      NC,-1)*z*rln2*CF*pow(omx,-1) - 43./4.*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF + 3*ln(x)*pow(NC,-1)*x*\
      pow(z,-1)*rln2*CF + ln(x)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 4*ln(x)*pow(NC,-1)*x*CF + 4*ln(\
      x)*pow(NC,-1)*x*CF*omx + ln(x)*pow(NC,-1)*x*sqrtxz1*CF - 15./2.*ln(x)*pow(NC,-1)*x*z*CF - 2*\
      ln(x)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-2) + 2*ln(x)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-1) + 2\
      *ln(x)*pow(NC,-1)*pow(x,2)*CF + 2*ln(x)*pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-2) - 4*ln(x)*pow(\
      NC,-1)*pow(x,3)*CF*pow(omxmz,-1) - 2*ln(x)*pow(NC,-1)*pow(x,4)*CF*pow(omxmz,-2) + 35./3.*ln(x\
      )*NC*pow(z,-1)*CF*pow(omx,-1) - 163./12.*ln(x)*NC*pow(z,-1)*CF + 4*ln(x)*NC*pow(z,-1)*rln2*CF\
      *pow(omx,-1) - 2*ln(x)*NC*pow(z,-1)*rln2*CF - 4*ln(x)*NC*CF*pow(omx,-1) + ln(x)*NC*CF - 8*ln(\
      x)*NC*rln2*CF*pow(omx,-1) + 2*ln(x)*NC*rln2*CF - 2*ln(x)*NC*sqrtxz1*CF*pow(omx,-1) - 51./4.*\
      ln(x)*NC*z*CF*pow(omx,-1)
                result +=  + 13./2.*ln(x)*NC*z*CF + 2*ln(x)*NC*z*rln2*CF*pow(omx,-1) - 8./3.*ln(x)*NC*pow(z,2)*\
      CF*pow(omx,-1) - 8./3.*ln(x)*NC*pow(z,2)*CF - 67./12.*ln(x)*NC*x*pow(z,-1)*CF - 2*ln(x)*NC*x*\
      pow(z,-1)*rln2*CF + 5*ln(x)*NC*x*CF + 2*ln(x)*NC*x*rln2*CF + 2*ln(x)*NC*x*sqrtxz1*CF + 13./2.\
      *ln(x)*NC*x*z*CF + 2*ln(x)*NC*x*z*rln2*CF + 16./3.*ln(x)*NC*x*pow(z,2)*CF
                result +=  + 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*ln(x)*\
      ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*CF*pow(\
      omx,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 - \
      z)*pow(NC,-1)*x*pow(z,-1)*CF - 4*ln(x)*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*\
      ln(x)*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)*CF + 4*ln(x)*ln(1 + sqrtxz1 - z)*NC*CF*pow(omx,-1) - 2\
      *ln(x)*ln(1 + sqrtxz1 - z)*NC*z*CF*pow(omx,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*NC*x*pow(z,-1)*\
      CF + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(x)*ln(1 + sqrtxz1\
       + z)*pow(NC,-1)*pow(z,-1)*CF - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*CF*pow(omx,-1) + ln(x)\
      *ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*\
      pow(z,-1)*CF + 4*ln(x)*ln(1 + sqrtxz1 + z)*NC*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*NC\
      *CF - 2*ln(x)*ln(1 + sqrtxz1 + z)*NC*x*CF - 2*ln(x)*ln(1 + sqrtxz1 + z)*NC*x*z*CF - 17*pow(\
      ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 11./2.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF + \
      24*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) - 9*pow(ln(x),2)*pow(NC,-1)*CF - 12*pow(ln(x),2)*\
      pow(NC,-1)*z*CF*pow(omx,-1)
                result +=  + 1./2.*pow(ln(x),2)*pow(NC,-1)*z*CF + 25./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF\
       - 23*pow(ln(x),2)*pow(NC,-1)*x*CF + 31./2.*pow(ln(x),2)*pow(NC,-1)*x*z*CF + 10*pow(ln(x),2)*\
      NC*pow(z,-1)*CF*pow(omx,-1) - 11./2.*pow(ln(x),2)*NC*pow(z,-1)*CF - 10*pow(ln(x),2)*NC*CF*\
      pow(omx,-1) + 9*pow(ln(x),2)*NC*CF + 5*pow(ln(x),2)*NC*z*CF*pow(omx,-1) - 1./2.*pow(ln(x),2)*\
      NC*z*CF - 11./2.*pow(ln(x),2)*NC*x*pow(z,-1)*CF + 9*pow(ln(x),2)*NC*x*CF - 17./2.*pow(ln(x),2\
      )*NC*x*z*CF + 16*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 5*ln(x)*ln(z)*pow(NC,-1)*\
      pow(z,-1)*CF - 25*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 10*ln(x)*ln(z)*pow(NC,-1)*CF + 25./\
      2.*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 11*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 20*\
      ln(x)*ln(z)*pow(NC,-1)*x*CF - 17*ln(x)*ln(z)*pow(NC,-1)*x*z*CF - 6*ln(x)*ln(z)*NC*pow(z,-1)*\
      CF*pow(omx,-1) + 3*ln(x)*ln(z)*NC*pow(z,-1)*CF + 19*ln(x)*ln(z)*NC*CF*pow(omx,-1) - 18*ln(x)*\
      ln(z)*NC*CF + 7./2.*ln(x)*ln(z)*NC*z*CF*pow(omx,-1) + 3*ln(x)*ln(z)*NC*x*pow(z,-1)*CF - 16*\
      ln(x)*ln(z)*NC*x*CF - ln(x)*ln(z)*NC*x*z*CF + 20*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) - 5*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF - 26*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(\
      omx,-1) + 10*ln(x)*ln(omx)*pow(NC,-1)*CF + 13*ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(\
      x)*ln(omx)*pow(NC,-1)*z*CF - 15*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF + 30*ln(x)*ln(omx)*\
      pow(NC,-1)*x*CF
                result +=  - 19*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 16*ln(x)*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1)\
       + 8*ln(x)*ln(omx)*NC*pow(z,-1)*CF + 16*ln(x)*ln(omx)*NC*CF*pow(omx,-1) - 16*ln(x)*ln(omx)*NC\
      *CF - 8*ln(x)*ln(omx)*NC*z*CF*pow(omx,-1) + ln(x)*ln(omx)*NC*z*CF + 8*ln(x)*ln(omx)*NC*x*pow(\
      z,-1)*CF - 16*ln(x)*ln(omx)*NC*x*CF + 15*ln(x)*ln(omx)*NC*x*z*CF + 24*ln(x)*ln(omz)*pow(\
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 15./2.*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 34*ln(x)*ln(\
      omz)*pow(NC,-1)*CF*pow(omx,-1) + 13*ln(x)*ln(omz)*pow(NC,-1)*CF + 17*ln(x)*ln(omz)*pow(NC,-1)\
      *z*CF*pow(omx,-1) - ln(x)*ln(omz)*pow(NC,-1)*z*CF - 35./2.*ln(x)*ln(omz)*pow(NC,-1)*x*pow(\
      z,-1)*CF + 33*ln(x)*ln(omz)*pow(NC,-1)*x*CF - 22*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF - 14*ln(x)*\
      ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 15./2.*ln(x)*ln(omz)*NC*pow(z,-1)*CF + 14*ln(x)*ln(omz)\
      *NC*CF*pow(omx,-1) - 13*ln(x)*ln(omz)*NC*CF - 7*ln(x)*ln(omz)*NC*z*CF*pow(omx,-1) + ln(x)*ln(\
      omz)*NC*z*CF + 15./2.*ln(x)*ln(omz)*NC*x*pow(z,-1)*CF - 13*ln(x)*ln(omz)*NC*x*CF + 12*ln(x)*\
      ln(omz)*NC*x*z*CF - 3*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 5*ln(z)*pow(NC,-1)*pow(\
      z,-1)*CF - 2*ln(z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) + ln(z)*pow(NC,-1)*pow(z,-1)*rln2\
      *CF - 3*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 2*ln(z)*pow(NC,-1)*pow(z,-1)*\
      sqrtxz1*CF + 8*ln(z)*pow(NC,-1)*CF*pow(omx,-1) - 4*ln(z)*pow(NC,-1)*CF + 2*ln(z)*pow(NC,-1)*\
      rln2*CF*pow(omx,-1)
                result +=  + ln(z)*pow(NC,-1)*sqrtxz1*CF*pow(omx,-1) - 7*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(\
      z)*pow(NC,-1)*z*CF - ln(z)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) + 5*ln(z)*pow(NC,-1)*x*pow(z,-1)*\
      CF + ln(z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF + ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 7*ln(z)\
      *pow(NC,-1)*x*CF + ln(z)*pow(NC,-1)*x*sqrtxz1*CF + 9*ln(z)*pow(NC,-1)*x*z*CF + 4*ln(z)*NC*\
      pow(z,-1)*CF*pow(omx,-1) + 44./3.*ln(z)*NC*pow(z,-1)*CF - 4*ln(z)*NC*pow(z,-1)*rln2*CF*pow(\
      omx,-1) + 2*ln(z)*NC*pow(z,-1)*rln2*CF - 2*ln(z)*NC*CF*pow(omx,-1) + 14*ln(z)*NC*CF - 8*ln(z)\
      *NC*rln2*CF*pow(omx,-1) + 6*ln(z)*NC*rln2*CF - 2*ln(z)*NC*sqrtxz1*CF*pow(omx,-1) + 6*ln(z)*NC\
      *z*CF*pow(omx,-1) + 2*ln(z)*NC*z*CF - 2*ln(z)*NC*z*rln2*CF*pow(omx,-1) + 4./3.*ln(z)*NC*pow(\
      z,2)*CF + 11./3.*ln(z)*NC*x*pow(z,-1)*CF + 2*ln(z)*NC*x*pow(z,-1)*rln2*CF - 2*ln(z)*NC*x*CF\
       + 6*ln(z)*NC*x*rln2*CF + 2*ln(z)*NC*x*sqrtxz1*CF - 13*ln(z)*NC*x*z*CF + 6*ln(z)*NC*x*z*rln2*\
      CF - 8./3.*ln(z)*NC*x*pow(z,2)*CF
                result +=  + 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - \
      ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*CF\
      *pow(omx,-1) + ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(z)*ln(1 + sqrtxz1\
       - z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*ln(z)*ln(1 + sqrtxz1 - z)*NC*CF*pow(omx,-1) - 2*ln(z)*ln(\
      1 + sqrtxz1 - z)*NC*CF - 2*ln(z)*ln(1 + sqrtxz1 - z)*NC*x*CF - 2*ln(z)*ln(1 + sqrtxz1 - z)*NC\
      *x*z*CF + 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + \
      z)*NC*pow(z,-1)*CF + 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*CF*pow(omx,-1) - 4*ln(z)*ln(1 + sqrtxz1\
       + z)*NC*CF + 2*ln(z)*ln(1 + sqrtxz1 + z)*NC*z*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*\
      NC*x*pow(z,-1)*CF - 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*x*CF - 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*x*z*\
      CF - 4*ln(z)*ln(1 + z)*NC*pow(z,-1)*CF*pow(omx,-1) - 4*ln(z)*ln(1 + z)*NC*CF*pow(omx,-1) - 2*\
      ln(z)*ln(1 + z)*NC*z*CF*pow(omx,-1) - 3*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + \
      pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF + 6*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) - 4*pow(ln(z)\
      ,2)*pow(NC,-1)*CF - 3*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*pow(ln(z),2)*pow(\
      NC,-1)*z*CF
                result +=  + 2*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF - 4*pow(ln(z),2)*pow(NC,-1)*x*CF + 9./2.*\
      pow(ln(z),2)*pow(NC,-1)*x*z*CF + pow(ln(z),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 5./2.*pow(ln(z),2\
      )*NC*pow(z,-1)*CF - 3*pow(ln(z),2)*NC*CF*pow(omx,-1) + 9*pow(ln(z),2)*NC*CF + 1./2.*pow(ln(z)\
      ,2)*NC*z*CF*pow(omx,-1) + 1./2.*pow(ln(z),2)*NC*z*CF + 5./2.*pow(ln(z),2)*NC*x*pow(z,-1)*CF\
       + 7*pow(ln(z),2)*NC*x*CF + 15./2.*pow(ln(z),2)*NC*x*z*CF - 8*ln(z)*ln(omx)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) + 3*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF + 12*ln(z)*ln(omx)*pow(NC,-1)*\
      CF*pow(omx,-1) - 6*ln(z)*ln(omx)*pow(NC,-1)*CF - 6*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 7*ln(z)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 12*ln(z)*ln(omx)*pow(NC,-1)*x*CF + 9*ln(z)*ln(\
      omx)*pow(NC,-1)*x*z*CF + 8*ln(z)*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) - 3*ln(z)*ln(omx)*NC*\
      pow(z,-1)*CF - 8*ln(z)*ln(omx)*NC*CF*pow(omx,-1) + 14*ln(z)*ln(omx)*NC*CF + 4*ln(z)*ln(omx)*\
      NC*z*CF*pow(omx,-1) - 3*ln(z)*ln(omx)*NC*x*pow(z,-1)*CF + 12*ln(z)*ln(omx)*NC*x*CF - ln(z)*\
      ln(omx)*NC*x*z*CF - 12*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 4*ln(z)*ln(omz)*\
      pow(NC,-1)*pow(z,-1)*CF + 20*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 8*ln(z)*ln(omz)*pow(\
      NC,-1)*CF - 10*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + 6*ln(z)*ln(omz)*pow(NC,-1)*x*pow(\
      z,-1)*CF - 12*ln(z)*ln(omz)*pow(NC,-1)*x*CF + 10*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF + 4*ln(z)*\
      ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1)
                result +=  - 5*ln(z)*ln(omz)*NC*pow(z,-1)*CF - 4*ln(z)*ln(omz)*NC*CF*pow(omx,-1) + 10*ln(z)*ln(\
      omz)*NC*CF + 2*ln(z)*ln(omz)*NC*z*CF*pow(omx,-1) - 5*ln(z)*ln(omz)*NC*x*pow(z,-1)*CF + 10*ln(\
      z)*ln(omz)*NC*x*CF - 10*ln(z)*ln(omz)*NC*x*z*CF - 6*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) - 11./4.*ln(omx)*pow(NC,-1)*pow(z,-1)*CF + 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 4*\
      ln(omx)*pow(NC,-1)*CF - 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 1./2.*ln(omx)*pow(NC,-1)*z*CF\
       + 17./4.*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 3*ln(omx)*pow(NC,-1)*x*CF + 4*ln(omx)*pow(\
      NC,-1)*x*z*CF + 4*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) + 125./12.*ln(omx)*NC*pow(z,-1)*CF - 4*\
      ln(omx)*NC*CF*pow(omx,-1) - 3*ln(omx)*NC*CF + 4*ln(omx)*NC*z*CF*pow(omx,-1) - 7./2.*ln(omx)*\
      NC*z*CF + 4./3.*ln(omx)*NC*pow(z,2)*CF + 41./12.*ln(omx)*NC*x*pow(z,-1)*CF - 6*ln(omx)*NC*x*\
      CF - 3*ln(omx)*NC*x*z*CF - 8./3.*ln(omx)*NC*x*pow(z,2)*CF
                result +=  - 5*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 2*pow(ln(omx),2)*pow(\
      NC,-1)*pow(z,-1)*CF + 6*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) - 3*pow(ln(omx),2)*pow(\
      NC,-1)*CF - 3*pow(ln(omx),2)*pow(NC,-1)*z*CF*pow(omx,-1) + 1./2.*pow(ln(omx),2)*pow(NC,-1)*z*\
      CF + 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1)*CF - 11*pow(ln(omx),2)*pow(NC,-1)*x*CF + 13./2.*\
      pow(ln(omx),2)*pow(NC,-1)*x*z*CF + 4*pow(ln(omx),2)*NC*pow(z,-1)*CF*pow(omx,-1) - 7./2.*pow(\
      ln(omx),2)*NC*pow(z,-1)*CF - 4*pow(ln(omx),2)*NC*CF*pow(omx,-1) + 6*pow(ln(omx),2)*NC*CF + 2*\
      pow(ln(omx),2)*NC*z*CF*pow(omx,-1) - 1./2.*pow(ln(omx),2)*NC*z*CF - 7./2.*pow(ln(omx),2)*NC*x\
      *pow(z,-1)*CF + 6*pow(ln(omx),2)*NC*x*CF - 11./2.*pow(ln(omx),2)*NC*x*z*CF - 12*ln(omx)*ln(\
      omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 5*ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 16*ln(\
      omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 8*ln(omx)*ln(omz)*pow(NC,-1)*CF - 8*ln(omx)*ln(omz)*\
      pow(NC,-1)*z*CF*pow(omx,-1) + ln(omx)*ln(omz)*pow(NC,-1)*z*CF + 11*ln(omx)*ln(omz)*pow(NC,-1)\
      *x*pow(z,-1)*CF - 20*ln(omx)*ln(omz)*pow(NC,-1)*x*CF + 13*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF\
       + 4*ln(omx)*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1)
                result +=  - 6*ln(omx)*ln(omz)*NC*pow(z,-1)*CF - 4*ln(omx)*ln(omz)*NC*CF*pow(omx,-1) + 10*ln(omx\
      )*ln(omz)*NC*CF + 2*ln(omx)*ln(omz)*NC*z*CF*pow(omx,-1) - ln(omx)*ln(omz)*NC*z*CF - 6*ln(omx)\
      *ln(omz)*NC*x*pow(z,-1)*CF + 10*ln(omx)*ln(omz)*NC*x*CF - 9*ln(omx)*ln(omz)*NC*x*z*CF - 8*ln(\
      omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 11./4.*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 8*ln(omz)\
      *pow(NC,-1)*CF*pow(omx,-1) + ln(omz)*pow(NC,-1)*CF - 8*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + \
      2*ln(omz)*pow(NC,-1)*z*CF + 25./4.*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF - 4*ln(omz)*pow(NC,-1)*x\
      *CF*omx + 9./2.*ln(omz)*pow(NC,-1)*x*z*CF + 2*ln(omz)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-2) - \
      2*ln(omz)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-1) - 2*ln(omz)*pow(NC,-1)*pow(x,2)*CF - 2*ln(omz)\
      *pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-2) + 4*ln(omz)*pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-1) + 2*\
      ln(omz)*pow(NC,-1)*pow(x,4)*CF*pow(omxmz,-2) + 2*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 125./\
      12.*ln(omz)*NC*pow(z,-1)*CF - 2*ln(omz)*NC*CF*pow(omx,-1) - 6*ln(omz)*NC*CF + 2*ln(omz)*NC*z*\
      CF*pow(omx,-1) - 5*ln(omz)*NC*z*CF + 4./3.*ln(omz)*NC*pow(z,2)*CF + 65./12.*ln(omz)*NC*x*pow(\
      z,-1)*CF - 6*ln(omz)*NC*x*CF + 1./2.*ln(omz)*NC*x*z*CF - 8./3.*ln(omz)*NC*x*pow(z,2)*CF
                result += - 8*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 3*pow(ln(omz),2)*pow(\
      NC,-1)*pow(z,-1)*CF + 12*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) - 5*pow(ln(omz),2)*pow(\
      NC,-1)*CF - 6*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1) + 1./2.*pow(ln(omz),2)*pow(NC,-1)*z*\
      CF + 7*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1)*CF - 13*pow(ln(omz),2)*pow(NC,-1)*x*CF + 17./2.*\
      pow(ln(omz),2)*pow(NC,-1)*x*z*CF + pow(ln(omz),2)*NC*pow(z,-1)*CF*pow(omx,-1) - 5./2.*pow(ln(\
      omz),2)*NC*pow(z,-1)*CF - pow(ln(omz),2)*NC*CF*pow(omx,-1) + 4*pow(ln(omz),2)*NC*CF + 1./2.*\
      pow(ln(omz),2)*NC*z*CF*pow(omx,-1) - 1./2.*pow(ln(omz),2)*NC*z*CF - 5./2.*pow(ln(omz),2)*NC*x\
      *pow(z,-1)*CF + 4*pow(ln(omz),2)*NC*x*CF - 7./2.*pow(ln(omz),2)*NC*x*z*CF + 2*Li2(1./2. - 1./\
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(1./2. - 1./\
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF
                result +=  - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*CF*pow(omx,-1)\
       + Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(1.\
      /2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2(1./2. - 1./\
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*Li2(1./2. - 1./2.*\
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*\
      pow(z,-1)*sqrtxz1)*NC*CF - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*z*CF*\
      pow(omx,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*pow(z,-1)*CF + 2*\
      Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*CF + 2*Li2(1./2. - 1./2.*pow(\
      z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*z*CF - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
      sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*\
      pow(NC,-1)*CF*pow(omx,-1) - Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)\
      *z*CF*pow(omx,-1) + Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(\
      z,-1)*CF + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF*pow(\
      omx,-1) - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF - 2*Li2(1./\
      2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*CF
                result +=  + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*z*CF*pow(omx,-1) - 2*\
      Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*pow(z,-1)*CF - 2*Li2(1./2. + 1./2.\
      *pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*CF - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(\
      z,-1)*sqrtxz1)*NC*x*z*CF + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*\
      pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF - 2*Li2(1./2. - 1./\
      2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*CF*pow(omx,-1) + Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(\
      NC,-1)*z*CF*pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*\
      Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*CF*pow(omx,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*\
      z)*NC*CF - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*x*CF - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./\
      2.*z)*NC*x*z*CF - 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       + Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(1./2. - 1./2.*sqrtxz1\
       + 1./2.*z)*pow(NC,-1)*CF*pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*z*CF*\
      pow(omx,-1) + Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2(1./2. - \
      1./2.*sqrtxz1 + 1./2.*z)*NC*CF*pow(omx,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*CF + 2\
      *Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*x*CF + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*x*z\
      *CF
                result +=  + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(1 - x*pow(z,-1))*\
      pow(NC,-1)*pow(z,-1)*CF - 4*Li2(1 - x*pow(z,-1))*pow(NC,-1)*CF*pow(omx,-1) + 2*Li2(1 - x*pow(\
      z,-1))*pow(NC,-1)*CF + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(1 - x*pow(\
      z,-1))*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*CF - 2*Li2(1 - x*pow(\
      z,-1))*pow(NC,-1)*x*z*CF - 2*Li2(1 - x*pow(z,-1))*NC*pow(z,-1)*CF*pow(omx,-1) + Li2(1 - x*\
      pow(z,-1))*NC*pow(z,-1)*CF + 2*Li2(1 - x*pow(z,-1))*NC*CF*pow(omx,-1) - 2*Li2(1 - x*pow(z,-1)\
      )*NC*CF - Li2(1 - x*pow(z,-1))*NC*z*CF*pow(omx,-1) + Li2(1 - x*pow(z,-1))*NC*x*pow(z,-1)*CF\
       - 2*Li2(1 - x*pow(z,-1))*NC*x*CF + 2*Li2(1 - x*pow(z,-1))*NC*x*z*CF - 4*Li2( - z)*NC*pow(\
      z,-1)*CF*pow(omx,-1) - 4*Li2( - z)*NC*CF*pow(omx,-1) - 2*Li2( - z)*NC*z*CF*pow(omx,-1) - 2*\
      Li2(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 3./2.*Li2(x)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(x)*\
      pow(NC,-1)*CF*pow(omx,-1) - Li2(x)*pow(NC,-1)*CF - Li2(x)*pow(NC,-1)*z*CF*pow(omx,-1) + 3./2.\
      *Li2(x)*pow(NC,-1)*x*pow(z,-1)*CF - Li2(x)*pow(NC,-1)*x*CF + Li2(x)*pow(NC,-1)*x*z*CF - 1./2.\
      *Li2(x)*NC*pow(z,-1)*CF - Li2(x)*NC*CF - 1./2.*Li2(x)*NC*x*pow(z,-1)*CF - Li2(x)*NC*x*CF + \
      Li2(x)*NC*x*z*CF - 4*Li2(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 6*Li2(z)*pow(NC,-1)*CF*pow(\
      omx,-1) - 3*Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(z)*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(z\
      )*pow(NC,-1)*x*CF
                result +=  - Li2(z)*pow(NC,-1)*x*z*CF - 3*Li2(z)*NC*pow(z,-1)*CF - 2*Li2(z)*NC*CF - 3*Li2(z)*NC*\
      x*pow(z,-1)*CF - 11*Li2(z)*NC*x*z*CF
            if z < round(1 - x, ndecimals) and z < x:
                result += 4*pow(NC,-1)*pow(z,-1)*CF - 5./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) + 1./6.*\
      pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF - 6*pow(NC,-1)*CF + 2*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1)\
       - 1./3.*pow(NC,-1)*pow(pi,2)*CF + 4*pow(NC,-1)*z*CF*pow(omx,-1) - pow(NC,-1)*z*pow(pi,2)*CF*\
      pow(omx,-1) - 4*pow(NC,-1)*x*pow(z,-1)*CF + 3./2.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*CF - 3*\
      pow(NC,-1)*x*pow(pi,2)*CF + 5./3.*pow(NC,-1)*x*z*pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*pow(z,-1)\
      *CF*pow(omx,-1) + 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1) - 12*ln(x)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 12*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF - 12*ln(x)*pow(NC,-1)*x*CF + 12*ln(x)*pow(NC,-1)*x*z*CF\
       + 13*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 3*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*\
      CF - 19*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) + 6*pow(ln(x),2)*pow(NC,-1)*CF + 19./2.*pow(\
      ln(x),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 10*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF + 20*pow(ln(\
      x),2)*pow(NC,-1)*x*CF - 13*pow(ln(x),2)*pow(NC,-1)*x*z*CF - 16*ln(x)*ln(z)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) + 5*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF + 26*ln(x)*ln(z)*pow(NC,-1)*CF*\
      pow(omx,-1) - 10*ln(x)*ln(z)*pow(NC,-1)*CF - 13*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 11*\
      ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF - 22*ln(x)*ln(z)*pow(NC,-1)*x*CF + 16*ln(x)*ln(z)*pow(\
      NC,-1)*x*z*CF - 20*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 4*ln(x)*ln(omx)*pow(\
      NC,-1)*pow(z,-1)*CF
                result +=  + 28*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) - 8*ln(x)*ln(omx)*pow(NC,-1)*CF - 14*ln(\
      x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 16*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 32*ln(x\
      )*ln(omx)*pow(NC,-1)*x*CF + 20*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 22*ln(x)*ln(omz)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) + 5*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 32*ln(x)*ln(omz)*pow(\
      NC,-1)*CF*pow(omx,-1) - 10*ln(x)*ln(omz)*pow(NC,-1)*CF - 16*ln(x)*ln(omz)*pow(NC,-1)*z*CF*\
      pow(omx,-1) + 17*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF - 34*ln(x)*ln(omz)*pow(NC,-1)*x*CF\
       + 22*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + 2*ln(x)*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       - ln(x)*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x\
      )*ln(xmz)*pow(NC,-1)*CF + 2*ln(x)*ln(xmz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln(xmz)*pow(\
      NC,-1)*x*pow(z,-1)*CF + 2*ln(x)*ln(xmz)*pow(NC,-1)*x*CF - 2*ln(x)*ln(xmz)*pow(NC,-1)*x*z*CF\
       + 4*ln(x)*ln(omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(x)*ln(omxmz)*pow(NC,-1)*pow(\
      z,-1)*CF - 6*ln(x)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x)*ln(omxmz)*pow(NC,-1)*CF + 3*\
      ln(x)*ln(omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*ln(x)*ln(omxmz)*pow(NC,-1)*x*pow(z,-1)*CF + 6\
      *ln(x)*ln(omxmz)*pow(NC,-1)*x*CF - 4*ln(x)*ln(omxmz)*pow(NC,-1)*x*z*CF + 6*ln(z)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) - 6*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(z)*pow(NC,-1)*z*CF*pow(\
      omx,-1)
                result +=  - 6*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(z)*pow(NC,-1)*x*CF - 6*ln(z)*pow(NC,-1)*x*\
      z*CF + 5*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*pow(ln(z),2)*pow(NC,-1)*pow(\
      z,-1)*CF - 9*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(ln(z),2)*pow(NC,-1)*CF + 9./2.*\
      pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF + 6*pow(\
      ln(z),2)*pow(NC,-1)*x*CF - 5*pow(ln(z),2)*pow(NC,-1)*x*z*CF + 8*ln(z)*ln(omx)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF - 12*ln(z)*ln(omx)*pow(NC,-1)*\
      CF*pow(omx,-1) + 4*ln(z)*ln(omx)*pow(NC,-1)*CF + 6*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1)\
       - 6*ln(z)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF + 12*ln(z)*ln(omx)*pow(NC,-1)*x*CF - 8*ln(z)*ln(\
      omx)*pow(NC,-1)*x*z*CF + 12*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 4*ln(z)*ln(\
      omz)*pow(NC,-1)*pow(z,-1)*CF - 20*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(z)*ln(omz)*\
      pow(NC,-1)*CF + 10*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(z)*ln(omz)*pow(NC,-1)*x*\
      pow(z,-1)*CF + 16*ln(z)*ln(omz)*pow(NC,-1)*x*CF - 12*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF - 2*ln(z\
      )*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + ln(z)*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(\
      z)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(xmz)*pow(NC,-1)*CF - 2*ln(z)*ln(xmz)*pow(\
      NC,-1)*z*CF*pow(omx,-1) + ln(z)*ln(xmz)*pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(z)*ln(xmz)*pow(\
      NC,-1)*x*CF
                result +=  + 2*ln(z)*ln(xmz)*pow(NC,-1)*x*z*CF + 6*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       - 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*\
      pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(omx)*pow(NC,-1)*x*CF - 6*ln(omx)*pow(NC,-1)*x*z*CF + 5*pow(\
      ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 1./2.*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF\
       - 6*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) + pow(ln(omx),2)*pow(NC,-1)*CF + 3*pow(ln(omx),\
      2)*pow(NC,-1)*z*CF*pow(omx,-1) - 9./2.*pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1)*CF + 9*pow(ln(\
      omx),2)*pow(NC,-1)*x*CF - 5*pow(ln(omx),2)*pow(NC,-1)*x*z*CF + 16*ln(omx)*ln(omz)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) - 3*ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 22*ln(omx)*ln(omz)*\
      pow(NC,-1)*CF*pow(omx,-1) + 6*ln(omx)*ln(omz)*pow(NC,-1)*CF + 11*ln(omx)*ln(omz)*pow(NC,-1)*z\
      *CF*pow(omx,-1) - 13*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF + 26*ln(omx)*ln(omz)*pow(\
      NC,-1)*x*CF - 16*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF + 8*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) - 8*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(\
      omz)*pow(NC,-1)*x*pow(z,-1)*CF + 8*ln(omz)*pow(NC,-1)*x*CF - 8*ln(omz)*pow(NC,-1)*x*z*CF + 8*\
      pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 3./2.*pow(ln(omz),2)*pow(NC,-1)*pow(\
      z,-1)*CF - 11*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) + 3*pow(ln(omz),2)*pow(NC,-1)*CF + 11./\
      2.*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1)
                result +=  - 13./2.*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1)*CF + 13*pow(ln(omz),2)*pow(NC,-1)*x*CF\
       - 8*pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 4*ln(omz)*ln(omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) + ln(omz)*ln(omxmz)*pow(NC,-1)*pow(z,-1)*CF + 6*ln(omz)*ln(omxmz)*pow(NC,-1)*CF*pow(\
      omx,-1) - 2*ln(omz)*ln(omxmz)*pow(NC,-1)*CF - 3*ln(omz)*ln(omxmz)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 3*ln(omz)*ln(omxmz)*pow(NC,-1)*x*pow(z,-1)*CF - 6*ln(omz)*ln(omxmz)*pow(NC,-1)*x*CF + 4*\
      ln(omz)*ln(omxmz)*pow(NC,-1)*x*z*CF - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1)\
      *CF*pow(omx,-1) + Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1)*CF + 4*Li2(pow(x,-1)*\
      z*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1) - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*\
      CF - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(pow(x,-1)*z*pow(\
      omx,-1)*omz)*pow(NC,-1)*x*pow(z,-1)*CF - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*x*CF\
       + 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*x*z*CF - 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*CF + 4*Li2(omx*pow(\
      omz,-1))*pow(NC,-1)*CF*pow(omx,-1) - 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*CF - 2*Li2(omx*pow(\
      omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1)*CF - 2*\
      Li2(omx*pow(omz,-1))*pow(NC,-1)*x*CF + 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*x*z*CF - Li2(z*pow(\
      omx,-1))*pow(NC,-1)*pow(z,-1)*CF
                result +=  - 2*Li2(z*pow(omx,-1))*pow(NC,-1)*CF*pow(omx,-1) + 2*Li2(z*pow(omx,-1))*pow(NC,-1)*CF\
       + Li2(z*pow(omx,-1))*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(z*pow(omx,-1))*pow(NC,-1)*x*pow(z,-1)\
      *CF - 2*Li2(z*pow(omx,-1))*pow(NC,-1)*x*CF + 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) - 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) + \
      Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(x*z*pow(omx,-1)*pow(\
      omz,-1))*pow(NC,-1)*x*pow(z,-1)*CF + 4*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x*CF - 2*\
      Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x*z*CF + 2*Li2(z)*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) - 2*Li2(z)*pow(NC,-1)*CF*pow(omx,-1) + Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(z)*\
      pow(NC,-1)*x*pow(z,-1)*CF + 4*Li2(z)*pow(NC,-1)*x*CF - 2*Li2(z)*pow(NC,-1)*x*z*CF
            if z > round(1 - x, ndecimals) and z < x:
                result += 4*pow(NC,-1)*pow(z,-1)*CF - 5./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) + 1./6.*\
      pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF - 6*pow(NC,-1)*CF + 2*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1)\
       - 1./3.*pow(NC,-1)*pow(pi,2)*CF + 4*pow(NC,-1)*z*CF*pow(omx,-1) - pow(NC,-1)*z*pow(pi,2)*CF*\
      pow(omx,-1) - 4*pow(NC,-1)*x*pow(z,-1)*CF + 3./2.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*CF - 3*\
      pow(NC,-1)*x*pow(pi,2)*CF + 5./3.*pow(NC,-1)*x*z*pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*pow(z,-1)\
      *CF*pow(omx,-1) + 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1) - 12*ln(x)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 12*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF - 12*ln(x)*pow(NC,-1)*x*CF + 12*ln(x)*pow(NC,-1)*x*z*CF\
       + 4*ln(x)*ln( - omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(x)*ln( - omxmz)*pow(NC,-1)*\
      pow(z,-1)*CF - 6*ln(x)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x)*ln( - omxmz)*pow(\
      NC,-1)*CF + 3*ln(x)*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*ln(x)*ln( - omxmz)*pow(\
      NC,-1)*x*pow(z,-1)*CF + 6*ln(x)*ln( - omxmz)*pow(NC,-1)*x*CF - 4*ln(x)*ln( - omxmz)*pow(\
      NC,-1)*x*z*CF + 13*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 7./2.*pow(ln(x),2)*pow(\
      NC,-1)*pow(z,-1)*CF - 20*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) + 7*pow(ln(x),2)*pow(NC,-1)*\
      CF + 10*pow(ln(x),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 19./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)\
      *CF + 19*pow(ln(x),2)*pow(NC,-1)*x*CF - 13*pow(ln(x),2)*pow(NC,-1)*x*z*CF - 20*ln(x)*ln(z)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)
                result +=  + 6*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF + 32*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) - \
      12*ln(x)*ln(z)*pow(NC,-1)*CF - 16*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 14*ln(x)*ln(z)*\
      pow(NC,-1)*x*pow(z,-1)*CF - 28*ln(x)*ln(z)*pow(NC,-1)*x*CF + 20*ln(x)*ln(z)*pow(NC,-1)*x*z*CF\
       - 16*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 3*ln(x)*ln(omx)*pow(NC,-1)*pow(\
      z,-1)*CF + 22*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) - 6*ln(x)*ln(omx)*pow(NC,-1)*CF - 11*\
      ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 13*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 26*\
      ln(x)*ln(omx)*pow(NC,-1)*x*CF + 16*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 22*ln(x)*ln(omz)*pow(\
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 6*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 34*ln(x)*ln(omz)*\
      pow(NC,-1)*CF*pow(omx,-1) - 12*ln(x)*ln(omz)*pow(NC,-1)*CF - 17*ln(x)*ln(omz)*pow(NC,-1)*z*CF\
      *pow(omx,-1) + 16*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF - 32*ln(x)*ln(omz)*pow(NC,-1)*x*CF\
       + 22*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + 2*ln(x)*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       - ln(x)*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x\
      )*ln(xmz)*pow(NC,-1)*CF + 2*ln(x)*ln(xmz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln(xmz)*pow(\
      NC,-1)*x*pow(z,-1)*CF + 2*ln(x)*ln(xmz)*pow(NC,-1)*x*CF - 2*ln(x)*ln(xmz)*pow(NC,-1)*x*z*CF\
       + 6*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 6*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(z)*\
      pow(NC,-1)*z*CF*pow(omx,-1)
                result +=  - 6*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(z)*pow(NC,-1)*x*CF - 6*ln(z)*pow(NC,-1)*x*\
      z*CF + 5*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*pow(ln(z),2)*pow(NC,-1)*pow(\
      z,-1)*CF - 9*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(ln(z),2)*pow(NC,-1)*CF + 9./2.*\
      pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF + 6*pow(\
      ln(z),2)*pow(NC,-1)*x*CF - 5*pow(ln(z),2)*pow(NC,-1)*x*z*CF + 8*ln(z)*ln(omx)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF - 12*ln(z)*ln(omx)*pow(NC,-1)*\
      CF*pow(omx,-1) + 4*ln(z)*ln(omx)*pow(NC,-1)*CF + 6*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1)\
       - 6*ln(z)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF + 12*ln(z)*ln(omx)*pow(NC,-1)*x*CF - 8*ln(z)*ln(\
      omx)*pow(NC,-1)*x*z*CF + 16*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 5*ln(z)*ln(\
      omz)*pow(NC,-1)*pow(z,-1)*CF - 26*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 10*ln(z)*ln(omz)*\
      pow(NC,-1)*CF + 13*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 11*ln(z)*ln(omz)*pow(NC,-1)*x*\
      pow(z,-1)*CF + 22*ln(z)*ln(omz)*pow(NC,-1)*x*CF - 16*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF - 2*ln(z\
      )*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + ln(z)*ln(xmz)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(\
      z)*ln(xmz)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(xmz)*pow(NC,-1)*CF - 2*ln(z)*ln(xmz)*pow(\
      NC,-1)*z*CF*pow(omx,-1) + ln(z)*ln(xmz)*pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(z)*ln(xmz)*pow(\
      NC,-1)*x*CF
                result +=  + 2*ln(z)*ln(xmz)*pow(NC,-1)*x*z*CF + 6*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       - 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*\
      pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(omx)*pow(NC,-1)*x*CF - 6*ln(omx)*pow(NC,-1)*x*z*CF + 5*pow(\
      ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 1./2.*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF\
       - 6*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) + pow(ln(omx),2)*pow(NC,-1)*CF + 3*pow(ln(omx),\
      2)*pow(NC,-1)*z*CF*pow(omx,-1) - 9./2.*pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1)*CF + 9*pow(ln(\
      omx),2)*pow(NC,-1)*x*CF - 5*pow(ln(omx),2)*pow(NC,-1)*x*z*CF + 12*ln(omx)*ln(omz)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) - 2*ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 16*ln(omx)*ln(omz)*\
      pow(NC,-1)*CF*pow(omx,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)*CF + 8*ln(omx)*ln(omz)*pow(NC,-1)*z*\
      CF*pow(omx,-1) - 10*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF + 20*ln(omx)*ln(omz)*pow(NC,-1)\
      *x*CF - 12*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF + 8*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       - 8*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(omz)*\
      pow(NC,-1)*x*pow(z,-1)*CF + 8*ln(omz)*pow(NC,-1)*x*CF - 8*ln(omz)*pow(NC,-1)*x*z*CF - 4*ln(\
      omz)*ln( - omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + ln(omz)*ln( - omxmz)*pow(NC,-1)*pow(\
      z,-1)*CF + 6*ln(omz)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*CF
                result +=  - 3*ln(omz)*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) + 3*ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*x*pow(z,-1)*CF - 6*ln(omz)*ln( - omxmz)*pow(NC,-1)*x*CF + 4*ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*x*z*CF + 8*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*pow(ln(omz),2)*pow(\
      NC,-1)*pow(z,-1)*CF - 12*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(ln(omz),2)*pow(\
      NC,-1)*CF + 6*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*pow(ln(omz),2)*pow(NC,-1)*x*pow(\
      z,-1)*CF + 12*pow(ln(omz),2)*pow(NC,-1)*x*CF - 8*pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 2*Li2(\
      pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*\
      omx*omz)*pow(NC,-1)*CF*pow(omx,-1) - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2(pow(x,-1)*pow(\
      z,-1)*omx*omz)*pow(NC,-1)*x*CF + 2*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x*z*CF + Li2(\
      pow(z,-1)*omx)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*CF*pow(omx,-1) - 2*\
      Li2(pow(z,-1)*omx)*pow(NC,-1)*CF - Li2(pow(z,-1)*omx)*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(pow(\
      z,-1)*omx)*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*x*CF - 2*Li2(omx*pow(\
      omz,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + Li2(omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*CF\
       + 4*Li2(omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) - 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*CF - \
      2*Li2(omx*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1)
                result +=  + Li2(omx*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1)*CF - 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*\
      x*CF + 2*Li2(omx*pow(omz,-1))*pow(NC,-1)*x*z*CF + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(\
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*CF - \
      4*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) + 2*Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*pow(NC,-1)*CF + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - \
      Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*pow(NC,-1)*x*CF - 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*x*z*CF + 2*Li2(z)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*Li2(z)*pow(NC,-1)*CF*pow(omx,-1) + Li2(z)*pow(NC,-1)*\
      z*CF*pow(omx,-1) - 2*Li2(z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*Li2(z)*pow(NC,-1)*x*CF - 2*Li2(z)*\
      pow(NC,-1)*x*z*CF
            if z < round(1 - x, ndecimals) and z > x:
                result += 4*pow(NC,-1)*pow(z,-1)*CF - 3*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) + 5./6.*pow(\
      NC,-1)*pow(z,-1)*pow(pi,2)*CF - 6*pow(NC,-1)*CF + 14./3.*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1)\
       - 5./3.*pow(NC,-1)*pow(pi,2)*CF + 4*pow(NC,-1)*z*CF*pow(omx,-1) - 7./3.*pow(NC,-1)*z*pow(\
      pi,2)*CF*pow(omx,-1) - 4*pow(NC,-1)*x*pow(z,-1)*CF + 13./6.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*\
      CF - 13./3.*pow(NC,-1)*x*pow(pi,2)*CF + 3*pow(NC,-1)*x*z*pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1) + 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1) - 12*ln(x)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 12*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF - 12*ln(x)*pow(NC,-1)*x*CF + 12*ln(x)*pow(NC,-1)\
      *x*z*CF + 2*ln(x)*ln( - xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(x)*ln( - xmz)*pow(\
      NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x)*ln( - xmz)*pow(\
      NC,-1)*CF + 2*ln(x)*ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln( - xmz)*pow(NC,-1)*x*\
      pow(z,-1)*CF + 2*ln(x)*ln( - xmz)*pow(NC,-1)*x*CF - 2*ln(x)*ln( - xmz)*pow(NC,-1)*x*z*CF + 14\
      *pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 7./2.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*\
      CF - 21*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) + 7*pow(ln(x),2)*pow(NC,-1)*CF + 21./2.*pow(\
      ln(x),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 21./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF + 21*\
      pow(ln(x),2)*pow(NC,-1)*x*CF - 14*pow(ln(x),2)*pow(NC,-1)*x*z*CF - 18*ln(x)*ln(z)*pow(NC,-1)*\
      pow(z,-1)*CF*pow(omx,-1)
                result +=  + 6*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF + 30*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) - \
      12*ln(x)*ln(z)*pow(NC,-1)*CF - 15*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) + 12*ln(x)*ln(z)*\
      pow(NC,-1)*x*pow(z,-1)*CF - 24*ln(x)*ln(z)*pow(NC,-1)*x*CF + 18*ln(x)*ln(z)*pow(NC,-1)*x*z*CF\
       - 18*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 3*ln(x)*ln(omx)*pow(NC,-1)*pow(\
      z,-1)*CF + 24*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) - 6*ln(x)*ln(omx)*pow(NC,-1)*CF - 12*\
      ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 15*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 30*\
      ln(x)*ln(omx)*pow(NC,-1)*x*CF + 18*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 24*ln(x)*ln(omz)*pow(\
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 6*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 36*ln(x)*ln(omz)*\
      pow(NC,-1)*CF*pow(omx,-1) - 12*ln(x)*ln(omz)*pow(NC,-1)*CF - 18*ln(x)*ln(omz)*pow(NC,-1)*z*CF\
      *pow(omx,-1) + 18*ln(x)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF - 36*ln(x)*ln(omz)*pow(NC,-1)*x*CF\
       + 24*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + 4*ln(x)*ln(omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)\
       - ln(x)*ln(omxmz)*pow(NC,-1)*pow(z,-1)*CF - 6*ln(x)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*\
      ln(x)*ln(omxmz)*pow(NC,-1)*CF + 3*ln(x)*ln(omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*ln(x)*ln(\
      omxmz)*pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(x)*ln(omxmz)*pow(NC,-1)*x*CF - 4*ln(x)*ln(omxmz)*pow(\
      NC,-1)*x*z*CF + 6*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 6*ln(z)*pow(NC,-1)*CF*pow(\
      omx,-1)
                result +=  + 6*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(z)*\
      pow(NC,-1)*x*CF - 6*ln(z)*pow(NC,-1)*x*z*CF - 2*ln(z)*ln( - xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) + ln(z)*ln( - xmz)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(\
      omx,-1) - 2*ln(z)*ln( - xmz)*pow(NC,-1)*CF - 2*ln(z)*ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + ln(z)*ln( - xmz)*pow(NC,-1)*x*pow(z,-1)*CF - 2*ln(z)*ln( - xmz)*pow(NC,-1)*x*CF + 2*ln(z)*\
      ln( - xmz)*pow(NC,-1)*x*z*CF + 6*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 5./2.*\
      pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF - 11*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) + 5*pow(ln(z\
      ),2)*pow(NC,-1)*CF + 11./2.*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 7./2.*pow(ln(z),2)*\
      pow(NC,-1)*x*pow(z,-1)*CF + 7*pow(ln(z),2)*pow(NC,-1)*x*CF - 6*pow(ln(z),2)*pow(NC,-1)*x*z*CF\
       + 6*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*\
      CF - 8*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(z)*ln(omx)*pow(NC,-1)*CF + 4*ln(z)*ln(\
      omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 5*ln(z)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF + 10*ln(z)*ln(\
      omx)*pow(NC,-1)*x*CF - 6*ln(z)*ln(omx)*pow(NC,-1)*x*z*CF + 14*ln(z)*ln(omz)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) - 5*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 24*ln(z)*ln(omz)*pow(NC,-1)*\
      CF*pow(omx,-1) + 10*ln(z)*ln(omz)*pow(NC,-1)*CF + 12*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(\
      omx,-1)
                result +=  - 9*ln(z)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF + 18*ln(z)*ln(omz)*pow(NC,-1)*x*CF - 14*\
      ln(z)*ln(omz)*pow(NC,-1)*x*z*CF + 6*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 6*ln(omx)*\
      pow(NC,-1)*CF*pow(omx,-1) + 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*pow(NC,-1)*x*\
      pow(z,-1)*CF + 6*ln(omx)*pow(NC,-1)*x*CF - 6*ln(omx)*pow(NC,-1)*x*z*CF + 7*pow(ln(omx),2)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 3./2.*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF - 10*pow(\
      ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) + 3*pow(ln(omx),2)*pow(NC,-1)*CF + 5*pow(ln(omx),2)*pow(\
      NC,-1)*z*CF*pow(omx,-1) - 11./2.*pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1)*CF + 11*pow(ln(omx),2)\
      *pow(NC,-1)*x*CF - 7*pow(ln(omx),2)*pow(NC,-1)*x*z*CF + 12*ln(omx)*ln(omz)*pow(NC,-1)*pow(\
      z,-1)*CF*pow(omx,-1) - ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 14*ln(omx)*ln(omz)*pow(\
      NC,-1)*CF*pow(omx,-1) + 2*ln(omx)*ln(omz)*pow(NC,-1)*CF + 7*ln(omx)*ln(omz)*pow(NC,-1)*z*CF*\
      pow(omx,-1) - 11*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF + 22*ln(omx)*ln(omz)*pow(NC,-1)*x*\
      CF - 12*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF + 8*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 8\
      *ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 8*ln(omz)*pow(\
      NC,-1)*x*pow(z,-1)*CF + 8*ln(omz)*pow(NC,-1)*x*CF - 8*ln(omz)*pow(NC,-1)*x*z*CF + 10*pow(ln(\
      omz),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 5./2.*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF - \
      15*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1)
                result +=  + 5*pow(ln(omz),2)*pow(NC,-1)*CF + 15./2.*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1)\
       - 15./2.*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1)*CF + 15*pow(ln(omz),2)*pow(NC,-1)*x*CF - 10*\
      pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 4*ln(omz)*ln(omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + \
      ln(omz)*ln(omxmz)*pow(NC,-1)*pow(z,-1)*CF + 6*ln(omz)*ln(omxmz)*pow(NC,-1)*CF*pow(omx,-1) - 2\
      *ln(omz)*ln(omxmz)*pow(NC,-1)*CF - 3*ln(omz)*ln(omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) + 3*ln(omz\
      )*ln(omxmz)*pow(NC,-1)*x*pow(z,-1)*CF - 6*ln(omz)*ln(omxmz)*pow(NC,-1)*x*CF + 4*ln(omz)*ln(\
      omxmz)*pow(NC,-1)*x*z*CF + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(\
      pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1)*CF - 4*Li2(pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1)\
       + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*CF + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1)\
       - Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*CF - \
      2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*z*CF - Li2(z*pow(omx,-1))*pow(NC,-1)*pow(z,-1)*CF - 2*\
      Li2(z*pow(omx,-1))*pow(NC,-1)*CF*pow(omx,-1) + 2*Li2(z*pow(omx,-1))*pow(NC,-1)*CF + Li2(z*\
      pow(omx,-1))*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(z*pow(omx,-1))*pow(NC,-1)*x*pow(z,-1)*CF - 2*\
      Li2(z*pow(omx,-1))*pow(NC,-1)*x*CF + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*\
      CF*pow(omx,-1) - Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*CF - 4*Li2(x*pow(z,-1)\
      *omx*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1)
                result +=  + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*CF + 2*Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*x*pow(\
      z,-1)*CF + 2*Li2(x*pow(z,-1)*omx*pow(omz,-1))*pow(NC,-1)*x*CF - 2*Li2(x*pow(z,-1)*omx*pow(\
      omz,-1))*pow(NC,-1)*x*z*CF + 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(\
      omx,-1) - 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*CF*pow(omx,-1) + Li2(x*z*pow(omx,-1)*\
      pow(omz,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x*\
      pow(z,-1)*CF + 4*Li2(x*z*pow(omx,-1)*pow(omz,-1))*pow(NC,-1)*x*CF - 2*Li2(x*z*pow(omx,-1)*\
      pow(omz,-1))*pow(NC,-1)*x*z*CF + 2*Li2(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*Li2(z)*pow(\
      NC,-1)*CF*pow(omx,-1) + Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(z)*pow(NC,-1)*x*pow(z,-1)*\
      CF + 4*Li2(z)*pow(NC,-1)*x*CF - 2*Li2(z)*pow(NC,-1)*x*z*CF
            if z > round(1 - x, ndecimals) and z > x:
                result += 4*pow(NC,-1)*pow(z,-1)*CF - 5./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) + 1./6.*\
      pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF - 6*pow(NC,-1)*CF + 2*pow(NC,-1)*pow(pi,2)*CF*pow(omx,-1)\
       - 1./3.*pow(NC,-1)*pow(pi,2)*CF + 4*pow(NC,-1)*z*CF*pow(omx,-1) - pow(NC,-1)*z*pow(pi,2)*CF*\
      pow(omx,-1) - 4*pow(NC,-1)*x*pow(z,-1)*CF + 3./2.*pow(NC,-1)*x*pow(z,-1)*pow(pi,2)*CF - 3*\
      pow(NC,-1)*x*pow(pi,2)*CF + 5./3.*pow(NC,-1)*x*z*pow(pi,2)*CF - 12*ln(x)*pow(NC,-1)*pow(z,-1)\
      *CF*pow(omx,-1) + 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1) - 12*ln(x)*pow(NC,-1)*z*CF*pow(omx,-1)\
       + 12*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF - 12*ln(x)*pow(NC,-1)*x*CF + 12*ln(x)*pow(NC,-1)*x*z*CF\
       + 4*ln(x)*ln( - omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(x)*ln( - omxmz)*pow(NC,-1)*\
      pow(z,-1)*CF - 6*ln(x)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x)*ln( - omxmz)*pow(\
      NC,-1)*CF + 3*ln(x)*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) - 3*ln(x)*ln( - omxmz)*pow(\
      NC,-1)*x*pow(z,-1)*CF + 6*ln(x)*ln( - omxmz)*pow(NC,-1)*x*CF - 4*ln(x)*ln( - omxmz)*pow(\
      NC,-1)*x*z*CF + 2*ln(x)*ln( - xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(x)*ln( - xmz)*\
      pow(NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1) + 2*ln(x)*ln( - xmz)*\
      pow(NC,-1)*CF + 2*ln(x)*ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln( - xmz)*pow(NC,-1)*\
      x*pow(z,-1)*CF + 2*ln(x)*ln( - xmz)*pow(NC,-1)*x*CF - 2*ln(x)*ln( - xmz)*pow(NC,-1)*x*z*CF + \
      12*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)
                result +=  - 3*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF - 18*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1)\
       + 6*pow(ln(x),2)*pow(NC,-1)*CF + 9*pow(ln(x),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 9*pow(ln(x),2)\
      *pow(NC,-1)*x*pow(z,-1)*CF + 18*pow(ln(x),2)*pow(NC,-1)*x*CF - 12*pow(ln(x),2)*pow(NC,-1)*x*z\
      *CF - 18*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 5*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)\
      *CF + 28*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) - 10*ln(x)*ln(z)*pow(NC,-1)*CF - 14*ln(x)*ln(z\
      )*pow(NC,-1)*z*CF*pow(omx,-1) + 13*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF - 26*ln(x)*ln(z)*\
      pow(NC,-1)*x*CF + 18*ln(x)*ln(z)*pow(NC,-1)*x*z*CF - 18*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF\
      *pow(omx,-1) + 4*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF + 26*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(\
      omx,-1) - 8*ln(x)*ln(omx)*pow(NC,-1)*CF - 13*ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 14*\
      ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 28*ln(x)*ln(omx)*pow(NC,-1)*x*CF + 18*ln(x)*ln(omx)\
      *pow(NC,-1)*x*z*CF - 20*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 5*ln(x)*ln(omz)*\
      pow(NC,-1)*pow(z,-1)*CF + 30*ln(x)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 10*ln(x)*ln(omz)*pow(\
      NC,-1)*CF - 15*ln(x)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + 15*ln(x)*ln(omz)*pow(NC,-1)*x*pow(\
      z,-1)*CF - 30*ln(x)*ln(omz)*pow(NC,-1)*x*CF + 20*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF + 6*ln(z)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 6*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(z)*pow(NC,-1)*\
      z*CF*pow(omx,-1)
                result +=  - 6*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(z)*pow(NC,-1)*x*CF - 6*ln(z)*pow(NC,-1)*x*\
      z*CF - 2*ln(z)*ln( - xmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + ln(z)*ln( - xmz)*pow(NC,-1)*\
      pow(z,-1)*CF + 4*ln(z)*ln( - xmz)*pow(NC,-1)*CF*pow(omx,-1) - 2*ln(z)*ln( - xmz)*pow(NC,-1)*\
      CF - 2*ln(z)*ln( - xmz)*pow(NC,-1)*z*CF*pow(omx,-1) + ln(z)*ln( - xmz)*pow(NC,-1)*x*pow(z,-1)\
      *CF - 2*ln(z)*ln( - xmz)*pow(NC,-1)*x*CF + 2*ln(z)*ln( - xmz)*pow(NC,-1)*x*z*CF + 4*pow(ln(z)\
      ,2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 3./2.*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF - 7*pow(\
      ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) + 3*pow(ln(z),2)*pow(NC,-1)*CF + 7./2.*pow(ln(z),2)*pow(\
      NC,-1)*z*CF*pow(omx,-1) - 5./2.*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF + 5*pow(ln(z),2)*pow(\
      NC,-1)*x*CF - 4*pow(ln(z),2)*pow(NC,-1)*x*z*CF + 10*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*\
      pow(omx,-1) - 3*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF - 16*ln(z)*ln(omx)*pow(NC,-1)*CF*pow(\
      omx,-1) + 6*ln(z)*ln(omx)*pow(NC,-1)*CF + 8*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - 7*ln(\
      z)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF + 14*ln(z)*ln(omx)*pow(NC,-1)*x*CF - 10*ln(z)*ln(omx)*\
      pow(NC,-1)*x*z*CF + 14*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 4*ln(z)*ln(omz)*\
      pow(NC,-1)*pow(z,-1)*CF - 22*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(z)*ln(omz)*pow(\
      NC,-1)*CF + 11*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 10*ln(z)*ln(omz)*pow(NC,-1)*x*pow(\
      z,-1)*CF
                result +=  + 20*ln(z)*ln(omz)*pow(NC,-1)*x*CF - 14*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF + 6*ln(omx)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 6*ln(omx)*pow(\
      NC,-1)*z*CF*pow(omx,-1) - 6*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF + 6*ln(omx)*pow(NC,-1)*x*CF - 6\
      *ln(omx)*pow(NC,-1)*x*z*CF + 5*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 1./2.*\
      pow(ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF - 6*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) + pow(ln(\
      omx),2)*pow(NC,-1)*CF + 3*pow(ln(omx),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 9./2.*pow(ln(omx),2)*\
      pow(NC,-1)*x*pow(z,-1)*CF + 9*pow(ln(omx),2)*pow(NC,-1)*x*CF - 5*pow(ln(omx),2)*pow(NC,-1)*x*\
      z*CF + 12*ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*ln(omx)*ln(omz)*pow(NC,-1)*\
      pow(z,-1)*CF - 16*ln(omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 4*ln(omx)*ln(omz)*pow(NC,-1)*CF\
       + 8*ln(omx)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) - 10*ln(omx)*ln(omz)*pow(NC,-1)*x*pow(z,-1)*\
      CF + 20*ln(omx)*ln(omz)*pow(NC,-1)*x*CF - 12*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF + 8*ln(omz)*\
      pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 8*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) + 8*ln(omz)*pow(\
      NC,-1)*z*CF*pow(omx,-1) - 8*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF + 8*ln(omz)*pow(NC,-1)*x*CF - 8\
      *ln(omz)*pow(NC,-1)*x*z*CF - 4*ln(omz)*ln( - omxmz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + ln(\
      omz)*ln( - omxmz)*pow(NC,-1)*pow(z,-1)*CF + 6*ln(omz)*ln( - omxmz)*pow(NC,-1)*CF*pow(omx,-1)\
       - 2*ln(omz)*ln( - omxmz)*pow(NC,-1)*CF
                result +=  - 3*ln(omz)*ln( - omxmz)*pow(NC,-1)*z*CF*pow(omx,-1) + 3*ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*x*pow(z,-1)*CF - 6*ln(omz)*ln( - omxmz)*pow(NC,-1)*x*CF + 4*ln(omz)*ln( - omxmz)*pow(\
      NC,-1)*x*z*CF + 8*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*pow(ln(omz),2)*pow(\
      NC,-1)*pow(z,-1)*CF - 12*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) + 4*pow(ln(omz),2)*pow(\
      NC,-1)*CF + 6*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 6*pow(ln(omz),2)*pow(NC,-1)*x*pow(\
      z,-1)*CF + 12*pow(ln(omz),2)*pow(NC,-1)*x*CF - 8*pow(ln(omz),2)*pow(NC,-1)*x*z*CF - 2*Li2(\
      pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*\
      omx*omz)*pow(NC,-1)*CF*pow(omx,-1) - Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*z*CF*pow(\
      omx,-1) + 2*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2(pow(x,-1)*pow(\
      z,-1)*omx*omz)*pow(NC,-1)*x*CF + 2*Li2(pow(x,-1)*pow(z,-1)*omx*omz)*pow(NC,-1)*x*z*CF - 2*\
      Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + Li2(pow(x,-1)*z*pow(\
      omx,-1)*omz)*pow(NC,-1)*pow(z,-1)*CF + 4*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(\
      omx,-1) - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*CF - 2*Li2(pow(x,-1)*z*pow(omx,-1)*\
      omz)*pow(NC,-1)*z*CF*pow(omx,-1) + Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*x*pow(z,-1)*CF\
       - 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*pow(NC,-1)*x*CF + 2*Li2(pow(x,-1)*z*pow(omx,-1)*omz)*\
      pow(NC,-1)*x*z*CF
                result +=  + Li2(pow(z,-1)*omx)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*CF*\
      pow(omx,-1) - 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*CF - Li2(pow(z,-1)*omx)*pow(NC,-1)*z*CF*pow(\
      omx,-1) - Li2(pow(z,-1)*omx)*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(pow(z,-1)*omx)*pow(NC,-1)*x*CF\
       + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(pow(omx,-1)*omz)*pow(\
      NC,-1)*pow(z,-1)*CF - 4*Li2(pow(omx,-1)*omz)*pow(NC,-1)*CF*pow(omx,-1) + 2*Li2(pow(omx,-1)*\
      omz)*pow(NC,-1)*CF + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(pow(omx,-1)*omz\
      )*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(pow(omx,-1)*omz)*pow(NC,-1)*x*CF - 2*Li2(pow(omx,-1)*omz)\
      *pow(NC,-1)*x*z*CF + 2*Li2(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*Li2(z)*pow(NC,-1)*CF*\
      pow(omx,-1) + Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*\
      Li2(z)*pow(NC,-1)*x*CF - 2*Li2(z)*pow(NC,-1)*x*z*CF
            if z > x:
                result += - NC*pow(z,-1)*CF + NC*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) - 1./2.*NC*pow(z,-1)*pow(pi,2)\
      *CF + 3*NC*CF - NC*pow(pi,2)*CF*pow(omx,-1) + NC*pow(pi,2)*CF - NC*z*CF*pow(omx,-1) + 1./2.*\
      NC*z*pow(pi,2)*CF*pow(omx,-1) + NC*x*pow(z,-1)*CF - 1./2.*NC*x*pow(z,-1)*pow(pi,2)*CF + NC*x*\
      pow(pi,2)*CF - NC*x*z*pow(pi,2)*CF + 6*ln(x)*NC*pow(z,-1)*CF*pow(omx,-1) - 6*ln(x)*NC*CF*pow(\
      omx,-1) + 9*ln(x)*NC*CF + 6*ln(x)*NC*z*CF*pow(omx,-1) - 6*ln(x)*NC*x*pow(z,-1)*CF - 6*ln(x)*\
      NC*x*z*CF - 2*ln(x)*ln( - xmz)*NC*pow(z,-1)*CF*pow(omx,-1) + ln(x)*ln( - xmz)*NC*pow(z,-1)*CF\
       + 2*ln(x)*ln( - xmz)*NC*CF*pow(omx,-1) - 2*ln(x)*ln( - xmz)*NC*CF - ln(x)*ln( - xmz)*NC*z*CF\
      *pow(omx,-1) + ln(x)*ln( - xmz)*NC*x*pow(z,-1)*CF - 2*ln(x)*ln( - xmz)*NC*x*CF + 2*ln(x)*ln(\
       - xmz)*NC*x*z*CF - 7*pow(ln(x),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 7./2.*pow(ln(x),2)*NC*pow(\
      z,-1)*CF + 7*pow(ln(x),2)*NC*CF*pow(omx,-1) - 7*pow(ln(x),2)*NC*CF - 7./2.*pow(ln(x),2)*NC*z*\
      CF*pow(omx,-1) + 7./2.*pow(ln(x),2)*NC*x*pow(z,-1)*CF - 7*pow(ln(x),2)*NC*x*CF + 7*pow(ln(x),\
      2)*NC*x*z*CF + 12*ln(x)*ln(z)*NC*pow(z,-1)*CF*pow(omx,-1) - 6*ln(x)*ln(z)*NC*pow(z,-1)*CF - \
      12*ln(x)*ln(z)*NC*CF*pow(omx,-1) + 12*ln(x)*ln(z)*NC*CF + 6*ln(x)*ln(z)*NC*z*CF*pow(omx,-1)\
       - 6*ln(x)*ln(z)*NC*x*pow(z,-1)*CF + 12*ln(x)*ln(z)*NC*x*CF - 12*ln(x)*ln(z)*NC*x*z*CF + 12*\
      ln(x)*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) - 6*ln(x)*ln(omx)*NC*pow(z,-1)*CF - 12*ln(x)*ln(omx\
      )*NC*CF*pow(omx,-1)
                result +=  + 12*ln(x)*ln(omx)*NC*CF + 6*ln(x)*ln(omx)*NC*z*CF*pow(omx,-1) - 6*ln(x)*ln(omx)*NC*x\
      *pow(z,-1)*CF + 12*ln(x)*ln(omx)*NC*x*CF - 12*ln(x)*ln(omx)*NC*x*z*CF + 6*ln(x)*ln(omz)*NC*\
      pow(z,-1)*CF*pow(omx,-1) - 3*ln(x)*ln(omz)*NC*pow(z,-1)*CF - 6*ln(x)*ln(omz)*NC*CF*pow(\
      omx,-1) + 6*ln(x)*ln(omz)*NC*CF + 3*ln(x)*ln(omz)*NC*z*CF*pow(omx,-1) - 3*ln(x)*ln(omz)*NC*x*\
      pow(z,-1)*CF + 6*ln(x)*ln(omz)*NC*x*CF - 6*ln(x)*ln(omz)*NC*x*z*CF - 4*ln(z)*NC*pow(z,-1)*CF*\
      pow(omx,-1) + 4*ln(z)*NC*CF*pow(omx,-1) - 6*ln(z)*NC*CF - 4*ln(z)*NC*z*CF*pow(omx,-1) + 4*ln(\
      z)*NC*x*pow(z,-1)*CF + 4*ln(z)*NC*x*z*CF + 2*ln(z)*ln( - xmz)*NC*pow(z,-1)*CF*pow(omx,-1) - \
      ln(z)*ln( - xmz)*NC*pow(z,-1)*CF - 2*ln(z)*ln( - xmz)*NC*CF*pow(omx,-1) + 2*ln(z)*ln( - xmz)*\
      NC*CF + ln(z)*ln( - xmz)*NC*z*CF*pow(omx,-1) - ln(z)*ln( - xmz)*NC*x*pow(z,-1)*CF + 2*ln(z)*\
      ln( - xmz)*NC*x*CF - 2*ln(z)*ln( - xmz)*NC*x*z*CF - 5*pow(ln(z),2)*NC*pow(z,-1)*CF*pow(\
      omx,-1) + 5./2.*pow(ln(z),2)*NC*pow(z,-1)*CF + 5*pow(ln(z),2)*NC*CF*pow(omx,-1) - 5*pow(ln(z)\
      ,2)*NC*CF - 5./2.*pow(ln(z),2)*NC*z*CF*pow(omx,-1) + 5./2.*pow(ln(z),2)*NC*x*pow(z,-1)*CF - 5\
      *pow(ln(z),2)*NC*x*CF + 5*pow(ln(z),2)*NC*x*z*CF - 10*ln(z)*ln(omx)*NC*pow(z,-1)*CF*pow(\
      omx,-1) + 5*ln(z)*ln(omx)*NC*pow(z,-1)*CF + 10*ln(z)*ln(omx)*NC*CF*pow(omx,-1) - 10*ln(z)*ln(\
      omx)*NC*CF - 5*ln(z)*ln(omx)*NC*z*CF*pow(omx,-1) + 5*ln(z)*ln(omx)*NC*x*pow(z,-1)*CF - 10*ln(\
      z)*ln(omx)*NC*x*CF
                result +=  + 10*ln(z)*ln(omx)*NC*x*z*CF - 2*ln(z)*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + ln(z)*\
      ln(omz)*NC*pow(z,-1)*CF + 2*ln(z)*ln(omz)*NC*CF*pow(omx,-1) - 2*ln(z)*ln(omz)*NC*CF - ln(z)*\
      ln(omz)*NC*z*CF*pow(omx,-1) + ln(z)*ln(omz)*NC*x*pow(z,-1)*CF - 2*ln(z)*ln(omz)*NC*x*CF + 2*\
      ln(z)*ln(omz)*NC*x*z*CF - 4*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) + 4*ln(omx)*NC*CF*pow(omx,-1)\
       - 6*ln(omx)*NC*CF - 4*ln(omx)*NC*z*CF*pow(omx,-1) + 4*ln(omx)*NC*x*pow(z,-1)*CF + 4*ln(omx)*\
      NC*x*z*CF - 4*pow(ln(omx),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*pow(ln(omx),2)*NC*pow(z,-1)*CF\
       + 4*pow(ln(omx),2)*NC*CF*pow(omx,-1) - 4*pow(ln(omx),2)*NC*CF - 2*pow(ln(omx),2)*NC*z*CF*\
      pow(omx,-1) + 2*pow(ln(omx),2)*NC*x*pow(z,-1)*CF - 4*pow(ln(omx),2)*NC*x*CF + 4*pow(ln(omx),2\
      )*NC*x*z*CF - 4*ln(omx)*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*ln(omx)*ln(omz)*NC*pow(z,-1)*\
      CF + 4*ln(omx)*ln(omz)*NC*CF*pow(omx,-1) - 4*ln(omx)*ln(omz)*NC*CF - 2*ln(omx)*ln(omz)*NC*z*\
      CF*pow(omx,-1) + 2*ln(omx)*ln(omz)*NC*x*pow(z,-1)*CF - 4*ln(omx)*ln(omz)*NC*x*CF + 4*ln(omx)*\
      ln(omz)*NC*x*z*CF - 2*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*ln(omz)*NC*CF*pow(omx,-1) - 3*\
      ln(omz)*NC*CF - 2*ln(omz)*NC*z*CF*pow(omx,-1) + 2*ln(omz)*NC*x*pow(z,-1)*CF + 2*ln(omz)*NC*x*\
      z*CF - pow(ln(omz),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 1./2.*pow(ln(omz),2)*NC*pow(z,-1)*CF + \
      pow(ln(omz),2)*NC*CF*pow(omx,-1) - pow(ln(omz),2)*NC*CF - 1./2.*pow(ln(omz),2)*NC*z*CF*pow(\
      omx,-1)
                result +=  + 1./2.*pow(ln(omz),2)*NC*x*pow(z,-1)*CF - pow(ln(omz),2)*NC*x*CF + pow(ln(omz),2)*NC\
      *x*z*CF + 2*Li2(pow(omx,-1)*omz)*NC*pow(z,-1)*CF*pow(omx,-1) - Li2(pow(omx,-1)*omz)*NC*pow(\
      z,-1)*CF - 2*Li2(pow(omx,-1)*omz)*NC*CF*pow(omx,-1) + 2*Li2(pow(omx,-1)*omz)*NC*CF + Li2(pow(\
      omx,-1)*omz)*NC*z*CF*pow(omx,-1) - Li2(pow(omx,-1)*omz)*NC*x*pow(z,-1)*CF + 2*Li2(pow(omx,-1)\
      *omz)*NC*x*CF - 2*Li2(pow(omx,-1)*omz)*NC*x*z*CF - 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*NC*pow(\
      z,-1)*CF*pow(omx,-1) + Li2(x*pow(z,-1)*pow(omx,-1)*omz)*NC*pow(z,-1)*CF + 2*Li2(x*pow(z,-1)*\
      pow(omx,-1)*omz)*NC*CF*pow(omx,-1) - 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*NC*CF - Li2(x*pow(\
      z,-1)*pow(omx,-1)*omz)*NC*z*CF*pow(omx,-1) + Li2(x*pow(z,-1)*pow(omx,-1)*omz)*NC*x*pow(z,-1)*\
      CF - 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*NC*x*CF + 2*Li2(x*pow(z,-1)*pow(omx,-1)*omz)*NC*x*z*\
      CF + 2*Li2(z)*NC*pow(z,-1)*CF*pow(omx,-1) - Li2(z)*NC*pow(z,-1)*CF - 2*Li2(z)*NC*CF*pow(\
      omx,-1) + 2*Li2(z)*NC*CF + Li2(z)*NC*z*CF*pow(omx,-1) - Li2(z)*NC*x*pow(z,-1)*CF + 2*Li2(z)*\
      NC*x*CF - 2*Li2(z)*NC*x*z*CF
            if z < x:
                result += - NC*pow(z,-1)*CF + NC*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) - 1./2.*NC*pow(z,-1)*pow(pi,2)\
      *CF + 3*NC*CF - NC*pow(pi,2)*CF*pow(omx,-1) + NC*pow(pi,2)*CF - NC*z*CF*pow(omx,-1) + 1./2.*\
      NC*z*pow(pi,2)*CF*pow(omx,-1) + NC*x*pow(z,-1)*CF - 1./2.*NC*x*pow(z,-1)*pow(pi,2)*CF + NC*x*\
      pow(pi,2)*CF - NC*x*z*pow(pi,2)*CF + 6*ln(x)*NC*pow(z,-1)*CF*pow(omx,-1) - 6*ln(x)*NC*CF*pow(\
      omx,-1) + 9*ln(x)*NC*CF + 6*ln(x)*NC*z*CF*pow(omx,-1) - 6*ln(x)*NC*x*pow(z,-1)*CF - 6*ln(x)*\
      NC*x*z*CF - 6*pow(ln(x),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 3*pow(ln(x),2)*NC*pow(z,-1)*CF + 6*\
      pow(ln(x),2)*NC*CF*pow(omx,-1) - 6*pow(ln(x),2)*NC*CF - 3*pow(ln(x),2)*NC*z*CF*pow(omx,-1) + \
      3*pow(ln(x),2)*NC*x*pow(z,-1)*CF - 6*pow(ln(x),2)*NC*x*CF + 6*pow(ln(x),2)*NC*x*z*CF + 10*ln(\
      x)*ln(z)*NC*pow(z,-1)*CF*pow(omx,-1) - 5*ln(x)*ln(z)*NC*pow(z,-1)*CF - 10*ln(x)*ln(z)*NC*CF*\
      pow(omx,-1) + 10*ln(x)*ln(z)*NC*CF + 5*ln(x)*ln(z)*NC*z*CF*pow(omx,-1) - 5*ln(x)*ln(z)*NC*x*\
      pow(z,-1)*CF + 10*ln(x)*ln(z)*NC*x*CF - 10*ln(x)*ln(z)*NC*x*z*CF + 10*ln(x)*ln(omx)*NC*pow(\
      z,-1)*CF*pow(omx,-1) - 5*ln(x)*ln(omx)*NC*pow(z,-1)*CF - 10*ln(x)*ln(omx)*NC*CF*pow(omx,-1)\
       + 10*ln(x)*ln(omx)*NC*CF + 5*ln(x)*ln(omx)*NC*z*CF*pow(omx,-1) - 5*ln(x)*ln(omx)*NC*x*pow(\
      z,-1)*CF + 10*ln(x)*ln(omx)*NC*x*CF - 10*ln(x)*ln(omx)*NC*x*z*CF + 8*ln(x)*ln(omz)*NC*pow(\
      z,-1)*CF*pow(omx,-1) - 4*ln(x)*ln(omz)*NC*pow(z,-1)*CF - 8*ln(x)*ln(omz)*NC*CF*pow(omx,-1) + \
      8*ln(x)*ln(omz)*NC*CF
                result +=  + 4*ln(x)*ln(omz)*NC*z*CF*pow(omx,-1) - 4*ln(x)*ln(omz)*NC*x*pow(z,-1)*CF + 8*ln(x)*\
      ln(omz)*NC*x*CF - 8*ln(x)*ln(omz)*NC*x*z*CF - 2*ln(x)*ln(xmz)*NC*pow(z,-1)*CF*pow(omx,-1) + \
      ln(x)*ln(xmz)*NC*pow(z,-1)*CF + 2*ln(x)*ln(xmz)*NC*CF*pow(omx,-1) - 2*ln(x)*ln(xmz)*NC*CF - \
      ln(x)*ln(xmz)*NC*z*CF*pow(omx,-1) + ln(x)*ln(xmz)*NC*x*pow(z,-1)*CF - 2*ln(x)*ln(xmz)*NC*x*CF\
       + 2*ln(x)*ln(xmz)*NC*x*z*CF - 4*ln(z)*NC*pow(z,-1)*CF*pow(omx,-1) + 4*ln(z)*NC*CF*pow(\
      omx,-1) - 6*ln(z)*NC*CF - 4*ln(z)*NC*z*CF*pow(omx,-1) + 4*ln(z)*NC*x*pow(z,-1)*CF + 4*ln(z)*\
      NC*x*z*CF - 4*pow(ln(z),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*pow(ln(z),2)*NC*pow(z,-1)*CF + 4*\
      pow(ln(z),2)*NC*CF*pow(omx,-1) - 4*pow(ln(z),2)*NC*CF - 2*pow(ln(z),2)*NC*z*CF*pow(omx,-1) + \
      2*pow(ln(z),2)*NC*x*pow(z,-1)*CF - 4*pow(ln(z),2)*NC*x*CF + 4*pow(ln(z),2)*NC*x*z*CF - 8*ln(z\
      )*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) + 4*ln(z)*ln(omx)*NC*pow(z,-1)*CF + 8*ln(z)*ln(omx)*NC*\
      CF*pow(omx,-1) - 8*ln(z)*ln(omx)*NC*CF - 4*ln(z)*ln(omx)*NC*z*CF*pow(omx,-1) + 4*ln(z)*ln(omx\
      )*NC*x*pow(z,-1)*CF - 8*ln(z)*ln(omx)*NC*x*CF + 8*ln(z)*ln(omx)*NC*x*z*CF - 4*ln(z)*ln(omz)*\
      NC*pow(z,-1)*CF*pow(omx,-1) + 2*ln(z)*ln(omz)*NC*pow(z,-1)*CF + 4*ln(z)*ln(omz)*NC*CF*pow(\
      omx,-1) - 4*ln(z)*ln(omz)*NC*CF - 2*ln(z)*ln(omz)*NC*z*CF*pow(omx,-1) + 2*ln(z)*ln(omz)*NC*x*\
      pow(z,-1)*CF - 4*ln(z)*ln(omz)*NC*x*CF + 4*ln(z)*ln(omz)*NC*x*z*CF + 2*ln(z)*ln(xmz)*NC*pow(\
      z,-1)*CF*pow(omx,-1)
                result +=  - ln(z)*ln(xmz)*NC*pow(z,-1)*CF - 2*ln(z)*ln(xmz)*NC*CF*pow(omx,-1) + 2*ln(z)*ln(xmz)\
      *NC*CF + ln(z)*ln(xmz)*NC*z*CF*pow(omx,-1) - ln(z)*ln(xmz)*NC*x*pow(z,-1)*CF + 2*ln(z)*ln(xmz\
      )*NC*x*CF - 2*ln(z)*ln(xmz)*NC*x*z*CF - 4*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) + 4*ln(omx)*NC*\
      CF*pow(omx,-1) - 6*ln(omx)*NC*CF - 4*ln(omx)*NC*z*CF*pow(omx,-1) + 4*ln(omx)*NC*x*pow(z,-1)*\
      CF + 4*ln(omx)*NC*x*z*CF - 4*pow(ln(omx),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*pow(ln(omx),2)*NC\
      *pow(z,-1)*CF + 4*pow(ln(omx),2)*NC*CF*pow(omx,-1) - 4*pow(ln(omx),2)*NC*CF - 2*pow(ln(omx),2\
      )*NC*z*CF*pow(omx,-1) + 2*pow(ln(omx),2)*NC*x*pow(z,-1)*CF - 4*pow(ln(omx),2)*NC*x*CF + 4*\
      pow(ln(omx),2)*NC*x*z*CF - 4*ln(omx)*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*ln(omx)*ln(omz)*\
      NC*pow(z,-1)*CF + 4*ln(omx)*ln(omz)*NC*CF*pow(omx,-1) - 4*ln(omx)*ln(omz)*NC*CF - 2*ln(omx)*\
      ln(omz)*NC*z*CF*pow(omx,-1) + 2*ln(omx)*ln(omz)*NC*x*pow(z,-1)*CF - 4*ln(omx)*ln(omz)*NC*x*CF\
       + 4*ln(omx)*ln(omz)*NC*x*z*CF - 2*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*ln(omz)*NC*CF*pow(\
      omx,-1) - 3*ln(omz)*NC*CF - 2*ln(omz)*NC*z*CF*pow(omx,-1) + 2*ln(omz)*NC*x*pow(z,-1)*CF + 2*\
      ln(omz)*NC*x*z*CF - pow(ln(omz),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 1./2.*pow(ln(omz),2)*NC*pow(\
      z,-1)*CF + pow(ln(omz),2)*NC*CF*pow(omx,-1) - pow(ln(omz),2)*NC*CF - 1./2.*pow(ln(omz),2)*NC*\
      z*CF*pow(omx,-1) + 1./2.*pow(ln(omz),2)*NC*x*pow(z,-1)*CF - pow(ln(omz),2)*NC*x*CF + pow(ln(\
      omz),2)*NC*x*z*CF
                result +=  + 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*NC*pow(z,-1)*CF*pow(omx,-1) - Li2(pow(x,-1)*z*\
      omx*pow(omz,-1))*NC*pow(z,-1)*CF - 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*NC*CF*pow(omx,-1) + 2*\
      Li2(pow(x,-1)*z*omx*pow(omz,-1))*NC*CF + Li2(pow(x,-1)*z*omx*pow(omz,-1))*NC*z*CF*pow(omx,-1)\
       - Li2(pow(x,-1)*z*omx*pow(omz,-1))*NC*x*pow(z,-1)*CF + 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*NC\
      *x*CF - 2*Li2(pow(x,-1)*z*omx*pow(omz,-1))*NC*x*z*CF - 2*Li2(omx*pow(omz,-1))*NC*pow(z,-1)*CF\
      *pow(omx,-1) + Li2(omx*pow(omz,-1))*NC*pow(z,-1)*CF + 2*Li2(omx*pow(omz,-1))*NC*CF*pow(\
      omx,-1) - 2*Li2(omx*pow(omz,-1))*NC*CF - Li2(omx*pow(omz,-1))*NC*z*CF*pow(omx,-1) + Li2(omx*\
      pow(omz,-1))*NC*x*pow(z,-1)*CF - 2*Li2(omx*pow(omz,-1))*NC*x*CF + 2*Li2(omx*pow(omz,-1))*NC*x\
      *z*CF + 2*Li2(z)*NC*pow(z,-1)*CF*pow(omx,-1) - Li2(z)*NC*pow(z,-1)*CF - 2*Li2(z)*NC*CF*pow(\
      omx,-1) + 2*Li2(z)*NC*CF + Li2(z)*NC*z*CF*pow(omx,-1) - Li2(z)*NC*x*pow(z,-1)*CF + 2*Li2(z)*\
      NC*x*CF - 2*Li2(z)*NC*x*z*CF
        elif orders == '001':
            if z != x and z != round(1 - x, ndecimals):
                result += - ln(omz)*LMUA*pow(NC,-1)*pow(z,-1)*CF + ln(omz)*LMUA*pow(NC,-1)*CF - 1./2.*ln(omz)*LMUA*pow(NC,-1)*z\
                          *CF - ln(omz)*LMUA*pow(NC,-1)*x*pow(z,-1)*CF + ln(omz)*LMUA*pow(NC,-1)*x*CF - 1./2.*ln(omz)*\
                          LMUA*pow(NC,-1)*x*z*CF + 3*ln(omz)*LMUA*NC*pow(z,-1)*CF - 5*ln(omz)*LMUA*NC*CF + 1./2.*ln(omz\
                          )*LMUA*NC*z*CF + 3*ln(omz)*LMUA*NC*x*pow(z,-1)*CF - 5*ln(omz)*LMUA*NC*x*CF + 9./2.*ln(omz)*\
                          LMUA*NC*x*z*CF - ln(omx)*LMUA*pow(NC,-1)*x*pow(z,-1)*CF + ln(omx)*LMUA*pow(NC,-1)*x*CF - 1./2.*ln(\
                          omx)*LMUA*pow(NC,-1)*x*z*CF + ln(omx)*LMUA*NC*pow(z,-1)*CF - ln(omx)*LMUA*NC*CF + 1./2.*ln(\
                          omx)*LMUA*NC*z*CF + ln(omx)*LMUA*NC*x*pow(z,-1)*CF - ln(omx)*LMUA*NC*x*CF + 1./2.*ln(omx)*\
                          LMUA*NC*x*z*CF - 2*ln(x)*LMUA*NC*CF*pow(omx,-1) + ln(x)*LMUA*NC*CF + ln(x)*LMUA*NC*z*CF*pow(omx,-1)\
                           - 1./2.*ln(x)*LMUA*NC*z*CF - ln(x)*LMUA*NC*x*pow(z,-1)*CF + ln(x)*LMUA*NC*x*CF - 1./2.*ln(x)\
                          *LMUA*NC*x*z*CF - 2*ln(x)*LMUA*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + ln(x)*LMUA*pow(NC,-1)*pow(z,-1)*CF + 2*ln(x)*LMUA*pow(NC,-1)*CF*\
                          pow(omx,-1) - ln(x)*LMUA*pow(NC,-1)*CF - ln(x)*LMUA*pow(NC,-1)*z*CF*pow(omx,-1) + 1./2.*ln(x)\
                          *LMUA*pow(NC,-1)*z*CF + ln(x)*LMUA*pow(NC,-1)*x*pow(z,-1)*CF - ln(x)*LMUA*pow(NC,-1)*x*CF + 1.\
                          /2.*ln(x)*LMUA*pow(NC,-1)*x*z*CF + 2*ln(x)*LMUA*NC*pow(z,-1)*CF*pow(omx,-1) - ln(x)*LMUA*NC*\
                          pow(z,-1)*CF - ln(omx)*LMUA*pow(NC,-1)*pow(z,-1)*CF + ln(omx)*LMUA*pow(NC,-1)*CF - 1./2.*ln(omx)*LMUA*pow(\
                          NC,-1)*z*CF + ln(z)*LMUA*pow(NC,-1)*CF + 1./2.*ln(z)*LMUA*pow(NC,-1)*z*CF\
                           - ln(z)*LMUA*pow(NC,-1)*x*CF - 1./2.*ln(z)*LMUA*pow(NC,-1)*x*z*CF - 2*ln(z)*LMUA*NC*pow(z,-1)*CF - 5*ln(z)*LMUA*NC\
                          *CF - 1./2.*ln(z)*LMUA*NC*z*CF - 2*ln(z)*LMUA*NC*x*pow(z,-1)*CF - 3*ln(z)*LMUA*NC*x*CF - 15./\
                          2.*ln(z)*LMUA*NC*x*z*CF + 3*LMUA*pow(NC,-1)*pow(z,-1)*CF - 5./2.*LMUA*pow(NC,-1)*CF - 3./2.*LMUA*pow(NC,-1)*x*CF + LMUA*pow(NC,-1)*x*z*CF\
                           - 53./6.*LMUA*NC*pow(z,-1)*CF + 29./6.*LMUA*NC*CF + 3*LMUA*NC*z*CF - 4./3.*LMUA*NC*pow(z,2)*\
                          CF - 23./6.*LMUA*NC*x*pow(z,-1)*CF - 1./6.*LMUA*NC*x*CF + 11./3.*LMUA*NC*x*z*CF + 8./3.*LMUA*\
                          NC*x*pow(z,2)*CF - 1./3.*LMUA*NF*pow(z,-1)*CF + 2./3.*LMUA*NF*CF - 1./3.*LMUA*NF*x*pow(z,-1)*CF + 2./3.*LMUA*NF*x*CF - 2./3.*LMUA*NF*x*z*CF
        elif orders == '010':
            if z != x and z != round(1 - x, ndecimals):
                result += - 7./4.*LMUF*pow(NC,-1)*pow(z,-1)*CF + 5./2.*LMUF*pow(NC,-1)*CF - 2*\
                          LMUF*pow(NC,-1)*z*CF + 1./4.*LMUF*pow(NC,-1)*x*pow(z,-1)*CF + 1./2.*LMUF*pow(NC,-1)*x*CF - 1./\
                          2.*LMUF*pow(NC,-1)*x*z*CF + 7./4.*LMUF*NC*pow(z,-1)*CF - 5./2.*LMUF*NC*CF + 2*LMUF*NC*z*CF - \
                          1./4.*LMUF*NC*x*pow(z,-1)*CF - 1./2.*LMUF*NC*x*CF + 1./2.*LMUF*NC*x*z*CF - 2*ln(x)*LMUF*pow(\
                          NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 3./2.*ln(x)*LMUF*pow(NC,-1)*pow(z,-1)*CF + 2*ln(x)*LMUF*\
                          pow(NC,-1)*CF*pow(omx,-1) - 2*ln(x)*LMUF*pow(NC,-1)*CF - ln(x)*LMUF*pow(NC,-1)*z*CF*pow(\
                          omx,-1) + 1./2.*ln(x)*LMUF*pow(NC,-1)*z*CF + 3./2.*ln(x)*LMUF*pow(NC,-1)*x*pow(z,-1)*CF - 2*\
                          ln(x)*LMUF*pow(NC,-1)*x*CF + 3./2.*ln(x)*LMUF*pow(NC,-1)*x*z*CF + 2*ln(x)*LMUF*NC*pow(z,-1)*\
                          CF*pow(omx,-1) - 3./2.*ln(x)*LMUF*NC*pow(z,-1)*CF - 2*ln(x)*LMUF*NC*CF*pow(omx,-1) + 2*ln(x)*\
                          LMUF*NC*CF + ln(x)*LMUF*NC*z*CF*pow(omx,-1) - 1./2.*ln(x)*LMUF*NC*z*CF - 3./2.*ln(x)*LMUF*NC*\
                          x*pow(z,-1)*CF + 2*ln(x)*LMUF*NC*x*CF - 3./2.*ln(x)*LMUF*NC*x*z*CF - ln(z)*LMUF*pow(NC,-1)*pow(z,-1)*CF + ln(z)*LMUF*pow(\
                          NC,-1)*CF - 1./2.*ln(z)*LMUF*pow(NC,-1)*z*CF - ln(z)*LMUF*pow(NC,-1)*x*pow(z,-1)*CF + ln(z)*\
                          LMUF*pow(NC,-1)*x*CF - 1./2.*ln(z)*LMUF*pow(NC,-1)*x*z*CF + ln(z)*LMUF*NC*pow(z,-1)*CF - ln(z\
                          )*LMUF*NC*CF + 1./2.*ln(z)*LMUF*NC*z*CF + ln(z)*LMUF*NC*x*pow(z,-1)*CF - ln(z)*LMUF*NC*x*CF\
                           + 1./2.*ln(z)*LMUF*NC*x*z*CF - 2*ln(omx)*LMUF*pow(NC,-1)*pow(\
                          z,-1)*CF + 3*ln(omx)*LMUF*pow(NC,-1)*CF - 1./2.*ln(omx)*LMUF*pow(NC,-1)*z*CF - 2*ln(omx)*LMUF\
                          *pow(NC,-1)*x*pow(z,-1)*CF + 3*ln(omx)*LMUF*pow(NC,-1)*x*CF - 5./2.*ln(omx)*LMUF*pow(NC,-1)*x\
                          *z*CF + 2*ln(omx)*LMUF*NC*pow(z,-1)*CF - 3*ln(omx)*LMUF*NC*CF + 1./2.*ln(omx)*LMUF*NC*z*CF + \
                          2*ln(omx)*LMUF*NC*x*pow(z,-1)*CF - 3*ln(omx)*LMUF*NC*x*CF + 5./2.*ln(omx)*LMUF*NC*x*z*CF - ln(\
                          omz)*LMUF*pow(NC,-1)*pow(z,-1)*CF + ln(omz)*LMUF*pow(NC,-1)*CF - 1./2.*ln(omz)*LMUF*pow(\
                          NC,-1)*z*CF - ln(omz)*LMUF*pow(NC,-1)*x*pow(z,-1)*CF + ln(omz)*LMUF*pow(NC,-1)*x*CF - 1./2.*\
                          ln(omz)*LMUF*pow(NC,-1)*x*z*CF + ln(omz)*LMUF*NC*pow(z,-1)*CF - ln(omz)*LMUF*NC*CF + 1./2.*ln(omz)*LMUF*NC*z*CF + \
                          ln(omz)*LMUF*NC*x*pow(z,-1)*CF - ln(omz)*LMUF*NC*x*CF + 1./2.*ln(omz)*LMUF*NC*x*z*CF
        elif orders == '100':
            if z != x and z != round(1 - x, ndecimals):
                result += - 11./6.*LMUR*NC*pow(z,-1)*CF + 11./3.*LMUR*NC*CF - 11./6.*LMUR*NC*x*pow(z,-1)*CF + 11./3.*LMUR*NC*x*CF - 11./3.*LMUR*NC*x*z*CF + 1./3.*\
                          LMUR*NF*pow(z,-1)*CF - 2./3.*LMUR*NF*CF + 1./3.*LMUR*NF*x*pow(z,-1)*CF - 2./3.*LMUR*NF*x*CF+ 2./3.*LMUR*NF*x*z*CF
        elif orders == '011':
            if z != x and z != round(1 - x, ndecimals):
                result += + LMUA*LMUF*pow(NC,-1)*pow(z,-1)*CF - LMUA*LMUF*pow(NC,-1)*CF + 1./2.*LMUA*LMUF*pow(NC,-1)*z*CF + LMUA*LMUF*pow(NC,-1)*x*pow(z,-1)*CF \
                          - LMUA*LMUF*pow(NC,-1)*x*CF + 1./2.*LMUA*LMUF*pow(NC,-1)*x*z*CF - LMUA*LMUF*NC*pow(z,-1)*CF + LMUA*LMUF*NC*CF - 1./2.*LMUA*LMUF*NC*z*CF - LMUA*LMUF*NC*x*pow(z,-1)*CF + LMUA*LMUF*NC*x*CF - 1./2.*LMUA*LMUF*NC*x*z*CF
        return result
    elif rsl == 'rs':
        result = 0
        return result
    elif rsl == 'rl':
        result = 0
        return result
    elif rsl == 'sr':
        result = 0
        if orders == '000':
            result_0r = 9./2.*pow(NC,-1)*pow(z,-1)*CF + 2./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF - 17./4.*pow(NC,-1)\
                        *CF - 5./6.*pow(NC,-1)*pow(pi,2)*CF + 5./2.*pow(NC,-1)*z*CF + 5./12.*pow(NC,-1)*z*pow(pi,2)*\
                        CF - 55./18.*NC*pow(z,-1)*CF - 2./3.*NC*pow(z,-1)*pow(pi,2)*CF + 95./12.*NC*CF + 1./6.*NC*\
                        pow(pi,2)*CF - 31./6.*NC*z*CF - 3./4.*NC*z*pow(pi,2)*CF - 13./9.*NC*pow(z,2)*CF  + 3./2.*ln(z)*pow(NC,-1)*\
                        pow(z,-1)*CF - 89./6.*ln(z)*NC*pow(z,-1)*CF + 2*ln(z)*NC*CF + 2*ln(z)*NC*z*CF + 4./3.*ln(z)*\
                        NC*pow(z,2)*CF + 4*ln(z)*ln(1 + z)*NC*pow(z,-1)*CF + 4*ln(z)*ln(1 + z)*NC*CF\
                         + 2*ln(z)*ln(1 + z)*NC*z*CF - pow(ln(z),2)*pow(NC,-1)*CF + 1./2.*pow(ln(z),2)*pow(NC,-1)*z*\
                        CF - 6*pow(ln(z),2)*NC*pow(z,-1)*CF - 3*pow(ln(z),2)*NC*CF - 11./2.*pow(ln(z),2)*NC*z*CF + 2*\
                        ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 2*ln(z)*ln(omz)*pow(NC,-1)*CF + ln(z)*ln(omz)*pow(\
                        NC,-1)*z*CF + 6*ln(z)*ln(omz)*NC*pow(z,-1)*CF - 6*ln(z)*ln(omz)*NC*CF + 3*ln(z)*ln(omz)*NC*z*\
                        CF + 3*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(omz)*pow(NC,-1)*CF + 3./4.*ln(omz)*pow(NC,-1)*z\
                        *CF - 40./3.*ln(omz)*NC*pow(z,-1)*CF + 12*ln(omz)*NC*CF + 1./4.*ln(omz)*NC*z*CF + 4./3.*ln(\
                        omz)*NC*pow(z,2)*CF - 2*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF + 2*pow(ln(omz),2)*pow(NC,-1)*CF\
                         - pow(ln(omz),2)*pow(NC,-1)*z*CF + 4*pow(ln(omz),2)*NC*pow(z,-1)*CF - 4*pow(ln(omz),2)*NC*CF\
                         + 2*pow(ln(omz),2)*NC*z*CF + 4*Li2( - z)*NC*pow(z,-1)*CF + 4*Li2( - z)*NC*CF + 2*Li2( - z)*\
                        NC*z*CF + 6*Li2(z)*pow(NC,-1)*pow(z,-1)*CF - 5*Li2(z)*pow(NC,-1)*CF + 5./2.*Li2(z)*pow(NC,-1)\
                        *z*CF + 6*Li2(z)*NC*pow(z,-1)*CF + Li2(z)*NC*CF + 11./2.*Li2(z)*NC*z*CF
            result_1r = 3*pow(NC,-1)*pow(z,-1)*CF - 4*pow(NC,-1)*CF + 3./4.*pow(NC,-1)*z*CF - 40./3.*NC*pow(z,-1)*\
                        CF + 12*NC*CF + 1./4.*NC*z*CF + 4./3.*NC*pow(z,2)*CF - 2*ln(z)*pow(NC,-1)*pow(z,-1)*CF + ln(z)*\
                        pow(NC,-1)*CF - 1./2.*ln(z)*pow(NC,-1)*z*CF - 2*ln(z)*NC*pow(z,-1)*CF - 5*ln(z)*NC*CF - 7./2.\
                        *ln(z)*NC*z*CF - 4*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(omz)*pow(NC,-1)*CF - 2*ln(omz)*pow(\
                        NC,-1)*z*CF + 8*ln(omz)*NC*pow(z,-1)*CF - 8*ln(omz)*NC*CF + 4*ln(omz)*NC*z*CF
            result_2r = - 3*pow(NC,-1)*pow(z,-1)*CF + 3*pow(NC,-1)*CF - 3./2.*pow(NC,-1)*z*CF + 3*NC*pow(z,-1)*CF - 3*NC*CF + 3./2.*NC*z*CF
            result += result_0r*1/(1-x) + result_1r*ln(1-x)/(1-x) + result_2r*ln(1-x)*ln(1-x)/(1-x)
        elif orders == '001':
            result_0r = - 1./2.*ln(z)*LMUA*pow(NC,-1)*z*CF + 4*ln(z)*LMUA*NC*pow(z,-1)*CF + 3*ln(z)*LMUA*NC*\
                        CF + 9./2.*ln(z)*LMUA*NC*z*CF + 2*ln(omz)*LMUA*pow(NC,-1)*pow(z,-1)*CF - 2*ln(omz)*LMUA*pow(NC,-1)*CF + \
                        ln(omz)*LMUA*pow(NC,-1)*z*CF - 6*ln(omz)*LMUA*NC*pow(z,-1)*CF + 6*ln(omz)*LMUA*NC*CF - 3*ln(\
                        omz)*LMUA*NC*z*CF - 3./2.*LMUA*pow(NC,-1)*pow(z,-1)*CF + 5./2.*LMUA*pow(NC,-1)*CF - LMUA*pow(\
                        NC,-1)*z*CF + 49./6.*LMUA*NC*pow(z,-1)*CF - 41./6.*LMUA*NC*CF - 11./6.*LMUA*NC*z*CF - 4./3.*\
                        LMUA*NC*pow(z,2)*CF + 2./3.*LMUA*NF*pow(z,-1)*CF - 2./3.*LMUA*NF*CF + 1./3.*LMUA*NF*z*CF + ln(z)*LMUA*pow(NC,-1)*CF
            result_1r = + 2*LMUA*pow(NC,-1)*pow(z,-1)*CF - 2*LMUA*pow(NC,-1)*CF + LMUA*pow(NC,-1)*z*CF - 2*LMUA*NC*pow(z,-1)*CF + 2*LMUA*NC*CF - LMUA*NC*z*CF
            result += result_0r*1/(1-x) + result_1r*ln(1-x)/(1-x)
        elif orders == '010':
            result_0r =  + 2*ln(omz)*LMUF*pow(NC,-1)*pow(z,-1)*CF - 2*ln(omz)*LMUF*pow(NC,-1)*CF\
                         + ln(omz)*LMUF*pow(NC,-1)*z*CF - 2*ln(omz)*LMUF*NC*pow(z,-1)*CF + 2*ln(omz)*LMUF*NC*CF - ln(\
                        omz)*LMUF*NC*z*CF + 2*ln(z)*LMUF*pow(NC,-1)*pow(z,-1)*CF - 2*ln(z)*LMUF*pow(NC,-1)*CF + ln(z)*\
                        LMUF*pow(NC,-1)*z*CF - 2*ln(z)*LMUF*NC*pow(z,-1)*CF + 2*ln(z)*LMUF*NC*CF - ln(z)*LMUF*NC*z*CF + 3./2.*LMUF*pow(NC,-1)*pow(z,-1)*CF - 3./2.*LMUF*pow(\
                        NC,-1)*CF + 7./4.*LMUF*pow(NC,-1)*z*CF - 3./2.*LMUF*NC*pow(z,-1)*CF + 3./2.*LMUF*NC*CF - 7./4.*LMUF*NC*z*CF
            result_1r = + 4*LMUF*pow(NC,-1)*pow(z,-1)*CF - 4*LMUF*pow(NC,-1)*CF + 2*LMUF*pow(NC,-1)*z*CF - 4*LMUF*NC*pow(z,-1)*CF + 4*LMUF*NC*CF - 2*LMUF*NC*z*CF
            result += result_0r*1/(1-x) + result_1r*ln(1-x)/(1-x)
        elif orders == '100':
            result_0r = + 11./3.*LMUR*NC*pow(z,-1)*CF - 11./3.*LMUR*NC*CF + 11./6.*LMUR*NC*z*CF - 2./3.*LMUR*NF*pow(z,-1)*CF + 2./3.*LMUR*NF*CF - 1./3.*LMUR*NF*z*CF
            result += result_0r*1/(1-x)
        elif orders == '011':
            result_0r = - 2*LMUA*LMUF*pow(NC,-1)*pow(z,-1)*CF + 2*LMUA*LMUF*pow(NC,-1)*CF - LMUA*LMUF*pow(NC,-1)*z*CF + 2*LMUA*LMUF*NC*pow(z,-1)*CF - 2*LMUA*LMUF*NC*CF + LMUA*LMUF*NC*z*CF
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
            result += - 5*pow(NC,-1)*pow(z,-1)*zeta3*CF - 1./4.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF + 3*pow(NC,-1)\
      *CF + 3*pow(NC,-1)*zeta3*CF + 2./3.*pow(NC,-1)*pow(pi,2)*CF + 13./8.*pow(NC,-1)*z*CF - 3./2.*\
      pow(NC,-1)*z*zeta3*CF - 1./8.*pow(NC,-1)*z*pow(pi,2)*CF + 1169./54.*NC*pow(z,-1)*CF - 14*NC*\
      pow(z,-1)*zeta3*CF + 4./3.*NC*pow(z,-1)*pow(rln2,3)*CF - 1./4.*NC*pow(z,-1)*pow(pi,2)*CF - 2./\
      3.*NC*pow(z,-1)*pow(pi,2)*rln2*CF - 295./18.*NC*CF + 4./3.*NC*pow(rln2,3)*CF - 5./3.*NC*pow(\
      pi,2)*CF - 2./3.*NC*pow(pi,2)*rln2*CF - 389./72.*NC*z*CF - 12*NC*z*zeta3*CF + 2./3.*NC*z*pow(\
      rln2,3)*CF + 7./24.*NC*z*pow(pi,2)*CF - 1./3.*NC*z*pow(pi,2)*rln2*CF - 269./54.*NC*pow(z,2)*\
      CF
            result += - 2*ln(1 + z)*NC*pow(z,-1)*pow(rln2,2)*CF + 1./3.*ln(1 + z)*NC*pow(\
      z,-1)*pow(pi,2)*CF - 2*ln(1 + z)*NC*pow(rln2,2)*CF + 1./3.*ln(1 + z)*NC*pow(pi,2)*CF - ln(1\
       + z)*NC*z*pow(rln2,2)*CF + 1./6.*ln(1 + z)*NC*z*pow(pi,2)*CF + 9./2.*ln(z)*pow(NC,-1)*pow(\
      z,-1)*CF + 1./3.*ln(z)*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF - 67./8.*ln(z)*pow(NC,-1)*CF - 1./2.\
      *ln(z)*pow(NC,-1)*pow(pi,2)*CF + 45./8.*ln(z)*pow(NC,-1)*z*CF + 1./4.*ln(z)*pow(NC,-1)*z*pow(\
      pi,2)*CF + 71./18.*ln(z)*NC*pow(z,-1)*CF - ln(z)*NC*pow(z,-1)*pow(pi,2)*CF + 247./8.*ln(z)*NC\
      *CF - 1./6.*ln(z)*NC*pow(pi,2)*CF + 31./8.*ln(z)*NC*z*CF - 11./12.*ln(z)*NC*z*pow(pi,2)*CF + \
      31./9.*ln(z)*NC*pow(z,2)*CF
            result += + ln(z)*ln(1 + z)*NC*z*CF  + pow(ln(z),2)*pow(NC,-1)*CF - \
      13./16.*pow(ln(z),2)*pow(NC,-1)*z*CF - 20./3.*pow(ln(z),2)*NC*pow(z,-1)*CF - 5*pow(ln(z),2)*\
      NC*CF - 7./16.*pow(ln(z),2)*NC*z*CF  + 3*pow(ln(z),2)*ln(1 + z)*NC*pow(z,-1)*CF + 3*pow(ln(z),2)*ln(1\
       + z)*NC*CF + 3./2.*pow(ln(z),2)*ln(1 + z)*NC*z*CF - 5./12.*pow(ln(z),3)*pow(NC,-1)*CF + 5./\
      24.*pow(ln(z),3)*pow(NC,-1)*z*CF
            result +=  - 10./3.*pow(ln(z),3)*NC*pow(z,-1)*CF - 5./4.*pow(ln(z),3)*NC*CF - 65./24.*pow(ln(z),\
      3)*NC*z*CF + 2*pow(ln(z),2)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 2*pow(ln(z),2)*ln(omz)*pow(\
      NC,-1)*CF + pow(ln(z),2)*ln(omz)*pow(NC,-1)*z*CF + pow(ln(z),2)*ln(omz)*NC*pow(z,-1)*CF - \
      pow(ln(z),2)*ln(omz)*NC*CF + 1./2.*pow(ln(z),2)*ln(omz)*NC*z*CF + 3*ln(z)*ln(omz)*NC*z*CF  + 4*ln(z)*ln(omz)*ln(1 + z)*NC*pow(z,-1)*CF + 4*ln(z)*ln(omz)\
      *ln(1 + z)*NC*CF + 2*ln(z)*ln(omz)*ln(1 + z)*NC*z*CF + 2*ln(z)*pow(ln(omz),2)*pow(NC,-1)*pow(\
      z,-1)*CF - 3./2.*ln(z)*pow(ln(omz),2)*pow(NC,-1)*CF + 3./4.*ln(z)*pow(ln(omz),2)*pow(NC,-1)*z\
      *CF + 5*ln(z)*pow(ln(omz),2)*NC*pow(z,-1)*CF - 3./2.*ln(z)*pow(ln(omz),2)*NC*CF + 15./4.*ln(z\
      )*pow(ln(omz),2)*NC*z*CF + 2*ln(z)*Li2( - z)*NC*pow(z,-1)*CF + 2*ln(z)*Li2( - z)*NC*CF + ln(z\
      )*Li2( - z)*NC*z*CF + 6*ln(z)*Li2(z)*pow(NC,-1)*pow(z,-1)*CF - 6*ln(z)*Li2(z)*pow(NC,-1)*CF\
       + 3*ln(z)*Li2(z)*pow(NC,-1)*z*CF - 4*ln(z)*Li2(z)*NC*pow(z,-1)*CF + 4*ln(z)*Li2(z)*NC*CF - 2\
      *ln(z)*Li2(z)*NC*z*CF + 9./2.*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 1./3.*ln(omz)*pow(NC,-1)*pow(\
      z,-1)*pow(pi,2)*CF - 9./2.*ln(omz)*pow(NC,-1)*CF - 1./2.*ln(omz)*pow(NC,-1)*pow(pi,2)*CF + 5./\
      2.*ln(omz)*pow(NC,-1)*z*CF
            result +=  + 1./4.*ln(omz)*pow(NC,-1)*z*pow(pi,2)*CF - 55./18.*ln(omz)*NC*pow(z,-1)*CF - 2*ln(\
      omz)*NC*pow(z,-1)*pow(rln2,2)*CF - ln(omz)*NC*pow(z,-1)*pow(pi,2)*CF + 23./3.*ln(omz)*NC*CF\
       - 2*ln(omz)*NC*pow(rln2,2)*CF + 1./2.*ln(omz)*NC*pow(pi,2)*CF - 31./6.*ln(omz)*NC*z*CF - ln(\
      omz)*NC*z*pow(rln2,2)*CF - 11./12.*ln(omz)*NC*z*pow(pi,2)*CF - 13./9.*ln(omz)*NC*pow(z,2)*CF\
        + 4*ln(omz)*ln(1 + z)*NC*pow(z,-1)*rln2*CF + 4*ln(omz)*ln(1 + z)*NC*rln2*CF\
       + 2*ln(omz)*ln(1 + z)*NC*z*rln2*CF
            result +=  - 2*ln(omz)*pow(ln(1 + z),2)*NC*pow(z,-1)*CF - 2*ln(omz)*pow(ln(1 + z),2)*NC*CF - ln(\
      omz)*pow(ln(1 + z),2)*NC*z*CF + 3./2.*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF - 2*pow(ln(omz),\
      2)*pow(NC,-1)*CF + 1./8.*pow(ln(omz),2)*pow(NC,-1)*z*CF - 20./3.*pow(ln(omz),2)*NC*pow(z,-1)*\
      CF + 6*pow(ln(omz),2)*NC*CF - 1./8.*pow(ln(omz),2)*NC*z*CF + 2./3.*pow(ln(omz),2)*NC*pow(z,2)\
      *CF  - 5./6.*pow(ln(omz),3)*pow(NC,-1)*pow(z,-1)*CF\
       + 5./6.*pow(ln(omz),3)*pow(NC,-1)*CF - 5./12.*pow(ln(omz),3)*pow(NC,-1)*z*CF + 7./6.*pow(ln(\
      omz),3)*NC*pow(z,-1)*CF - 7./6.*pow(ln(omz),3)*NC*CF + 7./12.*pow(ln(omz),3)*NC*z*CF + 4*ln(\
      omz)*Li2( - z)*NC*pow(z,-1)*CF + 4*ln(omz)*Li2( - z)*NC*CF + 2*ln(omz)*Li2( - z)*NC*z*CF + 5*\
      ln(omz)*Li2(z)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(omz)*Li2(z)*pow(NC,-1)*CF + 2*ln(omz)*Li2(z)*\
      pow(NC,-1)*z*CF + 5*ln(omz)*Li2(z)*NC*pow(z,-1)*CF + 2*ln(omz)*Li2(z)*NC*CF + 5*ln(omz)*Li2(z\
      )*NC*z*CF + 2./3.*ln(opz)*NC*pow(z,-1)*pow(pi,2)*CF + 2./3.*ln(opz)*NC*pow(pi,2)*CF + 1./3.*\
      ln(opz)*NC*z*pow(pi,2)*CF - 4*Li3(1./2. - 1./2.*z)*NC*pow(z,-1)*CF - 4*Li3(1./2. - 1./2.*z)*\
      NC*CF - 2*Li3(1./2. - 1./2.*z)*NC*z*CF - 4*Li3(1./2. + 1./2.*z)*NC*pow(z,-1)*CF - 4*Li3(1./2.\
       + 1./2.*z)*NC*CF
            result +=  - 2*Li3(1./2. + 1./2.*z)*NC*z*CF + 3*Li3(1 - z)*pow(NC,-1)*pow(z,-1)*CF - 2*Li3(1 - z\
      )*pow(NC,-1)*CF + Li3(1 - z)*pow(NC,-1)*z*CF + 7*Li3(1 - z)*NC*pow(z,-1)*CF + 8*Li3(1 - z)*NC\
      *CF + 6*Li3(1 - z)*NC*z*CF + 2*Li3( - z)*NC*pow(z,-1)*CF + 2*Li3( - z)*NC*CF + Li3( - z)*NC*z\
      *CF + 4*Li3(1/(1 + z))*NC*pow(z,-1)*CF + 4*Li3(1/(1 + z))*NC*CF + 2*Li3(1/(1 + z))*NC*z*CF - \
      4*Li3(1/(1 + z) - 1/(1 + z)*z)*NC*pow(z,-1)*CF - 4*Li3(1/(1 + z) - 1/(1 + z)*z)*NC*CF - 2*\
      Li3(1/(1 + z) - 1/(1 + z)*z)*NC*z*CF - 6*Li3(z)*pow(NC,-1)*pow(z,-1)*CF + 8*Li3(z)*pow(NC,-1)\
      *CF - 4*Li3(z)*pow(NC,-1)*z*CF + 20*Li3(z)*NC*pow(z,-1)*CF - 2*Li3(z)*NC*CF + 15*Li3(z)*NC*z*\
      CF + Li2( - z)*NC*z*CF  - 3./2.*Li2(z)*pow(NC,-1)*pow(z,-1)*CF + Li2(z)*pow(NC,-1)*z*CF + 89./6.*\
      Li2(z)*NC*pow(z,-1)*CF - 2*Li2(z)*NC*CF + Li2(z)*NC*z*CF - 4./3.*Li2(z)*NC*pow(z,2)*CF
            result_0r = 9./2.*pow(NC,-1)*pow(z,-1)*CF + 2./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF - 17./4.*pow(NC,-1)\
                        *CF - 5./6.*pow(NC,-1)*pow(pi,2)*CF + 5./2.*pow(NC,-1)*z*CF + 5./12.*pow(NC,-1)*z*pow(pi,2)*\
                        CF - 55./18.*NC*pow(z,-1)*CF - 2./3.*NC*pow(z,-1)*pow(pi,2)*CF + 95./12.*NC*CF + 1./6.*NC*\
                        pow(pi,2)*CF - 31./6.*NC*z*CF - 3./4.*NC*z*pow(pi,2)*CF - 13./9.*NC*pow(z,2)*CF  + 3./2.*ln(z)*pow(NC,-1)*\
                        pow(z,-1)*CF - 89./6.*ln(z)*NC*pow(z,-1)*CF + 2*ln(z)*NC*CF + 2*ln(z)*NC*z*CF + 4./3.*ln(z)*\
                        NC*pow(z,2)*CF + 4*ln(z)*ln(1 + z)*NC*pow(z,-1)*CF + 4*ln(z)*ln(1 + z)*NC*CF\
                         + 2*ln(z)*ln(1 + z)*NC*z*CF - pow(ln(z),2)*pow(NC,-1)*CF + 1./2.*pow(ln(z),2)*pow(NC,-1)*z*\
                        CF - 6*pow(ln(z),2)*NC*pow(z,-1)*CF - 3*pow(ln(z),2)*NC*CF - 11./2.*pow(ln(z),2)*NC*z*CF + 2*\
                        ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 2*ln(z)*ln(omz)*pow(NC,-1)*CF + ln(z)*ln(omz)*pow(\
                        NC,-1)*z*CF + 6*ln(z)*ln(omz)*NC*pow(z,-1)*CF - 6*ln(z)*ln(omz)*NC*CF + 3*ln(z)*ln(omz)*NC*z*\
                        CF + 3*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(omz)*pow(NC,-1)*CF + 3./4.*ln(omz)*pow(NC,-1)*z\
                        *CF - 40./3.*ln(omz)*NC*pow(z,-1)*CF + 12*ln(omz)*NC*CF + 1./4.*ln(omz)*NC*z*CF + 4./3.*ln(\
                        omz)*NC*pow(z,2)*CF - 2*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF + 2*pow(ln(omz),2)*pow(NC,-1)*CF\
                         - pow(ln(omz),2)*pow(NC,-1)*z*CF + 4*pow(ln(omz),2)*NC*pow(z,-1)*CF - 4*pow(ln(omz),2)*NC*CF\
                         + 2*pow(ln(omz),2)*NC*z*CF + 4*Li2( - z)*NC*pow(z,-1)*CF + 4*Li2( - z)*NC*CF + 2*Li2( - z)*\
                        NC*z*CF + 6*Li2(z)*pow(NC,-1)*pow(z,-1)*CF - 5*Li2(z)*pow(NC,-1)*CF + 5./2.*Li2(z)*pow(NC,-1)\
                        *z*CF + 6*Li2(z)*NC*pow(z,-1)*CF + Li2(z)*NC*CF + 11./2.*Li2(z)*NC*z*CF
            result_1r = 3*pow(NC,-1)*pow(z,-1)*CF - 4*pow(NC,-1)*CF + 3./4.*pow(NC,-1)*z*CF - 40./3.*NC*pow(z,-1)*\
                        CF + 12*NC*CF + 1./4.*NC*z*CF + 4./3.*NC*pow(z,2)*CF - 2*ln(z)*pow(NC,-1)*pow(z,-1)*CF + ln(z)*\
                        pow(NC,-1)*CF - 1./2.*ln(z)*pow(NC,-1)*z*CF - 2*ln(z)*NC*pow(z,-1)*CF - 5*ln(z)*NC*CF - 7./2.\
                        *ln(z)*NC*z*CF - 4*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 4*ln(omz)*pow(NC,-1)*CF - 2*ln(omz)*pow(\
                        NC,-1)*z*CF + 8*ln(omz)*NC*pow(z,-1)*CF - 8*ln(omz)*NC*CF + 4*ln(omz)*NC*z*CF
            result_2r = - 3*pow(NC,-1)*pow(z,-1)*CF + 3*pow(NC,-1)*CF - 3./2.*pow(NC,-1)*z*CF + 3*NC*pow(z,-1)*CF - 3*NC*CF + 3./2.*NC*z*CF
            result += result_0r*ln(1-x) + result_1r*ln(1-x)*ln(1-x)/2 + result_2r*ln(1-x)*ln(1-x)*ln(1-x)/3
        elif orders == '001':
            result += - 9./2.*LMUA*pow(NC,-1)*pow(z,-1)*CF - 1./3.*LMUA*\
                      pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF + 17./4.*LMUA*pow(NC,-1)*CF + 1./2.*LMUA*pow(NC,-1)*pow(\
                      pi,2)*CF - 7./4.*LMUA*pow(NC,-1)*z*CF - 1./4.*LMUA*pow(NC,-1)*z*pow(pi,2)*CF + 55./18.*LMUA*\
                      NC*pow(z,-1)*CF + 1./3.*LMUA*NC*pow(z,-1)*pow(pi,2)*CF - 95./12.*LMUA*NC*CF + 1./6.*LMUA*NC*\
                      pow(pi,2)*CF + 31./12.*LMUA*NC*z*CF + 7./12.*LMUA*NC*z*pow(pi,2)*CF + 13./9.*LMUA*NC*pow(z,2)\
                      *CF - 4*Li2( - z)*LMUA*NC*pow(z,-1)*CF - 4*Li2( - z)*LMUA*NC*CF - 2*Li2(\
                        - z)*LMUA*NC*z*CF - 6*Li2(z)*LMUA*pow(NC,-1)*pow(z,-1)*CF + 5*Li2(z)*LMUA*pow(NC,-1)*CF - 5./2.*Li2(z)*LMUA*pow(\
                        NC,-1)*z*CF - 6*Li2(z)*LMUA*NC*pow(z,-1)*CF - Li2(z)*LMUA*NC*CF - 11./2.*Li2(z)*LMUA*NC*z*CF - 3./2.*ln(omz)*LMUA*pow(NC,-1)*pow(z,-1)*CF + 5./2.*ln(omz)*\
                        LMUA*pow(NC,-1)*CF + 49./6.*ln(omz)*LMUA*NC*pow(z,-1)*CF - 41./6.*ln(omz)*LMUA*NC*CF - 17./6.\
                        *ln(omz)*LMUA*NC*z*CF - 4./3.*ln(omz)*LMUA*NC*pow(z,2)*CF + 2./3.*ln(omz)*LMUA*NF*pow(z,-1)*\
                        CF - 2./3.*ln(omz)*LMUA*NF*CF + 1./3.*ln(omz)*LMUA*NF*z*CF + 2*pow(ln(omz),2)*LMUA*pow(NC,-1)*pow(z,-1)*CF - 2*pow(ln(omz),2)*LMUA*pow(NC,-1)*CF + \
                        pow(ln(omz),2)*LMUA*pow(NC,-1)*z*CF - 4*pow(ln(omz),2)*LMUA*NC*pow(z,-1)*CF + 4*pow(ln(omz),2\
                        )*LMUA*NC*CF - 2*pow(ln(omz),2)*LMUA*NC*z*CF - 3./2.*ln(z)*LMUA*pow(NC,-1)*CF + 3./4.*ln(z)*LMUA*pow(NC,-1)*z*CF + 29./3.*\
                        ln(z)*LMUA*NC*pow(z,-1)*CF + 19./6.*ln(z)*LMUA*NC*CF - 55./12.*ln(z)*LMUA*NC*z*CF - 4./3.*ln(\
                        z)*LMUA*NC*pow(z,2)*CF + 2./3.*ln(z)*LMUA*NF*pow(z,-1)*CF - 2./3.*ln(z)*LMUA*NF*CF + 1./3.*\
                        ln(z)*LMUA*NF*z*CF - 2*ln(z)*ln(omz)*LMUA*pow(NC,-1)*pow(z,-1)*CF + 2*ln(z)*ln(omz)*LMUA*pow(NC,-1)*CF - ln(z)*ln(\
                        omz)*LMUA*pow(NC,-1)*z*CF - 6*ln(z)*ln(omz)*LMUA*NC*pow(z,-1)*CF + 6*ln(z)*ln(omz)*LMUA*NC*CF\
                         - 3*ln(z)*ln(omz)*LMUA*NC*z*CF - 4*ln(z)*ln(1 + z)*LMUA*NC*pow(z,-1)*CF - 4\
                         *ln(z)*ln(1 + z)*LMUA*NC*CF - 2*ln(z)*ln(1 + z)*LMUA*NC*z*CF + pow(ln(z),2)*LMUA*pow(NC,-1)*CF - 1./2.*pow(ln(z),2)*\
                         LMUA*pow(NC,-1)*z*CF + 6*pow(ln(z),2)*LMUA*NC*pow(z,-1)*CF + 3*pow(ln(z),2)*LMUA*NC*CF + 11./\
                         2.*pow(ln(z),2)*LMUA*NC*z*CF + 1./3.*LMUA*NF*z*CF
            result_0r = - 1./2.*ln(z)*LMUA*pow(NC,-1)*z*CF + 4*ln(z)*LMUA*NC*pow(z,-1)*CF + 3*ln(z)*LMUA*NC*\
                        CF + 9./2.*ln(z)*LMUA*NC*z*CF + 2*ln(omz)*LMUA*pow(NC,-1)*pow(z,-1)*CF - 2*ln(omz)*LMUA*pow(NC,-1)*CF + \
                        ln(omz)*LMUA*pow(NC,-1)*z*CF - 6*ln(omz)*LMUA*NC*pow(z,-1)*CF + 6*ln(omz)*LMUA*NC*CF - 3*ln(\
                        omz)*LMUA*NC*z*CF - 3./2.*LMUA*pow(NC,-1)*pow(z,-1)*CF + 5./2.*LMUA*pow(NC,-1)*CF - LMUA*pow(\
                        NC,-1)*z*CF + 49./6.*LMUA*NC*pow(z,-1)*CF - 41./6.*LMUA*NC*CF - 11./6.*LMUA*NC*z*CF - 4./3.*\
                        LMUA*NC*pow(z,2)*CF + 2./3.*LMUA*NF*pow(z,-1)*CF - 2./3.*LMUA*NF*CF + 1./3.*LMUA*NF*z*CF + ln(z)*LMUA*pow(NC,-1)*CF
            result_1r = + 2*LMUA*pow(NC,-1)*pow(z,-1)*CF - 2*LMUA*pow(NC,-1)*CF + LMUA*pow(NC,-1)*z*CF - 2*LMUA*NC*pow(z,-1)*CF + 2*LMUA*NC*CF - LMUA*NC*z*CF
            result += result_0r*ln(1-x) + result_1r*ln(1-x)*ln(1-x)/2
        elif orders == '010':
            result += - 1./3.*LMUF*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF + 1./3.*LMUF*pow(NC,-1)*pow(pi,2)*CF + 3./4.*LMUF*pow(NC,-1)*z*CF - 1./6.*LMUF*pow(NC,-1)*z*\
                      pow(pi,2)*CF + 1./3.*LMUF*NC*pow(z,-1)*pow(pi,2)*CF - 1./3.*LMUF*NC*pow(pi,2)*CF - 3./4.*LMUF\
                      *NC*z*CF + 1./6.*LMUF*NC*z*pow(pi,2)*CF + 3./2.*ln(omz)*LMUF*pow(NC,-1)*pow(z,-1)*CF - 3./2.*ln(omz)*LMUF*pow(NC,-1)*CF + 3./4.*\
                      ln(omz)*LMUF*pow(NC,-1)*z*CF - 3./2.*ln(omz)*LMUF*NC*pow(z,-1)*CF + 3./2.*ln(omz)*LMUF*NC*CF\
                       - 3./4.*ln(omz)*LMUF*NC*z*CF + 3./2.*ln(z)*LMUF*pow(NC,-1)*pow(z,-1)*CF - 3./2.*ln(z)*LMUF*pow(NC,-1)*CF + 3./4.*ln(z)*\
                      LMUF*pow(NC,-1)*z*CF - 3./2.*ln(z)*LMUF*NC*pow(z,-1)*CF + 3./2.*ln(z)*LMUF*NC*CF - 3./4.*ln(z\
                      )*LMUF*NC*z*CF
            result_0r =  + 2*ln(omz)*LMUF*pow(NC,-1)*pow(z,-1)*CF - 2*ln(omz)*LMUF*pow(NC,-1)*CF\
                         + ln(omz)*LMUF*pow(NC,-1)*z*CF - 2*ln(omz)*LMUF*NC*pow(z,-1)*CF + 2*ln(omz)*LMUF*NC*CF - ln(\
                        omz)*LMUF*NC*z*CF + 2*ln(z)*LMUF*pow(NC,-1)*pow(z,-1)*CF - 2*ln(z)*LMUF*pow(NC,-1)*CF + ln(z)*\
                        LMUF*pow(NC,-1)*z*CF - 2*ln(z)*LMUF*NC*pow(z,-1)*CF + 2*ln(z)*LMUF*NC*CF - ln(z)*LMUF*NC*z*CF + 3./2.*LMUF*pow(NC,-1)*pow(z,-1)*CF - 3./2.*LMUF*pow(\
                        NC,-1)*CF + 7./4.*LMUF*pow(NC,-1)*z*CF - 3./2.*LMUF*NC*pow(z,-1)*CF + 3./2.*LMUF*NC*CF - 7./4.*LMUF*NC*z*CF
            result_1r = + 4*LMUF*pow(NC,-1)*pow(z,-1)*CF - 4*LMUF*pow(NC,-1)*CF + 2*LMUF*pow(NC,-1)*z*CF - 4*LMUF*NC*pow(z,-1)*CF + 4*LMUF*NC*CF - 2*LMUF*NC*z*CF
            result += result_0r*ln(1-x) + result_1r*ln(1-x)*ln(1-x)/2
        elif orders == '100':
            result += + 11./6.*LMUR*NC*z*CF - 1./3.*LMUR*NF*z*CF + 11./3.*ln(omz)*LMUR*NC*pow(z,-1)*CF - 11./3.*ln(omz)*LMUR*NC*CF + 11./6.*ln(omz)*LMUR*NC*z*CF - 2./3.*ln(omz)*LMUR*NF*pow(z,-1)*CF + 2./3.*ln(omz)*LMUR*NF*CF - 1./3.*ln(omz)*LMUR*NF*z*CF\
                      + 11./3.*ln(z)*LMUR*NC*pow(z,-1)*CF - 11./3.*ln(z)*LMUR*NC*CF + 11./6.*ln(z)*LMUR*NC*z*CF - 2./3.*ln(z)*LMUR*NF*pow(z,-1)*CF + 2./3.*ln(z)*LMUR*NF*CF - 1./3.*ln(z)*LMUR*NF*z*CF
            result_0r = + 11./3.*LMUR*NC*pow(z,-1)*CF - 11./3.*LMUR*NC*CF + 11./6.*LMUR*NC*z*CF - 2./3.*LMUR*NF*pow(z,-1)*CF + 2./3.*LMUR*NF*CF - 1./3.*LMUR*NF*z*CF
            result += result_0r*ln(1-x)
        elif orders == '011':
            result += - 3./2.*LMUA*LMUF*pow(NC,-1)*pow(z,-1)*CF + 3./2.*LMUA*LMUF*pow(NC,-1)*CF - 3./4.*LMUA*LMUF*pow(NC,-1)*z*CF + 3./2.*LMUA*LMUF*NC*pow(z,-1)*CF - 3./2.*LMUA*LMUF*NC*CF + 3./4.*LMUA*LMUF*NC*z*CF
            result_0r = - 2*LMUA*LMUF*pow(NC,-1)*pow(z,-1)*CF + 2*LMUA*LMUF*pow(NC,-1)*CF - LMUA*LMUF*pow(NC,-1)*z*CF + 2*LMUA*LMUF*NC*pow(z,-1)*CF - 2*LMUA*LMUF*NC*CF + LMUA*LMUF*NC*z*CF
            result += result_0r*ln(1-x)
        elif orders == '101':
            result += - 11./3.*LMUA*LMUR*NC*pow(z,-1)*CF + 11./3.*LMUA*LMUR*NC*CF - 11./6.*LMUA*LMUR*NC*z*CF + 2./3.*LMUA*LMUR*NF*pow(z,-1)*CF - 2./3.*LMUA*LMUR*NF*CF + 1./3.*LMUA*LMUR*NF*z*CF
        elif orders == '002':
            result += - ln(omz)*pow(LMUA,2)*pow(NC,-1)*pow(z,-1)*CF + ln(omz)*pow(LMUA,2)*pow(NC,-1)*CF - 1./2.*ln(omz)*pow(LMUA,2)*pow(NC,-1)*z*CF\
                       + 3*ln(omz)*pow(LMUA,2)*NC*pow(z,-1)*CF - 3*ln(omz)*pow(LMUA,2)*NC*CF + 3./2.*ln(omz)*pow(\
                      LMUA,2)*NC*z*CF - 1./2.*pow(LMUA,2)*pow(NC,-1)*CF + 1./8.*pow(LMUA,2)*pow(NC,-1)*z*CF - 3./\
                      2.*pow(LMUA,2)*NC*pow(z,-1)*CF + 5./6.*pow(LMUA,2)*NC*CF + 53./24.*pow(LMUA,2)*NC*z*CF + 2./3.\
                      *pow(LMUA,2)*NC*pow(z,2)*CF - 2./3.*pow(LMUA,2)*NF*pow(z,-1)*CF + 2./3.*pow(LMUA,2)*NF*CF - 1.\
                      /3.*pow(LMUA,2)*NF*z*CF - 1./2.*ln(z)*pow(LMUA,2)*pow(NC,-1)*CF + 1./4.*ln(z)*pow(LMUA,2)*pow(\
                        NC,-1)*z*CF - 2*ln(z)*pow(LMUA,2)*NC*pow(z,-1)*CF - 3./2.*ln(z)*pow(LMUA,2)*NC*CF - 9./4.*ln(\
                        z)*pow(LMUA,2)*NC*z*CF
        return result
    elif rsl == 'ls':
        result = 0
        return result
    elif rsl == 'll':
        result = 0
        return result
    else:
        raise ValueError('Invalid rsl value')
