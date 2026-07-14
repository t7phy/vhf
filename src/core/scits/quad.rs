// use std::cmp::Ordering;
// use std::collections::BinaryHeap;

// // Gauss-Kronrod 7/15 nodes for the interval [-1, 1].
// // Because the nodes are symmetric, we only store the positive half.
// // Index 0 is the center (x=0). Indices 1-7 are the positive nodes.
// const GK_NODES: [f64; 8] = [
//     0.0000000000000000,
//     0.2077849550078985,
//     0.4058451513773972, // Gauss node
//     0.5860872354676911,
//     0.7415311855993944, // Gauss node
//     0.8648644233597691,
//     0.9491079123427585, // Gauss node
//     0.9914553711208126,
// ];

// // 15-point Kronrod weights corresponding to the nodes above.
// const K15_WEIGHTS: [f64; 8] = [
//     0.2094821410847278,
//     0.2044329400752989,
//     0.1903505780647854,
//     0.1690047266392679,
//     0.1406532597155259,
//     0.1047900103222502,
//     0.06309209262997855,
//     0.02293532201052922,
// ];

// // 7-point Gauss weights. They align with the even indices of the Kronrod nodes.
// const G7_WEIGHTS: [f64; 4] = [
//     0.4179591836734694, // corresponds to GK_NODES[0]
//     0.3818300505051189, // corresponds to GK_NODES[2]
//     0.2797053914892767, // corresponds to GK_NODES[4]
//     0.1294849661688697, // corresponds to GK_NODES[6]
// ];

// #[derive(Clone, Copy, Debug)]
// struct Interval {
//     a: f64,
//     b: f64,
//     integral: f64,
//     error: f64,
// }

// // Implement standard ordering logic so the BinaryHeap acts as a Max-Heap based on error.
// impl PartialEq for Interval {
//     fn eq(&self, other: &Self) -> bool {
//         self.error == other.error
//     }
// }
// impl Eq for Interval {}

// impl PartialOrd for Interval {
//     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
//         self.error.partial_cmp(&other.error)
//     }
// }
// impl Ord for Interval {
//     fn cmp(&self, other: &Self) -> Ordering {
//         self.partial_cmp(other).unwrap_or(Ordering::Equal)
//     }
// }

// /// Evaluates a specific interval using the G7-K15 rule.
// fn evaluate_interval<F: Fn(f64) -> f64>(f: &F, a: f64, b: f64) -> Interval {
//     let half_length = (b - a) / 2.0;
//     let center = (a + b) / 2.0;

//     let mut integral_k15 = f(center) * K15_WEIGHTS[0];
//     let mut integral_g7 = f(center) * G7_WEIGHTS[0];

//     // Exploit symmetry to evaluate the nodes
//     for i in 1..8 {
//         let x = half_length * GK_NODES[i];
//         let f_val = f(center + x) + f(center - x);
        
//         integral_k15 += f_val * K15_WEIGHTS[i];
        
//         // Gauss nodes are located at the even indices of our array
//         if i % 2 == 0 {
//             integral_g7 += f_val * G7_WEIGHTS[i / 2];
//         }
//     }

//     // Scale to the size of the interval
//     integral_k15 *= half_length;
//     integral_g7 *= half_length;

//     // The core of Gauss-Kronrod: Error is the difference between the high and low order rules
//     let error = (integral_k15 - integral_g7).abs();

//     Interval {
//         a,
//         b,
//         integral: integral_k15,
//         error,
//     }
// }

// /// A pure Rust implementation of scipy.integrate.quad (Adaptive G7-K15 Quadrature).
// /// Returns a tuple of (integral_estimate, error_estimate).
// pub fn quad<F: Fn(f64) -> f64>(f: F, a: f64, b: f64, epsrel: f64) -> (f64, f64) {
//     let max_intervals = 500; // Hard subdivision limit 
//     let epsabs = 1e-14; // Small absolute baseline to prevent infinite loops on integrals near 0

//     let mut heap = BinaryHeap::with_capacity(max_intervals);
//     let initial_interval = evaluate_interval(&f, a, b);
    
//     let mut total_integral = initial_interval.integral;
//     let mut total_error = initial_interval.error;
    
//     heap.push(initial_interval);

//     // Adaptive loop: Continually split the interval with the worst error
//     while total_error > (epsrel * total_integral.abs()).max(epsabs) && heap.len() < max_intervals {
//         let worst = heap.pop().unwrap();
        
