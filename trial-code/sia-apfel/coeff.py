from definitions import CA, CF, ZETA2, ZETA3
from numpy import log
from hpl import Hr1, Hr2, Hr3

z2 = ZETA2
z3 = ZETA3


def ct_nlo_q_reg(X): #C2NS1TA(X):
    result = CF * (3*(-1 + X)**2 + 2*(-1 + X**2) * log(1-X) + 4*(1 + X**2)*log(X))/(1-X)
    return result
    
def ct_nlo_q_sing(X): #C2NS1TB(X):    
    result = 2 * CF * ( 2 * log( 1 - X ) - 3 / 2 ) / ( 1 - X )
    return result
    
def ct_nlo_q_loc(X): #C2NS1TC(X):
    result = 2 * CF * ( log( 1 - X )**2 - 3 * log( 1 - X ) / 2 + ( 4 * ZETA2 - 9 / 2 ) )
    return result
    
def ct_nlo_g_reg(X): #C2G1TA(X):
    result = 4 * CF * (2*(-1 + X) + (2 + (X-2)*X)*log(- (X - 1) * X**2))/(X)
    return result
    
def cl_nlo_q_reg(X): #CLNS1TA(X):
    result = 2 * CF
    return result

def cl_nlo_g_reg(X): #CLG1TA(X):
    result = 8 * CF * ( 1 - X ) / X
    return result

def ca_nlo_q_reg(X): #C3NS1TA(X):
    result = 2 * CF * ( - ( 1 + X ) * log( 1 - X ) + 2 * ( 1 + X**2 ) * log(X) / ( 1 - X ) + 1 / 2 - X / 2 )
    return result
    
def ca_nlo_q_sing(X): #C3NS1TB(X): 
    result = 2 * CF * ( 2 * log( 1 - X ) - 3 / 2 ) / ( 1 - X )
    return result
    
def ca_nlo_q_loc(X): #C3NS1TC(X):  
    result = 2 * CF * ( log( 1 - X )**2 - 3 * log( 1 - X ) / 2 + ( 4 * ZETA2 - 9 / 2 ) )
    return result

