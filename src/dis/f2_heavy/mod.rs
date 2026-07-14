pub mod f2nc_nlo_gvv;
pub mod f2nc_nnlo_gvv;
pub mod f2nc_n3lo_gvv;

pub mod f2nc_nlo_gaa;
pub mod f2nc_nnlo_gaa;

pub mod f2nc_nnlo_psvv;
pub mod f2nc_n3lo_psvv;

pub mod f2nc_nnlo_psaa;

pub mod f2nc_nnlo_ns;

pub mod f2cc_nlo_g;

pub mod f2cc_nlo_ns;

pub mod fh_grids;

use crate::dis::internal::*;

pub fn wgplg(m: i32, n: i32, x: f64) -> f64 {
    nl(m, n, x).re
}

// ── Shared cgBar1 helpers (h1, h2, h3) ────────────────────────────────

pub fn cgbar1_h1(chi: f64, chiq: f64) -> f64 {
    -pow(pi,2)/6. - 2.*Li2(-chi) + Li2((1. - chiq)/(1. + chi)) - Li2((chi*(1. - chiq))/(1. + chi)) - Li2(-((chi*(1. - chiq))/((1. + chi)*chiq))) + Li2((-1. + chiq)/((1. + chi)*chiq)) + pow(ln(chi),2)/2. + ln(chi)*(ln(chiq) - ln(chi + chiq) - ln(1. + chi*chiq))
}

pub fn cgbar1_h2(chi: f64, chiq: f64) -> f64 {
    -pow(pi,2)/6. + 2.*Li2(-chi) + 2.*Li2(chi) - ln(chi)/2. - ln(chi)*(ln(chiq) - ln(chi + chiq) - ln(1. + chi*chiq))
}

pub fn cgbar1_h3(chi: f64, chiq: f64) -> f64 {
    ln(1. - chi) + ln(1. + chi) + (-ln(chi) + ln(chiq) - ln(chi + chiq) - ln(1. + chi*chiq))/2.
}

// ── Gluon LO threshold limits ──────────────────────────────────────────

pub fn cg0t_f2_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    pi / 2.0 * rhoq / (rhoq - 1.0) * beta
}

pub fn cg0t_f2_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    pi * beta * (1.0 - 2.0 * rhoq) * rhoq / (2.0 * (rhoq - 1.0))
}

// ── Gluon NLO resummation coefficients ─────────────────────────────────

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

pub fn cg1_a10_f2_vv_ok(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    let g2 = cg1_a10_g2(xi);
    g1 + g2 - (pow(pi, 2) * rhoq) / (32. * (-1. + rhoq))
        + ((-5. + (7. - 2. * rhoq) * rhoq) * ln(chiq)) / (8. * betaq * (-1. + rhoq))
        - (rhoq * pow(ln(chiq), 2)) / (32. * (-1. + rhoq))
        - ((-3. + rhoq) * ln(rhoq / (2. * (-1. + rhoq)))) / (4. * (-2. + rhoq))
}

