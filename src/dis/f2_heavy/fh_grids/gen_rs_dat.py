#!/usr/bin/env python3
"""
gen_dat_rs.py

For every .dat file in a given directory, writes a self-contained .rs file
containing:

  · Three pub static arrays (X, Y, BODY)
  · A OnceLock-backed accessor function that builds and caches the
    RectBivariateSpline on first call, so the spline is constructed exactly
    once regardless of how many times the integrand is evaluated.

Usage
-----
    python gen_dat_rs.py <dat_dir> [out_dir]
        [--kx KX] [--ky KY]
        [--spline IMPORT_PATH]

    dat_dir         directory containing .dat files (scanned non-recursively)
    out_dir         where to write .rs files (default: same as dat_dir)
    --kx, --ky      spline degrees (default: 3, reproducing scipy's bicubic)
    --spline        fully-qualified Rust path to RectBivariateSpline
                    (default: crate::core::interpolation::RectBivariateSpline)

Example
-------
    python gen_dat_rs.py data/ src/core/ \\
        --kx 3 --ky 3 \\
        --spline crate::core::interpolation::RectBivariateSpline

Each generated file is a self-contained Rust module.  Drop it into your src/
tree and declare it with `pub mod <stem>;`.
"""

import argparse
import os
import re
import sys


# ── parsing ────────────────────────────────────────────────────────────────────

def parse_dat(path: str) -> tuple[list[float], list[float], list[float]]:
    """
    Read a whitespace-separated 2-D .dat file and return (x, y, body).

    Expected layout:
        CORNER  y0      y1      y2  ...
        x0      z[0,0]  z[0,1]  z[0,2]  ...
        x1      z[1,0]  z[1,1]  z[1,2]  ...
        ...

    Returns
    -------
    x    : first column, rows 1..   (row-axis coordinates)
    y    : first row,    cols 1..   (column-axis coordinates)
    body : remaining values, row-major;  body[i * len(y) + j] == f(x[i], y[j])
    """
    rows: list[list[float]] = []

    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append([float(tok) for tok in line.split()])

    if len(rows) < 2:
        raise ValueError(f"need at least 2 rows, found {len(rows)}")
    if len(rows[0]) < 2:
        raise ValueError(f"need at least 2 columns, found {len(rows[0])}")

    ncols = len(rows[0])
    for i, row in enumerate(rows):
        if len(row) != ncols:
            raise ValueError(
                f"row {i} has {len(row)} columns, expected {ncols} "
                f"— file is not rectangular"
            )

    x    = [row[0] for row in rows[1:]]
    y    = rows[0][1:]
    body = [v for row in rows[1:] for v in row[1:]]

    return x, y, body


# ── formatting ─────────────────────────────────────────────────────────────────

def fmt_f64(v: float) -> str:
    """
    Format a Python float as a Rust f64 literal.

    Python 3's repr() uses the Ryu algorithm — the shortest decimal string
    guaranteed to round-trip exactly to the same IEEE 754 bit pattern.
    Rust's float parser accepts the same format (including scientific notation
    like 1e-10), so no precision is ever lost.
    """
    if not (v == v) or v in (float("inf"), float("-inf")):
        raise ValueError(f"non-finite value {v!r} cannot be a Rust literal")
    return f"{v!r}f64"


def fmt_array_body(values: list[float], columns: int = 8) -> str:
    """Interior of a Rust array literal, wrapped at `columns` values per line."""
    lines = []
    for start in range(0, len(values), columns):
        chunk = values[start : start + columns]
        lines.append("    " + ", ".join(fmt_f64(v) for v in chunk) + ",")
    return "\n".join(lines)


def stem_to_prefix(stem: str) -> str:
    """
    Convert a filename stem to a valid uppercase Rust identifier prefix.
    e.g.  "my-grid.2"  →  "MY_GRID_2"
    """
    ident = re.sub(r"[^A-Za-z0-9]", "_", stem).upper()
    if ident and ident[0].isdigit():
        ident = "_" + ident
    return ident


def stem_to_fn(stem: str) -> str:
    """Lowercase snake_case function name from a filename stem."""
    fn = re.sub(r"[^A-Za-z0-9]", "_", stem).lower()
    if fn and fn[0].isdigit():
        fn = "_" + fn
    return fn + "_spline"


def stem_to_mod(stem: str) -> str:
    """
    Convert a filename stem to a valid Rust module name (lowercase snake_case).
    e.g.  "cg1-F2_AA-bulk"  →  "cg1_f2_aa_bulk"
    """
    mod = re.sub(r"[^A-Za-z0-9]", "_", stem).lower()
    if mod and mod[0].isdigit():
        mod = "_" + mod
    return mod


