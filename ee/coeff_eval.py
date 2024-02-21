from . import coeff
from core.conv import convolution, evaluate_loc
from core.interpolation import compute_basis_functions, interpolator
from eko.interpolation import lambertgrid

def eval_c2_lo(x, interpolator_at_x):
    res_q = evaluate_loc(x, interpolator_at_x, coeff.c2_lo_q_loc)
    return res_q

def eval_c2_nlo(x, mode_log, basis_functions, interpolator_at_x):
    res_q, err_q = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nlo_q_reg, coeff.c2_nlo_q_sing, coeff.c2_nlo_q_loc)
    res_g, err_g = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nlo_g_reg)
    return res_q, err_q, res_g, err_g

def eval_c2_nnlo(x, mode_log, basis_functions, interpolator_at_x, NF):
    res_ns, err_ns = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nnlo_ns_reg, coeff.c2_nnlo_ns_sing, coeff.c2_nnlo_ns_loc, NF)
    res_ps, err_ps = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nnlo_ps_reg, None, None, NF)
    res_g, err_g = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nnlo_g_reg, None, None, NF)
    return res_ns, err_ns, res_ps, err_ps, res_g, err_g

def eval_c2(order, x, mode_log, basis_functions, interpolator_at_x, NF):
    if order not in ['lo', 'nlo', 'nnlo']:
        raise ValueError('Order must be one of lo, nlo, nnlo')
    res_dict = {}
    filler_arr = [0 for _ in range(len(basis_functions))]
    if order in ['lo', 'nlo', 'nnlo']:
        res_dict['lo_ns'] = eval_c2_lo(x, interpolator_at_x)
        res_dict['lo_ps'] = filler_arr
        res_dict['lo_g'] = filler_arr
    if order in ['nlo', 'nnlo']:
        res_dict['nlo_ns'], _, res_dict['nlo_g'], _ = eval_c2_nlo(x, mode_log, basis_functions, interpolator_at_x)
        res_dict['nlo_ps'] = filler_arr
    if order in ['nnlo']:
        res_dict['nnlo_ns'], _, res_dict['nnlo_ps'], _, res_dict['nnlo_g'], _ = eval_c2_nnlo(x, mode_log, basis_functions, interpolator_at_x, NF)
    return res_dict

xgrid = lambertgrid(50, 0.001, 1)  #[0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 0.9]
bf = compute_basis_functions(xgrid, 4)
x = 0.15
interpolator_at_x = interpolator(x, bf)
c2test = eval_c2('nnlo', x, True, bf, interpolator_at_x, 5)
print(c2test)

