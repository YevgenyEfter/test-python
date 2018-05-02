from factorial import Factorial
import unittest


class TestFactorial(unittest.TestCase):
    def setUp(self):
        self.factorial = Factorial()

    def test_factorial(self):
        self.assertEqual(self.factorial.calcFactorial(3), 6)
        self.assertRaises(ValueError, self.factorial.calcFactorial, -1)


if __name__ == "__main__":
    unittest.main()