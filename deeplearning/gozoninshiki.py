#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:04:00 2020

@author: yuchangnan
"""


from keras.layers import Activation, Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.utils import np_utils
import numpy as np
import cv2

# 学習データ
x = np.array([], np.int8) # 画像データ
y = np.array([], np.int8) # 正解データ

# 環境に合わせて変更してください。
dir_path = "/Users/yuchangnan/Desktop/acodona/deeplearning/"
            # 0       1          2          3
name_list = ['maru', 'sankaku', 'shikaku', 'hoshi'] # 〇 △ □ ☆
for kind, kind_name in enumerate(name_list):
    for n in range(10):
        # 画像データを読み込んで、学習データとして追加します
        path = dir_path + kind_name + "/" + str(n) + ".png"
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) # グレースケールでファイル読み込み（縦 * 横 の2次元）
        x = np.append(x, img)  # 画像を1次元配列として追加
        y = np.append(y, kind)

        # 学習データを増やすため、画像を反転させたデータを学習データとして追加します

        # 上下反転
        img2 = cv2.flip(img, 0)
        x = np.append(x, img2)
        y = np.append(y, kind)

        # 左右反転
        img2 = cv2.flip(img, 1)
        x = np.append(x, img2)
        y = np.append(y, kind)

        # 上下左右反転
        img2 = cv2.flip(img, -1)
        x = np.append(x, img2)
        y = np.append(y, kind)


# 画像データを4次元に変換します
# print(x.shape) # (125440,) = 160 * 28 * 28  (160 = 10(画像数) * 4(種類) * 4(反転))
x = x.reshape(-1, 28, 28, 1)
# print(x.shape) # (160, 28, 28, 1)

# 正解を one-hot 表現に変換
#  0 -> [1 0 0 0]
#  1 -> [0 1 0 0]
#  2 -> [0 0 1 0]
#  3 -> [0 0 0 1]
y = np_utils.to_categorical(y)
# print(y)


# モデルの生成
model = Sequential()

# 畳み込み層
# 入力:(28 * 28, 1枚)
# フィルター:(3 * 3 * 1枚) * 32枚
model.add(Conv2D(filters = 32, kernel_size = (3, 3), strides = (1, 1), padding='same', input_shape = (28, 28, 1)))
model.add(Activation('relu'))
# 出力:(28 * 28, 32枚)

# 畳み込み層
model.add(Conv2D(filters = 32, kernel_size = (3, 3), strides = (1, 1), padding='same'))
model.add(Activation('relu'))
# 出力:(28 * 28, 32枚)

# 畳み込み層
model.add(Conv2D(filters = 32, kernel_size = (3, 3), strides = (1, 1), padding='same'))
model.add(Activation('relu'))
# 出力:(28 * 28, 32枚)

#----------------------------------------

# プーリング層
model.add(MaxPooling2D(pool_size = (2, 2))) # strides のデフォルトは pool_size
# 出力:(14 * 14, 32枚)

# 過学習の抑制（ランダムでニューロンの無効化）
model.add(Dropout(rate = 0.5)) # 50% 無効

#----------------------------------------

# 畳み込み層
# フィルター:(3 * 3 * 32枚) * 64枚
model.add(Conv2D(filters = 64, kernel_size = (3, 3), strides = (1, 1), padding='same'))
model.add(Activation('relu'))
# 出力:(14 * 14, 64枚)

# 畳み込み層
model.add(Conv2D(filters = 64, kernel_size = (3, 3), strides = (1, 1), padding='same'))
model.add(Activation('relu'))
# 出力:(14 * 14, 64枚)

# 畳み込み層
model.add(Conv2D(filters = 64, kernel_size = (3, 3), strides = (1, 1), padding='same'))
model.add(Activation('relu'))
# 出力:(14 * 14, 64枚)

#----------------------------------------

# プーリング層
model.add(MaxPooling2D(pool_size = (2, 2)))
# 出力:(7 * 7, 64枚)

# 過学習の抑制（ランダムでニューロンの無効化）
model.add(Dropout(rate = 0.5))

# 全結合層へ変換
model.add(Flatten())
# 出力:(3136)

# 全結合層
model.add(Dense(4096))
model.add(Activation('relu'))

# 過学習の抑制（ランダムでニューロンの無効化）
model.add(Dropout(rate = 0.5))

# 全結合層
model.add(Dense(4)) # 種類の数だけ用意する
model.add(Activation('softmax'))

# コンパイル
model.compile(
    loss = 'categorical_crossentropy',
    optimizer = 'adam',
    metrics = ['accuracy'])

# 学習
model.fit(x, y, epochs = 30)
# model.load_weights('weights.hdf5') # 学習済みの重みデータの読み込み。読み込む場合は fit() 不要

# 重みの保存
model.save_weights('weights.hdf5') 

# モデルの構造をテキスト出力
model.summary()


# テストデータ
test = np.array([], np.int8)
for n in range(4): # テストデータ４件
    img = cv2.imread(dir_path + "test/" + str(n) + ".png", cv2.IMREAD_GRAYSCALE)
    test = np.append(test, img)

test = test.reshape(-1, 28, 28, 1)

# 予測（分類）
result = np.argmax(model.predict(test), axis = 1)
print(result)