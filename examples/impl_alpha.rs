use scirs2_core::ndarray::{array, Array1, ArrayView1};
use scirs2_integrate::ode::{solve_ivp, ODEMethod, ODEOptions};

use vhf::core::sm_params as sm;

#[derive(Clone, Copy, Debug)]
enum FermionKind {
    Lepton,
    UpTypeQuark,
    DownTypeQuark,
}

#[derive(Clone, Copy, Debug)]
struct Threshold {
    mass: f64,
    kind: FermionKind,
}

fn thresholds() -> Vec<Threshold> {
    let mut v = vec![
        Threshold { mass: sm::m_electron(), kind: FermionKind::Lepton },
        Threshold { mass: sm::m_muon(),     kind: FermionKind::Lepton },
        Threshold { mass: sm::m_tau(),      kind: FermionKind::Lepton },

        Threshold { mass: sm::m_up(),       kind: FermionKind::UpTypeQuark },
        Threshold { mass: sm::m_charm(),    kind: FermionKind::UpTypeQuark },
        Threshold { mass: sm::m_top(),      kind: FermionKind::UpTypeQuark },

        Threshold { mass: sm::m_down(),     kind: FermionKind::DownTypeQuark },
        Threshold { mass: sm::m_strange(),  kind: FermionKind::DownTypeQuark },
        Threshold { mass: sm::m_bottom(),   kind: FermionKind::DownTypeQuark },
    ];

    v.sort_by(|a, b| a.mass.partial_cmp(&b.mass).unwrap());
    v
}

fn threshold_charge_factor(kind: FermionKind) -> f64 {
    match kind {
        FermionKind::Lepton => 1.0,
        FermionKind::UpTypeQuark => 4.0 / 3.0,
        FermionKind::DownTypeQuark => 1.0 / 3.0,
    }
}

fn active_charge_sum(q: f64) -> f64 {
    thresholds()
        .iter()
        .filter(|thr| q >= thr.mass)
        .map(|thr| threshold_charge_factor(thr.kind))
        .sum()
}

fn zeta3() -> f64 {
    1.202_056_903_159_594_285_4
}

fn zeta4() -> f64 {
    std::f64::consts::PI.powi(4) / 90.0
}

fn zeta5() -> f64 {
    1.036_927_755_143_369_926_3
}

// MSbar QED beta function in explicit alpha convention:
//
// d alpha / d ln(Q)
//   = b0 alpha^2
//   + b1 alpha^3
//   + b2 alpha^4
//   + b3 alpha^5
//   + b4 alpha^6
//
// pto = 0: fixed alpha
// pto = 1: 1-loop
// pto = 2: 2-loop
// pto = 3: 3-loop
// pto = 4: 4-loop
// pto = 5: 5-loop
//
// Important:
// These coefficients use the known single-fermion MSbar QED beta-function
// coefficients, promoted here by replacing the single unit-charge factor by
// charge_sum = Σ_f Nc_f Q_f^2.
//
// This is exact at 1 loop and 2 loops in this normalization.
// At 3 loops and beyond, the fully general multi-charge expression contains
// additional charge-invariant structures. This function keeps the compact
// effective-charge implementation.
fn beta_alpha_em_with_charge_sum(alpha: f64, charge_sum: f64, pto: i32) -> f64 {
    if pto <= 0 {
        return 0.0;
    }

    let pi = std::f64::consts::PI;

    // Coefficients c_i defined by:
    //
    // d(a)/d ln(Q^2) = c1 a^2 + c2 a^3 + c3 a^4 + c4 a^5 + c5 a^6,
    //
    // where a = alpha / pi.
    //
    // Then:
    //
    // d alpha / d ln(Q) = 2 pi * d(a)/d ln(Q^2)
    //
    // so each term becomes:
    //
    // b_i alpha^(i+1) = 2 c_i alpha^(i+1) / pi^i.
    //
    let c1 = (1.0 / 3.0) * charge_sum;
    let c2 = (1.0 / 4.0) * charge_sum;

    let c3 = (-31.0 / 288.0) * charge_sum;

    let c4 = -(
        2785.0 / 31104.0
        + (13.0 / 36.0) * zeta3()
    ) * charge_sum;

    let c5 = (
        -195067.0 / 497664.0
        - (13.0 / 96.0) * zeta4()
        - (25.0 / 96.0) * zeta3()
        + (215.0 / 96.0) * zeta5()
    ) * charge_sum;

    let mut beta = 0.0;

    if pto >= 1 {
        beta += 2.0 * c1 * alpha.powi(2) / pi;
    }

    if pto >= 2 {
        beta += 2.0 * c2 * alpha.powi(3) / pi.powi(2);
    }

    if pto >= 3 {
        beta += 2.0 * c3 * alpha.powi(4) / pi.powi(3);
    }

    if pto >= 4 {
        beta += 2.0 * c4 * alpha.powi(5) / pi.powi(4);
    }

    if pto >= 5 {
        beta += 2.0 * c5 * alpha.powi(6) / pi.powi(5);
    }

    beta
}

