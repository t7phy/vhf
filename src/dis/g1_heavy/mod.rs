pub mod g1nc_nlo_gvv;
pub mod g1nc_nlo_gaa;
pub mod g1nc_nnlo_gvv;
pub mod g1nc_nnlo_gaa;
pub mod g1nc_nnlo_psvv;
pub mod g1nc_nnlo_psaa;
pub mod g1nc_nnlo_ns;

use crate::dis::internal::*;
use crate::dis::f2_heavy::{ADLER_LOGXIS};

// ── Gluon LO threshold limit (same for VV and AA) ─────────────────────

pub fn cg0t_x2g1(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    pi / 2.0 * rhoq / (rhoq - 1.0) * beta
}

// ── Gluon NLO resummation coefficients (x2g1-specific a10) ────────────

fn cg1_a10_g1(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    (-pow(pi, 2) / 2. + Li2(-(rhoq / (-2. + rhoq)))
        - (2. * (1. - rhoq) * ln(chiq)) / betaq
        - (3. * pow(ln(chiq), 2)) / 2.
        + pow(ln(rhoq / (-2. + rhoq)), 2) / 2.)
        / 8.
}

fn cg1_a10_g2(xi: f64) -> f64 {
    let (rhoq, _betaq, chiq) = mof_xi(xi);
    (12.5 - 15. * rln2 + 9. * pow(rln2, 2) + pow(ln(chiq), 2)
        - pow(ln(rhoq / (2. * (-1. + rhoq))), 2))
        / 4.
}

// x2g1 VV OK = F2 VV OK (identical expression)
pub fn cg1_a10_x2g1_vv_ok(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    let g2 = cg1_a10_g2(xi);
    g1 + g2 - (pow(pi, 2) * rhoq) / (32. * (-1. + rhoq))
        + ((-5. + (7. - 2. * rhoq) * rhoq) * ln(chiq)) / (8. * betaq * (-1. + rhoq))
        - (rhoq * pow(ln(chiq), 2)) / (32. * (-1. + rhoq))
        - ((-3. + rhoq) * ln(rhoq / (2. * (-1. + rhoq)))) / (4. * (-2. + rhoq))
}

// x2g1 VV QED = F2 VV QED (identical expression)
pub fn cg1_a10_x2g1_vv_qed(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    -(g1 / (-1. + rhoq))
        + (pow(pi, 2) * (-4. + 3. * rhoq)) / (96. * (-1. + rhoq))
        - (-9. + 5. * rhoq) / (8. * (-2. + rhoq))
        - ln(chiq) / (8. * betaq)
        + ((-4. + rhoq) * pow(ln(chiq), 2)) / (32. * (-1. + rhoq))
        + ((-3. + (5. - 2. * rhoq) * rhoq) * ln(rhoq / (2. * (-1. + rhoq))))
            / (4. * pow(-2. + rhoq, 2) * (-1. + rhoq))
}

pub fn cg1_a10_x2g1_aa_ok(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    let g2 = cg1_a10_g2(xi);
    g2 + g1 / pow(-1. + rhoq, 2)
        + (pow(pi, 2) * (11. - 7. * rhoq) * rhoq) / (96. * pow(-1. + rhoq, 2))
        + (3. * ln(chiq)) / (8. * betaq)
        + ((9. - 5. * rhoq) * rhoq * pow(ln(chiq), 2)) / (32. * pow(-1. + rhoq, 2))
        + ((1. + rhoq * (-5. - 2. * (-3. + rhoq) * rhoq)) * ln(rhoq / (2. * (-1. + rhoq))))
            / (4. * (-2. + rhoq) * pow(-1. + rhoq, 2))
}

pub fn cg1_a10_x2g1_aa_qed(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    (5. - 2. * rhoq) / (8. * (-2. + rhoq))
        + (g1 * (1. + (-4. + rhoq) * rhoq)) / pow(-1. + rhoq, 2)
        + (pow(pi, 2) * (4. + rhoq * (-19. + 7. * rhoq))) / (96. * pow(-1. + rhoq, 2))
        + ((-2. + (5. - 2. * rhoq) * rhoq) * ln(chiq)) / (8. * betaq * (-2. + rhoq))
        + ((4. + rhoq * (-17. + 5. * rhoq)) * pow(ln(chiq), 2)) / (32. * pow(-1. + rhoq, 2))
        + ((1. + (-2. + rhoq) * rhoq * (-3. + 2. * rhoq)) * ln(rhoq / (2. * (-1. + rhoq))))
            / (4. * pow(-2. + rhoq, 2) * (-1. + rhoq))
}

// ── Gluon NLO threshold limits ─────────────────────────────────────────

