#solution to 3.5
def do_4times(f):
 do_twise(f)
 do_twise(f)

def do_twise(g):
 g()
 g()

def print_line_type1():
 print '+',' -'*4,

def print_line_type2():
 print '|',' '*8,

def printplus():
 print '+'

def printbar():
 print '|'

def printrow():
 do_twise(print_line_type1)
 printplus()
 print ' '
def printcolmn():
 do_twise(print_line_type2)                 
 printbar()
 print ' '

def print_2grid():
 printrow()
 do_4times(printcolmn)
 printrow()
 do_4times(printcolmn)
 printrow()
print_grid()
 
