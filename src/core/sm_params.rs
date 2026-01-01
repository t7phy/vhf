use serde::Deserialize;
use std::path::{Path, PathBuf};
use std::sync::OnceLock;

/// The structure containing all physical parameters.
/// We use #[serde(default)] so if a user YAML is missing a key, 
/// it pulls that specific key from the PDG defaults.
#[derive(Deserialize, Debug, Clone)]
#[serde(default)]
pub struct Parameters {
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
    pub m_kaon: f64,
    pub m_proton: f64,
    pub gamma_w: f64,
    pub gamma_z: f64,
    pub alpha_s_at_mz: f64,
    pub alpha_em_at_mz: f64,
}

/// Hard-coded PDG Defaults
impl Default for Parameters {
    fn default() -> Self {
        Self {
            m_up: 0.00216,
            m_down: 0.00467,
            m_strange: 0.093,
            m_charm: 1.27,
            m_bottom: 4.18,
            m_top: 172.69,
            m_w: 80.377,
            m_z: 91.1876,
            m_h: 125.25,
            m_pion: 0.13957,
            m_kaon: 0.49367,
            m_proton: 0.93827,
            gamma_w: 2.085,
            gamma_z: 2.4952,
            alpha_s_at_mz: 0.1179,
            alpha_em_at_mz: 0.007755, // ~1/128.9
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

pub fn m_up() -> f64      { get().m_up }
pub fn m_down() -> f64    { get().m_down }
pub fn m_strange() -> f64 { get().m_strange }
pub fn m_charm() -> f64   { get().m_charm }
pub fn m_bottom() -> f64  { get().m_bottom }
pub fn m_top() -> f64     { get().m_top }
pub fn m_w() -> f64       { get().m_w }
pub fn m_z() -> f64       { get().m_z }
pub fn m_h() -> f64       { get().m_h }
pub fn gamma_w() -> f64   { get().gamma_w }
pub fn gamma_z() -> f64   { get().gamma_z }
pub fn alpha_s() -> f64   { get().alpha_s_at_mz }
pub fn alpha_em() -> f64  { get().alpha_em_at_mz }