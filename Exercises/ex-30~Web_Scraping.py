# Web scraping is the automated process of extracting data from websites. 
# It involves programmatically accessing web pages, parsing their HTML or XML content, and then extracting specific information like text, images, links, or tables. 
# Web scraping is used for various purposes, including market research, data analysis, price comparison, and content aggregation. 

# BeautifulSoup is a Python library designed for parsing HTML and XML documents. 
# It provides a convenient way to navigate, search, and modify the parse tree, making it easy to extract data from web pages. 
# BeautifulSoup is particularly well-suited for scraping static content where the HTML is readily available. 
# It often works in conjunction with HTTP request libraries like requests to fetch the web page content.

# Selenium is a powerful tool primarily used for automating web browsers.
#  While it's widely used for testing web applications, it's also a valuable tool for web scraping, especially for dynamic websites that rely heavily on JavaScript to render content. 
# Selenium can interact with browsers (like Chrome or Firefox) to simulate user actions, such as clicking buttons, 
# filling out forms, and scrolling, allowing access to content that might not be present in the initial HTML source.

# curl_cffi is a Python library that provides a CFFI-based wrapper around libcurl, a widely used C library for transferring data with URLs. 
# It offers advanced features for web scraping, including support for TLS fingerprint spoofing (like JA3/TLS), HTTP/2, and asynchronous operations. 
# This makes curl_cffi particularly useful for bypassing anti-scraping measures that rely on detecting automated requests.

#It is also possible to use APIS for web scraping. Check https://www.youtube.com/watch?v=ji8F8ppY8bs
import os
os.system("cls" if os.name == "nt" else "clear")
# os.system('pip install beautifulsoup4 requests') # uncomment and install if needed

import requests
from bs4 import BeautifulSoup

# url = 'https://archive.ics.uci.edu/datasets'

# response = requests.get(url)
# content  = response.text

# soup = BeautifulSoup(content, 'html.parser')

# print(soup.title)
# print(soup.title.get_text())

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content  = response.text
soup = BeautifulSoup(content, 'html.parser')


# soup.find() finds the first occurrence
# soup.find_all() finds all occurrences
# soup.select() finds all occurrences based on CSS selectors
# print(soup.prettify()) # Prints HTML in a readable format.

sections = soup.find_all('section', class_='stat-section')
result = []
for section in sections:
    title_tag = section.find("h4", class_="stat-group-title")
    if title_tag.get_text(strip=True) == "Community":
        ul = section.find("ul", class_="custom-stat-list")
        data = {}
        data["Section"] = title_tag.get_text(strip=True)
        for li in ul.find_all("li"):
            label = li.find("span", class_="stat-label").get_text(strip=True)
            figure = li.find("span", class_="stat-figure").get_text(strip=True)
            data[label] = figure
        result.append(data)

print(result)


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find_all('table')[1]

titles = table.find_all('th')

world_table_titles = [title.get_text(strip=True) for title in titles]

import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')[1:]

for row in column_data:
    row_data = row.find_all('td')
    individual_row = [data.get_text(strip=True) for data in row_data]

    length = len(df)
    df.loc[length] = individual_row

print(df)


#  To fetch url and save to file

# def fetchAndSaveToFile(url, path):
#     response = requests.get(url)
#     with open(path, "w") as file:
#         file.write(response.text)

# fetchAndSaveToFile('https://www.example.com', './data/example.html')

# with oppen('./data/example.html', 'r') as file:
#     content = file.read()
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())

# wE can use proxies and rate limiting to avoid getting blocked while web scraping.