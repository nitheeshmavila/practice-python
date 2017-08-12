def fib(n):
    # this is noramal recursive implementation it is very slow
    if n == 0 or n == 1:
        value = n
    else:
        value = fib(n-1) + fib(n-2)
        return(value)


def fibImproved(n):
    # it is an improved version using "memorization"
    lookUpTable = {}
    try:
        if lookUpTable[n]:
            return(lookUpTable[n])
    except:
        if n == 0 or n ==1:
            value = n
        else:
            value = fibImproved(n-1) + fibImproved(n-2)
        lookUpTable[n] = value
        return value

def fibDynamic(n):
    # using dynamic programing . this is the fastest version of the three
    fibTable = {}
    fibTable[0] = 0
    fibTable[1] = 1
    for i in range(2, n+1):
        fibTable[i] = fibTable[i-1] + fibTable[i-2]
    return(fibTable[n])
