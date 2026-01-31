#![allow(unused_variables)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(non_camel_case_types)]

#[macro_use]
pub(crate) mod internal {
    // pub use std::collections::HashMap;

    pub use crate::core::libfunc::{pow, ln, ArcTan, InvTanInt};
    pub use crate::core::nielsen::{Li2, Li3};
    pub use crate::core::constants::{NQCD, rln2, pi, zeta3, CF};
    pub const lmur: f64 = 0.5;
    pub const lmuf: f64 = 0.5;
    pub const lmua: f64 = 1.0;

    pub fn mysqrt(x: f64) -> f64 {
        x.sqrt()
    }

    // pub type basic_fn = fn(f64, f64, f64) -> f64;
    // pub type order_list = HashMap<&'static str, basic_fn>;
    // pub type sv_map = HashMap<&'static str, order_list>;
    // #[macro_export]
    // macro_rules! generate_sv_map {
    //     ( $( $scale:expr => [ $( ($cat:expr, $func:ident) ),* ] ),* $(,)? ) => {{
    //         let mut master_map = $crate::sidis::internal::sv_map::new();
    //         $(
    //             let mut inner_list = $crate::sidis::internal::order_list::new();
    //             $(
    //                 inner_list.insert($cat, $func as $crate::sidis::internal::basic_fn);
    //             )*
    //             master_map.insert($scale, inner_list);
    //         )*
    //         master_map
    //     }};
    // }
    pub type SIDISFunc = fn(f64, f64, f64) -> f64;

    #[derive(Default)]
    pub struct SIDISCoeffs {
        pub rr: Option<SIDISFunc>, pub rs: Option<SIDISFunc>, pub rl: Option<SIDISFunc>,
        pub sr: Option<SIDISFunc>, pub ss: Option<SIDISFunc>, pub sl: Option<SIDISFunc>,
        pub lr: Option<SIDISFunc>, pub ls: Option<SIDISFunc>, pub ll: Option<SIDISFunc>,
    }

    // macro_rules! mkcoeff {
    //     (@parse _) => { None };
    //     (@parse $id:ident) => { Some($id) };

    //     (@gen_wrappers $s:expr, [
    //         $RG_RG:tt, $RG_D0:tt, $RG_D1:tt, $RG_D2:tt, $RG_D3:tt, $RG_DL:tt,
    //         $D0_RG:tt, $D0_D0:tt, $D0_D1:tt, $D0_D2:tt, $D0_D3:tt, $D0_DL:tt,
    //         $D1_RG:tt, $D1_D0:tt, $D1_D1:tt, $D1_D2:tt, $D1_D3:tt, $D1_DL:tt,
    //         $D2_RG:tt, $D2_D0:tt, $D2_D1:tt, $D2_D2:tt, $D2_D3:tt, $D2_DL:tt,
    //         $D3_RG:tt, $D3_D0:tt, $D3_D1:tt, $D3_D2:tt, $D3_D3:tt, $D3_DL:tt,
    //         $DL_RG:tt, $DL_D0:tt, $DL_D1:tt, $DL_D2:tt, $DL_D3:tt, $DL_DL:tt
    //     ]) => {
    //         paste::paste! {
    //             fn [<rs_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let omz = 1.0 - z;
    //                 let lz = omz.ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $RG_D0) { res += f(x, z, nf) / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $RG_D1) { res += f(x, z, nf) * lz / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $RG_D2) { res += f(x, z, nf) * lz.powi(2) / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $RG_D3) { res += f(x, z, nf) * lz.powi(3) / omz; }
    //                 res
    //             }

