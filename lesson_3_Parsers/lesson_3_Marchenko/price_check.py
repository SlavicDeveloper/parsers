import sqlite3

conn = sqlite3.connect('products.db') 
c = conn.cursor()

try:
    question = float(input("Введите число, относительно которого будут выведены большие цены: "))
except ValueError:
    print("Вы ввели не число, остановка программы")
    exit()

c.execute(f"SELECT * FROM products WHERE price > {question} ")
records = c.fetchall()

for row in records:
    print("Name: ", row[0])
    print("Price: ", row[1])
