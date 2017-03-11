#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:24:57 2017

@author: juan
"""

# This program numerically derives functions

import hw2_numericalIntegral as ni

def closestInterval(x, grid):
    for i in range(len(grid) - 1):
        if grid[i] <= x and x <= grid[i + 1]:
            return (grid[i], grid[i + 1])
    return 0

def forwardDifference(function, x, lowerLimit, upperLimit, N):
    h = (upperLimit - lowerLimit) / N
    interval = (x, x + h)
    functionValues = ni.evaluateFunction(interval, function)
    return (functionValues[1] - functionValues[0]) / (interval[1] - interval[0]) 

def centeredDifference(function, x, lowerLimit, upperLimit, N):
    malla = ni.grid(lowerLimit, upperLimit, N)
    interval = closestInterval(x, malla)
    functionValues = ni.evaluateFunction(interval, function)
    return (functionValues[1] - functionValues[0]) / (interval[1] - interval[0])
