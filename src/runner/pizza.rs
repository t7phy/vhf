use pineappl::boc::{BinsWithFillLimits, Channel, Kinematics, Order, ScaleFuncForm, Scales};
use pineappl::convolutions::{Conv, ConvType};
use pineappl::grid::Grid;
use pineappl::interpolation::{Interp, InterpMeth, Map, ReweightMeth};
use pineappl::pids::PidBasis;
use pineappl::subgrid::ImportSubgridV1;
use pineappl::packed_array::PackedArray;

use ndarray::ArrayD;
use std::fs::File;

fn pid(particle: &str) -> i32 {
    match particle {
        "proton"      => 2212,
        "anti-proton" => -2212,
        "neutron"     => 2112,
        "pion+"       => 211,
        "pion-"       => -211,
        "pion0"       => 111,
        "kaon+"       => 321,
        "kaon-"       => -321,
        "kaon0"       => 311,
        _ => panic!("Unknown or unsupported hadron: '{}'. Contact the author if you think this is a mistake.", particle)
    }
}

// struct GridAttributes {
//     convolutions: Vec<Conv>,
//     kinematics: Vec<Kinematics>,
//     interpolations: Vec<Interp>,
//     scales: Vec<Scales>,
//     fill_limits: Vec<BinsWithFillLimits>,
// }

pub fn generate_grid(
    grid_name: &str,
    convs: Vec<(i32, bool, bool)>, // (particle_name, polarized, timelike)
    num_bins: usize,                // number of bins
    // orders: Vec<[u8; 5]>,           // vector of orders
    // channels: Vec<Vec<(Vec<i32>, f64)>>,
    subgrids: Vec<MySubgrid>,
) {

    let num_convs = convs.len();

    let mut convolutions = Vec::new();
    let mut kinematics = Vec::new();
    let mut interpolations = Vec::new();

    kinematics.push(Kinematics::Scale(0));
    interpolations.push(Interp::new(
        1.0,
        10.0,
        20,
        3,
        ReweightMeth::NoReweight,
        Map::ApplGridH0,
        InterpMeth::Lagrange,
    ));

    for (i, conv) in convs.into_iter().enumerate() {
        let (particle, polarized, timelike) = conv;
        convolutions.push(Conv::new(ConvType::new(polarized, timelike), particle));
        interpolations.push(Interp::new(
            0.0001,
            1.0,
            50,
            4,
            ReweightMeth::NoReweight,
            Map::ApplGridF2,
            InterpMeth::Lagrange,
        ));
        kinematics.push(Kinematics::X(i));
    }

    let scale_funcs = Scales {
        ren: ScaleFuncForm::Scale(0),
        fac: ScaleFuncForm::Scale(0),
        frg: ScaleFuncForm::Scale(0),
    };

    let mut fill_limits = Vec::new();
    for i in 0..=num_bins {
        fill_limits.push(i as f64);
    }

    let grid_bins = BinsWithFillLimits::from_fill_limits(fill_limits).expect("invalid fill limits");

    let mut grid_orders = Vec::new();
    // for order in orders {
    //     grid_orders.push(Order::new(order[0], order[1], order[2], order[3], order[4]));
    // }
    for i in 0..=3 {
        grid_orders.push(Order::new(i, 2, 0, 0, 0));
    }

    // let mut grid_channels = Vec::new();
    // for ch in channels {
    //     let mut channel = Vec::new();
    //     for partonic_channel in ch {
    //         channel.push(partonic_channel);
    //     }
    //     let channel = Channel::new(channel);
    //     grid_channels.push(channel);
    // }
    // let grid_channels: Vec<Channel> = channels.into_iter().map(Channel::new).collect();
    let pids = vec![21, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6, 22];

    let raw_channels: Vec<Vec<(Vec<i32>, f64)>> = match num_convs {
        1 => {
            pids
                .iter()
                .map(|&pid| vec![(vec![pid], 1.0)])
                .collect()
        }
    
        2 => {
            let mut result = Vec::with_capacity(pids.len() * pids.len());
    
            for &a in &pids {
                for &b in &pids {
                    result.push(vec![(vec![a, b], 1.0)]);
                }
            }
    
            result
        }
    
        _ => panic!("convs.len() must be 1 or 2"),
    };
    
    let grid_channels: Vec<Channel> = raw_channels
        .into_iter()
        .map(Channel::new)
        .collect();

    let mut grid = Grid::new(
        grid_bins,
        grid_orders,
        grid_channels,
        PidBasis::Pdg,
        convolutions,
        interpolations,
        kinematics,
        scale_funcs,
    );

    for subgrid in subgrids {
        let (b, o, c) = subgrid.boc_index;
        let arrayd = subgrid.subgrid;
        let packed_subrgid = PackedArray::from(arrayd.view());
        let import_subgrid = ImportSubgridV1::new(packed_subrgid, subgrid.itp_nodes);
        let subgrid = import_subgrid.into();
        grid.subgrids_mut()[[o, b, c]] = subgrid;
    }

    // // TODO: replace `1, 2, 3` with the right shape
    // let subgrid = PackedArray::new(vec![1, 2, 3]);
    // // TODO: replace `0, 1, 2` with the right order, bin and channel index
    // grid.subgrids_mut()[[0, 1, 2]] = Subgrid::new(subgrid).into();

    // // use this or put the argument of `set_bsfl` as the value of `grid_bins`
    // grid.set_bwfl(BinsWithFillLimits::from_limits_and_normalizations(
    //         /* TODO: add bin limits */,
    //         // TODO: use the right normalizations
    //         vec![1.0; grid_bins.len()])
    //     // TODO: hand the error
    //     .unwrap());

    grid.optimize();

    let filename = format!("{}.pineappl.lz4", grid_name);

    // grid.write_lz4(
    //     File::create(filename)
    //         // TODO: handle the error
    //         .unwrap(),
    // );
    match File::create(&filename) {
        Ok(file) => {
            if let Err(e) = grid.write_lz4(file) {
                eprintln!("Failed to write grid to file '{}': {}", filename, e);
            } else {
                println!("Grid successfully written to '{}'", filename);
            }
        }
        Err(e) => {
            eprintln!("Failed to create file '{}': {}", filename, e);
        }
    }
}

