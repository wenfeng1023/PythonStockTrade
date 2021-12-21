# 02 - Positive sum
# Given a list
# - [6, -10, 7, 7, 5, -8, -7, 0, -7, -3, 5, -10, -7, 5, 5]

# Sum all positive integers

# Approach
# - Firs simple with Python built in list
# - Then with Pandas

l = [6, -10, 7, 7, 5, -8, -7, 0, -7, -3, 5, -10, -7, 5, 5]

print( l )
print( len(l) )
print( sum(l) )

def positive_sum(l):
    p_sum = 0
    for i in l:
        if i > 0:
            p_sum = p_sum + i
    return p_sum

print( positive_sum(l) )

print( sum([n for n in l if n > 0]) )

### Series

import pandas as pd

s = pd.Series(l)
print( s )
print( l )
print( s > 0 )
print( s[s > 0] )
print( l )
print( s[s > 0].sum() )

# %timeit positive_sum(l)
# %timeit s[s > 0].sum()








