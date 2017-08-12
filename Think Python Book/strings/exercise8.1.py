'''Exercise 8.1.
-----------------
 Write a function that takes a string as an argument and displays the letters backward,
one per line.'''

def backward(s):
    for i in range(len(s), 0, -1):
        print(s[i-1])


