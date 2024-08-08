#!/bin/bash

# Activate the correct conda environment
source /data/theorie/gseevent/.conda/bin/activate sidis

which python 
# Get the command line arguments
order=$1
nth_x=$2
nth_z=$3
nth_function=$4

# Call the Python function with the arguments
cd /data/theorie/gseevent/SIDIS/
python -m dev.parellization.test_speed_comparison $order $nth_x $nth_z $nth_function