def ct_nnlo_ns_reg(X, NF): #C2NSP2TA(X, NF):
    DX = 1/X
    DM = 1/(1-X)
    DP = 1/(1+X)
    DL1 = log(1-X)


    CTeq2 = CF*CA * ( 1271/270 + 4829/270*X - 24/5*X**2 + 24/5*DX - 3155/54*DM - 36*z3*X - 28*z3*DP + 28*z3*DM - 4*z2*X + 24/5*z2*X**3 - 12*Hr1(-1, X)*z2 + 20*Hr1(-1, X)*z2*X + 32*Hr1(-1, X)*z2*DP - 359/15*Hr1(0, X) - 143/5*Hr1(0, X)*X - 24/5*Hr1(0, X)*X**2 - 24/5*Hr1(0, X)*DX + 8*Hr1(0, X)*DP + 206/3*Hr1(0, X)*DM + 12*Hr1(0, X)*z2 + 20*Hr1(0, X)*z2*X + 8*Hr1(0, X)*z2*DP - 32*Hr1(0, X)*z2*DM - 25/9*Hr1(1, X) + 311/9*Hr1(1, X)*X - 367/9*Hr1(1, X)*DM + 8*Hr1(1, X)*z2 - 8*Hr1(1, X)*z2*DM - 4*Hr2(-1, 0, X) - 4*Hr2(-1, 0, X)*X + 24/5*Hr2(-1, 0, X)*X**3 + 24/5*Hr2(-1, 0, X)*DX**2 + 11/3*Hr2(0, 0, X) + 23/3*Hr2(0, 0, X)*X - 24/5*Hr2(0, 0, X)*X**3 - 22/3*Hr2(0, 0, X)*DM - 22/3*Hr2(0, 1, X) - 22/3*Hr2(0, 1, X)*X +44/3*Hr2(0, 1, X)*DM + 22/3*Hr2(1, 1, X) + 22/3*Hr2(1, 1, X)*X - 44/3*Hr2(1, 1, X)*DM - 8*Hr2(-1, -1, 0, X) + 24*Hr2(-1, -1, 0, X)*X )
    CTeq2 = CTeq2 + CF*CA * ( 32*Hr2(-1, -1, 0, X)*DP - 16*Hr2(-1, 0, 0, X) + 8*Hr2(-1, 0, 0, X)*X + 24*Hr2(-1, 0, 0, X)*DP + 8*Hr2(-1, 0, 1, X) - 8*Hr2(-1, 0, 1, X)*X - 16*Hr2(-1, 0, 1, X)*DP + 16*Hr2(0, -1, 0, X)*X + 8*Hr2(0, -1, 0, X)*DP - 24*Hr2(0, -1, 0, X)*DM - 36*Hr2(0, 0, 0, X)*X - 36*Hr2(0, 0, 0, X)*DP + 36*Hr2(0, 0, 0, X)*DM - 4*Hr2(0, 0, 1, X) + 4*Hr2(0, 0, 1, X)*X + 8*Hr2(0, 0, 1, X)*DP + 4*Hr2(0, 1, 0, X) + 4*Hr2(0, 1, 0, X)*X - 8*Hr2(0, 1, 0, X)*DM + 4*Hr2(1, 0, 0, X) + 12*Hr2(1, 0, 0, X)*X - 16*Hr2(1, 0, 0, X)*DM - 4*Hr2(1, 0, 1, X) - 4*Hr2(1, 0, 1, X)*X + 8*Hr2(1, 0, 1, X)*DM + 4*Hr2(1, 1, 0, X) + 4*Hr2(1, 1, 0, X)*X - 8*Hr2(1, 1, 0, X)*DM )
    CTeq2 = CTeq2 + CF**2 * ( 279/10 - 279/10*X + 48/5*X**2 - 48/5*DX + 51/2*DM + 56*z3 + 128*z3*X + 56*z3*DP - 152*z3*DM - 24*z2 - 48/5*z2*X**3 + 12*z2*DM + 24*Hr1(-1, X)*z2 - 40*Hr1(-1, X)*z2*X -64*Hr1(-1, X)*z2*DP + 376/5*Hr1(0, X) + 166/5*Hr1(0, X)*X + 48/5*Hr1(0, X)*X**2 + 48/5*Hr1(0, X)*DX - 16*Hr1(0, X)*DP - 106*Hr1(0, X)*DM - 4*Hr1(0, X)*z2 - 20*Hr1(0, X)*z2*X - 16*Hr1(0, X)*z2*DP + 40*Hr1(0, X)*z2*DM + 13*Hr1(1, X) - 51*Hr1(1, X)*X + 27*Hr1(1, X)*DM - 8*Hr1(1, X)*z2 + 8*Hr1(1, X)*z2*X + 8*Hr2(-1, 0, X) + 8*Hr2(-1, 0, X)*X - 48/5*Hr2(-1, 0, X)*X**3 - 48/5*Hr2(-1, 0, X)*DX**2 - 66*Hr2(0, 0, X) - 30*Hr2(0, 0, X)*X + 48/5*Hr2(0, 0, X)*X**3 + 66*Hr2(0, 0, X)*DM + 12*Hr2(0, 1, X) - 4*Hr2(0, 1, X)*X + 12*Hr2(0, 1, X)*DM - 28*Hr2(1, 0, X) + 28*Hr2(1, 0, X)*X + 24*Hr2(1, 0, X)*DM + 16*Hr2(1, 1, X) + 8*Hr2(1, 1, X)*X - 36*Hr2(1, 1, X)*DM + 16*Hr2(-1, -1, 0, X) )
    CTeq2 = CTeq2 + CF**2 * (  - 48*Hr2(-1, -1, 0, X)*X - 64*Hr2(-1, -1, 0, X)*DP + 32*Hr2(-1, 0, 0, X) - 16*Hr2(-1, 0, 0, X)*X - 48*Hr2(-1, 0, 0, X)*DP - 16*Hr2(-1, 0, 1, X) + 16*Hr2(-1, 0, 1, X)*X + 32*Hr2(-1, 0, 1, X)*DP - 32*Hr2(0, -1, 0, X)*X - 16*Hr2(0, -1, 0, X)*DP + 48*Hr2(0, -1, 0, X)*DM + 66*Hr2(0, 0, 0, X) + 138*Hr2(0, 0, 0, X)*X + 72*Hr2(0, 0, 0, X)*DP - 160*Hr2(0, 0, 0, X)*DM - 8*Hr2(0, 0, 1, X) - 24*Hr2(0, 0, 1, X)*X - 16*Hr2(0, 0, 1, X)*DP + 8*Hr2(0, 0, 1, X)*DM + 36*Hr2(0, 1, 0, X) + 36*Hr2(0, 1, 0, X)*X - 72*Hr2(0, 1, 0, X)*DM - 16*Hr2(0, 1, 1, X) - 16*Hr2(0, 1, 1, X)*X + 40*Hr2(0, 1, 1, X)*DM - 12*Hr2(1, 0, 0, X) - 28*Hr2(1, 0, 0, X)*X + 40*Hr2(1, 0, 0, X)*DM - 16*Hr2(1, 0, 1, X) - 16*Hr2(1, 0, 1, X)*X + 32*Hr2(1, 0, 1, X)*DM - 24*Hr2(1, 1, 0, X) - 24*Hr2(1, 1, 0, X)*X + 48*Hr2(1, 1, 0, X)*DM + 24*Hr2(1, 1, 1, X) + 24*Hr2(1, 1, 1, X)*X - 48*Hr2(1, 1, 1, X)*DM )
    CTeq2 = CTeq2 + NF*CF * (  - 59/27 - 17/27*X + 247/27*DM + 10/3*Hr1(0, X) + 6*Hr1(0, X)*X - 32/3*Hr1(0, X)*DM - 14/9*Hr1(1, X) - 26/9*Hr1(1, X)*X + 58/9*Hr1(1, X)*DM - 2/3*Hr2(0, 0, X) - 2/3*Hr2(0, 0, X)*X + 4/3*Hr2(0, 0, X)*DM + 4/3*Hr2(0, 1, X) + 4/3*Hr2(0, 1, X)*X - 8/3*Hr2(0, 1, X)*DM - 4/3*Hr2(1, 1, X) - 4/3*Hr2(1, 1, X)*X + 8/3*Hr2(1, 1, X)*DM )
    
    A3 = 8*CF**2
    A2 = - 22/3*CA*CF - 18*CF**2 + 4/3*CF*NF
    A1 = - 8*z2*CA*CF + 16*z2*CF**2 + 367/9*CA*CF - 27*CF**2 - 58/9*CF*NF
    A0 = 44/3*z2*CA*CF + 40*z3*CA*CF - 8*z3*CF**2 - 3155/54*CA*CF + 51/2*CF**2 + 247/27*CF*NF - 8/3*z2*CF*NF

    CTeq2L = DM * ( DL1**3 * A3 + DL1**2 * A2 + DL1 * A1 + A0) 
    result = CTeq2 - CTeq2L
    return result

