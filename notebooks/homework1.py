# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:37:49 2017

@author: juan
"""

import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    
def exponencial(x):        
    serie = 0
    for i in range(750):
        serie += ((x)**i / factorial(i))
        #print(str(i) +"  "+ str(serie))
    return serie

def prueba(y):
    return abs(math.exp(y) - exponencial(y))

for i in range(-50, 50):
    print(str(i) + ": " + str(prueba(i)))