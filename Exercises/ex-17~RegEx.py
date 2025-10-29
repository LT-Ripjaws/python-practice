import os
os.system('cls' if os.name == 'nt' else 'clear')
import re

#re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
#re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
#re.findall: Returns a list containing all matches
#re.split: Takes a string, splits it at the match points, returns a list
#re.sub: Replaces one or many matches within a string

#Match
txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match) 

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

#Search
# It returns an object with span and match
search = re.search('first', txt, re.I)
print(search)

#Searching for All Matches Using findall
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']


# if no re.I flag then:
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']


# Replacing words with re.sub()
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

# To declare RegEx variable r'' like:
regex = r"hey"

# What is the most frequent word in the following paragraph?
paragraph = '''I love teaching. If you do not love teaching what else can you love.
    I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

words = re.findall(r'\b\w+\b', paragraph)

from collections import Counter

word_counts = Counter(words) #makes a dictionary

sorted_counts = sorted([(count, word) for word, count in word_counts.items()], #we loop thru the dictionary and sort it out in (count,word) format
                       reverse=True)

print(sorted_counts)

sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True) # Here we did a x[1] because we want to sort according to the numbers and thats in the second index like ('love', 6)
print(sorted_counts)

