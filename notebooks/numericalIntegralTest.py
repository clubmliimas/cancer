#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 19:50:58 2017

@author: juan
"""

u =  1
l = -1

import hw2_numericalIntegral as nI
import math

def f(x):
    return 1 / (math.sqrt(1 - (x * x)))

#integral = 0.2702097501352921


#for i in range(2, 11):
#    malla = grid(l, u, i)
#    print(malla)
#    evaluationPoints = evaluationPoint(malla, 0)
#    print(evaluationPoints)
#    print(evaluateFunction(evaluationPoints, f))
i = 100000
#print("primer ejemplo")
print(str(1 / i))
#print(str(nI.rectangleRule(f, l, u, i)))
print(str(nI.midpointRule(f, l, u, i)))
#print(str(nI.trapezoidalRule(f, l, u, i)))
#print(abs(integral - nI.rectangleRule(f, l, u, i)) / abs(integral - nI.trapezoidalRule(f, l, u, i)))
#print()
#
#print(abs(integral - nI.rectangleRule(f, l, u, i)))
#print(abs(integral - nI.midpointRule(f, l, u, i)))
#print(abs(integral - nI.trapezoidalRule(f, l, u, i)))