import backtrader as bt
from backtrader import cerebro
import pandas as pd
import pandas_datareader as pdr
import datetime as dt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

def get_stock_data(name):
    Stock_datasets = pdr.get_data_yahoo(name)
    return Stock_datasets

class MyStrategy(bt.Strategy):
    def __init__(self):
        print("init")
    
    def start(self):
        print("This world call me")

    def prenext(self):
        print("Not mature")

    def nextstart(self):
        print("Rites of passage")

    def next(self):
        print("A new bar")

    def stop(self):
        print("I should leave this world")

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    name = "TQQQ"
    data = get_stock_data(name)


    brf_daily = bt.feeds.PandasData(dataname=data,name='TQQQ',
    fromdate= dt.datetime(2019,1,1),
    todate=dt.datetime(2020,12,31))

  
    cerebro.adddata(brf_daily)
    cerebro.addstrategy(MyStrategy)
    cerebro.run()
    # cerebro.plot()
    b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    cerebro.plot(b)
 

