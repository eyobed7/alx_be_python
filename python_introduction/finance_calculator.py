monthly_income = float(input("Enter your monthly income:"))
monthly_expense = float(input("Enter your total monthly expenses:"))
monthly_Savings = monthly_income - monthly_expense
print("Your monthly savings are $",monthly_Savings)
Projected_Savings = monthly_Savings * 12 + (monthly_Savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:$", Projected_Savings) 

