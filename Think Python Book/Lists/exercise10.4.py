'''
Exercise 10-4.
---------------
Write a function called middle that takes a list and returns a new list that contains all
but the first and last elements. So middle([1,2,3,4]) should return [2,3] .'''

def middle(l):
    ll = l[:]
    ll.pop(0)
    ll.pop(-1)
    return ll

l = [1,2,3,4,5]
print(l)
print(middle(l))
print(l)

