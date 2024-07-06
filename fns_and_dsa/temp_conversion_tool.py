# Define the global conversion factors

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
CELSIUS_TO_FAHRENHEIT_OFFSET = 32

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_OFFSET
    return fahrenheit

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def main():
    user_input = float(input("Enter the temperature to convert: "))
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

