import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from book_to_scrap.items import BookToScrapItem

class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        items = response.xpath("//li[@class = 'col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/h3/a/@href").getall()
        for item in items:
            yield response.follow(item, callback = self.item_parse)

    def item_parse(self, response:HtmlResponse):
        loader = ItemLoader(item=BookToScrapItem(), response=response)
        loader.add_xpath("name", "//h1/text()")
        loader.add_xpath("photo", "//div[@class = 'item active']/img/@src")
        loader.add_value("url", response.url)
        loader.add_xpath("price", "//p[@class='price_color']/text()")

        yield loader.load_item()
        