import unittest
from polarized_txt_to_python.rename_txt_to_cpp import (
    cpp_to_python_func_def,
    cpp_to_python_if_statement,
)


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


if __name__ == "__main__":
    unittest.main()
