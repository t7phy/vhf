#![allow(unused_variables)]
#![allow(non_upper_case_globals)]
#![allow(non_snake_case)]

pub mod f2_light;
pub mod f2_heavy;
pub mod f3;
pub mod f3_heavy;
pub mod fl_light;
pub mod fl_heavy;
pub mod g1;
pub mod g1_heavy;
pub mod g4;
pub mod g4_heavy;
pub mod gl;
pub mod gl_heavy;

pub mod dis_ext;

pub mod couplings;

pub use internal::{CoeffFuncs, DISFunc};

pub(crate) mod internal {
    pub use crate::core::libfunc::{pow, log, ln};
    pub use crate::core::constants::{CA, CF, TR, z2, z3, pi, rln2};
    pub use crate::core::polylogs::{nl, Li2};
    pub use crate::dis::couplings;
    pub use crate::core::sm_params;
    // pub use polylog::Li2;
    pub const d3: f64 = 1.0 / 3.0;
    pub const d9: f64 = 1.0 / 9.0;
    pub const d27: f64 = 1.0 / 27.0;
    pub const d81: f64 = 1.0 / 81.0;
    pub const d243: f64 = 1.0 / 243.0;

    pub const inv4PI: f64 = 1.0 / (4.0 * pi);

    pub fn get_quark_mass(pid: i8) -> f64 {
        let pid = pid.abs();
        let mass: f64 = match pid {
            1 => sm_params::m_down(),
            2 => sm_params::m_up(),
            3 => sm_params::m_strange(),
            4 => sm_params::m_charm(),
            5 => sm_params::m_bottom(),
            6 => sm_params::m_top(),
            _ => panic!("Invalid flavor number: {}", pid),
        };
        mass
    }

    pub fn below_threshold(x: f64, Q2: f64, m2:f64) -> bool {
        Q2 * (1.0 - x) / x <= 4.0 * m2
    }

    // pub fn mof_fn1(input_type: &str, input: Vec<f64>) -> (f64, f64, f64) {
    //     match (input_type, input.len()) {
    //         ("xi", 1) => {
    //             let rho_q = - 4.0 / input[0];
    //             let beta_q = (1.0 - rho_q).sqrt();
    //             let chi_q = (beta_q - 1.0) / (beta_q + 1.0);
    //             (rho_q, beta_q, chi_q)
    //         },
    //         ("eta", 1) => {
    //             let rho = 1.0 / (1.0 + input[0]);
    //             let beta = (1.0 - rho).sqrt();
    //             let chi = (1.0 - beta) / (1.0 + beta);
    //             (rho, beta, chi)
    //         },
    //         ("prime", 2) => {
    //             let rho = 1.0 / (1.0 + input[1]);
    //             let rho_q = - 4.0 / input[0];
    //             let rho_p = 1.0 / (1.0 / rho - 1.0 / rho_q);
    //             let beta_p = (1.0 - rho_p).sqrt();
    //             let chi_p = (1.0 - beta_p) / (1.0 + beta_p);
    //             (rho_p, beta_p, chi_p)
    //         },
    //         _ => panic!("Invalid input type or length: {} with length {}", input_type, input.len()),
    //     }
    // }
    pub fn mof_xi(xi: f64) -> (f64, f64, f64) {
        let rho_q = - 4.0 / xi;
        let beta_q = (1.0 - rho_q).sqrt();
        let chi_q = (beta_q - 1.0) / (beta_q + 1.0);
        (rho_q, beta_q, chi_q)
    }
    pub fn mof_eta(eta: f64) -> (f64, f64, f64) {
        let rho = 1.0 / (1.0 + eta);
        let beta = (1.0 - rho).sqrt();
        let chi = (1.0 - beta) / (1.0 + beta);
        (rho, beta, chi)
    }
    pub fn mof_prime(xi: f64, eta: f64) -> (f64, f64, f64) {
        let rho = 1.0 / (1.0 + eta);
        let rho_q = - 4.0 / xi;
        let rho_p = 1.0 / (1.0 / rho - 1.0 / rho_q);
        let beta_p = (1.0 - rho_p).sqrt();
        let chi_p = (1.0 - beta_p) / (1.0 + beta_p);
        (rho_p, beta_p, chi_p)
    }

    pub type DISFunc = fn(f64, f64) -> f64;

    #[derive(Clone, Copy)]
    pub struct CoeffFuncs {
        pub r_fn: DISFunc,
        pub s_fn: DISFunc,
        pub l_fn: DISFunc,
    }

    impl CoeffFuncs {
        pub fn r(&self, x: f64, y: f64) -> f64 { (self.r_fn)(x, y) }
        pub fn s(&self, x: f64, y: f64) -> f64 { (self.s_fn)(x, y) }
        pub fn l(&self, x: f64, y: f64) -> f64 { (self.l_fn)(x, y) }
    }

    pub fn zero_func(_: f64, _: f64) -> f64 {
        0.0
    }

    #[macro_export]
    macro_rules! mkcoeff {
        // Pattern 1: Helper for function names
        // (wrap _) => { None };
        // (wrap $id:ident) => { Some($id) };
        (wrap _) => { zero_func };
        (wrap $id:ident) => { $id };

        // Pattern 2: The main call
        ($r:tt, $s:tt, $l:tt) => {
            pub fn cf() -> CoeffFuncs {
                CoeffFuncs {
                    r_fn: mkcoeff!(wrap $r),
                    s_fn: mkcoeff!(wrap $s),
                    l_fn: mkcoeff!(wrap $l),
                }
            }
        };
    }
    
    pub(crate) use mkcoeff;
}

pub fn dis_factor_none(_: f64, _: f64) -> f64 {
    1.0
}
pub fn dis_factor_f2(x: f64, q: f64) -> f64 {
    todo!()
}
pub fn dis_factor_fl(x: f64, q: f64) -> f64 {
    todo!()
}
pub fn dis_factor_f3(x: f64, q: f64) -> f64 {
    todo!()
}
pub fn dis_factor_global(x: f64, q: f64) -> f64 {
    todo!()
}

// struct CfBox {
//     pub cf: internal::CoeffFuncs,
//     pub coupling: fn(i8, f64, String, bool) -> Vec<(i8, f64)>,
//     // pub norm:
//     pub orders: [i8; 5],
//     as_norm: f64,
// }

// impl CfBox {
//     fn new(cf: internal::CoeffFuncs, 
//         coupling: fn(i8, f64, String, bool) -> Vec<(i8, f64)>,
//         orders: [i8; 5],
//         as_norm: f64) -> Self {
//         Self {
//             cf,
//             coupling,
//             orders,
//             as_norm,
//         }
//     }
// }
