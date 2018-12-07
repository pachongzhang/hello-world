# -*- coding: utf-8 -*-
import scrapy

import json
class QichaSpider(scrapy.Spider):
    name = 'chacha'
    # allowed_domains = ["httpbin.ort/get"]
    start_urls = ['https://www.qichacha.com/']
    header={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
        'cookie':'acw_tc=ca6cface15439941893891001e60b5d964832a06c50494a20d2fd1bbf0; QCCSESSID=tidlc4086k5fobigplu79cf540; UM_distinctid=1677d39ae7b507-0de03fc8a801eb-675d7620-144000-1677d39ae7c726; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1543994192; zg_did=%7B%22did%22%3A%20%221677d39af87639-00ee9fff9884aa-675d7620-144000-1677d39af88821%22%7D; hasShow=1; _uab_collina=154399419393156557103836; saveFpTip=true; CNZZDATA1254842228=1871495589-1543991242-%7C1544007442; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201544007362239%2C%22updated%22%3A%201544009486655%2C%22info%22%3A%201543994191760%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1544009487'
    }
    def start_requests(self):
        sturl='https://www.qichacha.com/search?key=%E5%B0%8F%E7%B1%B3'
        yield scrapy.Request(sturl,self.parse,headers=self.header )
    def parse(self, response):
        # print(response.text)
        list =response.xpath('//*[@class="m_srchList"]//td[2]')
        for i in list:
            name=''.join(i.xpath('a//text()').extract()).strip()
            url='https://www.qichacha.com'+''.join(i.xpath('a//@href').extract()).strip()
            if len(url)>60:
                yield scrapy.Request(url,self.parse1,headers=self.header)
            else:
                pass

    def parse1(self, response):
        # print(response.text)
        gsxinxi=response.xpath('//*[@class="panel b-a base_info"]/table[2]//tr/td//text()').extract()
        time=response.xpath('//*[@class="m-r"]//text()').extract()
        print(time)
        # date=json.loads(response.text).get('data').get('resultList')
        # for i in date:
        #     p_id=i.get('pid')
        #     title=i.get('titleName')
        #     validityFrom=i.get('validityFrom')
        #     legalPerson=i.get('legalPerson')
        #     d_url='https://xin.baidu.com/detail/compinfo?pid='+p_id
        #     yield scrapy.Request(d_url,self.parse2)
    def parse2(self, response):
        biao=response.xpath('//*[@class="zx-detail-tab"]/li/@data-type').extract()
        for i in biao:
            print(i)
            url='https://xin.baidu.com/detail/{}?pid=xlTM-TogKuTwwE*ugFaA174RM-M95D6oWwmd&tot=xlTM-TogKuTw4lx*FVCRZtVfgz-LmIUaawmd&_=1543894922254'.format(i)
