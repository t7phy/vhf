from configs.eh import *


def cl_lo_q2q_eq(x, z, rsl, orders):
    return 0

def ct_lo_q2q_eq(x, z, rsl, orders):
    if rsl == 'll' and orders == '000':
        return 1.
    else:
        return 0

def cl_nlo_g2q_eq(x, z, rsl, orders):
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

def cl_nlo_q2g_eq(x, z, rsl, orders):
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

def cl_nlo_q2q_eq(x, z, rsl, orders):
    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != round(1 - x, ndecimals):
                result += 4*x*z*CF
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

def ct_nlo_g2q_eq(x, z, rsl, orders):

    omx = 1.-x

    if rsl == 'rr':
        result = 0
        if orders == '000':
            if z != x and z != round(1 - x, ndecimals):
                result += pow(z,-1)*TR - 2*TR - 2*x*pow(z,-1)*TR + 4*x*TR + 2*pow(x,2)*pow(z,-1)*TR - 4*pow(x,2)*TR
        return result
    elif rsl == 'rs':
        result = 0
        if orders == '000':
            result_r0 = TR - 2*x*TR + 2*pow(x,2)*TR
            result += result_r0*1/(1-z)
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

def ct_nlo_q2g_eq(x, z, rsl, orders):

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
