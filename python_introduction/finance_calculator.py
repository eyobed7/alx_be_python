monthly_income = float(input("Enter your monthly income:"))
monthly_expense = float(input("Enter your total monthly expenses:"))
monthly_Savings=float( monthly_income) - float(monthly_expense)
print("Your monthly savings are $",float( monthly_income) - float(monthly_expense))
print("Projected savings after one year, with interest, is:$", float(monthly_Savings * 12 + (monthly_Savings * 12 * 0.05)))

