import datetime

# Get the current date and time
current_date = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", current_date)
number_of_days=int(input('Enter the number of days to add to the current date: '))
delta = datetime.timedelta(days=number_of_days)
def calculate_future_date():
    future_date = current_date + delta
    if future_date.day < 10 :
        print(f"Future date: {future_date.year}-0{future_date.month}-0{future_date.day}")
    else:
        print(f"Future date: {future_date.year}-{future_date.month}-{future_date.day}")
calculate_future_date()
