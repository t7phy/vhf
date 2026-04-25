use rayon::prelude::*;
use rand::{Rng, SeedableRng};
use rand_chacha::ChaCha8Rng;
use std::f64;

/// Maximum dimensions supported without heap allocation in the hot loop.
const MAX_DIM: usize = 10;
/// Prevents floating-point underflow from collapsing bins to zero width.
const MIN_BIN_WIDTH: f64 = 1e-12;

/// Configuration for the VEGAS integrator.
#[derive(Debug, Clone)]
pub struct VegasConfig {
    /// Number of dimensions of the integrand.
    pub ndim: usize,
    /// Total budget for function evaluations across all iterations.
    pub max_evals: usize,
    /// Minimum iterations to run before convergence checks.
    pub min_iters: usize,
    /// Maximum iterations allowed.
    pub max_iters: usize,
    /// Target relative error (std_dev / estimate).
    pub epsrel: f64,
    /// Target absolute error.
    pub epsabs: f64,
    /// Number of adaptive bins per dimension (Standard: 50).
    pub bins_per_dim: usize,
    /// Grid stiffness: higher values make the grid more aggressive (Standard: 1.5).
    pub alpha: f64,
    /// Enable stratified sampling for guaranteed domain coverage.
    pub stratified: bool,
    /// Thread count: 0 for all available cores, 1 for sequential.
    pub num_threads: usize,
}

impl Default for VegasConfig {
    fn default() -> Self {
        Self {
            ndim: 1,
            max_evals: 100_000,
            min_iters: 5,
            max_iters: 15,
            epsrel: 1e-4,
            epsabs: 1e-15,
            bins_per_dim: 50,
            alpha: 1.5,
            stratified: true,
            num_threads: 0,
        }
    }
}

/// Results and reliability diagnostics of the integration.
#[derive(Debug, Clone, Default)]
pub struct VegasResult {
    /// The best estimate of the integral.
    pub estimate: f64,
    /// The 1-sigma statistical uncertainty.
    pub std_dev: f64,
    /// Chi-square per degree of freedom. Values near 1.0 indicate consistency.
    pub chi_sq_per_df: f64,
    /// Probability (Q) that the observed Chi-Square is consistent. 
    /// If p_value < 0.01, the result may be unreliable.
    pub p_value: f64,
    /// Total function evaluations actually performed.
    pub actual_evals: usize,
    /// Number of iterations completed.
    pub iters_completed: usize,
}

pub struct Vegas {
    config: VegasConfig,
    grid: Vec<Vec<f64>>,
}

impl Vegas {
    pub fn new(mut config: VegasConfig) -> Self {
        assert!(config.ndim <= MAX_DIM, "ndim exceeds MAX_DIM ({})", MAX_DIM);
        if config.num_threads == 0 {
            config.num_threads = rayon::current_num_threads();
        }

        let mut grid = vec![vec![0.0; config.bins_per_dim + 1]; config.ndim];
        let step = 1.0 / config.bins_per_dim as f64;
        for d in 0..config.ndim {
            for i in 0..=config.bins_per_dim {
                grid[d][i] = i as f64 * step;
            }
        }
        Self { config, grid }
    }

    pub fn integrate<F>(&mut self, func: F) -> VegasResult
    where
        F: Fn(&[f64]) -> f64 + Sync + Send,
    {
        let pool = rayon::ThreadPoolBuilder::new()
            .num_threads(self.config.num_threads)
            .build()
            .unwrap();

        pool.install(|| self.internal_integrate(func))
    }

