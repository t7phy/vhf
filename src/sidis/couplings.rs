use crate::core::sm_params as sm;
use crate::core::constants::{pi};

pub fn alpha_em(_q: f64) -> f64{
    // Todo: solve RGE 
    return 1./137.0;
}

fn prop_factor(propagator: &str, q2: f64) -> f64 {
    let G_F = sm::G_F();
    let M_z2 = sm::m_z().powi(2);
    let M_w2 = sm::m_w().powi(2);
    let sqrt2 = 2.0_f64.sqrt();
    let alpha_em = alpha_em(q2);
    match propagator {
        "phph" => 1.0,
        "phZ" => (G_F*M_z2/(2.0*sqrt2*pi*alpha_em))*(q2/(q2 + M_z2)),
        "ZZ" => prop_factor("phZ", q2).powi(2),
        "W" => 0.5 * ((G_F*M_w2/(4.0*pi*alpha_em))*(q2/(q2 + M_w2))).powi(2),
        _ => panic!("Unknown propagator: {}", propagator),
    } 
}

fn lep_charges(pid: i32) -> (f64, f64, f64) {
    let sign = pid.signum() as f64;
    
    let em_charge: f64 = match pid.abs() {
        11 | 13 | 15 => -1.0,
        12 | 14 | 16 => 0.0,
        _ => panic!("Invalid lepton PID: {}", pid),
    } * sign;

    let weak_isospin3: f64 = match pid.abs() {
        11 | 13 | 15 => -0.5,
        12 | 14 | 16 => 0.5,
        _ => panic!("Invalid lepton PID: {}", pid),
    } * sign;

    let g_v: f64 = weak_isospin3 - 2.0 * em_charge * sm::sin2_theta_w();

    (em_charge, g_v, weak_isospin3)
}

fn quark_charges(pid: i32) -> (f64, f64, f64) {
    let sign = pid.signum() as f64;

    let em_charge: f64 = match pid.abs() {
        1 | 3 | 5 => -1.0 / 3.0,
        2 | 4 | 6 =>  2.0 / 3.0,
        _ => panic!("Invalid quark PID: {}", pid),
    } * sign;

    let weak_isospin3: f64 = match pid.abs() {
        1 | 3 | 5 => -0.5,
        2 | 4 | 6 =>  0.5,
        _ => panic!("Invalid quark PID: {}", pid),
    } * sign;

    let g_v: f64 = weak_isospin3 - 2.0 * em_charge * sm::sin2_theta_w();

    (em_charge, g_v, weak_isospin3)
}

fn lepton_coupling(coupling_type: &str, lep_pid: i32, helicity: &str) -> f64 {
    let lambda = match helicity {
        "L" => -1.0,
        "R" => 1.0,
        "unpol" => 0.0,
        _ => panic!("Invalid helicity: {}", helicity),
    };

    let lep_number = lep_pid.signum() as f64;
    let lep_charges = lep_charges(lep_pid);

    let coupling = match coupling_type {
        "phph" => lep_charges.0.powi(2),
        "phZ" => lep_charges.0 * (lep_charges.1 - lep_number * lambda * lep_charges.2),
        "phZ_pv" => lep_charges.0 * (lep_charges.2 - lep_number * lambda * lep_charges.1),
        "ZZ" => lep_charges.1.powi(2) + lep_charges.2.powi(2) - 2.0 * lep_number * lambda * lep_charges.1 * lep_charges.2,
        "ZZ_pv" => 2.0 * lep_charges.1 * lep_charges.2 - lep_number * lambda * (lep_charges.1.powi(2) + lep_charges.2.powi(2)),
        "w" => (1.0 - lep_number * lambda).powi(2),
        _ => panic!("Invalid coupling type: {}", coupling_type),
    };
    coupling
}

