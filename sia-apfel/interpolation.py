import numpy as np

def area_block_map(xgrid, poly_deg):
    num_x = len(xgrid)
    num_areas = num_x - 1
    blocks_index = []
    if poly_deg % 2 == 0: po2 = poly_deg // 2 - 1
    else: po2 = poly_deg // 2
    for i in range(num_areas):
        kmin = max(0, i - po2)
        kmax = kmin + poly_deg
        if kmax >= num_x:
            kmax = num_areas
            kmin = kmax - poly_deg
        blocks_index.append((kmin, kmax))
    return blocks_index

def basis_function(poly_index, xgrid, blocks_index, basis_functions):
    bflist = []
    for i, (kmin, kmax) in enumerate(blocks_index):
        ref_indices = []
        if kmin <= poly_index <= kmax:
            xmin = xgrid[i]
            xmax = xgrid[i + 1]
            for j in range(kmin, kmax + 1): 
                if j != poly_index: ref_indices.append(j)
            xj = xgrid[poly_index]
            denominator = 1
            for j in ref_indices: denominator *= (xj - xgrid[j])
            coeffs = np.ones(1)
            for s, k in enumerate(ref_indices):
                xk = xgrid[k]
                Mxk_coeffs = -xk * coeffs
                coeffs = np.concatenate(([0.0], coeffs))
                coeffs[: s +1] += Mxk_coeffs
            coeffs /= denominator
            coeffs = coeffs.tolist()
            bflist.append({'xmin': xmin, 'xmax': xmax, 'coeffs': coeffs})
    basis_functions['p_'+str(poly_index)] = bflist
    return basis_functions

def compute_basis_functions(xgrid, poly_deg, mode_log=True):
    if mode_log:
        xgrid = np.log(xgrid)
    num_x = len(xgrid)
    blocks_index = area_block_map(xgrid, poly_deg)
    basis_functions = {}
    for i in range(num_x): basis_functions['p_'+str(i)] = {}
    for i in range(num_x):
        basis_functions = basis_function(i, xgrid, blocks_index, basis_functions)
    return basis_functions

xgrid = [0.1, 0.2, 0.1, 0.3, 0.4, 0.5, 0.6 ,0.7, 0.8, 1.0]
# adict = compute_basis_functions(xgrid, 3)
# for i in adict:
#     print(i)

# def process_xgrid(xgrid, mode_log=True):
#     if mode_log:
#         xgrid = np.log(xgrid)
#     return xgrid

def interpolator(ev_point, basis_functions, mode_log=True):
    if mode_log:
        ev_point = np.log(ev_point)
    res_list = []
    for i in range(len(basis_functions)):
        res = 0
        for j in range(len(basis_functions['p_'+str(i)])):
            if basis_functions['p_'+str(i)][j]['xmin'] < ev_point <= basis_functions['p_'+str(i)][j]['xmax']:
                for k, l in enumerate(basis_functions['p_'+str(i)][j]['coeffs']):
                    res += l * np.power(ev_point, k)
        res_list.append(res)
    return res_list

# print(interpolator(0.234567, adict))

def point_interpolator(ev_point, basis_functions, i, mode_log=True):
    if mode_log:
        ev_point = np.log(ev_point)
    res = 0
    for j in range(len(basis_functions['p_'+str(i)])):
        if basis_functions['p_'+str(i)][j]['xmin'] < ev_point <= basis_functions['p_'+str(i)][j]['xmax']:
            for k, l in enumerate(basis_functions['p_'+str(i)][j]['coeffs']):
                res += l * np.power(ev_point, k)
    return res

