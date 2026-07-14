use crate::dis::internal::*;
use crate::dis::f2_heavy::{dq1_h4, ADLER_LOGXIS, ADLER_F2_VV};
use crate::core::scits::cubic_spline::CubicSpline;
use std::sync::OnceLock;

fn adler_spline() -> &'static CubicSpline {
    static SPLINE: OnceLock<CubicSpline> = OnceLock::new();
    SPLINE.get_or_init(|| CubicSpline::new(&ADLER_LOGXIS, &ADLER_F2_VV))
}

pub fn r_00(x: f64, Q2: f64, pid: f64) -> f64 {
    let m2 = get_quark_mass(pid as i8).powi(2);
    if below_threshold(x, Q2, m2) {
        return 0.0;
    }
    let xi = Q2 / m2;
    let eta = (xi / 4.0 * (1.0 / x - 1.0) - 1.0).min(1e5);
    let prefac = Q2 / (pi * m2) / x * (4.0 * pi).powi(2);

    let (rho, beta, chi) = mof_eta(eta);
    let (rhop, betap, chip) = mof_prime(xi, eta);
    let h4 = dq1_h4(xi, eta);

    // dq1_g4_VA = -dq1_F2_VV
    -prefac * (beta*(2.*pow(rho,2)*(718. + 5.*rho) - 4.*rho*(758. + 91.*rho)*rhop + (2488. + 5108.*rho)*pow(rhop,2) - 6456.*pow(rhop,3)) + h4*(-288.*pow(rho,2) + 288.*rho*rhop + 36.*(-4. + 3.*pow(rho,2))*pow(rhop,2) - 972.*rho*pow(rhop,3) + 972.*pow(rhop,4)) + (27.*pow(rho,2)*(-8. + pow(rho,2)) + 18.*rho*(8. + 3.*pow(rho,2))*rhop + 486.*pow(rho,2)*pow(rhop,2) - 972.*rho*pow(rhop,3))*ln(chi) + betap*(912.*pow(rho,2) - 24.*rho*(56. + 23.*rho)*rhop + 48.*(17. + 52.*rho)*pow(rhop,2) - 2256.*pow(rhop,3))*ln((chi - chip)/(1. - chi*chip)))/(5184.*pi*rho)
}

pub fn l_00(x: f64, Q2: f64, pid: f64) -> f64 {
    let m2 = get_quark_mass(pid as i8).powi(2);
    if below_threshold(x, Q2, m2) {
        return 0.0;
    }
    let xi = Q2 / m2;
    // Adler("g4","VA") = -Adler("F2","VV")
    adler_spline().ev(xi.log10())
}