# ── code generation ────────────────────────────────────────────────────────────

def generate_rs(
    source_name:  str,
    x:            list[float],
    y:            list[float],
    body:         list[float],
    kx:           int,
    ky:           int,
    spline_path:  str,
) -> str:
    """
    Produce the full contents of a .rs file for one .dat file.

    The file contains:
      · Three pub static arrays (PREFIX_X, PREFIX_Y, PREFIX_BODY)
      · A private OnceLock<RectBivariateSpline> static
      · A pub accessor fn that initialises the spline on first call only
    """
    stem   = os.path.splitext(source_name)[0]
    prefix = stem_to_prefix(stem)
    fn     = stem_to_fn(stem)
    ny     = len(y)

    # The last segment of the import path is the type name used in code.
    type_name = spline_path.rsplit("::", 1)[-1]

    return (
        f"// Generated from {source_name} — do not edit by hand.\n"
        f"//\n"
        f"// Grid:     {len(x)} × {ny}  ({len(body)} body values)\n"
        f"// Degrees:  kx = {kx},  ky = {ky}\n"
        f"// Indexing: {prefix}_BODY[i * {ny} + j] == f({prefix}_X[i], {prefix}_Y[j])\n"
        f"\n"
        f"use std::sync::OnceLock;\n"
        f"use {spline_path};\n"
        f"\n"
        f"// ── raw grid data {'─' * 58}\n"
        f"\n"
        f"/// Row-axis coordinates (x).\n"
        f"pub static {prefix}_X: [f64; {len(x)}] = [\n"
        f"{fmt_array_body(x)}\n"
        f"];\n"
        f"\n"
        f"/// Column-axis coordinates (y).\n"
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
        description="Generate Rust static arrays + spline accessor from .dat files."
    )
    parser.add_argument("dat_dir",        help="directory containing .dat files")
    parser.add_argument("out_dir",        nargs="?", help="output directory (default: dat_dir)")
    parser.add_argument("--kx",           type=int, default=3, help="spline degree along x (default: 3)")
    parser.add_argument("--ky",           type=int, default=3, help="spline degree along y (default: 3)")
    parser.add_argument("--spline",       default="crate::core::scits::rect_bivariate_spline::RectBivariateSpline",
                        help="fully-qualified Rust path to RectBivariateSpline")
    args = parser.parse_args()

    dat_dir = args.dat_dir
    out_dir = args.out_dir or dat_dir

    if not os.path.isdir(dat_dir):
        print(f"Error: {dat_dir!r} is not a directory", file=sys.stderr)
        sys.exit(1)

    if not (1 <= args.kx <= 5 and 1 <= args.ky <= 5):
        print("Error: kx and ky must be in 1..=5", file=sys.stderr)
        sys.exit(1)

    os.makedirs(out_dir, exist_ok=True)

    dat_files = sorted(f for f in os.listdir(dat_dir) if f.endswith(".dat"))
    if not dat_files:
        print(f"No .dat files found in {dat_dir!r}", file=sys.stderr)
        sys.exit(1)

    stems = []

    for filename in dat_files:
        dat_path = os.path.join(dat_dir, filename)
        stem     = os.path.splitext(filename)[0]
        mod_name = stem_to_mod(stem)
        rs_path  = os.path.join(out_dir, mod_name + ".rs")

        try:
            x, y, body = parse_dat(dat_path)
        except (ValueError, OSError) as exc:
            print(f"Error: {dat_path}: {exc}", file=sys.stderr)
            sys.exit(1)

        rs_content = generate_rs(filename, x, y, body, args.kx, args.ky, args.spline)

        with open(rs_path, "w") as fh:
            fh.write(rs_content)

        stems.append(mod_name)
        label = os.path.basename(rs_path)
        if mod_name != stem:
            label += f"  (sanitised from {stem}.rs)"
        print(f"  {filename:30s}  →  {label}"
              f"  ({len(x)}×{len(y)} grid, {len(body)} body values)")

    # Write mod.rs listing every generated module.
    mod_rs_path = os.path.join(out_dir, "mod.rs")
    mod_lines   = ["// Auto-generated by gen_dat_rs.py — do not edit by hand.\n"]
    mod_lines  += [f"pub mod {s};\n" for s in stems]

    with open(mod_rs_path, "w") as fh:
        fh.writelines(mod_lines)

    print(f"\n  mod.rs  ({len(stems)} module{'s' if len(stems) != 1 else ''})")


if __name__ == "__main__":
    main()