import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'}

def start_work(url):
    html = get_page(url)
    parse_page(html)

def get_page(url):
    resp = requests.get(url,headers = headers)
    resp.encoding = 'gbk'
    html = resp.text
    return html

def parse_page(html):
    soup = BeautifulSoup(html,'html.parser')
    data1 = soup.find('div',attrs={'id':"info"})
    data2 = data1.find_all('p')[0].get_text().strip()
    # print(data2)
    f1.write(data2+'\n')
    data3 = data1.find_all('p')[3].get_text().strip()
    # print(data3)
    f1.write(data3 + '\n')
    data4 = soup.find_all('dd')
    chapter_counter = 0
    for item in data4:
        chapter_counter+=1
        chapter_name = item.find('a').get_text().strip()
        f1.write(chapter_name + '\t')
        # print(chapter_name)
        if chapter_counter<=30:
            chapter_url = 'http://www.biquge.com.tw' + item.find('a').get('href')
            html = get_page(chapter_url)
            content = parse_detail_page(html)
            f2.write(content+'\n\n')

def parse_detail_page(html):
    soup = BeautifulSoup(html,'html.parser')
    text = soup.find('div',attrs={'id':'content'}).get_text().strip()
    return text

if __name__ == '__main__':
    f1 = open('./novel_infor.txt','w',encoding='utf-8')
    f2 = open('./novel_30.txt','a',encoding='utf-8')
    url = 'http://www.biquge.com.tw/2_2016/'
    start_work(url)
    f1.close()
    f2.close()