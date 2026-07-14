use crate::sia::internal::*;

fn r_00(z: f64, nf: f64) -> f64 {
    let dz = 1.0/z;
    let dm = 1.0/(1.0-z);
    let dp = 1.0/(1.0+z);
    let dl1 = log(1.0-z);
    let a3 = 8.0*pow(CF, 2);
    let a2 = - 22.0/3.0*CA*CF - 18.0*pow(CF, 2) + 4.0/3.0*CF*nf;
    let a1 = - 8.0*z2*CA*CF + 16.0*z2*pow(CF, 2) + 367.0/9.0*CA*CF - 27.0*pow(CF, 2) - 58.0/9.0*CF*nf;
    let a0 = 44.0/3.0*z2*CA*CF + 40.0*z3*CA*CF - 8.0*z3*pow(CF, 2) - 3155.0/54.0*CA*CF + 51.0/2.0*pow(CF, 2) + 247.0/27.0*CF*nf - 8.0/3.0*z2*CF*nf;

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
    let Hr3m101 = hm101(z);
    let Hr30m10 = h0m10(z);
    let Hr3000 = h000(z);
    let Hr3001 = h001(z);
    let Hr3010 = h010(z);
    let Hr3011 = h011(z);
    let Hr3100 = h100(z);
    let Hr3101 = h101(z);
    let Hr3110 = h110(z);
    let Hr3111 = h111(z);

    let result1 = CF * CA * ( 325./54. + 895./54.*z - 3155./54.*dm - 36.*z3 + 28.*z3*dp + 28.*z3*dm + 12.*z2 + 8.*z2*z + 8.*z2*z2 + 20.*Hr1m1*z2 - 12.*Hr1m1*z2*z - 32. *Hr1m1*z2*dp + 27.*Hr10 - 193./3.*Hr10*z - 8.* Hr10*dp + 206./3.*Hr10*dm + 20.*Hr10*z2 + 12.* Hr10*z2*z - 8.*Hr10*z2*dp - 32.*Hr10*z2*dm - 19./ 9.*Hr11 + 305./9.*Hr11*z - 367./9.*Hr11*dm + 8.*Hr11*z2*z - 8.*Hr11*z2*dm + 4.*Hr2m10 + 4.* Hr2m10*z + 8.*Hr2m10*z2 + 8.*Hr2m10*dz + 59./ 3.*Hr200 + 71./3.*Hr200*z - 8.*Hr200*z2 - 22./3.*Hr200*dm - 46./3.*Hr201 - 46./3.* Hr201*z + 44./3.*Hr201*dm + 22./3.*Hr211 + 22./3.*Hr211*z - 44./3.*Hr211*dm + 24.*Hr3m1m10 - 8.*Hr3m1m10*z - 32.*Hr3m1m10*dp + 8.* Hr3m100 - 16.*Hr3m100*z - 24.*Hr3m100*dp - 8. *Hr3m101 ) + CF * CA * ( 8.*Hr3m101*z + 16.*Hr3m101* dp + 16.*Hr30m10 - 8.*Hr30m10*dp - 24.*Hr30m10*dm - 36.*Hr3000 + 36.*Hr3000*dp + 36.*Hr3000*dm + 4.*Hr3001 - 4.*Hr3001*z - 8.*Hr3001*dp + 4.*Hr3010 + 4.*Hr3010*z - 8.*Hr3010*dm + 12.*Hr3100 + 4.*Hr3100*z - 16.*Hr3100*dm - 4.*Hr3101 - 4.*Hr3101*z + 8.*Hr3101* dm + 4.*Hr3110 + 4.*Hr3110*z - 8.*Hr3110*dm ) + CF * CF * (  - 19./2. + 19./2.*z + 51./2. *dm + 128.*z3 + 56.*z3*z - 56.*z3*dp - 152.*z3*dm - 52.*z2 - 20.*z2*z - 16.*z2*z2 + 12.*z2*dm - 40.* Hr1m1*z2 + 24.*Hr1m1*z2*z + 64.*Hr1m1*z2*dp - 2.* Hr10 + 92.*Hr10*z + 16.*Hr10*dp - 106.*Hr10*dm - 20.*Hr10*z2 - 4.*Hr10*z2*z + 16.*Hr10*z2*dp + 40.*Hr10*z2*dm - 5.*Hr11 - 33.*Hr11*z + 27.* Hr11*dm + 8.*Hr11*z2 - 8.*Hr11*z2*z - 8.*Hr2m10 - 8.*Hr2m10*z - 16.*Hr2m10*z2 - 16.*Hr2m10 *dz - 86.*Hr200 - 74.*Hr200*z + 16.*Hr200*z2 + 66.*Hr200*dm + 32.*Hr201 + 8.*Hr201*z + 12. *Hr201*dm - 12.*Hr210 + 12.*Hr210*z + 24.* Hr210*dm + 8.*Hr211 + 16.*Hr211*z - 36.*Hr211*dm - 48.*Hr3m1m10 + 16.*Hr3m1m10*z + 64.* Hr3m1m10*dp - 16.*Hr3m100 + 32.*Hr3m100*z + 48.*Hr3m100*dp ) + CF * CF * ( 16.*Hr3m101 - 16.*Hr3m101*z- 32.*Hr3m101*dp - 32.*Hr30m10 + 16.*Hr30m10*dp+ 48.*Hr30m10*dm + 138.*Hr3000 + 66.*Hr3000*z- 72.*Hr3000*dp - 160.*Hr3000*dm - 24.*Hr3001 - 8.*Hr3001*z + 16.*Hr3001*dp + 8.*Hr3001*dm + 36.*Hr3010 + 36.*Hr3010*z - 72.*Hr3010*dm - 16.*Hr3011 - 16.*Hr3011*z + 40.*Hr3011*dm - 28.*Hr3100 - 12.*Hr3100*z + 40.*Hr3100*dm - 16.*Hr3101 - 16.*Hr3101*z + 32.*Hr3101*dm - 24.*Hr3110 - 24.*Hr3110*z + 48.*Hr3110*dm + 24.*Hr3111 + 24.*Hr3111*z - 48.*Hr3111*dm ) + nf * CF * ( 55./27. - 131./27.*z + 247./  27.*dm + 2.*Hr10 + 22./3.*Hr10*z - 32./3.*  Hr10*dm - 2./9.*Hr11 - 38./9.*Hr11*z + 58./9.  *Hr11*dm - 2./3.*Hr200 - 2./3.*Hr200*z + 4.  /3.*Hr200*dm + 4./3.*Hr201 + 4./3.*Hr201*z  - 8./3.*Hr201*dm - 4./3.*Hr211 - 4./3.*  Hr211*z + 8./3.*Hr211*dm );
    let result2 = dm * ( pow(dl1, 3) * a3 + pow(dl1, 2) * a2 + dl1 * a1 + a0 );
    result1 - result2
}

