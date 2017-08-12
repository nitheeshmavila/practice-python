'''
Problem 11: Write a function dups to find all duplicates in the list.

>>> dups([1, 2, 1, 3, 2, 5])
[1, 2]'''

import collections

def dups(l):
    dup = []
    count = collections.Counter(l)
    for key in count.keys():
        if count[key] >= 2:
            dup.append(key)
    return dup 
    

print(dups([1, 2, 1, 3, 2, 5]))
