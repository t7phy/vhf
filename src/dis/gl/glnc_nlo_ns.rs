use crate::dis::internal::*;
use super::super::fl::flnc_nlo_ns;

fn r_00(x: f64, nf: f64) -> f64 {
    return flnc_nlo_ns::cf().r(x, nf);
}

mkcoeff!(r_00, _, _);
