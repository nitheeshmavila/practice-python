'''
Exercise 6.3.
-------------
 Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False
otherwise'''

def isBetween(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

