# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

class ZjwfollowerPipeline(object):
    def __init__(self):
        self.f = open("followerinfo6.csv", "w", newline='')

    def process_item(self, item, spider):
        dict_item = dict(item)
        fieldnames = ['name', 'locations', 'business', 'employments_company', 'employments_job', 'educations_school', 'educations_major', 'identity', 'description', 'marked_answers_count', 'thanked_count', 'voteup_count', 'favorite_count']
        writer = csv.DictWriter(self.f, fieldnames = fieldnames)
        try:
            writer.writerow(dict_item)
        except:
            errinfo = {"name":"写入异常"}
            fieldnames = ['name']
            writer = csv.DictWriter(self.f, fieldnames = fieldnames)
            writer.writerow(errinfo)
        return item
    
    def close_spider(self, spider):
        self.f.close()