    //             fn [<rl_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let lz = (1.0 - z).ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $RG_DL) { res += f(x, z, nf); }
    //                 if let Some(f) = mkcoeff!(@parse $RG_D0) { res += f(x, z, nf) * lz; }
    //                 if let Some(f) = mkcoeff!(@parse $RG_D1) { res += f(x, z, nf) * lz.powi(2) / 2.0; }
    //                 if let Some(f) = mkcoeff!(@parse $RG_D2) { res += f(x, z, nf) * lz.powi(3) / 3.0; }
    //                 if let Some(f) = mkcoeff!(@parse $RG_D3) { res += f(x, z, nf) * lz.powi(4) / 4.0; }
    //                 res
    //             }

    //             fn [<sr_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let omx = 1.0 - x;
    //                 let lx = omx.ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $D0_RG) { res += f(x, z, nf) / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_RG) { res += f(x, z, nf) * lx / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_RG) { res += f(x, z, nf) * lx.powi(2) / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_RG) { res += f(x, z, nf) * lx.powi(3) / omx; }
    //                 res
    //             }

    //             fn [<ss_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let omx = 1.0 - x;
    //                 let omz = 1.0 - z;
    //                 let lx = omx.ln();
    //                 let lz = omz.ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lz / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lz.powi(2) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lz.powi(3) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx * lz / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx * lz.powi(2) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx * lz.powi(3) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(2) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(2) * lz / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(3) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(3) * lz / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / (omx * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / (omx * omz); }
    //                 res
    //             }

    //             fn [<sl_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let omx = 1.0 - x;
    //                 let lx = omx.ln();
    //                 let lz = (1.0 - z).ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $D0_DL) { res += f(x, z, nf) / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) * lz / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lz.powi(2) / (2.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lz.powi(3) / (3.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lz.powi(4) / (4.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_DL) { res += f(x, z, nf) * lx / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx * lz / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx * lz.powi(2) / (2.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx * lz.powi(3) / (3.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx * lz.powi(4) / (4.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_DL) { res += f(x, z, nf) * lx.powi(2) / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(2) * lz / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / (2.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / (3.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(4) / (4.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_DL) { res += f(x, z, nf) * lx.powi(3) / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(3) * lz / omx; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / (2.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / (3.0 * omx); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(4) / (4.0 * omx); }
    //                 res
    //             }

    //             fn [<lr_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let lx = (1.0 - x).ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $DL_RG) { res += f(x, z, nf); }
    //                 if let Some(f) = mkcoeff!(@parse $D0_RG) { res += f(x, z, nf) * lx; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_RG) { res += f(x, z, nf) * lx.powi(2) / 2.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_RG) { res += f(x, z, nf) * lx.powi(3) / 3.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_RG) { res += f(x, z, nf) * lx.powi(4) / 4.0; }
    //                 res
    //             }

    //             fn [<ls_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let omz = 1.0 - z;
    //                 let lx = (1.0 - x).ln();
    //                 let lz = omz.ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $DL_D0) { res += f(x, z, nf) / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $DL_D1) { res += f(x, z, nf) * lz / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $DL_D2) { res += f(x, z, nf) * lz.powi(2) / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $DL_D3) { res += f(x, z, nf) * lz.powi(3) / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) * lx / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lx * lz / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lx * lz.powi(2) / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lx * lz.powi(3) / omz; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx.powi(2) / (2.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx.powi(2) * lz / (2.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / (2.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / (2.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(3) / (3.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(3) * lz / (3.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / (3.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / (3.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(4) / (4.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(4) * lz / (4.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(4) * lz.powi(2) / (4.0 * omz); }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(4) * lz.powi(3) / (4.0 * omz); }
    //                 res
    //             }

