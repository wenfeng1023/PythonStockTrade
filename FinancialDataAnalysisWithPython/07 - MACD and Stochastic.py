# 07 - MACD and Stochastic
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib notebook

remote_file = "https://raw.githubusercontent.com/LearnPythonWithRune/FinancialDataAnalysisWithPython/main/AAPL.csv"
data = pd.read_csv(remote_file, index_col=0, parse_dates=True)

print( data.head() )

# 	Open	High	Low	Close	Adj Close	Volume
# Date						
# 2020-01-27	77.514999	77.942497	76.220001	77.237503	76.576187	161940000
# 2020-01-28	78.150002	79.599998	78.047501	79.422501	78.742477	162234000
# 2020-01-29	81.112503	81.962502	80.345001	81.084999	80.390747	216229200
# 2020-01-30	80.135002	81.022499	79.687500	80.967499	80.274246	126743200
# 2020-01-31	80.232498	80.669998	77.072502	77.377502	76.714989	199588400

# ### MACD
# - MACD is a lagging indicator when trading on the crossovers
# - https://www.investopedia.com/terms/m/macd.asp

# **Calculation** (12-26-9 MACD (default))
# - MACD=12-Period EMA − 26-Period EMA
# - Singal line 9-Perioed EMA of MACD

# ### Stochastic oscillator
# - Lagging indicator
# - https://www.investopedia.com/terms/s/stochasticoscillator.asp

# **Calculations**
# - 14-high: Maximum of last 14 trading days
# - 14-low: Minimum of last 14 trading days
# - %K: (Last close - 14-low)*100 / (14-high - 14-low)
# - %D: Simple Moving Average of %K

high14 = data['High'].rolling(14).max()
low14 = data['Low'].rolling(14).min()
data['%K'] = (data['Close'] - low14)*100/(high14 - low14)
data['%D'] = data['%K'].rolling(3).mean()

print( data.tail() )


# Open	High	Low	Close	Adj Close	Volume	MACD	Signal line	%K	%D
# Date										
# 2021-01-20	128.660004	132.490005	128.550003	132.029999	132.029999	104319500	1.168345	1.733879	58.792896	25.533726
# 2021-01-21	133.800003	139.669998	133.589996	136.869995	136.869995	120529500	1.653950	1.717893	78.931506	49.802857
# 2021-01-22	136.279999	139.850006	135.020004	139.070007	139.070007	114459400	2.191061	1.812527	94.209365	77.311256
# 2021-01-25	143.070007	145.089996	136.539993	142.919998	142.919998	157282400	2.894026	2.028827	88.401934	87.180935
# 2021-01-26	143.600006	144.300003	141.369995	142.080002	142.080002	50388565	3.344794	2.292020	83.912378	88.841226

fig, ax = plt.subplots()
data[['%K', '%D']].loc['2020-11-01':].plot(ax=ax)
ax.axhline(80, c='r', alpha=0.3)
ax.axhline(20, c='r', alpha=0.3)
data['Close'].loc['2020-11-01':].plot(ax=ax, alpha=0.3, secondary_y=True)

plt.grid()
plt.show(block=True)


