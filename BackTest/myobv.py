import backtrader as bt
import pandas_datareader as pdr
import datetime as dt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

# get data of stock
def get_stock(name, start=None, end=None):
    data = pdr.get_data_yahoo(name,start)
    return data

class My_OBV(bt.Strategy):
    def __init__(self):
        self.obv = bt.talib.OBV(self.data.close, self.data.volume)
        self.bb = bt.talib.SMA(self.data, timeperiod=20)
        self.obv.plotinfo.subplot = True

    def next(self):
        if not self.position and self.obv>0:
            self.order =self.buy()
        if self.getposition().size<0 and self.obv>0:
            self.order=self.close()
            self.order = self.buy()
        if not self.position and self.obv<0:
            self.order = self.sell()
        if self.getposition().size>0 and self.obv<0:
            self.order =self.close()
            self.order = self.sell()

if __name__ =="__main__":
    
    name ="TQQQ"
    start = dt.datetime(2020,1,1)
    end = dt.datetime(2022,2,28)
    data = get_stock(name,start, end)

    print(data.tail())

    cerebro = bt.Cerebro()

    data = bt.feeds.PandasData(dataname=data,name=name)
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Add a strategy
    cerebro.addstrategy(My_OBV)

    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')
    cerebro.addanalyzer(bt.analyzers.DrawDown,_name='_DrawDown')
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer,_name='_tradeanalyzer')
    
    result = cerebro.run()
    analyzer = {}
    print(result[0].analyzers._DrawDown.get_analysis())
    print(result[0].analyzers._SharpeRatio.get_analysis())

    # cerebro.plot()

    b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    cerebro.plot(b)