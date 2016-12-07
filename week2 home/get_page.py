# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import random
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}
proxy_lists=[
    '1.82.216.134:80',
    '211.143.146.235:80',
    '111.12.82.4:80'
]
ip=random.choice(proxy_lists)
proies ={'http':'http://'+ip}
product_links=[]


def page_url(url):

    web_data=requests.get(url,headers=headers)
    page=BeautifulSoup(web_data.text,"html.parser")
    datas=page.select('tr.zzinfo > td.t > a.t')
    print (datas)
    for data in datas:

        url=data.get('href').split('?')[0]
        print (url)
        product_links.append(url)

    return product_links
page_url('http://sh.ganji.com/jiaju/o2/')

print (product_links)