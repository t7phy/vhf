import unittest
from importlib import import_module
import re
import os
import cmath
import math

modules = {
    "c1pg2qeq": "C1Pg2qEq_DR0123_scheme",
    "c1pq2geq": "C1Pq2gEq_DR0123_scheme",
    "c1pq2qeq": "C1Pq2qEq_DR0123_scheme",
    "c2pg2geq": "C2Pg2gEq_DR0123_scheme",
    "c2pg2qeq": "C2Pg2qEq_DR0123_scheme",
    "c2pq2geq": "C2Pq2gEq_DR0123_scheme",
    "c2pq2qbeq": "C2Pq2qbEq_DR0123_scheme",
    "c2pq2qeq": "C2Pq2qEq_DR0123_scheme",
    "c2pq2qeqp": "C2Pq2qEqp_DR0123_scheme",
    "c2pq2qpbes": "C2Pq2qpbEs_DR0123_scheme",
    "c2pq2qpeq": "C2Pq2qpEq_DR0123_scheme",
    "c2pq2qpeqp": "C2Pq2qpEqp_DR0123_scheme",
    "c2pq2qpes": "C2Pq2qpEs_DR0123_scheme",
}

functions_ordered = dict()
functions_original = dict()
for module, func_name in modules.items():
    module_ordered = import_module(f"sidisprocessed.step1pol.ordered.python.{module}")
    module_original = import_module(f"sidisprocessed.step1pol.original.python.{module}")

    functions_ordered[func_name] = getattr(module_ordered, func_name)
    functions_original[func_name] = getattr(module_original, func_name)

    del module_ordered
    del module_original


def get_orders():
    dir = "./sidisprocessed/step1pol/ordered/python"
    pattern = r'order == "(.*?)"'
    files = os.listdir(dir)
    orders = list()
    # Convert order to if statement and/or use our library conventions
    for filename in files:
        file_path = dir + "/" + filename
        if filename.endswith(".py"):
            with open(file_path, "r") as file:
                for line in file:
                    order = re.search(pattern, line)
                    if order:
                        order = order.group(1)
                        if order not in orders:
                            orders.append(order)

    print(orders)


def check_close_enough(value1, value2, percentage):
    """
    Check if the relative difference between values is smaller than a given percentage
    value1: float
    value2: float
    percentage: float, 1% is 0.01
    """
    # Avoid devisions by 0
    if value1 == 0:
        value1 = percentage * 1e-3
    if value2 == 0:
        value2 = percentage * 1e-3

    diff = abs(value1 - value2)

    # Ensure biggest relative difference is measured
    if abs(value1) < abs(value2):
        relative_diff = diff / abs(value1)
    else:
        relative_diff = diff / abs(value2)

    if relative_diff < percentage:
        return True
    else:
        return False


class TestComparisonOrderedAndOriginal(unittest.TestCase):
    def setUp(self):
        # Precission in decimals
        self.precision = 1e-4  # 0.01%
        self.ndecimal = 10

        # TODO: Note that x-values below 1e-6 do not pass.
        self.x_values = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.25, 0.5, 0.9]
        self.z_values = [1e-3, 1e-2, 1e-1, 0.25, 0.5, 0.9]
        self.cx_values = ["D", "R", "0", "1", "2", "3"]
        self.cz_values = ["D", "R", "0", "1", "2", "3"]
        # Check what orders there are in the original code
        self.orders = ["000", "001", "002", "010", "011", "100", "110", "020", "101"]

        self.func_names = functions_ordered.keys()

    def func_loop_orders(self, LMUR, LMUF, LMUA, orders):
        for func_name in self.func_names:
            for inx in self.x_values:
                for inz in self.z_values:
                    for cx in self.cx_values:
                        for cz in self.cz_values:
                            # Call the functions and get the results
                            result_ordered = 0
                            for order in orders:
                                result_ordered += functions_ordered[func_name](
                                    inx,
                                    inz,
                                    cx,
                                    cz,
                                    order,
                                    LMUR=LMUR,
                                    LMUF=LMUF,
                                    LMUA=LMUA,
                                    ndecimals=self.ndecimal,
                                ).real
                            result_original = functions_original[func_name](
                                inx,
                                inz,
                                cx,
                                cz,
                                order,
                                LMUR=LMUR,
                                LMUF=LMUF,
                                LMUA=LMUA,
                                ndecimals=self.ndecimal,
                            ).real

                            if check_close_enough(result_ordered, result_original, self.precision):
                                assert True
                            else:
                                print(f"func_name: {func_name}, inx: {inx}, inz: {inz}, cx: {cx}, cz: {cz}, muR: {LMUR}, muF: {LMUF}, muA: {LMUA}, order: {orders}")
                                print(f"result_ordered: {result_ordered}, result_original: {result_original}, approximate relative difference: {round(abs(result_ordered - result_original) / abs(result_original), 6) * 100}%")
                                assert False

    def test_all_orders_LMUX_zero(self):
        LMUR = 0.0
        LMUF = 0.0
        LMUA = 0.0
        orders = self.orders
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_all_orders_LMUX(self):
        LMUR = 0.9
        LMUF = 0.9
        LMUA = 0.9
        orders = self.orders
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_000_order(self):
        LMUR = 0.0
        LMUF = 0.0
        LMUA = 0.0
        orders = ["000"]
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_LMUR_order(self):
        LMUR = 0.9
        LMUF = 0.0
        LMUA = 0.0
        orders = ["000", "100"]
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_LMUF_order(self):
        LMUR = 0.0
        LMUF = 0.9
        LMUA = 0.0
        orders = ["000", "010", "020"]
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_LMUA_order(self):
        LMUR = 0.0
        LMUF = 0.0
        LMUA = 0.9
        orders = ["000", "001", "002"]
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_LMUR_LMUF_order(self):
        LMUR = 0.9
        LMUF = 0.9
        LMUA = 0.0
        orders = ["000", "100", "010", "110", "020"]
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_LMUR_LMUA_order(self):
        LMUR = 0.9
        LMUF = 0.0
        LMUA = 0.9
        orders = ["000", "100", "001", "101", "002"]
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)

    def test_LMUF_LMUA_order(self):
        LMUR = 0.0
        LMUF = 0.9
        LMUA = 0.9
        orders = ["000", "010", "001", "011", "002", "020"]
        self.func_loop_orders(LMUR, LMUF, LMUA, orders)


# def test_higher_orders(self):


if __name__ == "__main__":
    unittest.main()
