use crate::sia::internal::*;

fn r_00(z: f64, _nf: f64) -> f64 {    
    let Hr10 = h0(z);
    let Hr11 = h1(z);
    let Hr2m10 = hm10(z);
    let Hr200 = h00(z);
    let Hr201 = h01(z);
    let Hr211 = h11(z);
    let Hr3000 = h000(z);
    let Hr3001 = h001(z);
    let Hr3011 = h011(z);

    let result = CF * ( - 118./3. + 70./3.*z + 512./27.*z*z - 80./27./z + 16.*z3 + 16.*z3*z - 8.*z2 - 32.*z2*z - 200./ 3.*Hr10 - 104./3.*Hr10*z - 128./9.*Hr10*z*z - 16./3.*Hr10/z + 16.*Hr10*z2 + 16.*Hr10*z2*z + 92. /3.*Hr11 - 68./3.*Hr11*z - 32./3.*Hr11*z*z + 8./3.*Hr11/z - 16.*Hr2m10 - 16.*Hr2m10*z - 16. /3.*Hr2m10*z*z - 16./3.*Hr2m10/z - 14.*Hr200 - 14.*Hr200*z + 16./3.*Hr200*z*z + 64./3.*Hr200/z + 4.*Hr201 + 20.*Hr201*z + 16./3.*Hr201* z*z - 32./3.*Hr201/z + 4.*Hr211 - 4.*Hr211*z - 16./3.*Hr211*z*z + 16./3.*Hr211/z + 44.*Hr3000 + 44.*Hr3000*z - 24.*Hr3001 - 24.*Hr3001*z + 8.* Hr3011 + 8.*Hr3011*z );
    result
}

mkcoeff!(r_00, _, _);