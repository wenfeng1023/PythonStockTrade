# # Buy and Hold
# - S&P 500
# - Diversification
# - 8-10% annual return

import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib notebook

start = dt.datetime(1999, 1, 1)
sp500 = pdr.get_data_yahoo("^GSPC", start)


# ### The lost decade
# - 1999 - 2009
print( sp500.head() )

fig, ax = plt.subplots()
sp500['Close'].plot(ax=ax)
plt.savefig("plot.png", dpi=200)
plt.grid()
plt.show(block=False)

print( sp500['2009'].head() )
print( sp500['1999'].head() )

fig, ax = plt.subplots()
sp500['Close'].loc[:'2009-01-01'].plot()
plt.grid()
plt.show(block=True)
plt.waitforbuttonpress()
plt.close('all')

## Performance
### GAGR
data = sp500['Close'].loc['1999':'2008']
total_return = data.iloc[-1]/data.iloc[0]
print( total_return )
(data.iloc[-1]/data.iloc[0])**(1/10) - 1

### Drawdown
rolling_max = data.cummax()
daily_drawdown = data/rolling_max - 1

max_drawdown = daily_drawdown.cummin().iloc[-1]

print( max_drawdown )


# ### Project
# - Test the S&P 500 for the period 2010-2020
# #### Step 1
# - get the data
data = sp500['Close'].loc['2010':'2019']
(data.iloc[-1]/data.iloc[0])**(1/10) - 1

# #### Step 2
# - Calculate CAGR
# #### Step 3
# - Calculate max dropdown
rolling_max = data.cummax()
daily_drawdown = data/rolling_max - 1
max_drawdown = daily_drawdown.cummin().iloc[-1]
print( max_drawdown )


