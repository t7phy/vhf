use rayon::prelude::*;
use std::sync::atomic::{AtomicUsize, Ordering};
use vhf::sidis::CoeffFuncs as Cf2D;
use vhf::sidis::fl::FLC2q2qM::cf;

const EPS: f64 = 1e-14;
const MAX_PRINT_PER_COMPONENT: usize = 10;
const PROGRESS_STEP: usize = 5000;

#[derive(Default, Clone, Copy)]
struct Stats {
    total: usize,
    bad: usize,
    nan: usize,
    inf: usize,
    printed: usize,
}

impl Stats {
    fn merge(self, other: Self) -> Self {
        Self {
            total: self.total + other.total,
            bad: self.bad + other.bad,
            nan: self.nan + other.nan,
            inf: self.inf + other.inf,
            printed: self.printed + other.printed,
        }
    }
}

fn check_component(name: &str, f: fn(f64, f64, f64) -> f64, x: f64, z: f64, nf: f64, stats: &mut Stats) {
    stats.total += 1;
    let val = f(x, z, nf);
    if !val.is_finite() {
        stats.bad += 1;
        if val.is_nan() { stats.nan += 1; } else { stats.inf += 1; }
        if stats.printed < MAX_PRINT_PER_COMPONENT {
            println!("BAD {:>2}: x = {:.16e}, z = {:.16e}, value = {:?}", name, x, z, val);
            stats.printed += 1;
        }
    }
}

fn scan_point(cf: &Cf2D, x: f64, z: f64, nf: f64, stats: &mut [Stats; 9]) {
    check_component("rr", cf.rr_fn, x, z, nf, &mut stats[0]);
    check_component("rs", cf.rs_fn, x, z, nf, &mut stats[1]);
    check_component("rl", cf.rl_fn, x, z, nf, &mut stats[2]);
    check_component("sr", cf.sr_fn, x, z, nf, &mut stats[3]);
    check_component("ss", cf.ss_fn, x, z, nf, &mut stats[4]);
    check_component("sl", cf.sl_fn, x, z, nf, &mut stats[5]);
    check_component("lr", cf.lr_fn, x, z, nf, &mut stats[6]);
    check_component("ls", cf.ls_fn, x, z, nf, &mut stats[7]);
    check_component("ll", cf.ll_fn, x, z, nf, &mut stats[8]);
}

fn merge_all(mut a: [Stats; 9], b: [Stats; 9]) -> [Stats; 9] {
    for i in 0..9 { a[i] = a[i].merge(b[i]); }
    a
}

