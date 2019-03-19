# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:14:33 2019

@author: Diah Hevyka M
"""
n = input("Enter number that will calculate the sum of all multiples of 3 or 5 : ")
n = int(n)

jumlah = 0

for i in range(n+1):
    if (i % 3 == 0) or (i % 5 == 0):
        jumlah = jumlah + i

print(jumlah)
