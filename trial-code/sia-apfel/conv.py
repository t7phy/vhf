import coeff
import numpy as np
from eko import interpolation
from scipy import integrate
from interpolation import point_interpolator, compute_basis_functions, interpolator

eps_integration_border = 1e-10

eps_integration_abs = 1e-13

# def intgrd_reg(z, x, is_log, areas, reg, reg_args):
#     if is_log:
#         pdf_at_x_ov_z_div_z = interpolation.log_evaluate_x(x/z, areas)/z
#     else:
#         pdf_at_x_ov_z_div_z = interpolation.evaluate_x(x/z, areas)/z

#     reg_integrand = reg(z, reg_args) * pdf_at_x_ov_z_div_z
#     return reg_integrand

# def intgrd_sing(z, x, is_log, areas, sing, sing_args, pdf_at_x):
#     if is_log:
#         pdf_at_x_ov_z_div_z = interpolation.log_evaluate_x(x/z, areas)/z
#     else:
#         pdf_at_x_ov_z_div_z = interpolation.evaluate_x(x/z, areas)/z

#     sing_integrand = sing(z, sing_args) * (pdf_at_x_ov_z_div_z - pdf_at_x)
#     return sing_integrand
def integrand_reg(z, x, basis_functions, j, reg, *reg_args):
    intgrd = reg(z, *reg_args) * point_interpolator(x/z, basis_functions, j)/z
    return intgrd

def integrand_sing(z, x, basis_functions, j, interpolator_at_x, sing, *sing_args):
    intgrd = sing(z, *sing_args) * (point_interpolator(x/z, basis_functions, j)/z - interpolator_at_x[j])
    return intgrd

def integrator(x, basis_functions, integration_func, *func_args):
    res, err = [], []
    for i in range(len(basis_functions)):
        if np.exp(basis_functions['p_'+str(i)][-1]['xmax']) <= x:
            res.append(0)
            err.append(0)
        elif np.exp(basis_functions['p_'+str(i)][0]['xmin']) <= x < np.exp(basis_functions['p_'+str(i)][-1]['xmax']):
            z_min = x * (1 + eps_integration_border)
            z_max = np.exp(basis_functions['p_'+str(i)][-1]['xmax']) * (1 - eps_integration_border)
            r, e = integrate.quad(integrand_reg, z_min, z_max, args=(x, basis_functions, i, integration_func, *func_args), epsabs=eps_integration_abs)
            res.append(r)
            err.append(e)
        else:
            z_min = np.exp(basis_functions['p_'+str(i)][0]['xmin']) * (1 + eps_integration_border)
            z_max = np.exp(basis_functions['p_'+str(i)][-1]['xmax']) * (1 - eps_integration_border)
            r, e = integrate.quad(integrand_sing, z_min, z_max, args=(x, basis_functions, i, point_interpolator(x, basis_functions, i), integration_func, *func_args), epsabs=eps_integration_abs)
            res.append(r)
            err.append(e)
    return res, err

def evaluate_loc(x, interpolator_at_x, loc_func, *loc_args):
    res = []
    for i in range(len(interpolator_at_x)):
        res.append(loc_func(x, *loc_args)*interpolator_at_x[i])
    return res
        

    #     area_borders = []
    #     for j in range(len(basis_functions['p_'+str(i)])):
    #         area_borders.append(basis_functions['p_'+str(i)][j]['xmin'])
    #         area_borders.append(basis_functions['p_'+str(i)][j]['xmax'])
    #     breakpoints = x / np.exp(np.unique(area_borders))
    #     print(breakpoints)
    #     #print(max(breakpoints))
    #     z_max = min(max(breakpoints), 1)
    #     z_min = x * (1 + eps_integration_border)
    #     z_max = z_max * (1 - eps_integration_border)
    #     print(z_min, z_max)
    #     r, e = integrate.quad(integrand_reg, z_min, z_max, args=(x, basis_functions, i, integration_func, *func_args), epsabs=eps_integration_abs)
    #     res.append(r)
    #     err.append(e)
    # return res, err

# bfs = compute_basis_functions([0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0], 3)
# print(bfs)
# print(integrate_reg(0.1, bfs, coeff.ct_nlo_q_reg))

# grid = np.unique([0.1, 0.2, 0.3, 0.4, 0.5, 0.6 ,0.7, 0.8, 1.0])
# print(0.2/grid)
# print(0.2, min(max(0.2/grid), 1))

# print(interpolator(0.01, bfs))