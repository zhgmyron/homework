# -*- coding: UTF-8 -*-

import get_channel
import get_page
import page_info
import conn_mongodb
import pymongo

#update the channellist

# url='http://sh.ganji.com/wu/'
# get_channel.channel(url)
conn=conn_mongodb.conn()
customer_info=conn.channel.find()
for item in customer_info:
    url= item['channel']
    name=item['channel'].split('/')[-2]
    print (name)
    # url=url+
    # get_page.page_url()
