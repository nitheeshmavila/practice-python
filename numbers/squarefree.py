'''A positive integer is said to be square free, if it is not divisible by any square integer strictly greater than 1. For instance, 5, 10 and 21 are square free, while 4 and 48 are not, since 4 is divisible by 22 and 48 is divisible by 42.

Write a Python function squarefree(n) that takes a positive integer argument and returns True if the integer is square free, and False otherwise.'''

def squareIntList(n):
    i = 2
    l = []
    while(i*i < n):
        l.append(i*i)
        i += 1
    return l
         
def squareFree(n):
    sqint = squareIntList(n)
    for i in sqint:
        if n%i == 0:
            return False
    return True


print(squareFree(1001))
                

