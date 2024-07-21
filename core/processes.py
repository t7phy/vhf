import numpy as np
from .conv import conv2
from scipy.integrate import quad

def unpol_sidis_F2(x, z, y, ct_func, cl_func, itp_points):
    ct = conv2(x, z, ct_func.cf, '000', itp_points[0], itp_points[1])
    ct_grid = np.array(ct())
    cl = conv2(x, z, cl_func.cf, '000', itp_points[0], itp_points[1])
    cl_grid = np.array(cl())
    if type(y) == tuple:
        ct_integral, _ = quad(lambda y: (1-y)/y, y[0], y[1])
        cl_integral, _ = quad(lambda y: (1+(1-y)**2)/(2*y), y[0], y[1])
        grid = ct_integral * ct_grid + cl_integral * cl_grid
    else:
        grid = (1-y)/y * ct_grid + (1+(1-y)**2)/(2*y) * cl_grid
    itp_grids = {}
    for channels in ct_func.channel_map:
        itp_grids[channels] = (grid * ct_func.channel_map[channels]).tolist()
    return itp_grids

    # if sy[0] != None:
    #     y = Q2/(sy[0] * x)
    # else:
    #     y = sy[1]
    # CT = conv2(x, z, ct, sv_order, itp_grids[0], itp_grids[1])
    # CL = conv2(x, z, cl, sv_order, itp_grids[0], itp_grids[1])
    # ct_grid = np.array(CT()) * (1-y)/y
    # cl_grid = np.array(CL()) * (1+(1-y)**2)/(2*y)
    # return ct_grid + cl_grid

