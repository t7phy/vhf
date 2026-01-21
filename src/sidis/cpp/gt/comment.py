import os
import re
from collections import defaultdict

def update_cpp_files():
    # Patterns for detection
    header_pattern = r"Branch extraction report:"
    line_regex = re.compile(r"-\s+([A-Z0-9_]+):\s+([\d, ]+)")
    duplicate_check = "Inverted Branch Report (By Number):"

    files = [f for f in os.listdir('.') if f.endswith('.cpp')]

    if not files:
        print("No .cpp files found.")
        return

    for filename in files:
        with open(filename, 'r') as f:
            content = f.read()

        # Skip if the file doesn't have the report or already has the inverted version
        if header_pattern not in content:
            continue
        if duplicate_check in content:
            print(f"Skipping {filename}: Inverted report already exists.")
            continue

        # Process the specific file's content
        inverted_map = defaultdict(list)
        matches = line_regex.findall(content)
        
        if not matches:
            continue

        for key, values_str in matches:
            values = [v.strip() for v in values_str.split(',') if v.strip()]
            for val in values:
                inverted_map[val].append(key)

        # Build the new comment block
        output_lines = ["\n/*", f"  {duplicate_check}"]
        for num in sorted(inverted_map.keys()):
            keys_list = ", ".join(sorted(inverted_map[num]))
            output_lines.append(f"  - {num}: {keys_list}")
        output_lines.append("*/\n")
        
        inverted_block = "\n".join(output_lines)

        # Append to the file
        with open(filename, 'a') as f:
            f.write(inverted_block)
        
        print(f"Successfully updated {filename}")

if __name__ == "__main__":
    update_cpp_files()