fn nc_quark_coupling(coupling_type: &str, quark1_pid: i32, quark2_pid: i32) -> f64 {
    let quark1_charges = quark_charges(quark1_pid);
    let quark2_charges = quark_charges(quark2_pid);
    let coupling = match coupling_type {
        "v_phph" => quark1_charges.0 * quark2_charges.0,
        "v_phZ" => quark1_charges.0 * quark2_charges.1 + quark1_charges.1 * quark2_charges.0,
        "v_ZZ" => quark1_charges.1 * quark2_charges.1,
        "a_phph" => 0.0,
        "a_phZ" => 0.0,
        "a_ZZ" => quark1_charges.2 * quark2_charges.2,
        "i_phph" => 0.0,
        "i_phZ" => 2.0 * quark1_charges.0 * quark2_charges.2,
        "i_ZZ" => quark1_charges.1 * quark2_charges.2 + quark1_charges.2 * quark2_charges.1,
        _ => panic!("Invalid coupling type: {}", coupling_type),
    };
    coupling
}

fn cc_quark_coupling(quark1_pid: i32, quark2_pid: i32) -> f64 {
    let (up_pid, dn_pid) = match (quark1_pid.abs(), quark2_pid.abs()) {
        (u, d) if [2,4,6].contains(&u) && [1,3,5].contains(&d) => (quark1_pid.abs(), quark2_pid.abs()),
        (d, u) if [1,3,5].contains(&d) && [2,4,6].contains(&u) => (quark2_pid.abs(), quark1_pid.abs()),
        _ => panic!("v_W requires one up-type and one down-type quark, got {} {}", quark1_pid, quark2_pid),
    };

    let ckm = match (up_pid, dn_pid) {
        (2, 1) => sm::ckm_ud(),
        (2, 3) => sm::ckm_us(),
        (2, 5) => sm::ckm_ub(),
        (4, 1) => sm::ckm_cd(),
        (4, 3) => sm::ckm_cs(),
        (4, 5) => sm::ckm_cb(),
        (6, 1) => sm::ckm_td(),
        (6, 3) => sm::ckm_ts(),
        (6, 5) => sm::ckm_tb(),
        _ => panic!("Unknown CKM combination: up={} dn={}", up_pid, dn_pid),
    };

    ckm.powi(2)
}

/*---------------------------------------\
|                                        |
|                                        |
|          unpol DIS couplings           |
|                                        |
|                                        |
\---------------------------------------*/

pub fn nc_dis_coupling(l_pid: i32, q_pid: i32, q2: f64, interaction_type: &str) -> f64 {
    // NC lepton beams are unpolarized; CC lepton beams are left-handed particles and right-handed antiparticles
    let coupling = match interaction_type {
        "em" => prop_factor("phph", q2) * lepton_coupling("phph", l_pid, "unpol") * nc_quark_coupling("v_phph", q_pid, q_pid),
        "nc" => nc_dis_coupling(l_pid, q_pid, q2, "em") +
            prop_factor("phZ", q2) * lepton_coupling("phZ", l_pid, "unpol") * nc_quark_coupling("v_phZ", q_pid, q_pid) +
            prop_factor("ZZ", q2) * lepton_coupling("ZZ", l_pid, "unpol") * (nc_quark_coupling("v_ZZ", q_pid, q_pid) + nc_quark_coupling("a_ZZ", q_pid, q_pid)),
        "nc_pv" => prop_factor("phZ", q2) * lepton_coupling("phZ_pv", l_pid, "unpol") * nc_quark_coupling("i_phZ", q_pid, q_pid) +
            prop_factor("ZZ", q2) * lepton_coupling("ZZ_pv", l_pid, "unpol") * nc_quark_coupling("i_ZZ", q_pid, q_pid),
        _ => panic!("Invalid interaction type: {}", interaction_type),
    };
    coupling
}

pub fn nc_ns(l_pid: i32, nf: i32, q2: f64, interaction_type: &str) -> Vec<(i32, f64)> {
    let mut vec: Vec<(i32, f64)> = vec![];
    if interaction_type == "nc_pv" {
        for i in 1..=nf {
            vec.push((i, nc_dis_coupling(l_pid, i, q2, "nc_pv")));
            vec.push((-i, -nc_dis_coupling(l_pid, -i, q2, "nc_pv")));
        }
    } else {
        for i in 1..=nf {
            vec.push((i, nc_dis_coupling(l_pid, i, q2, interaction_type)));
            vec.push((-i, nc_dis_coupling(l_pid, -i, q2, interaction_type)));
        }
    }
    vec
}

