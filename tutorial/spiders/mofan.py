# -*- coding: utf-8 -*-
import scrapy


class MofanSpider(scrapy.Spider):
    name = "mofan"
    allowed_domains = ["'https://morvanzhou.github.io/'"]
    start_urls = ['http://'https://morvanzhou.github.io/'/']

    def parse(self, response):
        pass
