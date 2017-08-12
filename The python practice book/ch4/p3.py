'''
Problem 3: What will be the output of the following program?
'''
try:
    print "a"
    raise Exception("doom")
except:
    print "b"
else:
    print "c"
finally:
    print "d"
'''

output
-----
a
b
d
'''
