'''
Problem 7
--------
 Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?'''
def min(l):
    l.sort()
    return l[0]

def max(l):
    l.sort()
    return l[-1]