fn s_00(z: f64, nf: f64) -> f64 {
    let dm = 1.0/(1.0-z);
    let dl1 = log(1.0-z);
    let a3 = 8.0*pow(CF, 2);
    let a2 = - 22.0/3.0*CA*CF - 18.0*pow(CF, 2) + 4.0/3.0*CF*nf;
    let a1 = - 8.0*z2*CA*CF + 16.0*z2*pow(CF, 2) + 367.0/9.0*CA*CF - 27.0*pow(CF, 2) - 58.0/9.0*CF*nf;
    let a0 = 44.0/3.0*z2*CA*CF + 40.0*z3*CA*CF - 8.0*z3*pow(CF, 2) - 3155.0/54.0*CA*CF + 51.0/2.0*pow(CF, 2) + 247.0/27.0*CF*nf - 8.0/3.0*z2*CF*nf;

    let result = dm * ( pow(dl1, 3) * a3 + pow(dl1, 2) * a2 + dl1 * a1 + a0);
    result
}

fn l_00(z: f64, nf: f64) -> f64 {
    let dl1 = log(1.0-z);
    let a3 = 8.0*pow(CF, 2);
    let a2 = - 22.0/3.0*CA*CF - 18.0*pow(CF, 2) + 4.0/3.0*CF*nf;
    let a1 = - 8.0*z2*CA*CF + 16.0*z2*pow(CF, 2) + 367.0/9.0*CA*CF - 27.0*pow(CF, 2) - 58.0/9.0*CF*nf;
    let a0 = 44.0/3.0*z2*CA*CF + 40.0*z3*CA*CF - 8.0*z3*pow(CF, 2) - 3155.0/54.0*CA*CF + 51.0/2.0*pow(CF, 2) + 247.0/27.0*CF*nf - 8.0/3.0*z2*CF*nf;

    let result1 = CA*CF * ( - 5465./72. + 140./3.*z3 + 215./3.*z2 - 49./5.*pow(z2, 2) ) + CF*CF * ( 331./8. - 78.*z3 - 39.*z2 + 30.*pow(z2, 2) ) + CF*nf * ( 457./36. + 4./3.*z3 - 38./3.*z2 );
    let result2 = pow(dl1, 4) * a3/4. + pow(dl1, 3) * a2/3.  + pow(dl1, 2) * a1/2. + dl1 * a0;
    result1 + result2
}

mkcoeff!(r_00, s_00, l_00);
