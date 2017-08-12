'''
Problem 10: Write a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.

>>> fib = profile(fib)
>>> fib(20)
time taken: 0.1 sec
10946'''

import time

def profile(f):
    def new_f(x):
        t1 = time.time()
        print(f(x))
        return time.time() - t1
        
    return new_f

@profile
def fib(n):
    fibTable = {}
    fibTable[0] = 0
    fibTable[1] = 1
    for i in range(2, n+1):
        fibTable[i] = fibTable[i-1] + fibTable[i-2]
    return(fibTable[n])

print(fib(21))        
    
