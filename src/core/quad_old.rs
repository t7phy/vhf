/// Result of a quadrature integration
pub struct QuadResult {
    pub estimate: f64,
    pub error_est: f64,
}

/// A simplified 1D Adaptive Gauss-Kronrod Integrator (like scipy.quad)
pub struct Quad;

impl Quad {
    // Gauss-Kronrod G7/K15 constants for the interval [-1, 1]
    const X: [f64; 8] = [
        0.0000000000000000, 0.2077849550078985, 0.4058451513773972, 
        0.5860872354676911, 0.7415311855993944, 0.8648644233597691, 
        0.9491079123427585, 0.9914553711208126
    ];
    // Weights for K15
    const WK: [f64; 8] = [
        0.2094821410847278, 0.2044391360536415, 0.1903505780647854, 
        0.1690047266392679, 0.1406532597103252, 0.1047900103222502, 
        0.0630920925110191, 0.0229353220105292
    ];
    // Weights for G7
    const WG: [f64; 8] = [
        0.4179591836734694, 0.0, 0.3818300505051189, 0.0, 
        0.2797053914892767, 0.0, 0.1294849661688697, 0.0
    ];

    /// Integrate f from a to b with adaptive bisection
    pub fn integrate<F>(f: &F, a: f64, b: f64, epsrel: f64, limit: usize) -> QuadResult 
    where F: Fn(f64) -> f64 {
        Self::adaptive_gk(f, a, b, epsrel, limit, 0)
    }

    fn adaptive_gk<F>(f: &F, a: f64, b: f64, epsrel: f64, limit: usize, depth: usize) -> QuadResult
    where F: Fn(f64) -> f64 {
        let center = 0.5 * (a + b);
        let half_width = 0.5 * (b - a);
        let abs_half_width = half_width.abs();

        let mut gk15 = f(center) * Self::WK[0];
        let mut g7 = f(center) * Self::WG[0];

        for i in 1..8 {
            let dx = half_width * Self::X[i];
            let f_sum = f(center - dx) + f(center + dx);
            gk15 += f_sum * Self::WK[i];
            g7 += f_sum * Self::WG[i];
        }

        let res_k15 = gk15 * abs_half_width;
        let res_g7 = g7 * abs_half_width;
        let error = (res_k15 - res_g7).abs();

        if depth < limit && error > epsrel * res_k15.abs() {
            let left = Self::adaptive_gk(f, a, center, epsrel, limit, depth + 1);
            let right = Self::adaptive_gk(f, center, b, epsrel, limit, depth + 1);
            QuadResult {
                estimate: left.estimate + right.estimate,
                error_est: left.error_est + right.error_est,
            }
        } else {
            QuadResult { estimate: res_k15, error_est: error }
        }
    }
}