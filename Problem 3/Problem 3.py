# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:24:54 2019

@author: Diah Hevyka M
"""
#600851475143
numb = 600851475143
i=2
while i < numb:
    if (numb % i == 0):
        numb = numb / i
    else:
        if i > 2:
            i += 2 
        else:
            i += 1
print(numb)
