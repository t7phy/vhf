import os
import glob
import shutil

def stabilize_rust_codebase(directory="."):
    # Dictionary of exact catastrophic cancellations mapped to their factored forms.
    # Ordered largest to smallest to avoid substring collision bugs.
    replacements = {
        "1.0 + 4.0 * x - 8.0 * x * z + 6.0 * pow(x, 2) - 16.0 * pow(x, 2) * z + 16.0 * pow(x, 2) * pow(z, 2) + 4.0 * pow(x, 3) - 8.0 * pow(x, 3) * z + pow(x, 4)": 
        "pow(pow(1.0 - x, 2) + 4.0 * x * (1.0 - z), 2)",
        
        "1.0 + 2.0 * x - 4.0 * x * z + pow(x, 2)": 
        "(pow(1.0 - x, 2) + 4.0 * x * (1.0 - z))",

        "1.0 - 2.0 * z + pow(z, 2) - 2.0 * x + 2.0 * x * z + pow(x, 2)": 
        "pow(1.0 - x - z, 2)",

        "pow(z, 2) - 2.0 * x * z + pow(x, 2)": 
        "pow(x - z, 2)",

        "1.0 - 2.0 * x + pow(x, 2)": "pow(1.0 - x, 2)",
        
        "1.0 - 2.0 * z + pow(z, 2)": "pow(1.0 - z, 2)"
    }

    # Find all .rs files in the directory and subdirectories
    # recursive=True allows it to dig into your src/ and internal/ folders
    search_pattern = os.path.join(directory, "**/*.rs")
    rust_files = glob.glob(search_pattern, recursive=True)

    files_fixed = 0

    for filepath in rust_files:
        # Skip files that have already been backed up to prevent double-processing
        if filepath.endswith("_old.rs"):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                code = f.read()
            except UnicodeDecodeError:
                # Skip over any non-text files that somehow got a .rs extension
                continue 

        # Check if any problematic math exists in this specific file
        needs_fixing = any(bad_math in code for bad_math in replacements)

        if needs_fixing:
            # 1. Generate the backup filename (e.g., FTC2q2qM_old.rs)
            # [:-3] slices off the ".rs" extension before appending the new suffix
            old_filepath = filepath[:-3] + "_old.rs"
            
            # 2. Rename the current file to act as our backup
            shutil.move(filepath, old_filepath)
            
            # 3. Do all the mathematical replacements in memory
            for bad_math, good_math in replacements.items():
                code = code.replace(bad_math, good_math)
                
            # 4. Write the stabilized code to the original filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
                
            print(f"Fixed: {filepath}")
            print(f"  -> Backup saved as: {os.path.basename(old_filepath)}\n")
            files_fixed += 1

    print(f"Done! Scanned {len(rust_files)} files, successfully stabilized {files_fixed} files.")

if __name__ == "__main__":
    # Run on the current directory by default. 
    # You can change "." to a specific path like "./src" if needed.
    stabilize_rust_codebase(".")