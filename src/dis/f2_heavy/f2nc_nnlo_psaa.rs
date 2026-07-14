use crate::dis::internal::*;
use crate::dis::f2_heavy::fh_grids::cq1_f2_aa_bulk::cq1_f2_aa_bulk_spline as grid;
use crate::dis::f2_heavy::fh_grids::cq1_f2_aa_bulk::{CQ1_F2_AA_BULK_X, CQ1_F2_AA_BULK_Y};
use crate::dis::f2_heavy::{cgbar1_h1, cq1t_f2_aa, cq1hv_f2};

const LNETA_TH_MIX: f64 = 0.0; // ln(1e0)
const LNXI_HV_MIX: f64 = 7.3132203482534845; // ln(1.5e3)

pub fn r_00(x: f64, Q2: f64, pid: f64) -> f64 {

    let m2 = get_quark_mass(pid as i8).powi(2);

    let mut res: f64;
    if below_threshold(x, Q2, m2) {
        res = 0.0;
    } else {
        let xi = Q2 / m2;
        let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;

        let prefac = Q2 / (pi * m2) / x * (4.0 * pi).powi(2);

        let (rho, beta, chi) = mof_eta(eta);
        let (rhoq, betaq, chiq) = mof_xi(xi);

        // log part (cqBarF1_F2_AA)
        let h1 = cgbar1_h1(chi, chiq);

        let cqbarf1 = (256.*chi*chiq*(-3.*h1*rho*(rho - rhoq)*(-1. + rhoq)*(rho*(-4. + rhoq) - 2.*(-1. + rhoq)*rhoq) + beta*(-1. + rhoq)*rhoq*(pow(rho,2)*(-32. + rhoq) + rho*(14. - 3.*rhoq)*rhoq + 2.*pow(rhoq,2)) + (rho*(-1. + rhoq)*(6.*pow(rhoq,2)*(1. + rhoq) + 3.*rho*rhoq*(-14. + (-6. + rhoq)*rhoq) - pow(rho,2)*(-28. + pow(rhoq,2)))*ln(chi))/2. + betaq*(pow(rho,3)*(14. - 13.*rhoq) + 3.*pow(rho,2)*(-2. + rhoq)*rhoq + (4. - 5.*rhoq)*pow(rhoq,3) + 3.*rho*pow(rhoq,2)*(-4. + 5.*rhoq))*ln((chi + chiq)/(1. + chi*chiq))))/(9.*(-1. + beta)*pow(1. + beta,5)*pow(1. + betaq,8)*pow(chi + chiq,3)*pow(1. + chi*chiq,3)*pow(1. - pow(chiq,2),2)*pi);

        // log independent part
        let mut cq1: f64;
        let lneta = eta.ln();
        let lnxi = xi.ln();

        let lneta_min = CQ1_F2_AA_BULK_X[0];
        let lnxi_max = CQ1_F2_AA_BULK_Y[CQ1_F2_AA_BULK_Y.len() - 1];

        if lneta < lneta_min {
            cq1 = cq1t_f2_aa(xi, eta);
        } else if lnxi > lnxi_max {
            cq1 = cq1hv_f2(xi, eta);
        } else if lneta >= LNETA_TH_MIX && lnxi <= LNXI_HV_MIX {
            cq1 = grid().ev(lneta, lnxi);
        } else if lnxi <= LNXI_HV_MIX {
            let b = grid().ev(lneta, lnxi);
            let tp = cq1t_f2_aa(xi, eta);
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
