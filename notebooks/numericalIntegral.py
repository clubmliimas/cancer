# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:40:55 2017

@author: juan
"""

def grid(lower, upper, N):
    output = ()
    for i in range(N + 1):
        t = i / N
        output = output + (t * upper + (1 - t) * lower, )
    return output

def evaluationPoint(grid,  t):
    output = ()
    for i in range(len(grid) - 1):
        x = t * grid[i + 1] + (1 - t) * grid[i]
        output += (x, )
    return output

def evaluateFunction(sequence, function):
    output = ()
    for i in range(len(sequence)):
        output = output + (function(sequence[i]), )
    return output

def rectangleRule(function, lowerLimit, upperLimit, N):
    h = (upperLimit - lowerLimit) / N
    malla = grid(lowerLimit, upperLimit, N)
    evaluationPoints = evaluationPoint(malla, 0)
    functionValues = evaluateFunction(evaluationPoints, function)
    output = 0.0
    for i in range(len(functionValues)):
        output += h * functionValues[i]
    return output

def midpointRule(function, lowerLimit, upperLimit, N):
    h = (upperLimit - lowerLimit) / N
    malla = grid(lowerLimit, upperLimit, N)
    evaluationPoints = evaluationPoint(malla, 1/2)
    functionValues = evaluateFunction(evaluationPoints, function)
    output = 0.0
    for i in range(len(functionValues)):
        output += h * functionValues[i]
    return output

def trapezoidalRule(function, lowerLimit, upperLimit, N):
    h = (upperLimit - lowerLimit) / N
    malla = grid(lowerLimit, upperLimit, N)
    functionValues = evaluateFunction(malla, function)
    output = 0.0
    for i in range(len(functionValues) - 1):
        output += h / 2 * (functionValues[i] + functionValues[i + 1])
    return output