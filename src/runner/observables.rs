#![allow(non_camel_case_types)]

pub enum DISObservable {
    F2,
    HERARED,
    xF3
}

pub enum pDISObservable {
    g1
}

pub enum SIAObservable {
    F2
}

pub enum SIDISObservable {
    F2,
}

pub enum pSIDISObservable {
    g1,
}

pub enum ProcessObservable {
    DIS_NC(DISObservable),
    DIS_CC(DISObservable),
    pDIS_NC(pDISObservable),
    pDIS_CC(pDISObservable),
    SIA(SIAObservable),
    SIDIS_NC(SIDISObservable),
    SIDIS_CC(SIDISObservable),
    pSIDIS_NC(pSIDISObservable),
    pSIDIS_CC(pSIDISObservable)
}


pub struct Observable {
    pub process: ProcessObservable,
    pub coeffs: Vec<Vec<(String, String)>> // (coefficient function, multiplicative factor function)
}

// let dis_nc_f2 = Observable {

// }




