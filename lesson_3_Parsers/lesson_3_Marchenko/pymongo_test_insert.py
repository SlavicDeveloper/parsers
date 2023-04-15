import requests
from bs4 import BeautifulSoup as bs
import sqlite3


conn = sqlite3.connect('products.db') 
c = conn.cursor()
data_list = []

try:
    page_number = int(input("Введите номер страницы для парсинга: "))
except ValueError:
    print("Введено не число")
    exit()

c.execute("CREATE TABLE IF NOT EXISTS products (name TEXT NOT NULL, price REAL NOT NULL)")

def append_data(title, price): 
    data_list.append((title, price))



while True:
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{page_number}.html")

    if response.status_code != 404:
        soup = bs(response.content, "html.parser")            
        books = soup.find_all("article")

        for book in books:
            title = book.find("h3").find("a")["title"]
            price = book.select_one("div[class='product_price'] p[class='price_color']").text
            price = float(price[1: ])
            append_data(title, price)
        page_number += 1

    else:
        print("Страница не найдена")
        break

c.executemany("INSERT INTO products VALUES (?, ?)", data_list)

conn.commit()


conn.close()