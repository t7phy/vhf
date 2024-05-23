import unittest

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

modules = {
    "c1pg2qeq":"C1Pg2qEq",
    "c1pq2geq",
    "c1pq2qeq",
    "c2pg2geq",
    "c2pg2qeq",
    "c2pq2geq",
    "c2pq2qbeq",
    "c2pq2qeq",
    "c2pq2qeqp",
    "c2pq2qpbes",
    "c2pq2qpeq",
    "c2pq2qpeqp",
    "c2pq2qpes",
}

for module in modules:
    globals()[f"ordered_{module}"] = __import__(
        f"sidisprocessed.step1pol.ordered.python.{module}", fromlist=[""]
    )
    globals()[f"original_{module}"] = __import__(
        f"sidisprocessed.step1pol.original.python.{module}", fromlist=[""]
    )


class TestResults(unittest.TestCase):
    def test_same_result_per_func(self):
        assert True
