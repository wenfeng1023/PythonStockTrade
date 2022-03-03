'''
A example of custom new indicator with backtrade. 
We will creat a new indicator which calculate three EMA lines.
According to these three lines, we will make a backtest for TQQQ

'''

import backtrader as bt
from cv2 import EVENT_FLAG_SHIFTKEY
from pandas import PeriodDtype
import pandas_datareader as pdr
import datetime as dt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

def get_stock_data(name):
    Stock_datasets = pdr.get_data_yahoo(name)
    return Stock_datasets

'''
   Create a new class to inherit the class of Indicator.  
'''
class My_indicator(bt.Indicator):
    # add three columns in backtrade
    lines = ('mid','top','bot',)
    params = (('maperiod',20),
              ('period',3),
              ('highRate',1.2),
              ('lowRate',0.85),)
    #set these three lines in the main plot. 
    plotinfo = dict(subplot=False)

    def __init__(self):
        ema = bt.ind.EMA(self.data, period=self.p.maperiod)

        #Calculate lines of EMA which is middle, top and bottom
        self.l.mid=bt.ind.EMA(ema,period=self.p.period)
        self.l.top=bt.ind.EMA(self.mid*self.p.highRate,\
                              period=self.p.period)
        self.l.bot=bt.ind.EMA(self.mid*self.p.lowRate,\
                              period=self.p.period)
        super(My_indicator, self).__init__()

'''
Create a class of  TestStrategy and inherit bt.Strategy.
The fuction of this class is to write strategy of backtest.
'''
class TestStrategy(bt.Strategy):

    params=(('period',20),)

    def __init__(self):
        self.order = None
        # self.mid = My_indicator(self.data).mid 
        # self.top = My_indicator(self.data).top
        # self.bot = My_indicator(self.data).bot
        self.macd = bt.indicators.MACDHisto(self.data.close)
        self.sma5 = bt.indicators.SMA(self.data.close,period=5)
        self.sma30 = bt.indicators.SMA(self.data.close, period=30)
        # self.dif = bt.indicators.EMA(self.data.close, period = 12,plot= False) - bt.indicators.EMA(self.data.close, period= 26, plot=False)
        self.DIF = self.macd.lines.macd
        self.DEA = self.macd.lines.signal
        # self.dea = bt.indicators.EMA(self.dif, period = 9)
        self.crossover = bt.indicators.CrossOver(self.sma5, self.sma30)
        self.dif_crossover = bt.indicators.CrossOver(self.DIF, self.DEA)
        # self.buy_sig = bt.And(self.DIF>0,self.DEA>0,self.dif_crossover>0)
        # self.sell_sig = bt.And(self.DIF<0,self.DEA<0,self.dif_crossover<0)

            
        # self.sell_sig = bt.indicators.CrossDown(self.sma5, self.sma30)
        # self.buy_sig=bt.And(\
        #    self.data.close>self.mid,\
        #    self.data.volume==bt.ind.Highest(\
        #    self.data.volume,period=self.p.period))

        # #set the signal of sell
        # self.sell_sig=self.data.close>self.top

    def next(self):
        print('当前可用资金:', self.broker.getcash())
        print("当前总资产:", self.broker.getvalue())
        print("当前持仓量:", self.broker.getposition(self.data).size)
        print("当前持仓成本:", self.broker.getposition(self.data).price)
        if self.crossover>0:
            self.order = self.buy(size=100)
        else:
            if self.crossover<0:
                self.order = self.sell(size=100)

        # if not self.position:
        #     total_value = self.broker.getvalue()

        #     ss=int((total_value/100)/self.datas[0].close[0])*100

        #     #Buy
        #     if self.buy_sig:
        #         self.order=self.buy(size=100)
        # #sell
        # else:
        #     if self.sell_sig:
        #         self.sell()

if __name__ == '__main__':
    name = 'TQQQ'
    data = get_stock_data(name)

    cerebro  = bt.Cerebro()
    # cerebro.addobserver(bt.observers.DrawDown)

    brf_daily = bt.feeds.PandasData(dataname=data,name='TQQQ',
    fromdate= dt.datetime(2021,1,1),
    todate=dt.datetime(2021,12,31))

    cerebro.adddata(brf_daily)
    cerebro.addstrategy(TestStrategy)

    # set cash 
    startcash = 100000
    cerebro.broker.setcash(startcash)
    cerebro.broker.setcommission(commission=0.001) 
    cash_value = cerebro.broker.getcash() # 获取当前可用资金

    print(cash_value)

    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')
    # cerebro.addanalyzer(bt.analyzers.sharpe)

    result = cerebro.run()
    print("--------------- DrawDown -----------------")
    print(result[0].analyzers._DrawDown.get_analysis())

    portvalue = cerebro.broker.getvalue()
    pnl = portvalue - startcash

    print(f'Total funds: {round(portvalue,2)}')
    print(f'net income: {round(pnl,2)}')

    # cerebro.plot(numfigs=1)
    b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    cerebro.plot(b)
 

