def safe_divide(numerator, denominator):
    try:
         
       num= float(numerator)
       den= float(denominator)    
    except ZeroDivisionError :
        print("Error: Cannot divide by zero.")
    except ValueError :
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {num / den}")
        return num / de

    

     
