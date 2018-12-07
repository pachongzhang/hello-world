# -*- coding: utf-8 -*-
import scrapy
import re
import json
import execjs
import random
class BaiduSpider(scrapy.Spider):
    name = 'qixin'
    # allowed_domains = ["httpbin.ort/get"]
    start_urls = ['https://xin.baidu.com/']
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
        'Cookie':'BAIDUID=D6065F0F5D8ACAA391B8483B0CDDDD7B:FG=1; BIDUPSID=D6065F0F5D8ACAA391B8483B0CDDDD7B; PSTM=1533179924; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=1431_21082_18560_26350_27244_27509; PSINO=2; log_guid=da219b6c82bdfe08f34ebc338de3f067; ZX_HISTORY=%5B%7B%22visittime%22%3A%222018-12-04+11%3A02%3A06%22%2C%22pid%22%3A%22xlTM-TogKuTw%2A5jgkFaM6yjJScY%2ASYH%2Apwmd%22%7D%2C%7B%22visittime%22%3A%222018-12-04+11%3A01%3A10%22%2C%22pid%22%3A%22xlTM-TogKuTw4WL1Qk4mc7%2Aw3sdOh6YpQwmd%22%7D%5D; Hm_lvt_baca6fe3dceaf818f5f835b0ae97e4cc=1543892385,1543893928; Hm_lpvt_baca6fe3dceaf818f5f835b0ae97e4cc=1543893971'
    }
    def parse(self, response):
        global keyword
        keyword = 'taobao'
        url = 'https://xin.baidu.com/s/l?q=taobao&t=0&p=0'
        yield scrapy.Request(url,self.parse1)
    def parse1(self, response):
        con=json.loads(response.text).get('data')
        date=con.get('resultList')
        page=con.get('totalPageNum')
        for i in range(1,page):
            next_page='https://xin.baidu.com/s/l?q=taobao&t=0&p='
            yield scrapy.Request(next_page,self.parse)
        for i in date:
            p_id=i.get('pid')
            title=i.get('titleName')
            validityFrom=i.get('validityFrom')
            legalPerson=i.get('legalPerson')
            d_url='https://xin.baidu.com/detail/compinfo?pid='+p_id
            yield scrapy.Request(d_url,self.parse2,meta={'p_id':p_id})
    def parse2(self, response):
        biao=response.xpath('//*[@class="zx-detail-tab"]/li/@data-type').extract()
        p_id=response.meta['p_id']
        jd=re.findall('</script><script>func(.*?)\(function\(\)',response.text,re.S)[0]
        hd=re.findall('\(function\(\)(.*?)\)\(\)',response.text,re.S)[0]
        tk=re.search(".*?\('(.*?)'\).*?\('(.*?)'\).*?\('(.*?)'\).*",hd)
        # print(tk.group(1),tk.group(2))
        tid=re.findall(tk.group(2)+'="(.*?)">',response.text,re.S)[0]
        b_id=re.findall('<span id="'+tk.group(3)+'">(\d+)</span>',response.text,re.S)[0]
        cmd=execjs.compile('func'+jd)
        key=cmd.call('mix',tid,b_id)
        for i in biao:
            if 'R' in i:
                c_id=re.sub('(R\w+)','ajax',i)
                url='https://xin.baidu.com/detail/{}?pid={}&p=1&tot={}'.format(c_id,p_id,key)
                yield scrapy.Request(url,self.show,meta={'name':i})
    def show(self, response):
        if response.text:
            data=json.loads(response.text)
            name=response.meta['name']
            # if data:
            with open(str(random.randint(1,1000))+'.text','w')as f:
                f.write(str(data))

