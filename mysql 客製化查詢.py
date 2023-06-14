# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:41:53 2023

@author: USER
"""

import db
try:
    while True:
        name = input('輸入姓名q離開:')
        if name == 'q':
            break
        sql = "select * from students where name = '{}'".format(name)
        
        db.cur.execute(sql)
        data = db.cur.fetchone() 
        
        if data == None: 
            print('找不到')
        else:
            print(list(data))
            print('姓名:',data[1])
            print('年齡:',data[2])
            print('性別:',data[3])
finally: #不管是否出錯都關閉
    db.conn.close()