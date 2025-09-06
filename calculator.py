# Simple Calculator Program

# Ask user for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Results ---")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# Division with zero check
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Division by zero is not possible!")