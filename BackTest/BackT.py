import backtrader as bt
from datetime import datetime
import pandas as pd

class firstStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=21)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy(size=100)
        else:
            if self.rsi > 70:
                self.sell(size=100)
class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)


dataframe = pd.read_csv("./TQQQ.csv", parse_dates=True,index_col=0)
print(dataframe.head())    
#Get Apple data from Yahoo Finance.
# data = bt.feeds.Quandl(
#     dataname='APPL',
#     fromdate = datetime(2016,1,1),
#     todate = datetime(2017,1,1),
#     buffered= True
#     )
data = bt.feeds.PandasData(dataname=dataframe)
cerebro = bt.Cerebro()
cerebro.addstrategy(firstStrategy)

cerebro.adddata(data)

cerebro.run()
cerebro.plot()

# #Variable for our starting cash
# startcash = 10000

# #Create an instance of cerebro
# cerebro = bt.Cerebro()

# #Add our strategy
# cerebro.addstrategy(SmaCross)

# #Get Apple data from Yahoo Finance.
# data = bt.feeds.Quandl(
#     dataname='TQQQ',
#     fromdate = datetime(2016,1,1),
#     todate = datetime(2017,1,1),
#     buffered= True
#     )

# #Add the data to Cerebro
# cerebro.adddata(data)

# # Set our desired cash start
# cerebro.broker.setcash(startcash)

# # Run over everything
# cerebro.run()

# #Get final portfolio Value
# portvalue = cerebro.broker.getvalue()
# pnl = portvalue - startcash

# #Print out the final result
# print('Final Portfolio Value: ${}'.format(portvalue))
# print('P/L: ${}'.format(pnl))

# #Finally plot the end results
# cerebro.plot(style='candlestick')