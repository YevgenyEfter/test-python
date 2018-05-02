from calc_backend import CalculatorBackend
import unittest
from unittest import mock
from unittest.mock import patch


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

    @mock.patch("calc_backend.Factorial.calcFactorial")
    def test_factorial_decorator(self, mocked_calcFactorial):
        mocked_calcFactorial.return_value = 120

        result = self.calculator.factorial(3)

        self.assertTrue(mocked_calcFactorial.called)
        mocked_calcFactorial.assert_called_with(3)
        self.assertEqual(result, 120)

    def test_factorial_context_manager(self):
        with patch("calc_backend.Factorial.calcFactorial") as mocked_calcFactorial:
            mocked_calcFactorial.return_value = 120

            result = self.calculator.factorial(3)

            self.assertTrue(mocked_calcFactorial.called)
            mocked_calcFactorial.assert_called_with(3)
            self.assertEqual(result, 120)


if __name__ == "__main__":
    unittest.main()