def safe_divide(numerator, denominator):
    try:
        numerator=(input("Enter the numerator value"))
        denominator=(input("Enter the denominator value")) 
        float(numerator)
        float(denominator)    
    except ZeroDivisionError :
        print("Error: Cannot divide by zero.")
    except ValueError :
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {numerator / denominator}")
        return numerator / denominator

    

     
