#![allow(non_snake_case)]

use serde::{Deserialize, Serialize};
use std::path::{Path, PathBuf};
use std::sync::OnceLock;

/// The structure containing all physical parameters.
/// We use #[serde(default)] so if a user YAML is missing a key, 
/// it pulls that specific key from the PDG defaults.
#[derive(Serialize, Deserialize, Debug, Clone)]
#[serde(default)]
pub struct Parameters {
    pub m_electron: f64,
    pub m_muon: f64,
    pub m_tau: f64,
    pub m_up: f64,
    pub m_down: f64,
    pub m_strange: f64,
    pub m_charm: f64,
    pub m_bottom: f64,
    pub m_top: f64,
    pub m_w: f64,
    pub m_z: f64,
    pub m_h: f64,
    pub m_pion: f64,
    pub m_pion0: f64,
    pub m_kaon: f64,
    pub m_kaon0: f64,
    pub m_proton: f64,
    pub m_neutron: f64,
    pub m_deuteron: f64,
    pub gamma_w: f64,
    pub gamma_z: f64,
    pub alpha_s_at_mz: f64,
    pub alpha_em_at_0: f64,
    pub G_F: f64,
    pub sin2_theta_w_at_mz: f64,
    pub ckm_ud: f64,
    pub ckm_us: f64,
    pub ckm_ub: f64,
    pub ckm_cd: f64,
    pub ckm_cs: f64,
    pub ckm_cb: f64,
    pub ckm_td: f64,
    pub ckm_ts: f64,
    pub ckm_tb: f64,
    // pub ckm_matrix: [[f64; 3]; 3],
}

/// Hard-coded PDG Defaults
impl Default for Parameters {
    fn default() -> Self {
        Self {
            m_electron: 0.00051099895,
            m_muon: 0.1056583755,
            m_tau: 1.77693,
            m_up: 0.00216,
            m_down: 0.00470,
            m_strange: 0.0935,
            m_charm: 1.2730,
            m_bottom: 4.183,
            m_top: 172.52,
            m_w: 80.3692,
            m_z: 91.1880,
            m_h: 125.20,
            m_pion: 0.13957039,
            m_pion0: 0.1349768,
            m_kaon: 0.493677,
            m_kaon0: 0.497611,
            m_proton: 0.93827208816,
            m_neutron: 0.9395654205,
            m_deuteron: 1.875612945,
            gamma_w: 2.14,
            gamma_z: 2.4955,
            alpha_s_at_mz: 0.1180,
            alpha_em_at_0: 0.0072973525643,
            G_F: 1.1663785,
            sin2_theta_w_at_mz: 0.23122,
            ckm_ud: 0.97367,
            ckm_us: 0.22431,
            ckm_ub: 0.00382,
            ckm_cd: 0.221,
            ckm_cs: 0.975,
            ckm_cb: 0.0411,
            ckm_td: 0.0086,
            ckm_ts: 0.0415,
            ckm_tb: 1.010,
            // ckm_matrix: [
            //     [ckm_ud, ckm_us, ckm_ub],
            //     [ckm_cd, ckm_cs, ckm_cb],
            //     [ckm_td, ckm_ts, ckm_tb],
            // ]
        }
    }
}

/// The Global Singleton Storage
static INSTANCE: OnceLock<Parameters> = OnceLock::new();

/// PUBLIC API: Initialize with a specific directory (called by CLI 'run')
pub fn init(custom_path: Option<&Path>) {
    let params = load_from_disk(custom_path);
    // If someone calls init twice, the second call is ignored to maintain safety.
    let _ = INSTANCE.set(params);
}

/// INTERNAL: The Cascading Discovery Logic
fn load_from_disk(search_dir: Option<&Path>) -> Parameters {
    let mut config_path = match search_dir {
        Some(p) => p.to_path_buf(),
        None => PathBuf::from("."), // Default to current working directory
    };
    config_path.push("sm_parameters.yaml");

    // Workflow: Read File -> Parse YAML -> Fallback to Default if any step fails
    std::fs::read_to_string(&config_path)
        .ok()
        .and_then(|contents| serde_yaml::from_str::<Parameters>(&contents).ok())
        .unwrap_or_else(|| {
            // Optional: You could use a logging crate here to print a warning
            // that the file was not found and defaults are being used.
            Parameters::default()
        })
}

/// INTERNAL: Accessor for the singleton
fn get() -> &'static Parameters {
    INSTANCE.get_or_init(|| load_from_disk(None))
}

// --- PUBLIC MATH ACCESSORS ---
// These allow your physics modules to use the parameters 
// without needing any function arguments.

pub fn m_electron() -> f64 { get().m_electron }
pub fn m_muon() -> f64    { get().m_muon }
pub fn m_tau() -> f64     { get().m_tau }
pub fn m_up() -> f64      { get().m_up }
pub fn m_down() -> f64    { get().m_down }
pub fn m_strange() -> f64 { get().m_strange }
pub fn m_charm() -> f64   { get().m_charm }
pub fn m_bottom() -> f64  { get().m_bottom }
pub fn m_top() -> f64     { get().m_top }
pub fn m_w() -> f64       { get().m_w }
pub fn m_z() -> f64       { get().m_z }
pub fn m_h() -> f64       { get().m_h }
pub fn m_pion() -> f64    { get().m_pion }
pub fn m_pion0() -> f64   { get().m_pion0 }
pub fn m_kaon() -> f64    { get().m_kaon }
pub fn m_kaon0() -> f64   { get().m_kaon0 }
pub fn m_proton() -> f64  { get().m_proton }
pub fn m_neutron() -> f64 { get().m_neutron }
pub fn m_deuteron() -> f64 { get().m_deuteron }
pub fn gamma_w() -> f64   { get().gamma_w }
pub fn gamma_z() -> f64   { get().gamma_z }
pub fn alpha_s() -> f64   { get().alpha_s_at_mz }
pub fn alpha_em() -> f64  { get().alpha_em_at_0 }
pub fn G_F() -> f64       { get().G_F }
pub fn sin2_theta_w() -> f64 { get().sin2_theta_w_at_mz }
pub fn ckm_ud() -> f64    { get().ckm_ud }
pub fn ckm_us() -> f64    { get().ckm_us }
pub fn ckm_ub() -> f64    { get().ckm_ub }
pub fn ckm_cd() -> f64    { get().ckm_cd }
pub fn ckm_cs() -> f64    { get().ckm_cs }
pub fn ckm_cb() -> f64    { get().ckm_cb }
pub fn ckm_td() -> f64    { get().ckm_td }
pub fn ckm_ts() -> f64    { get().ckm_ts }
pub fn ckm_tb() -> f64    { get().ckm_tb }
// pub fn ckm_matrix() -> [[f64; 3]; 3] { get().ckm_matrix }