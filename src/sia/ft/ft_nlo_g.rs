use crate::sia::internal::*;

fn r_00(z: f64, nf: f64) -> f64 {
    4.0 * CF * (2.0 * (-1.0 + z) + (2.0 + (z - 2.0) * z) * log(- (z - 1.0) * pow(z, 2)))/(z)
}


mkcoeff!(r_00, _, _);
