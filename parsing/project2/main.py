from bs4 import BeautifulSoup as bs
import requests
import json

URL = "https://24.kg/"

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
date_of_news = soup.find_all(class_="lineDate")
news_time = soup.find_all('div', class_="time")
news_title = soup.find('div', class_="row lineNews").find_all('div', class_="title")
news_list = []
for time, title in  zip(news_time, news_title):
    news_list.append({
        'TIME':time.text,
        "TITLE":title.text
    })
with open('/home/hello/Рабочий стол/practice/parsing/project2/news_data.json', 'w') as file:
    json.dump(news_list, file, ensure_ascii=False, indent=4)

# print(news_title[0].text)

# parent = soup.find('div', class_="one").find_parent()
# print(parent.text)