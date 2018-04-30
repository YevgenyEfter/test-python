class Factorial:
    def calcFactorial(self, number):
        if number < 0:
            raise ValueError("Number can't be negative.")

        result = 1
        for i in range(1, number + 1):
            result *= i

        return result
