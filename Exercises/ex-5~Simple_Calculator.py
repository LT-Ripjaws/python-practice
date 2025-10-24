# Python calculator.
import os
os.system('cls' if os.name == 'nt' else 'clear')

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def operation(operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "You did not enter a valid operator."
    return result

print(f"Result: {operation(operator)}")