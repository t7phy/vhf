use crate::dis::internal::*;
use crate::dis::f2_heavy::fh_grids::cg1_fl_aa_bulk::cg1_fl_aa_bulk_spline as grid;
use crate::dis::f2_heavy::fh_grids::cg1_fl_aa_bulk::{CG1_FL_AA_BULK_X, CG1_FL_AA_BULK_Y};
use crate::dis::f2_heavy::{cgbar1_h1, cgbar1_h2, cgbar1_h3};
use crate::dis::fl_heavy::{cg1t_fl_aa, cg1hv_fl};

const LNETA_TH_MIX: f64 = -2.302585092994046;
const LNXI_HV_MIX: f64 = 7.3132203482534845;

pub fn r_00(x: f64, Q2: f64, pid: f64) -> f64 {
    let m2 = get_quark_mass(pid as i8).powi(2);
    if below_threshold(x, Q2, m2) {
        return 0.0;
    }
    let xi = Q2 / m2;
    let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;
    let prefac = Q2 / (pi * m2) / x * (4.0 * pi).powi(2);

    let (rho, beta, chi) = mof_eta(eta);
    let (rhoq, betaq, chiq) = mof_xi(xi);

    let h1 = cgbar1_h1(chi, chiq);
    let h2 = cgbar1_h2(chi, chiq);
    let h3 = cgbar1_h3(chi, chiq);

    let cgbar1 = (8.*chi*chiq*(192.*beta*h3*pow(rho,2)*(-1. + rhoq)*rhoq*(2. + rhoq) + 48.*h1*rho*(rho - rhoq)*(-1. + rhoq)*rhoq*(3.*rho + rhoq) + 48.*h2*rho*(-1. + rhoq)*rhoq*(pow(rho,2)*(-1. + rhoq) - 4.*rho*rhoq + pow(rhoq,2)) + 2.*beta*(-1. + rhoq)*rhoq*(-288.*pow(rho,2) - 184.*pow(rho,2)*rhoq + (16. + 9.*(-2. + rho)*rho)*pow(rhoq,2)) - rho*(-1. + rhoq)*(-384.*pow(rho,2) + 8.*rho*(24. + 35.*rho)*rhoq - 112.*(-3. + rho)*rho*pow(rhoq,2) + 3.*(-4. + rho)*(4. + 3.*rho)*pow(rhoq,3))*ln(chi) - 32.*betaq*(rho - rhoq)*(2.*rho*pow(rhoq,2) - pow(rhoq,3) + pow(rho,2)*(-12. + 11.*rhoq))*ln((chi + chiq)/(1. + chi*chiq))))/((-1. + beta)*pow(1. + beta,5)*pow(1. + betaq,8)*pow(chi + chiq,3)*pow(1. + chi*chiq,3)*pow(1. - pow(chiq,2),2)*pi);

    let lneta = eta.ln();
    let lnxi = xi.ln();
    let lneta_min = CG1_FL_AA_BULK_X[0];
    let lnxi_max = CG1_FL_AA_BULK_Y[CG1_FL_AA_BULK_Y.len() - 1];

    let cg1 = if lneta < lneta_min {
        cg1t_fl_aa(xi, eta)
    } else if lnxi > lnxi_max {
        cg1hv_fl(xi, eta)
    } else if lneta >= LNETA_TH_MIX && lnxi <= LNXI_HV_MIX {
        grid().ev(lneta, lnxi)
    } else if lnxi <= LNXI_HV_MIX {
        let b = grid().ev(lneta, lnxi);
        let tp = cg1t_fl_aa(xi, eta);
        (tp * (lneta - LNETA_TH_MIX) + b * (lneta_min - lneta)) / (lneta_min - LNETA_TH_MIX)
    } else {
        let b = grid().ev(lneta, lnxi);
        let hv = cg1hv_fl(xi, eta);
        (hv * (LNXI_HV_MIX - lnxi) + b * (lnxi - lnxi_max)) / (LNXI_HV_MIX - lnxi_max)
    };

    prefac * (cg1 + cgbar1 * lnxi)
}
