from importlib import import_module
import argparse
import os
import json

from dev.parellization.conv_normal import conv2 as conv2_normal
from dev.parellization.conv_1nested import conv2 as conv2_1nested
from core.libfunc import lambertgrid

debug_flag = False
thresshold = 1e-9
# Define the phase space points, always in a list
x = [0.05]

z = [
    0.1,
    0.15,
    0.2,
    0.223,
    0.249,
    0.274,
    0.299,
    0.324,
    0.349,
    0.374,
    0.399,
    0.424,
    0.449,
    0.474,
    0.499,
    0.524,
    0.549,
    0.574,
    0.599,
    0.624,
    0.649,
    0.674,
    0.699,
    0.724,
    0.749,
    0.795,
    0.85,
    0.9,
    0.95,
]

# Dict with all the functions to load
functions_per_order = {
    "LO": {
        "file_path": "eh/unpol/lo_nlo.py",
        "functions": ["cl_lo_q2q_eq", "ct_lo_q2q_eq"],
        "len": 2,
    },
    "NLO": {
        "file_path": "eh/unpol/lo_nlo.py",
        "functions": [
            "cl_nlo_g2q_eq",
            "cl_nlo_q2g_eq",
            "cl_nlo_q2q_eq",
            "ct_nlo_g2q_eq",
            "ct_nlo_q2g_eq",
            "ct_nlo_q2q_eq",
        ],
        "len": 6,
    },
    "NNLO": {
        "file_path": "eh/unpol/nnlo/all_nnlo.py",
        "functions": [
            "cl_nnlo_g2g_eq",
            "cl_nnlo_g2q_eq",
            "cl_nnlo_q2g_eq",
            "cl_nnlo_q2q_eq",
            "cl_nnlo_q2q_eqp",
            "cl_nnlo_q2qb_eq",
            "cl_nnlo_q2qp_eq",
            "cl_nnlo_q2qp_eqp",
            "cl_nnlo_q2qp_es",
            "cl_nnlo_q2qpb_es",
            "ct_nnlo_g2g_eq",
            "ct_nnlo_g2q_eq",
            "ct_nnlo_q2g_eq",
            "ct_nnlo_q2q_eq",
            "ct_nnlo_q2q_eqp",
            "ct_nnlo_q2qb_eq",
            "ct_nnlo_q2qp_eq",
            "ct_nnlo_q2qp_eqp",
            "ct_nnlo_q2qp_es",
            "ct_nnlo_q2qpb_es",
        ],
        "len": 20,
    },
}

# Define the grids to run over
xgrid = lambertgrid(50, 1e-5, 1.0)
zgrid = lambertgrid(50, 1e-2, 1.0)


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

        ## Parse the arguments
        args = parser.parse_args()

        ## Input variables
        order = args.order
        nth_x = args.nth_x
        nth_z = args.nth_z
        nth_function = args.nth_function

        # perform check if correct order
        if order not in ["LO", "NLO", "NNLO"]:
            raise ValueError("Invalid order provided")
    else:
        order = "LO"
        nth_x = 0
        nth_z = 0
        nth_function = 1

    return order, nth_x, nth_z, nth_function


# Get the arguments
order, nth_x, nth_z, nth_function = get_arguments(debug_flag)

# Check if the nths values are within the range
if nth_x >= len(x):
    raise ValueError("nth_x is out of range")
if nth_z >= len(z):
    raise ValueError("nth_z is out of range")
if nth_function >= len(functions_per_order[order]["functions"]):
    raise ValueError("nth_function is out of range")

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

result_1nested = conv2_1nested(x, z, function, "000", xgrid, zgrid)()
result_normal = conv2_normal(x, z, function, "000", xgrid, zgrid)()
restult_normal2 = conv2_normal(x, z, function, "000", xgrid, zgrid)()

# Check if the same
## Create the file name
# Function to get the variable name
def get_var_name(var, scope):
    for name, value in scope.items():
        if value is var:
            return name
    return None

def compare_two_files(result1, result2, order, x, z, function_name):
    passed = True
    differences = list()
    for i in range(len(result1)):
        for j in range(len(result1[i])):
            for k in range(len(result1[i][j])):
                difference = abs(result1[i][j][k] - result2[i][j][k])
                if difference > thresshold:
                    passed = False
                    differences.append(difference)

    ## Store per order
    results_dir = f"dev/parellization/test_results/agreement/{order}/{get_var_name(result1,globals())}_vs_{get_var_name(result2,globals())}"
    os.makedirs(results_dir, exist_ok=True)
    if not passed:
        file_name = f"order{order}_x{x}_z{z}_{function_name}".replace(".", "") + ".json"

        with open(os.path.join(results_dir, file_name), "w") as f:
            json.dump(differences, f)  # Assuming otp is the list you want to store

        print(f"Results saved to {os.path.join(results_dir, file_name)}")
    else:
        file_name = "Passed"
        with open(os.path.join(results_dir, file_name), "w") as f:
            f.write("Passed")
        print(f"Results saved to {os.path.join(results_dir, file_name)}")


compare_two_files(result_normal, result_1nested, order, x, z, function_name)
compare_two_files(result_normal, restult_normal2, order, x, z, function_name)