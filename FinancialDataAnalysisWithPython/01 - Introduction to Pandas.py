# # Introduction to DataFrames
# - Read data from CSV (downloadable from Yahoo! Finance)
# - Understand data types
# - Set index
# - Parse dates 
# - Use index with **loc**
# - Use indexing with **iloc**

import pandas as pd

remote_file = "https://raw.githubusercontent.com/LearnPythonWithRune/FinancialDataAnalysisWithPython/main/AAPL.csv"
data = pd.read_csv(remote_file, index_col=0, parse_dates=True)

print( data.head() )

print( data.dtypes )
print( data.index )
print( data.loc['2020-01-27'] )
print( data.loc[:'2020-07-01'] )
print( data.iloc[0] )
print( data.loc['2020-01-27'] )
print( data.iloc[-1] )
print( data.tail() )


