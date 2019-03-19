# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:18:38 2019

@author: Diah Hevyka M
"""

n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                 n = a * b
print(n)
print(a," ", b, " ", x, " ", s)