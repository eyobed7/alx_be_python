def safe_divide(numerator, denominator):
    try:
        numerator=float(input("Enter the numerator value"))
        denominator=float(input("Enter the denominator value"))       
    except ZeroDivisionError :
        print("Error: Cannot divide by zero.")
    except ValueError :
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {numerator / denominator}")
        return numerator / denominator

    

     
