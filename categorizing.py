import re


def contains_LMUx(s, x):
    """
    Check if the string s contains the substring "LMU" followed by x.

    Args:
        s (str): The string to search.
        x (str): The string to append to "LMU" and search for in s.

    Returns:
        bool: True if "LMU" + x is found in s, False otherwise.
    """
    return bool(re.search(r"LMU" + re.escape(x), s))


import re


def find_pow_terms(s, x):
    """
    Find all occurrences of "pow(LMUx, n)" in the string s and return the exponents n.

    Args:
        s (str): The string to search.
        x (str): The string to append to "LMU" and search for in s.

    Returns:
        list: A list of integers representing the exponents found.
    """
    # Define the pattern for "pow(LMUx, n)"
    pattern = r"pow\s*\(\s*LMU" + re.escape(x) + r"\s*,\s*([+-]?\d+)\s*\)"
    matches = re.findall(pattern, s)
    return [int(n) for n in matches]


def find_order(s, x):
    """
    Calculate the order of "LMUx" in the string s.

    Args:
        s (str): The string to search.
        x (str): The string to append to "LMU" and search for in s.

    Returns:
        int: The order of "LMUx" in s.
    """
    pow_terms = find_pow_terms(s, x)
    occurences_LMUx = s.count("LMU" + x)
    occurences_pow_LMUx = len(pow_terms)

    return occurences_LMUx - occurences_pow_LMUx + sum(pow_terms)


def split_string(s):
    first_paren = s.find("(")
    last_paren = s.rfind(")")

    if first_paren == -1 or last_paren == -1:
        return [s]  # No parentheses found, return the string as is

    return [s[:first_paren], s[first_paren : last_paren + 1], s[last_paren + 1 :]]


def split_expression(expression):
    """
    Split the expression on brackets.

    Args:
        expression (str): The expression to split.

    Returns:
        list: A list of strings representing the split terms.
    """
    # Split the expression on brackets
    split_on_brackets = [s.strip() for s in re.split(r"(?<=\()|(?<=\))", expression)]

    # Remove empty strings
    split_on_brackets = [s for s in split_on_brackets if s]

    # Check if the string is a standalone term, i.e. "()+()" and not(()+())
    split_on_term = list()
    term = ""
    for plus_term in split_on_brackets:
        term += plus_term
        n_lef_paren = term.count("(")
        n_right_paren = term.count(")")

        if n_lef_paren == n_right_paren:
            split_on_term.append(term)
            term = ""
        elif n_lef_paren > n_right_paren:
            continue
        elif n_lef_paren < n_right_paren:
            raise ValueError("Invalid input string, encountered )() situation.")

    # When there are single terms, split a(b)c into a, (b), c
    split_on_term = [term for s in split_on_term for term in split_string(s)]
    split_on_term = [s for s in split_on_term if s]

    return split_on_term


def split_to_individual_terms(input_str):
    """
    Split the input string on plus signs to individual terms.

    Args:
        input_str (str): The string to split.

    Returns:
        list: A list of strings representing the split terms.
    """
    # Split the input string on plus signs
    split_on_plus = [s.strip() for s in input_str.split("+")]

    # Check if the string is a standalone term, i.e. "()+()" and not(()+())
    split_on_term = list()
    term = ""
    for plus_term in split_on_plus:
        term += plus_term
        n_lef_paren = term.count("(")
        n_right_paren = term.count(")")

        if n_lef_paren == n_right_paren:
            split_on_term.append(term)
            term = ""
        elif n_lef_paren > n_right_paren:
            term += "+"
        elif n_lef_paren < n_right_paren:
            raise ValueError("Invalid input string, encountered )() situation.")

    return split_on_term


def replace_minus_sign(input_str):
    """
    Replace all minus signs in the input string with "+(-1)*".

    Args:
        input_str (str): The string to replace minus signs in.

    Returns:
        str: The input string with minus signs replaced.
    """
    return input_str.replace("-", "+(-1)*")


def revert_minus_sign(input_str):
    """
    Revert all occurrences of "+(-1)*" in the input string to minus signs.

    Args:
        input_str (str): The string to revert "+(-1)*" in.

    Returns:
        str: The input string with "+(-1)*" reverted to minus signs.
    """
    return input_str.replace("+(-1)*", "-")


