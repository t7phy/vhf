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


def split_per_var_line(s):
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
    split_on_term = [term for s in split_on_term for term in split_per_var_line(s)]
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


def split_to_line_per_var(s, var):
    lines = re.split(rf"\s*{var}\s*=\s*|\s*{var}\s*\+=\s*", s)
    lines = [line for line in lines if line]
    return lines


def get_all_present_orders(dict_dict):
    dict_list = list(dict_dict.values())
    dict_set = set(key for d in dict_list for key in d)
    return sorted(list(dict_set))


def create_file_with_split_orders(s: str, output_file: str, var: str):
    """
    Function to create a file with the split orders.
    s: str, the string to be split.
    var: Variable name to be split, e.g. tmp or res.
    output_file: str, the file to write the output to.
    """
    # Split based on var position, respect original
    lines = split_to_line_per_var(s, var)

    # Remove res references, put in later
    orders_per_line = dict()
    for i, line in enumerate(lines):
        line = remove_var_n_semicolon(line, var)
        orders_per_line[i] = split_to_order(line)

    orders_present = get_all_present_orders(orders_per_line)

    if "uncategorized" in orders_present:
        print("Uncategorized terms present, please categorize manually.")
    else:
        print("All terms categorized.")

    with open(output_file, "w") as f:
        f.write("// Split orders:\n")
        f.write(f"{var} = 0;\n")
        for order in orders_present:
            f.write(f"// Order {order}:\n")
            for _, line in orders_per_line.items():
                if order not in line:
                    continue
                f.write(f"{var} += ")
                terms = line[order]
                for i, term in enumerate(terms):
                    term = revert_minus_sign(term)
                    f.write(f"{term} + ")
                f.write("0;\n")


