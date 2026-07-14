use rayon::prelude::*;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::time::Instant;

// Import both the old and new structs/functions
use vhf::sidis::CoeffFuncs as Cf2D;
use vhf::sidis::fl::FLC2q2qM::cf as cf_new;
use vhf::sidis::fl::FLC2q2qM_old::cf as cf_old;

const EPS: f64 = 1e-14;
const MAX_PRINT_PER_COMPONENT: usize = 10;
const PROGRESS_STEP: usize = 20000;

// Tolerances
const REL_TOL: f64 = 1e-4; 
const ABS_TOL: f64 = 1e-12;

#[derive(Clone, Copy)]
struct Point {
    x: f64,
    z: f64,
}

#[derive(Default, Clone, Copy)]
struct Stats {
    total: usize,
    bad_old: usize,
    bad_new: usize,
    nan_new: usize,
    inf_new: usize,
    fixed: usize,       
    mismatches: usize,  
    printed_bad: usize,
    printed_diff: usize,
}

impl Stats {
    fn merge(self, other: Self) -> Self {
        Self {
            total: self.total + other.total,
            bad_old: self.bad_old + other.bad_old,
            bad_new: self.bad_new + other.bad_new,
            nan_new: self.nan_new + other.nan_new,
            inf_new: self.inf_new + other.inf_new,
            fixed: self.fixed + other.fixed,
            mismatches: self.mismatches + other.mismatches,
            printed_bad: self.printed_bad + other.printed_bad,
            printed_diff: self.printed_diff + other.printed_diff,
        }
    }
}

// Evaluates all 9 components for a given point and Coefficient Function instance
fn evaluate_all(cf: &Cf2D, p: &Point, nf: f64) -> [f64; 9] {
    [
        (cf.rr_fn)(p.x, p.z, nf),
        (cf.rs_fn)(p.x, p.z, nf),
        (cf.rl_fn)(p.x, p.z, nf),
        (cf.sr_fn)(p.x, p.z, nf),
        (cf.ss_fn)(p.x, p.z, nf),
        (cf.sl_fn)(p.x, p.z, nf),
        (cf.lr_fn)(p.x, p.z, nf),
        (cf.ls_fn)(p.x, p.z, nf),
        (cf.ll_fn)(p.x, p.z, nf),
    ]
}