pub fn cg1_a10_f2_vv_qed(xi: f64) -> f64 {
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

pub fn cg1_a10_f2_aa_ok(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    let g2 = cg1_a10_g2(xi);
    g2 - (pow(pi, 2) * rhoq * (3. + rhoq * (-25. + 18. * rhoq)))
        / (96. * pow(-1. + rhoq, 2) * (-1. + 2. * rhoq))
        + (g1 * (-1. - rhoq * (-4. + rhoq + pow(rhoq, 2))))
            / (pow(-1. + rhoq, 2) * (-1. + 2. * rhoq))
        + ((-3. + 2. * rhoq * (2. + rhoq)) * ln(chiq))
            / (8. * betaq * (-1. + 2. * rhoq))
        - (rhoq * (1. + rhoq * (-19. + 14. * rhoq)) * pow(ln(chiq), 2))
            / (32. * pow(-1. + rhoq, 2) * (-1. + 2. * rhoq))
        - ((-1. + (-1. + rhoq) * pow(rhoq, 2)) * ln(rhoq / (2. * (-1. + rhoq))))
            / (4. * (-2. + rhoq) * (-1. + rhoq) * (-1. + 2. * rhoq))
}

pub fn cg1_a10_f2_aa_qed(xi: f64) -> f64 {
    let (rhoq, betaq, chiq) = mof_xi(xi);
    let g1 = cg1_a10_g1(xi);
    (-5. - 4. * (-3. + rhoq) * rhoq) / (8. * (-2. + rhoq) * (-1. + 2. * rhoq))
        + (g1 * (-1. + (-2. + rhoq) * rhoq * (-2. + 3. * rhoq)))
            / (pow(-1. + rhoq, 2) * (-1. + 2. * rhoq))
        + (pow(pi, 2) * (-4. + rhoq * (19. + rhoq * (-41. + 18. * rhoq))))
            / (96. * pow(-1. + rhoq, 2) * (-1. + 2. * rhoq))
        - ((1. + 6. * (-1. + rhoq) * rhoq) * ln(chiq))
            / (8. * betaq * (-1. + 2. * rhoq))
        + ((-4. + rhoq * (17. + 7. * rhoq * (-5. + 2. * rhoq))) * pow(ln(chiq), 2))
            / (32. * pow(-1. + rhoq, 2) * (-1. + 2. * rhoq))
        + ((1. + rhoq) * (-1. + rhoq * (7. + rhoq * (-7. + 2. * rhoq)))
            * ln(rhoq / (2. * (-1. + rhoq))))
            / (4. * pow(-2. + rhoq, 2) * (-1. + rhoq) * (-1. + 2. * rhoq))
}

// ── Gluon NLO threshold limits ─────────────────────────────────────────

pub fn cg1t_f2_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let coulomb = pow(pi, 2) / (16.0 * beta) * (2.0 * CF - CA);
    let a12 = 1.0;
    let a11 = -5.0 / 2.0 + 3.0 * rln2;
    let a10_ok = cg1_a10_f2_vv_ok(xi);
    let a10_qed = cg1_a10_f2_vv_qed(xi);
    let res = CA * (a12 * ln(beta).powi(2) + a11 * ln(beta) + a10_ok)
        + 2.0 * CF * a10_qed;
    cg0t_f2_vv(xi, eta) / pow(pi, 2) * (coulomb + res)
}

pub fn cg1t_f2_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let coulomb = pow(pi, 2) / (16.0 * beta) * (2.0 * CF - CA);
    let a12 = 1.0;
    let a11 = -5.0 / 2.0 + 3.0 * rln2;
    let a10_ok = cg1_a10_f2_aa_ok(xi);
    let a10_qed = cg1_a10_f2_aa_qed(xi);
    let res = CA * (a12 * ln(beta).powi(2) + a11 * ln(beta) + a10_ok)
        + 2.0 * CF * a10_qed;
    cg0t_f2_aa(xi, eta) / pow(pi, 2) * (coulomb + res)
}

// ── Gluon NNLO high-virtuality limit (BMSN massless) ───────────────────

fn c2g2am0_aq2(x: f64) -> f64 {
    let dlx = x.ln();
    let dlm = (1.0 - x).ln();
    let a1 = 16.0 / x / 3.0 - 124.0 * x * x / 3.0 + 32.0 * x + 4.0
        + (16.0 * x * x - 16.0 * x + 8.0) * dlm
        + (32.0 * x + 8.0) * dlx;
    let b1 = -2.0 + 8.0 * x + (16.0 * x * x - 16.0 * x + 8.0) * dlm
        + (-16.0 * x * x + 8.0 * x - 4.0) * dlx;
    TR * (CA * a1 + CF * b1)
}

