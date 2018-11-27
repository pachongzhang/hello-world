# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql

class LianjiaPipeline(object):
    def __init__(self):
        self.MG_Client = pymongo.MongoClient('localhost')['lianjia']['infor']
        self.conn=pymysql.connect(
            host='localhost',
            user='root',
            password='1111',
            db='lian',
            charset='utf8'
        )
        self.cur=self.conn.cursor()
    def process_item(self, item, spider):
        self.MG_Client.insert(dict(item))
        # items['title'] = title
        # items['house_infor'] = house_infor
        # items['positionInfo'] = positionInfo
        # items['followInfo'] = followInfo
        # items['subwayInfo'] = subwayInfo
        # items['taxInfo'] = taxInfo
        # items['haskeyInfo'] = haskeyInfo
        # items['totalPrice'] = totalPrice
        # items['unitPrice'] = unitPrice
        sql='insert into lian(title,house_infor,positionInfo,followInfo,subwayInfo,taxInfo,haskeyInfo,totalPrice,unitPrice) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        ite=(item['title'],item['house_infor'],item['positionInfo'],item['followInfo'],item['subwayInfo'],item['taxInfo'],item['haskeyInfo'],item['totalPrice'],item['unitPrice'])
        self.cur.execute(sql,ite)
        self.conn.commit()

        return item
