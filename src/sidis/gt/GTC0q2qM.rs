use crate::sidis::internal::*;

fn DL_DL_000(x: f64, z: f64, NF: f64) -> f64 {
    let res: f64 = -1. / 2.;
    return res;
}

mkcoeff!(
    ("000", [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, DL_DL_000])
);

/*
  SV mapping:
  - 000: DL_DL
*/
