"""Reference values for f3, g4, gL heavy NC NNLO using LeProHQ."""
import numpy as np
import LeProHQ

m_c = 1.273
m2 = m_c**2

test_points = [
    (0.01, 10.0), (0.1, 10.0), (0.001, 100.0), (0.01, 100.0),
    (0.1, 100.0), (0.5, 10.0), (0.3, 10.0), (0.001, 10000.0),
    (0.01, 10000.0), (0.4, 10.0), (0.01, 5000.0),
]

print("# x, Q2, f3_r, f3_l, g4_r, g4_l, gl_r, gl_l")
for x, Q2 in test_points:
    xi = Q2 / m2
    eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0
    shat = Q2 * (1.0 - x) / x
    if shat <= 4.0 * m2:
        print(f"{x:.6e}, {Q2:.6e}, 0, 0, 0, 0, 0, 0")
        continue
    prefac_nnlo = Q2 / (np.pi * m2) / x * (4.0 * np.pi) ** 2

    f3_r = prefac_nnlo * LeProHQ.dq1("xF3", "VA", xi, eta)
    f3_l = -LeProHQ.Adler("xF3", "VA", xi)

    eta_g4 = min(eta, 1e5)
    g4_r = prefac_nnlo * LeProHQ.dq1("g4", "VA", xi, eta_g4)
    g4_l = -LeProHQ.Adler("g4", "VA", xi)

    gl_r = prefac_nnlo * LeProHQ.dq1("gL", "VA", xi, eta)
    gl_l = -LeProHQ.Adler("gL", "VA", xi)

    print(
        f"{x:.6e}, {Q2:.6e}, "
        f"{f3_r:.15e}, {f3_l:.15e}, "
        f"{g4_r:.15e}, {g4_l:.15e}, "
        f"{gl_r:.15e}, {gl_l:.15e}"
    )
