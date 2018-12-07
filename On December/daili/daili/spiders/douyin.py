# -*- coding: utf-8 -*-
import scrapy
import re
import json
import requests
class DouyinSpider(scrapy.Spider):
    name = 'douyin'
    # allowed_domains = ["httpbin.ort/get"]
    # start_urls = ['https://aweme.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&user_id=104805227292&count=20&retry_type=no_retry&iid=52978067746&device_id=60121858174&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=251&version_name=2.5.1&device_platform=android&ssmix=a&device_type=SM-G955F&device_brand=samsung&language=zh&os_api=19&os_version=4.4.2&uuid=355757010120216&openudid=1202b50d03ef6296&manifest_version_code=251&resolution=720*1280&dpi=240&update_version_code=2512&_rticket=1543902939819&ts=1543902938&as=a10531203a2d4c96264355&cp=1adbc757a76b0460e1okwo&mas=011a4ef116dc7a29a0acab7cae48ef117facaccc2c6c4c6c9cc62c']
    headers = {'User-Agent': 'okhttp/3.10.0.1'}
    headersa = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

    def start_requests(self):
        start_urls = 'https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=0&user_id=59875777753&count=20&retry_type=no_retry&iid=52978067746&device_id=60121858174&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=251&version_name=2.5.1&device_platform=android&ssmix=a&device_type=SM-G955F&device_brand=samsung&language=zh&os_api=19&os_version=4.4.2&uuid=355757010120216&openudid=1202b50d03ef6296&manifest_version_code=251&resolution=1280*720&dpi=240&update_version_code=2512&_rticket=1543922308518&ts=1543922307&as=a12596c0b3383cb2d64355&cp=6d83c35a39660622e1ukco&mas=019d4550cf5abaeb2cd37320ac517a9062acaccc2c6c264c46c6cc'
        yield scrapy.Request(start_urls,self.parse,headers=self.headers)
    def parse(self, response):
        print(response.text)
        data=json.loads(response.text).get('aweme_list')
        print(data)
        for i in data:
            # print(i)
            url=i.get('share_url')
            yield scrapy.Request(url,self.parse1,headers=self.headers)
    def parse1(self, response):
        d_url=re.findall(' playAddr: "(.*?)",',response.text,re.S)[0]
        name=response.xpath('//*[@class="desc"]/text()').extract_first()

        request=requests.get(d_url,headers=self.headersa).content
        with open('./daili'+name+'.mp4','wb+')as f:
            f.write(request)
            f.flush()
