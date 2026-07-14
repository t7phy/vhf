#![allow(non_camel_case_types)]
use rayon::vec;
// --------------------------------------------|
use serde::Deserialize;
use std::fs;
use std::os::linux::raw;
use std::path::Path;
// use std::io::{Result, Error, Write};
use std::io::{self};
use crate::core::sm_params;
use std::path::PathBuf;
// --------------------------------------------|
use crate::dis::internal::CoeffFuncs as Cf1D;
use crate::sidis::internal::CoeffFuncs as Cf2D;
use crate::dis::{dis_factor_none, f2_light};
use crate::core::conv1d::Conv1DPointGrid;
use crate::core::interpolation::lambertgrid;
use crate::runner::handle_json::{append_partonic_subgrid, write_channel_subgrid, ChannelEntry};
// --------------------------------------------|
// --------------------------------------------|

/* -----------------------------------------------------------\
|                                                             |
|               Step 1: Process the runcard                   |
|                                                             |
\----------------------------------------------------------- */

#[derive(Debug, Deserialize)]
pub struct RuncardConfig {
    pub output_type: OutputType,
    pub run_name: String,
    pub process: Process,
    pub fns: FNS,
    pub qcd_perturbative_order: u8,
    pub scale_variations: bool,
    pub unit_prefix: String,
    pub bins: Bin,
}

impl RuncardConfig {
    pub fn load(path: &str) -> Result<Self, Box<dyn std::error::Error>> {
        let yaml_str = std::fs::read_to_string(path)?;
        let config: RuncardConfig = serde_yaml::from_str(&yaml_str)?;

        config.bins.check_consistency(&config.process)?;

        println!("Runcard loaded and validated");

        Ok(config)
    }

    pub fn setup_subgrids(&self) -> std::io::Result<()> {
        let num_bins = self.num_bins();
        let num_orders = self.num_orders();
        let num_cfs = self.total_cfs();

        let num_channels = self.process.num_partonic_channels();

        // --- Create partonic_subgrids ---
        let partonic_dir_path = Path::new(PARTONIC_DIR);
        if !partonic_dir_path.exists() {
            fs::create_dir(partonic_dir_path)?;
        }
    
        // Create all partonic files
        for b in 0..num_bins {
            for o in 0..num_orders {
                for c in 0..num_channels {
                    let file_path = partonic_subgrid_path(b, o, c);
                    if !file_path.exists() {
                        fs::File::create(file_path)?;
                    }
                }
            }
        }

        // --- Create channel_subgrids ---
        let channel_dir_path = Path::new(CHANNEL_DIR);
        if !channel_dir_path.exists() {
            fs::create_dir(channel_dir_path)?;
        }

        // Create all channel files
        for b in 0..num_bins {
            for ch in 0..num_cfs {
                let file_path = channel_subgrid_path(b, ch);
                if !file_path.exists() {
                    fs::File::create(file_path)?;
                }
            }
        }
    
        Ok(())
    }
    
    pub fn create_joblist(&self) -> usize {
        let total_jobs = self.num_bins() * self.total_cfs();

        let content: String = (0..total_jobs)
            .map(|i| format!("vhf run {}", i))
            .collect::<Vec<_>>()
            .join("\n");

        if let Err(e) = std::fs::write("joblist", content) {
            eprintln!("Couldn't write joblist file: {}", e);
        }

        total_jobs
    }

    pub fn prepare(path: &str) -> Result<Self, Box<dyn std::error::Error>> {

        let config = Self::load(path)?;

        // 3. Generate SM Parameters (Safe: won't overwrite existing)
        generate_sm_card()?;

        // 4. Create the Joblist File
        let total_jobs = config.create_joblist();
        println!("Created 'joblist' with {} total jobs.", total_jobs);

        // 5. Initialize Subgrids Directory and Files
        config.setup_subgrids()?;
        println!("Subgrids initialized.");

        println!("Preparation successful.");
        
        // Return the config instance so the caller can still use its data
        Ok(config)
    }

    pub fn num_bins(&self) -> usize {
        self.bins.data.len()
    }

