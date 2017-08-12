'''
Exercise 11.1
--------------
Suppose you are given a string and you want to count how many times each letter appears.'''

def histogram(s):
    c = {}
    for i in s:
        if i not in  c: 
            c[i] = 1
        else:
            c[i] += 1
    return(c) 
print(histogram('nitheesh'))


