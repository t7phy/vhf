import os
import glob
import shutil
import re

def optimize_pow(match):
    """
    Regex callback to convert pow(VAR, INT) into explicit multiplication.
    """
    var = match.group(1)
    power = int(match.group(2))
    
    if power == 2:
        return f"({var} * {var})"
    elif power == 3:
        return f"({var} * {var} * {var})"
    elif power == 4:
        return f"({var} * {var} * {var} * {var})"
    elif power == -1:
        return f"(1.0 / {var})"
    elif power == -2:
        return f"(1.0 / ({var} * {var}))"
    elif power == -3:
        return f"(1.0 / ({var} * {var} * {var}))"
    else:
        # Fallback to Rust's native integer-power method (which is hardware-optimized)
        return f"{var}.powi({power})"

def stabilize_and_optimize(directory="."):
    # 1. Algebraic Stabilizations (Now using native Rust .powi(2) for speed)
    replacements = {
        "1.0 + x - mysqrt(1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2))": 
        "4.0 * x * z / (1.0 + x + mysqrt((1.0 - x).powi(2) + 4.0 * x * (1.0 - z)))",

        "1.0 + 4.0 * x - 8.0 * x * z + 6.0 * pow(x, 2) - 16.0 * pow(x, 2) * z + 16.0 * pow(x, 2) * pow(z, 2) + 4.0 * pow(x, 3) - 8.0 * pow(x, 3) * z + pow(x, 4)": 
        "((1.0 - x).powi(2) + 4.0 * x * (1.0 - z)).powi(2)",
        
        "1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)": 
        "(1.0 - x).powi(2) + 4.0 * x * (1.0 - z)",

        "1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)": 
        "(1.0 - x - z).powi(2)",

        "pow(z, 2) - 2.0 * x * z + pow(x, 2)": 
        "(x - z).powi(2)",

        "1.0 - 2.0 * x + pow(x, 2)": "(1.0 - x).powi(2)",
        "1.0 - 2.0 * z + pow(z, 2)": "(1.0 - z).powi(2)"
    }

    # Regex to find `pow(variable, integer)` where variable is alphanumeric (x, z, NQCD, pi)
    pow_regex = re.compile(r"pow\(([a-zA-Z0-9_]+),\s*(-?\d+)\)")

    search_pattern = os.path.join(directory, "**/*.rs")
    rust_files = glob.glob(search_pattern, recursive=True)

    files_fixed = 0

    for filepath in rust_files:
        if filepath.endswith("_old.rs"):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                code = f.read()
            except UnicodeDecodeError:
                continue 

        # Check if file needs either algebraic fixing OR power optimization
        needs_algebra = any(bad_math in code for bad_math in replacements)
        needs_pow_opt = bool(pow_regex.search(code))

        if needs_algebra or needs_pow_opt:
            old_filepath = filepath[:-3] + "_old.rs"
            shutil.move(filepath, old_filepath)
            
            # Apply algebraic stabilizing
            for bad_math, good_math in replacements.items():
                code = code.replace(bad_math, good_math)
                
            # Apply `pow()` optimizations
            code = pow_regex.sub(optimize_pow, code)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
                
            print(f"Optimized: {filepath}")
            files_fixed += 1

    print(f"Done! Optimized {files_fixed} files.")

if __name__ == "__main__":
    stabilize_and_optimize(".")