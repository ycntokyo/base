#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:49:16 2020

@author: yuchangnan
"""


import numpy as np

x = 5        # 初期値（ランダム）
lr = 0.01    # 学習率(learning rate))
gradient = 0 # 勾配（傾き）

for i in range(500):
    
    # 傾きの取得 (y=x^2 を事前に微分して y = 2x にしてある)
    gradient = 2 * x
    
    # ほぼ水平になったら処理を抜けます
    if np.abs(gradient) < 0.1:
        break
    
    # 変数を更新（学習）します
    x = x + lr * gradient * -1 # 傾きとは反対に増減させるため、-1 を掛けています
    
    # 途中経過の出力
    print("{:04}: 傾き={:6.3f}  移動量={:5.3f}  x={:5.3f}".format(
          i,
          round(gradient,3), 
          round(lr * gradient * -1,3), 
          round(x,3)))