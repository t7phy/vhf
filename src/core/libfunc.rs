#![allow(non_snake_case)]

/// Natural logarithm ln(x)
pub fn ln(x: f64) -> f64 {
    x.ln()
}

pub fn log(x: f64) -> f64 {
    x.ln()
}

/// The integral of arctan(x), which is x*arctan(x) - 0.5*ln(1 + x^2)
pub fn InvTanInt(x: f64) -> f64 {
    // Rust allows simple math to look very clean
    x * x.atan() - 0.5 * (1.0 + x * x).ln()
}

/// Arctangent atan(x)
pub fn ArcTan(x: f64) -> f64 {
    x.atan()
}

pub trait Power<Exponent> {
    fn pow(base: f64, exp: Exponent) -> f64;
}

// Case 1: y is an i32 (Integer)
impl Power<i32> for f64 {
    fn pow(base: f64, exp: i32) -> f64 {
        base.powi(exp) // Uses Rust's optimized integer power
    }
}

// Case 2: y is an f64 (Float)
impl Power<f64> for f64 {
    fn pow(base: f64, exp: f64) -> f64 {
        base.powf(exp) // Uses Rust's float power
    }
}

// The generic wrapper function
pub fn pow<T>(x: f64, y: T) -> f64 
where 
    f64: Power<T> 
{
    <f64 as Power<T>>::pow(x, y)
}