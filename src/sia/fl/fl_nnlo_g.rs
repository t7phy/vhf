use crate::sia::internal::*;

fn r_00(z: f64, nf: f64) -> f64 {
    let dz = 1.0 / z;
    let Hr10 = h0(z);
    let Hr11 = h1(z);
    let Hr2m10 = hm10(z);
    let Hr200 = h00(z);
    let Hr201 = h01(z);
    let Hr210 = h10(z);
    let Hr211 = h11(z);

    let result = CF * CA * ( - 320./3. - 160./3.*z + 32./3.*z*z +448./3.*dz - 64.*z2 + 32.*z2*dz + 112.*Hr10 + 32.*Hr10*z- 16./3.*Hr10*z*z - 352./3.*Hr10*dz - 144.*Hr11- 16.*Hr11*z + 16./3.*Hr11*z*z + 464./3.*Hr11*dz + 32.*Hr2m10 + 32.*Hr2m10*dz - 96.*Hr200 - 128.*Hr200*dz+ 64.*Hr201 + 64.*Hr210 - 64.*Hr210*dz - 32.*Hr211 + 32.*Hr211*dz ) + CF * CF * ( 24./5. + 248./15.*z - 32./15.*z*z - 96./5.*dz + 16.*z2 + 32./15.*z2*z*z*z - 8./5.*Hr10 - 224./15.*Hr10*z - 32./15.*Hr10*z*z+ 96./5.*Hr10*dz + 24.*Hr11 + 8.*Hr11*z - 32.*Hr11*dz - 32./3.*Hr2m10 + 32./15.*Hr2m10*z*z*z + 64./5.*Hr2m10*dz*z + 48.*Hr200 - 32./15.*Hr200*z*z*z - 16.*Hr201 );
    result
}

mkcoeff!(r_00, _, _);