fn main() {
    // Set global thread pool to 16
    rayon::ThreadPoolBuilder::new().num_threads(16).build_global().unwrap();

    let nf = 5.0;
    let cf_inst = cf();
    let mut global_stats = [Stats::default(); 9];

    // ---------------------------------------------------------
    // 1) Uniform scan: 200 x 200 = 40,000 points
    // ---------------------------------------------------------
    println!("Running uniform 200x200 scan on 16 threads...");
    let n_uniform = 1000usize;
    let progress = AtomicUsize::new(0);
    
    let stats_uniform = (0..n_uniform).into_par_iter().map(|ix| {
        let mut local = [Stats::default(); 9];
        let x = EPS + (1.0 - 2.0 * EPS) * (ix as f64) / ((n_uniform - 1) as f64);
        for iz in 0..n_uniform {
            let z = EPS + (1.0 - 2.0 * EPS) * (iz as f64) / ((n_uniform - 1) as f64);
            scan_point(&cf_inst, x, z, nf, &mut local);
            let c = progress.fetch_add(1, Ordering::Relaxed);
            if c > 0 && c % PROGRESS_STEP == 0 { println!("Progress: {} points...", c); }
        }
        local
    }).reduce(|| [Stats::default(); 9], merge_all);

    global_stats = merge_all(global_stats, stats_uniform);

    
    // ---------------------------------------------------------
    // 2) Endpoint-biased scan
    // ---------------------------------------------------------
    println!("\nRunning endpoint-biased scan on 16 threads...");
    let n_edge = 100_000usize;
    let progress_edge = AtomicUsize::new(0);

    let stats_edge = (1..=n_edge).into_par_iter().map(|i| {
        let mut local = [Stats::default(); 9];
        let t = (i as f64) / (n_edge as f64);
        let x = (1.0 - t.powi(8)).clamp(EPS, 1.0 - EPS);
        let z = (1.0 - t.powi(8)).clamp(EPS, 1.0 - EPS);

        scan_point(&cf_inst, x, z, nf, &mut local);
        scan_point(&cf_inst, x, 0.5, nf, &mut local);
        scan_point(&cf_inst, 0.5, z, nf, &mut local);

        let c = progress_edge.fetch_add(1, Ordering::Relaxed);
        if c > 0 && c % PROGRESS_STEP == 0 { println!("Progress (Edge): {} iterations...", c); }
        local
    }).reduce(|| [Stats::default(); 9], merge_all);

    global_stats = merge_all(global_stats, stats_edge);

    // ---------------------------------------------------------
    // 3) Near z = x
    // ---------------------------------------------------------
    println!("\nRunning near-diagonal scan z ~ x on 16 threads...");
    let n_diag = 100_000usize;
    let progress_diag = AtomicUsize::new(0);

    let stats_diag = (1..=n_diag).into_par_iter().map(|i| {
        let mut local = [Stats::default(); 9];
        let x = EPS + (1.0 - 2.0 * EPS) * (i as f64) / ((n_diag + 1) as f64);
        let z1 = (x + 1e-12).clamp(EPS, 1.0 - EPS);
        let z2 = (x - 1e-12).clamp(EPS, 1.0 - EPS);

        scan_point(&cf_inst, x, z1, nf, &mut local);
        scan_point(&cf_inst, x, z2, nf, &mut local);

        let c = progress_diag.fetch_add(1, Ordering::Relaxed);
        if c > 0 && c % PROGRESS_STEP == 0 { println!("Progress (Diag): {} iterations...", c); }
        local
    }).reduce(|| [Stats::default(); 9], merge_all);

    global_stats = merge_all(global_stats, stats_diag);

    // ---------------------------------------------------------
    // 4) Near z = 1 - x
    // ---------------------------------------------------------
    println!("\nRunning near-antidiagonal scan z ~ 1-x on 16 threads...");
    let n_anti = 100_000usize;
    let progress_anti = AtomicUsize::new(0);

    let stats_anti = (1..=n_anti).into_par_iter().map(|i| {
        let mut local = [Stats::default(); 9];
        let x = EPS + (1.0 - 2.0 * EPS) * (i as f64) / ((n_anti + 1) as f64);
        let z0 = 1.0 - x;
        let z1 = (z0 + 1e-12).clamp(EPS, 1.0 - EPS);
        let z2 = (z0 - 1e-12).clamp(EPS, 1.0 - EPS);

        scan_point(&cf_inst, x, z1, nf, &mut local);
        scan_point(&cf_inst, x, z2, nf, &mut local);

        let c = progress_anti.fetch_add(1, Ordering::Relaxed);
        if c > 0 && c % PROGRESS_STEP == 0 { println!("Progress (Anti): {} iterations...", c); }
        local
    }).reduce(|| [Stats::default(); 9], merge_all);

    global_stats = merge_all(global_stats, stats_anti);
    

    print_summary(&global_stats);
}

fn print_summary(stats: &[Stats; 9]) {
    let names = ["rr", "rs", "rl", "sr", "ss", "sl", "lr", "ls", "ll"];
    println!("\n================ FINAL SUMMARY ================\n");
    for (name, st) in names.iter().zip(stats.iter()) {
        println!(
            "{:>2}: total = {:>8}, bad = {:>8}, NaN = {:>8}, Inf = {:>8}",
            name, st.total, st.bad, st.nan, st.inf
        );
    }
}