    pub fn num_orders(&self) -> usize {
        self.qcd_perturbative_order as usize + 1
    }

    pub fn total_cfs(&self) -> usize {
        let max_order = self.num_orders();
        match obtain_cfs(&self.process) {
            CFsVec::Cf1D(v) => v.iter().take(max_order).map(|inner| inner.len()).sum(),
            CFsVec::Cf2D(v) => v.iter().take(max_order).map(|inner| inner.len()).sum(),
        }
    }
}

pub const PARTONIC_DIR: &str = "partonic_subgrids";
pub const CHANNEL_DIR: &str = "channel_subgrids";

pub fn channel_subgrid_path(bin: usize, cf: usize) -> PathBuf {
    Path::new(CHANNEL_DIR).join(format!("{}_{}.json", bin, cf))
}

pub fn partonic_subgrid_path(bin: usize, order: usize, channel: usize) -> PathBuf {
    Path::new(PARTONIC_DIR).join(format!("{}_{}_{}.json", bin, order, channel))
}

#[derive(Debug, Deserialize)]
pub enum OutputType {
    InterpolationGrid,
    TheoryPrediction(String, usize)
}

// TODO: move observables from String to enum
// #[derive(Debug, Deserialize, PartialEq)]
// pub enum Observable {
//     F2,
//     FL,
//     XF3,
// }

#[derive(Debug, Deserialize)]
#[serde(tag = "process_type")]
pub enum Process {
    DIS_NC {
        observable: String, // e.g. "F2", "HERARED", "xF3"
        lepton: i32, // PDG pid
        hadron: i32, // PDG pid
        electroweak_interaction_type: ElectroweakInteractionType, // em, nc
    },
    DIS_CC {
        observable: String, // e.g. "F2", "HERARED", "xF3"
        lepton: i32, // PDG pid
        hadron: i32, // PDG pid
    },
    pDIS_NC {
        observable: String,
        lepton: i32, 
        hadron: i32,
    },
    pDIS_CC {
        observable: String,
        lepton: i32, 
        hadron: i32,
    }, 
    SIA {
        observable: String, // e.g. "F2", 
        lepton1: i32, // PDG pid
        lepton2: i32, // PDG pid
        hadron: i32, // PDG pid
        kin_var: SiaKinVar,
        electroweak_interaction_type: ElectroweakInteractionType, // em, nc
    },
    SIDIS_NC {
        observable: String, // e.g. "F2"
        lepton: i32, // PDG pid
        hadron_in: i32, // PDG pid
        hadron_out: i32, // PDG pid
        electroweak_interaction_type: ElectroweakInteractionType, // em, nc
    },
    SIDIS_CC {
        observable: String, // e.g. "F2"
        lepton: i32, // PDG pid
        hadron_in: i32, // PDG pid
        hadron_out: i32, // PDG pid
    },
    pSIDIS_NC {
        observable: String, 
        lepton: i32, 
        hadron_in: i32,
        hadron_out: i32,
    }, 
    pSIDIS_CC {
        observable: String, 
        lepton: i32, 
        hadron_in: i32,
        hadron_out: i32,
    },
}

impl Process {
    pub fn num_partonic_channels(&self) -> usize {
        match self {
            Process::DIS_NC { .. } | Process::DIS_CC { .. } | Process::pDIS_NC { .. } | Process::pDIS_CC { .. } | Process::SIA { .. } => 14,
            Process::SIDIS_NC { .. } | Process::SIDIS_CC { .. } | Process::pSIDIS_NC { .. } | Process::pSIDIS_CC { .. } => 14 * 14,
        }
    }
}

#[derive(Debug, Deserialize)]
pub enum ElectroweakInteractionType {
    em,
    nc,
    cc
}

#[derive(Debug, Deserialize)]
pub enum SiaKinVar {
    z,
    xp,
    ph,
    xi
}

#[derive(Debug, Deserialize)]
pub enum FNS {
    ZMVFNS,
    FFNS(i8)
}

#[derive(Debug, Deserialize)]
#[serde(untagged)]
pub enum Binning {
    point { val: f64 },
    range { min: f64, max: f64 },
}

