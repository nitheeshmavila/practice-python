'''
Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?'''

import p4

def factorial(n):
    l = list(range(1, n+1))
    return p4.product(l)


print(factorial(10))
