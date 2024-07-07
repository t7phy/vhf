from core.conv import conv2
from core.libfunc import lambertgrid
import time

from eh.unpol.nnlo.ct import c2t_q2qp_es

xgrid = lambertgrid(50, 1e-5, 1.0)
zgrid = lambertgrid(50, 1e-2, 1.0)

start_time = time.time()
trial = conv2(0.9, 0.9, c2t_q2qp_es.ct_nnlo_q2qp_es, '000', xgrid, zgrid)
otp = trial()
end_time = time.time()
print(otp)
print("Execution time: {:.2f} seconds".format(end_time - start_time))