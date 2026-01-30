use crate::dis::internal::*;
use super::super::fl::flnc_nnlo_nsp;

fn r_00(x: f64, nf: f64) -> f64 {
    return flnc_nnlo_nsp::cf().r.unwrap()(x, nf);
}

fn l_00(x: f64, nf: f64) -> f64 {
    return flnc_nnlo_nsp::cf().l.unwrap()(x, nf);
}

mkcoeff!(r_00, _, l_00);