#[derive(Debug, Clone, Copy, Deserialize)]
pub enum BinningType {
    point,
    range,
}

#[derive(Debug, Deserialize)]
#[serde(untagged)]
pub enum KinVar {
    sidis { x: Binning, z: Binning, q: Binning },

    dis { x: Binning, q: Binning },
    
    sia_z { z: Binning, q: Binning },
    sia_xp { xp: Binning, q: Binning },
    sia_ph { ph: Binning, q: Binning },
    sia_xi { xi: Binning, q: Binning }
}

#[derive(Debug, Deserialize)]
pub struct Bin {
    xz_binning_type: BinningType,
    q_binning_type: BinningType,
    data: Vec<KinVar>    
}

impl Bin {
    /// Validates that the kinematic entries in 'data' match the physics Process 
    /// and follow the binning rules (point vs range) defined in the header.
    pub fn check_consistency(&self, process: &Process) -> Result<(), String> {
        for (i, entry) in self.data.iter().enumerate() {
            // 1. Validate Process Type vs Kinematic Structure
            match (process, entry) {
                // DIS: Must use dis {x, q}
                (Process::DIS_NC {..} | Process::DIS_CC {..} | Process::pDIS_NC {..} | Process::pDIS_CC {..}, KinVar::dis { .. }) => (),
                
                // SIDIS: Must use sidis {x, z, q}
                (Process::SIDIS_NC {..} | Process::SIDIS_CC {..} | Process::pSIDIS_NC {..} | Process::pSIDIS_CC {..}, KinVar::sidis { .. }) => (),
                
                // SIA: Must match the specific variant (z, xp, ph, xi) defined in the SIA config
                (Process::SIA { kin_var: k, .. }, _) => {
                    match (k, entry) {
                        (SiaKinVar::z,  KinVar::sia_z  { .. }) => (),
                        (SiaKinVar::xp, KinVar::sia_xp { .. }) => (),
                        (SiaKinVar::ph, KinVar::sia_ph { .. }) => (),
                        (SiaKinVar::xi, KinVar::sia_xi { .. }) => (),
                        (expected, _) => return Err(format!(
                            "Bin {} error: SIA process expects kin_var {:?}, but found different data structure", 
                            i, expected
                        )),
                    }
                }
                
                // Catch-all for mismatches (e.g., trying to use DIS bins for a SIDIS process)
                (p, e) => return Err(format!("Bin {} error: Process type {:?} is incompatible with entry structure {:?}", i, p, e)),
            }

            // 2. Validate Binning Consistency (Point vs Range)
            match entry {
                KinVar::dis { x, q } => {
                    self.check_single_binning(i, "x", &self.xz_binning_type, x)?;
                    self.check_single_binning(i, "q", &self.q_binning_type, q)?;
                },
                KinVar::sidis { x, z, q } => {
                    self.check_single_binning(i, "x", &self.xz_binning_type, x)?;
                    self.check_single_binning(i, "z", &self.xz_binning_type, z)?;
                    self.check_single_binning(i, "q", &self.q_binning_type, q)?;
                },
                KinVar::sia_z { z, q } => {
                    self.check_single_binning(i, "z", &self.xz_binning_type, z)?;
                    self.check_single_binning(i, "q", &self.q_binning_type, q)?;
                },
                KinVar::sia_xp { xp, q } => {
                    self.check_single_binning(i, "xp", &self.xz_binning_type, xp)?;
                    self.check_single_binning(i, "q", &self.q_binning_type, q)?;
                },
                KinVar::sia_ph { ph, q } => {
                    self.check_single_binning(i, "ph", &self.xz_binning_type, ph)?;
                    self.check_single_binning(i, "q", &self.q_binning_type, q)?;
                },
                KinVar::sia_xi { xi, q } => {
                    self.check_single_binning(i, "xi", &self.xz_binning_type, xi)?;
                    self.check_single_binning(i, "q", &self.q_binning_type, q)?;
                }
            }
        }
        Ok(())
    }

