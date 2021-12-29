from os import name
import backtrader as bt
from datetime import datetime
import pandas as pd
import pandas_datareader as pdr

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
                self.buy(size=100)
        else:
            if self.rsi > 70:
                self.sell(size=100)
class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)
#simple moving average


if __name__ == '__main__':
    data = "TQQQ"
    # dataframe = pd.read_csv("./TQQQ.csv", parse_dates=True,index_col=0)
    dataframe = get_data(data)
    print(dataframe.head())    
#Get Apple data from Yahoo Finance.
# data = bt.feeds.Quandl(
#     dataname='APPL',
#     fromdate = datetime(2016,1,1),
#     todate = datetime(2017,1,1),
#     buffered= True
#     )

    # get data from pandas dataframe
    data = bt.feeds.PandasData(dataname=dataframe,name='TQQQ')
    cerebro = bt.Cerebro()

    # Add your strategy
    cerebro.addstrategy(SmaCross)

    # Add your data
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