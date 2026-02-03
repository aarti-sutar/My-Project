
number1 = float(input("Enter first number1 : "))
number2 = float(input("Enter second number2 : "))

operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

if operation == "add":
    print("Result:", number1 + number2)
elif operation == "subtract":
    print("Result:", number1 - number2)
elif operation == "multiply":
    print("Result:", number1 * number2)
elif operation == "divide":
    if number2 == 0:
        print("Error: Division by zero not allowed")
    else:
        print("Result:", number1 / number2)
else:
    print("Invalid operation")
    