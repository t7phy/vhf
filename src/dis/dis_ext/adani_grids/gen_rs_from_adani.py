#!/usr/bin/env python3
"""
gen_rs_from_adani.py

Long-term replacement for the two-step
    yadism/extras/heavy_em_n3lo/produce_grids.py
    yadism/extras/heavy_em_n3lo/yad_grids.py
pipeline: this single script reproduces both steps (grid-axis generation
and the `adani` massive-coefficient-function evaluation over that grid) but
writes Rust source directly instead of intermediate `.npy` files.

Pipeline (see heavy_em_n3lo/README.md for the original two-script version):

  1. Build the (eta, xi) axes exactly as `produce_grids.py` does:
         eta = geomspace(1e-5, 9.9e5, 73)
         xi  = geomspace(1e-3, 1e9,  84)
  2. For every (nf, kind, channel) in {3,4,5} x {"2","L"} x {"g","q"}
     (order fixed at 3, i.e. N3LO), build an
     `adani.ApproximateCoefficientFunction` and evaluate `fxBand` over the
     full (xi, eta) grid in parallel, exactly as `yad_grids.py` does.
  3. For each of the 3 scale variations (-1, 0, +1) returned by `fxBand`,
     emit a `.rs` file in the same format as
     ~/vhf/src/dis/f2_heavy/fh_grids/*.rs (and the earlier
     ~/nnpdf_dis/rust_n3lo/*.rs, generated from yadism's precomputed .npy
     grids): three `pub static` arrays (X, Y, BODY) plus a
     `OnceLock`-cached `*_spline()` accessor.

Note on `adani.ApproximateCoefficientFunction`'s signature: the local
~/nnpdf_dis/adani checkout has a `damp_power` parameter (added after
`yad_grids.py` was written) inserted *before* `NLL`/`highscale_version` in
the constructor, so `yad_grids.py`'s old positional call
`(order, kind, channel, True, adani.Exact)` no longer means what it used
to (it now sets `damp_power=True, NLL=adani.Exact`, which the current
version's type checking rejects outright). This script calls with explicit
keywords (`NLL=True, highscale_version=adani.Exact`) to preserve the
original intent and stay robust to future signature changes.

Usage
-----
    python gen_rs_from_adani.py [out_dir]
        [--cores N] [--kx KX] [--ky KY] [--spline IMPORT_PATH]
        [--nf 3 4 5] [--kind 2 L] [--channel g q] [--order 3]

    out_dir     where to write .rs files (default: this script's directory)
    --cores     worker processes for the `adani` evaluation (default: all cores)

Requires the `adani` Python package to be built/installed
(`pip install ~/nnpdf_dis/adani`).
"""

import argparse
import itertools
import os
import re
import sys
import time
from multiprocessing import Pool

import numpy as np

try:
    import adani
except ImportError:
    print(
        "Error: the `adani` package is not importable. Build/install it first, e.g.\n"
        "    python -m venv .bench_venv && source .bench_venv/bin/activate\n"
        "    pip install ~/nnpdf_dis/adani",
        file=sys.stderr,
    )
    sys.exit(1)


# ── grid axes (mirrors produce_grids.py) ────────────────────────────────────────

def build_axes() -> tuple[np.ndarray, np.ndarray]:
    """(eta, xi) axes, identical construction to produce_grids.py."""
    eta_grid = np.geomspace(1e-5, 9.9e5, 73, endpoint=True)
    xi_grid = np.geomspace(1e-3, 1e9, 84, endpoint=True)
    return eta_grid, xi_grid


# ── adani evaluation (mirrors yad_grids.py) ─────────────────────────────────────

def x_eta(eta: float, m2Q2: float) -> float:
    return 1.0 / (1.0 + 4.0 * m2Q2 * (eta + 1))


# Populated per-(nf, kind, channel) combination before the Pool is spawned;
# inherited by worker processes via fork, exactly as yad_grids.py relies on.
_massive = None
_nf = None


def _init_worker(massive, nf) -> None:
    global _massive, _nf
    _massive = massive
    _nf = nf


def _eval_point(pair: tuple[float, float]) -> list[float]:
    eta, xi = pair
    m2Q2 = 1.0 / xi
    m2mu2 = 1.0 / xi
    x = x_eta(eta, m2Q2)
    res = _massive.fxBand(x, m2Q2, m2mu2, _nf)
    return [res.GetLower(), res.GetCentral(), res.GetHigher()]


