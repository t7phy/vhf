// use crate::core::sm_params::{theta_w, m_z, m_w};
use crate::core::sm_params::{m_z, m_w, sin2_theta_w, G_F};
use crate::core::constants::{pi};

pub fn alpha_em(_q: f64) -> f64{
    // Todo: solve RGE and move to crate::core
    return 1./137.0;
}

pub fn ew_charges(pid: i8) -> (f64, f64, f64) {
    let (em_charge, weak_isospin3) = match pid.abs() {
    1 | 3 | 5 => (-1.0/3.0, -0.5),
    2 | 4 | 6 => (2.0/3.0, 0.5),
    11 | 13 | 15 => (-1.0, -0.5),
    12 | 14 | 16 => (0.0, 0.5),
    _ => panic!("Invalid fermion PID: {}", pid),
};

    // let sign = pid.signum() as f64;
    // let em_charge: f64 = c * sign;
    // let weak_isospin3: f64 = i * sign;

    let g_a: f64 = weak_isospin3;
    let g_v: f64 = weak_isospin3 - 2.0 * em_charge * sin2_theta_w();

    (em_charge, g_v, g_a)
}

pub fn dis_coupling(l_pid: i8, q_pid: i8, q2: f64, interaction_type: String, pv: bool) -> f64 {
    let w_phph: f64 = ew_charges(l_pid).0.powi(2) * ew_charges(q_pid).0.powi(2);
    // let eta_phz: f64 = q2/(m_z().powi(2) + q2) * 1.0/(4.0*theta_w().sin().powi(2)*theta_w().cos().powi(2));
    // eta_phz /= (1 - k_eta_phz);
    let G_F = G_F();
    let M_z2 = m_z().powi(2);
    let M_w2 = m_w().powi(2);
    let sqrt2 = 2.0_f64.sqrt();
    let alpha_em = alpha_em(q2);
    let eta_phz: f64 = (G_F*M_z2/(2.0*sqrt2*pi*alpha_em))*(q2/(q2 + M_z2));

    if interaction_type == "em" && !pv {
        return w_phph;
    }

    else if interaction_type == "em" && pv {
        panic!("Parity violating structure functions do not exist for EM interactions")
    }

    else if interaction_type == "nc" {
        
        let (lep_e, lep_v, lep_a) = ew_charges(l_pid);
        let (q_e, q_v, q_a) = ew_charges(q_pid);
        if !pv {
            let w_phz: f64 = 2.0 * eta_phz * lep_e * lep_v * q_e * q_v;
            let w_zz: f64 = eta_phz.powi(2) * (lep_v.powi(2) + lep_a.powi(2)) * (q_v.powi(2) + q_a.powi(2));
            return w_phph + w_phz + w_zz;
        } else {
            let w_phz: f64 = 2.0 * eta_phz * lep_e * lep_a * q_e * q_a;
            let w_zz: f64 = eta_phz.powi(2) * 4.0 * lep_v * lep_a * q_v * q_a;
            return w_phz + w_zz;
        }
    }

    else if interaction_type == "cc" {
        let _eta_w: f64 = (eta_phz/2.0 * (1.0 + q2/m_z().powi(2))/(1.0 + q2/m_w().powi(2))).powi(2);
        todo!()
    }
    else {
        panic!("Invalid interaction type: {}", interaction_type);
    }
}

pub fn dis_coupling_fl11(l_pid: i8, q_pid: i8, nf: i8, q2:f64, interaction_type: String) -> f64 {
    
    fn charge(coupling_type: char, diagram: &str, pid: i8) -> f64 {
        let val: f64 = match (coupling_type, diagram) {
            ('V', "phph" | "zph") => ew_charges(pid).0,
            ('A', "phph" | "zph") => 0.0,
            ('V', "phz" | "zz") => ew_charges(pid).1,
            ('A', "phz" | "zz") => ew_charges(pid).2,
            _ => panic!("Wrong coupling type or diagram for FL11")
        };
        val
    }
    let res = |ct1: char, ct2: char, diagram: &str| -> f64 {
        let mut res1: f64 = 0.0;
        for i in 1..=nf {
            res1 += charge(ct1, diagram, i);
        }
        res1 /= nf as f64;
        let res2: f64 = charge(ct2, diagram, q_pid);
        res1 * res2
    };

    let w_phph: f64 = ew_charges(l_pid).0.powi(2) * res('V', 'V', "phph");
    let eta_phz: f64 = q2/(m_z().powi(2) + q2) * 1.0/(4.0*sin2_theta_w()*(1.0 - sin2_theta_w()));
    // eta_phz /= (1 - k_eta_phz);

    if interaction_type == "em" {
        return w_phph;
    }

    else if interaction_type == "nc" {
        let (lep_e, lep_v, lep_a) = ew_charges(l_pid);

        let w_phz: f64 = eta_phz * lep_e * lep_v * (res('V', 'V', "phz") + res('A', 'A', "phz"));
        let w_zph: f64 = eta_phz * lep_e * lep_v * res('V', 'V', "zph");
        let w_zz: f64 = eta_phz.powi(2) * (lep_v.powi(2) + lep_a.powi(2)) * (res('V', 'V', "zz") + res('A', 'A', "zz"));
        return w_phph + w_phz + w_zph + w_zz;
    }
    
    else {
        panic!("Invalid interaction type: {} for FL11", interaction_type);
    }

}
    
