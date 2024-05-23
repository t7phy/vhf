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

# import sidisprocessed.step1pol.original.python.c1pg2qeq as ordered_c1pg2qeq
# import sidisprocessed.step1pol.original.python.c1pq2geq as ordered_c1pq2geq
# import sidisprocessed.step1pol.original.python.c1pq2qeq as ordered_c1pq2qeq
# import sidisprocessed.step1pol.original.python.c2pg2geq as ordered_c2pg2geq
# import sidisprocessed.step1pol.original.python.c2pg2qeq as ordered_c2pg2qeq
# import sidisprocessed.step1pol.original.python.c2pq2geq as ordered_c2pq2geq
# import sidisprocessed.step1pol.original.python.c2pq2qbeq as ordered_c2pq2qbeq
# import sidisprocessed.step1pol.original.python.c2pq2qeq as ordered_c2pq2qeq
# import sidisprocessed.step1pol.original.python.c2pq2qeqp as ordered_c2pq2qeqp
# import sidisprocessed.step1pol.original.python.c2pq2qpbes as ordered_c2pq2qpbes
# import sidisprocessed.step1pol.original.python.c2pq2qpeq as ordered_c2pq2qpeq

# modules = [
#     "c1pg2qeq",
#     "c1pq2geq",
#     "c1pq2qeq",
#     "c2pg2geq",
#     "c2pg2qeq",
#     "c2pq2geq",
#     "c2pq2qbeq",
#     "c2pq2qeq",
#     "c2pq2qeqp",
#     "c2pq2qpbes",
#     "c2pq2qpeq",
#     "c2pq2qpeqp",
#     "c2pq2qpes",
# ]

# for module in modules:
#     globals()[f"ordered_{module}"] = __import__(
#         f"sidisprocessed.step1pol.ordered.python.{module}", fromlist=[""]
#     )
#     globals()[f"original_{module}"] = __import__(
#         f"sidisprocessed.step1pol.original.python.{module}", fromlist=[""]
#     )

import sidisprocessed.step1pol.ordered.python as ordered


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
            ("(a+b(c)d)i(e+f(g)h)", ["(a+b(c)d)", "i", "(e+f(g)h)"]),
            (
                "(a+b(c)d)i(e+f(g)h)j(e+f(g)h)k",
                ["(a+b(c)d)", "i", "(e+f(g)h)", "j", "(e+f(g)h)", "k"],
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
        a = 1.5
        b = 2
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
            ("LMUA*LMUF*pow(\nNC,+(-1)*1)", 2, True),
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
                "(LMUR + LMUA)(a+b) + (LMUR +a)e(LMUA+b)+(LMUR+d) + LMUA*LMUR(a+b) + c",
                {
                    "Uncategorized": ["(LMUR+LMUA)(a+b)"],
                    "000": ["c"],
                    "100": ["(LMUR+d)"],
                    "101": ["(LMUR+a)e(LMUA+b)", "LMUA*LMUR(a+b)"],
                },
            ),
            (
                "7. / 18. * pow(z,-1) * LMUA * CF + 1. / 3. * pow(z,-1) * pow(LMUA, 2) * CF + 2 * LMUA * CF * pow(NC,-1) + 10. / 3. * LMUA * CF + 1. / 4. * pow(LMUA, 2)",
                {
                    "002": [
                        "1. / 3. * pow(z,+(-1)*1) * pow(LMUA, 2) * CF",
                        "1. / 4. * pow(LMUA, 2)",
                    ],
                    "001": [
                        "7. / 18. * pow(z,+(-1)*1) * LMUA * CF",
                        "2 * LMUA * CF * pow(NC,+(-1)*1)",
                        "10. / 3. * LMUA * CF",
                    ],
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


class TestResults(unittest.TestCase):
    def test_same_result_per_func(self):
        assert True


if __name__ == "__main__":
    unittest.main()