pub fn nc_g(l_pid: i32, nf: i32, q2: f64, interaction_type: &str) -> Vec<(i32, f64)> {
    let mut ch_tot: f64 = 0.0;
    for i in 1..=nf {
        ch_tot += nc_dis_coupling(l_pid, i, q2, interaction_type);
    }
    let ch_avg: f64 = ch_tot/nf as f64;
    let mut vec: Vec<(i32, f64)> = vec![];
    vec.push((21, ch_avg));
    vec
}

pub fn nc_ps(l_pid: i32, nf: i32, q2: f64, interaction_type: &str) -> Vec<(i32, f64)> {
    let mut ch_tot: f64 = 0.0;
    for i in 1..=nf {
        ch_tot += nc_dis_coupling(l_pid, i, q2, interaction_type);
    }
    let ch_avg: f64 = ch_tot/nf as f64;
    let mut vec: Vec<(i32, f64)> = vec![];
    for i in 1..=nf {
        vec.push((i, ch_avg));
        vec.push((-i, ch_avg));
    }
     vec
}

pub fn nc_v(l_pid: i32, nf: i32, q2: f64) -> Vec<(i32, f64)> {
    let mut ch_tot: f64 = 0.0;
    for i in 1..=nf {
        ch_tot += nc_dis_coupling(l_pid, i, q2, "nc_pv");
    }
    let ch_avg: f64 = ch_tot/nf as f64;
    let mut vec: Vec<(i32, f64)> = vec![];
    for i in 1..=nf {
        vec.push((i, ch_avg));
        vec.push((-i, -ch_avg));
    }
    vec
}
    