    fn internal_integrate<F>(&mut self, func: F) -> VegasResult
    where
        F: Fn(&[f64]) -> f64 + Sync + Send,
    {
        let mut all_estimates = Vec::with_capacity(self.config.max_iters);
        let mut all_weights = Vec::with_capacity(self.config.max_iters);
        let mut total_evals = 0;
        let bins_f64 = self.config.bins_per_dim as f64;

        for iter in 1..=self.config.max_iters {
            // Stratification logic
            let (strat_k, samples_per_stratum) = if self.config.stratified && self.config.ndim <= 6 {
                let k = (self.config.max_evals as f64 / self.config.max_iters as f64)
                    .powf(1.0 / self.config.ndim as f64).floor() as usize;
                if k > 1 {
                    let total_s = k.pow(self.config.ndim as u32);
                    let per_s = ((self.config.max_evals / self.config.max_iters) / total_s).max(1);
                    (k, per_s)
                } else { (1, self.config.max_evals / self.config.max_iters) }
            } else { (1, self.config.max_evals / self.config.max_iters) };

            let n_calls = if strat_k > 1 {
                strat_k.pow(self.config.ndim as u32) * samples_per_stratum
            } else { samples_per_stratum };

            let (iter_sum, iter_sum_sq, d_counts) = (0..n_calls)
                .into_par_iter()
                .fold(
                    || (0.0, 0.0, vec![vec![0.0; self.config.bins_per_dim]; self.config.ndim]),
                    |mut acc, i| {
                        let mut rng = ChaCha8Rng::seed_from_u64(i as u64 + (iter as u64 * 0xdeadbeef));
                        let mut x = [0.0; MAX_DIM];
                        let mut bin_idxs = [0usize; MAX_DIM];
                        let mut u = [0.0; MAX_DIM];
                        
                        if strat_k > 1 {
                            let mut temp_i = i / samples_per_stratum;
                            for d in 0..self.config.ndim {
                                let coord = temp_i % strat_k;
                                temp_i /= strat_k;
                                u[d] = (coord as f64 + rng.gen::<f64>()) / strat_k as f64;
                            }
                        } else {
                            for d in 0..self.config.ndim { u[d] = rng.gen::<f64>(); }
                        }

                        let mut weight = 1.0;
                        for d in 0..self.config.ndim {
                            let r = u[d];
                            let b_idx = ((r * bins_f64) as usize).min(self.config.bins_per_dim - 1);
                            let b_width = self.grid[d][b_idx+1] - self.grid[d][b_idx];
                            x[d] = self.grid[d][b_idx] + (r * bins_f64 - b_idx as f64) * b_width;
                            weight *= b_width * bins_f64;
                            bin_idxs[d] = b_idx;
                        }

                        let f_val = func(&x[..self.config.ndim]);
                        let f_w = f_val * weight;
                        
                        acc.0 += f_w;
                        acc.1 += f_w * f_w;
                        
                        let refine_val = f_w.powi(2);
                        for d in 0..self.config.ndim { acc.2[d][bin_idxs[d]] += refine_val; }
                        acc
                    }
                )
                .reduce(
                    || (0.0, 0.0, vec![vec![0.0; self.config.bins_per_dim]; self.config.ndim]),
                    |mut a, b| {
                        a.0 += b.0; a.1 += b.1;
                        for d in 0..self.config.ndim {
                            for i in 0..self.config.bins_per_dim { a.2[d][i] += b.2[d][i]; }
                        }
                        a
                    }
                );

            total_evals += n_calls;
            let n = n_calls as f64;
            let iter_est = iter_sum / n;
            let iter_var = ((iter_sum_sq / n) - iter_est.powi(2)).max(0.0) / n;
            let iter_var = iter_var.max(f64::MIN_POSITIVE); 
            
            all_estimates.push(iter_est);
            all_weights.push(1.0 / iter_var);

            // Compute cumulative diagnostics
            let mut sum_w = 0.0;
            let mut sum_we = 0.0;
            for j in 0..all_estimates.len() {
                sum_w += all_weights[j];
                sum_we += all_weights[j] * all_estimates[j];
            }
            let cur_global_est = sum_we / sum_w;
            let cur_std = (1.0 / sum_w).sqrt();

            if iter >= self.config.min_iters {
                let rel_err = cur_std / cur_global_est.abs().max(1e-18);
                if rel_err < self.config.epsrel || cur_std < self.config.epsabs {
                    return self.package_result(cur_global_est, cur_std, &all_estimates, &all_weights, total_evals, iter);
                }
            }
            self.refine_grid(&d_counts);
        }

        let mut sum_w = 0.0;
        let mut sum_we = 0.0;
        for j in 0..all_estimates.len() {
            sum_w += all_weights[j];
            sum_we += all_weights[j] * all_estimates[j];
        }
        let final_est = sum_we / sum_w;
        let final_std = (1.0 / sum_w).sqrt();
        self.package_result(final_est, final_std, &all_estimates, &all_weights, total_evals, self.config.max_iters)
    }

