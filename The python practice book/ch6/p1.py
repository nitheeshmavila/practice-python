'''
Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.'''

def product(m, n):
    if m == 0 or n == 0:
        return 0
    else:
        return m + product(m, n - 1)


    
