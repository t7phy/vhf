from numpy import log, pi, power
from nielsen import nielsen as nl
from scipy.special import zeta


def Hr1(a, x):

    if a == 0:
        result = log(x)
    elif a == 1:
        result = - log(1-x)
    elif a == -1:
        result = log(1+x)
    else:
        raise Exception('wat yu doinnn!!???')

    return result

def Hr2(a, b, x):

    if a == 0 and b == 0:
        result = power(log(x), 2)/2
    elif a == 0 and b == 1:
        result = nl(1, 1, x)
    elif a == 1 and b == 0:
        result = - log(x)*log(1-x) - nl(1, 1, x)
    elif a == 1 and b == 1:
        result = power(log(1-x), 2)/2
    elif a == -1 and b == 0:
        result = log(x)*log(1+x) + nl(1, 1, - x)
    else:
        raise Exception('wwat yu doinnn!!???')

    return result

def Hr3(a, b, c, x):

    if a == -1 and b == -1 and c == 0:
        result = (log(1+x)*(power(pi(), 2) + 3*(- log(-x) + log(x))*log(1+x)) - 6*nl(2, 1, 1+x) + 6*zeta(3))/6
    elif a == -1 and b == 0 and c == 0:
        result = power(log(x), 2)*log(1+x)/2 + log(x)*nl(1, 1, -x) - nl(2, 1, -x)
    elif a == -1 and b == 0 and c == 1:
        result = power(pi(), 2)*log(2)/6 - power(log(2), 3)/3 - (power(pi(), 2) + 6*power(log(2), 2))/12 + power(log(1-x), 2)*(log((1-x)/8) - 3*log(x))/6 - log(1+x)*(power(pi(), 2) - 6*power(log(2), 2) + log(64)*log(1+x))/12 - log(1-x)*nl(1, 1, -x) + nl(2, 1, (1-x)/2) - nl(2, 1, 1-x) + nl(2, 1, -x) - nl(2, 1, 2*x/(-1+x)) + nl(2, 1, x/(1+x)) - nl(2, 1, 2*x/(1+x)) + nl(2, 1, (1+x)/2) - 3*zeta(3)/4
    elif a == 0 and b == -1 and c == 0:
        result = - log(x)*nl(1, 1, -x) + 2*nl(2, 1, -x)
    elif a == 0 and b == 0 and c == 0:
        result = power(log(x), 3)/6
    elif a == 0 and b == 0 and c == 1:
        result = nl(2, 1, x)
    elif a == 0 and b == 1 and c == 0:
        result = log(x)*nl(1, 1, x) - 2*nl(2, 1, x)
    elif a == 0 and b == 1 and c == 1:
        result = log(x)*power(log(1-x), 2)/2 + log(1-x)*nl(1, 1, 1-x) - nl(2, 1, 1-x) + zeta(3)
    elif a == 1 and b == 0 and c == 0:
        result = - power(log(x), 2)*log(1-x)/2 - log(x)*nl(1, 1, x) + nl(2, 1, x)
    elif a == 1 and b == 0 and c == 1:
        result = - log(x)*power(log(1-x), 2) - 2*log(1-x)*nl(1, 1, 1-x) - log(1-x)*nl(1, 1, x) + 2*nl(2, 1, 1-x) - 2*zeta(3)
    elif a == 1 and b == 1 and c == 0:
        result = log(x)*power(log(1-x), 2) + log(1-x)*nl(1, 1, 1-x) + log(1-x)*nl(1, 1, x) - nl(2, 1, 1-x) + zeta(3)
    elif a == 1 and b == 1 and c == 1:
        result = - power(log(1-x), 3)/6
    else:
        raise Exception('wwwat yu doinnn!!???')
    return result