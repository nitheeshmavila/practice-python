'''
Problem 4: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''
def treemap(fn, l, result = None):
    if result == None:
        result = []
    for i in l:
        if  isinstance(i, list):
            result.append(treemap(fn, i))
        else:
            result.append(fn(i))
    return result

print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))
