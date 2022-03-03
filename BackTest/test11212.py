import pandas_datareader as prd
name ='TQQQ'
data = prd.get_data_yahoo(name)

print(data.head())