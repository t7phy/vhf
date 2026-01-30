use crate::dis::internal::*;
use super::super::f3::f3nc_nnlo_nsp;

fn r_00(x: f64, nf: f64) -> f64 {
    return f3nc_nnlo_nsp::cf().r.unwrap()(x, nf);
}

fn s_00(x: f64, nf: f64) -> f64 {
    return f3nc_nnlo_nsp::cf().s.unwrap()(x, nf);
}

fn l_00(x: f64, nf: f64) -> f64 {
    return f3nc_nnlo_nsp::cf().l.unwrap()(x, nf);
}

mkcoeff!(r_00, s_00, l_00);
