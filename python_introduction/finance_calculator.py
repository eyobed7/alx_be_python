Monthly_Income = float(input("Enter your monthly income:"))
Monthly_Expense = float(input("Enter your total monthly expenses:"))
Monthly_Savings = Monthly_Income - Monthly_Expense
print(f"Your monthly savings are: {Monthly_Savings}")

Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: {Projected_Savings}")

