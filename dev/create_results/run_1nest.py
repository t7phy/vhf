from importlib import import_module
import argparse
import os
import json

import time

from core.libfunc import lambertgrid
import math

from dev.create_results.conv_1nested import conv2 as conv2_1nested
from dev.create_results.phase_space_points import (
    phase_space_per_experiment,
    functions_per_order,
)

debug_flag = False


def get_arguments(debug_flag=False):
    if not debug_flag:
        # Get the arguments
        ## Create the parser
        parser = argparse.ArgumentParser(description="Process some integers.")

        ## Add arguments
        parser.add_argument(
            "order", type=str, help="The order (LO, NLO, NNLO) of the calculation"
        )
        parser.add_argument("nth_x", type=int, help="The nth x value")
        parser.add_argument("nth_z", type=int, help="The nth z value")
        parser.add_argument("nth_function", type=int, help="The nth function")
        parser.add_argument(
            "dataset", type=str, help="The nth dataset: COMPASS, HERMES, Old_points"
        )

        ## Parse the arguments
        args = parser.parse_args()

        ## Input variables
        order = args.order
        nth_x = args.nth_x
        nth_z = args.nth_z
        nth_function = args.nth_function
        dataset = args.dataset

        # perform check if correct order
        if order not in ["LO", "NLO", "NNLO"]:
            raise ValueError("Invalid order provided")
        if dataset not in ["COMPASS", "HERMES", "Old_points"]:
            raise ValueError("Invalid dataset provided")
    else:
        order = "LO"
        nth_x = 0
        nth_z = 0
        nth_function = 1
        dataset = "COMPASS"

    return order, nth_x, nth_z, nth_function, dataset


# Get the arguments
order, nth_x, nth_z, nth_function, dataset = get_arguments(debug_flag)

x = phase_space_per_experiment[dataset]["x"]
z = phase_space_per_experiment[dataset]["z"]

# Check if the nths values are within the range
if nth_x >= phase_space_per_experiment[dataset]["x_len"]:
    raise ValueError("nth_x is out of range")
if nth_z >= phase_space_per_experiment[dataset]["z_len"]:
    raise ValueError("nth_z is out of range")
if nth_function >= len(functions_per_order[order]["functions"]):
    raise ValueError("nth_function is out of range")


# Get lambagrids
def decide_lowest_lambdagrid(x: list):
    min_order_of_magnitude = min(math.floor(math.log10(abs(val))) for val in x)

    return 10 ** (min_order_of_magnitude - 1)


xgrid = lambertgrid(50, decide_lowest_lambdagrid(x), 1.0)
zgrid = lambertgrid(50, decide_lowest_lambdagrid(z), 1.0)

# Get the x, z and function
x = x[nth_x]
z = z[nth_z]
function_name = functions_per_order[order]["functions"][nth_function]
function = getattr(
    import_module(
        functions_per_order[order]["file_path"].replace("/", ".").replace(".py", "")
    ),
    function_name,
)


start_time = time.time()
result_1nested = conv2_1nested(x, z, function, "000", xgrid, zgrid)()
end_time = time.time()
time_diff = end_time - start_time

# Convert time difference to hh/mm/ss format
hours, rem = divmod(time_diff, 3600)
minutes, seconds = divmod(rem, 60)
time_diff_formatted = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

## Store per order

file_name = f"x{x}_z{z}_{function_name}".replace(".", "") + ".json"
results_dir = f"dev/create_results/results/{dataset}/{order}"
os.makedirs(results_dir, exist_ok=True)

with open(os.path.join(results_dir, file_name), "w") as f:
    json.dump(result_1nested, f)

# Append the time difference to an existing text file
time_log_file = "time_log.txt"  # Replace with the path to your existing text file
with open(os.path.join(results_dir, time_log_file), "a") as f:
    f.write(time_diff_formatted + "\n")

print(f"Results saved to {os.path.join(results_dir, file_name)}")
