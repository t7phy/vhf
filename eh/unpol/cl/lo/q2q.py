from configs.eh import *

def cf(x, z, rsl, orders):
    return 0

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
