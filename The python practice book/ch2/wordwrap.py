'''Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

$ python wordwrap.py she.txt 30
I'm sure that the shells are
seashore shells.
So if she sells seashells on
the seashore,
The shells that she sells are
seashells I'm sure.
She sells seashells on the
seashore;'''

import sys

def printLine(line):
    newline1 = ''
    newline2 = ''
    words = line.split(' ')
    for word in words:
        if len(newline1) <= 30:
            newline1 = newline1 + word + ' '
        else:
            newline2 = newline2 + word + ' '
    print(newline1)
    return newline2

def main():
    fp = open(sys.argv[1])
    for line in fp:
        if len(line) > int(sys.argv[2]):
            extraWords = printLine(line)
            while extraWords:
                extraWords = printLine(extraWords)

if __name__=='__main__':
    main()
