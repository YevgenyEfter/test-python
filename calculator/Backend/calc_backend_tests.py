from calc_backend import CalculatorBackend
import unittest


class CalculatorBackendTests(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorBackend()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()