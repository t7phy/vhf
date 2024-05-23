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
            if z != x and z != 1.-x:
                result += - 9*pow(NC,-1)*pow(z,-1)*CF - 4*pow(NC,-1)*pow(z,-1)*pow(rln2,2)*CF*pow(omx,-1) + 2*pow(
      NC,-1)*pow(z,-1)*pow(rln2,2)*CF - 6*pow(NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF*pow(omx,-1) + 4*pow(
      NC,-1)*pow(z,-1)*sqrtxz1*rln2*CF + 8./3.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF*pow(omx,-1) - 13./
      12.*pow(NC,-1)*pow(z,-1)*pow(pi,2)*CF + 41./4.*pow(NC,-1)*CF + 4*pow(NC,-1)*pow(rln2,2)*CF*
      pow(omx,-1) + 2*pow(NC,-1)*sqrtxz1*rln2*CF*pow(omx,-1) - 10./3.*pow(NC,-1)*pow(pi,2)*CF*pow(
      omx,-1) + 7./6.*pow(NC,-1)*pow(pi,2)*CF - 4*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*pow(NC,-1)*z*
      CF - 2*pow(NC,-1)*z*pow(rln2,2)*CF*pow(omx,-1) + 5./3.*pow(NC,-1)*z*pow(pi,2)*CF*pow(omx,-1)
       - 1./6.*pow(NC,-1)*z*pow(pi,2)*CF + 4*pow(NC,-1)*x*pow(z,-1)*CF + 2*pow(NC,-1)*x*pow(z,-1)*
      pow(rln2,2)*CF + 2*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*rln2*CF - 29./12.*pow(NC,-1)*x*pow(z,-1)*
      pow(pi,2)*CF - 2*pow(NC,-1)*x*CF*pow(omxmz,-1) + 23./4.*pow(NC,-1)*x*CF + 2*pow(NC,-1)*x*
      sqrtxz1*rln2*CF + 25./6.*pow(NC,-1)*x*pow(pi,2)*CF - 11./2.*pow(NC,-1)*x*z*CF - 5./2.*pow(
      NC,-1)*x*z*pow(pi,2)*CF + 2*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-1) - 2*pow(NC,-1)*pow(x,2)*CF
       - 2*pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-1) + 215./18.*NC*pow(z,-1)*CF - 2*NC*pow(z,-1)*pow(
      pi,2)*CF*pow(omx,-1) + 17./12.*NC*pow(z,-1)*pow(pi,2)*CF - 163./12.*NC*CF - 8*NC*pow(rln2,2)*
      CF*pow(omx,-1) + 4*NC*pow(rln2,2)*CF - 4*NC*sqrtxz1*rln2*CF*pow(omx,-1) + 4./3.*NC*pow(pi,2)*
      CF*pow(omx,-1);
      tmp +=  - 1./2.*NC*pow(pi,2)*CF + NC*z*CF*pow(omx,-1) + 4./3.*NC*z*CF - NC*z*pow(pi,2)*CF*
      pow(omx,-1) + 1./6.*NC*z*pow(pi,2)*CF - 31./9.*NC*pow(z,2)*CF - 43./18.*NC*x*pow(z,-1)*CF + 
      17./12.*NC*x*pow(z,-1)*pow(pi,2)*CF - 37./12.*NC*x*CF + 4*NC*x*pow(rln2,2)*CF + 4*NC*x*
      sqrtxz1*rln2*CF - 5./6.*NC*x*pow(pi,2)*CF + 1./3.*NC*x*z*CF + 4*NC*x*z*pow(rln2,2)*CF + 5./2.
      *NC*x*z*pow(pi,2)*CF + 53./9.*NC*x*pow(z,2)*CF;
      tmp +=  + 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(
      omx,-1) - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*rln2*CF + 6*ln(1 + sqrtxz1 - z)*pow(
      NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*
      CF - 8*ln(1 + sqrtxz1 - z)*pow(NC,-1)*rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*
      sqrtxz1*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) - 4*ln(1 + 
      sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF - 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*pow(z,-1)*
      sqrtxz1*CF - 2*ln(1 + sqrtxz1 - z)*pow(NC,-1)*x*sqrtxz1*CF - 4*ln(1 + sqrtxz1 - z)*NC*pow(
      z,-1)*rln2*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)*rln2*CF + 12*ln(1 + sqrtxz1 - 
      z)*NC*rln2*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 - z)*NC*rln2*CF + 4*ln(1 + sqrtxz1 - z)*NC*
      sqrtxz1*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 - z)*NC*z*rln2*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - 
      z)*NC*x*pow(z,-1)*rln2*CF - 4*ln(1 + sqrtxz1 - z)*NC*x*rln2*CF - 4*ln(1 + sqrtxz1 - z)*NC*x*
      sqrtxz1*CF;
      tmp +=  - 4*ln(1 + sqrtxz1 - z)*NC*x*z*rln2*CF - 4*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(
      z,-1)*CF*pow(omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*pow(z,-1)*CF + 4*pow(ln(1 + 
      sqrtxz1 - z),2)*pow(NC,-1)*CF*pow(omx,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*z*CF*pow(
      omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*pow(NC,-1)*x*pow(z,-1)*CF + 4*pow(ln(1 + sqrtxz1 - z),
      2)*NC*pow(z,-1)*CF*pow(omx,-1) - 2*pow(ln(1 + sqrtxz1 - z),2)*NC*pow(z,-1)*CF - 4*pow(ln(1 + 
      sqrtxz1 - z),2)*NC*CF*pow(omx,-1) + 2*pow(ln(1 + sqrtxz1 - z),2)*NC*z*CF*pow(omx,-1) - 2*pow(
      ln(1 + sqrtxz1 - z),2)*NC*x*pow(z,-1)*CF - 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*pow(
      z,-1)*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*CF - 4*ln(1 + 
      sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*CF*pow(omx,-1) + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z
      )*NC*CF - 2*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*z*CF*pow(omx,-1) + 2*ln(1 + sqrtxz1 - 
      z)*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1)*CF + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*x*CF
       + 4*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*NC*x*z*CF + 4*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*
      rln2*CF*pow(omx,-1) - 2*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*rln2*CF + 4*ln(1 + sqrtxz1 + z)*NC*
      rln2*CF*pow(omx,-1) - 4*ln(1 + sqrtxz1 + z)*NC*rln2*CF + 2*ln(1 + sqrtxz1 + z)*NC*z*rln2*CF*
      pow(omx,-1) - 2*ln(1 + sqrtxz1 + z)*NC*x*pow(z,-1)*rln2*CF - 4*ln(1 + sqrtxz1 + z)*NC*x*rln2*
      CF;
      tmp +=  - 4*ln(1 + sqrtxz1 + z)*NC*x*z*rln2*CF + 12*ln(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)
       + 1./4.*ln(x)*pow(NC,-1)*pow(z,-1)*CF - 6*ln(x)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) + 3
      *ln(x)*pow(NC,-1)*pow(z,-1)*rln2*CF - 3*ln(x)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 2
      *ln(x)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF - 12*ln(x)*pow(NC,-1)*CF*pow(omx,-1) + ln(x)*pow(
      NC,-1)*CF + 6*ln(x)*pow(NC,-1)*rln2*CF*pow(omx,-1) + ln(x)*pow(NC,-1)*sqrtxz1*CF*pow(omx,-1)
       + 51./4.*ln(x)*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*ln(x)*pow(NC,-1)*z*CF - 3*ln(x)*pow(
      NC,-1)*z*rln2*CF*pow(omx,-1) - 43./4.*ln(x)*pow(NC,-1)*x*pow(z,-1)*CF + 3*ln(x)*pow(NC,-1)*x*
      pow(z,-1)*rln2*CF + ln(x)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF + 4*ln(x)*pow(NC,-1)*x*CF + 4*ln(
      x)*pow(NC,-1)*x*CF*omx + ln(x)*pow(NC,-1)*x*sqrtxz1*CF - 15./2.*ln(x)*pow(NC,-1)*x*z*CF - 2*
      ln(x)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-2) + 2*ln(x)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-1) + 2
      *ln(x)*pow(NC,-1)*pow(x,2)*CF + 2*ln(x)*pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-2) - 4*ln(x)*pow(
      NC,-1)*pow(x,3)*CF*pow(omxmz,-1) - 2*ln(x)*pow(NC,-1)*pow(x,4)*CF*pow(omxmz,-2) + 35./3.*ln(x
      )*NC*pow(z,-1)*CF*pow(omx,-1) - 163./12.*ln(x)*NC*pow(z,-1)*CF + 4*ln(x)*NC*pow(z,-1)*rln2*CF
      *pow(omx,-1) - 2*ln(x)*NC*pow(z,-1)*rln2*CF - 4*ln(x)*NC*CF*pow(omx,-1) + ln(x)*NC*CF - 8*ln(
      x)*NC*rln2*CF*pow(omx,-1) + 2*ln(x)*NC*rln2*CF - 2*ln(x)*NC*sqrtxz1*CF*pow(omx,-1) - 51./4.*
      ln(x)*NC*z*CF*pow(omx,-1);
      tmp +=  + 13./2.*ln(x)*NC*z*CF + 2*ln(x)*NC*z*rln2*CF*pow(omx,-1) - 8./3.*ln(x)*NC*pow(z,2)*
      CF*pow(omx,-1) - 8./3.*ln(x)*NC*pow(z,2)*CF - 67./12.*ln(x)*NC*x*pow(z,-1)*CF - 2*ln(x)*NC*x*
      pow(z,-1)*rln2*CF + 5*ln(x)*NC*x*CF + 2*ln(x)*NC*x*rln2*CF + 2*ln(x)*NC*x*sqrtxz1*CF + 13./2.
      *ln(x)*NC*x*z*CF + 2*ln(x)*NC*x*z*rln2*CF + 16./3.*ln(x)*NC*x*pow(z,2)*CF;
      tmp +=  + 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 2*ln(x)*
      ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF - 4*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*CF*pow(
      omx,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 - 
      z)*pow(NC,-1)*x*pow(z,-1)*CF - 4*ln(x)*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*
      ln(x)*ln(1 + sqrtxz1 - z)*NC*pow(z,-1)*CF + 4*ln(x)*ln(1 + sqrtxz1 - z)*NC*CF*pow(omx,-1) - 2
      *ln(x)*ln(1 + sqrtxz1 - z)*NC*z*CF*pow(omx,-1) + 2*ln(x)*ln(1 + sqrtxz1 - z)*NC*x*pow(z,-1)*
      CF + 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - ln(x)*ln(1 + sqrtxz1
       + z)*pow(NC,-1)*pow(z,-1)*CF - 2*ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*CF*pow(omx,-1) + ln(x)
      *ln(1 + sqrtxz1 + z)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(x)*ln(1 + sqrtxz1 + z)*pow(NC,-1)*x*
      pow(z,-1)*CF + 4*ln(x)*ln(1 + sqrtxz1 + z)*NC*CF*pow(omx,-1) - 2*ln(x)*ln(1 + sqrtxz1 + z)*NC
      *CF - 2*ln(x)*ln(1 + sqrtxz1 + z)*NC*x*CF - 2*ln(x)*ln(1 + sqrtxz1 + z)*NC*x*z*CF - 17*pow(
      ln(x),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 11./2.*pow(ln(x),2)*pow(NC,-1)*pow(z,-1)*CF + 
      24*pow(ln(x),2)*pow(NC,-1)*CF*pow(omx,-1) - 9*pow(ln(x),2)*pow(NC,-1)*CF - 12*pow(ln(x),2)*
      pow(NC,-1)*z*CF*pow(omx,-1);
      tmp +=  + 1./2.*pow(ln(x),2)*pow(NC,-1)*z*CF + 25./2.*pow(ln(x),2)*pow(NC,-1)*x*pow(z,-1)*CF
       - 23*pow(ln(x),2)*pow(NC,-1)*x*CF + 31./2.*pow(ln(x),2)*pow(NC,-1)*x*z*CF + 10*pow(ln(x),2)*
      NC*pow(z,-1)*CF*pow(omx,-1) - 11./2.*pow(ln(x),2)*NC*pow(z,-1)*CF - 10*pow(ln(x),2)*NC*CF*
      pow(omx,-1) + 9*pow(ln(x),2)*NC*CF + 5*pow(ln(x),2)*NC*z*CF*pow(omx,-1) - 1./2.*pow(ln(x),2)*
      NC*z*CF - 11./2.*pow(ln(x),2)*NC*x*pow(z,-1)*CF + 9*pow(ln(x),2)*NC*x*CF - 17./2.*pow(ln(x),2
      )*NC*x*z*CF + 16*ln(x)*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 5*ln(x)*ln(z)*pow(NC,-1)*
      pow(z,-1)*CF - 25*ln(x)*ln(z)*pow(NC,-1)*CF*pow(omx,-1) + 10*ln(x)*ln(z)*pow(NC,-1)*CF + 25./
      2.*ln(x)*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 11*ln(x)*ln(z)*pow(NC,-1)*x*pow(z,-1)*CF + 20*
      ln(x)*ln(z)*pow(NC,-1)*x*CF - 17*ln(x)*ln(z)*pow(NC,-1)*x*z*CF - 6*ln(x)*ln(z)*NC*pow(z,-1)*
      CF*pow(omx,-1) + 3*ln(x)*ln(z)*NC*pow(z,-1)*CF + 19*ln(x)*ln(z)*NC*CF*pow(omx,-1) - 18*ln(x)*
      ln(z)*NC*CF + 7./2.*ln(x)*ln(z)*NC*z*CF*pow(omx,-1) + 3*ln(x)*ln(z)*NC*x*pow(z,-1)*CF - 16*
      ln(x)*ln(z)*NC*x*CF - ln(x)*ln(z)*NC*x*z*CF + 20*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(
      omx,-1) - 5*ln(x)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF - 26*ln(x)*ln(omx)*pow(NC,-1)*CF*pow(
      omx,-1) + 10*ln(x)*ln(omx)*pow(NC,-1)*CF + 13*ln(x)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(
      x)*ln(omx)*pow(NC,-1)*z*CF - 15*ln(x)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF + 30*ln(x)*ln(omx)*
      pow(NC,-1)*x*CF;
      tmp +=  - 19*ln(x)*ln(omx)*pow(NC,-1)*x*z*CF - 16*ln(x)*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1)
       + 8*ln(x)*ln(omx)*NC*pow(z,-1)*CF + 16*ln(x)*ln(omx)*NC*CF*pow(omx,-1) - 16*ln(x)*ln(omx)*NC
      *CF - 8*ln(x)*ln(omx)*NC*z*CF*pow(omx,-1) + ln(x)*ln(omx)*NC*z*CF + 8*ln(x)*ln(omx)*NC*x*pow(
      z,-1)*CF - 16*ln(x)*ln(omx)*NC*x*CF + 15*ln(x)*ln(omx)*NC*x*z*CF + 24*ln(x)*ln(omz)*pow(
      NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 15./2.*ln(x)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF - 34*ln(x)*ln(
      omz)*pow(NC,-1)*CF*pow(omx,-1) + 13*ln(x)*ln(omz)*pow(NC,-1)*CF + 17*ln(x)*ln(omz)*pow(NC,-1)
      *z*CF*pow(omx,-1) - ln(x)*ln(omz)*pow(NC,-1)*z*CF - 35./2.*ln(x)*ln(omz)*pow(NC,-1)*x*pow(
      z,-1)*CF + 33*ln(x)*ln(omz)*pow(NC,-1)*x*CF - 22*ln(x)*ln(omz)*pow(NC,-1)*x*z*CF - 14*ln(x)*
      ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 15./2.*ln(x)*ln(omz)*NC*pow(z,-1)*CF + 14*ln(x)*ln(omz)
      *NC*CF*pow(omx,-1) - 13*ln(x)*ln(omz)*NC*CF - 7*ln(x)*ln(omz)*NC*z*CF*pow(omx,-1) + ln(x)*ln(
      omz)*NC*z*CF + 15./2.*ln(x)*ln(omz)*NC*x*pow(z,-1)*CF - 13*ln(x)*ln(omz)*NC*x*CF + 12*ln(x)*
      ln(omz)*NC*x*z*CF - 3*ln(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 5*ln(z)*pow(NC,-1)*pow(
      z,-1)*CF - 2*ln(z)*pow(NC,-1)*pow(z,-1)*rln2*CF*pow(omx,-1) + ln(z)*pow(NC,-1)*pow(z,-1)*rln2
      *CF - 3*ln(z)*pow(NC,-1)*pow(z,-1)*sqrtxz1*CF*pow(omx,-1) + 2*ln(z)*pow(NC,-1)*pow(z,-1)*
      sqrtxz1*CF + 8*ln(z)*pow(NC,-1)*CF*pow(omx,-1) - 4*ln(z)*pow(NC,-1)*CF + 2*ln(z)*pow(NC,-1)*
      rln2*CF*pow(omx,-1);
      tmp +=  + ln(z)*pow(NC,-1)*sqrtxz1*CF*pow(omx,-1) - 7*ln(z)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(
      z)*pow(NC,-1)*z*CF - ln(z)*pow(NC,-1)*z*rln2*CF*pow(omx,-1) + 5*ln(z)*pow(NC,-1)*x*pow(z,-1)*
      CF + ln(z)*pow(NC,-1)*x*pow(z,-1)*rln2*CF + ln(z)*pow(NC,-1)*x*pow(z,-1)*sqrtxz1*CF - 7*ln(z)
      *pow(NC,-1)*x*CF + ln(z)*pow(NC,-1)*x*sqrtxz1*CF + 9*ln(z)*pow(NC,-1)*x*z*CF + 4*ln(z)*NC*
      pow(z,-1)*CF*pow(omx,-1) + 44./3.*ln(z)*NC*pow(z,-1)*CF - 4*ln(z)*NC*pow(z,-1)*rln2*CF*pow(
      omx,-1) + 2*ln(z)*NC*pow(z,-1)*rln2*CF - 2*ln(z)*NC*CF*pow(omx,-1) + 14*ln(z)*NC*CF - 8*ln(z)
      *NC*rln2*CF*pow(omx,-1) + 6*ln(z)*NC*rln2*CF - 2*ln(z)*NC*sqrtxz1*CF*pow(omx,-1) + 6*ln(z)*NC
      *z*CF*pow(omx,-1) + 2*ln(z)*NC*z*CF - 2*ln(z)*NC*z*rln2*CF*pow(omx,-1) + 4./3.*ln(z)*NC*pow(
      z,2)*CF + 11./3.*ln(z)*NC*x*pow(z,-1)*CF + 2*ln(z)*NC*x*pow(z,-1)*rln2*CF - 2*ln(z)*NC*x*CF
       + 6*ln(z)*NC*x*rln2*CF + 2*ln(z)*NC*x*sqrtxz1*CF - 13*ln(z)*NC*x*z*CF + 6*ln(z)*NC*x*z*rln2*
      CF - 8./3.*ln(z)*NC*x*pow(z,2)*CF;
      tmp +=  + 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 
      ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*pow(z,-1)*CF - 2*ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*CF
      *pow(omx,-1) + ln(z)*ln(1 + sqrtxz1 - z)*pow(NC,-1)*z*CF*pow(omx,-1) - ln(z)*ln(1 + sqrtxz1
       - z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*ln(z)*ln(1 + sqrtxz1 - z)*NC*CF*pow(omx,-1) - 2*ln(z)*ln(
      1 + sqrtxz1 - z)*NC*CF - 2*ln(z)*ln(1 + sqrtxz1 - z)*NC*x*CF - 2*ln(z)*ln(1 + sqrtxz1 - z)*NC
      *x*z*CF + 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*pow(z,-1)*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + 
      z)*NC*pow(z,-1)*CF + 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*CF*pow(omx,-1) - 4*ln(z)*ln(1 + sqrtxz1
       + z)*NC*CF + 2*ln(z)*ln(1 + sqrtxz1 + z)*NC*z*CF*pow(omx,-1) - 2*ln(z)*ln(1 + sqrtxz1 + z)*
      NC*x*pow(z,-1)*CF - 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*x*CF - 4*ln(z)*ln(1 + sqrtxz1 + z)*NC*x*z*
      CF - 4*ln(z)*ln(1 + z)*NC*pow(z,-1)*CF*pow(omx,-1) - 4*ln(z)*ln(1 + z)*NC*CF*pow(omx,-1) - 2*
      ln(z)*ln(1 + z)*NC*z*CF*pow(omx,-1) - 3*pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 
      pow(ln(z),2)*pow(NC,-1)*pow(z,-1)*CF + 6*pow(ln(z),2)*pow(NC,-1)*CF*pow(omx,-1) - 4*pow(ln(z)
      ,2)*pow(NC,-1)*CF - 3*pow(ln(z),2)*pow(NC,-1)*z*CF*pow(omx,-1) - 1./2.*pow(ln(z),2)*pow(
      NC,-1)*z*CF;
      tmp +=  + 2*pow(ln(z),2)*pow(NC,-1)*x*pow(z,-1)*CF - 4*pow(ln(z),2)*pow(NC,-1)*x*CF + 9./2.*
      pow(ln(z),2)*pow(NC,-1)*x*z*CF + pow(ln(z),2)*NC*pow(z,-1)*CF*pow(omx,-1) + 5./2.*pow(ln(z),2
      )*NC*pow(z,-1)*CF - 3*pow(ln(z),2)*NC*CF*pow(omx,-1) + 9*pow(ln(z),2)*NC*CF + 1./2.*pow(ln(z)
      ,2)*NC*z*CF*pow(omx,-1) + 1./2.*pow(ln(z),2)*NC*z*CF + 5./2.*pow(ln(z),2)*NC*x*pow(z,-1)*CF
       + 7*pow(ln(z),2)*NC*x*CF + 15./2.*pow(ln(z),2)*NC*x*z*CF - 8*ln(z)*ln(omx)*pow(NC,-1)*pow(
      z,-1)*CF*pow(omx,-1) + 3*ln(z)*ln(omx)*pow(NC,-1)*pow(z,-1)*CF + 12*ln(z)*ln(omx)*pow(NC,-1)*
      CF*pow(omx,-1) - 6*ln(z)*ln(omx)*pow(NC,-1)*CF - 6*ln(z)*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1)
       + 7*ln(z)*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 12*ln(z)*ln(omx)*pow(NC,-1)*x*CF + 9*ln(z)*ln(
      omx)*pow(NC,-1)*x*z*CF + 8*ln(z)*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) - 3*ln(z)*ln(omx)*NC*
      pow(z,-1)*CF - 8*ln(z)*ln(omx)*NC*CF*pow(omx,-1) + 14*ln(z)*ln(omx)*NC*CF + 4*ln(z)*ln(omx)*
      NC*z*CF*pow(omx,-1) - 3*ln(z)*ln(omx)*NC*x*pow(z,-1)*CF + 12*ln(z)*ln(omx)*NC*x*CF - ln(z)*
      ln(omx)*NC*x*z*CF - 12*ln(z)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 4*ln(z)*ln(omz)*
      pow(NC,-1)*pow(z,-1)*CF + 20*ln(z)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 8*ln(z)*ln(omz)*pow(
      NC,-1)*CF - 10*ln(z)*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + 6*ln(z)*ln(omz)*pow(NC,-1)*x*pow(
      z,-1)*CF - 12*ln(z)*ln(omz)*pow(NC,-1)*x*CF + 10*ln(z)*ln(omz)*pow(NC,-1)*x*z*CF + 4*ln(z)*
      ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1);
      tmp +=  - 5*ln(z)*ln(omz)*NC*pow(z,-1)*CF - 4*ln(z)*ln(omz)*NC*CF*pow(omx,-1) + 10*ln(z)*ln(
      omz)*NC*CF + 2*ln(z)*ln(omz)*NC*z*CF*pow(omx,-1) - 5*ln(z)*ln(omz)*NC*x*pow(z,-1)*CF + 10*ln(
      z)*ln(omz)*NC*x*CF - 10*ln(z)*ln(omz)*NC*x*z*CF - 6*ln(omx)*pow(NC,-1)*pow(z,-1)*CF*pow(
      omx,-1) - 11./4.*ln(omx)*pow(NC,-1)*pow(z,-1)*CF + 6*ln(omx)*pow(NC,-1)*CF*pow(omx,-1) + 4*
      ln(omx)*pow(NC,-1)*CF - 6*ln(omx)*pow(NC,-1)*z*CF*pow(omx,-1) + 1./2.*ln(omx)*pow(NC,-1)*z*CF
       + 17./4.*ln(omx)*pow(NC,-1)*x*pow(z,-1)*CF - 3*ln(omx)*pow(NC,-1)*x*CF + 4*ln(omx)*pow(
      NC,-1)*x*z*CF + 4*ln(omx)*NC*pow(z,-1)*CF*pow(omx,-1) + 125./12.*ln(omx)*NC*pow(z,-1)*CF - 4*
      ln(omx)*NC*CF*pow(omx,-1) - 3*ln(omx)*NC*CF + 4*ln(omx)*NC*z*CF*pow(omx,-1) - 7./2.*ln(omx)*
      NC*z*CF + 4./3.*ln(omx)*NC*pow(z,2)*CF + 41./12.*ln(omx)*NC*x*pow(z,-1)*CF - 6*ln(omx)*NC*x*
      CF - 3*ln(omx)*NC*x*z*CF - 8./3.*ln(omx)*NC*x*pow(z,2)*CF;
      tmp +=  - 5*pow(ln(omx),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 2*pow(ln(omx),2)*pow(
      NC,-1)*pow(z,-1)*CF + 6*pow(ln(omx),2)*pow(NC,-1)*CF*pow(omx,-1) - 3*pow(ln(omx),2)*pow(
      NC,-1)*CF - 3*pow(ln(omx),2)*pow(NC,-1)*z*CF*pow(omx,-1) + 1./2.*pow(ln(omx),2)*pow(NC,-1)*z*
      CF + 6*pow(ln(omx),2)*pow(NC,-1)*x*pow(z,-1)*CF - 11*pow(ln(omx),2)*pow(NC,-1)*x*CF + 13./2.*
      pow(ln(omx),2)*pow(NC,-1)*x*z*CF + 4*pow(ln(omx),2)*NC*pow(z,-1)*CF*pow(omx,-1) - 7./2.*pow(
      ln(omx),2)*NC*pow(z,-1)*CF - 4*pow(ln(omx),2)*NC*CF*pow(omx,-1) + 6*pow(ln(omx),2)*NC*CF + 2*
      pow(ln(omx),2)*NC*z*CF*pow(omx,-1) - 1./2.*pow(ln(omx),2)*NC*z*CF - 7./2.*pow(ln(omx),2)*NC*x
      *pow(z,-1)*CF + 6*pow(ln(omx),2)*NC*x*CF - 11./2.*pow(ln(omx),2)*NC*x*z*CF - 12*ln(omx)*ln(
      omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 5*ln(omx)*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 16*ln(
      omx)*ln(omz)*pow(NC,-1)*CF*pow(omx,-1) - 8*ln(omx)*ln(omz)*pow(NC,-1)*CF - 8*ln(omx)*ln(omz)*
      pow(NC,-1)*z*CF*pow(omx,-1) + ln(omx)*ln(omz)*pow(NC,-1)*z*CF + 11*ln(omx)*ln(omz)*pow(NC,-1)
      *x*pow(z,-1)*CF - 20*ln(omx)*ln(omz)*pow(NC,-1)*x*CF + 13*ln(omx)*ln(omz)*pow(NC,-1)*x*z*CF
       + 4*ln(omx)*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1);
      tmp +=  - 6*ln(omx)*ln(omz)*NC*pow(z,-1)*CF - 4*ln(omx)*ln(omz)*NC*CF*pow(omx,-1) + 10*ln(omx
      )*ln(omz)*NC*CF + 2*ln(omx)*ln(omz)*NC*z*CF*pow(omx,-1) - ln(omx)*ln(omz)*NC*z*CF - 6*ln(omx)
      *ln(omz)*NC*x*pow(z,-1)*CF + 10*ln(omx)*ln(omz)*NC*x*CF - 9*ln(omx)*ln(omz)*NC*x*z*CF - 8*ln(
      omz)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - 11./4.*ln(omz)*pow(NC,-1)*pow(z,-1)*CF + 8*ln(omz)
      *pow(NC,-1)*CF*pow(omx,-1) + ln(omz)*pow(NC,-1)*CF - 8*ln(omz)*pow(NC,-1)*z*CF*pow(omx,-1) + 
      2*ln(omz)*pow(NC,-1)*z*CF + 25./4.*ln(omz)*pow(NC,-1)*x*pow(z,-1)*CF - 4*ln(omz)*pow(NC,-1)*x
      *CF*omx + 9./2.*ln(omz)*pow(NC,-1)*x*z*CF + 2*ln(omz)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-2) - 
      2*ln(omz)*pow(NC,-1)*pow(x,2)*CF*pow(omxmz,-1) - 2*ln(omz)*pow(NC,-1)*pow(x,2)*CF - 2*ln(omz)
      *pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-2) + 4*ln(omz)*pow(NC,-1)*pow(x,3)*CF*pow(omxmz,-1) + 2*
      ln(omz)*pow(NC,-1)*pow(x,4)*CF*pow(omxmz,-2) + 2*ln(omz)*NC*pow(z,-1)*CF*pow(omx,-1) + 125./
      12.*ln(omz)*NC*pow(z,-1)*CF - 2*ln(omz)*NC*CF*pow(omx,-1) - 6*ln(omz)*NC*CF + 2*ln(omz)*NC*z*
      CF*pow(omx,-1) - 5*ln(omz)*NC*z*CF + 4./3.*ln(omz)*NC*pow(z,2)*CF + 65./12.*ln(omz)*NC*x*pow(
      z,-1)*CF - 6*ln(omz)*NC*x*CF + 1./2.*ln(omz)*NC*x*z*CF - 8./3.*ln(omz)*NC*x*pow(z,2)*CF;
      tmp += - 8*pow(ln(omz),2)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 3*pow(ln(omz),2)*pow(
      NC,-1)*pow(z,-1)*CF + 12*pow(ln(omz),2)*pow(NC,-1)*CF*pow(omx,-1) - 5*pow(ln(omz),2)*pow(
      NC,-1)*CF - 6*pow(ln(omz),2)*pow(NC,-1)*z*CF*pow(omx,-1) + 1./2.*pow(ln(omz),2)*pow(NC,-1)*z*
      CF + 7*pow(ln(omz),2)*pow(NC,-1)*x*pow(z,-1)*CF - 13*pow(ln(omz),2)*pow(NC,-1)*x*CF + 17./2.*
      pow(ln(omz),2)*pow(NC,-1)*x*z*CF + pow(ln(omz),2)*NC*pow(z,-1)*CF*pow(omx,-1) - 5./2.*pow(ln(
      omz),2)*NC*pow(z,-1)*CF - pow(ln(omz),2)*NC*CF*pow(omx,-1) + 4*pow(ln(omz),2)*NC*CF + 1./2.*
      pow(ln(omz),2)*NC*z*CF*pow(omx,-1) - 1./2.*pow(ln(omz),2)*NC*z*CF - 5./2.*pow(ln(omz),2)*NC*x
      *pow(z,-1)*CF + 4*pow(ln(omz),2)*NC*x*CF - 7./2.*pow(ln(omz),2)*NC*x*z*CF + 2*Li2(1./2. - 1./
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(1./2. - 1./
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF;
      tmp +=  - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*CF*pow(omx,-1)
       + Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(1.
      /2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2(1./2. - 1./
      2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF*pow(omx,-1) + 2*Li2(1./2. - 1./2.*
      pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*
      pow(z,-1)*sqrtxz1)*NC*CF - 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*z*CF*
      pow(omx,-1) + 2*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*pow(z,-1)*CF + 2*
      Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*CF + 2*Li2(1./2. - 1./2.*pow(
      z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*z*CF - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*
      sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*
      sqrtxz1)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*
      pow(NC,-1)*CF*pow(omx,-1) - Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)
      *z*CF*pow(omx,-1) + Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*pow(NC,-1)*x*pow(
      z,-1)*CF + 4*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF*pow(
      omx,-1) - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*pow(z,-1)*CF - 2*Li2(1./
      2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*CF;
      tmp +=  + 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*z*CF*pow(omx,-1) - 2*
      Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*pow(z,-1)*CF - 2*Li2(1./2. + 1./2.
      *pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*NC*x*CF - 2*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(
      z,-1)*sqrtxz1)*NC*x*z*CF + 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*
      pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF - 2*Li2(1./2. - 1./
      2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*CF*pow(omx,-1) + Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(
      NC,-1)*z*CF*pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*CF + 4*
      Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*CF*pow(omx,-1) - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*
      z)*NC*CF - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*NC*x*CF - 2*Li2(1./2. - 1./2.*sqrtxz1 - 1./
      2.*z)*NC*x*z*CF - 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1)
       + Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(1./2. - 1./2.*sqrtxz1
       + 1./2.*z)*pow(NC,-1)*CF*pow(omx,-1) - Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*z*CF*
      pow(omx,-1) + Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*pow(NC,-1)*x*pow(z,-1)*CF - 4*Li2(1./2. - 
      1./2.*sqrtxz1 + 1./2.*z)*NC*CF*pow(omx,-1) + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*CF + 2
      *Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*x*CF + 2*Li2(1./2. - 1./2.*sqrtxz1 + 1./2.*z)*NC*x*z
      *CF;
      tmp +=  + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) - Li2(1 - x*pow(z,-1))*
      pow(NC,-1)*pow(z,-1)*CF - 4*Li2(1 - x*pow(z,-1))*pow(NC,-1)*CF*pow(omx,-1) + 2*Li2(1 - x*pow(
      z,-1))*pow(NC,-1)*CF + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*z*CF*pow(omx,-1) - Li2(1 - x*pow(
      z,-1))*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(1 - x*pow(z,-1))*pow(NC,-1)*x*CF - 2*Li2(1 - x*pow(
      z,-1))*pow(NC,-1)*x*z*CF - 2*Li2(1 - x*pow(z,-1))*NC*pow(z,-1)*CF*pow(omx,-1) + Li2(1 - x*
      pow(z,-1))*NC*pow(z,-1)*CF + 2*Li2(1 - x*pow(z,-1))*NC*CF*pow(omx,-1) - 2*Li2(1 - x*pow(z,-1)
      )*NC*CF - Li2(1 - x*pow(z,-1))*NC*z*CF*pow(omx,-1) + Li2(1 - x*pow(z,-1))*NC*x*pow(z,-1)*CF
       - 2*Li2(1 - x*pow(z,-1))*NC*x*CF + 2*Li2(1 - x*pow(z,-1))*NC*x*z*CF - 4*Li2( - z)*NC*pow(
      z,-1)*CF*pow(omx,-1) - 4*Li2( - z)*NC*CF*pow(omx,-1) - 2*Li2( - z)*NC*z*CF*pow(omx,-1) - 2*
      Li2(x)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 3./2.*Li2(x)*pow(NC,-1)*pow(z,-1)*CF + 2*Li2(x)*
      pow(NC,-1)*CF*pow(omx,-1) - Li2(x)*pow(NC,-1)*CF - Li2(x)*pow(NC,-1)*z*CF*pow(omx,-1) + 3./2.
      *Li2(x)*pow(NC,-1)*x*pow(z,-1)*CF - Li2(x)*pow(NC,-1)*x*CF + Li2(x)*pow(NC,-1)*x*z*CF - 1./2.
      *Li2(x)*NC*pow(z,-1)*CF - Li2(x)*NC*CF - 1./2.*Li2(x)*NC*x*pow(z,-1)*CF - Li2(x)*NC*x*CF + 
      Li2(x)*NC*x*z*CF - 4*Li2(z)*pow(NC,-1)*pow(z,-1)*CF*pow(omx,-1) + 6*Li2(z)*pow(NC,-1)*CF*pow(
      omx,-1) - 3*Li2(z)*pow(NC,-1)*z*CF*pow(omx,-1) - 2*Li2(z)*pow(NC,-1)*x*pow(z,-1)*CF + 2*Li2(z
      )*pow(NC,-1)*x*CF;
      tmp +=  - Li2(z)*pow(NC,-1)*x*z*CF - 3*Li2(z)*NC*pow(z,-1)*CF - 2*Li2(z)*NC*CF - 3*Li2(z)*NC*
      x*pow(z,-1)*CF - 11*Li2(z)*NC*x*z*CF;
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
