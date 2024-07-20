from configs.eh import *

def cf(x, z, rsl, orders):

    omz = 1.-z

    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != round(1 - x, ndecimals):
                result += - pow(z,-1)*CF + 2*CF - x*pow(z,-1)*CF + 2*x*CF - 2*x*z*CF
        return result
    elif rsl == 'rs':
        result = 0
        return result
    elif rsl == 'rl':
        result = 0
        return result
    elif rsl == 'sr':
        result = 0
        if orders == '000':
            result_0r = 2*pow(z,-1)*CF - 2*CF + z*CF
            result += result_0r*1/(1-x)
        return result
    elif rsl == 'ss':
        result = 0
        return result
    elif rsl == 'sl':
        result = 0
        return result
    elif rsl == 'lr':
        result = 0
        if orders == '000':
            result += z*CF  + 2*ln(z)*pow(z,-1)*CF - 2*ln(z)*CF + ln(z)*z*CF + 2*ln(omz)*pow(z,-1)*CF - 2*ln(omz)*CF + ln(omz)*z*CF
            result_0r = 2*pow(z,-1)*CF - 2*CF + z*CF
            result += result_0r*ln(1-x)
        elif orders == '001':
            result += - 2*LMUA*pow(z,-1)*CF + 2*LMUA*CF - LMUA*z*CF
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