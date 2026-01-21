#![allow(unused_variables)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]

pub(crate) mod internal {
    pub use std::collections::HashMap;

    pub use crate::core::libfunc::{pow, ln, ArcTan, InvTanInt};
    pub use crate::core::nielsen::{Li2, Li3};
    pub use crate::core::constants::{NQCD, rln2, pi, zeta3, CF};
    pub const lmur: f64 = 0.5;
    pub const lmuf: f64 = 0.5;
    pub const lmua: f64 = 1.0;

    pub fn mysqrt(x: f64) -> f64 {
        x.sqrt()
    }
}

pub mod ft;
pub mod fl;
pub mod f3;
pub mod gt;
pub mod gl;
pub mod g1;