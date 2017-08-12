'''
Exercise 6.2.
-------------
 Use incremental development to write a function called hypotenuse that returns the
length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record
each stage of the development process as you go.'''
import math

def hypotenuse(l1, l2):
    # return the lenght of the hypotenuse of a right triangle given the lengths of the two legs as arguments.
    r = l1 ** 2 + l2 ** 2
    return math.sqrt(r)


