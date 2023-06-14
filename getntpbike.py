# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:31:22 2023

@author: USER
"""

import db
import json
import requests
url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'
data = requests.get(url).text
bike = json.loads(data)
for item in bike:
    station = item['sna']
    sql = "select * from ntpbike where station = '{}'".format(station)
    db.cur.execute(sql) #執行sql
    row = db.cur.fetchone() #one all 都可以，因為迴圈一次一筆 法一
    #count = db.cur.rowcount() 法二 算資料中筆數有多少筆
    if row is None: #沒有資料新增
        sql = "insert into ntpbike(station,tot,rent,space,area,address,lat,lng) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(item['sna'],item['tot'],item['sbi'],item['bemp'],item['sarea'],item['ar'],item['lat'],item['lng'])
        db.cur.execute(sql)
        db.conn.commit()
    else: #有資料update
        sql = "update ntpbike set rent = '{}',space = '{}' where station = '{}'".format(item['sbi'],item['bemp'],item['sna']) #where重要
        db.cur.execute(sql)
        db.conn.commit()
db.conn.close()
        
    