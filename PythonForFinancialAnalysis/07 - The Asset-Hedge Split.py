# The Asset/Hedge Split

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
eval_set1 =[]

def evaluate_split(data, split):
    a = np.sum(split)
    portfolio = [a, 1. - a]
         
    eval_set = ((data/data.iloc[0])*portfolio).sum(axis=1)
    
    cagr = (eval_set.iloc[-1]/eval_set.iloc[0])**(1/10) - 1

    rolling_max = eval_set.cummax()
    daily_drawdown = eval_set/rolling_max - 1
    drawdown = daily_drawdown.cummin().iloc[-1]

    log_returns = np.log(eval_set/eval_set.shift())
    volatility = log_returns.std()*(252**.5)

    return cagr, drawdown, volatility

# print( evaluate_split(data, .5) )

x = np.arange(0, 1.01, .05)

df = pd.DataFrame(x)
print(evaluate_split(data, x))

res = df.apply(lambda x: evaluate_split(data, x), axis=1)

df['CAGR'] = res.str[0]
df['Drawdown'] = res.str[1]
df['Volatility'] = res.str[2]

df.set_index(0, inplace=True)

print( df )

fig, ax = plt.subplots()
df.plot(ax=ax)
plt.grid()
plt.show(block=True)
plt.waitforbuttonpress()
plt.close('all')