// Threshold matching.
//
// At the moment this implements continuity:
//
// alpha_above(m_f) = alpha_below(m_f)
//
// This is the correct LO matching.
// Higher-order finite matching constants require the explicit MSbar
// decoupling relation for alpha_em across each charged-fermion threshold.
// The beta function above is implemented to 5 loops, but this matching
// function is still identity unless those constants are inserted.
fn match_alpha_em_at_threshold(
    alpha_below: f64,
    _threshold: Threshold,
    _pto: i32,
) -> f64 {
    alpha_below
}

fn evolve_alpha_em_between(
    alpha0: f64,
    q0: f64,
    q1: f64,
    charge_sum: f64,
    pto: i32,
) -> Result<f64, String> {
    if q0 == q1 || pto <= 0 {
        return Ok(alpha0);
    }

    if q0 <= 0.0 || q1 <= 0.0 {
        return Err("evolve_alpha_em_between requires positive scales".to_string());
    }

    let t0 = q0.ln();
    let t1 = q1.ln();

    let y0: Array1<f64> = array![alpha0];

    let rhs = move |_t: f64, y: ArrayView1<f64>| {
        array![beta_alpha_em_with_charge_sum(y[0], charge_sum, pto)]
    };

    let options = ODEOptions {
        method: ODEMethod::RK45,
        rtol: 1e-10,
        atol: 1e-14,
        ..Default::default()
    };

    let result = solve_ivp(rhs, [t0, t1], y0, Some(options))
        .map_err(|e| format!("solve_ivp failed: {e:?}"))?;

    let last = result
        .y
        .last()
        .ok_or_else(|| "solve_ivp returned empty solution".to_string())?;

    Ok(last[0])
}

pub fn alpha_em(q2: f64, pto: i32) -> Result<f64, String> {
    if !q2.is_finite() || q2 < 0.0 {
        return Err("q2 must be non-negative and finite".to_string());
    }

    if pto < 0 || pto > 5 {
        return Err("pto must be between 0 and 5".to_string());
    }

    let alpha0 = sm::alpha_em();

    if q2 == 0.0 || pto == 0 {
        return Ok(alpha0);
    }

    let q_target = q2.sqrt();

    let all_thresholds = thresholds();
    let q_start = sm::m_electron();

    if q_target <= q_start {
        return Ok(alpha0);
    }

    let mut alpha = alpha0;
    let mut q_current = q_start;

    // Electron active immediately above m_e.
    let mut charge_sum = 1.0;

    for thr in all_thresholds {
        if thr.mass <= q_current {
            continue;
        }

        if thr.mass >= q_target {
            break;
        }

        alpha = evolve_alpha_em_between(
            alpha,
            q_current,
            thr.mass,
            charge_sum,
            pto,
        )?;

        alpha = match_alpha_em_at_threshold(alpha, thr, pto);

        charge_sum += threshold_charge_factor(thr.kind);
        q_current = thr.mass;
    }

    alpha = evolve_alpha_em_between(
        alpha,
        q_current,
        q_target,
        charge_sum,
        pto,
    )?;

    Ok(alpha)
}

fn alpha_em_one_loop_analytic_no_threshold(
    alpha0: f64,
    q0: f64,
    q: f64,
    charge_sum: f64,
) -> f64 {
    let b0 = (2.0 / (3.0 * std::f64::consts::PI)) * charge_sum;
    1.0 / (1.0 / alpha0 - b0 * (q / q0).ln())
}

fn main() -> Result<(), String> {
    let mz = sm::m_z();
    let q2_mz = mz * mz;

    for pto in 0..=5 {
        let aem_mz = alpha_em(q2_mz, pto)?;
        println!(
            "pto = {pto}: alpha_em(MZ^2) = {:.15}, 1/alpha = {:.10}",
            aem_mz,
            1.0 / aem_mz
        );
    }

    let q0 = 20.0;
    let q = 80.0;

    let alpha0 = alpha_em(q0 * q0, 1)?;

    let charge_sum = active_charge_sum(q0);

    if (active_charge_sum(q) - charge_sum).abs() > 1e-14 {
        return Err("sanity-check interval crosses a threshold".to_string());
    }

    let alpha_num =
        evolve_alpha_em_between(alpha0, q0, q, charge_sum, 1)?;

    let alpha_ana =
        alpha_em_one_loop_analytic_no_threshold(alpha0, q0, q, charge_sum);

    println!();
    println!("Sanity check: no-threshold LO evolution");
    println!("alpha0({q0} GeV)   = {:.15}", alpha0);
    println!("alpha_num({q} GeV) = {:.15}", alpha_num);
    println!("alpha_ana({q} GeV) = {:.15}", alpha_ana);
    println!(
        "absolute diff      = {:.6e}",
        alpha_num - alpha_ana
    );
    println!(
        "relative diff      = {:.6e}",
        (alpha_num - alpha_ana) / alpha_ana
    );

    Ok(())
}