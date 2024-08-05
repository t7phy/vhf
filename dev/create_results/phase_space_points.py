import os

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
