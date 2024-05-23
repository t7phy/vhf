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
      tmp = -3 * pow(z, -1) * CF - 5. / 2. * pow(z, -1) * LMUF * CF + 10 * CF + 5 * LMUF * CF + 3 * x * pow(z, -1) * CF + 5. / 2. * x * pow(z, -1) * LMUF * CF - 10 * x * CF - 5 * x * LMUF * CF + 1. / 6. * pow(pi, 2) * pow(z, -1) * CF - 1. / 3. * pow(pi, 2) * CF + 1. / 6. * pow(pi, 2) * x * pow(z, -1) * CF - 1. / 3. * pow(pi, 2) * x * CF - 3 * ln(x) * pow(z, -1) * CF - ln(x) * pow(z, -1) * LMUF * CF + 1. / 2. * ln(x) * CF * pow(poly2, -1) + 8 * ln(x) * CF + 2 * ln(x) * LMUF * CF + 3 * ln(x) * x * pow(z, -1) * CF - ln(x) * x * pow(z, -1) * LMUF * CF - 1. / 2. * ln(x) * x * CF * pow(poly2, -1) - 4 * ln(x) * x * CF + 2 * ln(x) * x * LMUF * CF - 1. / 2. * ln(x) * pow(x, 2) * CF * pow(poly2, -1) + 1. / 2. * ln(x) * pow(x, 3) * CF * pow(poly2, -1) + 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * CF * pow(sqrtxz2, -1) + 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1) - ln(x) * ln(1 - sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1) - 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * CF * pow(sqrtxz2, -1) - 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * x * CF * pow(sqrtxz2, -1) + ln(x) * ln(1 + sqrtxz2 + x) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * CF * pow(sqrtxz2, -1) - 1. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1);
      tmp += -pow(ln(x), 2) * pow(z, -1) * CF + 2 * pow(ln(x), 2) * CF - pow(ln(x), 2) * x * pow(z, -1) * CF + 2 * pow(ln(x), 2) * x * CF + ln(x) * ln(z) * pow(z, -1) * CF - ln(x) * ln(z) * CF + ln(x) * ln(z) * x * pow(z, -1) * CF -
             ln(x) * ln(z) * x * CF + ln(x) * ln(omz) * pow(z, -1) * CF - 2 * ln(x) * ln(omz) * CF + ln(x) * ln(omz) * x * pow(z, -1) * CF - 2 * ln(x) * ln(omz) * x * CF + 5. / 2. * ln(z) * pow(z, -1) * CF + 1. / 2. * ln(z) * CF * pow(poly2, -1) +
             ln(z) * CF * pow(omz, -1) - 2 * ln(z) * CF - 5. / 2. * ln(z) * x * pow(z, -1) * CF + 1. / 2. * ln(z) * x * CF * pow(poly2, -1) - ln(z) * x * CF * pow(omz, -1) + 2 * ln(z) * x * CF - 1. / 2. * ln(z) * pow(x, 2) * CF * pow(poly2, -1) - 1. / 2. * ln(z) * pow(x, 3) * CF * pow(poly2, -1) + 5. / 2. * ln(omx) * pow(z, -1) * CF - 5 * ln(omx) * CF - 5. / 2. * ln(omx) * x * pow(z, -1) * CF + 5 * ln(omx) * x * CF + 5. / 2. * ln(omz) * pow(z, -1) * CF - 5 * ln(omz) * CF - 5. / 2. * ln(omz) * x * pow(z, -1) * CF + 5 * ln(omz) * x * CF + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1);
      tmp += -1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) *
                 pow(poly2, -1) -
             7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * CF * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * CF * pow(sqrtxz2, -1) - 1. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * CF * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) - 1. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * CF * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * CF * pow(sqrtxz2, -1);
      tmp += -Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * CF * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) + 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * CF * pow(sqrtxz2, -1) + 1. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * CF * pow(sqrtxz2, -1) * pow(poly2, -1) - Li2(x) * pow(z, -1) * CF + 2 * Li2(x) * CF - Li2(x) * x * pow(z, -1) * CF + 2 * Li2(x) * x * CF;

 """
    create_file_with_split_orders(s, output_file, "tmp")
