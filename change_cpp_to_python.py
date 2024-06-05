import os
import re
import subprocess


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
    python_code = python_code.replace(" +=", " += (")
    if not "return" in cpp_code:
        python_code = python_code.replace(";", ")")

    return python_code


def replace_cpp_with_python_replace_easy_char(cpp_code):
    python_code = cpp_code.replace("&&", "and")
    python_code = python_code.replace("||", "or")
    python_code = python_code.replace("//", "#")

    return python_code


def convert_if_statement_to_include_round(s):
    indent = re.split(r"if", s)[0]
    s = s.strip()
    # Replace C++ syntax with Python syntax
    parts = re.split(r" == | and | \|\| | or | != | < | > | <= | >= |if |:", s)
    parts = [k for k in parts if k]

    # Replace C++ syntax with Python syntax
    if len(parts) > 1:
        for i in range(0, len(parts), 2):
            x = parts[i]
            y = parts[i + 1]
            if '"' in x or "'" in x or '"' in y or "'" in y:
                continue
            else:
                parts[i] = f"round({x}, ndecimals)"
                parts[i + 1] = f"round({y}, ndecimals)"

    # Join the parts
    delimters = re.findall(r" == | and | \|\| | or | != | < | > | <= | >= |if |:", s)

    python_code = indent
    for i in range(len(parts)):
        python_code += delimters[i] + parts[i]

    python_code += delimters[-1] + "\n"
    return python_code


def convert_cpp_to_python(file_name, folder_path, cpp_folder_name="cpp", python_folder_name="python"):
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
                python_line = replace_cpp_with_python_replace_ensure_closed_decleration(line)
                python_line = replace_cpp_with_python_remove_redundancies(python_line)
                python_line = replace_cpp_with_python_replace_easy_char(python_line)
                python_line = cpp_to_python_if_statement(python_line)
                python_file.append(python_line)
                a = 1

    # Remove the .cpp extension from the file name
    file_name = file_name.split(".")[0] + ".py"
    file_path = folder_path + f"/{python_folder_name}/{file_name}"

    with open(file_path, "w") as file:
        for line in python_file:
            file.write(line)


def replace_order_with_if(s):
    # The pattern to match
    pattern = r"# Order (\d+):"

    # The replacement function
    def replacement(match):
        x = match.group(1)
        return f'if ("{x}" in orders):'

    # Replace the string
    new_s = re.sub(pattern, replacement, s)

    return new_s


def convert_to_our_library(file_path):
    # Read the file line by line
    python_file = list()
    add_indendt_flag = False
    tmp_flag = False
    with open(file_path, "r") as file:
        for i, line in enumerate(file):

            # Ignore parts of the settings from import statements
            if i > 2 and i < 13:
                continue

            if "(inx,inz,cx,cz,Q,muR,muF,muA)" in line.replace(" ", ""):
                line = re.sub(
                    r"\(inx, inz, cx, cz,\s*Q, muR, muF, muA\)",
                    "(inx, inz, cx, cz, orders:list, ndecimals=ndecimals, Q=Q, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA)",
                    line,
                )
            if "log(" in line:
                line = line.replace("log(", "ln(")
            if "mysqrt(" in line:
                line = line.replace("mysqrt(", "sqrt(")
            if add_indendt_flag and "+=" in line and not (tmp_flag and "res" in line):
                line = "\t" + line
            else:
                add_indendt_flag = False
            if "tmp" in line:
                tmp_flag = True
            else:
                tmp_flag = False
            if "# Order" in line:
                line = replace_order_with_if(line)
                add_indendt_flag = True
            if "if" in line:
                line = convert_if_statement_to_include_round(line)
            python_file.append(line)

    # Add the import statements at the beginning
    import_statements = ["from configs.eh import *\n"]

    # Add the import statements at the beginning
    python_file = import_statements + python_file

    # Store the new file
    with open(file_path, "w") as file:
        for line in python_file:
            file.write(line)


def format_file_with_black(file_path, line_length):
    # Run the black command
    subprocess.run(["black", f"--line-length={line_length}", file_path], check=True)


if __name__ == "__main__":
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
            convert_cpp_to_python(filename, dir)
            # os.remove("polarized/" + filename)

    files = os.listdir(dir + "/python")
    # Convert order to if statement and/or use our library conventions
    for filename in files:
        if filename.endswith(".py") and not "__init__" in filename:
            convert_to_our_library(dir + "/python/" + filename)
            format_file_with_black(dir + "/python/" + filename, 400)
