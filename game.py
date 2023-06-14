# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:12:10 2023

@author: USER
"""

from OO05 import dancer,adviser,swordsman
import random
import time
if __name__ =='__main__':
    print('歡迎來到online三國')
    player = list()
    com = list()
    #玩家角色
    while len(player)<2: #玩家角色數:2
        num = int(input('1.劍士 2.舞者 3.軍師'))
        if 0<num<4: #防呆
            name = input('輸入角色名字:')
            if num == 1:
                player.append(swordsman(name,100,1)) #帶入物件
            elif num == 2:
                player.append(dancer(name,100,1))
            else:
                player.append(adviser(name,100,1))
     #電腦角色
    role = ['關羽','張飛','趙雲','索隆','黃忠','馬超']
    while len(com)<2: #電腦角色數:2
       num = random.randint(1,3)
       name = random.choice(role) #從role中隨機挑一個出來
       if num == 1:
           com.append(swordsman(name,100,1)) #帶入物件
       elif num == 2:
           com.append(dancer(name,100,1))
       else:
           com.append(adviser(name,100,1))
    while len(player)>0 and len(com)>0: #玩家電腦角色都>0才打
        number = random.randint(1,100)
        if number%2 ==0: #看誰攻擊(奇數偶數)
             p = player[random.randint(0,len(player)-1)] #玩家電腦挑選角色
             c = com[random.randint(0,len(com)-1)]
             if isinstance(p,adviser):
                 p.skill()
             else:
                 p.fight() #玩家攻擊
             print('打向',c.getname())
             blood = c.changehp(random.randint(10,20))
             print('剩餘血量:',blood)
             if blood <= 0:
                 com.remove(c) #若血量<=0移除當前角色
        else:
             #電腦攻擊
             p = player[random.randint(0,len(player)-1)] #玩家電腦挑選角色
             c = com[random.randint(0,len(com)-1)]
             c.fight() #電腦攻擊
             print('打向',p.getname())
             blood = p.changehp(random.randint(10,20))
             print('剩餘血量:',blood)
             if blood <= 0:
                 player.remove(p) #若血量<=0移除當前角色
        time.sleep(0.5) #跑一次迴圈停0.5秒
    if len(player) >0:
        print('玩家win')
    else:
        print('電腦win')
             
             
             
    