def ct_nnlo_ns_sing(X, NF): #C2NS2TB(X, NF):  #### to check: should it be nsp?
    DL1 = log(1-X)
    DM  = 1/(1-X)

    A3 = 8*CF**2
    A2 = - 22/3*CA*CF - 18*CF**2 + 4/3*CF*NF
    A1 = - 8*z2*CA*CF + 16*z2*CF**2 + 367/9*CA*CF - 27*CF**2 - 58/9*CF*NF
    A0 = 44/3*z2*CA*CF + 40*z3*CA*CF - 8*z3*CF**2 - 3155/54*CA*CF + 51/2*CF**2 + 247/27*CF*NF - 8/3*z2*CF*NF

    result = DM * ( DL1**3 * A3 + DL1**2 * A2 + DL1 * A1 + A0)
    return result

def ct_nnlo_nsp_loc(X, NF): #C2NSP2TC(X, NF):
    C2DELT =  CA*CF * ( - 5465/72 + 140/3*z3 + 215/3*z2 - 49/5*z2**2 ) + CF**2 * ( 331/8 - 78*z3 - 39*z2 + 30*z2**2 ) + CF*NF * ( 457/36 + 4/3*z3 - 38/3*z2 )
    DL1 = log(1-X)

    A3 = 8*CF**2
    A2 = - 22/3*CA*CF - 18*CF**2 + 4/3*CF*NF
    A1 = - 8*z2*CA*CF + 16*z2*CF**2 + 367/9*CA*CF - 27*CF**2 - 58/9*CF*NF
    A0 = 44/3*z2*CA*CF + 40*z3*CA*CF - 8*z3*CF**2 - 3155/54*CA*CF + 51/2*CF**2 + 247/27*CF*NF - 8/3*z2*CF*NF

    result =   DL1**4 * A3/4 + DL1**3 * A2/3  + DL1**2 * A1/2 + DL1 * A0 + C2DELT
    return result

def ct_nnlo_ps_reg(X, NF): #C2PS2TA(X, NF):
    DX = 1/X
    cTeqps2 = NF*CF * (  - 118/3 + 70/3*X + 512/27*X**2 - 80/27*DX + 16*z3 + 16*z3*X - 8*z2 - 32*z2*X - 200/3*Hr1(0, X) - 104/3*Hr1(0, X)*X - 128/9*Hr1(0, X)*X**2 - 16/3*Hr1(0, X)*DX + 16*Hr1(0, X)*z2 + 16*Hr1(0, X)*z2*X + 92/3*Hr1(1, X) - 68/3*Hr1(1, X)*X - 32/3*Hr1(1, X)*X**2 + 8/3*Hr1(1, X)*DX - 16*Hr2(-1, 0, X) - 16*Hr2(-1, 0, X)*X - 16/3*Hr2(-1, 0, X)*X**2 - 16/3*Hr2(-1, 0, X)*DX - 14*Hr2(0, 0, X) - 14*Hr2(0, 0, X)*X + 16/3*Hr2(0, 0, X)*X**2 + 64/3*Hr2(0, 0, X)*DX + 4*Hr2(0, 1, X) + 20*Hr2(0, 1, X)*X + 16/3*Hr2(0, 1, X)*X**2 - 32/3*Hr2(0, 1, X)*DX + 4*Hr2(1, 1, X) - 4*Hr2(1, 1, X)*X -16/3*Hr2(1, 1, X)*X**2 + 16/3*Hr2(1, 1, X)*DX + 44*Hr2(0, 0, 0, X) + 44*Hr2(0, 0, 0, X)*X - 24*Hr2(0, 0, 1, X) - 24*Hr2(0, 0, 1, X)*X + 8*Hr2(0, 1, 1, X) + 8*Hr2(0, 1, 1, X)*X )
    result = cTeqps2
    return result

