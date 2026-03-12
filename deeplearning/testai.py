import keras
from keras.layers import Dense
from keras.layers import Activation
from keras.utils.vis_utils import plot_model
from keras.utils import np_utils
import numpy as np

# 学習データ:入力
in_data = [
    [0, 0], 
    [1, 0], 
    [0, 1], 
    [1, 1]
]

# 学習データ:正解データ
#out_data = [0, 0, 0, 1] # and
#out_data = [0, 1, 1, 1] # or
out_data = [0, 1, 1, 0] # xor

# エラーが出るので ndarray に変換する。
# エラー：ValueError: Error when checking model input: the list of Numpy arrays that you are passing to your model is not the size the model expected. 
# Expected to see 1 array(s), but instead got the following list of 4 arrays:
in_data  = np.array(in_data)

# 正解データを one-hot 表現への変換
# model.compile() で loss = 'sparse_categorical_crossentropy' を使う場合や、
# binary_crossentropy を使う場合は不要です。
out_data = np_utils.to_categorical(out_data, np.max(out_data) + 1)


# モデルの生成
model = keras.models.Sequential()

# 入力層:ユニット数2 - 中間層:ユニット数16
model.add(Dense(units = 16, input_dim = 2)) # units:次の層（中間層）のユニット数  input_dim:入力数
model.add(Activation('relu')) # 活性化関数(sigmoid, relu, softmax など)

# 出力層
model.add(Dense(2))
model.add(Activation('softmax')) # 活性化関数

# モデルのコンパイル
model.compile(
    loss = 'categorical_crossentropy', # 損失関数：クロスエントロピー誤差
                                       # 最適化アルゴリズム
    # optimizer = 'sgd',               #   SGD(確率的勾配降下法)
    optimizer = 'adam',                #   Adam
    metrics = ['accuracy'])            # モデルの精度の表示

# 出力層のノード数を１つにして、シグモイド関数を使う場合は以下のようにする
# この場合、上記の np_utils.to_categorical() の行をコメントにすること
#
# # 出力層
# model.add(Dense(1))
# model.add(Activation('sigmoid'))
#
# # モデルのコンパイル
# model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])


# モデルの画像出力(graphviz をインストールしていない場合はコメントにする)
#plot_model(model, "model.png", show_shapes = True, show_layer_names = True)

# 学習
model.fit(in_data, out_data, epochs = 1000) # epochs:反復学習させる回数
# model.load_weights('weights.hdf5') # 学習済みの重みデータの読み込み。読み込む場合は fit() 不要

# 予測
# result = model.predict(in_data)       # 出力層の値
result = model.predict_classes(in_data) # 出力層の値を分類に変換した値
print(result)

# 重みの保存
# 今回学習した内容をファイルで保存する
model.save_weights('weights.hdf5')