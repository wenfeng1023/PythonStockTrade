import backtesting
import pandas as pd
from backtesting import Backtest, Strategy
from pandas_ta import rsi
import pandas_datareader as pdr
import datetime as dt


def download_daily_data(symbol: str, filepath: str):
    pass


def get_daily_data(symbol):
    # start = dt.datetime(2010,1,1)
    # end = dt.datetime(2020,1,1)
    data = pdr.get_data_yahoo(symbol)
    return data

def get_adjusted_close():
    pass

def add_symbol_adjusted_close(symbol: str, full_df: pd.DataFrame) -> pd.DataFrame:
    
    new_df = get_daily_data(symbol)

    close_df = pd.DataFrame(index=new_df.index)
    close_df[symbol] = new_df.adjusted_close

    return full_df.merge(close_df, left_index=True, right_index=True)

class BasicRsiStrategy(Strategy):
    def init(self):
        self.rsi = self.I(rsi, self.data.df.Close, length=14)

    def next(self):
        today = self.rsi[-1]
        yesterday = self.rsi[-2]

        # Crosses below 30 (oversold, time to buy)
        if yesterday > 30 and today < 30 and not self.position.is_long:
            self.buy()

        # Crosses above 70 (overbought, time to sell)
        elif yesterday < 70 and today > 70 and self.position.size > 0:
            self.position.close()
        


if __name__ == '__main__':
    symbol = 'TQQQ'
    data = get_daily_data(symbol)
    # data = add_symbol_adjusted_close('Adj Close',data)
    print(data.head())
    strategy = BasicRsiStrategy

    bt = Backtest(
        data=data,
        strategy=strategy,
        cash = 1000,
        commission=.002,
        exclusive_orders=False,
        trade_on_close=False
    )
stats = bt.run()
print(stats)

bt.plot(
        smooth_equity=True,
        superimpose=True,
        filename='TQQQ',
        show_legend=True
    )