    /// Helper to verify a single variable matches the expected binning type
    fn check_single_binning(&self, index: usize, var: &str, expected: &BinningType, found: &Binning) -> Result<(), String> {
        match (expected, found) {
            (BinningType::point, Binning::point { .. }) => Ok(()),
            (BinningType::range, Binning::range { .. }) => Ok(()),
            (_exp, _) => Err(format!(
                "Bin {} error: Variable '{}' has incorrect binning type",
                index, var
            )),
        }
    }
}

pub fn generate_sm_card() -> io::Result<()> {
    let path = Path::new("sm_parameters.yaml");

    if path.exists() {
        println!("⚠️  sm_parameters.yaml already exists. Skipping generation.");
        return Ok(());
    }

    let defaults = sm_params::Parameters::default();
    let yaml_body = serde_yaml::to_string(&defaults)
        .map_err(|e| io::Error::new(io::ErrorKind::Other, e))?;

    // --- Define your Header ---
    let header = "# =========================================================\n\
                  # VIRTUAL HADRON FACTORY - Standard Model Parameters\n\
                  # Values are based on PDG 2024/2025 averages.\n\
                  # All masses and widths are in GeV.\n\
                  # Sin^2(theta_w) is the effective value at the M_Z scale.\n\
                  # =========================================================\n\n";

    // Combine header and the serialized data
    let full_content = format!("{}{}", header, yaml_body);

    // Write to disk
    fs::write(path, full_content)?;

    println!("A sm_parameters.yaml card with with default PDG values has been created. It can be edited to adopt custom values for SM parameters.");
    Ok(())
}


/* -----------------------------------------------------------\ 
|                                                             |
|              Step 2: Perform the computations               |
|                                                             |
\----------------------------------------------------------- */

fn pid_index(pid: i32) -> usize {
    match pid {
        21 => 0,
        1..=6 => pid as usize,
        -6..=-1 => (6 + (-pid)) as usize, // -1 -> 7 ... -6 -> 12
        22 => 13,
        _ => panic!("invalid pid: {}", pid),
    }
}

fn pid_pair_index(a: i32, b: i32) -> usize {
    let i = pid_index(a);
    let j = pid_index(b);
    let n = 14;

    i * n + j
}

pub struct JobInfo {
    pub config: RuncardConfig,
    pub bin_index: usize,
    pub perturbative_order: usize,
    pub cf_index_in_order: usize,
    pub flat_cf_index: usize, // ADDED
}

pub fn identify_job(index: usize) -> Result<JobInfo, Box<dyn std::error::Error>> {
    let config = RuncardConfig::load("runcard.yaml")?;
    let cfs_vec = obtain_cfs(&config.process);

    let max_order = config.num_orders();
    let cf_counts: Vec<usize> = match &cfs_vec {
        CFsVec::Cf1D(orders) => orders.iter().take(max_order).map(|v| v.len()).collect(),
        CFsVec::Cf2D(orders) => orders.iter().take(max_order).map(|v| v.len()).collect(),
    };

    let total_cfs_per_bin = config.total_cfs();
    let bin_index = index / total_cfs_per_bin;
    let flat_cf_index = index % total_cfs_per_bin;

    if bin_index >= config.num_bins() {
        return Err(format!("Index {} is out of range.", index).into());
    }

    let mut remainder = flat_cf_index;
    let mut target_order = 0;
    let mut target_inner_idx = 0;

    for (order_idx, &count) in cf_counts.iter().enumerate() {
        if remainder < count {
            target_order = order_idx;
            target_inner_idx = remainder;
            break;
        }
        remainder -= count;
    }

    Ok(JobInfo {
        config,
        bin_index,
        perturbative_order: target_order,
        cf_index_in_order: target_inner_idx,
        flat_cf_index, // PASS THIS ALONG
    })
}

pub fn compute_dis_nf(fns: FNS, q: &f64) -> f64 {
    let q = *q;
    let (fns, pid) = match fns {
        FNS::ZMVFNS => ("zmvfns", 0),
        FNS::FFNS(p) => ("ffns", p),
    };

    if fns == "zmvfns" {
        if q > sm_params::m_bottom() {5.0}
        else if q > sm_params::m_charm() {4.0}
        else {3.0}
    } else if fns == "ffns" {
        todo!()
    } else {
        5.0
    }
}

