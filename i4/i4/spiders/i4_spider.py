import scrapy

from i4.items import I4Item


class MySpider(scrapy.Spider):
    name = "i4"
    allowed_domains = ["www.i4.cn"]  # 设定域名
    start_urls = ["https://www.i4.cn/news_1.html"]  # 填写爬取地址

    def parse(self, response):
        print(response)
        item = I4Item()
        item['title']=response.xpath('//article[@class="ibox"]/div/div/div/a[2]/text()').extract()
        item['content'] =response.xpath('//article[@class="ibox"]/div/div/div/a[3]/text()').extract()
        yield item
