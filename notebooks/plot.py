#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:11:25 2017

@author: juan
"""

#This program plots data

import numpy as np
import matplotlib.pyplot as plt

x_data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y_data = (1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1)

y_alternative = (2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2)

fig = plt.subplot()
fig.scatter(x_data, y_data)
fig.scatter(x_data, y_alternative)
plt.show()
