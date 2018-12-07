# -*- coding: utf-8 -*-
import scrapy

import json
class DazhongSpider(scrapy.Spider):
    name = 'dianpin'
    # allowed_domains = ["httpbin.ort/get"]
    start_urls = ['http://www.dianping.com/']
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
        'Cookie':'cy=2; cye=beijing; _lxsdk_cuid=16719fe6a17c8-001ee763c7cdde-675d7620-144000-16719fe6a18c8; _lxsdk=16719fe6a17c8-001ee763c7cdde-675d7620-144000-16719fe6a18c8; _hc.v=f74c7c18-d2ca-7339-794d-1f8a8263727b.1542329363; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=1677be106e0-57f-56a-b25%7C%7C193'
    }
    def parse(self, response):
        g_id =response.xpath('//*[@class="nc-items"]/a/@data-cat-id').extract()
        r_id=response.xpath('//*[@class="nc-items Hide"]/a/@data-cat-id').extract()
        print(g_id,r_id)
        # global keyword
        # keyword = 'taobao'
        # url = 'https://xin.baidu.com/s/l?q=taobao&t=0&p=1'

    def parse1(self, response):
        date=json.loads(response.text).get('data').get('resultList')
        for i in date:
            p_id=i.get('pid')
            title=i.get('titleName')
            validityFrom=i.get('validityFrom')
            legalPerson=i.get('legalPerson')
            d_url='https://xin.baidu.com/detail/compinfo?pid='+p_id
            yield scrapy.Request(d_url,self.parse2)
    def parse2(self, response):
        biao=response.xpath('//*[@class="zx-detail-tab"]/li/@data-type').extract()
        for i in biao:
            print(i)
            url='https://xin.baidu.com/detail/{}?pid=xlTM-TogKuTwwE*ugFaA174RM-M95D6oWwmd&tot=xlTM-TogKuTw4lx*FVCRZtVfgz-LmIUaawmd&_=1543894922254'.format(i)
