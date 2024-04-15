from core.definitions import CA, CF, ZETA2, ZETA3
from numpy import log

############################# NLO COEFFICIENTS #############################

# CT qq

def ct_nlo_qq_rr(x, z):
    result = 2*(1 + x*z)
    return 2 * CF * result

def ct_nlo_qq_rs(x, z):
    result = - (1 + x)/(1 - z)
    return 2* CF * result

def ct_nlo_qq_rl(x, z):
    result = 1 - x - log(x)*(1 + x**2)/(1 - x) - (1 + x)*log(1 - z) + (x**2 - 1)*log(1 - x)/(1 - x)
    return 2 * CF * result

def ct_nlo_qq_sr(x, z):
    result = - (1 + z)/(1 - x)
    return 2* CF * result

def ct_nlo_qq_ss(x, z):
    result = 2/((1 - x)*(1 - z))
    return 2 * CF * result

def ct_nlo_qq_sl(x, z):
    result = 2*log(1 - x)/(1 - x) + 2*log(1 - z)/(1 - x)
    return 2* CF * result

def ct_nlo_qq_lr(x, z):
    result = 1 - z + log(z)*(1 + z**2)/(1 - z) - (1 + z)*log(1 - x) + (z**2 - 1)*log(1 - z)/(1 - z)
    return 2 * CF * result

def ct_nlo_qq_ls(x, z):
    result = 2*log(1 - z)/(1 - z) + 2*log(1 - x)/(1 - z)
    return 2 * CF * result

def ct_nlo_qq_ll(x, z):
    result = -8 + log(1 - x)**2 + log(1 - z)**2
    return 2 * CF * result

# CT gq

def ct_nlo_gq_rr(x, z):
    result = 2*(1 + x - x*z) + (1 + x)/z
    return 2 * CF * result

# def ct_nlo_gq_rs(x, z):
#     result = 2 * CF
#     return result

# def ct_nlo_gq_rl(x, z):
#     result = 2 * CF 
#     return result

def ct_nlo_gq_sr(x, z):
    result = (1 + (1 - z)**2)/(z * (1 - x))
    return 2 * CF * result

# def ct_nlo_gq_ss(x, z):
#     result = 2 * CF
#     return result

# def ct_nlo_gq_sl(x, z):
#     result = 2 * CF
#     return result

def ct_nlo_gq_lr(x, z):
    result = z + (1 + (1 - z)**2) * log(z)/z - (2 + z*(z - 2))*(log(z) - log (z - x*z))/z + log(1 - z)*(-1 + (1 + (1 - z)**2)/z)
    return 2 * CF * result

def ct_nlo_gq_ls(x, z):
    result = log(1 - z)
    return 2 * CF * result

def ct_nlo_gq_ll(x, z):
    result = (z - z**2)*log(1 - z)
    return 2 * CF * result

# CT qg

def ct_nlo_qg_rr(x, z):
    result = (x**2 + (1 - x)**2)/z - 2*(x**2 + (1 - x)**2)
    return result

def ct_nlo_qg_rs(x, z):
    result = (x**2 + (1 - x)**2)/(1 - z)
    return result

def ct_nlo_qg_rl(x, z):
    result = 2*x*(1 - x) - log(x)*(x**2 + (1 - x)**2) + (1 - 2*x + 2*x**2)*log(1 - z) + (x**2 + (1 - x)**2 - 1)*log(1 - x)
    return result

# def ct_nlo_qg_sr(x, z):
#     return

# def ct_nlo_qg_ss(x, z):
#     return

def ct_nlo_qg_sl(x, z):
    result = log(1 - x)
    return result

# def ct_nlo_qg_lr(x, z):
#     return

# def ct_nlo_qg_ls(x, z):
#     return

def ct_nlo_qg_ll(x, z):
    result = (x - x**2) * log(1 - x)
    return result

# CL qq

def cl_nlo_qq_rr(x, z):
    result = 8 * CF * x * z
    return result

# CL gq

def cl_nnlo_gq_rr(x, z):
    result = 8 * CF * x * (1 - z)
    return result

# CL qg

def cl_nlo_qg_rr(x, z):
    result = 8 * x * (1 - x)
    return result