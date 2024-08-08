import numpy as np
import warnings
from scipy import integrate
from core.interpolation import point_interpolator, compute_basis_functions, interpolator

from scipy.integrate import IntegrationWarning

# Ignore the specific IntegrationWarning
warnings.filterwarnings("ignore", category=IntegrationWarning)

eps_integration_border = 1e-10

eps_integration_abs = 1e-13

class conv1:
    
    def __init__(self, x, coeff_func, itp_xgrid, mode_log=True, coeff_map=None):
        self.x = x
        self.coeff_func = coeff_func
        self.itp_xgrid = itp_xgrid
        self.mode_log = mode_log
        self.basis_functions = compute_basis_functions(self.itp_xgrid, 4, self.mode_log)
        self.interpolator_at_x = interpolator(self.x, self.basis_functions)
        if coeff_map is None:
            self.coeff_map = {'r': 1, 's': 1, 'l': 1}
        else:
            self.coeff_map = coeff_map
  
    # def integrand(self, xhat, j):
    #     return (self.coeff_func(xhat, 'r') * point_interpolator(self.x/xhat, self.basis_functions, j) / xhat
    #             + self.coeff_func(xhat, 's') * (point_interpolator(self.x/xhat, self.basis_functions, j) / xhat - self.interpolator_at_x[j]))

    def integrand_r(self, xhat, j):
        return self.coeff_func(xhat, 'r') * point_interpolator(self.x/xhat, self.basis_functions, j)/xhat
    
    def integrand_s(self, xhat, j):
        return self.coeff_func(xhat, 's') * (point_interpolator(self.x/xhat, self.basis_functions, j)/xhat - self.interpolator_at_x[j])
    
    def evaluate_l(self):
        return [self.coeff_func(self.x, 'l') * self.interpolator_at_x[i] for i in range(len(self.interpolator_at_x))]
    
    def integrator(self):
        res, err = [], []
        for i in range(len(self.basis_functions)):
            res_r, err_r, res_s, err_s = 0, 0, 0, 0
            if self.mode_log:
                min_xmin = np.exp(self.basis_functions['p_'+str(i)][0]['xmin'])
                max_xmax = np.exp(self.basis_functions['p_'+str(i)][-1]['xmax'])
            else:
                min_xmin = self.basis_functions['p_'+str(i)][0]['xmin']
                max_xmax = self.basis_functions['p_'+str(i)][-1]['xmax']
            if max_xmax <= self.x:
                for lists in [res, err]:
                    lists.append(0)
            elif min_xmin <= self.x < max_xmax:
                x_intv_low = self.x * (1 + eps_integration_border)
                x_intv_high = max_xmax * (1 - eps_integration_border)
                if self.coeff_map['r'] == 1:
                    res_r, err_r = integrate.quad(self.integrand_r, x_intv_low, x_intv_high, args=(i), epsabs=eps_integration_abs)
                if self.coeff_map['s'] == 1:
                    res_s, err_s = integrate.quad(self.integrand_s, x_intv_low, x_intv_high, args=(i), epsabs=eps_integration_abs)
                res.append(res_r + res_s)
                err.append(err_r + err_s)
            else:
                x_intv_low = min_xmin * (1 + eps_integration_border)
                x_intv_high = max_xmax * (1 - eps_integration_border)
                if self.coeff_map['r'] == 1:
                    res_r, err_r = integrate.quad(self.integrand_r, x_intv_low, x_intv_high, args=(i), epsabs=eps_integration_abs)
                if self.coeff_map['s'] == 1:
                    res_s, err_s = integrate.quad(self.integrand_s, x_intv_low, x_intv_high, args=(i), epsabs=eps_integration_abs)
                res.append(res_r + res_s)
                err.append(err_r + err_s)

        return res, err
    
    
    def convolution(self):
        res, err = self.integrator()
        if self.coeff_map['l'] == 1:
            loc_res = self.evaluate_l()
            res = [res[i] + loc_res[i] for i in range(len(res))]
        return res, err
    
    def __call__(self):
        return self.convolution()