fn c2g2am0_aq(x: f64) -> f64 {
    let dlx = x.ln();
    let dlx2 = dlx * dlx;
    let dlm = (1.0 - x).ln();
    let dlm2 = dlm * dlm;
    let dlp = (1.0 + x).ln();
    let s111mx = wgplg(1, 1, 1.0 - x);
    let s11mx = wgplg(1, 1, -x);
    let a2 = -(16.0 + 32.0 * x * x) * z2 + 1628.0 * x * x / 9.0
        - 368.0 * x / 3.0 - 220.0 / 3.0 + 208.0 / x / 9.0
        + (16.0 * x * x - 16.0 * x + 8.0) * dlm2
        - (48.0 * x + 16.0) * dlx2
        + (-536.0 * x * x / 3.0 + 160.0 * x - 8.0 + 32.0 / x / 3.0) * dlm
        + (200.0 * x * x - 192.0 * x) * dlx
        + (96.0 * x - 32.0 * x * x) * dlx * dlm
        + (64.0 * x + 16.0) * s111mx
        - (32.0 * x * x + 32.0 * x + 16.0) * (s11mx + dlx * dlp);
    let b2 = (-64.0 * x * x + 64.0 * x - 32.0) * z2 + 16.0 * x * x - 68.0 * x + 36.0
        + (32.0 * x * x - 32.0 * x + 16.0) * dlm2
        + (32.0 * x * x - 16.0 * x + 8.0) * dlx2
        + (-80.0 * x * x + 96.0 * x - 28.0) * dlm
        + (80.0 * x * x - 48.0 * x + 8.0) * dlx
        + (-64.0 * x * x + 48.0 * x - 24.0) * dlx * dlm
        + (8.0 - 16.0 * x) * s111mx;
    TR * (CA * a2 + CF * b2)
}

