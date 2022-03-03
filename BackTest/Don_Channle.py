import pandas_datareader as pdr
import matplotlib.pylab as plt
import datetime as dt
import numpy as np
import pandas as pd

# get data of stock
def get_stock(name, start=None, end=None):
    data = pdr.get_data_yahoo(name,start, end)
    return data

'''
    the price of Close crosses the upboundDC upwards
    set the buy signal
'''
def upbreak(close, upDC):
    n = min(len(close), len(upDC))
    close = close[-n:]
    upDC = upDC [-n:]
    signal = pd.Series(0,index=close.index)
    for i in range(1, len(close)):
        if all([close[i]>upDC[i],close[i-1]<upDC[i-1]]):
            signal[i] = 1
    return signal

'''
    the price of Close crosses the upboundDC downwards
    set the sell signal
'''

def downbreak(close, downDC):
    n = min(len(close), len(downDC))
    close = close[-n:]
    downDC = downDC [-n:]
    signal = pd.Series(0,index=close.index)
    for i in range(1, len(close)):
        if all([close[i]<downDC[i],close[i-1]>downDC[i-1]]):
            signal[i] = 1
    return signal

'''
    Caculate  Donchian Channel
'''
def don_channel(data, period):
    close = data['Close']
    hight = data['High']
    low = data['Low']

   
    upDC = pd.Series(0.0, index=close.index)
    downDC = pd.Series(0.0,index=close.index)
    midDC = pd.Series(0.0, index=close.index)

    # upDC = hight.rolling(20).max()
    # downDC = low.rolling(20).max()
    # midDC = 0.5*(upDC+downDC)
    # print(upDC)
   
    # calculate the bound highest price during a period
    for i in range(period, len(close)):
        upDC[i] = max(hight[(i-period):i])
        downDC[i] = max(low[(i-period):i])
        midDC[i] = 0.5*(upDC[i]+downDC[i])

    upDC= upDC[period:]
    downDC = downDC[period:]
    midDC = midDC[period:]

    print(upDC)

    # get up signal
    up_signal = upbreak(close, upDC)
    # get down_signal
    down_signal = downbreak(close, downDC)

    # set the strategy 
    # up,signal =1
    # down, signal = -1
    # merge signal
    break_signal = up_signal - down_signal

    #Calculate the win rate for this strategy
    tradeSig = break_signal.shift(1)
    ret = close / close.shift(1) -1
    tradeRet = (ret*tradeSig).dropna()
    tradeRet[tradeRet==-0]=0
    winRate = len(tradeRet[tradeRet>0]) / len(tradeRet[tradeRet!=0])

    print(winRate)

    plt.plot(close['2021'],label='close',color='k')
    plt.plot(upDC['2021'],label='upboundDC',color='b',linestyle='dashed')
    plt.plot(downDC['2021'],label='downboundDC',color='b',linestyle='dashed')
    plt.plot(midDC['2021'],label='midDC',color='r', linestyle='-.' )
    plt.title('TQQQ Donchian Channels in 2021')
    plt.legend()
    plt.show()



if __name__=='__main__':
    name ="TQQQ"
    start = dt.datetime(2020,1,1)
    end = dt.datetime(2021,12,31)
    data = get_stock(name, start, end)
    don_channel(data,20)

