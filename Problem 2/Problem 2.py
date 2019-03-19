# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:28:13 2019

@author: Diah Hevyka M
"""

n = input ("")
n = int(n)

sum = 2
result = 0
prev = 1
next = 2

while(sum<4000000):
    if (sum % 2 == 0):
        result += sum
    sum = prev + next
    prev = next
    next = sum

print(result)