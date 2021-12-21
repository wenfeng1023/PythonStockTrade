# # Pandas-datareader
# - https://pandas-datareader.readthedocs.io/en/latest/

import pandas_datareader as pdr
import datetime as dt

ticker = "AAPL"
start = dt.datetime(2019, 1, 1)
end = dt.datetime(2020, 12, 31)

data = pdr.get_data_yahoo(ticker, start, end)

print( data.head() )
print( data.index )
print( data.dtypes )
print( data.tail() )
data2 = pdr.get_data_stooq(ticker, start)
print( data2.head() )
print( data2.tail() )
nasdaq_sym = pdr.get_nasdaq_symbols()
print( nasdaq_sym.loc['AAPL'] )
print( len(nasdaq_sym) )











