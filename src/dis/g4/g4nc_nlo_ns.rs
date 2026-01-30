use crate::dis::internal::*;
use super::super::f2::f2nc_nlo_ns;

fn r_00(x: f64, nf: f64) -> f64 {
    return f2nc_nlo_ns::cf().r.unwrap()(x, nf);
}

fn s_00(x: f64, nf: f64) -> f64 {
    return f2nc_nlo_ns::cf().s.unwrap()(x, nf);
}

fn l_00(x: f64, nf: f64) -> f64 {
    return f2nc_nlo_ns::cf().l.unwrap()(x, nf);
}

mkcoeff!(r_00, s_00, l_00);
