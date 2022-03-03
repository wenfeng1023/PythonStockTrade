from asyncio import base_tasks
import backtrader as bt
from pandas import Period
import pandas_datareader as pdr
import datetime as dt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

def get_stock_data(name,start=None, end=None):
    Stock_datasets = pdr.get_data_yahoo(name,start,end)
    return Stock_datasets

class mystrategy(bt.Strategy):
    def __init__(self):
        self.bbbands = bt.indicators.BollingerBands(self.data.close)
        # self.bbbands = bt.indicators.BollingerBandsPct(self.data.close)
        # self.kdj = bt.indicators.Stochastic(self.data)
    def next (self):
        pass

if __name__ == '__main__':
    name = 'TQQQ'
    start = dt.datetime(2019,1,1)
    end = dt.datetime(2022,1,1)
    data = get_stock_data(name,start,end)
    print(data.head())

    cerebro  = bt.Cerebro()
    # cerebro.addobserver(bt.observers.DrawDown)

    brf_daily = bt.feeds.PandasData(dataname=data,name='TQQQ')

    cerebro.adddata(brf_daily)
    cerebro.addstrategy(mystrategy)

    result = cerebro.run()

    cerebro.plot(numfigs=1)
    
    # b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    # cerebro.plot(b)
        