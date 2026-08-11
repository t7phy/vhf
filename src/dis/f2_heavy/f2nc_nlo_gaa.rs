use crate::dis::internal::*;

fn r_00(x: f64, Q2: f64, pid: f64, _nf: f64, _var: i8) -> f64 {

    let m2 = get_quark_mass(pid as i8).powi(2);
    
    let mut res: f64;
    if below_threshold(x, Q2, m2) {
        res = 0.0;
    } else {
        let xi = Q2 / m2;
        let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;
        let prefac = Q2 / (pi * m2);
        let (rho, beta, chi) = mof_eta(eta);
        let (rhoq, _betaq, _chiq) = mof_xi(xi);
        res = (beta*pi*rho*rhoq*(pow(rho,2) + pow(rhoq,2) + rho*rhoq*(6. + rhoq)))/(2.*pow(rho - rhoq,3)) + (pi*rho*rhoq*(6.*rho*pow(rhoq,2) - 2.*(-1. + rhoq)*pow(rhoq,2) + pow(rho,2)*(2. - (-2. + rhoq)*rhoq))*chi.ln())/(4.*pow(rho - rhoq,3));
        res *= prefac / x;
    }
    res
}
