use crate::dis::internal::*;
use super::super::f2::f2nc_nnlo_nsp;

fn r_00(x: f64, nf: f64) -> f64 {
    return f2nc_nnlo_nsp::cf().r(x, nf);
}

fn s_00(x: f64, nf: f64) -> f64 {
    return f2nc_nnlo_nsp::cf().s(x, nf);
}

fn l_00(x: f64, nf: f64) -> f64 {
    return f2nc_nnlo_nsp::cf().l(x, nf);
}

mkcoeff!(r_00, s_00, l_00);
