# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapeItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            elem = ScrapeItem()
            elem["text"] = quote.css('span.text::text').extract_first()
            elem["author"] = quote.css('small.author::text').extract_first()
            elem["tags"] = quote.css('div.tags a.tag::text').extract()
            yield elem
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