pub fn nc_dis_fl11_coupling(l_pid: i32, q_pid: i32, nf: i32, q2: f64, interaction_type: &str) -> f64 {

    fn charge(coupling_type: char, diagram: &str, pid: i32) -> f64 {
        let ew_charges = quark_charges(pid);
        let val: f64 = match (coupling_type, diagram) {
            ('V', "phph" | "Zph") => ew_charges.0,
            ('A', "phph" | "Zph") => 0.0,
            ('V', "phZ" | "ZZ") => ew_charges.1,
            ('A', "phZ" | "ZZ") => ew_charges.2,
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

    let lep_charges = lep_charges(l_pid);

    let coupling = match interaction_type {
        "em" => prop_factor("phph", q2) * lepton_coupling("phph", l_pid, "unpol") * res('V', 'V', "phph"),
        "nc" => nc_dis_fl11_coupling(l_pid, q_pid, nf, q2, "em") +
            prop_factor("phZ", q2) * lep_charges.0 * lep_charges.1 * (res('V', 'V', "phZ") + res('A', 'A', "phZ") + res('V', 'V', "Zph"))+
            prop_factor("ZZ", q2) * (lep_charges.1.powi(2) + lep_charges.2.powi(2)) * (res('V', 'V', "ZZ") + res('A', 'A', "ZZ")),
        _ => panic!("Invalid interaction type: {}", interaction_type)
    };
    coupling
}

pub fn cc_dis_coupling(l_pid: i32, quark1_pid: i32, quark2_pid: i32, q2: f64) -> f64 {
    if l_pid > 0 {prop_factor("W", q2) * lepton_coupling("w", l_pid, "L") * 2.0 * cc_quark_coupling(quark1_pid, quark2_pid) } 
    else { prop_factor("W", q2) * lepton_coupling("w", l_pid, "R") * 2.0 * cc_quark_coupling(quark1_pid, quark2_pid) }
}

/*---------------------------------------\
|                                        |
|                                        |
|         unpol SIDIS couplings          |
|                                        |
|                                        |
\---------------------------------------*/

pub fn nc_sidis_coupling(interaction_type: &str, coupling_type: &str, l_pid: i32, quark1_pid: i32, quark2_pid: i32, q2: f64) -> f64 {
    let coupling_piece = match interaction_type {
        "em" => match coupling_type {
            "v" => prop_factor("phph", q2) * lepton_coupling("phph", l_pid, "unpol") * nc_quark_coupling("v_phph", quark1_pid, quark2_pid),
            "a" => 0.0,
            _ => panic!("Invalid coupling type: {} for EM interaction", coupling_type),
        },
        "nc" => match coupling_type {
            "v" => nc_sidis_coupling("em", "v", l_pid, quark1_pid, quark2_pid, q2) +
                prop_factor("phZ", q2) * lepton_coupling("phZ", l_pid, "unpol") * nc_quark_coupling("v_phZ", quark1_pid, quark2_pid) +
                prop_factor("ZZ", q2) * lepton_coupling("ZZ", l_pid, "unpol") * nc_quark_coupling("v_ZZ", quark1_pid, quark2_pid),
            "a" => prop_factor("ZZ", q2) * lepton_coupling("ZZ", l_pid, "unpol") * nc_quark_coupling("a_ZZ", quark1_pid, quark2_pid),
            "i" => prop_factor("phZ", q2) * lepton_coupling("phZ_pv", l_pid, "unpol") * nc_quark_coupling("i_phZ", quark1_pid, quark2_pid) +
                prop_factor("ZZ", q2) * lepton_coupling("ZZ_pv", l_pid, "unpol") * nc_quark_coupling("i_ZZ", quark1_pid, quark2_pid),
            _ => panic!("Invalid coupling type: {} for NC interaction", coupling_type),
        },
        _ => panic!("Invalid interaction type: {}", interaction_type),
    };
    coupling_piece
}

pub fn cc_sidis_coupling(l_pid: i32, quark1_pid: i32, quark2_pid: i32, q2: f64) -> f64 {
    // if l_pid > 0 {
    //     prop_factor("W", q2) * lepton_coupling("w", l_pid, "L") * 2.0 * cc_quark_coupling(quark1_pid, quark2_pid)
    // } else {
    //     prop_factor("W", q2) * lepton_coupling("w", l_pid, "R") * 2.0 * cc_quark_coupling(quark1_pid, quark2_pid)
    // }
    cc_dis_coupling(l_pid, quark1_pid, quark2_pid, q2)
}

pub fn nc_sym_default(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        let coupling_v = nc_sidis_coupling(interaction_type, "v", l_pid, i, i, q2);
        let coupling_a = nc_sidis_coupling(interaction_type, "a", l_pid, i, i, q2);
        vec.push((i, i, coupling_v + coupling_a));
        vec.push((-i, -i, coupling_v + coupling_a));
    }
    vec
}

pub fn nc_sym_q2g(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_sym_default(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.1 = 21);
    vec
}

pub fn nc_sym_g2q(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_sym_default(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.0 = 21);
    vec
}

pub fn nc_sym_q2qmfcon2(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        let mut entry: f64 = 0.0;
        for j in 1..=nf {
            if j != i {
                entry += nc_sidis_coupling(interaction_type, "v", l_pid, j, j, q2) + nc_sidis_coupling(interaction_type, "a", l_pid, j, j, q2);
            }
        }
        vec.push((i, i, entry));
        vec.push((-i, -i, entry));
    }
    vec
}

pub fn nc_sym_q2qmanow(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        // let mut entry, : f64 = quark_charges(i).2;
        let mut entry: f64 = 0.0;
        for j in 1..=nf {
            if j != i {
                entry += quark_charges(j).2;
            }
        }
        entry *= quark_charges(i).2;
        vec.push((i, i, entry));
        vec.push((-i, -i, entry))
    }
    vec
}

pub fn nc_sym_q2gmanow(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_sym_q2qmanow(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.1 = 21);
    vec
}

pub fn nc_syn_g2qmanow(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_sym_q2qmanow(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.0 = 21);
    vec
}

pub fn nc_sym_g2g(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut entry: f64 = 0.0;
    for i in 1..=nf {
        entry += nc_sidis_coupling(interaction_type, "v", l_pid, i, i, q2) + nc_sidis_coupling(interaction_type, "a", l_pid, i, i, q2);
    }
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    vec.push((21, 21, entry));
    vec
} 

pub fn nc_sym_g2gmaanow(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut entry: f64 = 0.0;
    for i in 1..=nf {
        entry += quark_charges(i).2;
    }
    entry *= entry;
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    vec.push((21, 21, entry));
    vec
}

