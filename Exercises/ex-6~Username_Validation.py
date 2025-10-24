# Validate User input exercise
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Username cannot be more than 12 characters.
# Username must not contain spaces.
# Username must not contain any digits.

username = input("Enter your username: ")

def validateUsername(username):
    if len(username) > 12:
        return "Username cannot be more than 12 characters."
    elif username.find(" ") != -1:
        return "No spaces"
    elif not username.isalpha():
        return "No digits."
    else:
        return f"Nice name you got there {username}"

print(validateUsername(username))