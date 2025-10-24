# List related exercises:
import os
import math
os.system('cls' if os.name == 'nt' else 'clear')

# Declare an empty list
lst = []
print(type(lst))

# Declare a list with more than 5 items
lst1 = [1,2,3,4,5,6]
print(lst1)

# Find the length of your list
print(f"length of 2nd list: {len(lst1)}",f"\nlength of 1st list: {len(lst)}")

# Get the first item, the middle item and the last item of the list
print(f"First item: {lst1[0]}",f"\nMiddle item: {lst1[int((0+(len(lst1)-1))/2)]}",f"\nLast item: {lst1[len(lst1)-1]}")

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Michael", 25, 6, "single", "12/AveSt/CAL"]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

# Print the number of companies in the list
print("Number of companies:",len(it_companies))

# Print the list after modifying one of the companies
it_companies[4] = "Cisco"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Samsung")
print(it_companies)

# Insert an IT company in the middle of the companies list
middle = math.floor((len(it_companies)/2))
it_companies.insert(middle,"Canva")
print(it_companies)

# Check if a certain company exists in the it_companies list.
company = "Apple"
if company in it_companies:
    print(f"Exists: {company}")
else:
    print("Doesnt exist")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# middle companies sliced
middle_comp = it_companies[middle]
print(middle_comp)

#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min = min(ages)
max = max(ages)
print(f"min age: {min}\nmax age: {max}")

#Add the min age and the max age again to the list
ages.append(min)
ages.append(max)

print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
median = ages[int((len(ages)-1)/2)]
print(ages)
print(median)

# Find the average age (sum of all items divided by their number )
avg_age = int(sum(ages)/(len(ages)))
print(avg_age)

summ = 0
for age in ages:
    summ += age
    
avg_age = int(summ/len(ages))
print(avg_age)

# Find the range of the ages (max minus min)
range = max - min
print(range)

# 2D list example
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

