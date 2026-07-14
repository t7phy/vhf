#![allow(unused_variables)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(non_camel_case_types)]
#![allow(unused_parens)]

pub use internal::{CoeffFuncs, SIDISFunc};

pub mod couplings;

#[macro_use]
pub(crate) mod internal {
    // pub use std::collections::HashMap;

    pub use crate::core::libfunc::{pow, ln, ArcTan, InvTanInt};
    pub use crate::core::polylogs::{Li2, Li3};
    pub use crate::core::constants::{NQCD, rln2, pi, zeta3, CF};
    pub const lmur: f64 = 0.5;
    pub const lmuf: f64 = 0.5;
    pub const lmua: f64 = 1.0;

    pub fn mysqrt(x: f64) -> f64 {
        x.sqrt()
    }

    pub type SIDISFunc = fn(f64, f64, f64) -> f64;

    #[derive(Clone, Copy)]
    pub struct CoeffFuncs {
        pub rr_fn: SIDISFunc, pub rs_fn: SIDISFunc, pub rl_fn: SIDISFunc,
        pub sr_fn: SIDISFunc, pub ss_fn: SIDISFunc, pub sl_fn: SIDISFunc,
        pub lr_fn: SIDISFunc, pub ls_fn: SIDISFunc, pub ll_fn: SIDISFunc,
    }
    
    impl CoeffFuncs {
        pub fn rr(&self, x: f64, z: f64, nf: f64) -> f64 { (self.rr_fn)(x, z, nf) }
        pub fn rs(&self, x: f64, z: f64, nf: f64) -> f64 { (self.rs_fn)(x, z, nf) }
        pub fn rl(&self, x: f64, z: f64, nf: f64) -> f64 { (self.rl_fn)(x, z, nf) }
        pub fn sr(&self, x: f64, z: f64, nf: f64) -> f64 { (self.sr_fn)(x, z, nf) }
        pub fn ss(&self, x: f64, z: f64, nf: f64) -> f64 { (self.ss_fn)(x, z, nf) }
        pub fn sl(&self, x: f64, z: f64, nf: f64) -> f64 { (self.sl_fn)(x, z, nf) }
        pub fn lr(&self, x: f64, z: f64, nf: f64) -> f64 { (self.lr_fn)(x, z, nf) }
        pub fn ls(&self, x: f64, z: f64, nf: f64) -> f64 { (self.ls_fn)(x, z, nf) }
        pub fn ll(&self, x: f64, z: f64, nf: f64) -> f64 { (self.ll_fn)(x, z, nf) }
    }
    
    pub fn zero_func(_: f64, _: f64, _: f64) -> f64 {
        0.0
    }
    
    macro_rules! mkcoeff {
        // Helper remains Option to allow internal optimization checks
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
    
            // New default cf function
            pub fn cf() -> CoeffFuncs {
                cf_sv("000")
            }
    
            // Renamed function
            pub fn cf_sv(scale: &str) -> CoeffFuncs {
                match scale {
                    $(
                        $scale => {
                            // --- Local Wrapper Definitions ---
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
                            CoeffFuncs {
                                rr_fn: mkcoeff!(@parse $RG_RG).unwrap_or(zero_func),
                                
                                rs_fn: if mkcoeff!(@parse $RG_D0).is_some() || mkcoeff!(@parse $RG_D1).is_some() || mkcoeff!(@parse $RG_D2).is_some() || mkcoeff!(@parse $RG_D3).is_some() 
                                    { rs_wrap } else { zero_func },
                                    
                                rl_fn: if mkcoeff!(@parse $RG_DL).is_some() || mkcoeff!(@parse $RG_D0).is_some() || mkcoeff!(@parse $RG_D1).is_some() || mkcoeff!(@parse $RG_D2).is_some() || mkcoeff!(@parse $RG_D3).is_some() 
                                    { rl_wrap } else { zero_func },
                                    
                                sr_fn: if mkcoeff!(@parse $D0_RG).is_some() || mkcoeff!(@parse $D1_RG).is_some() || mkcoeff!(@parse $D2_RG).is_some() || mkcoeff!(@parse $D3_RG).is_some() 
                                    { sr_wrap } else { zero_func },
                                    
                                ss_fn: if mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                       mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                       mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                       mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                    { ss_wrap } else { zero_func },
                                    
                                sl_fn: if mkcoeff!(@parse $D0_DL).is_some() || mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                       mkcoeff!(@parse $D1_DL).is_some() || mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                       mkcoeff!(@parse $D2_DL).is_some() || mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                       mkcoeff!(@parse $D3_DL).is_some() || mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                    { sl_wrap } else { zero_func },
                                    
                                lr_fn: if mkcoeff!(@parse $DL_RG).is_some() || mkcoeff!(@parse $D0_RG).is_some() || mkcoeff!(@parse $D1_RG).is_some() || mkcoeff!(@parse $D2_RG).is_some() || mkcoeff!(@parse $D3_RG).is_some() 
                                    { lr_wrap } else { zero_func },
                                    
                                ls_fn: if mkcoeff!(@parse $DL_D0).is_some() || mkcoeff!(@parse $DL_D1).is_some() || mkcoeff!(@parse $DL_D2).is_some() || mkcoeff!(@parse $DL_D3).is_some() ||
                                       mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                       mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                       mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                       mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                    { ls_wrap } else { zero_func },
                                    
                                ll_fn: if mkcoeff!(@parse $DL_DL).is_some() || mkcoeff!(@parse $DL_D0).is_some() || mkcoeff!(@parse $DL_D1).is_some() || mkcoeff!(@parse $DL_D2).is_some() || mkcoeff!(@parse $DL_D3).is_some() ||
                                       mkcoeff!(@parse $D0_DL).is_some() || mkcoeff!(@parse $D0_D0).is_some() || mkcoeff!(@parse $D0_D1).is_some() || mkcoeff!(@parse $D0_D2).is_some() || mkcoeff!(@parse $D0_D3).is_some() ||
                                       mkcoeff!(@parse $D1_DL).is_some() || mkcoeff!(@parse $D1_D0).is_some() || mkcoeff!(@parse $D1_D1).is_some() || mkcoeff!(@parse $D1_D2).is_some() || mkcoeff!(@parse $D1_D3).is_some() ||
                                       mkcoeff!(@parse $D2_DL).is_some() || mkcoeff!(@parse $D2_D0).is_some() || mkcoeff!(@parse $D2_D1).is_some() || mkcoeff!(@parse $D2_D2).is_some() || mkcoeff!(@parse $D2_D3).is_some() ||
                                       mkcoeff!(@parse $D3_DL).is_some() || mkcoeff!(@parse $D3_D0).is_some() || mkcoeff!(@parse $D3_D1).is_some() || mkcoeff!(@parse $D3_D2).is_some() || mkcoeff!(@parse $D3_D3).is_some() 
                                    { ll_wrap } else { zero_func },
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
