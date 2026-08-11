use crate::dis::internal::*;
use crate::dis::dis_ext::adani_grids::{
    c2g_nf3_var0, c2g_nf3_var1, c2g_nf3_var_1,
    c2g_nf4_var0, c2g_nf4_var1, c2g_nf4_var_1,
    c2g_nf5_var0, c2g_nf5_var1, c2g_nf5_var_1
};

pub fn r_00(x: f64, Q2: f64, pid: f64, nf: f64, var: i8) -> f64 {

    let m2 = get_quark_mass(pid as i8).powi(2);

    let xi = Q2 / m2;
    let eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0;

    let grid = match (nf, var) {
        (3.0, -1) => c2g_nf3_var_1::c2g_nf3_var_1_spline(),
        (3.0, 0) => c2g_nf3_var0::c2g_nf3_var0_spline(),
        (3.0, 1) => c2g_nf3_var1::c2g_nf3_var1_spline(),
        (4.0, -1) => c2g_nf4_var_1::c2g_nf4_var_1_spline(),
        (4.0, 0) => c2g_nf4_var0::c2g_nf4_var0_spline(),
        (4.0, 1) => c2g_nf4_var1::c2g_nf4_var1_spline(),
        (5.0, -1) => c2g_nf5_var_1::c2g_nf5_var_1_spline(),
        (5.0, 0) => c2g_nf5_var0::c2g_nf5_var0_spline(),
        (5.0, 1) => c2g_nf5_var1::c2g_nf5_var1_spline(),
        _ => panic!("Unsupported number of flavors or variation: nf={}, var={}", nf, var),
    };

    let res: f64;
    if below_threshold(x, Q2, m2) {
        res = 0.0;
    } else {
        res = grid.ev(xi, eta);
    }

    res
}