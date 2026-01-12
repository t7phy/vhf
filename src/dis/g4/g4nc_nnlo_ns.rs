use super::super::f2::f2nc_nnlo_nsp;

pub fn r_00(x: f64, nf: f64) -> f64 {
    return f2nc_nnlo_nsp::r_00(x, nf);
}

pub fn s_00(x: f64, nf: f64) -> f64 {
    return f2nc_nnlo_nsp::s_00(x, nf);
}

pub fn l_00(x: f64, nf: f64) -> f64 {
    return f2nc_nnlo_nsp::l_00(x, nf);
}
