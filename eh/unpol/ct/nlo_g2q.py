from configs.eh import *

def cf(x, z, rsl, orders):

    omx = 1.-x

    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != round(1 - x, ndecimals):
                result += pow(z,-1)*TR - 2*TR - 2*x*pow(z,-1)*TR + 4*x*TR + 2*pow(x,2)*pow(z,-1)*TR - 4*pow(x,2)*TR
        return result
    elif rsl == 'rs':
        if orders == '000':
            result_r0 = TR - 2*x*TR + 2*pow(x,2)*TR
            result += result_r0*1/(1-z)
        result = 0
        return result
    elif rsl == 'rl':
        result = 0
        if orders == '000':
            result += 2*x*TR - 2*pow(x,2)*TR  - ln(x)*TR + 2*ln(x)*x*TR - 2*ln(x)*pow(x,2)*TR + ln(omx)*TR - 2*ln(omx)*x*TR + 2*ln(omx)*pow(x,2)*TR
            result_r0 = TR - 2*x*TR + 2*pow(x,2)*TR
            result += result_r0*ln(1-z)
        elif orders == '010':
            result += - LMUF*TR + 2*LMUF*x*TR - 2*LMUF*pow(x,2)*TR
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
