use crate::core::sm_params::{m_z, m_w, gamma_z};

pub fn sia_couplings(pid: i32, q: f64) -> f64 {
    // from eq. (2.10) of hep-ph/9609377

    let e_l: f64 = -1.0;
    
    let e_q: f64 = match pid {
        1 | 3 | 5 => -1.0 / 3.0,
        2 | 4 | 6 => 2.0 / 3.0,
        -1 | -3 | -5 => 1.0 / 3.0,
        -2 | -4 | -6 => -2.0 / 3.0,
        _ => panic!("Unknown PID {}", pid),
    };

    let theta_w = (m_w() / m_z()).acos();

    let c_a_l = 1.0 / (2.0 * (2.0 * theta_w).sin());
    let c_v_l = -c_a_l * (1.0 - 4.0 * theta_w.sin().powi(2));
    
    let (c_a_q, c_v_q) = match pid.abs() {
        1 | 3 | 5 => {
            (c_a_l, -c_a_l * (1.0 - (4.0 / 3.0) * theta_w.sin().powi(2)))
        }
        2 | 4 | 6 => {
            (-c_a_l, c_a_l * (1.0 - (8.0 / 3.0) * theta_w.sin().powi(2)))
        }
        _ => unreachable!(), // Handled by the panic above
    };

    let abs_z = ((q.powi(2) - m_z().powi(2)).powi(2) + (m_z() * gamma_z()).powi(2)).sqrt();

    let ew_charge = 
        e_l.powi(2) * e_q.powi(2) +
        e_l * e_q * c_v_l * c_v_q * (2.0 * q.powi(2) * (q.powi(2) - m_z().powi(2))) / abs_z.powi(2) +
        (c_v_l.powi(2) + c_a_l.powi(2)) * (c_v_q.powi(2) + c_a_q.powi(2)) * q.powi(2).powi(2) / abs_z.powi(2);

    ew_charge
}