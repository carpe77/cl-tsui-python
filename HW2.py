# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:03:04 2023

@author: chih kang tsui
"""

data = [80,60,70,90,49,33,89]
data.sort()
print(data)
key = int(input('輸入數字:'))
high = len(data)-1 
low = 0
mid = int((low+high)/2)
if data.index(key) == mid:
    print('找到了')
if data.index(key)>mid:
    newdata = data[mid+1:]
    print(newdata)
    low1 = 0
    high1 = len(newdata)-1
    mid1 = int((low1+high1)/2)
    if newdata.index(key) == mid1:   
        print('找到了')
    if newdata.index(key)>mid1:
        newdata1 = newdata[mid1+1:]
        print(newdata1)
        low2 = 0
        high2 = len(newdata1)-1
        mid2 = int((low2+high2)/2)
        if newdata1.index(key)== mid2:
            print('找到了')
    if newdata.index(key)<mid1:
        newdata1 = newdata[:mid1]
        print(newdata1)
        low2 = 0
        high2 = len(newdata1)-1
        mid2 = int((low2+high2)/2)
        if newdata1.index(key)== mid2:
            print('找到了')
    
if data.index(key) < mid:
    newdata = data[:mid]
    print(newdata)
    low1 = 0
    high1 = len(newdata)-1
    mid1 = int((low1+high1)/2)
    if newdata.index(key) == mid1:   
        print('找到了')
    if newdata.index(key)>mid1:
        newdata1 = newdata[mid1+1:]
        print(newdata1)
        low2 = 0
        high2 = len(newdata1)-1
        mid2 = int((low2+high2)/2)
        if newdata1.index(key)== mid2:
            print('找到了')
    if newdata.index(key)<mid1:
        newdata1 = newdata[:mid1]
        print(newdata1)
        low2 = 0
        high2 = len(newdata1)-1
        mid2 = int((low2+high2)/2)
        if newdata1.index(key)== mid2:
            print('找到了')
    

