import backtrader as bt
from backtrader import cerebro
import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pylab as plt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo
from sqlalchemy import false

def get_stock_data(name):
    Stock_datasets = pdr.get_data_yahoo(name)
    return Stock_datasets

# Add other indicator to lines
class PandasData_more(bt.feeds.PandasData):
    lines = ('ac',)
    params = (
        ('ac', -1),

        )



class three_bars(bt.Indicator):
    lines =('up','down')
    def __init__(self):
        self.addminperiod(4)
        self.plotinfo.plotmaster = self.data
    
    def next(self):
        self.up[0] = max(max(self.data.close.get(ago=-1,size=3)),max(self.data.open.get(ago=-1,size=3)))
        self.down[0] = min(min(self.data.close.get(ago=-1,size=3)),min(self.data.open.get(ago=-1,size=3)))
        
class MyStrategy(bt.Strategy):
    def __init__(self):
        # print("--------- 打印 self.datas 第一个数据表格的 lines ----------")
        # print(self.lines.getlinealiases())
        # print(self.datas[0].lines.getlinealiases())
        # print('Adj Close:', self.datas[0].lines.ac)
        # print("0 索引:",'datetime',self.data.lines.datetime.date(0), 'Ad Close',self.data.lines.ac[0])
        self.up_down = three_bars(self.data)
        self.buy_signal = bt.indicators.CrossOver(self.data.ac,self.up_down.up)
        self.sell_signal = bt.indicators.CrossDown(self.data.ac,self.up_down.down)
        self.buy_signal.plotinfo.plot = False
        self.sell_signal.plotinfo.plot = False
    
    def start(self):
        print("This world call me")

    def prenext(self):
        print("Not mature")

    def nextstart(self):
        print("Rites of passage")

    def next(self):

        if not self.position and self.buy_signal[0] ==1:
            self.order =self.buy()
        if self.getposition().size<0 and self.buy_signal[0]==1:
            self.order=self.close()
            self.order = self.buy()
        if not self.position and self.sell_signal[0]==1:
            self.order = self.sell()
        if self.getposition().size>0 and self.sell_signal[0]==1:
            self.order =self.close()
            self.order = self.sell()

    def stop(self):
        print("I should leave this world")

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    name = "TQQQ"
    data = get_stock_data(name)

    # print(data[dt.datetime(2020-12-31)])

    data['ac'] =data['Adj Close']


    # brf_daily = bt.feeds.PandasData(dataname=data,name='TQQQ',
    # fromdate= dt.datetime(2019,1,1),
    # todate=dt.datetime(2020,12,31))

    brf_daily = PandasData_more(dataname=data,name='TQQQ',
    fromdate= dt.datetime(2019,1,1),
    todate=dt.datetime(2020,12,31))

  
    cerebro.adddata(brf_daily)
    cerebro.addstrategy(MyStrategy)

    cerebro.run()
    cerebro.plot(style='candle')
    # b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    # cerebro.plot(b)
 

