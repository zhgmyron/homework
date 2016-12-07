# -*- coding: UTF-8 -*-

import pymongo


def conn():
    client=pymongo.MongoClient('localhost',27017)
    db = client['58city']
    return db
