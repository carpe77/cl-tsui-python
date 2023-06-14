# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:12:42 2023

@author: chih kang tsui
"""

import random
bet = []
while True:
    bet.append(int(input('請輸入號碼:')))
    if len(bet)==6:
        break
print(bet)
num = []
while True:
    num.append(random.randint(1,49))
    if len(num)==6:
        break
print(num)


