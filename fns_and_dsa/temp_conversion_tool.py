# Define the global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def main():
    try:
        user_input = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    user_choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if user_choice == "C":
        # Convert from Celsius to Fahrenheit
        fahrenheit_temp = convert_to_fahrenheit(user_input)
        print(f"{user_input:.2f}°C is {fahrenheit_temp:.2f}°F")
    elif user_choice == "F":
        # Convert from Fahrenheit to Celsius
        celsius_temp = convert_to_celsius(user_input)
        print(f"{user_input:.2f}°F is {celsius_temp:.2f}°C")
    else:
        print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()


