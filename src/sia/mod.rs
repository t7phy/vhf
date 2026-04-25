// #![allow(unused_variables)]
#![allow(non_upper_case_globals)]
#![allow(non_snake_case)]

pub mod ft;
pub mod fl;
pub mod f3;

pub mod couplings;

pub(crate) mod internal {
    pub use crate::core::libfunc::{pow, log};
    pub use crate::core::constants::{CF, CA, z2, z3};
    pub use crate::core::polylogs::*;
    pub use crate::dis::internal::{CoeffFuncs, zero_func};
    pub use crate::mkcoeff;
}

