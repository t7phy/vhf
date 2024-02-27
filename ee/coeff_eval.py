from . import coeff
from core.conv import convolution, evaluate_loc
from core.interpolation import compute_basis_functions, interpolator
from eko.interpolation import lambertgrid
import numpy as np
import pineappl

def eval_c2_lo(x, interpolator_at_x):
    res_q = evaluate_loc(x, interpolator_at_x, coeff.c2_lo_q_loc)
    return res_q

def eval_c2_nlo(x, mode_log, basis_functions, interpolator_at_x):
    res_q, err_q = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nlo_q_reg, coeff.c2_nlo_q_sing, coeff.c2_nlo_q_loc)
    res_g, err_g = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nlo_g_reg)
    return res_q, err_q, res_g, err_g

def eval_c2_nnlo(x, mode_log, basis_functions, interpolator_at_x, NF):
    res_ns, err_ns = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nnlo_ns_reg, coeff.c2_nnlo_ns_sing, coeff.c2_nnlo_ns_loc, NF)
    res_ps, err_ps = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nnlo_ps_reg, None, None, NF)
    res_g, err_g = convolution(x, mode_log, basis_functions, interpolator_at_x, coeff.c2_nnlo_g_reg, None, None, NF)
    return res_ns, err_ns, res_ps, err_ps, res_g, err_g

def eval_c2(order, x, mode_log, basis_functions, interpolator_at_x, NF):
    if order not in ['lo', 'nlo', 'nnlo']:
        raise ValueError('Order must be one of lo, nlo, nnlo')
    res_dict = {}
    filler_arr = [0 for _ in range(len(basis_functions))]
    if order in ['lo', 'nlo', 'nnlo']:
        res_dict['lo_ns'] = eval_c2_lo(x, interpolator_at_x)
        res_dict['lo_ps'] = filler_arr
        res_dict['lo_g'] = filler_arr
    if order in ['nlo', 'nnlo']:
        res_dict['nlo_ns'], _, res_dict['nlo_g'], _ = eval_c2_nlo(x, mode_log, basis_functions, interpolator_at_x)
        res_dict['nlo_ps'] = filler_arr
    if order in ['nnlo']:
        res_dict['nnlo_ns'], _, res_dict['nnlo_ps'], _, res_dict['nnlo_g'], _ = eval_c2_nnlo(x, mode_log, basis_functions, interpolator_at_x, NF)
    return res_dict

xgrid = lambertgrid(50, 0.001, 1)  #[0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 0.9]
bf = compute_basis_functions(xgrid, 4)
# x = 0.15
# interpolator_at_x = interpolator(x, bf)
# c2test = eval_c2('nnlo', x, True, bf, interpolator_at_x, 5)
# print(c2test)

def basis_transform(pre_results):
    e2_avg = (4/9 + 1/9 + 4/9 + 1/9 + 1/9)/5
    ns_weights = {'g': 0, 'ph': 0, 'u': 4/9, 'd': 1/9, 's': 1/9, 'c': 4/9, 'b': 1/9, 't': 0, 'ub': 4/9, 'db': 1/9, 'sb': 1/9, 'cb': 4/9, 'bb': 1/9, 'tb': 0}
    g_weights = {'g': e2_avg, 'ph': 0, 'u': 0, 'd': 0, 's': 0, 'c': 0, 'b': 0, 't': 0, 'ub': 0, 'db': 0, 'sb': 0, 'cb': 0, 'bb': 0, 'tb': 0}
    ps_weights = {'g': 0, 'ph': 0, 'u': e2_avg, 'd': e2_avg, 's': e2_avg, 'c': e2_avg, 'b': e2_avg, 't': 0, 'ub': e2_avg, 'db': e2_avg, 'sb': e2_avg, 'cb': e2_avg, 'bb': e2_avg, 'tb': 0}    

    results = {}

    for order in ['lo', 'nlo', 'nnlo']:
        for partons in ['g', 'ph', 'u', 'd', 's', 'c', 'b', 't', 'ub', 'db', 'sb', 'cb', 'bb', 'tb']:
            results[order + '_' + partons] = []
            for i in range(len(pre_results[order + '_ns'])):
                if partons == 'g':
                    results[order + '_' + partons].append(pre_results[order + '_g'][i] * g_weights[partons])
                elif partons == 'ph':
                    results[order + '_' + partons].append(0)
                else:
                    results[order + '_' + partons].append(pre_results[order + '_ns'][i] * ns_weights[partons] + pre_results[order + '_ps'][i] * ps_weights[partons])
    return results

# c2res = basis_transform(c2test)
# print(c2res)

interpolation_xgrid = xgrid

interpolation_polynomial_degree = 4
lepton_pid = 11
pids = [21, 22, 2, 1, 3, 4, 5, 6, -2, -1, -3, -4, -5, -6]

   # init pineappl objects
lumi_entries = [
    pineappl.lumi.LumiEntry([(pid, lepton_pid, 1.0)]) for pid in pids
]
orders = [pineappl.grid.Order(o, 0, 0, 0) for o in [0, 1, 2]]
bins = 5
bin_limits = list(map(float, range(0, bins + 1)))
    # subgrid params
params = pineappl.subgrid.SubgridParams()
params.set_reweight(False)
params.set_x_bins(len(interpolation_xgrid))
params.set_x_max(interpolation_xgrid[-1])
params.set_x_min(interpolation_xgrid[0])
params.set_x_order(interpolation_polynomial_degree)

grid = pineappl.grid.Grid.create(lumi_entries, orders, bin_limits, params)
limits = []

for bin_, (x, q2) in enumerate([(0.1, 17.), (0.2, 17.), (0.3, 17.), (0.4, 17.), (0.5, 17.)]):
    interpolator_at_x = interpolator(x, bf)
    c2test = eval_c2('nnlo', x, True, bf, interpolator_at_x, 5)
    c2res = basis_transform(c2test)
    limits.append((q2, q2))
    limits.append((x, x))
    for o_index, order in enumerate(['lo', 'nlo', 'nnlo']):
        for p_index, partons in enumerate(['g', 'ph', 'u', 'd', 's', 'c', 'b', 't', 'ub', 'db', 'sb', 'cb', 'bb', 'tb']): 
            # import pdb; pdb.set_trace()
            inparr = np.array(c2res[order + '_' + partons], dtype=np.float64)
            if not any(inparr != 0.0):
                continue
            subgrid = pineappl.import_only_subgrid.ImportOnlySubgridV1(
                    inparr[np.newaxis, :, np.newaxis],
                    [q2],
                    interpolation_xgrid,
                    [1.0],
                )
            grid.set_subgrid(o_index, bin_, p_index, subgrid)

normalizations = [1.0] * bins
remapper = pineappl.bin.BinRemapper(normalizations, limits)
grid.set_remapper(remapper)
grid.set_key_value("initial_state_1", "2212")
grid.set_key_value("initial_state_2", str(lepton_pid))
grid.set_key_value("lumi_id_types", "pdg_mc_ids")
grid.set_key_value("y_label", "obsname")
grid.optimize()
grid.write('filename')