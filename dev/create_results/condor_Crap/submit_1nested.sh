#!/bin/bash

# Activate the correct conda environment
source /data/theorie/gseevent/.conda/bin/activate sidis

# Get the command line arguments
order=$1
nth_x=$2
nth_z=$3
nth_function=$4
dataset=$5

# Call the Python function with the arguments
cd /data/theorie/gseevent/SIDIS/
python -m dev.create_results.run_1nest $order $nth_x $nth_z $nth_function $dataset
echo "Done"