# Visualization
### Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib notebook

csv_file = "https://raw.githubusercontent.com/LearnPythonWithRune/PythonForFinancialAnalysis/main/AAPL.csv"
aapl = pd.read_csv(csv_file, index_col="Date", parse_dates=True)

print( aapl.head() )
fig, ax = plt.subplots()
aapl['Close'].plot(ax=ax)
plt.grid()
plt.show(block=False)

aapl['MA20'] = aapl['Close'].rolling(20).mean()
aapl['MA200'] = aapl['Close'].rolling(200).mean()

fig, ax = plt.subplots()
aapl[['MA20', 'MA200', 'Close']].plot(ax=ax)
plt.grid()

fig, ax = plt.subplots()
aapl[['MA20', 'MA200', 'Close']].loc['2020':].plot(ax=ax)
plt.grid()

fig, ax = plt.subplots(2, 2)
plt.grid()

aapl['Open'].loc['2020':].plot(ax=ax[0, 0], c='r')
plt.grid()

aapl['Close'].loc['2020':].plot(ax=ax[0, 1], c='g')
aapl['High'].loc['2020':].plot(ax=ax[1, 0], c='c')
aapl['Low'].loc['2020':].plot(ax=ax[1, 1], c='y')

ax[0, 0].legend()
ax[0, 1].legend()
ax[1, 0].legend()
ax[1, 1].legend()
plt.tight_layout()
plt.show(block=False)
plt.grid()

import pandas_datareader as pdr
import datetime as dt

tickers = ['AAPL', 'MSFT']

start = dt.datetime(2020, 1, 1)
end   = dt.datetime(2021, 1, 1)
data  = pdr.get_data_yahoo(tickers, start, end)


data = data['Adj Close']
print( data.head() )

norm = data/data.iloc[0]
print( norm.head() )


fig, ax = plt.subplots()
norm.plot(ax=ax)
plt.grid()

aapl_rtn = norm['AAPL'].iloc[-1] - 1
msft_rtn = norm['MSFT'].iloc[-1] - 1

aapl_rtn, msft_rtn

fig, ax = plt.subplots()
ax.bar(['AAPL', 'MSFT'], [aapl_rtn, msft_rtn], color=['b', 'c'])
ax.set_title("Return")
plt.show(block=False)
plt.grid()

plt.waitforbuttonpress()
plt.close('all')