fn c2g2am0_a0(x: f64) -> f64 {
    let dlx = x.ln();
    let dlx2 = dlx * dlx;
    let dlx3 = dlx2 * dlx;
    let dlm = (1.0 - x).ln();
    let dlm2 = dlm * dlm;
    let dlm3 = dlm2 * dlm;
    let dlp = (1.0 + x).ln();
    let dlp2 = dlp * dlp;
    let s11 = wgplg(1, 1, 1.0 - x);
    let s121mx = wgplg(1, 2, 1.0 - x);
    let s12mx = wgplg(1, 2, -x);
    let s211mx = wgplg(2, 1, 1.0 - x);
    let s21mx = wgplg(2, 1, -x);
    let s111mx = s11;
    let s11mx = wgplg(1, 1, -x);
    let zz = (1.0 - x) / (1.0 + x);
    let s21z = wgplg(2, 1, zz);
    let s21mz = wgplg(2, 1, -zz);

    let a31 = dlx3 * (16.0 / 3.0 + 16.0 * x)
        + dlx2 * dlm * (-8.0 + 16.0 * x * x - 64.0 * x)
        + dlx2 * dlp * (12.0 + 32.0 * x * x + 24.0 * x)
        + dlx2 * (-114.0 * x * x + 184.0 * x)
        + dlx * dlm2 * (-16.0 * x * x + 48.0 * x)
        + dlx * dlm * dlp * (-16.0 - 32.0 * x * x - 32.0 * x)
        + dlx * dlm * (16.0 + 292.0 * x * x - 288.0 * x)
        + dlx * dlp2 * (8.0 + 16.0 * x);
    let a32 = dlx * dlp * (-48.0 + 208.0 * x * x / 3.0 + 16.0 * x - 32.0 / x / 3.0)
        + dlx * z2 * (-16.0 + 32.0 * x * x - 160.0 * x)
        + dlx * s111mx * (32.0 * x)
        + dlx * s11mx * (24.0 + 32.0 * x * x + 48.0 * x)
        + dlx * (292.0 / 3.0 - 5780.0 * x * x / 9.0 + 332.0 * x)
        + dlm2 * (-6.0 - 214.0 * x * x / 3.0 + 64.0 * x + 16.0 / x / 3.0)
        + z2 * dlm * (-40.0 - 64.0 * x * x + 48.0 * x);
    let a33 = dlm * s111mx * (16.0 + 64.0 * x)
        + dlm * s11mx * (-16.0 - 32.0 * x * x - 32.0 * x)
        + dlm * (-112.0 / 3.0 + 2996.0 * x * x / 9.0 - 860.0 * x / 3.0 + 208.0 / x / 9.0)
        + z2 * dlp * (8.0 + 16.0 * x)
        + dlp * s11mx * (16.0 + 32.0 * x)
        + s21mz * (-16.0 - 32.0 * x * x - 32.0 * x)
        + s21z * (16.0 + 32.0 * x * x + 32.0 * x);
    let a34 = z2 * (-4.0 + 796.0 * x * x / 3.0 - 208.0 * x - 32.0 / x)
        + z3 * (-12.0 - 8.0 * x * x - 56.0 * x)
        + s111mx * (20.0 + 80.0 * x * x / 3.0 - 64.0 * x + 64.0 / x / 3.0)
        + s211mx * (-16.0 - 128.0 * x)
        + s121mx * (40.0 + 144.0 * x)
        + s11mx * (-48.0 + 208.0 * x * x / 3.0 + 16.0 * x - 32.0 / x / 3.0)
        + s21mx * (-24.0 - 48.0 * x)
        + s12mx * (16.0 + 32.0 * x)
        + 80.0 / x / 9.0 + 466.0 / 9.0 - 878.0 * x * x / 9.0 + 260.0 * x / 9.0;
    let a3 = a31 + a32 + a33 + a34;

    let b31 = dlx3 * (-8.0 / 3.0 - 32.0 * x * x / 3.0 + 16.0 * x / 3.0)
        + dlx2 * dlm * (16.0 + 48.0 * x * x - 32.0 * x)
        + dlx2 * dlp * (16.0 + 16.0 * x * x + 32.0 * x)
        + dlx2 * (-4.0 - 96.0 * x * x * x / 5.0 - 52.0 * x * x + 8.0 * x / 3.0)
        + dlx * dlm2 * (-20.0 - 48.0 * x * x + 40.0 * x)
        + dlx * dlm * (24.0 + 168.0 * x * x - 160.0 * x)
        + dlx * dlp2 * (-32.0 - 32.0 * x * x - 64.0 * x)
        + dlx * dlp * (96.0 + 192.0 * x * x * x / 5.0 + 128.0 * x / 3.0);
    let b32 = 16.0 * dlx * dlp / x / x / 15.0 - 16.0 * dlx / x / 15.0
        + dlx * z2 * (32.0 + 64.0 * x * x - 64.0 * x)
        + dlx * s111mx * (32.0 * x * x)
        + dlx * s11mx * (-32.0 - 32.0 * x * x + 64.0 * x)
        + dlx * (-712.0 / 15.0 - 672.0 * x * x / 5.0 + 136.0 * x / 5.0)
        + dlm3 * (8.0 + 16.0 * x * x - 16.0 * x)
        + dlm2 * (-22.0 - 84.0 * x * x + 88.0 * x)
        + z2 * dlm * (-32.0 * x * x);
    let b33 = dlm * s111mx * (8.0 - 16.0 * x)
        + dlm * (28.0 + 96.0 * x * x - 132.0 * x)
        + z2 * dlp * (-32.0 - 32.0 * x * x - 64.0 * x)
        + dlp * s11mx * (-64.0 - 64.0 * x * x - 128.0 * x)
        + z2 * (48.0 + 192.0 * x * x * x / 5.0 + 104.0 * x * x - 208.0 * x / 3.0)
        + z3 * (112.0 + 192.0 * x * x - 96.0 * x);
    let b34 = s111mx * (-24.0 + 64.0 * x * x - 48.0 * x)
        + s211mx * (-24.0 - 32.0 * x * x + 48.0 * x)
        + s121mx * (-32.0 + 64.0 * x)
        + s11mx * (96.0 + 192.0 * x * x * x / 5.0 + 128.0 * x / 3.0)
        + 16.0 * s11mx / x / x / 15.0 + 16.0 / x / 15.0
        + s21mx * (96.0 + 96.0 * x * x - 64.0 * x)
        + s12mx * (-64.0 - 64.0 * x * x - 128.0 * x)
        - 904.0 / 15.0 + 328.0 * x * x / 5.0 + 68.0 * x / 5.0;
    let b3 = b31 + b32 + b33 + b34;

    TR * (CA * a3 + CF * b3)
}

pub fn cg1hv_f2(xi: f64, eta: f64) -> f64 {
    let l = xi.ln();
    let z = xi / (4.0 * (1.0 + eta) + xi);
    let n = xi * 16.0 * pi / z;
    (c2g2am0_aq2(z) * l * l + c2g2am0_aq(z) * l + c2g2am0_a0(z)) / n
}

