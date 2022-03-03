import pandas as pd
import pandas_datareader as pdr
import matplotlib.pylab as plt
import datetime as dt
import mplfinance as mpf
def get_stock(name, start=None,end= None):
    data  = pdr.get_data_yahoo(name,start, end)
    return data

def momentum_c(close,period):
    lag5close = close.shift(period)
    momentum = close - lag5close
    momentum = momentum.dropna()
    return momentum


if __name__=="__main__":
    name ="AAPL"
    start = dt.datetime(2011,1,1)
    end = dt.datetime(2021,12,31)

    data = get_stock(name,start, end)
    mo = momentum_c(data['Close'],35)

    plt.subplot(211)
    plt.plot(data['Close'],'b*')
    plt.xlabel('data')
    plt.ylabel('Close')
    plt.title('TQQQ 5 Momentum')
    plt.subplot(212)
    plt.plot(data['Close'],'r-*')
    plt.xlabel('data')
    plt.ylabel('Momentum5')
    plt.show()
    # mpf.plot(data,type='candle')