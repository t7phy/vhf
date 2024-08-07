# Central binning used, not the limits
phase_space_per_experiment = {
    "COMPASS": {
        "x": [0.007, 0.015, 0.025, 0.035, 0.05, 0.08, 0.12, 0.16, 0.29],
        "z": [
            0.225,
            0.275,
            0.325,
            0.375,
            0.425,
            0.475,
            0.525,
            0.575,
            0.625,
            0.675,
            0.725,
            0.8,
        ],
        "x_len": 9,
        "z_len": 12,
    },
    "HERMES": {
        "x": [0.0315, 0.0475, 0.065, 0.0875, 0.12, 0.25, 0.35, 0.5],
        "z": [0.15, 0.25, 0.35, 0.5, 0.7, 0.95],
        "x_len": 8,
        "z_len": 6,
    },
    "Old_points": {
        "x": [0.05],
        "z": [
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
        ],
        "x_len": 1,
        "z_len": 29,
    },
}


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
