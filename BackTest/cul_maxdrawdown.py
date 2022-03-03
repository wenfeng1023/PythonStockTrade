import  ffn 
data = ffn.get('TQQQ', start='2020-01-01', end='2022-02-28')
MDD = ffn.calc_max_drawdown(data)
print (MDD)
