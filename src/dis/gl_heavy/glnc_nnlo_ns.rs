use crate::dis::internal::*;
use crate::dis::f2_heavy::{dq1_h4, ADLER_LOGXIS};
use crate::dis::fl_heavy::ADLER_FL_VV;
use crate::core::scits::cubic_spline::CubicSpline;
use std::sync::OnceLock;

fn adler_spline() -> &'static CubicSpline {
    static SPLINE: OnceLock<CubicSpline> = OnceLock::new();
    SPLINE.get_or_init(|| CubicSpline::new(&ADLER_LOGXIS, &ADLER_FL_VV))
}

pub fn r_00(x: f64, Q2: f64, pid: f64) -> f64 {
    let m2 = get_quark_mass(pid as i8).powi(2);
    if below_threshold(x, Q2, m2) {
        return 0.0;
    }
    let xi = Q2 / m2;
    let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;
    let prefac = Q2 / (pi * m2) / x * (4.0 * pi).powi(2);

    let (rho, beta, chi) = mof_eta(eta);
    let (rhop, betap, chip) = mof_prime(xi, eta);
    let h4 = dq1_h4(xi, eta);

    // dq1_gL_VA = -dq1_FL_VV
    -prefac * (rhop*(beta*(4.*rho*(-38. + 23.*rho) + (200. + 532.*rho)*rhop - 744.*pow(rhop,2)) + h4*(-108.*rho*pow(rhop,2) + 108.*pow(rhop,3)) + (18.*pow(rho,3) + 54.*pow(rho,2)*rhop - 108.*rho*pow(rhop,2))*ln(chi) + betap*(-48.*rho + (48. + 264.*rho)*rhop - 264.*pow(rhop,2))*ln((chi - chip)/(1. - chi*chip))))/(864.*pi*rho)
}

pub fn l_00(x: f64, Q2: f64, pid: f64) -> f64 {
    let m2 = get_quark_mass(pid as i8).powi(2);
    if below_threshold(x, Q2, m2) {
        return 0.0;
    }
    let xi = Q2 / m2;
    // Adler("gL","VA") = -Adler("FL","VV")
    adler_spline().ev(xi.log10())
}
