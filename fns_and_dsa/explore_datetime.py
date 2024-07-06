from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print("Current date and time:", formatted_current_date)
    
    # Get the number of days to add from the user
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    
    # Calculate the timedelta
    delta = timedelta(days=number_of_days)
    
    def calculate_future_date():
        # Calculate the future date
        future_date = current_date + delta
        
        # Format the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
        
        # Print the future date
        print("Future date:", formatted_future_date)

    calculate_future_date()

# Call the function to display the current date and time
display_current_datetime()


