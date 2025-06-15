def mod():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if b == 0:
        print("Error: Cannot mod by zero.")
        return None
    else:
        result = a % b
        print("The remainder is:", result)
        return result

mod()
