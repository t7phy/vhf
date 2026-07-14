import numpy as np
from scipy.integrate import quad, dblquad, nquad
from test_interpolation import lambertgrid, compute_basis_functions, interpolator, integration_regions, point_interpolator

CF = 4/3
z2 = 1.644934066
xgrid_itp = lambertgrid(100, 1e-5, 1)
eps_integration_border = 1e-10

def r_00(x, nf=3):
    return CF*( - 2. * (1. + x) * np.log((1. - x) / x) - 4. * np.log(x) / (1. - x) + 6. + 4. * x)

def s_00(x, nf=3):
    return (-3. * CF)/(1. - x) + (4. * CF) * np.log(1. - x) / (1. - x)

def l_00(x, nf=3):
    return - CF * (9. + 4. * z2) + (-3. * CF) * np.log(1. - x) + (4. * CF) * pow(np.log(1. - x), 2)/2

c2 = {
    "r": r_00,
    "s": s_00,
    "l": l_00
}

def xfxQ2(pid, x, Q2=2):
    if pid == 3 or pid == -3:
        return 0.2 * (xfxQ2(-1, x, Q2) + xfxQ2(-2, x, Q2))
    elif pid == -2:
        return xfxQ2(-1, x, Q2) * (1 - x)
    elif pid == -1:
        return  0.1939875 * pow(x, -0.1) * pow(1 - x, 6)
    elif pid == 0 or pid == 21:
        return 1.7 * pow(x, -0.1) * pow(1 - x, 5)
    elif pid == 1:
        return  3.064320 * pow(x, 0.8) * pow(1 - x, 4) + xfxQ2(-1, x, Q2)
    elif pid == 2:
        return  5.107200 * pow(x, 0.8) * pow(1 - x, 3) + xfxQ2(-2, x, Q2)
    else:
        raise NotImplementedError("PID not implemented")
    

    
alpha_s = 0.35
a_s = alpha_s / (4. * np.pi)

class pointwise_trad:
    def __init__(self, x, pid):
        self.x = x
        self.pid = pid

    def fxQ2(self, x, Q2=2):
        return xfxQ2(self.pid, x, Q2) / x

    def integrand(self, xhat):
        return r_00(xhat) * self.fxQ2(self.x / xhat) / xhat + s_00(xhat) * (self.fxQ2(self.x / xhat) / xhat - self.fxQ2(self.x))
    
    def ev_l(self):
        return l_00(self.x) * self.fxQ2(self.x)
    
    def compute(self):
        integral, error = quad(self.integrand, self.x, 1, epsabs=0, epsrel=1e-8)
        return integral + self.ev_l()
    
    def __call__(self):
        return self.compute()
    
class pointwise_hypercube:
    def __init__(self, x, pid):
        self.x = x
        self.pid = pid

    def fxQ2(self, x, Q2=2):
        return xfxQ2(self.pid, x, Q2) / x

    def integrand_hypercube(self, u):
        # 1. Map u in [0, 1] to xhat in [x, 1]
        xhat = self.x + (1 - self.x) * u
        
        # 2. Calculate the original functional value
        # (Using your original logic)
        term1 = r_00(xhat) * self.fxQ2(self.x / xhat) / xhat
        term2 = s_00(xhat) * (self.fxQ2(self.x / xhat) / xhat - self.fxQ2(self.x))
        
        f_val = term1 + term2
        
        # 3. Multiply by the Jacobian (1 - x)
        return f_val * (1 - self.x)
    
    def ev_l(self):
        return l_00(self.x) * self.fxQ2(self.x)
    
    def compute(self):
        # Now the limits are strictly 0 and 1
        integral, error = quad(self.integrand_hypercube, 0, 1, epsabs=0, epsrel=1e-8)
        return integral + self.ev_l()
    
    def __call__(self):
        return self.compute()
    
