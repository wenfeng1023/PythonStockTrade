import pandas_datareader as pdr
import datetime as dt

start = dt.datetime(2010, 1, 1)
aapl = pdr.get_data_yahoo("AAPL", start)

aapl.head()
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2020, 1, 1)

aapl = pdr.get_data_yahoo("AAPL", start, end)

print( aapl )
tickers = ['AAPL', 'MSFT', 'NFLX', 'AMZN']
start = dt.datetime(2010, 1, 1)
data = pdr.get_data_yahoo(tickers, start)

print( data.head() )

data = data['Adj Close']
print( data.head() )

norm = data/data.iloc[0]
print( norm.head() )

portfolio = [.25, .25, .25, .25]
weights = (norm*portfolio)
print( weights.head() )
weights['Total'] = (norm*portfolio).sum(axis=1)
print( weights.head() )

print( (weights*100000).head() )
print( (weights*100000).tail() )
print( (weights['Total']*100000).iloc[-1] )


