use crate::dis::internal::*;

pub fn r_00(x: f64, Q2: f64, pid: f64) -> f64 {
    let m2 = get_quark_mass(pid as i8).powi(2);
    if below_threshold(x, Q2, m2) {
        return 0.0;
    }
    let xi = Q2 / m2;
    let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;
    let prefac = Q2 / (pi * m2);
    let (rho, beta, chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    prefac / x * ((beta*pi*pow(rho,2)*pow(rhoq,2)*(2. + rhoq))/pow(rho - rhoq,3) - (pi*rho*pow(rhoq,2)*(pow(rho,2)*(-1. + rhoq) - 4.*rho*rhoq + pow(rhoq,2))*ln(chi))/(2.*pow(rho - rhoq,3)))
}