// ── Pure-singlet NNLO high-virtuality limit (BMSN massless) ────────────

fn c2ps2am0_aq2(x: f64) -> f64 {
    let dlx = x.ln();
    let a1 = -16.0 * x * x / 3.0 - 4.0 * x + 4.0 + 16.0 / x / 3.0
        + 8.0 * (1.0 + x) * dlx;
    CF * TR * a1
}

fn c2ps2am0_aq(x: f64) -> f64 {
    let dlx = x.ln();
    let dlx2 = dlx * dlx;
    let dlm = (1.0 - x).ln();
    let s11 = wgplg(1, 1, 1.0 - x);
    let a2 = -64.0 * x * x / 9.0 + 160.0 * x / 3.0 - 208.0 / 3.0 + 208.0 / x / 9.0
        + 32.0 * x * x * dlx
        + 16.0 * (1.0 + x) * (-dlx2 + dlx * dlm + s11)
        + (-32.0 * x * x / 3.0 - 8.0 * x + 8.0 + 32.0 / x / 3.0) * dlm;
    CF * TR * a2
}

fn c2ps2am0_a0(x: f64) -> f64 {
    let dlx = x.ln();
    let dlx2 = dlx * dlx;
    let dlx3 = dlx * dlx2;
    let dlm = (1.0 - x).ln();
    let dlm2 = dlm * dlm;
    let dlp = (1.0 + x).ln();
    let s11 = wgplg(1, 1, 1.0 - x);
    let s12 = wgplg(1, 2, 1.0 - x);
    let s21 = wgplg(2, 1, 1.0 - x);
    let s11m = wgplg(1, 1, -x);
    let a3 = (1.0 + x)
        * (16.0 * dlx3 / 3.0 - 16.0 * dlx2 * dlm + 8.0 * dlx * dlm2
            - 32.0 * z2 * dlx + 16.0 * dlm * s11 + 32.0 * s12 - 16.0 * s21)
        + (40.0 * x - 16.0 * x * x) * dlx2
        + 32.0 * x * x * dlx * dlm
        + (280.0 / 3.0 - 704.0 * x * x / 9.0 - 88.0 * x) * dlx
        + (4.0 - 16.0 * x * x / 3.0 - 4.0 * x + 16.0 / x / 3.0) * dlm2
        + (-208.0 / 3.0 - 64.0 * x * x / 9.0 + 160.0 * x / 3.0 + 208.0 / x / 9.0) * dlm
        + (-16.0 + 64.0 * x * x / 3.0 - 16.0 * x - 32.0 / x) * z2
        + (16.0 - 16.0 * x + 64.0 / x / 3.0 + 32.0 * x * x / 3.0) * s11
        + (-32.0 - 32.0 * x * x / 3.0 - 32.0 * x - 32.0 / x / 3.0) * (s11m + dlx * dlp)
        + 304.0 / 9.0 + 832.0 * x * x / 9.0 - 1216.0 * x / 9.0 + 80.0 / x / 9.0;
    CF * TR * a3
}

pub fn cq1hv_f2(xi: f64, eta: f64) -> f64 {
    let lnxi = xi.ln();
    let z = xi / (4.0 * (1.0 + eta) + xi);
    let n = xi * 16.0 * pi / z;
    (c2ps2am0_aq2(z) * lnxi * lnxi + c2ps2am0_aq(z) * lnxi + c2ps2am0_a0(z)) / n
}

// ── Pure-singlet NLO threshold limit ───────────────────────────────────

const KQPH: f64 = 1.0 / 3.0;  // 1/NC
const KGPH: f64 = 1.0 / 8.0;  // 1/(NC^2 - 1)

pub fn cq1t_f2_vv(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    let a11 = 1.0;
    let a10 = -13.0 / 12.0 + 3.0 / 2.0 * rln2;
    cg0t_f2_vv(xi, eta)
        * beta * beta / pow(pi, 2)
        * (rhoq / (rhoq - 1.0))
        * (KQPH / 6.0 / KGPH)
        * (a11 * ln(beta) + a10)
}

