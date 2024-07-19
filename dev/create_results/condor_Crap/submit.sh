#!/bin/bash

# Get the command line arguments
order=$1
nth_x=$2
nth_z=$3
nth_function=$4

# Call the Python function with the arguments
cd /data/theorie/gseevent/SIDIS/
export PYTHONPATH="${PYTHONPATH}:/data/theorie/gseevent/SIDIS/"
pwd
python dev/create_results/run.py $order $nth_x $nth_z $nth_function