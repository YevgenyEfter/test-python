from Backend.calc_backend import CalculatorBackend

EXIT_CODE = 9


def main():
    calculator = CalculatorBackend()

    print("Welcome to the Calculator!\n")

    userRequest = 0
    while userRequest != EXIT_CODE:
        print("Please choose an operation:")
        print("1. Add numbers.")
        print("2. Subtract numbers.")
        print("3. Multiply numbers.")
        print("4. Divide numbers.")
        print("5. Divide integer numbers.")
        print("6. Calculate factorial.\n")
        print(str(EXIT_CODE) + ". Exit.")

        userRequest = int(input())

        if userRequest == EXIT_CODE:
            break

        if userRequest < 6:
            a = int(input("Please enter the 1st number: "))
            b = int(input("Please enter the 2nd number: "))
        else:
            a = int(input("Please enter a number: "))

        result = -1

        if userRequest == 1:
            result = calculator.add(a, b)
        elif userRequest == 2:
            result = calculator.subtract(a, b)
        elif userRequest == 3:
            result = calculator.multiply(a, b)
        elif userRequest == 4:
            try:
                result = calculator.divide(a, b)
            except ZeroDivisionError:
                print("Can't divide by 0. Try again.")
                continue
        elif userRequest == 5:
            result = calculator.integer_divide(a, b)
        elif userRequest == 6:
            result = calculator.factorial(a)

        print("The result is " + str(result))

    print("Thanks for using the Calculator!")
