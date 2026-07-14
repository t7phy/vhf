pub mod flnc_nlo_gvv;
pub mod flnc_nlo_gaa;
pub mod flnc_nnlo_gvv;
pub mod flnc_nnlo_gaa;
pub mod flnc_nnlo_psvv;
pub mod flnc_nnlo_psaa;
pub mod flnc_nnlo_ns;

use crate::dis::internal::*;
use crate::dis::f2_heavy::{cgbar1_h1, cgbar1_h2, cgbar1_h3, dq1_h4, wgplg};
use crate::dis::f2_heavy::{ADLER_LOGXIS};

// ── Gluon LO threshold limits ──────────────────────────────────────────

pub fn cg0t_fl_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    4.0 * pi * beta.powi(3) * rhoq.powi(2) / (3.0 * (1.0 - rhoq).powi(3))
}

pub fn cg0t_fl_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    pi * beta * rhoq.powi(2) / (1.0 - rhoq)
}

// ── Gluon NLO resummation coefficients (FL-specific a10) ──────────────

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

pub fn cg1_a10_fl_vv_ok(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    let g2 = cg1_a10_g2(xi);
    0.6805555555555556 + g2
        - (pow(pi, 2) * (-4. + rhoq) * rhoq) / (24. * pow(-1. + rhoq, 2))
        + (g1 * (1. + 2. * rhoq)) / pow(-1. + rhoq, 2)
        - rln2
        - ((-4. + rhoq) * rhoq * pow(ln(chiq), 2)) / (8. * pow(-1. + rhoq, 2))
        + ((-1. + rhoq * (-3. - 2. * (-3. + rhoq) * rhoq)) * ln(rhoq / (2. * (-1. + rhoq))))
            / (4. * (-2. + rhoq) * pow(-1. + rhoq, 2))
}

pub fn cg1_a10_fl_vv_qed(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    (3. - 2. * rhoq) / (8. * (-2. + rhoq))
        - (g1 * (-1. + 6. * rhoq)) / pow(-1. + rhoq, 2)
        - (pow(pi, 2) * (-1. + 6. * rhoq)) / (24. * pow(-1. + rhoq, 2))
        + ((-6. + rhoq + pow(rhoq, 2)) * ln(chiq)) / (8. * betaq * (-2. + rhoq))
        - ((-1. + 6. * rhoq) * pow(ln(chiq), 2)) / (8. * pow(-1. + rhoq, 2))
        + ((3. + 2. * rhoq * (5. + (-5. + rhoq) * rhoq)) * ln(rhoq / (2. * (-1. + rhoq))))
            / (4. * pow(-2. + rhoq, 2) * (-1. + rhoq))
}

pub fn cg1_a10_fl_aa_ok(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    let g2 = cg1_a10_g2(xi);
    g2 + (pow(pi, 2) * (4. - 9. * (-1. + rhoq) * rhoq)) / (96. * pow(-1. + rhoq, 2))
        + (g1 * (4. - rhoq * (1. + rhoq))) / (2. * pow(-1. + rhoq, 2))
        + ((2. - 3. * rhoq + pow(rhoq, 3)) * ln(chiq)) / (8. * betaq * pow(-1. + rhoq, 2))
        + ((4. - 7. * (-1. + rhoq) * rhoq) * pow(ln(chiq), 2)) / (32. * pow(-1. + rhoq, 2))
        + ((-4. + 5. * rhoq - pow(rhoq, 3)) * ln(rhoq / (2. * (-1. + rhoq))))
            / (8. * (-2. + rhoq) * pow(-1. + rhoq, 2))
}

pub fn cg1_a10_fl_aa_qed(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    -(-5. + 2. * rhoq) / (8. * (-2. + rhoq))
        + (g1 * rhoq * (-7. + 3. * rhoq)) / (2. * pow(-1. + rhoq, 2))
        + (pow(pi, 2) * rhoq * (-17. + 9. * rhoq)) / (96. * pow(-1. + rhoq, 2))
        + ((-0.5 + rhoq - (3. * pow(rhoq, 2)) / 8.) * ln(chiq)) / (betaq * (-2. + rhoq))
        + (rhoq * (-15. + 7. * rhoq) * pow(ln(chiq), 2)) / (32. * pow(-1. + rhoq, 2))
        + ((12. + rhoq * (-7. + rhoq * (-3. + 2. * rhoq))) * ln(rhoq / (2. * (-1. + rhoq))))
            / (8. * pow(-2. + rhoq, 2) * (-1. + rhoq))
}

// ── Gluon NLO threshold limits ─────────────────────────────────────────

