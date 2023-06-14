# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:10:42 2023

@author: USER
"""
#try finally
def divresult(num1,num2):
    try:
        result = num1//num2
        print('結果:',result)
    finally: #不管有沒有錯誤一定要執行
        print('計算完畢')
divresult(10,5)
print()
divresult(10,0)
print('程式執行完畢') #沒有處理，有錯誤所以不會執行這行(和try05相比)