def compute_grid(
    nf: int, kind: str, channel: str, order: int, eta_grid, xi_grid, cores: int
) -> np.ndarray:
    """Returns an (len(xi), len(eta), 3) array of [lower, central, higher]."""
    if order > 1:
        massive = adani.ApproximateCoefficientFunction(
            order, kind, channel, NLL=True, highscale_version=adani.Exact
        )
    elif order == 1:
        massive = adani.ExactCoefficientFunction(order, kind, channel)
    else:
        raise ValueError("order must be 1, 2 or 3")

    pairs = [(eta, xi) for xi in xi_grid for eta in eta_grid]

    with Pool(cores, initializer=_init_worker, initargs=(massive, nf)) as pool:
        flat = pool.map(_eval_point, pairs)

    return np.array(flat).reshape(len(xi_grid), len(eta_grid), 3)


# ── Rust formatting (mirrors rust_n3lo/gen_rs_npy.py) ───────────────────────────

def fmt_f64(v: float) -> str:
    """Shortest round-tripping decimal repr, as a Rust f64 literal."""
    if not (v == v) or v in (float("inf"), float("-inf")):
        raise ValueError(f"non-finite value {v!r} cannot be a Rust literal")
    return f"{v!r}f64"


def fmt_array_body(values: list[float], columns: int = 8) -> str:
    lines = []
    for start in range(0, len(values), columns):
        chunk = values[start : start + columns]
        lines.append("    " + ", ".join(fmt_f64(v) for v in chunk) + ",")
    return "\n".join(lines)


def stem_to_prefix(stem: str) -> str:
    ident = re.sub(r"[^A-Za-z0-9]", "_", stem).upper()
    if ident and ident[0].isdigit():
        ident = "_" + ident
    return ident


def stem_to_fn(stem: str) -> str:
    fn = re.sub(r"[^A-Za-z0-9]", "_", stem).lower()
    if fn and fn[0].isdigit():
        fn = "_" + fn
    return fn + "_spline"


def stem_to_mod(stem: str) -> str:
    mod = re.sub(r"[^A-Za-z0-9]", "_", stem).lower()
    if mod and mod[0].isdigit():
        mod = "_" + mod
    return mod


def generate_rs(
    source_name: str,
    x: list[float],
    y: list[float],
    body: list[float],
    kx: int,
    ky: int,
    spline_path: str,
) -> str:
    stem = source_name
    prefix = stem_to_prefix(stem)
    fn = stem_to_fn(stem)
    ny = len(y)
    type_name = spline_path.rsplit("::", 1)[-1]

    return (
        f"// Generated directly from adani (xi/eta grid, {source_name}) — do not edit by hand.\n"
        f"//\n"
        f"// Grid:     {len(x)} × {ny}  ({len(body)} body values)\n"
        f"// Axes:     x = xi (row-axis), y = eta (column-axis)\n"
        f"// Degrees:  kx = {kx},  ky = {ky}\n"
        f"// Indexing: {prefix}_BODY[i * {ny} + j] == f({prefix}_X[i], {prefix}_Y[j])\n"
        f"\n"
        f"use std::sync::OnceLock;\n"
        f"use {spline_path};\n"
        f"\n"
        f"// ── raw grid data {'─' * 58}\n"
        f"\n"
        f"/// Row-axis coordinates (xi).\n"
        f"pub static {prefix}_X: [f64; {len(x)}] = [\n"
        f"{fmt_array_body(x)}\n"
        f"];\n"
        f"\n"
        f"/// Column-axis coordinates (eta).\n"
        f"pub static {prefix}_Y: [f64; {ny}] = [\n"
        f"{fmt_array_body(y)}\n"
        f"];\n"
        f"\n"
        f"/// Grid values, row-major: `{prefix}_BODY[i * {ny} + j] == f(x[i], y[j])`.\n"
        f"pub static {prefix}_BODY: [f64; {len(body)}] = [\n"
        f"{fmt_array_body(body)}\n"
        f"];\n"
        f"\n"
        f"// ── spline (built once, reused forever) {'─' * 42}\n"
        f"\n"
        f"static _{prefix}_SPLINE: OnceLock<{type_name}> = OnceLock::new();\n"
        f"\n"
        f"/// Returns the degree-({kx},{ky}) interpolating spline over `{source_name}`.\n"
        f"///\n"
        f"/// The spline is constructed on the **first call only**; every subsequent\n"
        f"/// call returns a reference to the same object at zero cost.  Safe to call\n"
        f"/// from multiple threads simultaneously — `OnceLock` guarantees exactly-once\n"
        f"/// initialisation even under concurrent access.\n"
        f"#[inline]\n"
        f"pub fn {fn}() -> &'static {type_name} {{\n"
        f"    _{prefix}_SPLINE.get_or_init(|| {{\n"
        f"        {type_name}::new(\n"
        f"            &{prefix}_X,\n"
        f"            &{prefix}_Y,\n"
        f"            &{prefix}_BODY,\n"
        f"            {kx},\n"
        f"            {ky},\n"
        f"        )\n"
        f"    }})\n"
        f"}}\n"
    )