//         let c = (worst.a + worst.b) / 2.0;
        
//         let left = evaluate_interval(&f, worst.a, c);
//         let right = evaluate_interval(&f, c, worst.b);
        
//         // Update running totals by removing the parent interval and adding the children
//         total_integral += left.integral + right.integral - worst.integral;
//         total_error += left.error + right.error - worst.error;
        
//         heap.push(left);
//         heap.push(right);
//     }

//     // If we hit our subdivision limit without reaching tolerance, print SciPy's warning
//     if total_error > (epsrel * total_integral.abs()).max(epsabs) {
//         eprintln!(
//             "IntegrationWarning: The maximum number of subdivisions ({}) has been achieved.\n\
//              If increasing the limit yields no improvement it is advised to analyze \n\
//              the integrand in order to determine the difficulties.",
//             max_intervals
//         );
//     }

//     (total_integral, total_error)
// }

// // fn main() {
// //     // Standard normal distribution example
// //     let target_accuracy = 1e-8;
    
// //     let (val, err) = quad(|x| x.sin(), 0.0, std::f64::consts::PI, target_accuracy);
// //     println!("sin(x) over [0, π]:");
// //     println!("Value: {:.10}", val);
// //     println!("Error: {:.1e}\n", err);

// //     // Harder test with a singularity-like peak
// //     let (val2, err2) = quad(|x| 1.0 / (x * x + 0.001), -1.0, 1.0, target_accuracy);
// //     println!("1 / (x^2 + 0.001) over [-1, 1]:");
// //     println!("Value: {:.10}", val2);
// //     println!("Error: {:.1e}", err2);
// // }

// use std::cmp::Ordering;
// use std::collections::BinaryHeap;

// // Gauss-Kronrod 7/15 nodes and weights
// const GK_NODES: [f64; 8] = [
//     0.0000000000000000, 0.2077849550078985, 0.4058451513773972, 0.5860872354676911,
//     0.7415311855993944, 0.8648644233597691, 0.9491079123427585, 0.9914553711208126,
// ];
// const K15_WEIGHTS: [f64; 8] = [
//     0.2094821410847278, 0.2044329400752989, 0.1903505780647854, 0.1690047266392679,
//     0.1406532597155259, 0.1047900103222502, 0.06309209262997855, 0.02293532201052922,
// ];
// const G7_WEIGHTS: [f64; 4] = [
//     0.4179591836734694, 0.3818300505051189, 0.2797053914892767, 0.1294849661688697,
// ];

// #[derive(Clone, Copy, Debug)]
// struct Interval {
//     a: f64,
//     b: f64,
//     integral: f64,
//     error: f64,
// }

// impl PartialEq for Interval {
//     fn eq(&self, other: &Self) -> bool {
//         self.error == other.error
//     }
// }
// impl Eq for Interval {}
// impl PartialOrd for Interval {
//     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
//         self.error.partial_cmp(&other.error)
//     }
// }
// impl Ord for Interval {
//     fn cmp(&self, other: &Self) -> Ordering {
//         self.partial_cmp(other).unwrap_or(Ordering::Equal)
//     }
// }

// /// Allows bounds to either be hardcoded floats or functions of the previous arguments.
// pub enum Bound<'a> {
//     Fixed(f64, f64),
//     Dynamic(Box<dyn Fn(&[f64]) -> (f64, f64) + 'a>),
// }

// /// The core Gauss-Kronrod interval evaluator
// fn evaluate_interval<F: FnMut(f64) -> f64>(f: &mut F, a: f64, b: f64) -> Interval {
//     let half_length = (b - a) / 2.0;
//     let center = (a + b) / 2.0;

//     let mut integral_k15 = f(center) * K15_WEIGHTS[0];
//     let mut integral_g7 = f(center) * G7_WEIGHTS[0];

//     for i in 1..8 {
//         let x = half_length * GK_NODES[i];
//         let f_val = f(center + x) + f(center - x);
        
//         integral_k15 += f_val * K15_WEIGHTS[i];
//         if i % 2 == 0 {
//             integral_g7 += f_val * G7_WEIGHTS[i / 2];
//         }
//     }

//     integral_k15 *= half_length;
//     integral_g7 *= half_length;

//     Interval {
//         a, b,
//         integral: integral_k15,
//         error: (integral_k15 - integral_g7).abs(),
//     }
// }

