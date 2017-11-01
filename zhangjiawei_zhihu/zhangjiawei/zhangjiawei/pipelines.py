# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import json

class ZhangjiaweiPipeline(object):
    def __init__(self):
        self.f = open("zhangjiawei.csv", "w", newline='')

    def process_item(self, item, spider):
        dict_item = dict(item)
        fieldnames = ['name', 'follower_count', 'headline', 'gender', 'answer_count', 'articles_count', 'url_token', 'detail']
        writer = csv.DictWriter(self.f, fieldnames = fieldnames)
        #writer.writeheader()
        writer.writerow(dict_item)
        '''content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content.encode("utf-8"))'''
        return item

    def close_spider(self, spider):
        self.f.close()

class Url_token_Pipeline(object):
    def __init__(self):
        self.f = open("follower_url.txt",'w')

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.f.write(dict_item['url_token'])
        self.f.write('\n')
        return item

    def close_spider(self, spider):
        self.f.close()
