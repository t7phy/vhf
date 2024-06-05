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
        return f'if "{x}" == order:'

    # Replace the string
    new_s = re.sub(pattern, replacement, s)

    return new_s


def add_rsl_function(func_name):

    # Lowercase the string

    new_func_name = func_name.lower()

    # Add _ after the first p
    new_func_name = re.sub(r"(p)", r"\1_", new_func_name, count=1)

    # Add _ before the first e
    new_func_name = re.sub(r"(e)", r"_\1", new_func_name, count=1)

    return f"""
def {new_func_name}(x, z, rsl, order,f={func_name}_DR0123_scheme):
    if rsl == "ll":
        f_DD = f(x, z, "D", "D", order)
        f_D0 = ln(1 - z) * f(x, z, "D", "0", order)
        f_D1 = 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "D", "1", order)
        f_D2 = 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "D", "2", order)
        f_00 = ln(1 - x) * ln(1 - z) * f(x, z, "0", "0", order)
        f_01 = ln(1 - x) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "0", "1", order)
        f_02 = ln(1 - x) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "0", "2", order)
        f_10 = 1 / 2 * pow(ln(1 - x), 2) * ln(1 - z) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - x), 2) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - x), 2) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "1", "2", order)
        f_20 = 1 / 3 * pow(ln(1 - x), 3) * ln(1 - z) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - x), 3) * 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - x), 3) * 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "2", "2", order)

        return f_DD + f_D0 + f_D1 + f_D2 + f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    elif rsl == "lr":
        f_DR = f(x, z, "D", "R", order)
        f_0R = ln(1 - x) * f(x, z, "0", "R", order)
        f_1R = 1 / 2 * pow(ln(1 - x), 2) * f(x, z, "1", "R", order)
        f_2R = 1 / 3 * pow(ln(1 - x), 3) * f(x, z, "2", "R", order)

        return f_DR + f_0R + f_1R + f_2R

    elif rsl == "rl":
        f_RD = f(x, z, "R", "D", order)
        f_R0 = ln(1 - z) * f(x, z, "R", "0", order)
        f_R1 = 1 / 2 * pow(ln(1 - z), 2) * f(x, z, "R", "1", order)
        f_R2 = 1 / 3 * pow(ln(1 - z), 3) * f(x, z, "R", "2", order)

        return f_RD + f_R0 + f_R1 + f_R2

    elif rsl == "rr":
        f_RR = f(x, z, "R", "R", order)

        return f_RR

    elif rsl == "rs":
        f_R0 = 1 / (1 - z) * f(x, z, "R", "0", order)
        f_R1 = ln(1 - z) / (1 - z) * f(x, z, "R", "1", order)
        f_R2 = pow(ln(1 - z), 2) / (1 - z) * f(x, z, "R", "2", order)

        return f_R0 + f_R1 + f_R2

    elif rsl == "sr":
        f_0R = 1 / (1 - x) * f(x, z, "0", "R", order)
        f_1R = ln(1 - x) / (1 - x) * f(x, z, "1", "R", order)
        f_2R = pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "R", order)

        return f_0R + f_1R + f_2R

    elif rsl == "ss":
        f_00 = 1 / ((1 - x) * (1 - z)) * f(x, z, "0", "0", order)
        f_01 = ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "0", "1", order)
        f_02 = pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "0", "2", order)
        f_10 = ln(1 - x) / ((1 - x) * (1 - z)) * f(x, z, "1", "0", order)
        f_11 = ln(1 - x) * ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "1", "1", order)
        f_12 = ln(1 - x) * pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "1", "2", order)
        f_20 = pow(ln(1 - x), 2) / ((1 - x) * (1 - z)) * f(x, z, "2", "0", order)
        f_21 = pow(ln(1 - x), 2) * ln(1 - z) / ((1 - x) * (1 - z)) * f(x, z, "2", "1", order)
        f_22 = pow(ln(1 - x), 2) * pow(ln(1 - z), 2) / ((1 - x) * (1 - z)) * f(x, z, "2", "2", order)

        return f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    elif rsl == "ls":
        f_D0 = 1 / (1 - z) * f(x, z, "D", "0", order)
        f_D1 = ln(1 - z) / (1 - z) * f(x, z, "D", "1", order)
        f_D2 = pow(ln(1 - z), 2) / (1 - z) * f(x, z, "D", "2", order)
        f_00 = ln(1 - x) / (1 - z) * f(x, z, "0", "0", order)
        f_01 = ln(1 - x) * ln(1 - z) / (1 - z) * f(x, z, "0", "1", order)
        f_02 = ln(1 - x) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "0", "2", order)
        f_10 = 1 / 2 * pow(ln(1 - x), 2) / (1 - z) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - x), 2) * ln(1 - z) / (1 - z) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - x), 2) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "1", "2", order)
        f_20 = 1 / 3 * pow(ln(1 - x), 3) / (1 - z) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - x), 3) * ln(1 - z) / (1 - z) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - x), 3) * pow(ln(1 - z), 2) / (1 - z) * f(x, z, "2", "2", order)

        return f_D0 + f_D1 + f_D2 + f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    elif rsl == "sl":
        f_0D = 1 / (1 - x) * f(x, z, "0", "D", order)
        f_1D = ln(1 - x) / (1 - x) * f(x, z, "1", "D", order)
        f_2D = pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "D", order)
        f_00 = ln(1 - z) / (1 - x) * f(x, z, "0", "0", order)
        f_01 = ln(1 - z) * ln(1 - x) / (1 - x) * f(x, z, "0", "1", order)
        f_02 = ln(1 - z) * pow(ln(1 - x), 2) / (1 - x) * f(x, z, "0", "2", order)
        f_10 = 1 / 2 * pow(ln(1 - z), 2) / (1 - x) * f(x, z, "1", "0", order)
        f_11 = 1 / 2 * pow(ln(1 - z), 2) * ln(1 - x) / (1 - x) * f(x, z, "1", "1", order)
        f_12 = 1 / 2 * pow(ln(1 - z), 2) * pow(ln(1 - x), 2) / (1 - x) * f(x, z, "1", "2", order)
        f_20 = 1 / 3 * pow(ln(1 - z), 3) / (1 - x) * f(x, z, "2", "0", order)
        f_21 = 1 / 3 * pow(ln(1 - z), 3) * ln(1 - x) / (1 - x) * f(x, z, "2", "1", order)
        f_22 = 1 / 3 * pow(ln(1 - z), 3) * pow(ln(1 - x), 2) / (1 - x) * f(x, z, "2", "2", order)

        return f_0D + f_1D + f_2D + f_00 + f_01 + f_02 + f_10 + f_11 + f_12 + f_20 + f_21 + f_22

    else:
        raise ValueError("Incorrect rsl choice, rsl must have a value of: 'll', 'lr', 'rl', 'rr', 'rs', 'sr', 'ss', 'ls' or 'sl'")
    """


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

            # Rename the function
            if "def " in line:
                func_name = re.search(r"def (.*?)(\(|:)", line).group(1)
                line = line.replace(func_name, func_name + "_DR0123_scheme")

            if "(inx,inz,cx,cz,Q,muR,muF,muA)" in line.replace(" ", ""):
                line = re.sub(
                    r"\(inx, inz, cx, cz,\s*Q, muR, muF, muA\)",
                    "(inx:float, inz:float, cx:str, cz:str, order:str, ndecimals=ndecimals, LMUR=LMUR, LMUF=LMUF, LMUA=LMUA)",
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

    # Add the general function with rsl_ordering
    if not func_name:
        raise ValueError("No function name found in the file")

    python_file.append(add_rsl_function(func_name))

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
