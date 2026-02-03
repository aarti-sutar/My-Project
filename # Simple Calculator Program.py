# Simple Calculator Program

# Take input from the user
numberA = float(input("Enter Number A: "))
numberB = float(input("Enter Number B: "))

# Select arithmetic operation
print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation
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

else:
    print("Invalid Choice!")
