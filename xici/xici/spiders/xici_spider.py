# -*- coding: utf-8 -*-
import scrapy

from xici.items import XiciItem


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    urls = {'http://www.xicidaili.com/nn/',}

    def start_requests(self):
        reqs = []
        for i in range(1,100):
            req = scrapy.Request('http://www.xicidaili.com/nn/%s'%i)
            reqs.append(req)
        return reqs

    def parse(self, response):
        item = XiciItem()
        item['IP'] = response.xpath('//*[@id="ip_list"]/tbody/tr/td[2]').extract()
        item['POST'] = response.xpath('//*[@id="ip_list"]/tbody/tr/td[3]').extract()
        item['POSITION'] = response.xpath('//*[@id="ip_list"]/tbody/tr/td[4]').extract()
        item['TYPE'] = response.xpath('//*[@id="ip_list"]/tbody/tr/td[6]').extract()
        item['SPEED'] = response.xpath('//*[@id="ip_list"]/tbody/tr/td[7]').extract()
        item['LAST_CHECK_TIME'] = response.xpath('//*[@id="ip_list"]/tbody/tr/td[8]').extract()
        yield item
