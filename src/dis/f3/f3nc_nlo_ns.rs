use crate::dis::internal::*;
use super::super::f2::f2nc_nlo_ns;

pub fn r_00(x: f64, nf: f64) -> f64 {
    let res: f64 = f2nc_nlo_ns::r_00(x, nf) - 2.0 * CF * (1.0 + x);
    return res;
}

pub fn s_00(x: f64, nf: f64) -> f64 {
    return f2nc_nlo_ns::s_00(x, nf);
}

pub fn l_00(x: f64, nf: f64) -> f64 {
    return f2nc_nlo_ns::l_00(x, nf);
}
