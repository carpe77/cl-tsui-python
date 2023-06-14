# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:26:54 2023

@author: USER
"""
#條件查詢
import sqlite3
conn = sqlite3.connect('demo.db')
#sql = "select * from students where sex = 'F' and age >20 and age < 25" #條件查詢用where
sql = "select * from students where sex = 'F' and age between 20 and 25"#between:介於(都含等號)
#between 只能用在整數、日期
#注意有沒有重複單引號
cursor = conn.cursor() 
cursor.execute(sql)
res = cursor.fetchall()

for row in res:
    print(row[1])
    print(row[3])
    print(row[4])
    print()

conn.commit()
conn.close()
