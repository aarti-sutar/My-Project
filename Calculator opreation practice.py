
number1 = float(input("enter number1 : "))
number2 = float(input("enter number2 : "))
number3 = float(input("Enter Number3 : "))
number4 = float(input("Enter Number4 : "))

print("\nselect opretion: ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    result = numberA + numberB
    print("Result:", result)

elif choice == '2':
    result = numberA - numberB
    print("Result:", result)

elif choice == '3':
    result = numberA * numberB
    print("Result:", result)

elif choice == '4':
    if numberB != 0:
        result = numberA / numberB
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero!")
