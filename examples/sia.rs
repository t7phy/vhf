use vhf::sia::ft::*;
use vhf::sia::fl::*;
use vhf::core::scits::quad::{quad, nquad, Bound};
use neopdf::pdf::PDF;

pub fn main() {
    let z_vec = [
        0.01 , 0.02 , 0.05 , 0.07 , 0.1  , 0.2  , 0.3  , 0.4  , 0.5  , 0.6  , 0.7  , 0.8  , 0.9  
    ];

    let Q = 10.0;
    let nf = 5.0;
    let ff = PDF::load("MAPFF10NNLOPIp", 0);
    let pid = 21;

    let res_ft = |x: f64| -> f64 {
        let cf = ft_nnlo_g::cf();
        let fxq = ff.xfxq2(pid, &[x, Q * Q]) / x;

        let (val_r, _) = quad(
            |xhat: f64| {
                let fxq = ff.xfxq2(pid, &[x / xhat, Q * Q]) / (x / xhat);
                fxq * cf.r(xhat, nf) / xhat
            },
            x,
            1.0,
            1e-6,
        );
        let (val_s, _) = quad(
            |xhat: f64| {
                let fxq_xhat = ff.xfxq2(pid, &[x / xhat, Q * Q]) / (x / xhat);
                cf.s(xhat, nf) * (fxq_xhat / xhat - fxq)   // fxq here = the OUTER, fixed D(x)
            },
            x, 1.0, 1e-6,
        );
        let val_l = fxq * cf.l(x, nf);

        let res = val_l + val_r + val_s;
        res
    };

    let res_fl = |x: f64| -> f64 {
        let cf = fl_nnlo_g::cf();
        let fxq = ff.xfxq2(pid, &[x, Q * Q]) / x;

        let (val_r, _) = quad(
            |xhat: f64| {
                let fxq = ff.xfxq2(pid, &[x / xhat, Q * Q]) / (x / xhat);
                fxq * cf.r(xhat, nf) / xhat
            },
            x,
            1.0,
            1e-6,
        );
        let (val_s, _) = quad(
            |xhat: f64| {
                let fxq_xhat = ff.xfxq2(pid, &[x / xhat, Q * Q]) / (x / xhat);
                cf.s(xhat, nf) * (fxq_xhat / xhat - fxq)
            },
            x, 1.0, 1e-6,
        );
        let val_l = fxq * cf.l(x, nf);

        let res = val_l + val_r + val_s;
        res
    };

    for z in z_vec.iter() {
        let val = res_ft(*z) + res_fl(*z);
        println!("{:.6e} {:.6e}", z, val);
    }
}