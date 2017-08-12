'''
Exercise 10-9.
--------------
Write a function called remove_duplicates that takes a list and returns a new list with
only the unique elements from the original. Hint: they don’t have to be in the same order'''

def removeDuplicates(l):
    return list(set(l))

l=[23,23,43,45,33,55,2,3,44,44,44]
print(removeDuplicates(l))
print(l)
