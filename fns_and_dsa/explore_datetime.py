import datetime

# Get the current date and time
current_date = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", current_date)

# Get the number of days to add from the user
number_of_days = int(input('Enter the number of days to add to the current date: '))

# Calculate the timedelta
delta = datetime.timedelta(days=number_of_days)

def calculate_future_date():
    # Calculate the future date
    future_date = current_date + delta

    # Format the day and month to ensure two digits
    formatted_day = f"{future_date.day:02}"
    formatted_month = f"{future_date.month:02}"

    # Print the future date
    print(f"Future date: {future_date.year}-{formatted_month}-{formatted_day}")

calculate_future_date()

