'''
Exercise 7.2.
------------
 Encapsulate this loop in a function called square_root that takes a as a parameter,
chooses a reasonable value of x , and returns an estimate of the square root of a .'''

def squareRoot(a):
    x = 2
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y 
    return y


