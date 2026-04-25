use clap::{Parser, Subcommand};
use std::process;
// Replace 'vhf' with your actual crate name from Cargo.toml if different
use vhf::runner::runner_core::{RuncardConfig, run}; 

/// === VIRTUAL HADRON FACTORY ===
/// Est. 2025
#[derive(Parser)]
#[command(name = "vhf")]
#[command(about = "Virtual Hadron Factory CLI", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Option<Commands>,
}

#[derive(Subcommand)]
enum Commands {
    /// Process the runcard.yaml and prepare the run environment
    Prepare,
    
    /// Compute the specified point in the runcard
    Run {
        /// Index of the subgrid point
        index: usize,
    },
    
    /// Produce the PineAPPL grid from results
    Combine,
}

fn vhf_home() {
    println!("=== VIRTUAL HADRON FACTORY ===");
    println!("Est. 2025");
    println!("      [ASCII ART PLACEHOLDER]\n");
    println!("Available subcommands:");
    println!("  prepare    Process runcard.yaml and prepare the run");
    println!("  run        Compute the specified point");
    println!("  combine    Produce the PineAPPL grid");
    println!("\nUse --help with a subcommand for more info.");
}

fn main() {
    let cli = Cli::parse();

    match cli.command {
        Some(Commands::Prepare) => {
            println!("Initializing the run using 'runcard.yaml'...");
            
            // Call the prepare function
            if let Err(e) = RuncardConfig::prepare("runcard.yaml") {
                eprintln!("❌ Error during preparation: {}", e);
                process::exit(1);
            }
        }
        
        Some(Commands::Run { index }) => {
            println!("Running computation for index {}...", index);
            
            // Execute the run logic in the current directory
            if let Err(e) = run(index) {
                eprintln!("❌ Error executing run for index {}: {}", index, e);
                process::exit(1);
            } else {
                println!("✅ Successfully completed run {}", index);
            }
        }
        
        Some(Commands::Combine) => {
            println!("Combining results from the current directory...");
            todo!("Implement runner::combine_grid logic here");
        }
        
        // This handles the case where the user types just 'vhf'
        None => {
            vhf_home();
        }
    }
}