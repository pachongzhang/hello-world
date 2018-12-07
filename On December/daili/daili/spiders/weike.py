
# -*- coding: utf-8 -*-
import scrapy
import re
import json
import execjs
from newspaper import Article
import random
class WeikeSpider(scrapy.Spider):
    name = 'weike'
    # allowed_domains = ["httpbin.ort/get"]
    start_urls = ['https://www.ofweek.com/']
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
        'Cookie':'Hm_lvt_28a416fcfc17063eb9c4f9bb1a1f5cda=1544148301; __utma=57425525.62732120.1544148301.1544148301.1544148301.1; __utmc=57425525; __utmz=57425525.1544148301.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID=F5D563A5187368E96DAA9A54AB19ABCB; __utmt=1; Hm_lpvt_28a416fcfc17063eb9c4f9bb1a1f5cda=1544149486; __utmb=57425525.22.10.1544148301'
    }
    keyword = input('请输入要查询的内容：')
    def start_requests(self):
        global keyword
        for i in range(1,5):
            url ='http://www.ofweek.com/newquery.action?type=1&keywords={}&pagenum={}'.format(self.keyword,i)
            yield scrapy.Request(url,self.parse,headers=self.header)
    def parse(self, response):
        d_url=response.xpath('//*[@class="zixun"]/div/a/@href').extract()
        for next_page in d_url:
            yield scrapy.Request(next_page,self.parse2,headers=self.header)
    def parse2(self, response):
        if response.xpath('//*[@class="tag_left"]/nobr/span/text()'):
            time=''.join(response.xpath('//*[@class="tag_left"]/nobr/span/text()').extract()).strip()
        else:
            time=''
        if response.xpath('//*[@class="tag_left"]/nobr//a/@title|//*[@class="tag_left"]/nobr//span/@title'):
            laiyuang=response.xpath('//*[@class="tag_left"]/nobr//a/@title|//*[@class="tag_left"]/nobr//span/@title').extract_first()
        else:
            laiyuang=''
        if response.xpath('//h1/text()'):
            title=response.xpath('//h1/text()').extract_first()
        else:
            title=''
        if response.xpath('//*[@class="article_con"]//text()'):
            content=''.join(response.xpath('//*[@class="article_con"]//text()').extract()).strip()
        else:
            content=''
        if response.xpath('//*[@class="article_con"]//img/@src'):
            img=response.xpath('//*[@class="article_con"]//img/@src').extract()
        else:
            img=[]
        if response.xpath('//*[@name="Keywords"]/@content'):
            keyword=response.xpath('//*[@name="Keywords"]/@content').extract_first()
        else:
            keyword=''
        if response.xpath('//*[@name="Description"]/@content'):
            daodu=''.join(response.xpath('//*[@name="Description"]/@content').extract()).strip()
        else:
            daodu=''
        print(title,'\n',time,'\n',daodu,'\n',img,'\n',keyword)
    # def show(self, response):
    #     if response.text:
    #         data=json.loads(response.text)
    #         name=response.meta['name']
    #         # if data:
    #         with open(str(random.randint(1,1000))+'.text','w')as f:
    #             f.write(str(data))
