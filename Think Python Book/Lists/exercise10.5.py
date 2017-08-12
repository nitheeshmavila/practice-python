'''
Exercise 10-5.
---------------
Write a function called chop that takes a list, modifies it by removing the first and last
elements, and returns None .'''

def chop(l):
    l.pop(0)
    l.pop(-1)
    return None

l=[12,3,3,4,5,6]
print(l)
chop(l)
print(l)
