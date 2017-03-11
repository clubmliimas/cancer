#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:33:50 2017

@author: juan
"""
import numpy as np
import naturalCubicSpline as spline
import numericalIntegral as nI
import matplotlib.pyplot as plt
import math


samplePoints = 40


def f(x):
    return math.exp(-(x ** 2))

sample =  (0,1)
functionSample = (0,1)

derivatives = spline.Derivatives(sample, functionSample)


def g(x):
    return spline.naturalCubicSpline(x, sample, functionSample,derivatives)

b = np.array([[8,1,7], [4,3,9], [5,2,6]])
vecfun = np.vectorize(g)
result = vecfun(b)
print (result)
