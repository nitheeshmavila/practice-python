'''
Problem 4: Implement a function product, to compute product of a list of numbers.

>>> product([1, 2, 3])
6
'''

def product(l):
    pr = 1
    for i in l:
        pr *= i
    return pr

#print(product([1, 2, 3]))
