# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import pymongo
import random

client = pymongo.MongoClient('localhost',27017)
pig = client['58city']
customer_info = pig['diannao']

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}
proxy_lists=[
            '1.82.216.134:80',
            '211.153.17.151:80',
            '1.82.216.135'
]
ip=random.choice(proxy_lists)
proxies ={'http':'http://'+ip}

url='http://zhuanzhuan.58.com/detail/798002970415104003z.shtml'
channel_list=[]

web_data=requests.get(url,headers=headers,proxies=proxies)
page=BeautifulSoup(web_data.text,'html.parser')

data={
    'title':page.select('h1.info_titile')[0].text,
    'look_time': page.select('span.look_time')[0].text,
    'price':page.select('div.price_li > span > i')[0].text,
    'place':page.select('div.palce_li > span > i')[0].text
}

print (proxies)