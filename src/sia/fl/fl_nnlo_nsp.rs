use crate::sia::internal::*;

fn r_00(z: f64, nf: f64) -> f64 {
    let dz = 1.0 / z;
    let Hr1m1 = hm1(z);
    let Hr10 = h0(z);
    let Hr11 = h1(z);
    let Hr2m10 = hm10(z);
    let Hr200 = h00(z);
    let Hr201 = h01(z);
    let Hr210 = h10(z);
    let Hr211 = h11(z);
    let Hr3m1m10 = hm1m10(z);
    let Hr3m100 = hm100(z);
    let Hr30m10 = h0m10(z);
    let Hr3100 = h100(z);

    let result = CF * CA * ( 1729./45. - 98./15.*z - 16./5.*z*z -24./5.*dz + 16.*z2*z + 16./5.*z2*z*z*z - 8.*Hr1m1*z2- 146./15.*Hr10 + 8./5.*Hr10*z - 16./5.*Hr10*z*z + 24./5.*Hr10*dz + 46./3.*Hr11 - 8.*Hr11*z2 + 8.*Hr2m10 + 16.*Hr2m10*z + 16./5.*Hr2m10*z*z*z - 24./5.*Hr2m10*dz*z - 16.*Hr200*z - 16./5.*Hr200*z*z*z - 16.*Hr3m1m10 + 8.*Hr3m100+ 16.*Hr30m10 + 8.*Hr3100 ) + CF * CF * ( - 147./5. - 18./5.*z + 32./5.*z*z + 48./5.*dz + 4.*z2 - 32.*z2*z - 32./5.*z2*z*z*z + 16.*Hr1m1*z2 + 34./5.*Hr10 + 24./5.*Hr10*z + 32./5.*Hr10*z*z - 48./5.*Hr10*dz - 14.*Hr11 - 4.*Hr11*z + 16.*Hr11*z2 - 16.*Hr2m10- 32.*Hr2m10*z - 32./5.*Hr2m10*z*z*z + 48./5.*Hr2m10*dz*z - 12.*Hr200 + 32.*Hr200*z + 32./5.*Hr200*z*z*z - 4.*Hr201 - 16.*Hr210 + 8.*Hr211 + 32.*Hr3m1m10 - 16.*Hr3m100 - 32.*Hr30m10 - 16.*Hr3100 ) + nf * CF * ( - 50./9. + 4./3.*z + 4./3. *Hr10 - 4./3.*Hr11 );
    result
}

mkcoeff!(r_00, _, _);
