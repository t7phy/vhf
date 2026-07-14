use crate::dis::internal::*;
use crate::dis::f2_heavy::fh_grids::cg1_f2_vv_bulk::cg1_f2_vv_bulk_spline as grid;
use crate::dis::f2_heavy::fh_grids::cg1_f2_vv_bulk::{CG1_F2_VV_BULK_X, CG1_F2_VV_BULK_Y};
use crate::dis::f2_heavy::{cg1t_f2_vv, cg1hv_f2};

const LNETA_TH_MIX: f64 = -2.302585092994046; // ln(1e-1)
const LNXI_HV_MIX: f64 = 7.3132203482534845;  // ln(1.5e3)

pub fn r_00(x: f64, Q2: f64, pid: f64) -> f64 {

    // let m2 = get_quark_mass(pid as i8).powi(2);
    let m2 = pid;

    let mut res: f64;
    if below_threshold(x, Q2, m2) {
        res = 0.0;
    } else {
        let xi = Q2 / m2;
        let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;

        let prefac = Q2 / (pi * m2) / x * (4.0 * pi).powi(2);

        let (rho, beta, chi) = mof_eta(eta);
        let (rhoq, betaq, chiq) = mof_xi(xi);

        // log part
        let h1 = -pow(pi,2)/6. - 2.*Li2(-chi) + Li2((1. - chiq)/(1. + chi)) - Li2((chi*(1. - chiq))/(1. + chi)) - Li2(-((chi*(1. - chiq))/((1. + chi)*chiq))) + Li2((-1. + chiq)/((1. + chi)*chiq)) + pow(ln(chi),2)/2. + ln(chi)*(ln(chiq) - ln(chi + chiq) - ln(1. + chi*chiq));
        let h2 = -pow(pi,2)/6. + 2.*Li2(-chi) + 2.*Li2(chi) - ln(chi)/2. - ln(chi)*(ln(chiq) - ln(chi + chiq) - ln(1. + chi*chiq));
        let h3 = ln(1. - chi) + ln(1. + chi) + (-ln(chi) + ln(chiq) - ln(chi + chiq) - ln(1. + chi*chiq))/2.;

        let cgbar1 = (8.*chi*chiq*(96.*beta*h3*rho*(-1. + rhoq)*(pow(rho,2) + pow(rhoq,2) + rho*rhoq*(6. + rhoq)) + 48.*h1*rho*(rho - rhoq)*(-1. + rhoq)*(-rhoq + rho*(5. + 2.*rhoq)) + 2.*beta*(-1. + rhoq)*rhoq*(62.*rho*rhoq + 8.*pow(rhoq,2) - pow(rho,2)*(632. + 95.*rhoq)) + 24.*h2*rho*(-1. + rhoq)*(-2.*pow(rhoq,2) - 2.*rho*pow(rhoq,2) + pow(rho,2)*(-2. + (-4. + rhoq)*rhoq)) + rho*(-1. + rhoq)*(568.*pow(rho,2) - 48.*rho*(11. + 8.*rho)*rhoq + (48. + rho*(-96. + 59.*rho))*pow(rhoq,2))*ln(chi) - 8.*betaq*(rho - rhoq)*(-2.*rho*rhoq*(4. + rhoq) + pow(rhoq,2)*(4. + rhoq) + pow(rho,2)*(-68. + 73.*rhoq))*ln((chi + chiq)/(1. + chi*chiq))))/((-1. + beta)*pow(1. + beta,5)*pow(1. + betaq,8)*pow(chi + chiq,3)*pow(1. + chi*chiq,3)*pow(1. - pow(chiq,2),2)*pi);

        // log independent part
        let mut cg1: f64;
        let lneta = eta.ln();
        let lnxi = xi.ln();

        let lneta_min = CG1_F2_VV_BULK_X[0];
        let lnxi_max = CG1_F2_VV_BULK_Y[CG1_F2_VV_BULK_Y.len() - 1];

        if lneta < lneta_min {
            cg1 = cg1t_f2_vv(xi, eta);
        } else if lnxi > lnxi_max {
            cg1 = cg1hv_f2(xi, eta);
        } else if lneta >= LNETA_TH_MIX && lnxi <= LNXI_HV_MIX {
            cg1 = grid().ev(lneta, lnxi);
        } else if lnxi <= LNXI_HV_MIX {
            let b = grid().ev(lneta, lnxi);
            let tp = cg1t_f2_vv(xi, eta);
            cg1 = (tp * (lneta - LNETA_TH_MIX) + b * (lneta_min - lneta))
                / (lneta_min - LNETA_TH_MIX);
        } else {
            let b = grid().ev(lneta, lnxi);
            let hv = cg1hv_f2(xi, eta);
            cg1 = (hv * (LNXI_HV_MIX - lnxi) + b * (lnxi - lnxi_max))
                / (LNXI_HV_MIX - lnxi_max);
        }

        // combine everything
        res = prefac * (cg1 + cgbar1 * lnxi);
    }
    res
}