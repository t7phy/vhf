use polylog::Li2;
use pyo3::prelude::*;

/// Here are defined the rust functions wrapped in pyO3
#[pyfunction]
fn hr1(a: u16, x: f64) -> PyResult<f64> {
    let result: f64 = match a {
        0 => x.ln(),
        1 => (-(1.0 - x)).ln(),
        2 => (1.0 + x).ln(),
        _ => unimplemented!("Option not valid for a={a}."),
    };
    Ok(result)
}

#[pyfunction]
fn hr2(a: u16, b: u16, x: f64) -> PyResult<f64> {
    let array: [u16; 2] = [a, b];
    let result: f64 = match array {
        [0, 0] => (x.ln()).powi(2) / 2.0,
        [0, 1] => x.li2(),
        [1, 0] => (-x).ln() * (1.0 - x).ln() - x.li2(),
        [1, 1] => ((1.0 - x).ln()).powi(2) / 2.0,
        [2, 0] => x.ln() * (1.0 + x).ln() + (-x).li2(),
        _ => unimplemented!("Option not valid for a={a} and b={b}."),
    };
    Ok(result)
}

/// Here is the construction of the module
#[pymodule]
fn vhf_py(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hr1, m)?)?;
    m.add_function(wrap_pyfunction!(hr2, m)?)?;
    Ok(())
}