    fn package_result(&self, est: f64, std: f64, e: &[f64], w: &[f64], evals: usize, iters: usize) -> VegasResult {
        let mut chi_sq = 0.0;
        for i in 0..e.len() {
            chi_sq += w[i] * (e[i] - est).powi(2);
        }
        let df = (iters as f64 - 1.0).max(1.0);
        let p_val = VegasStats::gamma_q(df / 2.0, chi_sq / 2.0);

        VegasResult {
            estimate: est,
            std_dev: std,
            chi_sq_per_df: chi_sq / df,
            p_value: p_val,
            actual_evals: evals,
            iters_completed: iters,
        }
    }

    fn refine_grid(&mut self, d_counts: &[Vec<f64>]) {
        for d in 0..self.config.ndim {
            let mut smoothed = vec![0.0; self.config.bins_per_dim];
            for i in 0..self.config.bins_per_dim {
                let prev = d_counts[d][if i > 0 { i - 1 } else { 0 }];
                let curr = d_counts[d][i];
                let next = d_counts[d][if i < self.config.bins_per_dim - 1 { i + 1 } else { i }];
                let avg = (prev + curr + next) / 3.0;
                smoothed[i] = (avg + 1e-30).powf(self.config.alpha);
            }

            let total_w: f64 = smoothed.iter().sum();
            let step = total_w / self.config.bins_per_dim as f64;
            let mut new_grid = vec![0.0; self.config.bins_per_dim + 1];
            let mut cur_w = 0.0;
            let mut old_bin = 0;
            let mut old_bin_frac = 0.0;

            for i in 1..self.config.bins_per_dim {
                let target = i as f64 * step;
                while cur_w + smoothed[old_bin] * (1.0 - old_bin_frac) < target {
                    cur_w += smoothed[old_bin] * (1.0 - old_bin_frac);
                    old_bin += 1;
                    old_bin_frac = 0.0;
                }
                let needed = target - cur_w;
                let frac_needed = needed / smoothed[old_bin];
                let old_width = self.grid[d][old_bin+1] - self.grid[d][old_bin];
                let next_val = self.grid[d][old_bin] + (old_bin_frac + frac_needed) * old_width - (old_bin_frac * old_width);
                new_grid[i] = next_val.max(new_grid[i-1] + MIN_BIN_WIDTH);
                old_bin_frac += frac_needed;
                cur_w = target;
            }
            new_grid[self.config.bins_per_dim] = 1.0;
            self.grid[d] = new_grid;
        }
    }
}

pub struct VegasStats;
impl VegasStats {
    pub fn gamma_q(a: f64, x: f64) -> f64 {
        if x < 0.0 || a <= 0.0 { return 1.0; }
        if x < a + 1.0 { 1.0 - Self::series_g(a, x) } else { Self::continued_fraction_g(a, x) }
    }
    fn series_g(a: f64, x: f64) -> f64 {
        let mut sum = 1.0 / a;
        let mut term = sum;
        for i in 1..100 {
            term *= x / (a + i as f64);
            sum += term;
            if term.abs() < sum.abs() * 1e-14 { break; }
        }
        sum * (-x + a * x.ln() - Self::log_gamma(a)).exp()
    }
    fn continued_fraction_g(a: f64, x: f64) -> f64 {
        let mut b = x + 1.0 - a;
        let mut c = 1.0 / 1e-30;
        let mut d = 1.0 / b;
        let mut h = d;
        for i in 1..100 {
            let an = -(i as f64) * (i as f64 - a);
            b += 2.0;
            d = an.mul_add(d, b);
            if d.abs() < 1e-30 { d = 1e-30; }
            c = b + an / c;
            if c.abs() < 1e-30 { c = 1e-30; }
            d = 1.0 / d;
            let delta = d * c;
            h *= delta;
            if (delta - 1.0).abs() < 1e-14 { break; }
        }
        h * (-x + a * x.ln() - Self::log_gamma(a)).exp()
    }
    fn log_gamma(x: f64) -> f64 {
        let coeff = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5];
        let mut y = x;
        let mut tmp = x + 5.5;
        tmp -= (x + 0.5) * tmp.ln();
        let mut ser = 1.000000000190015;
        for c in coeff { y += 1.0; ser += c / y; }
        -tmp + (2.5066282746310005 * ser / x).ln()
    }
}