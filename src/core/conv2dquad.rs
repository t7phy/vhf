use crate::sidis::CoeffFuncs as Cf2D;
use super::interpolation::{BasisCache, compute_basis_functions, point_interpolator, interpolator, integration_regions};

use crate::core::quad::{quad, nquad, Bound};

use rayon::prelude::*;


const EPS_INTEGRATION_BORDER: f64 = 1e-10;


pub struct Conv2DPointQuad {
    pub x: f64,
    pub z: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf2D,
    pub pid_pdf: i32,
    pub pid_ff: i32,
    pub fxq_pdf: fn(i32, f64, f64) -> f64,
    pub fxq_ff: fn(i32, f64, f64) -> f64,
    pub epsrel: f64,
}

impl Conv2DPointQuad {
    pub fn new(
        x: f64,
        z: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf2D,
        pid_pdf: i32,
        pid_ff: i32,
        fxq_pdf: fn(i32, f64, f64) -> f64,
        fxq_ff: fn(i32, f64, f64) -> f64,
        epsrel: f64,
    ) -> Self {
        Self {
            x,
            z,
            q,
            nf,
            coeff_func,
            pid_pdf,
            pid_ff,
            fxq_pdf,
            fxq_ff,
            epsrel,
        }
    }

    pub fn compute(&self) -> f64 {
        self.compute_full().0
    }

    pub fn compute_full(&self) -> (f64, f64) {
        assert!(self.x > 0.0 && self.x <= 1.0, "x must satisfy 0 < x <= 1");
        assert!(self.z > 0.0 && self.z <= 1.0, "z must satisfy 0 < z <= 1");

        let x = self.x;
        let z = self.z;
        let q = self.q;
        let nf = self.nf;
        let pid_pdf = self.pid_pdf;
        let pid_ff = self.pid_ff;
        let fxq_pdf = self.fxq_pdf;
        let fxq_ff = self.fxq_ff;
        let coeff_func = &self.coeff_func;

        let pdf_at_x = fxq_pdf(pid_pdf, x, q);
        let ff_at_z = fxq_ff(pid_ff, z, q);

        let bounds = vec![
            Bound::Fixed(x, 1.0),
            Bound::Fixed(z, 1.0),
        ];

        let (integral_val_xz, integral_err_xz) = nquad(
            |args: &[f64]| -> f64 {
                let xhat = args[0];
                let zhat = args[1];

                let pdf_val = fxq_pdf(pid_pdf, x / xhat, q);
                let ff_val = fxq_ff(pid_ff, z / zhat, q);
                let pdf_term_val = pdf_val / xhat;
                let ff_term_val = ff_val / zhat;

                coeff_func.rr(xhat, zhat, nf) * pdf_term_val * ff_term_val
                    + coeff_func.rs(xhat, zhat, nf) * pdf_term_val * (ff_term_val - ff_at_z)
                    + coeff_func.sr(xhat, zhat, nf) * (pdf_term_val - pdf_at_x) * ff_term_val
                    + coeff_func.ss(xhat, zhat, nf) * (pdf_term_val - pdf_at_x) * (ff_term_val - ff_at_z)
            },
            &bounds,
            self.epsrel,
        );
                
        let (integral_val_x, integral_err_x) = quad(
            |xhat: f64| -> f64 {
                let pdf_val = fxq_pdf(pid_pdf, x / xhat, q);
                let pdf_term_val = pdf_val / xhat;

                coeff_func.rl(xhat, z, nf) * pdf_term_val * ff_at_z
                    + coeff_func.sl(xhat, z, nf) * (pdf_term_val - pdf_at_x) * ff_at_z
            },
            x,
            1.0,
            self.epsrel,                
        );

        let (integral_val_z, integral_err_z) = quad(
            |zhat: f64| -> f64 {
                let ff_val = fxq_ff(pid_ff, z / zhat, q);
                let ff_term_val = ff_val / zhat;

                coeff_func.lr(x, zhat, nf) * ff_term_val * pdf_at_x
                    + coeff_func.ls(x, zhat, nf) * (ff_term_val - ff_at_z) * pdf_at_x
            },
            z,
            1.0,
            self.epsrel,
        );

        let local_term = coeff_func.ll(x, z, nf) * pdf_at_x * ff_at_z;

        let res = integral_val_xz + integral_val_x + integral_val_z + local_term;
        let err = integral_err_xz + integral_err_x + integral_err_z;

        (res, err)
    }
}

