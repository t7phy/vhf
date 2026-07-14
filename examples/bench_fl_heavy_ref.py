"""Generate reference values for fl_heavy NC NNLO benchmarks using LeProHQ."""
import numpy as np
import LeProHQ

m_c = 1.273
m2 = m_c**2

test_points = [
    (0.01, 10.0), (0.1, 10.0), (0.001, 100.0), (0.01, 100.0),
    (0.1, 100.0), (0.5, 10.0), (0.3, 10.0), (0.001, 10000.0),
    (0.01, 10000.0), (0.4, 10.0), (0.01, 5000.0),
]

print("# x, Q2, gvv, gaa, psvv, psaa, ns_r, ns_l")
for x, Q2 in test_points:
    xi = Q2 / m2
    eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0
    shat = Q2 * (1.0 - x) / x
    if shat <= 4.0 * m2:
        print(f"{x:.6e}, {Q2:.6e}, 0, 0, 0, 0, 0, 0")
        continue
    prefac_nnlo = Q2 / (np.pi * m2) / x * (4.0 * np.pi) ** 2
    gvv = prefac_nnlo * (LeProHQ.cg1("FL", "VV", xi, eta) + LeProHQ.cgBar1("FL", "VV", xi, eta) * np.log(xi))
    gaa = prefac_nnlo * (LeProHQ.cg1("FL", "AA", xi, eta) + LeProHQ.cgBar1("FL", "AA", xi, eta) * np.log(xi))
    psvv = prefac_nnlo * (LeProHQ.cq1("FL", "VV", xi, eta) + LeProHQ.cqBarF1("FL", "VV", xi, eta) * np.log(xi))
    psaa = prefac_nnlo * (LeProHQ.cq1("FL", "AA", xi, eta) + LeProHQ.cqBarF1("FL", "AA", xi, eta) * np.log(xi))
    ns_r = prefac_nnlo * LeProHQ.dq1("FL", "VV", xi, eta)
    ns_l = -LeProHQ.Adler("FL", "VV", xi)
    print(f"{x:.6e}, {Q2:.6e}, {gvv:.15e}, {gaa:.15e}, {psvv:.15e}, {psaa:.15e}, {ns_r:.15e}, {ns_l:.15e}")
