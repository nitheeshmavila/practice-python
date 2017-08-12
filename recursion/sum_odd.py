''' This programe recursively compute the sum of odd numbers  in a list'''


def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]

def isOdd(i):
    return i % 2 != 0

def sumOdd(xs):
    if null(xs):
        return 0
    elif isOdd(head(xs)):
        return head(xs) + sumOdd(tail(xs))
    else:
        return sumOdd(tail(xs))
        

print(sumOdd([12,3,2,3,10,100]))
