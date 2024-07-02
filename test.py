from eh.unpol.nnlo import *
from dev.sidis_reorder_code.step1_unpol.ordered.python import (c2tg2geq, c2lg2geq, c2lg2qeq, c2lq2geq, c2lq2qeq, c2lq2qeqp, c2tq2qpeqp, c2lq2qbeq, c2lq2qpbes, c2tq2qpes, c2tq2qpeq, c2tq2qpbes, c2tq2qeqp, c2tq2qeq, c2tq2qbeq, c2tq2geq, c2tg2qeq, c2lq2qpes, c2lq2qpeqp, c2lq2qpeq)

x_list = [0.00001, 0.00012, 0.00123, 0.01234, 0.12345, 0.2, 0.5, 0.9]
z_list = [0.001, 0.002, 0.012, 0.123, 0.2, 0.5, 0.9]

rsl_list = ['rr', 'rs', 'rl', 'sr', 'ss', 'sl', 'lr', 'ls', 'll']
sv_list = ['000', '001', '010', '100', '011', '101', '110', '002', '020']

func_list = [
    (ct.c2t_g2g_eq.ct_nnlo_g2g_eq, c2tg2geq.C2Tg2gEq),
    (ct.c2t_g2q_eq.ct_nnlo_g2q_eq, c2tg2qeq.C2Tg2qEq),
    (ct.c2t_q2g_eq.ct_nnlo_q2g_eq, c2tq2geq.C2Tq2gEq),
    (ct.c2t_q2q_eq.ct_nnlo_q2q_eq, c2tq2qeq.C2Tq2qEq),
    (ct.c2t_q2q_eqp.ct_nnlo_q2q_eqp, c2tq2qeqp.C2Tq2qEqp),
    (ct.c2t_q2qb_eq.ct_nnlo_q2qb_eq, c2tq2qbeq.C2Tq2qbEq),
    (ct.c2t_q2qp_eq.ct_nnlo_q2qp_eq, c2tq2qpeq.C2Tq2qpEq),
    (ct.c2t_q2qp_eqp.ct_nnlo_q2qp_eqp, c2tq2qpeqp.C2Tq2qpEqp),
    (ct.c2t_q2qp_es.ct_nnlo_q2qp_es, c2tq2qpes.C2Tq2qpEs),
    (ct.c2t_q2qpb_es.ct_nnlo_q2qpb_es, c2tq2qpbes.C2Tq2qpbEs),
    (cl.c2l_g2g_eq.cl_nnlo_g2g_eq, c2lg2geq.C2Lg2gEq),
    (cl.c2l_g2q_eq.cl_nnlo_g2q_eq, c2lg2qeq.C2Lg2qEq),
    (cl.c2l_q2g_eq.cl_nnlo_q2g_eq, c2lq2geq.C2Lq2gEq),
    (cl.c2l_q2q_eq.cl_nnlo_q2q_eq, c2lq2qeq.C2Lq2qEq),
    (cl.c2l_q2q_eqp.cl_nnlo_q2q_eqp, c2lq2qeqp.C2Lq2qEqp),
    (cl.c2l_q2qb_eq.cl_nnlo_q2qb_eq, c2lq2qbeq.C2Lq2qbEq),
    (cl.c2l_q2qp_eq.cl_nnlo_q2qp_eq, c2lq2qpeq.C2Lq2qpEq),
    (cl.c2l_q2qp_eqp.cl_nnlo_q2qp_eqp, c2lq2qpeqp.C2Lq2qpEqp),
    (cl.c2l_q2qp_es.cl_nnlo_q2qp_es, c2lq2qpes.C2Lq2qpEs),
    (cl.c2l_q2qpb_es.cl_nnlo_q2qpb_es, c2lq2qpbes.C2Lq2qpbEs)
]

func_list_debug = [
    (ct.c2t_g2q_eq.ct_nnlo_g2q_eq, c2tg2qeq.C2Tg2qEq),
]

flist = func_list

def tests():
    for x in x_list:
        for z in z_list:
            print('x = ', x, '    z = ', z)
            for rsl in rsl_list:
                for sv in sv_list:
                    for i in range(len(flist)):
                        m = (flist[i][0](x, z, rsl, sv)).real
                        a = flist[i][1](x, z, rsl, sv).real
                        if m == 0 and a == 0:
                            continue
                        p_diff = (m-a)/m * 100
                        if p_diff > 1e-9:
                            print('diff = ', p_diff, ' %')
                            print('x = ', x, ' z = ', z, ' rsl = ', rsl, ' sv = ', sv)
                            print('manual = ', m)
                            print('auto = ', a)
                            print('func = ', flist[i][1])
                            print('')
                    
tests()