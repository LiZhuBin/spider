# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class I4Item(scrapy.Item):
    title = scrapy.Field()  # 标题
    content = scrapy.Field()  # 内容

