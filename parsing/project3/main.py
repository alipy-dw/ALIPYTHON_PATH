from bs4 import BeautifulSoup as bs
import requests

url = 'https://brandshop.ru/dickies/'

header = {
    "Accept" : "*/*",
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36" 
}

response = requests.get(url, headers=header)
src = response.text

with open('') as file:
    ...