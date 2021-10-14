import scrapy


class DmozSpiderSpider(scrapy.Spider):
    name = 'dmoz_spider'
    allowed_domains = ['ru.wikinews.org/wiki/Main_Page']
    start_urls = ['http://ru.wikinews.org/wiki/Main_Page/']

    def parse(self, response):
        pass
