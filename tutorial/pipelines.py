# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class TutorialPipeline(object):
    def open_spider(self,spider):
        self.cn = sqlite3.connect('i4_sqlite')
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        print(spider.name)
        insert_sql = 'insert into '
        return item