class pointwise_hypercube_grid:

    def __init__(self, x, itp_xgrid, mode_log=True):
        self.x = x
        self.itp_xgrid = itp_xgrid
        self.mode_log = mode_log
        self.basis_functions = compute_basis_functions(itp_xgrid, 4, mode_log=mode_log)
        self.interpolator_at_x = interpolator(self.x, self.basis_functions)
        self.integration_regions = integration_regions(self.x, itp_xgrid)

    def integrand_hypercube(self, u, xnode, a, b, coeff_func):
        res = 0.
        xhat = a + (b - a) * u
        if "r" in coeff_func:            
            res += coeff_func["r"](xhat) * point_interpolator(self.x / xhat, self.basis_functions, xnode, mode_log=self.mode_log) / xhat
        if "s" in coeff_func:
            res += coeff_func["s"](xhat) * (point_interpolator(self.x / xhat, self.basis_functions, xnode, mode_log=self.mode_log) / xhat - self.interpolator_at_x[xnode])
        return res * (b - a)
    
    def ev_l(self, xnode):
        return l_00(self.x) * self.interpolator_at_x[xnode]
    
    def compute(self):
        grid = []
        for xnode in range(len(self.itp_xgrid)):
            # print("Computing node ", xnode, " at x = ", self.itp_xgrid[xnode])
            res = 0.
            max_xmax = self.basis_functions['p_'+str(xnode)][-1]['xmax']
            if self.mode_log:
                max_xmax = np.exp(max_xmax)
            if self.x >= (1 - eps_integration_border) or max_xmax <= self.x:
                grid.append(0.)
            else:
                for i in self.integration_regions:
                    x_intv_low = i[0] * (1 + eps_integration_border)
                    x_intv_high = i[1] * (1 - eps_integration_border)
                    res += quad(self.integrand_hypercube, 0, 1, args=(xnode, x_intv_low, x_intv_high), epsabs=0, epsrel=1e-8)[0]
                res += self.ev_l(xnode)
                grid.append(res)
        return grid
    
    def __call__(self):
        return self.compute()
    
class conv_1d_grid:

    def __init__(self, x, itp_xgrid, coeff_func, mode_log=True):
        self.x = x
        self.itp_xgrid = itp_xgrid
        self.coeff_func = coeff_func
        self.mode_log = mode_log
        self.basis_functions = compute_basis_functions(itp_xgrid, 4, mode_log=mode_log)
        self.interpolator_at_x = interpolator(self.x, self.basis_functions)
        self.integration_regions = integration_regions(self.x, itp_xgrid)
    
    def compute(self):
        grid = []
        has_r = "r" in self.coeff_func
        has_s = "s" in self.coeff_func
        c_r = self.coeff_func.get("r")
        c_s = self.coeff_func.get("s")
        def optimized_integrand(u, xnode, a, b):
            xhat = a + (b - a) * u
            res = 0.
            
            # Pre-calculate common terms
            interp_val = point_interpolator(self.x / xhat, self.basis_functions, xnode, mode_log=self.mode_log)
            term_val = interp_val / xhat
            
            if has_r:
                res += c_r(xhat) * term_val
            if has_s:
                res += c_s(xhat) * (term_val - self.interpolator_at_x[xnode])
                
            return res * (b - a)
        for xnode in range(len(self.itp_xgrid)):
            # print("Computing node ", xnode, " at x = ", self.itp_xgrid[xnode])
            res = 0.
            max_xmax = self.basis_functions['p_'+str(xnode)][-1]['xmax']
            if self.mode_log:
                max_xmax = np.exp(max_xmax)
            if self.x >= (1 - eps_integration_border) or max_xmax <= self.x:
                grid.append(0.)
            else:
                for i in self.integration_regions:
                    x_intv_low = i[0] * (1 + eps_integration_border)
                    x_intv_high = i[1] * (1 - eps_integration_border)
                    res += quad(optimized_integrand, 0, 1, args=(xnode, x_intv_low, x_intv_high), epsabs=0, epsrel=1e-8)[0]
                if "l" in self.coeff_func:
                    res += self.coeff_func["l"](self.x) * self.interpolator_at_x[xnode]
                grid.append(res)
        return grid
    
    def __call__(self):
        return self.compute()

def pointwise_hypercube_grid_eval(x, pid):
    grid = conv_1d_grid(x, xgrid_itp, c2, mode_log=True)()
    def fxQ2(x_val, Q2=2):
        return xfxQ2(pid, x_val, Q2) / x_val
    pdf_arr = [fxQ2(x_val) for x_val in xgrid_itp]
    result = np.dot(grid, pdf_arr)
    return result

