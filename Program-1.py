class Calculator:
    def calculate(self, a, b, operation):
        if operation == "add":
            return a + b
        elif operation == "sub":
            return a - b
        elif operation == "mul":
            return a * b
        elif operation == "div":
            if b == 0:
                return "Error division by zero"
            return a / b
        else:
            return "Invalid operation"


if __name__ == "__main__":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    op = input("Enter operation (add, sub, mul, div): ").lower()

    calc = Calculator()
    print("Result:", calc.calculate(a, b, op))