def check_if_term_can_be_categorized(term: str, sum_order: int):
    """
    Checks if a term can be categorized based on the sum of the orders of the term.
    Currently known uncaterogized terms are of the shape a(LMUR + LMUA), or equivalent.
    Term: str, the term(s) to be checked.
    sum_order: int, the sum of the orders of the term.
    returns: bool, True if the term can be categorized, False otherwise.
    """
    if sum_order > 1 and "+" in term:
        sub_terms = split_expression(term)
        n_sub_terms = len(sub_terms)
        for sub_term in sub_terms:
            order_R = find_order(sub_term, "R")
            order_F = find_order(sub_term, "F")
            order_A = find_order(sub_term, "A")
            sum_order = order_R + order_F + order_A

            if n_sub_terms == 1 and sum_order > 1 and "+" in sub_term:
                return False
            elif n_sub_terms == 1:
                return True
            elif check_if_term_can_be_categorized(sub_term, sum_order):
                continue
            else:
                return False
        # If all sub_terms can be categorized, return True
        return True
    else:
        return True


def split_to_order(s: str):
    """
    Function aims to split all the terms in the string s into orders based of LMUR, LMUF, LMUA.
    In additition there is a category for terms that have to be determined by hand: uncategorized.
    Returns a dictionary with keys as the order and values as the terms.
    """
    # Ensure only plus sign is used
    s = s.replace("-", "+(-1)*")

    # Split the string into individual terms
    terms = split_to_individual_terms(s)

    # Put the terms into the respective order
    orders = dict()
    for term in terms:
        order_R = find_order(term, "R")
        order_F = find_order(term, "F")
        order_A = find_order(term, "A")

        sum_order = order_R + order_F + order_A

        # Check if the term can be categorized
        if check_if_term_can_be_categorized(term, sum_order):
            key = f"{order_R}{order_F}{order_A}"
            if key in orders:
                orders[key].append(term)
            else:
                orders[key] = [term]
        else:
            if "Uncategorized" in orders:
                orders["Uncategorized"].append(term)
            else:
                orders["Uncategorized"] = [term]

    return orders


def remove_var_n_semicolon(s, var):
    return (
        s.replace(f"{var}=", "")
        .replace(f"{var} =", "")
        .replace(f"{var}+=", "")
        .replace(f"{var} +=", "")
        .replace(";", "")
    )


def create_file_with_split_orders(s: str, output_file: str, var: str):
    """
    Function to create a file with the split orders.
    s: str, the string to be split.
    var: Variable name to be split, e.g. tmp or res.
    output_file: str, the file to write the output to.
    """
    # Remove res references, put in later
    s = remove_var_n_semicolon(s, var)
    orders = split_to_order(s)

    with open(output_file, "w") as f:
        f.write("// Split orders:\n")
        f.write(f"{var} = 0;\n")
        for order, terms in orders.items():
            f.write(f"// Order {order}:\n")
            f.write(f"{var} += ")
            for i, term in enumerate(terms):
                if i % 20 == 0 and i != 0:
                    f.write(f"0;\n{var} += ")
                term = revert_minus_sign(term)
                f.write(f"{term} + ")
            f.write("0;\n")


