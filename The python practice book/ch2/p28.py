'''
Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

>>> enumerate(["a", "b", "c"])
[(0, "a"), (1, "b"), (2, "c")]
>>> for index, value in enumerate(["a", "b", "c"]):
...     print index, value
0 a
1 b
2 c'''


def enumerate(l):
    return [(i, l[i])
            for i in range(len(l))]
for index, value in enumerate(["a", "b", "c"]):     
    print(index, value)    
