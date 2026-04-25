use serde::{Serialize, Deserialize};
use std::fs::OpenOptions;
use std::io::{BufRead, BufReader, Write};
use std::path::Path;
use ndarray::{ArrayD, IxDyn};
use fs2::FileExt;

#[derive(Serialize, Deserialize)]
pub struct TensorEntry {
    pub data: Vec<f64>,
    pub shape: Vec<usize>,
}

#[derive(Serialize, Deserialize)]
pub struct ChannelEntry {
    pub data: Vec<f64>,
    pub shape: Vec<usize>,
    pub couplings: Vec<(usize, f64)>,
    pub order: usize,
    pub completed: bool,
}

pub fn write_channel_subgrid(path: &str, entry: &ChannelEntry) -> std::io::Result<()> {
    let file = std::fs::File::create(path)?;
    serde_json::to_writer(file, entry)?;
    Ok(())
}

pub fn append_partonic_subgrid(path: &str, data: Vec<f64>, shape: Vec<usize>) -> std::io::Result<()> {
    if !Path::new(path).exists() {
        return Err(std::io::Error::new(
            std::io::ErrorKind::NotFound,
            format!("File '{}' does not exist", path),
        ));
    }

    let entry = TensorEntry { data, shape };

    let mut file = OpenOptions::new()
        .write(true)
        .append(true)
        .open(Path::new(path))?;

    file.lock_exclusive()?; 

    let json = serde_json::to_string(&entry).unwrap();
    writeln!(file, "{}", json)?;

    file.unlock()?;
    Ok(())
}

// pub enum Tensor {
//     TwoD(Vec<Vec<f64>>),
//     ThreeD(Vec<Vec<Vec<f64>>>),
// }

// pub fn append_tensor_to_file(path: &str, tensor: Tensor) -> std::io::Result<()> {
//     // Ensure file exists
//     if !Path::new(path).exists() {
//         return Err(std::io::Error::new(
//             std::io::ErrorKind::NotFound,
//             format!("File '{}' does not exist", path),
//         ));
//     }

//     // Flatten tensor
//     let (data, shape) = match tensor {
//         Tensor::TwoD(v) => {
//             let rows = v.len();
//             let cols = if rows > 0 { v[0].len() } else { 0 };
//             let flat = v.into_iter().flatten().collect();
//             (flat, vec![rows, cols])
//         }
//         Tensor::ThreeD(v) => {
//             let d1 = v.len();
//             let d2 = if d1 > 0 { v[0].len() } else { 0 };
//             let d3 = if d2 > 0 { v[0][0].len() } else { 0 };
//             let flat = v.into_iter().flat_map(|m| m.into_iter().flatten()).collect();
//             (flat, vec![d1, d2, d3])
//         }
//     };

//     let entry = TensorEntry { data, shape };

//     // Open file in append mode
//     let mut file = OpenOptions::new()
//         .write(true)
//         .append(true)
//         .open(Path::new(path))?;

//     // --- Acquire exclusive lock (blocking) ---
//     file.lock_exclusive()?; // fs2 handles cross-platform locking safely

//     // Write JSON entry
//     let json = serde_json::to_string(&entry).unwrap();
//     writeln!(file, "{}", json)?;

//     // Unlock automatically when file is dropped, or you can call:
//     file.unlock()?;

//     Ok(())
// }

// --- Read + sum all entries using ArrayD ---
fn sum_tensors_from_file(path: &str) -> ArrayD<f64> {
    let file = std::fs::File::open(path).expect("file must exist");
    let reader = BufReader::new(file);

    let mut result: Option<ArrayD<f64>> = None;

    for line in reader.lines() {
        let line = line.unwrap();
        let entry: TensorEntry = serde_json::from_str(&line).unwrap();

        let arr = ArrayD::from_shape_vec(IxDyn(&entry.shape), entry.data)
            .expect("shape mismatch or invalid data");

        match &mut result {
            Some(acc) => *acc += &arr,
            None => result = Some(arr),
        }
    }

    result.expect("no entries in file")
}