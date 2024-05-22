import unittest
from categorizing import (
    split_expression,
    split_to_individual_terms,
    replace_minus_sign,
    revert_minus_sign,
    find_order,
    check_if_term_can_be_categorized,
    split_to_order,
    remove_var_n_semicolon,
)


class TestStringFunction(unittest.TestCase):
    def test_split_to_individual_termsf(self):
        test_cases = [
            ("a(b)c + d(e)f", ["a(b)c", "d(e)f"]),
            ("a(b(c)d+e(f)g)+h(i)j", ["a(b(c)d+e(f)g)", "h(i)j"]),
            ("a(b)c(d)e + f(g)h", ["a(b)c(d)e", "f(g)h"]),
            ("a(b(c)d+e(f)g)h(i)j + k(l)m", ["a(b(c)d+e(f)g)h(i)j", "k(l)m"]),
            ("(a+b(c)d)(e+f(g)h)i+j()", ["(a+b(c)d)(e+f(g)h)i", "j()"]),
        ]

        for i, (input_str, expected_output) in enumerate(test_cases):
            self.assertEqual(
                split_to_individual_terms(input_str),
                expected_output,
                f"Failed on case {i+1}: {input_str}",
            )

    def test_split_expression(self):
        test_cases = [
            ("(a+b(c)d)(e+f(g)h)", ["(a+b(c)d)", "(e+f(g)h)"]),
            ("(a+b(c)d)i(e+f(g)h)", ["(a+b(c)d)", "i(e+f(g)h)"]),
            (
                "(a+b(c)d)i(e+f(g)h)j(e+f(g)h)",
                ["(a+b(c)d)", "i(e+f(g)h)", "j(e+f(g)h)"],
            ),
        ]

        for i, (input_str, expected_output) in enumerate(test_cases):
            self.assertEqual(
                split_expression(input_str),
                expected_output,
                f"Failed on case {i+1}: {input_str}",
            )

    def test_replace_minus_sign(self):
        test_cases = [
            ("a-b", "a+(-1)*b"),
            ("a+b**-1", "a+b**+(-1)*1"),
            ("pow(b,-1)", "pow(b,+(-1)*1)"),
            ("a+b**(a-8)", "a+b**(a+(-1)*8)"),
        ]

        for i, (min_sign, plus_min_sign) in enumerate(test_cases):
            self.assertEqual(
                replace_minus_sign(min_sign),
                plus_min_sign,
                f"Failed on case {i+1}: {min_sign}",
            )
            self.assertEqual(
                revert_minus_sign(plus_min_sign),
                min_sign,
                f"Failed on case {i+1}: {min_sign}",
            )

    def test_evaluated_expressions_minus_sign(self):
        a = 2
        b = 4
        test_cases = [
            ("a-b", "a+(-1)*b"),
            ("a+b**-1", "a+b**+(-1)*1"),
            ("pow(b,-1)", "pow(b,+(-1)*1)"),
            ("a+b**(a-8)", "a+b**(a+(-1)*8)"),
        ]

        for i, (input_str, expected_str) in enumerate(test_cases):
            input_result = eval(input_str)
            expected_result = eval(expected_str)
            self.assertEqual(
                input_result, expected_result, f"Failed on case {i+1}: {input_str}"
            )

    def test_find_order(self):
        test_cases = [
            ("LMUA + b*pow(LMUA,3)*pow(LMUB,2) + pow(LMUA,2) + LMUA", "A", 7),
            ("LMUA + b*pow(LMUA,3)*pow(LMUB,2) + pow(LMUA,2) + LMUA", "B", 2),
            ("LMUA + b*pow(LMUA,3)*pow(LMUB,2) + pow(LMUA,2) + LMUA", "C", 0),
        ]

        for i, (s, x, expected_sum) in enumerate(test_cases):
            result = find_order(s, x)
            self.assertEqual(result, expected_sum, f"Failed on case {i+1}: {s}")

    def test_check_if_term_can_be_categorized(self):
        test_cases = [
            ("(LMUR + LMUA)(a+b)", 2, False),
            ("(a+(LMUR + LMUA))(a+b)", 2, False),
            ("(LMUR +a)e(LMUA+b)", 2, True),
            ("1./2.*pow(z,-1)*LMUA*LMUF*pow(\nNC,-1)", 2, True),
            # test below should return False since it is an edge case that
            # the current algorithm cannot categorize (would require seperation of a*() into [a,()])
            ("LMUA*LMUF*pow(\nNC,+(-1)*1)", 2, False),
        ]
        for i, (term, sum_order, expected_result) in enumerate(test_cases):
            result = check_if_term_can_be_categorized(term, sum_order)
            self.assertEqual(result, expected_result, f"Failed on case {i+1}: {term}")

    def test_split_to_order(self):
        test_cases = [
            (
                "LMUA + b*pow(LMUA,3)*pow(LMUR,2) + pow(LMUR,2) + LMUA*b +c",
                {
                    "000": ["c"],
                    "001": ["LMUA", "LMUA*b"],
                    "200": ["pow(LMUR,2)"],
                    "203": ["b*pow(LMUA,3)*pow(LMUR,2)"],
                },
            ),
            (
                "(LMUR + LMUA)(a+b) + (LMUR +a)e(LMUA+b)+(LMUR+d) + c",
                {
                    "Uncategorized": ["(LMUR+LMUA)(a+b)"],
                    "000": ["c"],
                    "100": ["(LMUR+d)"],
                    "101": ["(LMUR+a)e(LMUA+b)"],
                },
            ),
        ]

        for i, (s, expected_result) in enumerate(test_cases):
            result = split_to_order(s)
            self.assertEqual(result, expected_result, f"Failed on case {i+1}: {s}")

    def test_remove_res(self):
        test_cases = [
            ("ares=bres+=cres+=d", "res", "abcd"),
            ("res+=1ad3+332", "res", "1ad3+332"),
            ("res+=1ad3+332;\n", "res", "1ad3+332\n"),
            ("atmp=btmp+=ctmp+=d", "tmp", "abcd"),
            ("tmp+=1ad3+332", "tmp", "1ad3+332"),
            ("tmp+=1ad3+332;\n", "tmp", "1ad3+332\n"),
        ]

        for i, (s, var, expected_result) in enumerate(test_cases):
            result = remove_var_n_semicolon(s, var)
            self.assertEqual(result, expected_result, f"Failed on case {i+1}: {s}")


if __name__ == "__main__":
    unittest.main()
