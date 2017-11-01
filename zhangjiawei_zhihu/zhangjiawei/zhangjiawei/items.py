# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhangjiaweiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 关注者名字
    name = scrapy.Field()
    # 关注者粉丝数
    follower_count = scrapy.Field()
    # 关注者签名
    headline = scrapy.Field()
    # 关注者性别
    gender = scrapy.Field()
    # 关注者回答数
    answer_count = scrapy.Field()
    # 关注者文章数
    articles_count = scrapy.Field()
    # 关注者api的url
    url_token = scrapy.Field()
    # 关注者详细信息
    detail = scrapy.Field()