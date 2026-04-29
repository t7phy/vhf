#![allow(non_snake_case)]

use num_complex::Complex64;
use super::constants::pi as PI;
use super::constants::{ZETA3};

// Constants from Python
const I: Complex64 = Complex64::new(0.0, 1.0);
const Z0: f64 = 0.0;
const Z1: f64 = 1.0;
const HF: f64 = Z1 / 2.0;
const C1: f64 = 4.0 * Z1 / 3.0;
const C2: f64 = Z1 / 3.0;

const FCT: [f64; 5] = [1.0, 1.0, 2.0, 6.0, 24.0];
const SGN: [f64; 5] = [1.0, -1.0, 1.0, -1.0, 1.0];

const S1: [[f64; 4]; 4] = [
    [1.6449340668482, 1.2020569031596, 1.0823232337111, 1.0369277551434],
    [1.2020569031596, 0.27058080842778, 0.096551159989444, f64::NAN],
    [1.0823232337111, 0.096551159989444, f64::NAN, f64::NAN],
    [1.0369277551434, f64::NAN, f64::NAN, f64::NAN],
];

const C: [[f64; 4]; 4] = [
    [1.6449340668482, 1.2020569031596, 1.0823232337111, 1.0369277551434],
    [0.0, -1.8940656589945, -3.0142321054407, f64::NAN],
    [1.8940656589945, 3.0142321054407, f64::NAN, f64::NAN],
    [0.0, f64::NAN, f64::NAN, f64::NAN],
];

const INDEX: [usize; 31] = [
    1, 2, 3, 4, 0, 0, 0, 0, 0, 0,
    5, 6, 7, 0, 0, 0, 0, 0, 0, 0,
    8, 9, 0, 0, 0, 0, 0, 0, 0, 0,
    10,
];

const NC: [usize; 10] = [24, 26, 28, 30, 22, 24, 26, 19, 22, 17];

