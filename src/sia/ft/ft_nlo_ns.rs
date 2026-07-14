use crate::sia::internal::*;

fn r_00(z: f64, _nf: f64) -> f64 {
    CF * (3.0 * pow(-1.0 + z, 2) + 2.0 * (-1.0 + pow(z, 2)) * log(1.0 - z) + 4.0 * (1.0 + pow(z, 2))*log(z))/(1.0 - z)
}

fn s_00(z: f64, _nf: f64) -> f64 {
    2.0 * CF * ( 2.0 * log( 1.0 - z ) - 3.0 / 2.0 ) / ( 1.0 - z )
}

fn l_00(z: f64, _nf: f64) -> f64 {
    2.0 * CF * ( pow(log( 1.0 - z ), 2) - 3.0 * log( 1.0 - z ) / 2.0 + ( 4.0 * z2 - 9.0 / 2.0 ) )
}

mkcoeff!(r_00, s_00, l_00);
