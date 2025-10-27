# Exercise - 4: This exercise focuses on if-else statements and match case
import os
os.system('cls' if os.name == 'nt' else 'clear')

# def isEligible(age):
#     message = ""
#     if age >= 70:
#         message = "You are too old"
#     elif 18<= age < 70:
#         message = "Congratulations you are eligible"
#     elif age <= 0:
#         message = "Are you sure you've been born yet?"
#     else:
#         message = "You are too young to be eligible"
#     return message

# age = int(input("How old are you?: "))
# print(f"Checking eligiblity......Oh wow! {isEligible(age)}")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

# my_age = 25

# def check_age(your_age, my_age):
#     if your_age < 1 or your_age > 105:
#         print("fam you invalid or smth?")
#     elif your_age > my_age:
#         if your_age == my_age + 1:
#             print(f"You are 1 year older")
#         else:   
#             difference = your_age - my_age
#             print(f"You are {difference} years older")
#     elif your_age < my_age:
#         if your_age == my_age - 1:
#             print("I am 1 year older")
#         else:
#             difference = my_age - your_age
#             print(f"I am {difference} years older.")
#     elif my_age == your_age:
#         print("Damn we same fam")

# try:
#     your_age = int(input("Enter your age: "))
#     check_age(your_age,my_age)
# except Exception as e:
#     print(e)

# Write a code which gives grade to students according to theirs scores: 
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
# def grades(marks):
#     if 80 <= marks <= 100:
#         print('Congratulations you got A')
#     elif 70 <= marks < 80:
#         print("Congratulations you got B! Try harder next time!")
#     elif 60 <= marks < 70:
#         print("Its okay you can do better")
#     elif 50 <= marks <= 60:
#         print("This is worrying, you really need to start focusing")
#     else:
#         print("oh god you are stupid af or you entered an invalid number")

# try:
#     marks = int(input("Enter your marks: "))
#     grades(marks)
# except Exception as e:
#     print(e)

# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

# def season_checker(month):
#     match month:
#         case 'january' | 'february' | 'december':
#             print("The Season is Winter!")
#         case 'march' | 'april' | 'may':
#             print("The Season is Spring!")
#         case 'june' | 'july' | 'august':
#             print("The Season is Summer!")
#         case 'september' | 'october' | 'november':
#             print("The Season is Autumn!")
#         case _:
#             print('Invalid month, please try again')
            

# month = input("Enter a month to check it's season!: ").lower()
# season_checker(month)


# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# * If the person is married and if he lives in a country, print the information
person = {
    'first_name': 'Chinmoy',
    'last_name': 'Guha',
    'age': 3000,
    'country': 'Autralia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

if person.get('skills') != None:
    print(f"The middle skill is {person['skills'][int((len(person['skills'])/2))]}")
else:
    print("No skillz")

if person.get('is_married') == True and person.get('country') != None:
    print(f"Person lives in {person.get('country')} and he is married")
elif person.get('is_married') == False and person.get('country') != None:
    print(f"Person lives in {person.get('country')} and he is not married")
else:
    print("he homeless")
    