pub fn cg1t_fl_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let coulomb = pow(pi, 2) / (16.0 * beta) * (2.0 * CF - CA);
    let a12 = 1.0;
    let a11 = -5.0 / 2.0 + 3.0 * rln2 - 2.0 / 3.0; // FL VV has extra -2/3
    let a10_ok = cg1_a10_fl_vv_ok(xi);
    let a10_qed = cg1_a10_fl_vv_qed(xi);
    let res = CA * (a12 * ln(beta).powi(2) + a11 * ln(beta) + a10_ok)
        + 2.0 * CF * a10_qed;
    cg0t_fl_vv(xi, eta) / pow(pi, 2) * (coulomb + res)
}

pub fn cg1t_fl_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let coulomb = pow(pi, 2) / (16.0 * beta) * (2.0 * CF - CA);
    let a12 = 1.0;
    let a11 = -5.0 / 2.0 + 3.0 * rln2; // FL AA: no extra correction
    let a10_ok = cg1_a10_fl_aa_ok(xi);
    let a10_qed = cg1_a10_fl_aa_qed(xi);
    let res = CA * (a12 * ln(beta).powi(2) + a11 * ln(beta) + a10_ok)
        + 2.0 * CF * a10_qed;
    cg0t_fl_aa(xi, eta) / pow(pi, 2) * (coulomb + res)
}

// ── Gluon NNLO high-virtuality limit (BMSN massless, FL) ──────────────

fn clg2am0_aq(x: f64) -> f64 {
    let dlx = x.ln();
    let dlm = (1.0 - x).ln();
    let a1 = 64.0 * x * (1.0 - x) * dlm - 128.0 * x * dlx - 32.0 - 160.0 * x
        + 544.0 * x * x / 3.0 + 32.0 / x / 3.0;
    let b1 = 32.0 * x * dlx + 16.0 * (1.0 - 2.0 * x * x + x);
    TR * (CA * a1 + CF * b1)
}

fn clg2am0_a0(x: f64) -> f64 {
    let dlx = x.ln();
    let dlx2 = dlx * dlx;
    let dlm = (1.0 - x).ln();
    let dlm2 = dlm * dlm;
    let dlp = (1.0 + x).ln();
    let s11 = wgplg(1, 1, 1.0 - x);
    let s11m = wgplg(1, 1, -x);
    let a2 = 96.0 * x * dlx2 + (64.0 * x * x - 192.0 * x) * dlx * dlm
        + (32.0 - 416.0 * x * x + 256.0 * x) * dlx
        + 32.0 * x * (1.0 - x) * dlm2
        + (-32.0 + 928.0 * x * x / 3.0 - 288.0 * x + 32.0 / x / 3.0) * dlm
        + 64.0 * x * x * z2 - 128.0 * x * s11
        + 64.0 * x * (1.0 + x) * (s11m + dlx * dlp)
        + 32.0 / 3.0 - 1696.0 * x * x / 9.0 + 544.0 * x / 3.0 - 32.0 / x / 9.0;
    let b2 = -(64.0 * x * x * x / 5.0 + 64.0 * x / 3.0) * dlx2
        + 32.0 * x * (s11 + dlx * dlm)
        + (-208.0 / 15.0 + 192.0 * x * x / 5.0 - 416.0 * x / 5.0 - 64.0 / x / 15.0) * dlx
        + (16.0 - 64.0 * x * x + 48.0 * x) * dlm
        + (128.0 * x * x * x / 5.0 - 64.0 * x / 3.0) * z2
        + (128.0 * x * x * x / 5.0 - 64.0 * x / 3.0 + 64.0 / x / x / 15.0) * (s11m + dlx * dlp)
        - 256.0 / 15.0 + 672.0 * x * x / 5.0 - 608.0 * x / 5.0 + 64.0 / x / 15.0;
    TR * (CA * a2 + CF * b2)
}

pub fn cg1hv_fl(xi: f64, eta: f64) -> f64 {
    let l = xi.ln();
    let z = xi / (4.0 * (1.0 + eta) + xi);
    let n = xi * 16.0 * pi / z;
    (clg2am0_aq(z) * l + clg2am0_a0(z)) / n
}

// ── Pure-singlet NNLO high-virtuality limit (BMSN massless, FL) ────────

fn clps2am0_aq(x: f64) -> f64 {
    let dlx = x.ln();
    let a1 = -32.0 * x * dlx - 32.0 + 64.0 * x * x / 3.0 + 32.0 / x / 3.0;
    CF * TR * a1
}

