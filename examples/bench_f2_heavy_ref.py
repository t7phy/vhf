"""Generate reference values for f2_heavy NC NNLO benchmarks using LeProHQ."""
import numpy as np
import LeProHQ

m_c = 1.273
m2 = m_c**2

test_points = [
    (0.01, 10.0),
    (0.1, 10.0),
    (0.001, 100.0),
    (0.01, 100.0),
    (0.1, 100.0),
    (0.5, 10.0),
    (0.3, 10.0),
    (0.001, 10000.0),
    (0.01, 10000.0),
    (0.4, 10.0),
    (0.01, 5000.0),
]

print("# f2_heavy NC NNLO reference (LeProHQ)")
print("# x, Q2, xi, eta, gvv, gaa, psvv, psaa, ns_r, ns_l")

for x, Q2 in test_points:
    xi = Q2 / m2
    eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0
    shat = Q2 * (1.0 - x) / x

    if shat <= 4.0 * m2:
        print(f"{x:.6e}, {Q2:.6e}, {xi:.6e}, {eta:.6e}, 0, 0, 0, 0, 0, 0")
        continue

    prefac = Q2 / (np.pi * m2)
    prefac_nnlo = prefac / x * (4.0 * np.pi) ** 2

    # gluon VV
    cg1_vv = LeProHQ.cg1("F2", "VV", xi, eta)
    cgbar1_vv = LeProHQ.cgBar1("F2", "VV", xi, eta)
    gvv = prefac_nnlo * (cg1_vv + cgbar1_vv * np.log(xi))

    # gluon AA
    cg1_aa = LeProHQ.cg1("F2", "AA", xi, eta)
    cgbar1_aa = LeProHQ.cgBar1("F2", "AA", xi, eta)
    gaa = prefac_nnlo * (cg1_aa + cgbar1_aa * np.log(xi))

    # pure-singlet VV
    cq1_vv = LeProHQ.cq1("F2", "VV", xi, eta)
    cqbarf1_vv = LeProHQ.cqBarF1("F2", "VV", xi, eta)
    psvv = prefac_nnlo * (cq1_vv + cqbarf1_vv * np.log(xi))

    # pure-singlet AA
    cq1_aa = LeProHQ.cq1("F2", "AA", xi, eta)
    cqbarf1_aa = LeProHQ.cqBarF1("F2", "AA", xi, eta)
    psaa = prefac_nnlo * (cq1_aa + cqbarf1_aa * np.log(xi))

    # non-singlet
    eta_ns = min(eta, 1e8)
    ns_r = prefac_nnlo * LeProHQ.dq1("F2", "VV", xi, eta_ns)
    ns_l = -LeProHQ.Adler("F2", "VV", xi)

    print(
        f"{x:.6e}, {Q2:.6e}, {xi:.6e}, {eta:.6e}, "
        f"{gvv:.15e}, {gaa:.15e}, {psvv:.15e}, {psaa:.15e}, "
        f"{ns_r:.15e}, {ns_l:.15e}"
    )
