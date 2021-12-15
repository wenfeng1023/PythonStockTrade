import numpy as np

import pandas_datareader as pdr

import datetime as dt

import pandas as pd

start = dt.datetime(2020, 1, 1)

data = pdr.get_data_yahoo("AAPL", start)


print( data.head() )

print( data.index )

print( data.dtypes )

print( type(data) )


data.to_numpy()

arr = data.to_numpy()

print( arr.shape )

print( len(data) )

print( arr[0] )

print( data.head(1) )

print( arr.dtype )

small = arr[:10, 0].copy()

print( small )

print( data.head() )

print( np.max(small) )

print( small.max() )

print( small.argmax() )


print( small )

print( small[small.argmax()] )

print( np.log(small) )

print( np.log(data) )

print( data/data.shift() )

print( data.head() )

print( 75.144997/75.150002 )


print( np.sum(np.log(data/data.shift())) )

print( np.log(data/data.iloc[0]).tail(1) )

print( small.shape )

print( small )

print( small.reshape(2, 5) )

print( small.reshape(10, 1) )

print( small.reshape(-1, 1) )


# Portfolios

tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']

start = dt.datetime(2020, 1, 1)

data = pdr.get_data_yahoo(tickers, start)


print( data.head() )

data = data['Adj Close']


print( data.head() )

portfolios = [.25, .15, .40, .20]

print( np.sum(portfolios) )

print( (data/data.iloc[0])*portfolios*100000 )


weight = np.random.random(4)

weight /= weight.sum()

print( weight )

print( weight.sum() )

print( np.sum((data/data.iloc[0])*portfolios*100000, axis=1) )

print( np.sum((data/data.iloc[0])*weight*100000, axis=1) )