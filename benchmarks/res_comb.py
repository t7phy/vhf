import lhapdf
import numpy as np
import yaml
from core.libfunc import lambertgrid

p = lhapdf.mkPDF("NNPDF31_nlo_pch_as_0118")
f = lhapdf.mkPDF("MAPFF10NNLOPIp")

xgrid = lambertgrid(50, 1e-5, 1.0)
zgrid = lambertgrid(50, 1e-2, 1.0)

Q = 2.45
alphas = p.alphasQ(Q)

pdf = {}
ff = {}

for j in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 21]:
    pdf[j] = np.empty((50, 1))
    ff[j] = np.empty((1, 50))
    for i in range(50):
        pdf[j][i][0] = p.xfxQ(j, xgrid[i], Q)
        ff[j][0][i] = f.xfxQ(j, zgrid[i], Q)

xpoints = [0.05]
zpoints = [0.1, 0.15, 0.2, 0.223, 0.249, 0.274, 0.299, 0.324, 0.349, 0.374, 0.399, 0.424, 0.449, 0.474, 0.499, 0.524, 0.549, 0.574, 0.599, 0.624, 0.649, 0.674, 0.699, 0.724, 0.749, 0.795, 0.85, 0.9, 0.95]

with open('benchmarks/240721/res_0_0.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

res = 0
for channel, itpg in data.items():
    convp = pdf[channel[0]]
    convf = ff[channel[1]]
    res += (convf @ (itpg @ convp))[0][0]

print(res)
# res = np.array(data[(-2, -2)])
# print(ff[-2]@(res@pdf[-2]))