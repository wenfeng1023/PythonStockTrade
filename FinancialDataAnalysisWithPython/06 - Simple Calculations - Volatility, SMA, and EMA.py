# 06 - Simple Calculations - Volatility, SMA, and EMA
# # Calculating simple 
# - Pct change
# - Log returns
# - Standard deviation (Volatility)
# - Rolling
#     - Simple Moving Avarage
#     - Exponential Moving Average
# ### Standard deviation

# - $\sigma_{p} = \sigma_{daily}\times \sqrt{p}$
# - $\sigma_{annually} = \sigma_{daily}\times \sqrt{252}$
 
#     *(252 trading days per year)*

import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib notebook

remote_file = "https://raw.githubusercontent.com/LearnPythonWithRune/FinancialDataAnalysisWithPython/main/AAPL.csv"
data = pd.read_csv(remote_file, index_col=0, parse_dates=True)

print( data.head() )
data['%-chg'] = data['Close'].pct_change()
print( data.head() )
(79.422501 - 77.237503)/77.237503 

import numpy as np
data['Log returns'] = np.log(data['Close']/data['Close'].shift())
print( data.head() )
print( data['Log returns'].std() )
volatility = data['Log returns'].std()*252**.5
print( volatility )
str_vol = str(round(volatility, 4)*100)
print( str_vol )

fig, ax = plt.subplots() 
data['Log returns'].hist(ax=ax, bins=50, alpha=0.6, color='b')
ax.set_xlabel("Log return")
ax.set_ylabel("Freq of log return")
ax.set_title("AAPL volatility: " + str_vol + "%")
# plt.grid()
plt.show(block=False)

print( data.head() )
data['MA10'] = data['Close'].rolling(10).mean()
print( data.tail() )
data['EMA10'] = data['Close'].ewm(span=10, adjust=False).mean()
print( data.tail() )

fig, ax = plt.subplots()
data[['MA10', 'EMA10']].loc['2020-12-01':].plot(ax=ax)
data['Close'].loc['2020-12-01':].plot(ax=ax, alpha=0.25)
plt.grid()
plt.show(block=False)
plt.waitforbuttonpress()
plt.close('all')