fn clps2am0_a0(x: f64) -> f64 {
    let dlx = x.ln();
    let dlx2 = dlx * dlx;
    let dlm = (1.0 - x).ln();
    let spx = wgplg(1, 1, 1.0 - x);
    let a2 = 32.0 * x * (dlx2 - dlx * dlm - spx)
        + (-32.0 + 64.0 * x * x / 3.0 + 32.0 / x / 3.0) * dlm
        + (32.0 - 64.0 * x * x - 32.0 * x) * dlx
        + 32.0 / 3.0 + 320.0 * x * x / 9.0 - 128.0 * x / 3.0 - 32.0 / x / 9.0;
    CF * TR * a2
}

pub fn cq1hv_fl(xi: f64, eta: f64) -> f64 {
    let lnxi = xi.ln();
    let z = xi / (4.0 * (1.0 + eta) + xi);
    let n = xi * 16.0 * pi / z;
    (clps2am0_aq(z) * lnxi + clps2am0_a0(z)) / n
}

// ── Pure-singlet NLO threshold limits ──────────────────────────────────

const KQPH: f64 = 1.0 / 3.0;
const KGPH: f64 = 1.0 / 8.0;

pub fn cq1t_fl_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    // FL VV has different aq coefficients
    let a11 = 1.0 - 2.0 / 5.0;
    let a10 = -77.0 / 100.0 + 9.0 / 10.0 * rln2;
    cg0t_fl_vv(xi, eta)
        * beta * beta / pow(pi, 2)
        * (rhoq / (rhoq - 1.0))
        * (KQPH / 6.0 / KGPH)
        * (a11 * ln(beta) + a10)
}

pub fn cq1t_fl_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    let a11 = 1.0;
    let a10 = -13.0 / 12.0 + 3.0 / 2.0 * rln2;
    cg0t_fl_aa(xi, eta)
        * beta * beta / pow(pi, 2)
        * (rhoq / (rhoq - 1.0))
        * (KQPH / 6.0 / KGPH)
        * (a11 * ln(beta) + a10)
}

// ── Adler FL data ──────────────────────────────────────────────────────

pub static ADLER_FL_VV: [f64; 141] = [
    2.37037e-7, 2.98412e-7, 3.75678e-7, 4.7295e-7,
    5.95409e-7, 7.49575e-7, 9.43658e-7, 1.18799e-6,
    1.4956e-6, 1.88284e-6, 2.37035e-6, 2.98409e-6,
    3.75674e-6, 4.72944e-6, 5.954e-6, 7.4956e-6,
    9.43636e-6, 0.0000118796, 0.0000149554, 0.0000188276,
    0.0000237022, 0.0000298389, 0.0000375642, 0.0000472895,
    0.0000595323, 0.0000749442, 0.0000943452, 0.000118767,
    0.00014951, 0.000188207, 0.000236916, 0.000298225, 0.00037539,
    0.000472505, 0.000594722, 0.000748515, 0.000942025, 0.00118548,
    0.00149173, 0.00187689, 0.00236122, 0.00297008, 0.00373526,
    0.00469656, 0.00590371, 0.00741883, 0.00931929, 0.0117014,
    0.0146845, 0.0184165, 0.0230797, 0.0288981, 0.0361457,
    0.0451558, 0.0563314, 0.0701561, 0.0872054, 0.108158, 0.133802,
    0.165048, 0.202921, 0.248565, 0.303222, 0.368217, 0.444916,
    0.534693, 0.63887, 0.758666, 0.895142, 1.04915, 1.22128,
    1.41187, 1.62094, 1.84828, 2.09337, 2.3555, 2.63378, 2.92716,
    3.23451, 3.55466, 3.88642, 4.22861, 4.58009, 4.9398, 5.30674,
    5.67998, 6.05871, 6.44217, 6.82969, 7.22069, 7.61466, 8.01114,
    8.40975, 8.81016, 9.21208, 9.61526, 10.0195, 10.4246, 10.8305,
    11.237, 11.6439, 12.0513, 12.4591, 12.8671, 13.2754, 13.6839,
    14.0925, 14.5012, 14.9101, 15.3191, 15.7281, 16.1372, 16.5463,
    16.9555, 17.3647, 17.7739, 18.1832, 18.5924, 19.0017, 19.411,
    19.8203, 20.2297, 20.639, 21.0483, 21.4576, 21.867, 22.2763,
    22.6856, 23.095, 23.5043, 23.9137, 24.323, 24.7324, 25.1417,
    25.5511, 25.9604, 26.3697, 26.7791, 27.1884, 27.5978, 28.0071,
];
