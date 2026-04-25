#![allow(unused_variables)]
#![allow(non_upper_case_globals)]

pub mod f2;
pub mod f3;
pub mod fl;
pub mod g1;
pub mod g4;
pub mod gl;

pub mod couplings;

pub mod processes;

pub use internal::{CoeffFuncs, DISFunc};

pub(crate) mod internal {
    pub use crate::core::libfunc::{pow, log};
    pub use crate::core::constants::{CA, CF, TR, z2, z3};
    pub use crate::core::polylogs::nl;
    pub use crate::dis::couplings;
    // pub use polylog::Li2;
    pub const d3: f64 = 1.0 / 3.0;
    pub const d9: f64 = 1.0 / 9.0;
    pub const d27: f64 = 1.0 / 27.0;
    pub const d81: f64 = 1.0 / 81.0;
    pub const d243: f64 = 1.0 / 243.0;

    pub const inv4PI: f64 = 1.0 / (4.0 *std::f64::consts::PI);


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
