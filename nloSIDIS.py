from definitions import CF
from numpy import power as npp
from numpy import log as ln

# abreviations

def P_til_qq(a):
    return 0

def P_til_gq(a):
    return (1+npp(1-a, 2))/a

def P_til_qg(a):
    return npp(a, 2) + npp(1-a, 2)

def del_P_til_qg(a):
    return 2-a

def del_P_til_qg(a):
    return 2*a-1

def L_1(a):
    return 0

def L_2(a):
    return (1+npp(a,2))*ln(a)/(1-a)

# coeff. funcs.

def C_qq_1(x, z, M, MF, Q2):
    if x==1:
        d1x = 1
    else:
        d1x = 0
    if z==1:
        d1z = 1
    else:
        d1z = 0
    result = 0
    return result

def C_gq_1(x, z, MF, Q2):
    if x==1:
        d1x = 1
    else:
        d1x = 0
    if z==1:
        d1z = 1
    else:
        d1z = 0
    result = 0
    return result

def C_qg_1(x, z, MF, Q2):
    if x==1:
        d1x = 1
    else:
        d1x = 0
    if z==1:
        d1z = 1
    else:
        d1z = 0
    result = 0
    return result

def C_qq_L(x, z):
    return 4*CF*x*z

def C_gq_L(x, z):
    return 4*CF*x*(1-z)

def C_qg_L(x):
    return 4*x*(1-x)

def del_C_qq_N(x, z, M, MF, Q2):
    return C_qq_1(x, z, M, MF, Q2) - 2*CF*(1-x)*(1-z)

def del_C_gq_N(x, z, MF, Q2):
    return C_gq_1(x, z, MF, Q2) - 2*CF*z*(1-x)

def del_C_qg_N(x, z, M, Q2):
    if x==1:
        d1x = 1
    else:
        d1x = 0
    if z==1:
        d1z = 1
    else:
        d1z = 0
    result = 0
    return result

def del_C_qq_H(x, z, M, MF, Q2):
    if x==1:
        d1x = 1
    else:
        d1x = 0
    result = del_C_qq_N(x, z, M, MF, Q2) + 2*CF*(1-z)*d1x
    return result

def del_C_gq_H(x, z, MF, Q2):
    if x==1:
        d1x = 1
    else:
        d1x = 0
    result = 0
    return result

def del_C_qg_H(x, z, MF, Q2):
    return C_qg_1(x, z, MF, Q2) - P_til_qg(x)*(1-z)/z

def del_C_qq_1NH(x, z, M, MF, Q2):
    if x==1:
        d1x = 1
    else:
        d1x = 0
    result = C_qq_1(x, z, M, MF, Q2) + 2*CF*(1-z)*d1x
    return result

def del_C_gq_1NH(x, z, MF, Q2):
    return del_C_gq_H(x, z, MF, Q2) - 2*CF*z*(1-x)

def del_C_qg_1NH(x, z, M, Q2):
    return del_C_qg_N(x, z, M, Q2) - del_P_til_qg(x)*(1-z)/z

def del_C_qq_LNH(x, z):
    return C_qq_L(x, z)

def del_C_gq_LNH(x, z):
    return -4*CF*x*(1-z)

def del_C_qg_LNH():
    return 0