pub fn cg1t_x2g1_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let coulomb = pow(pi, 2) / (16.0 * beta) * (2.0 * CF - CA);
    let a12 = 1.0;
    let a11 = -5.0 / 2.0 + 3.0 * rln2;
    let a10_ok = cg1_a10_x2g1_vv_ok(xi);
    let a10_qed = cg1_a10_x2g1_vv_qed(xi);
    let res = CA * (a12 * ln(beta).powi(2) + a11 * ln(beta) + a10_ok)
        + 2.0 * CF * a10_qed;
    cg0t_x2g1(xi, eta) / pow(pi, 2) * (coulomb + res)
}

pub fn cg1t_x2g1_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let coulomb = pow(pi, 2) / (16.0 * beta) * (2.0 * CF - CA);
    let a12 = 1.0;
    let a11 = -5.0 / 2.0 + 3.0 * rln2;
    let a10_ok = cg1_a10_x2g1_aa_ok(xi);
    let a10_qed = cg1_a10_x2g1_aa_qed(xi);
    let res = CA * (a12 * ln(beta).powi(2) + a11 * ln(beta) + a10_ok)
        + 2.0 * CF * a10_qed;
    cg0t_x2g1(xi, eta) / pow(pi, 2) * (coulomb + res)
}

// ── Pure-singlet NLO threshold limits ──────────────────────────────────

const KQPH: f64 = 1.0 / 3.0;
const KGPH: f64 = 1.0 / 8.0;

pub fn cq1t_x2g1_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    let a11 = 1.0;
    let a10 = -13.0 / 12.0 + 3.0 / 2.0 * rln2 - 1.0 / 4.0; // x2g1 VV extra -1/4
    cg0t_x2g1(xi, eta)
        * beta * beta / pow(pi, 2)
        * (rhoq / (rhoq - 1.0))
        * (KQPH / 6.0 / KGPH)
        * (a11 * ln(beta) + a10)
}

pub fn cq1t_x2g1_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    let a11 = 1.0;
    let a10 = -13.0 / 12.0 + 3.0 / 2.0 * rln2; // no correction for AA
    cg0t_x2g1(xi, eta)
        * beta * beta / pow(pi, 2)
        * (rhoq / (rhoq - 1.0))
        * (KQPH / 6.0 / KGPH)
        * (a11 * ln(beta) + a10)
}

// ── Adler x2g1 data ───────────────────────────────────────────────────

pub static ADLER_X2G1_VV: [f64; 141] = [
    3.55556e-7, 4.47618e-7, 5.63518e-7, 7.09427e-7,
    8.93115e-7, 1.12437e-6, 1.41549e-6, 1.782e-6,
    2.2434e-6, 2.82428e-6, 3.55555e-6, 4.47618e-6,
    5.63517e-6, 7.09426e-6, 8.93115e-6, 0.0000112436,
    0.0000141549, 0.00001782, 0.000022434, 0.0000282427,
    0.0000355555, 0.0000447616, 0.0000563515, 0.0000709423,
    0.0000893109, 0.000112436, 0.000141548, 0.000178198,
    0.000224337, 0.000282422, 0.000355546, 0.000447603, 0.000563494,
    0.000709389, 0.000893055, 0.00112427, 0.00141534, 0.00178176,
    0.00224303, 0.00282368, 0.00355461, 0.00447468, 0.00563279,
    0.00709049, 0.00892518, 0.0112342, 0.01414, 0.0177963,
    0.0223966, 0.0281837, 0.0354622, 0.0446144, 0.0561193,
    0.0705763, 0.0887348, 0.11153, 0.140126, 0.17597, 0.220853,
    0.276986, 0.347087, 0.43448, 0.543207, 0.678151, 0.845171,
    1.05123, 1.30455, 1.61473, 1.99284, 2.45159, 3.00533, 3.67016,
    4.4639, 5.40617, 6.51828, 7.82323, 9.34566, 11.1118, 13.1492,
    15.487, 18.1556, 21.1866, 24.6128, 28.4679, 32.7867, 37.6051,
    42.9594, 48.887, 55.4258, 62.6146, 70.4924, 79.099, 88.4746,
    98.6596, 109.695, 121.622, 134.483, 148.318, 163.171, 179.082,
    196.096, 214.253, 233.598, 254.171, 276.018, 299.18, 323.7,
    349.622, 376.988, 405.842, 436.227, 468.186, 501.763, 537.001,
    573.942, 612.631, 653.111, 695.425, 739.616, 785.728, 833.805,
    883.889, 936.024, 990.253, 1046.62, 1105.17, 1165.94, 1228.98,
    1294.33, 1362.04, 1432.14, 1504.69, 1579.72, 1657.28, 1737.41,
    1820.16, 1905.56, 1993.67, 2084.52, 2178.16, 2274.64,
];
