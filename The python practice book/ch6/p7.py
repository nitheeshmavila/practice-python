'''
Problem 7: Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.

Hint: Use os.listdir and os.path.isdir funtions.

$ python dirtree.py foo/
foo/
|-- a.txt
|-- b.txt
|-- bar/
|   |-- p.txt
|   `-- q.txt
`-- c.txt
'''
import os
import sys

s = '|    '
count = 0

def printTree(dirt,count):
    filenames = os.listdir(dirt)
    for filename in filenames:
        if not os.path.isdir(os.path.abspath(dirt+'/'+filename)):
            if filename == filenames[-1]:
                print s*count+'\--',filename
            else:
                print s*count+'|--',filename
        else:
            print s*count+'|--',filename
            dirt = dirt+'/'+filename
            printTree(dirt, count + 1)
def main():
    d = sys.argv[1]
    print d
    printTree(d, count)

if __name__ == '__main__':
    main()

