import scrapy
from Mofan.items import MofanItem

class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://morvanzhou.github.io/',
    ]
    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        item = MofanItem()
        item['title']=response.xpath('//*[@id="recent-update"]/li/a/img')
    # item['url']=response.xpath('//*[@id="recent-update"]/li/a/img')
        yield item
# lastly, run this in terminal
# scrapy runspider 5-2-scrapy.py -o res.json