def ct_nnlo_g_reg(X, NF): #C2G2TA(X, NF):
    DX = 1/X

    cTeg2 = CF*CA * (  - 36 - 106*X - 928/27*X**2 + 4438/27*DX + 64*z3 - 136*z3*X - 240*z3*DX + 32*z2 + 64*z2*X - 56*z2*DX + 16*Hr1(-1, X)*z2 + 8*Hr1(-1, X)*z2*X + 32*Hr1(-1, X)*z2*DX + 772/3*Hr1(0, X) + 172/3*Hr1(0, X)*X + 256/9*Hr1(0, X)*X**2 + 496/3*Hr1(0, X)*DX - 128*Hr1(0, X)*z2 - 16*Hr1(0, X)*z2*X + 32*Hr1(0, X)*z2*DX + 236/3*Hr1(1, X) + 4/3*Hr1(1, X)*X + 32/3*Hr1(1, X)*X**2 - 356/3*Hr1(1, X)*DX - 48*Hr1(1, X)*z2 + 24*Hr1(1, X)*z2*X + 32*Hr1(1, X)*z2*DX + 80*Hr2(-1, 0, X) + 56*Hr2(-1, 0, X)*X + 32/3*Hr2(-1, 0, X)*X**2 + 80/3*Hr2(-1, 0, X)*DX - 32*Hr2(0, 0, X) + 4*Hr2(0, 0, X)*X - 32/3*Hr2(0, 0, X)*X**2 - 464/3*Hr2(0, 0, X)*DX - 96*Hr2(0, 1, X) - 16*Hr2(0, 1, X)*X - 32/3*Hr2(0, 1, X)*X**2 + 496/3*Hr2(0, 1, X)*DX - 64*Hr2(1, 0, X) + 8*Hr2(1, 0, X)*X + 64*Hr2(1, 0, X)*DX + 96*Hr2(1, 1, X) - 16*Hr2(1, 1, X)*X + 32/3*Hr2(1, 1, X)*X**2 - 344/3*Hr2(1, 1, X)*DX - 32*Hr2(-1, -1, 0, X) - 16*Hr2(-1, -1, 0, X)*X + 96*Hr2(-1, 0, 0, X) + 48*Hr2(-1, 0, 0, X)*X + 80*Hr2(-1, 0, 0, X)*DX - 32*Hr2(-1, 0, 1, X) - 16*Hr2(-1, 0, 1, X)*X - 32*Hr2(-1, 0, 1, X)*DX + 64*Hr2(0, -1, 0, X) + 32*Hr2(0, -1, 0, X)*X + 64*Hr2(0, -1, 0, X)*DX - 176*Hr2(0, 0, 0, X) - 248*Hr2(0, 0, 0, X)*X - 320*Hr2(0, 0, 0, X)*DX + 128*Hr2(0, 0, 1, X) + 96*Hr2(0, 0, 1, X)*X + 96*Hr2(0, 0, 1, X)*DX + 96*Hr2(0, 1, 0, X) - 48*Hr2(0, 1, 0, X)*X - 96*Hr2(0, 1, 0, X)*DX - 48*Hr2(0, 1, 1, X) - 24*Hr2(0, 1, 1, X)*X - 16*Hr2(0, 1, 1, X)*DX + 64*Hr2(1, 0, 0, X) - 32*Hr2(1, 0, 0, X)*X - 48*Hr2(1, 0, 0, X)*DX - 32*Hr2(1, 0, 1, X) + 16*Hr2(1, 0, 1, X)*X + 32*Hr2(1, 0, 1, X)*DX - 64*Hr2(1, 1, 0, X) + 32*Hr2(1, 1, 0, X)*X + 64*Hr2(1, 1, 0, X)*DX + 16*Hr2(1, 1, 1, X) - 8*Hr2(1, 1, 1, X)*X - 16*Hr2(1, 1, 1, X)*DX )
    cTeg2 = cTeg2 + CF**2 * (  - 604/5 + 154/5*X - 16/5*X**2 + 316/5*DX + 32*z3 - 80*z3*X - 64*z3*DX - 32*z2 - 72*z2*X + 16/5*z2*X**3 + 64*Hr1(-1, X)*z2 + 32*Hr1(-1, X)*z2*X + 32*Hr1(-1, X)*z2*DX + 418/5*Hr1(0, X) - 262/5*Hr1(0, X)*X - 16/5*Hr1(0, X)*X**2 + 144/5*Hr1(0, X)*DX + 32*Hr1(0, X)*z2 - 16*Hr1(0, X)*z2*X + 24*Hr1(1, X)*X - 8*Hr1(1, X)*DX + 80*Hr1(1, X)*z2 - 40*Hr1(1, X)*z2*X - 48*Hr1(1, X)*z2*DX - 64*Hr2(-1, 0, X) - 96*Hr2(-1, 0, X)*X + 16/5*Hr2(-1, 0, X)*X**3 - 64/5*Hr2(-1, 0, X)*DX**2 - 64*Hr2(0, 0, X) + 166*Hr2(0, 0, X)*X - 16/5*Hr2(0, 0, X)*X**3 - 80*Hr2(0, 1, X) + 12*Hr2(0, 1, X)*X + 96*Hr2(0, 1, X)*DX - 16*Hr2(1, 0, X)*X + 112*Hr2(1, 1, X) - 28*Hr2(1, 1, X)*X - 96*Hr2(1, 1, X)*DX + 128*Hr2(-1, -1, 0, X) + 64*Hr2(-1, -1, 0, X)*X + 64*Hr2(-1, -1, 0, X)*DX - 64*Hr2(-1, 0, 0, X) - 32*Hr2(-1, 0, 0, X)*X - 32*Hr2(-1, 0, 0, X)*DX -128*Hr2(0, -1, 0, X) + 88*Hr2(0, 0, 0, X) - 44*Hr2(0, 0, 0, X)*X + 16*Hr2(0, 0, 1, X) - 8*Hr2(0, 0, 1, X)*X - 64*Hr2(0, 0, 1, X)*DX + 64*Hr2(0, 1, 0, X) - 32*Hr2(0, 1, 0, X)*X - 64*Hr2(0, 1, 0, X)*DX - 80*Hr2(0, 1, 1, X) + 40*Hr2(0, 1, 1, X)*X + 96*Hr2(0, 1, 1, X)*DX - 128*Hr2(1, 0, 0, X) + 64*Hr2(1, 0, 0, X)*X + 96*Hr2(1, 0, 0, X)*DX - 48*Hr2(1, 0, 1, X) + 24*Hr2(1, 0, 1, X)*X + 48*Hr2(1, 0, 1, X)*DX - 16*Hr2(1, 1, 0, X) + 8*Hr2(1, 1, 0, X)*X + 16*Hr2(1, 1, 0, X)*DX + 80*Hr2(1, 1, 1, X) - 40*Hr2(1, 1, 1, X)*X - 80*Hr2(1, 1, 1, X)*DX )
    result = cTeg2
    return result
    