pub struct Conv2DBinQuad {
    pub xmin: f64,
    pub xmax: f64,
    pub zmin: f64,
    pub zmax: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf2D,
    pub pid_pdf: i32,
    pub pid_ff: i32,
    pub fxq_pdf: fn(i32, f64, f64) -> f64,
    pub fxq_ff: fn(i32, f64, f64) -> f64,
    pub epsrel: f64,
}

impl Conv2DBinQuad {
    pub fn new(
        xmin: f64,
        xmax: f64,
        zmin: f64,
        zmax: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf2D,
        pid_pdf: i32,
        pid_ff: i32,
        fxq_pdf: fn(i32, f64, f64) -> f64,
        fxq_ff: fn(i32, f64, f64) -> f64,
        epsrel: f64,
    ) -> Self {
        Self {
            xmin,
            xmax,
            zmin,
            zmax,
            q,
            nf,
            coeff_func,
            pid_pdf,
            pid_ff,
            fxq_pdf,
            fxq_ff,
            epsrel,
        }
    }

    pub fn compute(&self) -> f64 {
        self.compute_full().0
    }

    pub fn compute_full(&self) -> (f64, f64) {
        assert!(self.xmin > 0.0, "xmin must be > 0");
        assert!(self.xmax <= 1.0, "xmax must be <= 1");
        assert!(self.zmin > 0.0, "zmin must be > 0");
        assert!(self.zmax <= 1.0, "zmax must be <= 1");
        assert!(self.xmin < self.xmax, "require xmin < xmax");
        assert!(self.zmin < self.zmax, "require zmin < zmax");

        let xmin = self.xmin;
        let xmax = self.xmax;
        let zmin = self.zmin;
        let zmax = self.zmax;
        let q = self.q;
        let nf = self.nf;
        let pid_pdf = self.pid_pdf;
        let pid_ff = self.pid_ff;
        let fxq_pdf = self.fxq_pdf;
        let fxq_ff = self.fxq_ff;
        let coeff_func = &self.coeff_func;
        let epsrel = self.epsrel;

        // 4D doubly-nonlocal piece:
        // ∫ dx ∫ dz ∫_x^1 dxhat ∫_z^1 dzhat [ rr + rs + sr + ss ]
        let bounds_xz = vec![
            Bound::Fixed(xmin, xmax),
            Bound::Fixed(zmin, zmax),
            Bound::Dynamic(Box::new(|args: &[f64]| {
                let x = args[0];
                (x, 1.0)
            })),
            Bound::Dynamic(Box::new(|args: &[f64]| {
                let z = args[1];
                (z, 1.0)
            })),
        ];

        let (integral_val_xz, integral_err_xz) = nquad(
            |args: &[f64]| -> f64 {
                let x = args[0];
                let z = args[1];
                let xhat = args[2];
                let zhat = args[3];

                let pdf_at_x = fxq_pdf(pid_pdf, x, q);
                let ff_at_z = fxq_ff(pid_ff, z, q);

                let pdf_val = fxq_pdf(pid_pdf, x / xhat, q);
                let ff_val = fxq_ff(pid_ff, z / zhat, q);

                let pdf_term_val = pdf_val / xhat;
                let ff_term_val = ff_val / zhat;

                coeff_func.rr(xhat, zhat, nf) * pdf_term_val * ff_term_val
                    + coeff_func.rs(xhat, zhat, nf) * pdf_term_val * (ff_term_val - ff_at_z)
                    + coeff_func.sr(xhat, zhat, nf) * (pdf_term_val - pdf_at_x) * ff_term_val
                    + coeff_func.ss(xhat, zhat, nf)
                        * (pdf_term_val - pdf_at_x)
                        * (ff_term_val - ff_at_z)
            },
            &bounds_xz,
            epsrel,
        );

        // 3D x-edge piece:
        // ∫ dx ∫ dz ∫_x^1 dxhat [ rl + sl ]
        let bounds_x = vec![
            Bound::Fixed(xmin, xmax),
            Bound::Fixed(zmin, zmax),
            Bound::Dynamic(Box::new(|args: &[f64]| {
                let x = args[0];
                (x, 1.0)
            })),
        ];

        let (integral_val_x, integral_err_x) = nquad(
            |args: &[f64]| -> f64 {
                let x = args[0];
                let z = args[1];
                let xhat = args[2];

                let pdf_at_x = fxq_pdf(pid_pdf, x, q);
                let ff_at_z = fxq_ff(pid_ff, z, q);

                let pdf_val = fxq_pdf(pid_pdf, x / xhat, q);
                let pdf_term_val = pdf_val / xhat;

                coeff_func.rl(xhat, z, nf) * pdf_term_val * ff_at_z
                    + coeff_func.sl(xhat, z, nf) * (pdf_term_val - pdf_at_x) * ff_at_z
            },
            &bounds_x,
            epsrel,
        );

        // 3D z-edge piece:
        // ∫ dx ∫ dz ∫_z^1 dzhat [ lr + ls ]
        let bounds_z = vec![
            Bound::Fixed(xmin, xmax),
            Bound::Fixed(zmin, zmax),
            Bound::Dynamic(Box::new(|args: &[f64]| {
                let z = args[1];
                (z, 1.0)
            })),
        ];

        let (integral_val_z, integral_err_z) = nquad(
            |args: &[f64]| -> f64 {
                let x = args[0];
                let z = args[1];
                let zhat = args[2];

                let pdf_at_x = fxq_pdf(pid_pdf, x, q);
                let ff_at_z = fxq_ff(pid_ff, z, q);

                let ff_val = fxq_ff(pid_ff, z / zhat, q);
                let ff_term_val = ff_val / zhat;

                coeff_func.lr(x, zhat, nf) * ff_term_val * pdf_at_x
                    + coeff_func.ls(x, zhat, nf) * (ff_term_val - ff_at_z) * pdf_at_x
            },
            &bounds_z,
            epsrel,
        );

        // 2D local piece:
        // ∫ dx ∫ dz ll(x,z,nf) f(x,q) D(z,q)
        let bounds_local = vec![
            Bound::Fixed(xmin, xmax),
            Bound::Fixed(zmin, zmax),
        ];

        let (local_val, local_err) = nquad(
            |args: &[f64]| -> f64 {
                let x = args[0];
                let z = args[1];

                let pdf_at_x = fxq_pdf(pid_pdf, x, q);
                let ff_at_z = fxq_ff(pid_ff, z, q);

                coeff_func.ll(x, z, nf) * pdf_at_x * ff_at_z
            },
            &bounds_local,
            epsrel,
        );

        let total_val = integral_val_xz + integral_val_x + integral_val_z + local_val;
        let total_err = integral_err_xz + integral_err_x + integral_err_z + local_err;

        (total_val, total_err)
    }
}