class binwise_trad:
    def __init__(self, pid, xlow, xhigh):
        self.pid = pid
        self.xlow = xlow
        self.xhigh = xhigh

    def fxQ2(self, x, Q2=2):
        return xfxQ2(self.pid, x, Q2) / x

    def main_integrand(self, xhat, x):
        term1 = r_00(xhat) * self.fxQ2(x / xhat) / xhat
        term2 = s_00(xhat) * (self.fxQ2(x / xhat) / xhat - self.fxQ2(x))
        return term1 + term2

    def l_term_integrand(self, x):
        return l_00(x) * self.fxQ2(x)

    def compute(self):
        gfun = lambda x: x
        hfun = lambda x: 1
        
        integral_2d, err_2d = dblquad(
            self.main_integrand, 
            self.xlow, 
            self.xhigh, 
            gfun, 
            hfun, 
            epsrel=1e-8
        )

        integral_l, err_l = quad(
            self.l_term_integrand, 
            self.xlow, 
            self.xhigh, 
            epsrel=1e-8
        )

        return integral_2d + integral_l
    
    def __call__(self):
        return self.compute()    
    
class binwise_hypercube:
    def __init__(self, pid, xlow, xhigh):
        self.pid = pid
        self.xlow = xlow
        self.xhigh = xhigh

    def fxQ2(self, x, Q2=2):
        return xfxQ2(self.pid, x, Q2) / x
    
    def main_integrand(self, xhat, x):
        term1 = r_00(xhat) * self.fxQ2(x / xhat) / xhat
        term2 = s_00(xhat) * (self.fxQ2(x / xhat) / xhat - self.fxQ2(x))
        return term1 + term2

    def l_term_integrand(self, x):
        return l_00(x) * self.fxQ2(x)
    
    def hypercube_2d_integrand(self, v, u):
        # 1. Map u -> x (Outer variable)
        x_range = self.xhigh - self.xlow
        x = self.xlow + x_range * u
        
        # 2. Map v -> xhat (Inner variable, depends on x)
        xhat_range = 1 - x
        xhat = x + xhat_range * v
        
        # 3. Calculate the original function value
        f_val = self.main_integrand(xhat, x)
        
        # 4. Multiply by the Total Jacobian
        # (x_range is J1, xhat_range is J2)
        return f_val * x_range * xhat_range
    
    def compute_hypercube(self):
        # Integral 1: The 2D part (now 0 to 1 for both)
        # Note: dblquad takes (func, outer_low, outer_high, inner_low, inner_high)
        # But inner limits are now constant functions
        integral_2d, _ = dblquad(
            self.hypercube_2d_integrand,
            0, 1,           # u limits
            lambda u: 0,    # v lower limit
            lambda u: 1,    # v upper limit
            epsrel=1e-8
        )
    
        # Integral 2: The 1D part (similar transformation as before)
        x_range = self.xhigh - self.xlow
        def l_integrand_mapped(u):
            x = self.xlow + x_range * u
            return self.l_term_integrand(x) * x_range
    
        integral_l, _ = quad(l_integrand_mapped, 0, 1, epsrel=1e-8)
    
        return integral_2d + integral_l

    def __call__(self):
        return self.compute_hypercube()

# import vegas

# class binwise_vegas:
#     def __init__(self, pid, xlow, xhigh, nitn=10, neval=10000):
#         self.pid = pid
#         self.xlow = xlow
#         self.xhigh = xhigh
#         self.nitn = nitn
#         self.neval = neval

#     def fxQ2(self, x, Q2=2):
#         # We use np.asarray to ensure math operators work element-wise
#         return xfxQ2(self.pid, np.asarray(x), Q2) / x
    
#     def main_integrand(self, xhat, x):
#         term1 = r_00(xhat) * self.fxQ2(x / xhat) / xhat
#         term2 = s_00(xhat) * (self.fxQ2(x / xhat) / xhat - self.fxQ2(x))
#         return term1 + term2

#     def l_term_integrand(self, x):
#         return l_00(x) * self.fxQ2(x)

#     @vegas.batchintegrand
#     def vegas_2d_wrapper(self, y):
#         # y is the [0, 1] hypercube from Vegas
#         x_range = self.xhigh - self.xlow
#         x = self.xlow + x_range * y[:, 0]
        
