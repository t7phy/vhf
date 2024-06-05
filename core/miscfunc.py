from scipy.integrate import quad
import numpy as np
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
