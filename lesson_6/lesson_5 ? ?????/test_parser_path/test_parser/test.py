import requests
from lxml import html

response = requests.get("https://hh.ru/search/vacancy?text=python&salary=&area=2019&ored_clusters=true&page=0&items_on_page=20")

root = html.fromstring(response.content)

salary = root.xpath("//span[@data-qa = 'vacancy-serp__vacancy-compensation']/text()").get()   

for el in salary:
    print(el)