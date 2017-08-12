'''
Problem 4: Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.
$ python dirtree.py foo
foo
|-- a.txt
|-- b.txt
|-- code
|   |-- a.py
|   |-- b.py
|   |-- docs
|   |   |-- a.txt
|   |   \-- b.txt
|   \-- x.py
\-- z.txt
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



