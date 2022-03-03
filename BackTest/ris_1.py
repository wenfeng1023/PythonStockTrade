from cProfile import label
from operator import index
from turtle import down
import pandas_datareader as pdr
import matplotlib.pylab as plt
import pandas as pd
import datetime as dt
import numpy as np
from pyparsing import lineStart

def get_stock(name, start=None, end=None):
    data = pdr.get_data_yahoo(name,start, end)
    return data

def ris_c(close,period):
    clChange = close-close.shift(1)
    clChange = clChange.dropna()
    upPrc = pd.Series(0,index=clChange.index)
    #对应相应时间位置放入数据
    upPrc[clChange>0] = clChange[clChange>0]

    downPrc = pd.Series(0,index=clChange.index)
    downPrc[clChange<0] = -clChange[clChange<0]
    rsidata = pd.concat([close,clChange,upPrc,downPrc],axis=1)
    rsidata.columns=['Close','PrcChange','upPrc','downPrc']
    rsidata = rsidata.dropna()

    up = rsidata['upPrc'].rolling(period).mean()
    down = rsidata['downPrc'].rolling(period).mean()
    ris = 100*(up/(up+down)) 
    return ris

def rsi(data, period):
    data['difPrc']= data['Close'].diff(1)
    data['upPrc'] = data.loc[data['difPrc']>0,['difPrc']]
    data['downPrc'] = -data.loc[data['difPrc']<0,['difPrc']]
    data=data.fillna(0)
    
    up = data['upPrc'].rolling(period).mean()
    down = data['downPrc'].rolling(period).mean()
    ris = 100*(up/(up+down)) 
    
    return ris 



if __name__=="__main__":
    name ="TQQQ"
    start = dt.datetime(2020,1,1)
    end = dt.datetime(2021,12,31)
    data = get_stock(name, start, end)
    # ris1 = ris_c(data['Close'],5)
    rsi6 = rsi(data,6)
    rsi24 =rsi(data,24)
    # print(ris1.head(10))
    plt.plot(rsi6,label='Rsi6')
    plt.plot(rsi24,label='Rsi24',color='red',linestyle='dashed')
    plt.title('RIS Gold and Death')
    plt.ylim(-10,110)
    plt.legend()
    plt.show()