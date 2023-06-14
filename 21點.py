# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:38:17 2023

@author: USER
"""

import random
cards = list()
for i in range(1,14):  #1-13號
    for y in range(1,5): #每個數字有4個花色  =>52張
        cards.append(i)
def buycards():
    cards = list()
for i in range(1,14):  #1-13號
    for y in range(1,5): #每個數字有4個花色  =>52張
        cards.append(i)
    
#拿牌
def givecards():
    point = cards.pop(0) #發第一張牌
    if point>=10:
        point = 10
    return point
         
#洗牌
def washcard(cards):
    for i in range(200):
        first = random.randint(0,len(cards)-1) #洗52張牌，所以是從0-51 =>len(cards-1)
        end = random.randint(0,len(cards)-1)
        cards[first],cards[end] = cards[end],cards[first] #first,end交換(onlypython) *類氣泡排序法
washcard(cards)
#print(cards)
#因為是串列裡面換位置外面也會換
print('歡迎來到21點')
print('-'*30)
mymoney = 100
while mymoney>0:
    gameP=mymoney
    while True: #確認錢比代幣多
        gameP = int(input('押注代幣:'))
        if gameP>mymoney:
            print('代幣不足目前代幣是:',mymoney)
        else:
            break
    print()
    print('下注代幣為:',gameP)
    NPC = list()
    player = list()    
    NPC.append(givecards())
    print('莊家?點')
    player.append(givecards())
    print('玩家:',player[0],'點') #玩家的第一張牌要翻開(索引值0)
    print('-'*30)
    NPC.append(givecards())
    print('莊家:',NPC[1],'點') #莊家第二張要翻開(索引值1)
    player.append(givecards())
    print('玩家:',player[1],'點')
    print('目前玩家總點數:',sum(player))
    print('-'*30)
    #玩家補牌
    q = 'y' #預設要加牌
    i = 2 #要補排從索引值2開始
    while q == 'y':
        q = input('請問玩家要加牌嗎(y/n)')
        if q != 'y': #不補牌
            break
        player.append(givecards())
        print('玩家:',player[i],'點')
        print('玩家總點數:',sum(player),'點')
        i += 1 #下次補牌從索引值3開始
        if sum(player)>21:
            
            print('玩家爆了')
            break
        if sum(player) == 21:
            break
    #莊家補牌
    print('莊家點數',sum(NPC),'點')
    if sum(player)<21:
        i = 2
        while sum(NPC)<sum(player):
            NPC.append(givecards())
            print('莊家點數:',NPC[i],'點')
            print('莊家總點數:',sum(NPC),'點')
            i+=1
    if sum(player)<21:
        if sum(NPC)>21 or sum(NPC)<sum(player) or sum(player) == 21:
            mymoney+=gameP
            print('莊家輸了')
        elif sum(NPC) == sum(player):
            mymoney-=gameP
            print('莊家贏了')
        elif len(player) == 5:
            mymoney += gameP*2
            print('玩家過五關')
        elif sum(NPC) == 21 or sum(NPC)>sum(player) :
            mymoney-=gameP
            print('莊家贏了')
    elif sum(NPC) == sum(player):
        mymoney-=gameP
        print('莊家贏')
    elif len(NPC)== 5 and sum(NPC)<=21:
        mymoney-=gameP
        print('莊家過五關')
    elif sum(player)>21:
        mymoney-=gameP
        print('莊家贏了')
    print()
    print('-'*30)
    print('目前你剩餘:',mymoney,'元')
    q = input('繼續請按y:')
    if q != 'y':
        break
    if len(cards) == 0:
        buycards()
        
    
    
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    