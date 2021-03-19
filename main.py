from bs4 import BeautifulSoup
import requests

source = requests.get('https://en.wikipedia.org/wiki/Halloween').text
soup = BeautifulSoup(source, 'lxml')
# ..................................................
# DISPLAY TITLE

title = soup.find('h1', class_='firstHeading')
final_title = title.text
print(final_title)

# DISPLAY TABLE

# print(soup.prettify())
square = soup.find('div', class_='toc')
# print(square)
table = square.find('ul')
# print(table)
table_details = table.text

print(table_details)