// /// The inner adaptive quadrature loop for finite bounds
// fn quad_core<F: FnMut(f64) -> f64>(mut f: F, a: f64, b: f64, epsrel: f64) -> (f64, f64) {
//     let max_intervals = 500;
//     let epsabs = 1e-14;

//     let mut heap = BinaryHeap::with_capacity(max_intervals);
//     let initial_interval = evaluate_interval(&mut f, a, b);
    
//     let mut total_integral = initial_interval.integral;
//     let mut total_error = initial_interval.error;
    
//     heap.push(initial_interval);

//     while total_error > (epsrel * total_integral.abs()).max(epsabs) && heap.len() < max_intervals {
//         let worst = heap.pop().unwrap();
//         let c = (worst.a + worst.b) / 2.0;
        
//         let left = evaluate_interval(&mut f, worst.a, c);
//         let right = evaluate_interval(&mut f, c, worst.b);
        
//         total_integral += left.integral + right.integral - worst.integral;
//         total_error += left.error + right.error - worst.error;
        
//         heap.push(left);
//         heap.push(right);
//     }

//     if total_error > (epsrel * total_integral.abs()).max(epsabs) {
//         eprintln!(
//             "IntegrationWarning: The maximum number of subdivisions ({}) has been achieved.",
//             max_intervals
//         );
//     }

//     (total_integral, total_error)
// }

// /// 1D Adaptive Gauss-Kronrod Quadrature with support for infinite bounds.
// pub fn quad<F: FnMut(f64) -> f64>(mut f: F, a: f64, b: f64, epsrel: f64) -> (f64, f64) {
//     // Map infinite bounds to finite ones using variable substitution
//     if a == std::f64::NEG_INFINITY && b == std::f64::INFINITY {
//         let mut mapped_f = |t: f64| {
//             let t2 = t * t;
//             let den = 1.0 - t2;
//             let x = t / den;
//             let dx_dt = (1.0 + t2) / (den * den);
//             f(x) * dx_dt
//         };
//         quad_core(&mut mapped_f, -1.0, 1.0, epsrel)

//     } else if a.is_finite() && b == std::f64::INFINITY {
//         let mut mapped_f = |t: f64| {
//             let x = a + (1.0 - t) / t;
//             let dx_dt = 1.0 / (t * t);
//             f(x) * dx_dt
//         };
//         quad_core(&mut mapped_f, 0.0, 1.0, epsrel)

//     } else if a == std::f64::NEG_INFINITY && b.is_finite() {
//         let mut mapped_f = |t: f64| {
//             let x = b - (1.0 - t) / t;
//             let dx_dt = 1.0 / (t * t);
//             f(x) * dx_dt
//         };
//         quad_core(&mut mapped_f, 0.0, 1.0, epsrel)

//     } else {
//         quad_core(&mut f, a, b, epsrel)
//     }
// }

// /// Recursive helper for N-dimensional integration.
// fn nquad_recursive<F>(
//     f: &F,
//     bounds: &[Bound],
//     current_args: &mut Vec<f64>,
//     epsrel: f64,
// ) -> (f64, f64)
// where
//     F: Fn(&[f64]) -> f64,
// {
//     if bounds.is_empty() {
//         return (f(current_args), 0.0);
//     }

//     // Resolve bounds dynamically based on currently populated arguments
//     let (a, b) = match &bounds[0] {
//         Bound::Fixed(a, b) => (*a, *b),
//         Bound::Dynamic(func) => func(current_args),
//     };

//     let remaining_bounds = &bounds[1..];

//     let mut integrand_1d = |x: f64| -> f64 {
//         current_args.push(x);
//         let (val, _err) = nquad_recursive(f, remaining_bounds, current_args, epsrel);
//         current_args.pop();
//         val
//     };

//     quad(&mut integrand_1d, a, b, epsrel)
// }

// /// N-Dimensional Adaptive Gauss-Kronrod Quadrature.
// pub fn nquad<F>(f: F, bounds: &[Bound], epsrel: f64) -> (f64, f64)
// where
//     F: Fn(&[f64]) -> f64,
// {
//     let mut args = Vec::with_capacity(bounds.len());
//     nquad_recursive(&f, bounds, &mut args, epsrel)
// }

// fn main() {
//     let target_accuracy = 1e-8;

//     println!("--- 1D Infinite Bound Test ---");
//     // Integral of e^-x from 0 to Infinity = 1.0
//     let (v1, e1) = quad(|x| (-x).exp(), 0.0, std::f64::INFINITY, target_accuracy);
//     println!("e^-x over [0, ∞]");
//     println!("Expected: 1.0");
//     println!("Result:   {:.10} (Error: {:.1e})\n", v1, e1);

