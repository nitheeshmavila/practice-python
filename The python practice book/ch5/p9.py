'''
Problem 9: The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.

>>> list(enumerate(["a", "b", "c"])
[(0, "a"), (1, "b"), (2, "c")]
>>> for i, c in enumerate(["a", "b", "c"]):
...     print i, c
...
0 a
1 b
2 c

Write a function my_enumerate that works like enumerate.

'''

def my_enumerate(l):
    i = 0
    for ch in l:
        yield (i,ch)
        i += 1

f = my_enumerate(["a", "b", "c"])
for i ,c in f:
    print(i,c)

