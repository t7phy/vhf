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

pub static ADLER_XF3_VA: [f64; 141] = [
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

// ── Gluon LO threshold limit (same for VV and AA) ─────────────────────

pub fn cg0t_x2g1(xi: f64, eta: f64) -> f64 {
    let (_rho, beta, _chi) = mof_eta(eta);
    let (rhoq, _betaq, _chiq) = mof_xi(xi);
    pi / 2.0 * rhoq / (rhoq - 1.0) * beta
}

// ── Gluon NLO resummation coefficients (x2g1-specific a10) ────────────

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
