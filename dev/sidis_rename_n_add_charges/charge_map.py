# The charge map, maps to coeficient names from the functions as described
# in the paper https://arxiv.org/abs/2401.16281v2, eq. 6

# PDG numbers
# d: 1
# u: 2
# s: 3
# c: 4
# b: 5
# g: 21
pdg_numbers = [1, 2, 3, 4, 5, 21]

# Charges quarks
d = -1 / 3
u = 2 / 3
s = -1 / 3
c = 2 / 3
b = -1 / 3

# Charges anti quarks
db = -d
ub = -u
sb = -s
cb = -c
bb = -b

# Charges squared
d2 = d**2
u2 = u**2
s2 = s**2
c2 = c**2
b2 = b**2

sum_q2 = d2 + u2 + s2 + c2 + b2


charge_map = {
    "nnlo_g2g": {(21, 21): sum_q2},
    "nnlo_g2q": {(21, 1): d2, (21, 2): u2, (21, 3): s2, (21, 4): c2, (21, 5): b2},
    "nnlo_q2g": {(1, 21): d2, (2, 21): u2, (3, 21): s2, (4, 21): c2, (5, 21): b2},
    "nnlo_q2q_ns": {(1, 1): d2, (2, 2): u2, (3, 3): s2, (4, 4): c2, (5, 5): b2},
    "nnlo_q2q_ps": {(1, 1): sum_q2, (2, 2): sum_q2, (3, 3): sum_q2, (4, 4): sum_q2, (5, 5): sum_q2},
    "nnlo_q2qb": {(1, -1): d2, (2, -2): u2, (3, -3): s2, (4, -4): c2, (5, -5): b2},
    "nnlo_q2qp_1": {
        (1, 2): d2,
        (1, 3): d2,
        (1, 4): d2,
        (1, 5): d2,
        (2, 1): u2,
        (2, 3): u2,
        (2, 4): u2,
        (2, 5): u2,
        (3, 1): s2,
        (3, 2): s2,
        (3, 4): s2,
        (3, 5): s2,
        (4, 1): c2,
        (4, 2): c2,
        (4, 3): c2,
        (4, 5): c2,
        (5, 1): b2,
        (5, 2): b2,
        (5, 3): b2,
        (5, 4): b2,
    },
    "nnlo_q2qp_2": {
        (2, 1): d2,
        (3, 1): d2,
        (4, 1): d2,
        (5, 1): d2,
        (1, 2): u2,
        (3, 2): u2,
        (4, 2): u2,
        (5, 2): u2,
        (1, 3): s2,
        (2, 3): s2,
        (4, 3): s2,
        (5, 3): s2,
        (1, 4): c2,
        (2, 4): c2,
        (3, 4): c2,
        (5, 4): c2,
        (1, 5): b2,
        (2, 5): b2,
        (3, 5): b2,
        (4, 5): b2,
    },
    "nnlo_q2qp_3": {
        (1, 2): d * u,
        (1, 3): d * s,
        (1, 4): d * c,
        (1, 5): d * b,
        (2, 3): u * s,
        (2, 4): u * c,
        (2, 5): u * b,
        (3, 4): s * c,
        (3, 5): s * b,
        (4, 5): c * b,
        (2, 1): d * u,
        (3, 1): d * s,
        (4, 1): d * c,
        (5, 1): d * b,
        (3, 2): u * s,
        (4, 2): u * c,
        (5, 2): u * b,
        (4, 3): s * c,
        (5, 3): s * b,
        (5, 4): c * b,
    },
}

# In case you want to add all possible combinations per formula
# charge_map_all = {}

# for key, value in charge_map.items():
#     combinations_present = list(value.keys())

#     for pdg_i in pdg_numbers:
#         for pdg_j in pdg_numbers:
#             if (pdg_i, pdg_j) not in combinations_present:
#                 value[(pdg_i, pdg_j)] = 0

#     charge_map_all[key] = value
