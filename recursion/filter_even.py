''' This programe recursively filter a list of even numbers from a given list'''

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]

def isEven(i):
    return i % 2 == 0

def cons(x, xs):
    return [x] + xs

def filterEven(xs):
    ''' returns new list composed of only even numbers from xs'''
    if not xs:    
        return []
    elif isEven(head(xs)):
        return cons(head(xs), filterEven(tail(xs)))
    else:
        return filterEven(tail(xs))

print(filterEven([1,2,3,4,5]))
        


