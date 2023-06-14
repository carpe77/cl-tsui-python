# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:21:42 2023

@author: USER
"""

num = []
while len(num)<6: #len:串列元素個數
    n = int(input('請輸入數字:'))
    if num.count(n) == 0:
        num.append(n)
    else:
        print(n,'數字重複')
#氣泡排序法
leng = len(num)
for i in range(leng-1):  #最後的會固定  len=6
    for j in range(leng-i-1): #倒數第二個會固定 len=5再來4再來3,2,1
        if num[j]<num[j+1]: #大排到小所以前面比後面小的時候要交換順序
            num[j],num[j+1] = num[j+1],num[j] #只有python可以這樣寫(其他要用temp)
print(num)
            
    
    