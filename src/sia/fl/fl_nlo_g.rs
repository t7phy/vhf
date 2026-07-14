use crate::sia::internal::*;

fn r_00(z: f64, _nf: f64) -> f64 {
    8. * CF * ( 1. - z ) / z
}

mkcoeff!(r_00, _, _);
