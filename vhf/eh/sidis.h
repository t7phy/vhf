#ifndef SIDIS_H
#define SIDIS_H

#include "../core/global_import.h"

const int LMUR = 1;
const int LMUF = 1;
const int LMUA = 1;

// C_T
double ct_lo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double ct_nlo_g2q_eq(double x, double z, double Q, int rsl, int orders);
double ct_nlo_q2g_eq(double x, double z, double Q, int rsl, int orders);
double ct_nlo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_g2g_eq(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_g2q_eq(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_q2g_eq(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_q2q_eqp(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_q2qb_eq(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_q2qp_eq(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_q2qp_eqp(double x, double z, double Q, int rsl, int orders);
double ct_nnlo_q2qp_es(double x, double z, double Q, int rsl, int orders);

// C_L
double cl_lo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double cl_nlo_g2q_eq(double x, double z, double Q, int rsl, int orders);
double cl_nlo_q2g_eq(double x, double z, double Q, int rsl, int orders);
double cl_nlo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_g2g_eq(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_g2q_eq(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_q2g_eq(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_q2q_eqp(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_q2qb_eq(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_q2qp_eq(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_q2qp_eqp(double x, double z, double Q, int rsl, int orders);
double cl_nnlo_q2qp_es(double x, double z, double Q, int rsl, int orders);

// C_P
double cp_lo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double cp_nlo_g2q_eq(double x, double z, double Q, int rsl, int orders);
double cp_nlo_q2g_eq(double x, double z, double Q, int rsl, int orders);
double cp_nlo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_g2g_eq(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_g2q_eq(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_q2g_eq(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_q2q_eq(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_q2q_eqp(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_q2qb_eq(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_q2qp_eq(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_q2qp_eqp(double x, double z, double Q, int rsl, int orders);
double cp_nnlo_q2qp_es(double x, double z, double Q, int rsl, int orders);

#endif // SIDIS_H