# ── main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute N3LO heavy coefficient-function grids with adani "
        "and emit Rust spline modules directly (no intermediate .npy)."
    )
    parser.add_argument("out_dir", nargs="?", help="output directory (default: this script's directory)")
    parser.add_argument("--cores", type=int, default=os.cpu_count(), help="worker processes (default: all cores)")
    parser.add_argument("--kx", type=int, default=3, help="spline degree along x (default: 3)")
    parser.add_argument("--ky", type=int, default=3, help="spline degree along y (default: 3)")
    parser.add_argument(
        "--spline",
        default="crate::core::scits::rect_bivariate_spline::RectBivariateSpline",
        help="fully-qualified Rust path to RectBivariateSpline",
    )
    parser.add_argument("--nf", type=int, nargs="+", default=[3, 4, 5])
    parser.add_argument("--kind", choices=["2", "L"], nargs="+", default=["2", "L"])
    parser.add_argument("--channel", choices=["g", "q"], nargs="+", default=["g", "q"])
    parser.add_argument("--order", type=int, default=3, choices=[1, 2, 3])
    args = parser.parse_args()

    out_dir = args.out_dir or os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)

    if not (1 <= args.kx <= 5 and 1 <= args.ky <= 5):
        print("Error: kx and ky must be in 1..=5", file=sys.stderr)
        sys.exit(1)

    eta_grid, xi_grid = build_axes()
    eta_list = eta_grid.tolist()
    xi_list = xi_grid.tolist()

    variations = [0] if args.order == 1 else [-1, 0, 1]

    stems = []
    combos = list(itertools.product(args.nf, args.kind, args.channel))
    for combo_idx, (nf, kind, channel) in enumerate(combos, start=1):
        print(
            f"[{combo_idx}/{len(combos)}] C{kind}{channel} nf={nf} order={args.order} "
            f"— grid ({len(xi_list)}×{len(eta_list)}), {args.cores} workers"
        )
        start = time.perf_counter()
        res_mat = compute_grid(nf, kind, channel, args.order, eta_list, xi_list, args.cores)
        print(f"    done in {time.perf_counter() - start:.1f}s")

        for variation in variations:
            source_name = f"C{kind}{channel}_nf{nf}_var{variation}"
            body = res_mat[:, :, variation + 1].flatten(order="C").tolist()

            mod_name = stem_to_mod(source_name)
            rs_path = os.path.join(out_dir, mod_name + ".rs")
            rs_content = generate_rs(source_name, xi_list, eta_list, body, args.kx, args.ky, args.spline)

            with open(rs_path, "w") as fh:
                fh.write(rs_content)

            stems.append(mod_name)
            print(f"    -> {os.path.basename(rs_path)}")

    mod_rs_path = os.path.join(out_dir, "mod.rs")
    mod_lines = ["// Auto-generated by gen_rs_from_adani.py — do not edit by hand.\n"]
    mod_lines += [f"pub mod {s};\n" for s in stems]
    with open(mod_rs_path, "w") as fh:
        fh.writelines(mod_lines)

    print(f"\n  mod.rs  ({len(stems)} module{'s' if len(stems) != 1 else ''})")


if __name__ == "__main__":
    main()
