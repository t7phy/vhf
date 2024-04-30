from core.definitions import CF, TR
from numpy import power as pow
from numpy import log as ln

def cl_nlo_g2q_eq(x, z, orders, rsl):
    
    if orders == '000':
        if rsl == 'rr':
            result = 8*x*TR - 8*pow(x, 2)*TR
        else:
            result = 0
    else:
        result = 0
    
    return result

def cl_nlo_q2g_eq(x, z, orders, rsl):

    if orders == '000':
        if rsl == 'rr':
            result = 4*x*CF - 4*x*z*CF
        else:
            result = 0
    else:
        result = 0
    
    return result

def cl_nlo_q2q_eq(x, z, orders, rsl):

    if orders == '000':
        if rsl == 'rr':
            result = 4*x*z*CF
        else:
            result = 0
    else:
        result = 0

    return result

def ct_nlo_g2q_eq(x, z, orders, rsl):

    omx = 1 - x
    omz = 1 - z

    if orders == '000':
        if rsl == 'rr':
            result = pow(z,-1)*TR - 2*TR - 2*x*pow(z,-1)*TR + 4*x*TR + 2*pow(x,2)*pow(z,-1)*TR - 4*pow(x,2)*TR
        elif rsl == 'rs':
            result_r0 = TR - 2*x*TR + 2*pow(x,2)*TR
            result = result_r0 * 1/(1-z)
        elif rsl == 'rl':
            result = 2*x*TR - 2*pow(x,2)*TR  - ln(x)*TR + 2*ln(x)*x* TR - 2*ln(x)*pow(x,2)*TR + ln(omx)*TR - 2*ln(omx)*x*TR + 2*ln(omx)*pow(x,2)*TR
            result_r0 = TR - 2*x*TR + 2*pow(x,2)*TR
            result = result + result_r0 * ln(1-z)
        else:
            result = 0
    elif orders == '010':
        if rsl == 'rl':
            result = - TR + 2*x*TR - 2*pow(x,2)*TR
        else:
            result = 0
    else:
        result = 0

    return result

def ct_nlo_q2g_eq(x, z, orders, rsl):

    omx = 1 - x
    omz = 1 - z

    if orders == '000':
        if rsl == 'rr':
            result = - pow(z,-1)*CF + 2*CF - x*pow(z,-1)*CF + 2*x*CF - 2*x*z*CF
        elif rsl == 'sr':
            result_0r = 2*pow(z,-1)*CF - 2*CF + z*CF
            result = result_0r * 1/(1-x)
        elif rsl == 'lr':
            result = z*CF + 2*ln(z)*pow(z,-1)*CF - 2*ln(z)*CF + ln(z)*z*CF + 2*ln(omz)*pow(z,-1)*CF - 2*ln(omz)*CF + ln(omz)*z*CF
            result_0r = 2*pow(z,-1)*CF - 2*CF + z*CF
            result = result + result_0r * ln(1-x)
        else:
            result = 0
    elif orders == '001':
        if rsl == 'lr':
            result = - 2*pow(z,-1)*CF + 2*CF - z*CF
        else:
            result = 0
    else:
        result = 0

    return result

def ct_nlo_q2q_eq(x, z, orders, rsl):

    omx = 1 - x
    omz = 1 - z

    if orders == '000':
        if rsl == 'rr':
            result = 2*CF + 2*x*z*CF
        elif rsl == 'rs':
            result_r0 = - CF - x*CF
            result = result_r0 * 1/(1-z)
        elif rsl == 'rl':
            result = CF - x*CF - 2*ln(x)*CF*pow(omx,-1) + ln(x)*CF + ln(x)*x*CF - ln(omx)* \
      CF - ln(omx)*x*CF
            result_r0 = - CF - x*CF
            result = result + result_r0 * ln(1-z)
        elif rsl == 'sr':
            result_0r = - CF - z*CF
            result = result_0r * 1/(1-x)
        elif rsl == 'sl':
            result_1l = 2*CF
            result = result_1l * ln(1-x)/(1-x)
        elif rsl == 'lr':
            result = CF - z*CF + 2*ln(z)*CF*pow(omz,-1) - ln(z)*CF - ln(z)*z*CF - ln(omz)*CF - ln(omz)*z*CF
            result_0r = - CF - z*CF
            result = result + result_0r * ln(1-x)
        elif rsl == 'ls':
            result_l1 = 2*CF 
            result = result_l1 * ln(1-z)/(1-z)
        elif rsl == 'll':
            result = - 8*CF  
            result_1l = 2*CF
            result_l1 = 2*CF
            result = result + result_1l * (1/2)*ln(1-x)*ln(1-x) + result_l1 * (1/2)*ln(1-z)*ln(1-z)
        else:
            result = 0
    elif orders == '001':
        if rsl == 'lr':
            result = CF + z*CF
        elif rsl == 'ls':
            result_l0 = - 2*CF
            result = result_l0 * 1/(1-z)
        elif rsl == 'll':
            result = - 3./2.*CF
            result_l0 = - 2*CF
            result = result + result_l0 * ln(1-z)
        else:
            result = 0
    elif orders == '010':
        if rsl == 'rl':
            result = CF + x*CF 
        elif rsl == 'sl':
            result_0l = - 2*CF
            result = result_0l * 1/(1-x)
        elif rsl == 'll':
            result = - 3./2.*CF
            result_0l = - 2*CF
            result = result + result_0l * ln(1-x)
        else:
            result = 0
    else:
        result = 0

    return result
