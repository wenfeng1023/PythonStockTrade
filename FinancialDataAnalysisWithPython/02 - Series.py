# # Series
# - Use **type** to get data type
# - Each column is a Series
# - Series show data type (dtype)
# - Calculate with Series
#     - Daily change
#     - Daily percentage change
#     - Normalize data
# - Similar to Excel
# - Indexing with Series

import pandas as pd

remote_file = "https://raw.githubusercontent.com/LearnPythonWithRune/FinancialDataAnalysisWithPython/main/AAPL.csv"
data = pd.read_csv(remote_file, index_col=0, parse_dates=True)

print( data.head() )
print( data.dtypes )
print( type(data) )
print( data['Close'] )
print( type(data['Close']) )
daily_chg = data['Open'] - data['Close']
print( data.head() )
print( daily_chg )
print( type(daily_chg) )
daily_pct_chg = (data['Close'] - data['Open'])/data['Open']*100
print( daily_pct_chg )
print( data['Close'].iloc[0] )
print( data['Close'].iloc[-1] )
norm = data['Close']/data['Close'].iloc[0]
print( norm )
print( data['Close'].iloc[0]*norm.iloc[-1] )
print( data['Close'].iloc[-1] )



