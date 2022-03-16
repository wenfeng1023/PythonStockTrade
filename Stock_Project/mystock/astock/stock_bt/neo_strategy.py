import backtrader as bt


'''
    sam_ris Strategy

'''
class sam_ris(bt.Strategy):
    def __init__(self):
        sma1 = bt.indicators.SMA(period=11, subplot=True)
        bt.indicators.SMA(period=17, plotmaster=sma1)
        bt.indicators.RSI()

    def next(self):
        pos = len(self.data)
        if pos == 45 or pos == 145:
            self.buy(self.datas[0], size=None)
            
        if pos == 116 or pos == 215:
            self.sell(self.datas[0], size=None)

'''
  Three days lines Strategy
  
'''
class three_bars(bt.Indicator):
    lines =('up','down')
    def __init__(self):
        self.addminperiod(4)
        self.plotinfo.plotmaster = self.data
    
    def next(self):
        self.up[0] = max(max(self.data.close.get(ago=-1,size=3)),max(self.data.open.get(ago=-1,size=3)))
        self.down[0] = min(min(self.data.close.get(ago=-1,size=3)),min(self.data.open.get(ago=-1,size=3)))
       
class three_days_line(bt.Strategy):
    def __init__(self):
        self.up_down = three_bars(self.data)
        self.buy_signal = bt.indicators.CrossOver(self.data.ac,self.up_down.up)
        self.sell_signal = bt.indicators.CrossDown(self.data.ac,self.up_down.down)
        self.buy_signal.plotinfo.plot = True
        self.sell_signal.plotinfo.plot = True


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

'''
   BollingerBands(BBands)

'''
class bbands(bt.Strategy):
    def __init__(self):
        # self.bbbands = bt.indicators.BollingerBands(self.data.close)
        self.bbbands = bt.indicators.BollingerBandsPct(self.data.close)
    def next (self):
        pass

'''
    Momentum Strategy

'''
class Momentum (bt.Strategy):
    def __init__(self):
        pass
    def next (self):
        pass
'''
    Simple Moving Average Strategy
'''

class Sma_St (bt.Strategy):
    params = (('myperiod',20),)
    def __init__(self):
        self.sma = bt.indicators.SMA(self.data.close, period = self.p.myperiod)
        self.buy_sell_signal = bt.indicators.CrossOver(self.data.close,self.sma)
        
    def next (self):
        if not self.position and self.buy_sell_signal>0:
            self.order = self.buy()
        if self.getposition().size<0 and self.buy_sell_signal>0: 
            self.order = self.close()
            self.order = self.buy()
        if not self.position and self.buy_sell_signal<0:
            self.order = self.sell()
        if self.getposition().size>0 and self.buy_sell_signal<0:
            self.order = self.close()
            self.order = self.sell()
'''
    Double Simple Moving Average Strategy
'''
class Double_SMA (bt.Strategy):
    params = (('myperiod1',5),('myperiod2',20),)
    def __init__(self):
        self.sma1 = bt.indicators.SMA(self.data.close,period = self.p.myperiod1)
        self.sma2 = bt.indicators.SMA(self.data.close, period = self.p.myperiod2)
        self.buy_sell_signal = bt.indicators.CrossOver(self.sma1,self.sma2)

    def next (self):
        if not self.position and self.buy_sell_signal>0:
            self.order = self.buy()
        if self.getposition().size<0 and self.buy_sell_signal>0: 
            self.order = self.close()
            self.order = self.buy()
        if not self.position and self.buy_sell_signal<0:
            self.order = self.sell()
        if self.getposition().size>0 and self.buy_sell_signal<0:
            self.order = self.close()
            self.order = self.sell()

        