def cl_nnlo_nsp_reg(X, NF): #CLNSP2TA(X, NF):
    DX = 1/X

    CLeq2 = CF*CA * ( 1729/45 - 98/15*X - 16/5*X**2 - 24/5*DX + 16*z2*X + 16/5*z2*X**3 - 8*Hr1(-1, X)*z2 - 146/15*Hr1(0, X) + 8/5*Hr1(0, X)*X - 16/5*Hr1(0, X)*X**2 + 24/5*Hr1(0, X)*DX + 46/3*Hr1(1, X) - 8*Hr1(1, X)*z2 + 8*Hr2(-1, 0, X) + 16*Hr2(-1, 0, X)*X + 16/5*Hr2(-1, 0, X)*X**3 - 24/5*Hr2(-1, 0, X)*DX**2 - 16*Hr2(0, 0, X)* - 16/5*Hr2(0, 0, X)*X**3 - 16*Hr2(-1, -1, 0, X) + 8*Hr2(-1, 0, 0, X) + 16*Hr2(0, -1, 0, X) + 8*Hr2(1, 0, 0, X) )
    CLeq2 = CLeq2 + CF**2 * (  - 147/5 - 18/5*X + 32/5*X**2 + 48/5*DX + 4*z2 - 32*z2*X - 32/5*z2*X**3 + 16*Hr1(-1, X)*z2 + 34/5*Hr1(0, X) + 24/5*Hr1(0, X)*X + 32/5*Hr1(0, X)*X**2 - 48/5*Hr1(0, X)*DX - 14*Hr1(1, X) - 4*Hr1(1, X)*X + 16*Hr1(1, X)*z2 - 16*Hr2(-1, 0, X) - 32*Hr2(-1, 0, X)*X - 32/5*Hr2(-1, 0, X)*X**3 + 48/5*Hr2(-1, 0, X)*DX**2 - 12*Hr2(0, 0, X) + 32*Hr2(0, 0, X)*X + 32/5*Hr2(0, 0, X)*X**3 - 4*Hr2(0, 1, X) - 16*Hr2(1, 0, X) + 8*Hr2(1, 1, X) + 32*Hr2(-1, -1, 0, X) - 16*Hr2(-1, 0, 0, X) - 32*Hr2(0, -1, 0, X) - 16*Hr2(1, 0, 0, X) )
    CLeq2 = CLeq2 + NF*CF * (  - 50/9 + 4/3*X + 4/3*Hr1(0, X) - 4/3*Hr1(1, X) )
    result = CLeq2
    return result
    
