from turtle import color, width
import backtrader as bt
import pandas_datareader as pdr
import datetime as dt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo



# get data of stock
def get_stock(name, start=None, end=None):
    data = pdr.get_data_yahoo(name,start, end)
    return data

class my_indicator(bt.Indicator):
    lines = ('volSMA','volume1',)
    
    plotinfo = dict(subplot=True)
    plotlines = dict(volume1 = dict (_method='bar', color = 'blue',alpha=0.50, width=1.0),volSMA = dict(markersize=20.0, width=20, color = 'red'))  

    def __init__(self):
        self.l.volume1 = self.data.volume
        self.volsma5 = bt.indicators.SMA(self.data.volume,period=5)
        self.volsma10 = bt.indicators.SMA(self.data.volume, period = 10)
        self.l.volSMA = (self.volsma5+self.volsma10)/2
        

class MyStrategy(bt.Strategy):
    def __init__(self):
        
        self.volSMA = my_indicator(self.data)
        self.sma5 = bt.indicators.SMA(self.data.close, period=5)
        self.sma20 = bt.indicators.SMA(self.data.close, period=20)

        self.buy_signal = bt.indicators.CrossOver(self.sma5,self.sma20)
        self.sell_signal = bt.indicators.CrossOver(self.sma5,self.sma20)
        self.buy_signal2 = self.data.lines.volume > self.volSMA
        self.sell_signal2 = self.data.lines.volume<=self.volSMA

        

    def next (self):
        # if not self.position and  self.buy_signal>0 and self.buy_signal2:
        #     self.order = self.buy()
        # if self.getposition().size<0 and self.buy_signal>0 and self.buy_signal2:
        #     self.order=self.close()
        #     print('Closing', self.getposition(self.data).size)
        #     self.order = self.buy()
        # if not self.position and self.sell_signal<0 and self.sell_signal2:
        #     self.order = self.sell()
        # if self.getposition().size>0 and self.sell_signal<0 and self.sell_signal2:
        #     self.order = self.close()
        #     print('Closing', self.getposition(self.data).size)
        #     self.order = self.sell()

        if  not self.position and self.buy_signal>0 and self.buy_signal2:
            self.order = self.buy(size=100)
        if not self.position and self.sell_signal<0 and self.sell_signal2:
            self.order = self.sell(size=100)
        if self.position and self.buy_signal>0 and self.buy_signal2:
            self.order = self.close(size=100)
            self.order = self.buy(size=100)
        if self.position and self.sell_signal<0 and self.sell_signal2:
            self.order = self.close(size=100)
            self.order = self.sell(size=100)
        


if __name__ =="__main__":
    name ="AAPL"
    start = dt.datetime(2020,1,1)
    end = dt.datetime(2021,12,31)
    data = get_stock(name, start, end)

    print(data.head())
    
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(MyStrategy)

    data = bt.feeds.PandasData(dataname=data,name=name)
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # set cash 
    startcash = 100000
    cerebro.broker.setcash(startcash)
    cerebro.broker.setcommission(commission=0.001) 
    cash_value = cerebro.broker.getcash() # 获取当前可用资金
    portvalue = cerebro.broker.getvalue()
    pnl = portvalue - startcash

    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='_Returns', tann=252)
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='_TimeReturn')

    result = cerebro.run()

    print(f'总资金: {round(portvalue,2)}')
    print(f'净收益: {round(pnl,2)}')

    print(result[0].analyzers._AnnualReturn.get_analysis())
    print(result[0].analyzers._Returns.get_analysis())
    print(result[0].analyzers._TimeReturn.get_analysis())

    # cerebro.plot()

    b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    cerebro.plot(b)