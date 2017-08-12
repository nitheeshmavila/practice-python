''' This programe recursively compute the sum of even numbers  in a list'''


def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]

def isEven(i):
    return i % 2 == 0

def sumEven(xs):
    if null(xs):
        return 0
    elif isEven(head(xs)):
        return head(xs) + sumEven(tail(xs))
    else:
        return sumEven(tail(xs))
        

print(sumEven([12,3,2,3,10,100]))
