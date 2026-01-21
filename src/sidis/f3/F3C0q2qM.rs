use crate::sidis::internal::*;

pub fn DL_DL_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = 1.0;
    return res;
}
pub fn get_sv_map() -> HashMap<&'static str, Vec<&'static str>> {
    let mut m = HashMap::new();
    m.insert("000", vec!["DL_DL"]);
    m
}