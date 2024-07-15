from .conv import conv2

def unpol_sidis_F2(x, z, Q2, sy, ct, cl, sv_order, itp_grids):
    if sy[0] != None:
        y = Q2/(sy[0] * x)
    else:
        y = sy[1]
    CT = conv2(x, z, ct, sv_order, itp_grids[0], itp_grids[1])
    CL = conv2(x, z, cl, sv_order, itp_grids[0], itp_grids[1])
    ct_grid = np.array(CT()) * (1-y)/y
    cl_grid = np.array(CL()) * (1+(1-y)**2)/(2*y)
    return ct_grid + cl_grid

