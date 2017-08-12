'''
Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.

>>> tree_reverse([[1, 2], [3, [4, 5]], 6])
[6, [[5, 4], 3], [2, 1]]'''

def treeReverse(lst, result=None):
    if result == None:
        result = []
    for i in lst:
        if isinstance(i,list):
            result.insert(0,treeReverse(i))
        else:
            result.insert(0,i)
    return result

print(treeReverse([[1, 2], [3, [4, 5]], 6]))

