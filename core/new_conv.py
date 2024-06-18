import numpy as np
from scipy import integrate
from .interpolation import point_interpolator, compute_basis_functions, interpolator

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

    def __init__(self, x, z, coeff_func, itp_xgrid, itp_zgrid, mode_log=True, coeff_map=None):
        self.x = x
        self.z = z
        self.coeff_func = coeff_func
        self.itp_xgrid = itp_xgrid
        self.itp_zgrid = itp_zgrid
        self.mode_log = mode_log
        self.basis_functions_x = compute_basis_functions(self.itp_xgrid, 4, self.mode_log)
        self.basis_functions_z = compute_basis_functions(self.itp_zgrid, 4, self.mode_log)
        self.interpolator_at_x = interpolator(self.x, self.basis_functions_x)
        self.interpolator_at_z = interpolator(self.z, self.basis_functions_z)
        if coeff_map is None:
            self.coeff_map = {'rr': 1, 'rs': 1, 'rl': 1, 'sr': 1, 'ss': 1, 'sl': 1, 'lr': 1, 'ls': 1, 'll': 1}
        else:
            self.coeff_map = coeff_map

    def integrand_rr(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'rr') * point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat * point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat
    
    def integrand_rs(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'rs') * point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat * (point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat - self.interpolator_at_z[k])
    
    def integrand_rl(self, xhat, j, k):
        return self.coeff_func(xhat, self.z, 'rl') * point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat * self.interpolator_at_z[k]
    
    def integrand_sr(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'sr') * (point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat - self.interpolator_at_x[j]) * point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat
    
    def integrand_ss(self, xhat, zhat, j, k):
        return self.coeff_func(xhat, zhat, 'ss') * (point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat - self.interpolator_at_x[j]) * (point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat - self.interpolator_at_z[k])
    
    def integrand_sl(self, xhat, j, k):
        return self.coeff_func(xhat, self.z, 'sl') * (point_interpolator(self.x/xhat, self.basis_functions_x, j)/xhat - self.interpolator_at_x[j]) * self.interpolator_at_z[k]
    
    def integrand_lr(self, xhat, zhat, j, k):
        return self.coeff_func(self.x, zhat, 'lr') * self.interpolator_at_x[j] * point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat
    
    def integrand_ls(self, xhat, zhat, j, k):
        return self.coeff_func(self.x, zhat, 'ls') * self.interpolator_at_x[j] * (point_interpolator(self.z/zhat, self.basis_functions_z, k)/zhat - self.interpolator_at_z[k])
    
    def evaluate_ll(self):
        return [[self.coeff_func(self.x, self.z, 'll') * self.interpolator_at_x[j] * self.interpolator_at_z[k] for j in range(len(self.interpolator_at_x))] for k in range(len(self.interpolator_at_z))]
    
    # def integrator(self):
    #     res, err = [[]], [[]]


