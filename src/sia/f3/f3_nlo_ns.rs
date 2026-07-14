use crate::sia::internal::*;

fn r_00(z: f64, _nf: f64) -> f64 {
    2. * CF * ( - ( 1. + z ) * log( 1. - z ) - 2. * ( 1. + pow(z, 2) ) * log(z) / ( 1. - z ) + 1. / 2. - z / 2. )
}

fn s_00(z: f64, _nf: f64) -> f64 {
    2. * CF * ( 2. * log( 1. - z ) - 3. / 2. ) / ( 1. - z )
}

fn l_00(z: f64, _nf: f64) -> f64 {
    2. * CF * ( pow(log( 1. - z ), 2) - 3. * log( 1. - z ) / 2. + ( 4. * z2 - 9. / 2. ) )
}

mkcoeff!(r_00, s_00, l_00);
