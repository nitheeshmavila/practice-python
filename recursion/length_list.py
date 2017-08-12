'''Finding the length of a list by recursion'''

def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]

def mylen(xs):
    if null(xs):
        return 0
    else:
        return 1 + mylen(tail(xs))

print(mylen([12,2132,23,43,21,34]))