pub fn cq1t_f2_aa(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    let a11 = 1.0;
    let a10 = -13.0 / 12.0 + 3.0 / 2.0 * rln2;
    cg0t_f2_aa(xi, eta)
        * beta * beta / pow(pi, 2)
        * (rhoq / (rhoq - 1.0))
        * (KQPH / 6.0 / KGPH)
        * (a11 * ln(beta) + a10)
}

// ── Non-singlet dq1 helper ─────────────────────────────────────────────

pub fn dq1_h4(xi: f64, eta: f64) -> f64 {
    let (_rho, _beta, chi) = mof_eta(eta);
    let (_rhop, _betap, chip) = mof_prime(xi, eta);
    -Li2(((1. + chi) * chip) / (1. + chip))
        + Li2(((1. + chi) * chip) / (chi * (1. + chip)))
        + Li2((1. + chip) / (1. + chi))
        - Li2((chi * (1. + chip)) / (1. + chi))
        + pow(ln(chi), 2) / 2.
        + ln(chi) * (ln(1. + chi) - ln(chi - chip) + ln(1. + chip) - ln(1. - chi * chip))
}

// ── Adler sum rule data (cubic spline over log10(xi)) ──────────────────

pub static ADLER_LOGXIS: [f64; 141] = [
    -6.,-5.9,-5.8,-5.7,-5.6,-5.5,-5.4,-5.3,-5.2,-5.1,
    -5.,-4.9,-4.8,-4.7,-4.6,-4.5,-4.4,-4.3,-4.2,-4.1,
    -4.,-3.9,-3.8,-3.7,-3.6,-3.5,-3.4,-3.3,-3.2,-3.1,
    -3.,-2.9,-2.8,-2.7,-2.6,-2.5,-2.4,-2.3,-2.2,-2.1,
    -2.,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1,
    -1.,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,
    0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,
    1.,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,
    2.,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,
    3.,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,
    4.,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,
    5.,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,
    6.,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,
    7.,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,
    8.,
];

pub static ADLER_F2_VV: [f64; 141] = [
    4.31775e-6, 5.36701e-6, 6.67017e-6, 8.28834e-6,
    0.0000102973, 0.0000127909, 0.0000158856, 0.0000197252,
    0.0000244882, 0.0000303952, 0.0000377195, 0.000046799,
    0.0000580514, 0.0000719934, 0.0000892633, 0.00011065,
    0.000137127, 0.000169897, 0.000210444, 0.000260599, 0.000322616,
    0.000399279, 0.000494012, 0.000611035, 0.000755539, 0.000933909,
    0.00115399, 0.00142544, 0.00176009, 0.00217248, 0.00268042,
    0.00330576, 0.00407523, 0.00502155, 0.00618472, 0.00761361,
    0.00936784, 0.0115201, 0.014159, 0.0173921, 0.0213505,
    0.0261929, 0.032112, 0.0393408, 0.048161, 0.0589126, 0.072005,
    0.0879306, 0.10728, 0.130762, 0.159221, 0.193666, 0.235296,
    0.285534, 0.34606, 0.418859, 0.506261, 0.610996, 0.736251,
    0.885731, 1.06373, 1.27518, 1.52578, 1.82201, 2.17126,
    2.58189, 3.06332, 3.62608, 4.28195, 5.04395, 5.92647, 6.94529,
    8.11761, 9.46211, 10.999, 12.7498, 14.7379, 16.9877, 19.5254,
    22.3784, 25.5756, 29.1471, 33.1242, 37.5395, 42.4266, 47.8201,
    53.7557, 60.2696, 67.3993, 75.1826, 83.6582, 92.8653, 102.844,
    113.633, 125.275, 137.81, 151.279, 165.724, 181.187, 197.709,
    215.334, 234.104, 254.061, 275.247, 297.706, 321.481, 346.615,
    373.15, 401.13, 430.598, 461.596, 494.169, 528.36, 564.211,
    601.767, 641.07, 682.163, 725.091, 769.897, 816.623, 865.313,
    916.011, 968.76, 1023.6, 1080.58, 1139.75, 1201.13, 1264.79,
    1330.75, 1399.07, 1469.79, 1542.95, 1618.6, 1696.77, 1777.52,
    1860.88, 1946.89, 2035.62, 2127.08, 2221.34, 2318.42,
];
