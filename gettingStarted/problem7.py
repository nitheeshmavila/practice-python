'''
Problem 7: How many multiplications are performed when each of the following lines(line 1 and line 2) of code is executed?
'''
noofCalls = 0
def square(n):
    print(n)
    global noofCalls
    noofCalls += 1
    return n*n

def printCalls():
    print('no of multiplications performed:',noofCalls)


print(square(5)) # line1
printCalls()
print(square(2*5)) #line2
printCalls()




'''
output
-----
no of multiplications performed:1
'''


