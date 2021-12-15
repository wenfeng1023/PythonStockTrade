# 01 - Sum two lists
# 01 - Sum two lists
# Given two lists
# - [53, 43, 11, 91, 35, 67, 60, 59, 6, 31]
# - [52, 84, 87, 83, 4, 98, 46, 31, 97, 3]

# Create a list with the sum
# - [105, 127, 98, 174, 39, 165, 106, 90, 103, 34]

# First using Python lists then with Pandas

l1 = [53, 43, 11, 91, 35, 67, 60, 59, 6, 31]
l2 = [52, 84, 87, 83, 4, 98, 46, 31, 97, 3]

def pairwise_sum(l1, l2):
    if len(l1) != len(l2):
        # return None
        raise Exception("Lists not same size/length")
    l3 = [0]*len(l1)
    for i in range(len(l1)):
        l3[i] = l1[i] + l2[i]
    return l3

pairwise_sum(l1, l2)

# r = pairwise_sum([1, 2, 3, 4], [2, 3, 4])

# if r == None:
#     print("None result")
# else:
#     print("Okay")

### DataFrame

import pandas as pd

df = pd.DataFrame([l1, l2])

print( df )
print( df.sum() )
# print( l3 )
df2 = pd.DataFrame([[1, 2 ,3], [2, 3, 4, 4]])
print( df2 )
dft = df.transpose()
print( df )
print( dft )
dft['c'] = dft[0] + dft[1]
print( dft )
df3 = pd.DataFrame({'a': l1, 'b': l2})
print( df3 )
df3['c'] = df3['a'] + df3['b']
print( df3 )


