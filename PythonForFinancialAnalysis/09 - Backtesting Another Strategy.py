# Backtesting Another Strategy

import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook

tickers = ['SPY', 'IWM', 'MDY', 'QQQ', 'TLT']

start = dt.datetime(2007, 1, 1)
end = dt.datetime(2021, 1, 1)

data = pdr.get_data_yahoo(tickers, start, end, interval='m')

data = data['Adj Close']

data['Short'] = 1.0
data = data[['SPY', 'IWM', 'MDY', 'QQQ', 'Short', 'TLT']]

log_returns = np.log(data/data.shift())

strat = log_returns[['SPY', 'IWM', 'MDY', 'QQQ', 'Short']].copy()
rolling_sum = strat.copy()

for ticker in ['SPY', 'IWM', 'MDY', 'QQQ', 'Short']:
    rolling_sum[ticker] = rolling_sum[ticker].rolling(3).sum()
    
rtn = strat[rolling_sum.apply(lambda x: x == rolling_sum.max(axis=1)).shift()].sum(axis=1)*.6
rtn = rtn + log_returns['TLT']*.4

# ### Project
# - Backtesting the strategy

# #### Step 1
# - Modify to evaluate monthly data

# #### Step 2
# - Copy paste visualization

def visualize(backtest, spy, start, end):
    def x_titles(spy_val, bt_val):
        spy_str = str(round(spy_val*100, 1))
        bt_str = str(round(bt_val*100, 1))
        return ['SPY\n' + spy_str + '%', 'Backtest\n' + bt_str + '%']
        
    spy_cagr, spy_drawdown, spy_vol = calculate(spy, start, end)
    bt_cagr, bt_drawdown, bt_vol = calculate(backtest, start, end)

    fig, ax = plt.subplots(2, 2)
    
    spy.loc[start:end].cumsum().apply(np.exp).plot(ax=ax[0, 0])
    backtest.loc[start:end].cumsum().apply(np.exp).plot(ax=ax[0, 0], label='Backtest', c='c')
    ax[0, 0].legend()
    ax[0, 0].set_xticks([start, end])
    
    x = x_titles(spy_cagr, bt_cagr)
    ax[0, 1].bar(x, [spy_cagr, bt_cagr], color=['b', 'c'])
    ax[0, 1].set_title("CAGR")
    
    x = x_titles(spy_drawdown, bt_drawdown)
    ax[1, 0].bar(x, [spy_drawdown, bt_drawdown], color=['b', 'c'])
    ax[1, 0].set_title("Drawdown")

    x = x_titles(spy_vol, bt_vol)
    ax[1, 1].bar(x, [spy_vol, bt_vol], color=['b', 'c'])
    ax[1, 1].set_title("Volatility")

    plt.tight_layout()
    
# #### Step 3
# - Backtest 2008 to end 2017
# - Backtest 2011 to end 2020

visualize(rtn, log_returns['SPY'], '2008', '2017')

visualize(rtn, log_returns['SPY'], '2011', '2020')




