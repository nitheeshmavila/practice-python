'''Problem 9: What will be the output of the following program?
'''
x = 1
def f():
    x = 2
    return x
print(x)
print(f())
print(x)

'''
output
------
1
2
1
'''
