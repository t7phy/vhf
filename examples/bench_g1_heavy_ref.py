"""Reference values for g1_heavy NC NNLO using LeProHQ (proj=x2g1)."""
import numpy as np
import LeProHQ

m_c = 1.273
m2 = m_c**2

test_points = [
    (0.01, 10.0), (0.1, 10.0), (0.001, 100.0), (0.01, 100.0),
    (0.1, 100.0), (0.5, 10.0), (0.3, 10.0), (0.4, 10.0),
]

print("# x, Q2, gvv, gaa, psvv, psaa, ns_r, ns_l")
for x, Q2 in test_points:
    xi = Q2 / m2
    eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0
    shat = Q2 * (1.0 - x) / x
    if shat <= 4.0 * m2:
        print(f"{x:.6e}, {Q2:.6e}, 0, 0, 0, 0, 0, 0")
        continue
    prefac = Q2 / (np.pi * m2) / x * (4.0 * np.pi) ** 2
    gvv = prefac * (LeProHQ.cg1("x2g1", "VV", xi, eta) + LeProHQ.cgBar1("x2g1", "VV", xi, eta) * np.log(xi))
    gaa = prefac * (LeProHQ.cg1("x2g1", "AA", xi, eta) + LeProHQ.cgBar1("x2g1", "AA", xi, eta) * np.log(xi))
    psvv = prefac * (LeProHQ.cq1("x2g1", "VV", xi, eta) + LeProHQ.cqBarF1("x2g1", "VV", xi, eta) * np.log(xi))
    psaa = prefac * (LeProHQ.cq1("x2g1", "AA", xi, eta) + LeProHQ.cqBarF1("x2g1", "AA", xi, eta) * np.log(xi))
    ns_r = prefac * LeProHQ.dq1("x2g1", "VV", xi, eta)
    ns_l = -LeProHQ.Adler("x2g1", "VV", xi)
    print(f"{x:.6e}, {Q2:.6e}, {gvv:.15e}, {gaa:.15e}, {psvv:.15e}, {psaa:.15e}, {ns_r:.15e}, {ns_l:.15e}")
