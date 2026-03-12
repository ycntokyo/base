#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:07:06 2020

@author: yuchangnan
"""


import numpy as np
import matplotlib.pyplot as plt

def relu(lst):
    lst[lst <= 0] = 0
    return lst
    
# ソフトマックス関数(ndarray版)
def softmax(x):
    # max() と sum() で次元が減り、
    # 元の x と直接計算ができなくなるため、転置（行列の入替）しておきます
    x = x.T
    
    # オーバーフロー対策。最大値が0になり、他はマイナスになる。
    x = x - np.max(x, axis = 0)
    
    # ソフトマックス
    y = np.exp(x) / np.sum(np.exp(x), axis = 0)
    
    return y.T #転置していたので元に戻して返す

# クロスエントロピー誤差の取得
def cross_entropy_error(y, t):
    size = y.shape[0]
    
    loss = 0
    for i in range(size):
        # 値 1 のインデックスを取得します
        idx = t[i].argmax()
        
        # 損失を加算します
        loss = loss + np.log(y[i, idx] + 1e-7)
    
    loss = - loss / size
       
    return loss

# 予測します
# ニューラルネットワークの計算を行い、ソフトマックスで結果を返す
def predict(v1, w1, b1, w2, b2):
    v2 = np.dot(v1, w1) + b1
    v2 = relu(v2)
    
    v3 = np.dot(v2, w2) + b2
    
    return np.argmax(softmax(v3))


def get_weight(v1, w1, b1, w2, b2, t_value):
    data_count = t_value.shape[0]
    
    c = 0
    for i in range(5000):
        
        #--------------------
        #  順方向
        #--------------------
        v2 = np.dot(v1, w1) + b1
        v2_org = v2.copy() #誤差逆伝播で使用
        v2 = relu(v2)
        
        v3 = np.dot(v2, w2) + b2
        
        softmax_result = softmax(v3)

        # 現在の損失率とグラフの表示
        if c % 100 == 0:
            draw_graph(w1, b1, w2, b2)
            print("損失率", cross_entropy_error(softmax_result, t_value))
            c = 0
       
        c = c + 1
        
        #--------------------
        #  誤差逆伝播
        #--------------------
        
        # 「ソフトマックス + クロスエントロピー誤差」が逆伝播する値は「結果 - 正解」になる
        # 学習データ毎の誤差をあとで合算するため、事前に誤差をデータ数で割る
        gosa = (softmax_result - t_value) / data_count
        
        # 重みとバイアスの微分
        dw2 = np.dot(v2.T, gosa)
        db2 = np.sum(gosa, axis = 0)
        
        #誤差に重みをかけて、前の層へ誤差を伝播していきます
        gosa = np.dot(gosa, w2.T)
        
        # ReLU で値が 0 になっていた場合は、誤差を 0 にします
        gosa[v2_org <= 0] = 0
        
        # 重みとバイアスの微分
        dw1 = np.dot(v1.T, gosa)
        db1 = np.sum(gosa, axis = 0)
        
        #誤差に重みをかけて、前の層へ誤差を伝播していきます
        # gosa = np.dot(gosa, w1.T)
       
        #--------------------
        #  重みとバイアスの更新
        #--------------------
        learning_rate = 0.01  # 学習率
        w1 -= dw1 * learning_rate
        w2 -= dw2 * learning_rate
        b1 -= db1 * learning_rate
        b2 -= db2 * learning_rate

    return (w1, b1, w2, b2)


# グラフの描画
def draw_graph(w1, b1, w2, b2):
    plt.grid()            # グリッド表示
    plt.xlim([-1.5, 1.5]) # グラフ描画範囲(X軸)
    plt.ylim([-1.5, 1.5]) # グラフ描画範囲(Y軸)
    
    # グラフ描画
    x_list = np.arange(-1, 1.6, 0.1) # x軸
    y_list = np.arange(-1, 1.6, 0.1) # y軸
    for y in y_list:
        for x in x_list:
            p = predict(np.array([x, y]), w1, b1, w2, b2)
            if p == 1:
                plt.scatter(x, y, c = 'b')
                
    plt.show()
    
    print("{0} {1} {2} {3}".format(
        predict(np.array([0, 0]), w1, b1, w2, b2),
        predict(np.array([0, 1]), w1, b1, w2, b2),
        predict(np.array([1, 0]), w1, b1, w2, b2),
        predict(np.array([1, 1]), w1, b1, w2, b2)))


#--------------------
#  メイン
#--------------------

# 重みとバイアス
w1 = np.random.randn( 2, 16) * 0.1
w2 = np.random.randn(16,  2) * 0.1
b1 = np.zeros(16)
b2 = np.zeros(2)

# 入力データ(論理演算の全組み合わせ)
input_value = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])

# 正解データ(one-hot表現)
t_value = np.array([
    [1, 0],
    [0, 1],
    [0, 1],
    [1, 0],
])

# 適切な重みとバイアスの取得
(w1, b1, w2, b2) = get_weight(input_value, w1, b1, w2, b2, t_value)