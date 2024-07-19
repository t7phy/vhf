import os

# List of source files
source_files = []

# Directories to search for files
directories = ["eh/unpol/nnlo/cl", "eh/unpol/nnlo/ct"]
# Get the absolute path of the current directory
current_directory = os.getcwd()

# Iterate over each directory
for directory in directories:
    # Get the absolute path of the directory
    directory_path = os.path.join(current_directory, directory)
    # Get all files in the directory
    files = os.listdir(directory_path)
    # Add the files to the source_files list with relative path
    source_files.extend(
        [os.path.join(directory, file) for file in files if file[0] == "c"]
    )

# Target file
target_file = current_directory + "/eh/unpol/nnlo/all_nnlo.py"

# Open the target file in write mode
with open(target_file, "w") as tf:
    # Write the specified lines to the beginning of the target file
    tf.write("from configs.eh import *\n\nLMUR = 1\nLMUF = 1\nLMUA = 1\n\n")
    # Iterate over each source file
    for source_file in source_files:

        # Open the source file in read mode
        with open(source_file, "r") as sf:
            # Skip the first 6 lines
            for _ in range(6):
                next(sf)
            # Copy the rest of the contents to the target file
            for line in sf:
                tf.write(line)
