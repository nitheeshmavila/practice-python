'''
Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.

>>> cumulative_product([1, 2, 3, 4])
[1, 2, 6, 24]
>>> cumulative_product([4, 3, 2, 1])
[4, 12, 24, 24]'''

def cumilativeProduct(l):
    pList = []
    p = 1
    for i in l:
        p *= i
        pList.append(p)
    return pList

print(cumilativeProduct([1, 2, 3, 4]))
