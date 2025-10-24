# A menu based calculator.
import os
os.system('cls' if os.name == 'nt' else 'clear')

num1 = ""
num2 = ""
operator = ''

def user_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("invalid input")
    
    operator = input("What would you like to perform (+,-,/,*)?: ")
    return num1,num2,operator

def calculation(operator,num1,num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/' and num2 == 0:
        return "Cannot divide by a 0"
    elif operator == '/':
        return num1 / num2
    elif operator == '*':
        return num1 * num2
    else:
        return ("invalid operation")
    
while True:
    choice = input("Do you want to do calculation? (y/n): ").lower()
    if choice == 'n':
        print("goodbye!")
        break
    elif choice == 'y':
        num1, num2, operator = user_input()  
        print(calculation(operator, num1, num2))
    else:
        print("invalid choice")