def cl_nnlo_ps_reg(X, NF): #CLPS2TA(X, NF):
    DX = 1/X
    cLeqps2 = NF*CF * (  - 56/3 + 104/3*X - 8*X**2 - 8*DX + 8*z2 - 16*Hr1(0, X) - 16*Hr1(0, X)*X + 8/3*Hr1(0, X)*X**2 + 32/3*Hr1(0, X)*DX + 8*Hr1(1, X)*X - 8/3*Hr1(1, X)*X**2 - 16/3*Hr1(1, X)*DX + 24*Hr2(0, 0, X) - 8*Hr2(0, 1, X) )
    result = cLeqps2
    return result

def cl_nnlo_g_reg(X, NF): #CLG2TA(X, NF):
    DX = 1/X

    cLeg2 = CF*CA * (  - 320/3 - 160/3*X + 32/3*X**2 +448/3*DX - 64*z2 + 32*z2*DX + 112*Hr1(0, X) + 32*Hr1(0, X)*X - 16/3*Hr1(0, X)*X**2 - 352/3*Hr1(0, X)*DX - 144*Hr1(1, X) - 16*Hr1(1, X)*X + 16/3*Hr1(1, X)*X**2 + 464/3*Hr1(1, X)*DX + 32*Hr2(-1, 0, X) + 32*Hr2(-1, 0, X)*DX - 96*Hr2(0, 0, X) - 128*Hr2(0, 0, X)*DX + 64*Hr2(0, 1, X) + 64*Hr2(1, 0, X) - 64*Hr2(1, 0, X)*DX - 32*Hr2(1, 1, X) + 32*Hr2(1, 1, X)*DX )
    cLeg2 = cLeg2 + CF**2 * ( 24/5 + 248/15*X - 32/15*X**2 - 96/5*DX + 16*z2 + 32/15*z2*X**3 - 8/5*Hr1(0, X) - 224/15*Hr1(0, X)*X - 32/15*Hr1(0, X)*X**2 + 96/5*Hr1(0, X)*DX + 24*Hr1(1, X) + 8*Hr1(1, X)*X - 32*Hr1(1, X)*DX - 32/3*Hr2(-1, 0, X) + 32/15*Hr2(-1, 0, X)*X**3 + 64/5*Hr2(-1, 0, X)*DX**2 + 48*Hr2(0, 0, X) - 32/15*Hr2(0, 0, X)*X**3 - 16*Hr2(0, 1, X) )
    result = cLeg2
    return result

