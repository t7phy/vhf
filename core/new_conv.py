import numpy as np
from scipy import integrate
from .interpolation import point_interpolator, compute_basis_functions, interpolator

eps_integration_border = 1e-10

eps_integration_abs = 1e-13

class conv1:
    
    def __init__(self, x, coeff_func, itp_xgrid, mode_log, coeff_map=None):
        self.x = x
        self.coeff_func = coeff_func
        self.itp_xgrid = itp_xgrid
        self.mode_log = mode_log
        self.basis_functions = compute_basis_functions(self.itp_xgrid, 4, self.mode_log)
        self.interpolator_at_x = interpolator(self.x, self.basis_functions)
        self.coeff_map = coeff_map
  
    def integrand(self, xhat, j):
        return (self.coeff_func(xhat, 'r') * point_interpolator(self.x/xhat, self.basis_functions, j) / xhat
                + self.coeff_func(xhat, 's') * (point_interpolator(self.x/xhat, self.basis_functions, j) / xhat - self.interpolator_at_x[j]))

    # def integrand_r(self, xhat, j):
    #     return self.coeff_func(xhat, 'r') * point_interpolator(self.x/xhat, self.basis_functions, j)/xhat
    
    # def integrand_s(self, xhat, j, interpolator_at_x):
    #     return self.coeff_func(xhat, 's') * (point_interpolator(self.x/xhat, self.basis_functions, j)/xhat - interpolator_at_x[j])
    
    def evaluate_l(self):
        return [self.coeff_func(self.x, 'l') * self.interpolator_at_x[i] for i in range(len(self.interpolator_at_x))]
    
    def integrator(self):
        res, err = [], []
        for i in range(len(self.basis_functions)):
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
                z_min = self.x * (1 + eps_integration_border)
                z_max = max_xmax * (1 - eps_integration_border)
                r, e = integrate.quad(self.integrand, z_min, z_max, args=(i), epsabs=eps_integration_abs)
                # res_r, err_r = integrate.quad(self.integrand_r, z_min, z_max, args=(i), epsabs=eps_integration_abs)
                # res_s, err_s = integrate.quad(self.integrand_s, z_min, z_max, args=(i, interpolator_at_x), epsabs=eps_integration_abs)
                res.append(r)
                err.append(e)
            else:
                z_min = min_xmin * (1 + eps_integration_border)
                z_max = max_xmax * (1 - eps_integration_border)
                r, e = integrate.quad(self.integrand, z_min, z_max, args=(i), epsabs=eps_integration_abs)
                # res_r, err_r = integrate.quad(self.integrand_r, z_min, z_max, args=(i), epsabs=eps_integration_abs)
                # res_s, err_s = integrate.quad(self.integrand_s, z_min, z_max, args=(i, interpolator_at_x), epsabs=eps_integration_abs)
                res.append(r)
                err.append(e)

        return res, err
    
    def convolution(self):
        res, err = self.integrator()
        loc_res = self.evaluate_l()
        res = [res[i] + loc_res[i] for i in range(len(res))]
        return res, err
    
    def __call__(self):
        return self.convolution()  