pub struct MySubgrid {
    boc_index: (usize, usize, usize),
    subgrid: ArrayD<f64>,
    itp_nodes: Vec<Vec<f64>>,
}

// pub enum SubgridArrayTypes {
//     Conv1(Vec<Vec<f64>>),
//     Conv2(Vec<Vec<Vec<f64>>>),
//     Conv3(Vec<Vec<Vec<Vec<f64>>>>),
// }

// impl SubgridArrayTypes {
//     pub fn into_arrayd(self) -> ArrayD<f64> {
//         match self {
//             SubgridArrayTypes::Conv1(v) => {
//                 let shape = vec![v.len(), v[0].len()];
//                 let flat: Vec<f64> = v.into_iter().flatten().collect();
//                 ArrayD::from_shape_vec(shape, flat).expect("Invalid dimensions for Conv1")
//             }
//             SubgridArrayTypes::Conv2(v) => {
//                 let shape = vec![v.len(), v[0].len(), v[0][0].len()];
//                 let flat: Vec<f64> = v.into_iter().flatten().flatten().collect();
//                 ArrayD::from_shape_vec(shape, flat).expect("Invalid dimensions for Conv2")
//             }
//             SubgridArrayTypes::Conv3(v) => {
//                 let shape = vec![v.len(), v[0].len(), v[0][0].len(), v[0][0][0].len()];
//                 let flat: Vec<f64> = v.into_iter().flatten().flatten().flatten().collect();
//                 ArrayD::from_shape_vec(shape, flat).expect("Invalid dimensions for Conv3")
//             }
//         }
//     }
// }