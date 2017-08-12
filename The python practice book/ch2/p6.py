'''
Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?

>>> reverse([1, 2, 3, 4])
[4, 3, 2, 1]
>>> reverse(reverse([1, 2, 3, 4]))
[1, 2, 3, 4]'''

def reverse(l):
    return [ l[i]  for i in range(-1, -len(l) -1, -1)]

print(reverse([1, 2, 3, 4]))
