use crate::dis::internal::*;
use super::super::f3::f3nc_nlo_ns;

fn r_00(x: f64, nf: f64) -> f64 {
    return f3nc_nlo_ns::cf().r(x, nf);
}

fn s_00(x: f64, nf: f64) -> f64 {
    return f3nc_nlo_ns::cf().s(x, nf);  
}

fn l_00(x: f64, nf: f64) -> f64 {
    return f3nc_nlo_ns::cf().l(x, nf);
}

mkcoeff!(r_00, s_00, l_00);
