import lhapdf
from scipy.integrate import quad

p = lhapdf.mkPDF("NNPDF31_nlo_pch_as_0118")
f = lhapdf.mkPDF("MAPFF10NNLOPIp")

q = 2.45
x = 0.05
z = [0.1, 0.15, 0.2, 0.223, 0.249, 0.274, 0.299, 0.324, 0.349, 0.374, 0.399, 0.424, 0.449, 0.474, 0.499, 0.524, 0.549, 0.574, 0.599, 0.624, 0.649, 0.674, 0.699, 0.724, 0.749, 0.795, 0.85, 0.9, 0.95]
y_integral, _ = quad(lambda y: (1-y)/y, 0.3, 0.5)
res = []
for i in range(len(z)):
    res.append((
    # LO q2q channel, only contains local-local part, no
    # integration needed
        p.xfxQ(-5, x, q) * f.xfxQ(-5, z[i], q) * (1/9) +
        p.xfxQ(-4, x, q) * f.xfxQ(-4, z[i], q) * (4/9) +
        p.xfxQ(-3, x, q) * f.xfxQ(-3, z[i], q) * (1/9) +
        p.xfxQ(-2, x, q) * f.xfxQ(-2, z[i], q) * (4/9) +
        p.xfxQ(-1, x, q) * f.xfxQ(-1, z[i], q) * (1/9) +
        p.xfxQ(1, x, q) * f.xfxQ(1, z[i], q) * (1/9) +
        p.xfxQ(2, x, q) * f.xfxQ(2, z[i], q) * (4/9) +
        p.xfxQ(3, x, q) * f.xfxQ(3, z[i], q) * (1/9) +
        p.xfxQ(4, x, q) * f.xfxQ(4, z[i], q) * (4/9) +
        p.xfxQ(5, x, q) * f.xfxQ(5, z[i], q) * (1/9) 
    )* y_integral/0.2)

print(res)