    //             fn [<ll_wrapper_ $s>](x: f64, z: f64, nf: f64) -> f64 {
    //                 let lx = (1.0 - x).ln();
    //                 let lz = (1.0 - z).ln();
    //                 let mut res = 0.0;
    //                 if let Some(f) = mkcoeff!(@parse $DL_DL) { res += f(x, z, nf); }
    //                 if let Some(f) = mkcoeff!(@parse $DL_D0) { res += f(x, z, nf) * lz; }
    //                 if let Some(f) = mkcoeff!(@parse $DL_D1) { res += f(x, z, nf) * lz.powi(2) / 2.0; }
    //                 if let Some(f) = mkcoeff!(@parse $DL_D2) { res += f(x, z, nf) * lz.powi(3) / 3.0; }
    //                 if let Some(f) = mkcoeff!(@parse $DL_D3) { res += f(x, z, nf) * lz.powi(4) / 4.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_DL) { res += f(x, z, nf) * lx; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) * lx * lz; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lx * lz.powi(2) / 2.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lx * lz.powi(3) / 3.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lx * lz.powi(4) / 4.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_DL) { res += f(x, z, nf) * lx.powi(2) / 2.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx.powi(2) * lz / 2.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / 4.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / 6.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(4) / 8.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_DL) { res += f(x, z, nf) * lx.powi(3) / 3.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(3) * lz / 3.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / 6.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / 9.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(4) / 12.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_DL) { res += f(x, z, nf) * lx.powi(4) / 4.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(4) * lz / 4.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(4) * lz.powi(2) / 8.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(4) * lz.powi(3) / 12.0; }
    //                 if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(4) * lz.powi(4) / 16.0; }
    //                 res
    //             }

    //             fn [<cf_get_ $s>]() -> SIDISCoeffs {
    //                 SIDISCoeffs {
    //                     rr: mkcoeff!(@parse $RG_RG),
                        
    //                     rs: if mkcoeff!(@parse $RG_D0).is_some() || mkcoeff!(@parse $RG_D1).is_some() || mkcoeff!(@parse $RG_D2).is_some() || mkcoeff!(@parse $RG_D3).is_some() { Some([<rs_wrapper_ $s>]) } else { None },

    //                     rl: if mkcoeff!(@parse $RG_DL).is_some() || mkcoeff!(@parse $RG_D0).is_some() || mkcoeff!(@parse $RG_D1).is_some() || mkcoeff!(@parse $RG_D2).is_some() || mkcoeff!(@parse $RG_D3).is_some() { Some([<rl_wrapper_ $s>]) } else { None },

    //                     sr: if mkcoeff!(@parse $D0_RG).is_some() || mkcoeff!(@parse $D1_RG).is_some() || mkcoeff!(@parse $D2_RG).is_some() || mkcoeff!(@parse $D3_RG).is_some() { Some([<sr_wrapper_ $s>]) } else { None },

    //                     ss: if mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
    //                            mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
    //                            mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
    //                            mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some()
    //                     { Some([<ss_wrapper_ $s>]) } else { None },

    //                     sl: if mkcoeff!(@parse $D0_DL).is_some() || mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
    //                            mkcoeff!(@parse $D1_DL).is_some() || mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
    //                            mkcoeff!(@parse $D2_DL).is_some() || mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
    //                            mkcoeff!(@parse $D3_DL).is_some() || mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some()
    //                     { Some([<sl_wrapper_ $s>]) } else { None },

    //                     lr: if mkcoeff!(@parse $DL_RG).is_some() || mkcoeff!(@parse $D0_RG).is_some() || mkcoeff!(@parse $D1_RG).is_some() || mkcoeff!(@parse $D2_RG).is_some() || mkcoeff!(@parse $D3_RG).is_some() { Some([<lr_wrapper_ $s>]) } else { None },

    //                     ls: if mkcoeff!(@parse $DL_D0).is_some() || mkcoeff!(@parse $DL_D1).is_some() || mkcoeff!(@parse $DL_D2).is_some() || mkcoeff!(@parse $DL_D3).is_some() ||
    //                            mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
    //                            mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
    //                            mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
    //                            mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some()
    //                     { Some([<ls_wrapper_ $s>]) } else { None },

