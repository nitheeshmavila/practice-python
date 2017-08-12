'''
Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

>>> a = array(2, 3)
>>> a
[[None, None, None], [None, None, None]]
>>> a[0][0] = 5
[[5, None, None], [None, None, None]]'''

def array(m, n):
    return [[None for i in range(n)] for j in range(m)]

a = array(2,3)
print(a)
a[0][1] = 2
print(a)
