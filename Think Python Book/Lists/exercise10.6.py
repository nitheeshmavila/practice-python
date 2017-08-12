'''
Exercise 10-6.
--------------
Write a function called is_sorted that takes a list as a parameter and returns True if
the list is sorted in ascending order and False otherwise. You can assume (as a precon
dition) that the elements of the list can be compared with the relational operators < , > ,
etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a'])
should return False .
'''

def isSorted(l):
    ll = l[:]
    ll.sort()
    if ll == l:
        return True
    else:
        return False


print(isSorted([1,2,2]))
print(isSorted(['b','a']))
