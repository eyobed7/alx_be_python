Monthly_income = int(input("Enter your monthly income:"))
Monthly_expense = int(input("Enter your total monthly expenses:"))
Monthly_Savings = Monthly_income - Monthly_expense
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Your monthly savings are ",Projected_Savings)

