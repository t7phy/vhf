#![allow(unused_variables)]
#![allow(non_upper_case_globals)]

pub(crate) mod internal {
    pub use crate::core::libfunc::{pow, log};
    pub use crate::core::constants::{CA, CF, TR, z2, z3};
    pub use crate::core::nielsen::nl;
    // pub use polylog::Li2;
    pub const d3: f64 = 1.0 / 3.0;
    pub const d9: f64 = 1.0 / 9.0;
    pub const d27: f64 = 1.0 / 27.0;
    pub const d81: f64 = 1.0 / 81.0;
    pub const d243: f64 = 1.0 / 243.0;
}

pub mod f2;
pub mod f3;
pub mod fl;
pub mod g1;
pub mod g4;
pub mod gl;
