'''
Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

>>> def even(x): return x %2 == 0
...
>>> filter(even, range(10))
[0, 2, 4, 6, 8]'''

even = lambda x : x % 2 == 0

def filter(f ,a):
    return [ i for i in a if f(i)]

print(filter(even, range(10)) )
