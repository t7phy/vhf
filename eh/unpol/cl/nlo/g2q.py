from configs.eh import *

def cf(x, z, rsl, orders):
    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != round(1 - x, ndecimals):
                result += 8*x*TR - 8*pow(x,2)*TR
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
    (21, 1): charges.d2,
    (21, 2): charges.u2,
    (21, 3): charges.s2,
    (21, 4): charges.c2,
    (21, 5): charges.b2,
    (21, -1): charges.d2,
    (21, -2): charges.u2,
    (21, -3): charges.s2,
    (21, -4): charges.c2,
    (21, -5): charges.b2
}