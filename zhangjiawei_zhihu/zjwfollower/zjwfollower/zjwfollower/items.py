# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZjwfollowerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #姓名
    name = scrapy.Field()
    #地址
    locations = scrapy.Field()
    #行业
    business = scrapy.Field()
    #工作公司
    employments_company = scrapy.Field()
    #工作职业
    employments_job = scrapy.Field()
    #学校
    educations_school = scrapy.Field()
    #专业
    educations_major = scrapy.Field()
    #认证信息
    identity = scrapy.Field()
    #优秀回答者
    #best_answerer = scrapy.Field()
    #描述
    description = scrapy.Field()
    #收录回答数
    marked_answers_count = scrapy.Field()
    #感谢数
    thanked_count = scrapy.Field()
    #点赞数
    voteup_count = scrapy.Field()
    #favorited_count
    favorite_count = scrapy.Field()