def calculator():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation!")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers.")

        if input("Do you want to calculate again? (y/n): ") != 'y':
            break

calculator()