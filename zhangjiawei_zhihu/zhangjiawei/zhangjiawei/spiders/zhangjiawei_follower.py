# -*- coding: utf-8 -*-
import scrapy
import json
import time
from zhangjiawei.items import ZhangjiaweiItem
from zhangjiawei.settings import COOKIE


class ZhangjiaweiFollowerSpider(scrapy.Spider):
    name = 'zhangjiawei_follower'
    allowed_domains = ['zhihu.com']
    baseURL = "https://www.zhihu.com/api/v4/members/zhang-jia-wei/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset="
    offset = 1227760
    start_urls = [baseURL + str(offset) + "&limit=20"]
    cookie = COOKIE

    def start_requests(self):
        yield scrapy.Request(self.baseURL + str(self.offset) + "&limit=20", cookies = self.cookie,callback = self.parse)

    def parse(self, response):
        data_list = json.loads(response.body.decode("utf-8"))['data']
        if len(data_list) == 0:
            return

        for data in data_list:
            global item
            item  = ZhangjiaweiItem()
            if data['follower_count'] > 100:
                item['name'] = data['name']
                item['follower_count'] = data['follower_count']
                item['headline'] = data['headline']
                item['gender'] = data['gender']
                item['answer_count'] = data['answer_count']
                item['articles_count'] = data['articles_count']
                item['url_token'] = data['url_token']
                yield item
            else:
                pass
        self.offset += 20
        time.sleep(1)
        yield scrapy.Request(self.baseURL + str(self.offset) + "&limit=20", cookies = self.cookie,callback = self.parse)