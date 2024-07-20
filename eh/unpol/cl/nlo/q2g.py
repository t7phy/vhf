from configs.eh import *

def cf(x, z, rsl, orders):
    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != round(1 - x, ndecimals):
                result += 4*x*CF - 4*x*z*CF
        return result
    elif rsl == 'rs':
        result = 0
        return result
    elif rsl == 'rl':
        result = 0
        return result
    elif rsl == 'sr':
        result = 0
        return result
    elif rsl == 'ss':
        result = 0
        return result
    elif rsl == 'sl':
        result = 0
        return result
    elif rsl == 'lr':
        result = 0
        return result
    elif rsl == 'ls':
        result = 0
        return result
    elif rsl == 'll':
        result = 0
        return result
    else:
        raise ValueError('Invalid rsl value')
    
channel_map = {
    (1, 21): charges.d2,
    (2, 21): charges.u2,
    (3, 21): charges.s2,
    (4, 21): charges.c2,
    (5, 21): charges.b2,
    (-1, 21): charges.d2,
    (-2, 21): charges.u2,
    (-3, 21): charges.s2,
    (-4, 21): charges.c2,
    (-5, 21): charges.b2,
}