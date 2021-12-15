# Backtesting an Active Strategy

import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook

tickers = ['SPY', 'TLT']

start = dt.datetime(2007, 1, 1)
end = dt.datetime(2021, 1, 1)

data = pdr.get_data_yahoo(tickers, start, end)

data = data['Adj Close']

ma = data['SPY'].rolling(200).mean()

signal_line = data['SPY'] - ma
signal_line = signal_line.apply(np.sign)

log_return = np.log(data/data.shift())

rtn = signal_line.clip(lower=0).shift(1)*log_return['SPY']
rtn = rtn - (signal_line.clip(upper=0).shift())*log_return['TLT']

print( rtn.loc['2008':].cumsum().apply(np.exp) )

print( log_return['SPY'].loc['2008':].cumsum().apply(np.exp) )

fig, ax = plt.subplots()

rtn.loc['2008':].cumsum().apply(np.exp).plot(ax=ax, label='Backtest')
log_return['SPY'].loc['2008':].cumsum().apply(np.exp).plot(ax=ax)
ax.legend()

plt.grid()
plt.show(block=True)
plt.waitforbuttonpress()
plt.close('all')


# ### Project
# - Backtesting different periods and visualize results

# #### Step 1
# - Make a function which calucates the CAGR, maximum drawdown, and volatility

# #### Step 2
# - Use our function on SPY from 2008 to end 2017
# - And on our strategy in the same period

calculate(log_return['SPY'], '2008', '2017')

calculate(rtn, '2008', '2017')

# #### Step 3
# - Create a visual reprentation of the result