pub fn compute_dis_sg(config: &RuncardConfig, bin_index: usize, perturbative_order: usize, cf_index_in_order: usize) -> (Vec<Vec<f64>>, Vec<(usize, f64)>) {

    let sg: Vec<Vec<f64>>;
    let mut raw_couplings: Vec<(i8, f64)>;

    let bin_entry = &config.bins.data[bin_index];
    let itp_xgrid = lambertgrid(100, 1e-5, 1.0);
    let interaction_str = match &config.process {
        Process::DIS_NC { electroweak_interaction_type, .. } => format!("{:?}", electroweak_interaction_type).to_lowercase(),
        Process::DIS_CC { .. } | Process::pDIS_CC { .. } => "cc".to_string(),
        _ => unreachable!("Process type not supported for DIS subgrid computation"),
    };

    let cfs_enum = obtain_cfs(&config.process);
    let CFsVec::Cf1D(cf) = cfs_enum else { panic!("Expected Cf1D for DIS"); };

    let (x_bin, q_bin) = match bin_entry {
        KinVar::dis { x, q } => (x, q),
        _ => panic!("Expected DIS kinematic entry at bin index {}", bin_index),
    };

    match (config.bins.xz_binning_type, config.bins.q_binning_type) {
        (BinningType::point, BinningType::point) => {
            let Binning::point { val: x_val } = x_bin else { unreachable!() };
            let Binning::point { val: q_val } = q_bin else { unreachable!() };
            
            let fns_val = match &config.fns { FNS::ZMVFNS => FNS::ZMVFNS, FNS::FFNS(p) => FNS::FFNS(*p) };
            let nf = compute_dis_nf(fns_val, &q_val);
            
            let cf = &cf[perturbative_order][cf_index_in_order]; 
            
            let mut sg_vec = Conv1DPointGrid::new(*x_val, *q_val, nf, cf.0.clone(), cf.3, itp_xgrid, true).compute();
            
            for val in sg_vec.iter_mut() {
                *val *= cf.1;
            }

            sg = vec![sg_vec]; 

            
            // Fetch the raw couplings and convert them immediately to indices
            raw_couplings = (cf.2)(nf, *q_val, interaction_str);
            
        },
        (BinningType::point, BinningType::range) => {
            todo!()
        },
        (BinningType::range, BinningType::point) => {
            todo!()
        },
        (BinningType::range, BinningType::range) => {
            todo!()
        }
    }
    let couplings: Vec<(usize, f64)> = raw_couplings
        .into_iter()
        .map(|(pid, factor)| (pid_index(pid as i32), factor))
        .collect();
    (sg, couplings)
}

pub fn compute_sia_sg(config: &RuncardConfig, bin_index: usize, peturbative_order: usize, cf_index_in_order: usize) -> Vec<Vec<Vec<f64>>> {
    todo!()
}

pub fn compute_sidis_sg(config: &RuncardConfig, bin_index: usize, peturbative_order: usize, cf_index_in_order: usize) -> Vec<Vec<Vec<Vec<f64>>>> {
    todo!()
}