fn main() {
    rayon::ThreadPoolBuilder::new().num_threads(16).build_global().unwrap();

    let nf = 5.0;
    let cf_new_inst = cf_new();
    let cf_old_inst = cf_old();
    
    // ---------------------------------------------------------
    // Phase 1: Generate all points
    // ---------------------------------------------------------
    println!("Generating scan points...");
    let mut points: Vec<Point> = Vec::with_capacity(200_000);

    // Uniform
    let n_uniform = 200usize;
    for ix in 0..n_uniform {
        let x = EPS + (1.0 - 2.0 * EPS) * (ix as f64) / ((n_uniform - 1) as f64);
        for iz in 0..n_uniform {
            let z = EPS + (1.0 - 2.0 * EPS) * (iz as f64) / ((n_uniform - 1) as f64);
            points.push(Point { x, z });
        }
    }

    // Edge
    let n_edge = 20_000usize;
    for i in 1..=n_edge {
        let t = (i as f64) / (n_edge as f64);
        let x = (1.0 - t.powi(8)).clamp(EPS, 1.0 - EPS);
        let z = (1.0 - t.powi(8)).clamp(EPS, 1.0 - EPS);
        points.push(Point { x, z });
        points.push(Point { x, z: 0.5 });
        points.push(Point { x: 0.5, z });
    }

    // Diag
    let n_diag = 20_000usize;
    for i in 1..=n_diag {
        let x = EPS + (1.0 - 2.0 * EPS) * (i as f64) / ((n_diag + 1) as f64);
        let z1 = (x + 1e-12).clamp(EPS, 1.0 - EPS);
        let z2 = (x - 1e-12).clamp(EPS, 1.0 - EPS);
        points.push(Point { x, z: z1 });
        points.push(Point { x, z: z2 });
    }

    // Anti-Diag
    let n_anti = 20_000usize;
    for i in 1..=n_anti {
        let x = EPS + (1.0 - 2.0 * EPS) * (i as f64) / ((n_anti + 1) as f64);
        let z0 = 1.0 - x;
        let z1 = (z0 + 1e-12).clamp(EPS, 1.0 - EPS);
        let z2 = (z0 - 1e-12).clamp(EPS, 1.0 - EPS);
        points.push(Point { x, z: z1 });
        points.push(Point { x, z: z2 });
    }

    let total_points = points.len();
    println!("Total points to evaluate: {}\n", total_points);

    // ---------------------------------------------------------
    // Phase 2: Time OLD Code
    // ---------------------------------------------------------
    println!("Evaluating OLD code on 16 threads...");
    let progress_old = AtomicUsize::new(0);
    let start_old = Instant::now();
    
    let results_old: Vec<[f64; 9]> = points.par_iter().map(|p| {
        let res = evaluate_all(&cf_old_inst, p, nf);
        let c = progress_old.fetch_add(1, Ordering::Relaxed);
        if c > 0 && c % PROGRESS_STEP == 0 { println!("  Old Progress: {} / {} points", c, total_points); }
        res
    }).collect();
    
    let time_old = start_old.elapsed();
    println!("-> OLD code finished in {:.4} seconds\n", time_old.as_secs_f64());

    // ---------------------------------------------------------
    // Phase 3: Time NEW Code
    // ---------------------------------------------------------
    println!("Evaluating NEW code on 16 threads...");
    let progress_new = AtomicUsize::new(0);
    let start_new = Instant::now();
    
    let results_new: Vec<[f64; 9]> = points.par_iter().map(|p| {
        let res = evaluate_all(&cf_new_inst, p, nf);
        let c = progress_new.fetch_add(1, Ordering::Relaxed);
        if c > 0 && c % PROGRESS_STEP == 0 { println!("  New Progress: {} / {} points", c, total_points); }
        res
    }).collect();
    
    let time_new = start_new.elapsed();
    println!("-> NEW code finished in {:.4} seconds\n", time_new.as_secs_f64());

    // --- TIMING SUMMARY ---
    let speedup = time_old.as_secs_f64() / time_new.as_secs_f64();
    println!("=================== PERFORMANCE SUMMARY ===================");
    println!("Old Code Time : {:.4} s", time_old.as_secs_f64());
    println!("New Code Time : {:.4} s", time_new.as_secs_f64());
    println!("Speedup       : {:.2}x FASTER", speedup);
    println!("===========================================================\n");

    let time_old = start_old.elapsed().as_secs_f64();
    let time_new = start_new.elapsed().as_secs_f64();

    // ---------------------------------------------------------
    // Phase 4: Compare Results
    // ---------------------------------------------------------
    println!("Comparing results for correctness...");
    let names = ["rr", "rs", "rl", "sr", "ss", "sl", "lr", "ls", "ll"];
    
    // We zip the points, old results, and new results together in parallel
    let global_stats: [Stats; 9] = points.into_par_iter()
        .zip(results_old.into_par_iter())
        .zip(results_new.into_par_iter())
        .map(|((p, old_vals), new_vals)| {
            let mut local_stats = [Stats::default(); 9];
            
            for i in 0..9 {
                let name = names[i];
                let val_old = old_vals[i];
                let val_new = new_vals[i];
                let stats = &mut local_stats[i];
                
                stats.total += 1;
                let old_ok = val_old.is_finite();
                let new_ok = val_new.is_finite();

                if !old_ok {
                    stats.bad_old += 1;
                    if new_ok { stats.fixed += 1; }
                }

                if !new_ok {
                    stats.bad_new += 1;
                    if val_new.is_nan() { stats.nan_new += 1; } else { stats.inf_new += 1; }
                    if stats.printed_bad < MAX_PRINT_PER_COMPONENT {
                        println!("NEW BAD {:>2}: x = {:.16e}, z = {:.16e}, value = {:?}", name, p.x, p.z, val_new);
                        stats.printed_bad += 1;
                    }
                }

                if new_ok && old_ok {
                    let diff = (val_new - val_old).abs();
                    let max_val = val_new.abs().max(val_old.abs());
                    
                    let is_mismatch = if max_val < ABS_TOL {
                        diff > ABS_TOL
                    } else {
                        (diff / max_val) > REL_TOL
                    };

                    if is_mismatch {
                        stats.mismatches += 1;
                        if stats.printed_diff < MAX_PRINT_PER_COMPONENT {
                            let rel_diff = diff / max_val;
                            println!(
                                "MISMATCH {:>2}: x = {:.16e}, z = {:.16e}\n  old  = {:?}\n  new  = {:?}\n  rel_diff = {:.2e}",
                                name, p.x, p.z, val_old, val_new, rel_diff
                            );
                            stats.printed_diff += 1;
                        }
                    }
                }
            }
            local_stats
        }).reduce(|| [Stats::default(); 9], merge_all);

    print_summary(&global_stats, time_old, time_new);
}

fn merge_all(mut a: [Stats; 9], b: [Stats; 9]) -> [Stats; 9] {
    for i in 0..9 {
        a[i] = a[i].merge(b[i]);
    }
    a
}

fn print_summary(stats: &[Stats; 9], time_old: f64, time_new: f64) {
    let names = ["rr", "rs", "rl", "sr", "ss", "sl", "lr", "ls", "ll"];
    println!("\n============================ FINAL SUMMARY ============================\n");
    println!(
        "{:>2} | {:>9} | {:>9} | {:>9} | {:>10} | {:>10}",
        "ID", "Total Pts", "Old NaNs", "New NaNs", "NaNs Fixed", "Mismatches"
    );
    println!("-----------------------------------------------------------------------");
    for (name, st) in names.iter().zip(stats.iter()) {
        println!(
            "{:>2} | {:>9} | {:>9} | {:>9} | {:>10} | {:>10}",
            name, st.total, st.bad_old, st.bad_new, st.fixed, st.mismatches
        );
    }
    
    // Print timings at the very end so they aren't lost!
    println!("\n=================== PERFORMANCE SUMMARY ===================");
    println!("Old Code Time : {:.4} s", time_old);
    println!("New Code Time : {:.4} s", time_new);
    let speedup = time_old / time_new;
    println!("Speedup       : {:.2}x FASTER", speedup);
    println!("===========================================================\n");
}