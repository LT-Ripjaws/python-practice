# Shopping Cart Program
import os
os.system('cls' if os.name == 'nt' else 'clear')

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ").lower()
    if food == 'q':
        break
    else:
        try:
            price = float(input(f"Enter the price of {food}: $"))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Invalid price, it must be numeric")
        

print("----- YOUR CART -----")

for food in foods:
    print(food, end=' ')

for price in prices:
    total += price
print(f"\nYour total is: ${total}")