    //                     ll: if mkcoeff!(@parse $DL_DL).is_some() || mkcoeff!(@parse $DL_D0).is_some() || mkcoeff!(@parse $DL_D1).is_some() || mkcoeff!(@parse $DL_D2).is_some() || mkcoeff!(@parse $DL_D3).is_some() ||
    //                            mkcoeff!(@parse $D0_DL).is_some() || mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
    //                            mkcoeff!(@parse $D1_DL).is_some() || mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
    //                            mkcoeff!(@parse $D2_DL).is_some() || mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
    //                            mkcoeff!(@parse $D3_DL).is_some() || mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some()
    //                     { Some([<ll_wrapper_ $s>]) } else { None },
    //                 }
    //             }
    //         }
    //     };

    //     ( $( ($scale:expr, $list:tt) ),* ) => {
    //         $( mkcoeff!(@gen_wrappers $scale, $list); )*

    //         pub fn scales() -> &'static [&'static str] {
    //             &[ $( $scale ),* ]
    //         }

    //         pub fn cf(scale: &str) -> SIDISCoeffs {
    //             paste::paste! {
    //                 match scale {
    //                     $( $scale => [<cf_get_ $scale>](), )*
    //                     _ => panic!("Scale {} not supported", scale),
    //                 }
    //             }
    //         }
    //     };
    // }

