# -*- coding: utf-8 -*-
import scrapy
import json
import time
from zjwfollower.items import ZjwfollowerItem
from zjwfollower.settings import COOKIE


class ZhangjiaweiFollowerSpider(scrapy.Spider):
    name = 'followerdetail'
    allowed_domains = ['zhihu.com']
    baseURL = "?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_force_renamed%2Cis_bind_sina%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"
    with open ('D:\\python\\code\\zhangjiawei_zhihu\\zjwfollower\\zjwfollower\\data\\url_token4.txt', 'r') as f:
        follower_urls = f.readlines()
    url_count = 0
    follower_url = follower_urls[url_count]
    start_urls = ["https://www.zhihu.com/api/v4/members/"+follower_url + baseURL]
    cookie = COOKIE
    #print(follower_urls)

    def start_requests(self):
        yield scrapy.Request("https://www.zhihu.com/api/v4/members/"+ self.follower_url + self.baseURL, cookies = self.cookie,callback = self.parse)

    def parse(self, response):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+ str(response.status))
        if response.status == 200:
            #加载网页json数据            
            data_list = json.loads(response.body.decode("utf-8"))
            item = ZjwfollowerItem()
            #获取名字
            item['name'] = data_list['name']
            #获取位置
            if data_list['locations']:
                item['locations'] = ((data_list['locations'])[0])['name']
            #获取行业
            if 'business' in data_list:
                item['business'] = (data_list['business'])['name']
            else:
                item['business'] = '' 
            #获取职业经历
            if data_list['employments']:
                if 'company' in (data_list['employments'])[0]:      
                    item['employments_company'] = (((data_list['employments'])[0])['company'])['name']
                else:
                    item['employments_company'] = ''
                if 'job' in (data_list['employments'])[0]:
                    item['employments_job'] = (((data_list['employments'])[0])['job'])['name']
                else:
                    item['employments_job'] = ''
            else:
                item['employments_company'] = ''
                item['employments_job'] = ''
            #获取教育经历
            if 'educations' in data_list: 
                if data_list['educations']:
                    if 'school' in (data_list['educations'])[0]:
                        item['educations_school'] = (((data_list['educations'])[0])['school'])['name']
                    else:
                        item['educations_school'] = ''
                    if 'major' in (data_list['educations'])[0]:
                        item['educations_major'] = (((data_list['educations'])[0])['major'])['name']
                    else:
                        item['educations_major'] = ''               
                else:
                    item['educations_school'] = ''
                    item['educations_major'] = ''
            else:
                item['educations_school'] = ''
                item['educations_major'] = ''

            if data_list['badge']:
                badgelen = len(data_list['badge'])
                item['identity'] = ''
                #item['best_answerer'] = ''
                #获取认证信息
                for i in range(0, badgelen-1):
                    if ((data_list['badge'])[i])['type'] == "identity":
                        item['identity'] =  ((data_list['badge'])[i])['description']
                #获取最佳回答者信息
                '''for i in range(0, badgelen-1):
                    if 'topics' in (data_list['badge'])[i]:
                        topics_len = len(((data_list['badge'])[i])['topics'])
                        for j in range(0, topics_len-1):
                            item['best_answerer'] = item['best_answerer'] + ((((data_list['badge'])[i])['topics'])[j])['name']'''
            #获取个人简介
            item['description'] = data_list['description']
            #获取知乎收录回答数
            item['marked_answers_count'] = data_list['marked_answers_count']
            #获取感谢数
            item['thanked_count'] = data_list['thanked_count']
            #获取点赞数
            item['voteup_count'] = data_list['voteup_count']
            #获取收藏数
            item['favorite_count'] = data_list['favorited_count']
            yield item
            self.url_count += 1
            if self.url_count % 10 == 0:
                time.sleep(1)
            if self.url_count < len(self.follower_urls):
                follower_url = self.follower_urls[self.url_count]
                print("--------------------------------------------"+follower_url+"--------------------")
                yield scrapy.Request("https://www.zhihu.com/api/v4/members/"+ follower_url + self.baseURL, cookies = self.cookie, callback = self.parse)
            else:
                return
        elif response.status == 404:
            print("==============================================================")
            item = ZjwfollowerItem()
            item['name'] = "网址异常"
            item['locations'] = "网址异常"
            yield item
            self.url_count += 1
            if self.url_count % 10 == 0:
                time.sleep(1)
            if self.url_count < len(self.follower_urls):
                follower_url = self.follower_urls[self.url_count]
                print("--------------------------------------------"+follower_url+"--------------------")
                yield scrapy.Request("https://www.zhihu.com/api/v4/members/"+ follower_url + self.baseURL, cookies = self.cookie, callback = self.parse)
            else:
                return
