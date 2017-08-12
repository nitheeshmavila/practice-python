'''
Problem 10
----------
 What will be the output of the following program?
'''
x = 1
def f():
    y = x
    x = 2
    return x + y


print(x)
print(f())
print(x)

'''
output
------
UnboundLocalError: local variable 'x' referenced before assignment
'''
