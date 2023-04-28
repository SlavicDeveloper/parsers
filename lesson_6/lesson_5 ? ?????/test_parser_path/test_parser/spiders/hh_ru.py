import scrapy
from scrapy.http import HtmlResponse
from test_parser.items import TestParserItem


class HhRuSpider(scrapy.Spider): 
    name = "hh_ru"
    allowed_domains = ["hh.ru"]
    start_urls = [
        "https://hh.ru/search/vacancy?text=python&salary=&area=2019&ored_clusters=true&page=0&items_on_page=20"
                  ]

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        href = response.xpath("//a[@class='serp-item__title']/@href").getall()
        for el in href:
            yield response.follow(el, callback=self.parse_vacansy)


    def parse_vacansy(self, response:HtmlResponse):
        title = response.css("h1::text").get()
        job_href = response.url
        prefix = response.xpath("//span[@data-qa='vacancy-salary-compensation-type-net']/text()[1]").get()
        min_salary = response.xpath("//span[@data-qa='vacancy-salary-compensation-type-net']/text()[2]").get()
        max_salary = response.xpath("//span[@data-qa='vacancy-salary-compensation-type-net']/text()[6]").get()
        print("?????????", prefix)
        if max_salary == "руб.":
            max_salary = "No info"

        if prefix == "до ":
            max_salary = min_salary
            min_salary = "No info"

        yield TestParserItem(
            name = title, 
            href = job_href,      
            salary_check_min = min_salary,
            salary_check_max = max_salary,   
       )
        
        

        
        
       

