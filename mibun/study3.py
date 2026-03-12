#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:58:55 2020

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

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    
    for idx in range(step_num):
        
        grad = numerical_gradient(f, x)
        
        x -=lr * grad
        
    return x
    

init_x = np.array([3.0,4.0])

print("勾配降下法結果 " + str(gradient_descent(function_2, init_x = init_x, lr = 0.1, step_num=100)))

