// use vhf::core::interpolation::{lambertgrid, compute_basis_functions, interpolator};
// use std::fs::File;
// use std::io::Write;

// fn main() {
//     // 1. Setup Grid
//     let n_pts = 50;
//     let x_min = 1e-5;
//     let x_max = 1.0;
//     let xgrid = lambertgrid(n_pts, x_min, x_max);

//     // 2. Compute Basis Functions (The large dictionary)
//     let poly_deg = 3;
//     let bfs = compute_basis_functions(xgrid.clone(), poly_deg, true);

//     // 3. Evaluate at a few test points
//     let test_points = vec![0.0001, 0.001, 0.05, 0.2, 0.8];
//     let mut interp_results = Vec::new();
//     for &p in &test_points {
//         interp_results.push(interpolator(p, &bfs, true));
//     }

//     // 4. Export all data to JSON for Python comparison
//     let data = serde_json::json!({
//         "xgrid": xgrid,
//         "basis_functions": bfs,
//         "test_points": test_points,
//         "interp_results": interp_results
//     });

//     let mut file = File::create("interp_comparison.json").unwrap();
//     file.write_all(serde_json::to_string_pretty(&data).unwrap().as_bytes()).unwrap();
    
//     println!("Exported interp_comparison.json for Python verification.");
// }

use vhf::core::interpolation::{lambertgrid, compute_basis_functions, interpolator};
use std::fs::File;
use std::io::Write;

fn main() {
    // 1. Setup Grid
    let n_pts = 50;
    let x_min = 1e-5;
    let x_max = 1.0;
    let xgrid = lambertgrid(n_pts, x_min, x_max);

    // 2. Compute Basis Functions (Returns BasisCache struct)
    let poly_deg = 4;
    let cache = compute_basis_functions(xgrid.clone(), poly_deg, true);

    // 3. Evaluate at a few test points
    // let test_points = vec![0.0001, 0.001, 0.05, 0.2, 0.8];
    let test_points = vec![
        // The Edges
        1.000000000000e-05, 1.000000000001e-05, 1.1e-05,
        0.999999999999, 1.0,

        // The "Log-Curve" (Geometric progression)
        2e-05, 5e-05, 1e-04, 2e-04, 5e-04, 
        1e-03, 2e-03, 5e-03, 1e-02, 2e-02, 
        5e-02, 0.1, 0.15, 0.2, 0.25, 
        0.3, 0.35, 0.4, 0.45, 0.5, 
        0.55, 0.6, 0.65, 0.7, 0.75, 
        0.8, 0.85, 0.9, 0.95,

        // Potential "Node" boundaries (Middle of the Lambert grid)
        0.00045, 0.0078, 0.012, 0.045, 0.089,
        0.123, 0.456, 0.789, 0.912, 0.987,
        0.000015, 0.000025, 0.000035, 0.000045, 0.000055, 0.000065
    ];
    let mut interp_results = Vec::new();
    for &p in &test_points {
        interp_results.push(interpolator(p, &cache));
    }

    // 4. Export all data to JSON
    // Note: cache.functions is now a Vec<Vec<BasisPiece>>
    // The JSON "basis_functions" will be a list of lists, not a dict.
    let data = serde_json::json!({
        "xgrid": xgrid,
        "basis_functions": cache.functions, 
        "test_points": test_points,
        "interp_results": interp_results
    });

    let mut file = File::create("interp_comparison.json").unwrap();
    file.write_all(serde_json::to_string_pretty(&data).unwrap().as_bytes()).unwrap();
    
    println!("Exported interp_comparison.json for Python verification.");
}