pub fn nc_sym_q2qpm1(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "v", l_pid, i, i, q2) + nc_sidis_coupling(interaction_type, "a", l_pid, i, i, q2);
                vec.push((i, j, entry));
                vec.push((-i, -j, entry));
                vec.push((i, -j, entry));
                vec.push((-i, j, entry));
            }
        }
    }
    vec
}

pub fn nc_sym_q2qpm2(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "v", l_pid, j, j, q2) + nc_sidis_coupling(interaction_type, "a", l_pid, j, j, q2);
                vec.push((i, j, entry));
                vec.push((-i, -j, entry));
                vec.push((i, -j, entry));
                vec.push((-i, j, entry));
            }
        }
    }
    vec
}

pub fn nc_sym_mnow3(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "v", l_pid, i, j, q2);
                vec.push((i, j, entry));
                vec.push((i, -j, -entry));
                vec.push((-i, -j, entry));
                vec.push((-i, j, -entry));
            }
        }
    }
    vec
}

pub fn nc_sym_mnow4(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "a", l_pid, i, j, q2);
                vec.push((i, j, entry));
                vec.push((i, -j, entry));
                vec.push((-i, -j, entry));
                vec.push((-i, j, entry));
            }
        }
    }
    vec
}

pub fn nc_sym_q2qb(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_sym_default(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.1 = -e.1);
    vec
}

pub fn nc_asym_default(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_sym_default(nf, interaction_type, l_pid, q2);
    for i in 1..=nf {
        let coupling = nc_sidis_coupling(interaction_type, "i", l_pid, i, i, q2);
        vec.push((i, i, coupling));
        vec.push((-i, -i, -coupling));
    }
    vec
}

pub fn nc_asym_q2g(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_asym_default(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.1 = 21);
    vec
}

pub fn nc_asym_g2q(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_asym_default(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.0 = 21);
    vec
}

pub fn nc_asym_q2qmanow(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        // let mut entry, : f64 = quark_charges(i).2;
        let mut entry: f64 = 0.0;
        for j in 1..=nf {
            if j != i {
                entry += quark_charges(j).2;
            }
        }
        entry *= 2.0 * quark_charges(i).1;
        vec.push((i, i, entry));
        vec.push((-i, -i, -entry))
    }
    vec
}

pub fn nc_asym_q2gmanow(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_asym_q2qmanow(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.1 = 21);
    vec
}

pub fn nc_asym_g2qmanow(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_asym_q2qmanow(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.0 = 21);
    vec
}

pub fn nc_asym_q2qpm1(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "i", l_pid, i, i, q2);
                vec.push((i, j, entry));
                vec.push((-i, -j, -entry));
                vec.push((i, -j, entry));
                vec.push((-i, j, -entry));
            }
        }
    }
    vec
}

pub fn nc_asym_q2qpm2(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "i", l_pid, j, j, q2);
                vec.push((i, j, entry));
                vec.push((-i, -j, -entry));
                vec.push((i, -j, -entry));
                vec.push((-i, j, entry));
            }
        }
    }
    vec
}

pub fn nc_asym_mnow3(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "i", l_pid, i, j, q2);
                vec.push((i, j, entry));
                vec.push((-i, -j, -entry));
                vec.push((i, -j, entry));
                vec.push((-i, j, -entry));
            }
        }
    }
    vec
}

pub fn nc_asym_mnow4(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec: Vec<(i32, i32, f64)> = vec![];
    for i in 1..=nf {
        for j in 1..=nf {
            if j != i {
                let entry: f64 = nc_sidis_coupling(interaction_type, "i", l_pid, j, i, q2);
                vec.push((i, j, entry));
                vec.push((-i, -j, -entry));
                vec.push((i, -j, -entry));
                vec.push((-i, j, entry));
            }
        }
    }
    vec
}

pub fn nc_asym_q2qb(nf: i32, interaction_type: &str, l_pid: i32, q2: f64) -> Vec<(i32, i32, f64)> {
    let mut vec = nc_asym_default(nf, interaction_type, l_pid, q2);
    vec.iter_mut().for_each(|e| e.1 = -e.1);
    vec
}
