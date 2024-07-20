from configs.eh import *

def ct_nlo_q2q_eq(x, z, rsl, orders):

    omx = 1.-x
    omz = 1.-z

    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != round(1 - x, ndecimals):
                result += 2*CF + 2*x*z*CF
        return result
    elif rsl == 'rs':
        result = 0
        if orders == '000':
            result_r0 = - CF - x*CF
            result += result_r0*1/(1-z)
        return result
    elif rsl == 'rl':
        result = 0
        if orders == '000':
            result += CF - x*CF - 2*ln(x)*CF*pow(omx,-1) + ln(x)*CF + ln(x)*x*CF - ln(omx)*CF - ln(omx)*x*CF
            result_r0 = - CF - x*CF
            result += result_r0*ln(1-z)
        elif orders == '010':
            result += + LMUF*CF + LMUF*x*CF
        return result
    elif rsl == 'sr':
        result = 0
        if orders == '000':
            result_0r = - CF - z*CF
            result += result_0r*1/(1-x)
        return result
    elif rsl == 'ss':
        result = 0
        if orders == '000':
            result_00 = 2*CF
            result += result_00*(1/(1-x))*(1/(1-z))
        return result
    elif rsl == 'sl':
        result = 0
        if orders == '000':
            result_1l = 2*CF
            result += result_1l*ln(1-x)/(1-x)
            result_00 = 2*CF
            result += result_00*(1/(1-x))*(ln(1-z))
        elif orders == '010':
            result_0l = - 2*LMUF*CF
            result += result_0l*1/(1-x)
        return result
    elif rsl == 'lr':
        result = 0
        if orders == '000':
            result += CF - z*CF + 2*ln(z)*CF*pow(omz,-1) - ln(z)*CF - ln(z)*z*CF - ln(omz)*CF - ln(omz)*z*CF
            result_0r = - CF - z*CF
            result += result_0r*ln(1-x)
        elif orders == '001':
            result += + LMUA*CF + LMUA*z*CF
        return result
    elif rsl == 'ls':
        result = 0
        if orders == '000':
            result_l1 = 2*CF
            result += result_l1*ln(1-z)/(1-z)
            result_00 = 2*CF
            result += result_00*(ln(1-x))*(1/(1-z))
        elif orders == '001':
            result_l0 = - 2*LMUA*CF
            result += result_l0*1/(1-z)
        return result
    elif rsl == 'll':
        result = 0
        if orders == '000':
            result += - 8*CF
            result_1l = 2*CF
            result += result_1l*ln(1-x)*ln(1-x)/2
            result_l1 = 2*CF
            result += result_l1*ln(1-z)*ln(1-z)/2
            result_00 = 2*CF
            result += result_00*(ln(1-x))*(ln(1-z))
        elif orders == '001':
            result += - 3./2.*LMUA*CF
            result_l0 = - 2*LMUA*CF
            result += result_l0*ln(1-z)
        elif orders == '010':
            result += - 3./2.*LMUF*CF
            result_0l = - 2*LMUF*CF
            result += result_0l*ln(1-x)
        return result
    else:
        raise ValueError('Invalid rsl value')

channel_map = {
    (1, 1): charges.d2,
    (2, 2): charges.u2,
    (3, 3): charges.s2,
    (4, 4): charges.c2,
    (5, 5): charges.b2,
    (-1, -1): charges.d2,
    (-2, -2): charges.u2,
    (-3, -3): charges.s2,
    (-4, -4): charges.c2,
    (-5, -5): charges.b2
}
