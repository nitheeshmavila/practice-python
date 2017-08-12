'''
Exercise 12.1
---------------
Write a function called sumall that takes any number of arguments and returns their
sum.'''

def sumall(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum

print(sumall(13,17,10))