pub struct Conv2DPointGrid {
    pub x: f64,
    pub z: f64,
    pub q: f64,
    pub nf: f64,
    pub coeff_func: Cf2D,
    // pub obs_def_func: fn(f64, f64, f64) -> f64,
    pub itp_xgrid: Vec<f64>,
    pub itp_zgrid: Vec<f64>,
    pub mode_log_x: bool,
    pub mode_log_z: bool,
    pub basis_functions_x: BasisCache,
    pub basis_functions_z: BasisCache,
    pub interpolator_at_x: Vec<f64>,
    pub interpolator_at_z: Vec<f64>,
    pub integration_regions_x: Option<Vec<(f64, f64)>>,
    pub integration_regions_z: Option<Vec<(f64, f64)>>,
}

impl Conv2DPointGrid {
    pub fn new(
        x: f64,
        z: f64,
        q: f64,
        nf: f64,
        coeff_func: Cf2D,
        // obs_def_func: fn(f64, f64, f64) -> f64,
        itp_xgrid: Vec<f64>,
        itp_zgrid: Vec<f64>,
        mode_log_x: bool,
        mode_log_z: bool,
    ) -> Self {
        let basis_functions_x = compute_basis_functions(itp_xgrid.clone(), 4, mode_log_x);
        let basis_functions_z = compute_basis_functions(itp_zgrid.clone(), 4, mode_log_z);

        let interpolator_at_x = interpolator(x, &basis_functions_x);
        let interpolator_at_z = interpolator(z, &basis_functions_z);

        let regions_x = integration_regions(x, &itp_xgrid);
        let regions_z = integration_regions(z, &itp_zgrid);

        Self {
            x,
            z,
            q,
            nf,
            coeff_func,
            // obs_def_func,
            itp_xgrid,
            itp_zgrid,
            mode_log_x,
            mode_log_z,
            basis_functions_x,
            basis_functions_z,
            interpolator_at_x,
            interpolator_at_z,
            integration_regions_x: regions_x,
            integration_regions_z: regions_z,
        }
    }

