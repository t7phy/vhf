import unittest

from dev.sidis_reorder_code.step1_pol.ordered.python.c2pq2qpes import C2Pq2qpEs_DR0123_scheme
from dev.sidis_reorder_code.step1_pol.ordered.python.c2pq2qpbes import C2Pq2qpbEs_DR0123_scheme


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
        self.x_values = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.25, 0.5, 0.9]
        self.z_values = [1e-3, 1e-2, 1e-1, 0.25, 0.5, 0.9]
        self.cx_values = ["D", "R", "0", "1", "2", "3"]
        self.cz_values = ["D", "R", "0", "1", "2", "3"]
        # Check what orders there are in the original code
        self.orders = ["000", "001", "002", "010", "011", "100", "110", "020", "101"]
        self.LMUA = 1
        self.LMUR = 1
        self.LMUF = 1

    def func_loop_orders(self, fplus, fminus):
        for order in self.orders:
            for inx in self.x_values:
                for inz in self.z_values:
                    for cx in self.cx_values:
                        for cz in self.cz_values:
                            result_plus = fplus(
                                inx,
                                inz,
                                cx,
                                cz,
                                order,
                                LMUR=self.LMUR,
                                LMUF=self.LMUF,
                                LMUA=self.LMUA,
                                ndecimals=self.ndecimal,
                            ).real
                            result_minus = fminus(
                                inx,
                                inz,
                                cx,
                                cz,
                                order,
                                LMUR=self.LMUR,
                                LMUF=self.LMUF,
                                LMUA=self.LMUA,
                                ndecimals=self.ndecimal,
                            ).real

                            # The functions should give the same result but with a minus sign difference.
                            if round(abs(result_minus + result_plus), 4) == 0:
                                assert True
                            else:
                                print(
                                    f"inx: {inx}, inz: {inz}, cx: {cx}, cz: {cz}, muR: {self.LMUR}, muF: {self.LMUF}, muA: {self.LMUA}, order: {order}"
                                )
                                print(
                                    f"result_plus: {result_plus}, result_minus: {result_minus}, approximate difference: {round(abs(result_minus + result_plus), 4)}"
                                )
                                assert False

    def test_dif(self):
        self.func_loop_orders(fplus=C2Pq2qpEs_DR0123_scheme, fminus=C2Pq2qpbEs_DR0123_scheme)


# def test_higher_orders(self):


if __name__ == "__main__":
    unittest.main()
