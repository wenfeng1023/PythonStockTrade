import pandas_datareader as pdr
import pandas as pd
import matplotlib.pylab as plt
import datetime as dt
import numpy as np
import finplot as fplt



def get_stock(name,start=None,end=None):
    stock = pdr.get_data_yahoo(name,start,end)
    return stock

def candlestick(t, o, h, l, c):
    plt.figure(figsize=(12,4))
    color = ["green" if close_price > open_price else "red" for close_price, open_price in zip(c, o)]
    plt.bar(x=t, height=np.abs(o-c), bottom=np.min((o,c), axis=0), width=0.6, color=color)
    plt.bar(x=t, height=h-l, bottom=l, width=0.1, color=color)




if __name__=="__main__":
    name = "TQQQ"
    start = dt.datetime(2010,1,1)
    end = dt.datetime(2010,12,31)
    data = get_stock(name,start,end)
    data['clop'] = data['Close']-data["Open"]
    # print(data.head())
    
    clop = data['clop']
    clop1 = data['clop'].shift(1) 
    clop2 = data['clop'].shift(2)

    Shape =[0,0,0]

    for i in range(3,len(clop)):
        if all([clop2[i]<0, abs(clop1[i])<0.05, abs(clop[i])>abs(clop2[i]*0.5)]):
            Shape.append(1)
        else:
            Shape.append(0)

    Open= data['Open']
    Topen = data['Open'].shift(1)
    Tclose = data['Close'].shift(1)
    Tclose2 = data['Close'].shift(2)

    Doji =[0,0,0]
    for i in range(3,len(Open)):
        if all([Topen[i]<Open[i],Topen[i]<Tclose2[i],Tclose[i]<Open[i],(Tclose[i]<Tclose2[i])]):
            Doji.append(1)
        else:
            Doji.append(0)

    ret = data['Close']/data['Close'].shift(1)-1
    ret1 = ret.shift(1)
    ret2 = ret.shift(2)
    
    Trend =[0,0,0]
    for i in range(3,len(ret)):
        if all([ret1[i]<0,ret2[i]<0]):
            Trend.append(1)
        else:
            Trend.append(0)

    StarSig = []
    for i in range(len(Trend)):
        if all([Shape[i]==1,Doji[i]==1,Trend[i]==1]):
            StarSig.append(1)
        else:
            StarSig.append(0)
    print(StarSig)

    for i in range(len(StarSig)):
        if StarSig[i]==1:
            print(data.index[i])
    print(type(data))

    # candlestick(
    # data["2010-02":"2010-12"].index,
    # data["2010-02":"2010-12"]["Open"],
    # data["2010-02":"2010-12"]["High"],
    # data["2010-02":"2010-12"]["Low"],
    # data["2010-02":"2010-12"]["Close"]
    # )

    # plt.grid(alpha=0.2)
    # plt.show()
    fplt.candlestick_ochl(data[['Open', 'Close', 'High', 'Low']])
    fplt.show()
    



