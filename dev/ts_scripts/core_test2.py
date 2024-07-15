from core.conv import conv2
from core.libfunc import lambertgrid
import time
import lhapdf

from eh.unpol.nnlo.ct import c2t_g2g_eq

xgrid = lambertgrid(50, 1e-5, 1.0)
zgrid = lambertgrid(50, 1e-2, 1.0)

start_time = time.time()
trial = conv2(0.6, 0.7, c2t_g2g_eq.ct_nnlo_g2g_eq, '000', xgrid, zgrid)
otp = trial()
end_time = time.time()
print(otp)
print("Execution time: {:.2f} seconds".format(end_time - start_time))

# p = lhapdf.mkPDF('NNPDF40_nnlo_as_01180', 0)
# f = lhapdf.mkPDF('MAPFF10NNLOPIp', 0)

# start_time = time.time()

# trial = conv2(0.6, 0.7, 100, c2t_g2g_eq.ct_nnlo_g2g_eq, p, f, 21, 21)
# otp, _ = trial()
# print(otp)

# end_time = time.time()
# print("Execution time: {:.2f} seconds".format(end_time - start_time))
