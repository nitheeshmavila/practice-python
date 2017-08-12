'''
Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

$ python grep.py she.txt sure
The shells that she sells are seashells I'm sure.
I'm sure that the shells are seashore shells.'''

import sys

fp = open(sys.argv[1])
for line in fp:
    if line.find(sys.argv[2]) != -1:
        print(line)
    else:
        pass