    // pub(crate) use mkcoeff;
    macro_rules! mkcoeff {
    // Helper to turn _ into None and identifiers into Some
    (@parse _) => { None::<SIDISFunc> };
    (@parse $id:ident) => { Some($id as SIDISFunc) };

    ( $( ($scale:expr, [
        $RG_RG:tt, $RG_D0:tt, $RG_D1:tt, $RG_D2:tt, $RG_D3:tt, $RG_DL:tt,
        $D0_RG:tt, $D0_D0:tt, $D0_D1:tt, $D0_D2:tt, $D0_D3:tt, $D0_DL:tt,
        $D1_RG:tt, $D1_D0:tt, $D1_D1:tt, $D1_D2:tt, $D1_D3:tt, $D1_DL:tt,
        $D2_RG:tt, $D2_D0:tt, $D2_D1:tt, $D2_D2:tt, $D2_D3:tt, $D2_DL:tt,
        $D3_RG:tt, $D3_D0:tt, $D3_D1:tt, $D3_D2:tt, $D3_D3:tt, $D3_DL:tt,
        $DL_RG:tt, $DL_D0:tt, $DL_D1:tt, $DL_D2:tt, $DL_D3:tt, $DL_DL:tt
    ]) ),* $(,)? ) => {

        pub fn scales() -> &'static [&'static str] {
            &[ $( $scale ),* ]
        }

        pub fn cf(scale: &str) -> SIDISCoeffs {
            match scale {
                $(
                    $scale => {
                        // --- Local Wrapper Definitions ---
                        // These exist ONLY within this match arm scope.

                        fn rs_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let omz = 1.0 - z;
                            let lz = omz.ln();
                            let mut res = 0.0;
                            if let Some(f) = mkcoeff!(@parse $RG_D0) { res += f(x, z, nf) / omz; }
                            if let Some(f) = mkcoeff!(@parse $RG_D1) { res += f(x, z, nf) * lz / omz; }
                            if let Some(f) = mkcoeff!(@parse $RG_D2) { res += f(x, z, nf) * lz.powi(2) / omz; }
                            if let Some(f) = mkcoeff!(@parse $RG_D3) { res += f(x, z, nf) * lz.powi(3) / omz; }
                            res
                        }

                        fn rl_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let lz = (1.0 - z).ln();
                            let mut res = 0.0;
                            if let Some(f) = mkcoeff!(@parse $RG_DL) { res += f(x, z, nf); }
                            if let Some(f) = mkcoeff!(@parse $RG_D0) { res += f(x, z, nf) * lz; }
                            if let Some(f) = mkcoeff!(@parse $RG_D1) { res += f(x, z, nf) * lz.powi(2) / 2.0; }
                            if let Some(f) = mkcoeff!(@parse $RG_D2) { res += f(x, z, nf) * lz.powi(3) / 3.0; }
                            if let Some(f) = mkcoeff!(@parse $RG_D3) { res += f(x, z, nf) * lz.powi(4) / 4.0; }
                            res
                        }

                        fn sr_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let omx = 1.0 - x;
                            let lx = omx.ln();
                            let mut res = 0.0;
                            if let Some(f) = mkcoeff!(@parse $D0_RG) { res += f(x, z, nf) / omx; }
                            if let Some(f) = mkcoeff!(@parse $D1_RG) { res += f(x, z, nf) * lx / omx; }
                            if let Some(f) = mkcoeff!(@parse $D2_RG) { res += f(x, z, nf) * lx.powi(2) / omx; }
                            if let Some(f) = mkcoeff!(@parse $D3_RG) { res += f(x, z, nf) * lx.powi(3) / omx; }
                            res
                        }

                        fn ss_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let omx = 1.0 - x; let omz = 1.0 - z;
                            let lx = omx.ln(); let lz = omz.ln();
                            let mut res = 0.0;
                            let den = omx * omz;
                            if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) / den; }
                            if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lz / den; }
                            if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lz.powi(2) / den; }
                            if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lz.powi(3) / den; }
                            if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx / den; }
                            if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx * lz / den; }
                            if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx * lz.powi(2) / den; }
                            if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx * lz.powi(3) / den; }
                            if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(2) / den; }
                            if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(2) * lz / den; }
                            if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / den; }
                            if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / den; }
                            if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(3) / den; }
                            if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(3) * lz / den; }
                            if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / den; }
                            if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / den; }
                            res
                        }

                        fn sl_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let omx = 1.0 - x; let lx = omx.ln(); let lz = (1.0 - z).ln();
                            let mut res = 0.0;
                            // Logic for mapping all Di_Dk cross terms to sl endpoint
                            if let Some(f) = mkcoeff!(@parse $D0_DL) { res += f(x, z, nf) / omx; }
                            if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) * lz / omx; }
                            if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lz.powi(2) / (2.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lz.powi(3) / (3.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lz.powi(4) / (4.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D1_DL) { res += f(x, z, nf) * lx / omx; }
                            if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx * lz / omx; }
                            if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx * lz.powi(2) / (2.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx * lz.powi(3) / (3.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx * lz.powi(4) / (4.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D2_DL) { res += f(x, z, nf) * lx.powi(2) / omx; }
                            if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(2) * lz / omx; }
                            if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / (2.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / (3.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(4) / (4.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D3_DL) { res += f(x, z, nf) * lx.powi(3) / omx; }
                            if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(3) * lz / omx; }
                            if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / (2.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / (3.0 * omx); }
                            if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(4) / (4.0 * omx); }
                            res
                        }

                        fn lr_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let lx = (1.0 - x).ln();
                            let mut res = 0.0;
                            if let Some(f) = mkcoeff!(@parse $DL_RG) { res += f(x, z, nf); }
                            if let Some(f) = mkcoeff!(@parse $D0_RG) { res += f(x, z, nf) * lx; }
                            if let Some(f) = mkcoeff!(@parse $D1_RG) { res += f(x, z, nf) * lx.powi(2) / 2.0; }
                            if let Some(f) = mkcoeff!(@parse $D2_RG) { res += f(x, z, nf) * lx.powi(3) / 3.0; }
                            if let Some(f) = mkcoeff!(@parse $D3_RG) { res += f(x, z, nf) * lx.powi(4) / 4.0; }
                            res
                        }

                        fn ls_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let omz = 1.0 - z; let lx = (1.0 - x).ln(); let lz = omz.ln();
                            let mut res = 0.0;
                            if let Some(f) = mkcoeff!(@parse $DL_D0) { res += f(x, z, nf) / omz; }
                            if let Some(f) = mkcoeff!(@parse $DL_D1) { res += f(x, z, nf) * lz / omz; }
                            if let Some(f) = mkcoeff!(@parse $DL_D2) { res += f(x, z, nf) * lz.powi(2) / omz; }
                            if let Some(f) = mkcoeff!(@parse $DL_D3) { res += f(x, z, nf) * lz.powi(3) / omz; }
                            if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) * lx / omz; }
                            if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lx * lz / omz; }
                            if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lx * lz.powi(2) / omz; }
                            if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lx * lz.powi(3) / omz; }
                            if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx.powi(2) / (2.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx.powi(2) * lz / (2.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / (2.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / (2.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(3) / (3.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(3) * lz / (3.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / (3.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / (3.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(4) / (4.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(4) * lz / (4.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(4) * lz.powi(2) / (4.0 * omz); }
                            if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(4) * lz.powi(3) / (4.0 * omz); }
                            res
                        }

                        fn ll_wrap(x: f64, z: f64, nf: f64) -> f64 {
                            let lx = (1.0 - x).ln(); let lz = (1.0 - z).ln();
                            let mut res = 0.0;
                            if let Some(f) = mkcoeff!(@parse $DL_DL) { res += f(x, z, nf); }
                            if let Some(f) = mkcoeff!(@parse $DL_D0) { res += f(x, z, nf) * lz; }
                            if let Some(f) = mkcoeff!(@parse $DL_D1) { res += f(x, z, nf) * lz.powi(2) / 2.0; }
                            if let Some(f) = mkcoeff!(@parse $DL_D2) { res += f(x, z, nf) * lz.powi(3) / 3.0; }
                            if let Some(f) = mkcoeff!(@parse $DL_D3) { res += f(x, z, nf) * lz.powi(4) / 4.0; }
                            if let Some(f) = mkcoeff!(@parse $D0_DL) { res += f(x, z, nf) * lx; }
                            if let Some(f) = mkcoeff!(@parse $D0_D0) { res += f(x, z, nf) * lx * lz; }
                            if let Some(f) = mkcoeff!(@parse $D0_D1) { res += f(x, z, nf) * lx * lz.powi(2) / 2.0; }
                            if let Some(f) = mkcoeff!(@parse $D0_D2) { res += f(x, z, nf) * lx * lz.powi(3) / 3.0; }
                            if let Some(f) = mkcoeff!(@parse $D0_D3) { res += f(x, z, nf) * lx * lz.powi(4) / 4.0; }
                            if let Some(f) = mkcoeff!(@parse $D1_DL) { res += f(x, z, nf) * lx.powi(2) / 2.0; }
                            if let Some(f) = mkcoeff!(@parse $D1_D0) { res += f(x, z, nf) * lx.powi(2) * lz / 2.0; }
                            if let Some(f) = mkcoeff!(@parse $D1_D1) { res += f(x, z, nf) * lx.powi(2) * lz.powi(2) / 4.0; }
                            if let Some(f) = mkcoeff!(@parse $D1_D2) { res += f(x, z, nf) * lx.powi(2) * lz.powi(3) / 6.0; }
                            if let Some(f) = mkcoeff!(@parse $D1_D3) { res += f(x, z, nf) * lx.powi(2) * lz.powi(4) / 8.0; }
                            if let Some(f) = mkcoeff!(@parse $D2_DL) { res += f(x, z, nf) * lx.powi(3) / 3.0; }
                            if let Some(f) = mkcoeff!(@parse $D2_D0) { res += f(x, z, nf) * lx.powi(3) * lz / 3.0; }
                            if let Some(f) = mkcoeff!(@parse $D2_D1) { res += f(x, z, nf) * lx.powi(3) * lz.powi(2) / 6.0; }
                            if let Some(f) = mkcoeff!(@parse $D2_D2) { res += f(x, z, nf) * lx.powi(3) * lz.powi(3) / 9.0; }
                            if let Some(f) = mkcoeff!(@parse $D2_D3) { res += f(x, z, nf) * lx.powi(3) * lz.powi(4) / 12.0; }
                            if let Some(f) = mkcoeff!(@parse $D3_DL) { res += f(x, z, nf) * lx.powi(4) / 4.0; }
                            if let Some(f) = mkcoeff!(@parse $D3_D0) { res += f(x, z, nf) * lx.powi(4) * lz / 4.0; }
                            if let Some(f) = mkcoeff!(@parse $D3_D1) { res += f(x, z, nf) * lx.powi(4) * lz.powi(2) / 8.0; }
                            if let Some(f) = mkcoeff!(@parse $D3_D2) { res += f(x, z, nf) * lx.powi(4) * lz.powi(3) / 12.0; }
                            if let Some(f) = mkcoeff!(@parse $D3_D3) { res += f(x, z, nf) * lx.powi(4) * lz.powi(4) / 16.0; }
                            res
                        }

                        // --- Struct Return ---
                        SIDISCoeffs {
                            rr: mkcoeff!(@parse $RG_RG),
                            rs: if mkcoeff!(@parse $RG_D0).is_some() || mkcoeff!(@parse $RG_D1).is_some() || mkcoeff!(@parse $RG_D2).is_some() || mkcoeff!(@parse $RG_D3).is_some() { Some(rs_wrap) } else { None },
                            rl: if mkcoeff!(@parse $RG_DL).is_some() || mkcoeff!(@parse $RG_D0).is_some() || mkcoeff!(@parse $RG_D1).is_some() || mkcoeff!(@parse $RG_D2).is_some() || mkcoeff!(@parse $RG_D3).is_some() { Some(rl_wrap) } else { None },
                            sr: if mkcoeff!(@parse $D0_RG).is_some() || mkcoeff!(@parse $D1_RG).is_some() || mkcoeff!(@parse $D2_RG).is_some() || mkcoeff!(@parse $D3_RG).is_some() { Some(sr_wrap) } else { None },
                            ss: if mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                   mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                   mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                   mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                { Some(ss_wrap) } else { None },
                            sl: if mkcoeff!(@parse $D0_DL).is_some() || mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                   mkcoeff!(@parse $D1_DL).is_some() || mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                   mkcoeff!(@parse $D2_DL).is_some() || mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                   mkcoeff!(@parse $D3_DL).is_some() || mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                { Some(sl_wrap) } else { None },
                            lr: if mkcoeff!(@parse $DL_RG).is_some() || mkcoeff!(@parse $D0_RG).is_some() || mkcoeff!(@parse $D1_RG).is_some() || mkcoeff!(@parse $D2_RG).is_some() || mkcoeff!(@parse $D3_RG).is_some() 
                                { Some(lr_wrap) } else { None },
                            ls: if mkcoeff!(@parse $DL_D0).is_some() || mkcoeff!(@parse $DL_D1).is_some() || mkcoeff!(@parse $DL_D2).is_some() || mkcoeff!(@parse $DL_D3).is_some() ||
                                   mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                   mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                   mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                   mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                { Some(ls_wrap) } else { None },
                            ll: if mkcoeff!(@parse $DL_DL).is_some() || mkcoeff!(@parse $DL_D0).is_some() || mkcoeff!(@parse $DL_D1).is_some() || mkcoeff!(@parse $DL_D2).is_some() || mkcoeff!(@parse $DL_D3).is_some() ||
                                   mkcoeff!(@parse $D0_DL).is_some() || mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                   mkcoeff!(@parse $D1_DL).is_some() || mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                   mkcoeff!(@parse $D2_DL).is_some() || mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                   mkcoeff!(@parse $D3_DL).is_some() || mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                { Some(ll_wrap) } else { None },
                        }
                    },
                )*
                _ => panic!("Scale {} not supported", scale),
            }
        }
    };
}
}

pub mod ft;
pub mod fl;
pub mod f3;
pub mod gt;
pub mod gl;
pub mod g1;
