use crate::sia::internal::*;

fn r_00(z: f64, _nf: f64) -> f64 {
    let Hr10 = h0(z);
    let Hr11 = h1(z);
    let Hr200 = h00(z);
    let Hr201 = h01(z);

    let result = CF * ( - 56./3. + 104./3.*z - 8.*z*z - 8./z + 8.*z2 - 16.*Hr10 - 16.*Hr10*z + 8./3.*Hr10*z*z + 32./3.*Hr10/z + 8.*Hr11*z - 8./3.*Hr11*z*z - 16./3.*Hr11/z + 24.*Hr200 - 8.*Hr201 );
    result
}

mkcoeff!(r_00, _, _);