//     println!("--- 2D Functional Bound Test ---");
//     // Area of a circle with radius 1: 
//     // Integrate 1 dy dx where x in [-1, 1] and y in [-sqrt(1-x^2), sqrt(1-x^2)]
//     let bounds_2d = vec![
//         Bound::Fixed(-1.0, 1.0), // Outer bound (x)
//         Bound::Dynamic(Box::new(|args: &[f64]| { // Inner bound (y) depends on x
//             let x = args[0];
//             let y_bound = (1.0 - x * x).sqrt();
//             (-y_bound, y_bound)
//         })),
//     ];
//     let func_2d = |_args: &[f64]| 1.0;
    
//     let (v2, e2) = nquad(func_2d, &bounds_2d, target_accuracy);
//     println!("Double integral area of unit circle");
//     println!("Expected: {:.10} (π)", std::f64::consts::PI);
//     println!("Result:   {:.10} (Error: {:.1e})", v2, e2);
// }

use std::cmp::Ordering;
use std::collections::BinaryHeap;

// Gauss-Kronrod 7/15 nodes and weights on [-1, 1]
const GK_NODES: [f64; 8] = [
    0.0000000000000000,
    0.2077849550078985,
    0.4058451513773972,
    0.5860872354676911,
    0.7415311855993944,
    0.8648644233597691,
    0.9491079123427585,
    0.9914553711208126,
];

const K15_WEIGHTS: [f64; 8] = [
    0.2094821410847278,
    0.2044329400752989,
    0.1903505780647854,
    0.1690047266392679,
    0.1406532597155259,
    0.1047900103222502,
    0.06309209262997855,
    0.02293532201052922,
];

const G7_WEIGHTS: [f64; 4] = [
    0.4179591836734694,
    0.3818300505051189,
    0.2797053914892767,
    0.1294849661688697,
];

#[derive(Clone, Copy, Debug)]
struct QuadResult {
    value: f64,
    error: f64,
}

#[derive(Clone, Copy, Debug)]
struct Interval {
    a: f64,
    b: f64,
    integral: f64,
    error: f64,
    abs_integral: f64,
}

impl PartialEq for Interval {
    fn eq(&self, other: &Self) -> bool {
        self.error == other.error
    }
}
impl Eq for Interval {}

impl PartialOrd for Interval {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        match (self.error.is_nan(), other.error.is_nan()) {
            (true, true) => Some(Ordering::Equal),
            (true, false) => Some(Ordering::Greater),
            (false, true) => Some(Ordering::Less),
            (false, false) => self.error.partial_cmp(&other.error),
        }
    }
}

impl Ord for Interval {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Equal)
    }
}

/// Allows bounds to either be fixed numbers or functions of previous arguments.
pub enum Bound<'a> {
    Fixed(f64, f64),
    Dynamic(Box<dyn Fn(&[f64]) -> (f64, f64) + 'a>),
}

/// Evaluate one interval with GK 7/15.
/// Returns:
/// - Kronrod integral estimate
/// - local error estimate
/// - local estimate of integral of |f|
fn evaluate_interval<F>(f: &mut F, a: f64, b: f64) -> Interval
where
    F: FnMut(f64) -> f64,
{
    let half_length = 0.5 * (b - a);
    let center = 0.5 * (a + b);

    let fc = f(center);

    let mut integral_k15 = fc * K15_WEIGHTS[0];
    let mut integral_g7 = fc * G7_WEIGHTS[0];
    let mut abs_integral = fc.abs() * K15_WEIGHTS[0];

    for i in 1..8 {
        let x = half_length * GK_NODES[i];
        let fp = f(center + x);
        let fm = f(center - x);

        integral_k15 += (fp + fm) * K15_WEIGHTS[i];
        abs_integral += (fp.abs() + fm.abs()) * K15_WEIGHTS[i];

        if i % 2 == 0 {
            integral_g7 += (fp + fm) * G7_WEIGHTS[i / 2];
        }
    }

    integral_k15 *= half_length;
    integral_g7 *= half_length;
    abs_integral *= half_length;

    let raw_error = (integral_k15 - integral_g7).abs();

    // Small roundoff floor based on local scale.
    let roundoff_floor = 50.0 * f64::EPSILON * abs_integral;

    Interval {
        a,
        b,
        integral: integral_k15,
        error: raw_error.max(roundoff_floor),
        abs_integral,
    }
}

