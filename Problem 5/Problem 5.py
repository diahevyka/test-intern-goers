# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:10:15 2019

@author: Diah Hevyka M
Problem 5
"""
result = False
num = 0
i = 0

while (result == False):
    i+=20
    if(i%11==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18== 0 and i%19==0 and i%20==0):
        result = True

print(i)