# Exercise 2: Shopping Cart program
import os
os.system('cls' if os.name == 'nt' else 'clear')

item = input("What is the item ordered?: ")
price = float(input("Enter price of the item: "))
quantity = int(input("Enter amount of items (how many): "))
total = price * quantity

print(f"You have ordered {quantity}x {item}, and the total amount to pay is ${total}")



