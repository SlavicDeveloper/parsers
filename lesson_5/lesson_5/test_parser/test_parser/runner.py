from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from spiders.hh_ru import HhRuSpider

if __name__ == "__main__":
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(HhRuSpider)

    reactor.run()