# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class BookToScrapPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (name, photo, url, price REAL)")
    def process_item(self, item, spider):
        self.cur.execute(f"INSERT INTO books(name, photo, url, price) VALUES (?, ?, ?, ?)", (item["name"][0], item["photo"][0], item["url"][0], item["price"][0]))
        self.conn.commit()
        return item