pub fn nc_ns(nf: i8, q: f64, interaction_type: String, pv: bool) -> Vec<(i8, f64)> {
    let q2 = q.powi(2);
    let mut vec: Vec<(i8, f64)> = vec![];
    // !!!! ATTENTION: right now lepton pid is harcoded to electron. adjust this
    if pv {
        for i in 1..=nf {
            vec.push((i, dis_coupling(11, i, q2, interaction_type.clone(), true)));
            vec.push((-i, -dis_coupling(11, i, q2, interaction_type.clone(), true)));
        }
    } else {
        for i in 1..=nf {
            vec.push((i, dis_coupling(11, i, q2, interaction_type.clone(), false)));
            vec.push((-i, dis_coupling(11, i, q2, interaction_type.clone(), false)));
        }
    }
    vec
}

pub fn nc_ns_fl11(nf: i8, q: f64, interaction_type: String) -> Vec<(i8, f64)> {
    let q2 = q.powi(2);
    let mut vec: Vec<(i8, f64)> = vec![];
    for i in 1..=nf {
        vec.push((i, dis_coupling_fl11(11, i, nf, q2, interaction_type.clone())));
        vec.push((-i, dis_coupling_fl11(11, i, nf, q2, interaction_type.clone())));
    }
    vec
}

pub fn nc_g(nf:i8, q: f64, interaction_type: String) -> Vec<(i8, f64)> {
    let q2 = q.powi(2);
    let mut ch_tot: f64 = 0.0;
    for i in 1..=nf {
        ch_tot += dis_coupling(11, i, q2, interaction_type.clone(), false);
    }
    let ch_avg: f64 = ch_tot/nf as f64;
    let mut vec: Vec<(i8, f64)> = vec![];
    vec.push((21, ch_avg));
    vec
}

pub fn nc_g_fl11(nf:i8, q: f64, interaction_type: String) -> Vec<(i8, f64)> {
    let q2 = q.powi(2);
    let mut ch_tot: f64 = 0.0;
    for i in 1..=nf {
        ch_tot += dis_coupling_fl11(11, i, nf, q2, interaction_type.clone());
    }
    let ch_avg: f64 = ch_tot/nf as f64;
    let mut vec: Vec<(i8, f64)> = vec![];
    vec.push((21, ch_avg));
    vec
}

pub fn nc_s(nf:i8, q: f64, interaction_type: String) -> Vec<(i8, f64)> {
    let q2 = q.powi(2);
    let mut ch_tot: f64 = 0.0;
    for i in 1..=nf {
        ch_tot += dis_coupling(11, i, q2, interaction_type.clone(), false);
    }
    let ch_avg: f64 = ch_tot/nf as f64;
    let mut vec: Vec<(i8, f64)> = vec![];
    for i in 1..=nf {
        vec.push((i, ch_avg));
        vec.push((-i, ch_avg));
    }
    vec
}

pub fn nc_v(nf:i8, q: f64, interaction_type: String) -> Vec<(i8, f64)> {
    let q2 = q.powi(2);
    let mut ch_tot: f64 = 0.0;
    for i in 1..=nf {
        ch_tot += dis_coupling(11, i, q2, interaction_type.clone(), true);
    }
    let ch_avg: f64 = ch_tot/nf as f64;
    let mut vec: Vec<(i8, f64)> = vec![];
    for i in 1..=nf {
        vec.push((i, ch_avg));
        vec.push((-i, -ch_avg));
    }
    vec
}
