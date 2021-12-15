# 04 - Visualize DataFrames - Matplotlib
# # Visualize
# - Learn to use Matplotlib
# - Subplots
# - Multiple plots
# - Bar plots

import pandas as pd

remote_file = "https://raw.githubusercontent.com/LearnPythonWithRune/FinancialDataAnalysisWithPython/main/AAPL.csv"
data = pd.read_csv(remote_file, index_col=0, parse_dates=True)

print( data.head() )
print( data.plot() )

import matplotlib.pyplot as plt
# %matplotlib notebook

data.plot()
data['Close'].plot()
plt.grid()
plt.show(block=False)

fig, ax = plt.subplots()
data['Close'].plot(ax=ax)
ax.set_ylabel("Price")
ax.set_title("AAPL")
plt.grid()
plt.show(block=False)



fig, ax = plt.subplots(2, 2)
data['Open'].plot(ax=ax[0, 0], title="Open")
data['High'].plot(ax=ax[0, 1], title="High")
data['Low'].plot(ax=ax[1, 0], title="Low")
data['Close'].plot(ax=ax[1, 1], title="Close")
plt.tight_layout()
plt.grid()
plt.show(block=False)


fig, ax = plt.subplots()
data['Volume'].loc['2020-07-01':'2020-08-15'].plot.barh(ax=ax)
plt.grid()
plt.show(block=True)
plt.waitforbuttonpress()
plt.close('all')





