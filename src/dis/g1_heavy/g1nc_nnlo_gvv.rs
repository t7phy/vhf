use crate::dis::internal::*;
use crate::dis::f2_heavy::fh_grids::cg1_x2g1_vv_bulk::cg1_x2g1_vv_bulk_spline as grid;
use crate::dis::f2_heavy::fh_grids::cg1_x2g1_vv_bulk::{CG1_X2G1_VV_BULK_X, CG1_X2G1_VV_BULK_Y};
use crate::dis::f2_heavy::{cgbar1_h1, cgbar1_h2, cgbar1_h3};
use crate::dis::g1_heavy::cg1t_x2g1_vv;

const LNETA_TH_MIX: f64 = -2.302585092994046; // ln(1e-1)
const LNXI_HV_MIX: f64 = 7.3132203482534845;  // ln(1.5e3)

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

    let cgbar1 = (192.*chi*chiq*(-1. + rhoq)*(4.*h1*rho*(rho - rhoq)*(2.*rho - rhoq) + 32.*beta*rho*rhoq*(-rho + rhoq) - 2.*h2*rho*(rho - rhoq)*(rho + rhoq) + 4.*beta*h3*rho*(rho - rhoq)*(rho + 3.*rhoq) - rho*(rho - rhoq)*(11.*rhoq + rho*(-13. + 4.*rhoq))*ln(chi) - 4.*betaq*rho*(3.*pow(rho,2) - 4.*rho*rhoq + pow(rhoq,2))*ln((chi + chiq)/(1. + chi*chiq))))/((-1. + beta)*pow(1. + beta,5)*pow(1. + betaq,8)*pow(chi + chiq,3)*pow(1. + chi*chiq,3)*pow(1. - pow(chiq,2),2)*pi);

    let lneta = eta.ln();
    let lnxi = xi.ln();
    let lneta_min = CG1_X2G1_VV_BULK_X[0];
    let lnxi_max = CG1_X2G1_VV_BULK_Y[CG1_X2G1_VV_BULK_Y.len() - 1];

    let cg1 = if lneta < lneta_min {
        cg1t_x2g1_vv(xi, eta)
    } else if lnxi > lnxi_max {
        panic!("High virtuality limit not available for x2g1")
    } else if lneta >= LNETA_TH_MIX && lnxi <= LNXI_HV_MIX {
        grid().ev(lneta, lnxi)
    } else if lnxi <= LNXI_HV_MIX {
        let b = grid().ev(lneta, lnxi);
        let tp = cg1t_x2g1_vv(xi, eta);
        (tp * (lneta - LNETA_TH_MIX) + b * (lneta_min - lneta)) / (lneta_min - LNETA_TH_MIX)
    } else {
        panic!("High virtuality limit not available for x2g1")
    };

    prefac * (cg1 + cgbar1 * lnxi)
}
