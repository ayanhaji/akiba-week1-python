# Task 4: Temperature Station

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("\nTemperature Conversion")
print(f"Celsius: {celsius:g}°C")
print(f"Fahrenheit: {fahrenheit:g}°F")

# Bonus: Fahrenheit to Celsius
fahrenheit_input = float(
    input("\nEnter temperature in Fahrenheit: ")
)

celsius_result = (fahrenheit_input - 32) * 5 / 9

print(f"Celsius: {celsius_result:.2f}°C")