if __name__ == "__main__":
    output_file = "split_orders.txt"
    s = """
              tmp = 2 * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 47. / 16. * pow(z, -1) * pow(NC, -1) - 2 * pow(z, -1) * NC * pow(omz, -1) - 33. / 16. * pow(z, -1) * NC + 1. / 6. * pow(z, -1) * LMUR * NF - 11. / 12. * pow(z, -1) * LMUR * NC - 1. / 6. * pow(z, -1) * LMUF * NF - 61. / 12. * pow(z, -1) * LMUF * NC - 1. / 8. * pow(NC, -1) * pow(poly2, -1) - 4 * pow(NC, -1) * pow(omz, -1) - 2 * pow(NC, -1) + 1. / 8. * NC * pow(poly2, -1) + 3 * NC * pow(omz, -1) + 14 * NC - 1. / 3. * LMUR * NF + 11. / 6. * LMUR * NC - 5. / 4. * LMUF * pow(NC, -1) + 1. / 3. * LMUF * NF + 137. / 12. * LMUF * NC - 1. / 4. * LMUA * pow(NC, -1) + 1. / 4. * LMUA * NC - 1. / 4. * LMUA * LMUF * pow(NC, -1) + 1. / 4. * LMUA * LMUF * NC - 1. / 4. * z * pow(NC, -1) * pow(omxmz, -1) + 51. / 16. * z * pow(NC, -1) + 1. / 4. * z * NC * pow(omxmz, -1) - 51. / 16. * z * NC + 3. / 4. * z * LMUF * pow(NC, -1) - 3. / 4. * z * LMUF * NC - 3. / 8. * z * LMUA * pow(NC, -1) + 3. / 8. * z * LMUA * NC - 1. / 4. * z * LMUA * LMUF * pow(NC, -1) + 1. / 4. * z * LMUA * LMUF * NC + 1. / 2. * pow(z, 2) * pow(NC, -1) * pow(omxmz, -1) - 1. / 2. * pow(z, 2) * NC * pow(omxmz, -1) - 4 * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 11. / 4. * x * pow(z, -1) * pow(NC, -1) + 4 * x * pow(z, -1) * NC * pow(omz, -1) + 3. / 4. * x * pow(z, -1) * NC - 1. / 3. * x * pow(z, -1) * LMUR * NF + 11. / 6. * x * pow(z, -1) * LMUR * NC + 1. / 3. * x * pow(z, -1) * LMUF * NF + 25. / 6. * x * pow(z, -1) * LMUF * NC + 1. / 8. * x * pow(NC, -1) * pow(poly2, -1) + 3 * x * pow(NC, -1) * pow(omz, -1) + 37. / 8. * x * pow(NC, -1) - 1. / 8. * x * NC * pow(poly2, -1) - 4 * x * NC * pow(omz, -1) - 117. / 8. * x * NC + 2. / 3. * x * LMUR * NF - 11. / 3. * x * LMUR * NC + 3. / 2. * x * LMUF * pow(NC, -1) - 2. / 3. * x * LMUF * NF - 59. / 6. * x * LMUF * NC + 1. / 2. * x * LMUA * LMUF * pow(NC, -1) - 1. / 2. * x * LMUA * LMUF * NC;
              tmp += -11. / 4. * x * z * pow(NC, -1) + 11. / 4. * x * z * NC - x * z * LMUF * pow(NC, -1) + x * z * LMUF * NC + 1. / 4. * x * z * LMUA * pow(NC, -1) - 1. / 4. * x * z * LMUA * NC + 1. / 2. * x * z * LMUA * LMUF * pow(NC, -1) - 1. / 2. * x * z * LMUA * LMUF * NC + 2 * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 2 * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 1. / 8. * pow(x, 2) * pow(NC, -1) * pow(poly2, -1) - 2 * pow(x, 2) * pow(NC, -1) * pow(omz, -1) - 1. / 8. * pow(x, 2) * NC * pow(poly2, -1) - 1. / 8. * pow(x, 3) * pow(NC, -1) * pow(poly2, -1) + 1. / 8. * pow(x, 3) * NC * pow(poly2, -1) -
                     13. / 12. * pow(pi, 2) * pow(z, -1) * pow(NC, -1) + 1. / 3. * pow(pi, 2) * pow(z, -1) * NC * pow(omz, -1) + 1. / 3. * pow(pi, 2) * pow(z, -1) * NC - 3. / 4. * pow(pi, 2) * pow(NC, -1) * pow(omz, -1) + 5. / 6. * pow(pi, 2) * pow(NC, -1) - 1. / 6. * pow(pi, 2) * NC * pow(omz, -1) - 3. / 2. * pow(pi, 2) * NC - 1. / 6. * pow(pi, 2) * z * pow(NC, -1) + 1. / 6. * pow(pi, 2) * z * NC + 3. / 2. * pow(pi, 2) * x * pow(z, -1) * pow(NC, -1) - 2. / 3. * pow(pi, 2) * x * pow(z, -1) * NC * pow(omz, -1) + 1. / 3. * pow(pi, 2) * x * pow(z, -1) * NC + 3. / 2. * pow(pi, 2) * x * pow(NC, -1) * pow(omz, -1) - 5. / 6. * pow(pi, 2) * x * pow(NC, -1) + 1. / 3. * pow(pi, 2) * x * NC * pow(omz, -1) + 1. / 2. * pow(pi, 2) * x * NC - 1. / 6. * pow(pi, 2) * x * z * pow(NC, -1) + 1. / 6. * pow(pi, 2) * x * z * NC - 5. / 6. * pow(pi, 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) - 1. / 2. * pow(pi, 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) - 1. / 6. * ln(pow(x, -1) * z * omx * omz) * pow(z, -1) * NF - 1. / 6. * ln(pow(x, -1) * z * omx * omz) * NF * pow(omz, -1) - 8 * ln(x) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 33. / 8. * ln(x) * pow(z, -1) * pow(NC, -1) - 1. / 6. * ln(x) * pow(z, -1) * NF + 8 * ln(x) * pow(z, -1) * NC * pow(omz, -1);
              tmp += -101. / 8. * ln(x) * pow(z, -1) * NC - 2 * ln(x) * pow(z, -1) * LMUF * NC - 3. / 16. * ln(x) * pow(NC, -1) * pow(poly2, -2) - 3. / 8. * ln(x) * pow(NC, -1) * pow(poly2, -1) + 7. / 2. * ln(x) * pow(NC, -1) * pow(omz, -1) - 1. / 2. * ln(x) * pow(NC, -1) * pow(omxmz, -2) + ln(x) * pow(NC, -1) * pow(omxmz, -1) + 41. / 16. * ln(x) * pow(NC, -1) - 1. / 6. * ln(x) * NF * pow(omz, -1) + 3. / 16. * ln(x) * NC * pow(poly2, -2) + 7. / 8. * ln(x) * NC * pow(poly2, -1) - 13. / 2. * ln(x) * NC * pow(omz, -1) + 1. / 2. * ln(x) * NC * pow(omxmz, -2) - 1. / 2. * ln(x) * NC * pow(omxmz, -1) + 207. / 16. * ln(x) * NC - 1. / 4. * ln(x) * LMUF * pow(NC, -1) + 17. / 4. * ln(x) * LMUF * NC - 1. / 4. * ln(x) * LMUA * pow(NC, -1) + 1. / 4. * ln(x) * LMUA * NC - 1. / 4. * ln(x) * z * pow(NC, -1) * pow(omxmz, -2) + 2 * ln(x) * z * pow(NC, -1) * pow(omxmz, -1) - 3. / 4. * ln(x) * z * pow(NC, -1) + 1. / 4. * ln(x) * z * NC * pow(omxmz, -2) - 7. / 2. * ln(x) * z * NC * pow(omxmz, -1) + 7. / 4. * ln(x) * z * NC + 1. / 4. * ln(x) * z * LMUF * pow(NC, -1) - 1. / 4. * ln(x) * z * LMUF * NC - 1. / 4. * ln(x) * z * LMUA * pow(NC, -1) + 1. / 4. * ln(x) * z * LMUA * NC + 3. / 4. * ln(x) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -2) - 5. / 2. * ln(x) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -1) - 3. / 4. * ln(x) * pow(z, 2) * NC * pow(omxmz, -2) + 7. / 2. * ln(x) * pow(z, 2) * NC * pow(omxmz, -1) + 16 * ln(x) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 17. / 4. * ln(x) * x * pow(z, -1) * pow(NC, -1) - 16 * ln(x) * x * pow(z, -1) * NC * pow(omz, -1) + 73. / 4. * ln(x) * x * pow(z, -1) * NC - 2 * ln(x) * x * pow(z, -1) * LMUF * NC + 3. / 16. * ln(x) * x * pow(NC, -1) * pow(poly2, -2) + 1. / 2. * ln(x) * x * pow(NC, -1) * pow(poly2, -1) - 4 * ln(x) * x * pow(NC, -1) * pow(omz, -1) - 1. / 2. * ln(x) * x * pow(NC, -1) * pow(xmz, -1);
              tmp += +3. / 2. * ln(x) * x * pow(NC, -1) * pow(omxmz, -2) - 3 * ln(x) * x * pow(NC, -1) * pow(omxmz, -1) - 251. / 16. * ln(x) * x * pow(NC, -1) - 3. / 16. * ln(x) * x * NC * pow(poly2, -2) - ln(x) * x * NC * pow(poly2, -1) + 10 * ln(x) * x * NC * pow(omz, -1) - 3. / 2. * ln(x) * x * NC * pow(omxmz, -2) + 3 * ln(x) * x * NC * pow(omxmz, -1) + 3. / 16. * ln(x) * x * NC - 1. / 2. * ln(x) * x * LMUF * pow(NC, -1) + 9. / 2. * ln(x) * x * LMUF * NC + 1. / 2. * ln(x) * x * LMUA * pow(NC, -1) - 1. / 2. * ln(x) * x * LMUA * NC + 1. / 2. * ln(x) * x * z * LMUF * pow(NC, -1) - 1. / 2. * ln(x) * x * z * LMUF * NC +
                     1. / 2. * ln(x) * x * z * LMUA * pow(NC, -1) - 1. / 2. * ln(x) * x * z * LMUA * NC - 8 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 8 * ln(x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 3. / 8. * ln(x) * pow(x, 2) * pow(NC, -1) * pow(poly2, -2) - 1. / 8. * ln(x) * pow(x, 2) * pow(NC, -1) * pow(poly2, -1) + 8 * ln(x) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + ln(x) * pow(x, 2) * pow(NC, -1) * pow(xmz, -1) - 3. / 2. * ln(x) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -2) + 3. / 2. * ln(x) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -1) + ln(x) * pow(x, 2) * pow(NC, -1) - 3. / 8. * ln(x) * pow(x, 2) * NC * pow(poly2, -2) + 5. / 8. * ln(x) * pow(x, 2) * NC * pow(poly2, -1) + 3. / 2. * ln(x) * pow(x, 2) * NC * pow(omxmz, -2) - 3. / 2. * ln(x) * pow(x, 2) * NC * pow(omxmz, -1) - 3. / 8. * ln(x) * pow(x, 3) * pow(NC, -1) * pow(poly2, -2) + 1. / 2. * ln(x) * pow(x, 3) * pow(NC, -1) * pow(omxmz, -2) + 3. / 8. * ln(x) * pow(x, 3) * NC * pow(poly2, -2) - 1. / 2. * ln(x) * pow(x, 3) * NC * pow(poly2, -1) - 1. / 2. * ln(x) * pow(x, 3) * NC * pow(omxmz, -2) - 3. / 16. * ln(x) * pow(x, 4) * pow(NC, -1) * pow(poly2, -2) + 3. / 16. * ln(x) * pow(x, 4) * NC * pow(poly2, -2);
              tmp += +3. / 16. * ln(x) * pow(x, 5) * pow(NC, -1) * pow(poly2, -2) - 3. / 16. * ln(x) * pow(x, 5) * NC * pow(poly2, -2) - ln(x) * ln(1 - sqrtxz2 + x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * pow(z, -1) * NC * pow(sqrtxz2, -1) - 3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 5. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 7. / 4. * ln(x) * ln(1 - sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 13. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(omz, -1) - ln(x) * ln(1 - sqrtxz2 + x) * NC * pow(sqrtxz2, -1) - 3 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1) + 3 * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 29. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 2. * ln(x) * ln(1 - sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1) - 69. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1) - 29. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1) + 69. / 8. * ln(x) * ln(1 - sqrtxz2 + x) * x * z * NC * pow(sqrtxz2, -1) - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1);
              tmp += +9. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3 * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 111. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) - 9. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1) - 11. / 16. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) - ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 9. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 9. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 7. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 32. * ln(x) * ln(1 - sqrtxz2 + x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + ln(x) * ln(1 + sqrtxz2 + x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * pow(z, -1) * NC * pow(sqrtxz2, -1);
              tmp += +3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 5. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 7. / 4. * ln(x) * ln(1 + sqrtxz2 + x) * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 13. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) * pow(omz, -1) + ln(x) * ln(1 + sqrtxz2 + x) * NC * pow(sqrtxz2, -1) + 3 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1) - 3 * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 29. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * x * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 2. * ln(x) * ln(1 + sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1) + 69. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * x * NC * pow(sqrtxz2, -1) + 29. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1) - 69. / 8. * ln(x) * ln(1 + sqrtxz2 + x) * x * z * NC * pow(sqrtxz2, -1) + 3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1) - 9. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1);
              tmp += +3 * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 111. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) + 9. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1) + 11. / 16. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 2) * NC * pow(sqrtxz2, -1) + ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 9. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 9. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 7. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 32. * ln(x) * ln(1 + sqrtxz2 + x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 2 * ln(x) * ln(1 + x) * pow(z, -1) * pow(NC, -1) + 2 * ln(x) * ln(1 + x) * pow(NC, -1) - ln(x) * ln(1 + x) * NC -
                     ln(x) * ln(1 + x) * z * pow(NC, -1) + ln(x) * ln(1 + x) * z * NC - 4 * ln(x) * ln(1 + x) * x * pow(z, -1) * pow(NC, -1) + 4 * ln(x) * ln(1 + x) * x * pow(NC, -1) - 2 * ln(x) * ln(1 + x) * x * NC - 2 * ln(x) * ln(1 + x) * x * z * pow(NC, -1);
              tmp += +2 * ln(x) * ln(1 + x) * x * z * NC - 2 * ln(x) * ln(1 + x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 2 * ln(x) * ln(1 + x) * pow(x, 2) * pow(NC, -1) - 2 * ln(x) * ln(1 + x) * pow(x, 2) * NC + 3 * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 11. / 4. * pow(ln(x), 2) * pow(z, -1) * pow(NC, -1) - 5. / 2. * pow(ln(x), 2) * pow(z, -1) * NC * pow(omz, -1) - pow(ln(x), 2) * pow(z, -1) * NC + 3 * pow(ln(x), 2) * pow(NC, -1) * pow(omz, -1) - 19. / 4. * pow(ln(x), 2) * pow(NC, -1) + 1. / 4. * pow(ln(x), 2) * NC * pow(omz, -1) + 33. / 4. * pow(ln(x), 2) * NC - 6 * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 7. / 2. * pow(ln(x), 2) * x * pow(z, -1) * pow(NC, -1) + 5 * pow(ln(x), 2) * x * pow(z, -1) * NC * pow(omz, -1) - 4 * pow(ln(x), 2) * x * pow(z, -1) * NC - 6 * pow(ln(x), 2) * x * pow(NC, -1) * pow(omz, -1) + 13. / 2. * pow(ln(x), 2) * x * pow(NC, -1) - 1. / 2. * pow(ln(x), 2) * x * NC * pow(omz, -1) - 5. / 2. * pow(ln(x), 2) * x * NC + 2 * pow(ln(x), 2) * x * z * pow(NC, -1) - 2 * pow(ln(x), 2) * x * z * NC + 3 * pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + pow(ln(x), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) - 3. / 2. * pow(ln(x), 2) * pow(x, 2) * pow(NC, -1) + 3. / 2. * pow(ln(x), 2) * pow(x, 2) * NC - 2 * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 9. / 4. * ln(x) * ln(z) * pow(z, -1) * pow(NC, -1) + 3 * ln(x) * ln(z) * pow(z, -1) * NC * pow(omz, -1) + 3. / 4. * ln(x) * ln(z) * pow(z, -1) * NC - 4 * ln(x) * ln(z) * pow(NC, -1) * pow(omz, -1) + 5. / 2. * ln(x) * ln(z) * pow(NC, -1) + 1. / 2. * ln(x) * ln(z) * NC * pow(omz, -1) - 11. / 2. * ln(x) * ln(z) * NC + 1. / 2. * ln(x) * ln(z) * z * pow(NC, -1) - 1. / 2. * ln(x) * ln(z) * z * NC;
              tmp += +4 * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 17. / 2. * ln(x) * ln(z) * x * pow(z, -1) * pow(NC, -1) - 6 * ln(x) * ln(z) * x * pow(z, -1) * NC * pow(omz, -1) + 5. / 2. * ln(x) * ln(z) * x * pow(z, -1) * NC + 8 * ln(x) * ln(z) * x * pow(NC, -1) * pow(omz, -1) - 9 * ln(x) * ln(z) * x * pow(NC, -1) + ln(x) * ln(z) * x * NC * pow(omz, -1) + 9 * ln(x) * ln(z) * x * NC - 2 * ln(x) * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 2 * ln(x) * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) - 8 * ln(x) * ln(omx) * pow(z, -1) * pow(NC, -1) - 2 * ln(x) * ln(omx) * pow(z, -1) * NC * pow(omz, -1) + 4 * ln(x) * ln(omx) * pow(z, -1) * NC - 19. / 2. * ln(x) * ln(omx) * pow(NC, -1) * pow(omz, -1) + 13. / 2. * ln(x) * ln(omx) * pow(NC, -1) + 7. / 2. * ln(x) * ln(omx) * NC * pow(omz, -1) -
                     11. / 2. * ln(x) * ln(omx) * NC + ln(x) * ln(omx) * z * pow(NC, -1) - ln(x) * ln(omx) * z * NC + 16 * ln(x) * ln(omx) * x * pow(z, -1) * pow(NC, -1) + 4 * ln(x) * ln(omx) * x * pow(z, -1) * NC * pow(omz, -1) - 8 * ln(x) * ln(omx) * x * pow(z, -1) * NC + 19 * ln(x) * ln(omx) * x * pow(NC, -1) * pow(omz, -1) - 13 * ln(x) * ln(omx) * x * pow(NC, -1) - 7 * ln(x) * ln(omx) * x * NC * pow(omz, -1) + 11 * ln(x) * ln(omx) * x * NC - 2 * ln(x) * ln(omx) * x * z * pow(NC, -1) + 2 * ln(x) * ln(omx) * x * z * NC - 5 * ln(x) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1) - 7 * ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + ln(x) * ln(omx) * pow(x, 2) * pow(NC, -1) - ln(x) * ln(omx) * pow(x, 2) * NC - 7 * ln(x) * ln(omz) * pow(z, -1) * pow(NC, -1) + 5 * ln(x) * ln(omz) * pow(z, -1) * NC - 6 * ln(x) * ln(omz) * pow(NC, -1) * pow(omz, -1) + 11. / 2. * ln(x) * ln(omz) * pow(NC, -1) + 3 * ln(x) * ln(omz) * NC * pow(omz, -1) - 21. / 2. * ln(x) * ln(omz) * NC;
              tmp += +14 * ln(x) * ln(omz) * x * pow(z, -1) * pow(NC, -1) - 4 * ln(x) * ln(omz) * x * pow(z, -1) * NC + 12 * ln(x) * ln(omz) * x * pow(NC, -1) * pow(omz, -1) - 10 * ln(x) * ln(omz) * x * pow(NC, -1) - 6 * ln(x) * ln(omz) * x * NC * pow(omz, -1) + 8 * ln(x) * ln(omz) * x * NC - ln(x) * ln(omz) * x * z * pow(NC, -1) + ln(x) * ln(omz) * x * z * NC - 5 * ln(x) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) - 3 * ln(x) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + 4 * ln(z) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 13. / 8. * ln(z) * pow(z, -1) * pow(NC, -1) + 1. / 6. * ln(z) * pow(z, -1) * NF - 4 * ln(z) * pow(z, -1) * NC * pow(omz, -1) + 69. / 8. * ln(z) * pow(z, -1) * NC - 3. / 16. * ln(z) * pow(NC, -1) * pow(poly2, -2) - 3. / 8. * ln(z) * pow(NC, -1) * pow(poly2, -1) - 5. / 2. * ln(z) * pow(NC, -1) * pow(omz, -1) - 83. / 16. * ln(z) * pow(NC, -1) + 1. / 6. * ln(z) * NF * pow(omz, -1) + 3. / 16. * ln(z) * NC * pow(poly2, -2) + 7. / 8. * ln(z) * NC * pow(poly2, -1) + 7 * ln(z) * NC * pow(omz, -1) - 77. / 16. * ln(z) * NC - 1. / 2. * ln(z) * LMUF * pow(NC, -1) * pow(omz, -1) + 1. / 4. * ln(z) * LMUF * pow(NC, -1) + 1. / 2. * ln(z) * LMUF * NC * pow(omz, -1) - 1. / 4. * ln(z) * LMUF * NC + 1. / 2. * ln(z) * LMUA * pow(NC, -1) * pow(omz, -1) - 3. / 4. * ln(z) * LMUA * pow(NC, -1) - 1. / 2. * ln(z) * LMUA * NC * pow(omz, -1) + 3. / 4. * ln(z) * LMUA * NC + 9. / 8. * ln(z) * z * pow(NC, -1) - 9. / 8. * ln(z) * z * NC + 1. / 4. * ln(z) * z * LMUF * pow(NC, -1) - 1. / 4. * ln(z) * z * LMUF * NC - 1. / 4. * ln(z) * z * LMUA * pow(NC, -1) + 1. / 4. * ln(z) * z * LMUA * NC - 8 * ln(z) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 2 * ln(z) * x * pow(z, -1) * pow(NC, -1) + 8 * ln(z) * x * pow(z, -1) * NC * pow(omz, -1) - 10 * ln(z) * x * pow(z, -1) * NC - 3. / 16. * ln(z) * x * pow(NC, -1) * pow(poly2, -2);
              tmp += -1. / 2. * ln(z) * x * pow(NC, -1) * pow(poly2, -1) + 3 * ln(z) * x * pow(NC, -1) * pow(omz, -1) + 1. / 2. * ln(z) * x * pow(NC, -1) * pow(xmz, -1) + 187. / 16. * ln(z) * x * pow(NC, -1) + 3. / 16. * ln(z) * x * NC * pow(poly2, -2) + ln(z) * x * NC * pow(poly2, -1) - 8 * ln(z) * x * NC * pow(omz, -1) - 83. / 16. * ln(z) * x * NC + ln(z) * x * LMUF * pow(NC, -1) * pow(omz, -1) - 1. / 2. * ln(z) * x * LMUF * pow(NC, -1) - ln(z) * x * LMUF * NC * pow(omz, -1) + 1. / 2. * ln(z) * x * LMUF * NC - ln(z) * x * LMUA * pow(NC, -1) * pow(omz, -1) + 3. / 2. * ln(z) * x * LMUA * pow(NC, -1) + ln(z) * x * LMUA * NC * pow(omz, -1) - 3. / 2. * ln(z) * x * LMUA * NC - 5. / 4. * ln(z) * x * z * pow(NC, -1) + 5. / 4. * ln(z) * x * z * NC - 1. / 2. * ln(z) * x * z * LMUF * pow(NC, -1) + 1. / 2. * ln(z) * x * z * LMUF * NC + 1. / 2. * ln(z) * x * z * LMUA * pow(NC, -1) - 1. / 2. * ln(z) * x * z * LMUA * NC + 4 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 4 * ln(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 3. / 8. * ln(z) * pow(x, 2) * pow(NC, -1) * pow(poly2, -2) - 1. / 8. * ln(z) * pow(x, 2) * pow(NC, -1) * pow(poly2, -1) - 4 * ln(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) - ln(z) * pow(x, 2) * pow(NC, -1) * pow(xmz, -1) - 3. / 8. * ln(z) * pow(x, 2) * NC * pow(poly2, -2) + 5. / 8. * ln(z) * pow(x, 2) * NC * pow(poly2, -1) + 3. / 8. * ln(z) * pow(x, 3) * pow(NC, -1) * pow(poly2, -2) - 3. / 8. * ln(z) * pow(x, 3) * NC * pow(poly2, -2) + 1. / 2. * ln(z) * pow(x, 3) * NC * pow(poly2, -1) - 3. / 16. * ln(z) * pow(x, 4) * pow(NC, -1) * pow(poly2, -2) + 3. / 16. * ln(z) * pow(x, 4) * NC * pow(poly2, -2) - 3. / 16. * ln(z) * pow(x, 5) * pow(NC, -1) * pow(poly2, -2) + 3. / 16. * ln(z) * pow(x, 5) * NC * pow(poly2, -2) + 5. / 4. * pow(ln(z), 2) * pow(z, -1) * pow(NC, -1);
              tmp += -1. / 2. * pow(ln(z), 2) * pow(z, -1) * NC * pow(omz, -1) - 1. / 4. * pow(ln(z), 2) * pow(z, -1) * NC +
                     pow(ln(z), 2) * pow(NC, -1) * pow(omz, -1) - 1. / 4. * pow(ln(z), 2) * pow(NC, -1) + 1. / 4. * pow(ln(z), 2) * NC * pow(omz, -1) + 1. / 2. * pow(ln(z), 2) * NC + 1. / 4. * pow(ln(z), 2) * z * pow(NC, -1) - 1. / 4. * pow(ln(z), 2) * z * NC - 5. / 2. * pow(ln(z), 2) * x * pow(z, -1) * pow(NC, -1) + pow(ln(z), 2) * x * pow(z, -1) * NC * pow(omz, -1) + 1. / 2. * pow(ln(z), 2) * x * pow(z, -1) * NC - 2 * pow(ln(z), 2) * x * pow(NC, -1) * pow(omz, -1) + 1. / 2. * pow(ln(z), 2) * x * pow(NC, -1) - 1. / 2. * pow(ln(z), 2) * x * NC * pow(omz, -1) - pow(ln(z), 2) * x * NC - 1. / 2. * pow(ln(z), 2) * x * z * pow(NC, -1) + 1. / 2. * pow(ln(z), 2) * x * z * NC + 1. / 2. * pow(ln(z), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + pow(ln(z), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + 7. / 2. * ln(z) * ln(omx) * pow(z, -1) * pow(NC, -1) -
                     3. / 2. * ln(z) * ln(omx) * pow(z, -1) * NC + 4 * ln(z) * ln(omx) * pow(NC, -1) * pow(omz, -1) - 2 * ln(z) * ln(omx) * pow(NC, -1) - 3. / 2. * ln(z) * ln(omx) * NC * pow(omz, -1) + 5. / 2. * ln(z) * ln(omx) * NC - 7 * ln(z) * ln(omx) * x * pow(z, -1) * pow(NC, -1) + 3 * ln(z) * ln(omx) * x * pow(z, -1) * NC - 8 * ln(z) * ln(omx) * x * pow(NC, -1) * pow(omz, -1) + 4 * ln(z) * ln(omx) * x * pow(NC, -1) + 3 * ln(z) * ln(omx) * x * NC * pow(omz, -1) - 5 * ln(z) * ln(omx) * x * NC + 2 * ln(z) * ln(omx) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 3 * ln(z) * ln(omx) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + 3 * ln(z) * ln(omz) * pow(z, -1) * pow(NC, -1) - 5. / 2. * ln(z) * ln(omz) * pow(z, -1) * NC + 4 * ln(z) * ln(omz) * pow(NC, -1) * pow(omz, -1) - 7. / 2. * ln(z) * ln(omz) * pow(NC, -1) - 5. / 2. * ln(z) * ln(omz) * NC * pow(omz, -1);
              tmp += +11. / 2. * ln(z) * ln(omz) * NC - 6 * ln(z) * ln(omz) * x * pow(z, -1) * pow(NC, -1) + 5 * ln(z) * ln(omz) * x * pow(z, -1) * NC - 8 * ln(z) * ln(omz) * x * pow(NC, -1) * pow(omz, -1) + 7 * ln(z) * ln(omz) * x * pow(NC, -1) + 5 * ln(z) * ln(omz) * x * NC * pow(omz, -1) - 11 * ln(z) * ln(omz) * x * NC + ln(z) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 3 * ln(z) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + 9. / 4. * ln(omx) * pow(z, -1) * pow(NC, -1) + 1. / 6. * ln(omx) * pow(z, -1) * NF + 25. / 4. * ln(omx) * pow(z, -1) * NC + ln(omx) * pow(z, -1) * LMUF * NC + 3 * ln(omx) * pow(NC, -1) * pow(omz, -1) - 2 * ln(omx) * pow(NC, -1) + 1. / 6. * ln(omx) * NF * pow(omz, -1) - 1. / 2. * ln(omx) * NC * pow(omz, -1) - 14 * ln(omx) * NC + 1. / 4. * ln(omx) * LMUF * pow(NC, -1) - 9. / 4. * ln(omx) * LMUF * NC + 1. / 4. * ln(omx) * LMUA * pow(NC, -1) - 1. / 4. * ln(omx) * LMUA * NC - 3. / 8. * ln(omx) * z * pow(NC, -1) + 3. / 8. * ln(omx) * z * NC + 1. / 4. * ln(omx) * z * LMUF * pow(NC, -1) - 1. / 4. * ln(omx) * z * LMUF * NC + 1. / 4. * ln(omx) * z * LMUA * pow(NC, -1) - 1. / 4. * ln(omx) * z * LMUA * NC - 13. / 2. * ln(omx) * x * pow(z, -1) * pow(NC, -1) - 11. / 2. * ln(omx) * x * pow(z, -1) * NC - 2 * ln(omx) * x * pow(z, -1) * LMUF * NC - 8 * ln(omx) * x * pow(NC, -1) * pow(omz, -1) + 19. / 2. * ln(omx) * x * pow(NC, -1) + 2 * ln(omx) * x * NC * pow(omz, -1) + 21. / 2. * ln(omx) * x * NC - 1. / 2. * ln(omx) * x * LMUF * pow(NC, -1) + 9. / 2. * ln(omx) * x * LMUF * NC - 1. / 2. * ln(omx) * x * LMUA * pow(NC, -1) + 1. / 2. * ln(omx) * x * LMUA * NC + 3. / 4. * ln(omx) * x * z * pow(NC, -1) - 3. / 4. * ln(omx) * x * z * NC - 1. / 2. * ln(omx) * x * z * LMUF * pow(NC, -1) + 1. / 2. * ln(omx) * x * z * LMUF * NC - 1. / 2. * ln(omx) * x * z * LMUA * pow(NC, -1) + 1. / 2. * ln(omx) * x * z * LMUA * NC;
              tmp += -ln(omx) * pow(x, 2) * pow(NC, -1) + 3 * pow(ln(omx), 2) * pow(z, -1) * pow(NC, -1) - 3. / 4. * pow(ln(omx), 2) * pow(z, -1) * NC + 3 * pow(ln(omx), 2) * pow(NC, -1) * pow(omz, -1) - 9. / 4. * pow(ln(omx), 2) * pow(NC, -1) - 1. / 4. * pow(ln(omx), 2) * NC * pow(omz, -1) + 7. / 4. * pow(ln(omx), 2) * NC - 1. / 4. * pow(ln(omx), 2) * z * pow(NC, -1) + 1. / 4. * pow(ln(omx), 2) * z * NC - 6 * pow(ln(omx), 2) * x * pow(z, -1) * pow(NC, -1) + 3. / 2. * pow(ln(omx), 2) * x * pow(z, -1) * NC - 6 * pow(ln(omx), 2) * x * pow(NC, -1) * pow(omz, -1) + 9. / 2. * pow(ln(omx), 2) * x * pow(NC, -1) + 1. / 2. * pow(ln(omx), 2) * x * NC * pow(omz, -1) - 7. / 2. * pow(ln(omx), 2) * x * NC + 1. / 2. * pow(ln(omx), 2) * x * z * pow(NC, -1) - 1. / 2. * pow(ln(omx), 2) * x * z * NC + 2 * pow(ln(omx), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 2 * pow(ln(omx), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + 9. / 2. * ln(omx) * ln(omz) * pow(z, -1) * pow(NC, -1) - 2 * ln(omx) * ln(omz) * pow(z, -1) * NC + 4 * ln(omx) * ln(omz) * pow(NC, -1) * pow(omz, -1) - 4 * ln(omx) * ln(omz) * pow(NC, -1) - ln(omx) * ln(omz) * NC * pow(omz, -1) + 9. / 2. * ln(omx) * ln(omz) * NC - 1. / 2. * ln(omx) * ln(omz) * z * pow(NC, -1) + 1. / 2. * ln(omx) * ln(omz) * z * NC - 9 * ln(omx) * ln(omz) * x * pow(z, -1) * pow(NC, -1) + 4 * ln(omx) * ln(omz) * x * pow(z, -1) * NC - 8 * ln(omx) * ln(omz) * x * pow(NC, -1) * pow(omz, -1) + 8 * ln(omx) * ln(omz) * x * pow(NC, -1) + 2 * ln(omx) * ln(omz) * x * NC * pow(omz, -1) - 9 * ln(omx) * ln(omz) * x * NC + ln(omx) * ln(omz) * x * z * pow(NC, -1) - ln(omx) * ln(omz) * x * z * NC + 3 * ln(omx) * ln(omz) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 2 * ln(omx) * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + 7. / 4. * ln(omz) * pow(z, -1) * pow(NC, -1);
              tmp += +1. / 6. * ln(omz) * pow(z, -1) * NF + 23. / 4. * ln(omz) * pow(z, -1) * NC - 1. / 2. * ln(omz) * pow(z, -1) * LMUA * pow(NC, -1) + 1. / 2. * ln(omz) * pow(z, -1) * LMUA * NC + 2 * ln(omz) * pow(NC, -1) * pow(omz, -1) + 1. / 2. * ln(omz) * pow(NC, -1) * pow(omxmz, -2) - ln(omz) * pow(NC, -1) * pow(omxmz, -1) + ln(omz) * pow(NC, -1) + 1. / 6. * ln(omz) * NF * pow(omz, -1) - ln(omz) * NC * pow(omz, -1) - 1. / 2. * ln(omz) * NC * pow(omxmz, -2) + 1. / 2. * ln(omz) * NC * pow(omxmz, -1) - 13 * ln(omz) * NC + 1. / 4. * ln(omz) * LMUF * pow(NC, -1) - 1. / 4. * ln(omz) * LMUF * NC + 5. / 4. * ln(omz) * LMUA * pow(NC, -1) - 5. / 4. * ln(omz) * LMUA * NC + 1. / 4. * ln(omz) * z * pow(NC, -1) * pow(omxmz, -2) - 2 * ln(omz) * z * pow(NC, -1) * pow(omxmz, -1) + 17. / 8. * ln(omz) * z * pow(NC, -1) - 1. / 4. * ln(omz) * z * NC * pow(omxmz, -2) + 7. / 2. * ln(omz) * z * NC * pow(omxmz, -1) - 25. / 8. * ln(omz) * z * NC + 1. / 4. * ln(omz) * z * LMUF * pow(NC, -1) - 1. / 4. * ln(omz) * z * LMUF * NC + 1. / 4. * ln(omz) * z * LMUA * pow(NC, -1) - 1. / 4. * ln(omz) * z * LMUA * NC - 3. / 4. * ln(omz) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -2) + 5. / 2. * ln(omz) * pow(z, 2) * pow(NC, -1) * pow(omxmz, -1) + 3. / 4. * ln(omz) * pow(z, 2) * NC * pow(omxmz, -2) - 7. / 2. * ln(omz) * pow(z, 2) * NC * pow(omxmz, -1) - 9. / 2. * ln(omz) * x * pow(z, -1) * pow(NC, -1) - 7. / 2. * ln(omz) * x * pow(z, -1) * NC + ln(omz) * x * pow(z, -1) * LMUA * pow(NC, -1) - ln(omz) * x * pow(z, -1) * LMUA * NC - 6 * ln(omz) * x * pow(NC, -1) * pow(omz, -1) - 3. / 2. * ln(omz) * x * pow(NC, -1) * pow(omxmz, -2) + 3 * ln(omz) * x * pow(NC, -1) * pow(omxmz, -1) + 5. / 2. * ln(omz) * x * pow(NC, -1) + 4 * ln(omz) * x * NC * pow(omz, -1) + 3. / 2. * ln(omz) * x * NC * pow(omxmz, -2) - 3 * ln(omz) * x * NC * pow(omxmz, -1);
              tmp += +13. / 2. * ln(omz) * x * NC - 1. / 2. * ln(omz) * x * LMUF * pow(NC, -1) + 1. / 2. * ln(omz) * x * LMUF * NC - 5. / 2. * ln(omz) * x * LMUA * pow(NC, -1) + 5. / 2. * ln(omz) * x * LMUA * NC + 3. / 4. * ln(omz) * x * z * pow(NC, -1) - 3. / 4. * ln(omz) * x * z * NC - 1. / 2. * ln(omz) * x * z * LMUF * pow(NC, -1) + 1. / 2. * ln(omz) * x * z * LMUF * NC - 1. / 2. * ln(omz) * x * z * LMUA * pow(NC, -1) + 1. / 2. * ln(omz) * x * z * LMUA * NC + 3. / 2. * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -2) - 3. / 2. * ln(omz) * pow(x, 2) * pow(NC, -1) * pow(omxmz, -1) - 3. / 2. * ln(omz) * pow(x, 2) * NC * pow(omxmz, -2) + 3. / 2. * ln(omz) * pow(x, 2) * NC * pow(omxmz, -1) - 1. / 2. * ln(omz) * pow(x, 3) * pow(NC, -1) * pow(omxmz, -2) + 1. / 2. * ln(omz) * pow(x, 3) * NC * pow(omxmz, -2) + 5. / 2. * pow(ln(omz), 2) * pow(z, -1) * pow(NC, -1) - 5. / 4. * pow(ln(omz), 2) * pow(z, -1) * NC + 3. / 2. * pow(ln(omz), 2) * pow(NC, -1) * pow(omz, -1) - 2 * pow(ln(omz), 2) * pow(NC, -1) - pow(ln(omz), 2) * NC * pow(omz, -1) + 11. / 4. * pow(ln(omz), 2) * NC - 1. / 4. * pow(ln(omz), 2) * z * pow(NC, -1) + 1. / 4. * pow(ln(omz), 2) * z * NC - 5 * pow(ln(omz), 2) * x * pow(z, -1) * pow(NC, -1) + 5. / 2. * pow(ln(omz), 2) * x * pow(z, -1) * NC - 3 * pow(ln(omz), 2) * x * pow(NC, -1) * pow(omz, -1) + 4 * pow(ln(omz), 2) * x * pow(NC, -1) + 2 * pow(ln(omz), 2) * x * NC * pow(omz, -1) - 11. / 2. * pow(ln(omz), 2) * x * NC + 1. / 2. * pow(ln(omz), 2) * x * z * pow(NC, -1) - 1. / 2. * pow(ln(omz), 2) * x * z * NC + 2 * pow(ln(omz), 2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + 1. / 2. * pow(ln(omz), 2) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * NC * pow(sqrtxz2, -1);
              tmp += -3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 5. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 13. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(omz, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) - 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * NC * pow(sqrtxz2, -1) + 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 29. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1) - 69. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1) - 29. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(NC, -1) * pow(sqrtxz2, -1);
              tmp += +69. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * NC * pow(sqrtxz2, -1) - 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1) + 9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 111. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) - 9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1) - 11. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2);
              tmp += -1. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) *
                         pow(sqrtxz2, -1) * pow(poly2, -1) +
                     9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 7. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) +
                     Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(z, -1) * NC * pow(sqrtxz2, -1) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 5. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 13. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) * pow(omz, -1);
              tmp += +Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * NC * pow(sqrtxz2, -1) + 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(z, -1) * NC * pow(sqrtxz2, -1) - 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 29. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 2. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1) + 69. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * NC * pow(sqrtxz2, -1) + 29. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * pow(NC, -1) * pow(sqrtxz2, -1) - 69. / 8. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * x * z * NC * pow(sqrtxz2, -1) + 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1) - 9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 3 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1);
              tmp += -111. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) + 9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1) + 11. / 16. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 2) * NC * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 9. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 7. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 32. * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * pow(x, -1) * sqrtxz2) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) +
                     Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1);
              tmp += -1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(z, -1) * NC * pow(sqrtxz2, -1) + 3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 5. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 7. / 4. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 13. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - 1. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) * pow(omz, -1) +
                     Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) + 3 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1) - 3 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 29. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 2. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1) +
                     69. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * NC * pow(sqrtxz2, -1) + 29. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1) - 69. / 8. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * NC * pow(sqrtxz2, -1) + 3 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1);
              tmp += -Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1) - 9. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) +
                     3 * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 111. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) + 9. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1) + 11. / 16. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) + Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) - Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 9. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 1. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 9. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 7. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) - 3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2);
              tmp += +3. / 32. * Li2(1. / 2. - 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(z, -1) * NC * pow(sqrtxz2, -1) - 3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 5. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 7. / 4. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) + 13. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + 1. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) * pow(omz, -1) - Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * NC * pow(sqrtxz2, -1) - 3 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + 3. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(z, -1) * NC * pow(sqrtxz2, -1) + 3 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 29. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * pow(NC, -1) * pow(sqrtxz2, -1) - 3. / 2. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * NC * pow(sqrtxz2, -1) * pow(omz, -1) - 69. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * NC * pow(sqrtxz2, -1) - 29. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * pow(NC, -1) * pow(sqrtxz2, -1);
              tmp += +69. / 8. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * x * z * NC * pow(sqrtxz2, -1) - 3 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(z, -1) * NC * pow(sqrtxz2, -1) + 9. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) + 3. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) - 3 * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) + 111. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * pow(NC, -1) * pow(sqrtxz2, -1) - 9. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) * pow(omz, -1) - 11. / 16. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 2) * NC * pow(sqrtxz2, -1) - Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(z, -1) * pow(NC, -1) * pow(sqrtxz2, -1) + Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 3) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(omz, -1) - 9. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 1. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -1) + 9. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -2);
              tmp += -7. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 4) * NC * pow(sqrtxz2, -1) * pow(poly2, -1) + 3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 6) * pow(NC, -1) * pow(sqrtxz2, -1) * pow(poly2, -2) - 3. / 32. * Li2(1. / 2. + 1. / 2. * sqrtxz2 - 1. / 2. * x) * pow(x, 6) * NC * pow(sqrtxz2, -1) * pow(poly2, -2) - 2 * Li2(1 - x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 3. / 2. * Li2(1 - x * pow(z, -1)) * pow(z, -1) * pow(NC, -1) + Li2(1 - x * pow(z, -1)) * pow(z, -1) * NC * pow(omz, -1) - 1. / 2. * Li2(1 - x * pow(z, -1)) * pow(z, -1) * NC + 1. / 2. * Li2(1 - x * pow(z, -1)) * pow(NC, -1) * pow(omz, -1) + 1. / 2. * Li2(1 - x * pow(z, -1)) * pow(NC, -1) - 1. / 2. * Li2(1 - x * pow(z, -1)) * NC * pow(omz, -1) - 3. / 2. * Li2(1 - x * pow(z, -1)) * NC + 4 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) * pow(omz, -1) - 3 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * pow(NC, -1) - 2 * Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * NC * pow(omz, -1) + Li2(1 - x * pow(z, -1)) * x * pow(z, -1) * NC - Li2(1 - x * pow(z, -1)) * x * pow(NC, -1) * pow(omz, -1) - Li2(1 - x * pow(z, -1)) * x * pow(NC, -1) + Li2(1 - x * pow(z, -1)) * x * NC * pow(omz, -1) + 3 * Li2(1 - x * pow(z, -1)) * x * NC - 2 * Li2(1 - x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) * pow(omz, -1) + 2 * Li2(1 - x * pow(z, -1)) * pow(x, 2) * pow(z, -1) * pow(NC, -1) - 2 * Li2(-x) * pow(z, -1) * pow(NC, -1) + 2 * Li2(-x) * pow(NC, -1) - Li2(-x) * NC - Li2(-x) * z * pow(NC, -1) + Li2(-x) * z * NC - 4 * Li2(-x) * x * pow(z, -1) * pow(NC, -1) + 4 * Li2(-x) * x * pow(NC, -1) - 2 * Li2(-x) * x * NC - 2 * Li2(-x) * x * z * pow(NC, -1) + 2 * Li2(-x) * x * z * NC - 2 * Li2(-x) * pow(x, 2) * pow(z, -1) * pow(NC, -1);
              tmp += +2 * Li2(-x) * pow(x, 2) * pow(NC, -1) - 2 * Li2(-x) * pow(x, 2) * NC - 1. / 2. * Li2(x) * pow(z, -1) * pow(NC, -1) - 2 * Li2(x) * pow(z, -1) * NC * pow(omz, -1) - 1. / 2. * Li2(x) * pow(z, -1) * NC - 2 * Li2(x) * pow(NC, -1) * pow(omz, -1) + Li2(x) * pow(NC, -1) + 2 * Li2(x) * NC * pow(omz, -1) + 4 * Li2(x) * NC + Li2(x) * z * pow(NC, -1) - Li2(x) * z * NC + Li2(x) * x * pow(z, -1) * pow(NC, -1) + 4 * Li2(x) * x * pow(z, -1) * NC * pow(omz, -1) - 5 * Li2(x) * x * pow(z, -1) * NC + 4 * Li2(x) * x * pow(NC, -1) * pow(omz, -1) - 3 * Li2(x) * x * pow(NC, -1) - 4 * Li2(x) * x * NC * pow(omz, -1) + 5 * Li2(x) * x * NC - Li2(x) * x * z * pow(NC, -1) + Li2(x) * x * z * NC - 2 * Li2(x) * pow(x, 2) * pow(NC, -1) * pow(omz, -1) + Li2(x) * pow(x, 2) * pow(NC, -1) - Li2(x) * pow(x, 2) * NC - 1. / 2. * Li2(z) * pow(z, -1) * NC + Li2(z) * pow(NC, -1) * pow(omz, -1) - 2 * Li2(z) * pow(NC, -1) - 1. / 2. * Li2(z) * NC * pow(omz, -1) + 2 * Li2(z) * NC + Li2(z) * x * pow(z, -1) * NC - 2 * Li2(z) * x * pow(NC, -1) * pow(omz, -1) + 4 * Li2(z) * x * pow(NC, -1) + Li2(z) * x * NC * pow(omz, -1) - 4 * Li2(z) * x * NC - Li2(z) * pow(x, 2) * pow(z, -1) * pow(NC, -1) + Li2(z) * pow(x, 2) * pow(NC, -1) * pow(omz, -1);

 """
    create_file_with_split_orders(s, output_file, "tmp")
