from matplotlib import colors
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pylab as plt
import matplotlib.patches as mpatches

data = pdr.get_data_yahoo("TQQQ")
print(data.head())

Roll_Max = data['Adj Close'].cummax()
Daily_Drawdown = data['Adj Close']/Roll_Max - 1.0
Max_Daily_Drawdown = Daily_Drawdown.cummin()
Maximum_Drawdown = Max_Daily_Drawdown.min()*100


# fig, ax = plt.subplots(2,1)

# ax[0].plot(data.index,data["Adj Close"])
# ax[0].set_ylabel("Adj Close")
# ax[1].plot(Daily_Drawdown,'r')
# ax[1].set_ylabel("Daily_Drawdown")
# ax[1].grid(linestyle=":")
# red_patch = mpatches.Patch(color='red', label="MDD:"+ str(Maximum_Drawdown))
# ax[1].legend(handles=[red_patch])
# plt.show()


fig = plt.figure()
df = abs(Max_Daily_Drawdown)
ax1 = data['Adj Close'].plot()
data['Adj Close'].plot(ax=ax1,color='g')
df.plot(ax=ax1,color='b')
# df.plot(ax=ax)
plt.grid()
plt.yscale('log')
plt.show()
