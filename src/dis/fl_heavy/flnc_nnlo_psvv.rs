use crate::dis::internal::*;
use crate::dis::dis_ext::leprohq_grids::cq1_fl_vv_bulk::cq1_fl_vv_bulk_spline as grid;
use crate::dis::dis_ext::leprohq_grids::cq1_fl_vv_bulk::{CQ1_FL_VV_BULK_X, CQ1_FL_VV_BULK_Y};
use crate::dis::dis_ext::leprohq_funcs::{cq1t_fl_vv, cq1hv_fl};

const LNETA_TH_MIX: f64 = 0.0; // ln(1e0)
const LNXI_HV_MIX: f64 = 7.3132203482534845;

pub fn r_00(x: f64, Q2: f64, pid: f64, _nf: f64, _var: i8) -> f64 {
    let m2 = get_quark_mass(pid as i8).powi(2);
    if below_threshold(x, Q2, m2) {
        return 0.0;
    }
    let xi = Q2 / m2;
    let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;
    let prefac = Q2 / (pi * m2) / x * (4.0 * pi).powi(2);

    let (rho, beta, chi) = mof_eta(eta);
    let (rhoq, betaq, chiq) = mof_xi(xi);

    // cqBarF1_FL_VV (no h1 dependency)
    let cqbarf1 = (256.*chi*chiq*(-2.*beta*(-1. + rhoq)*rhoq*(2.*rho*pow(rhoq,2) + (2. - 3.*rhoq)*pow(rhoq,2) + pow(rho,2)*(-6. + 5.*rhoq)) - 4.*pow(rho,2)*pow(-1. + rhoq,2)*(rho*(-3. + rhoq) + 3.*rhoq)*ln(chi) + betaq*(-rho + rhoq)*(2.*rho*pow(rhoq,2) + pow(rhoq,3)*(-4. + 3.*rhoq) + pow(rho,2)*(12. + rhoq*(-22. + 9.*rhoq)))*ln((chi + chiq)/(1. + chi*chiq))))/(9.*(-1. + beta)*pow(1. + beta,5)*pow(1. + betaq,8)*pow(chi + chiq,3)*pow(1. + chi*chiq,3)*pow(1. - pow(chiq,2),2)*pi*(-1. + rhoq));

    let lneta = eta.ln();
    let lnxi = xi.ln();
    let lneta_min = CQ1_FL_VV_BULK_X[0];
    let lnxi_max = CQ1_FL_VV_BULK_Y[CQ1_FL_VV_BULK_Y.len() - 1];

    let cq1 = if lneta < lneta_min {
        cq1t_fl_vv(xi, eta)
    } else if lnxi > lnxi_max {
        cq1hv_fl(xi, eta)
    } else if lneta >= LNETA_TH_MIX && lnxi <= LNXI_HV_MIX {
        grid().ev(lneta, lnxi)
    } else if lnxi <= LNXI_HV_MIX {
        let b = grid().ev(lneta, lnxi);
        let tp = cq1t_fl_vv(xi, eta);
        (tp * (lneta - LNETA_TH_MIX) + b * (lneta_min - lneta)) / (lneta_min - LNETA_TH_MIX)
    } else {
        let b = grid().ev(lneta, lnxi);
        let hv = cq1hv_fl(xi, eta);
        (hv * (LNXI_HV_MIX - lnxi) + b * (lnxi - lnxi_max)) / (LNXI_HV_MIX - lnxi_max)
    };

    prefac * (cq1 + cqbarf1 * lnxi)
}
