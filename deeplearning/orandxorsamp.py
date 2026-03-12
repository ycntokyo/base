#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:51:24 2020

@author: yuchangnan
"""


import matplotlib.pyplot as plt
import numpy as np

# 活性化関数（出力層用）
def step(x):
    if x > 0:
        return 1
    else:
        return 0

# 活性化関数（中間層用）
def relu(x):
    if x > 0:
        return x
    else:
        return 0

# 予測する
def predict(layer, v1, v2, w1, w2, w3, w4, w5, w6, b1, b2, b3):
    
    # and と or
    if layer == 2:
        # 出力層の計算
        v3 = (v1 * w1) + (v2 * w2) + b1
    
        # 活性化関数の実行
        return step(v3)
    
    # xor
    if layer == 3:
        
        # 中間層の計算
        v3 = (v1 * w1) + (v2 * w3) + b1
        v4 = (v1 * w2) + (v2 * w4) + b2
    
        # 活性化関数の実行
        v3 = relu(v3)
        v4 = relu(v4)
        
        # 出力層の計算
        v5 = (v3 * w5) + (v4 * w6) + b3
        
        # 活性化関数の実行
        return step(v5)

# 重みをランダムで生成して、論理演算が行える重みを探して返します
def get_weight(layer, result_list):
    
    for _ in range(0, 100000): # 見つからない場合、増やす
        
        # 重みをランダムで設定
        w1 = np.random.rand() - 0.5
        w2 = np.random.rand() - 0.5
        w3 = np.random.rand() - 0.5
        w4 = np.random.rand() - 0.5
        w5 = np.random.rand() - 0.5
        w6 = np.random.rand() - 0.5
        
        # バイアス
        b1 = np.random.rand() - 0.5
        b2 = np.random.rand() - 0.5
        b3 = np.random.rand() - 0.5
        
        # 引数用
        param = (w1, w2, w3, w4, w5, w6, b1, b2, b3)
        
        # if predict(layer, 0, 0, w1, w2, w3, w4, w5, w6, b1, b2, b3) == result_list[0] and \
        #                 入力値
        if predict(layer, 0, 0, *param) == result_list[0] and \
           predict(layer, 0, 1, *param) == result_list[1] and \
           predict(layer, 1, 0, *param) == result_list[2] and \
           predict(layer, 1, 1, *param) == result_list[3]:
            return (w1, w2, w3, w4, w5, w6, b1, b2, b3)

    return None #見つからなかった場合

# グラフの描画
def draw_graph(title, layer, w1, w2, w3, w4, w5, w6, b1, b2, b3):
    plt.title(title)  # タイトル
    plt.grid()        # グリッド表示
    plt.xlim([-2, 2]) # グラフ描画範囲(X軸)
    plt.ylim([-2, 2]) # グラフ描画範囲(Y軸)
    
    # グラフ描画
    x_list = np.arange(-2, 2.1, 0.1) # x軸
    y_list = np.arange(-2, 2.1, 0.1) # y軸
    for y in y_list:
        for x in x_list:
            if predict(layer, x, y, w1, w2, w3, w4, w5, w6, b1, b2, b3) == 1:
                plt.scatter(x, y, c = 'b')
                
    plt.show()


layer = 2
result = get_weight(layer, [0, 1, 1, 1])
if result != None:
    draw_graph('OR', layer, *result)

#layer = 2
#result = get_weight(layer, [0, 0, 0, 1])
#if result != None:
#    draw_graph('AND', layer, *result)

# XOR の場合は、3層にしないと見つからない
#layer = 3
#result = get_weight(layer, [0, 1, 1, 0])
#if result != None:
#    draw_graph('XOR', layer, *result)