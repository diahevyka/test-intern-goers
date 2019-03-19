# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:18:38 2019

@author: Diah Hevyka M
"""
def Lpalindrome(i,j):    
    x = 0
    for a in range(i, j, -1):
        for b in range(a, j, -1):
            c = a * b
            if c > x:
                s = str(a * b)
                if s == s[::-1]:
                    x = a * b
    return x

n = input("Looking for the largest palindrome number of two n-digit number products. Input n: ")
n = int(n)

if(n==1):
    print(Lpalindrome(9,1))
elif(n==2):
    print(Lpalindrome(99,10))
elif(n==3):
    print(Lpalindrome(999,100))    
elif(n==4):
    print(Lpalindrome(9999,1000))
elif(n==5):
    print(Lpalindrome(99999,10000))
elif(n==6):
    print(Lpalindrome(999999,100000))
elif(n==7):
    print(Lpalindrome(9999999,1000000))
elif(n==8):
    print(Lpalindrome(99999999,10000000))
    

