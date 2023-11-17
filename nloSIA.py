from definitions import CF
from numpy import log as ln
from numpy import power as npp

def C_q_1(z):
    return 0

def C_g_1(z):
    return 2*CF*((1+npp(1-z, 2))/z)*ln((1-z)*npp(z, 2)-2*(1-z)/z)

def C_q_L(z):
    return CF

def C_g_L(z):
    return 4*CF*(1-z)/z

def del_C_q_1(z):
    return C_q_1(z) - CF*(1-z)

def del_C_g_1(z):
    return 2*CF*((2-z)*ln(npp(z, 2)*(1-z))-4+3*z)

def del_C_q_3(z):
    return C_q_1(z)

def del_C_q_L(z):
    return C_q_L(z)
