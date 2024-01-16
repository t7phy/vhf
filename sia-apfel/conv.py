
import numpy as np
from eko import interpolation
from scipy import integrate


def intgrd_reg(z, x, is_log, areas, reg, reg_args):
    if is_log:
        pdf_at_x_ov_z_div_z = interpolation.log_evaluate_x(x/z, areas)/z
    else:
        pdf_at_x_ov_z_div_z = interpolation.evaluate_x(x/z, areas)/z

    reg_integrand = reg(z, reg_args) * pdf_at_x_ov_z_div_z
    return reg_integrand

def intgrd_sing(z, x, is_log, areas, sing, sing_args, pdf_at_x):
    if is_log:
        pdf_at_x_ov_z_div_z = interpolation.log_evaluate_x(x/z, areas)/z
    else:
        pdf_at_x_ov_z_div_z = interpolation.evaluate_x(x/z, areas)/z

    sing_integrand = sing(z, sing_args) * (pdf_at_x_ov_z_div_z - pdf_at_x)
    return sing_integrand


