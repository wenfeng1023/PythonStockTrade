# 03 - Fibonacci
# Given the Fibonacci number defined as

# - $F_0 = 0$
# - $F_1 = 1$
# - $F_n = F_{n-1} + F_{n-2}$

# The sequence begins as follows

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# Create a list of first $n$ Fibonacci numbers.

# - https://en.wikipedia.org/wiki/Fibonacci_number

f0 = 0
f1 = 1

f2 = f1 + f0
print( f2 )

f3 = f2 + f1
print( f3 )

f4 = f3 + f2
print( f4 )

def fib(n):
    fn1 = 1
    fn2 = 0
    fn = 0
    for _ in range(n):
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn
    return fn

def fib2(n):
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

for i in range(15):
    print(i, fib(i), fib2(i))

# %timeit fib(20)
# %timeit fib2(20)






