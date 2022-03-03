import backtrader as bt
import pandas_datareader as pdr
from backtrader_plotting import Bokeh
from backtrader_plotting.schemes import Tradimo
from astock.stock_bt.neo_strategy import*


def get_data(name, start=None,end=None):
    if start =='' and end =='':
        start =None
        end = None
        data = pdr.get_data_yahoo(name,start,end)
    elif start =='' and end !='':
        start = None 
        data = pdr.get_data_yahoo(name,start,end)
    elif start !='' and end =='':
        end =None
        data = pdr.get_data_yahoo(name,start,end)
    else:
        data = pdr.get_data_yahoo(name,start,end)
    return data
    
# Add other indicator to lines
class PandasData_more(bt.feeds.PandasData):
    lines = ('ac',)
    params = (
        ('ac', -1),

        )


def run_bt(name,strategy,start =None,end=None):
    cerebro = bt.Cerebro()
    data = get_data(name,start,end)

    
    strategy =  eval(strategy)

    cerebro.addstrategy(strategy)

    brf_daily = PandasData_more(dataname=data,name=name)
    cerebro.adddata(brf_daily)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio)
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')
    cerebro.addobserver(bt.observers.DrawDown)

    result = cerebro.run()
    print("--------------- DrawDown -----------------")
    print(result[0].analyzers._DrawDown.get_analysis())

    b = Bokeh(style='bar',tabs='multi',output_mode='save', scheme=Tradimo(),filename='./astock/templates/test.html')
    cerebro.plot(b)
    
    