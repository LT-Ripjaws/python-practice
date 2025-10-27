# THis exercise focuses on loops
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Iterate 0 to 10 using for loop
for number in range(0,11):
    print(number, end=' ')

print() #line break

# Iterate 10 to 0 using for loop
for number in reversed(range(11)):
    print(number, end =' ')

print() #line break

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
triangle = '#'
for number in range(7):
    print(triangle)
    triangle += "#"

# Use nested loops to create the following:

for number in range(5):
    for number in range(8):
        print(triangle, end = '')
    print()

# Print the following pattern:

for number in range(11):
    print(f'{number} x {number} = {number * number}')

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.

add = 0
for number in range(101):
    add += number
print(f"Sum of all numbers: {add}") 

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
add_evens = 0
add_odds = 0
for number in range(101):
    if number % 2 == 0:
        add_evens += number
    else:
        add_odds += number

print(f"Sum of all evens: {add_evens} \nSum of all odds: {add_odds}")

