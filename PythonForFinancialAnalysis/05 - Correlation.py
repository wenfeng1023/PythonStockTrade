# Correlation


import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook

tickers = ['SPY', 'TLT']

start = dt.datetime(2008, 1, 1)
end = dt.datetime(2017, 12, 31)

data = pdr.get_data_yahoo(tickers, start, end)
data = data['Adj Close']

log_returns = np.log(data/data.shift())
log_returns.corr()

fig, ax = plt.subplots()
(data/data.iloc[0]).plot(ax=ax)
plt.grid()

data_set = data.loc['2008-05':'2011-04']

fig, ax = plt.subplots()
(data_set/data_set.iloc[0]).plot(ax=ax)
plt.grid()

plt.show(block=True)
plt.waitforbuttonpress()
plt.close('all')
