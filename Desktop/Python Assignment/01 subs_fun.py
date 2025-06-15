def subs():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    d = float(input("Enter fourth number: "))
    
    result = a - b - c - d
    result = abs(result)
    
    print("The result is:", result)
    return result

subs()