const A: [[f64; 10]; 31] = [
    [0.96753215043498, 0.95180889127832, 0.98161027991365, 1.0640521184614, 0.97920860669175, 0.95021851963952, 0.95064032186777, 0.98800011672229, 0.95768506546350, 0.99343651671347],
    [0.16607303292785, 0.43131131846532, 0.72926806320726, 1.0691720744981, 0.08518813148683, 0.29052529161433, 0.54138285465171, 0.04364067609601, 0.19725249679534, 0.02225770126826],
    [0.02487932292423, 0.10002250714905, 0.22774714909321, 0.41527193251768, 0.00855985222013, 0.05081774061716, 0.13649979590321, 0.00295091178278, 0.02603370313918, 0.00101475574703],
    [0.00468636195945, 0.02442415595220, 0.06809083296197, 0.14610332936222, 0.00121177214413, 0.00995543767280, 0.03417942328207, 0.00031477809720, 0.00409382168261, 8.17515625e-5],
    [0.00100162749616, 0.00622512463724, 0.02013701183064, 0.04904732648784, 0.00020722768531, 0.00211733895031, 0.00869027883583, 4.314846029e-5, 0.00072681707110, 8.99973547e-6],
    [0.00023200219609, 0.00164078831235, 0.00595478480197, 0.01606340860396, 3.996958691e-5, 0.00047859470550, 0.00225284084155, 6.9381823e-6, 0.00014091879261, 1.20823987e-6],
    [5.681782272e-5, 0.00044407920265, 0.00176769013959, 0.00518889350790, 8.38064065e-6, 0.00011334321308, 0.00059516089806, 1.2464035e-6, 2.920458914e-5, 1.8616913e-7],
    [1.449630056e-5, 0.00012277494168, 0.00052748218502, 0.00166298717324, 1.86848945e-6, 2.784733104e-5, 0.00015995617766, 2.4293628e-7, 6.37631144e-6, 3.174723e-8],
    [3.81632946e-6, 3.453981284e-5, 0.00015827461460, 0.00053058279969, 4.3666087e-7, 7.04788108e-6, 4.365213096e-5, 5.040827e-8, 1.4516785e-6, 5.85215e-9],
    [1.02990426e-6, 9.85869565e-6, 4.774922076e-5, 0.00016887029251, 1.0591733e-7, 1.8278874e-6, 1.207474688e-5, 1.099075e-8, 3.4205281e-7, 1.14739e-9],
    [2.8357538e-7, 2.84856995e-6, 1.447920408e-5, 5.368328059e-5, 2.647892e-8, 4.8387492e-7, 3.38018176e-6, 2.49467e-9, 8.294302e-8, 2.3652e-10],
    [7.938705e-8, 8.3170847e-7, 4.41154886e-6, 1.705923313e-5, 6.787e-9, 1.3033842e-7, 9.5632476e-7, 5.854e-10, 2.060784e-8, 5.082e-11],
    [2.25367e-8, 2.450395e-7, 1.3500387e-6, 5.42174374e-6, 1.77654e-9, 3.563769e-8, 2.7313129e-7, 1.4127e-10, 5.22823e-9, 1.131e-11],
    [6.47434e-9, 7.276496e-8, 4.1481779e-7, 1.72394082e-6, 4.7342e-10, 9.87174e-9, 7.866968e-8, 3.492e-11, 1.35066e-9, 2.59e-12],
    [1.87912e-9, 2.175802e-8, 1.2793307e-7, 5.4853275e-7, 1.2812e-10, 2.76586e-9, 2.283195e-8, 8.81e-12, 3.5451e-10, 6.1e-13],
    [5.5029e-10, 6.54616e-9, 3.95907e-8, 1.7467795e-7, 3.514e-11, 7.8279e-10, 6.67205e-9, 2.26e-12, 9.436e-11, 1.5e-13],
    [1.6242e-10, 1.98033e-9, 1.229055e-8, 5.56755e-8, 9.75e-12, 2.2354e-10, 1.96191e-9, 5.9e-13, 2.543e-11, 4.0e-14],
    [4.827e-11, 6.0204e-10, 3.82658e-9, 1.776234e-8, 2.74e-12, 6.435e-11, 5.8018e-10, 1.6e-13, 6.93e-12, 1.0e-14],
    [1.444e-11, 1.8385e-10, 1.19459e-9, 5.67224e-9, 7.7e-13, 1.866e-11, 1.7246e-10, 4.0e-14, 1.91e-12, f64::NAN],
    [4.34e-12, 5.637e-11, 3.7386e-10, 1.81313e-9, 2.2e-13, 5.45e-12, 5.151e-11, 1.0e-14, 5.3e-13, f64::NAN],
    [1.31e-12, 1.735e-11, 1.1727e-10, 5.8012e-10, 6.0e-14, 1.6e-12, 1.545e-11, f64::NAN, 1.5e-13, f64::NAN],
    [4.0e-13, 5.36e-12, 3.687e-11, 1.8579e-10, 2.0e-14, 4.7e-13, 4.65e-12, f64::NAN, 4.0e-14, f64::NAN],
    [1.2e-13, 1.66e-12, 1.161e-11, 5.955e-11, 1.0e-14, 1.4e-13, 1.41e-12, f64::NAN, 1.0e-14, f64::NAN],
    [4.0e-14, 5.2e-13, 3.66e-12, 1.911e-11, f64::NAN, 4.0e-14, 4.3e-13, f64::NAN, f64::NAN, f64::NAN],
    [1.0e-14, 1.6e-13, 1.16e-12, 6.14e-12, f64::NAN, 1.0e-14, 1.3e-13, f64::NAN, f64::NAN, f64::NAN],
    [f64::NAN, 5.0e-14, 3.7e-13, 1.97e-12, f64::NAN, f64::NAN, 4.0e-14, f64::NAN, f64::NAN, f64::NAN],
    [f64::NAN, 2.0e-14, 1.2e-13, 6.3e-13, f64::NAN, f64::NAN, 1.0e-14, f64::NAN, f64::NAN, f64::NAN],
    [f64::NAN, f64::NAN, 4.0e-14, 2.0e-13, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN],
    [f64::NAN, f64::NAN, 1.0e-14, 7.0e-14, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN],
    [f64::NAN, f64::NAN, f64::NAN, 2.0e-14, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN],
    [f64::NAN, f64::NAN, f64::NAN, 1.0e-14, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN],
];

