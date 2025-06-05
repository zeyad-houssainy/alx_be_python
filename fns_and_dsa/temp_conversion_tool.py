FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


try:
    temperature = float(temperature)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")


if unit.upper() == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
elif unit.upper() == "F":
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celsius}°C")
