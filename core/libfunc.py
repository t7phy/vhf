from scipy.integrate import quad
import numpy as np
import scipy as sp
from core.nielsen import nielsen as nl

def atanint(x):
    result, _ = quad(lambda t: np.arctan(t), 0, x)
    return result

def Li2(x):
    result = nl(1, 1, x)
    return result

def Li3(x):
    result = nl(2, 1, x)
    return result

def ln(x):
    if x < 0:
        return np.log(-x) + 1j * np.pi
    else:
        return np.log(x)

def lambertgrid(n_pts, x_min, x_max=1.0):
    
    def direct_relation(x):
        return 5 * (1 - x) - np.log(x)

    def inverse_relation(y):
        return np.real(1 / 5 * sp.special.lambertw(5 * np.exp(5 - y)))

    y_min = direct_relation(x_min)
    y_max = direct_relation(x_max)

    return [inverse_relation(y) for y in np.linspace(y_min, y_max, n_pts)]
