#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 19:51:47 2017

@author: juan
"""

import hw2_numericalDerivative as nD

u = 2
l = -1

def g(x):
    return x / (1 + x ** 4)

    
N = 10000
x = 0
dif_x_1 = nD.forwardDifference(g, x, l, u, N)
dif_x_2 = nD.centeredDifference(g, x, l, u, N)
print(dif_x_1)
print(dif_x_2)