/* 
    This function computes the Nielsen generalised polylogarithm nl(n,m,x) for n=1,2,3,4 and m=1,2,3,4 with n+m <= 5
*/

pub fn nl(n: i32, m: i32, x: f64) -> Complex64 {
    if n < 1 || n > 4 || m < 1 || m > 4 || n + m > 5 {
        panic!("ILLEGAL VALUES N,M");
    }

    if x == 1.0 {
        return Complex64::from(S1[(n - 1) as usize][(m - 1) as usize]);
    }

    let mut v: [Complex64; 6] = [Complex64::new(f64::NAN, f64::NAN); 6];
    let mut u: [Complex64; 5] = [Complex64::new(f64::NAN, f64::NAN); 5];

    if x > 2.0 || x < -1.0 {
        let x1: f64 = 1.0 / x;
        let h: f64 = C1 * x1 + C2;
        let alfa: f64 = h + h;
        v[0] = Complex64::from(1.0);
        v[1] = Complex64::new(-x, Z0).ln() + I * 0.0; // log(-X + I*Z0)
        for l in 2..=(n + m) as usize {
            v[l] = v[1] * v[l - 1] / (l as f64);
        }
        let mut sk: Complex64 = Complex64::from(0.0);
        for k in 0..=(m - 1) as usize {
            let m1: usize = (m as usize) - k;
            let r: f64 = x1.powi(m1 as i32) / (FCT[m1] * FCT[(n - 1) as usize]);
            let mut sj: Complex64 = Complex64::from(0.0);
            for j in 0..=k {
                let n1: usize = (n as usize) + k - j;
                let l: usize = INDEX[10 * n1 + m1 - 10 - 1];
                let mut b1: f64 = 0.0;
                let mut b2: f64 = 0.0;
                let mut b0: f64 = 0.0;
                for it in (0..=NC[l - 1]).rev() {
                    b0 = A[it][l - 1] + alfa * b1 - b2;
                    b2 = b1;
                    b1 = b0;
                }
                let q: f64 = (FCT[n1 - 1] / FCT[k - j]) * (b0 - h * b2) * r / (m1 as f64).powi(n1 as i32);
                sj += v[j] * q;
            }
            sk += sj * SGN[k];
        }
        let mut sj_final: Complex64 = Complex64::from(0.0);
        for j in 0..=(n - 1) as usize {
            sj_final += v[j] * C[(n as usize) - j - 1][(m - 1) as usize];
        }
        return sk * SGN[n as usize] + (sj_final + v[(n + m) as usize]) * SGN[m as usize];
    }

    if x > HF {
        let x1: f64 = 1.0 - x;
        let h: f64 = C1 * x1 + C2;
        let alfa: f64 = h + h;
        v[0] = Complex64::from(1.0);
        u[0] = Complex64::from(1.0);
        v[1] = Complex64::new(x1, Z0).ln();
        u[1] = Complex64::from(x.ln());
        for l in 2..=(m as usize) {
            v[l] = v[1] * v[l - 1] / (l as f64);
        }
        for l in 2..=(n as usize) {
            u[l] = u[1] * u[l - 1] / (l as f64);
        }
        let mut sk: Complex64 = Complex64::from(0.0);
        for k in 0..=(n - 1) as usize {
            let m1: usize = (n as usize) - k;
            let r: f64 = x1.powi(m1 as i32) / FCT[m1];
            let mut sj: Complex64 = Complex64::from(0.0);
            for j in 0..=(m - 1) as usize {
                let n1: usize = (m as usize) - j;
                let l: usize = INDEX[10 * n1 + m1 - 10 - 1];
                let mut b1: f64 = 0.0;
                let mut b2: f64 = 0.0;
                let mut b0: f64 = 0.0;
                for it in (0..=NC[l - 1]).rev() {
                    b0 = A[it][l - 1] + alfa * b1 - b2;
                    b2 = b1;
                    b1 = b0;
                }
                let q: f64 = SGN[j] * (b0 - h * b2) * r / (m1 as f64).powi(n1 as i32);
                sj += v[j] * q;
            }
            sk += u[k] * (S1[m1 - 1][(m - 1) as usize] - sj);
        }
        return sk + u[n as usize] * v[m as usize] * SGN[m as usize];
    }

    // Default case (x <= HF)
    let l: usize = INDEX[(10 * n + m - 10 - 1) as usize];
    let h: f64 = C1 * x + C2;
    let alfa: f64 = h + h;
    let mut b1: f64 = 0.0;
    let mut b2: f64 = 0.0;
    let mut b0: f64 = 0.0;
    for it in (0..=NC[l - 1]).rev() {
        b0 = A[it][l - 1] + alfa * b1 - b2;
        b2 = b1;
        b1 = b0;
    }
    Complex64::from((b0 - h * b2) * x.powi(m as i32) / (FCT[m as usize] * (m as f64).powi(n as i32)))
}

