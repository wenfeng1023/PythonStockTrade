# # Modify DataFrames and Useful functions
# - Calculate with columns
# - Create new columns
# - Drop columns
# - Min, Max, Argmin, and Argmax
# - Mean

import pandas as pd

remote_file = "https://raw.githubusercontent.com/LearnPythonWithRune/FinancialDataAnalysisWithPython/main/AAPL.csv"
data = pd.read_csv(remote_file, index_col=0, parse_dates=True)

print( data.head() )
data['Daily chg'] = data['Close'] - data['Open']
print( data.head() )
data['Normalized'] = data['Close'] / data['Close'].iloc[0]
print( data.head() )
print( data.tail() )
print( data['Close'].min() )
print( data.min() )
print( data['Close'].argmin() )
print( data.iloc[35:44] )
print( data['Normalized'].min() )
print( data['Normalized'].argmin() )
print( data['Close'].max() )
print( data['Close'].argmax() )
print( data.iloc[251:] )
print( data['Close'].mean() )
print( data.head() )
print( data.drop(labels=['High', 'Low', 'Adj Close', 'Volume'], axis=1, inplace=True) )
print( data.head() )