if __name__ == "__main__":
    output_file = "split_orders.txt"
    s = """
    res = 1169. / 54. * pow(z, -1) * CF * NC + 4. / 3. * pow(z, -1) * CF * NC * pow(rln2, 3) - 9. / 2. * pow(z, -1) * LMUA * CF * pow(NC, -1) + 55. / 18. * pow(z, -1) * LMUA * CF * NC + 2. / 3. * pow(z, -1) * LMUA * LMUR * CF * NF - 11. / 3. * pow(z, -1) * LMUA * LMUR * CF * NC - 3. / 2. * pow(z, -1) * LMUA * LMUF * CF * pow(NC, -1) + 3. / 2. * pow(z, -1) * LMUA * LMUF * CF * NC - 2. / 3. * pow(z, -1) * pow(LMUA, 2) * CF * NF - 3. / 2. * pow(z, -1) * pow(LMUA, 2) * CF * NC + 3 * CF * pow(NC, -1) - 295. / 18. * CF * NC + 4. / 3. * CF * NC * pow(rln2, 3) + 17. / 4. * LMUA * CF * pow(NC, -1) - 95. / 12. * LMUA * CF * NC - 2. / 3. * LMUA * LMUR * CF * NF + 11. / 3. * LMUA * LMUR * CF * NC + 3. / 2. * LMUA * LMUF * CF * pow(NC, -1) - 3. / 2. * LMUA * LMUF * CF * NC - 1. / 2. * pow(LMUA, 2) * CF * pow(NC, -1) + 2. / 3. * pow(LMUA, 2) * CF * NF + 5. / 6. * pow(LMUA, 2) * CF * NC + 13. / 8. * z * CF * pow(NC, -1) - 389. / 72. * z * CF * NC + 2. / 3. * z * CF * NC * pow(rln2, 3) - 1. / 3. * z * LMUR * CF * NF + 11. / 6. * z * LMUR * CF * NC + 3. / 4. * z * LMUF * CF * pow(NC, -1) - 3. / 4. * z * LMUF * CF * NC - 7. / 4. * z * LMUA * CF * pow(NC, -1) + 1. / 3. * z * LMUA * CF * NF + 31. / 12. * z * LMUA * CF * NC + 1. / 3. * z * LMUA * LMUR * CF * NF - 11. / 6. * z * LMUA * LMUR * CF * NC - 3. / 4. * z * LMUA * LMUF * CF * pow(NC, -1) + 3. / 4. * z * LMUA * LMUF * CF * NC + 1. / 8. * z * pow(LMUA, 2) * CF * pow(NC, -1) - 1. / 3. * z * pow(LMUA, 2) * CF * NF + 53. / 24. * z * pow(LMUA, 2) * CF * NC -
          269. / 54. * pow(z, 2) * CF * NC + 13. / 9. * pow(z, 2) * LMUA * CF * NC + 2. / 3. * pow(z, 2) * pow(LMUA, 2) * CF * NC - 5 * zeta3 * pow(z, -1) * CF * pow(NC, -1) - 14 * zeta3 * pow(z, -1) * CF * NC + 3 * zeta3 * CF * pow(NC, -1) - 3. / 2. * zeta3 * z * CF * pow(NC, -1) - 12 * zeta3 * z * CF * NC - 1. / 4. * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) - 1. / 4. * pow(pi, 2) * pow(z, -1) * CF * NC;
    res += -2. / 3. * pow(pi, 2) * pow(z, -1) * CF * NC * rln2 - 1. / 3. * pow(pi, 2) * pow(z, -1) * LMUF * CF * pow(NC, -1) + 1. / 3. * pow(pi, 2) * pow(z, -1) * LMUF * CF * NC - 1. / 3. * pow(pi, 2) * pow(z, -1) * LMUA * CF * pow(NC, -1) + 1. / 3. * pow(pi, 2) * pow(z, -1) * LMUA * CF * NC + 2. / 3. * pow(pi, 2) * CF * pow(NC, -1) - 5. / 3. * pow(pi, 2) * CF * NC - 2. / 3. * pow(pi, 2) * CF * NC * rln2 + 1. / 3. * pow(pi, 2) * LMUF * CF * pow(NC, -1) - 1. / 3. * pow(pi, 2) * LMUF * CF * NC + 1. / 2. * pow(pi, 2) * LMUA * CF * pow(NC, -1) + 1. / 6. * pow(pi, 2) * LMUA * CF * NC - 1. / 8. * pow(pi, 2) * z * CF * pow(NC, -1) + 7. / 24. * pow(pi, 2) * z * CF * NC - 1. / 3. * pow(pi, 2) * z * CF * NC * rln2 - 1. / 6. * pow(pi, 2) * z * LMUF * CF * pow(NC, -1) + 1. / 6. * pow(pi, 2) * z * LMUF * CF * NC - 1. / 4. * pow(pi, 2) * z * LMUA * CF * pow(NC, -1) + 7. / 12. * pow(pi, 2) * z * LMUA * CF * NC - 2 * ln(1 + z) * pow(z, -1) * CF * NC * pow(rln2, 2) - 2 * ln(1 + z) * CF * NC * pow(rln2, 2) - ln(1 + z) * z * CF * NC * pow(rln2, 2) + 1. / 3. * ln(1 + z) * pow(pi, 2) * pow(z, -1) * CF * NC + 1. / 3. * ln(1 + z) * pow(pi, 2) * CF * NC + 1. / 6. * ln(1 + z) * pow(pi, 2) * z * CF * NC + 9. / 2. * ln(z) * pow(z, -1) * CF * pow(NC, -1) + 71. / 18. * ln(z) * pow(z, -1) * CF * NC - 2. / 3. * ln(z) * pow(z, -1) * LMUR * CF * NF + 11. / 3. * ln(z) * pow(z, -1) * LMUR * CF * NC + 3. / 2. * ln(z) * pow(z, -1) * LMUF * CF * pow(NC, -1) - 3. / 2. * ln(z) * pow(z, -1) * LMUF * CF * NC + 2. / 3. * ln(z) * pow(z, -1) * LMUA * CF * NF + 29. / 3. * ln(z) * pow(z, -1) * LMUA * CF * NC - 2 * ln(z) * pow(z, -1) * pow(LMUA, 2) * CF * NC - 67. / 8. * ln(z) * CF * pow(NC, -1) + 247. / 8. * ln(z) * CF * NC + 2. / 3. * ln(z) * LMUR * CF * NF - 11. / 3. * ln(z) * LMUR * CF * NC - 3. / 2. * ln(z) * LMUF * CF * pow(NC, -1) + 3. / 2. * ln(z) * LMUF * CF * NC - 3. / 2. * ln(z) * LMUA * CF * pow(NC, -1);
    res += -2. / 3. * ln(z) * LMUA * CF * NF + 19. / 6. * ln(z) * LMUA * CF * NC - 1. / 2. * ln(z) * pow(LMUA, 2) * CF * pow(NC, -1) - 3. / 2. * ln(z) * pow(LMUA, 2) * CF * NC + 45. / 8. * ln(z) * z * CF * pow(NC, -1) + 31. / 8. * ln(z) * z * CF * NC - 1. / 3. * ln(z) * z * LMUR * CF * NF + 11. / 6. * ln(z) * z * LMUR * CF * NC + 3. / 4. * ln(z) * z * LMUF * CF * pow(NC, -1) -
           3. / 4. * ln(z) * z * LMUF * CF * NC + 3. / 4. * ln(z) * z * LMUA * CF * pow(NC, -1) + 1. / 3. * ln(z) * z * LMUA * CF * NF - 55. / 12. * ln(z) * z * LMUA * CF * NC + 1. / 4. * ln(z) * z * pow(LMUA, 2) * CF * pow(NC, -1) - 9. / 4. * ln(z) * z * pow(LMUA, 2) * CF * NC + 31. / 9. * ln(z) * pow(z, 2) * CF * NC - 4. / 3. * ln(z) * pow(z, 2) * LMUA * CF * NC + 1. / 3. * ln(z) * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) - ln(z) * pow(pi, 2) * pow(z, -1) * CF * NC - 1. / 2. * ln(z) * pow(pi, 2) * CF * pow(NC, -1) - 1. / 6. * ln(z) * pow(pi, 2) * CF * NC + 1. / 4. * ln(z) * pow(pi, 2) * z * CF * pow(NC, -1) - 11. / 12. * ln(z) * pow(pi, 2) * z * CF * NC - 4 * ln(z) * ln(1 + z) * pow(z, -1) * LMUA * CF * NC - 4 * ln(z) * ln(1 + z) * LMUA * CF * NC +
           ln(z) * ln(1 + z) * z * CF * NC - 2 * ln(z) * ln(1 + z) * z * LMUA * CF * NC - 20. / 3. * pow(ln(z), 2) * pow(z, -1) * CF * NC + 6 * pow(ln(z), 2) * pow(z, -1) * LMUA * CF * NC + pow(ln(z), 2) * CF * pow(NC, -1) - 5 * pow(ln(z), 2) * CF * NC + pow(ln(z), 2) * LMUA * CF * pow(NC, -1) + 3 * pow(ln(z), 2) * LMUA * CF * NC - 13. / 16. * pow(ln(z), 2) * z * CF * pow(NC, -1) - 7. / 16. * pow(ln(z), 2) * z * CF * NC - 1. / 2. * pow(ln(z), 2) * z * LMUA * CF * pow(NC, -1) + 11. / 2. * pow(ln(z), 2) * z * LMUA * CF * NC + 3 * pow(ln(z), 2) * ln(1 + z) * pow(z, -1) * CF * NC + 3 * pow(ln(z), 2) * ln(1 + z) * CF * NC + 3. / 2. * pow(ln(z), 2) * ln(1 + z) * z * CF * NC - 10. / 3. * pow(ln(z), 3) * pow(z, -1) * CF * NC - 5. / 12. * pow(ln(z), 3) * CF * pow(NC, -1);
    res += -5. / 4. * pow(ln(z), 3) * CF * NC + 5. / 24. * pow(ln(z), 3) * z * CF * pow(NC, -1) - 65. / 24. * pow(ln(z), 3) * z * CF * NC + 2 * pow(ln(z), 2) * ln(omz) * pow(z, -1) * CF * pow(NC, -1) + pow(ln(z), 2) * ln(omz) * pow(z, -1) * CF * NC - 2 * pow(ln(z), 2) * ln(omz) * CF * pow(NC, -1) - pow(ln(z), 2) * ln(omz) * CF * NC + pow(ln(z), 2) * ln(omz) * z * CF * pow(NC, -1) + 1. / 2. * pow(ln(z), 2) * ln(omz) * z * CF * NC - 2 * ln(z) * ln(omz) * pow(z, -1) * LMUA * CF * pow(NC, -1) - 6 * ln(z) * ln(omz) * pow(z, -1) * LMUA * CF * NC + 2 * ln(z) * ln(omz) * LMUA * CF * pow(NC, -1) + 6 * ln(z) * ln(omz) * LMUA * CF * NC + 3 * ln(z) * ln(omz) * z * CF * NC - ln(z) * ln(omz) * z * LMUA * CF * pow(NC, -1) - 3 * ln(z) * ln(omz) * z * LMUA * CF * NC + 4 * ln(z) * ln(omz) * ln(1 + z) * pow(z, -1) * CF * NC + 4 * ln(z) * ln(omz) * ln(1 + z) * CF * NC + 2 * ln(z) * ln(omz) * ln(1 + z) * z * CF * NC + 3 * ln(z) * pow(ln(omz), 2) * pow(z, -1) * CF * NC + 3. / 2. * ln(z) * pow(ln(omz), 2) * CF * pow(NC, -1) + 15. / 2. * ln(z) * pow(ln(omz), 2) * CF * NC - 3. / 4. * ln(z) * pow(ln(omz), 2) * z * CF * pow(NC, -1) + 21. / 4. * ln(z) * pow(ln(omz), 2) * z * CF * NC + 2 * ln(z) * Li2(-z) * pow(z, -1) * CF * NC + 2 * ln(z) * Li2(-z) * CF * NC + ln(z) * Li2(-z) * z * CF * NC + 6 * ln(z) * Li2(z) * pow(z, -1) * CF * pow(NC, -1) - 4 * ln(z) * Li2(z) * pow(z, -1) * CF * NC - 6 * ln(z) * Li2(z) * CF * pow(NC, -1) + 4 * ln(z) * Li2(z) * CF * NC + 3 * ln(z) * Li2(z) * z * CF * pow(NC, -1) - 2 * ln(z) * Li2(z) * z * CF * NC + 9. / 2. * ln(omz) * pow(z, -1) * CF * pow(NC, -1) - 55. / 18. * ln(omz) * pow(z, -1) * CF * NC - 2 * ln(omz) * pow(z, -1) * CF * NC * pow(rln2, 2) - 2. / 3. * ln(omz) * pow(z, -1) * LMUR * CF * NF + 11. / 3. * ln(omz) * pow(z, -1) * LMUR * CF * NC + 3. / 2. * ln(omz) * pow(z, -1) * LMUF * CF * pow(NC, -1);
    res += -3. / 2. * ln(omz) * pow(z, -1) * LMUF * CF * NC - 3. / 2. * ln(omz) * pow(z, -1) * LMUA * CF * pow(NC, -1) + 2. / 3. * ln(omz) * pow(z, -1) * LMUA * CF * NF + 49. / 6. * ln(omz) * pow(z, -1) * LMUA * CF * NC - ln(omz) * pow(z, -1) * pow(LMUA, 2) * CF * pow(NC, -1) + 3 * ln(omz) * pow(z, -1) * pow(LMUA, 2) * CF * NC - 9. / 2. * ln(omz) * CF * pow(NC, -1) + 23. / 3. * ln(omz) * CF * NC - 2 * ln(omz) * CF * NC * pow(rln2, 2) + 2. / 3. * ln(omz) * LMUR * CF * NF - 11. / 3. * ln(omz) * LMUR * CF * NC - 3. / 2. * ln(omz) * LMUF * CF * pow(NC, -1) + 3. / 2. * ln(omz) * LMUF * CF * NC + 5. / 2. * ln(omz) * LMUA * CF * pow(NC, -1) - 2. / 3. * ln(omz) * LMUA * CF * NF - 41. / 6. * ln(omz) * LMUA * CF * NC + ln(omz) * pow(LMUA, 2) * CF * pow(NC, -1) - 3 * ln(omz) * pow(LMUA, 2) * CF * NC + 5. / 2. * ln(omz) * z * CF * pow(NC, -1) - 31. / 6. * ln(omz) * z * CF * NC - ln(omz) * z * CF * NC * pow(rln2, 2) - 1. / 3. * ln(omz) * z * LMUR * CF * NF + 11. / 6. * ln(omz) * z * LMUR * CF * NC + 3. / 4. * ln(omz) * z * LMUF * CF * pow(NC, -1) - 3. / 4. * ln(omz) * z * LMUF * CF * NC + 1. / 3. * ln(omz) * z * LMUA * CF * NF - 17. / 6. * ln(omz) * z * LMUA * CF * NC - 1. / 2. * ln(omz) * z * pow(LMUA, 2) * CF * pow(NC, -1) + 3. / 2. * ln(omz) * z * pow(LMUA, 2) * CF * NC - 13. / 9. * ln(omz) * pow(z, 2) * CF * NC - 4. / 3. * ln(omz) * pow(z, 2) * LMUA * CF * NC + 2. / 3. * ln(omz) * pow(pi, 2) * pow(z, -1) * CF * pow(NC, -1) - 2. / 3. * ln(omz) * pow(pi, 2) * pow(z, -1) * CF * NC - ln(omz) * pow(pi, 2) * CF * pow(NC, -1) - ln(omz) * pow(pi, 2) * CF * NC + 1. / 2. * ln(omz) * pow(pi, 2) * z * CF * pow(NC, -1) - 7. / 6. * ln(omz) * pow(pi, 2) * z * CF * NC + 4 * ln(omz) * ln(1 + z) * pow(z, -1) * CF * NC * rln2 + 4 * ln(omz) * ln(1 + z) * CF * NC * rln2 + 2 * ln(omz) * ln(1 + z) * z * CF * NC * rln2 - 2 * ln(omz) * pow(ln(1 + z), 2) * pow(z, -1) * CF * NC;
    res += -2 * ln(omz) * pow(ln(1 + z), 2) * CF * NC - ln(omz) * pow(ln(1 + z), 2) * z * CF * NC + 3. / 2. * pow(ln(omz), 2) * pow(z, -1) * CF * pow(NC, -1) - 20. / 3. * pow(ln(omz), 2) * pow(z, -1) * CF * NC + 2 * pow(ln(omz), 2) * pow(z, -1) * LMUA * CF * pow(NC, -1) - 4 * pow(ln(omz), 2) * pow(z, -1) * LMUA * CF * NC - 2 * pow(ln(omz), 2) * CF * pow(NC, -1) + 6 * pow(ln(omz), 2) * CF * NC - 2 * pow(ln(omz), 2) * LMUA * CF * pow(NC, -1) + 4 * pow(ln(omz), 2) * LMUA * CF * NC + 1. / 8. * pow(ln(omz), 2) * z * CF * pow(NC, -1) - 1. / 8. * pow(ln(omz), 2) * z * CF * NC + pow(ln(omz), 2) * z * LMUA * CF * pow(NC, -1) - 2 * pow(ln(omz), 2) * z * LMUA * CF * NC + 2. / 3. * pow(ln(omz), 2) * pow(z, 2) * CF * NC - 5. / 6. * pow(ln(omz), 3) * pow(z, -1) * CF * pow(NC, -1) + 7. / 6. * pow(ln(omz), 3) * pow(z, -1) * CF * NC + 5. / 6. * pow(ln(omz), 3) * CF * pow(NC, -1) - 7. / 6. * pow(ln(omz), 3) * CF * NC - 5. / 12. * pow(ln(omz), 3) * z * CF * pow(NC, -1) + 7. / 12. * pow(ln(omz), 3) * z * CF * NC - 2 * ln(omz) * Li2(1 - z) * pow(z, -1) * CF * pow(NC, -1) - 2 * ln(omz) * Li2(1 - z) * pow(z, -1) * CF * NC + 3 * ln(omz) * Li2(1 - z) * CF * pow(NC, -1) + 9 * ln(omz) * Li2(1 - z) * CF * NC - 3. / 2. * ln(omz) * Li2(1 - z) * z * CF * pow(NC, -1) + 3. / 2. * ln(omz) * Li2(1 - z) * z * CF * NC + 4 * ln(omz) * Li2(-z) * pow(z, -1) * CF * NC + 4 * ln(omz) * Li2(-z) * CF * NC + 2 * ln(omz) * Li2(-z) * z * CF * NC + 3 * ln(omz) * Li2(z) * pow(z, -1) * CF * pow(NC, -1) + 3 * ln(omz) * Li2(z) * pow(z, -1) * CF * NC - ln(omz) * Li2(z) * CF * pow(NC, -1) + 11 * ln(omz) * Li2(z) * CF * NC + 1. / 2. * ln(omz) * Li2(z) * z * CF * pow(NC, -1) + 13. / 2. * ln(omz) * Li2(z) * z * CF * NC + 2. / 3. * ln(opz) * pow(pi, 2) * pow(z, -1) * CF * NC + 2. / 3. * ln(opz) * pow(pi, 2) * CF * NC;
    res += +1. / 3. * ln(opz) * pow(pi, 2) * z * CF * NC - 4 * Li3(1. / 2. - 1. / 2. * z) * pow(z, -1) * CF * NC - 4 * Li3(1. / 2. - 1. / 2. * z) * CF * NC - 2 * Li3(1. / 2. - 1. / 2. * z) * z * CF * NC - 4 * Li3(1. / 2. + 1. / 2. * z) * pow(z, -1) * CF * NC - 4 * Li3(1. / 2. + 1. / 2. * z) * CF * NC - 2 * Li3(1. / 2. + 1. / 2. * z) * z * CF * NC + 3 * Li3(1 - z) * pow(z, -1) * CF * pow(NC, -1) + 7 * Li3(1 - z) * pow(z, -1) * CF * NC - 2 * Li3(1 - z) * CF * pow(NC, -1) + 8 * Li3(1 - z) * CF * NC + Li3(1 - z) * z * CF * pow(NC, -1) + 6 * Li3(1 - z) * z * CF * NC + 2 * Li3(-z) * pow(z, -1) * CF * NC + 2 * Li3(-z) * CF * NC + Li3(-z) * z * CF * NC + 4 * Li3(1 / (1 + z)) * pow(z, -1) * CF * NC + 4 * Li3(1 / (1 + z)) * CF * NC + 2 * Li3(1 / (1 + z)) * z * CF * NC - 4 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * pow(z, -1) * CF * NC - 4 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * CF * NC - 2 * Li3(1 / (1 + z) - 1 / (1 + z) * z) * z * CF * NC - 6 * Li3(z) * pow(z, -1) * CF * pow(NC, -1) + 20 * Li3(z) * pow(z, -1) * CF * NC + 8 * Li3(z) * CF * pow(NC, -1) - 2 * Li3(z) * CF * NC - 4 * Li3(z) * z * CF * pow(NC, -1) + 15 * Li3(z) * z * CF * NC - 4 * Li2(-z) * pow(z, -1) * LMUA * CF * NC - 4 * Li2(-z) * LMUA * CF * NC +
           Li2(-z) * z * CF * NC - 2 * Li2(-z) * z * LMUA * CF * NC - 3. / 2. * Li2(z) * pow(z, -1) * CF * pow(NC, -1) + 89. / 6. * Li2(z) * pow(z, -1) * CF * NC - 6 * Li2(z) * pow(z, -1) * LMUA * CF * pow(NC, -1) - 6 * Li2(z) * pow(z, -1) * LMUA * CF * NC - 2 * Li2(z) * CF * NC + 5 * Li2(z) * LMUA * CF * pow(NC, -1) - Li2(z) * LMUA * CF * NC + Li2(z) * z * CF * pow(NC, -1) + Li2(z) * z * CF * NC - 5. / 2. * Li2(z) * z * LMUA * CF * pow(NC, -1) - 11. / 2. * Li2(z) * z * LMUA * CF * NC - 4. / 3. * Li2(z) * pow(z, 2) * CF * NC;

 """
    create_file_with_split_orders(s, output_file, "res")
