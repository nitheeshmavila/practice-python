'''
Exercise 7.1.
-------------
Rewrite the function print_n from Section 5.8 using iteration instead of recursion.


def print_n(s, n):
    # a function that prints a string n times.
    if n <= 0:
        return
    print s
    print_n(s, n-1)

'''


def printN(s, n):
    # prints a string n times (iterative solution)
    N = n
    while n > 0:
        print(s)
        n -= 1
    return 'printed %s %d times'%(s, N)    


