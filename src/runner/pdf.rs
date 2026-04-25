// use neopdf::pdf::PDF;

// pub fn mk_pdf(pdf_name: &str, member: usize) -> PDF {
//     PDF::load(pdf_name, member)
// }

// pub fn xfxq(pdf: &PDF, pid: i32, x: f64, q: f64) -> f64 {
//     pdf.xfxq2(pid, &[x, q.powi(2)])
// }

// pub fn alphas_q(pdf: &PDF, q: f64) -> f64 {
//     pdf.alphas_q2(q.powi(2))
// }

use neopdf::pdf::PDF;

pub struct InitPDF {
    mypdf: PDF,
}

impl InitPDF {
    /// Constructor to initialize the wrapper
    pub fn name_mem(pdf_name: &str, member: usize) -> Self {
        Self {
            mypdf: PDF::load(pdf_name, member),
        }
    }

    pub fn name(pdf_name: &str) -> Self {
        Self {
            mypdf: PDF::load(pdf_name, 0),
        }
    }

    /// Access xfxq without passing the pdf manually
    pub fn xfxq(&self, pid: i32, x: f64, q: f64) -> f64 {
        self.mypdf.xfxq2(pid, &[x, q.powi(2)])
    }

    pub fn fxq(&self, pid: i32, x: f64, q: f64) -> f64 {
        self.mypdf.xfxq2(pid, &[x, q.powi(2)]) / x
    }

    /// Access alphas_q without passing the pdf manually
    pub fn alphas_q(&self, q: f64) -> f64 {
        self.mypdf.alphas_q2(q.powi(2))
    }
}