fn quad_core<F>(mut f: F, a: f64, b: f64, epsrel: f64) -> QuadResult
where
    F: FnMut(f64) -> f64,
{
    let max_intervals = 500usize;
    let epsabs = 1e-14;

    if !a.is_finite() || !b.is_finite() {
        eprintln!("IntegrationWarning: non-finite bounds are not supported.");
        return QuadResult {
            value: f64::NAN,
            error: f64::NAN,
        };
    }

    if epsrel <= 0.0 || !epsrel.is_finite() {
        eprintln!("IntegrationWarning: epsrel must be positive and finite.");
        return QuadResult {
            value: f64::NAN,
            error: f64::NAN,
        };
    }

    if a == b {
        return QuadResult { value: 0.0, error: 0.0 };
    }

    let sign = if a < b { 1.0 } else { -1.0 };
    let (left, right) = if a < b { (a, b) } else { (b, a) };

    let mut heap = BinaryHeap::with_capacity(max_intervals);
    let initial = evaluate_interval(&mut f, left, right);

    let mut total_integral = initial.integral;
    let mut total_error = initial.error;

    heap.push(initial);

    while total_error > (epsrel * total_integral.abs()).max(epsabs) && heap.len() < max_intervals {
        let worst = heap.pop().unwrap();
        let c = 0.5 * (worst.a + worst.b);

        let left_iv = evaluate_interval(&mut f, worst.a, c);
        let right_iv = evaluate_interval(&mut f, c, worst.b);

        total_integral += left_iv.integral + right_iv.integral - worst.integral;
        total_error += left_iv.error + right_iv.error - worst.error;

        heap.push(left_iv);
        heap.push(right_iv);
    }

    if total_error > (epsrel * total_integral.abs()).max(epsabs) {
        eprintln!(
            "IntegrationWarning: maximum number of subintervals ({}) reached before target precision was achieved.",
            max_intervals
        );
    }

    QuadResult {
        value: sign * total_integral,
        error: total_error,
    }
}

/// 1D adaptive Gauss-Kronrod quadrature on finite intervals.
pub fn quad<F>(f: F, a: f64, b: f64, epsrel: f64) -> (f64, f64)
where
    F: FnMut(f64) -> f64,
{
    let res = quad_core(f, a, b, epsrel);
    (res.value, res.error)
}

/// Recursively computes value and propagated error for iterated integrals.
fn nquad_recursive<F>(
    f: &F,
    bounds: &[Bound],
    current_args: &mut Vec<f64>,
    epsrel: f64,
) -> QuadResult
where
    F: Fn(&[f64]) -> f64,
{
    if bounds.is_empty() {
        return QuadResult {
            value: f(current_args),
            error: 0.0,
        };
    }

    let (a, b) = match &bounds[0] {
        Bound::Fixed(a, b) => (*a, *b),
        Bound::Dynamic(func) => func(current_args),
    };

    let remaining = &bounds[1..];

    // Cache the inner value/error for the current x so that the paired
    // outer quadratures see consistent information at each sample point.
    let mut cache_x: Option<f64> = None;
    let mut cache_res = QuadResult { value: 0.0, error: 0.0 };

    let mut eval_inner = |x: f64| -> QuadResult {
        if let Some(xc) = cache_x {
            if x == xc {
                return cache_res;
            }
        }

        current_args.push(x);
        let res = nquad_recursive(f, remaining, current_args, epsrel);
        current_args.pop();

        cache_x = Some(x);
        cache_res = res;
        res
    };

    // Outer integral of the inner values.
    let value_res = quad_core(
        |x| eval_inner(x).value,
        a,
        b,
        epsrel,
    );

    // Outer integral of the inner error estimates.
    let propagated_inner_err = quad_core(
        |x| eval_inner(x).error,
        a,
        b,
        epsrel,
    );

    QuadResult {
        value: value_res.value,
        error: value_res.error + propagated_inner_err.value.abs() + propagated_inner_err.error,
    }
}

/// N-dimensional adaptive iterated Gauss-Kronrod quadrature.
pub fn nquad<F>(f: F, bounds: &[Bound], epsrel: f64) -> (f64, f64)
where
    F: Fn(&[f64]) -> f64,
{
    let mut args = Vec::with_capacity(bounds.len());
    let res = nquad_recursive(&f, bounds, &mut args, epsrel);
    (res.value, res.error)
}
