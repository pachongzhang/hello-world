# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from ..items import LianjiaItem

class LianjiaInforSpider(scrapy.Spider):
    name = "lianjia_infor"
    allowed_domains = ["www.lianjia.com"]
    # start_urls = ['https://bj.lianjia.com/ershoufang/']

    def start_requests(self):
        url_base = 'https://bj.lianjia.com/ershoufang'
        for i in range(1,51):
            url = url_base + '/pg' + str(i) + '/'
            yield scrapy.Request(url,self.parse)

    def parse(self, response):
        # soup = BeautifulSoup(response.text,'lxml')
        # item_list = soup.find_all('li',attrs={'class':"clear LOGCLICKDATA"})
        items = LianjiaItem()
        item_list = response.xpath('//li[@class="clear LOGCLICKDATA"]')
        for item in item_list:

            title = item.xpath('./div/div[1]/a/text()').extract_first()
            # title = item.find('div',attrs={'class':"title"}).find('a').get_text()

            house_infor = ','.join(item.xpath('div/div[2]/div/text()').extract())
            # print(house_infor)
            positionInfo = ','.join(item.xpath('div/div[3]/div/text()|div/div[3]/div/a/text()').extract())
            # print(positionInfo)
            followInfo = ','.join(item.xpath('div/div[4]/text()').extract())
            # print(followInfo)
            subwayInfo = item.xpath('div/div[4]/div[1]/span[@class="subway"]/text()').extract_first()
            # print(subwayInfo)
            taxInfo = item.xpath('div/div[4]/div[1]/span[@class="taxfree"]/text()').extract_first()
            # print(taxInfo)
            haskeyInfo = item.xpath('div/div[4]/div[1]/span[@class="haskey"]/text()').extract_first()
            # print(haskeyInfo)
            totalPrice = item.xpath('div/div[4]/div[2]/div[1]/span/text()').extract_first() + '万'
            # print(totalPrice)
            unitPrice = item.xpath('div/div[4]/div[2]/div[2]/span/text()').extract_first()
            # print(unitPrice)
            items['title'] = title
            items['house_infor'] = house_infor
            items['positionInfo'] = positionInfo
            items['followInfo'] = followInfo
            items['subwayInfo'] = subwayInfo
            items['taxInfo'] = taxInfo
            items['haskeyInfo'] = haskeyInfo
            items['totalPrice'] = totalPrice
            items['unitPrice'] = unitPrice
            yield items