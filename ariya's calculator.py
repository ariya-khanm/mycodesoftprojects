def add(m, n):
    return m + n

def subtract(m, n):
    return m - n

def multiply(m, n):
    return m * n

def divide(m, n):
    return m / n

def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    # Calculation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = divide(num1, num2)
    else:
        print("Invalid operation!")
        return

    # Output
    print("Result:", result)

calculator() 