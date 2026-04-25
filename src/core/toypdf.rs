// 1. The Interface
pub trait PDF {
    fn xfxq(&self, pid: i32, x: f64, q: f64) -> f64;
    fn alphasq(&self, q: f64) -> f64;
}
// 2. The Factory
// We still return Box<dyn PDF> because we need a "Fat Pointer"
// that carries the Vtable (the list of functions to run).
pub fn mk_pdf(name: &str) -> Box<dyn PDF> {
    match name {
        "ToyPDF1" => Box::new(ToyPDF1),
        "ToyPDF2" => Box::new(ToyPDF2),
        "ToyPDF3" => Box::new(ToyPDF3),
        _ => panic!("PDF set '{}' not found", name),
    }
}
// ==========================================
// Internal Models (All Empty)
// ==========================================
// Model 1: Recursive Logic
struct ToyPDF1; 
impl PDF for ToyPDF1 {
    fn xfxq(&self, pid: i32, x: f64, q: f64) -> f64 {
        if x <= 0.0 || x >= 1.0 { return 0.0; }
        match pid {
            3 | -3 => 0.2 * (self.xfxq(-1, x, q) + self.xfxq(-2, x, q)),
            -2 => self.xfxq(-1, x, q) * (1.0 - x),
            -1 => 0.1939875 * x.powf(-0.1) * (1.0 - x).powi(6),
            0 | 21 => 1.7 * x.powf(-0.1) * (1.0 - x).powi(5),
            1 => 3.064320 * x.powf(0.8) * (1.0 - x).powi(4) + self.xfxq(-1, x, q),
            2 => 5.107200 * x.powf(0.8) * (1.0 - x).powi(3) + self.xfxq(-2, x, q),
            _ => panic!("PID {} not implemented", pid),
        }
    }
    fn alphasq(&self, _q: f64) -> f64 { 0.118 }
}
// Model 2: Simple Shape
struct ToyPDF2;
impl PDF for ToyPDF2 {
    fn xfxq(&self, pid: i32, x: f64, _q: f64) -> f64 {
        if x <= 0.0 || x >= 1.0 { return 0.0; }
        match pid {
            0 | 21 => 2.0 * x.powf(-0.5) * (1.0 - x).powi(4), 
            _ => panic!("PID {} not implemented", pid),
        }
    }
    fn alphasq(&self, q: f64) -> f64 { 
        if q > 1.0 { 1.0 / q.ln() } else { 1.0 }
    } 
}
// Model 3: Hardcoded Norm (No internal state needed)
struct ToyPDF3;
impl PDF for ToyPDF3 {
    fn xfxq(&self, pid: i32, x: f64, _q: f64) -> f64 {
        let norm = 5.0; // Hardcoded inside the function instead of the struct
        match pid {
            0 | 21 => norm * x * (1.0 - x),
            _ => panic!("PID {} not implemented", pid),
        }
    }
    fn alphasq(&self, _q: f64) -> f64 { 0.118 }
}
