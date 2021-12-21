# 04 - Sort Numbers
# Natasha needs to sort the following list [7, 8, 2, 9, 5, 1, 8, 5, 3]

# She only knows how to sort 6 numbers.

# She shorts all 9 numbers as follows:
# - Sorts the first 6:  1, 2, 5, 7, 8, 9, 8, 5, 3
# - Sorts the last 6: 1, 2, 5, 3, 5, 7, 8, 8, 9
# - Sorts the first 6: 1, 2, 3, 5, 5, 7, 8, 8, 9

l = [7, 8, 2, 9, 5, 1, 8, 5, 3]
print( l[:6] )

l[:6] = sorted(l[:6])
print( l )

l[-6:] = sorted(l[-6:])
print( l )

l[:6] = sorted(l[:6])
print( l )

l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
l[:6] = sorted(l[:6])
l[-6:] = sorted(l[-6:])
l[:6] = sorted(l[:6])
print( l )



