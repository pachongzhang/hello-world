# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    house_infor = scrapy.Field()
    positionInfo = scrapy.Field()
    followInfo = scrapy.Field()
    subwayInfo = scrapy.Field()
    taxInfo = scrapy.Field()
    haskeyInfo = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice = scrapy.Field()
    pass
