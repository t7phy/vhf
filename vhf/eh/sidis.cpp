#include "sidis.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(eh, m) {
    // C_T
    m.def("ct_lo_q2q_eq", &ct_lo_q2q_eq);
    m.def("ct_nlo_g2q_eq", &ct_nlo_g2q_eq);
    m.def("ct_nlo_q2g_eq", &ct_nlo_q2g_eq);
    m.def("ct_nlo_q2q_eq", &ct_nlo_q2q_eq);
    m.def("ct_nnlo_g2g_eq", &ct_nnlo_g2g_eq);
    m.def("ct_nnlo_g2q_eq", &ct_nnlo_g2q_eq);
    m.def("ct_nnlo_q2g_eq", &ct_nnlo_q2g_eq);
    m.def("ct_nnlo_q2q_eq", &ct_nnlo_q2q_eq);
    m.def("ct_nnlo_q2q_eqp", &ct_nnlo_q2q_eqp);
    m.def("ct_nnlo_q2qb_eq", &ct_nnlo_q2qb_eq);
    m.def("ct_nnlo_q2qp_eq", &ct_nnlo_q2qp_eq);
    m.def("ct_nnlo_q2qp_eqp", &ct_nnlo_q2qp_eqp);
    m.def("ct_nnlo_q2qp_es", &ct_nnlo_q2qp_es);

    // C_L
    m.def("cl_lo_q2q_eq", &cl_lo_q2q_eq);
    m.def("cl_nlo_g2q_eq", &cl_nlo_g2q_eq);
    m.def("cl_nlo_q2g_eq", &cl_nlo_q2g_eq);
    m.def("cl_nlo_q2q_eq", &cl_nlo_q2q_eq);
    m.def("cl_nnlo_g2g_eq", &cl_nnlo_g2g_eq);
    m.def("cl_nnlo_g2q_eq", &cl_nnlo_g2q_eq);
    m.def("cl_nnlo_q2g_eq", &cl_nnlo_q2g_eq);
    m.def("cl_nnlo_q2q_eq", &cl_nnlo_q2q_eq);
    m.def("cl_nnlo_q2q_eqp", &cl_nnlo_q2q_eqp);
    m.def("cl_nnlo_q2qb_eq", &cl_nnlo_q2qb_eq);
    m.def("cl_nnlo_q2qp_eq", &cl_nnlo_q2qp_eq);
    m.def("cl_nnlo_q2qp_eqp", &cl_nnlo_q2qp_eqp);
    m.def("cl_nnlo_q2qp_es", &cl_nnlo_q2qp_es);

    // C_P
    m.def("cp_lo_q2q_eq", &cp_lo_q2q_eq);
    m.def("cp_nlo_g2q_eq", &cp_nlo_g2q_eq);
    m.def("cp_nlo_q2g_eq", &cp_nlo_q2g_eq);
    m.def("cp_nlo_q2q_eq", &cp_nlo_q2q_eq);
    m.def("cp_nnlo_g2g_eq", &cp_nnlo_g2g_eq);
    m.def("cp_nnlo_g2q_eq", &cp_nnlo_g2q_eq);
    m.def("cp_nnlo_q2g_eq", &cp_nnlo_q2g_eq);
    m.def("cp_nnlo_q2q_eq", &cp_nnlo_q2q_eq);
    m.def("cp_nnlo_q2q_eqp", &cp_nnlo_q2q_eqp);
    m.def("cp_nnlo_q2qb_eq", &cp_nnlo_q2qb_eq);
    m.def("cp_nnlo_q2qp_eq", &cp_nnlo_q2qp_eq);
    m.def("cp_nnlo_q2qp_eqp", &cp_nnlo_q2qp_eqp);
    m.def("cp_nnlo_q2qp_es", &cp_nnlo_q2qp_es);
}