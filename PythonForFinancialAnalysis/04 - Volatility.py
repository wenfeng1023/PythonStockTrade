import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = dt.datetime(1999, 1, 1)
end = dt.datetime(2008, 12, 31)

data = pdr.get_data_yahoo("^GSPC", start, end)

data['Log returns'] = np.log(data['Adj Close']/data['Adj Close'].shift())

data['Adj Close'].iloc[-1]/data['Adj Close'].iloc[0]

data['Log returns'].sum()

np.exp(data['Log returns'].sum())

data['Normalize'] = data['Adj Close']/data['Adj Close'].iloc[0]

data['Exp sum'] = data['Log returns'].cumsum().apply(np.exp)

data[['Normalize', 'Exp sum']].tail()

volatility = data['Log returns'].std()*(252**0.5)

print( volatility )


# ### Project
# - Visualize the volatility
# #### Step 1
# - Import matplotlib
# #### Step 2
# - Get the volatility as a string

str_vol = str(round(volatility, 3)*100)

# #### Step 3
# - Visualize it in a histogram

fig, ax = plt.subplots()
data['Log returns'].hist(ax=ax, bins=50, alpha=0.6, color='b')
ax.set_xlabel("Log returns of stock price")
ax.set_ylabel("Frequencey of log returns")
ax.set_title("Historic Volatility for S&P 500 (" + str_vol +"%)")
plt.show(block=True)
plt.grid()

print ( np.log(1.2)+np.log(1.15)+np.log(1.1)+np.log(1.3) )
print ( np.exp(0.6797579434409292) )
