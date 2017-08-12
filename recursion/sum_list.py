''' This programe recursively compute the sum of all elements in a list'''


def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]

def sumList(xs):
    if null(xs):
        return 0
    else:
        return head(xs) + sumList(tail(xs))

print(sumList([12,3,2,3,10,100]))
