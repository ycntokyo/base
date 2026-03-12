#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:06:09 2020

@author: yuchangnan
"""


import numpy as np

# ニューラルネットワークの計算
def calc(layer1_val, layer1_w, layer2_w, layer3_w, layer4_w):
    layer2_val = np.dot(layer1_val, layer1_w)
    layer3_val = np.dot(layer2_val, layer2_w)
    layer4_val = np.dot(layer3_val, layer3_w)
    layer5_val = np.dot(layer4_val, layer4_w)
    return layer5_val[0]


# 入力値
layer1_val = np.array([1, 2])

# 重み
w1, w2, w3, w4, w5  =  1, 2, 3, 4, 5
w6 ,w7, w8, w9, w10 =  6, 7, 8, 9,10
w11,w12,w13,w14,w15 = 11,12,13,14,15
w16,w17,w18,w19,w20 = 16,17,18,19,20
w21,w22,w23         = 21,22,23

# レイヤーごとの重み
layer1_w = np.array([[w1, w2, w3],
                     [w4, w5, w6]])

layer2_w = np.array([[w7,  w8,  w9],
                     [w10, w11, w12],
                     [w13, w14, w15]])

layer3_w = np.array([[w16, w17],
                     [w18, w19],
                     [w20, w21]])
    
layer4_w = np.array([[w22],
                     [w23]])

# 計算 1回目
result1 = calc(layer1_val, layer1_w, layer2_w, layer3_w, layer4_w)
print(result1, "1回目の計算結果")

# w1 で微分
a1 = layer1_val[0]
dw1 = w22 * w16 * w7 * a1 + \
      w22 * w18 * w8 * a1 + \
      w22 * w20 * w9 * a1 + \
      w23 * w17 * w7 * a1 + \
      w23 * w19 * w8 * a1 + \
      w23 * w21 * w9 * a1

print(" ", dw1, "w1の微分結果")

# w1 を 1 増加させる
layer1_w[0, 0] += 1

# 計算 2回目
result2 = calc(layer1_val, layer1_w, layer2_w, layer3_w, layer4_w)
print(result2      , "2回目の計算結果(w1増加後)" )
print(result1 + dw1, "1回目の計算結果 + w1の微分結果")