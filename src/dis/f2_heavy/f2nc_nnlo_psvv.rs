use crate::dis::internal::*;
use crate::dis::dis_ext::leprohq_grids::cq1_f2_vv_bulk::cq1_f2_vv_bulk_spline as grid;
use crate::dis::dis_ext::leprohq_grids::cq1_f2_vv_bulk::{CQ1_F2_VV_BULK_X, CQ1_F2_VV_BULK_Y};
use crate::dis::dis_ext::leprohq_funcs::{cgbar1_h1, cq1t_f2_vv, cq1hv_f2};

const LNETA_TH_MIX: f64 = 0.0; // ln(1e0)
const LNXI_HV_MIX: f64 = 7.3132203482534845; // ln(1.5e3)

pub fn r_00(x: f64, Q2: f64, pid: f64, _nf: f64, _var: i8) -> f64 {

    let m2 = get_quark_mass(pid as i8).powi(2);

    let res: f64;
    if below_threshold(x, Q2, m2) {
        res = 0.0;
    } else {
        let xi = Q2 / m2;
        let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;

        let prefac = Q2 / (pi * m2) / x * (4.0 * pi).powi(2);

        let (rho, beta, chi) = mof_eta(eta);
        let (rhoq, betaq, chiq) = mof_xi(xi);

        // log part (cqBarF1_F2_VV)
        let h1 = cgbar1_h1(chi, chiq);

        let cqbarf1 = (256.*chi*chiq*(3.*h1*rho*(rho - rhoq)*(-1. + rhoq)*(-2.*rhoq + rho*(4. + rhoq)) - 2.*beta*(-1. + rhoq)*rhoq*(-7.*rho*rhoq - pow(rhoq,2) + pow(rho,2)*(16. + rhoq)) + rho*(-1. + rhoq)*(-21.*rho*rhoq + 3.*pow(rhoq,2) + pow(rho,2)*(14. + (-6. + rhoq)*rhoq))*ln(chi) + betaq*(-rho + rhoq)*(-2.*rho*rhoq*(4. + rhoq) + pow(rhoq,2)*(4. + rhoq) + pow(rho,2)*(-14. + 19.*rhoq))*ln((chi + chiq)/(1. + chi*chiq))))/(9.*(-1. + beta)*pow(1. + beta,5)*pow(1. + betaq,8)*pow(chi + chiq,3)*pow(1. + chi*chiq,3)*pow(1. - pow(chiq,2),2)*pi);

        // log independent part
        let cq1: f64;
        let lneta = eta.ln();
        let lnxi = xi.ln();

        let lneta_min = CQ1_F2_VV_BULK_X[0];
        let lnxi_max = CQ1_F2_VV_BULK_Y[CQ1_F2_VV_BULK_Y.len() - 1];

        if lneta < lneta_min {
            cq1 = cq1t_f2_vv(xi, eta);
        } else if lnxi > lnxi_max {
            cq1 = cq1hv_f2(xi, eta);
        } else if lneta >= LNETA_TH_MIX && lnxi <= LNXI_HV_MIX {
            cq1 = grid().ev(lneta, lnxi);
        } else if lnxi <= LNXI_HV_MIX {
            let b = grid().ev(lneta, lnxi);
            let tp = cq1t_f2_vv(xi, eta);
            cq1 = (tp * (lneta - LNETA_TH_MIX) + b * (lneta_min - lneta))
                / (lneta_min - LNETA_TH_MIX);
        } else {
            let b = grid().ev(lneta, lnxi);
            let hv = cq1hv_f2(xi, eta);
            cq1 = (hv * (LNXI_HV_MIX - lnxi) + b * (lnxi - lnxi_max))
                / (LNXI_HV_MIX - lnxi_max);
        }

        // combine everything
        res = prefac * (cq1 + cqbarf1 * lnxi);
    }
    res
}
