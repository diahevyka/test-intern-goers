# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:24:54 2019

@author: Diah Hevyka M
"""
#600851475143
n = input("Enter the number to be searched for the biggest prime factor: ")
n = int(n)

i=2
while i < n:
    if (n % i == 0):
        n = n / i
    else:
        if i > 2:
            i += 2 
        else:
            i += 1
print(n)
