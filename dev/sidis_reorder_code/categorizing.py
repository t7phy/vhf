import re
import os


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
    indent = re.split(f"{var}", s)[0]
    lines = re.split(rf"\s*{var}\s*=\s*|\s*{var}\s*\+=\s*", s)
    lines = [line.replace("\n", "") for line in lines if line]
    return lines, indent


def get_all_present_orders(dict_dict):
    dict_list = list(dict_dict.values())
    dict_set = set(key for d in dict_list for key in d)
    return sorted(list(dict_set))


def create_file_with_split_orders(s: str, var: str):
    """
    Function to create a file with the split orders.
    s: str, the string to be split.
    var: Variable name to be split, e.g. tmp or res.
    output_file: str, the file to write the output to.
    """
    # Split based on var position, respect original
    lines, indent = split_to_line_per_var(s, var)

    # Remove res references, put in later
    orders_per_line = dict()
    for i, line in enumerate(lines):
        line = remove_var_n_semicolon(line, var)
        orders_per_line[i] = split_to_order(line)

    orders_present = get_all_present_orders(orders_per_line)

    if "uncategorized" in orders_present:
        print("\t!!! Uncategorized terms present, please categorize manually.  !!!")

    s_ordered = [f"{indent}// Split orders:\n"]
    s_ordered.append(f"{indent}{var} = 0;\n")
    for order in orders_present:
        s_ordered.append(f"{indent}// Order {order}:\n")
        for _, line in orders_per_line.items():
            if order not in line:
                continue
            s_ordered.append(f"{indent}{var} += ")
            terms = line[order]
            for i, term in enumerate(terms):
                term = revert_minus_sign(term)
                s_ordered.append(f"{term} + ")
            s_ordered.append("0;\n")

    return s_ordered


def categorize_a_file(
    file_name,
    folder_path,
    original_folder_name="original",
    ordered_folder_name="ordered",
):
    # Read the file line by line
    file_path = folder_path + f"/{original_folder_name}/cpp/{file_name}"
    print(f"File: {file_path}")
    categorized_file = list()
    with open(file_path, "r") as file:
        skip_until_i = 0
        for i, line in enumerate(file):
            # A bit of a weird structured loop
            if i < 15:
                categorized_file.append(line)
            # elif i < skip_until_i:
            #     continue
            elif "res" in line and not "double" in line and not "return" in line:
                skip_until_i = i
                lines_to_convert = str()
                while "return" not in line:
                    lines_to_convert += line
                    line = next(file)
                    skip_until_i += 1

                skip_until_i -= 1
                categorized_file += create_file_with_split_orders(
                    lines_to_convert, "res"
                )
                categorized_file.append(line)
            elif "tmp" in line and not "double" in line and not "return" in line:
                skip_until_i = i
                lines_to_convert = str()
                while "res" not in line:
                    lines_to_convert += line
                    skip_until_i += 1
                    line = next(file)

                categorized_file += create_file_with_split_orders(
                    lines_to_convert, "tmp"
                )
                categorized_file.append(line)
            else:
                categorized_file.append(line)

    file_path = folder_path + f"/{ordered_folder_name}/cpp/{file_name}"

    with open(file_path, "w") as file:
        for line in categorized_file:
            file.write(line)


if __name__ == "__main__":
    folder_path = "./sidisprocessed/step1pol"
    files = os.listdir(folder_path + "/original/cpp")
    for file_name in files:
        categorize_a_file(file_name, folder_path)
