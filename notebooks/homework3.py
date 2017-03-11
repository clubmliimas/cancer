#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:11:25 2017

@author: juan
"""

#This program plots data

import naturalCubicSpline as spline
import matplotlib.pyplot as plt
import numericalIntegral as nI


l = 0
u = 10
interpolationPoints = u * 25

sample =         (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
functionSample = (1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, )


def g(x):
    return spline.naturalCubicSpline(x, sample, functionSample)

interpolation = nI.grid(l,u, interpolationPoints)
interpolationValues = nI.evaluateFunction(interpolation, g)

fig = plt.subplot()
fig.scatter(interpolation, interpolationValues, alpha = 0.1)
fig.scatter(sample, functionSample, color = "r")
plt.show()