class conv2:

    def __init__(self, x, z, coeff_func, sv_order, itp_xgrid, itp_zgrid, mode_log=True, coeff_map=None):
        self.x = x
        self.z = z
        self.coeff_func = coeff_func
        self.sv_order = sv_order
        self.itp_xgrid = itp_xgrid
        self.itp_zgrid = itp_zgrid
        self.mode_log = mode_log
        self.basis_functions_x = compute_basis_functions(self.itp_xgrid, 4, self.mode_log)
        self.basis_functions_z = compute_basis_functions(self.itp_zgrid, 4, self.mode_log)
        self.interpolator_at_x = interpolator(self.x, self.basis_functions_x)
        self.interpolator_at_z = interpolator(self.z, self.basis_functions_z)
        if coeff_map is None:
            self.coeff_map = {'rr': ['000'], 'rs': ['000'], 'rl': ['000'], 'sr': ['000'], 'ss': ['000'], 'sl': ['000'], 'lr': ['000'], 'ls': ['000'], 'll': ['000']}
        else:
            self.coeff_map = coeff_map

    def integrand_rr(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'rr', self.sv_order).real * point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat * point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat
    
    def integrand_rs(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'rs', self.sv_order).real * point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat * (point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat - self.interpolator_at_z[k])
    
    def integrand_rl(self, xhat, j, k):
        return self.coeff_func(xhat, self.z, 'rl', self.sv_order).real * point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat * self.interpolator_at_z[k]
    
    def integrand_sr(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'sr', self.sv_order).real * (point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat - self.interpolator_at_x[j]) * point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat
    
    def integrand_ss(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'ss', self.sv_order).real * (point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat - self.interpolator_at_x[j]) * (point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat - self.interpolator_at_z[k])
    
    def integrand_sl(self, xhat, j, k):
        return self.coeff_func(xhat, self.z, 'sl', self.sv_order).real * (point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat - self.interpolator_at_x[j]) * self.interpolator_at_z[k]
    
    def integrand_lr(self, zhat, j, k):
        return self.coeff_func(self.x, zhat, 'lr', self.sv_order).real * self.interpolator_at_x[j] * point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat
    
    def integrand_ls(self, zhat, j, k):
        return self.coeff_func(self.x, zhat, 'ls', self.sv_order).real * self.interpolator_at_x[j] * (point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat - self.interpolator_at_z[k])
    
    def evaluate_ll(self):
        return [[self.coeff_func(self.x, self.z, 'll', self.sv_order).real * self.interpolator_at_x[j] * self.interpolator_at_z[k] for j in range(len(self.interpolator_at_x))] for k in range(len(self.interpolator_at_z))]
    
    def integrator(self):
        res = [[] for _ in range(len(self.basis_functions_z))]
        err = [[] for _ in range(len(self.basis_functions_z))]
        for i in range(len(self.basis_functions_z)):
            for j in range(len(self.basis_functions_x)):
                res_rr, err_rr, res_rs, err_rs, res_rl, err_rl, res_sr, err_sr, res_ss, err_ss, res_sl, err_sl, res_lr, err_lr, res_ls, err_ls = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                if self.mode_log:
                    min_xmin = np.exp(self.basis_functions_x['p_'+str(j)][0]['xmin'])
                    max_xmax = np.exp(self.basis_functions_x['p_'+str(j)][-1]['xmax'])
                    min_zmin = np.exp(self.basis_functions_z['p_'+str(i)][0]['xmin'])
                    max_zmax = np.exp(self.basis_functions_z['p_'+str(i)][-1]['xmax'])
                else:
                    min_xmin = self.basis_functions_x['p_'+str(j)][0]['xmin']
                    max_xmax = self.basis_functions_x['p_'+str(j)][-1]['xmax']
                    min_zmin = self.basis_functions_z['p_'+str(i)][0]['xmin']
                    max_zmax = self.basis_functions_z['p_'+str(i)][-1]['xmax']
                if max_xmax <= self.x or max_zmax <= self.z:
                    for lists in [res, err]:
                        lists[i].append(0)
                else:
                    if min_zmin <= self.z < max_zmax:
                        if min_xmin <= self.x < max_xmax:
                            x_intv_low = self.x * (1 + eps_integration_border)
                            x_intv_high = max_xmax * (1 - eps_integration_border)
                            z_intv_low = self.z * (1 + eps_integration_border)
                            z_intv_high = max_zmax * (1 - eps_integration_border)
                        else:
                            x_intv_low = min_xmin * (1 + eps_integration_border)
                            x_intv_high = max_xmax * (1 - eps_integration_border)
                            z_intv_low = self.z * (1 + eps_integration_border)
                            z_intv_high = max_zmax * (1 - eps_integration_border)
                    else:
                        if min_xmin <= self.x < max_xmax:
                            x_intv_low = self.x * (1 + eps_integration_border)
                            x_intv_high = max_xmax * (1 - eps_integration_border)
                            z_intv_low = min_zmin * (1 + eps_integration_border)
                            z_intv_high = max_zmax * (1 - eps_integration_border)
                        else:
                            x_intv_low = min_xmin * (1 + eps_integration_border)
                            x_intv_high = max_xmax * (1 - eps_integration_border)
                            z_intv_low = min_zmin * (1 + eps_integration_border)
                            z_intv_high = max_zmax * (1 - eps_integration_border)
                    if self.sv_order in self.coeff_map['rr']:
                        res_rr, err_rr = integrate.dblquad(self.integrand_rr, z_intv_low, z_intv_high, x_intv_low, x_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    if self.sv_order in self.coeff_map['rs']:
                        res_rs, err_rs = integrate.dblquad(self.integrand_rs, z_intv_low, z_intv_high, x_intv_low, x_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    if self.sv_order in self.coeff_map['rl']:
                        res_rl, err_rl = integrate.quad(self.integrand_rl, x_intv_low, x_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    if self.sv_order in self.coeff_map['sr']:
                        res_sr, err_sr = integrate.dblquad(self.integrand_sr, z_intv_low, z_intv_high, x_intv_low, x_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    if self.sv_order in self.coeff_map['ss']:
                        res_ss, err_ss = integrate.dblquad(self.integrand_ss, z_intv_low, z_intv_high, x_intv_low, x_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    if self.sv_order in self.coeff_map['sl']:
                        res_sl, err_sl = integrate.quad(self.integrand_sl, x_intv_low, x_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    if self.sv_order in self.coeff_map['lr']:
                        res_lr, err_lr = integrate.quad(self.integrand_lr, z_intv_low, z_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    if self.sv_order in self.coeff_map['ls']:
                        res_ls, err_ls = integrate.quad(self.integrand_ls, z_intv_low, z_intv_high, args=(j, i), epsabs=eps_integration_abs)
                    res[i].append(res_rr + res_rs + res_rl + res_sr + res_ss + res_sl + res_lr + res_ls)
                    err[i].append(err_rr + err_rs + err_rl + err_sr + err_ss + err_sl + err_lr + err_ls)

        return res, err
    
    def convolution(self):
        res, err = self.integrator()
        if self.sv_order in self.coeff_map['ll']:
            loc_res = self.evaluate_ll()
            res = [[res[i][j] + loc_res[i][j] for j in range(len(res[i]))] for i in range(len(res))]
        return res, err
    
    def __call__(self):
        return self.convolution()
            


