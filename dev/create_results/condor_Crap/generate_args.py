from dev.create_results.phase_space_points import (
    phase_space_per_experiment,
    functions_per_order,
)

orders = ["LO", "NLO", "NNLO"]  # LO, NLO, NNLO
datasets = ["HERMES", "COMPASS"]  # COMPASS, HERMES, Old_points

for order in orders:
    with open(f"{order}_args.txt", "w") as f:
        for dataset in datasets:
            len_x = phase_space_per_experiment[dataset]["x_len"]
            len_z = phase_space_per_experiment[dataset]["z_len"]
            len_function = functions_per_order[order]["len"]
            for x in range(0, len_x):
                for z in range(0, len_z):
                    for func in range(0, len_function):
                        f.write(f"{order} {x} {z} {func} {dataset}\n")
