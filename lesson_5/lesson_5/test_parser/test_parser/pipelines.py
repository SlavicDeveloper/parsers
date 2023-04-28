# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class TestParserPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("hh.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS jobs (Title, Href)")

    def process_item(self, item, spider):
        self.cur.execute(f"INSERT INTO jobs(Title, Href) VALUES (?, ?)", (item["name"], item["href"]))
        self.conn.commit()
        return item
        
        
        
       
