num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
oper = input("Choose the operation (+, -, *, /):" )
match oper:
    case "+":
        result=num1 + num2
        print(f"The result is {result}")
    case "-":
        result=num1 - num2
        print(f"The result is {result}")
    case "*":
        result=num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
             result=num1 / num2
             print(f"The result is {result}")    
    case _:
        print()

