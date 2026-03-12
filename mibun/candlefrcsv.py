#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:42:37 2020

@author: yuchangnan
"""




import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web
import mpl_finance as mpf
from matplotlib.dates import date2num


import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.finance as mpf
 
book = pd.read_csv("/Users/yuchangnan/Desktop/acodona/mibun/SH600002.csv")
#book = book.loc[500:550] #任意の50データを抜き取り
 
date = book["date"].values
open = book["open"].values
high = book["high"].values
low = book["low"].values
close = book["close"].values
 
df = pd.DataFrame({'始値':open, '終値':close, '高値':high, '安値':low}, index = date)
 
plt.figure(figsize=(8, 6))
ax = plt.subplot()
mpf.candlestick2_ohlc(ax, df['始値'], df['高値'], df['安値'], df['終値'], width=0.5, colorup="g", colordown="r")
ax.grid()
ax.legend()
ax.set_xlim(date[0],date[5])  # x軸の範囲
#fig.autofmt_xdate()  # x軸のオートフォーマット
#fig.autofmt_xdate() #x軸のオートフォーマット
 
plt.show()