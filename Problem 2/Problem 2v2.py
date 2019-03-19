# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:53:49 2019

@author: Diah Hevyka M
"""

x = []
def fibo(n):
    a,b,c = 0, 1, 1
    x.append(c)
    while c <= n:
        yield c
        a, b = b, c
        c = a + b
        x.append(c)
        
    x.pop()
    print(x)

def sum_fib_even(n):
    return sum(fib for fib in fibo(n) if fib % 2 == 0)

print(sum_fib_even(4000000))