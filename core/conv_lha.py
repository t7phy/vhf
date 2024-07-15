import numpy as np
from scipy import integrate
import lhapdf

eps_integration_border = 1e-10

eps_integration_abs = 1e-13

class conv1:

    def __init__(self, x, q2, coeff_func, pdf, pdf_pid, coeff_map=None):
        self.x = x
        self.q2 = q2
        self.f = coeff_func
        self.pdf = pdf
        self.ppid = pdf_pid
        if coeff_map is None:
            self.coeff_map = {'r': ['000'], 's': ['000'], 'l': ['000']}
        else:
            self.coeff_map = coeff_map
        self.sv_order = '000'

class conv2:

    def __init__(self, x, z, q2, coeff_func, pdf, ff, pdf_pid, ff_pid, coeff_map=None):
        self.x = x
        self.z = z
        self.q2 = q2
        self.f = coeff_func
        self.pdf = pdf
        self.ff = ff
        self.ppid = pdf_pid
        self.fpid = ff_pid
        if coeff_map is None:
            self.coeff_map = {'rr': ['000'], 'rs': ['000'], 'rl': ['000'], 'sr': ['000'], 'ss': ['000'], 'sl': ['000'], 'lr': ['000'], 'ls': ['000'], 'll': ['000']}
        else:
            self.coeff_map = coeff_map
        self.sv_order = '000'

    def integrand_rr(self, xhat, zhat):
        print(xhat, zhat)
        return self.f(xhat, zhat, 'rr', self.sv_order).real * self.pdf.xfxQ2(self.ppid, self.x/xhat, self.q2)/xhat * self.ff.xfxQ2(self.fpid, self.z/zhat, self.q2)/zhat

    def integrand_rs(self, xhat, zhat):
        return self.f(xhat, zhat, 'rs', self.sv_order).real * self.pdf.xfxQ2(self.ppid, self.x/xhat, self.q2)/xhat * (self.ff.xfxQ2(self.fpid, self.z/zhat, self.q2)/zhat - self.ff.xfxQ2(self.fpid, self.z, self.q2))

    def integrand_rl(self, xhat):
        return self.f(xhat, self.z, 'rl', self.sv_order).real * self.pdf.xfxQ2(self.ppid, self.x/xhat, self.q2)/xhat * self.ff.xfxQ2(self.fpid, self.z, self.q2)

    def integrand_sr(self, xhat, zhat):
        return self.f(xhat, zhat, 'sr', self.sv_order).real * (self.pdf.xfxQ2(self.ppid, self.x/xhat, self.q2)/xhat - self.pdf.xfxQ2(self.ppid, self.x, self.q2)) * self.ff.xfxQ2(self.fpid, self.z/zhat, self.q2)/zhat
    
    def integrand_ss(self, xhat, zhat):
        return self.f(xhat, zhat, 'ss', self.sv_order).real * (self.pdf.xfxQ2(self.ppid, self.x/xhat, self.q2)/xhat - self.pdf.xfxQ2(self.ppid, self.x, self.q2)) * (self.ff.xfxQ2(self.fpid, self.z/zhat, self.q2)/zhat - self.ff.xfxQ2(self.fpid, self.z, self.q2))

    def integrand_sl(self, xhat):
        return self.f(xhat, self.z, 'sl', self.sv_order).real * (self.pdf.xfxQ2(self.ppid, self.x/xhat, self.q2)/xhat - self.pdf.xfxQ2(self.ppid, self.x, self.q2)) * self.ff.xfxQ2(self.fpid, self.z, self.q2)

    def integrand_lr(self, zhat):
        return self.f(self.x, zhat, 'lr', self.sv_order).real * self.pdf.xfxQ2(self.ppid, self.x, self.q2) * self.ff.xfxQ2(self.fpid, self.z/zhat, self.q2)/zhat

    def integrand_ls(self, zhat):
        return self.f(self.x, zhat, 'ls', self.sv_order).real * self.pdf.xfxQ2(self.ppid, self.x, self.q2) * (self.ff.xfxQ2(self.fpid, self.z/zhat, self.q2)/zhat - self.ff.xfxQ2(self.fpid, self.z, self.q2))

    def ev_ll(self):
        return self.f(self.x, self.z, 'll', self.sv_order).real * self.pdf.xfxQ2(self.ppid, self.x, self.q2) * self.ff.xfxQ2(self.fpid, self.z, self.q2)

    def convolution(self):
        res, err = 0, 0
        x_intv_low = self.x
        x_intv_high = 1 - eps_integration_border
        z_intv_low = self.z
        z_intv_high = 1 - eps_integration_border
        if self.sv_order in self.coeff_map['rr']:
            r, e = integrate.dblquad(self.integrand_rr, z_intv_low, z_intv_high, x_intv_low, x_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['rs']:
            r, e = integrate.dblquad(self.integrand_rs, z_intv_low, z_intv_high, x_intv_low, x_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['rl']:
            r, e = integrate.quad(self.integrand_rl, x_intv_low, x_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['sr']:
            r, e = integrate.dblquad(self.integrand_sr, z_intv_low, z_intv_high, x_intv_low, x_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['ss']:
            r, e = integrate.dblquad(self.integrand_ss, z_intv_low, z_intv_high, x_intv_low, x_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['sl']:
            r, e = integrate.quad(self.integrand_sl, x_intv_low, x_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['lr']:
            r, e = integrate.quad(self.integrand_lr, z_intv_low, z_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['ls']:
            r, e = integrate.quad(self.integrand_ls, z_intv_low, z_intv_high, epsabs=eps_integration_abs)
            res += r
            err += e
        if self.sv_order in self.coeff_map['ll']:
            res += self.ev_ll()
        return res, err

    def __call__(self):
        return self.convolution()

