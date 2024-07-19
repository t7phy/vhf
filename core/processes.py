from .conv import conv2
from scipy.integrate import quad

def unpol_sidis_F2(x, z, y, ct_grid, cl_grid):
    if type(y) == tuple:
        grid = quad(lambda y: (1-y)/y, y[0], y[1]) * np.array(ct_grid) + quad(lambda y: (1+(1-y)**2)/(2*y), y[0], y[1]) * np.array(cl_grid)
    else:
        grid = (1-y)/y * np.array(ct_grid) + (1+(1-y)**2)/(2*y) * np.array(cl_grid)
    return grid

    # if sy[0] != None:
    #     y = Q2/(sy[0] * x)
    # else:
    #     y = sy[1]
    # CT = conv2(x, z, ct, sv_order, itp_grids[0], itp_grids[1])
    # CL = conv2(x, z, cl, sv_order, itp_grids[0], itp_grids[1])
    # ct_grid = np.array(CT()) * (1-y)/y
    # cl_grid = np.array(CL()) * (1+(1-y)**2)/(2*y)
    # return ct_grid + cl_grid

