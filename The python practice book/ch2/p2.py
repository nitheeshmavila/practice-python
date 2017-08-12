'''
Problem 2
---------
 Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.'''

def sum(l):
    count = 0
    for i in l:
        count += i
    return count

print(sum(['mn','niya']))
