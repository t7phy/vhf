import numpy as np
import scipy as sp

def lambertgrid(n_pts, x_min, x_max=1.0):
    
    def direct_relation(x):
        return 5 * (1 - x) - np.log(x)

    def inverse_relation(y):
        return np.real(1 / 5 * sp.special.lambertw(5 * np.exp(5 - y)))

    y_min = direct_relation(x_min)
    y_max = direct_relation(x_max)

    return [inverse_relation(y) for y in np.linspace(y_min, y_max, n_pts)]

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

def point_interpolator(ev_point, basis_functions, i, mode_log=True):
    if mode_log:
        ev_point = np.log(ev_point)
    res = 0
    for j in range(len(basis_functions['p_'+str(i)])):
        if basis_functions['p_'+str(i)][j]['xmin'] < ev_point <= basis_functions['p_'+str(i)][j]['xmax']:
            for k, l in enumerate(basis_functions['p_'+str(i)][j]['coeffs']):
                res += l * np.power(ev_point, k)
    return res

def integration_regions(x, itp_xgrid):
    if x <= itp_xgrid[0] or x >= itp_xgrid[-1]:
        return None
    else:
        region_borders_from_xgrid = itp_xgrid[np.searchsorted(itp_xgrid, x, side='right'):]
        region_borders = np.append(x, region_borders_from_xgrid)
        regions = [(region_borders[i], region_borders[i + 1]) for i in range(len(region_borders) - 1)]
        return regions

import json
import numpy as np
# Import your existing python functions here
# from interpolation import lambertgrid, compute_basis_functions, interpolator

# def run_verification():
#     # Load Rust results
#     with open("interp_comparison.json", "r") as f:
#         rs = json.load(f)

#     # 1. Compare Grid
#     py_grid = lambertgrid(50, 1e-5, 1.0)
#     grid_diff = np.abs(np.array(rs['xgrid']) - np.array(py_grid)).max()
#     print(f"Grid Difference: {grid_diff:.2e} {'✅' if grid_diff < 1e-15 else '❌'}")

#     # 2. Compare Basis Function Dictionary
#     # We compare the 'p_i' keys and the coeffs inside
#     py_bfs = compute_basis_functions(py_grid, 3, mode_log=True)
    
#     max_coeff_diff = 0
#     for p_key in py_bfs:
#         for i in range(len(py_bfs[p_key])):
#             py_c = np.array(py_bfs[p_key][i]['coeffs'])
#             rs_c = np.array(rs['basis_functions'][p_key][i]['coeffs'])
#             max_coeff_diff = max(max_coeff_diff, np.abs(py_c - rs_c).max())
    
#     print(f"Coeffs Difference: {max_coeff_diff:.2e} {'✅' if max_coeff_diff < 1e-13 else '❌'}")

#     # 3. Partition of Unity Check
#     print("\n--- Partition of Unity Check (Sum of Basis) ---")
#     for idx, pt in enumerate(rs['test_points']):
#         rs_res = np.array(rs['interp_results'][idx])
#         sum_basis = np.sum(rs_res)
#         diff_from_one = abs(1.0 - sum_basis)
#         print(f"Point {pt:5}: Sum = {sum_basis:.6f} | Diff = {diff_from_one:.2e} {'✅' if diff_from_one < 1e-12 else '❌'}")

# def run_verification():
#     # Load Rust results
#     with open("interp_comparison.json", "r") as f:
#         rs = json.load(f)

#     # 1. Compare Grid
#     py_grid = np.array(lambertgrid(50, 1e-5, 1.0))
#     rs_grid = np.array(rs['xgrid'])
    
#     # Relative difference: |a - b| / |b| * 100
#     grid_rel_diff = (np.abs(rs_grid - py_grid) / np.abs(py_grid)).max() * 100
#     print(f"Grid Max Rel Difference: {grid_rel_diff:.2e}% {'✅' if grid_rel_diff < 1e-12 else '❌'}")

#     # 2. Compare Basis Function Dictionary
#     py_bfs = compute_basis_functions(py_grid.tolist(), 3, mode_log=True)
    
