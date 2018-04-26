from Backend.Operations.factorial import Factorial

class CalculatorBackend:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def integer_divide(self, a, b):
        return a // b

    def factorial(self, number):
        return Factorial().calcFactorial(number)