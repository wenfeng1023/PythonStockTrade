import backtrader as bt
import datetime as dt
import pandas as pd
import pandas_datareader as pdr
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo

def get_data(data):
    Tdata = pdr.get_data_yahoo(data)
    return Tdata
class firstStrategy(bt.Strategy):

    def __init__(self):
        
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=21)
        self.dataclose = self.datas[0].close

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}') #Print date and close

    def next(self):
        # self.log('Close, %.2f' % self.dataclose[0])
        if not self.position:
            if self.rsi < 30:
                self.buy(size=200)
        else:
            if self.rsi > 70:
                self.close()
                self.sell(size=200)
class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)
class my_strategy2(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.MovingAverageSimple(self.datas[0].close, period = 20)
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
    def next (self):
        if not self.position:
            if self.dataclose[0]>self.sma[0]:
                self.order = self.buy(size=500)
            else:
                if self.dataclose[0]<self.sma[0]:
                    self.order = self.sell(size=500)
        
#simple moving average


if __name__ == '__main__':
    data = "TQQQ"
    # dataframe = pd.read_csv("./TQQQ.csv", parse_dates=True,index_col=0)
    dataframe = get_data(data)
    print(dataframe.tail())    

    data = bt.feeds.PandasData(dataname=dataframe,name='TQQQ',fromdate= dt.datetime(2010,1,1),
    todate=dt.datetime(2020,12,31))

    cerebro = bt.Cerebro()
    startcash = 10000
    cerebro.broker.setcash(startcash)
    cerebro.broker.setcommission(commission=0.002)

# ???????????????????????????
    portvalue = cerebro.broker.getvalue()
    pnl = portvalue - startcash
    
 
    
    # Add your strategy
    cerebro.addstrategy(my_strategy2)

    # Add your data
    cerebro.adddata(data)

        # ??????????????????
    # ???????????????????????????????????????
    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')
    # ??????????????????????????????
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')
    # ?????????????????????????????????
    cerebro.addanalyzer(bt.analyzers.Returns, _name='_Returns', tann=252)
    # ???????????????????????????????????????
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio', timeframe=bt.TimeFrame.Days, annualize=True, riskfreerate=0) # ??????????????????
    cerebro.addanalyzer(bt.analyzers.SharpeRatio_A, _name='_SharpeRatio_A')
    # ?????????????????????
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='_TimeReturn')

    result = cerebro.run()
    
    print(f'?????????: {round(portvalue,2)}')
    print(f'?????????: {round(pnl,2)}')
    pos = cerebro.broker.getposition(data)
    print('size:', pos.size)
    print('price:', pos.price)
    print('value:', cerebro.broker.get_value())
    print('cash:', cerebro.broker.get_cash())




    # ????????????
    print("--------------- AnnualReturn -----------------")
    print(result[0].analyzers._AnnualReturn.get_analysis())
    print("--------------- DrawDown -----------------")
    print(result[0].analyzers._DrawDown.get_analysis())
    print("--------------- Returns -----------------")
    print(result[0].analyzers._Returns.get_analysis())
    print("--------------- SharpeRatio -----------------")
    print(result[0].analyzers._SharpeRatio.get_analysis())
    print("--------------- SharpeRatio_A -----------------")
    print(result[0].analyzers._SharpeRatio_A.get_analysis())

    # cerebro.plot(volume=False, savefig=True, figfilename='backtrader-plot.html')
    b = Bokeh(style='bar',tabs='multi',output_mode='show', scheme=Tradimo())
    cerebro.plot(b)

