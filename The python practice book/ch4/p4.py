'''
Problem 4: What will be the output of the following program?
'''
def f():
    try:
        print "a"
        return
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"

f()

'''
output
-----
a
d
'''
