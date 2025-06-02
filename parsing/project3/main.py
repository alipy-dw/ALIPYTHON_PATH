from bs4 import BeautifulSoup as bs
import requests
import json

# url = 'https://brandshop.ru/brandlist/'

# header = {
#     "Accept" : '*/*',
#     "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36" 
# }

# response = requests.get(url, headers=header)
# src = response.text

# # with open('index.html', 'w') as file:
# #     file.write(src)

# soup = bs(src, 'lxml')
# all_product = soup.find_all('a', class_="link link_black")

# all_categories_dict = {}
# for i in all_product:
#     item_text = i.text
#     item_link = 'https://brandshop.ru' + i.get('href')
#     # print(f'Название - {item_text}, Ссылка - {item_link}')
#     all_categories_dict[item_text] = item_link

# with open ('categories.json', 'w') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open ('categories.json') as file:
    all_categories = json.load(file)

print(all_categories)