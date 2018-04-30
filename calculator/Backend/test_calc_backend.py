from calc_backend import CalculatorBackend
import unittest


class TestCalculatorBackend(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorBackend()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 4), 2.5)

    def test_integer_divide(self):
        self.assertEqual(self.calculator.integer_divide(10, 4), 2)

    #def test_factorial(self):
        #self.assertEqual(self.calculator.factorial(3), 6)


if __name__ == "__main__":
    unittest.main()