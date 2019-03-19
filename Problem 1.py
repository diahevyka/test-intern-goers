# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:14:33 2019

@author: Diah Hevyka M
"""

jumlah = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        jumlah = jumlah + i

print(jumlah)
