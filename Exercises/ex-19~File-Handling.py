import os
os.system('cls' if os.name == 'nt' else 'clear')

# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words

def countLineAndWords(filename):
    if os.path.exists(f'./data/{filename}.txt'):
        with open(f'./data/{filename}.txt') as file:
            lines = file.readlines()
            words = 0
            for line in lines:
                words += len(line.split(" "))
            print(f"Number of lines: {len(lines)}")
            print(f"Number of words: {words}")
    else:
        print("File does not exist")

print("Obama's Speech: ")
countLineAndWords('obama_speech')
print("\nMichelle Obama's Speech: ")
countLineAndWords('michelle_obama_speech')
print("\nDonald Trump's Speech")
countLineAndWords('donald_speech')
print("\nMelina Trump's Speech")
countLineAndWords('melina_trump_speech')

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
from collections import Counter
def most_spoken_languages(filename,length=2000):
    if os.path.exists(f'./data/{filename}.json'):
        with open(f'./data/{filename}.json', encoding='utf-8') as file:
            countries_list = json.load(file)
            
            all_languages = []
            for country in countries_list:
                all_languages.extend(country['languages'])
            lang_count = Counter(all_languages)
            if(length):
                print(lang_count.most_common(length))
            else:
                print(lang_count)
    else:
        print("File does not exist")

most_spoken_languages('countries_data',10)

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(filename,length=2000):
    if os.path.exists(f'./data/{filename}.json'):
        with open(f'./data/{filename}.json', encoding='utf-8') as file:
            countries_list = json.load(file)
            
            population = []
            for country in countries_list:
                population.append({'country':country['name'],'population':country['population']})

            sorted_population = sorted(population, key=lambda x: x['population'], reverse=True)
            
            top_countries = sorted_population[:length]
            print(top_countries)
    else:
        print("damn no files")

most_populated_countries('countries_data',10)

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
# import re
# def extract_email(filename):
#     if os.path.exists(f'./data/{filename}'):
#         with open(f'./data/{filename}',encoding='utf-8') as file:
#             lines = file.readlines()
#             emails = []
#             for line in lines:
#                 found_emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
#                 if found_emails:
#                     emails.extend(found_emails)
#             unique_emails = list(set(emails))
#             print(unique_emails)
#             print(f"\nTotal unique emails found: {len(unique_emails)}")
# extract_email('email_exchanges_big.txt')

# Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
import re
def find_most_frequent_words(filename,length=None):
    if os.path.exists(f'./data/{filename}'):
        with open(f'./data/{filename}', encoding='utf-8') as file:
            str = file.read()
            clean_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', str)
            clean_string = clean_string.replace('\n', ' ')
            words = clean_string.split()
            word_count = Counter(words)
            if(length):
                print(word_count.most_common(length))
            else:
                print(word_count)
    else:
        print("no existo fileo")

find_most_frequent_words('obama_speech.txt',10)

# Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# clean the text(clean_text), remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). 
# List of stop words are given below

from difflib import SequenceMatcher

stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 
              'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', 
              "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 
              'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 
              'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 
              'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 
              'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
              'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 
              'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
              "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', 
              "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 
              'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def similarity_checker(filename1,filename2):
    if os.path.exists(f'./data/{filename1}') and os.path.exists(f'./data/{filename2}'):
        with open(f'./data/{filename1}', encoding='utf-8') as file1, \
             open(f'./data/{filename2}', encoding='utf-8') as file2: 
            
            str1 = file1.read().lower()
            str2 = file2.read().lower()

            clean_string1 = re.sub(r'[^a-z\s]', ' ', str1)
            clean_string1 = clean_string1.replace('\n', ' ')

            clean_string2 = re.sub(r'[^a-z\s]', ' ', str2)
            clean_string2 = clean_string2.replace('\n', ' ') 

            words1 = clean_string1.split()
            words2 = clean_string2.split()

                                                                            # list comp ex:
                                                                            # names = ['alice', 'bob', 'charlie', 'david']
                                                                            # capitalized = [n.upper() for n in names if n.startswith('c')]
                                                                            # print(capitalized)
            words1 = [word for word in words1 if word not in stop_words]    # list comprehension >> new_list = [expression for item in iterable if condition] expression is what i want to put in the list. So think of it like, for item in items, do this>> but we set the do this before the loop statement.
            words2 = [word for word in words2 if word not in stop_words]
            
            text1 = ' '.join(words1)
            text2 = ' '.join(words2)

            similarity = SequenceMatcher(None, text1, text2).ratio()

            print(f"Similarity between {filename1} and {filename2}: {similarity:.2%}")
    else:
        print('File no existo')

similarity_checker('obama_speech.txt','michelle_obama_speech.txt')

# Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python
# b) Count the number lines containing Java and not JavaScript
import csv
# def read_csv(filename):
#     if os.path.exists(f'./data/{filename}.csv'):
#         with open(f'./data/{filename}.csv') as file:
#             # for i in range(1):
#             #     print(file.readline().strip())
#             csv_reader = csv.reader(file, delimiter=',')
#             for i, row in enumerate(csv_reader):
#                 print(row)
#                 if i == 4:  
#                     break
#                 
#     else:
#         print("file doesnt exist")

# read_csv('hacker_news')

def analyze_hacker_news(filename):
    python_count = 0
    java_count = 0

    if os.path.exists(f'./data/{filename}.csv'):
        with open(f'./data/{filename}.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)  

            for row in reader:
                title = row.get('title', '').lower()  

                # a) Count lines containing 'python'
                if 'python' in title:
                    python_count += 1

                # b) Count lines containing 'java' but NOT 'javascript'
                if 'java' in title and 'javascript' not in title:
                    java_count += 1

        print(f"Lines containing 'Python': {python_count}")
        print(f"Lines containing 'Java' but not 'JavaScript': {java_count}")
    else:
        print("File doesn't exist.")

analyze_hacker_news('hacker_news')