    pub fn compute(&self) -> Vec<Vec<f64>> {
        (0..self.itp_xgrid.len())
            .into_par_iter()
            .map(|xnode| {
                (0..self.itp_zgrid.len())
                    .map(|znode| {
                        let mut res: f64 = 0.0;

                        let pieces_x = &self.basis_functions_x.functions[xnode];
                        let max_xmax_raw = pieces_x.last().unwrap().xmax;
                        let max_xmax = if self.mode_log_x {
                            max_xmax_raw.exp()
                        } else {
                            max_xmax_raw
                        };

                        let pieces_z = &self.basis_functions_z.functions[znode];
                        let max_zmax_raw = pieces_z.last().unwrap().xmax;
                        let max_zmax = if self.mode_log_z {
                            max_zmax_raw.exp()
                        } else {
                            max_zmax_raw
                        };

                        if self.x >= (1.0 - EPS_INTEGRATION_BORDER)
                            || self.z >= (1.0 - EPS_INTEGRATION_BORDER)
                            || max_xmax <= self.x
                            || max_zmax <= self.z
                        {
                            return 0.0;
                        }

                        let interp_at_x = self.interpolator_at_x[xnode];
                        let interp_at_z = self.interpolator_at_z[znode];

                        let epsrel = 1e-6;

                        // Double piece in xhat and zhat:
                        if let (Some(ref regions_x), Some(ref regions_z)) =
                            (&self.integration_regions_x, &self.integration_regions_z)
                        {
                            for i in regions_x {
                                let ax = i.0 * (1.0 + EPS_INTEGRATION_BORDER);
                                let bx = i.1 * (1.0 - EPS_INTEGRATION_BORDER);

                                if bx <= ax {
                                    continue;
                                }

                                for j in regions_z {
                                    let az = j.0 * (1.0 + EPS_INTEGRATION_BORDER);
                                    let bz = j.1 * (1.0 - EPS_INTEGRATION_BORDER);

                                    if bz <= az {
                                        continue;
                                    }

                                    let bounds = vec![
                                        Bound::Fixed(ax, bx),
                                        Bound::Fixed(az, bz),
                                    ];

                                    let (quad_val, _quad_err) = nquad(
                                        |args: &[f64]| -> f64 {
                                            let xhat = args[0];
                                            let zhat = args[1];

                                            let interp_val_x = point_interpolator(
                                                self.x / xhat,
                                                &self.basis_functions_x,
                                                xnode,
                                            );
                                            let interp_val_z = point_interpolator(
                                                self.z / zhat,
                                                &self.basis_functions_z,
                                                znode,
                                            );

                                            let term_val_x = interp_val_x / xhat;
                                            let term_val_z = interp_val_z / zhat;

                                            let mut val: f64 = 0.0;
                                            val += self.coeff_func.rr(xhat, zhat, self.nf)
                                                * term_val_x
                                                * term_val_z;
                                            val += self.coeff_func.rs(xhat, zhat, self.nf)
                                                * term_val_x
                                                * (term_val_z - interp_at_z);
                                            val += self.coeff_func.sr(xhat, zhat, self.nf)
                                                * (term_val_x - interp_at_x)
                                                * term_val_z;
                                            val += self.coeff_func.ss(xhat, zhat, self.nf)
                                                * (term_val_x - interp_at_x)
                                                * (term_val_z - interp_at_z);
                                            // val *= (self.obs_def_func)(self.x, self.z, self.q);
                                            val
                                        },
                                        &bounds,
                                        epsrel,
                                    );

                                    res += quad_val;
                                }
                            }
                        }

                        // xhat-only piece:
                        if let Some(ref regions_x) = self.integration_regions_x {
                            for i in regions_x {
                                let a = i.0 * (1.0 + EPS_INTEGRATION_BORDER);
                                let b = i.1 * (1.0 - EPS_INTEGRATION_BORDER);

                                if b <= a {
                                    continue;
                                }

                                let (quad_val, _quad_err) = quad(
                                    |xhat: f64| -> f64 {
                                        if xhat <= 0.0 || xhat >= 1.0 {
                                            return 0.0;
                                        }

                                        let interp_val_x = point_interpolator(
                                            self.x / xhat,
                                            &self.basis_functions_x,
                                            xnode,
                                        );
                                        let term_val_x = interp_val_x / xhat;

                                        let mut val: f64 = 0.0;
                                        val += self.coeff_func.rl(xhat, self.z, self.nf)
                                            * term_val_x
                                            * interp_at_z;
                                        val += self.coeff_func.sl(xhat, self.z, self.nf)
                                            * (term_val_x - interp_at_x)
                                            * interp_at_z;
                                        // val *= (self.obs_def_func)(self.x, self.z, self.q);
                                        val
                                    },
                                    a,
                                    b,
                                    epsrel,
                                );

                                res += quad_val;
                            }
                        }

                        // zhat-only piece:
                        if let Some(ref regions_z) = self.integration_regions_z {
                            for j in regions_z {
                                let a = j.0 * (1.0 + EPS_INTEGRATION_BORDER);
                                let b = j.1 * (1.0 - EPS_INTEGRATION_BORDER);

                                if b <= a {
                                    continue;
                                }

                                let (quad_val, _quad_err) = quad(
                                    |zhat: f64| -> f64 {
                                        if zhat <= 0.0 || zhat >= 1.0 {
                                            return 0.0;
                                        }

                                        let interp_val_z = point_interpolator(
                                            self.z / zhat,
                                            &self.basis_functions_z,
                                            znode,
                                        );
                                        let term_val_z = interp_val_z / zhat;

                                        let mut val: f64 = 0.0;
                                        val += self.coeff_func.lr(self.x, zhat, self.nf)
                                            * term_val_z
                                            * interp_at_x;
                                        val += self.coeff_func.ls(self.x, zhat, self.nf)
                                            * (term_val_z - interp_at_z)
                                            * interp_at_x;
                                        // val *= (self.obs_def_func)(self.x, self.z, self.q);
                                        val
                                    },
                                    a,
                                    b,
                                    epsrel,
                                );

                                res += quad_val;
                            }
                        }

                        // Local term:
                        res += self.coeff_func.ll(self.x, self.z, self.nf)
                            * interp_at_x
                            * interp_at_z;

                        res
                    })
                    .collect()
            })
            .collect()
    }
}