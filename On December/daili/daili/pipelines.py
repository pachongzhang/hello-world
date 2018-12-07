# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests

class DailiPipeline(object):
    def process_item(self, item, spider):
        n = 1
        for i in item['url']:
            request = requests.get(i, headers={'Host': 'v3-dy.ixigua.com',
                                               'Connection': 'keep-alive',
                                               'Pragma': 'no-cache',
                                               'Cache-Control': 'no-cache',
                                               'Upgrade-Insecure-Requests': '1',
                                               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
                                               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                               'Accept-Encoding': 'gzip, deflate',
                                               'Accept-Language': 'zh-CN,zh;q=0.9'}, verify=False).content
            with open('./daili' + str(1) + '.mp4', 'wb+')as f:
                # print(i)
                #     for data in request:
                f.write(request)
                f.flush()
            n += 1
        return item
