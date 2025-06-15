def divide():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    else:
        result = a / b
        print("The result is:", result)
        return result

divide()
