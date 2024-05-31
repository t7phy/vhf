import os
import re
from change_cpp_to_python import (
    convert_python_to_cpp,
    convert_to_our_library,
    format_file_with_black,
)
from Problem_test_failing.python.c2pg2qeq_ordered import C2Pg2qEq as C2Pg2qEqOrdered
from Problem_test_failing.python.c2pg2qeq_original import C2Pg2qEq as C2Pg2qEqOriginal

# Description:
# The original code is a C++ code that has been converted to Python. The original code is in the file c2pg2qeq_original.cpp.
# Depending on the order of tmp += we get different results, see comments in the original cpp file.
# Note: to run the file properly, move it to the root directory of the project.


create_files_flag = True
dir = "./Problem_test_failing"
files = ["c2pg2qeq_original.cpp", "c2pg2qeq_ordered.cpp"]

if create_files_flag:
    # Convert all the .cpp files to python files
    for filename in files:
        if filename.endswith(".cpp"):
            convert_python_to_cpp(filename, dir)
            # os.remove("polarized/" + filename)

    files = os.listdir(dir + "/python")
    # Convert order to if statement and/or use our library conventions
    for filename in files:
        if filename.endswith(".py") and not "__init__" in filename:
            convert_to_our_library(dir + "/python/" + filename)
            # format_file_with_black(dir + "/python/" + filename, 400)

# Compare the results
inx = 0.9
inz = 0.1
cx = "R"
cz = "R"
Q = 1.0
muR = 1.0
muF = 1.0
muA = 1.0

result_ordered = C2Pg2qEqOrdered(inx, inz, cx, cz, Q, muR, muF, muA, "all", 10)
result_original = C2Pg2qEqOriginal(inx, inz, cx, cz, Q, muR, muF, muA, "all", 10)

print(
    f"Result ordered is {result_ordered}\nResult original is {result_original}\nCombined={result_ordered-result_original}"
)
