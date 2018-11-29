import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib import request
import time
import redis

class Download_Music():

    def __init__(self,url):
        self.url = url
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.2.3.4000'}
        self.rd = redis.Redis(db=7)

    # 请求网页
    def get_data(self):
        resp = requests.get(self.url,headers=self.headers).text
        return resp
    # 执行流程
    def run(self):
        html = self.get_data()#通过requests请求获取网页的内容
        IDict = self.parse_data(html)#解析网页的内容，获得歌曲的名称和id，存成一个字典
        pprint(IDict)#打印字典
        self.save_infor(IDict)#把抓取的歌曲的名称和id存成文件
        self.save_to_redis(IDict)
        # self.download_music_arbitary(IDict)#下载这个歌单里面的任意一首歌
        # self.download_music_all(IDict)#下载歌单里面的所有歌曲

    def save_to_redis(self, IDict):
        for k, v in IDict.items():
            self.rd.set(k,v)

    # 下载全部的歌曲
    def download_music_all(self,IDict):
        #遍历字典，获得键和值
        for k,v in IDict.items():
            url = r'http://music.163.com/song/media/outer/url?id=%s.mp3'% k
            # print(url)
            request.urlretrieve(url, r'E:\doc\bawei\pachong3\1604C\网易云音乐\music\%s.mp3' % v)
            time.sleep(0.5)
            print("%s.mp3下载成功！"%v)
        print("下载完毕！")
    #     下载任意一首音乐，手动选择
    def download_music_arbitary(self, IDict):
        while True:
            idstr = input("(输入0结束)请输入要下载歌曲的ID：")
            if int(idstr) == 0:
                print("您已成功退出！")
                break

            print("正在下载音乐内容，请等待！")
            url = r'http://music.163.com/song/media/outer/url?id=%s.mp3'%idstr
            # 通过给定的url，下载该url的内容，存入第二个参数设置的路径下的文件中
            request.urlretrieve(url,r'E:\doc\bawei\pachong3\1604C\网易云音乐\music\%s.mp3'%IDict[idstr])
            time.sleep(0.5)
            print("下载成功！")

    # 存储歌单文件
    def save_infor(self, IDict):
        # 遍历字典
        for k,v in IDict.items():
            with open('./music_list.txt','a',encoding='utf-8') as f:
                f.write(IDict[k] + '\t' + "ID:" + k + '\n')
    # 解析网页，获得歌名和id
    def parse_data(self,html):
        infors_dict={}
        bs = BeautifulSoup(html,'html.parser')
        infor1 = bs.find('ul',attrs={'class':'f-hide'})
        a_list = infor1.find_all('a')
        for item in a_list:
            #把歌曲的id作为键，歌曲的名称作为值，存到一个字典里面
            infors_dict[item.get('href').replace('/song?id=',"")] = item.get_text().strip()

        return infors_dict

if __name__ == '__main__':
    # 设置爬虫爬取的歌单地址
    url = 'https://music.163.com/#/playlist?id=2449161245'
    url_port = url.replace('/#','')#替换成能够爬取到内容的url地址
    DM = Download_Music(url_port)#Download_Music类生成一个对象
    DM.run()#调用对象的run方法