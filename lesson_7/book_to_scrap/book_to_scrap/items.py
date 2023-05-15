# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose

class BookToScrapItem(scrapy.Item):
    name = scrapy.Field()
    photo = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field(
        input_processor = Compose(lambda el: float(el[0][1:]))
    )