#         xhat_range = 1 - x
#         xhat = x + xhat_range * y[:, 1]
        
#         # Calculate and multiply by Total Jacobian (J_x * J_xhat)
#         return self.main_integrand(xhat, x) * x_range * xhat_range

#     @vegas.batchintegrand
#     def vegas_l_wrapper(self, y):
#         x_range = self.xhigh - self.xlow
#         x = self.xlow + x_range * y[:, 0]
#         return self.l_term_integrand(x) * x_range

#     def compute(self):
#         integ_2d = vegas.Integrator([[0, 1], [0, 1]])
#         integ_l = vegas.Integrator([[0, 1]])

#         # 1. Integrate 2D part
#         res_2d = integ_2d(self.vegas_2d_wrapper, nitn=self.nitn, neval=self.neval)
        
#         # 2. Integrate 1D part
#         res_l = integ_l(self.vegas_l_wrapper, nitn=self.nitn, neval=self.neval)

#         # Optional: Print summary to see if Chi-squared is near 1.0 (good convergence)
#         # print(res_2d.summary()) 
        
#         return res_2d.mean + res_l.mean

#     def __call__(self):
#         return self.compute()
    
# import matplotlib.pyplot as plt

# def run_convergence_test(pid, xlow, xhigh):
#     eval_counts = [1000, 5000, 10000, 50000, 100000]
#     errors = []
#     results = []

#     for n in eval_counts:
#         # Initialize our class with the current neval
#         calc = binwise_vegas(pid, xlow, xhigh, nitn=10, neval=n)
        
#         # We need the GVar objects to get the error, so we call compute slightly differently
#         # For this test, let's just look at the 2D integral component
#         integ = vegas.Integrator([[0, 1], [0, 1]])
#         res = integ(calc.vegas_2d_wrapper, nitn=10, neval=n)
        
#         results.append(res.mean)
#         errors.append(res.sdev)
#         print(f"N={n}: {res.mean:.6f} +/- {res.sdev:.6f}")

#     # Plotting
#     plt.figure(figsize=(8, 5))
#     plt.loglog(eval_counts, errors, 'o-', label='Measured Error (sdev)')
    
#     # Plot the theoretical 1/sqrt(N) line for comparison
#     theoretical_slope = [errors[0] * np.sqrt(eval_counts[0]) / np.sqrt(n) for n in eval_counts]
#     plt.loglog(eval_counts, theoretical_slope, '--', color='gray', label='Theoretical $1/\sqrt{N}$')
    
#     plt.xlabel('Number of Evaluations (neval)')
#     plt.ylabel('Numerical Uncertainty ($\sigma$)')
#     plt.title('Vegas Convergence Study')
#     plt.legend()
#     plt.grid(True, which="both", ls="-", alpha=0.5)
#     file_name = f"vegas_convergence_pid_{pid}.pdf"
#     plt.savefig(file_name, format='pdf', bbox_inches='tight')
#     print(f"Plot saved as {file_name}")
    
#     plt.close()



if __name__ == "__main__":
    test1 = pointwise_trad(0.2, 1)
    print("Result (traditional): ", test1())
    # test2 = pointwise_hypercube(0.02, 2)
    # print("Result (hypercube): ", test2())
    # test3 = pointwise_hypercube_grid_eval(0.02, 2)
    # print("Result (hypercube grid): ", test3)
    # print("rel diff tradi vs hypercube_grid: " , abs(test1() - test3) / abs(test1()) * 100, "%")
    print("-----------------------------")
    bin_test1 = binwise_trad(1, 0.001, 0.2)
    print("Bin Result (traditional): ", bin_test1())
    # bin_test2 = binwise_hypercube(2, 0.01, 0.1)
    # print("Bin Result (hypercube): ", bin_test2())
    # bin_test3 = binwise_vegas(2, 0.01, 0.1, nitn=10, neval=1000000)
    # print("Bin Result (vegas): ", bin_test3())
    # print("rel diff scipy vs vegas: " , abs(bin_test2() - bin_test3()) / abs(bin_test2()) * 100, "%") 
    # run_convergence_test(1, 0.01, 0.1)
    

