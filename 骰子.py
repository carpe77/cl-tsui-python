# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:12:23 2023

@author: chih kang tsui
"""

import random

def roll():
    dice = []
    while len(dice) < 4:
        dice.append(random.randint(1,6))
    return dice

i = 0
j = 0
while i<3 and j<3:
    dice = roll()
    print(dice)
    print('玩家的點數:',sum(dice))
    dice2 = roll()
    print(dice2)
    print('電腦的點數:',sum(dice2))
    if sum(dice) < sum(dice2):
        j += 1
        print('電腦贏的次數:',j)
    elif sum(dice)> sum(dice2):
        i += 1
        print('玩家贏的次數:',i)
    else:
        print('平手')
if i == 3:
    print('玩家獲勝')
else:
    print('電腦獲勝')





        

    
    