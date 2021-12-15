# # A Simple Portfolio
# - 50% SPY and 50% TLT

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

portfolio = [.5, .5]

fig, ax = plt.subplots()

((data/data.iloc[0])*portfolio).sum(axis=1).plot(ax=ax)
(data/data.iloc[0]).plot(ax=ax)

plt.grid()
plt.show(block=False)

strategy = ((data/data.iloc[0])*portfolio).sum(axis=1)
log_returns = np.log(strategy/strategy.shift())

### GAGR

(strategy.iloc[-1]/strategy.iloc[0])**(1/10) - 1

### Drawdown

rolling_max = strategy.cummax()
daily_drawdown = strategy/rolling_max - 1
max_drawdown = daily_drawdown.cummin().iloc[-1]
max_drawdown

### Volatility

log_returns.std()*(252**0.5)

# ### Project
# - Annual rebalance

# #### Step 1
# - Annual rebalance step

concat = []
for year in range(2008, 2018):
    rebalance = (data.loc[str(year)]/data.loc[str(year)].iloc[0]*portfolio).sum(axis=1)
    if year > 2008:
        rebalance = rebalance*concat[-1].iloc[-1]
    concat.append(rebalance)

    
strategy = pd.concat(concat)

# #### Step 2
# - CAGR

(strategy.iloc[-1]/strategy.iloc[0])**(1/10) - 1

# #### Step 3
# - Maximum drawdown

rolling_max = strategy.cummax()
daily_drawdown = strategy/rolling_max - 1
max_drawdown = daily_drawdown.cummin().iloc[-1]
print( max_drawdown )

# #### Step 4
# - Volatility

(np.log(strategy/strategy.shift())).std()*(252**0.5)

# #### Step 5
# - Visualization

fig, ax = plt.subplots()

(data/data.iloc[0]).plot(ax=ax)
strategy.plot(ax=ax)

plt.grid()
plt.show(block=True)
plt.waitforbuttonpress()
plt.close('all')