pub fn run(job_index: usize) -> Result<(), Box<dyn std::error::Error>> {
    // 1. Identify the job to get our indices and the parsed config
    let job_info = identify_job(job_index)?;
    
    let bin_index = job_info.bin_index;
    let order_index = job_info.perturbative_order;
    let cf_index = job_info.cf_index_in_order;
    let flat_cf_index = job_info.flat_cf_index;
    
    // We take ownership of config here so we can pass it to the compute functions
    let config = job_info.config; 

    // 2. Route the calculation based on the process type
    // We use matches! by reference so we don't accidentally move config.process 
    // before passing the full config to compute_dis_sg.
    if matches!(&config.process, Process::DIS_NC { .. } | Process::DIS_CC { .. } | Process::pDIS_NC { .. } | Process::pDIS_CC { .. }) {
        
        // Compute the 2D grid and extract couplings
        let (grid_2d, couplings) = compute_dis_sg(&config, bin_index, order_index, cf_index);
        
        // Compute shape
        let rows = grid_2d.len();
        let cols = if rows > 0 { grid_2d[0].len() } else { 0 };
        let shape = vec![rows, cols];
        
        // Flatten data for JSON entry
        let data: Vec<f64> = grid_2d.into_iter().flatten().collect();
        
        // Construct entry and write
        let channel_entry = ChannelEntry {
            data,
            shape,
            couplings,
            order: order_index,
            completed: true,
        };
        
        // let path = format!("channel_subgrids/{}_{}.json", bin_index, flat_cf_index);
        // write_channel_subgrid(&path, &channel_entry)?;
        let path = channel_subgrid_path(bin_index, flat_cf_index);
        write_channel_subgrid(path.to_str().unwrap(), &channel_entry)?;
        
    } else if matches!(&config.process, Process::SIA { .. }) {
        // let (grid, couplings) = compute_sia_sg(&config, bin_index, order_index, cf_index);
        todo!("Implement channel saving for SIA");
        
    } else if matches!(&config.process, Process::SIDIS_NC { .. } | Process::SIDIS_CC { .. } | Process::pSIDIS_NC { .. } | Process::pSIDIS_CC { .. }) {
        // let (grid, couplings) = compute_sidis_sg(&config, bin_index, order_index, cf_index);
        todo!("Implement channel saving for SIDIS");
        
    } else {
        return Err("Unsupported process type in run module".into());
    }

    Ok(())
}

/* -----------------------------------------------------------\
|                                                             |
|                Step 3: Output the results                   |
|                                                             |
\----------------------------------------------------------- */

pub fn combine(path: &str) {
    let config = RuncardConfig::load(path).expect("Failed to load runcard");

    let num_bins = config.num_bins();
    let num_cfs = config.total_cfs();

    let mut missing_jobs = Vec::new();

    // 1. Audit all jobs
    for b in 0..num_bins {
        for ch in 0..num_cfs {
            let job_index = b * num_cfs + ch;
            let file_path = channel_subgrid_path(b, ch);
            let is_completed = match std::fs::File::open(&file_path) {
                Ok(file) => {
                    // Try to parse the JSON and check the `completed` flag
                    match serde_json::from_reader::<_, ChannelEntry>(file) {
                        Ok(entry) => entry.completed,
                        Err(_) => false, // Invalid JSON or interrupted write
                    }
                }
                Err(_) => false, // File does not exist
            };

            if !is_completed {
                missing_jobs.push(job_index);
            }
        }
    }

    // 2. Abort if any jobs are missing or incomplete
    if !missing_jobs.is_empty() {
        println!("The following jobs are incomplete or missing. Please run/rerun them:");
        for job in missing_jobs {
            println!("vhf run {}", job);
        }
        return;
    }

    println!("All jobs completed successfully. Generating partonic subgrids...");

    // 3. Process channel subgrids into partonic subgrids
    for b in 0..num_bins {
        for ch in 0..num_cfs {
            let channel_path = channel_subgrid_path(b, ch);
            let file = std::fs::File::open(&channel_path).unwrap();
            let entry: ChannelEntry = serde_json::from_reader(file).unwrap();

            for (parton_index, factor) in entry.couplings {
                // 'c' is already the correct 0-13 channel index now
                let scaled_data: Vec<f64> = entry.data.iter().map(|&v| v * factor).collect();
                let partonic_path = partonic_subgrid_path(b, entry.order, parton_index);
                
                append_partonic_subgrid(
                    partonic_path.to_str().unwrap(), 
                    scaled_data, 
                    entry.shape.clone()
                ).expect("Failed to append partonic subgrid");
            }
        }
    }

    let grid_name = &config.run_name;

    let convs: Vec<(i32, bool, bool)> = match config.process {
        Process::DIS_NC {hadron, .. } | Process::DIS_CC {hadron, .. } => vec![(hadron, false, false)],
        Process::pDIS_NC {hadron, .. } | Process::pDIS_CC { hadron, .. } => vec![(hadron, true, false)],
        Process::SIA { hadron, .. } => vec![(hadron, false, true)],
        Process::SIDIS_NC { hadron_in, hadron_out, .. } | Process::SIDIS_CC { hadron_in, hadron_out, .. } => vec![(hadron_in, false, false), (hadron_out, false, true)],
        Process::pSIDIS_NC { hadron_in, hadron_out, .. } | Process::pSIDIS_CC { hadron_in, hadron_out, .. } => vec![(hadron_in, true, false), (hadron_out, true, true)]
        };
    
    todo!();
}

