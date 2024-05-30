import unittest
from change_cpp_to_python import (
    cpp_to_python_func_def,
    cpp_to_python_if_statement,
    convert_if_statement_to_include_round,
)

import re


class TestConversion(unittest.TestCase):
    def test_cpp_to_python_func_def_conversion(self):
        cpp_signature = "double C1Pq2gEq(double inx, double inz, std::string cx, \nstd::string cz, double Q, double muR, double muF, double muA)"
        expected_python_signature = "def C1Pq2gEq(inx, inz, cx, cz, Q, muR, muF, muA):"

        self.assertEqual(
            cpp_to_python_func_def(cpp_signature), expected_python_signature
        )

    def test_cpp_to_python_if_statement_conversion(self):
        cpp_code = 'if (cx == "D" && cz == "D")'
        expected_python_code = 'if cx == "D" && cz == "D":'

        self.assertEqual(cpp_to_python_if_statement(cpp_code), expected_python_code)

    def test_convert_cpp_to_python_round_in_if_statement(self):
        # Test 1
        cpp_code1 = "if z != x and k != y:"
        expected_python_code1 = "if round(z, ndecimals) != round(x, ndecimals) and round(k, ndecimals) != round(y, ndecimals):"
        self.assertEqual(
            convert_if_statement_to_include_round(cpp_code1),
            expected_python_code1,
        )

        # Test 2
        cpp_code2 = 'if cx == "D" and cz == "D":'
        expected_python_code2 = 'if cx == "D" and cz == "D":'
        self.assertEqual(
            convert_if_statement_to_include_round(cpp_code2),
            expected_python_code2,
        )


if __name__ == "__main__":
    unittest.main()
