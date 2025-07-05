def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter the number corresponding to the operation (1/2/3/4): "))
        if choice not in [ 1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print(f"The result is: {num1 + num2}")
        elif choice == 2:
            print(f"The result is: {num1 - num2}")
        elif choice == 3:
            print(f"The result is: {num1 * num2}")
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"The result is: {num1 / num2}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the calculator
calculator()