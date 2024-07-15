import os

# Define the specific if conditions to search for
if_conditions = [
    "if z < 1.-x and z < x:",
    "if z > 1.-x and z < x:",
    "if z < 1.-x and z > x:",
    "if z > 1.-x and z > x:",
    "if z < 1.-x:",
    "if z > 1.-x:",
    "if z != x and z != 1.-x:"
]

def replace_in_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    with open(file_path, "w") as file:
        for line in lines:
            # Check if the line contains any of the target if conditions
            if any(if_cond in line for if_cond in if_conditions):
                # Perform the replacement
                line = line.replace("1.-x", "round(1 - x, ndecimals)")
            file.write(line)

def find_and_replace(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):  # Assuming you're only interested in Python files
                replace_in_file(os.path.join(root, file))

# Replace 'your_directory_path' with the path to the directory containing your Python scripts
find_and_replace('/workspaces/vhf/eh/unpol')