/*
    These function compute the dilogarithm Li2(x) and trilogarithm Li3(x) using the nl function defined above.
*/

pub fn Li2(x: f64) -> f64 {
    nl(1, 1, x).re
}
// pub fn Li2_custom(x: f64) -> f64 {
//     const PI2_6: f64 = std::f64::consts::PI * std::f64::consts::PI / 6.0;

//     if x == 0.0 { return 0.0; }
//     if x == 1.0 { return PI2_6; }
//     if x == -1.0 { return -PI2_6 / 2.0; }

//     // Map to z in (-1, 0.5] using functional identities, accumulating offset
//     let (z, offset, sign) = if x > 0.5 && x < 1.0 {
//         (1.0 - x, PI2_6 - x.ln() * (1.0 - x).ln(), -1.0)
//     } else if x >= 1.0 {
//         (1.0 / x, -PI2_6 - 0.5 * x.ln() * x.ln(), -1.0)
//     } else if x < -1.0 {
//         (1.0 / x, -PI2_6 - 0.5 * (-x).ln() * (-x).ln(), -1.0)
//     } else {
//         (x, 0.0, 1.0)
//     };

//     // Taylor series: Li₂(z) = Σ zⁿ/n², converges fast for |z| ≤ 0.5
//     let mut sum = 0.0;
//     let mut zn = z;
//     for n in 1u64.. {
//         let term = zn / (n * n) as f64;
//         sum += term;
//         if term.abs() < 1e-17 * sum.abs() { break; }
//         zn *= z;
//     }

//     offset + sign * sum
// }

pub fn Li3(x: f64) -> f64 {
    nl(2, 1, x).re
}

/*
    These functions compute the harmonic polylogarithms HPLs upto weight 3 using the nl function defined above.
*/

pub fn h0(x: f64) -> f64 {
    x.ln()
}

pub fn h1(x: f64) -> f64 {
    -(1.0 - x).ln()
}

pub fn hm1(x: f64) -> f64 {
    (1.0 + x).ln()
}

pub fn h00(x: f64) -> f64 {
    x.ln().powi(2) * 0.5
}

pub fn h01(x: f64) -> f64 {
    nl(1, 1, x).re
}

pub fn h10(x: f64) -> f64 {
    - x.ln()*(1.0 - x).ln() - nl(1, 1, x).re
}

