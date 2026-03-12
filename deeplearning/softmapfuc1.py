#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:34:04 2020

@author: yuchangnan
"""


import numpy as np

def softmax(lst):
    print(np.max(lst))
    # リストの全要素に対して exp() を実行する
    exp_lst = np.exp(lst - np.max(lst))
    print(exp_lst)
    # RuntimeWarning: invalid value encountered in true_divide
    #exp_lst = np.exp(lst)
    
    # リストの全要素の合計を算出する
    exp_sum = np.sum(exp_lst)
    print(exp_sum)

    # リストの全要素を、上記の合計値で割る
    result_lst = exp_lst / exp_sum
    
    return result_lst


print(np.round(softmax([ 1,  10,   5,20,21,22]), 2)) # [0.   0.99 0.01]
#print(np.round(softmax([-5, -10, -15]), 2)) # [0.99 0.01 0.  ]
#print(np.round(softmax([15,  20,  10]), 2)) # [0.01 0.99 0.  ]
#print(np.round(softmax([-5, -10,  10]), 2)) # [0.   0.   1.  ]

# 一番大きい値のインデックスの取得
print(np.argmax(softmax([10, 20, 30]))) # 2