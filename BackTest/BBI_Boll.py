import backtrader as bt
from matplotlib import lines
import pandas_datareader as pdr
import datetime as dt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo
import pandas as pd
import quantstats

class BBIboll(bt.Indicator):
    lines = ('up','mid','down',)
    params = (('period_sm1',3),
            ('period_sm2',6),
            ('period_sm3',12),
            ('period_sm4',24),
            ('M',6),('N',11),)
    plotinfo = dict(subplot=False)

    def __init__(self):
        sm3 = bt.indicators.SMA(self.data, period = self.p.period_sm1)
        sm6 = bt.indicators.SMA(self.data, period= self.p.period_sm2)
        sm12 = bt.indicators.SMA(self.data, period= self.p.period_sm3)
        sm24 = bt.indicators.SMA(self.data, period= self.p.period_sm4)

        self.l.mid = (sm3+sm6+sm12+sm24)/4
        self.l.up = self.l.mid + self.p.M* bt.indicators.StandardDeviation(self.l.mid, period= self.p.N)
        self.l.down = self.l.mid - self.p.M* bt.indicators.StandardDeviation(self.l.mid, period= self.p.N)

    def next(self):
        pass

def get_stock_data(name,start=None, end=None):
    Stock_datasets = pdr.get_data_yahoo(name,start,end)
    return Stock_datasets

class mystrategy(bt.Strategy):
    def __init__(self):
        # self.bbbands = bt.indicators.BollingerBands(self.data.close)
        self.mid = BBIboll(self.data.close).mid
        self.up = BBIboll(self.data.close).up
        self.down = BBIboll(self.data.close).down
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
        