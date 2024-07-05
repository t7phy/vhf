import numpy as np
from eko import interpolation
from scipy import integrate
from .interpolation import point_interpolator, compute_basis_functions, interpolator

eps_integration_border = 1e-10

eps_integration_abs = 1e-13

def integrand(z, x, basis_functions, j, interpolator_at_x, reg_func, sing_func=None, *func_args):
    intgrd = reg_func(z, *func_args) * point_interpolator(x/z, basis_functions, j)/z
    if sing_func is not None:
        intgrd += sing_func(z, *func_args) * (point_interpolator(x/z, basis_functions, j)/z - interpolator_at_x[j])
    return intgrd

def evaluate_loc(x, interpolator_at_x, loc_func, *loc_args):
    res = []
    for i in range(len(interpolator_at_x)):
        res.append(loc_func(x, *loc_args)*interpolator_at_x[i])
    return res
        
def integrator(x, mode_log, basis_functions, interpolator_at_x, reg_func, sing_func=None, *func_args):
    res, err = [], []
    for i in range(len(basis_functions)):
        if mode_log:
            min_xmin = np.exp(basis_functions['p_'+str(i)][0]['xmin'])
            max_xmax = np.exp(basis_functions['p_'+str(i)][-1]['xmax'])
        else:
            min_xmin = basis_functions['p_'+str(i)][0]['xmin']
            max_xmax = basis_functions['p_'+str(i)][-1]['xmax']
        if max_xmax <= x:
            res.append(0)
            err.append(0)
        elif min_xmin <= x < max_xmax:
            z_min = x * (1 + eps_integration_border)
            z_max = max_xmax * (1 - eps_integration_border)
            r, e = integrate.quad(integrand, z_min, z_max, args=(x, basis_functions, i, interpolator_at_x, reg_func, sing_func, *func_args), epsabs=eps_integration_abs)
            res.append(r)
            err.append(e)
        else:
            z_min = min_xmin * (1 + eps_integration_border)
            z_max = max_xmax * (1 - eps_integration_border)
            r, e = integrate.quad(integrand, z_min, z_max, args=(x, basis_functions, i, interpolator_at_x, reg_func, sing_func, *func_args), epsabs=eps_integration_abs)
            res.append(r)
            err.append(e)
    return res, err

def convolution(x, mode_log, basis_functions, interpolator_at_x, reg_func, sing_func=None, loc_func=None, *func_args):
    res, err = integrator(x, mode_log, basis_functions, interpolator_at_x, reg_func, sing_func, *func_args)
    if loc_func is not None:
        loc_res = evaluate_loc(x, interpolator_at_x, loc_func, *func_args)
        res = [res[i] + loc_res[i] for i in range(len(res))]
    return res, err

