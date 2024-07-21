import sys
import yaml
import eh
from core.processes import unpol_sidis_F2
from core.libfunc import lambertgrid
cl = [eh.unpol.cl.lo.q2q, eh.unpol.cl.nlo.q2q, eh.unpol.cl.nlo.q2g, eh.unpol.cl.nlo.g2q]
ct = [eh.unpol.ct.lo.q2q, eh.unpol.ct.nlo.q2q, eh.unpol.ct.nlo.q2g, eh.unpol.ct.nlo.g2q]

itp_points = [lambertgrid(50, 1e-5, 1.0), lambertgrid(50, 1e-2, 1.0)]

x = 0.05
z = [0.1, 0.15, 0.2, 0.223, 0.249, 0.274, 0.299, 0.324, 0.349, 0.374, 0.399, 0.424, 0.449, 0.474, 0.499, 0.524, 0.549, 0.574, 0.599, 0.624, 0.649, 0.674, 0.699, 0.724, 0.749, 0.795, 0.85, 0.9, 0.95]

z_index = int(sys.argv[1])
func_index = int(sys.argv[2])

res = unpol_sidis_F2(0.05, z[z_index], (0.3, 0.5), ct[func_index], cl[func_index], itp_points)

with open('benchmarks/240721/res_'+str(z_index)+'_'+str(func_index)+'.yaml', 'w') as f:
    yaml.dump(res, f)

