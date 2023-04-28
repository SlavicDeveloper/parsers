# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestParserItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    salary_check_min = scrapy.Field()
    salary_check_max = scrapy.Field()