import backtrader as bt # 导入 Backtrader
import backtrader.indicators as btind # 导入策略分析模块
import backtrader.feeds as btfeeds # 导入数据模块
import pandas_datareader as pdr
import datetime as dt
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

def get_data(name,start=None, end =None):
    data = pdr.get_data_yahoo(name,start,end)
    return data

# 创建策略
class TestStrategy(bt.Strategy):

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        
        self.momentum = bt.indicators.Momentum(self.data.close, period=90)
        self.momentum6 = bt.indicators.Momentum(self.data.close, period = 6)
        # self.buy_sig = self.momentum > 0
        # self.sell_sig= self.momentum <0
        # self.buy_sig.plotinfo.plot = False
        # self.sell_sig.plotinfo.plot = False



    def next(self):
        # print('momentum',self.momentum.get(ago=0, size=3))
        
        if not self.position and self.momentum>0 and self.momentum6>0:
            self.order =self.buy()
        if self.getposition().size<0 and self.momentum>0 and self.momentum6>0:
            self.order = self.close()
            self.order = self.buy
        if not self.position and self.momentum<0 and self.momentum6<0:
            self.order = self.sell()
        if self.getposition().size>0 and self.momentum<0 and self.momentum6<0:
            self.order = self.close()
            self.order = self.sell()
 

if __name__ == '__main__':
    name ='TQQQ'
    start = dt.datetime(2011,1,1)
    end = dt.datetime(2021,12,31)
    dataframe = get_data(name,start,end)
  
    cerebro = bt.Cerebro()
   
    data = bt.feeds.PandasData(dataname=dataframe,name='TQQQ')
    
    cerebro.adddata(data)

    cerebro.addstrategy(TestStrategy)

    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')
    cerebro.addanalyzer(bt.analyzers.DrawDown,_name='_DrawDown')
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer,_name='_tradeanalyzer')

    
    cerebro.run()
    # cerebro.plot()

    b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    cerebro.plot(b)