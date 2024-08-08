import os
from dev.create_results.phase_space_points import x, z, functions_per_order


def extract_value_between(s, x, y):
    # Find the index of the first occurrence of x
    start_index = s.find(x)
    # If x is not found, return an empty string
    if start_index == -1:
        return ""
    # Adjust start_index to get the index after x
    start_index += 1

    # Find the index of the first occurrence of y after x
    end_index = s.find(y, start_index)
    # If y is not found, return an empty string
    if end_index == -1:
        return ""

    # Extract and return the value between x and y
    return s[start_index:end_index]


if __name__ == "__main__":
    order = "NNLO"
    existing_values = os.listdir(f"dev/create_results/results/{order}")

    values = [
        (
            extract_value_between(value, "x", "_"),
            extract_value_between(value, "z", "_"),
            "c" + extract_value_between(value, "c", "."),
        )
        for value in existing_values
    ]
    missing_values = list()
    missing_values_positions = list()
    for eq_pos, eq in enumerate(functions_per_order["NNLO"]["functions"]):
        for x_pos, x_val in enumerate(x):
            for z_pos, z_val in enumerate(z):
                if (
                    f"{x_val}".replace(".", ""),
                    f"{z_val}".replace(".", ""),
                    eq,
                ) not in values:
                    missing_values.append((x_val, z_val, eq))
                    missing_values_positions.append((x_pos, z_pos, eq_pos))

    missing_equations = list()

    for value in missing_values:
        print(value, "\n")

        if value[2] not in missing_equations:
            missing_equations.append(value[2])

    with open("args.txt", "w") as f:
        for value in missing_values_positions:
            f.write(f"{order} {value[0]} {value[1]} {value[2]}\n")

    a = 1
