from core.definitions import CA, CF, ZETA2, ZETA3
from numpy import log
from . import unpol_coeff as uc


############################# NLO COEFFICIENTS #############################

# CT qq

def ct_nlo_qq_rr(x, z):
    delta = -4 * CF * (1 - x) * (1 - z)
    return uc.ct_nlo_qq_rr(x, z) + delta

def ct_nlo_qq_rs(x, z):
    return uc.ct_nlo_qq_rs(x, z)

def ct_nlo_qq_rl(x, z):
    return uc.ct_nlo_qq_rl(x, z)

def ct_nlo_qq_sr(x, z):
    return uc.ct_nlo_qq_sr(x, z)

def ct_nlo_qq_ss(x, z):
    return uc.ct_nlo_qq_ss(x, z)

def ct_nlo_qq_sl(x, z):
    return uc.ct_nlo_qq_sl(x, z)

def ct_nlo_qq_lr(x, z):
    return uc.ct_nlo_qq_lr(x, z)

def ct_nlo_qq_ls(x, z):
    return uc.ct_nlo_qq_ls(x, z)

def ct_nlo_qq_ll(x, z):
    return uc.ct_nlo_qq_ll(x, z)


# CT gq

def ct_nlo_gq_rr(x, z):
    delta = -4 * CF * z * (1 - x)
    return uc.ct_nlo_gq_rr(x, z) + delta

def ct_nlo_gq_sr(x, z):
    return uc.ct_nlo_gq_sr(x, z)

def ct_nlo_gq_lr(x, z):
    return uc.ct_nlo_gq_lr(x, z)

def ct_nlo_gq_ls(x, z):
    return uc.ct_nlo_gq_ls(x, z)

def ct_nlo_gq_ll(x, z):
    return uc.ct_nlo_gq_ll(x, z)


# CT qg

def ct_nlo_qg_rr(x, z):
    result = -2*(2*x - 1) + (2*x - 1)/z
    return result

def ct_nlo_qg_rs(x, z):
    result = (2*x - 1)/(1 - z)
    return result

def ct_nlo_qg_rl(x, z):
    result = 2*(1 - x) - log(x)*(2*x - 1) + (2*x - 1)*log(1 - z) + (2*x - 2)*log(1 - x)
    return result

def ct_nlo_qg_sl(x, z):
    result = log(1 - x)
    return result

def ct_nlo_qg_ll(x, z):
    result = x + (1 - x)*log(1 - x)
    return result
