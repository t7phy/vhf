from configs.eh import *

LMUR = 1
LMUF = 1
LMUA = 1

def cl_nnlo_q2qp_es(x, z, rsl, orders):

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
                result += - 4./3.*pow(x,-1)*z*pow(pi,2)*CF*pow(opx,-1) + 4./3.*pow(x,-1)*z*pow(pi,2)*CF + 8./3.*\
          pow(x,-1)*pow(z,2)*pow(pi,2)*CF*pow(opx,-1) - 8./3.*pow(x,-1)*pow(z,2)*pow(pi,2)*CF + 2*CF - \
          2*z*CF - 4./3.*z*pow(pi,2)*CF*pow(opx,-1) + 8./3.*pow(z,2)*pow(pi,2)*CF*pow(opx,-1) - 2*x*CF\
           - 8*x*sqrtxz1*rln2*CF + 2*x*z*CF - 4./3.*x*z*pow(pi,2)*CF - 32*x*pow(z,2)*pow(rln2,2)*CF + 8.\
          /3.*x*pow(z,2)*pow(pi,2)*CF - 2*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF + 2*\
          ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*sqrtxz3*CF - 46*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*pow(z,2)*\
          sqrtxz3*CF + 6*ArcTan(z*sqrtxz3)*ln(z*sqrtxz3)*x*z*sqrtxz3*CF + 2*ArcTan(sqrtxz3)*ln(sqrtxz3)\
          *pow(x,-1)*z*sqrtxz3*CF - 2*ArcTan(sqrtxz3)*ln(sqrtxz3)*sqrtxz3*CF + 46*ArcTan(sqrtxz3)*ln(\
          sqrtxz3)*pow(z,2)*sqrtxz3*CF - 6*ArcTan(sqrtxz3)*ln(sqrtxz3)*x*z*sqrtxz3*CF + InvTanInt( - \
          sqrtxz3)*pow(x,-1)*z*sqrtxz3*CF - InvTanInt( - sqrtxz3)*sqrtxz3*CF + 23*InvTanInt( - sqrtxz3)\
          *pow(z,2)*sqrtxz3*CF - 3*InvTanInt( - sqrtxz3)*x*z*sqrtxz3*CF + 2*InvTanInt(z*sqrtxz3)*pow(\
          x,-1)*z*sqrtxz3*CF - 2*InvTanInt(z*sqrtxz3)*sqrtxz3*CF + 46*InvTanInt(z*sqrtxz3)*pow(z,2)*\
          sqrtxz3*CF - 6*InvTanInt(z*sqrtxz3)*x*z*sqrtxz3*CF - InvTanInt(sqrtxz3)*pow(x,-1)*z*sqrtxz3*\
          CF + InvTanInt(sqrtxz3)*sqrtxz3*CF - 23*InvTanInt(sqrtxz3)*pow(z,2)*sqrtxz3*CF + 3*InvTanInt(\
          sqrtxz3)*x*z*sqrtxz3*CF + 8*ln(1 + sqrtxz1 - z)*x*sqrtxz1*CF - 8*ln(1 + sqrtxz1 - z)*x*z*rln2\
          *CF
                result +=  + 48*ln(1 + sqrtxz1 - z)*x*pow(z,2)*rln2*CF + 8*pow(ln(1 + sqrtxz1 - z),2)*x*z*CF - \
          16*pow(ln(1 + sqrtxz1 - z),2)*x*pow(z,2)*CF - 8*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*x*z*\
          CF - 16*ln(1 + sqrtxz1 - z)*ln(1 + sqrtxz1 + z)*x*pow(z,2)*CF + 8*ln(1 + sqrtxz1 + z)*x*z*\
          rln2*CF + 16*ln(1 + sqrtxz1 + z)*x*pow(z,2)*rln2*CF + 1./2.*ln(x)*pow(x,-1)*pow(poly2,-1)*CF\
           - 1./2.*ln(x)*pow(x,-1)*CF - 16*ln(x)*pow(x,-1)*z*CF*pow(opx,-1) + 16*ln(x)*pow(x,-1)*z*CF\
           + 32*ln(x)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - 32*ln(x)*pow(x,-1)*pow(z,2)*CF - 1./2.*ln(x)*\
          pow(poly2,-1)*CF + 1./2.*ln(x)*CF - 16*ln(x)*z*CF*pow(opx,-1) - ln(x)*z*CF + 32*ln(x)*pow(\
          z,2)*CF*pow(opx,-1) - ln(x)*x*pow(poly2,-1)*CF + 11./2.*ln(x)*x*CF - 4*ln(x)*x*sqrtxz1*CF - 5\
          *ln(x)*x*z*CF + 8*ln(x)*x*z*rln2*CF - 32*ln(x)*x*pow(z,2)*rln2*CF + ln(x)*pow(x,2)*pow(\
          poly2,-1)*CF - 4*ln(x)*pow(x,2)*CF*pow(xmz,-1) - 7./2.*ln(x)*pow(x,2)*CF + 1./2.*ln(x)*pow(\
          x,3)*pow(poly2,-1)*CF + 4*ln(x)*pow(x,3)*CF*pow(xmz,-1) - 1./2.*ln(x)*pow(x,4)*pow(poly2,-1)*\
          CF + 1./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*ln(x)\
          *ln(1 - sqrtxz2 + x)*pow(x,-1)*pow(sqrtxz2,-1)*CF + 1./2.*ln(x)*ln(1 - sqrtxz2 + x)*pow(\
          sqrtxz2,-1)*CF - ln(x)*ln(1 - sqrtxz2 + x)*z*pow(sqrtxz2,-1)*CF - 3./4.*ln(x)*ln(1 - sqrtxz2\
           + x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 4*ln(x)*ln(1 - sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF\
           + 12*ln(x)*ln(1 - sqrtxz2 + x)*x*z*pow(sqrtxz2,-1)*CF
                result +=  - 12*ln(x)*ln(1 - sqrtxz2 + x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 9./2.*ln(x)*ln(1 - \
          sqrtxz2 + x)*pow(x,2)*pow(sqrtxz2,-1)*CF + 9*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,2)*z*pow(\
          sqrtxz2,-1)*CF + 3./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + \
          1./4.*ln(x)*ln(1 - sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*CF - 1./4.*ln(x)*ln(1 - sqrtxz2 + x)\
          *pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,-1)*pow(\
          sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,-1)*pow(sqrtxz2,-1)*CF\
           - 1./2.*ln(x)*ln(1 + sqrtxz2 + x)*pow(sqrtxz2,-1)*CF + ln(x)*ln(1 + sqrtxz2 + x)*z*pow(\
          sqrtxz2,-1)*CF + 3./4.*ln(x)*ln(1 + sqrtxz2 + x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 4*ln(x)\
          *ln(1 + sqrtxz2 + x)*x*pow(sqrtxz2,-1)*CF - 12*ln(x)*ln(1 + sqrtxz2 + x)*x*z*pow(sqrtxz2,-1)*\
          CF + 12*ln(x)*ln(1 + sqrtxz2 + x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF + 9./2.*ln(x)*ln(1 + sqrtxz2\
           + x)*pow(x,2)*pow(sqrtxz2,-1)*CF - 9*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF\
           - 3./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*ln(x)*\
          ln(1 + sqrtxz2 + x)*pow(x,3)*pow(sqrtxz2,-1)*CF + 1./4.*ln(x)*ln(1 + sqrtxz2 + x)*pow(x,5)*\
          pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 8*ln(x)*ln(1 + sqrtxz1 - z)*x*z*CF + 16*ln(x)*ln(1 + \
          sqrtxz1 - z)*x*pow(z,2)*CF + 16*ln(x)*ln(1 + sqrtxz1 + z)*x*pow(z,2)*CF + 4*ln(x)*ln(1 + x*\
          pow(z,-1))*pow(x,-1)*z*CF*pow(opx,-1)
                result +=  - 4*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-1)*z*CF - 8*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-1)*\
          pow(z,2)*CF*pow(opx,-1) + 8*ln(x)*ln(1 + x*pow(z,-1))*pow(x,-1)*pow(z,2)*CF + 4*ln(x)*ln(1 + \
          x*pow(z,-1))*z*CF*pow(opx,-1) - 8*ln(x)*ln(1 + x*pow(z,-1))*pow(z,2)*CF*pow(opx,-1) + 4*ln(x)\
          *ln(1 + x*pow(z,-1))*x*z*CF - 8*ln(x)*ln(1 + x*pow(z,-1))*x*pow(z,2)*CF - 8*ln(x)*ln(1 + x)*x\
          *CF + 24*ln(x)*ln(1 + x)*x*z*CF - 16*ln(x)*ln(1 + x)*x*pow(z,2)*CF + 4*ln(x)*ln(1 + x*z)*pow(\
          x,-1)*z*CF*pow(opx,-1) - 4*ln(x)*ln(1 + x*z)*pow(x,-1)*z*CF - 8*ln(x)*ln(1 + x*z)*pow(x,-1)*\
          pow(z,2)*CF*pow(opx,-1) + 8*ln(x)*ln(1 + x*z)*pow(x,-1)*pow(z,2)*CF + 4*ln(x)*ln(1 + x*z)*z*\
          CF*pow(opx,-1) - 8*ln(x)*ln(1 + x*z)*pow(z,2)*CF*pow(opx,-1) - 16*ln(x)*ln(1 + x*z)*x*pow(\
          z,2)*CF + 4*ln(x)*ln(z + x)*x*z*CF + 8*ln(x)*ln(z + x)*x*pow(z,2)*CF + 6*pow(ln(x),2)*pow(\
          x,-1)*z*CF*pow(opx,-1) - 6*pow(ln(x),2)*pow(x,-1)*z*CF - 12*pow(ln(x),2)*pow(x,-1)*pow(z,2)*\
          CF*pow(opx,-1) + 12*pow(ln(x),2)*pow(x,-1)*pow(z,2)*CF + 6*pow(ln(x),2)*z*CF*pow(opx,-1) - 12\
          *pow(ln(x),2)*pow(z,2)*CF*pow(opx,-1) + 4*pow(ln(x),2)*x*CF - 12*pow(ln(x),2)*x*z*CF + 8*pow(\
          ln(x),2)*x*pow(z,2)*CF - 4*ln(x)*ln(z)*pow(x,-1)*z*CF*pow(opx,-1) + 4*ln(x)*ln(z)*pow(x,-1)*z\
          *CF + 8*ln(x)*ln(z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - 8*ln(x)*ln(z)*pow(x,-1)*pow(z,2)*CF\
           - 4*ln(x)*ln(z)*z*CF*pow(opx,-1) + 8*ln(x)*ln(z)*pow(z,2)*CF*pow(opx,-1) + 4*ln(x)*ln(z)*x*z\
          *CF
                result +=  - 8*ln(x)*ln(z)*x*pow(z,2)*CF + 8*ln(x)*ln(omx)*pow(x,-1)*z*CF*pow(opx,-1) - 8*ln(x)*\
          ln(omx)*pow(x,-1)*z*CF - 16*ln(x)*ln(omx)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 16*ln(x)*ln(omx\
          )*pow(x,-1)*pow(z,2)*CF + 8*ln(x)*ln(omx)*z*CF*pow(opx,-1) - 16*ln(x)*ln(omx)*pow(z,2)*CF*\
          pow(opx,-1) + 8*ln(x)*ln(omx)*x*z*CF - 16*ln(x)*ln(omx)*x*pow(z,2)*CF - 8*ln(x)*ln(opx)*pow(\
          x,-1)*z*CF*pow(opx,-1) + 8*ln(x)*ln(opx)*pow(x,-1)*z*CF + 16*ln(x)*ln(opx)*pow(x,-1)*pow(z,2)\
          *CF*pow(opx,-1) - 16*ln(x)*ln(opx)*pow(x,-1)*pow(z,2)*CF - 8*ln(x)*ln(opx)*z*CF*pow(opx,-1)\
           + 16*ln(x)*ln(opx)*pow(z,2)*CF*pow(opx,-1) - 8*ln(x)*ln(opx)*x*z*CF + 16*ln(x)*ln(opx)*x*\
          pow(z,2)*CF + 1./2.*ln(z)*pow(x,-1)*pow(poly2,-1)*CF - 1./2.*ln(z)*pow(x,-1)*CF + 1./2.*ln(z)\
          *pow(poly2,-1)*CF + 3./2.*ln(z)*CF - ln(z)*z*CF - ln(z)*x*pow(poly2,-1)*CF - 1./2.*ln(z)*x*CF\
           - 4*ln(z)*x*sqrtxz1*CF + 5*ln(z)*x*z*CF - 8*ln(z)*x*z*rln2*CF - 32*ln(z)*x*pow(z,2)*rln2*CF\
           - ln(z)*pow(x,2)*pow(poly2,-1)*CF + 4*ln(z)*pow(x,2)*CF*pow(xmz,-1) + 7./2.*ln(z)*pow(x,2)*\
          CF + 1./2.*ln(z)*pow(x,3)*pow(poly2,-1)*CF - 4*ln(z)*pow(x,3)*CF*pow(xmz,-1) + 1./2.*ln(z)*\
          pow(x,4)*pow(poly2,-1)*CF + 16*ln(z)*ln(1 + sqrtxz1 - z)*x*pow(z,2)*CF + 8*ln(z)*ln(1 + \
          sqrtxz1 + z)*x*z*CF + 16*ln(z)*ln(1 + sqrtxz1 + z)*x*pow(z,2)*CF - 4*ln(z)*ln(1 + x*pow(z,-1)\
          )*pow(x,-1)*z*CF*pow(opx,-1) + 4*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-1)*z*CF + 8*ln(z)*ln(1 + x*\
          pow(z,-1))*pow(x,-1)*pow(z,2)*CF*pow(opx,-1)
                result +=  - 8*ln(z)*ln(1 + x*pow(z,-1))*pow(x,-1)*pow(z,2)*CF - 4*ln(z)*ln(1 + x*pow(z,-1))*z*\
          CF*pow(opx,-1) + 8*ln(z)*ln(1 + x*pow(z,-1))*pow(z,2)*CF*pow(opx,-1) - 4*ln(z)*ln(1 + x*pow(\
          z,-1))*x*z*CF + 8*ln(z)*ln(1 + x*pow(z,-1))*x*pow(z,2)*CF + 4*ln(z)*ln(1 + x*z)*pow(x,-1)*z*\
          CF*pow(opx,-1) - 4*ln(z)*ln(1 + x*z)*pow(x,-1)*z*CF - 8*ln(z)*ln(1 + x*z)*pow(x,-1)*pow(z,2)*\
          CF*pow(opx,-1) + 8*ln(z)*ln(1 + x*z)*pow(x,-1)*pow(z,2)*CF + 4*ln(z)*ln(1 + x*z)*z*CF*pow(\
          opx,-1) - 8*ln(z)*ln(1 + x*z)*pow(z,2)*CF*pow(opx,-1) - 16*ln(z)*ln(1 + x*z)*x*pow(z,2)*CF - \
          4*ln(z)*ln(z + x)*x*z*CF - 8*ln(z)*ln(z + x)*x*pow(z,2)*CF - 2*pow(ln(z),2)*pow(x,-1)*z*CF*\
          pow(opx,-1) + 2*pow(ln(z),2)*pow(x,-1)*z*CF + 4*pow(ln(z),2)*pow(x,-1)*pow(z,2)*CF*pow(\
          opx,-1) - 4*pow(ln(z),2)*pow(x,-1)*pow(z,2)*CF - 2*pow(ln(z),2)*z*CF*pow(opx,-1) + 4*pow(ln(z\
          ),2)*pow(z,2)*CF*pow(opx,-1) + 2*pow(ln(z),2)*x*CF - 8*pow(ln(z),2)*x*z*CF + 8*pow(ln(z),2)*x\
          *pow(z,2)*CF - 4*ln(z)*ln(omz)*x*CF + 8*ln(z)*ln(omz)*x*z*CF + 1./4.*Li2(1./2. - 1./2.*pow(\
          x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2.\
           - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*CF + 1./2.*Li2(1./2.\
           - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(sqrtxz2,-1)*CF - Li2(1./2. - 1./2.*pow(\
          x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*z*pow(sqrtxz2,-1)*CF - 3./4.*Li2(1./2. - 1./2.*pow(x,-1) - 1.\
          /2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF
                result +=  - 4*Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*CF + 12*\
          Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*z*pow(sqrtxz2,-1)*CF - 12*Li2(1./2.\
           - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 9./2.*Li2(1./2.\
           - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*pow(sqrtxz2,-1)*CF + 9*Li2(1./2. - 1./\
          2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 3./4.*Li2(1./2. - 1./\
          2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*\
          Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(sqrtxz2,-1)*CF - 1./4.*\
          Li2(1./2. - 1./2.*pow(x,-1) - 1./2.*pow(x,-1)*sqrtxz2)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)\
          *CF - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,-1)*pow(sqrtxz2,-1)*\
          pow(poly2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,-1)*\
          pow(sqrtxz2,-1)*CF - 1./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(\
          sqrtxz2,-1)*CF + Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*z*pow(sqrtxz2,-1)*CF\
           + 3./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*pow(\
          poly2,-1)*CF + 4*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*pow(sqrtxz2,-1)*CF\
           - 12*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*z*pow(sqrtxz2,-1)*CF + 12*Li2(\
          1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*x*pow(z,2)*pow(sqrtxz2,-1)*CF
                result +=  + 9./2.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*pow(\
          sqrtxz2,-1)*CF - 9*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,2)*z*pow(\
          sqrtxz2,-1)*CF - 3./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*pow(x,3)*pow(\
          sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*\
          pow(x,3)*pow(sqrtxz2,-1)*CF + 1./4.*Li2(1./2. - 1./2.*pow(x,-1) + 1./2.*pow(x,-1)*sqrtxz2)*\
          pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 8*Li2(1./2. - 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*\
          sqrtxz1)*x*z*CF + 8*Li2(1./2. + 1./2.*pow(z,-1) - 1./2.*pow(z,-1)*sqrtxz1)*x*z*CF - 1./4.*\
          Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1.\
          /2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(sqrtxz2,-1)*CF - 1./2.*Li2(1./2. - 1./2.*sqrtxz2\
           - 1./2.*x)*pow(sqrtxz2,-1)*CF + Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*z*pow(sqrtxz2,-1)*CF + \
          3./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 4*Li2(1./2.\
           - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*CF - 12*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*\
          z*pow(sqrtxz2,-1)*CF + 12*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF\
           + 9./2.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*pow(sqrtxz2,-1)*CF - 9*Li2(1./2. - 1./\
          2.*sqrtxz2 - 1./2.*x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF - 3./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.\
          *x)*pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF
                result +=  - 1./4.*Li2(1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,3)*pow(sqrtxz2,-1)*CF + 1./4.*Li2(\
          1./2. - 1./2.*sqrtxz2 - 1./2.*x)*pow(x,5)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2.\
           + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 1./4.*Li2(1./2. + 1./\
          2.*sqrtxz2 - 1./2.*x)*pow(x,-1)*pow(sqrtxz2,-1)*CF + 1./2.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*\
          x)*pow(sqrtxz2,-1)*CF - Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*z*pow(sqrtxz2,-1)*CF - 3./4.*\
          Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*pow(poly2,-1)*CF - 4*Li2(1./2. + 1./2.\
          *sqrtxz2 - 1./2.*x)*x*pow(sqrtxz2,-1)*CF + 12*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*z*pow(\
          sqrtxz2,-1)*CF - 12*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*x*pow(z,2)*pow(sqrtxz2,-1)*CF - 9./2.\
          *Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,2)*pow(sqrtxz2,-1)*CF + 9*Li2(1./2. + 1./2.*\
          sqrtxz2 - 1./2.*x)*pow(x,2)*z*pow(sqrtxz2,-1)*CF + 3./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)\
          *pow(x,3)*pow(sqrtxz2,-1)*pow(poly2,-1)*CF + 1./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(\
          x,3)*pow(sqrtxz2,-1)*CF - 1./4.*Li2(1./2. + 1./2.*sqrtxz2 - 1./2.*x)*pow(x,5)*pow(sqrtxz2,-1)\
          *pow(poly2,-1)*CF + 16*Li2(1./2. - 1./2.*sqrtxz1 - 1./2.*z)*x*pow(z,2)*CF - 16*Li2(1./2. - 1./\
          2.*sqrtxz1 + 1./2.*z)*x*pow(z,2)*CF + 4*Li2(1 - x*pow(z,-1))*x*CF - 8*Li2(1 - x*pow(z,-1))*x*\
          z*CF + 4*Li2( - x*pow(z,-1))*pow(x,-1)*z*CF*pow(opx,-1) - 4*Li2( - x*pow(z,-1))*pow(x,-1)*z*\
          CF
                result +=  - 8*Li2( - x*pow(z,-1))*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 8*Li2( - x*pow(z,-1))*\
          pow(x,-1)*pow(z,2)*CF + 4*Li2( - x*pow(z,-1))*z*CF*pow(opx,-1) - 8*Li2( - x*pow(z,-1))*pow(\
          z,2)*CF*pow(opx,-1) + 8*Li2( - x*pow(z,-1))*x*z*CF - 8*Li2( - x)*pow(x,-1)*z*CF*pow(opx,-1)\
           + 8*Li2( - x)*pow(x,-1)*z*CF + 16*Li2( - x)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) - 16*Li2( - x)\
          *pow(x,-1)*pow(z,2)*CF - 8*Li2( - x)*z*CF*pow(opx,-1) + 16*Li2( - x)*pow(z,2)*CF*pow(opx,-1)\
           - 8*Li2( - x)*x*CF + 16*Li2( - x)*x*z*CF + 4*Li2( - x*z)*pow(x,-1)*z*CF*pow(opx,-1) - 4*Li2(\
           - x*z)*pow(x,-1)*z*CF - 8*Li2( - x*z)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 8*Li2( - x*z)*pow(\
          x,-1)*pow(z,2)*CF + 4*Li2( - x*z)*z*CF*pow(opx,-1) - 8*Li2( - x*z)*pow(z,2)*CF*pow(opx,-1) - \
          16*Li2( - x*z)*x*pow(z,2)*CF + 8*Li2(x)*pow(x,-1)*z*CF*pow(opx,-1) - 8*Li2(x)*pow(x,-1)*z*CF\
           - 16*Li2(x)*pow(x,-1)*pow(z,2)*CF*pow(opx,-1) + 16*Li2(x)*pow(x,-1)*pow(z,2)*CF + 8*Li2(x)*z\
          *CF*pow(opx,-1) - 16*Li2(x)*pow(z,2)*CF*pow(opx,-1) + 8*Li2(x)*x*z*CF - 16*Li2(x)*x*pow(z,2)*\
          CF - 4*Li2(z)*x*CF + 8*Li2(z)*x*z*CF
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
