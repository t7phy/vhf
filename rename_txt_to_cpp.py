import os


def cpp_to_python_func_def(cpp_signature):
    # Remove the 'double' return type from the C++ signature
    cpp_signature = cpp_signature.replace("double ", "")

    # Remove exrtra \n
    cpp_signature = cpp_signature.replace("\n", "")

    # Replace C++ syntax with Python syntax
    python_signature = cpp_signature.replace("std::string ", "")
    python_signature = "def " + python_signature + ":"

    return python_signature


def cpp_to_python_if_statement(cpp_code):
    # Replace C++ if statement syntax with Python if statement syntax
    if "if (" in cpp_code:
        python_code = cpp_code.replace("if (", "if ")
        python_code = python_code.replace(")", ":")
    else:
        python_code = cpp_code

    return python_code


def replace_cpp_with_python_remove_redundancies(cpp_code):
    python_code = cpp_code.replace("std::string ", "")
    python_code = python_code.replace("double ", "")
    python_code = python_code.replace(";", "")
    python_code = python_code.replace("{", "")
    python_code = python_code.replace("}", "")

    return python_code


def replace_cpp_with_python_replace_ensure_closed_decleration(cpp_code):
    """
    Ensure that a = b; is replaced with a = (b) t to tackle multiple lines in b.
    """
    python_code = cpp_code.replace(" = ", " = (")
    python_code = python_code.replace("+=", "+= (")
    if not "return" in cpp_code:
        python_code = python_code.replace(";", ")")

    return python_code


def replace_cpp_with_python_replace_easy_char(cpp_code):
    python_code = cpp_code.replace("&&", "and")
    python_code = python_code.replace("||", "or")
    python_code = python_code.replace("//", "#")

    return python_code


def convert_python_to_cpp(
    file_name, folder_path, cpp_folder_name="cpp", python_folder_name="python"
):
    # Read the file line by line
    file_path = folder_path + f"/{cpp_folder_name}/{file_name}"
    python_file = list()
    with open(file_path, "r") as file:
        def_line = str()

        for i, line in enumerate(file):
            if i == 0:
                def_line = line
            elif i == 1:
                def_line += line
                python_file.append(cpp_to_python_func_def(def_line))
            else:
                python_line = replace_cpp_with_python_replace_ensure_closed_decleration(
                    line
                )
                python_line = replace_cpp_with_python_remove_redundancies(python_line)
                python_line = replace_cpp_with_python_replace_easy_char(python_line)
                python_line = cpp_to_python_if_statement(python_line)
                python_file.append(python_line)

    # Remove the .cpp extension from the file name
    file_name = file_name.split(".")[0] + ".py"
    file_path = folder_path + f"/{python_folder_name}/{file_name}"

    with open(file_path, "w") as file:
        for line in python_file:
            file.write(line)


# Get all files in the current directory
dir = "./sidisprocessed/step1pol/original"
files = os.listdir(dir + "/cpp")
rename_txt_flag = False

if rename_txt_flag:
    # Iterate over all files
    for filename in files:
        # Check if the current file is a text file
        if filename.endswith(".txt"):
            # Get the base name of the file (without the extension)
            base = os.path.splitext(filename)[0]
            # Rename the file to have a .cpp extension
            os.rename("polarized/" + filename, "polarized/" + base + ".cpp")

# Convert all the .cpp files to python files
for filename in files:
    if filename.endswith(".cpp"):
        convert_python_to_cpp(filename, dir)
        # os.remove("polarized/" + filename)
