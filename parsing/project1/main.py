from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://just-eat.by/kaktus-gomel/piccy'
response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
pizza_title = soup.find('div', class_="prds-list").find_all('div', class_="title")
pizza_desc = soup.find_all('div', class_="desc")
pizza_price = soup.find_all('div', class_="price")
pizza_text = []
for name, desc, price in list(zip(pizza_title, pizza_desc, pizza_price)):
    pizza_text.append({
        "TITLE":name.text,
        "DESC":desc.text,
        "PRICE":price.text
    })
with open("/home/hello/Рабочий стол/practice/parsing/project1/eat.json", 'w') as file:
    json.dump(pizza_text, file, ensure_ascii=False, indent=4 )

print(pizza_title[1].text)
print(pizza_desc[1].text)

description_header = soup.find('div', class_="brd shop-sale").find_parents()
print(description_header)