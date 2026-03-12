#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:23:21 2020

@author: yuchangnan
"""


import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader
import sklearn
import sklearn.linear_model
import sklearn.model_selection

# データウェアハウス
df_nvda = pandas_datareader.data.DataReader("NVDA","yahoo","2014-11-01")
#df_aapl = pandas_datareader.data.DataReader("AAPL","yahoo","2014-11-01")
#df_fb = pandas_datareader.data.DataReader("FB","yahoo","2014-11-01")
#df_gold = pandas_datareader.data.DataReader("GLD","yahoo","2014-11-01")


#終値のチャートを可視化
#df_nvda["Close"].plot(figsize=(16,5),color="green")
#df_fb["Close"].plot(figsize=(16,5),color="blue")
#df_gold["Close"].plot(figsize=(16,5),color="orange")
 
# figを保存
#plt.savefig("chart_001.png")
#plt.show()


# 統計処理
 
# 過去14日単純移動平均のcolumnを作成する
df_nvda["SMA"] = df_nvda["Close"].rolling(window=14).mean()
 
#終値と過去14日単純移動平均を比較したグラフを作成する
#df_nvda["Close"].plot(figsize=(15,6), color="red")
#df_nvda["SMA"].plot(figsize=(15,6), color="green")
#plt.show()
 
# 過去14日単純移動平均が追加されたデータフレームを確認
#df_nvda

# 始値に対する当日の変動率 % のcolumnを新規追加
#Ídf_nvda["change"] = ((df_nvda["Close"]-df_nvda["Open"])/df_nvda["Open"])*100
#df_aapl["change"] = ((df_aapl["Close"]-df_aapl["Open"])/df_aapl["Open"])*100
#df_fb["change"] = ((df_fb["Close"]-df_fb["Open"])/df_fb["Open"])*100
#df_gold["change"] = ((df_gold["Close"]-df_gold["Open"])/df_gold["Open"])*100
 
# 直近１００日間の変動率 %　を可視化 
#df_nvda["change"].tail(100).plot(figsize=(15,6), color="green")
#df_aapl["change"].tail(100).plot(figsize=(15,6), color="red")
#df_fb["change"].tail(100) .plot(figsize=(15,6), color="blue")
#df_gold["change"].tail(100) .plot(figsize=(15,6), color="gold")
 
# 保存
#plt.savefig("chart_variable.png")
#plt.show()



# 機械学習
df_nvda["label"] = df_nvda["Close"].shift(-30) #30日間過去にずらした。
df_nvda.tail(35)
#print(df_nvda.info())




# 入力データを作成する
# labelとSMA列は除外して　High Low Open Close Volume AdjClose change の計７列を使用する
X = np.array(df_nvda.drop(["label","SMA"],axis=1))
X.shape # (1172, 7)
 
# 入力データはスケーリングする（平均を引いて標準偏差で割る）
X = sklearn.preprocessing.scale(X) 
 
# ３０日前から現在までのデータを予測に使用する入力データとして定義
predict_data = X[ -30 : ]
predict_data.shape # (30, 7)
 
# 直近３０日間を除外した入力データ
X = X[ : -30]
X.shape #(1142, 7)

# 正解データを定義 :30日後の終値のこと
y = np.array(df_nvda["label"])
y.shape #(1172,)
 
 
# 正解データのない部分を削除
y = y[ : -30]
y.shape #(1142,)

# あるとこのエラーValueError: view limit minimum -36880.6 is less than 1 and is an invalid Matplotlib date value. This often happens if you pass a non-datetime value to an axis that has datetime units
#plt.plot(y)

# データを訓練用と検証用に分割する
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.2)
 
# 学習モデルを定義する（インスタンスの作成）
lr = sklearn.linear_model.LinearRegression()
 
# 学習する（fitメソド実行）
lr.fit(X_train, y_train)
 
#検証する
accuracy = lr.score(X_test, y_test)
accuracy # 0.9232607206984768

# 過去３０日間の入力データ predict_data から、
# それぞれ３０日後の未来終値データ predicted_dataを予測する
predicted_data=lr.predict(predict_data)
predicted_data.shape # (30,)
predicted_data

# 予測済みデータをデータフレームに追加するため、
# 予め、空データを入れておく
df_nvda["Predicted"] = np.nan
 
# 最終日indexを取得する
last_date = df_nvda.iloc[-1].name # Timestamp('2019-09-27 03:00:00')
 
# 1日の数値を定義（決まっている）
one_day = 86400
 
# 最終日に１日足す
next_unix = last_date.timestamp() + one_day

 
# 予測済みデータ
for data in predicted_data:
    
    # 日付を定義
    next_date=datetime.datetime.fromtimestamp(next_unix)
    
    # 1日カウントアップ
    next_unix += one_day
    
    # index（未来の日付）に予測終値を追加していく
    df_nvda.loc[next_date] = np.append([np.nan]*(len(df_nvda.columns)-1),data)

#print(df_nvda.info())
#できない 
#df_nvda.Date = pd.to_datetime(df_nvda.datetime)
#df_nvda.set_index('Date', inplace=ßTrue)

# 可視化：終値と予測終値
df_nvda["Close"].plot(figsize=(16,5),color="green")
df_nvda["Predicted"].plot(figsize=(16,5),color="orange")
 
# fig 保存
plt.savefig("predict_result.png")
plt.show()
 
#last_date　＃　ßTimestamp('2019-06-28 00:00:00')