def ca_nnlo_nsp_reg(X, NF): #C3NSP2TA(X, NF):
    DX = 1/X
    DM = 1/(1-X)
    DP = 1/(1+X)
    DL1 = log(1-X)
    CAeq2 = CF*CA * ( 325/54 + 895/54*X - 3155/54*DM - 36*z3 + 28*z3*DP + 28*z3*DM + 12*z2 + 8*z2*X + 8*z2*X**2 + 20*Hr1(-1, X)*z2 - 12*Hr1(-1, X)*z2*X - 32*Hr1(-1, X)*z2*DP + 27*Hr1(0, X) - 193/3*Hr1(0, X)*X - 8*Hr1(0, X)*DP + 206/3*Hr1(0, X)*DM + 20*Hr1(0, X)*z2 + 12*Hr1(0, X)*z2*X - 8*Hr1(0, X)*z2*DP - 32*Hr1(0, X)*z2*DM - 19/9*Hr1(1, X) + 305/9*Hr1(1, X)*X - 367/9*Hr1(1, X)*DM + 8*Hr1(1, X)*z2*X - 8*Hr1(1, X)*z2*DM + 4*Hr2(-1, 0, X) + 4*Hr2(-1, 0, X)*X + 8*Hr2(-1, 0, X)*X**2 + 8*Hr2(-1, 0, X)*DX + 59/3*Hr2(0, 0, X) + 71/3*Hr2(0, 0, X)*X - 8*Hr2(0, 0, X)*X**2 - 22/3*Hr2(0, 0, X)*DM - 46/3*Hr2(0, 1, X) - 46/3*Hr2(0, 1, X)*X + 44/3*Hr2(0, 1, X)*DM + 22/3*Hr2(1, 1, X) + 22/3*Hr2(1, 1, X)*X - 44/3*Hr2(1, 1, X)*DM + 24*Hr2(-1, -1, 0, X) - 8*Hr2(-1, -1, 0, X)*X - 32*Hr2(-1, -1, 0, X)*DP + 8*Hr2(-1, 0, 0, X) - 16*Hr2(-1, 0, 0, X)*X - 24*Hr2(-1, 0, 0, X)*DP - 8*Hr2(-1, 0, 1, X) )
    CAeq2 = CAeq2 + CF*CA * ( 8*Hr2(-1, 0, 1, X)*X + 16*Hr2(-1, 0, 1, X)*DP + 16*Hr2(0, -1, 0, X) - 8*Hr2(0, -1, 0, X)*DP - 24*Hr2(0, -1, 0, X)*DM - 36*Hr2(0, 0, 0, X) + 36*Hr2(0, 0, 0, X)*DP + 36*Hr2(0, 0, 0, X)*DM + 4*Hr2(0, 0, 1, X) - 4*Hr2(0, 0, 1, X)*X - 8*Hr2(0, 0, 1, X)*DP + 4*Hr2(0, 1, 0, X) + 4*Hr2(0, 1, 0, X)*X - 8*Hr2(0, 1, 0, X)*DM + 12*Hr2(1, 0, 0, X) + 4*Hr2(1, 0, 0, X)*X - 16*Hr2(1, 0, 0, X)*DM - 4*Hr2(1, 0, 1, X) - 4*Hr2(1, 0, 1, X)*X + 8*Hr2(1, 0, 1, X)*DM + 4*Hr2(1, 1, 0, X) + 4*Hr2(1, 1, 0, X)*X - 8*Hr2(1, 1, 0, X)*DM)
    CAeq2 = CAeq2 + CF**2 * (  - 19/2 + 19/2*X + 51/2*DM + 128*z3 + 56*z3*X - 56*z3*DP - 152*z3*DM - 52*z2 - 20*z2*X - 16*z2*X**2 + 12*z2*DM - 40*Hr1(-1, X)*z2 + 24*Hr1(-1, X)*z2*X + 64*Hr1(-1, X)*z2*DP - 2*Hr1(0, X) + 92*Hr1(0, X)*X + 16*Hr1(0, X)*DP - 106*Hr1(0, X)*DM - 20*Hr1(0, X)*z2 - 4*Hr1(0, X)*z2*X + 16*Hr1(0, X)*z2*DP + 40*Hr1(0, X)*z2*DM - 5*Hr1(1, X) - 33*Hr1(1, X)*X + 27*Hr1(1, X)*DM + 8*Hr1(1, X)*z2 - 8*Hr1(1, X)*z2*X - 8*Hr2(-1, 0, X) - 8*Hr2(-1, 0, X)*X - 16*Hr2(-1, 0, X)*X**2 - 16*Hr2(-1, 0, X)*DX - 86*Hr2(0, 0, X) - 74*Hr2(0, 0, X)*X + 16*Hr2(0, 0, X)*X**2 + 66*Hr2(0, 0, X)*DM + 32*Hr2(0, 1, X) + 8*Hr2(0, 1, X)*X + 12*Hr2(0, 1, X)*DM - 12*Hr2(1, 0, X) + 12*Hr2(1, 0, X)*X + 24*Hr2(1, 0, X)*DM + 8*Hr2(1, 1, X) + 16*Hr2(1, 1, X)*X - 36*Hr2(1, 1, X)*DM - 48*Hr2(-1, -1, 0, X) + 16*Hr2(-1, -1, 0, X)*X + 64*Hr2(-1, -1, 0, X)*DP - 16*Hr2(-1, 0, 0, X) + 32*Hr2(-1, 0, 0, X)*X + 48*Hr2(-1, 0, 0, X)*DP )
    CAeq2 = CAeq2 + CF**2 * ( 16*Hr2(-1, 0, 1, X) - 16*Hr2(-1, 0, 1, X)*X - 32*Hr2(-1, 0, 1, X)*DP - 32*Hr2(0, -1, 0, X) + 16*Hr2(0, -1, 0, X)*DP + 48*Hr2(0, -1, 0, X)*DM + 138*Hr2(0, 0, 0, X) + 66*Hr2(0, 0, 0, X)*X - 72*Hr2(0, 0, 0, X)*DP - 160*Hr2(0, 0, 0, X)*DM - 24*Hr2(0, 0, 1, X) - 8*Hr2(0, 0, 1, X)*X + 16*Hr2(0, 0, 1, X)*DP + 8*Hr2(0, 0, 1, X)*DM + 36*Hr2(0, 1, 0, X) + 36*Hr2(0, 1, 0, X)*X - 72*Hr2(0, 1, 0, X)*DM - 16*Hr2(0, 1, 1, X) - 16*Hr2(0, 1, 1, X)*X + 40*Hr2(0, 1, 1, X)*DM - 28*Hr2(1, 0, 0, X) - 12*Hr2(1, 0, 0, X)*X + 40*Hr2(1, 0, 0, X)*DM - 16*Hr2(1, 0, 1, X) - 16*Hr2(1, 0, 1, X)*X + 32*Hr2(1, 0, 1, X)*DM - 24*Hr2(1, 1, 0, X) - 24*Hr2(1, 1, 0, X)*X + 48*Hr2(1, 1, 0, X)*DM + 24*Hr2(1, 1, 1, X) + 24*Hr2(1, 1, 1, X)*X - 48*Hr2(1, 1, 1, X)*DM )
    CAeq2 = CAeq2 + NF*CF * ( 55/27 - 131/27*X + 247/27*DM + 2*Hr1(0, X) + 22/3*Hr1(0, X)*X - 32/3*Hr1(0, X)*DM - 2/9*Hr1(1, X) - 38/9*Hr1(1, X)*X + 58/9*Hr1(1, X)*DM - 2/3*Hr2(0, 0, X) - 2/3*Hr2(0, 0, X)*X + 4/3*Hr2(0, 0, X)*DM + 4/3*Hr2(0, 1, X) + 4/3*Hr2(0, 1, X)*X - 8/3*Hr2(0, 1, X)*DM - 4/3*Hr2(1, 1, X) - 4/3*Hr2(1, 1, X)*X + 8/3*Hr2(1, 1, X)*DM )
    
    A3 = 8*CF**2
    A2 = - 22/3*CA*CF - 18*CF**2 + 4/3*CF*NF
    A1 = - 8*z2*CA*CF + 16*z2*CF**2 + 367/9*CA*CF - 27*CF**2 - 58/9*CF*NF
    A0 = 44/3*z2*CA*CF + 40*z3*CA*CF - 8*z3*CF**2 - 3155/54*CA*CF + 51/2*CF**2 + 247/27*CF*NF - 8/3*z2*CF*NF

    CAeq2L = DM * ( DL1**3 * A3 + DL1**2 * A2 + DL1 * A1 + A0 ) 
    result = CAeq2 - CAeq2L
    return result