#     max_rel_coeff_diff = 0
#     for p_key in py_bfs:
#         for i in range(len(py_bfs[p_key])):
#             py_c = np.array(py_bfs[p_key][i]['coeffs'])
#             rs_c = np.array(rs['basis_functions'][p_key][i]['coeffs'])
            
#             # Avoid division by zero for tiny coefficients
#             denom = np.abs(py_c)
#             denom[denom < 1e-15] = 1e-15 
            
#             rel_diff = (np.abs(py_c - rs_c) / denom).max() * 100
#             max_rel_coeff_diff = max(max_rel_coeff_diff, rel_diff)
    
#     print(f"Coeffs Max Rel Difference: {max_rel_coeff_diff:.2e}% {'✅' if max_rel_coeff_diff < 1e-8 else '❌'}")

#     # 3. Partition of Unity Check
#     print("\n--- Partition of Unity Check (Relative Error) ---")
#     for idx, pt in enumerate(rs['test_points']):
#         rs_res = np.array(rs['interp_results'][idx])
#         sum_basis = np.sum(rs_res)
        
#         # Since the target is 1.0, absolute diff == relative diff
#         rel_diff_from_one = abs(1.0 - sum_basis) * 100
#         print(f"Point {pt:5}: Sum = {sum_basis:.6f} | Rel Err = {rel_diff_from_one:.2e}% {'✅' if rel_diff_from_one < 1e-10 else '❌'}")

def run_verification():
    # Load Rust results
    with open("interp_comparison.json", "r") as f:
        rs = json.load(f)

    # 1. Compare Grid
    py_grid = np.array(lambertgrid(50, 1e-5, 1.0))
    rs_grid = np.array(rs['xgrid'])
    
    grid_rel_diff = (np.abs(rs_grid - py_grid) / np.abs(py_grid)).max() * 100
    print(f"Grid Max Rel Difference: {grid_rel_diff:.2e}% {'✅' if grid_rel_diff < 1e-12 else '❌'}")

    # 2. Compare Basis Function Dictionary
    # Python still produces a Dictionary {'p_0': ...}
    py_bfs = compute_basis_functions(py_grid.tolist(), 4, mode_log=True)
    
    # Rust produced a List [[...], [...]]
    rs_bfs = rs['basis_functions']
    
    max_rel_coeff_diff = 0
    
    # Iterate by index to compare Dict (Py) vs List (Rust)
    for i in range(len(rs_bfs)):
        key = f"p_{i}" # Python key
        
        # Get list of pieces for this basis function
        py_pieces = py_bfs[key]
        rs_pieces = rs_bfs[i]
        
        if len(py_pieces) != len(rs_pieces):
            print(f"Mismatch in piece count for {key}")
            continue

        for j in range(len(py_pieces)):
            py_c = np.array(py_pieces[j]['coeffs'])
            rs_c = np.array(rs_pieces[j]['coeffs'])
            
            # Avoid division by zero for tiny coefficients
            denom = np.abs(py_c)
            denom[denom < 1e-15] = 1e-15 
            
            rel_diff = (np.abs(py_c - rs_c) / denom).max() * 100
            max_rel_coeff_diff = max(max_rel_coeff_diff, rel_diff)
    
    print(f"Coeffs Max Rel Difference: {max_rel_coeff_diff:.2e}% {'✅' if max_rel_coeff_diff < 1e-8 else '❌'}")

    # 3. Partition of Unity Check
    print("\n--- Partition of Unity Check (Relative Error) ---")
    for idx, pt in enumerate(rs['test_points']):
        rs_res = np.array(rs['interp_results'][idx])
        sum_basis = np.sum(rs_res)
        
        rel_diff_from_one = abs(1.0 - sum_basis) * 100
        # Relaxed threshold slightly for float precision at boundaries
        print(f"Point {pt:5}: Sum = {sum_basis:.6f} | Rel Err = {rel_diff_from_one:.2e}% {'✅' if rel_diff_from_one < 1e-9 else '❌'}")

if __name__ == "__main__":
    run_verification()