#solution to 3.4
a='spam'
def do_four(g,a):
 do_twice(print_twise,a)
 do_twice(print_twise,a)
def do_twice(f,a):
 f(a)
 f(a)
def print_twise(a):
 print a
do_four(do_twice,a)



