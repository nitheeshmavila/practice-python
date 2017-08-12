'''
Binary search
------------
Iterative implimentation'''

def binarySearch(alist, item):
    # return index if found and None otherwise
    first = 0
    last = len(alist) - 1
    found = None
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
