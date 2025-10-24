# Exercise - 4: This exercise focuses on if statements
import os
os.system('cls' if os.name == 'nt' else 'clear')

def isEligible(age):
    message = ""
    if age >= 70:
        message = "You are too old"
    elif 18<= age < 70:
        message = "Congratulations you are eligible"
    elif age <= 0:
        message = "Are you sure you've been born yet?"
    else:
        message = "You are too young to be eligible"
    return message

age = int(input("How old are you?: "))
print(f"Checking eligiblity......Oh wow! {isEligible(age)}")