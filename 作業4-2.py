# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:42:07 2023

@author: chih kang tsui
"""

a = int(input('輸入整數'))
b = int(input('輸入整數'))
c = int(input('輸入整數'))
if a==b==c:
    print('正三角形')
elif a==b or a==c or b==c and a+b>c and a+c>b and b+c>a:
    print('等腰三角形')
else:
    print('失敗')