# Some dictionary practice
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Create an empty dictionary called dog
dog = {}
print(type(dog))

# Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Jonathon'
dog['color'] = 'White'
dog['breed'] = 'Dalmatian'
dog['legs'] = 'Four'
dog['age'] = '5 y/o'

print(dog)
print(dog.get('breed'))
print(dog.keys())
print(dog.values())

for keys, values in dog.items():
    print(f"{keys} : {values}")

if dog.get('city'):
    print("yep")
else:
    print("nope")

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {'first_name' : 'Drakiel',
           'last_name' : 'Droners',
           'gender' : 'Male',
           'age' : 35,
           'martial status' : 'Married',
           'skills' : ['Fighting monsters', 'Playing', 'Cooking', 'Adventure'],
           'country' : 'The Sunken Atlantis',
           'address' : 'Secret'}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
skills = student.get('skills')
print(type(skills))

# Modify the skills values by adding one or two skills
student['skills'].append('AND EVERYTHING ELSE')

for keys, values in student.items():
    print(f"{keys}: {values}")

for skills in student.get('skills'):
    if 'Cooking' in skills:
        print("Found it")
        index = student['skills'].index('Cooking')
        student['skills'].insert(index,'Flying')
        break

for keys, values in student.items():
    print(f"{keys}: {values}")   


# Concession Stand Program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("------ MENU ------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------")

while True:
    food = input("Select an item from the menu (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) != None:
        cart.append(food)
    else:
        print("This food is not on the menu")

print("***** YOUR ORDER ******")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print("\n***** RECEIPT ******")
print(f"Your total is: ${total:.2f}")

# Another way of making dictionaries
line_style = dict(marker="*", markersize=10, markerfacecolor="blue", markeredgecolor="blue",
               linestyle='dashed', linewidth=2, color="red")
print(line_style)