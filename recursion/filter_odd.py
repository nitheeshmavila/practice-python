''' This programe recursively filter a list of odd numbers from a given list'''

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]

def isodd(i):
    return i % 2 != 0

def cons(x, xs):
    return [x] + xs

def filterOdd(xs):
    ''' returns new list composed of odd numbers from xs'''
    if not xs:    
        return []
    elif isodd(head(xs)):
        return cons(head(xs), filterOdd(tail(xs)))
    else:
        return filterOdd(tail(xs))

print(filterOdd([1,2,3,4,5]))
        


