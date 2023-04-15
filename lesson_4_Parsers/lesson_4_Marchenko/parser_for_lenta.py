import requests
from lxml import html 
import sqlite3

conn = sqlite3.connect('news.db')
c = conn.cursor()
data_lst = []

counter = 1
c.execute("CREATE TABLE IF NOT EXISTS news (author, text, news_href, publication_date)")

def append_data(author, text, news_href, publication_date): 
    data_lst.append((author, text, news_href, publication_date))

try:
    question = int(input("Введите число страниц, которое необходимо спарсить: "))
except ValueError:
    print('Введено некорректное значение: ')
    exit()

while counter != question:
    response = requests.get(f"https://lenta.ru/parts/news/{counter}").content
    root = html.fromstring(response.decode('utf-8'))
    news = root.xpath("//li[@class='parts-page__item']")

    for el in news:
        text = el.xpath(".//a/h3/text()")
        text.append("No Data")
        author = el.xpath(".//a/div/span/text()")
        author.append("No Data")
        news_href = el.xpath(".//a/@href")
        news_href.append("No Data")
        publication_date = el.xpath(".//a/div/time/text()")
        publication_date.append("No Data")
        append_data(author[0], text[0], news_href[0], publication_date[0])
        
    counter += 1


c.executemany("INSERT INTO news VALUES (?, ?, ?, ?)", data_lst)
conn.commit()
conn.close()