pub fn h11(x: f64) -> f64 {
    (1.0 - x).ln().powi(2) * 0.5
}

pub fn hm10(x: f64) -> f64 {
    x.ln()*(1.0 + x).ln() - nl(1, 1, -x).re
}

pub fn hm1m10(x: f64) -> f64 {
    let result = (Complex64::new(1.0 + x, 0.0).ln() * (Complex64::new(PI.powi(2), 0.0) 
    + (-Complex64::new(-x, 0.0).ln() 
    + Complex64::new(x, 0.0).ln()) * 3.0 * Complex64::new(1.0 + x, 0.0).ln()) 
    - nl(2, 1, 1.0 + x) * 6.0 + 6.0 * ZETA3) / 6.0;
    result.re
}

pub fn hm100(x: f64) -> f64 {
    x.ln().powi(2) * (1.0 + x).ln() / 2.0 + x.ln() * nl(1, 1, -x).re - nl(2, 1, -x).re
}

pub fn hm101(x: f64) -> f64 {
    (PI.powi(2) * 2.0_f64.ln() / 6.0) 
        - (2.0_f64.ln().powi(3) / 3.0) 
        - ((PI.powi(2) + 6.0 * 2.0_f64.ln().powi(2)) / 12.0) 
        + ((1.0 - x).ln().powi(2) * (((1.0 - x) / 8.0).ln() - 3.0 * x.ln()) / 6.0) 
        - ((1.0 + x).ln() * (PI.powi(2) - 6.0 * 2.0_f64.ln().powi(2) + 64.0_f64.ln() * (1.0 + x).ln()) / 12.0) 
        - ((1.0 - x).ln() * nl(1, 1, -x).re) 
        + nl(2, 1, (1.0 - x) / 2.0).re 
        - nl(2, 1, 1.0 - x).re 
        + nl(2, 1, -x).re 
        - nl(2, 1, 2.0 * x / (-1.0 + x)).re 
        + nl(2, 1, x / (1.0 + x)).re 
        - nl(2, 1, 2.0 * x / (1.0 + x)).re 
        + nl(2, 1, (1.0 + x) / 2.0).re 
        - (3.0 * ZETA3 / 4.0)
}

pub fn h0m10(x: f64) -> f64 {
    -x.ln() * nl(1, 1, -x).re + 2.0 * nl(2, 1, -x).re
}

pub fn h000(x: f64) -> f64 {
    x.ln().powi(3) / 6.0
}

pub fn h001(x: f64) -> f64 {
    nl(2, 1, x).re
}

pub fn h010(x: f64) -> f64 {
    x.ln() * nl(1, 1, x).re - 2.0 * nl(2, 1, x).re
}

pub fn h011(x: f64) -> f64 {
    x.ln() * (1.0 - x).ln().powi(2) / 2.0 + (1.0 - x).ln() * nl(1, 1, 1.0 - x).re - nl(2, 1, 1.0 - x).re + ZETA3
}

pub fn h100(x: f64) -> f64 {
    -x.ln().powi(2) * (1.0 - x).ln() / 2.0 - x.ln() * nl(1, 1, x).re + nl(2, 1, x).re
}

pub fn h101(x: f64) -> f64 {
    -x.ln() * (1.0 - x).ln().powi(2) - 2.0 * (1.0 - x).ln() * nl(1, 1, 1.0 - x).re - (1.0 - x).ln() * nl(1, 1, x).re + 2.0 * nl(2, 1, 1.0 - x).re - 2.0 * ZETA3
}

pub fn h110(x: f64) -> f64 {
    x.ln() * (1.0 - x).ln().powi(2) + (1.0 - x).ln() * nl(1, 1, 1.0 - x).re + (1.0 - x).ln() * nl(1, 1, x).re - nl(2, 1, 1.0 - x).re + ZETA3
}

pub fn h111(x: f64) -> f64 {
    -(1.0 - x).ln().powi(3) / 6.0
}
