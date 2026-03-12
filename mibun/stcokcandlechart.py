#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:20:06 2020

@author: yuchangnan
"""


import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web
import mpl_finance as mpf
from matplotlib.dates import date2num


#株価取得期間の設定
start = datetime.datetime(2017, 11, 1)
end = datetime.datetime(2020, 7, 8)

#株価取得
df = web.DataReader("AMZN", "yahoo", start, end)
#df = df.ix[:, ["Open", "Close","High","Low"]]
df = df.loc[:, ["Open", "Close","High","Low"]]

#画像作成
fig = plt.figure(figsize=(12, 9))
ax = plt.subplot()

xdate = [x.date() for x in df.index]  # 日付
ochl = np.vstack((date2num(xdate), df.values.T)).T

mpf.candlestick_ochl(ax, ochl, width=0.5, colorup="b", colordown="r")

ax.grid()  # グリッド表示
ax.set_xlim(df.index[0].date(), df.index[-1].date())  # x軸の範囲
fig.autofmt_xdate()  # x軸のオートフォーマット

ax.set_title("Amazon.com株")
ax.set_ylabel("Stock　Price")
plt.show()