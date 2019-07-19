import bs4
import re
import requests

response = requests.get('https://geekbrains.ru/')

# a) используя регулярные выражения (библиотеку re)
pattern = re.compile(r'<span class="total-users">(.*?)<\/span>')
resA = pattern.findall(response.text)[0]

# b) используя библиотеку BeautifulSoup
soup = bs4.BeautifulSoup(response.text, 'html.parser')
span = soup.find('span', {'class': 'total-users'})
resB = span.text

if(resA == resB):
    print('Значения одинаковые')
else:
    print('Значения разные')

pattern = re.compile(r'\D+')

count = pattern.sub('', resA)
print(f'Значение варианта A: {count}')

count = pattern.sub('', resB)
print(f'Значение варианта B: {count}')