'''
Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.

>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
[[1, 2, 3, 4], [5, 6, 7, 8], [9]]
'''

def group(l, size):
    n = 0
    output = []
    noofSublist = len(l) // size
    for i in range(noofSublist):
        output.append(l[n:n+size])
        n += size
    return output

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))      
