#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pymongo
import random

client=pymongo.MongoClient('localhost',27017)
ganji = client['58city']

customer_info = ganji['channelurl']

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



def channel(url):
    web_data=requests.get(url,headers=headers)
    page=BeautifulSoup(web_data.text,'html.parser')
    datas = page.select('dl.fenlei > dt > a')

    customer_info.drop()
    for data in datas:
        channel_url= 'http://sh.ganji.com'+data.get('href')

        customer_info.insert_one({'channel': channel_url})

