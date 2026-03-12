#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:32:21 2020

@author: yuchangnan
"""


import numpy as np
import matplotlib.pylab as plt

def function_2(x):
    return x[0]**2 + x[1]**2

def numerical_gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)
        
        x[idx]= tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2)/(2 * h)
        x[idx] = tmp_val
        
    return grad
    

print("x_0**2 + x_1**2 の（３、4)の勾配 " + str(numerical_gradient(function_2, np.array([3.0,4.0]))))

print("x_0**2 + x_1**2 の（0、2)の勾配 " + str(numerical_gradient(function_2, np.array([0.0,2.0]))))

print("x_0**2 + x_1**2 の（3、0)の勾配 " + str(numerical_gradient(function_2, np.array([3.0,0.0]))))

print("x_0**2 + x_1**2 の（0、0)の勾配 " + str(numerical_gradient(function_2, np.array([0.0,0.0]))))

