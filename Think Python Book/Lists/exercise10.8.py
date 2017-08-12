'''
Exercise 10-8.
---------------
The (so-called) Birthday Paradox:

1. Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
'''

def hasDuplicates(l):
    reatedElements = 0
    count = {}
    for i in l:
        count[i] = count.get(i, 0) + 1
    for key in count.keys():
        if count[key] > 1:
            return True
    return False

#print(hasDuplicates([12,23,3,0,2,3,28]))