/* -----------------------------------------------------------\
|                                                             |
|                        Process List                         |
|                                                             |
\----------------------------------------------------------- */

const inv4PI: f64 = 1.0/(4.0 *std::f64::consts::PI);
const inv2PI: f64 = 1.0/(2.0 *std::f64::consts::PI);

pub enum CFsVec {
    Cf1D(Vec<Vec<(Cf1D, f64, fn(f64, f64, String) -> Vec<(i8, f64)>, fn(f64, f64) -> f64)>>),
    Cf2D(Vec<Vec<(Cf2D, f64, fn(f64, f64, f64, String) -> Vec<(i8, f64)>, fn(f64, f64, f64) -> f64)>>)
}

pub fn obtain_cfs(process: &Process) -> CFsVec {
    match process {
        Process::DIS_NC { observable, .. } => {
            if observable == "F2" {
                CFsVec::Cf1D(vec![
                    vec![(f2_light::f2nc_lo_ns::cf(), 1.0, f2_light::f2nc_lo_ns::nc_coupling, dis_factor_none)],
                    vec![
                        (f2_light::f2nc_nlo_ns::cf(), inv4PI, f2_light::f2nc_nlo_ns::nc_coupling, dis_factor_none), 
                        (f2_light::f2nc_nlo_g::cf(), inv4PI, f2_light::f2nc_nlo_g::nc_coupling, dis_factor_none)
                        ],
                    vec![
                        (f2_light::f2nc_nnlo_nsp::cf(), inv4PI.powi(2), f2_light::f2nc_nnlo_nsp::nc_coupling, dis_factor_none), 
                        (f2_light::f2nc_nnlo_g::cf(), inv4PI.powi(2), f2_light::f2nc_nnlo_g::nc_coupling, dis_factor_none), 
                        (f2_light::f2nc_nnlo_ps::cf(), inv4PI.powi(2), f2_light::f2nc_nnlo_ps::nc_coupling, dis_factor_none)
                        ],
                    vec![
                        (f2_light::f2nc_n3lo_nsp::cf(), inv4PI.powi(3), f2_light::f2nc_n3lo_nsp::nc_coupling, dis_factor_none),
                        (f2_light::f2nc_n3lo_g::cf(), inv4PI.powi(3), f2_light::f2nc_n3lo_g::nc_coupling, dis_factor_none),
                        (f2_light::f2nc_n3lo_ps::cf(), inv4PI.powi(3), f2_light::f2nc_n3lo_ps::nc_coupling, dis_factor_none),
                        (f2_light::f2nc_n3lo_qfl11::cf(), inv4PI.powi(3), f2_light::f2nc_n3lo_qfl11::nc_coupling, dis_factor_none),
                        (f2_light::f2nc_n3lo_gfl11::cf(), inv4PI.powi(3), f2_light::f2nc_n3lo_gfl11::nc_coupling, dis_factor_none)
                        ]
                ])
            } else {
                panic!("Observable {} not implemented for DIS NC", observable);
            }
        },
        Process::DIS_CC { .. } => todo!(),
        Process::pDIS_NC { .. } => todo!(),
        Process::pDIS_CC { .. } => todo!(),
        Process::SIA { .. } => todo!(),
        // Process::SIDIS_NC { observable, .. } => {
        //     if observable == "DIF-X-SEC" {
        //         CFsVec::Cf2D(vec![])
        //     } else {
        //         panic!("Observable {} not implemented for SIDIS NC", observable);
        //     }
        // },
        Process::SIDIS_CC { .. } => todo!(),
        Process::pSIDIS_NC { .. } => todo!(),
        Process::pSIDIS_CC { .. } => todo!(),
    }
}

// pub fn obtain_cfs_2d(process: &Process) -> CFsVec {
//     todo!()
// }