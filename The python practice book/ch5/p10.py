'''
Problem 10: Implement a function izip that works like itertools.izip 

for x, y in itertools.izip(["a", "b", "c"], [1, 2, 3]):
...     print x, y
...
a 1
b 2
c 3
'''

def izip(l1, l2):
    for ch in l1:
        for num in l2:
            if l1.index(ch) == l2.index(num):
                yield ch,num

f = izip(["a", "b", "c"], [1, 2, 3])
for a, b in f:
    print(a,b)
