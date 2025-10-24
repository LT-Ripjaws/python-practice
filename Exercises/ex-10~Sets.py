# Set related exercises
import os
os.system('cls' if os.name == 'nt' else 'clear')

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]

''' Find the length of the set it_companies
    Add 'Twitter' to it_companies
    Insert multiple IT companies at once to the set it_companies
    Remove one of the companies from the set it_companies '''

print(len(it_companies))
it_companies.add("Twitter")

print(it_companies)
print(len(it_companies))

it_companies.update(['Cisco','Canva', 'Sony'])

print(it_companies)
print(len(it_companies))

removed_item = it_companies.pop()
print(removed_item)

it_companies.discard('Facebook')
print(it_companies)

''' Join A and B
    Find A intersection B
    Is A subset of B
    Are A and B disjoint sets
    Join A with B and B with A
    What is the symmetric difference between A and B '''

C = A.union(B)
print(C)

aIntB = A.intersection(B)
print(aIntB)

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.symmetric_difference(B))

''' Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''

age_set = set(age)
print(f"length of list age: {len(age)} and length of set age: {len(age_set)}")
print("List age has a greater length, because set has unique values whereas list has duplicate values.")

str = 'I am a teacher and i love to inspire and teach people'.lower()
str_list = str.split()
str_set = set(str_list)

print(str_set)
print(f"Unique words: {len(str_set)}")