def ca_nnlo_ns_sing(X, NF): #C3NS2TB(X, NF): ### to check: should it be nsp?
    DL1 = log(1-X)
    DM  = 1/(1-X)
    
    A3 = 8*CF**2
    A2 = - 22/3*CA*CF - 18*CF**2 + 4/3*CF*NF
    A1 = - 8*z2*CA*CF + 16*z2*CF**2 + 367/9*CA*CF - 27*CF**2 - 58/9*CF*NF
    A0 = 44/3*z2*CA*CF + 40*z3*CA*CF - 8*z3*CF**2 - 3155/54*CA*CF + 51/2*CF**2 + 247/27*CF*NF - 8/3*z2*CF*NF

    result = DM * ( DL1**3 * A3 + DL1**2 * A2 + DL1 * A1 + A0)
    return result

def ca_nnlo_nsp_loc(X, NF): #C3NSP2TC(X, NF):
    C2DELT =  CA*CF * ( - 5465/72 + 140/3*z3 + 215/3*z2 - 49/5*z2**2 ) + CF**2 * ( 331/8 - 78*z3 - 39*z2 + 30*z2**2 ) + CF*NF * ( 457/36 + 4/3*z3 - 38/3*z2 )
    DL1 = log(1-X)

    A3 = 8*CF**2
    A2 = - 22/3*CA*CF - 18*CF**2 + 4/3*CF*NF
    A1 = - 8*z2*CA*CF + 16*z2*CF**2 + 367/9*CA*CF - 27*CF**2 - 58/9*CF*NF
    A0 = 44/3*z2*CA*CF + 40*z3*CA*CF - 8*z3*CF**2 - 3155/54*CA*CF + 51/2*CF**2 + 247/27*CF*NF - 8/3*z2*CF*NF

    result = DL1**4 * A3/4 + DL1**3 * A2/3 + DL1**2 * A1/2 + DL1 * A0 + C2DELT
    return result
