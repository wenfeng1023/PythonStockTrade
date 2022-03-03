import backtrader as bt
from backtrader import cerebro
import pandas as pd
import pandas_datareader as pdr
import datetime as dt

def get_stock_data(name):
    Stock_datasets = pdr.get_data_yahoo(name)
    return Stock_datasets

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.count = 0 # 用于计算 next 的循环次数
        # 打印数据集和数据集对应的名称
        print("------------- init 中的索引位置-------------")
        print("0 索引:",'datetime',self.data.lines.datetime.date(0), 'close',self.data.lines.close[0])
        print("-1 索引:",'datetime',self.data.lines.datetime.date(-1),'close', self.data.lines.close[-1])
        print("-2 索引",'datetime', self.data.lines.datetime.date(-2),'close', self.data.lines.close[-2])
        print("1 索引:",'datetime',self.data.lines.datetime.date(1),'close', self.data.lines.close[1])
        print("2 索引",'datetime', self.data.lines.datetime.date(2),'close', self.data.lines.close[2])
        print("从 0 开始往前取3天的收盘价:", self.data.lines.close.get(ago=0, size=3))
        print("从-1开始往前取3天的收盘价:", self.data.lines.close.get(ago=-1, size=3))
        print("从-2开始往前取3天的收盘价:", self.data.lines.close.get(ago=-2, size=3))
        print("line的总长度:", self.data.buflen())
    
    def start(self):
        print("This world call me")

    def prenext(self):
        print("Not mature")

    def nextstart(self):
        print("Rites of passage")

    def next(self):
        # print('datetime', self.datas[0].datetime.date(0))
        print(f"------------- next 的第{self.count+1}次循环 --------------")
        print("数据起始当前时点（今日）:",'datetime',self.data.lines.datetime.date(0),'close', self.data.lines.close[0])
        # print("往前推1天（昨日）:",'datetime',self.data.lines.datetime.date(-1),'close', self.data.lines.close[-1])
        # print("往前推2天（前日）", 'datetime',self.data.lines.datetime.date(-2),'close', self.data.lines.close[-2])
        # print("前日、昨日、今日的收盘价:", self.data.lines.close.get(ago=0, size=3))
        # print("往后推1天（明日）:",'datetime',self.data.lines.datetime.date(1),'close', self.data.lines.close[1])
        # print("往后推2天（明后日）", 'datetime',self.data.lines.datetime.date(2),'close', self.data.lines.close[2])
        # print("已处理的数据点:", len(self.data))
        # print("line的总长度:", self.data0.buflen())
        self.count += 1

    def stop(self):
        print("I should leave this world")

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    name = "TQQQ"
    data = get_stock_data(name)
    print(data.tail())


    brf_daily = bt.feeds.PandasData(dataname=data,name='TQQQ',fromdate=dt.datetime(2021,1,1),todate=dt.datetime(2022,1,11))

  
    cerebro.adddata(brf_daily)
    cerebro.addstrategy(MyStrategy)
    cerebro.run()
 

