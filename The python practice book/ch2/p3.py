'''
Problem 3
 What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.

>>> sum(["hello", "world"])
"helloworld"
>>> sum(["aa", "bb", "cc"])
"aabbcc" '''

def sum(l):
    string = ''
    for s in l:
        string += s
    return string

print(sum(["hello", "world"]))
